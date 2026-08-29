# `(8,12)` order two: exceptional affine-Faber `J` correction fan

Date: 2026-08-26

Status: **EXACT-SOURCE CLIENT DESIGN.  THE GENERIC COMPLETED OPEN IS
HAND-CLOSED, BUT BOTH EXCEPTIONAL FACES, THEIR TOTAL-REES ACCESSIBILITY,
AND ALL TERMINAL/TAYLOR CONSEQUENCES REMAIN OPEN.**

## 0. Purpose and routing

This is the nonlinear successor to

```text
fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md
```

on the normalized `D(k10*Delta)` exact-square affine-Faber graph.  Put

```text
D=Delta/4,
s=5*D-4*beta,
alpha=5*D+2*s,
kappa=5*D-2*s.                                    (0.1)
```

The generic open `D(D*alpha*kappa)` is routed to the all-orders `J=0`
theorem.  The only primitive correction clients are

```text
P3A: D(D*kappa), alpha=0,       odd corank one;
P3K: D(D*alpha), kappa=0,       odd corank two.    (0.2)
```

They are disjoint on `D(D)`.  `D=0` routes to the higher-contact square
receiver, and `k10=0` routes to the two-load boundary.  No limit of this
client is used for either route.

## 1. Literal normalized model

The client must start with the complete ordinary Faber source

```text
Phi_ell =
 r_ell(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
 -Lambda^(12+ell)*delta_ell,

(delta1,...,delta7)=(0,mu2,0,mu4,0,mu6,J/4).       (1.1)
```

It forms the total-Rees chart and retains the raw kernel and torsion before
setting an exceptional parameter to zero.  Only after the exact weighted
division in (1.1) may it identify a normalized centered octic

```text
F=Q^2+N,
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0                          (1.2)
```

and normalized loads `(1,beta,gamma)`.  Every power of `Lambda`, all three
loads, every moving load jet, and the target variables at the weights in
(1.1) remain in the source compiler.  If normalizing `k10` introduces a
Kummer coordinate, both sheets and the deck action must be printed.

On the central graph

```text
c=n3=n2=n1=n0=0,
gamma=D*(5*D-4*s)/16,
mu2=D^2*s/32.                                      (1.3)
```

The even target variables solve the even rows coefficientwise:

```text
mu2=R2,              mu4=R4,              mu6=R6. (1.4)
```

Thus the accessibility equations are exactly

```text
R1=R3=R5=0,                    J=4*R7.             (1.5)
```

No even row is silently set to zero after (1.4).

## 2. Charged raw controls

The complete compiler must reproduce, before any predecessor reduction,
radical, localization, or support substitution,

```text
c^5+128*R5-96*p*R3-(12*p^2+32*r)*R1=0             (2.1)
```

on the exact-square normalized slice, and the sharper identity

```text
128*R3+32*p*R1=c^3*(5*Delta-8*beta).               (2.2)
```

Identity (2.1) is the global raw nilpotence/contact sentinel.  Identity
(2.2) shows that the `A`-face has a cubic primitive face.  Neither identity
may be applied unchanged after square-normal terms are introduced; their
full correction remainders must be emitted.

The preliminary graph pivots are

```text
det d(R6,R2-mu2)/d(beta,gamma)=D^4/64.             (2.3)
```

After the graph is established, (1.4) is the cheaper continuing even solve.

## 3. Odd block and why no quadratic pure-kernel term exists

Use

```text
u=n1-(p/2)*n3,
C0=(5*D-3*s)/4,
K0=5*D*kappa/16,
B0=-p^2/32-D/4,
q0=D*alpha/32.                                     (3.1)
```

The first differential of `(R1,R3,R5)` in `(c,u,n3)` is

```text
          c                 u                    n3
R1        q0                C0/4                 0
R3       -p*q0/4           -p*C0/16              K0/4
R5        q0*B0             (C0*B0+K0)/4         -p*K0/16,

det=-q0*K0^2/16.                                   (3.2)
```

