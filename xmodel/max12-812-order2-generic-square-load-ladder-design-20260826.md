# `(8,12)` order two: generic-square load-unit ladder

Date: 2026-08-26

Status: **SOURCE-TYPED TWO-GRADE AWS DESIGN; NO SQUARE-BRANCH OR
ORDER-TWO VERDICT.**

## 1. Charged scope

This design consumes the reviewed one-parameter source, first-normal
divisibility theorem, reviewed Padé support, and the matched square next-jet
navigation.  Work on the generic square open

```text
L=z^2+p/2,                 p!=0,
K=L^2,
N=L*(u3*z+u2).
```

The matched `Lambda^3` rows force `u2=u3=0` on reduced support.  Because the
first-contact chart is saturated by `(u2,u3,k10)`, the surviving open is
therefore `k10!=0`.  This implication is essential: `k10` is not inverted on
the whole square component, only after routing the nonzero-`M` branches
through the preceding grade.

Retain the next transverse coefficients exactly as

```text
K=L^2+Lambda*R,            R=cs*z+rs/4,
N=Lambda*S,                S=(v1*z+v0)/2.
```

Thus the degree-eight coefficient polynomial in the frozen normal chart is

```text
f=K^2+Lambda*N=K^2+Lambda^2*S.
```

All seven finite loads remain in the source.  Their scale factors are
`Lambda^2*k10`, `Lambda^6*k6`, `Lambda^10*k2`, and targets begin in grades
`13,...,19`.

## 2. Exact fourth-grade receiver

The binomial identities give

```text
f^(3/2)=K^3+(3/2)*Lambda^2*K*S
                 +(3/8)*Lambda^4*S^2/K+O(Lambda^6),
```

while every contribution of `Lambda^2*k10*f^(5/4)` through total grade four
is polynomial in `z`.  The `k6`, `k2`, and target terms occur later.
Consequently the negative part at total grade four is exactly

```text
[(3/8)*S^2/L^2]_- .                                  (2.1)
```

The compiler must recover (2.1) from the complete frozen seven-tail source,
not insert it in place of that source.  It then computes the raw ideal and
its radical on `D(p*k10)`.  Since `S` is linear, the expected reduced support
is

```text
v0=v1=0.                                             (2.2)
```

The raw quadratic thickness is retained for any conormal successor.

## 3. Exact fifth-grade receiver

Restrict only after the fourth-grade computation to `v0=v1=0`.  Then
`f=K^2` and the unloaded term is polynomial.  The first nonpolynomial
`k10` contribution is

```text
Lambda^2*k10*K^(5/2)
  = polynomial through grade four
    +Lambda^5*(5/16)*k10*R^3/L+O(Lambda^6).
```

Hence the total fifth-grade receiver is exactly

```text
[(5/16)*k10*R^3/L]_- .                               (3.1)
```

On `D(p*k10)`, the expected reduced support is

```text
cs=rs=0.                                             (3.2)
```

Indeed, writing `s=p/2`, `R=c*z+d`, the remainder of `R^3` modulo `L` is

```text
c*(3*d^2-s*c^2)*z + d*(d^2-3*s*c^2).
```

In characteristic zero the two coefficients have no common nonzero zero
when `s!=0`; the difference of the two ratio equations is the expected
`8*s` separator.  The AWS client must verify the conclusion directly over
`Q` and independently at a good prime.

## 4. Fail-closed endpoints

The compiler and engine must:

1. pin every charged byte and the canonical all-tail digest;
2. reconstruct all seven loaded source rows with their exact Lambda weights;
3. verify exact divisibility by `Lambda^4` after `u2=u3=0` and identity after
   division;
4. verify exact divisibility by `Lambda^5` after additionally setting
   `v0=v1=0`;
5. prove the two divided grades contain none of the forbidden later loads or
   targets;
6. compare the radicals with `(v0,v1)` and `(cs,rs)` by per-generator normal
   forms, never by an ideal-versus-scalar comparison;
7. print the raw nonreduced bases and all localization steps.

Run exact `Q` and an independent good-prime lane on AWS.  A modular endpoint
alone is navigation, not a characteristic-zero theorem.

## 5. Firewall and successor

This two-grade ladder concerns only the generic `p!=0` square chart after the
preceding reduced `M=0` gate.  It does not cover the degenerate core `p=0`,
the square/discriminant intersection, slower or resonant valuation ties, or
the higher-contact section obtained after (2.2)--(3.2).  In particular,
forcing `M=R=S=0` at these grades does not prove that a formal arc stays on
the fourth-power locus: higher coefficients can enter with larger weights.

The successor is a finite valuation/resonance atlas through grades 13--19,
including all three lower loads and the terminal row, followed by both
Taylor receivers.  No strict arc, square-component exclusion, order-two
closure, `(8,12)` closure, maximum-twelve theorem, or JC2 conclusion is made.
