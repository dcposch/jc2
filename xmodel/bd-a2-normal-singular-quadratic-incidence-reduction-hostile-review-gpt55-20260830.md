# Hostile review: normal singular quadratic incidence reduction

Reviewer: GPT-5.5 xhigh  
Review basis: `296bc55f8bd94b258337a874c94fc70c95b384a0`  
Producer reviewed:
`xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md`

## Custody and scope

The worktree head is the requested review basis.  The reviewed full-file
SHA-256 is

```text
f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
```

and the body through `<!-- BODY-END -->` has SHA-256

```text
b2a5c3b5e063333abd544be5c6a5d4b4b6dff1cd9a362b3471160a395ef03fea.
```

I read the full producer and the four Section 0 inputs named there:

```text
ac7ef8f5321f579d5e193b6ae3a9b0f1aa2a64421050bb71426b94258d984ffb
  xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-sol56-20260830.md

c9871c92ce8748fd934dc57061f667b49952a1aba39aee43eb3af7b0aadbf392
  xmodel/bd-a2-ramification-lattice-closure-coordinator-integration-sol56-20260830.md

ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md

6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md
```

No CAS, Singular, build, sampling, or input edit is used.  No new exit-price
assertion is made, so FALLACY-v2 requires no `charge_basis` line.

## Overall verdict

`CONFIRM_WITH_CORRECTIONS`.

The main reduction is mathematically sound in its declared normal,
characteristic-zero, class-`(2A+3B)` scope.  The safe theorem is not a
normal-singular exclusion.  It is a surface-theoretic reduction to a rational
Du Val resolution with an exact `D9(-1)` ambient orthogonal complement, plus
connected ramification and a local Cartan attachment equation.  Several
steps require explicit wording repairs before promotion, but I find no
counterexample to the stated maximum theorem after those repairs.

## 1. Cohomology and Leray bridge

Verdict: `CONFIRMED`, with a required anti-shortcut statement.

For `W=P2 times P1` and `X in |2A+3B|`, the hypersurface sequence is

```text
0 -> O_W(-2,-3) -> O_W -> O_X -> 0.
```

The producer's cohomology computation is correct.  On `P2`,

```text
H^p(P2,O(-2))=0 for p=0,1,2,
```

with the top vanishing by Serre duality against `H^0(P2,O(-1))`.  Kunneth
therefore kills every `H^i(W,O_W(-2,-3))`, despite
`H^1(P1,O(-3))` being nonzero, because every summand has a zero `P2`
factor.  The long exact sequence gives

```text
H^0(X,O_X)=C,  H^1(X,O_X)=0,  H^2(X,O_X)=0.
```

For the resolution `r:Xtilde->X`, normality gives `r_*O_Xtilde=O_X`; the
normal surface singular locus is finite, so `R^1r_*O_Xtilde` is supported
on finitely many points and has no higher cohomology.  The Leray five-term
sequence is exactly

```text
0 -> H^1(X,O_X) -> H^1(Xtilde,O_Xtilde)
  -> H^0(X,R^1r_*O_Xtilde) -> H^2(X,O_X)
  -> H^2(Xtilde,O_Xtilde) -> H^1(X,R^1r_*O_Xtilde).
```

Using the hypersurface vanishing gives

```text
H^1(Xtilde,O_Xtilde) ~= H^0(X,R^1r_*O_Xtilde),
H^2(Xtilde,O_Xtilde)=0.
```

This is the load-bearing bridge.  The vanishing of `H^1(O_X)` and
`H^2(O_X)` alone does not prove rational singularities; one must separately
prove `H^1(O_Xtilde)=0`, then finite support implies
`R^1r_*O_Xtilde=0`.

## 2. Rationality routes

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

The first-leg route is safe only as an optional application-scope route: a
dominant rational map from `A2` to `Xtilde` makes the smooth projective
surface unirational, hence rational in characteristic zero by Castelnuovo.
It must not be used to import any singular-boundary attachment conclusion
not present in the charged first-leg inputs.

