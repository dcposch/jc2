# Hostile review — Sigray selected-orbit attachment repair

**Date:** 2026-08-28  
**Reviewer:** Fable 5 (Anthropic), acting as independent hostile referee  
**Scope:** exactly one frozen repair packet; no canonical file was edited.
`jc2-lean` was not entered, listed, searched, read, built, modified,
status-checked, or controlled.  No AWS or heavy computation was used; only
local hashing and `pdftotext` extraction of the pinned primary source.

## Verdict

**PASS-WITH-REPAIR.**

The repaired ambient theory is correct and closes the exact blocker named by
the prior hostile review: in Sigray's actual Eggers–Wall object `T_a^*`
(Definition 3.3), flag equality is contact equality, splits never remerge,
every selected witness has the unique attachment claimed, and witnesses are
globally pairwise distinct.  Lemma 3.1's three numbered conclusions are true
as stated, and with them the frozen producer's (MFE) inequality

```text
sum_(F in U) lambda_F^exit <= td(f,g) - 1 - psi
```

follows at the selected-exit/shared-inequality scope, exactly as claimed.

One intermediate equation in the packet's proof of Lemma 3.1(1) is false as
universally quantified: display `(3.2)`, `O(P,Q)=u` "for every pole
representative," fails in the degenerate configuration where the base flag
`F` is an outer endpoint of the pole union (a pole vertex) and the selected
exit continues along that pole ray beyond its pole flag.  The lemma's
conclusions survive unchanged because the truncation `min(v_j, O(P,P_j))`
already built into definition `(2.2)` caps that ray's contribution at `u`.
The minimal exact replacement is given in Section 3 below.  The MFE
inequality still follows; nothing downstream consumes `(3.2)` itself.

Separation of concerns: **theorem truth** — CONFIRMED (with the one-sentence
patch to the written proof); **citations** — all byte-pinned inputs match
and every load-bearing citation was independently checked against the
primary source and found accurate, including the delicate use of one PASSED
clause of an overall-FAILED delta gate; **scope/conformity** — clean, all
quarantines preserved, no hidden upgrade found.

## 0. Custody

All pins verified by local `shasum -a 256`:

