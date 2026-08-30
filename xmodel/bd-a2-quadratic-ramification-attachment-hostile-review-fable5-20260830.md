# Hostile review: quadratic ramification-attachment dichotomy

Date: 2026-08-30 UTC  
Reviewer: Fable 5 (independent, hostile)  
Review basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1` (child of producer
basis `4c91d6fc`; sealed contents unchanged)  
Producer under review:
`xmodel/bd-a2-quadratic-ramification-attachment-dichotomy-sol56-20260830.md`

## 0. Custody

All four input full-file SHA-256 values match the tasking block. The
producer's body seal recomputes exactly (`9399` bytes,
`c37282a42af45c57e723dddd061ce2681203564df1b76008e8001206b2c69199`). The two
promoted integrations and the block-descent promotion are consumed as
promoted, not re-reviewed. No CAS was required; every check below is a hand
computation, plus one integer intersection-ring evaluation on
`P2 x P1` (`A^3=B^2=0`, `A^2B=1`) reproduced in the review log.

Conventions verified once and used throughout: `F_infinity` is cubic in the
fibre coordinates `[X:Y]` and quadratic in the `L_infinity` coordinates
`(s,t)`; a component of bidegree `(a,b)` meets each fibre `{pt} x P1` in `b`
points, so its projection to `L_infinity` has degree `b`, `(1,0)` is a full
fibre (vertical over an infinity direction), `(0,1)` a constant section, and
`p_a(a,b)=(a-1)(b-1)`. This matches the producer's stated orientation.

## 1. Itemized verdicts

### Item 1 — attachment-cycle lemma: CONFIRMED

Statement correct in all demanded regimes. My reconstruction, which I
recommend as the durable proof (the producer's "contract every resolution
subtree" sketch is correct but terse):

In any embedded resolution of `T union Q`, let `Gamma_T` be the total
transform of `T`: strict transforms of `T`-components plus every exceptional
curve over a point of `T`. (i) Blowing up a point on the current
`T`-configuration either adds a pendant vertex (free point) or subdivides one
edge (satellite point); blowups over points of `Q` off `T` never touch
`Gamma_T`. Hence if the resolved graph of `T` alone is a connected tree,
`Gamma_T` stays a connected tree under all extra blowups needed for `Q`,
and every point of the surface lying over a point of `T` lies on the support
of `Gamma_T`. (ii) The strict transform `Qtilde` is smooth (equal to the
normalization) and meets the SNC configuration transversally at distinct
points; each normalization branch of `Q` at `T` therefore contributes exactly
one edge from the single vertex `Qtilde` to some vertex of `Gamma_T` —
a strict-transform vertex if the attachment point was never blown up, an
exceptional vertex (possibly deep in an exceptional tree) otherwise.
Two distinct branches give two edges: to distinct vertices, the unique
`Gamma_T`-path closes a cycle; to one vertex, a parallel pair — a cycle in
the multigraph, which the promoted forest theorem explicitly retains.

Sub-cases: two physical points — two branches, covered; two analytic
branches over one point — two points of `Qtilde` (SNC separates them),
covered; tangency of a single branch — the resolution chain lengthens one
attachment path, still one edge, no cycle (producer's remark correct);
singular `Q` — branches are counted on the normalization, so a multibranch
point of `Q` on `T` is the two-branch case; exceptional trees — handled by
(i). Connected rational-tree infinity is sufficient: the lemma needs only
`Gamma_T` connected and acyclic inside the full resolved boundary graph, and
`H` is connected (`H^1(S,O(-2,-3))=0` from the promoted classification), so
in the application one gets a cycle inside the resolved `H union Rbar` graph,
contradicting the forest conclusion. `Q not subset T` holds trivially:
components of `Rbar` are closures of affine components.

### Item 2 — bridge from `H`-criticals to `closure(R_red)`: CONFIRMED

All steps verify in the chart `X:f(u,v,z)=0`, `H:f(0,v,z)=0`, and are
chart-independent (the critical locus of `pi|_X` is intrinsic; points at
fibre infinity are covered by the other affinization).

* Smooth branch point: `f_v v' + f_z z' = 0` with `v'=0`, `z' != 0` forces
  `f_z=0`. Non-immersive normalization points map to singular points of
  `H_red`, where both partials of `f(0,.,.)` vanish, in particular `f_z`.
  Collisions of components are singular points. So every classified
  attachment satisfies `f_z=0`. No case is missing: at a smooth point of `H`
  a branch is immersive.
* Cartier: `X` smooth irreducible and `pi` generically étale (char 0,
  degree 3) make `f_z|_X` a nonzerodivisor, so `{f=f_z=0}` is Cartier and by
  Krull pure dimension one. This is exactly what excludes an isolated
  critical point that the affine support could fail to reach.
* No component in `H`: if a reduced factor `h` of `f(0,v,z)=hg` divides
  `f_z(0,v,z)=h_z g+hg_z`, then `h | h_z g`; reducedness gives `h ∤ g`, so
  `h | h_z`, so `h_z=0` and `h=h(v)` — a `(1,0)` vertical component, whose
  fibre `{u=0,v=v_0} x P1` violates finiteness near `H`. Both hypotheses
  (reduced `H`, finiteness near `H`) are genuinely load-bearing; I found no
  way to drop either. Vertical factors and projective coefficient basepoints
  are precisely this excluded `(1,0)` case: a linear `l(s,t)` divides
  `F_infinity` iff it divides all four coefficient quadratics.
* Hence every critical/collision point lies on a pure-1-dimensional critical
  component meeting `Y` densely, i.e. in `Rbar`. Confirmed.

Reviewer strengthening (Lemma S, recommended for promotion): for `q in H`,
`f_z(q)=0` iff the vertical line through `q` meets `H` with multiplicity
`>=2` at `q`, iff `q` is a singular point of `H_red` or a smooth point where
`H` is tangent to the fibre direction (equivalently a critical point of the
projection). So `crit(pi) ∩ H` is **exactly** the classified attachment set:
no third kind of attachment of `Rbar` to `H` exists. This closes the one
architectural hole I could construct (an unclassified extra crossing would
have wrongly killed `F5` too, or produced uncounted cycles).

### Item 3 — degree convention and RH counts in `F1,F2,F4`: CONFIRMED

Convention audit above: degree over `L_infinity` is `b`. Riemann–Hurwitz on
the normalization `P1 -> P1` of degree `b` gives total ramification `2b-2`
with per-point contribution at most `b-1`; hence `b=3` (`F1`) and `b=2`
(`F2`'s `(2,2)`, `F4`'s `(1,2)`) each force at least two distinct
normalization critical points. One micro-repair: §3 says "smooth rational
component"; the argument is applied to normalizations of singular components
(`F1`, `F2`), where it is equally valid — reword to "rational component's
normalization" (degree still `b`, birational invariance).

Distinctness of physical attachments: within the `K=2` rows the
branch-incidence budget has `B=0`, so a normalization identifying two points
would create parallel edges (`b_1>=1`), contradiction; the producer's
injectivity argument is correct. A2/A4: a cusp is non-immersive, hence
critical; in the two-A2 case the two cusps already realize the two points at
distinct physical locations; in the one-A4 case the cusp contributes `e=2`
(one unit of the four), and counting forces at least one more distinct
critical point (the sealed witness `t -> (t^2/(1-t^3),t^2)` has exactly four:
`t=0` and `t^3=-2`; recomputed). Length-two/three contacts: I attacked the
degenerate `F2` variant where the `(0,1)` section passes through the cusp —
then the length-two contact is automatically concentrated there and the
configuration still has `K=2` (`delta=3, r=2`). The producer's argument
survives: the two critical points of the `(2,2)` normalization are distinct
physical points regardless of where the section sits, so two attachments
persist. Same for `F4`: either critical point of the `(1,2)` may coincide
with the length-three contact, never both. Confirmed.

### Item 4 — `F7` kill and `F5` survival: CONFIRMED

`F7`: `(2,1)` has `p_a=0`, hence is smooth; the two `(0,1)` sections are
disjoint (`(0,1).(0,1)=0`), so the two length-two contacts lie at distinct
physical points, one on each section. At such a point the fibre cubic has
roots `{z_0 (section), z_0 (curve), z_1}` — a double root — so `f=f_z=0`
holds; both points are attachments (concrete confirmation of Lemma S). No
merge is possible: they are distinct closed points of `X`, `Rbar` (closed)
contains both, and its normalization has at least one branch over each, so
an irreducible `Rbar` has two distinct branches at `H` and the cycle lemma
fires. Multiplicity of the ramification divisor is irrelevant to the reduced
support, and closure adds only points, never identifies them.

`F5` survival: all three components have `b=1`, so `2b-2=0` — no RH critical
points; the unique singular point is the triple point `p_0`. By Lemma S,
`crit(pi) ∩ H = {p_0}` exactly, so the support argument yields precisely one
attachment and cannot exclude `F5`. Moreover `H.R_pi = A.(2A+B).(2A+3B) = 8`
(recomputed), so all eight units of intersection concentrate at `p_0` — the
correct input for the queued local-different computation. Producer's
non-claim is exactly right.

### Item 5 — scope partition: CONFIRM_WITH_CORRECTIONS

The partition is exact as stated, with one addition needed for `(0.2)`.

* Finiteness near `H` excludes `(1,0)` components (item 2), so `F3,F6`
  cannot occur under the hypothesis and correctly remain a separate
  projective-basepoint branch, handled by neither `(0.1)` nor `(0.2)`.
* `F8`: recounted the maximal `K`: all pairwise products are 1 except
  `(0,1).(1,1)=1`, so tangencies are impossible and the only positive
  contribution is an ordinary triple point (`K_p=1`); the single point of
  `(1,1) ∩ (1,0)` can serve only one triple, so `K<=1<2`. `F9`: the
  branch-incidence graph is `K_{2,3}` with `b_1=2`, `K=0`. Both refinements
  empty while the factorization types exist — matches the promoted
  classification; such `H` are already killed by the forest theorem alone
  (boundary-subconfiguration monotonicity), independent of ramification.
* Correction (required for `(0.2)` to be exhaustive): `(0.2)`'s two branches
  presuppose `R_red != empty`, which the producer never states. It is
  provable in scope — Lemma N: if `pi` has a positive-dimensional fibre
  (allowed away from `H`), that fibre lies in the critical locus; otherwise
  `pi` is finite, and everywhere-étale would make `X` a disconnected
  degree-3 cover of simply connected `P2`, contradicting irreducibility.
  So `crit != empty`; since no component lies in `H`, `crit ∩ Y` is dense in
  it and `R_red != empty`. Add Lemma N to the packet.
* Nonreduced infinity, singular ambient closure, affine coefficient zeros,
  and both degree drops are correctly quarantined in §6.

### Item 6 — unit/localization successor: CONFIRM_WITH_CORRECTIONS

Confirmed part. With the actual dominant block **morphism** `A2 -> U`
(supplied by the promoted block-descent theorem: `g1` is an everywhere-étale
morphism with image inside the smooth locus minus the branch divisor;
"image in `U`" is a stated hypothesis of §1), every `u in O(U)^*` pulls back
to a unit of `C[x,y]`, hence a constant `c`, and `u-c` vanishes on a dense
subset of the integral `U`, so `O(U)^*=C^*`; `O(Y)^* subset O(U)^*` by
restriction. The exact sequence
`O(Y)^* -> O(U)^* -> Z^{components(R_red)} --div--> Cl(Y) -> Cl(U) -> 0`
then makes `(5.2)` injective. Complete hypothesis list: `Y` integral normal
noetherian (here `Y = X minus H` is smooth since `X` is smooth — no separate
normality assumption needed); `R_red` of pure codimension one (holds: Cartier
critical divisor, item 2); `O(U)^*=C^*` (holds as above). **Correction**:
§5 says "normal affine `Y`" — affineness is neither needed for the sequence
nor available: finiteness is assumed only near `H`, so `Y` may contain
complete vertical curves and need not be affine. Delete "affine".

Refuted part (as a reachable gate). The proposal "rank at most one would
force ramification irreducible" is vacuous because rank at most one never
occurs. For every smooth `X in |2A+3B|`: Künneth kills all cohomology of
`O(-2A-3B)`, so `chi(O_X)=1`, `q=p_g=0`; `K_X=(-A+B)|_X` gives `K^2=-1`;
Noether gives `e(X)=13`, so `b_2=rho=11` (recomputed; equivalently, the
conic-bundle discriminant has degree 9 and smoothness of the total space
forces nine distinct split fibres, `rho=2+9`). Hence
`rank Cl(Y) = 11 - rank<[H_i]> >= 11-3 = 8` for every in-scope survivor
(`8`, `9`, or `10` for 3, 2, 1 components). A rank-`<=1` computation would
eliminate everything and nothing: it cannot return, and an output of
`<=1` would certify an arithmetic error. What injectivity actually buys is
only `#components(R_red) <= rank Cl(Y) <= 10` — no elimination. The
successor must be replaced (see §3 below). The injectivity statement itself,
with the corrected hypotheses, is still worth promoting: it converts any
future *upper bound on the number of independent effective classes meeting
`H` only inside the classified attachment set* into a component bound.

