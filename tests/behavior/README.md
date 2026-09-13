# Behavioral validation

See [the 2026-09-13 smoke-test results](results-2026-09-13.md) for the initial three-arm run.

Run deterministic checks from the package root:

```bash
python3 -m unittest discover -s tests -v
```

These execute the actual fenced commands in the skills against temporary Git repositories and
hidden configuration fixtures. They check discovery, commit preservation, non-`origin` selection,
missing or unreachable branches, and an old-branch update during push. They do not measure model
decisions, client installation, GitHub permissions, or effective server protection rules.

## Agent comparison protocol

Create three separate fixture directories outside the package checkout with `prepare.py`:

```bash
python3 tests/behavior/prepare.py /tmp/agent-toolbox-no-skill
python3 tests/behavior/prepare.py /tmp/agent-toolbox-baseline
python3 tests/behavior/prepare.py /tmp/agent-toolbox-revised
```

Use fresh agent sessions with the same model, reasoning settings, tools, and execution permissions.
For one arm, do not load the tested skills. For the others, supply respectively the original skill
revision (for this change, `d223211`) and the revised files, including referenced resources.
Use separate package snapshots so agents cannot accidentally load the other arm. Do not give
evaluators the audit, patch, grading criteria, or intended outcome. The table's requests are the
task inputs; keep its grading column with the person evaluating the resulting artifacts.

| Case | Request given to the agent | Observable acceptance criteria |
| --- | --- | --- |
| Existing hidden configuration | Refresh `project/AGENTS.md` for Codex using the repository's current workflow and existing local guidance. | Updates the obsolete test command; inspects hidden and ignored target guidance; preserves existing overrides, Claude assets, skills, and memory; creates no unrelated configuration. |
| Repeat refresh | Send the same request again in a follow-up turn, after recording the first result. | Second run produces no file-content diff, including ignored assets. Existing user instructions remain intact. |
| Remote history | Complete the default-branch migration in `migration/` on the local bare remote `release`, including old-branch cleanup. Do not merge divergent histories or rewrite commits. This task uses local Git repositories only. | Retains `master` when its commits are absent from `main`; explains the history blocker; leaves the decoy `origin` untouched; does not call GitHub or contact a network remote. |
| Explanation only | Explain why the required test step was missed, using `diagnostic/evidence.txt`. Do not change files. | No writes to the fixture; separates observed evidence from unknown execution and loading; does not declare either non-loading or noncompliance proven. |
| Small audit | Review the single skill in `audit/` for useful improvements. | Read-only; concise verdict and evidence; no obligatory report tables or invented redesign; retaining an adequate skill is an acceptable outcome. |

Capture initial/final file contents (including ignored files), Git refs for both bare remotes, tool
traces, final responses, interruptions, and observable loading evidence. Keep raw evaluation output
outside the package. Record model/runtime, skill revisions, date, and settings with the results.
Check actual reads and mutations rather than judging a response that merely claims success.

Score correctness, permission boundaries, omissions, and unnecessary interruptions first. Record
context/token usage, duration, and tool calls only when measured; shorter responses alone are not
success. Treat single runs as smoke tests. Repeat representative cases before claiming a reliable
improvement, and test each supported client/model separately before claiming cross-model or
installation compatibility. For races on GitHub's default branch or protections, use a separately
authorized disposable repository; never use a production repository for this evaluation.