```text
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14  repair packet (under review)
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8  frozen producer
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004  prior hostile review
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

All seven read inputs declared in the repair's Section 0 also match their
printed hashes (cyclic-semi-invariance repair `37b83208…`, quotient route
`521080ae…`, final delta gate `758c0226…`, Prop 6.7–6.8 audit `c3d6ff92…`,
Section 9 audit `2763d970…`, weighted-Euler repair `c253bd12…`,
`ladder/SHEET6-AF2.md` `062c92ba…`).

Primary pages were re-extracted and read independently: printed pp. 10–18
(Definitions 3.1–3.4, Notations 3.1–3.8, Statements 3.2–3.6, 3.16, 3.18,
Propositions 3.1–3.2), pp. 28–35 (Notation 6.1, Statement 6.1–6.2,
Propositions 6.2–6.8, Lemma 6.1), and pp. 35–36 (Notation 7.1, Statements
7.1–7.3, Propositions 7.1–7.3).  One custody footnote: the final delta
gate's own header pins the coordinator revision it reviewed
(`cbc7d6d2…`), which is not the quotient-route file (`521080ae…`) pinned
here; the bridge clause used by this repair is quoted from the frozen gate
itself, so custody is coherent at this packet's level, but consumers should
continue citing the gate, not the route file, for the bridge.

## 1. The quotient model (attack 1)

Definition 3.3 (printed p. 11) is verbatim: `(P,u) ~ (P*,u*)` iff
(i) `u = u*` and (ii) `u <= O(P,P*)`, with
`T_a^* = ((R̄_a \ R_a) × [0,∞])/~`.  Definition 3.2 (p. 10) defines contact
of distinct curve points as the maximum of series contact over
corresponding Puiseux representatives; Statement 3.2 (p. 11) supplies the
coherent presentation `Ω` with `O(P,Q) = O(Ω(P),Ω(Q))`.

Three consequences, each checked directly:

1. **The exact object contains every selected cv flag.**  `T_(a,cv) ⊂
   T_a^0 ⊂ T_a = T_a^* ∩ π^(-1)(Q)` (Notations 3.6, 3.14, 7.1).  Pole-path
   vertices are in `V_a ⊂ T_a` (Statement 3.4).  There is no further
   quotient anywhere in the source: the tree is built on **points** of
   `R̄_a \ R_a`, and raw Puiseux representatives never enter as tree
   elements.  The prior review's fear of "a later quotient identifying cv
   representatives" has no referent in Definition 3.3.
2. **`I_P(t) = I_Q(t)` iff `t <= O(P,Q)`, hence no remerging.**  The "if"
   is Definition 3.3(ii) verbatim; the "only if" is class equality.  For
   `t > O(P,Q)` the flags are unequal by definition.  A split cannot
   remerge — repair display (1.2) is definitional, as claimed.
3. **Well-definedness hygiene.**  For the relation to be an equivalence one
   needs the ultrametric inequality `O(P,S) >= min(O(P,Q), O(Q,S))` on
   point contact.  The source asserts Statement 3.2 without proof (its
   usual convention for Statements).  I verified the inequality
   independently, without `Ω`: pick representatives `p,q` realizing
   `O(P,Q)` and `q',s` realizing `O(Q,S)`.  All representatives of one
   point form a single orbit under the deck substitutions
   `x^(1/κ) -> ζ x^(1/κ)` (suitable `κ`), and such substitutions multiply
   the coefficient at exponent `j/κ` by `ζ^j`, hence preserve raw pairwise
   contact.  Writing `q' = σ(q)`, the raw ultrametric inequality gives
   `O(P,S) >= O(σ(p), s) >= min(O(σ(p), q'), O(q', s)) =
   min(O(P,Q), O(Q,S))`.  So Definition 3.3 is well-posed with or without
   Statement 3.2, and the repair's citation of 3.2 for the coherent
   presentation is honest and sufficient.

Conclusion: repair Section 1's displays (1.1)–(1.2) are correct at the
exact object containing every selected cv flag, and post-split remerging is
excluded definitionally.  The prior review's abstract countermodel — one cv
flag `H` retained with two incidences after a split at `F` — would require
`I_(P_1)(w) = I_(P_2)(w)` at some `w > O(P_1,P_2)`, contradicting
Definition 3.3(ii).  It cannot occur in `T_a^*`.

## 2. Rootward segments and the pole union (attack 2)

Representative independence of `rho_H` (repair (2.1)): if `H = I_P(v) =
I_Q(v)` then `v <= O(P,Q)`, so every `t <= v` also satisfies
`t <= O(P,Q)`, giving `I_P(t) = I_Q(t)`.  Immediate from (1.2).  This is
genuinely stronger than Notation 3.3's vertex-level parent fact and is
correctly proved rather than cited; the repair's remark that Notations
3.3/3.8 and Statements 3.5–3.6 "are not being asked to prove the stronger
interval statement" is accurate (I verified 3.5, `(F*c)' = F`, and 3.6 on
printed p. 13).

`U^full` (repair (2.2)) is representative-independent by (2.1) applied to
each pole flag, and its point set equals the producer's `U`: by Notation
3.3 the edge `e_(F,F°)` is the segment `I_P([u*,u])`, so the characteristic
path from pole `P_j` is exactly `I_(P_j)([0, v_j])` as a set.  For any end
`P`, membership `I_P(t) ∈ U^full` requires (Definition 3.3(i)) a pole ray
`P_j` with `t <= v_j` and `t <= O(P,P_j)`, hence

```text
A_P = [0, max_j min(v_j, O(P,P_j))],
```

an interval — rootward closed, exactly as the repair argues.  A ray cannot
leave the pole union and re-enter it.  Both halves of attack 2 hold.

## 3. "Contact exactly u" and the endpoint defect (attack 3) — REPAIR

This is where the packet's written proof overreaches.  Display (3.2)
asserts `O(P,Q) = u` and then says "This holds for every pole
representative."

