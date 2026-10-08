# Aletheia Framework — Plan

**Status:** Active
**Stage:** Pre-alpha
**Owner:** andreipath26
**Non-goals:** This document is not a roadmap summary. The roadmap lives in README.md. This document is the operating plan — what gets built, in what order, under what rules, and what will never be built.

---

## 0. Product Claim

Aletheia gives the user a governed, modular, local-first personal AI advisor that indexes their entire digital life, answers with cryptographic provenance, and never executes a professional action without explicit human authorization enforced by signed intent tokens — at the cost of running on the user's own hardware, with cloud use only when the user opts in per query.

---

## 0.1 Standard Formats (R119)

Aletheia supports the following formats natively. Optimization or alternative formats are optional, not required.

**Documents:** PDF, DOCX, TXT, Markdown, HTML, CSV, JSON, YAML.

**Email:** MBOX, EML, IMAP (live sync).

**Images:** PNG, JPG, JPEG, WEBP, TIFF, BMP (with OCR via local vision models).

**Audio:** WAV, MP3, FLAC, OGG, M4A (transcription via local ASR).

**Code:** any plain-text source format, read as UTF-8 text.

**Knowledge artifacts:** Markdown (compiled wiki output), SQLite (local store), JSON Lines (audit log, tamper-evident chain).

**Module interface:** Agent Client Protocol (ACP), JSON-RPC over stdio and HTTP.

**Governance:** Intent Provenance Protocol (IPP), JSON with Ed25519 signatures.

Any new format is added by explicit decision, not by drift. The list above is the boundary.

---

## 1. What This Project Is

Aletheia is the integration layer for a three-project stack: KILN (runtime), WHAXON (domain expert), and Aletheia (memory and advisor). The core is domain-agnostic. Domain expertise plugs in via the Agent Client Protocol (ACP). Governance is enforced structurally via the Intent Provenance Protocol (IPP).

The user is the sovereign. Aletheia advises; the user decides. No professional action executes without explicit human authorization, enforced cryptographically, not by policy.

## 2. Prerequisites

Per the governing rule set (Rule 137), Aletheia work begins only after KILN and WHAXON are shipped — all three gates green. This is currently waived by explicit founder decision for the limited scope of "cement the position on GitHub." No implementation work beyond the skeleton and plan files is permitted until the prerequisite is met.

## 3. Minimum Viable Outcome

The smallest version still worth having shipped:

- IPP SDK: token issuance, validation, Narrowing Invariant, revocation.
- ACP interface: module registration, validation, mock module.
- KILN integration: query a local model, receive a cited answer.
- One working end-to-end demo: index a folder, ask a question, get a cited answer with a signed intent token in the audit log.

Everything else is above the floor.

## 4. Stopping Condition

Aletheia is finished when:

- Milestones 1–4 are shipped (core framework, provider flexibility, domain expert integration, public v0.1.0).
- The ACP module registry is live and third-party modules can be published.
- IPP is submitted to the IETF as a stable reference implementation.

Milestones 5–9 (multimodal, memory/learning, professional deployment, ecosystem, embodiment) are optional extensions. They do not gate the stopping condition.

## 5. What Would Kill This

Named, specific, plausible failure modes:

- **Technical:** IPP's central revocation registry makes air-gapped operation impossible without a local registry, and the local registry is too costly to build and maintain.
- **Dependency:** Agent Client Protocol is abandoned or its maintainers change the license incompatibly.
- **Legal:** The name "Aletheia" collides with an existing trademark in a way that forces a rename after public adoption.
- **Market:** A funded competitor (Hark, Tawn, Fomi) ships a governed, modular, local-first platform before Aletheia reaches v0.1.0.
- **Personal:** Solo operation becomes unsustainable across three-plus projects.

Each risk is reviewed at each portfolio review.

## 6. Never-Built List

Aletheia will never:

- Run unattended against non-consenting targets.
- Auto-approve scope expansion.
- Bypass the IPP executor boundary.
- Change what the LLM may propose without human approval.
- Silently repair corrupted artifacts. Detect, do not fix.
- Add features because a competitor has them.
- Add features because they are easy.
- Become a closed-source product. The core stays MIT.
- Send user data anywhere without explicit, logged, per-query consent.
- Claim compliance without evidence. Every compliance claim traces to a command, a run, or an audit.

## 7. Build Order

Per README.md, Milestones 1–9. The current session's scope is limited to skeleton and plan. Implementation begins at Milestone 1 after KILN and WHAXON are shipped.

## 8. Rules of Engagement

The governing rule set is the master document. This plan is subordinate to it. Where the rule set and this plan disagree, the rule set wins.

## 9. Related Projects

- KILN — runtime. Independent. Consumed via Ollama-compatible API.
- WHAXON — domain expert. Independent. Consumed via MCP/ACP. AGPL boundary documented in CONTRIBUTING.md.
- Aletheia — this project. Integration layer. MIT.

No project assumes another will exist. Each is independently valuable.

## 10. Deferred

- Financial projections: removed from public README by founder decision. Retained in personal notes only.
- Compliance certification (ISO 27001, 42001, SOC 2): deferred until post-funding.
- Full accessibility modules: deferred to Milestone 5.
- Embodiment: deferred to Milestone 9.

---

*This plan is the north star. Keep it current. Keep it clean. It is not a scratchpad.*
