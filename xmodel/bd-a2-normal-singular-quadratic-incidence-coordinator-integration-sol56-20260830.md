# Binding integration: normal singular quadratic incidence reduction

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `4b89b45e00be2589a3568c921bc8771fa257461e`  
Lifecycle: **PROMOTED REDUCTION; NORMAL SINGULAR STRATUM NOT CLOSED**

## 0. Verdict, custody, and exact endpoint

This integration binds the transactional producer

```text
f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md
  body 19112 / b2a5c3b5e063333abd544be5c6a5d4b4b6dff1cd9a362b3471160a395ef03fea
  manifest 3a868fca72c94509ae0ae522447092d9fcd7da818e9fd0a7270b1e8512855f3d
```

to the independent GPT-5.5 xhigh hostile review

```text
79db365031ce865263648c836f14f537d6be9cd3674092a004ec2f33bf570865
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-hostile-review-gpt55-20260830.md
  body 15418 / 7b7b0cdba15638180d24147eb0d1d84e869a5b4c5840b96efee086d60baf4325
  verdict CONFIRM_WITH_CORRECTIONS
```

The producer was authored and sealed against dependency basis
`145f96d65021ef364a5189c4ca385fe09d7b4f46`, first committed at
`296bc55f8bd94b258337a874c94fc70c95b384a0`, and reviewed on exactly that
commit.  The review receipt was root-sealed and committed at the present
integration basis.  These are distinct lifecycle facts; no frozen input was
mutated.  The reviewer independently reconstructed every cohomology,
generic-conic, relative-MMP, lattice, and ramification step and found no
mathematical gap.  Its corrections are binding below.

Let

```text
X subset P2 times P1,       [X]=2A+3B,
```

be an irreducible normal Cartier hypersurface over `C`, with projections
`pi:X->P2` and `q:X->P1`, and let `r:Xtilde->X` be its minimal resolution.
Then the following surface-theoretic reduction is promoted without requiring
the dominant first leg:

```text
the generic q-fibre is a smooth conic and Xtilde is rational;
every singularity of X is Du Val and r is crepant;
K_Xtilde=-A+B, K^2=-1, p_g=q=0, e_top=13, rho=11;
Xtilde is a nine-blowup of a Hirzebruch surface F_e, 0<=e<=3;
(ZA+ZB)^perp in NS(Xtilde) is exactly D9(-1);
the exceptional ADE lattice is a possibly nonprimitive root sublattice;
in particular its rank is <=9 and an E8 singularity is impossible;
the resolved ramification is the exact Cartier pullback of class 2A+B,
is connected, contains every exceptional curve, and locally obeys n=C_ADE*m.
```

This is a reduction, not an exclusion of the normal singular stratum.

## 1. Cohomology, rationality, and rational singularities

The hypersurface sequence on `W=P2 times P1` is

```text
0 -> O_W(-2,-3) -> O_W -> O_X -> 0.
```

Every cohomology group of `O_P2(-2)` vanishes; Kunneth therefore kills every
cohomology group of `O_W(-2,-3)`, even though `H^1(P1,O(-3))` is nonzero.
The long exact sequence gives

```text
H^1(X,O_X)=H^2(X,O_X)=0.
```

Normality gives `r_*O_Xtilde=O_X`, and the singular set is finite.  The Leray
five-term sequence consequently gives the exact bridge

```text
H^1(Xtilde,O_Xtilde) ~= H^0(X,R^1r_*O_Xtilde),
H^2(Xtilde,O_Xtilde)=0.
```

The hypersurface vanishing alone does not prove rational singularities; the
left-hand group still has to vanish.

Projection `q` supplies that vanishing directly.  Its generic fibre over
`C(P1)` is a ternary quadratic form.  If its generic symmetric matrix had rank
two, then after a finite separable extension a kernel vector `v` and Jacobi's
formula would give

```text
0=d(det M)=lambda*v^t(dM)v.
```