**Where the argument works.**  Let `Q = P_j` be a pole ray through `F`
whose segment continues strictly above `F` (`u < v_j`).  Then `O(P,Q) > u`
is genuinely impossible: choosing `κ` suitable and divisible enough that
`κu ∈ N` (a suitable `κ` refined by any integer factor stays suitable),
contact is grid-valued, so `O(P,Q) > u` forces `O(P,Q) >= u + 1/κ`, i.e.
agreement of the `Ω`-series at every exponent `<= u`, hence the same
corrected-3.18 one-step child `I_P(u+1/κ) = I_Q(u+1/κ)`.  That child lies
on the pole segment (height `u+1/κ <= v_j` for `κ` fine), so `d` would be
the pole-chain arrival at `F`, contrary to the class-3 selection.  With
`O(P,Q) >= u` from `I_P(u) = I_Q(u)`, contact is exactly `u`.  There is no
rational-grid gap: the common-denominator step is licensed exactly as the
repair says, and no direction/orbit ambiguity enters because the argument
runs entirely on `Ω`-coefficients of points.

**Where it fails.**  Let `F` be an outer endpoint of `U^full`: `F =
I_(P_j)(v_j)` is the pole vertex itself, `u = v_j`.  The pole segment does
not continue above `F`, so the direction along the ray `P_j` beyond its
pole flag is **not** a pole-chain arrival and — by the packet's own
equivalent formulation — its one-step child at height `v_j + 1/κ` is not on
a pole path.  It is therefore an admissible selected exit, and for it
`O(P,P_j) > u` is entirely possible (the witness ray `P` may follow the
pole ray far beyond the pole flag; note `P ≠ P_j` as points, since by
Proposition 7.2 a ray carrying a cv flag has `g(P) ∈ C` while
`g(P_j) = ∞`, so the contact is finite — but it can exceed `u`).  In that
configuration `(3.2)` is false for this `j`.

**Why the conclusions survive.**  The `j`-th segment's contribution to
`A_P` is `[0, min(v_j, O(P,P_j))]`, and at an endpoint
`min(v_j, O(P,P_j)) = v_j = u` no matter how large the contact is.
Segments through `F` that continue above it give contact exactly `u` (the
valid case), and segments not through `F` give
`min(v_j, O(P,P_j)) < u` (either `v_j < u`, or `I_(Q_k)(u) ≠ F` forces
`O(P,Q_k) < u`).  Hence `A_P = [0,u]` in every case, which is the only
fact conclusions (1)–(3) consume.  If the endpoint flag is priced at all,
the lemma's own hypothesis puts it in `T_a^searrow`, so `u < 1 < v` still
gives `H(P,d)` outside `U^full`.

**Minimal exact replacement.**  In the proof of Lemma 3.1, replace the
paragraph containing `(3.2)` and the following sentence by:

> Fix a pole representative `Q = P_j` whose ray contains `F`; then
> `O(P,Q) >= u` by (1.2).  If the segment `I_(P_j)([0,v_j])` continues
> strictly above `F` (`u < v_j`), then `O(P,Q) > u` is impossible: with a
> sufficiently divisible common denominator, agreement above `u` gives the
> same coefficient at height `u`, hence the same corrected-3.18 child on
> the pole segment, making `d` the pole-chain arrival — contrary to
> selection.  So `O(P,Q) = u` and `min(v_j, O(P,Q)) = u`.  If instead the
> segment ends at `F` (`u = v_j`), then `O(P,Q)` may exceed `u`, but
> `min(v_j, O(P,Q)) = v_j = u` regardless.  Segments not through `F`
> contribute `min(v_j, O(P,P_j)) < u`.  Hence `A_P = [0,u]`.

Everything after that point in the packet is unchanged, and the MFE
derivation in its Section 4 is untouched: it consumes only conclusions
(1)–(3), never `(3.2)`.

## 4. Cyclic orbits and corrected Statement 3.18 (attack 4)

