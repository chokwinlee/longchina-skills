# longchina public agent skills

This repository is the public distribution surface for longchina agent skills.

It intentionally does not contain the private product monorepo, backend source, web app source, deployment configuration, tests, or internal documentation.

## Install the agent skill

```bash
npx -y skills add chokwinlee/longchina-skills --skill longchina-data -a codex -y
```

Use `-a claude-code` or `-a cursor` for those agents.

## CLI requirement

The `longchina-data` skill assumes the `longchina` CLI is already installed and available on `PATH`. CLI installation is documented on the longchina website, not inside the skill package.
