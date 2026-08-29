# Preregistration: DEP-D3 cleanup DAG D4R1 type repair

Date: 2026-08-27

## Additive custody

This new case repairs, without mutating, the quarantined D4 freeze
`8a79c549...`.  D4 incorrectly labelled the `X`-dependent precursor
remainder `t^14 X-t^16/4` as the final Morse critical-value series.  D4R1
retains D4's generic factor-local cleanup construction but accepts the
five-row discriminator only after an exact evaluation of that cleanup DAG.
It depends on D3 (`DEP-D3`) and rolls back if D3 review changes its input.

## Corrected discriminator

In `Q[t,X]` define

```text
u_pre = H+t^6 X-(1/2)t^8,
R_pre = t^14 X-(1/4)t^16,
F = u_pre^2+R_pre
  = H^2+2t^6 H X-t^8 H+t^12 X^2.
```

`R_pre` is explicitly *not* the final Morse `U(t)`: it still contains the
local variable `X=c+z`.  All five surviving positive-weight rows must first
replay against the literal D3 raw support.  Then the generic cleanup DAG is
evaluated exactly under those five raw coefficients in

```text
A=Q[c]/(c^8-1).
```

The discriminator passes only if the resulting critical-value coefficient
is exactly `U_14=c`, encoded by the `A` vector `(0,1,0,0,0,0,0,0)`.  The
sparse precursor identity alone is insufficient.

## Generic cleanup contract

As in D4, fix `F0=H^2`, `G0=H^3`, retain all 400 positive-weight D3 raw
slots as leaves, solve `F_X(c+s,t)=0`, and compile every coefficient through
weight 22 of `U,W,V,Q,Gamma`.  Internal expression nodes are exact
`ConstA`, `Raw`, `Add`, or `Mul` nodes.  All series inversions must display a
constant unit in `A`; no raw-variable inversion is permitted.

The four factor IDs, the chart, the deck tag, orientation `u=H mod t`, and
determinant `H'(c)` are mandatory.  This is factor-local formal algebra and
not a global polynomial automorphism.

## Mutations and scope

Mutating either precursor sign, deleting a supporting row, inserting the
nonexistent raw `F14:X`, or replacing the required exact `U14=c` comparison
by the precursor remainder must fail.

No D4R1 result may claim a Keller specialization, a global polynomial
`E22`, global `H`-multiple control, an `8_28` face/family exclusion,
`G2-PSC`, `G2-BD`, a Keller pair, a counterexample, or JC2.  No descendant
may consume D4R1 before fresh hostile review.
