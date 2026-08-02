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
- Run canonical validation only through `python -m agentic_workflow.validation --all --repository .`; do not invoke a canonical gate directly or search for another venv/interpreter when a declared tool is missing.
- Let the deterministic runner execute `.agent/setup-project.sh` only for a recoverable environment failure and retry the exact failed command within its bounded budget.
- For ticket work, obtain the branch name from `awf github branch`; never invent a `feature/` or other branch alias.
- Run the relevant commands above, inspect the diff, and use an atomic Conventional Commit.
