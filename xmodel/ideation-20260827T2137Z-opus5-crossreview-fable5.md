# Hostile cross-review of the Opus5 blind ideation — round `20260827T2137Z`

Reviewer: **Fable 5** (Anthropic), exact model ID `claude-fable-5`, acting as
equal-standing hostile mathematical reviewer.
Date: 2026-08-27.
Report path: `xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md`
(the only file written this session; SHA-256 of the sealed bytes reported in
stdout at seal, not embedded).

## 0. Mandatory input custody (fail-closed gate passed)

- `xmodel/ideation-20260827T2137Z-opus5.md` — recomputed SHA-256
  `49dd042a15670f082ea4335610150eee3022fc7a37282df200e2ae3a052ea0a0` —
  **matches the pinned value**; read in full.
- `xmodel/ideation-20260827T2137Z-postseal-truth-delta.md` — actual SHA-256
  recorded at session start:
  `0e09faeb69480b7594864199fbd061291af490cf8e514d1795784fbf00ad9bee`;
  read in full and applied (§8).
- My own sealed submission `xmodel/ideation-20260827T2137Z-fable5.md`
  recomputes to `edd383ad…76bb`, matching the delta's custody line, and is
  used here only for the charged mechanism comparison (§7).

Headline of this review, stated up front: the **torsor theorem is correct
and I promote it**; the **budget arithmetic is exactly right**; but the
operational superstructure (row budget as allocation fact, `GATE-MARCH`,
Card B's rate semantics) fails hostile review at a specific, provable
point: **under the licensed exact-`p`-power presentation — the one the
promoted AUDIT block itself mandates — the `F_n`-linear part of every
`k_m = 1` gate row with `m >= 28` is identically class-exact (vacuous)**,
because `p^{n+2}/H^2` becomes a polynomial times a rational gauge there.
Exact desk computation (this session) gives licensed linear capacities of
**26 (P) and 35 (Q)** for rows 23–34 against the promoted ceilings 42/51,
and **27 (P) / 37 (Q) for the entire infinite tower**; everything beyond is
nonlinear carry with no proved realization. This also exposes a latent
artifact in the promoted stable-range claim at rows 28/30 (erratum E0,
which reaches my own prior review). Details, proofs, and exact tables in
§6; verdicts in §1.

---

## 1. Itemized verdict table

| # | Opus claim (location) | Verdict |
|---|---|---|
| 1 | `V_H -> U` is a finite étale `mu_4`-torsor; `O_{V_H} = ⊕ O_U p^j`; summand `j` carries `∇_j` (§3.1) | **CONFIRMED** (full proof re-derived, §2; hypothesis to add: `mu_4 ⊂ K` or read geometrically — R7R1 repair 2) |
| 2 | `H^1_dR(V_H) = ⊕_j H^1_dR(U, ∇_j)`; row `m` lives in summand `j = m mod 4` (§3.1) | **CONFIRMED** (`j = (n+2) mod 4 = m mod 4` since `20 ≡ 0`; matches promoted `q_n^σ = ζ^{n+2} q_n`) |
| 3 | Torsor capacity law `b_1(V_H) = 4(r-1)+c`, `c = #components = #{j: 4|j e_i ∀i} = Σ_j k_j` (§3.2) | **CONFIRMED — the round's one promotable new theorem** (§2; both `c`-formulas equal `gcd(4, gcd_i e_i)`; disconnected case verified) |
| 4 | Fixture table `42/51/12/87 = 3·b_1`; rows 25/26 codims `(3,4)`/`(4,4)` (§3.2) | **CONFIRMED** (all recomputed exactly this session; P/Q shapes verified against frozen artifacts, §4) |
| 5 | Per-row law re-derivation "independent proof… removes the stable-range caveat" (§3.2 Cor.) | **CONFIRMED WITH DEMOTION** — the per-row derivation is the *same* Deligne-index proof as the promoted corrected theorem, not an independent one; the dimension law never had an `m`-truncation, so nothing is removed; the torsor adds the sum-equals-`b_1` identity and the component reading of `k` (new), not a new per-row proof |
| 6 | Row-budget thresholds `P: 57/58`, `Q: 51/52`; rate `3.5 / 4.25` per row (§3.3) | **CONFIRMED AS ARITHMETIC, REFUTED AS OPERATIONAL SCHEDULE** — valid only as the crossing row of the cumulative count of abstract licensed class equations; the licensed rows' *linear realization* dies far earlier (§6), and the campaign-row ⟺ class identification is necessary-direction only (§5) |
| 7 | "Determinant-anchored tower cannot reduce F-side to origin before row 57/51" (headline, §3.3) | **CONFIRMED WITH REPAIR (terminology + scope)** — determinant rows end at `D34` (`D35 ≡ 0` structural, frozen R7R1 review); rows ≥ 35 are exact-identity-licensed class conditions, not determinant rows; true statement: the class-condition prefix cannot pin the 121/124-window before those rows, and its *linear* content can never pin it (§6) |
| 8 | "No computation through row 34 could possibly have emptied the P or Q face" (§3.3.1) | **REFUTED AS STATED** — true only of the homogeneous F-side class tower; the live lanes impose rows ≤ 22 plus inhomogeneous `D22 = 1` (branch-P preregistration: "Neither `D23=0` nor the `q1` image equation is an input to any solver lane"), and emptiness of *that* system is not bounded by class capacity |
| 9 | "Everything through row 34 was, provably, about one third of a computation" (headline) | **REFUTED** — the fictitious completion (rows 35–57) has zero linear supply on the window (§6) and unproved nonlinear realization; also the lanes' object is not the class tower (see #8) |
| 10 | Scope limit: tower is F-side-only, locus contains `F = 0`, decision only via `D22 = 1`; `124` of `~400` slots (§3.3.3–4) | **CONFIRMED IN SUBSTANCE, PHRASING REPAIRED** — `q_n` F-only (promoted); slots-zero point passes all tower rows; `D22 = 1` inhomogeneity is where death lives (`D22 = -L22(g22)`, polynomial `g22` forces `D22 ∈ (H)`, promoted); census F 124 / G 276 independently recounted from frozen `RAW_INPUT.json` this session; but raw determinant rows 23–34 *do* couple F- and G-slots bilinearly (`a+b=m`, G up to weight 21), so "leaves all 276 G slots free" is loose — correct claim: the *projected* F-side tower is G-free and never empty |
| 11 | §3.4 "tower is triangular, hence linear-time"; §6 `GATE-MARCH` | **REFUTED AS DESIGNED** — exact only for rows 23–27; at every `k_m = 1` row with `m ≥ 28` the licensed linear slot map is identically zero (theorem + exact table, §6); rows ≥ 37 have no `F_n` slot at all; the march's stop-rule (b) fires spuriously by pure algebra |
| 12 | Card A `TORSOR-BUDGET` | **PASS-half CONFIRMED** (law + numbers); **FAIL semantics miscalibrated**: realized codim above `Σ(r-1+k_m)` would indicate bounded-presentation strengthening of rows (row-22 precedent: polynomial-window codim 7 > class 4 on P, frozen), not falsify the torsor law |
| 13 | Card B `GATE-SURVIVOR` | **TARGET CONFIRMED, RATE SEMANTICS REFUTED** — independence is the right thing to test and evaluation-marching a given `F*` is sound; but the "predicted rate" must be the corrected licensed schedule (§6 table), else the guaranteed linear stall at rows 28/30/32/34/36 is misread as tower incapacity; constructing `F*` past row 27 is nonlinear work, not one solve per row |
| 14 | Card C `TD-END` | **CONFIRMED** — identity confirmed post-seal (delta item 5); discriminator well-posed; AMS caveat correctly filed |
| 15 | §1 dispositions: 2 lower; 3/16/25/26/33 raise; 7 raise; 43 lower | **CONFIRMED** — avenue-2 lower is exactly delta items 1–3; the finite-end raises stand on the delta-confirmed identity; avenue-43 primitivity lemma verified correct (three-line `h'(u)` argument; APPROACHES row 43 = Ritt decomposition, already marked "collapses to GGV", so the lower is coherent); 16/33 raises survive §6 with the receiver intact but the *instrument* repaired |
| 16 | §4.1/§4.2 composition and separation table, incl. `SCOPE-CONFLICT` (Kummer torsor vs Keller passport) | **CONFIRMED** — the explicit refusal to compose the two covers is correct and valuable; finite-end × gates INVALID (two unrelated curves) correct; LF40 separation matches my sealed §3.3/§4 independently (convergent) |
| 17 | §5.1 decisive object `κ(M)` | **REFUTED AS INSTRUMENTED** — the proposed march measures linear ranks only; `κ(M)` diverges from it from row 28 on; the trichotomy's "stall" branch is guaranteed and uninformative (§6) |
| 18 | §5.2 falsification object `F*` | **CONFIRMED WITH REPAIR** — see #13 |
| 19 | §8 lane dispositions | **CONFIRMED** except the held-quotient "prediction" (§6 of the producer report): the 466-generator quotient targets rows ≤ 22, where tower capacity says nothing; strike that inference from any 128-GiB commit decision (E10) |
| 20 | §9 insight (rate pinned by `χ`, unimprovable; `k_m` = component count) | **CONFIRMED for the ceiling, REFUTED for attainability** — the per-period ceiling `b_1/4` is genuinely unimprovable and the `h^0`/component reading of `k_m` is correct and new; but the realized licensed linear rate is 0 at the `k`-rows from 28 on, so "the only lever is more rows" understates how much worse it is |
| 21 | §10 honest ledger, §10.2 disclosed failures, §10.5 blindness | **CONFIRMED** — P-shape "inferred" upgrades to *frozen* (branch-P preregistration fixes `A = X^4-1`, `H = A^2`, `F1 = H`, `V = 1`); the dropped strong no-go is correctly reported false for the class tower; blindness and `jc2-lean` filename-touch disclosures adequate |

---

## 2. Focus 1 — the exact `mu_4`-torsor statement: PROVED

**Theorem (Opus §3.2, verified).** Char 0, `mu_4 ⊂ K` (else read
geometrically), `H = h_0 ∏ p_i^{e_i}`, `U = A^1 − Z(H)`,
`r = deg rad H`, `V_H = Spec O_U[p]/(p^4 − H)`.

1. *Étale torsor.* On `V_H`, `H ≠ 0` forces `p ≠ 0`, so
   `d(p^4 − H)/dp = 4p^3 ≠ 0`: finite étale of degree 4. `mu_4` acts by
   `p ↦ ζp` simply transitively on fibres: a torsor, classified by
   `χ: π_1(U) → mu_4`, loop `i ↦ ζ^{e_i}`.
2. *Character decomposition.* `H` invertible on `U` makes
   `O_{V_H} = ⊕_{j=0}^{3} O_U·p^j` free; `4p^3 dp = dH` gives
   `d(f p^j) = (df + f·(j/4)·dH/H)·p^j`, so the `p^j`-summand of the de
   Rham complex is the `∇_j = d + (j/4)dH/H` twisted complex, and (affine
   curve, group order invertible)
   `H^1_dR(V_H) = ⊕_j H^1_dR(U, ∇_j)`. The promoted character law
   `q_n^σ = ζ^{n+2} q_n` places row `m = n+22` in summand
   `j = (n+2) mod 4 = m mod 4`.
3. *Betti count, disconnected case included.* Each component of a smooth
   affine curve is homotopy-wedge of circles, so
   `χ(V_H) = b_0 − b_1 = c − b_1`; étale degree 4 gives
   `χ(V_H) = 4χ(U) = 4(1−r)`; hence `b_1(V_H) = 4(r−1) + c`.
4. *Component count.* `c = [mu_4 : im χ] = #{j ∈ Z/4 : χ^j = 1}`
   (cyclic group: both sides are `4/ord(χ)`), and `χ^j = 1` iff
   `4 | j e_i` for every `i`. Since `k_j := h^0(U, ∇_j) ∈ {0,1}` with flat
   section `H^{−j/4}` rational exactly under the same condition,
   `c = Σ_j k_j`. Numerically both equal `gcd(4, gcd_i e_i)`: P
   (`e = 2,2,2,2`): 2; Q (`2,2,2,1,1`): 1; `(X−a)^8`: 4; squarefree: 1 —
   each verified against the component structure directly (e.g. on P,
   `V_H = {p^2 = ±A}`, two components).

All four steps re-derived independently this session; no gap found. The
per-row corollary (`h^1 = r−1+k_j` via `χ_dR = rank·χ_top − Irr`, `Irr = 0`
for the logarithmic `∇_j`, consistent with the R7R2 regularity cut) is the
**same** derivation as the promoted corrected theorem `1cc41972…`, so it is
confirmation, not independence (verdict #5). What is genuinely new and
promotable: the single-curve packaging, the identity
`Σ_{j} (r−1+k_j) = b_1(V_H)` with `c = Σk_j` = component count, and
`42/51/12/87 = 3·b_1(V_H)` (rows 23–34 = exactly three periods).

## 3. Focus 2 — finite character sum vs. infinite row tower

What the identity bounds, precisely:

- **Per-row abstract receiver dimension** — `r−1+k_m` scalar class
  equations per licensed row, every `m`, no window truncation. This was
  already promoted; the torsor adds nothing per-row.
- **Per-period total** — `b_1(V_H)` per four consecutive rows. This is the
  new closed form.
- **Cumulative equation count** — at most `Σ_{m=23}^{M}(r−1+k_m)` class
  equations through row `M` (crossing 121/124 at `M = 57/58` on P,
  `51/52` on Q; recomputed).

What it does **not** bound: (i) realized codimension from below
(independence untested — Card B's true target); (ii) realized codimension
from above for the *campaign rows*, because the row ⟺ class identification
is proved in the necessary direction only (R7R1: rows ⟹ `q_n dX` exact in
`L`; the converse builds `W` over `L` and "need not descend … or produce
polynomials" — R7R1 firewall verbatim; row-22 precedent shows a
polynomial-presentation row can cut strictly more than its class); (iii)
anything about G-slots or rows ≤ 22.

The four receiver spaces being finite does **not** cap the tower: the
tower revisits each `H^1(U, ∇_j)` infinitely often with a *different*
class `[q_n]` each visit, so conditions accumulate in F-space without
bound. Conversely the "infinitely repeated row tower" is not an infinite
supply of determinant rows: `D35 ≡ 0` identically (`y`-free corners
`x^2, x^3`; frozen R7R1 review `7ab758fa…`), the sharp determinant maximum
is `D34`, and the finite system `D0..D21 = 0, D22 = 1, D23..D34 = 0`
forces `E = t^22` exactly, which then *licenses* the infinite `q_n` family
as derived necessary conditions (R7R1 client paragraph; the licensing rule
`n + 22 < N`). So the correct picture is: **finite determinant system;
infinite derived class tower; finite four-space receiver; unbounded
cumulative equation count; and — new, §6 — finite and small licensed
*linear* content (27 on P, 37 on Q, in total, forever).**

## 4. Focus 3 — recomputations and the assumption inventory

All recomputed exactly this session (script pinned in §13; excerpts):

```text
window dims n=1..14 : 16 15 14 13 12 11 10 9 | 7 6 5 3 | 2 1
census              : F1..F12 = 121,  F1..F14 = 124,  F_n = 0 for n>=15
F/G raw census      : F 124 / G 276 positive-weight slots, G max weight 21
                      (recounted from frozen D3 RAW_INPUT.json, matches)
k-sums rows 23..34  : P 42 = 3x14, Q 51 = 3x17, r=1 12 = 3x4, r=8 87 = 3x29
row 25/26 receivers : P (3,4), Q (4,4)          (match promoted)
budgets             : P 57 (>=121) / 58 (>=124); Q 51 / 52; r=8 39/40
rates               : 14/4 = 3.5 (P), 17/4 = 4.25 (Q)
```

Fixture shapes: branch P `H = A^2`, `A = X^4−1` squarefree quartic is
**frozen**, not inferred (branch-P preregistration `60e6b274…`); branch Q
`H = A^2B`, `deg A = 3`, `deg B = 2`, both squarefree, `gcd(A,B) = 1`
(promoted AUDIT block, 18:02Z). Opus's honest-ledger leap 1 dissolves in
his favor.

Assumptions the budget silently stacks (each named, none proved):

- **A1 (identification):** campaign row `m` ⟺ class condition, all `m`.
  Proved necessary-direction only; converse fails to produce polynomial
  `G`; row 22 is a frozen counterexample to the pattern.
- **A2 (window realizability):** each row realizes `r−1+k_m` on the frozen
  window. Now known **false** from row 28 on in the licensed presentation
  (§6); soundly verified only for rows 23–27 (P/Q).
- **A3 (independence across rows):** untested; Card B's target.
- **A4 (rows ≥ 35 exist as conditions):** yes, but only as
  exact-identity-licensed derived conditions (not determinant rows), and
  with zero linear window supply.
- **A5 (census):** verified (121/124/276 recounted).

## 5. Focus 4 — can F-side gates ever decide the endpoint?

Opus's scope claim survives in substance and is the report's soundest
strategic content: `q_n` is F-only (`Q = F^{1/4}`, promoted), the
slots-zero point satisfies every homogeneous tower row, so the tower locus
is never empty and the decision must come from the inhomogeneous
`D22 = 1`, where the promoted transfer `D22 = −L22(g22)` (polynomial
`g22` forces `D22 ∈ (H)`, incompatible with 1; rational target
`g22 = v/(8A^5B)`, `Bv' + (3/2)B'v = A`) lives. Two repairs:

- **Determinant coupling.** Raw rows 23–34 are bilinear and *do* involve
  G-slots (`F_a G_b`, `a + b = m`, G-slots up to weight 21 — recounted).
  The F-only statement is about the *projected* tower after G-elimination
  given lower rows. "Leaves all 276 G slots free" should read: the
  projected tower imposes nothing on G beyond what rows ≤ 22 already do.
- **Direction.** Because the class conditions are necessary-only, class
  capacity bounds the *outer* F-side locus. The actual survivor set
  (F extendable to polynomial G meeting the full target) sits inside it
  and can be smaller at every stage — so class capacity can never certify
  that a lane "had no chance"; it certifies only that the class instrument
  alone cannot finish. Verdict #8 follows.

## 6. Focus 5 — `GATE-MARCH` audit: the licensed linear tower is
## vacuous at every `k`-row from 28 on (NEW, proved + measured)

**Theorem (this review; three lines, from frozen formulas only).** The
`F_n`-linear term of `q_n` is `F_n p^{n+2}/(4H^2)` (promoted closed form;
re-derived: only the `u`-linear binomial term contributes, with
`P^n → p^n`). Writing `p^{n+2} = p^j H^{(n+2−j)/4}`,

```text
linear term = (F_n/4) · H^e · p^j,   e = (n+2-j)/4 - 2,   j = m mod 4.
```

If `k_m = 1` (i.e. `H^{j/4} ∈ K[X]`, a *polynomial* — exponents
`j e_i/4 ≥ 0`) and `e ≥ 0` (i.e. `n ≥ j + 6`, i.e. `m ≥ 28`), then for
every window `F_n` the linear term is `∇_j`-exact: gauge by the polynomial
`H^{j/4}` reduces it to a polynomial form in untwisted cohomology, which
integrates in `K[X] ⊂ O(U)`. Under the licensed reading — R7R1 (0.2)
exactness in `L`, which equals the with-poles class condition because a
pole of `w` off `Z(H)` would create one in `w' = q_n` — **the row's linear
part imposes nothing**. This is exactly the trap the promoted block's last
sentence warns about ("integer-shifting the twist … can make it vacuous;
use the exact `p`-power carried by `q_n`"), firing *inside* rows 28–34.
Affected rows: P — 28, 30, 32, 34, 36 (all even `m ≥ 28`; note
`H^{1/2} = A` polynomial); Q — 28, 32, 36; `r=1` control — every row
≥ 28. Every NL term (`F`-degree `d ≥ 2`) has `H`-exponent
`≤ (n+2)/4 − 2d < 0` for `n ≤ 13`, so the rows remain generically
nonvacuous — but **nonlinear, on lower slots**.

**Exact measured table** (fresh harness, exact `Q`, pole cap and degree
swept `M ∈ {4,6}`, `D ∈ {90,110}`, stable; licensed gate
`∃c ∈ K[X, 1/rad H]: c' + (j/4)(H'/H)c = (F_n/4)H^e` vs the row-24-style
shifted gate `4Hc' + jH'c = F_n` copied upward):

```text
P (H=(X^4-1)^2):   m: 23 24 25 26 27 28 29 30 31 32 33 34 | 35 36
  licensed rank       :  3  4  3  4  3  0  3  0  3  0  3  0 |  1  0   sum23-34 = 26
  shifted-op rank     :  3  4  3  4  3  4  3  4  3  3  3  3 |  1  1   sum23-34 = 40
  promoted law r-1+k  :  3  4  3  4  3  4  3  4  3  4  3  4 |  3  4   sum23-34 = 42

Q (H=(X^3-X)^2(X^2-4)): m: 23 24 25 26 27 28 29 30 31 32 33 34 | 35 36
  licensed rank       :  4  5  4  4  4  0  4  1  4  0  4  1 |  2  0   sum23-34 = 35
  shifted-op rank     :  4  5  4  4  4  5  4  4  4  4  4  2 |  2  1   sum23-34 = 48
  promoted law r-1+k  :  4  5  4  4  4  5  4  4  4  5  4  4 |  4  5   sum23-34 = 51
```

Consequences:

1. **Licensed linear capacity of the entire infinite tower: 27 (P),
   37 (Q)** — rows ≥ 37 have no window at all. The 121/124-slot window can
   *never* be pinned by the tower's linear content; every collapse route
   runs through the nonlinear carry classes, about which nothing is
   proved. This supersedes the budget as the honest capacity statement.
2. **`GATE-MARCH` as designed is exact only for rows 23–27.** From row 28
   the "one small linear solve" either reports no new conditions (licensed
   presentation, `k`-rows) or imposes conditions the licensed gate does
   not (shifted presentation — 4/5 phantom conditions per `k`-row). Stop
   rule (b) ("stall for two periods ⇒ gate-survivor falsification") fires
   spuriously by pure algebra; outcome-1 of §5.1 ("κ tracks the bound to
   row 58") is algebraically impossible for the instrument proposed.
3. **Erratum E0 to the promoted record (reaches my own prior review).**
   The 19:37Z block's "stable-range equality … stops at row 30" and my
   `1cc41972` §5.2 claim of law-agreement at rows 22–31 hold at rows
   28/30 only in the shifted presentation, which at those rows is *not*
   the licensed gate. Licensed equality stops at **row 27** (P/Q; control
   likewise suspect at 28–30). Rows 29/31/33 survive at full rank 3/4
   (genuine twist, measured). An additive erratum to the promoted block is
   required; the block's own final sentence is the authority for the
   repair.

**Cheapest literal test on a frozen branch** (charged question): with F
fixed rational, every raw determinant row is *linear in the G-slots*. So:
take the frozen branch-P fixture (`A = X^4−1`, `H = A^2`, `F1 = H`,
`F2 = (1+HZ)/4`, `F3 = (Z+AT)/8`), choose `Z, T, F_4, F_5` random rational
in the frozen windows subject to the (linear) licensed gates through row
27, leave `F_6` symbolic (11 window slots), solve rows `D_1..D_27 = 0`
for the 276 G-slots by exact linear algebra, and row-reduce `D_28`'s
compatibility onto the `F_6` window. Licensed prediction: **0** conditions
on `F_6` (an `F_6`-independent obstruction on lower slots); shifted
prediction: **codim 4**. One desk run (a few hundred exact-`Q` unknowns,
well inside the campaign's demonstrated pure-Python envelope) decides the
presentation question at the artifact level and doubles as the
long-outstanding row-`>=25` imposition run. This is the single most
information-dense cheap computation available to the tower programme.

## 7. Focus 6 — Opus's torsor vs. my sealed sector-intertwiner /
## coherent-compression mechanism

Both sealed reports independently found the same germ: my
`T_m(HY) = H·T_{m+4}(Y)` (operator form) is Opus's gauge intertwiner
`H·∇_{m+4} = ∇_m·H` (connection form) — same identity, blind-convergent,
both crediting the corrected theorem's representative-independence.

- **What subsumes what.** Opus's torsor *globalizes* my periodicity
  observation: the intertwiner says the four sector cokernels are one
  module each; the torsor says the four sectors are the isotypic pieces of
  one curve and computes their total by `χ`. Opus's Theorem 3.2 subsumes
  my ingredient 1 and is the cleaner object. Conversely my Card 1
  (assembly of each sector's classes into a section `γ_j(s)` of a
  finite-rank coherent module; Krull finite determinacy; effective `N0`
  by rational residue pairings) targets the half of the promoted open end
  that Opus's budget does not touch: Opus prices *when capacity suffices*
  (schedule, upper story); I target *when finitely many rows decide the
  whole tower* (determinacy, closure story). Neither subsumes the other's
  main claim.
- **What composes.** Cleanly: `V_H` is the natural home for my sector
  modules — `M_j` is coherent on (an `s`-family over) `V_H`'s `j`-isotypic
  piece, and my residue pairing is Opus's avenue-3/33 "residue pairing on
  `V_H`". A merged card — torsor receivers + `γ_j(s)` sections + `N0` —
  is the right successor object, with this review's §6 as a mandatory
  constraint: the *linear* part of `γ_j` dies at the `k`-rows from 28 on,
  so the pairing bookkeeping must be built on the full nonlinear carry,
  which strengthens the case for working with the assembled algebraic
  section rather than row-by-row.
- **What remains untyped.** (i) The per-sector algebraic assembly closed
  forms (my sealed negative control: `q_3` is not `[t^3](1/2)√F`; each
  sector needs its own functional). (ii) Realized-codim/independence
  (Opus Card B, corrected rates). (iii) The campaign-row ⟺ class
  identification at `m ≥ 28` (§6 discriminator). (iv) Any bridge from
  either mechanism to `D22 = 1` or rows ≤ 21 — both mechanisms are
  strictly tower-side.

## 8. Focus 7 — post-seal truth delta applied

- Items 1–3 (Corollary-7.4 corridor refuted; `C74-PLACE` split;
  `EXIT-RPMC(C) ≡ RPMC(C)`): Opus's §1 avenue-2 lower, §4.2(3), and §8
  coverage-redesign already conform (they are the delta's own source,
  now confirmed); no sentence of the Opus report relies on the refuted
  positive half or on `EXIT-RPMC(C)` being cheaper. **No stale
  dependency found.** This review likewise uses neither.
- Item 4 (VGG re-selection chart-rigid): consistent with Opus §4.2(3);
  no action.
- Item 5 (finite-end identity confirmed; Chau marked-profile congruence
  169→48, kills none): confirms the foundation of Card C and the
  7/25/26 raises; the congruence slightly *strengthens* the avenue-25
  raise (a second pruning instrument) without changing any verdict here.
- Item 6 (orientation/proximity/hash repairs): not used by the Opus
  report; noted for any G2 reuse.

## 9. Narrowest promotable theorems

**T1 (promote; Opus §3.2 with hypotheses pinned).** Over char-0 `K ⊇ mu_4`
(or geometrically), with `H, U, r, V_H` as above: `V_H → U` is a finite
étale `mu_4`-torsor; `H^1_dR(V_H) = ⊕_{j} H^1_dR(U, ∇_j)`;
`b_1(V_H) = 4(r−1) + c` with
`c = #components = #{j ∈ Z/4 : 4 | j e_i ∀i} = Σ_j k_j = gcd(4, gcd_i e_i)`;
row `m` lands in summand `m mod 4`; hence
`Σ_{m=23}^{34}(r−1+k_m) = 3·b_1(V_H)`, reproducing `42/51/12/87` on the
four frozen fixtures, and the per-period capacity ceiling `b_1(V_H)/4` per
row is `j`-uniform and cannot be improved by row selection.

**T2 (promote at rescoped wording).** For every `M ≥ 23` the licensed
class-gate prefix (rows 23..`M`) consists of at most
`Σ_{m=23}^{M}(r−1+k_m)` scalar conditions on the 124 frozen F-slots; the
sum first reaches 121 at `M = 57` (P) / 51 (Q) and 124 at 58/52. No
statement about realized codimension, about the actual determinant
system's F-projection, or about lanes follows.

**T3 (new, this review; needs different-model confirmation before
promotion).** In the licensed exact-`p`-power presentation, the
`F_n`-linear part of the row-`m` class gate is
`(F_n/4)H^{(n+2−j)/4−2}p^j`; it is identically class-exact at every row
with `k_m = 1` and `m ≥ 28`. Measured licensed linear ranks on the frozen
windows: P `3,4,3,4,3,0,3,0,3,0,3,0 | 1,0` (rows 23–36; total 26 through
34, 27 total); Q `4,5,4,4,4,0,4,1,4,0,4,1 | 2,0` (35 through 34, 37
total). The infinite tower's linear content cannot pin the window;
erratum E0 to the 19:37Z promoted block and to review `1cc41972` §5.2 at
rows 28/30 is required.

## 10. Errata list (Opus report unless marked)

- **E0 (promoted record + my own prior review; additive erratum
  required).** "Stable-range equality … stops at row 30" (AUDIT 19:37Z)
  and law-agreement at rows 28/30 (`1cc41972` §5.2) hold only in the
  shifted-operator presentation, which is not the licensed gate there;
  licensed equality stops at row 27. Discovered via the block's own
  exact-`p`-power mandate; exact table in §6.
- **E1.** "Determinant-anchored tower … before row 57": determinant rows
  end at `D34` (`D35 ≡ 0`); rows ≥ 35 are identity-licensed class
  conditions. Rephrase.
- **E2.** §3.3.1 "no computation through row 34 could have emptied the
  face": true only for the homogeneous class tower; the live lanes charge
  rows ≤ 22 + `D22 = 1` and are not capacity-bounded by it.
- **E3.** Headline "one third of a computation": unsupported; the
  completion's linear supply is zero and its nonlinear realization
  unproved.
- **E4.** §3.4 linear-time triangularity: fails from row 28 (§6) and
  trivially from row 37.
- **E5.** §6 stop rule (b): guaranteed spurious trigger; separate linear
  from carry cuts before any stall semantics.
- **E6.** Card A FAIL branch: over-rolls; realized codim above the class
  count would implicate A1 (bounded-presentation strengthening), not T1.
- **E7.** Card B rates: use the §6 licensed schedule; as written the
  discriminator misreads a theorem as a discovery.
- **E8.** "Leaves all 276 G slots free": raw rows 23–34 couple G-slots
  (weights ≤ 21) bilinearly; correct statement is about the projected
  tower.
- **E9 (in Opus's favor).** P-shape is frozen in
  `cases/ggv_8_28_upper_endpoint_branch_p_20260827/PREREGISTRATION.md`,
  not inferred.
- **E10.** §6 held-quotient "prediction": the 466-generator quotient
  targets rows ≤ 22; tower capacity is silent there; strike from the
  commit decision.
- **E11.** Headline "`b_1` is forced by `χ(U)` alone": needs the
  component count `c` too (Opus's own §3.2 is correct).
- **E12.** §3.2 "removes the stable-range caveat": the promoted dimension
  law never carried an `m`-truncation; the caveat was always about
  in-window realization, which the torsor does not touch (and which §6
  now moves the other way).

## 11. Cheapest discriminator per surviving conjectural step

| Conjectural step | Cheapest discriminator |
|---|---|
| Campaign row ⟺ class at `m ≥ 28` (A1) | The §6 linear-in-G imposition run: solve `D_1..D_27` for G-slots at a gate-satisfying rational F-prefix, reduce `D_28` onto the symbolic `F_6` window; 0 vs 4 conditions decides. Desk-scale, exact `Q`. |
| Row independence / realized codim (A3, Card B repaired) | Evaluation-march one explicit `F*` (rows 23–27 solved linearly, carry conditions solved by elimination on ≤ 12 equations) through rows 28–40 against the §6 schedule; record first death row. |
| Nonlinear carry classes actually cut (post-§6 realization) | Compute `[NL_6(F_1..F_5)]` residues at 20 random rational prefixes on P; nonzero generically ⇒ row 28 cuts (nonlinearly); all-zero ⇒ row 28 wholly vacuous and the capacity story shrinks again. Hours, desk. |
| Tower finiteness (my Card 1, composed with T1) | Untwisted-sector residue pairing on the P stratum: rationality + degree bound of one pairing `c_i(s)`; two desk days (unchanged from my sealed card, now with §6 as a constraint). |
| Card C usefulness | Instantiate `td = Σe_S − b_1 + 1` on the live `8_28` forest data; check both sides; ask if the forest bounds `Σe_S` (unchanged from Opus, delta-confirmed foundation). |
| Endpoint decidability (the actual face question) | Unchanged: the running rows-≤ 22 + `D22 = 1` lanes; nothing in this round touches their status. |

## 12. Did Opus supply significant unique capability over Fable this round?

**Yes, modestly and genuinely — one correct new theorem and one correct
strategic frame — but the operational layer did not survive review.**
Unique to Opus (absent from my sealed report): the torsor globalization
T1 with the `χ(V_H)` computation and the component-count reading of
`k_m` (elegant, promotable); the explicit 124-of-400 scope frame and the
`D22 = 1`-is-the-decidable-object sharpening (sound, verdict #10); the
avenue-43 primitivity freebie (correct); the budget arithmetic (correct
as arithmetic). Unique to my sealed report (absent from Opus's): the
determinacy/`N0` mechanism aimed at the same gap's other half; the
lower-face transfer with the LF40 ledger; the prefix-unit ladder; the
PROPER-LF40 warning. Shared blind convergence: the intertwiner, the
LF40/upper separation, `mu_4`-sector bookkeeping. However, the three
load-bearing *operational* claims of the Opus round (allocation headline,
`GATE-MARCH`, Card-B rates) all required the §6 repair, which neither
sealed report contained and which this review had to construct. Net: Opus
added real value at the theorem layer, comparable in size to — and
complementary with, not dominating — my own round; the allocation-facing
layer should not be consumed unrepaired.

## 13. Checks actually run (this session, all desk-scale exact)

1. SHA-256 of both mandatory inputs (match / recorded); of my sealed
   submission (matches delta); of every consulted source (§14).
2. Full reads: Opus report, post-seal delta, my sealed submission,
   corrected-theorem review `1cc41972`, R7R1 sol report, AUDIT 19:37Z /
   18:02Z / fixed-`H` endpoint blocks, branch-P preregistration; targeted
   reads: R7R1 fable5 review (D34/D35 block), APPROACHES row 43, D3
   `RAW_INPUT.json`.
3. Hand proofs: T1 steps 1–4 (étale, decomposition, `b_1`, both
   `c`-formulas = `gcd`); `j = m mod 4`; `4|e_i(12−m) ⟺ 4|e_i m`; the
   §6 vacuity theorem (gauge-polynomiality + `e ≥ 0` bookkeeping, NL
   pole-exponent count `≤ (n+2)/4 − 2d`); the avenue-43 `h'(u)` lemma;
   `N = ∅ ⇒ td = 1, b_1 = 0`; the `F_n`-linear binomial coefficient
   `p^{n+2}/(4H^2)` re-derivation, with the single-slot check
   `F = H^2 + F_6 t^6 ⇒ q_6 = F_6/4` exactly.
4. Exact harness `/tmp/f5_xreview_rowranks.py` (fresh, Fraction-based,
   SHA-256 `3ea962e1…0dd5b`, /tmp only): window census 121/124 and
   `F_{≥15} = 0`; `k`-schedules, `42/51/12/87 = 3·b_1`, `c = gcd` on all
   four fixtures; budgets 57/58, 51/52 (and control 39/40); row-25/26
   receivers (3,4)/(4,4); the licensed-vs-shifted rank tables of §6 on P
   and Q, rows 23–36, stable under `M ∈ {4,6}`, `D ∈ {90,110}`
   (asserted).
5. F 124 / G 276 positive-weight recount with per-weight histograms from
   the frozen D3 `RAW_INPUT.json`; G max weight 21 confirmed.
6. Post-seal delta conformance sweep over the Opus report (§8).

Not done: no AWS contact of any kind; no live-lane inspection; no
`jc2-lean` access of any kind (never entered, listed, searched, or read);
no Gröbner or other heavy algebra; the §6 linear-in-G imposition run is
specified, not executed; no canonical ledger edited (the E0 erratum is
*proposed* here for the coordinator, not applied).

## 14. Source pins (SHA-256, recomputed this session)

```text
49dd042a15670f082ea4335610150eee3022fc7a37282df200e2ae3a052ea0a0  xmodel/ideation-20260827T2137Z-opus5.md (pinned input, match)
0e09faeb69480b7594864199fbd061291af490cf8e514d1795784fbf00ad9bee  xmodel/ideation-20260827T2137Z-postseal-truth-delta.md (recorded)
edd383ad33838268cc7e700f2aa913dab73eb6744a60133a131a69eb7ef476bb  xmodel/ideation-20260827T2137Z-fable5.md (matches delta custody)
1cc41972d5049e68b8464a634c1cfae48ec5e0e1ba995475fa90998f7aad3984  xmodel/ideation-20260827T1808Z-opus5-hostile-review-fable5.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
60e6b274ca6daa64dd5dc2ddb9cd62984dbefff3ae04d612f2ec36fe1e1e26bf  cases/ggv_8_28_upper_endpoint_branch_p_20260827/PREREGISTRATION.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
ff7f774e072caf4433e95575ea6f8c5f6e8c9a124a3ca20636d5d5510d2b0ac3  AUDIT.md (working copy at read time)
ade8e0980c8c66c008da7eb57230abb222ff6c199b41c2151bc5506151e865aa  APPROACHES.md (working copy at read time)
3ea962e18f9505289391f4a85fb852d8736dc344317099d8fca8defd1bf0dd5b  /tmp/f5_xreview_rowranks.py (staged /tmp only, not a repo artifact)
```

## 15. Scope and firewall ledger

This review promotes nothing by itself. T1/T2 are recommended for
promotion by the coordinator; T3 and erratum E0 are review findings that
require different-model confirmation (the §6 discriminator is the
designated check) before entering the canonical record. Nothing here is a
face landing, family exclusion, Keller-pair statement, `D22 = 1`
solvability result, coverage/landing progress, K00 result, LF40
prediction, or JC2 conclusion. The §6 tables are statements about one
instrument class (licensed class gates, linear parts) on two frozen
fixture shapes; they say nothing about the mixed nonlinear prefix, raw
support constraints, rows ≤ 21, or the G-side, which remain the binding
side of the face problem. All live AWS lanes, the held quotient, and
Box02/Box03 were untouched and uninspected. Exactly one file was written
(this report); `/tmp` staging only otherwise; `jc2-lean` was never
touched in any way. My persistent memory contains summaries of my own
prior reviewed campaign work; every load-bearing fact used here was
re-verified against frozen artifacts this session, and the one place
where memory and the frozen record could have diverged (the promoted
stable-range claim) is exactly where this review filed an erratum against
my own prior work — affirmative evidence the audit is not an echo.

Model identity: Fable 5, exact model ID `claude-fable-5`.
Report path: `xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md`.
