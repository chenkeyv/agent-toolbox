# Skills

Reusable Codex skills live here.

Use one directory per skill:

```text
skills/
  example-skill/
    SKILL.md
    references/
    scripts/
```

Keep skill descriptions specific enough that Codex can choose the skill
implicitly when a task matches it. Put large references and helper scripts next
to the skill instead of expanding `SKILL.md` unnecessarily.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `agent-toolbox` | Load the reusable specialist-agent team and workflows. |
| `karpathy-guidelines` | Apply compact coding-agent guardrails for simple, surgical, verified changes. |
| `rename-master-to-main` | Safely migrate a Git repository default branch from `master` to `main`. |
