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

For projects that should use Agent Toolbox, start from the
[canonical `AGENTS.md` template](../skills/setup-agent-project/references/agents-template.md) and
tailor it to the target repository.

Use root `AGENTS.md` when the active client supports it; otherwise adapt the template to that
client's project-instruction file.

## Refresh Existing Projects

Refresh only the content between `<!-- agent-toolbox:start -->` and
`<!-- agent-toolbox:end -->`. If the markers are absent but a clear Agent Toolbox section exists,
wrap that section and normalize only it. Otherwise add one managed block without rewriting
project-specific rules. A second refresh should produce no diff unless the template changed.

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
