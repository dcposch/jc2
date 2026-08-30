# Hostile rereview: D3 one-point Halphen weighted-boundary obstruction

Date: 2026-08-30 UTC
Reviewer: Fable 5, independent hostile mathematical reviewer
Frozen basis charged to this review: `5d0f411f6ce1995b3a56abe8ea2ec4f2e0105d86`
Lane note: this is a fresh review; the prior lane failed operationally with no
report and contributes no mathematical verdict here.

## 0. Custody

All eight charged SHA-256 pins were verified before reading and all matched.
In addition, the body seals of the five charged markdown documents were
recomputed (bytes through the standalone `<!-- BODY-END -->` line inclusive)
and each matched its declared body length and body SHA-256, including the two
artifact manifests' `body_bytes`/`body_sha256` fields:

```text
obstruction  11732 / 2fc2cd21...40bee   corrigendum   3242 / aa6558...1092
local gates  10400 / 96f168...27a9     forest corr.   7280 / c07e64...0a98
block descent 8285 / 85db7a...e6e9f
```

The corrigendum is treated throughout as the binding producer wording.

## 1. Scope and imported interfaces

The packet proves a conditional emptiness: assuming (i) the promoted D3
one-point index-three Halphen row (exact plane CFS level two, minimal
strictly-Henselian-insoluble floor level one, nonsingular generic fibre,
normal total germ), (ii) the promoted local gates (triple-line first jet on
the `G=y^3` branch and the CFS state machine with its critical flags),
(iii) literal raw coefficient-base degree at most three in `t`,
(iv) occurrence as the actual morphic proper block, with the marked germ the
actual normal incidence, locally finite at the marked point, under the
promoted block-structure theorem, and (v) the promoted morphic
rational-forest theorem, the `m=3, T=2t0` critical shard has no actual
occurrence.

Premises (i), (ii), (iv), (v) are imported promoted interfaces, all of which
are among the charged files or hash-cited by them; I audited their *use*
here, not their internal proofs, per the review charge. Their exact roles:
the row and gates supply the constructible coefficient locus, including
`s!=0` and the final flags `kappa=0, eta!=0`; the block-structure theorem
supplies `g1` everywhere-defined étale with `g1(A^2) ⊆ Y_sm ∖ R` and `g2`
finite flat; the forest theorem supplies `tau(D)=0` for every strict-SNC
completion of any surface admitting an everywhere-defined dominant morphism
from `A^2`. The hash of the charged local-gates integration matches the
dependency pin inside the obstruction note, and the forest-correction
integration internally pins the producer hash `d49a44ce...` cited by the
note. Consistent.

## 2. Itemized hostile checks

### 2.1 Weighted-order census, translations, `eta!=0` — CONFIRMED

I re-derived the census fully by hand and by an independent SymPy
implementation using a different mechanism from the producer replay (grading
by torus substitution `(X,Y,t) -> (w^5X, w^4Y, w^3t)` and series collection
in `w`; the `(a,R3)` system solved as an explicit linear system with
determinant `2s^3`, unique on the imported `s!=0`).

Monomial census: `5a+4b+3c=15` has exactly four solutions,
`X^3, tY^3, t^2XY, t^5`, so (1.1) is literally the complete lowest face,
with the `X^3` and `tY^3` coefficients exactly `1` (from the normalized
`x^3` and the `y^3` term of `F1`), not merely nonzero.

Sub-face vanishing: I enumerated every monomial of weight `<= 14`
(`t..t^4`, `Yt..Yt^3`, `Y^2t, Y^2t^2`, `Xt..Xt^3`, `XYt`, `X^2t`, and all
`t^0` monomials) and verified each vanishes under exactly the stated
relations. Two structural facts sharpen Section 1 of the note and were
verified symbolically: with only the first-cube relations
(`q1=q2=C2=U2=0, R2=3s^2, C3=s^3`) and the `U3` relation imposed, and `a,
R3` left free, the only surviving sub-15 weights are 12 and 14, and

```text
weight-12 part = (d - lambda^3) * t^4,      weight-14 part = kappa * X t^3,
```

