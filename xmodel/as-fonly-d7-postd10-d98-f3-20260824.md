# AS F-only `p=3,D=7`: post-D10 degree-nine/eight F3 gate

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE REVIEW.**

## Headline

On the different-model-confirmed vertical and `g`-endpoint survivors of the
degree-ten gate, the next high rows admit a small exact compilation.

1. On the vertical branch, every degree-nine row has a global polynomial
   section.
2. The vertical degree-eight problem reduces by six source-typed constant
   pivots and an invertible triangular coordinate change to a `7 x 5`
   polynomial matrix.  Its only geometric ranks are `0,2,3,5`; ranks `1,4`
   do not occur.
3. Exhausting all `3^11=177147` literal F3 predecessor-digit points of that
   core leaves `50939` compatible points.
4. On the `g != 0` endpoint, the degree-ten pivots and two degree-nine rows
   first force `f_c=f_d=0`.  The remaining exact `13 x 14` system has `954`
   compatible points among all `4374` literal F3 assignments.

The exhaustions are exact for the actual F3 digit set.  They are **not** an
algebraic-closure/Fitting classification of compatibility, do not advance a
survivor through the next divided carry, and do not prove or disprove any
all-depth lift, characteristic-zero statement, or JC2.

## 1. Licensed input and integer orientation

This gate consumes the confirmed degree-ten producer

```text
xmodel/as-fonly-d7-degree10-pointwise-20260824.md
SHA-256 e4311a80aef2d3617c7b449e16cb19d34cfe25d31c558bb68f78ddc02fcae4ab
```

and its different-model hostile review

```text
xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md
SHA-256 8ccaa15fd9180660d5ab7e2957737c028a96bb5b28508378e0a3ca93964089b5
verdict CONFIRMED
```

That result in turn retains the confirmed, corrected 40-variable/30-row
divided-carry predecessor.  The quarantined 29-row predecessor is not used.

Over the integers, with

```text
P = x-x^3 + 3U + 9C,
Q = y     + 3V + 9D,
```

write

```text
L = U_x+V_y-x^2,
K = (U_x-x^2)V_y-U_yV_x,
M = (U_x-x^2)D_y+C_xV_y-U_yD_x-C_yV_x,
N = C_xD_y-C_yD_x.
```

Direct expansion fixes the sign and scale:

```text
det J(P,Q)-1 = 3L + 9(K+C_x+D_y) + 27M + 81N.       (1)
```

The degree-ten producer represented the degree-seven pieces of `C,D`.
For the lower rows this package adds their degree-six pieces source-honestly.
The six degree-six Frobenius directions of `U,V` have zero formal derivative
modulo three.  Four can nevertheless enter the divided integer derivative:

```text
f_a=u6_3, f_b=u6_6, f_c=v6_0, f_d=v6_3,

[L/3]_5 = f_a x^2 y^3 + 2 f_b x^5
          +2 f_c y^5 + f_d x^3 y^2.                (2)
```

The other two pure Frobenius directions are invisible here.  Before forming
the degree-nine/eight rows, the replay solves exactly

```text
[K+C_x+D_y+L/3]_5=0                                (3)
```

for six degree-six `C,D` coefficients, retaining eight free coefficients.
The vertical degree-five layer is zero, so no omitted degree-eight
`K/3` term exists.  The high rows used below are consequently the exact
degree-nine/eight coefficients of `M`, after (3).  On the `g` endpoint the
only degree-five term is `V_5=g x^5`; it likewise creates no degree-eight
`K/3` term.  No cubed or denominator-cleared surrogate replaces (1).

## 2. Vertical degree nine has a global section

In the vertical normal form, the four degree-nine rows have coefficient
matrix

```text
[-s  0   0   r  -p   0   0   0   0]
[-w -s   0   t  -q   r  -p   0   0]
[ 0 -w  -s   0   0   t  -q   r  -p]
[ 0  0  -w   0   0   0   0   t  -q]
```

and inhomogeneous column

```text
(r^3+prs,
 qrs+pst+prw,
 qst+qrw+ptw,
 t^3+qtw)^T.
```

The exact polynomial vector

```text
ell=(-pr,-qr-pt,-qt,r^2,0,-rt,0,t^2,0)^T          (4)
```

satisfies `A9*ell=b9`.  Thus `-ell` solves the affine equations with the
producer orientation `A9*xi+b9=0` at every base point, including every
rank-changing point.  No review wait is used to block the degree-eight gate.

## 3. Vertical degree-eight structural core

Six degree-eight rows have unit pivots in

```text
d7_0,c7_0,d7_3,c7_3,d7_6,c7_6.
```

After exact substitution, the remaining seven rows use five unknowns.  The
invertible triangular base change is

```text
R=r-sh,       T=t-wh,
P=p-rh-sh^2,  Q=q-th-wh^2.                         (5)
```

In these coordinates the coefficient matrix is

