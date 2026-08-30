# Producer: rational-forest first-leg gate and the first nonlinear Miranda family

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra with independent Sol multisection lane  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **EXACT DESK PRODUCER / DIFFERENT-MODEL HOSTILE REVIEW REQUIRED**

## 0. Verdict

The reviewed two-section log theorem has a simpler multisection successor.
For a smooth compactification with reduced SNC boundary, the first log
plurigenus is controlled by the genera of the boundary components and the
cycle rank of their dual graph.  Therefore any dominant `A^2` first leg
forces the resolved boundary to be a rational forest.

Applied to polynomial Miranda coefficients of target degree `d`, this gives:

```text
d>=3, smooth projective incidence closure: impossible, because p_g>0;
d=2, generic smooth incidence closure:      impossible, because the
                                             infinity curve has genus 2;
d=2, generic SNC full boundary:              bar-P_1=18.
```

This does not close all nonlinear cubic blocks.  It reduces the quadratic-
coefficient family to the explicit degeneration locus where the resolved
infinity boundary is a rational forest, plus nonreduced, singular-ambient,
projective-basepoint, and degree-drop strata.

## 1. Exact rational-forest theorem

Let `X` be a smooth projective complex surface and

```text
D=union_i D_i
```

a reduced SNC divisor.  Let `Gamma_D` be the dual multigraph, with one edge
for each intersection point, including parallel edges, and put

```text
tau(D)=sum_i genus(D_i)+b1(Gamma_D),
b1(Gamma_D)=#edges-#vertices+#connected_components.
```

The Poincare residue sequence is

```text
0 -> omega_X -> omega_X(D) -> omega_D -> 0.
```

The normalization sequence and duality for the possibly disconnected nodal
curve `D` give

```text
h^0(D,omega_D)=h^1(D,O_D)=tau(D).
```

Taking cohomology in the residue sequence yields the exact formula

```text
bar-P_1(X minus D)
 = p_g(X)+tau(D)-rank(partial),                       (1.1)
```

where

```text
partial:H^0(D,omega_D)->H^1(X,omega_X).
```

By Serre duality `h^1(X,omega_X)=q(X)`, so

```text
p_g(X)+max(tau(D)-q(X),0)
 <= bar-P_1(X minus D)
 <= p_g(X)+tau(D).                                   (1.2)
```

In particular, if `q(X)=0`, then

```text
bar-P_1(X minus D)=p_g(X)+sum_i genus(D_i)+b1(Gamma_D). (1.3)
```

Now suppose there is a dominant morphism

```text
A^2 -> U=X minus D.
```

It extends to a dominant rational map `P^2 --> X`, so `X` is unirational.
Over `C`, this forces `q(X)=p_g(X)=0`.  Since logarithmic Kodaira dimension
cannot increase under a dominant generically finite map from `A^2`, a
positive right side in (1.3) is impossible.  Thus:

> **Rational-forest gate.** Every component of the reduced resolved boundary
> of a target admitting a dominant `A^2` first leg is rational, and its dual
> graph is a forest.

This is a necessary condition, not a sufficient construction of a first leg.

## 2. Multisections and recovery of the two-section theorem

Let `P->P^1` be a ruled surface, `D_infinity` a section, and `C` an
irreducible `k`-multisection.  Let `Cbar` be its normalization, of genus `g`,
and let `r` be the number of analytic branches of `C` meeting
`D_infinity`; intersection multiplicity is not used in `r`.

After resolving the reduced boundary,

```text
bar-P_1(P minus (C union D_infinity))
 >= g+max(r-1,0).                                    (2.1)
```

Indeed, `Cbar` contributes `g`.  Each of the `r` distinct branch paths joins
the vertices corresponding to `Cbar` and `D_infinity`; the first makes them
connected and each further path adds a graph cycle.  Other multibranch
singularities can only add cycles or positive-genus components.  Equality
holds if `C` is smooth away from the displayed contacts and no additional
boundary singularity adds a cycle.

Consequently a dominant `A^2` first leg is impossible whenever

```text
genus(Cbar)>0       or       r>=2.                   (2.2)
```

Contact orders merely subdivide one path and do not change (2.1).  Nodes and
other multibranch self-singularities create cycles; unibranch cusps attach
trees and can remain invisible.  For two rational sections, the `#S` contact
fibres give `#S` paths and (1.3) gives `bar-P_1=#S-1`, recovering the reviewed
two-section result at its first plurigenus.

## 3. Sharp countercontrols and the discrepancy gate

Positive multisection degree alone is insufficient.  Take