with `d=-s^3a+s^2V2-sR3`. So the two final CFS conditions `27d=b^3` and
`kappa=0` are precisely the two lowest-graded obstructions, and weight 13
vanishes identically already. The coefficients of the face were confirmed:
`alpha = M111 - 2s*ell - 2*lambda*q0` (the replay's expanded form
`(3M2-2Q2q0-6ells+2q0^2s)/3` is the same expression with `lambda=b/3`
substituted), and the `t^5` coefficient equals the CFS flag `eta` of the
gates file verbatim, with no dependence on the eliminated `a, R3, U3`, so
there is no circularity.

Gauge audit: the shift `X=x+st, Y=y+lambda*t` is a parameter-dependent
*ambient linear coordinate change* at the marked point, which is a legal
germ isomorphism; no coefficient rescaling is used, no normalization of
`alpha` or `eta` is performed, and the theorem is stated for every `alpha`
and every `eta!=0`. The residual coefficient torus (after fixing the two
unit face coefficients) acts by `(alpha, eta) -> (theta*alpha,
theta^3*eta)`, under which both `eta!=0` and the dichotomy locus
`alpha^3+27eta=0` are invariant, so the stated parameterization is
gauge-safe even though one modulus (`alpha^3/eta`) would suffice.

`eta!=0` is not proved here; it is the final CFS exactness flag imported
from the promoted gates (last central form `z^2(kappa*X + eta*z)` with
`kappa=0, eta!=0`), and its two uses are identified below (2.2, 2.3).
Load-bearing degree bound: a `t^4` base coefficient would contribute a
weight-12 constant-in-`(X,Y)` term and destroy the census; the note
correctly flags literal base degree three as essential.

### 2.2 Curve dichotomy, irreducibility, quotient point, invariant — CONFIRMED

Independently re-derived, three ways where possible.

Quasi-smoothness. On the cone, `F=F_X=F_Y=F_t=0` with `t=0` forces the
origin; with `t=1`, the branch `X=Y=0` is killed by `F_t=5eta!=0`, and the
branch `XY=alpha^2/9` gives `X^3=Y^3=-alpha^3/27` and
`F_t=5(alpha^3+27eta)/27`. So the curve is quasi-smooth exactly off
`delta=alpha^3+27eta=0`. By elimination (not candidate substitution): on
`f_X=0` one has `Y=-3X^2/alpha`, and then `f_Y` factors as
`X(3X+alpha)(9X^2-3alpha X+alpha^2)/alpha^2`, whose nonzero roots are
exactly `27X^3=-alpha^3`; the `alpha=0` branch has only the origin,
excluded by `eta!=0`. This closes exhaustiveness of the note's enumeration.

One completion the note omits: Section 2.1's smoothness argument is carried
out in the affine chart. The three points of `E` at `w=0` (solving
`u^3+v^3=0`) must be checked; there `F_u=3u^2!=0` since `u!=0`, so `E` is
always smooth at infinity, on both strata. Trivial, but the written
derivation is complete only with this line; filed as a minor correction.

Hesse identification. The `t!=0` chart of `P(5,4,3)` is `C^2/mu_3` with the
residual action `(u,v)->(zeta^2u, zeta v)`; the index-cover closure is the
projective cubic (2.2), and I verified the compactification claim
rigorously: `C ∖ {[0:1:0]}` equals the free `mu_3` quotient of the affine
cubic; both `C` and `E/mu_3` are one-point completions smooth at the added
point, the affine curve has exactly one place at infinity downstairs (the
three cover places form one orbit), hence the completions are canonically
isomorphic. The fixed-point ledger `(1,1,eta)` at the three coordinate
vertices was checked; `eta!=0` is exactly what keeps the third vertex off
`E`, so the action on `E` is free — the first of the two uses of `eta!=0`
(the second: `C` misses the `mu_3` vertex of `P(5,4,3)`).

Smooth stratum. `E` smooth elliptic; a free degree-3 quotient has
`chi=0/3=0`, genus one. Genus cross-checks: the Hilbert-series formula in
the note evaluates to `2p_a = 15/4 - 3 + 9/4 - 1 = 2` (I also validated the
formula itself on `P^2` cubics/quartics, `P(1,1,2)` degree 4, and
`P(1,2,3)` degree 6); orbifold adjunction gives `deg K = 15*3/60 = 3/4 =
(2g-2) + (1-1/4)` with the single index-4 orbifold point, forcing `g=1`.
No hidden orbifold correction: the node (when present) lies at
`X^3=-alpha^3/27 != 0`, `t=1`, a free-orbit smooth point of the ambient,
away from all three vertices.

