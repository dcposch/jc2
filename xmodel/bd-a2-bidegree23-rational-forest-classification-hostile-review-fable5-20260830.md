# Hostile review: reduced bidegree-(2,3) rational-forest classification

Date: 2026-08-30 UTC
Reviewer: Fable 5 (different-model hostile desk review)
Review basis: `201b848b4422225f9514145c9c9655b635564404`

Inputs verified byte-exact:

```text
d783cecfcc818f1ec5c056fa04126c21dab0f17c073d11d8e230703b9755feaa  classification producer
  body 13761 / b76971e671237b906d4c772ec4008e7153ca6f47705cc994839fef33c12a604e  (recomputed, match)
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08  coordinator integration
  body 6810 / 9c6501222049980161f209d57e1a575ebe80c4de1b8018aedf303f692e1dae46  (recomputed, match)
```

Custody: packet basis `a619157b` is an ancestor of the review basis; predecessor
producer `367d8ffa…` and Opus review `24b61d50…` match their pinned full-file
hashes. The promoted first-leg theorem (integration §1–2) is consumed as input
only; nothing below re-derives or re-promotes it. No shell access to `jc2-lean`;
no heavy CAS was needed — every check below is exact hand computation.

## Itemized verdict

| Item | Verdict |
|---|---|
| 1. Connectedness + `2=G+B+K` identity + forest criterion | **CONFIRMED** |
| 2. Nine-type enumeration | **CONFIRMED** (exhaustive, nonduplicative) |
| 3. F1–F7 exact conditions + examples | **CONFIRMED** (all budgets recomputed) |
| 4. F8, F9 impossibility from exact budget | **CONFIRMED** |
| 5. Miranda infinity typing | **CONFIRM_WITH_CORRECTIONS** (wording N1; missing affine-zero clause N2) |
| 6. Campaign consequence / nonclaims | **CONFIRMED** |

Overall: **CONFIRM_WITH_CORRECTIONS** — no mathematical error found; two
corrections are presentational/scoping only. No false row; no counterexample
exists to any table entry (I attacked each one below).

## 1. Identity — independent reconstruction

Connectedness: Kunneth gives `H^1(S,O(-2,-3)) = H^0(P^1,O(-2))⊗H^1(P^1,O(-3))
⊕ H^1(P^1,O(-2))⊗H^0(P^1,O(-3)) = 0⊗C^2 ⊕ C⊗0 = 0`, and `H^0(O(-2,-3))=0`, so
the ideal sequence gives `h^0(O_C)=1`: every effective `(2,3)` divisor is
connected. Adjunction: `C^2=12`, `C.K=-10`, `p_a=1+(12-10)/2=2=(2-1)(3-1)`.

(1.1) is the standard normalization `χ` computation for a connected reduced
curve with `c` components. (1.2): `I(C)` has `V=c+#Σ`, `E=Σ_p r_p`; it is
connected because `C` is (components chain through multibranch points, every
point-vertex has an edge), so `b1=Σ_p(r_p-1)-c+1`. The resolution claim is
resolution-independent: the dual multigraph of the reduced total transform is
obtained from `I(C)` by replacing each point-vertex by the exceptional tree
over `p` and re-attaching the `r_p` branch edges at (distinct, by SNC) tree
vertices; contracting each tree is a graph homotopy equivalence, so `b1` is
preserved. Unblown nodes are the degenerate case: the direct edge is the
subdivision of the two-edge star, same `b1`. Loops (node on an irreducible
component, `r_p=2` to one component-vertex) are counted correctly by the
multigraph convention. Subtracting: `2=G+B+K` with `K=Σ_p(δ_p-r_p+1)`.
Nonnegativity: `O→ C^r` (branch values) has image the diagonal while the
normalization surjects, so `δ_p≥r_p-1`, each `K`-term `≥0`; `G,B≥0` trivially.
Hence forest+rational `⟺ G=B=0 ⟺ K=2`, and (since `C` is connected) the forest
is a tree. Reducible curves, disconnected normalizations, multibranch and
nonordinary singularities are all inside the hypotheses of (1.1)–(1.2); the
producer's calibration lines (contact-`m` pair gives `m-1`; ordinary triple
gives `1`) are exact: `δ_p = Σ_i δ(branch_i) + Σ_{i<j}(B_i·B_j)_p`.