All odd rows are equivariant for simultaneous sign change of
`(c,u,n3)`.  After pivot elimination, every reduced obstruction and `R7`
is therefore odd in the surviving kernel variables.  At a fixed exceptional
even point, a vanished linear term is followed by a cubic term, not a
quadratic one.  Apparent order-two terms arise only as

```text
(first even transverse jet)*(first odd kernel jet). (3.3)
```

Accordingly both primitive Newton charts assign

```text
weight(odd kernel)=1,          weight(even transverse)=2. (3.4)
```

This weighted cubic computation simultaneously covers arbitrary ramified
arcs: if the first odd order is `q`, the only possible nonlinear tie has
transverse order `2*q`.  A lower transverse order is handled first and
returns to the invertible generic block.

## 4. `P3A`: corank-one cubic fan

On `alpha=0`, `D*kappa` is a unit and

```text
C0=25*D/8,                 K0=25*D^2/8.            (4.1)
```

Use rows `(R1,R3)` to solve `(u,n3)`; their determinant is `C0*K0/16`, a
unit.  Let

```text
PsiA = R5 after the exact formal (u,n3) solve,
JA   = 4*R7 after the same solve.                  (4.2)
```

Parity gives unique formal factorizations

```text
PsiA=c*GA(E,c^2),                 JA=c*HA(E,c^2),  (4.3)
```

where `E` consists of every even coefficient/load/source correction.  The
client must compute the weighted degree-two quotients

```text
GA = lambdaA(E)+qA*c^2+higher,
HA = etaA(E)+jA*c^2+higher.                        (4.4)
```

Here `lambdaA` and `etaA` retain the full linear images of all even
transverse source corrections; they are not replaced by `alpha` unless the
literal source map proves that reduction.  Tangential jets in `(p,D)` and
along the singular locus remain parameters.

On the pure exact-square subspace, (2.2) gives the nonzero cubic sentinel

```text
R3+(p/4)*R1=(5*Delta/512)*c^3                    (4.5)
```

at `alpha=0`.  Because `(R1,R3)` are the chosen pivot rows, (4.5) is a
compiler control rather than by itself the value of `qA`; square-normal
pivot corrections can move the residual to `R5`.

The primitive `A` incidence ideal is

```text
IA=(lambdaA+qA*x^2, zeta*HA-1),                   (4.6)
```

after normalizing the first nonzero `c` coefficient to `x=1` when the deck
and base field permit, or retaining `x` and saturating by `x` otherwise.
The raw, nonreduced version is primary; its radical is navigation only.

Typed endpoints:

```text
A_J_EMPTY
  IA is the unit ideal over exact Q.  No primitive J-nonzero A-face lift.

A_J_SURVIVOR
  IA has exact-Q support and the next-grade lift Jacobian is a unit.  Emit
  the branch equations and launch terminal/Taylor provisionally.

A_J_TANGENT_ONLY
  The weighted face has support but every point has HA=0, or the lift
  Jacobian drops rank.  Prolong one further odd degree; do not claim access.

A_SOURCE_MAP_FAIL
  A normalized even/odd correction is absent, duplicated, torsion, or has
  the wrong Lambda weight.  Stop before using (4.6).
```

## 5. `P3K`: corank-two projective cubic fan

On `kappa=0`, `D*alpha` is a unit and

```text
q0=5*D^2/16,                 C0=-5*D/8.            (5.1)
```

Use one unit entry of (3.2) to solve one transverse odd variable.  A
convenient kernel basis is

```text
x: (c,u,n3)=(1,2*D,0),
y: (c,u,n3)=(0,0,1).                               (5.2)
```

Thus the corresponding normal polynomials are `2*D*z` and
`z^3+(p/2)z=z*T`.  Let the two unpivoted odd rows be `(PsiK1,PsiK2)` and
put `JK=4*R7` after the same solve.  Their primitive expansions have the
form

```text
(PsiK1,PsiK2)=LK(E)*(x,y)^t+CK(x,y)+higher,
JK             =etaK(E)*(x,y)^t+HK(x,y)+higher,    (5.3)
```

