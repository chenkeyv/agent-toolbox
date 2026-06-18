# Setup Guide

This guide shows how to install AgentTeam into another repository while keeping the team files
hidden, versioned, and easy to update.

## Recommended Layout

Use AgentTeam as a hidden Git submodule:

```text
target-repo/
  AGENTS.md
  .gitmodules
  .agents/
    AgentTeam/
      team.yaml
      agents/
      workflows/
      memory/
```

This keeps the target repository root clean while preserving AgentTeam's upstream Git history.

## Add AgentTeam To A Repository

From the target repository root:

```bash
git init
git submodule add -b main https://github.com/chenkeyv/AgentTeam.git .agents/AgentTeam
```

If the target repository already exists, skip `git init`.

## Add Codex Project Instructions

Create a root `AGENTS.md` in the target repository so Codex can discover the hidden team bundle:

```md
# Codex Project Instructions

## Repository Context

- This repository uses the hidden AgentTeam bundle at `.agents/AgentTeam`.
- `.agents/AgentTeam` is a Git submodule tracking `https://github.com/chenkeyv/AgentTeam.git` on `main`.
- When the user asks to use AgentTeam, read `.agents/AgentTeam/team.yaml` first, then the referenced workflow, agent profile, and memory files needed for the task.
- Keep target-project memory outside `.agents/AgentTeam`; point to the project-owned memory file here when one exists.
- Treat `.agents/AgentTeam/memory/` as reusable AgentTeam memory templates, not as the canonical place for target-project checkpoints. Current user instructions and current repository files take precedence.

## Working Rules

- Keep AgentTeam files under `.agents/AgentTeam` unless the user asks to move or upgrade the bundle.
- Preserve the nested AgentTeam Git metadata and `.gitmodules` entry so upstream updates remain available.
- Do not store secrets, credentials, or private personal details in AgentTeam memory files.
```

Codex discovers root `AGENTS.md` automatically when it works in the target repository.

## Restore After Cloning

When cloning a repository that uses AgentTeam as a submodule:

```bash
git clone --recurse-submodules <target-repo-url>
```

If the repository was already cloned without submodules:

```bash
git submodule update --init --recursive
```

## Update AgentTeam Later

To pull the latest AgentTeam files:

```bash
git submodule update --remote --checkout .agents/AgentTeam
git add .agents/AgentTeam
git commit -m "Update AgentTeam"
```

The first command works even when the submodule was restored in detached HEAD state. It fetches
the branch configured in `.gitmodules`, then checks out the latest matching AgentTeam commit. The
final two commands record the new submodule commit in the target repository.

## Use The Team

Example prompt:

```text
Use the AgentTeam workflow from .agents/AgentTeam. Goal: add GitHub issue templates to this repo.
```

Learning prompt:

```text
Use the AgentTeam Learning Coach from .agents/AgentTeam.

Topic:
I want to understand distributed systems from the ground up.
```

## Local Customization

Do not store target-project memory inside `.agents/AgentTeam/memory/` unless you maintain a fork
and intend to commit those changes to AgentTeam. That directory belongs to the AgentTeam submodule;
editing it for local state makes the submodule dirty and the changes will not be restored from the
parent repository alone.

For target-project memory, create a project-owned file outside the submodule and point the root
`AGENTS.md` to it. Example locations:

```text
learning/<topic>.md
docs/agent-memory.md
.agent-memory/project.md
```

Store only durable, reusable context, include provenance when possible, and avoid secrets or
unverifiable personal details.
