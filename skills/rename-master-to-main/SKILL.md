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
   - Treat remote `master` cleanup as in scope only when the user asks to remove the legacy branch
     or explicitly requests a complete migration that includes cleanup.
   - For remote migration, select one remote from the request and repository evidence. Record it
     as `migration_remote`; for GitHub, record the matching `HOST/OWNER/REPO` as `migration_repo`.
     Check `git remote get-url --all "$migration_remote"` and
     `git remote get-url --push --all "$migration_remote"`. Verify fetch and push address the same
     repository and there is only one push destination; resolve ambiguity before remote mutation.
     Check for mirror-push configuration before pushing. Use this remote and explicit GitHub
     repository throughout, including when another remote is named `origin`.
     If there is no remote, complete only the local rename and report that limitation.
   - Fetch the selected remote with `git fetch --prune "$migration_remote"` before evaluating
     branch state. Ensure both relevant branches were fetched even with a restricted refspec.

3. Determine and update the local state.
   - If local `main` already exists, do not blindly rename over it.
   - If local `master` exists and `main` does not, rename it with `git branch -m master main`.
   - If the current branch is `master`, use `git branch -m main`.
   - If neither branch exists locally, inspect remote branches before creating anything.
   - Run `git status --short --branch` after the local change.
   - For local-only scope, report the result and stop here.

4. Prepare and push only for remote migration scope.
   - Verify the fetched remote `master` tip is an ancestor of local `main`. Fetching does not
     advance the local branch. When local `main` is behind, fast-forward it if safe; when histories
     diverge, retain both branches and resolve the history deliberately before proceeding.
   - If remote `main` already exists, verify its history is also preserved by local `main`. Do not
     force-push over it. Missing history or an inconclusive shallow-clone check blocks migration
     until the necessary history is available.
   - Push with `git push -u "$migration_remote" refs/heads/main:refs/heads/main` and verify the
     remote result before changing repository settings.
   - If there is no remote, finish with the local rename and report that no remote update was possible.

5. Update the remote default branch when using GitHub.
   - Prefer GitHub CLI when available and authenticated:
     `gh repo edit "$migration_repo" --default-branch main`.
   - If `gh` lacks permissions, report the required manual step: change the default branch to
     `main` in the repository settings before deleting remote `master`.

6. Handle branch protection and rulesets before cleanup.
   - If `master` has required checks, signed commits, or protection rules, verify whether equivalent
     rules exist for `main`.
   - Confirm effective protection and rulesets for `main`, including required checks and any
     organization rules. An API permission failure is unknown protection state, not evidence that
     there are no rules. Unverified or missing required protections block cleanup.
   - Ensure `main` cannot be deleted or rewritten during cleanup, through effective rules or a
     coordinated write freeze. The old-branch lease below does not lock `main` or GitHub settings.

7. Delete the old remote branch only when cleanup is authorized and all checks pass.
   - Do not infer cleanup authority from a local-only rename.
   - Confirm the remote default branch is `main`, for example with
     `gh repo view "$migration_repo" --json defaultBranchRef`.
   - Immediately before deletion, recheck the destination, default branch, and protections, then
     refresh both remote tips and verify commit containment using the guarded block below.
     Do not substitute an earlier fetch or local `main` for this check.
   - Use the exact checked old-branch commit as a deletion lease. If remote `master` changes after
     the check, the push must fail. Stop on failure; do not retry without the lease or with a newly
     accepted tip until the entire safety check has been repeated.
   - If deletion is blocked by protections or permissions, leave it and explain the blocker.

8. Update local stale refs and tracking after remote migration.
   - Run `git fetch --prune "$migration_remote"`.
   - Verify remote `master` is absent after cleanup and remote `main` still contains the checked
     old tip. Recheck the remote default branch and refresh the selected remote's HEAD reference.
   - Check `git status --short --branch`.
   - Ensure the final branch is `main` and tracks the intended remote branch.

## Guarded Remote Cleanup

Run this block only after step 7's authorization, destination, default-branch, and protection
checks. It requires the selected `migration_remote` shell variable. The subshell exits before
deletion if either branch is missing, fetching fails, or containment cannot be proven.

<!-- test:remote-cleanup -->
```bash
(
  set -eu
  : "${migration_remote:?Set the verified migration remote}"
  git fetch --no-tags "$migration_remote" \
    "+refs/heads/master:refs/remotes/$migration_remote/master" \
    "+refs/heads/main:refs/remotes/$migration_remote/main"
  migration_old_oid=$(git rev-parse --verify "refs/remotes/$migration_remote/master^{commit}")
  migration_main_oid=$(git rev-parse --verify "refs/remotes/$migration_remote/main^{commit}")
  git merge-base --is-ancestor "$migration_old_oid" "$migration_main_oid" || {
    printf '%s\n' 'Remote main does not provably preserve master; leaving master intact.' >&2
    exit 1
  }
  printf 'Checked master %s is contained in main %s\n' "$migration_old_oid" "$migration_main_oid"
  git push --no-follow-tags \
    "--force-with-lease=refs/heads/master:$migration_old_oid" \
    "$migration_remote" :refs/heads/master
)
```

The explicit expected commit follows [Git's lease semantics](https://git-scm.com/docs/git-push).
It guards only the deletion of `master`; it does not authorize force-pushing `main`. If remote
`master` is already absent, skip this block and verify the completed migration. Never weaken
protections to make cleanup succeed.

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
- Never delete it unless its freshly fetched commits are contained in remote `main`, the required
  protections are verified, and an exact-commit lease guards deletion on the selected remote.
- Preserve unrelated local changes.
- Prefer non-interactive commands.
- Report any missing GitHub permissions, branch protection blockers, or absent remotes clearly.