where `LK` and `etaK` are linear in weight-two even transverse corrections,
and `CK`, `HK` are homogeneous cubics.  Every coefficient is computed from
the ordinary source.  No raw-Laurent Padé row is substituted.

Form the two projective kernel charts

```text
Kx: x=1, y=v,
Ky: y=1, x=v,                                      (5.4)
```

retain all even unfolding variables allowed by the literal source, impose
both leading equations in (5.3), and saturate by the leading `JK`.  The
endpoints `v=0` in both charts are retained; they cover unequal valuations
of the two kernel coordinates.  Deduplicate the `x*y != 0` overlap by the
transition `v |-> 1/v`, scheme-theoretically.

Typed endpoints are the `K` analogues of Section 4:

```text
K_J_EMPTY,
K_J_SURVIVOR,
K_J_TANGENT_ONLY,
K_SOURCE_MAP_FAIL.
```

If a chart is positive-dimensional, do not ask for a full primary
decomposition first.  Test `JK`-saturation, cover it by small coefficient
pivots, and certify lifting on each pivot open.  Only unresolved residual
support is decomposed.

## 6. Minimal complete-source compilers

Create two immutable packages, one per face.  Each compiler runs only on a
registered AWS EC2 lane and imports the complete frozen `tails.json`.  It
must:

1. independently reconstruct the seven ordinary Faber rows and verify the
   frozen digest;
2. substitute (1.2) coefficientwise, not by a post hoc square radical;
3. insert general formal coefficient, load, and target jets through ordinary
   order three, with the exact `Lambda` powers from (1.1);
4. verify (2.1), (2.2), (2.3), and every entry of (3.2) before face
   specialization;
5. solve only the declared unit pivots and print their determinants;
6. emit the reduced Kuranishi and `J` leading forms in (4.4) or (5.3), plus
   a direct substitution residual for every solved pivot;
7. keep the raw face ideals, then separately compute `J`-saturations and
   projective-chart overlaps; and
8. run exact `Q` as producer and characteristic 65521 as an independent
   software control.  Every displayed denominator and both exceptional
   factors are nonzero modulo 65521.

The jobs are small coefficient-jet clients: request at most 32 vCPUs and
64 GiB per lane, cap virtual memory, and stop each lane after 30 minutes.
Do not run compilation, Singular, SymPy, Sage, or another CAS locally.

### Stop conditions

Stop immediately on any of:

- a mismatch with the frozen full-tail digest or ordinary Faber connection;
- a failed coefficient-coordinate or total-Rees map;
- loss of a load, target, square-normal, moving-center, or deck variable;
- disagreement between a hand identity and exact-Q expansion;
- a pivot determinant not equal to the preregistered unit up to a printed
  unit factor;
- inconsistent `Kx/Ky` overlap; or
- exact-Q/good-prime disagreement not explained by a printed bad prime.

## 7. Promotion and downstream trigger

A `J_SURVIVOR` is provisional source accessibility, not a counterexample.
Without waiting for hostile review, launch in parallel:

1. the next correction grade needed for formal lifting;
2. terminal `[6,2]` with every correction and load retained;
3. the Taylor pullback at `x=0`; and
4. the Taylor pullback at `x=1`.

Promotion requires exact-Q custody, an independent hostile mathematical
review, a literal total-Rees overlap map, and a proved formal lifting
criterion.  If both faces return `J_EMPTY`, combine them with the reviewed
generic complete-local theorem to close the entire `D(k10*Delta)`
affine-Faber receiver locally; only then route the remaining `Delta=0` and
`k10=0` charts.

## 8. Explicit nonclaims

This design does not assert that either exceptional incidence ideal is empty
or nonempty, that normalized coefficient deformations are all source
accessible, or that a cubic leading solution prolongs.  It does not replace
the raw total-Rees ideal by its radical or symmetric algebra, identify a
Kummer sheet without its deck action, or infer finite-branch Taylor data from
an infinity expansion.  It does not treat `Delta=0`, `k10=0`, terminal
`[6,2]`, either Taylor family, the other square/discriminant receivers, order
two, `(8,12)`, maximum twelve, or JC2.
