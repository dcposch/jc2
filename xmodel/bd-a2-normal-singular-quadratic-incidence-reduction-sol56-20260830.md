# Normal singular quadratic incidence: Du Val and the exact `D9` ambient lattice

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic_degeneracy_frontier`  
Frozen basis: `145f96d65021ef364a5189c4ca385fe09d7b4f46`  
Lifecycle: **EXACT PROVISIONAL REDUCTION / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint, ancestry, and maximum theorem

This is the bounded normal-singular successor to the smooth quadratic packet

```text
ac7ef8f5321f579d5e193b6ae3a9b0f1aa2a64421050bb71426b94258d984ffb
  xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-sol56-20260830.md
```

and to the promoted smooth finite lattice integration

```text
c9871c92ce8748fd934dc57061f667b49952a1aba39aee43eb3af7b0aadbf392
  xmodel/bd-a2-ramification-lattice-closure-coordinator-integration-sol56-20260830.md.
```

The first-leg inputs are the promoted block structure and rational-forest
integrations

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md

6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md.
```

Let

```text
X subset P2 times P1,       [X]=2A+3B,               (0.1)
```

be an irreducible **normal** quadratic incidence hypersurface over `C`, and
write `pi:X->P2` and `q:X->P1` for the projections.  Let
`r:Xtilde->X` be the minimal resolution.  The intended application also has
the declared dominant `A2` first-leg open.  That first leg supplies one
rationality check, but the direct conic argument in Section 2 shows that the
surface-theoretic reduction itself does not require it.  The maximum exact
reduction proved here is:

> **NORMAL-Q2-REDUCE.**  Every singularity of `X` is Du Val.  The resolution
> `Xtilde` is rational and crepant, with
>
> ```text
> K_Xtilde=-A+B,       K_Xtilde^2=-1,
> p_g=q=0,             e_top=13,   rho=11.           (0.2)
> ```
>
> Projection to `P1` makes `Xtilde` a nine-blowup model of a Hirzebruch
> surface.  In a ruled blowup marking the orthogonal complement
>
> ```text
> L=(ZA+ZB)^perp subset NS(Xtilde)                   (0.3)
> ```
>
> is exactly the negative `D9` lattice
>
> ```text
> L = {c in Z^9 : sum c_i is even},
> c.c'=-sum c_i*c_i'.                                (0.4)
> ```
>
> The total exceptional ADE lattice is only a root sublattice of `L`; it is
> not asserted to equal `D9`.  In particular its rank is at most nine.

The alternative abstract even lattice `E8(-1) direct-sum <-4>` has the same
rank and determinant as (0.4), so determinant and parity do not decide the
issue.  Section 5 derives (0.4) from the ruled blowup marking and then
distinguishes the two candidates by their roots.  No `D9` identification is
assumed.

This packet does not eliminate the normal singular stratum.  Its exact
remaining gap is the effective, local-to-global classification of the total
transforms of infinity and the source different inside the `D9`-marked
lattice, including their multiplicities through the ADE exceptional trees.

## 1. Cohomology of the normal hypersurface

Put `W=P2 times P1`.  Because `X` is a Cartier divisor of class `(2,3)`,

```text
0 -> O_W(-2,-3) -> O_W -> O_X -> 0.                 (1.1)
```

Every cohomology group of `O_P2(-2)` vanishes: the top group is dual to
`H^0(O_P2(-1))`, and the intermediate group vanishes.  Kunneth therefore
gives

```text
H^i(W,O_W(-2,-3))=0       for every i.               (1.2)
```

Since `H^1(W,O_W)=H^2(W,O_W)=0`, the long exact sequence gives the exact
surface statements

```text
H^1(X,O_X)=0,             H^2(X,O_X)=0.              (1.3)
```

Normality implies `r_*O_Xtilde=O_X`, and the singular set is finite.  Hence
`R^1r_*O_Xtilde` is a finite-support sheaf.  The Leray five-term sequence,
using (1.3), is

