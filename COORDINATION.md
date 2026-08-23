# COORDINATION.md — the campaign protocol

Model-agnostic. No model is "the" coordinator: any sufficiently capable model
can fill any role below, including an unreleased one. Model names appear in
exactly one place: the roster at the bottom.

## Roles

- **Coordinator** — runs the loop. Each tick: read `notes.md` (queue + latest
  entries) → sweep the fleet (running lanes, remote boxes) → harvest finished
  lanes → route promotable results to adversarial review → bank everything to
  `notes.md` (and `AUDIT.md` on promotion) → launch next lanes per the queue →
  self-pace. The coordinator makes strategy calls between ticks and surfaces
  forks to the human rather than deciding irreversible or expensive things
  alone.
- **Research lane** — a single-task worker (prove / implement / compute /
  survey), launched via `ops/lane.sh <adapter> <tag> <promptfile>`. Owns its
  task end-to-end; delivers `xmodel/<tag>.md` (plus engines/certificates under
  `cases/` when computational). States its producer model in a header line.
- **Adversarial reviewer** — hostile verification of a specific claim, by
  direct recomputation, not deference. Deliverable: verdict per claim
  (CONFIRMED / REFUTED / GAP) with the computation shown.

## Invariants (non-negotiable)

1. **Dual-model promotion.** No result enters `AUDIT.md` at promoted tier
   until it survives hostile review by a *different model* than the one that
   produced it. Self-review does not count.
2. **Evidence tiers, fail-closed.** Every claim carries its tier (EXACT /
   PROVED / MOD-p / BOOK-RELATIVE / FORMAL / INTERNAL-UNREVIEWED / CONJECTURE).
   Absence of a certificate means the lower tier. Never state a verdict the
   certificate does not support.
3. **Bank everything.** Findings, decisions, corrections, and dead ends go to
   `notes.md` the tick they happen. Negative results are kept deliberately.
   At end of day the coordinator appends the day's digest entry (newest first)
   to `PROGRESS.md` — the one-entry-per-day campaign log.
4. **Lane isolation.** One lane, one task, one deliverable path. Lanes do not
   edit shared state (`notes.md`, `AUDIT.md`) — the coordinator banks.
   After installing any third-party CLI, smoke-test existing lanes.
5. **Replayability.** Computational claims ship as engines + certificates with
   exact replay commands and negative controls. Mod-p work records its primes.

## Operational hazards (learned; keep)

- msolve segfaults on very large inputs (32-bit exponent-index overflow):
  never feed full emission files; use exact slices / certificate routes.
- The codex CLI's shared `~/.codex/config.toml` can be mutated by third-party
  tools; the codex adapter strips `model =` lines before every launch.
- Two CODEX_HOMEs refreshing one account revoke each other's tokens: one home.
- Heredoc-in-launcher nested quoting breaks: lanes take prompt FILES.

## Bootstrap (for a fresh coordinator, any model)

1. Read this file, then `README.md`, then `AUDIT.md` (the ledger), then
   `APPROACHES.md` (the avenue map).
2. Read `notes.md` from the bottom up until the state is clear (queue, open
   lanes, triggers, holds). Do not re-derive settled facts.
3. Sweep the fleet (`pgrep -f 'codex exec|grok'`, `tail pilot-local.log`,
   `ops/FLEET.md` for boxes). Harvest anything finished.
4. Continue the loop. When in doubt: bank first, ask the human at forks,
   never promote unreviewed.

## Roster (the only place model names appear)

| Model | Adapter | Notes |
|---|---|---|
| Claude (Anthropic) | (session) | interactive session or `claude -p` |
| GPT / "Sol" (OpenAI) | `ops/adapters/codex.sh` | via codex CLI, account-default model |
| Grok (xAI) | `ops/adapters/grok.sh` | via `grok -p` |

Adding a model = one adapter script in `ops/adapters/`, one roster row. No
other file should need editing.
