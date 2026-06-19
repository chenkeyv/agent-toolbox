---
name: rename-master-to-main
description: Safely rename a Git repository default branch from master to main. Use when the user asks to change, migrate, rename, or switch a repo branch from master to main, including local branch rename, upstream tracking, GitHub default branch updates, branch protection considerations, and remote master cleanup.
---

# Rename Master To Main

Use this skill to migrate a repository from `master` to `main` without losing work,
breaking the remote default branch, or deleting the old branch too early.

## Workflow

1. Inspect the repository before changing anything.
   - Run `git status --short --branch`.
   - Run `git branch --all --verbose`.
   - Run `git remote -v`.
   - If a remote exists, run `git fetch --prune`.
   - Stop if there are unrelated local changes that could be confused with the branch migration.

2. Determine the current state.
   - If local `main` already exists, do not blindly rename over it.
   - If local `master` exists and `main` does not, rename it with `git branch -m master main`.
   - If the current branch is `master`, use `git branch -m main`.
   - If neither branch exists locally, inspect remote branches before creating anything.

3. Push `main` and set upstream.
   - Use `git push -u origin main` when `origin` exists.
   - If the repository has a different remote name, use that remote instead of assuming `origin`.
   - If there is no remote, finish with the local rename and report that no remote update was possible.

4. Update the remote default branch when using GitHub.
   - Prefer GitHub CLI when available and authenticated:
     `gh repo edit --default-branch main`.
   - If the repo is not inferred from the current directory, pass `OWNER/REPO`.
   - If `gh` lacks permissions, report the required manual step: change the default branch to
     `main` in the repository settings before deleting remote `master`.

5. Handle branch protection and rulesets before cleanup.
   - If `master` has required checks, signed commits, or protection rules, verify whether equivalent
     rules exist for `main`.
   - Do not delete remote `master` until the remote default branch is confirmed as `main`.

6. Delete the old remote branch only after confirmation.
   - Confirm the remote default branch is `main`, for example with
     `gh repo view --json defaultBranchRef`.
   - Then delete `master` with `git push origin --delete master`.
   - If deletion is blocked by protections or permissions, leave it and explain the blocker.

7. Update local stale refs and tracking.
   - Run `git fetch --prune`.
   - Check `git status --short --branch`.
   - Ensure the final branch is `main` and tracks the intended remote branch.

## Commit And Messaging

If repository files are changed as part of the migration, such as docs, CI config, badges,
or setup scripts that mention `master`, use a Conventional Commit message.

Use multiple `-m` flags for multiline commits:

```bash
git commit -m "chore(repo): rename default branch to main" \
  -m "Update branch references and repository setup docs."
```

## Safety Rules

- Never run `git reset --hard` or overwrite an existing `main` branch without explicit user approval.
- Never delete remote `master` before the remote default branch is confirmed as `main`.
- Preserve unrelated local changes.
- Prefer non-interactive commands.
- Report any missing GitHub permissions, branch protection blockers, or absent remotes clearly.
