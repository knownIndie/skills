---
name: gh-detailed-commit
description: Inspect changes, prepare a detailed diff-backed Git commit, commit it, and push it to the configured remote without a separate approval pause. Use for autonomous detailed commit-and-push workflows or explanatory Git history. Do not use for read-only Git inspection or pull-request-only work.
---

# Detailed Git commits

Create commits that let the user understand the work later without reopening every diff. Base every claim on the exact files entering the commit.

## Operating modes

- **Direct mode:** Invoking this skill authorizes Codex to inspect the requested work, stage the confirmed files, run relevant checks, create one detailed commit, and push it without asking for a separate commit-message approval.
- **Yeet preparation mode:** When an instruction requires this skill before `github:yeet`, inspect and stage the intended changes, run checks, and prepare the detailed message. Do not commit or push in this mode. Return the message and staged state to the caller, which then loads `github:yeet` for the publishing actions.

Choose the mode from the user request and active instructions. Never let both skills create separate commits or push the same change twice.

## Authorization and scope

- In direct mode, invoking this skill authorizes inspection, staging, validation, one commit, and a normal push of that commit.
- Do not pause for approval of the generated commit subject, body, staged scope, or push when the intended files are clear from the request and task context.
- Treat opening a pull request, amending an existing commit, rewriting history, and force-pushing as separate actions that require an explicit request.
- If the user narrows the request, follow that scope instead of treating the whole worktree as authorized.
- Never force-push unless the user explicitly requests it and confirms the target branch.
- Do not open a pull request unless the user explicitly asks for one.
- In yeet preparation mode, the publishing actions remain governed by the user's request and `github:yeet`.

## Inspect the proposed commit

1. Run `git status -sb` and identify the current branch and worktree state.
2. Inspect staged and unstaged changes with `git diff --cached`, `git diff`, their `--stat` forms, and `--name-status` when useful.
3. Determine which files belong to the requested work. Use the current task context and the diff as evidence.
4. If the worktree contains unrelated or ambiguous changes, stop and ask which files belong in the commit.
5. Stage only the confirmed files. Prefer explicit paths. Do not use `git add -A` unless the user confirmed the entire worktree is in scope.
6. Re-read the staged diff after staging. Generate the commit message only from `git diff --cached` and its statistics.

Do not describe unstaged or untracked work as committed. Do not infer motivations, behavior, or validation that the diff and task context do not establish.

## Run relevant checks

- Run the smallest relevant test, lint, type-check, build, or validation commands for the staged work if they have not already run.
- Record only checks that actually ran and their results.
- If a relevant check fails, report the failure and stop before committing or pushing. Continue only if the user explicitly approves proceeding with the known failure.

## Write the message

Use a concise, outcome-focused subject. Prefer 72 characters or fewer when accuracy permits. Name the functionality or behavior delivered instead of the act of editing files.

Avoid vague subjects such as:

- `Made changes`
- `Updated files`
- `Various fixes`
- `Work in progress`
- `Changes to project`

Write a detailed body using only the sections that add useful information:

```text
<Outcome-focused subject>

Summary
- <Functional or behavioral change>
- <Important implementation or developer-facing change>

Change statistics
- <N> files changed
- <N> insertions
- <N> deletions
- <N> new files, when applicable

Files changed
- path/to/file
  <What changed in this file and how it contributes to the result.>

New files
- path/to/new-file
  <What the new file is responsible for.>

Renamed or deleted files
- old/path -> new/path
  <Why the move matters, when established by the diff or task context.>

Validation
- <Command>: <result>

Notes
- <Relevant limitation, migration, compatibility detail, or deliberate deferral.>
```

Follow these content rules:

- Explain the functional outcome before implementation details.
- Include exact staged-diff statistics when available.
- Account for every committed file. Give each meaningful source, configuration, test, migration, or documentation file a short, specific explanation.
- Put created files in `New files` rather than duplicating them under `Files changed`.
- Include renamed and deleted files when present.
- Group generated or mechanical files only when individual explanations would add no information. State what caused the group to change, such as a dependency update or formatter run.
- Describe tests beside the functionality they verify when that relationship matters.
- Keep each file explanation to one or two sentences unless the change is unusually complex.
- Do not pad the body with generic phrases or restate filenames without explaining their role.
- Do not list a validation command unless it ran during this task or the current session has direct evidence that it ran against the same staged change.

## Commit and push

1. Confirm the staged diff still matches the files used to generate the message.
2. In direct mode, commit immediately with the generated subject and body and capture the commit SHA.
3. Push the current branch to its configured upstream. If no upstream exists but exactly one suitable remote is configured, push with `git push -u <remote> <branch>`.
4. If the remote or target branch is ambiguous, stop and ask the user. Do not guess between multiple remotes.
5. If the push is rejected, report the error. Do not force-push, rewrite history, merge, or rebase unless the user requests the next action.
6. In yeet preparation mode, do not run `git commit` or `git push`. Provide `github:yeet` with the generated subject, body, staged file list, check results, branch, and intended remote.
7. When `github:yeet` takes over, the detailed subject and body replace its default terse commit-message convention. It must not regenerate or shorten the message.
8. Never silently amend an existing commit or rewrite remote history.

## Report the result

In direct mode, report:

- Branch and remote.
- Commit SHA.
- Final subject.
- Number of committed files.
- Validation results.
- Push result.
- Anything deliberately excluded or still uncommitted.

In yeet preparation mode, report that the message and staged scope are ready for the `github:yeet` handoff. The final publishing report comes from `github:yeet`.

## Invocation boundary

This skill runs when Codex handles the commit workflow. A Git command or desktop button that bypasses the Codex agent cannot invoke a skill. To trigger the autonomous commit-and-push workflow, invoke `$gh-detailed-commit`. An active publishing instruction may route `$github:yeet` through this skill first.
