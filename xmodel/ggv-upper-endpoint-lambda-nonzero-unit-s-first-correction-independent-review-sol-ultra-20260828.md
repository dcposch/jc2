# Independent review: lambda-nonzero unit-S first correction

Date: 2026-08-28

Target: `xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-first-correction-sol-ultra-20260828.md`

Target SHA256: `c3f03f370eec64375af19dc684a17c52ee176b2aa1f6179cfedfa0c3a15cdb9a`

Verdict: **PASS**, with one reproducibility-coverage clarification and no mathematical repair.

## 1. Root relations and first correction

At a simple root `alpha` of `A`, write

```
a=A'(alpha), s=S(alpha), u=U(alpha), L=a+s*tau/4.
```

On exact `D=0`, `D=R-4SU` gives

```
R(alpha)=4su.
```

At the root the reviewed relation `P=A P1` gives `P(alpha)=0`; substituting
`P=256F5-RS+2S^2U` and the preceding value of `R` gives

```
F5(alpha)=s^2u/128.
```

Thus the non-square part of the relative epsilon-one coefficient is exactly

```
a^2u*tau^3/8 + a(4su)*tau^4/64 + (s^2u/128)*tau^5
 = u*tau^3(s*tau+4a)^2/128
 = u*tau^3 L^2/8.
```

The remaining contribution is the first epsilon derivative of `B(epsilon)^2`
where `B(0)=L^2`; it is `2L^2 B'(0)`.  Therefore the *complete* first
correction is divisible by `L^2`.  No unmentioned relation at higher order is
needed.

## 2. Complete mode/order census

Write

```
epsilon^-4 F = L^4 + epsilon*f1 + epsilon^2*f2 + ...,
L^2 | f1,
```

with no assumed `L`-divisibility for `fi`, `i>=2`.  The mode

```
c_m t^m F^((12-m)/8)
```

is born at relative epsilon delay `m/2` and has leading `L`-power
`(12-m)/2`.  Enumerating only monomials with nonzero generalized-binomial
coefficient gives the following exact minima through relative order four:

```
m=0:  order 0..4 -> 6,4,2,0,-2
m=2:  order 1..4 -> 5,3,1,-1
m=4:  order 2..4 -> 4,2,0
m=6:  order 3..4 -> 3,1
m=8:  order 4    -> 2
```

These are all modes that can occur by order four.  In particular, every
mode is regular through order three.  At order four the pure `F^(3/2)` mode
can first have `L^-2`, and the `c2` mode can first have `L^-1`; all newly born
or corrected `c4,c6,c8` terms remain regular.  Hence **relative order four is
indeed the first possible face-pole discriminator**.  This is a possibility
statement: additional order-four identities or cancellation could still
remove those poles.

## 3. Scope and checker clarification

The producer checker correctly proves the two displayed minima for the pure
and `c2` modes and checks the birth terms of `c4,c6`.  Its prose says it
"enumerates every partition contributing through relative order four," but
it does not explicitly enumerate the order-three/order-four corrections of
`c4,c6` or the birth of `c8`.  This is a checker-coverage overstatement, not
a mathematical error: the missing rows are `2,0`, `1`, and `2` respectively
and are all nonnegative.

The independent checker below fills that small gap, accounts for vanishing
binomial coefficients, and confirms the full table.  Its factor-coefficient,
weakened-`L|f1`, and omitted-mode mutations all fail.

```
python3 cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_first_correction_review_20260828/verify_unit_s_first_correction_review.py
```

Expected marker:

```
PASS_INDEPENDENT_UNIT_S_FIRST_CORRECTION_REVIEW
```

The conclusion remains local and face-theoretic.  It neither proves
order-four polynomiality nor enforces the global raw windows or endpoint.
