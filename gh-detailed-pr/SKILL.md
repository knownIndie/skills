---
name: gh-detailed-pr
description: Inspect a Git worktree, create and push a detailed diff-backed commit, then open a detailed GitHub pull request. Use when the user wants one autonomous commit-and-PR workflow. Do not use for commit-only, read-only Git inspection, or PR review work.
---

# Detailed Git pull requests

Turn the requested work into one documented commit and one GitHub pull request. This skill is self-contained. Do not invoke or depend on `gh-detailed-commit` or another publishing skill.

## Authorization and limits

Invoking this skill authorizes Codex to inspect the requested work, stage the files that clearly belong to it, run relevant checks, create one commit, push the current branch, and create one pull request. Do not pause for approval of the generated commit message, staged scope, push, PR title, or PR body when the intended work and targets are clear.

The invocation does not authorize force-pushing, amending commits, rebasing, merging, rewriting history, creating extra commits, or modifying an existing pull request. Do not perform those actions unless the user explicitly requests them.

Stop and ask for direction when:

- unrelated or ambiguous changes make the intended commit scope unclear;
- the current branch is the target repository's default branch;
- the remote, head branch, or base branch cannot be determined without guessing;
- a relevant validation command fails;
- the push is rejected;
- GitHub authentication is unavailable; or
- the current branch already has an open pull request.

Never bypass a failed check, use a destructive Git command, or force a remote update on your own.

## Inspect and stage the work

1. Run `git status -sb` and identify the current branch, upstream, and worktree state.
2. Inspect staged and unstaged changes with `git diff --cached`, `git diff`, their `--stat` forms, and `--name-status` when useful.
3. Inspect untracked files that may belong to the requested work without exposing secrets or unrelated contents.
4. Determine the intended files from the user request, current task context, and exact diff.
5. Stage only those files using explicit paths. Do not use `git add -A` unless the entire worktree is unambiguously in scope.
6. Re-read `git diff --cached`, its statistics, and its name status. Base every commit claim on this staged state.

Do not include unstaged or untracked work in the commit description. Do not infer behavior, motivation, or validation that the diff and task context do not establish.

## Validate the staged change

Run the smallest relevant tests, lint, type checks, builds, or artifact validation for the staged work. Record only commands that ran against the same staged state and their actual results.

If a check changes tracked files, inspect those changes and include them only when they are expected outputs of the requested work. Re-stage as needed and re-read the staged diff before writing the commit message.

## Write and create the commit

Use a concise, outcome-focused subject, preferably no longer than 72 characters. Avoid vague subjects such as `Update files`, `Various fixes`, or `Work in progress`.

Use only the body sections that add information:

```text
<Outcome-focused subject>

Summary
- <Functional or behavioral result>
- <Important implementation or developer-facing change>

Change statistics
- <N> files changed
- <N> insertions
- <N> deletions
- <N> new files, when applicable

Files changed
- path/to/file
  <What changed and how it contributes to the result.>

New files
- path/to/new-file
  <What the file is responsible for.>

Renamed or deleted files
- old/path -> new/path
  <Why the move matters, when established by the evidence.>

Validation
- <Command>: <result>

Notes
- <Known limitation, compatibility detail, migration, or deliberate deferral.>
```

Account for every staged file. Put created files under `New files`. Group generated or mechanical files only when separate explanations add no value, and state what caused the group to change.

Confirm that the staged diff still matches the message, then create the commit and capture its SHA. Never amend an existing commit.

## Push the branch

Push the current branch to its configured upstream. When no upstream exists and exactly one suitable remote is configured, use `git push -u <remote> <branch>`.

Do not push directly to the repository's default branch. If the branch or remote is ambiguous, stop instead of guessing. If the push fails, report the error and do not open the pull request.

## Inspect the complete pull request diff

Determine the base branch from the remote's default branch unless the user named a base. Fetch enough remote state to compare accurately when safe and needed.

Inspect the complete proposed PR, not only the new commit:

- commits in `<base>..HEAD`;
- `git diff <base>...HEAD`;
- diff statistics and name status; and
- relevant repository pull-request templates or contribution instructions.

The PR description must account for pre-existing branch commits and changes when they are part of the comparison. Do not present commit-only statistics as PR-wide statistics.

## Write and create the pull request

Use an outcome-focused title that describes the whole branch change. Write the body from the complete base-to-head comparison, repository instructions, and validation evidence.

Use only useful sections:

```text
## Summary

- <User-visible or functional outcome>
- <Important implementation detail>

## Changes

- <Logical change with relevant file or component context>

## Change statistics

- <N> files changed
- <N> insertions
- <N> deletions

## Validation

- `<command>`: <result>

## Notes

- <Compatibility detail, limitation, rollout concern, or deliberate deferral>
```

Honor the repository's PR template when present. Preserve required headings, checklists, issue references, and contributor declarations. Do not claim tests, screenshots, issue closure, compatibility, or deployment results without evidence.

Create a ready-for-review pull request with `gh pr create`. Create a draft only when the user asks for one. If `gh pr create` reports an existing PR for the branch, stop and return its URL without editing it.

## Report the result

Report:

- source and base branches;
- remote;
- commit SHA and subject;
- number of committed files;
- validation commands and results;
- push result;
- final PR title and URL; and
- excluded or still-uncommitted work.

## Invocation boundary

This workflow runs only when Codex handles it. A Git command or desktop button that bypasses Codex cannot invoke the skill. Invoke `$gh-detailed-pr` to trigger the autonomous commit, push, and pull-request workflow.
