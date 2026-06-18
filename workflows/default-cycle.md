# Default Delivery Workflow

Use this workflow when a request needs coordination across multiple agents.

## 1. Intake

Owner: Lead Orchestrator

- Restate the goal in one or two sentences.
- Identify expected deliverables.
- List constraints, assumptions, and unknowns.
- Select only the agents needed for the task.

Output:

- Goal statement.
- Agent assignment list.
- Initial plan.

## 2. Memory Load

Owner: Lead Orchestrator and assigned specialists

- Read only memory relevant to the current task.
- Treat current user instructions and current files as higher priority than memory.
- Note memory that appears stale, contradictory, or unsupported.
- Decide whether the task needs new memory entries at delivery time.

Output:

- Relevant memory notes.
- Stale or conflicting memory warnings.
- Memory update candidates.

## 3. Product Framing

Owner: Product Strategist

- Define the target user and problem.
- Convert the goal into requirements.
- Identify non-goals and scope boundaries.
- Write acceptance criteria.

Output:

- Requirements.
- Acceptance criteria.
- Scope notes.

## 4. Research

Owner: Research Analyst

Use only when the task depends on current or external information.

- Gather source-backed facts.
- Compare options using the agreed criteria.
- Note uncertainty and confidence level.

Output:

- Research summary.
- Sources.
- Recommendation.

## 5. Design

Owner: Solution Architect

- Inspect the existing system or project context.
- Propose the smallest sound technical approach.
- Identify dependencies, risks, and edge cases.
- Define verification steps.

Output:

- Design notes.
- Implementation plan.
- Verification plan.

## 6. Build

Owner: Implementation Engineer

- Make the scoped changes.
- Follow existing conventions.
- Add or update tests and docs when useful.
- Run relevant checks.

Output:

- Changed files.
- Test results.
- Notes for review.

## 7. Review

Owner: QA Reviewer

- Compare the result to the acceptance criteria.
- Check correctness, edge cases, regressions, and missing tests.
- Prioritize findings by severity.

Output:

- Findings.
- Required fixes or release recommendation.
- Residual risks.

## 8. Memory Update

Owner: Lead Orchestrator and relevant specialist

- Add or revise memory only when the information is reusable beyond the current task.
- Include source, confidence, owner, and updated date.
- Prefer updating an existing entry over creating a duplicate.
- Do not store secrets, credentials, or sensitive personal data.

Output:

- Memory entries added, updated, expired, or intentionally skipped.

## 9. Delivery

Owner: Lead Orchestrator

- Summarize what changed.
- Report verification performed.
- Name memory updates, limitations, and follow-up work.

Output:

- Final delivery summary.
