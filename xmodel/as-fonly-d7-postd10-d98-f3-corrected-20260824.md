# AS F-only `p=3,D=7`: source-corrected post-D10 D9/D8 gate

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE REVIEW.**

## Headline

This package is the source-honest replacement for the quarantined post-D10
D9/D8 package.  It starts again from the integer Jacobian, retains all six
degree-six Frobenius directions, and includes the formerly omitted divided
single-Frobenius cross-carry.

The corrected exact results are:

1. The vertical degree-nine global polynomial section survives unchanged.
2. The vertical degree-eight coefficient matrix and geometric rank strata
   survive, but the corrected affine column depends on six rather than four
   Frobenius variables.  The exact literal-F3 census is now
   `314127/1594323`; twelve of the `2187` structural bases have empty fibers.
3. The corrected `g != 0` endpoint is a `17 x 14` system, not the retracted
   `13 x 14` system.  Its exact literal-F3 census is `918/354294`.
4. Two explicit surviving vertical points are reconstructed as full
   cap-seven maps modulo 81.  Each has an uncancellable `x^8` residual at the
   next digit, hence each particular point is terminal modulo 243.  This is a
   pointwise negative control, not an obstruction to its whole stratum.

The finite censuses classify literal F3 points only.  They are **not**
algebraic-closure/Fitting classifications, and no full-D7, all-depth,
no-lift, characteristic-zero, counterexample, or JC2 conclusion is made.

## 1. Licensed input and quarantined predecessor

This gate consumes the confirmed D10 producer and review:

```text
xmodel/as-fonly-d7-degree10-pointwise-20260824.md
SHA-256 e4311a80aef2d3617c7b449e16cb19d34cfe25d31c558bb68f78ddc02fcae4ab

xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md
SHA-256 8ccaa15fd9180660d5ab7e2957737c028a96bb5b28508378e0a3ca93964089b5
verdict CONFIRMED
```

It also consumes the source correction frozen in

```text
xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md
SHA-256 26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d
```

The earlier report
`xmodel/as-fonly-d7-postd10-d98-f3-20260824.md` and its case directory remain
byte-preserved but quarantined.  None of their affine-column counts or hashes
are used here.

## 2. Exact integer source and the missing row

For

```text
P=x-x^3+3U+9C,  Q=y+3V+9D,
L=U_x+V_y-x^2,
K=(U_x-x^2)V_y-U_yV_x,
M=(U_x-x^2)D_y+C_xV_y-U_yD_x-C_yV_x,
N=C_xD_y-C_yD_x,
```

direct integer expansion gives

```text
det J(P,Q)-1 = 3L+9(K+C_x+D_y)+27M+81N.          (1)
```

Write `U=U0+UF`, `V=V0+VF`, where the degree-six Frobenius pieces are

```text
UF=fua*y^6+fa*x^3*y^3+fb*x^6,
VF=fc*y^6+fd*x^3*y^3+fvb*x^6.                    (2)
```

Every derivative in (2) is divisible by three over the integers.  After the
accepted row is divided, however, the single-Frobenius part of `K/3` is

```text
(UF_x/3)V0_y +(U0_x-x^2)(VF_y/3)
 -(UF_y/3)V0_x-U0_y(VF_x/3) mod 3.               (3)
```

The double-Frobenius product still vanishes after division modulo three.
The independent symbolic-integer replay derives (3) as
`(K(U0+UF,V0+VF)-K(U0,V0))/3 mod 3` and compares it termwise to the
generator.  It reaches degree eight vertically and degree nine on the
`g x^5` endpoint.  All six variables in (2) occur in the regenerated rows.

The accepted degree-five row is generated first:

```text
[K+C_x+D_y+L/3]_5=0,                              (4)
```

with

```text
[L/3]_5=fa*x^2*y^3+2fb*x^5+2fc*y^5+fd*x^3*y^2.
```

Six unit pivots in (4) leave eight degree-six `C,D` coefficients free.  The
following high rows are then generated from `M+(3)`, not from `M` alone.
No denominator-cleared or cubed surrogate is used.

## 3. Vertical D9 and D8 structure

The vertical Frobenius cross (3) has degree at most eight, so the four D9
rows are unchanged.  Their coefficient matrix is

```text
[-s  0   0   r  -p   0   0   0   0]
[-w -s   0   t  -q   r  -p   0   0]
[ 0 -w  -s   0   0   t  -q   r  -p]
[ 0  0  -w   0   0   0   0   t  -q]
```

and the exact polynomial vector

```text
ell=(-pr,-qr-pt,-qt,r^2,0,-rt,0,t^2,0)^T         (5)
```

satisfies `A9*ell=b9`, including on every rank-changing locus.

At D8, six source-typed unit pivots eliminate

```text
d7_0,c7_0,d7_3,c7_3,d7_6,c7_6.
```

Use the invertible triangular coordinates

```text
R=r-sh,  T=t-wh,  P=p-rh-sh^2,  Q=q-th-wh^2.      (6)
```

The remaining seven rows in five current-digit unknowns have coefficient
matrix

```text
[-P  0   0   Rs       0]
[-Q -P   0   Ts+Rw    Rs]
[ 0 -Q  -P   Tw       Ts+Rw]
[ 0  0  -Q    0       Tw]
[-h^3 0  0   -P        0]
[ 0 -h^3 0   -Q       -P]
[ 0  0 -h^3   0       -Q].                       (7)
```

Writing `A(z)=P+Qz`, `B(z)=(s+wz)(R+Tz)`, (7) is the coefficient map

