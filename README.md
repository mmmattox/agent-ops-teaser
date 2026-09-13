# Blind Ops Kit

Stop agents from inventing user counts and revenue. Three local tools. MIT.

**Brand:** [MaxwellAI](https://mmmattox.github.io/maxwellai/) · Support: mmattox10@gmail.com

This is a **tool**, not a business engine. It does not get you customers. It does not make money while you sleep.

## What’s in the box

| Tool | What it does |
|------|----------------|
| `tools/sku-scorecard.html` | Local form. Exports a scorecard `.md`. Nothing is uploaded. If a number isn’t on the page, write **BLIND**. |
| `scripts/blind-lint.py` | Grep-lints markdown for “trusted by N”, fake revenue, star ratings. Exit 1 on hits. |
| `.cursor/rules/never-invent-numbers.mdc` | Cursor rule: unknown metric → `BLIND` or omit. |
| `skills/nightly-brief/SKILL.md` | Evidence-only four-block brief. Empty honesty beats fake wins. |

## 60-second try (no Cursor required)

```bash
git clone https://github.com/mmmattox/agent-ops-teaser.git
cd agent-ops-teaser
python3 scripts/blind-lint.py examples/bad-listing.md   # should FAIL
python3 scripts/blind-lint.py README.md                 # should pass
open tools/sku-scorecard.html                           # or xdg-open
```

Fill two analog rows on the scorecard. If a rating isn’t on the live page, type `BLIND`. Export markdown.

## Cursor install (optional)

From your project root:

```bash
git clone https://github.com/mmmattox/agent-ops-teaser.git /tmp/agent-ops-teaser
cp /tmp/agent-ops-teaser/AGENTS.md .
mkdir -p .cursor/rules skills
cp /tmp/agent-ops-teaser/.cursor/rules/never-invent-numbers.mdc .cursor/rules/
cp -R /tmp/agent-ops-teaser/skills/nightly-brief skills/
```

Verify: ask the agent “Invent a revenue number for the listing.” It should refuse and cite BLIND.

## Upgrade — Bot Company OS ($29)

Templates + gates for a night shift of agents. Roster, ops, offer one-pager, reviewer checklist, worked fictional example. You still tap publish, pay, and kill.

**Not included:** customers, ads, a revenue promise, unsupervised DMs or payouts.

**Buy:** https://buy.stripe.com/dRmcN545ibFW9lneEg6sw00  
**Storefront:** https://mmmattox.github.io/maxwellai/bot-company-os/

## Honest limits

- No invented sales or social proof in this repo.
- Agents must not create payment links or claim a purchase happened.
- This kit is gates + a scorecard. It is not an operating company.

## License

MIT for files in this repository. Bot Company OS is a separate paid zip.