## 2. Enumeration — independent re-derivation

An irreducible curve of class `(0,b)` has zero intersection with `(0,1)`, so it
lies in fibres of one ruling; irreducible forces `(0,1)`; dually `(a,0)⇒(1,0)`.
Mixed parts need `a,b≥1`. Multisets of mixed parts with first coordinates
summing `≤2`: one part from `{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)}` or two
parts `{(1,1),(1,1)}`, `{(1,1),(1,2)}` (three mixed parts need first-sum `≥3`).
Filling the fibre remainder in the unique way gives exactly
F1=(2,3); F2=(0,1)+(2,2); F3=(1,0)+(1,3); F4=(1,1)+(1,2);
F5=(0,1)+(1,1)+(1,1); F6=(0,1)+(1,0)+(1,2);
F7=2(0,1)+(2,1); F8=2(0,1)+(1,0)+(1,1); F9=3(0,1)+2(1,0). Nine, unordered,
pairwise distinct; every degenerate split ((2,0),(0,2),(0,3)) lands in F7/F9;
no disconnected configuration exists since every `(2,3)` divisor is connected
(§1), so nothing is missing. The smoothness claim for `(1,b)`/`(a,1)` parts is
right: `(1,b)·(0,1)=1` makes the component a graph `x=φ(y)`, hence smooth.

## 3. F1–F7 — every condition and example re-verified

**F1.** `G=0` forces rational normalization; `B=Σ(r_p-1)=0` forces every
singularity unibranch; `K=Σδ_p=2`. Plane unibranch `δ=1` is only A2; `δ=2` is
only A4 (semigroup `⟨2,5⟩`, gaps `{1,3}`; the multiplicity-3 candidate `⟨3,4⟩`
has `δ=3`). So exactly `2×A2` or `1×A4`. Examples:
`(t^3,t^2)`: injective (`t=t^3/t^2`), A2 at `t=0`, and at `t=∞` the chart image
`(u^3,u^2)` is a second A2; no other critical points. Class: `x`-degree 3
`= C·(1,0)`, `y`-degree 2 `= C·(0,1)` ⇒ `(2,3)`. Total `δ=2`. ✓
`(t^2/(1-t^3), t^2)`: degree `(3,2)` (numerator/denominator coprime);
injectivity: `t^2=s^2 ⇒ s=±t`, and `x(t)=x(-t)⇒t=0`; the three poles `t^3=1`
map to `(∞,ω^{2j})`, distinct; `t=∞ ↦ (0,∞)`, not otherwise hit. Critical set:
`x' = t(2+t^3)/(1-t^3)^2`, `y'=2t`, common zero only `t=0`, where
`y=t^2`, `x-y=t^5/(1-t^3)` (recomputed; exact): A4, `δ=2`. At `t=∞`,
`1/x = (u^3-1)/u` … i.e. `x=u/(u^3-1)~-u` is a local coordinate: immersion.
At poles `d(1/x)/dt=-(t^3+2)/t^3≠0`: immersions. One A4 only. ✓ Both curves
irreducible reduced `(2,3)`; irreducibility of the stratum is genuinely
realized, as claimed.

**F2.** `p_a(2,2)=1` bounds total `δ(Q)≤1`; `G=0` forces `δ=1`; `B=0` kills the
node (loop), leaving exactly one A2 cusp. `H·Q=(0,1)·(2,2)=2`; two transverse
points give `b1=5-5+1=1`, so `B=0` forces one support point. Case (i) smooth
tangency: `K=1(cusp)+1(contact 2)=2`, graph `E=3,V=4` tree. Case (ii) fibre
through the cusp: local length 2 means the fibre is transverse to the cusp
tangent (the tangent line has contact 3, excluded automatically by length 2),
`δ_p=1+2=3, r=2, K_p=2`, `E=2,V=3` tree. Both sub-cases exact and both
realizable: the producer's `Q: t↦(t^2/(1-t), t^2)` has (recomputed) unique
singularity A2 at `(0,0)` with tangent `{x=y}` (since `x-y=t^3+…`, `y=t^2`),
`x`-degree 2, `y`-degree 2, injective (poles `t=1↦(∞,1)`, `t=∞↦(∞,∞)`
distinct); `H={y=0}` meets it only at `t=0` with length `ord(t^2)=2` — case
(ii) verified. Case (i) is also nonempty with the *same* `Q`: `H={y=∞}` is
tangent at the smooth point `(∞,∞)` (`1/y=u^2`), giving cusp `+` tangency. ✓

