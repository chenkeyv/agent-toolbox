# Agent Toolbox

Reusable agent tooling for turning ideas into researched, designed, implemented, reviewed,
and teachable work.

This directory is the installable Codex plugin package. The repository root exposes it through
`.agents/plugins/marketplace.json`, so install the marketplace once instead of cloning this repo into
every project.

The core agent profiles are framework-neutral on purpose. They are plain Markdown, and
`team.yaml` provides a lightweight structured index that can later be used by Codex, the
OpenAI Agents SDK, CrewAI, AutoGen, or a custom runner.

## Package Layout

| Path | Purpose |
| --- | --- |
| `.codex-plugin/plugin.json` | Codex plugin manifest. |
| `skills/` | Codex skill entrypoints bundled with this plugin. |
| `agents/` | Framework-neutral Markdown agent profiles. |
| `workflows/` | Reusable handoff and delivery workflows. |
| `memory/` | Reusable memory templates and schema, not project checkpoints. |
| `prompts/` | Reusable prompt templates. |
| `mcp/` | Token-free MCP examples and config snippets. |
| `subagents/` | Codex subagent role configs and notes. |
| `docs/` | Setup and operating guides. |

## Bundled Skills

| Skill | Purpose |
| --- | --- |
| `agent-toolbox` | Load the reusable specialist-agent team and workflows. |
| `rename-master-to-main` | Safely migrate a Git repository default branch from `master` to `main`. |

## Team Roster

| Agent | Purpose | Profile |
| --- | --- | --- |
| Lead Orchestrator | Breaks goals into work, routes tasks, and keeps decisions moving. | [agents/orchestrator.md](agents/orchestrator.md) |
| Product Strategist | Clarifies user needs, scope, tradeoffs, and success criteria. | [agents/product-strategist.md](agents/product-strategist.md) |
| Research Analyst | Finds reliable information, compares options, and records sources. | [agents/research-analyst.md](agents/research-analyst.md) |
| Learning Coach | Teaches topics from first principles and checks for durable understanding. | [agents/learning-coach.md](agents/learning-coach.md) |
| Solution Architect | Designs the technical approach and integration plan. | [agents/solution-architect.md](agents/solution-architect.md) |
| Implementation Engineer | Builds the requested changes with tests and practical documentation. | [agents/implementation-engineer.md](agents/implementation-engineer.md) |
| QA Reviewer | Reviews correctness, risks, edge cases, and release readiness. | [agents/qa-reviewer.md](agents/qa-reviewer.md) |

## Suggested Workflow

Start with the [default delivery workflow](workflows/default-cycle.md):

1. The Lead Orchestrator restates the goal and selects the needed agents.
2. Agents load relevant memory from the [memory folder](memory/README.md).
3. Product Strategist defines the target outcome and acceptance criteria.
4. Research Analyst gathers current facts when the work depends on external knowledge.
5. Solution Architect proposes a design and calls out key tradeoffs.
6. Implementation Engineer makes the change.
7. QA Reviewer checks the result against the acceptance criteria.
8. Lead Orchestrator summarizes what changed, what was verified, and what memory should be updated.

For learning goals, use the [learning cycle](workflows/learning-cycle.md). It routes the topic
through diagnosis, first-principles teaching, active checks, practice, and memory updates.

## Memory

Agent Toolbox uses explicit file-based memory so the team can learn without hiding state.

- Project memory template: [memory/project.md](memory/project.md)
- User preference memory template: [memory/user-preferences.md](memory/user-preferences.md)
- Research memory template: [memory/research.md](memory/research.md)
- Agent-specific memory templates: [memory/agents/](memory/agents/)
- Memory schema: [memory/schema.yaml](memory/schema.yaml)

Read bundled memory as reusable context, not truth. Current user instructions, current repository
files, and fresh source-backed facts always take priority over older memory.

## How To Use

After installing the plugin, start a new Codex thread and ask for Agent Toolbox explicitly:

```text
Use Agent Toolbox workflow. Goal: add GitHub issue templates to this repo.
```

Learning prompt:

```text
Use Agent Toolbox Learning Coach.

Topic:
I want to understand distributed systems from the ground up.

Goal:
Build a durable mental model, not just a summary.
```

See [docs/setup.md](docs/setup.md) for installation and project instruction examples.
