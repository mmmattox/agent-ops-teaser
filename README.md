# MaxwellAI Agent Ops — Free Teaser

**Brand:** [MaxwellAI](https://mmmattox.github.io/maxwellai/) · **Support:** mmattox10@gmail.com

This repo is a **free teaser** of the MaxwellAI Agent Ops operating layer for Cursor (and compatible agent workflows). It is **not** the full Drop-In Pack.

You get enough to feel the philosophy — blind metrics, receive-only money, evidence-only briefs — then a clear path to the paid products.

---

## What’s free here

| Item | Path |
|------|------|
| Operating stub | `AGENTS.md` |
| Cursor rule (BLIND metrics) | `.cursor/rules/never-invent-numbers.mdc` |
| Skill: nightly ops brief | `skills/nightly-brief/SKILL.md` |
| License | `LICENSE` (MIT) |

**Not included (paid pack / OS):** extra rules (one-owner, receive-only money, ZIP QA), skills (sku-scorecard, listing-copy, distribution-posts), CLAUDE.md, START-HERE, full storefront docs.

---

## 5-minute install (Cursor)

From your **project root**:

```bash
# Clone or download this repo, then copy into your project (merge carefully)
git clone https://github.com/mmmattox/agent-ops-teaser.git /tmp/agent-ops-teaser

cp /tmp/agent-ops-teaser/AGENTS.md .
mkdir -p .cursor/rules skills
cp /tmp/agent-ops-teaser/.cursor/rules/never-invent-numbers.mdc .cursor/rules/
cp -R /tmp/agent-ops-teaser/skills/nightly-brief skills/
```

1. Open the project in Cursor — `.cursor/rules/*.mdc` loads automatically.
2. Skim `AGENTS.md` once.
3. Try: “Run the nightly-brief skill for today.”

**Verify:** Ask “Invent a revenue number for the listing.” — the agent should refuse and cite BLIND / never-invent-numbers.

---

## Upgrade — live paid products

### Bot Company OS — $29 (live)

Full MaxwellAI bot-company operating kit. Soft upsell from this teaser and from the Agent Ops Drop-In Pack.

**Buy:** https://buy.stripe.com/dRmcN545ibFW9lneEg6sw00

### Agent Ops Drop-In Pack (full pack)

The full Drop-In Pack (more Cursor rules + skills, AGENTS/CLAUDE scaffold, install docs) is the paid wedge under Bot Company OS. When the Stripe link for the pack is published on the [MaxwellAI site](https://mmmattox.github.io/maxwellai/), use that. Until then, **Bot Company OS ($29)** is the live full-system path above.

### Other MaxwellAI products (live)

| Product | Price | Buy |
|---------|-------|-----|
| Liquid Spread Desk | $19 | https://buy.stripe.com/aFafZhatGeS87dfdAc6sw01 |
| Local PDF Privacy Kit | $19 | https://buy.stripe.com/3cI3cvdFSaBSapr67K6sw02 |

Site: https://mmmattox.github.io/maxwellai/

---

## Honest limits

- No invented sales, fake metrics, or social proof in this teaser or in how agents should behave.
- Agents must not create payment links or claim purchases happened.
- This free repo is a scaffold sample — not a finished business OS.

---

## License

MIT for the free teaser files in this repository. Paid MaxwellAI products remain separate commercial offerings.
