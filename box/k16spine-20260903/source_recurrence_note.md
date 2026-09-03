# Source audit and recurrence note: K=16 middle spine

Status: exact structural identities and a split-safe Laurent/Euler second
spine are proved below for `t>=2`; the terminal inconsistency is not proved
uniformly here.  The banked `t=1` calculation is a separate exact base case.
This note does not use any in-progress lane named in the task.

## 0. Frozen-source check and conventions

The receipt
`xmodel/k16-middle-spine-sol56-20260903.run.v2` was parsed mechanically: its
`charged_input_<i>_basename` and `charged_input_<i>_sha256` fields were joined
with `awk` and passed to `sha256sum -c`.  All fifteen files in
`/tmp/jc2-lane.jRo7RD/inputs` returned `OK`.

Put

```text
e=3t+1, q=2t+1, z=pi-gamma,
B=pi*z+b1*pi+b2, A=pi*B+b3, h=pi*A+b4.
```

These are the charged definitions and degrees
(`k16-uniform-structure-sol56-20260903.md:34-85`).  The exact raw band
identity is

```text
R_k = sum_(e+q-i-j=k) J(beta_j,alpha_i)
    + sum_(e+q-i-j-1=k)
        ((e-i)alpha_i J(beta_j,h)+(q-j)beta_j J(h,alpha_i)),
F_k=R_k+C_k=h C_(k+1)+N_k,
```

with monic division by the quartic `h`; no parameter leader is divided
(`k16-t3-uniform-sol56-20260903.md:125-145`).  The frozen builder implements
exactly this identity and orders its variables as `b1,...,b4`, then the
`alpha` coordinates by increasing deficit/basis position, then the `beta`
coordinates in the same manner
(`t_order_system.py:37-50,54-88,90-140`).

The first constant spine consists of `3t+4` pivots: the `A` coordinates of
`alpha_i`, `t+1<=i<=e`, with coefficient `q`; the `B` coordinates for
`2t+1<=i<=e`, with coefficient `2q`; and the two endpoint reductions.  It is
triangular from band `4t+1` through `2t`
(`k16-t3-uniform-sol56-20260903.md:346-401`).

After the `x=1` slice, write `y=beta_(q),B`.  The charged normalizer gives

```text
H_t=12q^2 y^2-12q(t+1)y+(t+1)(3t+2),
c=t(3t+1)y((t+1)-6qy)/(6q^3).
```

See `k16-uniform-structure-sol56-20260903.md:219-257`.  Put

```text
a=t+1,                 d=2qy-a.
```

Then, exactly,

```text
H_t=3d^2-a,
Res_y(H_t,A*d+B)=4q^2(3B^2-A^2*a).                 (0.1)
```

Thus `A_t=Q[d]/(3d^2-a)`.  At a split integer
`t=3s^2-1`, it is the product algebra obtained by evaluation at `d=+s` and
`d=-s`; a factor which vanishes on either component is never inverted.  The
split set and the product-algebra warning are charged at
`k16-uniform-structure-sol56-20260903.md:268-310,525-550`.

## 1. Compact exact band equations

After the constant spine, group the surviving expression as

```text
Q=U(X)+A R(X)+yB,
P=V(X)+A S(X)+B T(X)+g z,       L=X-b4,              (1.1)
```

where `g=g3`.  Direct expansion and monic reduction give

```text
C12=-RT+L(RT'-2R'T+2yS')+yS-b3(gR'+yT')-3gU',
C11=-2gR+L(2yT'-3gR'),

C00=L^2(R'S-RS')
   +L[b3(R'T-yS')+2b2(gR'-yT')+2TU'-2yV']
   +g*b3^2*R'+g*b2*R+g*b3*U'+b1*g*y,                (1.2)

C01=(b3*y-LR)V'+(LS-b3T-b2g)U'+g*y
     -b2*C12-b1*C11,
C03=-C12,
C02=-b1*C12-C11,
C10=-yg.                                             (1.3)
```

The independent-symbol verification is
`box/k16spine-20260903/compact_remainder.py:21-90`.  It is a polynomial
identity, not interpolation.