```text
H^1(Xtilde,O_Xtilde)  isomorphic to
H^0(X,R^1r_*O_Xtilde),
H^2(Xtilde,O_Xtilde)=0.                              (1.4)
```

Equation (1.4) is the required bridge: vanishing of `q(Xtilde)` is exactly
what turns the hypersurface cohomology into rational singularities.  The
vanishing (1.3) alone would not suffice.

## 2. Why the resolution is rational and the singularities are rational

There are two independent routes to `q(Xtilde)=0` in the declared scope.

First, the dominant first-leg morphism `A2->U subset X_sm` induces a dominant
rational map to `Xtilde`.  Compactifying the source and resolving
indeterminacy makes `Xtilde` unirational.  In characteristic zero a smooth
projective unirational surface has `p_g=q=0` (indeed it is rational by the
Castelnuovo criterion).  Thus the first-leg bridge already supplies the left
side of (1.4) as zero.

Second, the incidence itself gives a direct rationality check.  Projection

```text
q:X->P1                                                   (2.1)
```

has generic fibre a plane conic.  That conic is smooth.  To see the
load-bearing use of normality, represent it by a symmetric matrix `M(t)`.
If `det M` vanished identically and `M` had generic rank two, a kernel vector
`v` would satisfy all fibre derivatives.  Jacobi's formula gives

```text
0=(det M)'=trace(adj(M)M')=lambda*v^t*M'*v,
```

so the base derivative vanishes at the same generic point.  Its closure is a
curve in `Sing(X)`, contrary to normality.  Generic rank at most one has a
positive-dimensional fibre singular locus.  More explicitly, after a finite
extension of the function field a generic rank-one form is `lambda*l^2`;
both its fibre derivatives and its base derivative vanish along `l=0`.
That again produces a singular curve dominating the base, incompatible with
regularity in codimension one.  Generic rank zero is impossible for the
irreducible hypersurface.  Thus the generic conic is smooth.  Tsen's theorem
gives it a `C(P1)`-point, so it is `P1` over the function field and `Xtilde`
is rational.

Therefore `H^1(Xtilde,O_Xtilde)=0`.  Equation (1.4) gives

```text
H^0(R^1r_*O_Xtilde)=0.
```

A nonzero coherent sheaf of finite support has a nonzero global section, so

```text
R^1r_*O_Xtilde=0.                                    (2.2)
```

This is precisely rationality of every normal surface singularity of `X`.

## 3. Gorenstein rational implies Du Val and crepant

The hypersurface `X` is Gorenstein.  Dualizing adjunction, valid for the
normal Cartier hypersurface, gives

```text
omega_X=O_X(-A+B),       K_X=-A+B.                   (3.1)
```

Over `C`, a normal rational Gorenstein surface singularity is a rational
double point, equivalently a Du Val singularity.  Hence the exceptional
curves of the minimal resolution form a disjoint union of ADE Dynkin trees,
every irreducible exceptional curve has square `-2`, and

```text
K_Xtilde=r^*K_X=-A+B.                                (3.2)
```

Thus the resolution is crepant.  Ambient intersection gives

```text
A^2=3,       A.B=2,       B^2=0,
K_Xtilde^2=(-A+B)^2=-1.                              (3.3)
```

Rationality gives `chi(O_Xtilde)=1`.  Noether's formula and Hodge theory now
give

```text
c_2(Xtilde)=e_top(Xtilde)=12*chi-K^2=13,
b_2(Xtilde)=11,
rho(Xtilde)=11.                                      (3.4)
```

Here `rho=11` is the Picard rank of the smooth resolution, not the Weil
class-group rank of the singular surface.

## 4. The ruled nine-blowup marking

