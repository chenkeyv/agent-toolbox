# Setup Guide

Install Agent Toolbox once as a Codex plugin instead of adding it as a submodule to every project.

## Recommended Setup

Add this private repository as a Codex plugin marketplace, then install the `agent-toolbox` plugin:

```bash
codex plugin marketplace add chenkeyv/agent-toolbox --ref main
codex plugin add agent-toolbox@agent-toolbox
```

Start a new Codex thread after installation so the bundled skill is available.

## Local Development Setup

When testing changes from this local checkout before pushing them, add the local marketplace root:

```bash
codex plugin marketplace add /Users/keyv/Developer/agent-toolbox
codex plugin add agent-toolbox@agent-toolbox
```

After editing the plugin package, reinstall from the same marketplace and start a new thread.

## Project Instructions

For projects that should use Agent Toolbox, add a root `AGENTS.md` like this:

```md
# Codex Project Instructions

<!-- agent-toolbox:start -->
## Agent Toolbox Setup

- This repository uses the installed Agent Toolbox Codex plugin.
- When the user asks to use Agent Toolbox, use the installed plugin skill and follow its bundled team/workflow files.
- Keep project-specific learning state, checkpoints, secrets, credentials, and private local notes inside this repository, not inside Agent Toolbox.
- Current user instructions and current repository files take precedence over bundled Agent Toolbox memory templates.

## Working Rules

- Start by inspecting `git status --short --branch` and existing project instructions before changing files.
- Keep edits scoped to the requested setup and preserve unrelated local changes.
- Back conclusions, recommendations, and summaries with real evidence such as
  file references, command output, tests, source links, or measured data.
- Clearly label assumptions when evidence is unavailable.
- Do not vendor or clone Agent Toolbox into this repository unless plugin installation is unavailable.
- Store durable project memory in a project-owned path such as `learning/<topic>.md`, `docs/agent-memory.md`, or `.agent-memory/project.md`.
- Keep local agent assets as project-owned files under `.agents/` unless the user explicitly asks for an external Git submodule.
- Avoid committing secrets, credentials, OAuth state, or machine-local configuration.
- Use Conventional Commits for Git commit subjects (`type(scope): subject`).
- Keep Git commit message lines wrapped at 72 characters when practical.
- For multi-paragraph commit messages, use separate `-m` flags or a commit
  message file instead of escaped `\n` in a single `-m`.
- Run the most relevant validation after setup changes and report any checks that were skipped.
<!-- agent-toolbox:end -->

## Project-Specific Rules

- Add repository-specific build, test, lint, release, and ownership rules here.
```

Codex discovers root `AGENTS.md` automatically when it works in the target repository.

## Refresh Existing Projects

For existing projects, refresh only the content between:

```md
<!-- agent-toolbox:start -->
<!-- agent-toolbox:end -->
```

If a project does not have those markers yet, add them around the existing Agent Toolbox section
when one is clear. Otherwise add one managed block without rewriting project-specific rules. A
second refresh should produce no diff unless the template changed.

## Use The Team

Example task prompt:

```text
Use Agent Toolbox workflow. Goal: add GitHub issue templates to this repo.
```

Learning prompt:

```text
Use Agent Toolbox Learning Coach.

Topic:
I want to understand distributed systems from the ground up.
```

## Memory Boundary

Bundled files under `memory/` are reusable templates and context for the plugin. Project-specific
memory belongs in the project using the plugin. Store only durable, reusable context, include
provenance when possible, and avoid secrets or unverifiable personal details.
