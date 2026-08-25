# AS F-only `p=3,D=7`: exact degree-ten pointwise gate

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE REVIEW.**

## Headline

On the reviewed aligned deep branch, retain the original nonreduced
divided-carry predecessor.  After exact linear elimination, the next
degree-ten mixed-carry equations are an affine system

```text
A(base) xi + beta(base) = 0,       A is 8 by 9.             (1)
```

The field-valued rank and compatibility strata are now exact:

- rank zero is exactly the degree-five-zero vertical component;
- every nonzero degree-five point has rank three;
- ranks one, two, and four do not occur;
- the vertical component is compatible;
- on the nonzero rational-normal-cone component, compatibility has exactly
  two reduced endpoint branches.

Equivalently, the generic cone point is killed by the degree-ten row, but a
vertical component and two endpoint rays survive.  This is a scoped
pointwise gate, not emptiness of `D=7` and not a lift or JC2 statement.

## 1. Reviewed input and exact integer orientation

The consumed predecessor is

```text
xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md
SHA-256 cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194
```

Its different-model hostile review is **CONFIRMED**:

```text
xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-review-grok-20260824.md
SHA-256 4e915fb6f7e8701d1932b2b28df76db35859520bc94ffe8fb08a1cd679936ae8
```

The earlier 29-row predecessor remains quarantined.  No statement below
uses it.

Over the integers write

```text
P = x-x^3 + 3U + 9C,
Q = y     + 3V + 9D.
```

With

```text
L = U_x+V_y-x^2,
K = (U_x-x^2)V_y-U_yV_x,
M = (U_x-x^2)D_y+C_xV_y-U_yD_x-C_yV_x,
N = C_xD_y-C_yD_x,
```

direct expansion gives

```text
det J(P,Q)-1 = 3L + 9(K+C_x+D_y) + 27M + 81N.   (2)
```

The reviewed predecessor imposes the source-honest divided first residual,
including the missing `L/3` Cartier row.  For the present top calculation,
`C_7,D_7` first solve the seven total-degree-six coefficients of
`K+C_x+D_y`.  The only total-degree-ten term of the following residual is
then `M_10`: the preceding divided quotient has degree at most eight, lower
second-digit layers reach degree at most nine, and `81N/27` vanishes modulo
three.  This fixes the orientation and the right-hand side of (1).

## 2. Exact source compression; no radicalization

The confirmed predecessor has 40 displayed variables and 30 rows:

```text
14 first-divergence rows
 9 quadratic carry rows in degree 8
 6 quadratic carry rows in degree 7
 1 divided-linear Cartier row
```

The ten degree-one/two variables occur only in three independent linear
divergence rows.  Solving those rows gives an exact independent `A^7`
factor.  Four further degree-three coefficients are invisible to this gate.
The only relevant degree-three parameter is

```text
h=u3_2,   u3_1=0,   v3_1=2h,   v3_2=1.          (3)
```

For degree four set

```text
p=u4_0, q=u4_3, r=v4_0, s=v4_1, t=v4_3, w=v4_4,
u4_1=2r, u4_2=v4_2=0, u4_4=2t.                 (4)
```

For degree five, divergence plus the divided-linear Cartier row give

```text
a=u5_0,
b=u5_1=v5_0,
c=u5_2=v5_1,
d=u5_3,       v5_2=2d,
e=u5_4=v5_3,
f=u5_5=v5_4,
g=v5_5.                                            (5)
```

After these invertible linear eliminations the nonreduced predecessor is the
ideal `H` in

```text
F3[h,p,q,r,s,t,w,a,b,c,d,e,f,g]
```

with the following fifteen rows:

```text
ac+2b^2, ad+bc, 2bd+2c^2,
af+be+cd, 2ag+bf+ce+d^2, bg+cf+2de,
df+2e^2, 2dg+ef, eg+2f^2,

as+2br+2cp,
2bs+cr+2dp,
aw+2bt+2cq+ds+2er+2fp,
2bw+ct+2dq+2es+fr+gp,
dw+2et+2fq,
2ew+ft+gq.                                      (6)
```

The construction is an isomorphism, not a reduction to `sqrt(H)`:

```text
full 40-variable predecessor = A^11 x Spec(H),
dim(H)=7,
reduced Groebner size(H)=254,
radical Groebner size=29.
```

Here `A^11=A^7 x A^4` accounts for the omitted low layer and the four
irrelevant degree-three coefficients.  The six reviewed degree-six
Frobenius coefficients remain an additional `A^6` factor.  Their integer
derivatives are multiples of three: a single cross term can reach only
degree nine, while a double degree-six cross term at degree ten is divisible
by nine and is zero after the relevant division modulo three.  Thus none is
silently removed from (1).

Exact `minAssGTZ` on the thirteen-variable high ideal (drop the free `h`)
returns two dimension-six minimal primes:

- the vertical prime `P_v=(a,b,c,d,e,f,g)`;
- a 29-generator rational-normal-cone incidence prime `P_m`, printed in the
  replay.

This decomposition describes field support.  The Fitting calculation below
still starts from nonreduced `H`; the radical and the two primes never
replace it.

## 3. The degree-ten matrix

Solving the seven degree-six accepted-divergence rows leaves

```text
xi=(c7_0,c7_3,c7_6,d7_0,d7_1,d7_3,d7_4,d7_6,d7_7).
```

In the normal form (3)--(5), the coefficient matrix in (1) is

