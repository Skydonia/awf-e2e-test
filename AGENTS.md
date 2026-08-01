# Agent instructions

## Repository profile

- Languages: python
- Base branch: `develop` (configurable in `.agent-workflow.json`)
- Repository Brain state and metrics stay outside the repository.
- Use the repository skills `repository-context` and `adaptive-software-change` when available.

## Canonical commands

- `build`: `python -m build`
- `test`: `python -m pytest`

## Change rules

- Keep changes focused and preserve product behavior unless the task explicitly changes it.
- Read nested `AGENTS.md` files when present and add one only for genuinely different subtree rules.
- Never read, index, edit, or commit generated, vendored, or secret paths: `.env`, `.env.local`, `.pytest_cache`, `.venv`, `__pycache__`, `build`, `coverage`, `credentials.json`, `dist`, `id_ed25519`, `id_rsa`, `node_modules`, `vendor`, `venv`.
- Run the relevant commands above, inspect the diff, and use an atomic Conventional Commit.