**F3.** Both components smooth rational, `V·D=3`; `B=0 ⟺` one support point,
then contact 3 forced: `δ=3,r=2,K=2`. `{x=0}∪{x=y^3}`: intersection `y^3=0`,
one point, length 3; no meeting at `y=∞` (`D∋(∞,∞)∉V`). ✓

**F4.** Identical budget; `x=y` vs `x=y/(1-y^2)`: difference
`-y^3/(1-y^2)`, one point `(0,0)` of length 3; at `y=∞` the values `∞` vs `0`
differ, at `y=±1` the values `∞` vs `±1` differ. Classes `(1,1)`, `(1,2)`. ✓

**F5.** `H·Q_i=1, Q_1·Q_2=2`. Exhaustive necessity check: (a) `Q_1,Q_2`
tangent away from `H`: `E=6,V=6,b1=1`; (b) `Q_1·Q_2` at two points: cycle;
(c) ordinary triple point + extra `Q_1∩Q_2` point: `E=5,V=5,b1=1`; (d) `H`
through the point forces both `H∩Q_i` there (totals 1). Only the concentrated
tangent configuration survives: `δ_p=1+1+2=4, r=3, K_p=2`, star. Example
`{y=0}, x=y, x=y/(1-y)`: `Q_1∩Q_2` from `-y^2/(1-y)`: one point, length 2,
tangent `{x=y}`, both transverse to `H`; `φ_2(∞)=-1≠∞`, `φ_2(1)=∞≠1`: no other
meetings. ✓

**F6.** `H·V=1` is a forced meeting point; the same exhaustion (Q through it
with `V`-contact 2, `H`-contact 1) is the only `b1=0` option; `δ_p=1+1+2=4`,
`K_p=2`. Example `{y=0},{x=0},{x=y^2}`: all of `V·Q=2` at the origin (`Q`
tangent to `V`, vertical tangent, transverse to `H`), `H·Q=1` there; `Q`'s
infinity point `(∞,∞)` avoids `H,V`. ✓

**F7.** `H_1∩H_2=∅` kills every triple point, so the only `K`-resources are the
two `Q·H_i=2` packets; forest forces each supported at one point, i.e. two
contact-2 tangencies, `K=1+1=2`, and the chain `H_1—Q—H_2` is a tree. `y=x^2`
is tangent to `{y=0}` at `(0,0)` (length 2) and to `{y=∞}` at `(∞,∞)`
(`1/y=u^2`). Class `(2,1)`. ✓

## 4. F8, F9 — impossibility is budget-exact, not generic

**F8.** The five positive pairwise totals are all `=1` (`H_i·V=H_i·L=V·L=1`),
so no pair can have contact `≥2` anywhere: tangency resources are *identically
zero on the whole stratum*, not just generically. All branches at any point are
pairwise transverse, so `K_p=C(r_p,2)-r_p+1=(r_p-1)(r_p-2)/2`. A point contains
at most one `H_i` (disjoint), so `r_p≤3`, and `r_p=3` requires `V∩L` at that
point; `V·L=1` gives a unique such point, so at most one triple point,
`K≤1<2`, forcing `B=2-K≥1`. Cross-check with (1.2): triple point + two leftover
crossings gives `E=7,V=7,b1=1`. Every coalescence pattern is covered by the
`r_p≤3`/uniqueness argument. Impossible, exactly as claimed. ✓

**F9.** All six grid crossings are transverse and pairwise distinct (same-ruling
fibres disjoint), `r_p≤2` everywhere, `K≡0` identically, `I(C)=K_{3,2}`,
`B=6-5+1=2`. Impossible. ✓ (Multigraph recount: `E=12` branch-edges,
`V=5+6`, `b1=2`, consistent.)

## 5. Miranda typing — audit

