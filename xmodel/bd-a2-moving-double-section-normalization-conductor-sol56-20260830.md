# The moving double section has irregular normalization

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra delegated lane `/root/whole_portfolio_ideation`  
Frozen basis: `dca72076aa1615b0b1286fd4428a1acac7b65963`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Charge the promoted proper cubic-block first leg and the exact provisional
nonnormal reduction

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
6b324824e0c075b938bd5b7015d4e8d134bad7cb845ac7597212b61d91dfa7a5
  xmodel/bd-a2-nonnormal-quadratic-content-cone-dichotomy-sol56-20260830.md.
```

The latter leaves exactly the following possible nonnormal quadratic
incidence.  In `W=P2 times P1`, with target infinity `T=0`, let

```text
X=V(F),                  [X]=2A+3B,
F=Q^2 L+T Q S+T^2 R,                                  (0.1)
H=X intersect {T=0}=2C+D_0,
C={T=Q=0},              [C]=(1,1),
D_0={T=L=0},             [D_0]=(0,1).                 (0.2)
```

Here `Q` is an irreducible bilinear form and `L,S,R` are constant binary
forms in the fibre coordinates of degrees `1,2,3`.  The generic binary
cubic is irreducible, so `X` is integral.  The proper-block first leg gives
a dominant rational map `A2 --> X`, equivalently into its normalization,
through the promoted function-field/Stein identification.

The maximum exact conclusion is:

> **MOVING-DOUBLE-Q2-CLOSED.**  The strict transform of `X` in the blowup
> `Bl_C(W)` is its finite normalization `nu:Xnu->X`.  Its conductor is the
> ideal of `C`; the reduced conductor divisor upstairs is a smooth connected
> genus-one degree-two cover `pi_E:E->C`.  Equivalently, `delta_C` has four
> distinct simple zeros, and
>
> ```text
> pi_(E*) O_E = O_C direct-sum O_C(-2),
> K_Xnu+E=nu^*K_X,
> nu_*O_Xnu/O_X = O_C(-2).                            (0.3)
> ```
>
> Consequently
>
> ```text
> h^1(Xnu,O_Xnu)=1,             h^2(Xnu,O_Xnu)=0.     (0.4)
> ```
>
> Every resolution of `Xnu` has irregularity at least one.  This contradicts
> the dominant rational `A2` first leg.  Therefore the surviving nonnormal
> form (0.1) cannot occur in a proper cubic block of a noninvertible plane
> Keller map.

This closes the **nonnormal quadratic presentation stratum**.  It does not
close the separately reduced normal-singular quadratic stratum, prove that
an arbitrary cubic block admits a quadratic basis, construct a map, or
settle JC2.

The conductor-cover quartic is classified completely below.  The charged
case is already squarefree, so the genus-one conductor and the cohomological
irregularity give independent contradictions.  The degenerate quartic rows
explain exactly where the blowup would cease to be normal if the previously
proved affine-normality input were removed.

## 1. Why (0.1) is exactly quadratic transverse to `C`

Both projections `C->L_infinity` and `C->P1_fibre` have degree one, so they
are isomorphisms.  On a fibre-coordinate chart use the fibre coordinate
`z` as a coordinate along `C`.  Holding `z` fixed, the bilinear form `Q` is
a linear coordinate transverse to `C` inside `T=0`; `T` is the other normal
coordinate.  Since `L,S,R` depend only on the fibre coordinate, the completed
local equation along `C` is literally

```text
ell(z) Q^2+s(z) TQ+r(z) T^2=0,                       (1.1)
```

with no terms of normal degree at least three.  Here

```text
ell=L|C in H^0(C,O_C(1)),
s=S|C   in H^0(C,O_C(2)),
r=R|C   in H^0(C,O_C(3)).                            (1.2)
```

This exact homogeneity is load-bearing.  Treating (1.1) as only the tangent
cone would not justify the conductor calculation.

No point of `C` has `ell=s=r=0`.  Indeed `ell=0` fixes the unique fibre root
of `L`; if `s` and `r` also vanished there, the constant binary forms `S`
and `R` would both be divisible by `L`, and (0.1) would factor by `L`,
contrary to generic irreducibility.

Define the normal quadratic discriminant

```text
delta_C=s^2-4*ell*r in H^0(C,O_C(4)).                 (1.3)
```

This is not the full affine target cubic discriminant.  It is the
discriminant of the rank-two normal cone along the nonnormal boundary.

At the generic point of `C`, (1.1) is a binary quadratic over `C(C)`.  If
`delta_C=0`, that local equation is a square and is nonreduced.  If
`delta_C` is a nonzero square in `C(C)`, it factors into two linear forms
over `C(C)`.  Either conclusion contradicts that the localization of the
integral surface `X` is a domain.  Therefore

```text
delta_C is nonzero and nonsquare in C(C).             (1.4)
```

In particular all split conductor cases are already unavailable in the
charged integral scope.

The previously proved affine normality strengthens (1.4) to

```text
delta_C is squarefree.                                (1.5)
```

First note that a multiple zero cannot occur where `ell=0`.  That zero of
`ell` is simple.  If `s` is nonzero there, then `delta_C=s^2` is nonzero;
if `s=0`, Section 1 gives `r!=0` and `delta_C=s^2-4ell*r` has a simple zero.
Thus at every hypothetical multiple zero one has `ell!=0`, so both roots of
the normal quadratic lie in the original `T`-chart.

Indeed, on each fibre-coordinate chart the exact bidegrees make `L,S,R`
functions of `z` alone.  Thus in the blowup chart `Q=T*w` the strict
equation is

```text
G(z,w)=ell(z)w^2+s(z)w+r(z)=0,                       (1.6)
```

independent of the radial coordinate `T`.  After making one quadratic
coefficient a unit and completing the square, a multiple zero of `delta_C`
is exactly a singular point `(z_0,w_0)` of the curve `G=0`.  The strict
transform then has the codimension-one singular locus

```text
{(z_0,w_0)} times A1_T.
```

Every point of this line with `T!=0` is nonexceptional, and the blowup maps
it isomorphically into the affine incidence `X_aff`.  Thus `X_aff` would
fail `R_1`, contradicting the affine-normality theorem charged in Section
0.  This local argument covers `C` because the projection `C->P1_fibre` is
an isomorphism and the fibre-coordinate charts cover it.  Hence all four
zeros of `delta_C` are simple.

## 2. The blowup is finite and is the normalization

Let `rho:What->W` be the blowup of the smooth complete-intersection curve
`C=(T,Q)` and let `X'` be the strict transform.  The equation has order
exactly two along `C`, so

