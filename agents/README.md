# Agents

Each agent file is a reusable role profile. Keep these profiles specific enough to guide behavior,
but portable enough to use in different agent runtimes.

Recommended structure:

- Front matter with `id`, `name`, and `type`.
- Mission.
- Use when.
- Core responsibilities.
- Inputs and outputs.
- System prompt.

When adding a new agent, also update `../team.yaml` and the roster in `../README.md`.

