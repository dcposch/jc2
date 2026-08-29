# Provisional structural theorem — K00 grade five over the rank-zero plane

Date: 2026-08-29 UTC  
Author: Sol 5.6 internal exact-analysis lane, integrated by the coordinator  
Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`  
Lifecycle: `EXACT_PRODUCER_EVIDENCE / PROVISIONAL_PENDING_EXTERNAL_REVIEW`

## 0. Executive disposition

Direct exact reconstruction from the frozen atlas gives a Groebner-light
structural solution of the registered grade-five problem. Both the reduced
and nonreduced grade-four inputs remain proper as bare affine ideals, but
their common reduced grade-five locus projects to the origin of the leading
rank-zero plane. Since the K00 client is explicitly a valuation-one prefix,
that origin is the higher-valuation leak and is not source-compatible.

Provisional maximum conclusion:

```text
THE NORMALIZED VALUATION-ONE, C6=1, k10_0!=0 K00 SEED
HAS NO GRADE-FIVE-COMPATIBLE POINT.
```

This is not promoted until independent review. It closes only this normalized
valuation-one seed, not other coefficient valuations, a finite jet, an arc,
a polynomial map, the counterexample side of JC2, or JC2.

## 1. Exact structural identity

On the reviewed rank-zero plane put

```text
ell=(2s,t/8,s,t,s,2t),
mu=(s^2,st/8,16t^2,0,0,0),
w=u-mu.
```

For literal row `r`, let `Q_r=Lambda_(2,r)`, let `c3_r` be the pure
`d*_1`-cubic part of `Lambda_(3,r)`, and let
`M4_r=[k10_0]Lambda_(4,r)`. Exact sparse-polynomial reconstruction gives,
generatorwise for all seven rows,

```text
G5_r = DQ_r(w)[v]
       +(1/2) D^2 c3_r(ell)[w,w]
       +k * D M4_r(ell)[u-mu/2].
```

The raw coefficient identities

```text
[d_j,4] Lambda_(5,r) = [d_j,2] Lambda_(3,r),
[k10_1] Lambda_(5,r) = [k10_0] Lambda_(4,r)
```

explain the support census. Both right sides vanish at `ell`; hence the whole
`d*_4` block and `k10_1` disappear, while `v=d*_3` and `k=k10_0` return. The
essential ring is

```text
T5=Q[s,t,u0..u5,v0..v5,k,z],       z*k-1.
```

Restoring `d*_4,k10_1` adds only a free `A^7` factor.

## 2. Affine/Fitting compression

Write `G5=C(w)v+kM+N`. The coefficient matrix `[C(w)|M]` has constant right
kernel

```text
(2,0,1,0,1,0;0),
(0,1/8,0,1,0,2;0),
```

and constant left kernel

```text
(3/128,0,1/8,0,1,0,0),
e6,
(1/512,0,1/128,0,0,0,1).
```

Thus only the four quotient coordinates

```text
xi=(2v3-v5, v2-v4, 16v1-v5, v0-2v4)
```

matter. For the shifted prior block set

```text
a=2w3-w5,       b=w2-w4,
c=16w1-w5,      d=w0-2w4.
```

The reduced grade-four equations are `A=c-2a=0`, `B=d-4b=0`. For rows
one through four, the determinant of the quotient `4 x 4` affine matrix is

```text
(81/2^57) * (64*A^2+B^2)^2.
```

On `A=B=0`, put `H=16a^2+b^2`. The remaining coefficient rank is two on
`D(H)`, one on `H=0,(a,b)!=(0,0)`, and zero at `a=b=0`. Modulo the
grade-four scheme ideal, the other three rows satisfy the exact syzygies

```text
(3/128)G1+(1/8)G3+G5 = -(3/64)sQ1-(1/2)tQ2,
G6 = (3/32)tQ1-(1/32)sQ2-(1/4)tQ3,
(1/512)G1+(1/128)G3+G7 = (1/16)tQ2-(1/64)sQ3.
```

These identities compress the gate without discarding labels or scheme
structure.

## 3. Complete reduced-locus rank split

After eliminating `c,d` on the radical input, the two base residuals are

```text
F=a*b*s-16*a^2*t+b^2*t,
E=64*a*b*t+16*a^2*s-b^2*s.
```

The rank split is exhaustive over an algebraic closure.

- On `D(H)`, the coefficient determinant of `(F,E)` in `(s,t)` is `H^2`,
  so `s=t=0`.
- On `H=0,(a,b)!=(0,0)`, the surviving affine rows give, modulo `H=F=0`,
  a nonzero scalar multiple of `a*k*t^3`. Since `a` and `k` are nonzero,
  `t=0`, then `s=0`.
- At `a=b=0`, the only base equations are proportional to

  ```text
  k*t*(3s^2-64t^2),
  k*s*(s^2-192t^2),
  ```

  whose only common zero on `D(k)` is `s=t=0`.

Therefore the radical- and scheme-input variants have the common reduced
locus

```text
s=t=0,
16u1-4u3+u5=0,
u0-4u2+2u4=0,
C(u)v=0,
k!=0,
```

with `d*_4,k10_1` free. Both bare ideals are proper; a common rational
witness is `s=t=u=v=0`, `k=z=1`. The essential reduced locus has dimension
nine; restoring the dummy `A^7` gives dimension sixteen in the full
preregistered ring.

The schemes are not equal. Under the scheme input, `A` and `B` retain exact
nilpotency index three:

```text
A,A^2 notin I;  A^3 in I;
B,B^2 notin I;  B^3 in I;
A*B in I.
```

The nonmemberships follow by the retraction `s=t=v=0,k=z=1`, which returns
the grade-four scheme. Thus membership of `A` is the smallest exact
scheme/radical discriminator. As required by the general radical identity,
the two inputs do not differ geometrically.

One lightweight Singular check of the radical quotient returned `dim=7`
before the two free `v`-kernel directions, multiplicity 128, and
`s^12,t^12` nonzero but `s^13=t^13=0`. Those power/multiplicity observations
are single-engine discovery only; none is used in the geometric theorem.

## 4. Source-compatible consequence

The normalized valuation-one client writes

```text
d_i = Lambda*x_i + O(Lambda^2),
x=(d0_1,...,d5_1)=ell(s,t),
```

and requires the leading block `x` to be nonzero. Earlier K00 analysis
explicitly labels `x=0` the higher-valuation leak, not a valuation-one point.
Since `ell` is injective and grade five forces `s=t=0`,

```text
V(I_G5) intersect D((d0_1,...,d5_1))
  = V(I_G5) intersect (D(s) union D(t))
  = empty.
