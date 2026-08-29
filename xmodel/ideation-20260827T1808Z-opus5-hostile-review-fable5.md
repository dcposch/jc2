# Hostile different-model review — Opus5 `DR-INDEX` / capacity claims

Reviewer model identity: **Fable 5** (`claude-fable-5`), hostile reviewer.
Date: 2026-08-27.

Reviewed producer report:
`xmodel/ideation-20260827T1808Z-opus5.md`, SHA-256 recomputed and matching
`a9b2eb9023ac78733dcbf100e9b584e0445a894edd4098026a073f8ec87e5cff`.
Common packet: `xmodel/ideation-20260827T1808Z-packet.md`, recomputed and
matching `e388864250cdaa7bd23d5eb0babe8929bf0c02d80758ae91d708202ea9e2f6cc`.

Scope of this review: audit of every load-bearing mathematical claim in the
producer report, with the six charged foci.  Desk-scale exact arithmetic
only; no AWS, no live-job contact, no `jc2-lean` access, no canonical-ledger
edit.  This file is the only artifact written to the repository.

## 0. Independence disclosure (read first)

The shared workstation memory for this project contains a summary of the
producer's own law (`jc2-derham-gate-codimension-law`), written from the
producer session's perspective ("my blind ideation submission") and honestly
labelled there "mine, unreviewed, not promoted".  I am a different model, but
I share that persistent memory store.  Firewall applied: every verdict below
rests on (a) my own fresh hand derivations, recorded inline; (b) my own
independently written exact-`Q` harness (`/tmp/fable5_drindex_audit.py`, not
retained in the repository, method described below); and (c) direct reads of
the frozen campaign artifacts (R7R1, R5, R6, D3 raw input, D5G35, the two
pinned q-gate reviews, APPROACHES/AUDIT rows).  The review found several
material errors that the memory summary does **not** contain (window census
121 vs 126, `>=114` refuted, control count 83 vs 87, stable range 31 vs 30,
infinite-license scope gap), which is affirmative evidence the audit is not
an echo of the shared memory.

## 1. Summary verdict

The central mechanism is **correct and better licensed than the producer
himself claims**; the headline capacity numbers are **arithmetically wrong at
the margins** because the frozen D3 polygon windows are smaller than the
`K[X]_{<=16-j}` windows he assumed; and the headline sentence "the tower
cannot empty a degree-8 face" **overreaches its proof**, which caps only the
determinant-anchored rows 23–34, not the infinite tower that the exact
identity licenses.  One numeric lower bound (`>=114`) is refuted as stated.
Nothing in the report is unsound at the level of the connection, the index
formula, the `k_m` identification, or the row-25/26 predictions, all of which
I verified independently, including by deriving the actual row-25/26
campaign operators from frozen promoted formulas.

## 2. Atom-by-atom verdicts

