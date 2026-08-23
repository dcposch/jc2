# Depth-witness Lean semantic-fidelity review (hostile, definitions-only)

Review target: `/Users/dc/code/math/jc2-lean/depth-witness/`
(`Challenge.lean` definitional layer, `FIDELITY.md`, `README.md`;
`Solution.lean` is a placeholder and was checked only for absence of a
verdict theorem).

Informal sources, as claimed by `FIDELITY.md`, read from
`/Users/dc/code/math/jc72108` on 2026-08-20:

| Lean layer | Informal source |
| --- | --- |
| template ladder / tower | `SHEET6-TEMPLATE.md` §§0–1a (lines 33–80) |
| J-jet identity, depth-D rows, slot-20 inhomogeneity | `SHEET6-DIRECTIONB.md` header + §§0–1 (lines 22–92) |
| CORE2 census, W-unit chart, 36-fiber split | `SHEET6-DIRECTIONB.md` §7.S3 (lines 1091–1140) |
| PIN42 / no-log, D23/D25 extension data | same sheet §§7, 8, 8.S, 9, as FIDELITY states |

Orbit-registry details that the prose does not reprint were checked
against `cases/r1_experiment.py` `build_generators` / `gm_jet` (the
engine DirectionB cites as read-only chart machinery) and against the
banked D21 legend `cases/directionb_residual32.rows.txt`. Split-prime
constants were recomputed independently in `F_105337`, not copied from
the Lean kernel proofs.

This is a statement-level / definitional-fidelity review. `lake build`
was not part of the review.

---

## VERDICT: FAITHFUL

The Lean window is the unreduced residue-A J-jet object, not a CORE2
or Schur substitute. Index conventions, PIN42, W-unit saturation, and
the depth-`D` parameterization match the engine: depth `D` means rows
`k < D` (so D21 is rows `0..20`, D23 adds `21,22`, D25 adds `23,24`).
A point of `HasDepthWitness D` is a genuine campaign witness of that
window at the fixed split prime `p = 105337`, r3-embedding `795`,
B-frozen no-log PIN42 `W₁ W₂ ≠ 0` chart. Nothing in the definitional
layer silently drops a campaign equation, gauges a pole scale to `1`,
or replaces the row recurrence by a proper subset of eta-cells.

The parameterized proposition `HasDepthWitness D` is the right Palomar
shape for both verdict branches, with one disclosed coefficient-field
discipline that is load-bearing for EMPTY and is already stated in the
README: NONEMPTY needs an actual `ZMod 105337` point; EMPTY must be
proved by a unit-ideal / covering certificate, not by “no F_p-point
was found.” That is a proof obligation on a future Solution, not a
defect in the definitions.

No HIGH or MEDIUM defects. LOW nits are recorded at the end; none of
them changes a future D25 theorem.

---

## Hunt 1 — window / depth-condition structure

### Independent recomputation of the J-row (not copied from Lean)

G_m chart, DirectionB §0: `t = x^{-1/42}`, so `x = t^{-42}`;
`y = P(t) + η t^{32}` with prefix arc
`P = t^{12} + uf18 t^{18} + uf24 t^{24} + uf30 t^{30}`.
Chart Jacobian:

```
x_t y_η − x_η y_t = (−42 t^{-43}) · t^{32} = −42 t^{-11}.
```

Y-side jets, gauge `S_R = G_R = 1` (hence `c_f = c_g = 1` at this
window, DirectionB lines 194–196 and the RHS42 gate at
`directionb_window.py` 248–267):

```
f − a = t^{-12} Φ(t,η) (1 + O(t^{42})),
g     = t^{-18} Γ(t,η) (1 + O(t^{42})),
```

with `Φ = ∑_s F_s(η) t^s`, `Γ = ∑_s G_s(η) t^s`, and slot-zero leads
`F_0 = S_M P2`, `G_0 = G_M P3`, `S_M = 7^{12}/2^6`,
`G_M = −7^{18}/2^9`. Pulling `J(f,g) = 1` back through the chart is
exactly

```
(t Φ_t − 12 Φ) Γ_η − Φ_η (t Γ_t − 18 Γ) = −42 t^{20}.     (J)
```