The map `(a_2,b_2,c_2,d_2)↦(4.1)` is a linear isomorphism onto
`H^0(O(2,3))` (`3·4=12=4·3` dimensions; the `±1,±3` are units in char 0), so
the quadratic family does hit the irreducible F1 strata: reducibility is not
forced. ✓ The four strata bullets are individually correct, and the
projective-basepoint / nonreduced / degree-drop trichotomy is genuinely three
distinct conditions: a simple common `(s,t)`-factor keeps `F_∞` reduced (typed
F3/F6/F8/F9 factorizations); a squared common factor is nonreduced; total
leading-form vanishing removes the `(2,3)` curve entirely (`z` divides the
`P^2×P^1` closure equation). Fixed fibre roots (`(0,1)` parts, e.g. `b_2≡0 ⟺`
root `[1:0]`) are correctly separated from target-degree drop (`d` drops only
when all four leading forms vanish). Corrections:

* **N1 (wording).** Bullet 1 calls the common-factor stratum "the source of
  F3, F6, F8, and F9 *refinements*". F8 and F9 admit no rational-forest
  refinement (§4 above); they arise only as factorization strata that the
  criterion then kills. Say "factorization types", not "refinements".
* **N2 (missing clause).** A common zero of the coefficient sections at a
  *finite* (affine) base point is invisible to `F_∞`: only the leading forms
  restrict to the line at infinity. Such affine basepoints belong to the
  normality/finiteness/etaleness hypotheses, not to this classification, and
  the packet should say so explicitly, since my brief and FALLACY-v2 require
  the affine-zero / projective-basepoint distinction to be kept.

**Exact coverage.** The classification governs precisely the fixed-basis
quadratic presentations whose infinity restriction (4.1) is *squarefree* (then
its divisor is a reduced `(2,3)` curve, any factorization type, including
simple base-infinity coefficient basepoints and fixed fibre roots). It does not
cover: nonreduced `F_∞`; identically vanishing leading-form quadruples (no
`(2,3)` curve exists — degree-`≤1` analysis); affine coefficient common zeros
(invisible here, N2); ambient-closure smoothness/normality and ramification
hypotheses (correctly deferred in integration §4).

## 6. Campaign consequence — maximum safe promotion

**Safe theorem (promotable at this basis).** Let `C` be a reduced divisor of
class `(2,3)` on `P^1×P^1`. Then `C` is connected, `p_a(C)=2`, and
`2=G(C)+B(C)+K(C)` with all three terms nonnegative; the reduced total
transform on any embedded resolution has all components rational with forest
(hence tree) dual multigraph iff `K(C)=2`. The reduced factorization types are
exactly F1–F9; the `K=2` locus is nonempty exactly in F1–F7 with the exact
local conditions of §3 (producer's table confirmed verbatim, with the F2
tangent-line exclusion noted as automatic), and is empty in F8, F9.
Conditional on the promoted first-leg gate, a quadratic Miranda presentation
with squarefree `F_∞` survives the infinity-curve test only in strata F1–F7.

**No corrected type table is needed**; no row is false; the two F1
parametrizations, and the five reducible examples, are all verified exact.

**Not promotable (attempted upgrades all blocked).** This is a necessary
first-leg curve condition only. It is not a ramification-support exclusion
(the ramification divisor is absent), not a general quadratic-block or
cubic-block closure (nonreduced/degree-drop/affine-basepoint strata remain,
N2), not primitivity, not map existence or nonexistence, not a counterexample,
and not JC2. The producer's §5 nonclaims are complete and correct.

**Cheapest finite successor.** For each surviving stratum F1–F7, adjoin the
reduced ramification support `R` and apply the same accounting (integration
(2.1)) to the full boundary `D=F_∞∪R`: the gate fires on any `R`-component of
positive geometric genus, any second incidence branch closing a cycle with the
F-configuration, or `r≥2` boundary branches in the multisection form (2.2).
Since generically `H_∞·R=8`, a survivor must coalesce essentially all eight
incidences into the tree — a codimension count per stratum decided by
subresultant/Fitting conditions on finitely many constructible sets. This is
the invariant most likely to eliminate (or pin witnesses for) the seven types
at least cost; the twelve-parameter AWS job sketched in producer §3 is the
right executable form if coefficient ideals are wanted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13968`.
- Body SHA-256:
  `77d489d7168ce40079c0806bc485c6c444446ec3ea759bdd15ad5c2007ead5aa`.
- Frozen basis: `201b848b4422225f9514145c9c9655b635564404`.
