# Hostile review: quadratic ramification connectedness and F5 lattice closure

Verdict: CONFIRM_WITH_CORRECTIONS.

I confirm the mathematical closure of the stated smooth projectively finite
quadratic, reduced squarefree infinity, dominant-A2-first-leg, rational-forest
scope, charging the four integration/support packets only inside their stated
scopes. The corrections are custody/scope and wording repairs, not mathematical
failures of the connectedness or F5 lattice argument.

## 1. Custody and scope

- CONFIRM_WITH_CORRECTIONS. Current repository HEAD is
  `78da50bd31b3f7fd8d07ed8fc5ddbbf0ad4290d1`, matching the prompt basis. The
  five full-file hashes and body hashes checked against the prompt and embedded
  seals. However, the main packet itself records frozen basis
  `1efd7a76538e3fcdf51b999563262afc40d58947` at
  `xmodel/bd-a2-ramification-connectedness-f5-lattice-closure-sol56-20260830.md:5`
  and in its seal at line 414. Promotion should either correct that metadata or
  state explicitly that this is a sealed packet produced on `1efd...` and
  reviewed at `78da...`.
- The producer invokes the bidegree rational-forest classification within
  reduced squarefree infinity only, and keeps `F8,F9` out because they have no
  rational-tree refinement. This matches
  `xmodel/bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md:145-158`.
- It invokes the attachment packet within smooth, reduced, projectively finite
  quadratic scope only. The no-H-component, exact boundary critical set,
  nonemptiness, and unit/localization injection are exactly the promoted
  statements at
  `xmodel/bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md:86-108`
  and `:149-160`.
- It invokes the F5 local different packet only at the smooth F5 local triple
  point and only for the source different split `8=5+3`. This matches
  `xmodel/bd-a2-f5-local-different-two-branch-coordinator-integration-sol56-20260830.md:160-190`.
- It invokes the class-group rank no-go packet only for Picard rank eleven and
  for rejecting the old raw rank shortcut. This matches
  `xmodel/bd-a2-quadratic-classgroup-rank-no-go-sol56-20260830.md:117-153`.

## 2. Ramification class and connectedness

- CONFIRMED. In `P2 x P1`, with `X ~ 2A+3B`,
  `A^2=3`, `A.B=2`, `B^2=0` on `X`. Adjunction gives
  `K_X=(-3A-2B+2A+3B)|X=-A+B`. Since `pi^*K_P2=-3A`,
  the relative ramification class is
  `R_pi=K_X-pi^*K_P2=2A+B`, as stated at main lines 63-68.
- CONFIRMED. `O_X(2A+B)` is the restriction of `O(2,1)`, hence ample. The
  Jacobian determinant is nonzero because `pi` is generically finite in
  characteristic zero, so `R_pi` is a nonzero effective ample Cartier divisor.
- CONFIRMED. The Hodge-index proof of connected support is valid for
  nonreduced Cartier divisors and reducible support. If
  `D=D_1+D_2` with nonzero effective pieces and disjoint supports, ampleness
  gives `D.D_i>0`, hence `D_i^2>0`, and `D_1.D_2=0`; this gives two orthogonal
  positive directions, impossible on a smooth projective surface.
- CONFIRMED. The no-infinity-component bridge is supplied by the attachment
  integration: reduced `H`, characteristic zero, and finiteness near `H`
  exclude a critical Cartier component contained in `H`. Therefore every
  component of `R_pi` has affine generic point, and the projective support is
  the closure of reduced affine ramification plus boundary intersection
  points. There is no loophole from isolated boundary points.

## 3. Eliminating F1, F2, F4, F7

- CONFIRMED. The promoted attachment packet gives at least two distinct
  physical boundary critical points in `F1,F2,F4,F7`, and the exact critical
  set says those points are precisely attachments of the projective
  ramification support.
- CONFIRMED. Connectedness of `Supp(R_pi)` is enough to replace the older
  irreducibility hypothesis. In any resolved full boundary forest, the total
  transform of connected `H` is a tree and the total transform of connected
  `Supp(R_pi)` is a tree. Two distinct physical attachment points give two
  disjoint local joining paths between those trees; contracting the two trees
  gives two parallel edges, hence first Betti number at least one.
- Tangencies, embedded exceptional chains, singular ramification components,
  and multiple edges do not repair this. Blowups subdivide edges or add
  pendant vertices; they do not remove the two independent connections.
