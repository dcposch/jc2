# TDBOUND.md — the Bézout-defect td bound: empirical test

Status: **CONJECTURE TD-BOUND stated; unfalsified on the entire filed
corpus (2026-08-17, the empirical round of grok-lateral1.md §1).**
Machine gate: `cases/tdbound_scan.py` (6 checks, exit 0). Data
sources: the on-axis td=6 residue-A record, the 23 L6-surviving
off-axis entries (`cases/book_offaxis.py` census, td 7..14), the
td-7 §11a book (17 cells), the td-11 census (411 rows). No git
commit.

## 1. The data table (report first, patterns second)

| configuration | td | (m,n) | mn | q_h = (b_i) | law (i) `td<=mn` | law (ii) `td\|mn·Πq` | adjudication |
|---|---:|---|---:|---|---|---|---|
| on-axis residue-A (deg f=168, deg g=252, I_∞=42330) | 6 | (2,3) | 6 | (84-scale) | **HOLDS, AT EQUALITY** | holds | LIVE-FRONTIER (the record) |
| td-7 entry (+ its 17 book cells) | 7 | (2,3) | 6 | (1,2) | fails | fails | DEAD (td-7 book) |
| td-8 [2,2] | 8 | (2,3) | 6 | (2,2) | fails | holds | unadjudicated |
| td-10 ×2 | 10 | (2,3) | 6 | (2,1)/(1,1,2) | fails | fails | unadjudicated |
| td-11 ×3 (+ the 411 census rows) | 11 | (2,3)/(2,5) | 6/10 | (1,2)/(1,3)/(1,2,2) | fails | fails | DEAD (td-11 census) |
| td-12 (2,3) ×3, (2,5) | 12 | (2,3)/(2,5) | 6/10 | various | fails | 3 hold | unadjudicated |
| **td-12 (3,5), poles ((6,1,2,5),(6,1,2,5))** | **12** | **(3,5)** | **15** | **(2,2)** | **HOLDS (12 < 15)** | holds | **UNADJUDICATED — no book was ever built** |
| td-13 ×6 | 13 | (2,3)/(3,4) | 6/12 | various | fails | fails | DEAD (entry-tier rows) |
| td-14 ×5 | 14 | (2,3) | 6 | various | fails | fails | unadjudicated |

Chart-tier note: the td-7 cells' reduced `(d_p:d_q)` ratios are
`{(2,3),(3,5),(5,7)}` — chart data, NOT the configuration `(m,n)`;
kept separate.

## 2. Verdicts

* **Law (i) `td <= m·n`: UNFALSIFIED.** It holds on the one realized
  record (residue-A, **at equality** `6 = 2·3`, with
  `I_∞ = 168·252 − 6 = 42330` — 99.986% of the Bézout budget at
  infinity) and FAILS on 22 of 23 filed off-axis entries — **which
  is exactly the kill record**: every configuration the campaign's
  books have adjudicated dead (td-7's 17 cells, td-11's 411 rows,
  td-13's entry rows) violates the law. The law would retroactively
  EXPLAIN every kill the books produced by chart-tower labor.
* **Law (ii) `td | mn·Πq_h`** (with `q_h := (b_i)`, the MP4 edge
  powers — the available Cor-7.4-power reading at the entry tier):
  coarser — it admits the killed-expected td-8 `[2,2]` entry; law
  (i) is the sharp candidate.
* **The strongest clean pattern**: the live frontier sits at
  EQUALITY (`td = mn`), and **exactly one filed entry lies at or
  below the bound besides residue-A: the td-12 type-(3,5) entry —
  the single configuration in the entire filed range whose book was
  never built.** The candidate law refuses to kill precisely the
  one object nobody has adjudicated. Types occurring in the filed
  range are `{(2,3),(2,5),(3,4),(3,5)}` with `max mn = 15`, so the
  law caps the whole filed ladder at `td <= 15`.

## 3. CONJECTURE TD-BOUND

*For every dominant GGV-standard `(m,n)`-pair (Keller candidate in
rectangular normal form), the topological degree satisfies*

```text
        td  <=  m · n,
```

*with the sharper frontier form `td = m·n` suggested by the realized
record. Combined with Żoładek's `td >= 6` and the finiteness of the
GGV `(m,n)`-list, this makes the sheet ladder FINITE (REDUCTION gap
G5): only types with `mn >= 6` and rungs `6 <= td <= mn` survive —
in the filed range, residue-A `(2,3)@6` and the td-12 `(3,5)` entry
(plus the not-yet-filed `(3,5)` rungs `td <= 15` and `(3,4)` rung
`td = 12`).*

## 4. What a proof needs (the I_∞ accounting)

Bézout is the identity `td = deg f·deg g − I_∞`. The conjecture is
equivalent to `I_∞ >= deg f·deg g − mn = (B²−1)mn` at scale
`B = gcd(deg f, deg g)` — i.e., the certified edge-power contact
(Cor. 7.4: every edge is a power `λR^{qm}`) must consume all but an
`(m,n)`-shaped remainder of the budget. The promoted chart machinery
is the natural accountant: the campaign's `D_f/deg_p_f` ledgers ARE
contact-order data (the trunk certificate's global degrees
`2374050 : 3561075 = 2 : 3` carry the full infinity tower for the
td-7 kill), and the tower calculus already computes per-vertex
contact multiplicities exactly. The missing step is a lemma summing
those per-chart contacts to `I_∞` for an ARBITRARY admissible
configuration — the same L1–L9 frame data, read as intersection
multiplicities at the line at infinity. Grok's mixed-volume/BKK
route (`lib/families.py` supports, `case_rows(150)`) is the
independent cross-check track.

## 5. What this predicts, checkably

1. The unbuilt books (td 8, 10, 12-(2,3)/(2,5), 14) will all close —
   they violate the law.
2. The td-12 `(3,5)` entry is the next genuine frontier object and
   should RESIST the cheap instruments the way residue-A does.
3. Any future book kill of a `td <= mn` configuration other than by
   realization-tier arithmetic would FALSIFY the frontier form
   `td = mn`; a realized configuration with `td > mn` falsifies the
   conjecture outright — either would be a named major result.

## 6. Reproduction

```bash
python3 cases/tdbound_scan.py    # 6 checks, exit 0; prints the table
```

T1 scan size (24 primary rows + 17 + 411 inherited); T2 law (i)
verdicts; T3 the td-12 (3,5) singleton; T4 law (ii) coarseness; T5
the patterns (equality frontier, type census, I_∞, chart-tier
separation); T6 kill-consistency (zero counterexamples among
adjudicated rows). No git commit.
