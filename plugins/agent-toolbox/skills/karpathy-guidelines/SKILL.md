---
name: karpathy-guidelines
description: Coding-agent guardrails inspired by Andrej Karpathy's LLM coding failure-mode notes. Use for non-trivial implementation, refactoring, debugging, or code review tasks where Codex should surface assumptions, keep changes simple and surgical, avoid speculative abstractions, and define verifiable success criteria before iterating.
---

# Karpathy Guidelines

Use this skill as lightweight coding guardrails. Apply it to non-trivial code changes,
reviews, refactors, and debugging tasks. For obvious one-line edits, keep the process
brief and apply the principles silently.

## Operating Rules

1. Clarify risky ambiguity.
   - State assumptions only when they affect implementation, safety, or behavior.
   - Ask a question when ambiguity could lead to the wrong design or destructive action.
   - Present real tradeoffs when there is more than one plausible path.

2. Prefer the smallest useful change.
   - Implement the minimum behavior that satisfies the request.
   - Avoid speculative features, abstractions, configuration, and broad error handling.
   - If the solution grows unexpectedly, pause and simplify before continuing.

3. Keep changes surgical.
   - Touch only files and lines needed for the request.
   - Match existing style, naming, and local helper APIs.
   - Do not refactor adjacent code, rewrite comments, or remove unrelated dead code unless asked.
   - Clean up unused code introduced by the current change.

4. Work from success criteria.
   - Convert vague tasks into observable outcomes.
   - Decide verification before or during implementation.
   - Prefer tests or targeted checks that prove the requested behavior.
   - Report what was verified and what residual risk remains.

## Delivery Checklist

- Assumptions that mattered were stated or resolved.
- The diff is no broader than the request.
- Verification was run, or a clear reason was given.
- Follow-up suggestions are separated from completed work.
