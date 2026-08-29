# Registration: D1 `a=8` complete `k6`/`mu2` transition

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS PRODUCER.**

## Two exhaustive `k6` sections

On the reviewed generic-square chart `D(p*k10)`, fix

```text
ord(A)=8, ord(C)=9, ord(R)>=8.
```

Write `k6=k60+sigma*k61+sigma^2*k62+...` and split:

1. `D(k60)`: absolute grade 26 is only the simple-pole module
   `[(3/4)k60*C0/L]_-`.  Its first two denominator coefficients must be
   exactly `(3/4)k60*c1,(3/4)k60*c0`; seven-row vanishing then contradicts
   nonzero `C0` contact.
2. `V(k60)`: write `k6=sigma*k61+sigma^2*k62+...`.  Grades 27/28 have

   ```text
   U0+S0 ; U1+KRC+S1+target(mu2).
   ```

   The first numerator is `C0*(A0+k61)`.  The grade-28 `mu2` source row is
   retained exactly.  Under inverse Faber transform it has coefficients

   ```text
   h2=-mu2, h4=(p/2)mu2, h6=-(p^2/4)mu2,
   ```

   so its cleared `L^2` numerator is `-mu2*L` and vanishes at either root.
   The moving `U1/S1` connections cancel at the shifted-A root, leaving the
   nonzero `C0^2` residue.

These sections include `k6` identically zero and every positive valuation:
`k61` and `k62` may specialize to zero.  No unbounded valuation
substitution is used.

## Acceptance

Both sections compile directly from all seven frozen source tails, all loads,
and all targets.  Exact quotient extraction, support filters, moving
`T0+T1` row bridge, denominator recurrences, target inverse, two root
orientations, and deletion controls must pass.  Run exact Q on Box03 and
`F_65521` on r6d, each capped at 24 GiB, 600 seconds compile, and 1800
seconds Singular.  Fail closed on timeout, nonzero rc, marker mismatch,
`=FAIL`, `// **`, leading `?`, or `error occurred`.

## Firewall

This is only fixed `a=8` on `D(p*k10)` after the reviewed first-normal,
half-weight, and `M=0` gates.  It gives no a>=9, p=0/k10=0,
positive-order-k10, zero/infinity, fan, scheme, whole-square, order-two,
`(8,12)`, maximum-twelve, or JC2 conclusion.  It must remain compatible
with the exact all-load Chebyshev/Pell survivor.

