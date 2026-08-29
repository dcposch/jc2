# Preregistration: D1 target-free primary-C2 cell, `3<=c<=7`

Date: 2026-08-26

Status: **PREREGISTERED FINITE-THRESHOLD MAXIMAL-POLE PRODUCER.**

## Exact scope

Work only on the unit-load generic-square chart

```text
D(p*k0), ord(C)=c, 3<=c<=7,
ord(A)>=c, ord(R)>=c-1.
```

These inequalities are exactly the integral primary-`C2` lower cell for
the five unit-load horizontal weights.  The proof must not import the hand
support triage as a source theorem.

## Source ceiling and thresholds

For each integer `c=3,...,7`, independently enumerate all four frozen
binomial summands through absolute grade `T=10+2c`, at the boundary contacts
`a=c,r=c-1`, and repeat with padded cost bounds.  Expected boundary source:

```text
c=3: AC, C2, R3, RC, all at grade 16;
c=4,5,6: AC, C2, RC, all at grade 10+2c;
c=7: AC, C2, RC, k6*C, all at grade 24.
```

Every target begins at grade 28 or later, and `k2` must be absent through
the registered ceilings.

Raising `a` or `r` from the boundary may only delay families with positive
`A` or `R` exponent.  The producer must record this monotone source bridge;
it may not infer a closed tail from exact-contact density.

## Maximal-pole functional

At grade `T`, reconstruct the canonical pole-two numerator `N2` modulo
`L^2`, with `L=z^2+p/2`, from all seven literal rows and an independently
assembled analytic source.  On the finite etale root cover
`p=-2*lambda^2`, require the derived Faber pair

```text
N2(+lambda)=(3/8) C(+lambda)^2,
N2(-lambda)=(3/8) C(-lambda)^2.
```

All `AC`, `RC`, `R3`, and `k6*C` contributions have pole one and hence
carry a factor of `L` in the cleared pole-two numerator.  The coefficient charts
`D(c1)` and `D(c0)` must exhaust exact nonzero linear `C` and both localized
ideals must contain `1` before radicals.  Omitting the `C2` column must make
both root terminals zero.

## Acceptance and firewall

Run exact `Q`, `F_65519`, and `F_65521` on three AWS hosts with fresh tags,
ordinary polynomial rings, fail-closed validators, immutable custody, and
zero swap.  A PASS may close only the displayed target-free primary-`C2`
cell.  It says nothing about `c>=8`, any non-`C2`
primary/equality cell, positive-order leading load, `p=0`, `k0=0`, the
exact-square zero section, terminal/global charts, fan exhaustiveness,
order two, maximum twelve, or JC2.

The excluded `c=8` boundary is a required negative control, not an omitted
case: `k6*C/L` first occurs at grade 25, so its grade-26 moving-connection
prolongation contributes a pole-two term proportional to
`-ell1*k6*C/L^2`.  The grade-26 root functional is therefore not the pure
`(3/8)C^2` square used here.  That load/connection wall needs its own
successor.
