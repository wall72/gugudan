# AGENTS.md
Version: 1.1

## Purpose

This document defines default collaboration rules for AI coding agents
working on general software projects.

These rules are intended to remain reusable across repositories unless a
project-specific AGENTS.md overrides them.

---

## General Principles

- Prefer small and safe changes over large refactoring.
- Preserve existing project structure unless explicitly instructed.
- Fix the root cause when practical, not only the visible symptom.
- Always explain destructive or risky operations before executing them.
- Prefer readability and maintainability over clever code.
- Minimize unnecessary dependencies.
- Keep changes compatible with existing build and deployment pipelines.
- Respect existing architecture and team conventions unless they are clearly wrong.

---

## Git Repository Rules

When initializing a new repository, prefer standard Git defaults and the
repository's existing team conventions.

Example:

```bash
git init
git branch -m master main
```

Rules:

- Always use `main` as the default branch.
- Never force-push unless explicitly requested.
- Prefer small commits with clear commit messages.
- Ask before rewriting git history.
- Preserve existing repository settings when possible.
- Do not change Git identity, hooks, or remotes unless requested.

---

## Commit Style

Prefer conventional and readable commit messages.

Examples:

- feat: add login API
- fix: resolve null pointer issue in user service
- refactor: simplify deployment script
- docs: update README
- chore: cleanup unused configs

---

## Code Style

- Use clear naming.
- Avoid excessive abstraction.
- Prefer explicit code over implicit magic.
- Avoid premature optimization.
- Keep functions and classes focused on a single responsibility.
- Preserve existing formatting and linting conventions.

---

## Change Management

Before making non-trivial changes, briefly clarify:

1. the requested outcome
2. the likely root cause or affected area
3. the smallest safe implementation path
4. the main risk or assumption

Avoid mixing unrelated cleanup with feature or bug-fix work.

---

## Comment Policy

- Use Korean comments when writing comments for business logic explanations.
- Keep comments concise and meaningful.
- Do not add obvious comments.
- Prefer self-explanatory code whenever possible.

Good example:

```python
# 금융권 전문용어 코드값 매핑 처리
```

Bad example:

```python
# 변수에 값을 넣는다
```

---

## Safety Rules

Always ask before:

- deleting files
- changing database schemas
- force-pushing
- modifying production configuration
- executing irreversible shell commands

Avoid modifying these without explicit instruction when they already exist:

- `.env`
- `.env.*`
- `secrets/*`
- `migrations/*`
- lock files

Be especially careful with:

- rm -rf
- git reset --hard
- docker system prune
- recursive chmod/chown
- production DB migration
- authentication and authorization logic
- billing or payment flows

---

## .gitignore Defaults

Prefer adding common development artifacts to `.gitignore`.

Typical entries:

```gitignore
.idea/
.vscode/
node_modules/
dist/
build/
target/
coverage/
.env
*.log
.DS_Store
```

Do not overwrite existing `.gitignore` content unless requested.

---

## Dependency Rules

- Prefer existing libraries already used in the project.
- Add new dependencies only when they provide clear value.
- Prefer mature and well-maintained packages.
- Avoid adding heavy frameworks for small problems.

---

## Python Rules

- Prefer venv-based environments.
- Prefer project-local virtual environments over global environments.
- Respect the dependency tool already used by the repository.

Create virtual environments using:

```bash
python -m venv .venv
```

- Activate `.venv` before running Python commands.
- Prefer pytest for testing.
- Keep requirements minimal.
- Avoid globally installed dependencies.

---

## Java Rules

- Prefer Gradle or Maven standard layouts.
- Preserve enterprise compatibility where possible.
- Avoid unnecessary framework migration without request.
- Be cautious with legacy enterprise environments.

---

## Shell Script Rules

- Prefer safe shell scripting (`set -e` when appropriate).
- Avoid dangerous wildcard deletion.
- Add clear echo messages for important operations.

---

## Testing Rules

- Validate changed behavior with the smallest relevant test scope first.
- Cover the happy path and likely failure path when practical.
- Do not broaden test changes beyond the modified behavior without reason.
- If no automated tests exist, perform the narrowest available manual validation.

---

## Documentation

When creating a new project, prefer generating:

- README.md
- .gitignore
- basic project structure
- development instructions

README should include:

- Overview
- Architecture
- Build
- Run
- Deployment
- Troubleshooting

Update documentation when behavior, setup, configuration, or operational
assumptions change.

---

## AI Agent Behavior

- Think step-by-step before making large changes.
- Show important command sequences before execution.
- Ask for clarification if requirements are ambiguous.
- Prefer incremental modifications over full rewrites.
- Respect existing architecture decisions.
- Validate changes as soon as practical after editing.
- Do not silently make broad architectural changes.