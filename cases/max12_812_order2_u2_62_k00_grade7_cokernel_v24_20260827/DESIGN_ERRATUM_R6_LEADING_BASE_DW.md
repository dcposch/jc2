# V24R6 pre-algebra design erratum

Date: 2026-08-27

Status: **FAILED CLOSED BEFORE SOURCE FREEZE, AWS EXECUTION, OR TARGET
ALGEBRA.**

The frozen-content R6 draft
`PREREGISTRATION_R6_LEADING_BASE_DW.md` (SHA-256
`914e037406be3d121974fd7666ba55144b5ae3b9593af80408bf0e988eb16340`)
and its first compiler draft (SHA-256
`1513f48790bc49b2f470ef459b659d8458f7865c8d7ac1b098376b151eaa12ff`)
are retained as failed design history.

Two syntax-safe toy controls exposed the defects:

1. Singular removes the literal zero entry when constructing an ideal, so
   `ideal B=Q1,...,Q6,F10,z*W-1` has seven entries when `Q6=0`, not eight.
2. `lift(B,ideal(1),U,"slimgb")` is not a two-outcome membership API.  When
   `1` is not in `B`, Singular reports that the second module is not contained
   in the first rather than returning a typed nonunit fallback.

Consequently R6 could not honestly reach its intended proper branch.  No R6
source manifest was frozen, no R6 AWS job was launched, and no mathematical
result was produced or consumed.

R6R1 repairs the control flow by first using an exact standard basis only to
choose the branch.  It invokes direct `lift` only after exact unit detection;
on the proper branch it invokes tracked `liftstd`.  It treats the actual ideal
as seven generators while serializing the logical eight-slot certificate with
the `Q6` slot explicitly zero.
