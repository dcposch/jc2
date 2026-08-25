# Blind whole-portfolio ideation — round `20260825T0126Z` — coordinator

Cutoff: 2026-08-25T01:26Z.  This note was completed before reading any sibling
submission from the significant-news round.  I reread the complete 46-row
canonical inventory and the post-cutoff evidence.  None of the cards below
is a theorem or a JC2 conclusion; every new mathematical child is
review-gated, while producer work may proceed provisionally.

## News that changes allocation

1. **TD6:** the fixed source-typed two-center section `(C,1,U)` now has a
   producer-exact exhaustive open cover, and the generic full three-center
   `(C,V,U)` computation independently returns the same obstruction
   `-k/50`.  The two-center claim is under hostile review; the trivariate
   exceptional divisors are running on AWS.
2. **AS:** the campaign caught a divided-Frobenius source error before
   promotion.  Corrected rows leave `260847`, `33225`, and now `11881`
   visible states through degrees 11, 10, and 9.  Degree nine has enormous
   affine completion fibres.  Simple sequential census is no longer the
   right endgame object.
3. **Q8:** the selected terminal system is a balanced three-value Belyi
   problem with even infinity contact and Mason equality.  Exact Frobenius
   data make the Galois action on the eight Q8 contacts primitive, reducing
   geometric grouping to one eight-contact component or eight singleton
   components.  Exact component races are live on AWS.
4. **External sweep:** no new disclosed plane proof or counterexample was
   found.  Gao's `2608.00222` is explicitly for dimensions greater than two;
   `2605.12302` is the nonconstant/nonvanishing **real** Jacobian problem;
   the recent `e=3` polydegree candidate concerns closures of automorphism
   strata.  None changes a JC2 premise.  Search-index and private-claim lag
   remain limitations.

## New card A — AS finite Kuranishi automaton / singular Hensel cycle

This is the highest-value disproof card.

For a fixed degree/support cap, write the full coefficient map

```text
Phi(P,Q) = coefficients(det J(P,Q)-1)
```

over `Z_3`.  At the Artin--Schreier special fibre, split the fixed mod-three
tangent operator into image, kernel, and its Cartier/de Rham cokernel.  The
accepted-digit solves are the image equations; the source-honest divided
rows `Q12,Q11,Q10,Q9,...` are initial coordinates of the finite Kuranishi
obstruction on the kernel/carry state.

The campaign should stop thinking of the `3^16` and larger completion fibres
as objects to enumerate.  Instead:

1. prove a canonical bounded state consisting of the Cartier obstruction,
   capped quotient residues, and the integer carry data needed for the next
   division;
2. compile the exact transition correspondence `R subset S x S` over `F3`;
3. search symbolically for either a reachable directed cycle/positive-
   dimensional recurrent component, or a finite ranking function proving the
   reachable graph acyclic;
4. at each survivor, test a **two-step or multi-step Kuranishi Jacobian**, not
   the necessarily singular one-step determinant Jacobian.  A full-rank
   obstruction derivative gives a singular-Hensel continuation theorem and
   can replace all later digit enumeration.

A reachable recurrent state plus a proved transition-lifting lemma gives an
infinite bounded-degree `Z_3` polynomial Keller lift by compactness/Koenig;
the preserved collision gives a characteristic-zero counterexample after
base change.  Conversely, a finite acyclicity certificate kills this bounded
AS branch.  The immediate falsifier is failure of state sufficiency at Q9;
the immediate positive test is the multi-step obstruction rank on the first
emitted Q9 witness and on the dominant Q10 fibres.

Software should use decision diagrams or sparse algebraic correspondences,
not leaf enumeration, and must reconstruct every divided integer carry before
reduction.  The just-caught Frobenius error is the mandatory negative control.

## New card B — TD6 universal adjoint residue behind `-k/50`

This is the highest-value proof card.

The same unit `-k/50` has survived the fixed line, the complete two-center
cover, and two independent generic trivariate center computations.  Treat
that persistence as evidence for a source-level cohomology/residue class, not
as a reason to add moduli one at a time.

Construct the universal first-band adjoint functional `ell` before solving
pivots.  Test symbolically whether

```text
ell(P12) = -k/50,
d/dm ell(P12) = 0 modulo the original rows
```

for every remaining licensed center, dead-stretch, boundary, pole, and F1
modulus `m`.  The target is an invariant pairing in the cokernel of the
source transport—ideally a residue of the two-form—whose value is independent
of all section choices.  If successful, one universal identity kills the
whole connected TD6 source family; rank-change/Fitting divisors and projective
infinity still require raw rebuilds.  If one derivative is nonzero, it names
the smallest real escape modulus and prevents further blind atlas growth.

The current V8/V9 agreement is the positive control.  The V6 forbidden-`P`
denominator is the negative control: no universal functional may cancel a
nonunit chart factor.  This card connects avenues 2, 3, 27, 28, and 31 at a
typed finite-family level without claiming the missing global landing or
topological-degree ceiling.

## New card C — Q8 singleton Taylor/Belyi divisor obstruction

The live component computation has a binary branch:

- one component with all eight Q8 contacts is conditionally killed by the
  reviewed finite-contact theorem;
- eight singleton components survive the grouping argument.

For the singleton branch, do not search unrestricted coefficient space.
Use the exact terminal form