Coefficient of `t^k`, writing `i + j = k`:

```
Row_k = ∑_{i+j=k} [(i−12) F_i G_j' − (j−18) G_j F_i']
```

equals `0` for `k ≠ 20` and equals the constant polynomial `−42`
(the `η^0` term) at `k = 20`. This is the analysis form
`LHS + 42 = 0` of the residual-32 emission
(`Row_20[eta^0]+42`).

Lean `jacobianRow` is that sum, with `i` the Φ-slot, `k−i` the Γ-slot,
integer weights cast `ℤ → Coeff` (no `ℕ` underflow: `i ≤ k` from
`Finset.range (k+1)`), and `Polynomial.derivative` the η-derivative.
Lean `rowTarget` is `C(−42)` at `k = 20` and `0` elsewhere. The
`ZMod 105337` wrap of the weights is faithful for every campaign
depth: `|i−12|, |j−18| ≤ 41 ≪ p`.

Engine cross-check: `cases/directionb_strike.py` `jrows` builds the
same LHS as `jmul(tΦ_t−12Φ, Γ_η) − jmul(Φ_η, tΓ_t−18Γ)` and the
zero-extension gate asserts the `η^0` constant is exactly `−42`.

### Depth-D parameterization

The engine builds jets with truncation `slot < D`
(`gm_jet2(..., D)`) from generators of absolute depth `32+D`
(`build_generators(32+D)`), then reads rows `k = 0..D−1`. Chart
depth `D = 21` is the product over `F_p[η,t]/(t^{21})` whose last
row is `Row_20`. D23 adds rows 21 and 22 (Row_21 is identically zero;
Row_22 is new). D25 adds 23 and 24 (Row_23 identically zero; Row_24
new).

Lean `WindowConditions D x` is `∀ k < D, jacobianRow x k = rowTarget k`
plus the chart package. So:

| named depth | Lean rows | engine |
| --- | --- | --- |
| 21 | `k = 0..20` | D21 window through slot 20 |
| 23 | `k = 0..22` | D21 plus rows 21, 22 |
| 25 | `k = 0..24` | D23 plus rows 23, 24 |

No off-by-one. `IsCampaignDepth` requires `21 ≤ D ≤ 42` and `Odd D`.
The upper bound is the source fact that rows `k = 0..41` are pure
y-side (x-side leads `φ_f, φ_g` enter at `t^{42}`). The oddness is
the campaign ladder (two-row steps from D21). Harmless at D25; a
parameterization footgun at the y-side ceiling is a LOW nit below.

`TruncatesTo lower` agrees on `orbitCoefficient` for
`level < 32+lower`. That is exactly the largest absolute level that
can affect a through-factor slot `< lower` (through slot `s` reads
level `32+s`; off-factors read `12+s`, a strictly smaller cutoff).
D21 therefore agrees through level 52 and leaves 53/54 free for D23,
matching `build_generators(32+21)` versus the D23 tails at 53/54.

### Factor product and orbit registry

Lean `throughFactor` / `offFactor` / `orbitFactors` are `gm_jet`, not
a paraphrase:

- through d0, A-side, direction `k = 0`: `η − Ỹ` with `Ỹ` slot `s`
  equal to the phase-twisted level-`(32+s)` coefficient;
- every other factor: `P[12+s] − ζ^{c(12+s)} Y[12+s]` plus `η t^{20}`;
- phase `c = k + 7j` with `k < 7` and `j < orbitSize/7` (6 or 3).
  For these ranges `c < 42`, so Lean’s unreduced `ζ^{c·level}` equals
  the engine’s exponent `mod 42` by the proved identity `ζ^{42} = 1`.

`isAside` is exactly the six orbits whose level-12 coefficient is `1`
(P1, P2, Gp1, Gp2, G0p1, G0p2). B / GB42 / GB21 are off-factors with
level-12 coefficient `η_B`. Orbit sizes 42/21, f-orbits
`(P1,P2,B)` total 126, g-orbits total 189, even support on the three
size-21 orbits, shared `uf`/`vf` on the joint-tree A-arcs: all match
`build_generators`.

