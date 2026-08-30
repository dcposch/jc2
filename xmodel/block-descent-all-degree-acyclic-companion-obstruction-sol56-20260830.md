# All-degree acyclic-branch companion obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`cubic_affine_survivor` lane)  
Frozen basis: `fdfbf4bea317622fa80e7da7404ef9dc0e88026c`  
Lifecycle: **FINAL + VERIFIED / EXACT STANDALONE THEOREM**

## 0. Verdict

The cubic acyclic-branch obstruction is not special to `S3`.

**Theorem (all-degree acyclic companion obstruction).**  Let

```text
pi:X -> A2_C
```

be finite flat of degree `d>=2`, with `X` integral and normal.  Let `B` be
the nonempty reduced support of the non-etale locus of `pi`.  Suppose:

1. `B(C)` is connected and topologically simply connected; and
2. for every `b in B(C)`, the finite algebra over the henselian local base
   has a direct factor which is locally free of rank one:

```text
(pi_* O_X)_b tensor_(O_{A2,b}) O^h_{A2,b}
    = A_b x C_b,                     rank_(O^h_{A2,b})(A_b)=1.
```

Then no such cover exists.  Equivalently, the etale cover over `A2-B`
cannot be connected; integrality says that it is connected, giving the
contradiction.

There is a second, Euler-enhanced version which will be important below.
Let `R=NonEt_X(pi)` and `U=X-R`.  It is enough to assume only that every
irreducible component of `B` has a generically unramified sheet, provided

```text
e_c(U)>0.                                                     (0.1)
```

Under these weaker companion hypotheses, the same nonexistence conclusion
holds.  It also holds when `B` is disconnected but every connected component
is simply connected.  This version applies to the canonical normalization of
a hypothetical Keller map: the source is a ramification-avoiding open chart,
it supplies a generic unramified sheet over every branch component, and the
campaign's qualitative ruling argument extends verbatim to normalization
degree `d1=1`, giving `e_c(U)>=1`.

As a concrete endpoint, the canonical-normalization version combines with
the rank-three source-forest ledger to prove:

> There is no complex plane Keller map of generic field degree
> `[C(x,y):C(F,G)]=3`.

That corollary is proved in Sections 7--8.  It is stronger than the prior
strict-intermediate cubic-block exclusion: the middle normal surface here is
the normalization in the **full** source function field and the first leg
has degree one.

The theorem permits arbitrary degree, arbitrary ramification partitions on
the non-companion factors, and any positive number of rank-one factors.  It
does **not** apply if even one required branch point lacks a rank-one factor.
In campaign language, the `S0=empty` / every-point companion hypothesis is
an exact firewall, not a generic-fibre substitute.  No assertion is made
for a conductor or branch point without a length-one factor.

## 1. Charged classification and local facts

The classification source is

```text
Ivan Arzhantsev and Mikhail Zaidenberg,
"Acyclic curves and group actions on affine toric surfaces",
arXiv:1110.3028v2, Theorem 1.3(b).

41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
```

The paper defines `acyclic` as connected and simply connected.  Its theorem
applies to every **reduced** simply connected plane curve, including
reducible curves.  Up to a polynomial automorphism of `A2`, it gives

```text
(I)   y^epsilon_y p(x)=0;

(II)  x^epsilon_x y^epsilon_y
      product_(i=1)^r (y^a-kappa_i x^b)=0,
```

where the epsilons are zero or one, `p` has simple roots, `a,b>=1` are
coprime, `r>0`, and the nonzero `kappa_i` are distinct.  Polynomial base
automorphisms preserve every hypothesis of the theorem.

Three standard local facts will be used explicitly.

First, a unital finite-flat rank-one algebra over a local ring is the base
ring.  Indeed, its unit is nonzero modulo the maximal ideal and hence is a
basis by Nakayama.  Thus the displayed henselian factor is a genuine local
section.  On a sufficiently small analytic punctured neighborhood, the
local monodromy group fixes the corresponding sheet.  Several rank-one
factors give several individually fixed sheets.

