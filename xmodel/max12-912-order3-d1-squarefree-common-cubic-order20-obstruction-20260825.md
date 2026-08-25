# D1 squarefree common-cubic order-20 obstruction

Date: 2026-08-25  
Status: **PRODUCER THEOREM; INDEPENDENT REVIEW REQUIRED**

## Charged exact source

```text
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
bdb369f187284df82935488288d3752c4781e527eec1c38da80b757a26f50c38  xmodel/max12-912-order3-d1-isotrivial-strict-rees-saturation-20260825.md
a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md
```

The AWS reconstruction artifacts and their compilers are listed at the end.
The proof below is algebraic; it does not infer a theorem merely from a
sample or a component count.

## Theorem

Work in the exact ordinary isotrivial chart of the strict D1
coefficient-infinity gate.  Put

```text
Lambda=tau^3*rho,       kbar=Lambda^6*k,
r_l=Lambda^(12+l)*gamma_l,
gamma_3=mu, gamma_6=nu, gamma_8=1+tau,
gamma_l=0 otherwise.                                      (1)
```

Let a formal/Puiseux arc have projective common-cubic centre

```text
K_0=z^3+p_0*z+c_0
```

and suppose

```text
Delta_0=-4*p_0^3-27*c_0^2 != 0.                           (2)
```

Then the arc cannot satisfy the eight equations (1).  Equivalently, no
strict D1 coefficient-infinity arc is centred on the squarefree open part
of the reviewed common-cubic boundary.

This is uniform in `k,mu,nu`, including all zero-load strata, and uniform in
the strict slope.  It leaves only the double-root divisor `Delta_0=0` of the
projective common-cubic curve for the parent exact saturation.

Combining this theorem with the independently reviewed common-cubic
reduced-support theorem gives the following set-theoretic endpoint
corollary: if the global strict D1 Rees endpoint is nonunit, then its
projective support is contained in the single weighted-projective
double-root point represented by `(p_0,c_0)=(-3,2)`.  This says nothing about
the local scheme thickness or whether that point actually lifts.

## 1. Exact normal coordinates and the first nonzero map

Along the arc choose the moving depressed cubic

```text
K=z^3+p*z+c
```

from the `z^7,z^6` coefficients, and write

```text
f=K^3+E,       deg_z(E)<=5,       E=K*Q+R,
deg_z(Q)<=2,   deg_z(R)<=2.                              (3)
```

This is polynomial division by a monic cubic, hence an exact coordinate
change over the valuation ring.  The binomial expansions are

```text
f^(4/3)
 =K^4+(4/3)K*E+(2/9)K^(-2)E^2-(4/81)K^(-5)E^3+...,

kbar*f^(2/3)
 =kbar*(K^2+(2/3)K^(-1)E-(1/9)K^(-4)E^2+...).           (4)
```

The polynomial part is the exact Faber polynomial.  Consequently the
ordinary tail map has zero differential at `E=kbar=0`.  Its complete
quadratic normal generating function is

```text
T_2(z)
 =[(4/9)*rem_K(Q*R)/K
   +(2/9)*R^2/K^2
   +(2/3)*kbar*R/K]_- .                                  (5)
```

Here `[-]_-` means the strictly negative Laurent part at `z=infinity`.
Formula (5) is the compact form of all eight AWS-reconstructed quadrics.
It also exposes why the raw tangent cone is thick: directions with `R=0`
are invisible at quadratic order when `kbar=0`.

Let `z_0(w)` be the inverse of `K`, so `K(z_0(w))=w^3`.  A proper numerator
of degree at most two over `K` starts in rows 1--3 after substitution, and a
proper numerator of degree at most five over `K^2` starts in rows 1--6.
More precisely, if `S!=0`, `deg S=d<3j`, then

```text
S(z_0(w))/w^(3j)=lead(S)*w^(d-3j)+lower powers.           (6)
```

Thus its first `3j` tail coefficients determine `S` triangularly.

## 2. Valuation lemma on the squarefree chart

Normalize the rank-one valuation by `v(Lambda)=1` and set

```text
beta=v(Q),       alpha=v(R),                              (7)
```