The degree supports in (1.2)-(1.3) give, after `H/c`, five tags
`12,11,02,01,00` at bands `0,...,t-1`, four tags
`12,02,01,00` at bands `t,...,2t-1`, and tags `01,00` at band `2t`.
Therefore there are exactly `9t+2` rows.  After the `C12` and `C11`
coefficients have vanished in descending degree, (1.3) gives

```text
[L^k]C02=-b1[L^k]C12-[L^k]C11=0,
```

for every `0<=k<2t`.  This proves the `2t` zero-row recurrence.  Before this
count, the `2t` `C03` rows are exact duplicates of the `C12` rows.  This is
the all-`t` explanation of both observed duplicate phenomena.

## 2. Historical side-first coordinate order

For comparison with the fixed exact objects, the deterministic side-first
order is:

```text
band 2t:  tag 01 -> a_(2t+1),0; tag 00 -> a_(t+1),0;
band k=2t-1,...,0:
  tag 12 -> q_(e-k),1 if k>t, and q_(2t-k),0 if k<=t;
  tag 11 -> a_(t-k),0 if 1<=k<t, and q_q,0 if k=0;
  tag 00 -> a_(e-k),0, except b2 at k=t and b1 at k=0.
```

This is `1+(2t+1)+2t+t=5t+2` candidate pivots and leaves

```text
b3,b4,q_2,0,...,q_(t-1),0.                           (2.1)
```

Its exact Schur factors at the normalized homogeneous origin include, up to
nonzero rational associates,

| position | factor in `d` | raw resultant from (0.1) |
|---|---|---|
| top `01` | `1` | `1` |
| high `00`, band `t+s` | `d+s` | `4q^2(3s^2-a)` |
| high `12`, `t<k<2t` | `d` | `-4q^2 a` |
| band-`t` `12` | `3d+1` | `-12q^2(3t+2)` |
| band-`t` `00` | `2d+1` | `-4q^2(4t+1)` |
| low `00`, `0<k<t` | `y` | `a(3t+2)` |
| band-zero `11` | `3d+2a` | `12q^2 a(4t+1)` |
| band-zero `00` | `5d+2t+3` | `4q^2(3t+2)(4t+1)` |

The primitive `4y-1=(2d+1)/q` has resultant `-4(4t+1)`; rational
rescaling accounts for the table's displayed raw resultant.

This strict order is not split-safe: if `t=3s^2-1`, its factor `d+s`
vanishes on the `d=-s` component.  At `t=2` the exact safe order defers the
candidate `5y-1`; the later pivot `39y-10` has resultant `-3696`.  There is
one such obstruction on every split fibre, not a finite exceptional set.
The historical lower `t` tag-`12` factors, `t-1` tag-`11` factors, and the
general deferred split replacement do not have a proved closed formula in
this coordinate order.  The Laurent order below avoids all of them.

## 3. Laurent/Euler proof order and exact isomorphism

Set `p=pi`.  The charged tower gives Laurent identities

```text
A=L/p,
B=L/p^2-b3/p,
z=-b1-b2/p-b3/p^2+L/p^3.                              (3.1)
```

This is identity calculus, not localization of the solution set.  The map
from the polynomial chart into the Laurent ring is injective; after a
Laurent identity is proved, multiply by a sufficient power of `p`.  No
`p=0` branch is discarded.

Writing

```text
Q=U+Q1/p+Q2/p^2,             Q1=LR-yb3, Q2=yL,
P=P0+P1/p+P2/p^2+P3/p^3,
P0=V-gb1, P1=LS-b3T-gb2, P2=LT-gb3, P3=gL,           (3.2)
```

and using `J(X,p)=-p^3`, coefficient comparison is equivalent to five
polynomial identities.  The top identity is `c=-yg`.  The next gives

```text
R=LC,
T'=(g/(2y))(5C+3LC').                                 (3.3)
```

The constant term first gives `R(0)=0`; only then is division by `L` used.
Here `g` and `y` are units because `c=-yg` is a unit.  The next identity is
the Euler equation

```text
y(1+2L*d/dL)S
 =3gU'+RT-LRT'+2LR'T+g*b3(R/L+5R'/2).                (3.4)
```

