
# Aletheia Framework

**The framework that reveals what you already know.**

Aletheia (ἀλήθεια) is the Greek word for truth as *unconcealment*—the act of revealing what is hidden. That is what this framework does.

Aletheia is a privacy-first, modular framework for building personal AI systems that index, remember, reason over, and advise on your entire digital life. It runs locally by default, scales to the cloud when you choose, and never sends your data anywhere without explicit consent.

**Aletheia is an advisor, not a professional.** The user is the sovereign. Aletheia gathers intelligence, organizes knowledge, challenges assumptions, and proposes actions—but never executes a professional decision without explicit human authorization. This is enforced structurally through the Intent Provenance Protocol (IPP).

---

## Core Principles

1. **Local by default.** Your data stays on your hardware unless you explicitly choose otherwise.
2. **Provenance always.** Every answer cites its source. Nothing is asserted without evidence.
3. **Modular architecture.** Every capability is a pluggable module (Agent Client Protocol).
4. **Governance-native.** Every action carries a signed intent token (Intent Provenance Protocol).
5. **User-as-sovereign.** Aletheia proposes; you dispose.
6. **Provider-agnostic.** Local (KILN, Ollama) or cloud (Gemini, DeepSeek, Mistral, OpenAI, Anthropic).
7. **Accessibility-first.** Multimodal interaction is default. Disabled users are not an afterthought.
8. **Self-evolving.** Learns from interactions, anticipates needs, improves over time.
9. **Open-core.** MIT for the core framework. Commercial modules and support available.
10. **Fail-safe.** No irreversible actions without human approval. Audit trails everywhere.

---

## Architecture

Three layers, composable, user-defined:

