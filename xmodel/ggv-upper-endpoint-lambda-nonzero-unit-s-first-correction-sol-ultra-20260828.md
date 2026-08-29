# Lambda-nonzero unit-S face: the first correction is square-divisible

Date: 2026-08-28

Status: **EXACT DESK LEMMA; EARLY POLE ATTACK CLOSED THROUGH RELATIVE ORDER
THREE; REVIEW PENDING**

## Result

Work at a simple root `alpha` of `A`, put `epsilon=X-alpha`,
`A=epsilon*a(epsilon)`, and scale `t=epsilon*tau`.  On the reviewed
`lambda!=0`, active-`c2`, exact-`D=0` successor,

```text
S(alpha)=3 lambda A'(alpha) != 0,
D=0,                 P=A P1.
```

The leading normalized F-face is

```text
L(tau)^4,            L=A'(alpha)+S(alpha) tau/4.
```

Write `a=A'(alpha)`, `s=S(alpha)`, and `u=U(alpha)`.  The two reviewed lift
equations give

```text
R(alpha)=4su,
F5(alpha)=s^2u/128.
```

The part of the first `epsilon` correction not already visibly divisible by
`L^2` is therefore

```text
H1 = a^2u tau^3/8 + aR tau^4/64 + F5 tau^5
   = u tau^3 (s tau+4a)^2/128
   = u tau^3 L^2/8.                                  (1)
```

The derivative of the leading squared bracket contributes another multiple
of `L^2`.  Hence the entire normalized expansion begins

```text
epsilon^-4 F(X,epsilon tau)=L^4+epsilon L^2 K1+O(epsilon^2).  (2)
```

This closes the tempting first-pole attack.  More strongly, a partition
census in the binomial expansion shows that the smallest possible powers of
`L` in the relative epsilon orders 1,2,3,4 of `F^(3/2)` are

```text
4, 2, 0, -2.
```

The `c2*t^2*F^(5/4)` mode has minima `5,3,1,-1`; the born c4 and c6 leading
terms are also polynomial.  Thus the complete characteristic has no
fractional face pole through relative epsilon order three.  Order four is
the first possible discriminator, and cancellation there is not decided by
this lemma.

## Consequence for allocation

A unit-S calculation truncated at the first, second, or third relative
epsilon correction cannot exclude the `lambda!=0` branch by a face-factor
pole.  Either compute through relative order four with all born modes and raw
floors, or use the already staged full `lambda=1` raw-window compiler.  The
formal constant shear remains determinant-covariant but illegal on the raw
alphabet; this lemma does not restore it.

## Reproducibility and scope

Checker:

```text
cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_first_correction_20260828/
  verify_unit_s_first_correction.py
```

Expected marker: `PASS_EXACT_UNIT_S_FIRST_CORRECTION`.

The checker pins the reviewed Newton and q1/q3 packets, verifies `(1)` in a
sparse exact polynomial ring, and enumerates every partition contributing
through relative order four.  This is a local field/radical statement.  It
does not prove polynomiality at order four, endpoint emptiness, branch-P
emptiness, a Keller theorem, or JC2.