```text
[2c  0   0  2b  a   0   0   0   0]
[2d  0   0   c  2b  0   0   0   0]
[2f  2c  0  2e  d   2b  a   0   0]
[ g  2d  0   f  2e   c  2b  0   0]
[ 0  2f  2c  0   0  2e  d   2b  a]
[ 0   g  2d  0   0   f  2e   c  2b]
[ 0   0  2f  0   0   0   0  2e  d]
[ 0   0   g  0   0   0   0   f  2e].          (7)
```

The eight entries of `beta` are printed deterministically by
`generate_reduced_pointwise.py`.  They retain `h` and every relevant
degree-four variable.  The system is not replaced by a module-membership
test: pointwise compatibility is decided by augmented minors on every rank
stratum.

## 4. Complete field-valued rank/Fitting classification

Let `Z5=(a,b,c,d,e,f,g)`, `A_i` denote the ideal of `i`-minors of `A`, and
write `Aug=[A|beta]`.

The replay proves, over the original nonreduced `H`,

```text
I_1(A) = Z5,                                      (8)
I_4(A) = 0 modulo sqrt(H),                        (9)
(H+I_3(A)) : Z5^infinity = (1).                  (10)
```

Consequently rank zero is exactly the vertical component, every nonzero
degree-five field point has rank exactly three, and ranks one, two, and four
are absent.

On the vertical component, `beta=0` exactly, so (1) is compatible.  On the
nonzero rank-three locus the exact compatibility ideal is

```text
J = (H+I_4(Aug)) : Z5^infinity.                  (11)
```

It has Groebner size 53 and dimension six.  Only now, to describe its
field-valued support, take its radical.  The two-sided replay gives

```text
sqrt(J) = C_a intersect C_g,                     (12)

C_a=(b,c,d,e,f,g,s,w),
C_g=(a,b,c,d,e,f,p,q).
```

Both ideals have dimension six (including free `h`).  The two standard cone
charts independently recover (12):

```text
a != 0:  b=az,c=az^2,d=2az^3,e=2az^4,f=2az^5,g=2az^6,
          s=pz^2+rz, w=tz+qz^2,  compatibility ideal (z);

g != 0:  f=gz,e=gz^2,d=gz^3,c=2gz^4,b=2gz^5,a=2gz^6,
          p=sz^2-rz, q=wz^2-tz,  compatibility ideal (z^3).
```

The second chart records genuine nonreduced multiplicity, but its field
support is `z=0`.  If `a=g=0` on the cone, the cone equations force all of
`b,...,f` to vanish, so these two charts cover every nonzero field point.

Thus the complete pointwise outcome of this gate is:

```text
vertical: a=...=g=0                         survives;
a endpoint: b=...=g=0 and s=w=0             survives D10;
g endpoint: a=...=f=0 and p=q=0             survives D10;
every other nonzero cone point               fails D10.       (13)
```

No global polynomial section is asserted or required.

## 5. Integer controls and the next boundary

The integer replay reconstructs three points before interpreting the
Fitting result.  In every case `P=x-x^3+3U+9C`, `Q=y+3V+9D` has
`det J(P,Q)=1 mod 27` and zero degree-ten next residual.

The vertical and `g`-endpoint points extend one complete digit further within
cap seven.  Modulo 81 they are

```text
P = x-x^3+18x^5+54x^7,
Q_vertical = y+3x^2y,
Q_g        = y+3x^2y+3x^5.                    (14)
```

For both maps the literal integer determinant is

```text
1 + 81x^4 + 648x^6 + 1134x^8,
```

so it is exactly `1 mod 81`.  These are finite-precision controls only.

The `a` endpoint is a useful negative control:

```text
U=y^5,
V=x^2y,
C=2x^5+2x^2y^5,
D=0.
```

Its next residual divided by 27 is, modulo three,

```text
x^6 + xy^5 + 2x^3y^5.                          (15)
```

It passes the degree-ten row, but the degree-eight term `2x^3y^5` cannot be
hit by the divergence of a cap-seven next digit.  Thus it is not promoted to
a full mod-81 survivor.  This also demonstrates why (13) must not be called a
complete next-digit classification.

## 6. Scope and refusal ledger

This producer proves only the degree-ten pointwise gate on the reviewed
aligned deep `p=3,D=7` branch.  It retains the predecessor's nonreduced
structure and uses radicals only for field-support descriptions after the
Fitting ideals are formed.

It does **not**:

- solve every lower row of the following carry for the whole survivor locus;
- classify other associated-top branches or the full `D=7` scheme;
- prove that the vertical or `g` controls continue to arbitrary depth;
- prove a polynomial, restricted-analytic, or characteristic-zero lift;
- prove a no-lift theorem, a counterexample, or any JC2 implication.

The smallest successor is to attach the remaining next-carry rows to the
vertical and `g` endpoint branches, reconstruct every surviving digit over
the original integer expansion, and only then attempt the following depth.

## 7. Replay

From `cases/as_fonly_d7_degree10_pointwise_20260824/`:

```sh
python3 audit_source_compression.py
python3 replay_degree10_controls.py
Singular -q audit_high_radical_components.sing
Singular -q audit_pointwise_static.sing
python3 generate_reduced_pointwise.py | Singular -q
python3 audit_main_a_chart.py | Singular -q
python3 audit_main_g_chart.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

The static one-command Fitting/radical replay is
`Singular -q audit_pointwise_static.sing`; the independently generated
source replay is `python3 generate_reduced_pointwise.py | Singular -q`.
Each takes about 75 seconds on the producer host.  No AWS, rectangular search, random
sampling, floating point, or external solver is used.
