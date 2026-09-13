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
than part of the portable specification. A client may need a separate marketplace entry or manifest
for its installation flow; add such an adapter only for a documented target requirement while
keeping this portable package as the source of the skills.

See [docs/setup.md](docs/setup.md) for package use and project-instruction guidance.
See [tests/behavior/README.md](tests/behavior/README.md) for regression checks and agent evaluation.

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
| `audit-agent-assets` | Audit and modernize agent-facing assets for context efficiency and current model capabilities. |
| `prevent-repeat` | Investigate missed behavior and apply durable prevention. |
| `rename-master-to-main` | Migrate `master` to `main` with verified history preservation and guarded cleanup. |
| `setup-agent-project` | Discover client guidance and refresh evidence-driven project instructions idempotently. |

## How To Use

After installing the plugin, start a new task or chat and invoke the skill that matches the work.

```text
Use $audit-agent-assets to review this repository's agent-facing assets and recommend changes only when the evidence supports them.
```

```text
Use $prevent-repeat to investigate why this instruction was missed and recommend a durable fix.
```

```text
Use $setup-agent-project to configure this repository for agent-assisted work.
```

Keep secrets, credentials, local OAuth state, and project-specific checkpoints
out of this repository. Project memory belongs in the project using the plugin.