```text
P=P^1_z times P^1_w,
D_infinity={w=infinity},
C=closure({z=w^k}),       k>=2.
```

Relative to projection to `P^1_z`, `C` is a smooth rational `k`-multisection
meeting the infinity section in one branch, and the boundary graph is a tree.
In fact the complement is exactly `A^2`.  An explicit map is

```text
(w,t) |-> (w, z=[t:t*w^k+1]),
t=Z0/(Z1-w^k*Z0).
```

Thus the rational-forest gate is sharp at this type.

For any embedded log resolution `rho:Xtilde->X`, let

```text
N_E=v_E(D),
a_E=v_E(K_Xtilde-rho^*K_X),
lambda_E=N_E-a_E-1.
```

Then, exactly,

```text
K_Xtilde+Dtilde = rho^*(K_X+D)-sum_E lambda_E E,

bar-P_n(U)=dim {s in H^0(X,n(K_X+D)):
                v_E(s)>=n*lambda_E for every E}.     (3.1)
```

For two smooth branches tangent to order `mu`, the successive losses are
`lambda_(E_i)=i-1`.  A unibranch cusp can consume an effective `K+D` without
creating a graph cycle, so (3.1), rather than raw fibre degree or raw
effectivity, is the exact residual gate after the rational-forest test.

## 4. Homogeneous Miranda incidence geometry

Suppose a global trace-zero Miranda basis has polynomial coefficients of
common homogenized target degree `d`.  Homogenize in `[u:v:z]` and let

```text
X_d={Phi^h=0} subset P^2_[u:v:z] times P^1_[X:Y].
```

Write `A` and `B` for the two hyperplane classes.  The incidence hypersurface
has class `dA+3B`; if it is smooth and irreducible, adjunction gives

```text
K_(X_d)=(d-3)A+B.                                    (4.1)
```

For `d>=3`, restriction of ambient sections gives

```text
p_g(X_d)=h^0(X_d,K_Xd)=(d-1)(d-2)>0.                 (4.2)
```

Hence no dense open of such a smooth closure admits a dominant `A^2` first
leg.  A surviving presentation of degree at least three must have a singular
or degenerate infinity closure, a reducible/extraneous projective component,
or an actual degree drop after cancellation.  Polynomial changes of Miranda
basis can change presentation degree, so (4.2) is presentationwise, not yet
an intrinsic invariant of the cubic algebra.

## 5. The first nonlinear family: `d=2`

A smooth `X_2->P^1` is a conic bundle.  Tsen's theorem gives a rational point
on its generic conic over `C(P^1)`, so `X_2` is rational.  Its infinity curve

```text
H_infinity=X_2 intersect ({z=0} times P^1)
```

has bidegree `(2,3)` on `P^1 times P^1`, and is generically smooth of genus

```text
(2-1)(3-1)=2.
```

The rational-forest gate therefore excludes the generic quadratic-
coefficient Miranda block from the infinity component alone.

On the additional projectively finite smooth locus, for
`pi:X_2->P^2`, Hurwitz gives

```text
R_pi=2A+B,          H_infinity=A,
K_X2+H_infinity+R_pi=2A+2B.                          (5.1)
```

If `R_pi` is reduced, shares no component with `H_infinity`, and the pair is
generic SNC, adjunction/intersection give

```text
p_a(H_infinity)=2,
p_a(R_pi)=9,
H_infinity.R_pi=8,
bar-P_1=2+9+(8-1)=18.                                (5.2)
```

If the reduced pair is log canonical, (5.1) is ample and the complement is
log general type.  If it is not log canonical, (3.1) is the correct test.
Affine fixed-sheet information does not automatically control reducedness,
common components, or singularities at infinity.

## 6. Exact successor and nonclaims

The cheapest nonlinear successor is finite:

1. classify reduced bidegree-`(2,3)` infinity curves whose embedded
   resolution is a rational forest;
2. quarantine nonreduced infinity separately;
3. on each surviving stratum, add the ramification curve and retest the full
   resolved boundary forest; and
4. only then compute higher log plurigenera by the valuation conditions
   (3.1).

This producer does not exclude every quadratic or higher-degree presentation,
does not make presentation degree intrinsic, and proves no general cubic
block theorem, primitivity statement, map, counterexample, or JC2 result.
Promotion requires a different-model hostile review of (1.1)--(1.3), the
unirational implication, both countercontrols, the adjunction and genus
computations, and every projective-closure hypothesis.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8578`.
- Body SHA-256:
  `42aedb00e89804034c3a16f3205c12e18e14133cd9d0dc0189b7e286428ecf64`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
