---
name: adaptive-software-change
description: Execute maintainable software changes with deterministic repository context, risk-based verification, measured episodes, and safe connector-first GitHub ticket publication.
---

# Adaptive Software Change

1. Inspect repository instructions and `git status`; preserve unrelated changes.
2. Identify a GitHub issue only from explicit task metadata, `ticket #N`, `issue #N`, or an `/issues/N` URL. Fetch its canonical identity with the authenticated GitHub connector; never infer one. Prepare or reuse the ticket branch before editing and never work directly on the configured base branch.
3. Read the GitHub publication reference for issue work. The connector is mandatory for every GitHub capability it exposes. Never require, install, authenticate, or probe `gh` merely because the task targets GitHub; use it only as a targeted fallback for one demonstrably missing connector capability.
4. Run `awf --mode auto sync <repo>`, retrieve strictly bounded task context with `awf context`, recall relevant positive and negative memory, and start an episode containing the issue, branch, and base-branch metadata.
5. State acceptance criteria and the stop budget, then make the smallest coherent change. Do not broaden the file scope to compensate for uncertain context.
6. Run each detected canonical validation through `python -m agentic_workflow.validation "<canonical command>" --repository <repo>`. This deterministic runner classifies failures and, only for a declared recoverable environment failure, executes `.agent/setup-project.sh` once and retries the exact same command within the retry budget. Never replace a runnable canonical gate with an ad-hoc manual check.
7. A `functional_failure` or `environment_failure_blocking` is a blocking validation result. Stop before publication with its precise cause. Do not install arbitrary tools inferred from free-form error text.
8. After validations pass, synchronize the Repository Brain again, inspect the complete diff, preserve unrelated work, scan for secrets, and verify the staged files and intended Conventional Commit.
9. For a GitHub ticket, local implementation is never completion. Create the Conventional Commit with `Refs #N`, push the ticket branch, create or reuse the PR against the configured base branch, and verify the issue relationship. Retrieve GitHub's live default branch immediately before PR composition and use `Closes #N` only when the PR base is that default branch.
10. Record GitHub publication metrics on the episode before finishing it, including commit count, push, PR number/URL, and issue-link verification. Then call `awf episode finish <episode-id> --outcome success ...`. AWF must reject `success` for an issue episode while validation has failed or commit/push/PR/link requirements are incomplete.
11. Report separate `implementation_status`, `validation_status`, `publication_status`, and `stop_reason`. Use `completed / passed / pr_created|pr_reused / completed` only after the verified PR exists; otherwise report `blocked` or `incomplete`.
12. Never stop solely because `gh` is absent when the connector covers the task. Never merge by default, never force-push, never bypass protection, and never invent absent metrics.
