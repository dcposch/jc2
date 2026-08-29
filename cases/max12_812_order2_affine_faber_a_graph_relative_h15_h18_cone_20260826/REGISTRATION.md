# Registration: graph-relative delayed-`A` open band `15<H<18`

Date: 2026-08-26

Status: preregistered exact-support cone extraction; no source theorem before
predecessor composition and hostile review.

## Input and cell

Consume the frozen exact-Q/F65521 graph-relative support of
`K=E*H3+H5` after the corrected affine load-coordinate change.  Work on
`D(E*M)` with rational valuations

```text
15 < H < 18,
alpha=v(a) >= H/3,
q=min(v(U),v(V)) > 21-H,
v(R0,R1,S0,S1) >= 2q.
```

The leading affine graph is at grade 42.  Its transverse coordinates
`d6,d2,dm` have strictly positive excess above 42; `d4=mu4` has fixed
grade 48.  The intrinsic normal term has grade `3H`.

## Required exact check

For every one of the 365 collected exact-Q support terms, minimize at

```text
alpha=H/3, q=21-H, complements=2q,
d6=d2=dm=42, d4=48.
```

Prove by exact rational endpoint arithmetic that every nonintrinsic term is
strictly above `3H` throughout the open interval once the strict inequalities
in `q` and the graph deviations are restored.  Require that the only
non-strict new tie at the closed endpoint `H=18` is

```text
4*d4*a.
```

This endpoint is a routing wall, not part of the PASS cone.  The exact-Q
coefficient `-E*M^3*lambda^3/16` is the characteristic-zero unit;
F65521 supplies only the exponent-sequence control.

## Firewall

This client classifies support only after the grade-42 affine predecessor
and for `q>21-H`.  It does not prove the `q<21-H` quadratic block, the
equality `q=21-H`, source-to-chart coverage, the `H=18` target tie,
`18<H<21`, another center/load slope, factor degeneracies, total Rees,
order two, maximum twelve, or JC2.  Run only on AWS.
