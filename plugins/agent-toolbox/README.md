# Agent Toolbox

Reusable Codex skills for project setup, first-principles learning, behavior improvement, and safe
repository maintenance.

This directory is the installable Codex plugin package. The repository root exposes it through
`.agents/plugins/marketplace.json`, so install the marketplace once instead of cloning reusable
tooling into every project.

Agent Toolbox is skills-first on purpose. Codex discovers each focused workflow directly from its
`SKILL.md`, loading detailed instructions only when the task matches.

## Package Layout

| Path | Purpose |
| --- | --- |
| `.codex-plugin/plugin.json` | Codex plugin manifest. |
| `skills/` | Focused Codex skill entrypoints bundled with this plugin. |
| `memory/` | Reusable memory templates and schema, not project checkpoints. |
| `prompts/` | Reusable prompt templates. |
| `mcp/` | Token-free MCP examples and config snippets. |
| `docs/` | Setup and operating guides. |

## Bundled Skills

| Skill | Purpose |
| --- | --- |
| `learning-coach` | Teach concepts from first principles with active practice. |
| `prevent-repeat` | Investigate missed behavior and apply durable prevention. |
| `rename-master-to-main` | Safely migrate a Git repository default branch from `master` to `main`. |
| `setup-agent-project` | Configure repositories for Agent Toolbox and project-owned Codex workflows. |

## Memory

Agent Toolbox keeps reusable memory templates explicit and reviewable:

- Project memory template: [memory/project.md](memory/project.md)
- User preference memory template: [memory/user-preferences.md](memory/user-preferences.md)
- Research memory template: [memory/research.md](memory/research.md)
- Memory schema: [memory/schema.yaml](memory/schema.yaml)

Read bundled memory as reusable context, not truth. Current user instructions, current repository
files, and fresh source-backed facts always take priority over older memory. Write memory only when
the user authorizes it and the information belongs in the target project or explicit memory system.

## How To Use

After installing the plugin, start a new Codex thread and invoke the skill that matches the task.

Learning prompt:

```text
Use $learning-coach to teach me distributed systems from the ground up and check my understanding.
```

Behavior-retrospective prompt:

```text
Use $prevent-repeat to investigate why this instruction was missed and recommend a durable fix.
```

Project-setup prompt:

```text
Use $setup-agent-project to configure this repository for Codex-assisted work.
```

See [docs/setup.md](docs/setup.md) for installation and project instruction examples.