Second, put

```text
M=A2-B,                 E=X-pi^(-1)(B).
```

Then `E->M` is finite etale of degree `d`.  The nonempty open `E` in the
integral variety `X` is integral and connected.  Hence its monodromy

```text
rho:pi1(M,m0) -> S_d
```

is transitive.

Third, a generic meridian of every irreducible component of `B` has
nonidentity image.  Here normality is doing real work.  At the generic point
of a branch component the regular base has a DVR.  The local rings of the
normalization above it are DVRs.  In residue characteristic zero, a finite
extension with ramification index one and separable residue extension is
unramified.  Since the component lies in the non-etale support, some
ramification index is greater than one.  Tame local monodromy around a
general transverse disk is therefore nontrivial.  At such a general closed
point the rank-one hypothesis also gives that meridian at least one fixed
sheet.

Consequently, for every branch component its generic inertia permutation
`sigma` satisfies

```text
sigma != 1,             empty != Fix(sigma) != {1,...,d}.       (1.1)
```

No common companion label between different local neighborhoods is asserted
or needed.

## 2. The permutation lemma

For any permutation `sigma`, every element of its centralizer preserves
`Fix(sigma)` setwise.  Indeed, if `sigma(v)=v` and `g sigma=sigma g`, then

```text
sigma(gv)=g sigma(v)=gv.
```

Thus, when (1.1) holds, every subgroup of `C_{S_d}(sigma)` is intransitive.
This is independent of the remaining cycle lengths.  It covers partitions

```text
(e_1,...,e_k,1,...,1)
```

with arbitrary `e_i`, any number of fixed sheets, and every `d>=2`.  For
`d=2` there is no nonidentity permutation with a fixed point, so (1.1) is
already locally impossible.

## 3. Normal form (I): line degenerations and all combs

Consider

```text
B={y^epsilon_y p(x)=0}.
```

If `epsilon_y=0`, connectedness forces `p` to have exactly one root (the
nonempty case), so `B` is a vertical coordinate line.  If `epsilon_y=1`
and `p` is a nonzero constant, `B` is the horizontal coordinate line.  In
either line degeneration, `pi1(A2-B)=Z`, generated by the branch meridian
`h`.  By (1.1), `rho(h)` is nonidentity and has a nonempty proper fixed set.
The cyclic monodromy image preserves that set and is not transitive.

The remaining connected case is the comb

```text
B={y p(x)=0},
p(x)=product_(i=1)^s (x-alpha_i),        s>=1,
```

with distinct `alpha_i`.  Its complement is literally

```text
M=(C-{alpha_1,...,alpha_s}) x C*,
pi1(M)=F_s x <h>,                                           (3.1)
```

where `h` is a generic meridian of the horizontal spine `y=0`.  In
particular, `h` is central.  Choose a general spine point away from all
teeth.  By (1.1),

```text
sigma=rho(h) != 1,       empty != Fix(sigma) != {1,...,d}.
```

For every `gamma in pi1(M)`, equation (3.1) gives

```text
rho(gamma) sigma = sigma rho(gamma).
```

The permutation lemma makes `Fix(sigma)` a nonempty proper invariant subset
of the sheets.  The whole monodromy group is intransitive.  Notice what has
not occurred: companion sheets at teeth were never identified with the
companion at the spine, and no local label was propagated through the
incidence graph.

This also handles one tooth, arbitrarily many teeth, arbitrary generic
ramification partitions, and multiple generic companions.  The cases with
no horizontal spine were the coordinate-line degenerations above.

## 4. Normal form (II): the origin-local group is global

Now let

```text
B={x^epsilon_x y^epsilon_y
   product_(i=1)^r (y^a-kappa_i x^b)=0}.
```

All components pass through the origin.  Positive weighted scaling

```text
t.(x,y)=(t^a x,t^b y),              t>0,
```

preserves `B`.  Define

```text
N(x,y)=|x|^(2/a)+|y|^(2/b).
```