- Correction: phrase this as "the connected reduced support of the Cartier
  ramification divisor" rather than "connected total transforms belonging to
  `Supp(R_pi)`" when using graph language. Multiplicities play no role.

## 4. F5 conic-bundle lattice

- CONFIRMED. The conic-bundle structure has nine simple reducible fibres and
  `rho(X)=11`, as in the charged rank packet. With `F=B`, a section `S`, and
  fibre components `E_i` disjoint from `S`, the basis has
  `S^2=-2`, `S.F=1`, `E_i^2=-1`, and omitted pairings zero.
- CONFIRMED. In F5,
  `L=F-E_1`,
  `A=2S+5F-sum_{1}^{9}E_i`,
  `T=S+4F-sum_{2}^{9}E_i`,
  `K_X=-A+F=-2S-4F+sum E_i`, and
  `R_pi=2A+F=4S+11F-2sum E_i`. These recover
  `L^2=-1`, `S^2=T^2=-2`, `L.S=L.T=1`, `S.T=2`, and
  `R_pi.(L,S,T)=(2,3,3)`.
- CONFIRMED. If an irreducible curve `Z` has `A.Z=0`, then `pi(Z)` is a
  point and the ambient embedding forces `Z={point} x P1`; hence `F.Z=1`,
  `Z` is a smooth rational section of `q`, and adjunction gives `Z^2=-3`.
  Solving `Z.L=Z.S=Z.T=0` and `Z^2=-3` gives exactly
  `Z_I=S+2F-E_1-sum_{i in I}E_i` with
  `I subset {2,...,9}`, `|I|=4`.
- CONFIRMED. `Z_I.Z_J=1-|I cap J|`. Distinct effective A-null curves are
  different vertical copies `{point} x P1`, hence disjoint, so coexistence
  requires `|I cap J|=1`. The "no three" claim is true but unused here because
  the later multiplicity bound gives total A-null multiplicity at most two.
  It may be deleted for economy.

## 5. Local F5 different to global carriers

- CONFIRMED. The local packet proves two reduced smooth source-different
  branches at the unique boundary point, transverse to each other, with
  contact vectors `(1,1,1)` and `(1,2,2)` against `(L,S,T)`. The weight-three
  branch is the transverse one and the weight-five branch is tangent to the two
  `(1,1)` components.
- CONFIRMED. If the two local germs lay on one global prime, they would give
  two distinct normalization points over the connected infinity tree, producing
  a cycle. Thus any survivor has distinct global primes `D_3,D_5`. Since the
  local Cartier equation is reduced along both germs, their global Cartier
  coefficients are one.
- CONFIRMED. These two carriers exhaust `R_pi.(L,S,T)=(2,3,3)`. Every other
  effective component has nonnegative intersection with each `H_i`, hence zero
  intersection with each `H_i`, hence `A.C=0`, so it is one of the `Z_I`.
- CONFIRMED. If `x=F.D_3` and `y=F.D_5`, then `x,y>0`: a curve with
  `F`-degree zero lies in a conic fibre and has `A`-degree one or two, not
  three or five. Since `R_pi.F=4`, the remaining A-null Cartier multiplicity
  is `N=4-x-y`, so the only partitions are `2`, `1+1`, `1`, or none, exactly
  as enumerated.
- CONFIRM_WITH_CORRECTIONS. `D_3.D_5=1` is a necessary survivor condition:
  the local transverse boundary intersection already contributes one, and any
  further intersection would independently create a second path and violate
  the rational-forest hypothesis. The enumeration should explicitly say it is
  performed after imposing this necessary survivor condition.

## 6. Equations and enumeration

- CONFIRMED. For `j=2,...,9`,
  `D_3=xS+(2x+1)F-(x-1)E_1-sum a_jE_j` and
  `D_5=yS+(2y+2)F-(y-1)E_1-sum b_jE_j`. Here
  `a_j=D_3.E_j>=0`, `b_j=D_5.E_j>=0`, and integrality is Picard-lattice
  integrality.
- CONFIRMED. The contact vector with `T` gives
  `sum a_j=4x` and `sum b_j=4y`. Total class equality gives
  `a_j+b_j+c_j=2`, so `0<=a_j,b_j<=2` and no unbounded coefficient is hidden.
- CONFIRMED. With `K_X=-A+F`, rational normalization gives
  `delta_3=(D_3^2+x-1)/2` and
  `delta_5=(D_5^2+y-3)/2`, both integral and nonnegative. The square formulas
  and `D_3.D_5=1` give exactly main equations (4.7).