```text
X' ~ rho^*X-2*E_W,                                   (2.1)
```

where `E_W` is the exceptional divisor.  In the two blowup charts the
strict-transform equations are

```text
Q=T*w:       w^2 L+w S+R=0,
T=Q*tau:     L+tau S+tau^2 R=0.                      (2.2)
```

Over `p in C`, the exceptional fibre is the length-two zero scheme

```text
ell(p) q^2+s(p) qt+r(p)t^2=0
        in P1_[q:t].                                 (2.3)
```

The three coefficients never vanish together by Section 1.  Hence every
fibre of `X'->X` is finite; the map is proper, quasi-finite, birational, and
therefore finite.

The blowup ambient `What` is smooth and `X'` is a hypersurface, hence `S_2`.
The predecessor's exact `R_1` classification says that `C` is the sole
possible divisorial nonnormal support: affine codimension-one points are
normal, and the residual infinity component is generically regular.  Since
the integral hypersurface `X` is `S_2`, it follows that `X minus C` is
normal, so `X'` is normal off the exceptional curve.  Equations
(1.4)--(1.5) make the relative quadratic curve (2.3) smooth; in both charts
of (2.2) the surface is locally its product with the radial parameter.  Thus
`X'` is regular along the exceptional curve and is `R_1`, hence normal.  The
finite birational map is therefore the normalization:

```text
X'=Xnu.                                               (2.4)
```

Its exceptional curve

```text
E=Xnu intersect E_W
```

is smooth and integral by (1.4)--(1.5), and `pi_E:E->C` is finite flat of
degree two.  Flatness follows either from the nonzero relative quadratic
(2.3) or from `E` being a relative degree-two Cartier divisor with no
vertical component.

## 3. Exact conductor, conductor square, and canonical divisor

The full conductor ideal downstairs is exactly

```text
I_C=(T,Q)O_X.                                         (3.1)
```

This can be checked without a seminormality shortcut.  Locally on `C`, make
an invertible linear change of the two normal parameters so that the
coefficient of `q^2` in (1.1) is a unit.  The normalization is then generated
by `w=q/t`, with

```text
q=t*w,                a*w^2+b*w+c=0,       a in O_C^*.
```

Modulo the original ring it is generated by the class of `w`, and

```text
t*w=q,
q*w=t*w^2=-(b/a)q-(c/a)t
```

belong to the original ring.  Thus `I_C` annihilates the normalization
quotient.  More explicitly, reduction modulo the extended ideal gives the
free quadratic algebra

```text
O_C[w]/(a*w^2+b*w+c),
```

whereas the image of the original ring is its `O_C` summand.  Hence the
quotient is freely and faithfully generated over `O_C` by the class of
`w`.  Its annihilator is exactly `I_C`, proving (3.1) uniformly along the
four simple branch fibres; no generic-fibre conductor assertion is being
used in place of this calculation.