```text
(X,Y) -> (-AX+BY,-h^3 X-AY),  deg X<=2, deg Y<=1. (8)
```

An exact radical-minor replay over F3 gives

```text
rank <=4 = rank <=3 = V(coefficients of A^2+h^3 B),
rank <=2             = V(h,P,Q),
rank <=1 = rank 0    = V(P,Q,h,Rs,Ts+Rw,Tw).       (9)
```

Thus the only geometric ranks of (7) are `0,2,3,5`.  Statement (9) is valid
over algebraic extensions; the compatibility census below is narrower.

## 4. Corrected vertical literal-F3 compiler and census

The corrected column is affine in

```text
(fua,fa,fb,fc,fd,fvb).
```

For each structural base `(P,Q,R,T,s,w,h)`, let `A` be (7), `F` the six
Frobenius columns in the affine right side, and `b0` its constant column.
Put

```text
r=rank(A), c=rank([A F]), d=rank([A F b0]).
```

The exact projection compiler returns zero compatible Frobenius choices if
`c<d`, and otherwise returns `3^(6+r-c)`.  Its complete 2187-base histogram
is

```text
compatible Frobenius choices   bases
0                                 12
3                                 36
9                                 16
81                              1904
729                              219.             (10)
```

The complete rank-triple census is

```text
(r,c,d) count
(0,0,0)    1   (0,4,4)   16   (2,4,4)   16
(2,6,7)   12   (2,7,7)   36   (3,3,3)    2
(3,5,5)   64   (5,5,5)  216   (5,7,7) 1824.       (11)
```

The twelve empty bases are exactly

```text
P=Q=s=h=0,  R!=0, w!=0,  T arbitrary.
```

Their deterministic stream hash is

```text
5b66a63af070eff410c1824a6e6f4e73fc254da13eb5445dcb9bdae4c2ece701. (12)
```

An independent exhaustive loop over all `3^13=1594323` literal points gives

```text
(rank A,rank[A|b]) count
(0,0)                  873
(0,1)                11520
(2,2)                 1404
(2,3)                45252
(3,3)                 6642
(3,4)                41472
(5,5)               305208
(5,6)              1181952
compatible           314127.                       (13)
```

The rank-stream SHA-256 is

```text
e86fd1ec2724b5089039378c07e1a19a089042eeb4172b0342474f85d4d8b23d. (14)
```

The structural compiler and exhaustive loop agree on the total and every
fiber count.

## 5. Corrected `g != 0` endpoint

The three D10 rows still give the localized pivots
`g*c7_0,g*c7_3,g*c7_6`.  After those exact eliminations, the regenerated
D9/D8 system has `17` rows and `14` current-digit unknowns.  In particular,
the omitted degree-nine terms `2g*fua*x^4*y^5` and `g*fa*x^7*y^2` show why
the old four-row deletion was invalid.  No Frobenius variable is discarded.

The affine projection compiler over the 486 structural bases
`(r,s,t,w,h,g)`, `g!=0`, gives

```text
compatible Frobenius choices   bases
0                                360
3                                 36
9                                 90.              (15)
```

Its rank triples are

```text
(5,9,9):18, (5,10,10):36, (5,10,11):108,
(6,10,11):36, (8,12,12):72, (8,12,13):216.        (16)
```

Exhausting all `486*3^6=354294` literal points gives

```text
(rank A,rank[A|b]) count
(5,5)                  270
(5,6)               117828
(6,7)                26244
(8,8)                  648
(8,9)               209304
compatible              918.                       (17)
```

The rank-stream and empty-base hashes are respectively

```text
ce421ac61d73307c3d0bd553af9e23df7f040f6e7b3e85b4d7da06f220935b67,
2fdb6b61e6a98e9e4b39ce8459f62774cf6dacd161b04c6752e044e87e963b2e. (18)
```

## 6. Reconstructed next-carry controls

Four vertical fibers of sizes `3,9,81,729` are reconstructed with an exact
Gaussian solver.  Two particular high-row solutions have

```text
3-fiber:  {C,D}_12=x^12,
81-fiber: {C,D}_12=2x^12.                          (19)
```

At the following divided carry, other order-81 terms and a new cap-seven
digit reach total degree at most eleven.  Thus (19) obstructs those
**particular chosen high-row representatives**.  It does not show that every
solution in either fiber has the same class.

Two further representatives reconstruct to full integer maps modulo 81:

```text
P0=x-x^3+18x^5+54x^7,
Q0=y+3x^2y                         (729-fiber),

P0=x-x^3+18x^5+54x^7,
Q0=y+3x^2y+3x^4                    (9-fiber).
```

Both have the exact integer determinant

```text
1+81x^4+648x^6+1134x^8,                           (20)
```

so they are Keller modulo 81.  After division by 81, their next residual is
`x^4+2x^6+2x^8 mod 3`.  A cap-seven correction has divergence of degree at
most six, hence cannot cancel `2x^8`.  These two points are terminal modulo
243 at cap seven.  This remains only a pointwise control.

## 7. Replay and refusal scope

Portable case:

```text
cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/
```

Complete replay:

```sh
cd cases/as_fonly_d7_postd10_d98_f3_corrected_20260824
./replay_all.sh
```

The replay independently checks the integer divided-Frobenius source,
vertical D9 section, geometric rank loci, affine projection formulas, full
literal-F3 enumerations and hashes, reconstructed current digits, and the
next-carry controls.

This producer does not classify compatibility over `Fbar_3`, advance every
literal survivor, cover any unexamined D10 branch, prove failure at all
depths, produce a characteristic-zero map, or imply a JC2 result.
