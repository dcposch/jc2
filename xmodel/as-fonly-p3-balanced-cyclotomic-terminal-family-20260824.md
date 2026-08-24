# AS map-only `p=3`: balanced cyclotomic finite-depth terminal family

**Producer-internal verdict: FOR EVERY ODD `m>=3`, THERE IS A TRIANGULAR
TOTAL-DEGREE `D=2m+1` AS-SEED RESIDUE WHICH SURVIVES MODULO `3^(2m)` AND
HAS NO SAME-CAP LIFT MODULO `3^(2m+1)`. THIS IS A FAMILY OF FINITE-DEPTH
CONTROLS, NOT AN ALL-DEPTH LIFT OR COUNTEREXAMPLE.**

- Date: 2026-08-24
- Arithmetic: exact rational/`3`-adic coefficients with unit denominators
- Status: producer-internal, pending independent review
- Origin: generalization of the frozen `D=7`, depth-six triangular point

## 1. Balanced factorization

For odd `m>=3`, put

```text
S_m(z)=1+z+...+z^(m-1),
A_m(z)=(1+z)S_m(z),
B_m(z)=A_m(-z).
```

Because `m` is odd,

```text
S_m(z)S_m(-z)
 = (1-z^m)(1+z^m)/((1-z)(1+z))
 = (1-z^(2m))/(1-z^2).
```

Therefore

```text
A_m(z)B_m(z)=1-z^(2m).                              (1)
```

This is the balanced cyclotomic partition behind the previously isolated
identity at `m=3`.

## 2. Exact triangular maps

Set `z=3x^2` and define over `Z_3`

```text
P_m'(x)=A_m(3x^2),       P_m(0)=0,
Q_m(x,y)=y B_m(3x^2).
```

Explicitly, the coefficients of `A_m` are

```text
1,2,2,...,2,1,
```

so

```text
P_m=x
 +sum_(k=1)^(m-1) (2*3^k/(2k+1))x^(2k+1)
 +(3^m/(2m+1))x^(2m+1).                            (2)
```

Every coefficient lies in `Z_3`. Indeed, if `3^a` divides `2k+1`, then
`a<=k`; after cancellation the denominator is a `3`-adic unit. For `k=1`
the coefficient is exactly two. For every `k>=2` the coefficient has positive
`3`-adic valuation. Consequently

```text
(P_m,Q_m) mod 3=(x-x^3,y).                          (3)
```

Both coordinates have total degree `D=2m+1`.

## 3. Survival and terminal obstruction

The triangular determinant and (1) give the exact `Z_3[x]` identity

```text
det J(P_m,Q_m)
 =A_m(3x^2)B_m(3x^2)
 =1-3^(2m)x^(4m).                                  (4)
```

Thus this is a genuine map-only bounded-degree point modulo `3^(2m)`. Choose
the coefficient representatives of (2) modulo `3^(2m+1)` using their
unit-denominator `3`-adic values. Every same-residue next lift has the form

```text
P_new=P_m+3^(2m)U,
Q_new=Q_m+3^(2m)V,
deg U,deg V<=D.
```

The special-fibre derivative matrix is the identity, so after division by
`3^(2m)` its next residual is

```text
-x^(4m)+U_x+V_y mod 3.                              (5)
```

But `deg(U_x+V_y)<=D-1=2m<4m`. Hence the `x^(4m)` coefficient cannot be
cancelled. The displayed residue is terminal modulo `3^(2m+1)` at cap `D`.

For `m=3`, (2) modulo 729 is exactly

```text
P=x+2x^3+441x^5+108x^7,
Q=y-6x^2y+18x^4y-27x^6y,
```

and its clean next representative has `x^7` coefficient `1566`. Thus the
family independently recovers the frozen D7 point. The next member, `m=5`,
has degree eleven, survives through depth ten, and is terminal at depth
eleven.

## 4. Campaign meaning

This family is useful in three ways:

1. it supplies exact positive/terminal regression controls at arbitrarily
   large finite depths;
2. it proves that a theorem-calibrated negative degree need not die at a
   shallow Witt level—the survival depth can be `D-1` in this family;
3. it exposes a cyclotomic factor-partition search for other balanced
   triangular strata.

It does not give a compatible branch at fixed `D`: each member dies at its
next digit. It does not classify any full fixed-degree locus, bound the death
depth of other components, algebraize a Witt tower, give `A_infinity=0`,
descend a deck action, construct a characteristic-zero Keller map, or decide
JC2.

Replay:

```sh
python3 cases/as_fonly_p3_balanced_cyclotomic_family_20260824/replay.py
```