Upstairs the conductor ideal is `O_Xnu(-E)`.  The standard conductor pushout
is the exact sequence

```text
0 -> O_X
  -> nu_*O_Xnu direct-sum O_C
  -> pi_(E*)O_E
  -> 0.                                                (3.2)
```

Trace splitting for the finite flat double cover gives

```text
pi_(E*)O_E=O_C direct-sum M.                          (3.3)
```

The discriminant of this algebra is (1.3).  Since it is a section of
`O_C(4)=M^(-2)` and `Pic(P1)` has no two-torsion,

```text
M=O_C(-2).                                            (3.4)
```

Taking the quotient in (3.2) proves the last identity in (0.3).

The same conductor multiplicity follows by adjunction.  A codimension-two
blowup has

```text
K_What=rho^*K_W+E_W.
```

Combining this with (2.1) gives

```text
K_Xnu=nu^*K_X-E,
K_Xnu+E=nu^*K_X.                                     (3.5)
```

Thus `E` is the reduced conductor divisor with coefficient one.  It is not
being called the source different of the map to `P2`.

## 4. The irregularity obstruction

The original nonnormal hypersurface still has its Cartier restriction
sequence

```text
0 -> O_(P2 times P1)(-2,-3)
  -> O_(P2 times P1)
  -> O_X -> 0.                                       (4.1)
```

All cohomology of `O_P2(-2)` vanishes, so Kunneth and (4.1) give

```text
H^1(X,O_X)=H^2(X,O_X)=0.                             (4.2)
```

The normalization sequence obtained from (3.2) is

```text
0 -> O_X -> nu_*O_Xnu -> O_C(-2) -> 0.              (4.3)
```

Because `H^0(P1,O(-2))=0` and `h^1(P1,O(-2))=1`, its long exact sequence
gives exactly

```text
h^1(Xnu,O_Xnu)=1,             h^2(Xnu,O_Xnu)=0.       (4.4)
```

For any resolution `r:Xtilde->Xnu`, normality gives `r_*O_Xtilde=O_Xnu`.
The Leray edge sequence injects

```text
H^1(Xnu,O_Xnu) -> H^1(Xtilde,O_Xtilde),
```

so `q(Xtilde)>=1`.

On the other hand the promoted proper-block first leg gives a dominant
rational map `A2 --> Xnu`.  Compactify and resolve its source and target.
The resulting generically finite dominant map from a rational surface
injects holomorphic one-forms from `Xtilde`, forcing `q(Xtilde)=0`.  This is
the contradiction proving `MOVING-DOUBLE-Q2-CLOSED`.

The objects used here are fully typed: (1.3) is a conductor-cover
discriminant, (3.1) is a surface-normalization conductor ideal, (3.5) is the
canonical conductor divisor, and (4.4) is coherent cohomology.  None is the
full affine target discriminant, source ramification, source different, a
normalization-index divisor over `A2`, formal arc data, or finite-prefix
evidence.

## 5. Complete quartic and genus classification

Although Sections 1 and 4 already constrain and exclude the form, the
quartic classification records the exact failure mode of every discarded
degeneration.

For a connected nonsquare finite flat double cover, the normalization of
`E` is branched over the points where `ord_p(delta_C)` is odd.  If there are
`b` such points,

```text
g(Enorm)=(b-2)/2.                                    (5.1)
```

The nonzero quartic has one of the following divisor partitions.

```text
div(delta_C) generic algebra    exceptional quadratic / effect on blowup
----------------------------------------------------------------------------
1+1+1+1      nonsquare/connected smooth integral genus-one E; X'=Xnu
2+1+1        nonsquare/connected nodal E, normalization P1; X' nonnormal
3+1          nonsquare/connected cuspidal E, normalization P1; X' nonnormal
2+2          square/split       two P1s meeting twice; X generically reducible
4            square/split       two tangent P1s; X generically reducible
delta_C=0    repeated           generic double component; X nonreduced locally
```

Over `C`, an effective quartic divisor is even exactly when its section is
a square up to a scalar.  Hence (1.4) removes the last three rows in the
charged integral scope.  Equation (1.5) removes the middle two connected
rows: in the exact product chart (1.6), normalizing the surface would require
normalizing the nodal or cuspidal curve and would expose a nonnormal curve
meeting the affine locus.  The first row is the only charged case.

The relative exceptional quadratic has trace-zero line `O_C(-2)` in every
nonzero row, even though it is the actual normalization conductor only in
the first row.  Hence its arithmetic genus is always one:

```text
chi(O_E)=chi(O_C)+chi(O_C(-2))=0,
p_a(E)=1.                                             (5.2)
```

The three connected rows distribute this one unit respectively into
geometric genus, a two-branch node, or a one-branch cusp.  Only the first is
compatible with affine normality.

