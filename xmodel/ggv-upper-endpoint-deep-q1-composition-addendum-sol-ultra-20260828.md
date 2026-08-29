# Full-system q1 composition addendum for the deep endpoint locus

Date: 2026-08-28  
Status: **EXACT q1 REDUCTION + FINITE FOUR-ROOT SYSTEM + ONE-POINT TANGENT OBSTRUCTION; NO FULL EXCLUSION**

## 1. Verdict and custody

The q1 parametrization is used here only at its licensed full-system stage,
after D23.  It is not inferred from D7--D22.

On the active deep component `A|V0`, q1 collapses the apparent family to

```text
R0=lambda A,
V0=3lambda A A',
S=V0/A=3lambda A'.                                   (Q1)
```

The split `lambda=0` versus `lambda!=0` is geometrically useful, but the two
branches are equivalent under a legal constant source shear.  For
`lambda!=0`, the root-local leading fourth-power face is universal after the
natural `A'` normalization; globally, the shear

```text
X -> X-(3lambda/4)t
```

kills `F1`, preserves the target `t^22`, and preserves every raw degree
window.  Thus the q1 consequence pass reduces to `lambda=0`.

On `lambda=0`, all four roots of `A` are common `A,S` roots.  The preceding
Newton theorem then globally forces

```text
A | P1,
A | F7.                                                (Q2)
```

The remaining leading endpoint conditions form a finite 15-equation
difference system after eliminating `c14,c16,c18,c20` and the endpoint
kernel scalar.  I do not find a universal contradiction in that system.
At its exact square homogeneous seed, however, the endpoint direction is
already obstructed in the linearization: the exact four-root coefficient
matrix has rank 13 and the target augmentation rank 14.

This is a sharper next discriminator, not an emptiness theorem.  A nonlinear
component away from the square seed may still satisfy the finite system, and
subleading odd Newton rows have not yet been added.

The literal `(S,Q)=(1,1)` two-parameter-family point in the predecessor
packet is **not q1** and was checked only through D22.  It must not be used
as a D23/full-system survivor.

## 2. Exact q1 collapse

The licensed q1 formula and degree bound are

```text
V0=A'R0+2AR0',             deg R0<=4.
```

On `A|V0`, reduction modulo `A` gives

```text
0 = A'R0 mod A.
```

Because `A` is squarefree, `gcd(A,A')=1`, hence `A|R0`.  Since `A` is monic
quartic and `deg R0<=4`, `R0=lambda A`.  Substitution gives `(Q1)` exactly.
No D23 formula beyond its licensed q1 consequence is used below.

## 3. The `lambda!=0` face and exact reduction to `lambda=0`

Let `alpha` be a simple root of `A`.  With `z=t/A`, the reviewed active lift
gives the leading face

```text
A^-4 F(X,Az) -> (1+S(alpha)z/4)^4.
```

Under `(Q1)`, put `w=A'(alpha)z`.  Then every root has the same normalized
face

```text
(1+3lambda w/4)^4.                                    (U)
```

There is also an exact global explanation.  Since

```text
F0'=4A^3A',
F1=A^3S=3lambda A^3A'=(3lambda/4)F0',
```

set `h=3lambda/4` and define

```text
Fbar(X,t)=F(X-h t,t),
Gbar(X,t)=G(X-h t,t).
```

Then `Fbar_1=F1-hF0'=0`.  The determinant is exactly shear-covariant:

```text
Fbar_X(12Gbar-tGbar_t)+(tFbar_t-8Fbar)Gbar_X
 = [F_X(12G-tG_t)+(tF_t-8F)G_X](X-h t,t).
```

The two `h t F_XG_X` cross terms cancel.  The source shear has Jacobian one
and fixes `t`, so a target `t^22` remains `t^22`.

It also preserves the authoritative windows.  A monomial `X^d t^i` with
`d<=N-i` expands into `X^(d-r)t^(i+r)`, and

```text
d-r <= N-(i+r).
```

Thus the q1 `lambda!=0` branch is not a separate endpoint problem: it is
transported exactly to the `lambda=0` branch.  This constant shear is legal;
the analogous rational shear for arbitrary q1 data would not have this
automatic polynomial-window property.

## 4. Consequences on `lambda=0`

Now `S=0` identically.  On the exact active-`c2`, exact-`D=0` successor,

```text
Z=-AQ/2,
R=0,
4U=A ell,
256F5=A P1,
2048F6-8U^2=A e1.
```

Every simple root of `A` is a common root of `A` and `S`.  The slope-`3/5`
and slope-`4/7` arguments in the predecessor report apply at all four roots:

```text
P1(alpha)=F7(alpha)=0       for every A(alpha)=0.
```

Squarefreeness yields the global divisibilities `(Q2)`.  With the raw degree
windows one may write

```text
Q has degree <=2,
P1=A p2 with deg p2<=3,
U=A ell/4 with deg ell<=1,
e1 has degree <=6,
F7=A f7bar with deg f7bar<=5,
F8 has degree <=8.
```

Only the root values of `Q,e1,F8` enter the next leading face.  Evaluation
modulo `A` gives three degrees of freedom for `Q` and arbitrary four-tuples
for each of `e1,F8`.

## 5. Smallest leading four-root endpoint system

