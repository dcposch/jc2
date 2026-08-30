# Hostile review: canonical normalization and generic degree three

Date: 2026-08-30
Reviewer: GPT-5.5 hostile reconstruction
Scope: charged files only inside the repository, plus narrow primary-source
checks for Chau/Orevkov context.  No charged inputs, Git state, ledgers,
sibling reports, receipts, or `jc2-lean` were inspected or modified.

## Hash custody

All charged repository hashes reproduced exactly:

```text
28f29711366f58f4a1c9e6e5d7f16d8e6ca29fddf730bfd436100da04e4d2eda  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md
3d0b72c7001bf403fa334f746dd09a21d8a55fc8074f9b4680e249b92f73beb3  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md.artifact.json
a75a91d65f2f95766581edb5b6dcf4a8e958844a0e66987ec7d94c898800cb98  ops/block_descent_all_degree_acyclic_companion_replay.py
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
c229cbc4eb93722eb9d5c247c5e0616901a0e5cfce0278613cffc7f9e4fcbe85  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md
b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-addendum-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
```

The artifact JSON for the all-degree report records the same full hash and body
hash as the charged markdown.  I make no exit-price assertion; receipt status
`ABSENT` is therefore expected.

## Verdict summary

1. `CONFIRMED`: canonical normalization of a hypothetical Keller pair.
2. `CONFIRMED`: the source chart avoids source ramification and supplies only a
   generic unramified sheet over each target branch component.
3. `CONFIRM_WITH_CORRECTIONS`: the ruling and morphic-forest mechanisms extend
   to `d1=1`, but not by literal import of every proper-block sentence.
4. `CONFIRMED`: in rank three, `R_red -> B` is finite point-bijective and
   analytically homeomorphic, and each `B` component is an entire component of
   the Keller nonproperness curve before polynomial parametrization is used.
5. `CONFIRMED`: the source-incidence forest transfer works at `d1=1`, including
   self-branch and parallel-edge accounting, without a scheme isomorphism
   `R_red = B`.
6. `CONFIRMED`: the Euler recomputation forces uniquely
   `C=A1`, `h=1`, `S0=empty`, `Q=0`.
7. `CONFIRMED`: the final cubic monodromy contradiction proves
   `[C(x,y):C(F,G)] != 3`, and only that generic field-degree statement.
8. `CONFIRM_WITH_CORRECTIONS`: the replay results are exactly as claimed, but
   almost all geometry is prose mathematics, not replay-certified.

No item is refuted.  The main correction is provenance/scope hygiene: prior
proper-block integrations are not themselves stated at full-normalization
`d1=1`, so the endpoint must consume their proofs after rechecking the actual
hypotheses, not merely their old theorem labels.

## 1. Canonical normalization

`CONFIRMED`.

Let `A=C[F,G]` and `L=C(x,y)`.  Since the Jacobian determinant is a nonzero
constant, `F,G` are algebraically independent and the morphism
`A2 -> A2` is etale, hence locally quasi-finite.  The function-field extension
`L/Frac(A)` is therefore finite and separable.

For `S`, the integral closure of `A` in `L`, finiteness is legitimate:
`A ~= C[u,v]` is excellent/Nagata and `L/Frac(A)` is finite.  If `s in S`, then
`s` is integral over `A` and hence over `C[x,y]`; because `C[x,y]` is integrally
closed in `L`, `s in C[x,y]`.  Thus the inclusion `S subset C[x,y]` is literal
and defines

```text
j: A2_source -> Y=Spec(S),       pi:Y->Spec(A)=A2,       F=pi o j.
```

`Y` is integral, normal, affine, and finite over `A2`.  Normal surface local
rings are Cohen-Macaulay, and finite miracle flatness over the regular
two-dimensional target gives finite flatness.  The generic rank is
`[L:Frac(A)]`.

The map `j` is affine-separated, finite type, and birational.  Its fibres lie in
fibres of the etale Keller map `F`, so they are finite; hence `j` is
quasi-finite.  Zariski Main for a separated quasi-finite birational morphism to
a normal target gives an open immersion.  The separatedness premise is automatic
from affineness but must be said.

Since `pi|j(A2)` identifies with the etale map `F`, the open chart avoids
`R=NonEt_Y(pi)`.  If `R` were empty and the degree were at least two, `Y->A2`
would be a connected finite etale cover of the complex affine plane, impossible.
Purity gives divisorial non-etaleness once nonempty.

