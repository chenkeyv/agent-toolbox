# Setup Guide

Install Agent Toolbox once as a Codex plugin instead of adding reusable tooling to every project.

## Recommended Setup

Add this private repository as a Codex plugin marketplace, then install the plugin:

```bash
codex plugin marketplace add chenkeyv/agent-toolbox --ref main
codex plugin add agent-toolbox@agent-toolbox
```

Start a new Codex thread after installation so the bundled skills are available.

## Local Development Setup

When testing changes from this checkout before pushing them, add the local marketplace root:

```bash
codex plugin marketplace add /Users/keyv/Developer/agent-toolbox
codex plugin add agent-toolbox@agent-toolbox
```

After editing the package, reinstall from the same marketplace and start a new thread.

## Project Instructions

For projects that should use Agent Toolbox, add a root `AGENTS.md` like this:

```md
# Codex Project Instructions

<!-- agent-toolbox:start -->
## Agent Toolbox Setup

- This repository uses the installed Agent Toolbox Codex plugin or project-owned skills under `.agents/skills/`.
- Use task-specific skills when their descriptions match. Do not assume Agent Toolbox provides a multi-agent runtime.
- Current user instructions and current repository files take precedence over bundled skill guidance and memory templates.

## Project Memory

- Keep durable project memory in `.agent-memory/project.md`, `docs/agent-memory.md`, or a topic-specific file such as `learning/<topic>.md`.
- Keep project-specific checkpoints in this repository, not inside reusable tooling.
- Store only durable, useful context with provenance when practical.

## Working Rules

- Start by inspecting `git status --short --branch` and existing project instructions before changing files.
- Keep edits scoped to the requested setup and preserve unrelated local changes.
- Back every conclusion, recommendation, and summary with real evidence such as
  file references, command output, tests, experiments, source links, or
  measured data.
- Clearly label assumptions when evidence is unavailable.
- Do not commit secrets, credentials, OAuth state, or machine-local configuration.
- Do not vendor or clone reusable tooling into this repository unless plugin installation is unavailable or the user explicitly wants local skills.
- Keep repository-specific skills under `.agents/skills/`.
- Add or update tests with every change. If a test cannot be added, state the
  reason and what validation was run instead.
- When tests fail, identify the root cause before changing or dismissing the
  result, even if the failing case appears unrelated.
- When creating or amending Git commits, use Conventional Commits format
  (`type(scope): subject`).
- Split large or logically separate changes into multiple commits when that
  makes review or rollback clearer.
- Keep Git commit message lines wrapped at 72 characters when practical.
- For multi-line or multi-paragraph commit messages, preserve line breaks with
  separate `-m` flags or a commit message file instead of escaped `\n` in a
  single `-m` argument.
- Run the most relevant validation after setup changes and report any checks that were skipped.
<!-- agent-toolbox:end -->

## Project-Specific Rules

- Add repository-specific build, test, lint, release, and ownership rules here.
```

Codex discovers root `AGENTS.md` automatically when it works in the target repository.

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
Use $setup-agent-project to refresh this repository's Codex instructions.
```

## Project-Owned Skills

Put repository-specific reusable behavior under `.agents/skills/<skill-name>/SKILL.md`. Do not add
an agent roster or subagent configuration unless the project intentionally integrates a runtime
that consumes it.

## Memory Boundary

Bundled files under `memory/` are reusable templates. Project-specific memory belongs in the project
using the plugin. Store only durable, reusable context with provenance, and write it only when the
user authorizes persistence.