Then `N(t.(x,y))=t^2 N(x,y)`, and each weighted ray outside the origin
meets `N=1` exactly once.  If `L={N=1}-B`, there are explicit product
decompositions

```text
A2-B                         = (0,infinity) x L,
{0<N<delta}-B                = (0,sqrt(delta)) x L.
```

Therefore inclusion of an arbitrarily small origin complement into the
global complement is a homotopy equivalence and induces an isomorphism on
fundamental groups.

The rank-one henselian factor at the origin supplies a locally fixed sheet.
Because the origin-local group is the entire global group, the global image
lies in a point stabilizer in `S_d`.  It is intransitive.  This proof includes
one-component cones, smooth weighted degenerations, coordinate-axis factors,
and any number of rank-one factors.  It does not need a generic inertia
partition.

Sections 3 and 4 exhaust the Arzhantsev--Zaidenberg list.  In every row the
monodromy is intransitive, contradicting Section 1.  This proves the theorem.

## 5. Hostile controls and exact firewalls

### 5.1 One missing companion point defeats the theorem

The finite-flat cubic

```text
X={z^3-3xz+2y=0} -> A2_(x,y)
```

is the sharp control.  Eliminating `y` identifies `X` with `A2_(x,z)`, so
the source is integral and smooth.  The polynomial is monic in `z`, hence
the map is finite flat of degree three, and its reduced branch is the cusp

```text
B={y^2=x^3}.
```

This curve is connected, contractible, and of weighted-cone type.  Every
smooth branch point has fibre partition `(2,1)`, but the origin has the
single factor `z^3`, with no rank-one companion.  The complement cover is
connected and has transitive monodromy.  Thus a companion merely at general
points of every component is insufficient: the cone vertex, and in the
campaign every possible `S0` point, must be covered by the hypothesis.

### 5.2 Disconnected branch defeats label propagation

The cubic

```text
z^3-3z+2+xy=0
```

has reduced branch `xy(xy+4)=0`, a local `(2,1)` companion at every branch
point, and transitive `S3` monodromy.  Its branch is disconnected.  Two
differently labelled local transpositions can generate `S3`; local
companions alone do not globalize.  The proof above instead uses the central
spine meridian in a comb or one origin-local group which is already global
in a weighted cone.

### 5.3 Nonnormal conductor support can have identity inertia

Normality cannot silently be dropped from the generic-inertia step.  The
integral finite-flat double cover

```text
X={z^2=x^2 y} -> A2_(x,y)
```

is nonnormal.  Its reduced non-etale support is the contractible union of
the axes.  Off `x=0`, put `w=z/x`; the normalization is described by
`w^2=y`.  A generic meridian of the conductor axis `x=0` therefore has
identity monodromy even though that axis belongs to the non-etale support.
The full fixed set is not proper and its centralizer is all of `S2`.  This
example does not satisfy the rank-one hypothesis at its branch points and
is not a counterexample to the stated theorem; it isolates exactly why the
normality/tame-inertia premise was charged.  Nothing here licenses a claim
at a nonnormal conductor point lacking a length-one factor.

## 6. Generic companions plus positive Euler characteristic

Here is the promised strengthening.  Assume only that every irreducible
component of `B` has at least one generically unramified sheet, and retain
normality, integrality, finite flatness, and (0.1).  First suppose `B` is
connected and simply connected.

Normal form (I) needs no every-point hypothesis.  A generic point of the
spine of a comb, or of the unique component in a line degeneration, has both
a nontrivial inertia permutation and a fixed sheet.  Sections 2--3 apply
unchanged.

For normal form (II), write `B_i` for the irreducible components and put

```text
B_i^*=B_i-{0} isomorphic to C*.
```

The sets `B_i^*` are pairwise disjoint.  Define the constructible fibre-count
function

```text
u(z)=#(pi^(-1)(z) intersect U).
```

It equals `d` off `B`; let its generic value on `B_i^*` be `u_i>=1`.
For every special `z in B_i^*`,

```text
u(z)<=u_i.                                                   (6.1)
```

