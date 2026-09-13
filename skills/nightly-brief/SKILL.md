# Skill: nightly-brief

## When to use

Start or end of a work session. Produce a short ops brief so the next agent (or you tomorrow) knows state without inventing progress.

## Inputs

- Optional: date (default: today)
- Optional: notes the human pastes (shipped, blocked, ideas)
- Project files: AGENTS.md, any open MANIFEST or PRODUCT.md

## Steps

1. Scan the repo for what actually changed (git status / file mtimes if available). Do not invent commits.
2. Write a brief to `briefs/YYYY-MM-DD.md` (create `briefs/` if needed) using this template:

```markdown
# Nightly brief — YYYY-MM-DD

## Shipped (evidence only)
- ...

## In progress
- ...

## Blocked
- ...

## Metrics
- Revenue / users / conversions: BLIND (unless human pasted numbers)

## Money
- Receive-only. No agent-created payment links this session: yes/no

## Next three actions
1. ...
2. ...
3. ...

## Handoff
From: Ops
To: Builder | Copy | QA
Next: ...
```

3. Keep it under ~40 lines. No motivational filler.
4. If nothing shipped, say so explicitly — empty honesty beats fake wins.

## Output

- File: `briefs/YYYY-MM-DD.md`
- Chat: path + the three next actions

## Anti-patterns

- Inventing “shipped” items
- Adding fake KPIs
- Asking the human to re-summarize what the agent can see on disk