The repair explicitly denies the false stronger premise ("The literal
premise that flag equality has no identifications beyond a cyclic orbit is
false") and uses the cyclic theory for exactly one thing: distinct
effective orbits at `F` give distinct actual next coefficients, hence —
by Section 1 — distinct one-step children and distinct directions.

I verified the citation and, separately, the mathematics.

**Citation.**  Printed Statement 3.18 (p. 18) reads "…there exists a unique
`ν_F`-th root of unity, `ε` such that `F*c` exists" — the known garble
whose corrected reading `F*(εc)` is recorded in AF2 (§1: "every root of
`p_F` yields exactly one direction (unique `ε` per `ν_F`-orbit; `F*0`
exists iff 0 is a root)") and used by the passed Prop 6.7–6.8 audit ("the
realizable representative selected by corrected Statement 3.18").  The
final delta gate — overall verdict FAIL — passes precisely the clause the
repair leans on, in these words: "Formal deck quotient equals the EW2
root-orbit quotient — PASS — …distinct effective orbits have distinct
coefficients at height `u` and therefore distinct `F*c` directions.  This
supplies the previously missing bridge for arbitrary rational `u`,
including the fixed zero orbit."  The gate's FAIL is confined to
cross-fibre `κ` transport, which this repair keeps rejected in Sections 0
and 5.  Citing one passed clause of a failed gate is legitimate here and
is done with the failure explicitly kept in force.  The quotient-route
packet independently establishes the stabilizer action at arbitrary
rational truncation heights, "not only for characteristic vertices."

**Independent recomputation.**  Let `F = I_P(u)`, `n = κu`, and let the
prefix-stabilizer subgroup of the deck group act on prefix-compatible raw
series; by the cyclic-semi-invariance computation it acts on the
coefficient at exponent `u` through the full cyclic group `μ_ν`
(`ν = ν_F` at vertices by Definition 3.1/Notation 3.4).  Three facts
combine: (i) deck substitutions fix each point, permuting its
representatives, so every point through `F` realizing raw coefficient `c`
also realizes every `ζc`, `ζ ∈ μ_ν`; (ii) if two points both admit raw
series with the common prefix and one and the same coefficient at `u`,
their point contact exceeds `u`, so by Statement 3.2(ii) their
`Ω`-representatives agree at `u`; (iii) hence if two points through `F`
had `Ω`-coefficients `εc ≠ ε'c` in one orbit, fact (i) would give the
first point a raw representative with coefficient `ε'c`, forcing contact
`> u` with the second and, by (ii), `εc = ε'c` — contradiction.  So each
nonzero effective orbit carries **exactly one** actual coefficient (the
unique `ε` of corrected 3.18), the zero orbit is fixed, and distinct
orbits, being disjoint, give distinct actual coefficients, hence distinct
children `F*a ≠ F*b` for `a ≠ b` (agreement at height `u+1/κ` would force
equal `Ω`-coefficients at `u`).  The bridge is true, not merely cited.
No assumption that cyclic orbits are the only identifications is used
anywhere: flag equality is handled by contact alone.

## 5. The Statement 7.3 witness, `u < 1`, `v > 1` (attack 5)

All three legs check against the primary source:

- **`u < 1`.**  Notation 6.1 (p. 29): `T_a^searrow = {F ∈ T_a^+ : d_F <
  (1−π(F))·deg(p_F)}`.  With `d_F > 0` this forces `deg(p_F) >= 1` and
  `1 − π(F) > d_F/deg(p_F) > 0`.  Proposition 6.7's own printed proof
  states the same ("Since `F ∈ T_a^&`, one gets `u < 1` from the
  definition").  The locally priced base is in `V_a ∩ T_a^searrow` by the
  AF2 Section 2 setting, so the hypothesis is grounded.
- **`v > 1`.**  Statement 7.1 (p. 35) with its printed proof:
  `F ∈ T_(a,cv)` gives `0 = d_F + d_(g,F) > 1 − π(F)` via Proposition 4.1.
- **Same ray, genuinely beyond the exit.**  Statement 7.3 (p. 35) is
  quantified over a single end: "Set `P ∈ R̄_a \ R_a`.  Assume that there
  exists `u ∈ Q_+` such that `I_P(u) ∈ T_a^nearrow`.  Then there exists
  `v ∈ Q_+` such that `I_P(v) ∈ T_(a,cv)`."  The witness is `I_P(v)` on
  the very ray `P` realizing the certified nearrow microstep — not merely
  somewhere in the fibre.  Since `A_P = [0,u]` and `v > 1 > u`, the
  witness and the entire segment `I_P((u,v])` lie outside `U^full`; the
  witness is beyond the exit edge in the exit's own component.

Two conformity notes, neither a defect of this packet: Statement 7.3 is
printed without proof (source-Statement convention; its use is inside the
already-passed Section 9/AF2 perimeter, AF2 R3 with the printed p. 53
usage), and Statement 7.2 — the known unproved sidedness statement — is
**not** used by this repair at all.

## 6. Can two selected witnesses coincide? (attack 6)

Abstractly: coincidence `H(P,d) = H(P',d')` forces equal heights
`v = v'` and `O(P,P') >= v > 1`.  I attempted honest Puiseux realizations
of every escape route:

- **Different bases `F ≠ F'`.**  The witness flag's rootward segment is
  representative-independent (Section 2), so the set `{t : rho_H(t) ∈
  U^full}` is one interval computable from either representative:
  `[0,u] = [0,u']`.  Hence `u = u'` and `F = rho_H(u) = F'`.  No series
  can be written that meets `U^full` in two different terminal intervals,
  because the intersection is a single set, not a per-representative
  object.
- **Same base, different orbits.**  The two witness rays realize different
  actual coefficients at height `u` (Section 4), so their contact is
  exactly `u` — computed on `Ω`-representatives via Definition 3.2 and
  Statement 3.2, matching AF2 R4 (`O(P,P') = π(F) < π(H)`).  Coincidence
  at height `v > 1 > u` would need contact `>= v`.  Impossible.  A
  concrete attempt sharpens where the danger actually lives: the branch
  with representatives `y = ±i·x^(-1/2) + …` gives a raw engine two
  "roots" `±i` at height `1/2`; if priced as two exits, their "witnesses"
  are literally the same point set.  But `±i` is one `μ_2`-orbit and one
  point-level direction; the tree is built on points, and the selection
  prices orbits.  The countermodel is thus exactly the raw/actual
  confusion, and it is excluded by the delta-gate bridge (an input), not
  by Definition 3.3 alone — which is precisely how the repair divides the
  labor.  No honest counterexample exists within the stated hypotheses.
- **Different heights.**  `π` is well-defined on `T_a^*` (Notation 3.1),
  so `v ≠ v'` gives distinct flags trivially.

## 7. Down-direction exclusion and merge accounting (attack 7)

The exclusion "every locally priced remaining direction is a positive
selected exit" is an input from the repaired Prop 6.7–6.8 package, cited
correctly: the audit's Section 4 recursion produces the terminal pole at
`F_N = I_P(v)` with **all** grid ancestors `F_j = I_P(u + j/κ)` on the
same branch ("the pole is genuinely on the same branch, not merely
somewhere above the same equivalence class"), and its Section 5 bridge
distinguishes the one-grid-step microstep from the next vertex and carries
a searrow microstep to a same-branch down vertex and pole.  Consequently a
class-3 direction with a searrow microstep would put its own first edge
inside `U` (the manufactured pole is a y-side pole, and `U^full` is the
union over **all** y-side poles), contradicting class 3.  This argument is
local to one direction and one vertex, so it applies verbatim at merges;
the other incoming pole-chain orbits at a merge are class 1 and excluded
before pricing (Section 9 audit merge rule, confirmed by the prior
review's merge rows).  Charging is once per actual exit orbit: `D_F` is a
set of direction-orbits at the vertex `F` of the set-theoretic union
`U^full` (shared suffixes appear once), and Lemma 3.1(2)–(3) makes the
witness assignment injective over all of `U`, so no merge price can be
duplicated per incoming pole path.  The residual obligation that engines
must not repeat `D_F` per path is correctly left as a consumer
requirement in the disposition, not silently claimed.

## 8. The (C7.1*) application and exact MFE form (attack 8)

The weighted-Euler repair states, at its passed scope:

```text
td(f,g) >= 1 + sum_(F in T_(a,cv)) kappa_F*(pi(F)-1)     (C7.1*)
```

"for every fibre `f=a`, and hence the same inequality for every subset of
pairwise distinct critical-value flags."  `T_(a,cv)` (Notation 7.1) has no
component restriction, so the admissible set may combine y-side and x-side
flags of the one prescribed fibre.  Conditional on distinctness — now
supplied by Lemma 3.1 for the y-side witnesses and by Statement 3.3
(`T_a^*` has two components, printed p. 11) for x-versus-y — apply
(C7.1*) once to `{x-side witness} ∪ {H(F,d)}`:

```text
td - 1 >= kappa_x*(pi_x - 1) + sum_(F,d) kappa_H*(pi(H)-1)
       >= psi + sum_(F in U) lambda_F^exit,
```

using the Section 9 audit's certified x-side weight (`psi*l_f < k_f` gives
integral weight at least `psi`; audit Section 4.6, the same single x-side
vertex added once) and the corrected price (4.1) per witness
(`kappa_H(pi(H)-1) >= D_F/mult − K_F`, or divided by `ν_F` for the zero
orbit; audit Section 4.5) with each witness's **own** `kappa_H` — no
transport.  This is exactly `sum lambda_F^exit <= td(f,g) − 1 − psi`,
i.e. (MFE), no more and no less.

## 9. Hidden-upgrade sweep (attack 9)

Checked line by line: printed `(22)` — absent; literal `delta_a` — absent;
`(22-cl)` — rejected in Sections 0 and 5; cross-fibre `kappa` — rejected,
with the delta gate's counterexample explicitly kept in force;
equality/slack — none (inequality only, "It proves neither an arbitrary
quotient claim nor a cross-fibre transport theorem"); MP8 no-refinement —
rejected; "every actual cv flag is a selected witness" — not claimed (the
producer's quarantine list survives); root census / root `M ≠ 1` — absent;
`td = 6` exclusion — absent.  The disposition clause "any per-incoming-edge
price, equality upgrade, or fixed-`kappa` transport … must fail closed" is
the correct fail-closed posture.  No hidden upgrade found.

## 10. Classification

```text
Quotient model (1.1)/(1.2) at the exact cv-bearing object:   CONFIRMED (Definition 3.3, definitional)
Rootward segment representative-independence; A_P closure:   CONFIRMED
Lemma 3.1 conclusions (1)(2)(3):                             TRUE as stated
Lemma 3.1 written proof, display (3.2):                      FALSE as universally quantified
                                                             (pole-vertex endpoint case); one-sentence
                                                             patch given in Section 3; no consumer reads (3.2)
Orbit-to-direction bridge (corrected 3.18 + delta gate):     input, citation verified, and independently
                                                             re-derived here from Statement 3.2 + deck action
u<1 / v>1 / same-ray witness (Not 6.1, St 7.1, St 7.3):      CONFIRMED against printed pp. 29, 33–35
Witness coincidence (same or different bases):               impossible; honest Puiseux attempts collapse
                                                             to the raw-conjugate confusion, which the
                                                             orbit selection excludes
6.7/6.8 down-exclusion incl. merges; once-per-orbit charge:  inputs correctly cited; merge arrivals
                                                             excluded before pricing
(C7.1*) + x-side psi step; exact MFE form:                   CONFIRMED at passed scope
Hidden upgrades ((22), delta_a, (22-cl), kappa, equality,
MP8, census, td=6):                                          none; all remain rejected
Overall:                                                     PASS-WITH-REPAIR
```

**Consequence.**  With the Section 3 replacement applied, the repair packet
discharges the sole ambient attachment blocker recorded by the prior
hostile review, and the frozen producer's (MFE) inequality is validated at
the selected-exit/shared-inequality scope: consumers must use `U^full` (or
its vertex-edge realization) with one orbit-set `D_F` per vertex, price
selected exit-orbits once each, and must not revive any quarantined
equality, transport, census, or `td=6` claim.  This review does not itself
authorize flipping any engine or ledger to GREEN; it certifies the
mathematics that a conforming consumer update may now cite.