At the fibre singular point all fibre derivatives and the base derivative
would vanish, producing a curve in `Sing(X)`.  Generic rank one similarly has
form `lambda*l^2` after finite extension and is singular along `l=0`, including
in the base direction.  Both contradict regularity in codimension one;
generic rank zero contradicts the nonzero irreducible hypersurface.  Thus the
generic conic is smooth.

Tsen gives it a `C(P1)`-point, so it is `P1` over the function field and
`Xtilde` is rational.  Equivalently the point extends, by properness, to a
section of the resolved fibration.  Hence `H^1(O_Xtilde)=0`, the Leray bridge
gives `R^1r_*O_Xtilde=0`, and every normal surface singularity of `X` is
rational.  In the intended block application the dominant first leg gives an
independent unirationality check, but no singular boundary conclusion is
imported from it here.

## 2. Du Val, crepancy, and numerical invariants

The normal Cartier hypersurface is Gorenstein, and adjunction gives

```text
K_X=-A+B.
```

Over `C`, rational Gorenstein surface singularities are rational double
points, hence Du Val.  Their minimal resolutions are crepant:

```text
K_Xtilde=r^*K_X=-A+B.
```

Using `A^2=3`, `A.B=2`, and `B^2=0` gives `K^2=-1`.  Rationality gives
`chi(O_Xtilde)=1`; Noether and Hodge theory then give

```text
c_2=e_top=13,       b_2=rho=11,       p_g=q=0.
```

The Picard rank is that of the smooth resolution, not the Weil class-group
rank of the singular surface.

## 3. Geometric ruled marking and exact `D9(-1)` complement

The generic conic is geometrically connected, so the Stein factor of
`q o r` has function field `C(P1)` and the resolved fibration has connected
fibres.  The section excludes multiple fibres: its intersection with a fibre
is one.  Contracting vertical `-1` curves ends at a relatively minimal
genus-zero fibration with section and no multiple fibres, hence at a
`P1`-bundle `F_e` over `P1`.

Since `K_F_e^2=8` and `K_Xtilde^2=-1`, exactly nine vertical blowups, possibly
at infinitely near points, recover `Xtilde`.  In their integral total-transform
basis,

```text
S^2=-e, S.F=1, F^2=0,
E_i^2=-1, S.E_i=F.E_i=E_i.E_j=0  (i!=j),
K=-2S-(e+2)F+sum E_i.
```

Here `F=B`.  Comparing the canonical formula with `K=-A+F` forces

```text
A=2S+(e+3)F-sum_(i=1)^9 E_i.
```

The `E_i` are total-transform lattice classes; the statement does not claim
that all nine are simultaneously irreducible curves after infinitely near
blowups.  Each actual blowup adjoins its exceptional total-transform class,
so these eleven classes are an integral NS basis with no hidden index.  The
total transform of the negative section of `F_e` is effective.  Since `A` is
nef,

```text
0<=A.S=3-e,
```

and the Hirzebruch convention gives `0<=e<=3`.  This uses the total transform,
not an unqualified assertion about its strict transform.

For `x=aS+bF+sum c_iE_i`, orthogonality to `F` gives `a=0`, and orthogonality
to `A` gives

```text
2b+sum c_i=0.
```

Thus `b` is integral exactly when `sum c_i` is even, and `x^2=-sum c_i^2`.
This is the explicit integral isometry

```text
(ZA+ZF)^perp ~= D9(-1)
 = {(c_1,...,c_9) in Z^9 : sum c_i even},
```

not an inference from rank and determinant.  The pair `<A,F>` is primitive:
the coordinate minor using the `F` row and any `E_i` row has determinant one.