## 2. Generic sheets and firewalls

`CONFIRMED`.

For an irreducible target branch component `D=V(p_D)`, the pullback
`p_D(F,G)` is a nonzero nonconstant polynomial because
`C[u,v]->C[x,y]` is injective.  It is therefore a nonunit with a nonempty zero
curve.  At least one component of that zero curve dominates `D`; otherwise the
preimage over the generic point of `D` would be empty, contradicting dominance
and generic finiteness.  Every such source point maps through `j(A2)`, which is
disjoint from `R`, so `pi` has an unramified point over a dense open of `D`.

Residue degrees are not discarded.  The generic point above `D` may have residue
degree `f>1`; geometrically this contributes `f` fixed sheets for inertia, not
necessarily one globally labeled original source sheet.  The argument is
strictly generic.  It does not give rank-one henselian factors at omitted
target values, conductor points, or singular branch points.  The all-degree
report correctly treats this as a generic-versus-pointwise firewall.

Normality is load-bearing in the nontrivial-inertia step.  At a height-one
branch point, the normal source has DVR local rings; in characteristic zero, an
`e=1` separable factor is unramified, so a component of the non-etale support
forces some `e>1` and a nonidentity generic meridian.  Without normality the
charged nonnormal controls show identity inertia can occur on conductor
support.

## 3. Ruling and forest at first-leg degree one

`CONFIRM_WITH_CORRECTIONS`.

The qualitative ruling proof does extend to the canonical endpoint, but the
strict proper-block theorem label cannot be imported verbatim.  The exact
sentences that still require a strict intermediate field are:

```text
xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md:29-31
"This theorem ... applies only inside the proper-intermediate-field horn."

xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md:178-180
"Assume a hypothetical noninvertible complex Keller map has a proper intermediate field..."

xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md:41-46
the promoted sandwich is stated for
C(f,g) proper-subfield K proper-subfield C(x,y), with d1>=2 and d2>=2.

xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md:10-24
the old cubic theorem is expressly the strict intermediate degree-three block.
```

After replacing those theorem labels by the canonical normalization established
in item 1, the proof mechanisms survive:

- Maximal-etale-open affineness uses the finite map from normal affine `Y` to
  regular `A2`; no `d1>1` input is needed.
- Smoothness follows because `pi|U` is etale over smooth `A2`.
- Rationality is stronger at `d1=1`: `C(U)=C(x,y)`.
- Units are constant because pullback along the dominant open immersion
  `j:A2->U` injects `O(U)^*` into `C[x,y]^*=C^*`.
- Log Kodaira monotonicity along the dominant generically finite morphism
  `A2->U` gives `bar-kappa(U)=-infinity`.
- Miyanishi-Sugie plus the standard global-fibration extension gives an
  `A1`-fibration `rho:U->C`, with `C=A1` or `P1`.
- The reduced fibres are disjoint unions of affine lines, and the Euler identity
  `e_c(U)=e_c(C)+sum_t(q_t-1)` gives `e_c(U)>=1`.

The morphic rational-forest input also survives because its promoted theorem
requires only an everywhere-defined dominant morphism `A2 -> U`, exactly what
`j` supplies.  It does not require surjectivity, etaleness, or `d1>=2`.

## 4. Rank-three fibre census and nonproperness

`CONFIRMED`.

For a finite flat degree-three map over an algebraically closed closed target
point, the fibre has total length three.  A local factor of length one is a
finite-flat rank-one local algebra over the regular local base, hence the base
itself, so it is etale.  Therefore every non-etale source point consumes length
at least two.  Two distinct non-etale source points over the same target value
would consume length at least four, impossible.  Thus each branch value has
exactly one reduced non-etale source point, and

```text
R_red -> B
```

is finite and bijective on closed points.  Analytification makes it a proper
continuous bijection to a Hausdorff analytic curve, hence a homeomorphism.  This
is not a scheme isomorphism; cusp/conductor scheme structure remains possible.

Each component of `B` is an entire component of the Keller nonproperness curve.
Indeed `R` is contained in `Y-j(A2)`.  A sequence in the dense open chart
approaching a point of `R` cannot remain in a compact subset of the source, and
its `F`-image converges.  Hence `pi(R)` lies in `A(F)`.  Because `pi` is finite,
images of irreducible components of `R` are curves; a curve contained in the
curve `A(F)` is an irreducible component, not a finite subset.

