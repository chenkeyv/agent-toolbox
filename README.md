# AgentTeam

A starter agent team for turning ideas into researched, designed, implemented, and reviewed work.

This repo is framework-neutral on purpose. The agent profiles are plain Markdown, and `team.yaml`
provides a lightweight structured index that can later be used by Codex, the OpenAI Agents SDK,
CrewAI, AutoGen, or a custom runner.

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

AgentTeam uses explicit file-based memory so the team can learn without hiding state.

- Project memory: [memory/project.md](memory/project.md)
- User preference memory: [memory/user-preferences.md](memory/user-preferences.md)
- Research memory: [memory/research.md](memory/research.md)
- Agent-specific memory: [memory/agents/](memory/agents/)
- Memory schema: [memory/schema.yaml](memory/schema.yaml)

Read memory as context, not truth. Current user instructions, current files, and fresh source-backed
facts always take priority over older memory.

## How To Use

Copy the relevant agent profile into your agent runtime as the system or role instruction.
For multi-agent workflows, use `team.yaml` as the routing map, `memory/` as the shared
memory store, and `workflows/default-cycle.md` as the shared process.

Example task prompt:

```text
Use the AgentTeam workflow. Goal: add GitHub issue templates to this repo.
Lead Orchestrator should coordinate, Product Strategist should define the templates,
Implementation Engineer should create them, and QA Reviewer should review the final files.
```

Learning prompt:

```text
Use the AgentTeam Learning Coach.

Topic:
I want to understand distributed systems from the ground up.

Goal:
Build a durable mental model, not just a summary.

Output:
- First-principles explanation
- Simple worked example
- Common failure modes
- One exercise
- Check question before moving on
```