Equality stratum. With `c=-alpha/3`, `c^3=eta`, the factorization (2.4) was
verified modulo `omega^2+omega+1`, as was `sigma(L_k)=omega^2 L_{k-1}`, so
`sigma` maps the line `{L_{k-1}=0}` onto `{L_k=0}`: a free 3-cycle on lines.
The three vertices were computed explicitly and shown to form a single free
orbit `V01 -> V12 -> V02 -> V01`; the concurrency determinant is
`-3c(2omega+1) != 0`, so the triangle is honest (three distinct
non-concurrent lines, three ordinary nodes). Quotient: one `P^1` with its
two vertex points identified — irreducible rational, exactly one node. Node
type: the Hessian determinant `36XY-alpha^2` restricts to `3alpha^2 != 0`
on the singular locus, so the singularity is an ordinary node upstairs, and
the quotient is étale there, so an ordinary node downstairs; a cusp is
impossible. Reducibility of the coarse curve is impossible on either
stratum: for `delta!=0` smoothness plus Bézout, and in general `F` is monic
of degree 3 in `X` with no weight-5 monomial in `(Y,t)` available, so a
factorization would force `X | F`, contradicting `eta!=0`; on `delta=0` the
transitive line permutation gives one component. Quotient point: on the
`Y=1` index-4 cover the curve equation is `u^3+v+alpha v^2u+eta v^5` with
`t`-derivative 1 at the origin — smooth on the cover, smooth coarse image.

Hence the boundary invariant is `tau=1` on both strata: genus one
contribution when `delta!=0`; `b1=1` from the cycle when `delta=0`.
Confirmed exactly as claimed.

### 2.3 Normality of the strict transform, `uv+r^n` persistence — CONFIRMED

The corrigendum's item 3 (the strict transform itself is normal; nothing is
normalized) is correct and load-bearing. S2: in each chart the strict
transform is a `mu_{5},mu_4,mu_3` quotient of a hypersurface (the cover
equation `F-tilde` is not divisible by the exceptional coordinate since its
restriction is `P15 != 0`), and in characteristic zero the invariant ring is
a direct summand, hence CM, hence S2. R1: I verified the stronger pointwise
statement that the strict transform is smooth (on the relevant index cover)
at *every* point where `C` is smooth, because `d(F-tilde)` restricted to the
exceptional plane is `dP15`, nonzero wherever the reduced irreducible curve
`C` is smooth. So `Sing(S') ⊆ {node} ∪ {mu_4 point}`, and R1 holds; Serre
gives normality for every value of the higher-weight terms.

Node persistence. At the node (a free orbit, so the analysis lifts to a
smooth ambient chart), the transverse Hessian is nondegenerate
(`3alpha^2`), so parametric Morse reduction gives `uv+phi(r)=0` with
`r` the exceptional parameter. `phi=0` would make the germ two crossing
planes, singular along a curve, contradicting R1-normality just
established; so `phi = unit * r^n`, and the unit is absorbed by rescaling
one Morse coordinate. Resolution: for `n=1` the surface is already smooth
and the irreducible curve `C` has an honest node — one blowup makes the
strict transform meet the exceptional `P^1` twice, two parallel edges,
retained in the multigraph, `b1=1`; for `n>=2` the `A_{n-1}` chain joins
the two branches of the *same* irreducible component, giving a genuine
cycle through one vertex. Irreducibility of `C` (2.2) is exactly what makes
the two branches attach to a single vertex; verified, not assumed. The
`mu_4` point resolves to a Hirzebruch–Jung chain (a rational tree), and the
strict transform of the smooth irreducible branch meets the fibre in one
point in a good resolution, so no cycle is created or destroyed there.
The corrigendum's deletion of the "connectedness alone" sentence (item 5)
is correct: the explicit chain argument is the proof.

Resolution-independence: the constructed good resolution has
`sum g + b1 = 1`; this quantity is preserved by the point blowups
connecting any two good resolutions (blowups subdivide edges or add
rational leaves; genus components persist under strict transform and cannot
be contracted in the factorization), so *every* good resolution of the germ
carries the `tau=1` subconfiguration. The note's persistence sentences are
adequate for this.

### 2.4 Weierstrass/integral-closure bridge — CONFIRMED under corrigendum scope

