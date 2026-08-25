# Max12 `(9,12)` selected-Q8 rational etale point over `F_127`

Date: 2026-08-25  
Status: **producer-exact; conditional constant-field consequence; hostile different-model review required**

## 1. Exact point

In the exact localized selected-Q8 quotient over `F_127`, at `w=71` the
squarefree degree-190 `v` eliminant has the linear factor `v-50`.  Starting
again from the original eight generators—not from an eliminant-derived
candidate basis—pure Singular gives the unique rational point above this
factor:

```text
(c,d2,d4,x1,x3,x5,inv,v)
  = (47,67,27,122,123,39,11,50) in F_127.              (1.1)
```

Equivalently, the reduced point basis is

```text
v-50, inv-11, x5-39, x3+4,
x1+5, d4-27, d2+60, c-47.                             (1.2)
```

All eight original generators reduce to zero.  The point quotient has
vector-space dimension one.

## 2. Relative etaleness

Take the Jacobian of the original eight localized generators with respect to

```text
(c,d2,d4,x1,x3,x5,inv,v).
```

At (1.1) its determinant is

```text
51 mod 127 != 0.                                      (2.1)
```

Thus the total one-parameter quotient is smooth at this rational point and
the projection to the `w`-line is etale there.  This is stronger than merely
observing a linear factor in a derived eliminant.

## 3. Conditional constant-field lemma

Suppose a separate common-monic/finite-flat argument proves that the generic
degree-190 quotient over `F_127(w)` is arithmetically irreducible and that the
point (1.1) lies on its integral curve.  Then its algebraic constant field is
exactly `F_127`: a larger constant field `F_(127^e)`, `e>1`, would force every
closed point on the normalization to have degree divisible by `e`, whereas
the smooth rational point (1.1) lifts uniquely with degree one.  Since the
base field is perfect, this removes the constant-field obstruction to
geometric irreducibility.

The hypotheses in the preceding paragraph are charged.  The rational point
alone does not prove connectedness or arithmetic irreducibility.

## 4. AWS replay and hashes

The exact replay ran on AWS Box02 host `ip-172-30-0-186`, tag
`q8_p127_w71_v50_etale_v1`, and exited zero.  The separate harvested-output
audit ran under tag `q8_p127_w71_v50_etale_audit_v1` and also exited zero.

```text
generator.py       28a7c47608b1663221b3f128fa4d438df44d7fbef89b0d0e0695fe6255858ec7
run_remote.sh      7b5bd807f3c8235b82cef0d8d3122bf619d82e2e9d056b223699100fb9121722
input.sing         1f59eba0fbfd241f69b4d7110de39778991a26f6b40d53bcaed21f32924fa495
result.out         a89a55e7b31d79b2b60a218b0ebe195ab5e14585b1e44ed2d26a4a1edd4c81ab
audit.py           4ea722e914b22488240c2d1081ff34607855ab1bc23cd8df7115a1e40b26d1f8
audit.json         9ea871837b708d4abe4abbd242459b2a3629f9b48fbaa6d536d67e5bc85d4366
audit stderr       e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The portable case is
`cases/max12_912_order3_nu_q8_p127_rational_etale_point_aws_20260825`.

## 5. Scope exclusions

This report does not prove the common monic degree-190 family theorem,
arithmetic or geometric irreducibility, good-reduction lifting to
characteristic zero, coefficient-fibre/Taylor realization, terminal-row
compatibility, trajectory exclusion, maximum twelve, or JC2.