```text
[-P  0   0   Rs       0]
[-Q -P   0   Ts+Rw    Rs]
[ 0 -Q  -P   Tw       Ts+Rw]
[ 0  0  -Q    0       Tw]
[-h^3 0  0   -P        0]
[ 0 -h^3 0   -Q       -P]
[ 0  0 -h^3   0       -Q].                        (6)
```

The inhomogeneous column is emitted directly from (1)--(3) by
`generate_and_enumerate.py`; it retains all of
`f_a,f_b,f_c,f_d`.  It is not replaced by a module remainder.

For a conceptual rank check, put

```text
A(z)=P+Qz,  B(z)=(s+wz)(R+Tz),  H=h^3.
```

Matrix (6) is the coefficient map

```text
(X,Y) |-> (-A X+B Y, -H X-A Y),
deg X<=2, deg Y<=1.                                (7)
```

Its polynomial determinant is `Delta=A^2+HB`.  Exact radical-minor
calculation gives

```text
rank <=4 locus = rank <=3 locus = V(coefficients of Delta),
rank <=2 locus = V(h,P,Q),
rank <=1 locus = rank 0 locus
               = V(P,Q,h,Rs,Ts+Rw,Tw).             (8)
```

Thus the only geometric ranks are `5,3,2,0`.  This rank-locus statement is
valid over algebraic extensions of F3.  The compatibility counts below are
the deliberately narrower literal-F3 exhaustion.

## 4. Exact literal-F3 census of the vertical core

The enumeration order is

```text
base  = (P,Q,R,T,s,w,h),
fiber = (f_a,f_b,f_c,f_d),
```

with all entries in `{0,1,2}`.  Gaussian elimination is implemented over
F3 with no external solver.  The complete rank pair census is

```text
(rank A,rank[A|b]) count
(0,0)                 161
(0,1)                1216
(2,2)                 288
(2,3)                4896
(3,3)                1890
(3,4)                3456
(5,5)               48600
(5,6)              116640
total               177147
compatible           50939.                        (9)
```

The SHA-256 of the deterministic stream
`base || fiber || rank(A) || rank([A|b])` is

```text
d7910730247c3da26599fac9c11cb28472ec7591ef49c221a825ef5978e17bee. (10)
```

For each of the `3^7=2187` structural bases, count compatible points in its
81-point Frobenius fiber.  The complete histogram is

```text
compatible fiber points   number of structural bases
1                           8
3                          48
9                        1368
27                        432
81                        331.                     (11)
```

In particular, every structural base has at least one compatible Frobenius
choice at this row.  This is not a claim that a fixed earlier predecessor
may change its already chosen Frobenius digits.

## 5. Exact `g != 0` endpoint reduction and census

On the confirmed `g` endpoint, `p=q=0` and the degree-five layer is
`V_5=gx^5`.  Three degree-ten rows have unit-after-localization pivots
`g*c7_0,g*c7_3,g*c7_6`; since this chart assumes `g != 0`, they eliminate
those three variables.  Two degree-nine rows are exactly

```text
g*f_c=0,  g*f_d=0,                                  (12)
```

so `f_c=f_d=0` before any lower-row solve.  This dispatch occurs before
clearing or dividing by `g`.  The remaining source-derived system has
`13` rows and `14` current-digit unknowns.

Exhaust all

```text
(r,s,t,w,h,g,f_a,f_b) in F3^8,  g in {1,2}.
```

The complete census is

```text
(rank A,rank[A|b]) count
(5,5)                 306
(5,6)                1152
(6,7)                 324
(8,8)                 648
(8,9)                1944
total                 4374
compatible             954.                        (13)
```

The corresponding rank-stream hash is

```text
119580e2aab411d56dc2b41f6118cf9fd03768bb8cc10397c0aa2b29abcd2da8. (14)
```

Among the `2*3^5=486` structural bases `(r,s,t,w,h,g)`, the number of
compatible `(f_a,f_b)` choices has histogram

```text
0 choices   252 bases
1 choice    144 bases
9 choices    90 bases.                             (15)
```

Thus this row kills more than half of the structural `g` bases, but leaves
a nonempty exact survivor set.  The displayed earlier `g` control lies in
the simple survivor subbranch `h=r=t=0`; its later divided carry is not
decided here.

## 6. Refusal boundary

Accepted:

- exact source compilation of (1)--(3) on the confirmed vertical and
  `g != 0` D10 survivors;
- the global degree-nine section (4);
- exact rank-locus classification (8) for the vertical `7 x 5` matrix;
- exhaustive literal-F3 compatibility censuses (9)--(15).

Not accepted:

- algebraic-closure or scheme-theoretic compatibility classification for
  the inhomogeneous `7 x 5` or `13 x 14` systems;
- a claim that module nonmembership is pointwise inconsistency;
- advancement through the next divided integer carry;
- exhaustion of the `a` endpoint, other associated-top branches, or full
  `D=7`;
- any no-lift, all-depth, characteristic-zero, counterexample, or JC2
  inference.

The next typed discriminator is to reconstruct one full compatible current
digit on each fiber-count stratum, return to the integer Jacobian, divide by
the exact next power of three, and test the following cap-boundary/Cartier
row without changing the earlier chosen digits.