Indeed, every point of the special fibre lying in `U` is an etale point of
`pi`.  The complex inverse-function theorem gives a distinct local section
through each such point.  All these sections persist over nearby points, so
the nearby, and hence generic, fibre has at least as many unramified points.
Equivalently, fibre cardinality for the quasi-finite etale map `U->A2` is
lower semicontinuous.  Constructibility makes the exceptional set `P_i`
where `u!=u_i` finite.

If `u(0)>0`, an etale point above the origin splits off a rank-one factor
over the henselian local base.  The weighted radial global=origin-local
argument of Section 4 then makes the whole monodromy image fix a sheet,
contradicting transitivity.  Hence a hypothetical connected cover must have

```text
u(0)=0.                                                     (6.2)
```

The weighted cone has `e_c(B)=1`, so `e_c(A2-B)=0`.  Constructible Fubini,
`e_c(C*)=0`, (6.1), and (6.2) now give

```text
e_c(U)
 = d*e_c(A2-B)
   + sum_i [u_i*e_c(B_i^*-P_i)+sum_(z in P_i)u(z)] + u(0)
 = sum_i sum_(z in P_i)(u(z)-u_i)
 <=0.                                                       (6.3)
```

This contradicts (0.1).  Thus generic companions plus positive `e_c(U)`
exclude every normal form in every degree.

There is a useful disconnected extension.  Arzhantsev--Zaidenberg Corollary
1.2 states that every disconnected reduced plane curve whose connected
components are simply connected is equivalent to a union of `r>=2` parallel
lines.  Its complement has fundamental group `F_r`, freely generated by the
line meridians.  Write their images as `sigma_1,...,sigma_r`.  Normality and
generic companionship say that every `sigma_i` is nonidentity and has a
fixed point.  Put `c_i` for its number of nontrivial disjoint cycles and

```text
s_i=|Supp(sigma_i)|,       c_i>=1,       2<=s_i<=d-1.
```

Replace each nontrivial cycle by a spanning tree on its letters.  The union
of these cycle trees has exactly `sum_i(s_i-c_i)` edges, and its connected
components are the orbits of the generated group.  Transitivity therefore
gives

```text
sum_i(s_i-c_i)>=d-1,
sum_i s_i>=d-1+sum_i c_i>=d+r-1>=d+1.                    (6.4)
```

As above, the unramified-sheet count on the `i`-th line has generic value
`d-s_i` and can only drop at finitely many special points.  Since a line has
Euler characteristic one,

```text
e_c(U) <= d*e_c(A2-B)+sum_i(d-s_i)
        = d*(1-r)+r*d-sum_i s_i
        = d-sum_i s_i <= -1.                              (6.5)
```

This again contradicts (0.1).  Therefore the Euler-enhanced theorem excludes
every reduced branch for which **each connected component** is simply
connected, whether the branch is connected or not.

The sign in (6.1) and the Euler lower bound are load-bearing.  The quartic
cover

```text
X={w^4+a*w+b=0} -> A2_(a,b)
```

has irreducible weighted-cone branch `256b^3-27a^4=0`, generic partition
`(2,1,1)`, a total vertex `w^4`, and transitive monodromy.  Its etale-locus
open is

```text
U isomorphic to A1_w x Gm_(a+4w^3),       e_c(U)=0.
```

It saturates (6.3), showing that positivity cannot be omitted.

## 7. Canonical normalization of a Keller map

Let `F=(F,G):A2->A2` have nonzero constant Jacobian and suppose its generic
field degree is `d>=2`.  Put

```text
A=C[F,G],             L=C(x,y),
S=integral closure of A in L,       Y=Spec(S),
pi:Y->Spec(A)=A2.
```

All normalization interfaces can be proved directly at degree-one first
leg; no proper-intermediate-field assumption is used.

1. `F,G` are algebraically independent and `L/Frac(A)` is finite separable.
   Excellence of the polynomial ring `A` makes `S` finite over `A`.
   If `s in S`, its monic integral equation over `A` is also an integral
   equation over `C[x,y]`; since `C[x,y]` is integrally closed in `L`,
   `s in C[x,y]`.  Thus the literal inclusion `S subset C[x,y]` defines

   ```text
   j:A2_source -> Y,                 F=pi o j.
   ```