## 6. The actual normalized infinity boundary

Let `D` be the strict transform of the residual section `D_0`.  Pulling back
the Cartier divisor `H={T=0}` gives

```text
nu^*H=E+D,                 D isomorphic to P1.        (6.1)
```

There is exactly one physical attachment between `D` and `E`.  Indeed
`C` and `D_0` meet at the unique fibre root `p_0` of `L`.  In exceptional
direction coordinates `[Q:T]`, `ell(p_0)=0`, so (2.3) becomes

```text
T*(s(p_0)Q+r(p_0)T)=0.                               (6.2)
```

If `s(p_0)!=0`, the conductor cover is unramified over `p_0`, but `D`
approaches only the direction `[Q:T]=[1:0]`; it does **not** attach to both
points of the conductor fibre.  If `s(p_0)=0`, irreducibility forces
`r(p_0)!=0`; then `p_0` is a simple zero of `delta_C`, and `D` meets the
single ramification branch.  Thus both cases give one physical attachment
and one analytic branch of `E` there.

This distinction is important: the two points of an unramified conductor
fibre are not automatically two attachments of a single strict-transform
curve.

## 7. Exact rational-forest test

The binding rational-forest theorem is

```text
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md.
```

It forbids either a positive-genus resolved boundary component or a cycle
in the resolved dual multigraph.  The first-leg image lies over the affine
target, whereas `E` lies over `T=0`; hence `E` is contained in the complement
of the lifted first-leg open and its strict transform is an actual boundary
component in every resolution used by the theorem.  Shrinking the target
open only adds boundary and cannot remove this obstruction.  In the only
charged type
`1+1+1+1`, the strict transform of the smooth conductor `E` has genus one.
This directly contradicts the forest theorem, independently of Section 4.

For the exact threat map obtained by temporarily dropping affine normality:

* In type `2+1+1`, the integral curve `E` has two analytic branches at its
  node.  Any embedded resolution connects those two branches through a
  connected exceptional fibre; because both branches belong to the same
  strict-transform vertex, the dual multigraph contains a cycle.
* In type `3+1`, the cusp is unibranch and `D` has only the single attachment
  proved in Section 6.  Resolving this conductor subboundary produces only
  rational components and a tree.  The forest theorem alone would not
  exclude this row, but affine normality already does.

For completeness, if integrality were dropped, split type `2+2` has two
rational conductor components meeting at two distinct physical points and
hence two independent graph paths, a cycle.  Split type `4` has the same two
components tangent at one physical point; its embedded resolution is a tree,
so the conductor subboundary alone would not exclude it.

Equivalently, using the promoted branch-count formula on `E union D`, the
intrinsic boundary contribution is

```text
tau(E union D)=1 for 1+1+1+1, 2+1+1, and split 2+2;
tau(E union D)=0 for 3+1 and split 4.                 (7.1)
```

In the discarded degenerate rows the blowup is not the surface
normalization; (7.1) is only the curve-theoretic contribution before that
further normalization.  Additional exceptional, boundary, and
source-critical components can add obstructions.  No claim that either zero
row is globally realizable is made.

In the charged squarefree row, the roots of `delta_C` are
projection-critical for the conductor cover.
They are not automatically physical attachments of the reduced source
different of `Xnu->P2`.  Formula (3.5) changes the canonical class by the
conductor, so importing the smooth ramification class or asserting a second
cycle from these branch points would be invalid.  No such assertion is used:
Section 1 excludes the degenerate rows before any source-different argument,
and Sections 4 and 7 independently exclude the charged squarefree row.

## 8. Maximum safe conclusion and successor

The exact theorem is Sections 0--7.  In the charged squarefree case the
blowup is not merely a candidate partial desingularization: finiteness,
`S_2`, `R_1`, and the conductor square identify it with the normalization
and compute its irregularity.  The quartic classification is algebraic, not
sampled evidence.  The earlier genus-one heuristic is now a theorem because
affine normality forces the quartic to be squarefree; independently, the
normalization exact sequence gives the irregularity certificate (4.4).

The actionable successor is now the **normal-singular** packet's
ADE-decorated `D9` boundary/different classification.  There is no remaining
nonnormal quadratic conductor case to enumerate.  Basis coverage remains
presentation-scoped: this theorem says that any quadratic basis producing a
nonnormal projective incidence is impossible for a proper block; it does not
prove that a quadratic basis exists or control higher-degree bases.

No heavy computation, AWS result, formal arc, finite prefix, source map,
counterexample, or JC2 conclusion is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18927`.
- Body SHA-256:
  `dfd050e37b97b119f6170259f7417ac69e8109723abec4abe8260e3c7a33be57`.
- Frozen basis: `dca72076aa1615b0b1286fd4428a1acac7b65963`.