The displayed identity (4.1) was verified exactly: under the relations,
`F(t;0,0,1)=s^3t^3` (the `x^3` value vanishes, `F1(0,0,1)=0` on the
`H=y^3` branch, `F2(0,0,1)=C2=0`, `F3(0,0,1)=C3=s^3`). Since the fibre
value has `t`-order exactly 3 with unit top coefficient near the marked
point, Weierstrass preparation makes the incidence germ finite flat of
degree 3 over the affine target germ. This is *local* finiteness only; the
corrigendum's item 2 correctly retracts any global projective finiteness
reading, and the finite-flat global statement about `g2` is imported
separately from the block-structure theorem. The identification of this
local finite normal algebra with the actual block germ is precisely the
charged occurrence premise ("actual normal incidence"), imported, not
proved — its exact role is to convert the coefficient locus into the germ
of `Y` at a genuine block point. Finite incidence is nowhere conflated with
occurrence: the verdict is conditional on occurrence throughout (Sections
0, 5, 7 and corrigendum Section 2). The target-infinity alternative is
handled a fortiori and is sound: everything over a point of fixed target
infinity lies in the boundary of any completion of `V`.

### 2.5 Forest theorem applied morphically — CONFIRMED

The application is to the everywhere-defined morphism `g1: A^2 -> V` with
`V=g1(A^2)` *exactly* the image: open and smooth by the block-structure
theorem (étale `g1`, image inside `Y_sm ∖ R`), surjective by definition, so
the promoted morphic theorem applies with no shrinking and no rational
domination. The marked point is singular on `Y`: every monomial of weight
`>=15` in weights `(5,4,3)` has ordinary degree `>=3`, so the germ has
multiplicity at least 3; hence `p ∉ V`, and the entire extracted
configuration over `p` lies in the resolved boundary of every strict-SNC
completion built over a good resolution. `tau(D) >= 1` on a subconfiguration
contradicts `tau(D)=0`. The note explicitly refuses the rational-domination
substitute, consistent with the forest-correction counterexample
`(P^2, E)`. The corrigendum's item 1 (other Du Val points permitted,
neither used nor excluded) only adds rational trees elsewhere in the
boundary and cannot interfere. No leak found.

### 2.6 Executable replay — CONFIRMED

Environment: `uv 0.6.9`, `uv run --with sympy==1.14.0`, CPython 3.11.11,
darwin/arm64. Results:

- Ordinary, `-O`, `-OO`: all exit 0, outputs byte-identical, 599 bytes,
  SHA-256 `a5d5ec6b3abcca9d83edf45f04ff5ca81376f257d4ae0970004f5155041a150c`
  — exactly as claimed.
- `--mutate-t5-sign`: exit 1, stderr `FAIL:weighted face identity failed`,
  empty stdout — as claimed.
- Unknown argument: exit 1, `FAIL:unknown command-line argument` — argument
  parsing fails closed.
- AST `assert` count independently recomputed: 0; guards use `require`/
  RuntimeError and survive `-OO` by construction.

Replay scope, verified against the code: it derives the face, gap, genus
arithmetic, singular-candidate discriminant, triangle factorization, line
cycle, vertex ledger, and `Y=1` chart regularity. It does **not** prove:
exhaustiveness of the singular-point enumeration (it checks the candidate
family only; my elimination closes this), the compactification
identification `C ≅ E/mu_3`, normality of the strict transform, the
`uv+r^n` reduction, resolution invariance of `tau`, the Weierstrass bridge,
or either promoted interface theorem. The note's Section 6 says this
honestly. Cosmetic: the JSON `analytic_shift` strings mention `z` although
the script works in the `z=1` chart.

### 2.7 Price — CONFIRMED

The packet prices itself correctly: conditional closure of exactly one row
(`m=3, T=2t0`, both intrinsic shards, both Hesse strata) in the
actual-morphic occurrence scope; explicitly not an abstract class-`(3,3)`
surface nonexistence, not row attainment (the positive control
`(alpha,eta)=(0,1)` — which I verified satisfies every gate relation,
including `d=lambda^3` and `kappa=0`, with a smooth elliptic exceptional
curve — shows the locus is nonempty and the elimination is genuinely
map-side), not a Keller map, not a counterexample, not JC2. The other three
Hodge rows, other block degrees, and block non-occurrence remain open. No
new exit price is asserted and none is consumed incorrectly;
`charge_basis` is correctly absent, and remains absent here.

## 3. Itemized verdicts