2. `Y` is an integral normal affine surface.  A normal surface is
   Cohen--Macaulay, and finite miracle flatness over the regular
   two-dimensional target makes `pi` finite flat of degree `d`.
3. The map `j` is birational and of finite type.  Every `j`-fibre lies in a
   finite fibre of the etale, hence quasi-finite, Keller map `F`, so `j` is
   quasi-finite.  Zariski Main for a quasi-finite birational morphism to the
   normal target `Y` makes `j` an open immersion.
4. Since `j` is an open immersion and `pi o j=F` is etale, `j(A2)` is
   disjoint from `R=NonEt_Y(pi)`.  Hence `j` factors as a dominant open
   immersion `A2->U=Y-R`.  The larger boundary `Y-j(A2)` can also contain
   unramified points; only `R subset Y-j(A2)` is asserted.  If `R` were
   empty, connected finite-etale `Y->A2` would have degree one, so `R` is
   nonempty when `d>=2`.

Every irreducible branch component `D` has a generic unramified sheet.  Write
the target coordinates as `(u,v)` and let `D=V(p_D(u,v))`.  Injectivity of
`C[u,v]->C[x,y]` makes the pullback `p_D(F,G)` a nonconstant polynomial,
hence a nonunit with a nonempty zero curve.  Its image under the quasi-finite
map `F` is dense in `D`; every source point maps through the ramification-
avoiding chart `j(A2)`.  Thus an unramified point exists over a dense open of
`D`.  This argument is only generic: a finite set of target values can still
be omitted by `F`.

The positive-Euler input also extends to this `d1=1` endpoint.  The proof of
the promoted proper-block ruling theorem uses only the properties just
established, not `d1>1`:

```text
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
```

For clarity, its argument specializes as follows.  The maximal etale open
`U` is affine (Stacks Project, Tag `0ECD`, applied to the finite map from
normal affine `Y` to regular `A2`) and smooth.  It is rational because
`C(U)=L=C(x,y)`.  Pullback along the dominant `j` gives
`O(U)^*=C^*`, and logarithmic Kodaira monotonicity gives
`bar-kappa(U)=-infinity`.  The Miyanishi--Sugie cylinder theorem and the
standard extension to a global fibration supply

```text
rho:U->C,       C=A1 or P1,
```

whose reduced fibres are disjoint unions of affine lines.  If `q_t>=1` is
the number of reduced components of a bad fibre, constructible Euler
additivity gives

```text
e_c(U)=e_c(C)+Q,       Q=sum_t(q_t-1)>=0,
```

and therefore `e_c(U)>=1`.

Section 6 now proves the exact canonical-normalization corollary:

> For a hypothetical noninvertible Keller map of any generic degree, the
> reduced branch support of its full canonical normalization has at least
> one connected component with nontrivial fundamental group.

This is the full normalization, not a strict block.  The proof does not
upgrade generic companion sheets to companions at omitted target values;
it uses the Euler substitute at precisely those values.

## 8. Generic degree three is impossible

Assume now that the generic field degree of the Keller map is three.  The
canonical-normalization objects of Section 7 satisfy a stronger closed
ledger.  Every step formerly phrased for a "proper cubic block" depends
only on the displayed finite-flat sandwich and the actual dominant morphism
`j:A2->U`, so it remains valid at `d1=1`; the argument is reconstructed here.
The prior reviewed ledger is retained as provenance, not used to hide the
endpoint extension:

```text
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
```

First, a degree-three fibre contains exactly one reduced non-etale source
point over every branch value: each non-etale local factor has length at
least two, and two such points would consume length at least four.  Hence

```text
R_red -> B
```

is finite and point-bijective, and therefore a homeomorphism on complex
analytic spaces.

