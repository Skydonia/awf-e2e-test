---
name: adaptive-software-change
description: Execute maintainable software changes with deterministic repository context, risk-based verification, measured episodes, and safe connector-first GitHub ticket publication.
---

# Adaptive Software Change

1. Inspect repository instructions and `git status`; preserve unrelated changes.
2. Identify a GitHub issue only from explicit task metadata, `ticket #N`, `issue #N`, or an `/issues/N` URL. Use the authenticated GitHub connector to fetch its canonical identity when available; never infer one.
3. For an issue task, read [GitHub publication](references/github-publication.md) and route each operation independently. The connector is mandatory for every capability it exposes. Never require, install, authenticate, or probe `gh` merely because the task targets GitHub.
4. Use local `git` and repository tools for checkout, diff, patching, tests, and local commits when useful. Do not confuse local source work with GitHub API publication. Prepare or reuse the ticket branch through the connector when remote branch/ref operations are exposed.
5. If one precise capability is missing, continue all covered operations through the connector, use a targeted local fallback only for the missing capability, and request user action only as a last resort. `gh` is allowed solely as `gh_fallback` with an explicit capability reason.
6. Run `awf --mode auto sync <repo>`, retrieve bounded seeded context, recall both memory kinds, and start an episode containing the known issue fields.
7. State acceptance criteria and stop budget. Make the smallest coherent change, then run focused tests and the risk-appropriate quality gates.
8. Synchronize the index, inspect the complete diff, exclude unrelated work, scan for secrets, and validate the intended Conventional Commit.
9. Publish only after blocking gates pass. Use the connector for branch/file/commit/ref/PR operations it covers; create or reuse a PR to the configured base branch and verify the issue relationship.
10. Retrieve GitHub's live default branch immediately before PR composition. Use `Closes #N` only when the PR targets that branch; otherwise use the formal link or reciprocal-comment fallback.
11. Record `github_transport` for publication operations and `gh_fallback_reason` only when a precise connector capability was absent. Do not merge by default.

Stop on completion, exhausted budget, repeated no-progress, failed validation, missing configured base branch, or required authority. Never stop solely because `gh` is absent when the connector covers the task. Never force-push, bypass protection, invent metrics, or auto-promote this skill.