The abstract even lattice `E8(-1) direct-sum <-4>` has the same rank,
determinant, and cyclic discriminant form (`q=-1/4`) as `D9(-1)`; those data
alone are inconclusive.  The ruled marking decides.  As a control, `D9` has
exactly 144 roots `+/-e_i +/- e_j`, spanning rank nine, while
`E8(-1) direct-sum <-4>` has 240 roots, all in its rank-eight `E8` summand.
The exceptional lattice is therefore only a possibly nonprimitive ADE root
sublattice of the actual `D9(-1)`.  Its rank is at most nine.  An isometric
`E8(-1)` embedding would inject 240 roots into the 144 roots of `D9`, so an
`E8` singularity cannot occur.  No analogous `E6` or `E7` exclusion is made.

## 4. Exact ramification pullback and ADE attachment equations

The generically finite degree-three map `pi:X->P2` is separable.  On the smooth
locus its determinant is a nonzero section of

```text
omega_X tensor pi^*omega_P2^(-1)=O_X(2A+B).
```

Normality extends it across the finite singular set.  Its zero divisor `R_X`
is a nonzero effective Cartier divisor, and `2A+B` is the restriction of the
ample ambient class `O(2,1)`.  An effective ample Cartier divisor on a normal
projective surface has connected support.

Crepancy identifies the determinant line bundle after resolution.  More is
needed for divisors: the determinant section of `pi o r` and the pullback of
the determinant section of `pi` agree on the common smooth dense open and are
sections of that same line bundle.  Hence their zero divisors are exactly
equal:

```text
R_(pi o r)=r^*R_X ~ 2A+B.
```

It follows that

```text
R^2=20,       A.R=8,       B.R=4,
R.E=0 for every r-exceptional curve E.
```

Every exceptional curve occurs in `R_(pi o r)`: it is contracted to a point
by `pi o r`, so the differential has rank at most one at its generic point.
Thus `R_X` passes through every singular point.  Connectedness of the total
pullback support follows from connectedness of `Supp(R_X)` and connected
resolution fibres.

Over one ADE tree write

```text
R_(pi o r)=R_str+sum_i m_iE_i,       m_i>=1,
n_i=R_str.E_i>=0.
```

Intersecting with each `E_i`, whose square is `-2`, gives

```text
n_i=2m_i-sum_(j adjacent i)m_j,
n=C_ADE*m.
```

The positive Cartan matrix is nonsingular and `m` is strictly positive, so
`n` cannot vanish.  Thus nonexceptional ramification meets every exceptional
tree with positive total intersection.

This does not prove two physical attachments.  A nonzero vector may be
realized at one physical point, at a crossing of exceptional components, or
on a carrier not belonging to the typed first-leg boundary.  It determines
neither the carriers nor independent paths to infinity.

## 5. Exact remaining finite client and firewall

The next client is an ADE-decorated infinity/different lattice, not another
arbitrary Picard search.  Up to the `D9` Weyl action and `e=0,1,2,3`, it must
classify the root sublattices that are actually effective, solve their local
positive Cartan systems, and impose the global total-transform classes

```text
H_total~A,             R_total~2A+B.
```

For every survivor it must type the strict infinity components, Cartier
multiplicities through each ADE tree, strict ramification carriers,
exceptional boundary vertices, effectivity/irreducibility of nonexceptional
classes, and actual physical attachment points.  Only then may the rational-
forest cycle test or smooth lattice enumeration be reused.  Abstract root
embeddings are not occurrence or effectivity certificates.

This integration does not close the normal singular stratum, classify all ADE
root sublattices, or prove two boundary attachments.  Nonnormal incidence and
conductor geometry are separate.  Also outside are basis existence or
minimization, another coefficient/block degree, a primitive extension,
polynomial map, counterexample, or JC2.  No CAS or AWS computation is charged;
any future heavy or uncertain computation remains AWS-only after a reviewed
source packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10793`.
- Body SHA-256:
  `4dec24303419b380454fa0b255350b98d495c11c833d5eb75377ceafec565fef`.
- Frozen basis: `4b89b45e00be2589a3568c921bc8771fa257461e`.
