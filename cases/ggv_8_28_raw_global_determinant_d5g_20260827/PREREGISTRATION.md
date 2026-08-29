# Preregistration: D5G review-independent raw global determinant path

Date: 2026-08-27

## Frozen question

Implement only the D4R1-independent half of the held D5 design.  Starting
from D3's frozen literal raw `2S/3S` slots and the exact leading rows

```text
H=X^8-1, F0=H^2, G0=H^3,
```

compile the global determinant coefficients `D0,...,D22` directly in the
raw coefficient ring, preserve every contributing raw-row pair, and freeze
the unique decompositions

```text
D22=H*Q22+R22, deg_X R22<8,
D22=M(Y22)+rM22, deg_X rM22<7,
M(Y)=4H Y'+6H'Y.
```

No local Morse result, source equation, branch pattern, or face claim may be
consumed.

## Ring and representation

Let `C=Q[all 400 positive-weight D3 raw slots]` and `S=C[X]`.  A sparse term
is stored as

```text
(sorted tuple of zero, one, or two raw slot names; X degree) -> Q coefficient.
```

The coefficient tuple is the literal monomial in `C`.  Fixed leading-row
terms have an empty tuple; linear terms have one slot; positive/positive
pairs have two slots.  Every final determinant term additionally records all
pre-combination contributions `(weight i, weight j, derivative side,
source X degrees, rational coefficient)`.

## Authoritative recurrence

For `0<=n<=22`, compute only

```text
D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j').
```

This is the coefficient of

```text
12F_XG-8FG_X-t(F_XG_t-F_tG_X).
```

All polynomial arithmetic and divisions are exact over `Q`; `H` is monic,
so division in `C[X]` uses no localization.

## Controls

1. Recombine `H*Q22+R22` term-for-term to the literal `D22`.
2. Recombine `M(Y22)+rM22` term-for-term to `D22`.
3. Add the fixed polynomial `H` to `D22`; require unchanged `R22`, quotient
   `Q22+1`, and a changed `M` seven-vector.
4. Delete one named raw slot and require the direct determinant digest to
   change.
5. Replace the recurrence coefficient `(i-8)` by `(i-7)` and require a
   changed determinant digest.
6. Require `D0=0` from the exact square/cube leading rows.

## Dependency lock and scope

The prospective D4R1 naturality square is recorded as
`LOCKED_PENDING_FRESH_HOSTILE_REVIEW`; this compiler neither reads D4R1's
result nor asserts `D0=...=D21=0`.  It emits no target verdict.

A PASS proves only literal global determinant compilation, raw provenance,
and exact `H`/`M` decompositions.  It does not prove a Keller specialization,
`R22=1`, `Q22=0`, a local/global commutative square, an `8_28` face/family
exclusion, `G2-PSC`, `G2-BD`, a Keller pair, a counterexample, or JC2.
