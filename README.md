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
| Solution Architect | Designs the technical approach and integration plan. | [agents/solution-architect.md](agents/solution-architect.md) |
| Implementation Engineer | Builds the requested changes with tests and practical documentation. | [agents/implementation-engineer.md](agents/implementation-engineer.md) |
| QA Reviewer | Reviews correctness, risks, edge cases, and release readiness. | [agents/qa-reviewer.md](agents/qa-reviewer.md) |

## Suggested Workflow

Start with the [default delivery workflow](workflows/default-cycle.md):

1. The Lead Orchestrator restates the goal and selects the needed agents.
2. Product Strategist defines the target outcome and acceptance criteria.
3. Research Analyst gathers current facts when the work depends on external knowledge.
4. Solution Architect proposes a design and calls out key tradeoffs.
5. Implementation Engineer makes the change.
6. QA Reviewer checks the result against the acceptance criteria.
7. Lead Orchestrator summarizes what changed, what was verified, and what remains.

## How To Use

Copy the relevant agent profile into your agent runtime as the system or role instruction.
For multi-agent workflows, use `team.yaml` as the routing map and `workflows/default-cycle.md`
as the shared process.

Example task prompt:

```text
Use the AgentTeam workflow. Goal: add GitHub issue templates to this repo.
Lead Orchestrator should coordinate, Product Strategist should define the templates,
Implementation Engineer should create them, and QA Reviewer should review the final files.
```