Next, `B=pi(R)_red` is contained componentwise in the nonproper-value curve
`A_F`; equality of the whole curves is not asserted.  Indeed, `R` lies in
the boundary of the dense open chart `j(A2)`;
a sequence in that chart approaching a point of `R` escapes every compact
subset of the source while its `F`-image converges.  Since finite images of
components of `R` are curves, every component of `B` is an entire component
of `A_F`.  Nguyen Van Chau, *Note on the Jacobian condition and the
non-proper value set*, Annales Polonici Mathematici 84 (2004), 203--210,
DOI `10.4064/ap84-3-2`, Theorem 1, gives a polynomial parametrization of
every such component.  It follows that the normalization of every component
of `B`, and hence of `R_red`, is an affine line.

The everywhere-defined dominant morphism `j:A2->U` licenses the morphic
rational-forest theorem:

```text
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
```

Resolve the closure of `R` together with infinity.  The affine incidence
multigraph of `R_red`, retaining parallel branches, is a minor of the SNC
boundary forest.  It is therefore a forest.  Normalization additivity now
gives

```text
e_c(B)=e_c(R_red)=b0(R_red)=b0(B)=h>=1.                 (8.1)
```

Let `S0=A2-pi(U)`, the values with no unramified normalization sheet.
Section 7 makes `S0` finite.  The complete cubic fibre census is

```text
off B:       (1,1,1),       u(z)=3;
on B-S0:     (2,1),         u(z)=1;
on S0:       (3),           u(z)=0.
```

Constructible Fubini and the ruling identity give

```text
e_c(U)=3-2e_c(B)-|S0|=e_c(C)+Q.
```

If `C=P1`, this reads `2h+|S0|+Q=1`, impossible.  If `C=A1`, it reads
`2h+|S0|+Q=2`, whose unique solution is

```text
h=1,              S0=empty,              Q=0.          (8.2)
```

The connected incidence forest, with affine-line normalization components,
makes `R_red` contractible; the finite homeomorphism makes `B` contractible.
Equation (8.2) also upgrades the generic companion to a rank-one henselian
factor over **every** branch point.  The theorem of Section 0 now contradicts
the connected canonical cover.  Therefore

```text
[C(x,y):C(F,G)] != 3                                  (8.3)
```

for every complex polynomial Keller pair.  This says generic/topological
field degree three, not total polynomial degree three and not algebraic
degree of either coordinate separately.

## 9. Optimization-safe desk replay

The finite permutation claims are replayed by

```text
a75a91d65f2f95766581edb5b6dcf4a8e958844a0e66987ec7d94c898800cb98
  ops/block_descent_all_degree_acyclic_companion_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` runs have byte-identical stdout.
The stdout SHA-256 is

```text
71499353da07d047ec0d222454649779769e331db013845a5af3370fe7ebd35b
```

and the canonical payload SHA-256 embedded in that stdout is

```text
3586519ac48ca485bf4c91e8d32a5a89b3ebf3f77329b2e925abefd2e805f492
```

The replay exhausts canonical representatives of every nonidentity cycle
type with at least one fixed point for degrees two through eight.  For each
it enumerates the full centralizer and checks fixed-set invariance; it also
checks line cyclic groups, cone point stabilizers, multiple fixed points,
the degree-two empty cycle-type row, the missing-companion 3-cycle, the
disconnected two-transposition `S3` control saturating the `d+1` support
bound and Euler upper bound `-1`, and the nonnormal identity-inertia control.
It has zero AST `Assert` nodes.  The deliberate mutation
`--mutate-drop-centrality` is rejected.

The arbitrary-degree theorem is proved by the fixed-set identity in Section
2, not by extrapolation from degrees at most eight.  The replay does not
encode or claim to verify the acyclic-curve classification, the complement
presentations, normal generic inertia, henselian-to-analytic comparison, or
the realization of any algebraic cover.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23932`.
- Body SHA-256:
  `4d51593b20e6bbc473e54881370a1d748ca7337a56a9dda449f5deb5ddaa8724`.
- Frozen basis: `fdfbf4bea317622fa80e7da7404ef9dc0e88026c`.