`phi` / `gamma` are finite Cauchy products of those 126 + 189
factors. Slot `k` of a Cauchy product depends only on factor slots
`≤ k`, so the Lean untruncated series agrees with the engine’s
`slot < D` product on every row that `WindowConditions D` reads.
`TopConditions` is the §1 gate (E6 slot-0 leads, E1
`G_0^2 = F_0^3`, Row_0). Row_0 is also `jacobianRow 0 = 0`; the
duplication is redundant, not a change of object.

### PIN42

DirectionB §7: `Res_t(y dx) = −42 c_{42} = 0` at every 42-ramified
place, and the same `t`-level-42 coefficient at the 21-ramified
places (series in `u = t^2`). The six live pins are
`tf1_42, tf2_42, tg1_42, tg2_42, tg01_42, tg02_42`; the three B-side
pins are trivial on the frozen stratum.

Over `ZMod 105337`, `42` is a unit (`p ∤ 2·3·7`), so the residue pin
is exactly `c_{42} = 0`. Lean does this twice, consistently:

- `orbitCoefficient` returns `0` at level 42 for every live orbit
  (`38 ≤ level ∧ level ≠ 42`, plus the even-G0 guard);
- `NoLogPins` forces the six named tail fields to `0`.

Level 42 is consumed by the window: through-factor slot 10
(`32+10 = 42`) and off-factor slot 30. Baking the pin into the series
is the engine’s PIN42 monomial drop, not a missing equation.
`BFrozen` plus the B-orbit clause (`level = 12` then `η_B`, else `0`)
is the D21/D23/D25 frozen-B stratum.

### W-scale saturation

Campaign chart: `W1 W2 ≠ 0`, Rabinowitsch rows `uW_i W_i − 1`, and
`2 HW_i^2 = 3 W_i^2` (unsplit CORE2, §7.S3; residual-32 emission
lines 151–156 of the legend). Equivalently, after W-normalization,
`h_i = HW_i/W_i` satisfies `2 h_i^2 = 3`, which is the D25 family
algebra `B36`. Lean keeps the unreduced form:

```
2 HW1² = 3 W1²,  2 HW2² = 3 W2²,
uW1 · W1 = 1,    uW2 · W2 = 1,
uA · (α1 − α2) = 1.
```

Pole scales remain coordinates (level-37 coefficients of P1/P2).
They are not silently set to `1`. The CORE2 GB pinning
`W1^4 = 57673`, `W2^4 = 53212` (mod 105337) is a computed
consequence of Row_20 on the locus, not a definitional extra, and is
correctly absent from `WindowConditions`. Over a field, `W` a unit is
equivalent to `W ≠ 0`; the explicit inverse is the right algebraic
encoding of the saturation.

---

## Hunt 2 — silent weakenings of a future nonemptiness statement

Criterion: a Lean witness must be a genuine campaign witness. The
dangerous direction is Lean conditions *weaker* than the campaign
object.

Checked, and not present:

1. **Unreduced rows vs CORE2 / Schur.** `WindowConditions` is the
   orbit-generated J-rows, not the 38 residual labels, not the
   rank-4 Schur residuals of Row_22/Row_24. A CORE2 point is a
   computational presentation of this object; a Lean point *is* the
   object. The metadata census (`27` vars / `45` eqs, 22 pivots, 18
   remaining template coordinates, D23 DEEP10, D25 FRONTIER,
   eta-supports `{1,4,…,28}` and `{2,5,…,26}`) matches §7.S3 / §8 /
   §9 and is not substituted for the rows. Pivot cells match
   `cases/d25_assemble.py` `PIVROW` and `directionb_core23_final.py`
   `PIV22` entrywise. Residual labels match
   `cases/directionb_core2.rows.txt` (38 cells, PIN42 already
   removing `(10,28)`).

2. **Eta-support subset.** Residual-32 lists the 3-grid cells (77
   raw D21 cells; Lean `d21RawCells` matches that legend, including
   Row_6 = `η^{2,5,…,26}` — nine cells — which is the D21 ledger,
   not the D=7 prose “ten components through `η^{29}`”). Lean
   imposes the *full* polynomial identity in `Coeff[η]`. Extra grid
   vanishing is a strengthening.

