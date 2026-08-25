# D1 classical degree split at coefficient infinity

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER THEOREM; ADVERSARIAL REVIEW REQUIRED**

## Statement

Work over the characteristic-zero finite constant extension `L` carried by
a certified section.  Consider a Taylor-realizable trajectory in the cyclic
`D=e=1` order-three `(9,12)` normalization, with `A_i,R0 in L(s)` and
`k in L`,

```text
s=x/(x-1),  t^3=s,  u=t^2/(s-1)^2,
u^3=h=x^2(x-1)^4,
f(z)=z^9+sum_(i=0)^7 a_i z^i,
a_i=t^(i mod 3) A_i(s),
g=F_12(f)+k F_6(f),
z=u(y+R0).
```

After a polynomial source shear, take `R0` regular at `x=infinity`
(`s=1`).  With `v_(s-1)(s-1)=1`, put

```text
d_i=max(0,-v_(s-1)(A_i)),  0<=i<=7.
```

If

```text
d_i <= 3(9-i)  for every i,                         (1)
```

then the resulting polynomial coordinates have exact ordinary total degrees

```text
(deg_total P,deg_total Q)=(27,36).                  (2)
```

Consequently this sector contains no JC2 counterexample, by the
Guccione--Guccione--Valqui/Heitmann necessary condition
`gcd(deg_total P,deg_total Q)>=16`: here the gcd is `9`.

Thus every D1 counterexample client must lie on the strict weighted
coefficient-infinity sector

```text
d_i > 3(9-i) for at least one i.                    (3)
```

Explicitly, the first possible violations are

```text
d_0>27, d_1>24, d_2>21, d_3>18,
d_4>15, d_5>12, d_6>9,  or d_7>6.
```

This is a split, not a closure of (3).

## 1. The finite source-shear normalization

The coefficient of `y^8` in `P=f(u y+u R0)` is

```text
9 u^9 R0 = 9 h^3 R0.
```

Taylor polynomiality therefore makes `R0` a rational function of `x` whose
finite poles are bounded by the zero divisor of `h^3`.  Write its polynomial
part at `x=infinity` as `q(x)`.  Precomposition by the polynomial
automorphism `(x,y) |-> (x,y-q(x))` replaces `R0` by `R0-q` (up to the
irrelevant sign convention) and leaves the depressed cores `f,g`, hence all
`A_i`, unchanged.  It preserves the constant-Jacobian property and
automorphism/nonautomorphism status.  Thus a putative counterexample may be
tested after this shear, and we may assume that `R0` is regular at infinity.

Since

```text
s-1=1/(x-1),  t^3=s,
```

`t` is a unit at each place above `s=1`, while `u` has pole order two.
Let `v=v_(s-1)` on `L(s)`, normalized by `v(s-1)=1`.  The extension
`t^3=s` is etale at `s=1`, because `T^3-1` is separable in characteristic
zero.  Thus every place above `s=1` has ramification index one, `t` is a
unit, and `v(u)=-2`; no fractional valuation is hidden here.  Pole order at
`s=1` of an invariant rational function is its polynomial degree in `x`
once Stage B has killed the `t,t^2` components and established that the
invariant component lies in `L[x]`.

## 2. Degree of `P`

For `0<=ell<=9`,

```text
[y^ell]P = u^ell f^(ell)(u R0)/ell!
          = sum_(i>=ell) binom(i,ell) a_i u^i R0^(i-ell),
```

where the monic term is represented by `i=9`, `a_9=1`, `d_9=0`.
Because `R0` is regular at infinity, the summand indexed by `i` has pole
order at most

```text
d_i+2i <= 3(9-i)+2i = 27-i <= 27-ell.
```

The Taylor coordinate is in `L[x]`, so
`deg_x([y^ell]P)<=27-ell`.  Hence `deg_total P<=27`.  On the other hand,

```text
[y^9]P=u^9=h^3
```

has `x`-degree `18`; its term `h^3 y^9` has total degree `27` and cannot
cancel.  Therefore `deg_total P=27`.

## 3. Degree of `Q`

Use the exact Faber grading

```text
wt(z)=1, wt(a_i)=9-i, wt(k)=6.
```

Every monomial of `F_12(f)+k F_6(f)` has weight `12`.  If a monomial
contributing to the `z^j` coefficient contains `a_i` with multiplicity
`e_i` and `k` with multiplicity `e_k`, then

```text
sum_i e_i(9-i)+6e_k+j=12.                           (4)
```

After substituting `z=u(y+R0)`, its contribution to `[y^ell]Q`, with
`j>=ell`, has pole order at most

```text
sum_i e_i d_i + 2j
 <= 3 sum_i e_i(9-i)+2j
  = 36-18e_k-j
 <= 36-j
 <= 36-ell.
```

Stage-B Taylor membership gives `deg_x([y^ell]Q)<=36-ell`, hence
`deg_total Q<=36`.  The monic coefficient

```text
[y^12]Q=u^12=h^4
```

has `x`-degree `24`, so `h^4 y^12` has total degree `36`.  Thus
`deg_total Q=36`.

## 4. Consequence and exact firewall

The already primary-source-checked GGV/Heitmann theorem says that a
characteristic-zero plane Jacobian counterexample must satisfy

```text
gcd(deg_total P,deg_total Q)>=16.
```

Equations (1)--(2) instead give `gcd(27,36)=9`.  Therefore the bounded
weighted sector is counterexample-closed.

No claim is made for (3).  At that boundary the coefficient poles can raise
ordinary total degrees, and the leading equations can degenerate toward the
common-cubic locus `f=K^3`, `g=K^4+kK^2`.  Neither Stage-A finite fibres nor
generic affine Groebner data cover this weighted coefficient-infinity
divisor.  A valid D1 exclusion still has to classify that divisor (including
its integer valuation branches), or prove independently that Taylor
polynomiality removes it.

This note does not close `k=0`, a higher passport, the order-one Kummer leaf,
`(8,12)`, the full partial-`y` `(9,12)` cell, or JC2.

## Inputs

- `cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/PREREGISTRATION.md`
- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/stage_b_taylor.py`
- `xmodel/max12-partial-y-kummer-preflight-20260824.md`
- `xmodel/sol-fixed-total-d12-classical-closure-v2-20260825.md`
- `xmodel/sol-fixed-total-d12-classical-closure-review-as-20260825.md`
