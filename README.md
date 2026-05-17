# longchina public agent assets

This repository is the public distribution surface for longchina agent skills and CLI release binaries.

It intentionally does not contain the private product monorepo, backend source, web app source, deployment configuration, tests, or internal documentation.

## Install the agent skill

```bash
npx -y skills add chokwinlee/longchina-skills --skill longchina-data -a codex -y
```

Use `-a claude-code` or `-a cursor` for those agents.

## Install the CLI

The public installer downloads native CLI binaries from this repository's GitHub Releases:

```bash
curl -fsSL https://longchina.vercel.app/install.sh | sh
longchina status --json --skill-version 0.1.1
```
