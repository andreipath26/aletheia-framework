# Aletheia Framework — Resume From Cold

**Read this first. It takes under five minutes.**

**Status:** Pre-alpha
**Stage:** Skeleton and plan committed. No implementation.
**Last commit:** (populated at commit time)
**Current phase:** Milestone 1 — Governance Foundation (not started)
**Next unit of work:** IPP SDK — token schema, signing, validation, Narrowing Invariant

---

## What This Project Is

Aletheia is the integration layer for a three-project stack: KILN (runtime), WHAXON (domain expert), and Aletheia (memory and advisor). The core is domain-agnostic. Domain expertise plugs in via the Agent Client Protocol (ACP). Governance is enforced structurally via the Intent Provenance Protocol (IPP).

The user is the sovereign. Aletheia advises; the user decides. No professional action executes without explicit human authorization, enforced cryptographically, not by policy.

## Where the Project Lives

- Local: `/home/andreipath/Desktop/ALETHEIA FRAMEWORK/`
- Remote: `https://github.com/andreipath26/aletheia-framework`

## What Is In Flight

Nothing. This is a clean start after the skeleton commit.

## What Was In Flight Before

N/A. First session after skeleton.

## What To Read First

1. `docs/PLAN.md` — the operating plan.
2. `README.md` — the public vision and roadmap.
3. The master rule set — governs how work is done.

## What To Do Next

1. Confirm KILN and WHAXON are shipped (all three gates green). If not, this project stays paused per Rule 137.
2. If shipped: begin Milestone 1, IPP SDK. Design doc first (`docs/design/ipp-sdk.md`), then implementation.
3. Read the IETF draft `draft-haberkamp-ipp-01` before writing any IPP code.

## Current Blockers

- KILN and WHAXON not yet shipped. Waiver in effect for skeleton only. Implementation blocked until prerequisite met.

## Related Projects

- KILN: `https://github.com/andreipath26/KILN`
- WHAXON: `https://github.com/andreipath26/WHAXON`

## Project Rules (Quick Reference)

- Read the file first. Every file, before touching it.
- Design first, code after. Any change over 2 files or new abstraction.
- Three-gate discipline: functional completeness, evidence attached, no downstream debt.
- One session, one commit. Full test suite before push.
- Never-built list is authoritative. See `docs/PLAN.md` §6.
- The user is the sovereign. Aletheia advises.

---

*If this file is stale, the first action of the session is to update it.*