where the valuation of a polynomial is the minimum valuation of its
coefficients.  Both numbers are strictly positive because the arc is
centred on `f=K_0^3` and `Q,R` are exact normal coordinates.  Here and below
one may pass to a finite residue-field extension without changing a
divisibility conclusion.  We claim

```text
beta>=6,       alpha>=9.                                  (8)
```

The proof is insensitive to a finite residue-field extension, so split the
squarefree cubic `K_0`.  A polynomial of degree at most two cannot vanish at
all three roots of `K_0`.

Suppose first that `beta<6`, and let `Q_0,R_0` be leading coefficient
polynomials.  Terms containing `kbar` occur strictly after their pure
counterparts.  The only candidate leading valuations are

```text
beta+alpha  from Q*R/K,
2*alpha     from R^2/K^2,
3*beta      from Q^3/K^2.                                (9)
```

Comparing these three numbers gives the following exhaustive table.  A
zero target means divisibility by the displayed denominator.  If a leading
valuation is 15, the allowed `r_3` target replaces zero by a scalar multiple
of `K` modulo `K^2`; reducing modulo `K` gives the same root obstruction.

| range | first required congruence(s) modulo `K` |
|---|---|
| `alpha<beta` | `R_0^2=0` |
| `alpha=beta` | `R_0(2Q_0K+R_0)=0`, hence `R_0^2=0` |
| `beta<alpha<3beta/2` | first `Q_0R_0=0`, then `R_0^2=0` |
| `alpha=3beta/2` | `Q_0R_0=0` and `18R_0^2-4Q_0^3=0` |
| `3beta/2<alpha<2beta` | first `Q_0R_0=0`, then `Q_0^3=0` |
| `alpha=2beta` | `Q_0(9R_0K-Q_0^2)=0`, hence `Q_0^3=0` |
| `alpha>2beta` | `Q_0^3=0` |

All congruences in the table are in the reduced algebra
`L[z]/(K_0)`.  The first three and last three rows force `K_0|R_0` or
`K_0|Q_0`, impossible by degree.  In the middle row, at every root
`Q_0R_0=0`, while the second equation forces both values to be zero; again
both degree-two polynomials would vanish at all three roots.

There is one apparent target coincidence not encoded by simply writing
zero in the table: `beta+alpha=15` in the range
`3beta/2<alpha<2beta`.  It forces `5<beta<6`; the next term `Q_0^3/K_0^2`
then has valuation strictly between 15 and 18 and must vanish.  Hence
`K_0|Q_0`, the same contradiction.  The coincidences `3beta=15` reduce
modulo `K_0` to `Q_0^3=0` and are equally impossible.  This proves
`beta>=6`.

Now suppose `alpha<9`.  Since `beta>=6`, at valuation `2alpha<18` the only
term over denominator `K_0^2` which survives reduction modulo `K_0` is
`R_0^2`.  Any simultaneous term over `K_0` acquires a factor of `K_0` after
putting it over `K_0^2`.  A possible valuation-15 target is a scalar
multiple of `K_0` and also vanishes modulo `K_0`.  Therefore

```text
R_0^2=0 in L[z]/(K_0),
```

so squarefreeness gives `K_0|R_0`, again impossible by degree.  This proves
(8).

Equivalently, the only division used here is the implication
`X^n=0 => X=0` in the squarefree residue algebra.  No irreducibility of
`K_0` is assumed: after a finite splitting extension the algebra is a
product of three fields, and every displayed product equation is checked
componentwise.  This is exactly the step that fails at the double-root
point.

## 3. The order-20 obstruction

Under (8), every negative term of valuation at most 20 in (4) is contained
in exactly two layers:

```text
M=(2/9)*(2Q+3kbar)*R/K,                                  (10)
N=(1/81)*(18R^2-9kbar*Q^2-4Q^3)/K^2.                    (11)
```

The next terms are `Q^2R/K^3` and `kbar*Q*R/K^3`, both of valuation at
least 21; all remaining terms are later.  Let `z(w)` be the exact inverse
root of `f`, `f(z(w))=w^9`.  Linearizing
`K(z)^3+E(z)=w^9` at the moving inverse `z_0` shows that
`z(w)-z_0(w)` has coefficient valuation at least six (the Laurent-leading
coefficient of `3K^2K'` is a unit).  Substituting the exact inverse into a
layer of valuation at least 15 therefore changes nothing through valuation
20.

