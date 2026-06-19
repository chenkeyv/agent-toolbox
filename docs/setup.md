# Setup Guide

This guide shows how to install Agent Toolbox into another repository while keeping the team files
hidden, versioned, and easy to update.

## Recommended Layout

Use Agent Toolbox as a hidden Git submodule:

```text
target-repo/
  AGENTS.md
  .gitmodules
  .agents/
    agent-toolbox/
      team.yaml
      agents/
      skills/
      plugins/
      workflows/
      memory/
```

This keeps the target repository root clean while preserving Agent Toolbox's upstream Git history.

## Add Agent Toolbox To A Repository

Because this repository is private, make sure the target machine is authenticated
with GitHub before adding or updating the submodule.

From the target repository root:

```bash
git init
git submodule add -b main https://github.com/chenkeyv/agent-toolbox.git .agents/agent-toolbox
```

If the target repository already exists, skip `git init`.

## Add Codex Project Instructions

Create a root `AGENTS.md` in the target repository so Codex can discover the hidden team bundle:

```md
# Codex Project Instructions

## Repository Context

- This repository uses the hidden Agent Toolbox bundle at `.agents/agent-toolbox`.
- `.agents/agent-toolbox` is a Git submodule tracking `https://github.com/chenkeyv/agent-toolbox.git` on `main`.
- When the user asks to use Agent Toolbox, read `.agents/agent-toolbox/team.yaml` first, then the referenced workflow, agent profile, and memory files needed for the task.
- Keep target-project memory outside `.agents/agent-toolbox`; point to the project-owned memory file here when one exists.
- Treat `.agents/agent-toolbox/memory/` as reusable Agent Toolbox memory templates, not as the canonical place for target-project checkpoints. Current user instructions and current repository files take precedence.

## Working Rules

- Keep Agent Toolbox files under `.agents/agent-toolbox` unless the user asks to move or upgrade the bundle.
- Preserve the nested Agent Toolbox Git metadata and `.gitmodules` entry so upstream updates remain available.
- Do not store secrets, credentials, or private personal details in Agent Toolbox memory files.
```

Codex discovers root `AGENTS.md` automatically when it works in the target repository.

## Restore After Cloning

When cloning a repository that uses Agent Toolbox as a submodule:

```bash
git clone --recurse-submodules <target-repo-url>
```

If the repository was already cloned without submodules:

```bash
git submodule update --init --recursive
```

## Update Agent Toolbox Later

To pull the latest Agent Toolbox files:

```bash
git submodule update --remote --checkout .agents/agent-toolbox
git add .agents/agent-toolbox
git commit -m "Update Agent Toolbox"
```

The first command works even when the submodule was restored in detached HEAD state. It fetches
the branch configured in `.gitmodules`, then checks out the latest matching Agent Toolbox commit. The
final two commands record the new submodule commit in the target repository.

## Use The Team

Example prompt:

```text
Use the Agent Toolbox workflow from .agents/agent-toolbox. Goal: add GitHub issue templates to this repo.
```

Learning prompt:

```text
Use the Agent Toolbox Learning Coach from .agents/agent-toolbox.

Topic:
I want to understand distributed systems from the ground up.
```

## Local Customization

Do not store target-project memory inside `.agents/agent-toolbox/memory/` unless you maintain a fork
and intend to commit those changes to Agent Toolbox. That directory belongs to the Agent Toolbox submodule;
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
