# TD6 V83 producer theorem — explicit generic FIRST principal open

Date: 2026-08-26

Status: **PRODUCER-EXACT; DUAL AWS; HOSTILE REVIEW PENDING.**

Over the fixed source-typed A3 presentation and coefficient field
`K=E(C,V,U)`, the packed FIRST matrix has rank 38 on the explicitly certified
principal open

```text
D(U * H * B3 * R38),

H   = C-3U^2,
R38 = C*V^2*U + 8*C*U^4 - (1/2)*V^4
      - 7*V^2*U^3 + 8*U^6.
```

Indeed, the source-replayed 38-pivot minor factors, up to a nonzero constant
field unit, as `U^3*H*B3*R38`; clearing the complete packed-matrix denominator
contributes only `U*H`, so the recorded principal-open polynomial factors as
`U^4*H^2*B3*R38`.

Both r6d and Box03 returned rc zero from source archive SHA-256
`881c76cf9cbc3d8b10d6820dad95f366f8f5038c3fe08643ba6ed5c44a75d71f`.
Their pivot, factor, and raw-successor ledgers are byte-identical at SHAs
`475d9ed0...`, `bb990f4f...`, and `56e9c202...`; their mathematical stdout is
identical after removing only host and run-tag lines.  Every one of the 38
pivot source combinations replays.  Pivot omission, plus-one, and rank-37
negative controls all fire.

The extra divisor `R38=0` is an unresolved raw-fibre/alternate-minor debt.  A
selected minor vanishing there does not prove the matrix rank drops there.
Thus this theorem narrows the reviewed generic-FIRST-surjectivity corollary to
the displayed explicit open; it does not identify that open with
`D(U*H*B3)` and gives no claim on `R38=0`.

The immutable evidence case is
`cases/td6_c1_c2_c3_first_rank_open_v83_aws_20260826/`.  Its lightweight
custody verifier passes without rerunning algebra.  Scope remains
first-order, fixed presentation, and generic center only: no quadratic
persistence, nonlinear family, full TD6, SP-2, or JC2 result follows.