On `[L^m]S` its diagonal is `(2m+1)y`, a unit.

The next Laurent coefficient determines `P0'=V'` after its numerator has
been divided by `2yL`.  Divisibility at `L=0` solves `b1` with coefficient
`yg=-c`.  Its integration constant is uniquely chosen so that the scalar
part `V(h)` has zero constant, as required by the endpoint gauge.  The
missing `alpha_t` coefficient is equivalently
`[h^(q-1)]P0'=0`; this solves the integration constant `T(0)` in (3.3) with
coefficient `q/y`.  Consequently (3.3), (3.4), and this `P0'`
reconstruction give mutually inverse triangular maps between the old
post-first-spine coordinates and

```text
U=h^q+sum_(i=2)^(2t) q_i h^(q-i),
C=h^(t-1)+sum_(j=1)^(t-1) C_j h^(t-1-j),
T(0), b1,b2,b3,b4.                                    (3.5)
```

The reconstructed leading coefficients are not assumed.  They follow from

```text
(3t+2)g-2t*y*g2=-t(3t+1)H_t/(6q^3),
3qg+(t+1)g2=(4t+1)y*g1,
2qg2-tg1=2e*y.
```

Thus (3.3) has leading coefficient `g2`, (3.4) has leading coefficient
`g1`, and the reconstructed `V'` starts with `e h^(e-1)`.

This point is needed for the count: (3.3)-(3.4) alone do not visibly contain
the old scalar `V` variables; the `P0'` reconstruction is part of the
quotient-ring isomorphism.  The displayed parameterization has `3t+3`
variables versus the original `6t+2`, hence has removed `3t-1`.  Solving
`b1` and `T(0)` removes two more.

The last independent Laurent equation is

```text
E=(b3*y-LR)V'+(LS-b3T-b2g)U'+g*y=0.                  (3.6)
```

Its coefficients in descending degrees `4t,...,2t` eliminate consecutively

```text
C_1,...,C_(t-1), q_t,...,q_(2t), b2.                 (3.7)
```

There is one new variable of positive weight in each position.  Its
coefficient has weight zero, hence lies in `A_t` and cannot depend on a
positive-weight residual variable.  Thus its derivative at the homogeneous
origin is its exact nonlinear affine pivot, not merely a tangent test.

## 4. Closed Laurent pivot formulas and norms

For `1<=j<=t-1`, put

```text
A_C=9j^2t+18j^2-54jt^2-81jt-26j
    +72t^3+144t^2+88t+16,
B_C=-9j^2t-10j^2+24jt^2+33jt+10j
    -12t^3-20t^2-8t,
L_C=A_C*d+B_C.                                        (4.1)
```

The exact pivot is

```text
p_C=3t(3t+1)L_C/((t+1)(3t+2)^3(4t-2j+1)).           (4.2)
```

Writing `n=t-j`, its core norm is

```text
3B_C^2-a A_C^2=-(3t+2)^3 F_C,
F_C=3n^4+24n^3t+42n^3+66n^2t^2+146n^2t+119n^2
   +72nt^3+238nt^2+234nt+104n
   +27t^4+134t^3+223t^2+136t+32.                    (4.3)
```

Every coefficient of `F_C` is nonnegative and the final constant is
positive for `t>=2,n>=1`; hence all `C_j` pivots are units, also in every
split product algebra.

For `t<=j<=2t`, put

```text
A_Q=12t^2+16t+4-j(3t+4),
B_Q=2(t+1)(j-t),
L_Q=A_Q*d+B_Q.                                        (4.4)
```

Then

```text
p_Q=-3t(3t+1)(q-j)L_Q/
     ((t+1)q(3t+2)^2(4t-2j+1)),                      (4.5)

3B_Q^2-a A_Q^2=-(t+1)(3t+2)^2 F_Q,
F_Q(t,q-n)=n^2+4nt+6n+4t^2-3,  1<=n<=t+1.           (4.6)
```

The last expression is positive.  At `j=t`, (4.5) reduces to a nonzero
rational associate of `d`; no special branch is hidden.  The final `b2`
pivot is

```text
p_b2=g*d/(2y) ~ L_2=3q*d+(t+1),
Res_y(H_t,L_2)=-12q^2(t+1)(3t+2)(4t+1).              (4.7)
```

