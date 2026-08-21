# Agent Toolbox

Reusable agent skills for project setup, behavior improvement, and safe repository maintenance.

This repository root is a self-contained
[Agent Plugins 1.0](https://agent-plugins.org/specification) package. Compatible clients load the
portable `plugin.json` manifest and discover each immediate child under `skills/` as an Agent Skill.
The package is skills-first on purpose: detailed workflow instructions load only when a task matches
a focused skill.

## Install

Follow the active client's Agent Plugins setup instructions and select this repository root as the
plugin directory. Distribution, installation, enablement, and updates are client-specific rather
than part of the portable specification. Because this is a private repository, the chosen client or
local checkout must already have access to it.

See [docs/setup.md](docs/setup.md) for package use and project-instruction guidance.

## Layout

| Path | Purpose |
| --- | --- |
| `plugin.json` | Portable Agent Plugins 1.0 manifest. |
| `skills/` | Agent Skill entrypoints bundled with this plugin. |
| `memory/` | Reusable memory templates and schema, not project checkpoints. |
| `prompts/` | Reusable prompt templates. |
| `mcp/` | Token-free MCP examples and config snippets; not a runtime `mcp.json` component. |
| `docs/` | Setup and operating guides. |

## Bundled Skills

| Skill | Purpose |
| --- | --- |
| `prevent-repeat` | Investigate missed behavior and apply durable prevention. |
| `rename-master-to-main` | Safely migrate a Git repository default branch from `master` to `main`. |
| `setup-agent-project` | Configure repositories for Agent Toolbox and project-owned agent workflows. |

## How To Use

After installing the plugin, start a new task or chat and invoke the skill that matches the work.

```text
Use $prevent-repeat to investigate why this instruction was missed and recommend a durable fix.
```

```text
Use $setup-agent-project to configure this repository for agent-assisted work.
```

Keep secrets, credentials, local OAuth state, and project-specific checkpoints
out of this repository. Project memory belongs in the project using the plugin.
