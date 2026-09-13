# Setup Guide

Install Agent Toolbox once as an Agent Plugins 1.0 package instead of adding reusable tooling to
every project.

## Recommended Setup

Use the active client's Agent Plugins installation flow and select the repository root: the
directory containing `plugin.json` and `skills/`. Installation, distribution, enablement, and
updates are intentionally client-specific in the Agent Plugins specification.

The portable package does not itself require a marketplace wrapper or `.codex-plugin` manifest.
A target client's installation or distribution flow may require one even when the skills are
portable. Add only the adapter justified by that client's current documentation and the requested
setup, recording its target, purpose, and validation. Keep root `plugin.json` and `skills/` canonical
instead of duplicating skill sources. After installation, follow the client's reload or new-task
guidance so the bundled skills are available. Package validation alone does not verify installation
in every client.

## Local Development Setup

When testing changes from this checkout before pushing them, select this repository root as the
local Agent Plugin directory. After editing the package, refresh or reinstall it using the active
client's development workflow.

## Project Instructions

Follow the setup skill's [evidence-driven drafting workflow](../skills/setup-agent-project/SKILL.md).
The optional [`AGENTS.md` example](../skills/setup-agent-project/references/agents-example.md)
illustrates a finished result; the
[`content review](../skills/setup-agent-project/references/agents-content-review.md) checks the
draft for omissions. Neither requires a particular structure or content.

Use root `AGENTS.md` when the active client supports it; otherwise apply the same evidence-driven
tailoring process to that client's project-instruction file.

## Refresh Existing Projects

Re-evaluate the entire project instruction file against current repository evidence, including
project-specific rules outside any managed block. Update stale commands, paths, boundaries, and
ownership statements while preserving instructions that remain accurate.

Use `<!-- agent-toolbox:start -->` and `<!-- agent-toolbox:end -->` only as an ownership boundary for
project-specific Agent Toolbox workflow guidance. Do not add or retain a managed block merely
because Agent Toolbox is installed or its setup skill was used; remove empty markers. Resolve
conflicts through applicable instruction precedence and current evidence. Continue unaffected
inspection; pause dependent edits only when permission, ownership, or risk remains unresolved.
Apply the post-draft content review and
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