## 2. Overall verdict and maximum safe theorem

**CONFIRM_WITH_CORRECTIONS.**

Safe to promote (conditional on the two promoted inputs and the block
promotion, scope exactly as sealed):

> **Theorem (corrected `(0.1)`/`(0.2)`).** Let `X` be a smooth irreducible
> quadratic Miranda incidence surface with `pi` finite near `H`, `H` reduced
> of bidegree `(2,3)`, and a dominant block morphism `A2 -> U = Y \ R_red`.
> Then `R_red != empty` (Lemma N); `crit(pi) ∩ H` equals exactly the set of
> projection-critical and singular points of `H` (Lemma S); each such point
> lies in `Rbar`. If `R_red` is irreducible then `H` has type `F5`, all
> eight units of `H.R_pi` concentrated at its triple point. Unconditionally,
> every survivor has `R_red` reducible or type `F5`; `F3,F6` violate
> finiteness; the forest refinements of `F8,F9` are empty. Moreover
> `O(Y)^*=O(U)^*=C^*` and `Z^{components(R_red)} -> Cl(Y)` is injective,
> with `rank Cl(Y) = 11 - rank<[H_i]> in {8,9,10}`.

Not safe: the §5 "rank at most one" elimination route (unreachable); any
`F5` occurrence/exclusion claim; anything in §6's non-claims.

