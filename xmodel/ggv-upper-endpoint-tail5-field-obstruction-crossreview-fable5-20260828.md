# Hostile cross-review: cutoff-five upper-endpoint field obstruction

Reviewer: Fable 5, independent hostile lane
Date: 2026-08-28
Producer packet: `cases/ggv_8_28_upper_endpoint_tail5_desk_20260828/`
(RESULT.md `a4f627c1…b210`, analyzer `f62fc30a…497e`)

## Verdict

`PASS — independently confirmed as stated`

## Theorem as confirmed

Fix the branch-P square baseline `C=X^4-1, H=C^2, U=H+t/2, F=U^2, G=U^3`
inside the authoritative raw determinant system
(`RAW_DIRECT_SYSTEM.json`, SHA-256 `ead2fa40…e5a0`), set every raw
deformation parameter of weight below five to zero, and impose the literal
rows `D4=…=D21=0` together with `D22=1` (rows `D0…D3` vanish identically on
this stratum, no `G22` slot exists, no `D23` is imposed).  Then this system
has no characteristic-zero field-valued point.  The exclusion is
field-radical (six squarefreeness steps), covers both branches `V0=0` and
`V0!=0` exhaustively, and asserts nothing about the nonreduced scheme, the
full branch-P family, other GGV branches, Keller pairs, or JC2.

Every load-bearing number, identity, witness, and provenance link in the
packet was reproduced by fresh code written for this review
(`/tmp/tail5rev/recon.py`, `cascade.py`, `verify2.py`, `mutate.py`; my own
polynomial arithmetic, elimination, span, and quadratic-field machinery,
with my own synthetic symbol ids).  Nothing below rests on running the
producer's analyzer.

## 1. Hashes, custody, replay

* All eight frozen principal hashes match; `sha256sum -c` passes for both
  manifests, including the two upstream raw sources.  `RAW_INPUT.json`
  (weight source) **is pinned** here — the gap I flagged in the tail6
  review is closed in this packet.
* The raw-system hash `ead2fa40…` is pinned identically by the branch-P
  packet's own `SOURCE.sha256` and by the tail3/tail6/tail7 sibling
  packets; no stale-hash divergence anywhere.
* Producer replay `python3 analyze_tail5.py --check --output .`:
  **exit 0, 20.57 s**, status `PASS`, all eight payloads regenerated
  byte-identically.  Recorded as replay only; not counted as proof.

## 2. Independent reconstruction of the raw specialization

I rebuilt the entire specialized system from first principles: the frozen
recurrence `D_n = Σ_{i+j=n} ((12−j)F_i′G_j + (i−8)F_iG_j′)`, the square
fixture pieces `F_0=H^2, F_1=H, F_2=1/4; G_0=H^3, G_1=(3/2)H^2,
G_2=(3/4)H, G_3=1/8`, and one deformation slot `X^i` per retained
coordinate at its weight.

* **All 513 generators** of the frozen raw file, specialized to weight ≥ 5,
  match my recomputation term-for-term, with coefficient 1 — no row
  scaling, no normalization anywhere.  The single constant `-1` in row 22,
  `X^0` is exactly the affine target `D22=1`.
* Specialized `D_0…D_4` vanish identically (verified), so "D0…D21=0" is
  exact even though the file starts at row 4, and the 36 imposed row-4
  equations are vacuous on this stratum; rows 5–9 constrain linearly.
* Census: 252 retained of 303 (sub-five: 7 `z_`, 10 `tt_`, 34 weight-4
  slots).  Weight table matches the name formulas `f_i_j → 8+3i−j`,
  `g_i_j → 12+3i−j` with zero exceptions.
* Prefix: 201 equations, my own sparse exact elimination gives
  **rank 89, nullity 163**.  The frozen 163-vector nullspace annihilates
  every one of my reconstructed prefix rows, has rank 163, and is complete.
* All **312 substituted constraints match mine exactly**; the literal
  endpoint is `-1 - p32*p139 + p86*p91`, i.e.
  `-1 - F7[X^0]·G15[X^1] + F11[X^1]·G11[X^0]`, signs pinned by the
  recurrence itself (the `+1` from `(12−j)=1` at `f_1_0·g_0_1`, the `−1`
  from `(i−8)=−1` at `f_0_1·g_1_0`).