The morphism `q o r:Xtilde->P1` has smooth rational generic fibre and a
section by Tsen and properness.  Its fibres are connected by Stein
factorization, and the section excludes multiple fibres.  Contract vertical
`-1` curves.  The relative minimal-model theorem for a genus-zero fibration
with a section identifies the endpoint with a `P1`-bundle, hence with a
Hirzebruch surface `F_e`: a reducible genus-zero fibre on a smooth surface
contains a vertical `-1` component, while the section has already excluded
multiple fibres, so the relatively minimal endpoint has only smooth `P1`
fibres.  Thus this is a geometrically constructed marking, not a postulated
abstract Picard-lattice orbit.  The reverse map expresses `Xtilde` as
blowups at points of fibres, possibly infinitely near.

Since `K_(F_e)^2=8` and every blowup lowers `K^2` by one, (3.3) shows that
there are exactly nine blowups.  Use total-transform classes

```text
S^2=-e,       S.F=1,       F^2=0,
E_i^2=-1,     S.E_i=F.E_i=E_i.E_j=0  (i!=j),         (4.1)
```

where `F=B` and `i=1,...,9`.  The canonical class is

```text
K_Xtilde=-2S-(e+2)F+sum_(i=1)^9 E_i.                (4.2)
```

Write

```text
A=2S+bF+sum m_iE_i,
```

where the coefficient of `S` is forced by `A.F=2`.  Comparing (4.2) with
the crepant equality `K_Xtilde=-A+F` determines every coefficient, without
an effectivity assumption:

```text
A=2S+(e+3)F-sum_(i=1)^9 E_i.                        (4.3)
```

Equations (4.1)--(4.3) recover `A^2=3` and `A.F=2`.  They remain valid when
some blowup centres are infinitely near; the `E_i` are total-transform
lattice classes, not a claim that all nine are simultaneously irreducible
exceptional curves.  Moreover these eleven classes are an integral basis of
`NS(Xtilde)`: each vertical contraction is an actual blowdown and each
reverse step adjoins its total-transform exceptional class.  There is no
unmentioned finite-index overlattice in this marking.

The marking has the further inexpensive bound

```text
0<=e<=3.                                             (4.4)
```

Indeed the total transform of the negative section of `F_e` is effective,
`A` is nef, and (4.1)--(4.3) give `A.S=3-e`.

## 5. The orthogonal complement is `D9`, not an unproved guess

Let

```text
L=(ZA+ZF)^perp subset NS(Xtilde).                    (5.1)
```

Write a general class as

```text
x=aS+bF+sum c_iE_i.
```

The equation `x.F=0` gives `a=0`, and (4.3) then gives

```text
x.A=2b+sum c_i=0.                                    (5.2)
```

Thus `b` is integral exactly when `sum c_i` is even, and

```text
x^2=-sum c_i^2.                                      (5.3)
```

The map `x |-> (c_1,...,c_9)` is therefore an explicit integral isometry

```text
L isomorphic to D9(-1)
 = {(c_i) in Z^9 : sum c_i even},
   pairing -sum c_i c_i'.                            (5.4)
```

In particular `L` is even, negative definite, rank nine, and determinant
four.  The pair `ZA+ZF` is primitive in `NS(Xtilde)`: in the basis (4.1),
the two-by-two minor using the `F` and any `E_i` rows has determinant one.
Thus (5.4) is the actual orthogonal complement of the geometric primitive
pair, rather than merely a finite-index candidate.
No transitivity theorem for ruled markings is being used: one actual
relative blowdown supplies an integral basis in which the intrinsic lattice
`L` is computed, and the calculation is independent of `e` and of the
chosen blowdown order.

The abstract data “even, negative definite, rank nine, determinant four” do
**not** alone prove (5.4).  For example

```text
E8(-1) direct-sum <-4>                               (5.5)
```

has the same four properties.

The discriminant form also does not distinguish these two lattices.  For
`D9(-1)`, the class of

```text
g=(1/2,...,1/2)
```

generates the order-four discriminant group and has
`q(g)=-9/4=-1/4 mod 2Z`.  The generator of the discriminant group of the
`<-4>` summand in (5.5) has square `-1/4`.  Hence both discriminant forms are
the cyclic order-four form with value `-1/4`; primitivity and discriminant
data alone are still inconclusive.