1. Weighted census, translations, `eta!=0` provenance — **CONFIRMED**
   (with the sharpened graded decomposition: sub-15 residue is exactly
   `(d-lambda^3)t^4 + kappa Xt^3`).
2. Smooth/nodal dichotomy, irreducibility, quotient point, `tau=1` —
   **CONFIRM_WITH_CORRECTIONS** (add the one-line `w=0` smoothness check;
   everything else verified independently, including ordinary-node type and
   the free vertex 3-cycle).
3. Normality of strict transform, `uv+r^n`, parallel edges —
   **CONFIRMED** (corrigendum items 3 and 5 adopted; `phi=0` excluded by
   the proved normality, unit legally absorbed).
4. Weierstrass/integral-closure bridge — **CONFIRMED** in the corrigendum's
   local-finiteness scope; occurrence identification correctly flagged as
   imported premise.
5. Morphic forest application — **CONFIRMED** (no shrinking, no rational
   domination, singular center of multiplicity `>=3` missed by `g1`).
6. Replay — **CONFIRMED** (hash, byte count, three modes, mutation,
   fail-closed arguments, zero asserts all reproduced; non-software steps
   correctly declared).
7. Pricing — **CONFIRMED**.

## 4. Overall verdict

**CONFIRM_WITH_CORRECTIONS.**

Corrections, all minor and none affecting the verdict: (a) the binding
corrigendum's five wording repairs are each necessary and correct, and are
adopted; (b) Section 2.1's smoothness derivation must note the `w=0` points
(`F_u=3u^2!=0` there); (c) the replay's singular-locus check is
candidate-based and should not be cited as proving exhaustiveness of the
enumeration (the prose derivation plus the elimination above does); (d)
cosmetic `z` in the replay's `analytic_shift` metadata.

## 5. Maximum-safe theorem

Assume: the promoted D3 one-point index-three Halphen row (exact plane CFS
level two, minimal strictly-Henselian-insoluble floor level one,
nonsingular generic fibre, normal germ) with literal raw coefficient-base
degree at most three; the promoted local gates (triple-root branch with
`q1=q2=C2=U2=0`, `R2=3s^2`, `C3=s^3`, `3c=b^2`, `27d=b^3`, `kappa=0`,
`eta!=0`, `s!=0`); the promoted block-structure theorem; the promoted
morphic rational-forest theorem; and occurrence of this row as the actual
proper intermediate block with the marked germ the actual normal incidence,
locally finite at the marked point (or marked center on fixed target
infinity). Then for every surviving coefficient value — every `alpha`,
every `eta!=0`, every choice of the remaining free and higher-weight
coefficients — the marked germ has weighted order exactly 15 for weights
`(5,4,3)` with complete lowest face
`X^3+tY^3+alpha t^2XY+eta t^5`; the weighted blowup extracts the degree-15
curve `C_(alpha,eta) ⊂ P(5,4,3)`, which is smooth of genus one iff
`alpha^3+27eta!=0` and an irreducible one-node rational curve otherwise;
every good resolution of the germ carries a complete exceptional boundary
subconfiguration with `sum(genera)+b1=1`, lying in the resolved boundary of
`V=g1(A^2)`; and this contradicts `tau(D)=0` from the morphic
rational-forest theorem. Hence the `m=3, T=2t0` one-point Halphen row has
no actual morphic proper-block occurrence. Nothing herein constrains
abstract class-`(3,3)` surfaces under mere rational domination, the other
three Hodge rows, other block degrees, existence of blocks or intermediate
fields, any Keller map, or JC2.

## 6. Cheapest useful successor

Coordinator integration promoting this conditional row-closure with the
corrigendum wording (no new mathematics), then redirect the identical
weighted-boundary pipeline — census, Hesse quotient, `tau` ledger, forest
interface, all reusable verbatim — at the next surviving one-point Hodge
row of the promoted four-row input, for which the row-specific CFS state
machine is the only missing producer input. The previously suggested
global-control ramification audit is now unnecessary for this row: the
sharp control `(alpha,eta)=(0,1)` is already priced as failing the
map-side interface at the cheapest local place.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20554`.
- Body SHA-256:
  `ae5c2545da7c5422ad611a9d91dbd6bce7ea276102bf3d943b1c09197536ee80`.
- Frozen basis: `c005516819d1cb327659f550d694807c66c347f8`.
