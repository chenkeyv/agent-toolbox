# Setup Guide

Install Agent Toolbox once as an Agent Plugins 1.0 package instead of adding reusable tooling to
every project.

## Recommended Setup

Use the active client's Agent Plugins installation flow and select the repository root: the
directory containing `plugin.json` and `skills/`. Installation, distribution, enablement, and
updates are intentionally client-specific in the Agent Plugins specification.

Agent Toolbox does not require a Codex marketplace wrapper or `.codex-plugin` manifest. Add
client-specific packaging only when a requested capability is outside the portable format. After
installation, follow the client's reload or new-task guidance so the bundled skills are available.

## Local Development Setup

When testing changes from this checkout before pushing them, select this repository root as the
local Agent Plugin directory. After editing the package, refresh or reinstall it using the active
client's development workflow.

## Project Instructions

For projects that should use Agent Toolbox, inspect the target and generate its instructions freely
from the repository's actual structure, commands, constraints, and the user's request. Do not base
the result on a template or fixed section list. The optional
[`AGENTS.md` example](../skills/setup-agent-project/references/agents-example.md) illustrates one
possible finished result for a fictional project; it is not source material for the target file.
After the independent first draft is complete, use the
[`AGENTS.md` content review](../skills/setup-agent-project/references/agents-content-review.md) to
check for omitted categories of project facts. Any addition must still be written from repository
evidence, not copied from the review.

Use root `AGENTS.md` when the active client supports it; otherwise apply the same evidence-driven
tailoring process to that client's project-instruction file.

## Refresh Existing Projects

Re-evaluate the entire project instruction file against current repository evidence, including
project-specific rules outside any managed block. Update stale commands, paths, boundaries, and
ownership statements while preserving instructions that remain accurate.

Use `<!-- agent-toolbox:start -->` and `<!-- agent-toolbox:end -->` only as an ownership boundary for
project-specific Agent Toolbox workflow guidance. Do not add or retain a managed block merely
because Agent Toolbox is installed or its setup skill was used; remove empty markers. Stop when
ownership or an external-upstream relationship is unclear. Apply the post-draft content review and
make a second refresh produce no diff.

## Use The Skills

Behavior-retrospective prompt:

```text
Use $prevent-repeat to investigate why this behavior was missed and recommend a durable fix.
```

Project-setup prompt:

```text
Use $setup-agent-project to refresh this repository's agent instructions.
```

## Project-Owned Skills

Put repository-specific reusable behavior in the active client's project-owned skills directory.
Do not add an agent roster or subagent configuration unless the project intentionally integrates a
runtime that consumes it.

## Memory Boundary

Bundled files under `memory/` are reusable templates. Project-specific memory belongs in the project
using the plugin. Store only durable, reusable context with provenance, and write it only when the
user authorizes persistence.
