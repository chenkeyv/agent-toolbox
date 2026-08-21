---
name: rename-master-to-main
description: Safely rename a Git repository branch from master to main. Use for either a local-only branch rename or a full remote default-branch migration with upstream tracking, GitHub settings, branch protections, and optional remote master cleanup. Distinguish the requested scope before any remote mutation.
---

# Rename Master To Main

Use this skill to migrate a repository from `master` to `main` without losing work,
breaking the remote default branch, or deleting the old branch too early.

## Workflow

1. Inspect the repository before changing anything.
   - Run `git status --short --branch`.
   - Run `git branch --all --verbose`.
   - Run `git remote -v`.
   - Stop if there are unrelated local changes that could be confused with the branch migration.

2. Establish the requested scope before remote interaction.
   - Treat an explicit request to rename only the local branch as local-only.
   - Treat a request to migrate the repository default branch, update the remote, or complete the
     full `master`-to-`main` migration as remote migration scope.
   - If the scope is ambiguous, complete only safe local inspection and ask before fetching,
     pushing, changing remote settings, or deleting a branch.
   - For local-only scope, do not fetch, push, change the remote default branch, or delete remote
     `master`, even when a remote exists.
   - For remote migration scope, run `git fetch --prune` before evaluating remote branch state.
   - Treat remote `master` cleanup as in scope only when the user asks to remove the legacy branch
     or explicitly requests a complete migration that includes cleanup.

3. Determine and update the local state.
   - If local `main` already exists, do not blindly rename over it.
   - If local `master` exists and `main` does not, rename it with `git branch -m master main`.
   - If the current branch is `master`, use `git branch -m main`.
   - If neither branch exists locally, inspect remote branches before creating anything.
   - Run `git status --short --branch` after the local change.
   - For local-only scope, report the result and stop here.

4. Prepare and push only for remote migration scope.
   - Use `git push -u origin main` when `origin` exists.
   - If the repository has a different remote name, use that remote instead of assuming `origin`.
   - If there is no remote, finish with the local rename and report that no remote update was possible.

5. Update the remote default branch when using GitHub.
   - Prefer GitHub CLI when available and authenticated:
     `gh repo edit --default-branch main`.
   - If the repo is not inferred from the current directory, pass `OWNER/REPO`.
   - If `gh` lacks permissions, report the required manual step: change the default branch to
     `main` in the repository settings before deleting remote `master`.

6. Handle branch protection and rulesets before cleanup.
   - If `master` has required checks, signed commits, or protection rules, verify whether equivalent
     rules exist for `main`.
   - Do not delete remote `master` until the remote default branch is confirmed as `main`.

7. Delete the old remote branch only when cleanup is in scope and after confirmation.
   - Do not infer cleanup authority from a local-only rename.
   - Confirm the remote default branch is `main`, for example with
     `gh repo view --json defaultBranchRef`.
   - Then delete `master` with `git push origin --delete master`.
   - If deletion is blocked by protections or permissions, leave it and explain the blocker.

8. Update local stale refs and tracking after remote migration.
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
