# Agent Project Instructions

Use this as a starting point, then tailor it to the target project.

```md
# Agent Project Instructions

<!-- agent-toolbox:start -->
## Agent Toolbox Setup

- This repository uses the installed Agent Toolbox Agent Plugin or project-owned skills in the active client's supported location.
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
- Keep repository-specific skills in the active client's project-owned skills directory.
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