The explicit marking already decides between them.  As a further invariant
check, the roots of (5.4) are exactly

```text
plus-or-minus e_i plus-or-minus e_j,       i!=j,
```

so there are `4*binomial(9,2)=144` and they span rank nine.  In (5.5), every
square-`-2` vector lies in the `E8(-1)` summand; there are 240 such roots and
they span only rank eight inside the rank-nine lattice.  Hence (5.4) and
(5.5) are not isometric.  The `E8 direct-sum <-4>` alternative is explicitly
refuted here, not silently discarded.

## 6. What the ADE exceptional lattice actually inherits

Let `Lambda_exc` be the lattice generated by the irreducible curves
exceptional for `r`.  Pullback divisors have zero intersection with every
such curve, so

```text
Lambda_exc subset L=D9(-1).                          (6.1)
```

By Section 3, `Lambda_exc` is a direct sum of negative ADE root lattices.
Therefore the exact conclusions are only:

```text
rank Lambda_exc <= 9,
Lambda_exc is an integral root sublattice of D9(-1),
every exceptional curve is vertical for Xtilde->P1. (6.2)
```

The inclusion need not be primitive and need not have full rank.  No
determinant quotient may be taken without an index calculation.  In
particular `Lambda_exc=D9(-1)` is **not** promoted.

One additional exclusion is immediate and self-contained: an `E8(-1)` root
lattice cannot embed isometrically in `D9(-1)`, because its 240 distinct
roots would have to map to 240 distinct roots while `D9` has only 144.
Thus an `E8` singularity cannot occur in this normal incidence/first-leg
scope (indeed the first leg is not needed for this exclusion).  No analogous
exclusion of `E6` or `E7`, and no classification of all
root sublattices of `D9`, is asserted here.

## 7. Crepant ramification data and its exact limit

The map `pi:X->P2` is generically finite of degree `A^2=3`; in characteristic
zero it is generically separable.  On the smooth locus of `X`, the
determinant of `d pi` is therefore a nonzero section of

```text
omega_X tensor pi^*omega_P2^(-1)=O_X(2A+B).          (7.1)
```

Normality extends this section across the finite singular set.  Its divisor
`R_X` is a nonzero effective Cartier divisor in the ample class `2A+B`.
An effective ample Cartier divisor on a normal projective surface has
connected support.  Crepancy identifies the ramification divisor of
`pi o r` with the total Cartier pullback:

```text
R_Xtilde=r^*R_X ~ 2A+B.                              (7.2)
```

In the ruled marking this class is exactly

```text
R_Xtilde ~ 4S+(2e+7)F-2sum_(i=1)^9 E_i.
```

Consequently

```text
R_Xtilde^2=20,       A.R_Xtilde=8,       B.R_Xtilde=4,
R_Xtilde.C=0 for every r-exceptional curve C.         (7.3)
```

Its total support is connected.  On `Xtilde`, however, `2A+B` is only nef
and big: it has zero intersection with all ADE exceptional curves.  It is
not ample when `X` is singular.  Crepancy also does not mean that exceptional
curves are absent from the total different.  In fact every `r`-exceptional
curve occurs in `R_Xtilde`: the map `pi o r` contracts that curve to a point,
so its differential has rank at most one at the generic point of the curve
and its determinant vanishes there.  Consequently `R_X` passes through every
singular point of `X`.

There is a useful exact local equation, but not yet a classification.  Over
one singular point, write

```text
R_Xtilde=R_str+sum_i m_i E_i,       m_i>=1,          (7.4)
```

where the `E_i` form its ADE tree and `R_str` has no exceptional component.
Set `n_i=R_str.E_i>=0`.  Intersecting (7.4) with `E_i` and using (7.3) gives

```text
n_i=2m_i-sum_(j adjacent to i) m_j.                 (7.5)
```

