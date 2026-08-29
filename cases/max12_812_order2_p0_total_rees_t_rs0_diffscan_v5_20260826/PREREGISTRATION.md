# Preregistration: derivative-scan streaming `T-rs-0`

Date: 2026-08-26

Status: **NAVIGATION-ONLY SOFTWARE ACCELERATOR. NO REES, CHART,
MOVING-`p`, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

The frozen streaming V2 detects dependence on each of 76 candidates and
seven inactive-custody atoms using 581 exact substitutions.  The V3/V4
degree-scan experiment failed closed: V3's postcondition was overbroad and
V4 established that Singular 4.3.2 does not accept a variable as the second
argument of `deg`.  Neither failure produced a mathematical result.

V5 replaces exactly those 581 statements by

```text
diff(TPhi,x) != 0.
```

This is equivalent to dependence on `x` here.  Every frozen tail monomial
has coefficient-factor count at most nine and at most one load.  Each literal
source coefficient has total degree at most eight in the tested atoms.
Consequently each tested atom has exponent at most 72 in every emitted row;
the separate target terms have exponent one.  Thus formal differentiation
has kernel exactly the `x`-independent polynomials in characteristic zero and
in each allowed prime `32003`, `65521`, or `1000033`.  The compiler rechecks
the factor/load census and rejects any positive characteristic at most 72.

All other source text is byte-emitted by frozen V2.  V5 must agree at both
good primes with completed V2 before it can accelerate manifest discovery.
Exact Q plus a fresh prime and the actual Rees/base-change gate remain
mandatory.
