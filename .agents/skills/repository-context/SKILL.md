---
name: repository-context
description: Retrieve a ranked and strictly bounded task-specific context from the Repository Brain. Use before code investigation, planning, review, or implementation when repository evidence is needed without injecting the full codebase.
---

# Repository Context

1. Run `awf --mode auto sync <repo>` to update only changed and deleted files. If cloud state is absent, bootstrap it deterministically first.
2. Form a precise task query containing observed errors, symbols, or component names.
3. Run `awf context "<task>" --repository <repo> --max-tokens <budget> --max-files <limit>`. Add `--seed <path>` for known entry points.
4. Inspect selection reasons and truncation. Search indexed symbols through MCP before reading more files.
5. Expand only the missing branch of evidence. Do not compensate for an imprecise query by loading the repository.
6. Reject stale context when its index revision differs from the current status.