| Layer | Role | Reference Implementation |
|-------|------|--------------------------|
| **Runtime** | Fast, local inference | [KILN](https://github.com/andreipath26/KILN) |
| **Domain Expert** | Deterministic, auditable expertise | [WHAXON](https://github.com/andreipath26/WHAXON) |
| **Memory & Advisor** | Index, remember, reason, advise | Aletheia |

The core knows nothing about any specific domain. It ingests, indexes, retrieves, reasons, cites, and advises. Domain knowledge comes from modules. The integration contract is the Agent Client Protocol (ACP). Users compose their own stack.



+-------------------------------------------------------------+

|                      Aletheia Core                          |

|  (Memory, Provenance, Reasoning, Proactive Advisory,        |

|   Routing, Governance, Provider Abstraction)                |
+--------------------------+----------------------------------+

+-------------------+               +-------------------+

|  KILN (Runtime)   |               | WHAXON (Domain)   |

|  - Local, fast    |               | - Deterministic   |

|  - Per-layer      |               | - Cross-tool      |

|  - No GPU needed  |               | - Hard guardrails |
+-------------------+               +-------------------+




## The Governance Model

Aletheia is the Round Table, not the King. The user is the sovereign. Aletheia gathers intelligence, organizes knowledge, challenges assumptions, and proposes actions—but never executes a professional decision without explicit human authorization.

This is enforced structurally through the **Intent Provenance Protocol (IPP)**:

- Every action carries a signed intent token tracing back to a human principal.
- The Narrowing Invariant prevents any sub-agent from expanding its own authority.
- Every output carries provenance: source, timestamp, and confidence.

| Property | Meaning |
|----------|---------|
| **Lineage** | Every action traceable through unbroken cryptographic signatures to a human Principal |
| **Boundedness** | Every token carries explicit, machine-readable constraints on authorized scope |
| **Non-Repudiation** | Every token cryptographically signed; signer cannot deny issuance |
| **Interoperability** | Framework-agnostic, cloud-agnostic, jurisdiction-agnostic |

**The Narrowing Invariant:** A Derived Token MUST be strictly less than or equal to its Parent Token in every dimension of scope, delegation depth, and expiry. No sub-agent can ever expand its own authority.

---

## Legal & Compliance Layer

The Legal & Compliance Layer runs through all milestones. It is designed to be **free to implement now**, with formal certification deferred to post-funding.

| Area | What We Do Now | What We Defer |
|------|----------------|---------------|
| **License Compliance** | WHAXON consumed as external service (MCP/ACP), not linked. Documented in CONTRIBUTING.md. | — |
| **GDPR** | Local execution as default. Cloud is explicit user choice. Chapter V avoided. | — |
| **EU AI Act** | Model classification memos. Provider-drift checks. Transparency evidence. | Formal conformity assessment |
| **Record-Keeping** | Tamper-evident log. Retention controls. | — |
| **US State Laws** | Map users. Document obligations. AI system inventory. | — |
| **IP / FTO** | Full dependency license audit. CLA. Contractor agreements. | — |
| **Industry Standards** | OWASP LLM Top 10 mapping. | ISO 27001, ISO 42001, SOC 2 (investor-funded) |
| **Trust Center** | — | Public security page (Milestone 7) |

**Strategy:** Design for compliance now. Certify after funding. The architecture is already 70% of what auditors check.

---

## Roadmap

### Governing Principle

**Aggressive, forward-only, no half-done components.**

Every component ships production-ready: tested, documented, integrated. Nothing gets revisited. The timeline extends if needed. The quality standard never compromises.

**Prerequisite:** KILN and WHAXON are finished and shipped before Aletheia work begins. Full attention, no divided focus.

### The Three-Gate Discipline

Every milestone must pass three gates before the next begins:

| Gate | Requirement |
|------|-------------|
| **Gate 1: Functional Completeness** | Works out of the box. No hardcoded paths, no untested edge cases, no missing error handling. |
| **Gate 2: Evidence Attached** | Unit tests pass. Integration tests pass. Behavior verified under real conditions. Evidence is traceable. |
| **Gate 3: No Downstream Debt** | Does not create work for the next phase. Known limitations are explicit boundaries, not defects. |

---

### Milestone 1: Governance Foundation

**Goal:** Establish the constitutional layer and local core before building features.

**Deliverable:** IPP SDK, ACP interface, tamper-evident log, KILN integration.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Intent Provenance Protocol (IPP)** | Full SDK from IETF draft. Token schema, Narrowing Invariant, local revocation registry for air-gapped mode. | Document IPP as governance foundation. |
| **Agent Client Protocol (ACP)** | Adopt as module interface standard. Adapter pattern, validation layer, mock module for testing. | Document WHAXON as external service (MCP/ACP), not linked. |
| **Tamper-evident log** | Cryptographic hash chain. Each entry linked to previous. Fingerprint of latest entry stored separately. | Aligns with AI Act Article 12 and GDPR Articles 5, 32. |
| **Retention policy** | Configurable: how long logs are kept, when removed. | Aligns with GDPR storage limitation. |
| **KILN API integration** | Client, error handling, retry logic, streaming verification. | Model classification memo for KILN. |
| **Local ingestion** | Stoa or Last Archive for knowledge compilation. | Document local execution as GDPR default. |
| **CLA** | Contributor License Agreement. | IP ownership clarity. |
| **License policy** | Document in CONTRIBUTING.md. | AGPL compliance for WHAXON (external service, not linked). |
| **OWASP LLM Top 10 mapping** | Document mitigations as you build. | Security baseline. |
| **AI system inventory** | Track all systems: role, supplier, transparency category. | EU AI Act and US state compliance. |

**Definition of Done:** IPP tokens issue, validate, and revoke. ACP modules register and communicate. Log chain is verifiable. KILN answers queries. All tests pass. All documented.

---

### Milestone 2: Runtime & Provider Flexibility

**Goal:** Unified interface for local and cloud providers. User chooses their counsel.

**Deliverable:** Provider abstraction layer. All providers tested.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Provider abstraction layer** | Unified interface across KILN, Ollama, llama.cpp, OpenAI, Anthropic, Gemini, DeepSeek, Mistral. | — |
| **Provider adapters** | One per provider. Test against live API. Verify fallback logic. | Model classification memos for all providers. |
| **Provider-drift check** | Document for each model: Did you change purpose? Fine-tune? Market under own name? | EU AI Act provider territory assessment. |
| **GDPR transfer documentation** | Local execution avoids Chapter V. Cloud is explicit user choice. | GDPR Article 25 compliance. |
| **US state mapping** | Texas TRAIGA, Colorado AI Act, California ADMT, New York RAISE Act. | Document obligations per state. |
| **Model classification memos** | One per provider: license, classification, failure contact. | EU AI Act compliance. |

**Definition of Done:** User can switch providers mid-session. Local providers work offline. Cloud providers work with valid API keys. Fallback logic verified. All memos filed.

---

### Milestone 3: Domain Expert Integration

**Goal:** Wire WHAXON as first domain module via MCP/ACP.

**Deliverable:** WHAXON integrated. Governance enforced.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **WHAXON MCP server** | Expose catalog, scope enforcement, session management. | Document as external service. |
| **ACP integration with WHAXON** | WHAXON becomes ACP-compatible agent. | License boundary documented. |
| **Governance enforcement** | Every WHAXON action validates IPP token. Scope violation blocked. | Compliance evidence for AI Act. |
| **Live testing** | Test against real targets. Verify audit chain. | — |

**Definition of Done:** User says "scan this target." Aletheia queues, validates scope via IPP, executes through WHAXON. Audit trail complete. All tested.

---

### Milestone 4: Provider Routing & Release

**Goal:** Sensitivity-based routing. Public v0.1.0 release.

**Deliverable:** Routing logic, RBAC, Trust Center, full documentation, GitHub release.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Sensitivity classification (S1/S2/S3)** | Classify data by sensitivity. Route accordingly. | Align with EU AI Act transparency. |
| **Routing logic** | Local-only for S3. Redact for S2. Cloud allowed for S1. | GDPR and AI Act compliance. |
| **Sensitive data leak testing** | Verify S3 never reaches cloud. | — |
| **Multi-user RBAC (basic)** | Owner, Admin, Analyst, Reviewer. | Access control documentation for ISO 27001. |
| **Audit trail verification** | End-to-end chain integrity. | AI Act Article 12 compliance. |
| **Trust Center page** | Public security documentation. | Enterprise deal accelerator. |
| **Full documentation suite** | README, CONTRIBUTING, ARCHITECTURE, GOVERNANCE, COMPLIANCE. | — |
| **GitHub release v0.1.0** | Tag, release notes, changelog. | — |

**Definition of Done:** Framework is public. Documentation complete. All tests pass. Demo works end-to-end. No stubs.

---

### Milestone 5: Multimodal Input

**Goal:** Voice interaction, image understanding, screen capture.

**Deliverable:** Voice pipeline, screen OCR, multimodal input working.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Voice pipeline** | chuchote (wake-word -> VAD -> STT -> LLM -> TTS). Interrupt support. Memory across restarts. | Document audio processing for privacy. |
| **Screen OCR** | owocr (clipboard, screen region, Unix socket). Real-time text extraction. | Document data handling. |
| **Multimodal routing** | Voice and screen inputs route through same governance layer. | — |
| **FTO inventory** | Full dependency license audit. | Identify any AGPL, GPL, or bespoke licenses. |

**Definition of Done:** Voice commands work. Screen OCR works. All inputs governed by IPP. FTO complete.

---

### Milestone 6: Memory & Learning

**Goal:** AI learns from interactions, predicts needs, evolves.

**Deliverable:** Memory layer, preference learning, proactive suggestions.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Memory layer** | Soma-memory (local-first, 22.6x smaller disk, 3.2x faster store). | Document data retention. |
| **Preference learning** | Track IPP token approvals/rejections. Confidence adjustment based on user decisions. | Document as user consent mechanism. |
| **Proactive suggestions** | Pattern-based: "You usually scan before client meetings." | Document as advisory, not autonomous. |
| **Fine-tuning pipeline** | Troy/Lamark for local SFT/DPO. Personal style adaptation. | Model provenance documentation. |

**Definition of Done:** System anticipates needs based on past behavior. Every suggestion carries provenance. Retrieval quality verified. False positive rate measured.

---

### Milestone 7: Professional Deployment

**Goal:** Local server + remote access for professional teams.

**Deliverable:** RBAC, edge relays, audit trails, compliance prep.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Full RBAC** | Owner, Admin, Analyst, Reviewer, Client-Viewer. | Access control documentation for ISO 27001. |
| **Edge relay deployment** | Lightweight VPS relays (DigitalOcean, Linode). Persistent WebSocket connections. | Data transfer documentation. |
| **Per-department policies** | Legal uses local-only. Marketing uses cloud-allowed. | GDPR and AI Act compliance. |
| **Audit trail (immutable)** | Full IPP provenance chain. | AI Act Article 12 compliance. |
| **Trust Center (full)** | Certifications status, data handling, AI practices, security controls. | Enterprise deal accelerator. |
| **ISO 27001 prep** | Documentation, gap analysis. | Investor-funded certification. |
| **ISO 42001 prep** | Documentation, gap analysis. | Investor-funded certification. |
| **SOC 2 Type 1 prep** | Documentation, gap analysis. | Investor-funded certification. |

**Definition of Done:** Law firm deploys Aletheia on local server. 20 employees get secure remote access with role-based permissions. Compliance documentation ready for audit.

---

### Milestone 8: Module Ecosystem

**Goal:** Open platform for third-party modules.

**Deliverable:** ACP registry, domain templates, commercial support.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **ACP module registry** | Any ACP-compatible agent becomes Aletheia module. | Module licensing framework. |
| **Domain templates** | Legal, medical, accounting, education, security. | Domain-specific compliance. |
| **Commercial module support** | Third parties publish paid modules. Platform takes cut. | Revenue sharing agreements. |
| **SOC 2 Type 2** | Complete certification. | Annual renewal. |
| **EU AI Act readiness** | Full compliance if serving EU. | Market entry requirement. |

**Definition of Done:** Marketplace where doctor installs "Clinical Guidelines" module and lawyer installs "Contract Analysis" module. Full compliance achieved.

---

### Milestone 9: Embodiment

**Goal:** Physical embodiment for home, elder care, companionship.

**Deliverable:** Home agent, companion robot, spatial intelligence.

| Component | Implementation | Legal/Compliance Action |
|-----------|---------------|------------------------|
| **Home agent** | Donutbot-style: fall detection, medication reminders, proactive video calls. | Medical device regulations review. |
| **Companion robot** | Bubbo 1-style: proactive intelligence, emotion sensing. | Privacy impact assessment. |
| **Spatial intelligence** | ROS2 integration. | Safety certification. |

**Definition of Done:** Physical presence extending Aletheia beyond screens. Regulatory review complete.

---

### Cumulative Roadmap

| Milestone | Duration | Cumulative |
|-----------|----------|------------|
| **M1: Governance Foundation** | 3-5 weeks | 5 weeks |
| **M2: Runtime & Provider Flexibility** | 3-4 weeks | 9 weeks |
| **M3: Domain Expert Integration** | 3-4 weeks | 13 weeks |
| **M4: Provider Routing & Release** | 4-5 weeks | 18 weeks |
| **M5: Multimodal Input** | 4-6 weeks | 24 weeks |
| **M6: Memory & Learning** | 5-7 weeks | 31 weeks |
| **M7: Professional Deployment** | 4-6 weeks | 37 weeks |
| **M8: Module Ecosystem** | 6-8 weeks | 45 weeks |
| **M9: Embodiment** | 12-16 weeks | 61 weeks |

**Core framework (M1-M4) is complete and public in 13-18 weeks.**

**Full platform (M1-M8) is complete in ~11 months.**

**Embodiment (M9) adds 3-4 months.**

---

## Cross-Cutting Infrastructure

- **MCP-Native:** Everything exposes MCP.
- **Memory Backends:** Mem0, Letta for stateful agents.
- **Context Engineering:** Pyramid framework.
- **Privacy & Governance:** Federated Learning, Contextual Integrity enforcement.
- **Offline Multimodal RAG:** Unified semantic retrieval across documents, images, audio.
- **Governance Gap:** Audit trails, scoped permissions, kill switches are market differentiators.

---

## Tech Stack

| Layer | Component | License |
|-------|-----------|---------|
| Knowledge compilation | okforge | Open source |
| File search | DeskSearch | Open source |
| Email | mcp-email-index / GigaMail | Open source |
| OCR | pysmartocr | Open source |
| Chat UI | notex | Open source |
| Agent framework | loong-agent | Open source |
| Internet access | Agent-Reach | MIT |
| Web intelligence | wigolo-crewai | Open source |
| Voice | chuchote / NixOrb / EdgeVox | Open source |
| Screen capture | CatchMe | Open source |
| Memory | meeple / Mem0 / Letta | Open source |
| Fine-tuning | Troy / Lamark / mlx-lm-lora | Open source |
| Preference | feedloop | Open source |
| Proactive | ProAct / Pask / Aether | Research |
| Kids | Aria / Kids OpenCode | Open source |
| Student | Groundly / DeepStudent / Sidonie | Open source |
| Research | Redline / Khiip | Open source |
| Retention | Lemma / Gnosis / Huoshu | Open source |
| Accessibility | LARA / AIDEN / EnSightingAI | Research |
| Embodiment | Donutbot / Bubbo 1 | Research |
| Inference | ktransformers | Open source |
| Context | Pyramid framework | Research |
| Privacy | Federated Learning | Research |
| Governance | Audit trails / Kill switches | Design |

---

## Competitive Landscape

### What Competitors Have

| Company | Funding/Valuation | What They Do | Gap vs. Aletheia |
|---------|-------------------|--------------|------------------|
| **Hark** | $700M raised, $6B valuation | Proactive AI agent | Cloud-only, closed product, no local runtime, no domain modules, no governance |
| **Ghost Core** | $11M seed, a16z-backed | $3,499 personal AI computer, on-device | Hardware-locked, closed software, no WHAXON-equivalent, no IPP governance |
| **Underdog** | a16z, Khosla Ventures backed | Local AI assistant, Husky inference engine | Single closed assistant, no domain modules, no governance layer |
| **Mem0** | $24M raised | Memory layer for developers | Infrastructure only, not user-facing, no local runtime |
| **RedBear AI** | ~$30B RMB, $50M ARR | Memory-driven AGI, 500+ enterprise customers | Enterprise cloud, no consumer-hardware runtime, no modular architecture |

### What Nobody Has (Differentiation)

| Feature | Hark | Ghost | Underdog | Mem0 | **Aletheia** |
|---------|------|-------|----------|------|--------------|
| **Proactive Advisor** | Yes | Yes | No | No | Yes |
| **Local Runtime (KILN)** | No | Yes | Yes | No | Yes |
| **Domain Expert (WHAXON)** | No | No | No | No | Yes |
| **Modular Architecture (ACP)** | No | No | No | Yes (devs) | Yes |
| **Governance (IPP)** | No | No | No | No | Yes |
| **User-as-Sovereign** | No | Partial | Partial | N/A | Yes |
| **Provider Choice** | No | No | No | N/A | Yes |
| **Compliance-Ready Design** | No | No | No | No | Yes |

**The composition is the moat.**

---

## Financial Projections

### Market Size (2026)

- **Enterprise-Grade AI Agent Platform:** $6.5B (2025) -> $104B (2032), CAGR 43.9%
- **AI Assistant Market:** $19.1B (2025) -> $114.1B (2035), CAGR 19.6%

### Comparable Valuations

- **vLLM** (open-source inference engine, near-zero revenue): **$800M valuation** (January 2026)
- **Hark** (proactive AI agent): **$6B valuation**
- **Ghost Core** (local AI computer): **$11M seed, a16z-backed**
- **Underdog** (local AI assistant): **a16z, Khosla Ventures backed**

### Projected Ranges

| Scenario | Assumptions | Projected Valuation |
|----------|-------------|---------------------|
| **Open-source, no revenue** | Strong GitHub traction, differentiated by IPP + ACP | **$15M-$40M** (acquihire/strategic) |
| **Seed round, $750K ARR** | Professional pilots, 3-5 enterprise WHAXON deployments | **$25M-$50M** |
| **Series A, $4M ARR** | 15-25 enterprise customers, module marketplace live, KILN at Ollama parity | **$60M-$150M** |
| **Series B, $20M ARR** | 100+ enterprise customers, IPP adopted as standard | **$200M-$500M** |

**Upside case:** If IPP (IETF draft) becomes the standard for AI governance, and ACP becomes the standard for module integration, the platform becomes infrastructure. Infrastructure gets acquired for **$500M-$1B**.

---

## Status

**Pre-alpha.** Architecture and roadmap complete. Implementation begins after KILN and WHAXON are shipped.

---

## Sister Projects

- **[KILN](https://github.com/andreipath26/KILN)** — The fastest local LLM runtime. One binary per platform. One model file. One API. No cloud. No GPU required.
- **[WHAXON](https://github.com/andreipath26/WHAXON)** — Deterministic security testing platform with AI guardrails, cross-tool correlation, and four interfaces.

---

## Key Standards Referenced

- **IPP:** draft-haberkamp-ipp-01 (IETF)
- **ACP:** Agent Client Protocol v1
- **OWASP LLM Top 10 (2026)**
- **ISO/IEC 27001, 27701, 42001**
- **GDPR Articles 5, 25, 32, Chapter V**
- **EU AI Act Articles 12, 50, Annex IV**
- **US State Laws:** Texas TRAIGA, Colorado AI Act, California ADMT, New York RAISE Act

---

## License

MIT (core framework). See [LICENSE](LICENSE).

Commercial modules and enterprise support available separately.

---

*The framework that reveals what you already know.*