The primary Chau source check is consistent with the charged use:
arXiv:math/0305088 states that the nonproper value set of a nonsingular
polynomial map `C2 -> C2`, if nonempty, is a curve with one point at infinity,
and Theorem 1 parametrizes every irreducible component polynomially after the
standard coordinate setup.  Therefore the normalization of each component of
`B`, and of the corresponding component of `R_red`, is `A1`.

## 5. Source incidence forest at d1=1

`CONFIRMED`.

Apply the morphic forest theorem to the everywhere-defined dominant map
`j:A2->U`.  In a smooth strict-SNC completion of `U`, the boundary dual
multigraph is a forest.  Resolving the closure of `R_red` together with
infinity and surface singularities places the strict transforms of the affine
components and the exceptional chains inside that boundary.

The affine incidence multigraph of `R_red` is obtained from the boundary
forest by deleting irrelevant boundary vertices and contracting exceptional
trees.  This accounting retains:

- singular multibranch points as incidence vertices;
- self-branches as loops, which would force a cycle upstairs and are therefore
  excluded;
- parallel edges from two components meeting more than once, which would also
  force a cycle upstairs.

Thus the incidence multigraph is a forest.  If `c` is the number of normalized
`A1` components and `r_p` the number of normalization branches at each
multibranch affine point, then

```text
e_c(R_red) = c - sum_p (r_p-1) = b0(R_red).
```

The finite analytic homeomorphism `R_red -> B` transfers compactly supported
Euler characteristic and connected components, not scheme structure.  Hence

```text
e_c(B)=e_c(R_red)=b0(R_red)=b0(B)=h>=1.
```

## 6. Euler recomputation

`CONFIRMED`.

Let `S0=A2-pi(U)`.  Generic companions on each branch component make `S0`
finite: along each irreducible component of `B`, the unramified fibre-count
function is constructible, has positive generic value, and can drop only on a
finite exceptional subset.

The cubic fibre census is exactly:

```text
off B:    (1,1,1),  u(z)=3
B-S0:     (2,1),    u(z)=1
S0:       (3),      u(z)=0
```

Therefore

```text
e_c(U)
 = 3*e_c(A2-B) + e_c(B-S0)
 = 3*(1-e_c(B)) + (e_c(B)-|S0|)
 = 3 - 2h - |S0|.
```

The ruling gives `e_c(U)=e_c(C)+Q`, `Q=sum_t(q_t-1)>=0`.

If `C=P1`, then `3-2h-|S0|=2+Q`, i.e.
`2h+|S0|+Q=1`, impossible because `h>=1`.

If `C=A1`, then `3-2h-|S0|=1+Q`, i.e.
`2h+|S0|+Q=2`.  The unique solution is

```text
h=1,       S0=empty,       Q=0.
```

Thus `B` is connected.  With affine-line normalizations and forest incidence,
`B` is topologically contractible.  Since `S0` is empty, every branch point has
an unramified local length-one factor; finite-flat idempotent splitting over
the henselian local base gives a rank-one factor at every branch point.

## 7. Cubic monodromy contradiction

`CONFIRMED`.

At this point the all-degree acyclic companion obstruction applies directly:
`pi:Y->A2` is finite flat of degree three with integral normal source, `B` is a
nonempty reduced connected simply connected plane curve, and every branch point
has a rank-one henselian factor.

Reconstructing the monodromy proof gives the same contradiction.  Over
`M=A2-B`, the cover `Y-pi^{-1}(B) -> M` is finite etale of degree three and has
connected total space, so its monodromy is transitive.  At a general branch
point, normality gives nontrivial tame inertia; in degree three, a nonidentity
permutation with a fixed companion sheet is a transposition.

For the line/comb normal form of Arzhantsev-Zaidenberg, the relevant line or
spine meridian is central in the complement group.  The monodromy image
therefore lies in the centralizer of a transposition, preserving its fixed
sheet, hence is intransitive.

For the weighted-cone normal form, the rank-one factor at the origin gives an
analytic local fixed sheet.  Choosing a weighted sublevel inside the ordinary
analytic splitting ball and using positive weighted radial flow identifies the
origin-local complement group with the global complement group.  The global
image lies in a point stabilizer, again intransitive.