3. **PIN42 / B-freeze / W-units / A1≠A2.** All present. Omitting any
   of them would have been a genuine weakening (a `W = 0` point, a
   log-carrying `c_{42} ≠ 0` series, or a coalesced-pole point is
   not a campaign witness).

4. **Gauge `c_f c_g = 1`.** RHS `−42` rather than `−42/(c_f c_g)` is
   the banked `S_R = G_R = 1` gauge, certified by the RHS42 gate.
   A Lean witness is a gauge-fixed campaign witness.

5. **F_p-rational point.** `HasDepthWitness` asks for a
   `ZMod 105337` point, not geometric nonemptiness over an algebraic
   closure. That is *stronger* than “GB ≠ [1]”. README / FIDELITY
   already refuse to identify the two. A Lean NONEMPTY theorem is a
   reconstructed modular point, which is what the campaign wants in
   that branch.

6. **Finite window, not a polynomial pair.** In scope. README does
   not claim a formal germ, a characteristic-zero germ, or a Keller
   pair. No silent promotion.

The one disclosed *strengthening* that could make NONEMPTY harder
(not weaker) is the F_p-rational demand. That is the right Palomar
choice for an extracted witness, and it does not let a fake
campaign witness through.

---

## Hunt 3 — statement template, both verdict branches

```lean
HasDepthWitness D :=
  ∃ x : ResidueAData, IsCampaignDepth D ∧ WindowConditions D x
```

`IsCampaignDepth 23` and `IsCampaignDepth 25` are true arithmetic
facts, so at the named depths this is existence of a window point.
`WindowConditions 25 x` implies `WindowConditions 23 x` for the same
`x` (strictly more rows). The README table is therefore the right
ladder shape:

| D25 branch | intended theorem | scoped meaning |
| --- | --- | --- |
| NONEMPTY, extracted `F_p` point | `HasDepthWitness 25` | finite-window survival at this chart/prime/embedding |
| EMPTY on the 36 fibers, elimination certificate | `HasDepthWitness 23 ∧ ¬HasDepthWitness 25` | D23-alive / D25-dead modular chart kill |

Both branches talk about F_p-points of the same `WindowConditions`.
That is a coherent dual-use of one proposition.

The strength is *not* symmetric, and the README already says so:

- proving `HasDepthWitness 25` is stronger than geometric
  nonemptiness over `F_p-bar`;
- proving `¬HasDepthWitness 25` is weaker than “the ideal is `1` on
  every fiber over an algebraic closure.”

This is not a silent definitional defect. It is a proof-discipline
constraint on the EMPTY Solution: `¬HasDepthWitness 25` may be
inhabited only by a unit-ideal / 36-fiber covering certificate, never
by an F_p-search. A proper/nonunit ideal over an algebraic closure
cannot fill `HasDepthWitness` either (the converse direction, also
disclosed). If a later Solution wants the EMPTY theorem’s *statement*
to carry geometric strength, add an explicit unit-ideal predicate
rather than relying on the negation of the F_p-existential. That is
an optional lock, not a present infidelity: no emptiness theorem is
asserted in this phase, and `Solution.lean` is empty of verdicts.

The template is the right shape for D23-survives / D25-dies, which is
the campaign’s actual ladder (D23 F_p-witnesses are already banked).
If D23 were also empty, the conjunction would be the wrong theorem
and one would instead prove `¬HasDepthWitness 23` (or 21). That is
contingency, not a defect in the parameterized Prop.

---

## Hunt 4 — `ZMod p` setup vs the split primes

Requested coefficient field: the fixed split prime `105337` with the
banked radical_point embedding. Independently recomputed:

| datum | Lean | independent `mod 105337` |
| --- | --- | --- |
| `795² = 3` | `sqrtThree_sq` | holds |
| `2779^{42} = 1`, and `≠ 1` at proper divisors 6, 14, 21 | `zeta42_pow`, `zeta42_primitive` | primitive 42nd root |
| `2 · 24069⁷ = 3` | `etaB_seventh` | holds (engine `EB` / `BETA`) |
| `51107 · 2⁶ = 7^{12}` | `fLead_value` | `S_M` residue |
| `33066 · 2⁹ = −7^{18}` | `gLead_value` | `G_M` residue |
| `gLead² = fLead³` | `lead_tower_relation` | `s0 = 1` tower at slot 0 |