For a root `alpha` define

```text
u_alpha=(q_alpha,e_alpha,f_alpha)
       =(Q(alpha),e1(alpha),F8(alpha)),

p_alpha(z)=(1-q_alpha z/16)^2
            +e_alpha z^3/2048+f_alpha z^4.
```

Let the six lower global modes be `d_k=c_(2k)`, `1<=k<=6`.  Starting with

```text
p_alpha^(3/2)
 +sum_(k=1,...,6) d_k z^k p_alpha^((6-k)/4),
```

recursively choose the born coefficients needed to kill `z^7,z^8,z^9,z^10`.
Call the resulting four scalar maps

```text
B_r(u_alpha;d_1,...,d_6),        r=7,8,9,10,
```

and call the surviving `z^11` coefficient

```text
rho(u_alpha;d_1,...,d_6).
```

Because the modes `c14,c16,c18,c20` are global, and because
`A^5g22=I_A/8+gamma` with `I_A'=A`, the necessary root system is

```text
B_r(u_alpha;d)=d_r,              r=7,...,10,
rho(u_alpha;d)=I_A(alpha)/8+gamma.                    (F20)
```

This is 20 scalar equations over the four-root etale algebra.  Eliminating
the four `d_r` and `gamma` by comparing three roots with a base root gives
the smaller difference system

```text
B_r(u_alpha;d)-B_r(u_beta;d)=0,                        12 equations,
rho(u_alpha;d)-rho(u_beta;d)
  =(I_A(alpha)-I_A(beta))/8,                            3 equations. (F15)
```

The variables are the three-dimensional residue class of `Q`, the two
arbitrary four-tuples from `e1,F8`, and the six lower modes: 17 scalar
variables before subleading rows.  An optional `c22` and the homogeneous
kernel both disappear from `(F15)`.

This is the smallest exact leading-face discriminator I obtain from q1 plus
the reviewed D7--D22 cascade.  It is necessary, not sufficient: it omits the
half-step odd-face equations and the higher local coefficients needed when
the endpoint numerator has an order-two zero.

## 6. Exact tangent test at the square seed

For `A=X^4-1`, take the exact square face

```text
q_alpha=1,
e_alpha=f_alpha=0,
c2=c6=1,
c14=-6139/2^34,
c18=16369/2^47,
other scheduled modes through c20 zero.
```

It has

```text
rho=9207/2^57
```

at all four roots.  Since

```text
I_A/8=X^5/40-X/8 = -X/10 mod (X^4-1),
```

the seed itself fails the endpoint, as already known.

The new check linearizes all of `(F20)` over the exact root algebra
`Q[X]/(X^4-1)`.  It allows:

```text
delta Q in degrees 0..2,                3 variables,
delta e1, delta F8 modulo A,            4+4 variables,
delta c2,...,delta c20,                 10 variables,
delta gamma,                            1 variable.
```

The result is

```text
20 equations, 22 variables,
rank(J)=13,
rank([J | endpoint target])=14.                         (T)
```

Locally, the four regularity rows have rank three in the three face
variables `(q,e,f)`, while adjoining a unit endpoint change raises the
augmented rank to four.  Thus the square face cannot move infinitesimally
toward the nonconstant primitive class while preserving the four born-mode
compatibilities.

Unlike the earlier raw determinant tangent dual at `(X,t)=(0,8)`, this
obstruction is not merely the differential of a product whose four base
factors all vanish: the local regularity Jacobian has full rank three.  It is
still only a one-point, first-order statement.  Nonlinear branches or other
face points are not excluded.

## 7. Recommended next discriminator

The most direct upgrade is a finite exact injectivity/elimination test for
the face map

```text
u=(q,e,f) -> (B7(u;d),B8(u;d),B9(u;d),B10(u;d),rho(u;d)).
```

There are two useful outcomes:

1. If equality of the four `B_r` values forces equality of `u` on the
   active `c2!=0` locus (possibly after a short exceptional-factor split),
   all four q1 root faces coincide.  Then `(F15)` would force `I_A` to take
   one value at all four simple critical points, which is impossible.
2. If the map has a collision component, freeze its equations and append
   the three primitive differences from `(F15)`.  That component is the
   smallest honest nonlinear survivor, and the next half-step odd face can
   be computed only there.

This is a three-variable local map coupled across four etale components; it
is substantially smaller than another full raw D22 Groebner solve.

## 8. Reproducibility and scope

Checker:

```text
cases/ggv_8_28_upper_endpoint_deep_q1_composition_20260828/
  verify_deep_q1_composition.py
```

Checker SHA-256:

```text
76785c37348a91128bf72b640c4c04130d0b567155e27c0e19a9237085cb0a3e
```

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_deep_q1_composition_20260828/verify_deep_q1_composition.py
```

Expected marker:

```text
PASS_EXACT_DEEP_Q1_COMPOSITION
```

The checker pins the predecessor Newton/kernel verifier, rechecks `(Q1)` and
the shear coefficient, constructs the fractional face recurrence directly,
and performs exact rational elimination for `(T)`.  No AWS or CAS is used.

No full q1 endpoint exclusion, deep-locus emptiness theorem, D23 theorem,
Keller theorem, or proof/disproof of JC2 is claimed.