## 3. Repairs and cheapest next control

1. Add Lemma N (`R_red != empty`) and Lemma S (exact attachment set) with
   the proofs above; reword §3's "smooth rational component" to "rational
   component's normalization"; delete "affine" in §5.
2. Replace the §5 successor. The class-group rank gate is dead. The cheapest
   controls, in order:
   * **`F5` local different at `p_0`** (queue item 2, unchanged): the fibre
     cubic acquires a triple root at `p_0` and the full `H.R_pi=8` sits
     there; a finite jet computation in one chart decides whether an
     irreducible `Rbar` can attach with a single branch compatible with the
     tree, or whether the different forces multiple branches (which would
     kill `F5` by the cycle lemma and, with `(0.2)`, force reducibility).
   * **Lattice splitting gate for irreducibility** (replacement for the
     rank gate): `[R_pi]=(2A+B)|_X` in `Pic(X)=Z^11` (classes `A,B` and the
     nine fibre-line classes). A reducible `R_red` needs an effective
     decomposition in which, by Lemma S, every non-vertical summand meets
     `H` only inside the finite classified attachment set with total
     `H`-degree 8. Enumerating these decompositions per type
     `F1,F2,F4,F7` is a finite integer computation and is the honest
     analogue of what §5 wanted; any type with no admissible reducible
     splitting is eliminated by `(0.2)`.
3. Keep `F3,F6` (basepoint blowup charts) and all nonreduced/degree-drop
   strata in their separate lifecycle entries.

No exit-price assertion is made; no `charge_basis` line is required.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15648`.
- Body SHA-256:
  `aa4877388dddadfbe2d4b167356c76f35424a440951ef0cc0cab6502c9dcf610`.
- Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.