Thus, in positive Cartan notation, `n=C_ADE*m`.  The attachment vector `n`
cannot vanish: the ADE Cartan matrix is nonsingular, whereas every `m_i` is
positive.  Hence the nonexceptional ramification meets every exceptional
tree at least once, counted with intersection multiplicity.  Equations
(7.4)--(7.5) do not determine `m`, the number of physical attachment points,
or which nonexceptional components carry those attachments.

This is exactly where the smooth connectedness/attachment proof stops.  The
connected total support in (7.2) and the nonzero attachment vector (7.5) are
useful, but without the local pullback multiplicities and physical attachment
points through each ADE tree they do not supply two independent boundary
paths.

## 8. Hostile checks and false shortcuts

The reduction survives the following attacks.

* **`H^1(O_X)=H^2(O_X)=0` alone proves rational singularities.**  False.
  The missing term is `H^1(O_Xtilde)`.  Section 2 kills it by the first leg
  and independently by the conic/Tsen rationality argument before using
  Leray.
* **Normality is cosmetic.**  False.  It makes the singular set finite,
  supplies `r_*O=O`, and prevents a generically singular conic whose singular
  locus would dominate the base.  None of Sections 1--3 is transferred to a
  nonnormal closure.
* **Rational automatically means Du Val.**  False without Gorenstein.  The
  hypersurface Gorenstein property is the additional input.
* **Crepant means the exceptional curves do not occur in the different.**
  False.  It identifies the total pullback class and rational section; local
  Cartier pullback multiplicities remain.
* **Rank nine and determinant four imply `D9`.**  False, with (5.5) as the
  explicit control.  The ruled nine-blowup marking proves `D9`; the root
  counts independently distinguish the candidates.
* **The exceptional lattice is the orthogonal complement.**  False.  It is
  only a possibly nonprimitive ADE root sublattice.
* **The old smooth conic-bundle marking can be copied verbatim.**  The total
  transform lattice marking survives, but its effective `E_i` curves and
  fibre components may be altered by infinitely near centres and ADE
  resolutions.  Effectivity must be rebuilt.
* **Connected ramification already gives a cycle.**  Not without two typed
  physical attachments after resolving the ADE trees.

No CAS, finite-field sampling, or AWS computation is used.

## 9. Exact remaining gap and scope firewall

The next finite object is an **ADE-decorated boundary/different lattice**, not
a search over arbitrary Picard groups.  It must determine, for every allowed
root sublattice `Lambda_exc subset D9(-1)`:

1. the reduced strict transform and Cartier multiplicities of infinity
   `H~A`, including nonreduced leading forms and projective coefficient
   basepoints;
2. the total pullback of `R_X~2A+B` through each ADE tree, with local
   intersection and different multiplicities;
3. which exceptional vertices belong to the completed first-leg boundary;
4. the physical attachment points between the connected different support
   and the resolved infinity tree; and
5. effectivity and irreducibility of all nonexceptional carrier classes in
   the ruled nine-blowup marking.

Only after those data are typed can the rational-forest cycle test or the
smooth `F5` lattice enumeration be reused.  The present packet supplies no
normal-singular exclusion and no occurrence theorem.

The hypotheses are: characteristic zero; an irreducible normal Cartier
hypersurface of class `2A+3B`; the promoted proper cubic block/first-leg
scope when the first-leg route is invoked; and the minimal resolution.
Nonnormal incidence closures are wholly outside: their normalization,
conductor curve, cohomology sequence, and generic-conic singular locus need
separate treatment.  Also outside are basis minimization, a proof that an
arbitrary cubic block has a quadratic presentation, higher coefficient
degree, another block degree, block primitivity, a polynomial map, a
counterexample, and JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19112`.
- Body SHA-256:
  `b2a5c3b5e063333abd544be5c6a5d4b4b6dff1cd9a362b3471160a395ef03fea`.
- Frozen basis: `145f96d65021ef364a5189c4ca385fe09d7b4f46`.