Perform the polynomial remainders over the valuation ring using the
**moving** monic cubic `K`, not its residue specialization.  Put the two
proper layers over their common denominator.  Through valuation 20 they
have the exact form

```text
S(z_0(w))/w^6,       deg_z(S)<=5,                        (12)
```

because `K(z_0(w))=w^3` identically.  Thus arbitrary regular motion of
`p,c` introduces no extra denominator and requires no finite jet bound.
The valuation-15 and valuation-18 targets themselves are exactly

```text
(mu*Lambda^15*K+nu*Lambda^18)/K^2
```

after evaluation at `z_0`.  Subtract this moving numerator from `S`.
Triangularity (6), applied coefficient-by-coefficient over the valuation
ring, says that the zero rows through valuation below 20 force every lower
initial numerator to vanish; no derivative of the moving `K` can re-enter.

The exact targets (1) then have zero valuation-20 initial form in rows 1--7:
rows 3 and 6 occur only at valuations 15 and 18.  But row 8 has the nonzero
initial form of

```text
Lambda^20*(1+tau),
```

because `v(tau)>0`.  By the triangular observation (6), vanishing of even
the first six tails in (12) forces `S=0`, so its eighth tail is also zero.
This contradicts the row-8 target and proves the theorem.

The load weights used in this paragraph are exactly
`v(kbar)=6`, `v(mu*Lambda^15)=15`,
`v(nu*Lambda^18)=18`, and
`v(Lambda^20*(1+tau))=20`; the last leading coefficient is one.  Thus the
argument neither sets a load to a generic number nor divides by a load.

## 4. Exact leading system and composition control

At equality in (8), write

```text
Q=Lambda^6*Q_0+...,
R=Lambda^9*R_0+....                                      (13)
```

The entire initial system is the pair of polynomial congruences

```text
(2Q_0+3k)R_0 = (9/2)mu                 mod K_0,          (14)
18R_0^2-9kQ_0^2-4Q_0^3 = 81nu          mod K_0^2.        (15)
```

There are no other nonzero tail weights at most 20 before corrections.
The independent AWS extraction reproduced all eight coefficient rows of
(14)--(15) exactly.

The constant solution `Q_0=B,R_0=A` is the cubic-composition locus.  On it

```text
r3=(2/9)A(2B+3k),
r6=(2/9)A^2-(1/9)kB^2-(4/81)B^3,
r1=r2=r4=r5=r7=r8=0.                                   (16)
```

In the four transverse coordinates given by the nonconstant coefficients
of `Q_0,R_0`, the Jacobian of `(r1,r2,r4,r5,r7)` has rank four precisely
off

```text
D=B(2B+3k)^2+12A^2=0.                                   (17)
```

Indeed the minor omitting row 7 is exactly

```text
(16/59049)*D^2,                                          (18)
```

independent of `p,c`; the other four minors are `D^2` times the displayed
simple factors in the frozen AWS artifact.  Notice that `D` is, up to a
nonzero scalar, the Jacobian determinant of the load map `(A,B)->(r3,r6)`.

For navigation inside (14)--(15), write
`Q_0=q2*z^2+q1*z+q0`.  The exact equations imply

```text
q2^2*q1=0.                                               (19)
```

If `q2=0`, successive rows force `R_0` and `Q_0` to be constant, recovering
(16).  If `q2!=0`, then `q1=0`.  On the symbolic interior `c_0!=0`, direct
coefficient comparison in (14)--(15) gives

```text
c_0^2+3p_0^3=0,
q0=2p_0*q2,                 k=-(4/3)p_0*q2,
r0=p_0*r2,                  r1=-(c_0/p_0)r2,
r2^2=(2/9)p_0*q2^3,
mu=-(4/3)p_0^2*q2*r2,       nu=(8/81)p_0^3*q2^3.         (20)
```

