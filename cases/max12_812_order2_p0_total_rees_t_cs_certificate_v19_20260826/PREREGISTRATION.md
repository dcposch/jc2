# T-cs ordered-chart explicit unit certificate V19

Date: 2026-08-26

## Claim under test

V18R1 provisionally found that the exact-Q and F65521 ideals

```text
RawSpecial = (E10--12,Tg14_5,qrs,rho,1-u*cs,1-v*k)
```

are unit ideals after the literal T-cs substitution

```text
rs=cs*qrs,  c0=cs*qc0,  c1=cs*qc1.
```

V19 independently recomputes that positive test from the same frozen V9 and
V17 inputs and asks Singular for a lift of `1` through the 26 ordered raw
generators.  Acceptance requires matrices `L` and `U` with

```text
matrix(ideal(1))*U - matrix(RawSpecial)*L = 0
```

and with the single entry of `U` a nonzero constant.  Thus division by that
constant gives an explicit polynomial membership certificate for
`1 in RawSpecial`.

## Frozen construction and controls

- The V18 compiler is hash-pinned and its three-name V18R1 collision repair
  is replayed before the certificate-only tail is installed.
- The resulting script must contain the literal 22 upstream equations, four
  localization/special-fibre generators, an ordinary polynomial ring, and no
  qring.
- The lift residual is checked inside Singular before any PASS token or
  artifact write.  The raw ideal, lift matrix, and lift-unit matrix are all
  written and hashed.
- Exact Q runs on r6c.  F65521 runs independently on r6b as an encoding and
  software control; it is not evidence for characteristic zero by itself.
- Any source-freeze, compiler, engine, residual, constant-unit, artifact,
  resource-log, or validator failure is no verdict.

## Scope

A PASS supplies an explicit certificate for the same narrow V18R1 statement:
rho is a unit on
`V(rs/cs) intersect D_+(cs) intersect D(k)` for the grade-10--12 prefix plus
the complete fifth-row grade-14 equation.  It does not close later ordered
charts, the terminal receiver, `k=0`, Gate T, order two, maximum twelve, or
JC2.  V19 does not independently re-extract the upstream V9/V17 coefficients.