The direct conic route is independently valid after spelling out the
normality argument over the generic point.  Let `K=C(P1)` and let the
generic fibre of `q:X->P1` be the ternary quadratic form represented by a
symmetric matrix `M` over `K`.

If the generic rank is two, then over a finite separable extension there is
a kernel vector `v`, and `adj(M)=lambda vv^t` with `lambda != 0`.  Since
`det(M)=0` identically,

```text
0=d(det M)=trace(adj(M)dM)=lambda v^t(dM)v.
```

Thus the base derivative vanishes at the fibre singular point, while all
fibre derivatives already vanish there.  The closure of this generic point
is a curve in `Sing(X)`, contradicting normality.

If the generic rank is one, then after finite extension the form is
`lambda l^2`; on the line `l=0` the equation, all fibre derivatives, and
the base derivative vanish.  This again gives a positive-dimensional
singular locus.  Rank zero would make the generic equation vanish, contrary
to `X` being a nonzero irreducible hypersurface.  Hence normality forces the
generic conic to be smooth.

Tsen applies to the smooth conic over `C(P1)` and gives a rational point.
The point makes the conic `P1` over `K`, so the function field of `X` is
`C(P1)(u)`.  Equivalently, properness extends the generic point to a rational
section, and then to a section of the resolution.  Therefore `Xtilde` is a
rational surface and `H^1(O_Xtilde)=0`.  Feeding this back into Leray proves
that the singularities are rational.

Repair: state that connected fibres for the resolved fibration come from
the Stein factor having function field `C(P1)` because the generic conic is
geometrically connected.  The section is then used to exclude multiple
fibres, not to prove connectedness by itself.

## 3. Du Val, crepancy, and invariants

Verdict: `CONFIRMED`.

The characteristic-zero and normality inputs are sufficient.  Since `X` is
a normal Cartier hypersurface in the smooth threefold `P2 times P1`, it is
Gorenstein and adjunction gives

```text
K_X=(-3A-2B+2A+3B)|_X=-A+B.
```

The Leray/rationality bridge proves rational singularities.  A normal
rational Gorenstein surface singularity over `C` is Du Val, so the minimal
resolution is crepant:

```text
K_Xtilde=r^*K_X=-A+B.
```

The ambient intersections are

```text
A^2=3,  A.B=2,  B^2=0,
```

and hence

```text
K_Xtilde^2=(-A+B)^2=3-4=-1.
```

Rationality gives `chi(O_Xtilde)=1`.  Noether's formula gives

```text
e_top(Xtilde)=c_2=12 chi - K^2 = 13.
```

Since `q=p_g=0`, `b_2=e_top-2=11` and Hodge theory gives
`rho(Xtilde)=h^{1,1}=11`.

## 4. Relative MMP over `P1`

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

After the conic/Tsen step, `f=q o r:Xtilde->P1` is a genus-zero fibration
with connected fibres and a section.  The section excludes multiple fibres:
if a fibre had all multiplicities divisible by `m>1`, its intersection with
the section would be divisible by `m`, contradicting `section.fibre=1`.

Contract vertical `-1` curves.  A reducible genus-zero fibre on a smooth
surface with no multiple fibre contains a vertical `-1` component, so the
relatively minimal endpoint is a `P1`-bundle over `P1`, hence a Hirzebruch
surface `F_e`.  Reversing the contractions realizes `Xtilde` as nine
blowups of `F_e`, including infinitely near centres, because

```text
K_F_e^2=8,  K_Xtilde^2=-1.
```

In the total-transform basis

```text
S^2=-e,  S.F=1,  F^2=0,
E_i^2=-1,  E_i.E_j=0 (i != j),
```

the canonical class is

```text
K=-2S-(e+2)F+sum E_i.
```

Since `F=B` and `K=-A+F`, the class of the target hyperplane is forced:

```text
A=2S+(e+3)F-sum E_i.
```

This uses no effectivity of the `E_i` as simultaneous irreducible curves;
they are total-transform lattice classes.  The classes form an integral
Neron-Severi basis because each blowup adjoins one exceptional total
transform and the rational surface has `rho=11`.

The bound is also correct:

```text
0 <= e <= 3.
```