The Arzhantsev-Zaidenberg theorem covers every reduced connected simply
connected plane curve: the charged PDF defines acyclic as connected and simply
connected and Theorem 1.3(b) lists exactly the two normal-form families; its
Corollary 1.2 gives the disconnected parallel-line control.  Thus transitivity
and the acyclic companion obstruction are incompatible.

Conclusion:

```text
[C(x,y):C(F,G)] != 3
```

for any complex plane Keller pair.  This is a statement about generic
function-field degree/geometric degree.  It is not a statement about total
polynomial degree, not a statement about the degree of either coordinate, and
not a proof of JC2.

## 8. Replay and primary-source check

`CONFIRM_WITH_CORRECTIONS`.

Replay results:

```text
python3 ops/block_descent_all_degree_acyclic_companion_replay.py
python3 -O ops/block_descent_all_degree_acyclic_companion_replay.py
python3 -OO ops/block_descent_all_degree_acyclic_companion_replay.py
```

All three runs had byte-identical stdout with stdout SHA-256

```text
71499353da07d047ec0d222454649779769e331db013845a5af3370fe7ebd35b
```

and embedded payload SHA-256

```text
3586519ac48ca485bf4c91e8d32a5a89b3ebf3f77329b2e925abefd2e805f492.
```

The deliberate mutation

```text
python3 ops/block_descent_all_degree_acyclic_companion_replay.py --mutate-drop-centrality
```

failed with exit code `1` and the expected error:

```text
RuntimeError: an allowed comb image moved a spine-fixed sheet out of the fixed set
```

Replay-certified claims are only the finite permutation checks encoded in the
script: centralizer preservation of fixed sets for canonical cycle types in
degrees two through eight, cyclic intransitivity, point-stabilizer
intransitivity, and the missing-companion/disconnected/nonnormal controls.

Prose mathematics, not replay-certified:

- canonical normalization, finite flatness, and Zariski Main;
- acyclic curve classification and complement presentations;
- normal generic inertia and henselian-to-analytic splitting;
- generic companion existence and `S0` finiteness;
- maximal-etale-open affineness;
- Miyanishi-Sugie/global `A1`-fibration input;
- morphic forest transfer and incidence graph Euler identity;
- Chau/Jelonek nonproperness component parametrization;
- the rank-three fibre census outside finite permutation arithmetic;
- the final global transitivity contradiction as algebraic geometry.

The narrow primary-source search found no explicit degree-three Keller control
contrary to the endpoint.  It found the classical matching theorem: S. Yu.
Orevkov, "On three-sheeted polynomial mappings of C^2", Izvestiya Mathematics
29 (1987), 587-596; the MathDoc/MathNet record states that the Jacobian of a
three-sheeted polynomial mapping `C2 -> C2` cannot be constant.  The direct
download of the PostScript copy timed out, so I do not use Orevkov's proof as a
dependency here.  It is external corroboration, not replay certification and
not a replacement for the canonical-normalization argument above.

## Maximum-safe endpoint

`CONFIRMED` maximum-safe theorem:

> Let `F=(F,G):A2_C -> A2_C` be a complex polynomial Keller map.  Then the
> generic function-field degree satisfies
> `[C(x,y):C(F,G)] != 3`.

The stronger all-degree statement safely available from the charged argument is
conditional:

> For the full canonical normalization of a hypothetical noninvertible Keller
> map of any generic degree `d>=2`, the reduced branch support cannot have all
> connected components simply connected.  Equivalently, at least one connected
> component of that branch support has nontrivial fundamental group.

I do not promote any claim about polynomial coordinate degree, total degree,
existence of strict blocks, higher generic degrees, primitive monodromy, or JC2.

## Cheapest useful successor

The cheapest useful successor is now `BD-CANONICAL-BRANCH-PI1`: attack the
remaining canonical branch condition directly.  A hypothetical counterexample
of any degree must have a full-normalization branch component with nontrivial
`pi1`; combine the canonical open immersion `A2->U`, the constant-unit
`A1`-ruling, and nonproperness-component one-place constraints to restrict or
exclude non-acyclic branch components.  This avoids strict-block assumptions and
does not spend effort reproving the already classical three-sheeted endpoint.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18557`.
- Body SHA-256:
  `93a88664971b36c08a699286a8c1db9adda091681724a71d2e8c7c3b1a6aa094`.
- Frozen basis: `d08e8e5f50161d753f3fb86a6d4854afbc7e0390`.