| # | Atom (producer's claim) | Verdict |
|---|---|---|
| 1 | Rows 23/24 operators are `H^1_dR(A^1\Z(H), d+(m/4)dH/H)` gates | **CONFIRMED** (derivable from promoted R7R1; operator identities re-proved by hand both branches) |
| 2 | `dim H^1 = r-1+k_m`, Deligne index, signs/hypotheses | **CONFIRMED** (char 0, rank one, log poles incl. infinity, `U` affine; algebraic = analytic by regularity; sign-insensitive in `m`) |
| 3 | `k_m = 1 iff 4 | e_i m` **is** the R5 mode schedule | **CONFIRMED** (R5's frozen statement is integrality of `(12-n)e_i/4`, no positivity clause; identity `4|e_i(12-m) ⟺ 4|e_i m` exact) |
| 4 | `nu_m ≡ m/4 (mod Z)` from the `mu4` character, all rows | **CONFIRMED** (matches promoted `q_n^sigma = zeta^{n+2} q_n`; second independent derivation from the determinant's bilinear slot structure given below) |
| 5 | Extrapolation of the gate architecture to rows 25–34 | **CONFIRMED WITH REPAIR (in producer's favor)** — not a conjectural leap; derivable from promoted (0.2)+(0.4); artifact-level imposition run still outstanding |
| 6 | Row-25/26 predicted codims 3,4 (P) / 4,4 (Q) | **CONFIRMED** (my independent harness, exact `Q`, pole-cap stable; operators derived from frozen formulas, not assumed) |
| 7 | Stable range `m <= 39 - deg H` | **CONFIRMED WITH REPAIR** — correct for the idealized windows `[0..38-m]` he used; under the **frozen** polygon windows the control loses row 31 (observed 6 vs 7) |
| 8 | Truncated rows 32–34 on `X^8-1` measure 7,6,5 | **CONFIRMED** (reproduced exactly); but see #10 for the bookkeeping error it feeds |
| 9 | Capacity table: 126 F-slots; net gain `>0` per row for `j <= 16-r` | **REFUTED AS STATED / REPAIRED** — frozen windows give **121** slots for `j<=12` (F_9..F_12 have a low-degree polygon cut: dims 7,6,5,3); net gain is negative at `j=12`, `r>=4` |
| 10 | Lower bounds `>=78`, `>=66`, `>=114`, `>=43` | **`>=78`, `>=66` CONFIRMED WITH REPAIR** (survive via the exact class-count: `121-42=79`, `121-51=70`); **`>=114` REFUTED** (correct value `121-12=109`); control `>=43` rests on mixing an in-window count (83) with a conditions count (true class-count 87, honest bound `>=34`) |
| 11 | "The R7R1/de Rham tower cannot empty a degree-8 face" | **CONFIRMED WITH REPAIR (scope)** — proved only for the `O(t^35)`-licensed rows 23–34; the frozen target implies `E = t^22` **exactly**, which licenses an infinite tower (R7R1's own client paragraph and D5G35's `finite_tower_claim: NOT MADE`), for which no capacity bound is proved |
| 12 | Endpoint `M(Y)=4HY'+6H'Y` is `L_nu` at `nu ≡ 22/4`; R4-death = one class in `H^1(∇_22)` | **CONFIRMED WITH REPAIR** — family membership exact; but the endpoint obstruction lives in the polynomial-window presentation only: I computed that on branch P the with-poles row-22 gate is **vacuous** (codim 0), see §5.3 |
| 13 | Lower-face: `gamma ≡ 3 (mod 4)` rederivation; sufficiency suggestion; `r=2` | **CONFIRMED AND STRENGTHENED** — my sweep proves polynomial solvability **iff** `gamma ≡ 3 (mod 4)` for `gamma = 1..11`, minimal degree exactly `3 deg K/4`; completeness argument closes all degrees |
| 14 | §9 insight: resonance cuts harder; control fixture ~2x overstates | **CONFIRMED** (even rows 4 vs odd rows 3 on P, verified; `r=8` control vs `r<=5` survivors verified via R6) |
| 15 | R6 survivors at `h=8` have `r<=4` (b0) or `r<=5` (b2) | **CONFIRMED** — R6 `RESULT.json` lists exactly strata b0/b2 (codim 4, dim 4), and the mode-degree formula `r=(h-3b+2)/2 >= 0` excludes `b>=4` at `h=8` |
| 16 | §3.2 index/irregularity avenue; Euler–Poincaré with irregularity | **CONFIRMED as formula, PROVISIONAL as avenue** (untried, well-posed first computation) |
| 17 | Exact identities `12F_XG-8FG_X=-8P^20W_X`, `F_XG_t-F_tG_X=8P^19(P_XW_t-P_tW_X)` | **CONFIRMED** (complete hand proof, three lines each; matches R7R1 (0.1) with the correct minus sign, which I pinned independently via the promoted row-23 operator) |
| 18 | §3.3 row-33 reopen at twisted scope | **CONFIRMED** (the frozen revival condition in APPROACHES row 33 is quoted verbatim and the twisted class `d+(m/4)dH/H`, residues `m e_i/4`, meets it; untwisted case = `m ≡ 0 (4)` integral residues, exact) |
| 19 | §3.3 rigidity reading of rows 25/26 | **CONFIRMED as fact, PROVISIONAL as unification** — rank-one local systems on `P^1` minus points are rigid (standard); the "same phenomenon" reading of the passport null result is heuristic, and marked as such |
| 20 | Novelty labels: law/derivation/capacity `NEW`; sub-atoms `KNOWN` credited | **CONFIRMED** (greps reproduce his null results; both KNOWN credits located verbatim in `46736edc...` and `56a4b940...`; no duplication of promoted q1/q2 codimension atoms — the law reproduces them and says so) |
| 21 | Cards `DR-INDEX` / `LOW-R` / `K00-RAT` | **DR-INDEX CONFIRMED WITH REPAIR** (discriminator remains the right artifact test; its mathematical risk is now much lower than the card states); **LOW-R CONFIRMED WITH REPAIR** (the "frozen, unmodified compiler" hard-codes `H=X^8-1`; an H-swap is a mutation producing a new case, as its own rollback subtree admits); **K00-RAT PROVISIONAL** (design sound, dependencies quoted at correct scope) |
| 22 | Disposition vector factual premises (rows 16, 25, 26, 33, 36, 39, 45) | **CONFIRMED** (all quoted blocking conditions/verdicts located verbatim in APPROACHES.md; row-45 status correction is accurate) |

## 3. Focus 1 — the identification and the index formula

**The identification is a theorem, not an analogy, for every licensed row.**
Chain, all promoted or hand-proved here:

1. R7R1 (items 1–7 CONFIRMED by prior different-model review) gives the
   exact conjugacy `(0.2)`: `w_{n+22}' = -(n+2) q_n/16`, so determinant row
   `m = n+22` is, given rows below, the exactness of `q_n dX` in
   `L = K(X)(p)`, `p^4 = H`.  `Q = P^2 = F^{1/4}`, so **`q_n` is F-only**;
   the licensing rule (`E = t^22 + O(t^N)` licenses `n+22 < N`) is frozen in
   D5G35's `RESULT.json`.
2. Promoted repair 2 of R7R1: `q_n^sigma = zeta^{n+2} q_n`.  Since
   `n+2 ≡ n+22 (mod 4)`, `q_n` is pure of character `chi^m`.  Exactness in
   `L` of a pure-character form descends to the vanishing of its class in
   the `chi^m`-isotypic twisted de Rham complex on `U = A^1 \ Z(H)`; the
   antiderivative ansatz `c·p^{m mod 4}` gives, e.g. for `n=1`
   (`q1 = F1/(4p^5) = (F1/(4H^2))p^3`): `4Hc' - H'c = F1` after clearing —
   **exactly** the promoted branch-P/branch-Q operators.  I re-derived both:
   `H=A^2`, `S=Q/A` gives `2(2AQ'-3A'Q)`; `H=A^2B`, `S=Q/A` gives
   `4ABQ'-(6A'B+AB')Q = T_Q`.  Row 24 (`c=0`) gives `F2 = 4HS'`, the
   promoted residue gate.  The sign of the `t(F_XG_t-F_tG_X)` term in `E` is
   pinned by this: the opposite sign yields `4ABQ'-2A'BQ+AB'Q ≠ T_Q`.
3. `dim H^1_dR(U, ∇) = r - 1 + k_m`: `∇ = d + ν dH/H` has log poles at the
   `r` finite points and at infinity (residue `-2m ∈ Z` there, irrelevant
   since `∞ ∉ U`), hence is regular singular everywhere; Deligne's index
   formula for algebraic de Rham of a regular-singular connection on an
   affine curve gives `h^0 - h^1 = χ_top(U) = 1 - r`, and
   `h^0 = k_m ∈ {0,1}` with flat section `∏ p_i^{-m e_i/4} ∈ O(U)^×` iff
   every `m e_i/4` is an integer.  Hypotheses: characteristic zero; rank
   one; regularity (holds); `U` affine.  Algebraic-vs-analytic: they agree
   here precisely because the connection is regular; irregular connections
   would add `-Σ Irr` (Euler–Poincaré/Malgrange), which is what §3.2
   correctly proposes to exploit.  Signs: `k_m` is invariant under
   `m ↦ -m`, so the twist-sign convention cannot corrupt the count.

**A sharpening the producer needs (representative dependence).**  The
*class-vanishing set* is representative-independent, but the *window gate*
attached to an integer-shifted operator is not, and can silently become
vacuous, not merely renormalized.  Exact counterexample, computed: on branch
P (`H = A^2`, `A` squarefree quartic) at row 22, the reduced-representative
gate (`c = 2`, poles allowed) has codim 4; the campaign representative
`c = 6` **with poles allowed** has codim **0** — because
`F = L_6(S) ⟺ FA/4 = (A^3 S)'`, and a polynomial `FA` has no residues, so
every window `F` passes; while the polynomial-only `Y`-presentation has
codim 7 on the control (`= promoted M-cokernel 7`, reproduced).  On the
squarefree control all representatives give 7; at row 23 all of
`c ∈ {3,-1,11}` give 3.  So his §3.1 boldface warning is correct and is a
theorem-level constraint, not a bookkeeping tip: **the licensed gate is the
one carried by `q_n`'s exact `p`-power; integer shifts can kill it.**

## 4. Focus 2 — `k_m` versus the promoted R5 schedule

R5's frozen statement (read directly): "There is a nonzero rational
homogeneous mode at weight `n` exactly when `q_n e_i` is integral for every
`i`", `q_n = (12-n)/4`, modes `R_q = ∏ p_i^{(12-n)e_i/4} ∈ K(X)` —
**rational**, so no positivity clause; scope "below weight 22".  The
identity `4 | e_i(12-m) ⟺ 4 | e_i m` is exact (`4 | 12 e_i`).  Two
consequences verified:

- The packet's polynomial-kernel schedule (even `n = 2..12` on P;
  `n = 4,8,12` on Q) is exactly the integrality condition **plus** the
  positivity cutoff `n <= 12` from `R_q` polynomial; on P integrality is
  `2|n`, on Q it is `4|n`.  Both reproduced.
- My independent derivation of the slot-`m` linear part of `D_m` (below)
  produces the operator `4HR' + (m-12)H'R`, whose kernel is literally
  `H^{(12-m)/4} = R_q`.  So R5's mode, the packet's kernel schedule, and
  `k_m` are one object in three presentations; `k_m` extends R5's
  integrality beyond weight 22 through `h^0(U, ∇_m)`, where positivity is
  no longer required because `O(U)` inverts `H`.  Multiplicities enter only
  through `e_i` (verified on `e`-profiles `{2,2,2,2}`, `{2,2,2,1,1}`,
  `{3,2,2,1}`, `{4,2,1,1}`, `{6,1,1}`, `{8}`, `{4,4}`, `{1^8}`); infinity
  contributes no condition; the twist-representative freedom is harmless
  for `k_m` (sign/shift invariant).  **CONFIRMED.**

Second independent derivation of the exponent rule, from frozen campaign
formulas only (no `mu4`): write `E = Σ_{a+b=m}[(12-b)F_a'G_b - (8-a)F_a G_b']`
(the frozen D5G35 `E`, re-expanded).  The slot-`m` linear part at background
`(F_0, G_0) = (H^2, H^3)` is, after the substitution `R_m = G_m - (3/2)HF_m`,
**exactly** `-2H·[4HR_m' + (m-12)H'R_m]`: the `F_m`-terms cancel identically
(coefficient `-3(8-m) - 12 + 3(12-m) = 0`).  So `4ν ≡ m-12 ≡ m (mod 4)` with
no appeal to the deck action, and the endpoint `m=22` gives `4HR'+10H'R`,
which is `M(Y)/H` under `Y = HR` — the promoted "`r∘(H·)` diagonal iso".
The producer's character derivation and this slot derivation agree at all
`m`; his anchor rows 22/23/24 (`chi^2, chi^3, chi^0`) match promoted
`zeta^{n+2}`.

## 5. Focus 3 — rows 25/26 and the extrapolation license

**5.1 The extrapolation is derivable, and I derived it.**  From
`Q = F^{1/4} = p^2(1+f)^{1/4}`, `f = Σ F_j t^j/H^2`, and the inversion of
`t = sP(t)`, the binomial gives `q_n = F_n p^{n+2}/(4H^2) + NL(F_1..F_{n-1})`
for every `n`.  I computed the `n=3` case in closed form by hand:

```text
q3 = p^5 [ F3/(4H^2) - (3/32) F1 F2/H^4 + (11/512) F1^3/H^6 ] ,
```

and verified `q1, q2, q3` against six random exact fixtures (series
inversion over `Q`, all coefficients matched; `q1, q2` reproduce R7R1
`(0.4)` on the nose).  Clearing the character gives the **actual campaign
row-25 gate**: `∃c ∈ O(U): 4Hc' + H'c = F3 - (3/8)F1F2/H^2 + (11/128)F1^3/H^4`,
i.e. affine in `F3` with linear operator `4Hc' + H'c` (`4ν = 1 = 25 mod 4`);
row 26 likewise has `4Hc' + 2H'c` on the `F4` slot.  So the "cheapest actual
row-25/26 discriminator" is not hypothetical: it is these two operators with
these inhomogeneities, derived from frozen promoted formulas, not from the
abstract family.

**5.2 The discriminator values.**  My independent harness (fresh
implementation: pole-capped divisibility solve `S = T/rad(H)^{M}`, exact
remainder conditions, `Fraction` Gaussian rank; cap-swept) gives, in the
frozen `F3`/`F4` windows (`deg <= 13` / `deg <= 12`):

```text
row 25: branch P codim 3, branch Q codim 4   (predicted 3, 4)
row 26: branch P codim 4, branch Q codim 4   (predicted 4, 4)
```

together with full agreement with `r - 1 + k_m` at rows 22–31 on: generic P,
generic Q, `X^8-1` (rows 23–31: 7,8,7,7,7,8,7,7,7 = 65), `(X-1)^8` (codim 1
throughout), `(X^2-1)^4` (codim 2 throughout), and all four Grok46
degenerations at rows 23/24 (3,3,2,3 and 4,4,3,4), reproducing the promoted
q1/q2 codimensions 3/4/4/5 and Grok46's §1.3 table from `r` alone.

**5.3 Theorem-about-family vs theorem-about-campaign-rows.**  After this
review the gap is *narrower* than the producer's honest ledger states: his
leap 2 ("the `R_n` architecture may break above row 24") is effectively
closed at the mathematics level by (0.2)+(0.4)+binomial — the row-`m`
F-side necessary condition **is** the `H^1(∇_m)` class condition for every
licensed `m`, full stop.  What remains genuinely outstanding at the
campaign-artifact level: nobody has yet *imposed* the frozen 734-generator
target and exhibited the row-25 gate inside a compiled case.  Card 1's
discriminator therefore stays worthwhile as custody, but its FAIL branch
("a promoted-claim correction") is now very unlikely to fire for
mathematical reasons; if it fires, look for an implementation defect first.
Related repair from §3: the *endpoint* (row 22) is **not** a with-poles
`H^1` gate — on branch P that gate is vacuous (codim 0, §3 above), and the
promoted R4 endpoint-death lives entirely in the polynomial-window
presentation.  This strengthens, rather than weakens, the producer's own
support-pivot conclusion: the one row where the campaign has a proved death
is support-driven, not class-driven.

## 6. Focus 4 — stable range and the capacity table

**6.1 The frozen windows are not `K[X]_{<=16-j}`.**  Decoded from the frozen
D3 `RAW_INPUT.json` via the D5G35 compiler's own `enumerate_polygon`
(`f_i_j`: X-degree `i`, weight `w = 8+3i-j`, polygon `max(0,4i-8) <= j <=
3i+8`): slot `F_w` has X-degrees `ceil(max(0,(w-8)/3)) .. 16-w`.  The upper
bound matches the producer's assumption; the **lower cut is real** for
`w >= 9`.  Verified against the compiler's frozen census (F: 124
positive-weight slots, G: 276 — both reproduced exactly).  Consequences:

```text
dim F_w, w=1..12:  16 15 14 13 12 11 10 9 | 7 6 5 3   (total 121, not 126)
dim F_13, F_14:    2, 1                    (full F total 124)
```

- The `F1` 16-window and `F2` 15-window of the promoted q-gates are intact.
- The per-row claim "net gain `(17-j) - (r-1+k_m) > 0` for all
  `j <= 16-r`" is **false at `j >= 9`**: at `j=12`, branch P, the window has
  3 dimensions against 4 class conditions.
- The stable range under the frozen windows is `m <= 30` on the control
  (row 31 observed 6 vs predicted 7 once the low-degree cut is applied);
  rows 31 on P and Q still meet the law (3 and 4, verified).  His
  `m <= 39 - deg H` is correct only for the idealized `[0..38-m]` windows
  his harness (and my first pass) used.

**6.2 Corrected capacity arithmetic.**  The licensed gate at row `m` is
`[q_n] = 0 ∈ H^1(∇_m)`: exactly `r-1+k_m` scalar equations on
`(F_1..F_n)` regardless of window truncation (truncation only redistributes
which slots can absorb them).  Rows 23–34 therefore impose at most:

```text
branch P (r=4):  Σ = 42    free >= 121 - 42 = 79   (producer said >= 78: survives)
branch Q (r=5):  Σ = 51    free >= 121 - 51 = 70   (producer said >= 66: survives)
r = 1:           Σ = 12    free >= 109             (producer said >= 114: REFUTED)
control (r=8):   Σ = 87    free >= 34              (producer said 83 and >= 43)
```

The producer's 83 = 65 + 18 mixes the class count (65, rows 23–31) with an
in-window image count (18, rows 32–34); the class count for 32–34 is
8+7+7 = 22, total 87.  With the true frozen windows the in-window cuts for
rows 29–34 on the control are 7,7,6,6,5,3.  Nonemptiness of the solution
locus is exact (`F_j = 0` for all `j` passes every gate), so the Krull
bound `dim >= 121 - Σ` is rigorous given the window census; his `>= 78` and
`>= 66` stand only via the exact `Σ` (his own loose `12·r` route gives 73
and 61).  Double counting is in the safe direction (dependent equations cut
less); the nonlinear coupling enters only through the `NL(F_{<n})` shifts,
which move the affine conditions but not their count.

**6.3 The scope gap (load-bearing).**  Imposing the full frozen target
`D0..D21 = 0, D22 = 1, D23..D34 = 0` with `D35 ≡ 0` (structural) forces
`E = t^22` **exactly**, and R7R1's client paragraph plus D5G35's
`finite_tower_claim: NOT MADE` record that the exact identity licenses the
**infinite** tower `q_n` for all `n >= 1`.  Rows `n = 13, 14` land on
2- and 1-dimensional slots; rows `n >= 15` are `r-1+k_m` conditions each on
the *same* 124 F-parameters, infinitely many in total.  Noetherianity makes
finitely many suffice, but no bound is proved.  Therefore the honest
statement is: **the determinant-anchored sub-tower (rows 23–34, i.e. the
`O(t^35)` license) cannot empty the face; whether the full licensed tower
can remains open.**  The producer's §5 decisive object ("rows 23–34") is
scoped correctly; the §3.1 headline sentence and the memory phrase "caps the
whole tower" are not.

## 7. Focus 5 — rigidity, rank two, irregularity, avenues 16/25/33

- **Rigidity of rank one on `P^1` minus points**: standard and correct (a
  character of `pi_1` is determined by its local monodromies; no moduli).
  The inference "this is *why* the q-tower is information-poor and *why*
  the 169-passport screen produced no kill" is an interpretive unification
  across different categories (abelian characters vs permutation
  monodromy); sound as a heuristic, not a theorem, and the producer flags
  it as a connection, not a claim.  **CONFIRMED as fact / PROVISIONAL as
  unification.**
- **Rank two**: keeping `(F,G)` coupled gives a rank-two object with
  `χ = 2(1-r)` and, generically, positive-dimensional moduli (non-rigid) —
  directionally correct; no theorem yet that the campaign rows realize a
  non-rigid family.  **PROVISIONAL.**
- **Irregularity**: Euler–Poincaré `χ_dR = rank·χ_top - Σ Irr` is the right
  formula; every connection used so far is regular (verified for the whole
  `∇_m` family: log poles only), so the term is currently zero; the
  proposed first computation (irregularity of the `t`-direction pushforward
  at `t=0` on one frozen face) is well-posed and untried.  The two exact
  bivariate identities feeding it are proved (hand computation, three lines
  each, reproduced during this review).  **CONFIRMED formula / PROVISIONAL
  avenue.**
- **Row 33 reopen**: APPROACHES row 33's frozen revival condition ("any
  revival needs a genuinely twisted/client-specific class") is quoted
  accurately, and `∇_m` with residues `m e_i/4 ∉ Z` for `m ≢ 0 (4)` meets
  it; the untwisted automatic case is exactly `m ≡ 0 (4)`.  Narrow reopen
  as a GGV sub-lane is the correct disposition.  **CONFIRMED.**
- **Rows 16/25/26 raises**: factual premises verified verbatim (row 16's
  "no concrete invariant named", row 25's passport null result and S:7
  escape, row 26's "best cheap untried" consensus).  One coordinator-level
  note, not a producer error: the earlier same-day Fable5 ideation
  (`0935Z`) proposed a *different* row-16 invariant (Bernstein–Sato
  b-function data); it did not survive into the 13:49Z/16:06Z dedup
  baselines, and the packet's blindness rules made it unreadable to the
  producer.  The de Rham index invariant is distinct and now has promoted
  anchors; the raise is justified either way.  **CONFIRMED.**

## 8. Focus 6 — novelty and history

Repository greps (excluding the round pattern) reproduce the producer's
nulls for `rank-one connection`, `twisted de Rham`, `rigid local system`,
`middle convolution`, `chi_dR`, `information capacity`; `Deligne` appears
once (unrelated websweep), `Malgrange` twice (row-45 tautology context and
the `0935Z` b-function note), `irregularity` once in a 2026-08-24 zero-base
ideation in a different mechanism (conormal conductor of a pencil, not this
connection family).  The two `KNOWN` sub-atom credits are accurate: "q2
linear codim = number of distinct roots, `c(X-a)^8` exceptional" is in
`46736edc...` (§4.3/§5.1, lines sighted) and is Grok46 item 4; the indicial
coefficient `c(m+e/2)` is in `46736edc...` §5.1.  Grok46 §1.2 does decline
the intrinsic count exactly as quoted ("Opus did not claim `2g+residues=4`.
I do not either"), and the producer's resolution — the right invariant is
`χ` of the affine **base**, not the genus of the Kummer cover — is the
correct and new step.  No duplication of promoted q1/q2 codimension
results: the law *reproduces* them as consistency anchors and labels them
as such.  The single-law mechanism, the `h^0/h^1`-linkage to R5, the
`m/4` exponent rule, the stable-range analysis, and the capacity argument
are `NEW` in this campaign.  **CONFIRMED**, with the `0935Z`/`0453Z`
closest-hits above added for the record.

## 9. What may be promoted now, and what must wait

**Promotable now (with the repairs of §6 folded in):**

1. **Gate-law theorem (corrected statement in §10)**: identification,
   index dimension `r-1+k_m`, `k_m`≡R5 integrality, the `m mod 4` operator
   rule with its two independent derivations, and the in-window codimension
   values at rows 22–30 (all fixtures) plus rows 31 on P/Q — backed by the
   promoted R7R1/R5/D5G35 chain, my hand derivations, and two independent
   exact harnesses.
2. **Row-25/26 gate operators and codimensions** as *derived campaign
   gates* (operators `4Hc'+H'c`, `4Hc'+2H'c`; codims 3/4 and 4/4), pending
   only the artifact-level imposition run for full custody.
3. **The `q3` closed form** above (new exact formula, verified).
4. **Lower-face iff**: `4Kg'-3K'g=4K`, `K=xi(xi-rho)^gamma`, has a
   polynomial solution **iff** `gamma ≡ 3 (mod 4)` (checked exhaustively
   `gamma = 1..11`; completeness across all degrees by the leading-term
   argument: solutions can only have `deg g ∈ {1, 3·deg K/4}`), minimal
   degree exactly `3 deg K/4` — upgrading the promoted necessity to a desk
   iff on this range, as the producer conjectured.
5. **Capacity theorem, rescoped and renumbered**: rows 23–34 impose at most
   42/51/12/87 conditions on the 121 frozen F-parameters
   (`n <= 12`), leaving `>= 79 / 70 / 109 / 34` free on
   P / Q / `r=1` / control; the sub-tower cannot empty the face.
6. **Resonance-cuts-harder** (§9) and the control-fixture ~2x overstatement,
   with the R6 `b0/b2` closure (`r=(h-3b+2)/2 >= 0` kills `b >= 4` at
   `h=8`).

**Must remain proposed discriminators / not promotable:**

- Any statement about the **full infinite licensed tower** (§6.3), including
  the unqualified headline "the tower cannot empty the face" and any
  budget conclusion that relies on it beyond rows 23–34.
- The specific numbers `>= 78 / >= 66 / >= 114 / >= 43` in their published
  form (use 79/70/109/34 over 121).
- Rows 32–34 (and, on the control, 31) law values — out of stable range
  under frozen windows; solve densely (his ROWORACLE flag list should be
  31–34, and its predicted-rank checksum must use the polygon windows with
  the low-degree cut).
- `LOW-R`'s `H=c(X-a)^8` admissibility (unchecked, as the producer flags),
  and the card's "frozen, unmodified compiler" wording (the compiler
  hard-codes `H=X^8-1`; the run is a one-line H-mutation into a new case).
- `K00-RAT` (sound design; different lane; nothing verified here).
- §3.2 irregularity avenue and §3.3 rank-two escape (well-posed, untried).

## 10. Shortest corrected theorem statement

> **Theorem (de Rham gate law, corrected).**  Char `K = 0`,
> `H = h_0 ∏ p_i^{e_i}` of degree 8, `U = A^1 \ Z(H)`, `r = deg rad H`.
> For `n >= 1` put `m = n+22` and `∇_m = d + ν dH/H` for any
> `ν ≡ m/4 (mod Z)`.  (i) Under the R7R1 license
> (`E = t^22 + O(t^{m+1})`), the F-side necessary condition of determinant
> row `m` is `[q_n dX] = 0` in `H^1_dR(U, ∇_m)`, where
> `q_n = F_n p^{n+2}/(4H^2) + NL(F_1..F_{n-1})`; the class condition is
> representative-independent, the operator presentation
> `4HS' + (m mod 4)H'S` is not.  (ii)
> `dim H^1_dR(U, ∇_m) = r - 1 + k_m`, `k_m = 1` iff `4 | e_i m` for every
> `i`, and `k_m` coincides with the promoted R5 integrality schedule via
> `4 | e_i(12-m) ⟺ 4 | e_i m`.  (iii) In the frozen D3 windows
> (`F_n`: X-degrees `max(0, ⌈(n-8)/3⌉) .. 16-n`; 121 parameters for
> `n <= 12`), the observed gate codimension equals `r - 1 + k_m` for
> `23 <= m <= 30` (and at `m = 31` when `r <= 5`), and rows 23–34 impose at
> most `Σ_{m=23}^{34}(r-1+k_m)` = 42 (P) / 51 (Q) / 12 (`r=1`) / 87 (`r=8`)
> conditions, so the solution locus (which contains `F = 0`) has dimension
> `>= 79 / 70 / 109 / 34` respectively.  (iv) No bound is asserted for the
> infinite tower licensed by the exact identity `E = t^22`, for `D22 = 1`,
> or for rows `<= 21`.

## 11. Checks actually run (this review)

1. SHA-256 of the producer report and packet (match); byte-hash spot-check
   of both pinned q-gate reviews (`46736edc...`, `56a4b940...` reproduced).
2. Hand derivations, complete in §§3–5: row-23 operator identities on both
   branches from `q1 = F1/(4p^5)`; the slot-`m` linear part of `D_m` with
   exact `F_m`-cancellation and operator `4HR'+(m-12)H'R`; `Y = HR`
   endpoint match; `q3` closed form via binomial + series inversion; the
   two bivariate `P^8/P^12W` identities; the Deligne/Euler–Poincaré
   dimension count and its hypotheses; `4|e_i(12-m) ⟺ 4|e_i m`;
   lower-face degree-completeness argument.
3. Independent exact-`Q` harness (fresh code, `/tmp`, ~100 row-instances,
   pole-cap swept): law verified rows 22–31 on 9 fixture families
   including all four Grok46 degenerations (3,3,2,3 / 4,4,3,4), promoted
   codims 3/4/4/5 reproduced, control rows 23–31 sum 65, truncated rows
   32–34 = 7,6,5 (idealized windows) and 29–34 = 7,7,6,6,5,3 (frozen
   windows); row-25/26 discriminators 3,4 (P), 4,4 (Q); gauge sweep
   `c ∈ {3,-1,11}` stable at 3 (row 23) and the row-22 representative
   counterexample (0 vs 4 vs 7); `q1,q2,q3` closed forms on 6 random exact
   fixtures; lower-face `gamma = 1..11` sweep (solvable exactly at 3, 7,
   11 with degrees 3, 6, 9).
4. Frozen-artifact reads: R7R1 report + its CONFIRMED review; R5 report
   statement; R6 `RESULT.json` (b0/b2, codims, mode-degree formula); D3
   `RAW_INPUT.json` full slot census (F 124 / G 276 positive-weight,
   window formulas); D5G35 README/`TARGET_GATE`/`RESULT.json` (E-formula,
   licensing rule, D23/D24 mutation gates, 734 generators, first
   generators byte-checked against my expansion); APPROACHES rows 2, 3,
   16, 25, 26, 33, 36, 39, 45; the nu17 Grok review (`gamma ≡ 3 (mod 4)`
   necessity, sufficiency open); FACEPIN lifecycle field
   (`PRODUCER_UNREVIEWED...`), consistent with the producer's stated use.
5. Novelty greps as listed in §8.

Not done: no AWS, no imposition run of the 734-generator target, no
enumeration beyond `gamma = 11`, no K00-lane verification, no reading of
any peer ideation submission from this round, no `jc2-lean` access.

## 12. Scope firewall

This review promotes nothing by itself.  It confirms, repairs, and refutes
statements *about the producer report and the frozen face instruments*
only.  No face landing, no GGV-family exclusion, no Keller pair, no
statement about `D22 = 1` solvability, no `G2-PSC`/`G2-BD`/coverage
progress, no K00 result, no order-two or maximum-twelve claim, and no JC2
conclusion follows from anything here.  The capacity statements are about
one instrument class on one frozen chart family and say nothing about the
mixed nonlinear prefix, the raw-support constraints, or rows `<= 21`,
which remain the binding side of the face problem.

**Review verdict (restated for the ledger): mechanism and row-25/26
discriminators CONFIRMED (and strengthened to derived campaign gates);
capacity claims CONFIRMED WITH REPAIR on the 121-slot frozen windows
(`>=79 / >=70 / >=109 / >=34`); `>=114` REFUTED as stated; the
whole-tower cap is out of scope of the proof and must not be promoted.**

Output path: `xmodel/ideation-20260827T1808Z-opus5-hostile-review-fable5.md`
Model identity: Fable 5 (`claude-fable-5`).  The SHA-256 of the frozen
bytes of this file is computed by `shasum -a 256` at seal and reported in
the review transmittal; this file embeds no self-hash.