Split-prime arithmetic that the chart actually uses, all true at
`p = 105337`:

- `p` prime (Lean `norm_num`; campaign prime);
- `84 | (p−1)`, so 42nd roots exist;
- `legendre(3,p) = +1`;
- `3±795` are cubic residues: 3 cube roots each in `F_p`;
- `3/2` is both a square and a 7th power: 2 roots of `2h²−3 = 0`,
  and the B-root exists;
- `p ∤ 42`, so the Row_20 inhomogeneity and the no-log factor `−42`
  stay nonzero.

Fiber count: `3 × 3 × 2 × 2 = 36` F_p-rational radical embeddings
after fixing r3. Lean `RadicalPoint` leaves `α1, α2, HW, W` as
coordinates subject to the seven unsplit equations (r3, `ζ`, `η_B`
substituted, matching §7.S3 “after fixing r3, zeta, EB”). A point of
`HasDepthWitness` therefore lands on one of the 36 fibers; the
definition is not specialized to a single radical_point seed.

The sibling primes 105673 and 200257 satisfy the same splitting laws.
They are robustness lanes, not a second coefficient field of this
layer. A 105337-witness is a genuine modular campaign witness. The
conjugate embedding `r3 ↦ p−r3` is pole-swap / tau of the same
unsplit equations (Lean carries both cube laws), not a missing chart.

`Fact (Nat.Prime 105337)` is infrastructure for the `ZMod` field
instance, not an extra mathematical hypothesis.

---

## Template ladder (SHEET6-TEMPLATE.md §§0–1a)

Checked entrywise against the table at lines 69–80 and `Q(F)` at
lines 45–46. Lean `ladderDatum` is the literal table, including the
two unresolved source values as `none` (`M_R`, exact root tower
depth). `towardRoot` is `P_i → G_m → F_s → R`. `towerTerm` is
`h_0 = g`, `h_{j+1} = h_j^{k_j} − s_j (f−a)^{l_j}`.
`knownTowerExponents` is the pinned prefix `(2,3), (3,4), (7,23)`.
`mergePolynomial` is `(η³−(3+√3))(η³−(3−√3))` in the `σ = 6` gauge,
where `a_{1,2} = 3 ± √3`. None of this is read by
`WindowConditions`; none of it silently fills a residual.

α1/α2 naming: Lean `RadicalPoint.alpha1` is the source’s emitted
`A1` (cube root, level-32 coefficient), not Template’s merge
direction `a1 = 3+√3`. FIDELITY states the distinction. The merge
polynomial uses `a1, a2`; the orbit registry uses `A1, A2` with
`A1³ = a1`. That is the engine.

---

## FIDELITY.md / README accuracy

The declaration-by-declaration map is accurate on every load-bearing
item that was checked (J-row, depth-D, PIN42, W-units, orbit
registry, CORE2 census, TruncatesTo cutoff, lead residues, 36-fiber
count). Scope boundaries in both files match the Lean: no expanded
polynomials, no CORE2-equivalence proof, no witness, no char-0
claim, no inverse-limit claim. `formalization.yaml` `fidelity.divergences`
describes the actual divergences (CORE2 as metadata, F_p-point not
geometric nonemptiness, `D ≤ 42` y-side cap, `(72,108)` as campaign
label not chart degrees `(168,252)`).

`Solution.lean` does not assert `HasDepthWitness` or its negation.

---

## What was checked that could have been a defect, and is not

1. Depth off-by-one (`k ≤ D` including a nonexistent row, or `k < D`
   dropping Row_20 at D21). D21 is `k < 21`.
2. Jacobian weights `(i−12)` on the wrong factor, or `ℕ` subtraction
   wrapping `j−18` for `j < 18`. Casts go through `ℤ`.
3. RHS `−42/(S_M G_M)` or `+42`, or the inhomogeneity on the wrong
   row. Gauge-1 target is `C(−42)` at `k = 20` only.
