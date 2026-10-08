# Contributing to Aletheia Framework

Thank you for your interest. This document states the terms under which contributions are accepted. Read it fully before opening a pull request.

---

## 1. Contributor License Agreement (CLA)

All contributions require a signed Contributor License Agreement. The CLA grants the project a perpetual, worldwide, non-exclusive, royalty-free license to use, reproduce, modify, and distribute your contribution, including in commercial offerings.

**Why:** Aletheia's core is MIT. Commercial modules and enterprise support exist alongside it. Without a CLA, contributions create ambiguity about whether commercial use is permitted. The CLA removes that ambiguity for everyone.

The CLA will be published at `CLA.md` in the repository root. Until it is published, contributions are accepted only from the project owner.

## 2. License Boundaries

Aletheia is MIT-licensed. This means:

- The core framework is free to use, modify, and distribute, including commercially.
- You must retain the copyright notice and license text in any redistribution.
- You must not claim the project endorses your derivative.

**WHAXON is AGPL-3.0-or-later.** It is consumed by Aletheia as an **external service** via MCP/ACP. Its source is not linked, compiled into, or combined with Aletheia's codebase. Contributors must not introduce changes that would blur this boundary. If you are unsure whether a change respects the boundary, ask before opening a pull request.

**Model dependencies.** Aletheia does not ship model weights. It integrates with external models via the provider abstraction layer. Contributors must not embed model weights, fine-tuned checkpoints, or datasets with unclear licensing into the repository.

## 3. Trademark Policy

The name "Aletheia Framework" and the casual name "Aletheia" are project marks. See `TRADEMARK.md` for the full policy. In summary:

- You may use the name to refer to the unmodified project.
- You may not use the name to imply endorsement of your derivative, fork, or service.
- Forks must be clearly marked as forks and must not use the project marks as their primary name.

## 4. Contribution Rules

All contributions are subject to the governing rule set. The rules most relevant to contributors:

- **Read the file first.** Every file, before touching it. No editing a file you have not read in full.
- **Design before code.** Any change touching more than two files, introducing a new abstraction, changing a public interface, changing a data format, or changing an authorization boundary requires a design doc in `docs/design/` before implementation.
- **Three-gate discipline.** Every shipped component must pass: functional completeness, evidence attached, no downstream debt.
- **One session, one commit.** A session has a single scope. The commit closes that scope. No half-finished work.
- **Tests pass.** Every commit runs the full test suite. The pre-commit hook enforces this once tests exist.
- **Status honesty.** Every component's status is labeled: *verified under real conditions*, *verified under mock*, *untested*, *known broken with reason*, or *excluded by decision*. "Working" without a qualifier means verified under real conditions.
- **Error messages name the specific failure and the specific fix, or say "unknown."** No generic errors.
- **Every exit code means exactly one thing.**
- **No features added because a competitor has them, because they are easy, or because they would be nice to have.**
- **The never-built list is authoritative.** See `docs/PLAN.md` §6. Proposals to build an item on the list are rejected on sight.

## 5. Pull Request Requirements

A pull request is accepted only if:

1. It has a single, coherent scope, stated in the description.
2. It includes or updates tests for any behavior it changes.
3. It includes or updates documentation for any interface it changes.
4. It does not create downstream debt (see Three-Gate Discipline, Gate 3).
5. It does not touch files outside its stated scope.
6. It does not introduce a dependency without a license audit recorded in the pull request.
7. It does not add a feature to the never-built list.

## 6. What Is Not Accepted

- Features on the never-built list (`docs/PLAN.md` §6).
- Changes that blur the AGPL boundary with WHAXON.
- Changes that bypass the IPP executor boundary.
- Changes that auto-approve scope expansion.
- Changes that send user data anywhere without explicit per-query consent.
- "Cleaner architecture" refactors without a measured gain.
- Cosmetic changes bundled with functional changes.
- Dependency updates bundled with feature work.

## 7. Communication

- **Issues:** bug reports, feature proposals, questions.
- **Discussions:** design conversations, architecture debates, roadmap.
- **Pull requests:** code.

Before opening a pull request for anything larger than a bug fix, open an issue or start a discussion. It is cheaper to align on scope before writing code than after.

## 8. Responsible Use

Aletheia is an advisor. It is not a licensed professional in any field. Users are responsible for verifying any output before acting on it in a professional context. Contributors must not implement features that present Aletheia's output as professional advice.

## 9. Security

Report security issues privately. Do not open a public issue for a vulnerability. Contact the project owner directly. A `SECURITY.md` will be published with the first release.

---

*The framework that reveals what you already know.*
