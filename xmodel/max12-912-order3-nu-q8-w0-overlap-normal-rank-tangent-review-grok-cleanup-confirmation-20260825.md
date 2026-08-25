# Custody-cleanup confirmation

Read-only textual audit of the raw review, its `.run` metadata, the proposed cleanup companion, and the original review prompt. No hashes were recomputed.

## Proposition 1 — raw corruption vs intact body

**Confirmed.** The raw review is damaged exactly at lines 13–20: an execution/files-read preface (`This review used n…`) is overwritten by a second short final answer (through a premature `CONFIRMED` at line 17), then the files-read list resumes mid-token (`56\``). Heading `## 0` survives; `## 1` is missing.

Sections `## 2`–`## 9` (lines 22–257) are a coherent attack sequence (source identity, Fitting saturations, doubled rank-drop, tangent screen, engine/order/host custody, firewall, nonblocking hardenings) and end in `CONFIRMED`.

## Proposition 2 — nonmutating restoration, no broadening

**Confirmed.** The raw file still contains the collision; the cleanup is a separate companion that cites the same raw SHA-256 as the `.run` `report_sha256` and forbids silent edit of the raw bytes.

Restored execution context matches the `.run` file (no Bash/CAS/solver/network, exit 0, prompt SHA `3869efa0…1a0b`, the two producer-report hashes). Restored files-read inventory matches the original prompt, the remnant at raw lines 18–20, and raw §6 (two producer reports, both frozen case trees, pinned quotient compiler). It does not rewrite §§2–9.

The canonical conclusion restates the intact body without adding theorems.

## Proposition 3 — hashes, targets, inventory, verdict

**Confirmed** by string agreement (not recomputation):

| Item | Cleanup | `.run` / prompt / raw |
|---|---|---|
| Raw review SHA-256 | `6bdbd48a…abe67` | `.run` `report_sha256` |
| Prompt SHA-256 | `3869efa0…1a0b` | `.run` `prompt_sha256` |
| Fitting report SHA-256 | `fca71aaa…47df` | `.run` `target_fitting_sha256` |
| Tangent report SHA-256 | `e421aec0…33dbe` | `.run` `target_tangent_sha256` |
| Targets / cases | two reports, two AWS case dirs, compiler | same paths in raw header, prompt, and `.run` |
| Verdict | `CONFIRMED` | raw line 257, `.run` `verdict=CONFIRMED` |

The cleanup’s SHA-256 of the `.run` file itself is asserted only there; it is consistent with a nonmutating companion and was not recomputed.

## Explicit firewall recheck

- `K3=(d2,d4)` is the line `d2=d4=0` with `c` free in `A3` (raw §3–§4, §7). It is disjoint from the rank-drop `{d2-d4=1}` even scheme-theoretically.
- The rank-drop line and the rank-one point `(d2,d4)=(2,1)` are excluded **only** as ordinary `delta w=1` incidence (`K2=K1=K0=(1)`). That is not a claim about other deformations.
- Raw §7 and cleanup §3 leave ramified/weighted arcs (including through the drop line and `(2,1)`) and the full selected saturation `I:(w x5 (x3-2 x5))^infinity` charged. Also still open: `delta w=0`, higher jets, infinity, Taylor/terminal, trajectories, `(9,12)`, max-twelve, JC2.

No custody defect requiring repair.

CONFIRMED