4. Through-factors consuming levels `< 32`, or off-factors omitting
   `η t^{20}`. Match `gm_jet`.
5. Phase `k + 7j` versus `7k + j`, or twisting `ζ^{c·slot}` instead
   of absolute level. Absolute level, `c = k+7j`.
6. G0 odd tails surviving; B tails live; level 42 live in the series.
   All zero in `orbitCoefficient`.
7. `W` gauged to `1` (would drop W-scale from Row_20). Units, not
   ones.
8. `2 HW² = 3` without the `W²` (would be the normalized `h`,
   losing the level-37 coordinate). Unreduced `2 HW² = 3 W²`.
9. `A1³ = 3−r3` swap. Lean `α1³ = 3+√3`, `α2³ = 3−√3`, matching
   residual-32 `A1³−3−r3` and `A2³−3+r3`.
10. CORE2 residual list used as the definition of the window.
11. `HasDepthWitness` as nonempty-over-`F_p-bar`. It is an F_p point.
12. `D = 42` admitted as a y-side theorem that silently includes
    x-side row 42. `IsCampaignDepth` caps `D ≤ 42` with `k < D`, so
    the last possible row is 41.
13. `r3` left free (`72` fibers). Fixed at `795`; 36 fibers.
14. Missing `uA(A1−A2)−1` (would admit a coalesced merge). Present.
15. Template `M_R` or root tower depth invented. Both `none`.

None of these is present.

---

## LOW nits (not defects; no change to the verdict)

**LOW — `IsCampaignDepth` never names the full y-side package.**
`Odd D ∧ D ≤ 42` allows D41 (`k = 0..40`) and forbids D42
(`k = 0..41`). Row 41 is certified pure y-side and is not in any
`HasDepthWitness`. Irrelevant at D25, where the ladder is odd and
stops at Row_24. Fix if a “full y-side window” theorem is ever
named: allow `D = 42`, or drop `Odd`, or honestly cap `D ≤ 41`.

**LOW — `WindowConditions` itself is unguarded.** The y-side cap
lives in `IsCampaignDepth`, which `HasDepthWitness` and
`DepthExtension` both require. A future Solution that ignores the
wrapper and instantiates `WindowConditions 50` would be claiming
pure y-side rows past the x-side entry. Fail-closed at the public
Prop; footgun at the raw predicate.

**LOW — `HasDepthWitness` puts `IsCampaignDepth D` under the
existential.** The conjunct does not depend on `x`. Equivalent to
`IsCampaignDepth D ∧ ∃ x, WindowConditions D x`. Harmless at 23/25;
it makes `HasDepthWitness 24` false for parity reasons rather than
window reasons.

**LOW — EMPTY strength is in the certificate, not the Prop.**
README already requires an elimination certificate for the EMPTY
branch. If that discipline needs to be kernel-visible later, add an
explicit unit-ideal / “no point over any `Coeff`-algebra” predicate
and prove `¬HasDepthWitness` from it. Do not change
`HasDepthWitness` itself: the NONEMPTY branch wants the F_p point.

**LOW — yaml review status.** `formalization.yaml` still says
“self-assessed; separate Grok fidelity review pending.” Update when
touching the file.

None of these is a missing pin, a dropped W-saturation, a depth
off-by-one, a Jacobian-weight error, or a Challenge/README mismatch
on what a witness is.

---

## Constants appendix (independent of the Lean kernel)

```
p        = 105337
r3       = 795           r3² ≡ 3
ζ42      = 2779          primitive 42nd root
ηB       = 24069         2 ηB⁷ ≡ 3
S_M      = 51107         7¹² / 2⁶
G_M      = 33066         −7¹⁸ / 2⁹
(p−1)/84 ∈ ℕ,  (3/p) = 1,  3±r3 cubic residues,  3/2 square and 7th power
#A1-roots = 3,  #A2-roots = 3,  #h-roots = 2,  fibers = 36
```

These are the banked split-prime embedding used by
`cases/directionb_core_p105337.rows.txt` (`r3=795`),
`cases/sol_algkill.py` (`R3, BETA`), and the D23 witness JSON
(`zeta: 2779`).