* Raw-slot meanings all verified against the frozen basis: `p32=g_1_0`,
  `p86=g_0_1`, `p91=f_1_0` pure; `p139 = f_0_1` plus its forced G-lift;
  `F5[X^d]=p_{162−d}`, `F6[X^d]=p_{150−d}`, `F7[X^d]=p_{139−d}` all pure;
  `p120 = (1/2)g_0_3 + g_8_28 − 2g_4_16 + g_0_4`; `p129 = f_0_0` pure.
* The determinant makes no individual carrier a unit; the pointwise cover
  consequences `(b,c)≠(0,0)`, `(a,d)≠(0,0)` follow trivially from the
  endpoint.

## 3. Field-radical cascade D10–D15

My own staged elimination (fresh implementation, per-stage pivot
substitutions merged progressively — these are load-bearing, as in tail6)
reproduces every claim:

| row | compat/span | model check (mine) |
|---|---|---|
| D10 | 16 / 8 | span **equals** coefficients of `F5^2 mod H`; closes after `F5=C·B` |
| D11 | 16 / 9 | all 4 coefficients of `B^2 mod C` in span; post-`B=C·V` span = `{c−(3/4)p150·V0+(3/16)V0², p106−(3/8)V0²}` |
| D12 | 16 / 8 | span **equals** coefficients of `(F6−V/2)^2 mod H`; closes after `F6=V/2+C·W` |
| D13 | 16 / 9 | all 4 coefficients of `W^2 mod C` in span; post-`W=C·R` span = exactly `E13` |
| D14 | 16 / 9 | **all 4** coefficients of `(F7−R/2)^2 mod C` in span; post-`T` span = `{E13,E14}` |
| D15 | 17 / 11 | cumulative rank 12; **all 4** coefficients of `T^2 mod C` in the cumulative span; post-`T=C·Q` gives 9 rows of rank 4 ⊇ `{E13,E14,E15}` |

Squarefreeness and field semantics enter at exactly these six divisibility
promotions (`H|S²⇒C|S` twice, `C|S²⇒C|S` four times), each valid over a
characteristic-zero field because `C=X^4−1` is squarefree there, and each
correctly labelled field-radical, never scheme-level.  Degree windows are
sound (`B` deg ≤ 7, `V` ≤ 3, `W` ≤ 6, `R` ≤ 2, `T` ≤ 5, `Q` ≤ 1).  The
`b`-preserving coordinate changes (`T0=R0/2−b`, `q0=b−R0/2`, giving
`T1=−q1, T2=T3=0, T4=b−R0/2, T5=q1`) are exact invertible substitutions.
The fully composed carrier reconstruction is
`c = (3/16)V0² + (3/4)V0·R0 = (3/16)V0(V0+4R0)`, and my scalar core
matches the packet's `E13, E14, E15` symbol-for-symbol.  My per-row stage
logs match the frozen `stage_logs` in every field.

## 4. Gauge slice p129 (charge item 4)

`f_0_0 = F8[X^0]` occurs in **none of the 513 raw generators** (checked on
the full unspecialized file) and parameter 129 occurs in none of the 312
substituted constraints.  My reconstruction shows *why*: every
`F_8·G_j′`-contribution carries the factor `(i−8)=0` and `F_8′` kills the
`X^0` slot — precisely the additive symmetry `F → F+μt^8`, which changes
neither `F_X` nor `(t d/dt−8)F`.  So `p129=0` is a global additive slice
meeting every orbit, and since the constraint set is literally independent
of `p129`, the slice is a no-op for emptiness.  It is not a carrier
normalization.  **Finding:** the same mechanism gives a second,
undocumented gauge line `g_0_0 = G12[X^0]` (parameter `p69`, killed by
`(12−j)=0`, i.e. `G → G+ν·t^12`), also absent from all generators and all
constraints.  Harmless — a free line never referenced — but RESULT.md
names only the F-side gauge (documentation nit N2 below).

## 5. K17 (charge item 5)

`K17 = V0·(b·V0 + R0²)` lies in the span of my independently derived
post-D15 + D16 + D17 compatibilities.  The frozen 7-row witness
(indices 13, 17, 21, 25 in D16; 27, 31, 35 in D17 of the concatenated
list) reproduces `K17` **exactly on my rows**; my own solver finds a
different, equally valid 8-row witness — both verified by expansion.  The
cumulative invariant core over `Q[b,e,V0,R0]` has rank exactly 4 and
equals `span{E13,E14,E15,K17}` (my own forbidden-monomial-first echelon
intersection).  Falsification: perturbing one charged witness coefficient
by 1 breaks the reconstruction; mutating a charged raw D16 source
coefficient (`f_0_1·g_4_15`, `−4→−3`, in the X³ generator) makes the
frozen witness fail (charge-sensitive), while `K17` itself remains in the
mutated span — see §8 for the reading of that.

