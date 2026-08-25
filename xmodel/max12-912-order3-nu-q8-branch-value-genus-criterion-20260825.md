# Selected-Q8 branch-value genus criterion

Date: 2026-08-25  
Status: **COORDINATOR CONDITIONAL LEMMA; exact elimination endpoint and hostile
review pending**

Let `k` be a perfect field and let `H(w,v) in k[w,v]` be geometrically
integral, monic of degree `d` in `v`, and separable over `k(w)`.  Let `C` be
the smooth projective normalization of `H=0`.  The function `w` defines a
finite separable map

```text
pi: C -> P1_w
```

of degree `d`.

Write

```text
Delta(w) = disc_v(H).
```

Let `S(w)` be any nonzero polynomial whose geometric zero set contains the
`w`-coordinates of every affine singular point of `H=0`; for example, one
may take a generator of the radical elimination ideal

```text
rad(H,H_w,H_v) intersect k[w].
```

Define the conservative squarefree residual

```text
D = rad(Delta) / gcd(rad(Delta), S),     N = deg(D).    (1)
```

Then

```text
g(C) >= ceil((N-(2d-2))/2).                         (2)
```

In particular, for the selected-Q8 candidate, `d=190`, so

```text
N > 378  ==>  g(H)>0.                               (3)
```

## Proof

Because `H` is monic, a finite value `w=a` is a zero of `Delta` exactly when
the fibre polynomial `H(a,v)` has a repeated geometric root `v=b`.  Thus

```text
H(a,b)=H_v(a,b)=0.
```

If `D(a)=0`, equation (1) guarantees that `a` is not a zero of `S`; hence no
point of the fibre above `a` is an affine singular point.  In particular
`H_w(a,b) != 0`.  The point `(a,b)` is smooth, `v-b` is a local parameter,
and implicit differentiation gives

```text
d w / d v = -H_v/H_w = 0
```

there.  Therefore `pi` is ramified above `a`.  Distinct geometric roots of
the squarefree polynomial `D` are distinct finite branch values, so there
are at least `N` branch values.  This deliberately discards every
discriminant value that is also the projection of any singular point, even
when that value additionally supports honest smooth ramification; it is a
lower bound.

For a finite separable map to `P1`, wild or tame Riemann--Hurwitz uses the
different divisor:

```text
2g(C)-2 = -2d + deg(Diff_pi).
```

Every branch value has at least one ramified point, and every ramified point
has different exponent at least one.  Hence `deg(Diff_pi)>=N`, which gives
(2).  Points above `w=infinity` are not counted and can only increase the
different.

## Exact-computation acceptance gate

A producer using this criterion must freeze and independently replay:

1. the exact pinned coefficients of `H`, monicity, `d=190`, and geometric
   integrality;
2. nonzero `Delta`, its exact degree, `rad(Delta)`, and squarefreeness;
3. a fail-closed elimination proving that every solution of
   `H=H_w=H_v=0` has `S(w)=0` (not merely a sample of rational singular
   points);
4. the exact gcd/division in (1), `N`, and the strict comparison `N>378`;
5. a second term order or independent resultant/elimination replay, plus
   positive controls on a smooth ramification point and a singular value.

No claim may subtract the degree or multiplicity of the singular scheme
itself from the discriminant.  Only the radical set of projected singular
**values** is relevant.  This criterion proves geometric genus positivity of
the standalone curve `H`; it does not by itself prove source membership,
contact attachment, trajectory exclusion, maximum twelve, or JC2.