- CONFIRMED. I replayed the enumeration over all labelled four-subsets of
  `{2,...,9}`. Labelled counts are: doubled `Z`, 70 solutions, one permutation
  orbit; two distinct simple `Z`s with the required one-point subset
  intersection, zero; single `Z` rows `(1,2)` and `(2,1)`, zero; no-`Z` rows
  `(1,3),(2,2),(3,1)`, zero. This does not assume smoothness or general
  position beyond the rational-normalization delta test and the promoted
  forest condition.
- CONFIRMED. The unique orbit is
  `D_3=S+3F-sum_{j in J}E_j`,
  `D_5=S+4F-sum_{j in J}E_j`,
  `Z=S+2F-E_1-sum_{i in I}E_i`, with `J` the complement of `I` in
  `{2,...,9}`. Then
  `D_3^2=0`, `D_5^2=2`, `Z^2=-3`,
  `D_3.D_5=1`, `D_3.Z=3`, `D_5.Z=4`, and
  `R_pi=D_3+D_5+2Z`.

## 7. The two F5 contradictions

- CONFIRMED. The class relation is exact:
  `D_3+Z=2S+5F-E_1-sum_{2}^{9}E_i=A=L+S+T=H` in `Pic(X)`. Restricting to
  `Y=X-H` gives `[D_3]+[Z]=0` in `Cl(Y)`. The charged unit theorem gives
  `O(U)^*=O(Y)^*=C^*`, so the localization boundary map from the free group on
  reduced ramification primes into `Cl(Y)` is injective. The nonzero relation
  `[D_3]+[Z]=0` is therefore impossible. The Cartier coefficient `2` of `Z`
  in `R_pi` is irrelevant because the localization injection is on reduced
  primes.
- CONFIRMED. Independently, the graph contradiction survives every embedded
  resolution. The boundary point gives a path from `D_3` to `D_5` through the
  resolved infinity/different local configuration. Since `Z.H=0` and
  `D_3.Z,D_5.Z>0`, there is an affine interior path from `D_3` to `D_5` through
  `Z`. These paths are distinct. Blowups only subdivide them or add pendant
  exceptional vertices, so the cycle cannot disappear.

## 8. Maximum safe theorem

CONFIRM_WITH_CORRECTIONS. The safe promoted theorem is:

For a smooth irreducible incidence surface `X subset P2 x P1` of class
`2A+3B`, with `pi:X->P2` generically finite and finite near reduced squarefree
infinity `H`, under the promoted dominant `A2 -> U` first-leg hypotheses whose
resolved boundary is a rational forest and whose unit consequence is
`O(U)^*=C^*`, the reduced rational-forest infinity types
`F1,F2,F4,F5,F7` are impossible. Types `F3,F6` are outside this theorem because
they are projective-basepoint/nonfinite near infinity types, and `F8,F9` have
no rational-tree refinement.

This is not a general map-existence or nonexistence theorem. It does not cover
nonreduced infinity, singular incidence surfaces, affine coefficient common
zeros, target or fibre degree drops, basis minimization, general quadratic
closure, cubic closure, primitivity, counterexamples, or JC2.

## Repairs before promotion

1. Fix or annotate the frozen-basis metadata mismatch in the main packet.
2. State `D_3.D_5=1` as a necessary survivor condition; if it fails, the graph
   contradiction has already occurred.
3. In the F5 section, keep the labels explicit: `D_3` is the weight-three
   transverse branch and `D_5` is the weight-five tangent branch. Do not refer
   to tangent lines as branches.
4. Either delete the unused "no three pairwise one-intersecting" sentence or
   add its one-line inclusion-exclusion proof.
5. In the final theorem, repeat all scope exclusions listed above. In
   particular, do not state projective basepoint/nonfinite `F3,F6`,
   nonreduced infinity, singular incidence, affine coefficient common zeros,
   degree drops, basis minimization, general quadratic closure, or JC2 closure.

Cheapest next check: no CAS or larger lattice run is needed. The decisive next
action is a metadata/scope patch to the producer followed by a line-level
review that the promoted theorem text contains exactly the hypotheses in
Section 8.

No new exit-price assertion is made in this review.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11936`.
- Body SHA-256:
  `5e76465483713b91c9f65d9792d046f450d98e63fdb2bb123645b2938c2fdc03`.
- Frozen basis: `78da50bd31b3f7fd8d07ed8fc5ddbbf0ad4290d1`.