## 6. Branch cover (charge item 6)

**Exhaustive**: a field point has `V0=0` or `V0≠0`; no third case.

`V0=0`: I re-verified the division-free certificate by my own expansion:
the six generators are byte-identical to my independently derived objects
(literal endpoint = negated substituted row-22 `X^0` row, monic `c`
relation, `E13, E14, E15`, `V0`), and the cofactor product-sum is exactly
the constant polynomial `1`.  The pre-branch identity
`3b³ = 2b·E13 + 4b·E14 − (4R0+2V0)·E15 − V0³(V0/4+R0/2)` checks by direct
expansion.  No localization, no carrier choice, cofactors polynomial.

`V0≠0`: I **derived** (not assumed) the branch data by an independent
identity chain: with `R0=τV0`,
`K17 = V0²(b+τ²V0)` forces `b=−τ²V0`;
`E13 = V0·(e−τ²V0((3/2)τ−3/8))` forces `e`;
`E14 = (3/16)τ²V0²·(12τ²+6τ+1)` forces the quadratic (τ=0 is impossible:
`R0=0` gives `b=0` and then `E15=−V0³/8` forces `V0=0`);
`E15 = −(1/8)V0²(V0+12τ⁵+3τ⁴)` forces `V0=−3τ⁴(4τ+1)`.
Modulo `12τ²+6τ+1` these reduce exactly to the five displayed linear
substitutions `V0=τ/24, R0=−τ/48−1/288, b=−τ/144−1/576, e=−τ/192−7/4608,
c=τ/18432+1/36864`.  Discriminant `−12` is not a rational square, so the
quadratic is irreducible and `K=Q[τ]/(12τ²+6τ+1)` is a field covering
both conjugate embeddings; no root is selected or approximated.  The only
divisions in the whole branch are by `V0` (nonzero by hypothesis), by `τ`
(proved nonzero), and by rational constants.

## 7. D16–D18 quadratic-field unit (charge item 7)

Rebuilt entirely with my own code: 56 nonvanishing reduced base rows from
rows 15–18; doubling each with its τ-multiple gives Q-row counts
**44 / 78 / 112** through D16/D17/D18 with exact Q-ranks **20 / 38 / 58**.
The doubled-row construction is exactly the K-linear span over Q (verified
semantics: `Σ(c0+c1τ)f_i` ↔ Q-span of `{f_i, reduce(τ·f_i)}`); it does not
split `1` and `τ` into separate equations.  No scalar lies in the span
through D17; `1` first appears at D18.

The frozen certificate's 13-row rational witness **reproduces exactly `1`
on my independently derived rows**, and its grouping is exactly the eight
displayed K-cofactors of RESULT §5 (`D16[4]: 1119744; D16[12]: 5038848τ;
D16[16]: 10077696τ; D17[1]: −85847040/7−(386311680/7)τ;
D17[5]: −2985984−13436928τ; D18[2]: 103514112/7+(465813504/7)τ;
D18[6]: 7962624+35831808τ; D18[10]: 23887872/7+(107495424/7)τ`).  My own
solver finds a shorter 12-row unit (same D17/D18 part, different D16
τ-part) — units are non-unique in a rank-58 span of 112 rows; both were
verified by expansion.  Provenance is closed end-to-end: the certificate's
eight pre-branch and reduced term lists match my rows exactly (all 17
frozen D16/D17/D18 compatibility rows match mine content-and-order); the
recorded source-row combinations match my own elimination provenance
(e.g. compat (18,2) = 7·[row-18 X³] + 1·[row-18 X⁷] after stage-entry
substitutions); and those rows chain through my σ to the raw generators I
rebuilt from the recurrence.  No endpoint equation, no D19+ row, no
normalization, no numerical root, and no outside relation enters: the
eight rows are combinations of substituted rows 16–18 only, and the
substitutions chain only to rows 10–15 plus the licensed radical steps and
the derived branch forms.

