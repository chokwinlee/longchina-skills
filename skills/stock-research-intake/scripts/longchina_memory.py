#!/usr/bin/env python3
"""Local memory helper for the stock-research-intake skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ENTRY_DELIMITER = "\n§\n"
USER_LIMIT = 1500
MEMORY_LIMIT = 2500
FACTS_MAX_ENTRIES = 500
FACTS_MAX_BYTES = 100_000
FACTS_MAX_ENTRY_CHARS = 2_000
INVISIBLE_CHARS = {
    "\u200b",
    "\u200c",
    "\u200d",
    "\u2060",
    "\ufeff",
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",
}
THREAT_PATTERNS = [
    (re.compile(r"ignore\s+(previous|all|above|prior)\s+instructions", re.I), "prompt_injection"),
    (re.compile(r"disregard\s+(your|all|any)\s+(instructions|rules|guidelines)", re.I), "disregard_rules"),
    (re.compile(r"you\s+are\s+now\s+", re.I), "role_hijack"),
    (re.compile(r"system\s+prompt\s+override", re.I), "system_prompt_override"),
    (re.compile(r"curl\s+[^\n]*\$?\{?\w*(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|API)", re.I), "exfil_curl"),
    (re.compile(r"wget\s+[^\n]*\$?\{?\w*(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|API)", re.I), "exfil_wget"),
    (re.compile(r"cat\s+[^\n]*(\.env|credentials|\.netrc|\.pgpass|\.npmrc|\.pypirc)", re.I), "read_secrets"),
]


class FactsStorageError(Exception):
    """Raised when facts storage cannot be read safely."""


class MemoryStorageError(Exception):
    """Raised when text memory storage cannot be read safely."""


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        response(False, error=f"Argument error: {message}")
        raise SystemExit(2)


def memory_dir() -> Path:
    override = os.environ.get("LONGCHINA_MEMORY_DIR")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".longchina" / "memories"


def path_for(target: str) -> Path:
    if target == "user":
        return memory_dir() / "USER.md"
    if target == "memory":
        return memory_dir() / "MEMORY.md"
    if target == "facts":
        return memory_dir() / "facts.jsonl"
    raise ValueError(f"unknown target: {target}")


def scan_content(content: str) -> str | None:
    for char in INVISIBLE_CHARS:
        if char in content:
            return f"Blocked: content contains invisible unicode character U+{ord(char):04X}."
    for pattern, label in THREAT_PATTERNS:
        if pattern.search(content):
            return f"Blocked: content matches threat pattern '{label}'."
    return None


def validate_entries(path: Path, entries: list[str]) -> None:
    for index, entry in enumerate(entries, start=1):
        scan_error = scan_content(entry)
        if scan_error:
            raise MemoryStorageError(f"{path.name} entry {index} is unsafe. {scan_error}")


def read_entries(target: str, validate: bool = True) -> list[str]:
    path = path_for(target)
    if not path.exists():
        return []
    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise MemoryStorageError(f"{path.name} is not valid UTF-8: {error}") from error
    if not raw.strip():
        return []
    entries = [entry.strip() for entry in raw.split(ENTRY_DELIMITER) if entry.strip()]
    if validate:
        validate_entries(path, entries)
    return entries


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), prefix=".mem_", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def write_entries(target: str, entries: list[str]) -> None:
    atomic_write(path_for(target), ENTRY_DELIMITER.join(entries))


def target_limit(target: str) -> int:
    return USER_LIMIT if target == "user" else MEMORY_LIMIT


def response(success: bool, **payload: Any) -> None:
    print(json.dumps({"success": success, **payload}, ensure_ascii=False))


def fact_identity(fact: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(fact.get("type", "")).strip(),
        str(fact.get("canonical", "")).strip(),
        str(fact.get("raw", "")).strip(),
        str(fact.get("source", "")).strip(),
    )


def scan_fact_strings(value: Any, path: str = "fact") -> str | None:
    if isinstance(value, str):
        scan_error = scan_content(value)
        if scan_error:
            return f"{scan_error} Field: {path}."
        return None
    if isinstance(value, dict):
        for key, nested_value in value.items():
            scan_error = scan_fact_strings(nested_value, f"{path}.{key}")
            if scan_error:
                return scan_error
    elif isinstance(value, list):
        for index, nested_value in enumerate(value):
            scan_error = scan_fact_strings(nested_value, f"{path}[{index}]")
            if scan_error:
                return scan_error
    return None


def add_entry(target: str, content: str) -> None:
    content = content.strip()
    if not content:
        response(False, error="Content cannot be empty.")
        return
    scan_error = scan_content(content)
    if scan_error:
        response(False, error=scan_error)
        return
    entries = read_entries(target)
    if content in entries:
        response(True, target=target, entries=entries, entry_count=len(entries), message="Entry already exists.")
        return
    new_entries = entries + [content]
    total = len(ENTRY_DELIMITER.join(new_entries))
    limit = target_limit(target)
    if total > limit:
        response(False, error=f"{target} memory would exceed {limit} characters.", current_chars=len(ENTRY_DELIMITER.join(entries)), limit=limit)
        return
    write_entries(target, new_entries)
    response(True, target=target, entries=new_entries, entry_count=len(new_entries))


def replace_entry(target: str, old_text: str, content: str) -> None:
    old_text = old_text.strip()
    content = content.strip()
    if not old_text:
        response(False, error="old_text cannot be empty.")
        return
    if not content:
        response(False, error="content cannot be empty.")
        return
    scan_error = scan_content(content)
    if scan_error:
        response(False, error=scan_error)
        return
    entries = read_entries(target, validate=False)
    matches = [index for index, entry in enumerate(entries) if old_text in entry]
    if not matches:
        response(False, error=f"No entry matched '{old_text}'.")
        return
    if len(matches) > 1:
        response(False, error=f"Multiple entries matched '{old_text}'.", matches=[entries[index] for index in matches])
        return
    entries[matches[0]] = content
    total = len(ENTRY_DELIMITER.join(entries))
    limit = target_limit(target)
    if total > limit:
        response(False, error=f"{target} memory would exceed {limit} characters.", current_chars=total, limit=limit)
        return
    validate_entries(path_for(target), entries)
    write_entries(target, entries)
    response(True, target=target, entries=entries, entry_count=len(entries))


def remove_entry(target: str, old_text: str) -> None:
    old_text = old_text.strip()
    if not old_text:
        response(False, error="old_text cannot be empty.")
        return
    entries = read_entries(target, validate=False)
    matches = [index for index, entry in enumerate(entries) if old_text in entry]
    if not matches:
        response(False, error=f"No entry matched '{old_text}'.")
        return
    if len(matches) > 1:
        response(False, error=f"Multiple entries matched '{old_text}'.", matches=[entries[index] for index in matches])
        return
    entries.pop(matches[0])
    validate_entries(path_for(target), entries)
    write_entries(target, entries)
    response(True, target=target, entries=entries, entry_count=len(entries))


def read_facts(limit: int = 50) -> list[dict[str, Any]]:
    path = path_for("facts")
    if not path.exists():
        return []
    facts: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as error:
        raise FactsStorageError(f"facts.jsonl is not valid UTF-8: {error}") from error
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            fact = json.loads(line)
        except json.JSONDecodeError as error:
            raise FactsStorageError(f"facts.jsonl line {line_number} contains invalid JSON: {error}") from error
        if not isinstance(fact, dict):
            raise FactsStorageError(f"facts.jsonl line {line_number} must be a JSON object.")
        scan_error = scan_fact_strings(fact)
        if scan_error:
            raise FactsStorageError(f"facts.jsonl line {line_number} is unsafe. {scan_error}")
        facts.append(fact)
    return facts[-limit:]


def write_facts(facts: list[dict[str, Any]]) -> None:
    lines = [json.dumps(fact, ensure_ascii=False, sort_keys=True) for fact in facts]
    atomic_write(path_for("facts"), "\n".join(lines) + ("\n" if lines else ""))


def append_fact(raw_json: str) -> None:
    try:
        fact = json.loads(raw_json)
    except json.JSONDecodeError as error:
        response(False, error=f"Invalid JSON fact: {error}")
        return
    if not isinstance(fact, dict):
        response(False, error="Fact must be a JSON object.")
        return
    for key in ["type", "raw", "source", "confidence"]:
        if key not in fact:
            response(False, error=f"Fact missing required key '{key}'.")
            return
    raw = str(fact.get("raw", "")).strip()
    if not raw:
        response(False, error="Fact raw cannot be empty.")
        return
    scan_error = scan_fact_strings(fact)
    if scan_error:
        response(False, error=scan_error)
        return
    fact.setdefault("updated_at", datetime.now(timezone.utc).date().isoformat())
    serialized = json.dumps(fact, ensure_ascii=False, sort_keys=True)
    if len(serialized) > FACTS_MAX_ENTRY_CHARS:
        response(False, error=f"Fact entry would exceed {FACTS_MAX_ENTRY_CHARS} characters.", limit=FACTS_MAX_ENTRY_CHARS)
        return
    facts = read_facts(limit=FACTS_MAX_ENTRIES + 1)
    identity = fact_identity(fact)
    for existing in facts:
        if fact_identity(existing) == identity:
            response(True, fact=existing, fact_count=len(facts), message="Fact already exists.")
            return
    if len(facts) >= FACTS_MAX_ENTRIES:
        response(False, error=f"facts memory would exceed {FACTS_MAX_ENTRIES} entries.", current_entries=len(facts), limit=FACTS_MAX_ENTRIES)
        return
    path = path_for("facts")
    path.parent.mkdir(parents=True, exist_ok=True)
    projected_bytes = (path.stat().st_size if path.exists() else 0) + len((serialized + "\n").encode("utf-8"))
    if projected_bytes > FACTS_MAX_BYTES:
        response(False, error=f"facts memory would exceed {FACTS_MAX_BYTES} bytes.", current_bytes=path.stat().st_size if path.exists() else 0, limit=FACTS_MAX_BYTES)
        return
    with path.open("a", encoding="utf-8") as handle:
        handle.write(serialized + "\n")
    response(True, fact=fact, fact_count=len(facts) + 1)


def remove_fact(match: str) -> None:
    match = match.strip()
    if not match:
        response(False, error="match cannot be empty.")
        return
    needle = match.casefold()
    facts = read_facts(limit=FACTS_MAX_ENTRIES + 1)
    kept: list[dict[str, Any]] = []
    removed: list[dict[str, Any]] = []
    for fact in facts:
        haystack = "\n".join(str(fact.get(key, "")) for key in ["raw", "canonical", "type"]).casefold()
        if needle in haystack:
            removed.append(fact)
        else:
            kept.append(fact)
    write_facts(kept)
    response(True, removed_count=len(removed), fact_count=len(kept), facts=kept, removed=removed)


def read_all() -> None:
    user_entries = read_entries("user")
    memory_entries = read_entries("memory")
    facts = read_facts()
    response(
        True,
        user_entries=user_entries,
        memory_entries=memory_entries,
        facts=facts,
        usage={
            "user_chars": len(ENTRY_DELIMITER.join(user_entries)),
            "user_limit": USER_LIMIT,
            "memory_chars": len(ENTRY_DELIMITER.join(memory_entries)),
            "memory_limit": MEMORY_LIMIT,
        },
    )


def summarize() -> None:
    user_entries = read_entries("user")
    memory_entries = read_entries("memory")
    facts = read_facts(limit=10)
    lines = []
    if user_entries:
        lines.append("USER:")
        lines.extend(f"- {entry}" for entry in user_entries)
    if memory_entries:
        lines.append("MEMORY:")
        lines.extend(f"- {entry}" for entry in memory_entries)
    if facts:
        lines.append("FACTS:")
        lines.extend(f"- {fact.get('type')}: {fact.get('raw')}" for fact in facts)
    response(True, summary="\n".join(lines), user_entry_count=len(user_entries), memory_entry_count=len(memory_entries), fact_count=len(facts))


def main() -> None:
    parser = JsonArgumentParser(description="Manage Longchina local agent memory.")
    subparsers = parser.add_subparsers(dest="command", required=True, parser_class=JsonArgumentParser)

    subparsers.add_parser("read")
    subparsers.add_parser("summarize")

    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("content")

    replace_user = subparsers.add_parser("replace-user")
    replace_user.add_argument("old_text")
    replace_user.add_argument("content")

    remove_user = subparsers.add_parser("remove-user")
    remove_user.add_argument("old_text")

    add_memory = subparsers.add_parser("add-memory")
    add_memory.add_argument("content")

    replace_memory = subparsers.add_parser("replace-memory")
    replace_memory.add_argument("old_text")
    replace_memory.add_argument("content")

    remove_memory = subparsers.add_parser("remove-memory")
    remove_memory.add_argument("old_text")

    append_fact_parser = subparsers.add_parser("append-fact")
    append_fact_parser.add_argument("fact_json")

    remove_fact_parser = subparsers.add_parser("remove-fact")
    remove_fact_parser.add_argument("match")

    args = parser.parse_args()
    memory_dir().mkdir(parents=True, exist_ok=True)

    try:
        if args.command == "read":
            read_all()
        elif args.command == "summarize":
            summarize()
        elif args.command == "add-user":
            add_entry("user", args.content)
        elif args.command == "replace-user":
            replace_entry("user", args.old_text, args.content)
        elif args.command == "remove-user":
            remove_entry("user", args.old_text)
        elif args.command == "add-memory":
            add_entry("memory", args.content)
        elif args.command == "replace-memory":
            replace_entry("memory", args.old_text, args.content)
        elif args.command == "remove-memory":
            remove_entry("memory", args.old_text)
        elif args.command == "append-fact":
            append_fact(args.fact_json)
        elif args.command == "remove-fact":
            remove_fact(args.match)
    except (FactsStorageError, MemoryStorageError) as error:
        response(False, error=str(error))
        sys.exit(1)


if __name__ == "__main__":
    main()