Therefore all `2t+1` pivots in (3.7) are units.  Together with the
`3t-1` reconstruction pivots and the two `b1,T(0)` pivots, this is

```text
(3t-1)+2+(2t+1)=5t+2                                (4.8)
```

split-safe affine eliminations for every `t>=2`.  The symbolic derivation is
checked in `box/k16spine-20260903/laurent_pivot_formulas.py`; exact Laurent
records at `t=2,3,4` reproduce every factor.

## 5. Generating series, terminal family, and honest residual

The top face has

```text
F(Z)=1+Z+yZ^2,      G(Z)=F(Z)^(e/q)=sum_(n>=0) g_n Z^n,
q(n+1)g_(n+1)=(e-qn)g_n+(2e-q(n-1))y g_(n-1).        (5.1)
```

This follows from `qFG'-eF'G=0`; the charged first coefficients and `H_t`
are in `k16-uniform-structure-sol56-20260903.md:169-243`, and the frozen
symbolic checks are `uniform_binomial_identities.py:13-76`.  The relation
`H_t=0` is `g4=0`.  Since `2e-3q=-1`,

```text
g5=-y*g3/(5q)
  =-t(t+1)(3t+1)(5d+2t+3)/(60q^5),                  (5.2)
```

so `g5` is a unit by (0.1).  It explains the band-zero scalar pivot.  It does
not by itself identify the entire terminal ideal with a single coefficient
`g_N`: the exact middle equation (3.6) still contains `U,V,R,b3,b4`.

Let `sigma_t` denote the substitutions (3.3)-(4.7).  The exact closed
terminal family is

```text
T_(t,k)=[X^k] sigma_t(E),       0<=k<2t,              (5.3)
```

in

```text
A_t[b3,b4,q_2,...,q_(t-1)].                           (5.4)
```

It has `2t` rows in `t` variables, bands `0,...,2t-1`, and weighted degrees
`4t+1,...,2t+2`.  Formula (5.3) is executable and uniform, but this note does
not prove that its ideal is `[1]` for arbitrary `t`.  In particular, proving
that every nonconstant term in `T_(t,0)` is divisible by `b4` would make the
`b4=0` branch contradict the unit (5.2); that divisibility is known in the
small records but remains a separate all-`t` statement.  On `b4!=0`, weighted
normalization still leaves a growing `(2t-1)`-row system in `t-1` variables.

Thus the second affine spine and the duplicate/zero recurrence are closed;
the precise remaining theorem is

```text
for every t>=2,  <T_(t,0),...,T_(t,2t-1)> = <1>
in A_t[b3,b4,q_2,...,q_(t-1)].                        (5.5)
```

The cheapest exact test at a fixed split `t=3s^2-1` is to evaluate (5.3)
separately at `d=+s` and `d=-s`; off the split set, compute in the quadratic
field.  Never invert a componentwise zero factor.

## 6. Denominators and controls

The normalizer uses only `6q^3`; the leading coefficient of `H_t` is
`12q^2`.  These have no positive integral roots.  The Euler steps additionally
use positive rational integers, `y`, `g`, `yg=-c`, and `q/y`, all units by
the charged `c`-unit proof.  Formulas (4.2), (4.5) use only the positive
integer factors

```text
t, t+1, q, 3t+1, 3t+2, 4t-2j+1,
```

and their actual coefficient-algebra inversions are justified by the
nonzero norms (4.3), (4.6), and (4.7).  Any final generic certificate must
also include the still-unknown terminal-certificate denominators.  It would
be incorrect to announce a complete global `D(t)` before (5.5) is proved.

The exact low-level control

```text
Q=h^q+B, P=h^e+2pi-gamma, c=-1
```

satisfies levels `0,...,2t-1` and fails at `2t` and `3t+1`, exactly as charged
at `k16-t3-uniform-sol56-20260903.md:420-457`.  Hence no fixed low-band
shortcut replaces the moving recurrence.  The formulas above specialize at
all positive integers because every stated rational denominator and every
stated norm is nonzero; the separate `t=1` base case remains the banked exact
audit.
