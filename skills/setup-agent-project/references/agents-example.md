# Example AGENTS.md

This illustrative result for a fictional repository shows project specificity. Follow the
[setup workflow](../SKILL.md) to draft from the target project's evidence.

```md
# Lantern Agent Instructions

## Workspace Boundaries

- `crates/lantern-core` owns packet parsing and must remain independent of terminal and network
  libraries.
- `crates/lantern-cli` owns command-line arguments, terminal output, and calls to remote endpoints.
- Keep parser samples under `fixtures/`; use synthetic addresses and payloads rather than captured
  customer traffic.

## Compatibility

- Preserve the minimum Rust version recorded in `rust-toolchain.toml`.
- Treat the JSON emitted by `lantern inspect --json` as a public interface. Add a fixture test when
  changing its fields or value types.

## Validation

- Run `cargo fmt --check` after Rust edits.
- Run `cargo test --workspace` for behavior changes.
- Run `cargo clippy --workspace --all-targets -- -D warnings` before release-oriented delivery.
```

The example intentionally has no Agent Toolbox section: using the setup skill does not create a
project-specific need to mention Agent Toolbox.