Control confirmed: the D14–D15 carrier core is genuinely not a unit — the
recorded rational point (`a=144, b=−1/144, e=−1/256, V0=−1/24, R0=−1/144,
c=5/9216, d=0`) kills the projected core, the `c` relation, and the
endpoint; `K17 = −7/497664 ≠ 0` there, so D17 is exactly where that point
dies.  The two `TARGETS/*.sing` files are inert custody artifacts (23/14
and 22/13 vars/generators as stated; never executed — resource boundary
respected).

## 8. Hostile mutations (charge item 8)

| mutation | result |
|---|---|
| M1: one used raw D18 source coefficient (`f_0_1·g_4_13`, `−4→−3`, X³ generator feeding compat (18,2)) | claimed 13-row witness ≠ 1 (**detected**); mutated span rank 58→60 |
| M2: quadratic constant `+1 → −1` (re-reduction of pre-branch rows) | claimed witness ≠ 1 (**detected**); certificate's recorded `result_terms` equal my recomputation |
| M3: omit all τ-multiple rows | `1` **not** in the 56-row Q-span (**detected**) |
| M4: omit first charged cofactor | ≠ 1 (**detected**); certificate's recorded residual matches mine |
| M5: K17 — perturb one charged witness coefficient; mutate charged raw D16 source coefficient | both break the frozen witness (**detected**) |
| M6: reverse pivot order at stages 16–18 | ranks (20,38,58) and unit-at-D18 invariant — conclusion is not an elimination-convention artifact |

Charge-sensitive vs cosmetic: in M1, M2, and M5b the *fixed certificates*
fail while `1` (resp. `K17`) remains in the mutated spans via other
combinations.  That is the correct signature for an infeasibility
certificate: generic perturbation of an overdetermined empty system stays
empty, so "conclusion survives, certificate breaks" is exactly
charge-sensitivity, not fragility, and none of the producer's regressions
is vacuous.  No mutation I tried was cosmetic (none left a frozen
certificate accidentally valid).

## 9. Discovery notes (audited as claims)

* `…characteristic-core-unit-r0…`: its identity chain (1)–(4) is embodied
  in the `V0=0` certificate and the `3b³` identity, both verified; its
  open `v²=0` conditional is *superseded* (not resolved) by the packet's
  two-branch cover, which never needs `v²=0`; its gauge analysis matches
  my structural finding.
* `…d18-quadratic-branch-unit-r0…`: its ranks 20/38/58 and branch forms
  match; its alternative 13-row cofactor (different τ-parts, `D17[9]` in
  place of `D16[16]`) **also sums to exactly 1 on my rows** — a second
  valid unit representation, consistent with non-uniqueness.

## 10. Issues, ranked

No mathematical defects found.  Remaining items are documentation-level:

* **N1 (cosmetic labeling).** "prefix equations D0,…,D9: 201" — rows 0–3
  have no generators in the raw file and the 36 row-4 equations are
  identically zero on this stratum (both verified); the 201 count and the
  claim `D0=…=D21=0` are exact, but a reader may expect literal D0–D3
  rows.  One clarifying sentence would help.
* **N2 (documentation).** The second structurally absent gauge line
  `p69 = g_0_0 = G12[X^0]` (`G → G+ν·t^12`) is not mentioned in RESULT §3.
  Harmless (absent from every generator and constraint; no slice needed),
  but the gauge discussion reads as if `p129` were the only such line.
* **N3 (reader guidance).** The frozen K17 and D18 witnesses are one valid
  choice among many (my independent solver returns different, shorter
  ones).  Fine as frozen, but successor reviews should verify the frozen
  combinations by expansion (as done here) rather than expect solver
  agreement.
* **N4 (scope, already correct).** Characteristic zero is genuinely used
  (squarefreeness of `C` fails in char 2; witness denominators include 3
  and 7).  The packet claims char 0 only — correctly conservative.

None of these blocks promotion; conversely, every identity credited above
was re-proved outside the producer's code, not merely replayed.

## 11. Promotion recommendation

Promote as stated: a proved, field-valued exclusion of the fixed branch-P,
square-baseline, cutoff-five endpoint stratum, with the packet's firewalls
attached verbatim (field-radical only; no nonreduced-scheme claim; no
branch-P-family, Keller-pair, counterexample, or JC2 consequence; D23 not
imposed, G22 absent).  Safe downstream inputs for successor lanes: the
verified endpoint carrier map, the scalar core `E13/E14/E15`, `K17`, the
carrier reconstruction `c=(3/16)V0(V0+4R0)`, and the two unit
certificates.  The nonreduced-scheme question and the other cutoffs remain
open and are correctly not claimed.
