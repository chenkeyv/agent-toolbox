# Agent Toolbox Marketplace

This repository is a private Codex plugin marketplace for Agent Toolbox.
Install the marketplace once, then use the plugin from any project without adding
`.agents/agent-toolbox` as a per-project submodule.

## Install

From any shell that can access this private GitHub repo:

```bash
codex plugin marketplace add chenkeyv/agent-toolbox --ref main
codex plugin add agent-toolbox@agent-toolbox
```

For local development against this checkout:

```bash
codex plugin marketplace add /Users/keyv/Developer/agent-toolbox
codex plugin add agent-toolbox@agent-toolbox
```

Start a new Codex thread after installing or updating the plugin so Codex can
load the bundled skill.

## Layout

| Path | Purpose |
| --- | --- |
| `.agents/plugins/marketplace.json` | Marketplace catalog that exposes the plugin. |
| `plugins/agent-toolbox/` | Installable Codex plugin package. |
| `plugins/agent-toolbox/.codex-plugin/plugin.json` | Plugin manifest. |
| `plugins/agent-toolbox/skills/agent-toolbox/SKILL.md` | Codex skill entrypoint. |
| `plugins/agent-toolbox/agents/` | Framework-neutral Markdown agent profiles. |
| `plugins/agent-toolbox/workflows/` | Reusable handoff and delivery workflows. |
| `plugins/agent-toolbox/memory/` | Reusable memory templates and schema, not project checkpoints. |

Keep secrets, credentials, local OAuth state, and project-specific checkpoints
out of this repository. Project memory belongs in the project using the plugin.
