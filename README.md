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

---

## Architecture

Three layers, composable, user-defined:

| Layer | Role | Reference Implementation |
|-------|------|--------------------------|
| **Runtime** | Fast, local inference | [KILN](https://github.com/andreipath26/KILN) |
| **Domain Expert** | Deterministic, auditable expertise | [WHAXON](https://github.com/andreipath26/WHAXON) |
| **Memory & Advisor** | Index, remember, reason, advise | Aletheia |

The core knows nothing about any specific domain. It ingests, indexes, retrieves, reasons, cites, and advises. Domain knowledge comes from modules. The integration contract is the Agent Client Protocol (ACP). Users compose their own stack.

---

## The Governance Model

Aletheia is the Round Table, not the King. The user is the sovereign. Aletheia gathers intelligence, organizes knowledge, challenges assumptions, and proposes actions—but never executes a professional decision without explicit human authorization.

This is enforced structurally through the **Intent Provenance Protocol (IPP)**:

- Every action carries a signed intent token tracing back to a human principal.
- The Narrowing Invariant prevents any sub-agent from expanding its own authority.
- Every output carries provenance: source, timestamp, and confidence.

---

## Status

**Pre-alpha.** Architecture and roadmap complete. Implementation begins.

---

## Sister Projects

- **[KILN](https://github.com/andreipath26/KILN)** — The fastest local LLM runtime. One binary per platform. One model file. One API. No cloud. No GPU required.
- **[WHAXON](https://github.com/andreipath26/WHAXON)** — Deterministic security testing platform with AI guardrails, cross-tool correlation, and four interfaces.

---

## License

MIT. See [LICENSE](LICENSE).