Here `e>=0` is the Hirzebruch convention.  The total transform of the
negative section of `F_e` is effective on `Xtilde`, and `A` is nef as the
pullback of `O_P2(1)`, so

```text
0 <= A.S = 3-e.
```

Repair: the proof should explicitly distinguish "total transform of the
negative section" from an assertion about its strict transform after
infinitely near blowups.

## 5. Integral orthogonal complement

Verdict: `CONFIRMED`.

For

```text
x=aS+bF+sum c_iE_i,
```

the condition `x.F=0` gives `a=0`.  Then

```text
x.A=2b+sum c_i,
```

so `b` is integral exactly when `sum c_i` is even, and

```text
x^2=-sum c_i^2.
```

Thus the map to the `c_i` coordinates gives the exact integral isometry

```text
(ZA+ZF)^perp ~= D9(-1)
={c in Z^9 : sum c_i even},  (c,c')=-sum c_i c_i'.
```

The pair `<A,F>` is primitive: in the coordinate matrix for the two
generators, the minor using the `F` row and any `E_i` row has determinant
one.  Therefore no hidden finite-index quotient or overlattice is being
introduced by the complement calculation.

The producer is also right that determinant, parity, and discriminant form
alone do not identify the lattice.  `D9(-1)` and `E8(-1) direct-sum <-4>`
both have rank nine, determinant four, and cyclic discriminant form with a
generator of square `-1/4 mod 2Z`.  The ruled blowup marking, not those
abstract invariants, decides the issue.

The root-count control is valid.  In `D9(-1)`, roots are exactly
`+/-e_i +/- e_j` for `i != j`, so there are `4*binomial(9,2)=144`.  In
`E8(-1) direct-sum <-4>`, all square-`-2` vectors lie in the `E8(-1)`
summand, giving 240 roots spanning rank eight.  The lattices are not
isometric.  Moreover an `E8` exceptional singularity would embed an
`E8(-1)` root lattice into `D9(-1)` and would inject its 240 roots into the
144 roots of `D9`; this is impossible.  No analogous exclusion of `E6` or
`E7` follows.

## 6. Ramification and connectedness

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

The map `pi:X->P2` is generically finite of degree `A^2=3`, hence
generically separable in characteristic zero.  On `X_sm`, the determinant of
`dpi` is a section of

```text
omega_X tensor pi^*omega_P2^(-1) = O_X(2A+B).
```

Normality extends this section across the finite singular set.  Its divisor
is an effective Cartier divisor because `O_X(2A+B)` is invertible and the
section is nonzero on the integral surface.  It is nonzero as a divisor:
otherwise `O_X(2A+B)` would be trivial, contradicting its positive
intersection numbers.

The class `2A+B` is ample on `X`, being the restriction of `O(2,1)` from
`P2 times P1`.  An effective ample Cartier divisor on a normal projective
surface has connected support, so `Supp(R_X)` is connected.

Crepancy gives exact equality of divisors on the resolution, not merely
linear equivalence.  The determinant section for `pi o r` and the pullback
of the determinant section for `pi` are sections of the same line bundle
and agree away from the exceptional locus; hence

```text
R_(pi o r)=r^*R_X.
```

The intersection calculations are correct:

```text
R^2=(2A+B)^2=20,
A.R=8,
B.R=4,
R.C=0 for every r-exceptional curve C.
```

Every exceptional curve occurs in `R_(pi o r)`: it is contracted to a point
by `pi o r`, so the differential has rank at most one at its generic point
and the determinant vanishes there.  Consequently `R_X` passes through every
singular point of `X`.  The connected support of `r^*R_X` follows from
connectedness of `Supp(R_X)` and connected fibres of the resolution.

Repair: the packet should explicitly say "exact equality of determinant
divisors after pullback" before using exceptional coefficients.  Crepancy
alone gives the line bundle class; equality of sections gives the divisor.

## 7. Local ADE equations

Verdict: `CONFIRMED`, with a strict limit on interpretation.

Over one ADE tree, write

```text
R_(pi o r)=R_str+sum m_iE_i,
```

with `R_str` having no exceptional component.  Each `m_i>=1` because every
exceptional curve is a component of the ramification divisor of `pi o r`.
Set