This special leading branch is still squarefree: its cubic discriminant is
`77p_0^3`, so the order-20 theorem excludes its lift.  The `c_0=0,p_0!=0`
axis can retain a larger leading conic, but it too is squarefree and is
excluded without decomposing that conic.

## 5. Remaining chart and firewall

The proof uses reducedness of `L[z]/(K_0)` in the valuation lemma.  It does
**not** cover

```text
Delta_0=0,       (p_0,c_0)!=(0,0),                       (21)
```

where `K_0` has a double root.  Divisibility can then conceal a lower-order
normal term.  The triple-root depressed cubic is only `K_0=z^3`, the
irrelevant projective origin, so (21) is the sole projective survivor.  Over
an algebraic closure it can be parameterized as

```text
K_0=(z-a)^2*(z+2a),       p_0=-3a^2, c_0=2a^3, a!=0,
```

and normalized to one weighted projective point.  Thus the clean successor
is an exact double-root-chart Newton/saturation calculation, not the full
global Rees basis.

The concealment is real, not merely a missing proof technique.  At the
normalized double-root point

```text
K=(z-1)^2*(z+2),       Q=(z-1)*(z+2),       R=1/3,
Q*(9*R*K-Q^2)=-K^2.                                      (22)
```

Hence the leading `alpha=2*beta` numerator which forced `Q_0^3=0` after
squarefree reduction can instead be an honest polynomial at `Delta=0`.
Identity (22) is a negative control for extending the theorem across the
firewall; it is not by itself a formal arc.

No fixed finite jet has been asserted for that remaining chart.  Nothing
here proves access to a rational section, handles finite coefficient load,
handles D2 or another passport, or proves JC2.  Promotion requires an
independent proof review of the valuation table, the inverse-substitution
cutoff, and the exact row-8 target.

## AWS evidence and reproducibility

All substantive executions ran on Box03 `98.80.65.144` under the registered
job directories in
`cases/max12_912_order3_d1_normal_tangent_20260825/PREREGISTRATION.md`.
The local frozen artifacts are:

```text
45e0ac6715d95a41c5abb7e06d63c8dba026bcc46df0a6f21bfed724589189c5  aws_box03_v1/normal_tangent.stdout
0174eb6dd773b8c9c50d7c687ec19954e352a3242e7e7b19f4facdd14b31e008  aws_box03_v1/composition_jacobian.stdout
89509ae78d20f2bd8d1ddc3c03efcec5ee7ed256a0498c396ea1b9ac22344356  aws_box03_v1/composition_jacobian_factors.stdout
b48856259616b55738f19bdf9fa2422e932fddb500321da3a8145d5890a6c1ad  aws_box03_v1/weight20.stdout
3014446bcd826b0533bdacafb3b90ff36a86f747caaf1a48ba9f8702baf3006f  aws_box03_v1/general_leading.stdout
3ad230cda1ba83f21af53d5f4c4a698a595caddc4474396bd2574de8e5a4e462  aws_box03_v1/firewall_controls.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_v1/firewall_controls.stderr
```

Compiler hashes:

```text
401fb0754bee9a752447fc84438fc1fb2adfc6531ff995fcc32a029881da0578  derive_normal_tangent.py
e91c4ce34d110434239a667214d6591f6a91b64e2dadd5012bd9d83d2d4ce992  derive_composition_jacobian.py
c5212be95498fba41e66e5924e44f09ca88e310e5d006d588e788ba40f0a3f97  derive_weight20_gate.py
61b855a86bb276454df910e7e8c97eeff5c3fb37adc28c7872d545d502f5083f  derive_general_leading.py
202cc9895216ca8c3dd741de6339bded1413939d4c0b62e8707a19428757db8c  verify_firewall_controls.py
```

The last control independently verifies: the lower-triangular unit-diagonal
map from `deg S<=5` over `K^2` to its first six tails; the sharp omitted-layer
example `z/K^3`, whose first nonzero tail is exactly row 8; the double-root
identity (22); and direct binomial enumeration showing that every negative
layer through weight 20 is (10)--(11), while denominator power three first
appears at weight 21.  Its terminal marker is
`PASS-D1-SQUAREFREE-ORDER20-FIREWALL-CONTROLS`.