```

Equivalently, the two source charts `D(s)` and `D(t)` are unit. The bare
affine ideal survives only on the unsupported higher-valuation origin.

This provisionally kills the complete normalized valuation-one,
`C6=1,k10_0!=0` K00 seed at grade five. It does not decide another
coefficient valuation or show that every K00 deformation can be normalized
to valuation one.

## 5. Custody and review requirements

Charged hashes:

```text
40c1ab3448209e3d87173feb947a733f6fe54f7f  frozen basis
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860  grade-3 integration
0d2a9861126c8857e04a9170c8586b6b4eabe67d2e65d3b4d3b7e991774b614f  grade-4 primary
24640d0dacec16b27b4c7eb83419188aa86e3fc80b481b0ba64aa136348fc892  atlas compiler
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501  exact atlas JSON
```

Plane-specialized grade-five row term counts are
`(42,49,57,53,64,33,61)`. Their canonical exact-term digests are,
respectively,

```text
1cf445f836be0ce2eae28910fcdee0e0d717dcd37f16ebaf700aebe4a96524a8
57aee1669baaa19f605c1930bb1e45d81de1b4a9c5bc610ca9fd7cd6260275ad
86f25ab3356d7330c47012aee1339361d208b7cb0db70e95e112806e72abcfaf
8d36dabac290a3fce814b61f15ff20625275bc1332900108bdf3d90bb1bee9d4
0134117e3505e39faf1158b17be605ad9ec989d0183d5a376571983bb156a28d
93708527820e8aee0dc02906524a88f9a5cb098497811aee046524dcfba9d9ee
8bbae15796c871ddb61c9a47dfb59c2fd35fde1ca0c5036e6512f19712553b75
```

Independent review must rebuild from `exact_terms`, verify the rank split and
source-open interpretation, use named ring maps, test `D(s)` and `D(t)`, and
distinguish projection-to-origin from a singleton full locus. Heavy primary
decomposition is unnecessary for the geometric verdict and belongs on AWS
only if later scheme structure justifies it.

No peer current-round result was consumed. One broad search surfaced only the
already assigned scheme/radical variant labels from a peer prompt; no peer
report, log, or run record was read.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7295`.
- Body SHA-256:
  `25802ec587a1ae0a0ce46cb221ec87b42e70344ce7582554f612a61f2ee4a3a4`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
