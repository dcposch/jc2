# Promotion: formal weighted affine-Faber `A` direct unit

Date: 2026-08-26

Status: **PROMOTED AT THE EXACT POLYNOMIAL-IDENTITY SCOPE ONLY.**

## Promoted statement

In characteristic zero, substitute the exact depressed moving-discriminant
coordinates

```text
Q=A^2*(A^2+4*a*A+E)+(X+R1)*A+R0,
N=lam*(M*A*(A^2+4*a*A+E)+Y*A+M*X/2+S1*A+S0)
```

into all seven frozen complete ordinary-Faber tails.  Under the formal
weights

```text
a:5, X:Y:6, R*:S*:12, lam:15, loads/mu2:42,
```

the exact inverse-Faber combinations satisfy

```text
H3 = -(3/8)*t^42*lam^2*M*X*Y
     -(1/16)*t^45*lam^3*M^3                    mod t^46,
H5 =  (3/8)*t^42*E*lam^2*M*X*Y                 mod t^46.
```

Therefore

```text
E*H3+H5 = -(1/16)*t^45*E*lam^3*M^3             mod t^46,
```

which is a unit on `D(E*lam*M*K10)`.  Because this is a polynomial
congruence in all displayed symbols, arbitrary formal-series substitution
and common ramification preserve it.  This includes later moving-center
jets (in particular the formerly omitted `a6`), all tangent/complement
series admitted by these weights, unequal kernel orders at least six, and
higher kernel monomials through grade 45.

## Custody

```text
producer FREEZE.sha256:
  0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5
producer EVIDENCE.sha256:
  86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48
producer RESULT.md:
  5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d
hostile review:
  7349330c903e7a336738792324d63570fd0f14252c20754337c6c6f801fa1cf5
```

The hostile review independently rehashed the charged source, rebuilt all
seven tails and the inverse-Faber matrix, reran exact-Q algebra, checked the
cubic coefficient by hand, and ended `CONFIRMED`.

## Firewall

This promotion is not the broader valuative-composition theorem.  It does
not prove the two-sided `Q,N` or total-Rees source chart, the complement
absorption/weight bounds, the separate `q<6` certificate, `q=0` routing,
other load slopes, `m=0`, `p=0`, terminal/Taylor coverage, order two,
maximum twelve, or JC2.  Those gates remain separate; the composition
review is charged independently.
