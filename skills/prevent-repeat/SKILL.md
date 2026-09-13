---
name: prevent-repeat
description: Investigate a missed instruction, incorrect agent behavior, repeated mistake, or disappointing workflow outcome and turn it into a durable prevention. Use when the user asks why an agent did or did not do something, points out behavior that should not recur, says an instruction, skill, or rule was ignored, or asks how to prevent the same mistake. Compare expected and actual behavior using evidence, locate the failure layer, recommend the correct enforcement surface, and verify the fix without inventing hidden reasoning.
---

# Prevent Repeat

Turn corrective feedback into an evidence-backed cause analysis and the smallest durable fix.
Do not stop at an apology or a promise.

## Workflow

1. Establish the incident.
   - Restate the expected behavior, the observed behavior, and the practical impact.
   - Inspect the current request, applicable instructions, relevant skill metadata, tool calls and
     outputs, configuration, repository state, and prior evidence when available.
   - Separate confirmed facts, reasonable inference, and unknowns.
   - Explain observable decision or process failures without claiming access to hidden reasoning.

2. Locate the failure layer.
   - Check requirement clarity: was the expected behavior explicit, discoverable, and applicable?
   - Check instruction application: was the instruction loaded but missed or overridden?
     If loading is not observable, keep both "not loaded" and "loaded but not followed" as possible
     explanations rather than treating either as a confirmed cause.
   - Check routing: should a skill, app, connector, or specialist workflow have triggered?
   - Check sequencing: was a safe or required step attempted too late?
   - Check execution: did sandboxing, permissions, credentials, tools, or external state differ from
     the assumption?
   - Check verification: would a targeted check have caught the mistake before delivery?
   - Check persistence: was the prevention stored in a surface that cannot enforce it?
   - Identify the primary cause and any contributing causes. Do not recommend duplicating an
     instruction as the sole fix when the instruction already existed.

3. Select the prevention surface.

   | Need | Preferred surface |
   | --- | --- |
   | One-task correction | Current prompt or immediate implementation |
   | Personal behavior across repositories | Global `AGENTS.md` or global guidance |
   | Repository-specific convention | Repository or nested `AGENTS.md` |
   | Command permission boundary | Exec-policy rule or permission configuration |
   | Deterministic lifecycle enforcement | Hook |
   | Reusable diagnostic or task procedure | Skill |
   | Product behavior or regression | Test, assertion, linter, or validation script |
   | Durable contextual fact | Project memory, only when explicitly authorized |

   - Prefer the narrowest surface that covers the recurrence risk.
   - Prefer deterministic enforcement for high-risk or mechanically testable behavior.
   - Distinguish a permission rule from an instruction to request that permission; one does not
     necessarily cause the other to run.
   - Do not claim that a skill or prose instruction guarantees future behavior.

4. Act within the user's authority.
   - Diagnose and advise without modifying state when the user asked only for an explanation.
   - Implement the prevention when the user explicitly asks to add, fix, or apply it.
   - Preserve unrelated changes and avoid weakening security merely to remove friction.
   - Ask before making a materially broader change, publishing externally, or persisting sensitive
     information.

5. Verify the prevention.
   - Confirm that the chosen instruction or configuration is loaded in the intended scope.
   - Run the relevant validator, policy check, test, or live behavior probe.
   - Forward-test a realistic recurrence scenario without leaking the expected answer when useful.
   - Check for duplicate or conflicting guidance.
   - State any restart, reinstall, new-thread, or user action required for the fix to take effect.

## Delivery

Report the miss, the evidence-backed cause, the prevention and why it belongs at that layer, the
verification performed, and any residual risk. Lead with accountability when the agent made the
mistake, and avoid unsupported assurances such as "it will never happen again."