```text
n_i=R_str.E_i >= 0.
```

Since `R_(pi o r).E_i=0`, `E_i^2=-2`, and adjacent exceptional curves meet
once, one gets

```text
0=n_i-2m_i+sum_(j adjacent i)m_j,
n_i=2m_i-sum_(j adjacent i)m_j.
```

Thus, in positive ADE Cartan notation,

```text
n=C_ADE m.
```

The signs are correct.  The vector `n` cannot vanish: the ADE Cartan matrix
is nonsingular, while `m` has strictly positive entries.  Therefore the
nonexceptional ramification meets each exceptional tree in positive total
intersection.

This does not prove two physical boundary attachments.  A nonzero `n` may
be carried by one physical point, a point lying at an intersection of
exceptional components, or by a component not belonging to the completed
first-leg boundary.  The equations determine neither the number of physical
attachment points, nor the carrier components, nor whether those contacts
give independent paths to infinity.

## 8. Maximum theorem safe to promote

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The following theorem is safe after the repairs above:

Let `X` be an irreducible normal Cartier hypersurface of class `2A+3B` in
`P2 times P1` over `C`, and let `r:Xtilde->X` be its minimal resolution.
Then the generic `q:X->P1` conic is smooth, `Xtilde` is rational, and the
singularities of `X` are rational Du Val singularities.  The resolution is
crepant and satisfies

```text
K_Xtilde=-A+B,  K_Xtilde^2=-1,
p_g=q=0,  e_top=13,  rho=11.
```

The resolved projection to `P1` is a nine-blowup of a Hirzebruch surface
`F_e` with `0<=e<=3`.  In the total-transform blowup marking,

```text
A=2S+(e+3)F-sum E_i,
F=B,
(ZA+ZF)^perp = D9(-1).
```

The exceptional ADE lattice is a possibly nonprimitive root sublattice of
`D9(-1)`; in particular its rank is at most nine and no `E8` singularity
occurs.  The ramification divisor of `pi o r` is exactly the Cartier
pullback of the normal-surface ramification divisor in class `2A+B`; its
support is connected, every exceptional curve occurs in it, and each ADE
tree satisfies `n=C_ADE m` with `m_i>=1` and `n != 0`.

This does not exclude the normal singular stratum.  It does not classify
which ADE sublattices occur, does not prove effectivity of all lattice
carriers, does not identify the completed first-leg boundary through the
exceptional trees, and does not supply two physical attachments or a
rational-forest cycle.

The charged smooth inputs remain confined to the smooth, projectively finite,
reduced-squarefree, fixed-presentation quadratic stratum.  They cannot be
used to decide nonnormal incidences, singular infinity, singular
ramification multiplicities, basis minimization, arbitrary polynomial maps,
counterexamples, or JC2.

## Cheapest decisive successors

The smallest finite successor is an ADE-decorated
infinity/different-lattice packet, not a general Picard search.

It should enumerate, up to the `D9` Weyl action and the four values
`e=0,1,2,3`, the possible ADE root sublattices
`Lambda_exc subset D9(-1)` excluding `E8`; solve the local positive Cartan
systems `n=C_ADE m`; and impose compatibility with the global classes

```text
H_total ~ A,
R_total ~ 2A+B.
```

For each survivor it must record the strict infinity components, the
Cartier multiplicities through every ADE tree, the strict ramification
carriers, effectivity and irreducibility of nonexceptional classes, and the
actual physical intersection points after resolution.  Only after that data
is typed can the rational-forest and smooth lattice-cycle tests be reused.

Keep separate: nonnormal incidence closures and conductor geometry;
effectivity versus abstract lattice classes; classification of
ADE-decorated infinity/different data versus occurrence of such data;
coverage of alternate Miranda bases; polynomial-map existence; proposed
counterexamples; and JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15418`.
- Body SHA-256:
  `7b7b0cdba15638180d24147eb0d1d84e869a5b4c5840b96efee086d60baf4325`.
- Frozen basis: `296bc55f8bd94b258337a874c94fc70c95b384a0`.