```text
Z=T^3,  h=C*T^2/(T')^3,
A_T-lambda B_T squarefree,
deg rad(A_T B_T (A_T-lambda B_T))=D+1,
e_pass even.
```

Factor the Wronskian divisor passportwise.  At an `A_T` root of multiplicity
`alpha<=3`, `ord(h)=3-alpha`; at a `B_T` root of multiplicity `beta`,
`ord(h)=beta+3`.  Pull the two original Taylor families and the exact Q8
quotient jet into these divisor variables and seek a residue/valuation
inequality uniform in `D`, with the exact `e_pass=2` terminal solution as a
mandatory non-kill control.  Computationally, compile the Taylor numerators
against the universal Belyi Wronskian factorization and use adjoint sparse
linear algebra to find the first combination whose pole divisor cannot be
cancelled.  A finite local jet may then determine or exclude the singleton
component without a monolithic absolute primary decomposition.

If no uniform inequality appears, use the local Q8 jet as Hermite--Pade data
to enumerate the smallest even-contact passports.  Any degree cutoff must be
proved from the Taylor equations; Mason equality alone supplies no cutoff.

## New card D — cross-lane obstruction calculus

The AS Cartier rows, TD6 left-null unit, and Q8/Taylor residues are three
forms of the same operation: solve an exact differential image equation and
pair the remainder with a finite cokernel.  Build one small library that:

- constructs the image/cokernel over the correct base ring or quotient;
- retains divided integer provenance before reduction;
- transports adjoint witnesses across charts without inverting nonunits;
- emits a source-row cofactor certificate and a perturbation negative
  control.

This is a software accelerator, not a theorem, but it directly targets the
campaign's dominant source-error and exceptional-stratum failure modes.

## Complete avenue disposition

| Rows | Disposition after this round |
|---|---|
| 1 GGV | retain as certified landing/farm input; no untyped wider brute force |
| 2 sheet/Eggers--Wall | **continue**, with TD6 universal-adjoint card and full landing still charged |
| 3 strip ODE | retain as the model for the universal residue functional; no independent expansion |
| 4 formal germs | **continue only through the AS finite-state/Kuranishi formulation** |
| 5 JvdK descent | hold; no new cusp-avoidance invariant |
| 6--7 AM / asymptotic set | reserve only when a live component supplies typed place data |
| 8--12 inverse/Lee--Li/Zhao/face | hold or stopped at recorded gates |
| 13--16 Dixmier/PDO/D-module | defensive reserve; no plane candidate |
| 17--18 stabilization/GIT | stopped as global routes |
| 19 char-p/Witt | **continue at highest priority through card A** |
| 20 p-curvature | no standalone client beyond card A |
| 21 p-adic/model theory | merge into the proved singular-Hensel/Koenig endpoint of card A |
| 22--24 Diophantine/analytic/real | stop; newest real paper is type-incompatible |
| 25 Hurwitz | **continue on selected Q8 with Taylor coupling** |
| 26 primitive Galois | promoted from generic idea to live Q8 discriminator; no global td claim |
| 27--31 links/BMY/LND/surfaces/ZMT | reserve as receivers for typed Q8 or TD6 data, never free-standing slogans |
| 32 collision ideal | use only inside named Q8 projection/component computations |
| 33 symplectic primitives | untwisted form remains costume; card B needs the typed adjoint residue instead |
| 34--35 tangent sweep/dimension descent | hold; no new plane mechanism |
| 36 guided search | only source-typed AS transition search is licensed |
| 37 finite-field census | diagnostic/Galois/support role only |
| 38 tropical | reserve for support pruning after a source ideal exists |
| 39--45 cohomology/free/deformation/dynamics/Ritt/Moskowicz/differential Galois | stopped or low reserve; no new receiver |
| 46 formalization | certify promoted universal lemmas after discovery; never a discovery substitute |

## Campaign/software acceleration

1. Introduce a content-addressed AWS job broker: transitive source-closure
   manifest, immutable tag, host/resource cap, heartbeat, stdout/stderr/meta,
   automatic harvest, and exact parent/child DAG.  Refuse launch when an
   imported file is absent.  This would have prevented every omitted-source
   startup failure in the last cycle.
2. Race mathematically distinct exact algorithms on idle cores and cancel
   losers only after one yields a verifiable certificate.  Keep modular
   grouping support-only until an exact char-zero contraction/idempotent lands.
3. Make errata machine-propagating: a source claim marked quarantined should
   taint every descendant manifest automatically.  The old AS N11 result is
   the test case.
4. Keep reviewers no-Bash and background.  Producer branches may consume
   reasonable provisional results, but canonical promotion requires exact
   scope, source closure, hostile verdict, and any demanded shell replay on
   AWS.
5. Trigger the next whole-portfolio round in at most twelve hours, or sooner
   on any of: Q8 component dichotomy resolved, TD6 trivariate exceptional
   cover closed, an AS recurrent state/smooth Kuranishi point, or a new
   external plane claim.

## Ranked allocation

1. AS finite Kuranishi automaton / multi-step Hensel rank.
2. Q8 exact component result, then singleton Taylor/Belyi divisor gate.
3. TD6 universal adjoint residue while the trivariate raw atlas runs.
4. Background exact Q-membership for double-B and all hostile reviews.
5. Build the AWS/provenance broker in parallel with mathematics; it pays for
   itself after one avoided source-closure failure.

No proof or counterexample to JC2 has been found.
