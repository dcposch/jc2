# Hostile review request: K00 exact filtered compatibility through D8

Independently adjudicate the narrow exact-Q V10 claim.  Do not use producer
`PASS`, `ENDPOINT`, validator, or status strings as mathematical evidence.

## Frozen claim

At `C6=1`, with `m=(d0,...,d5)` and unloaded frozen tails `r1,...,r7`, the
complete cumulative multiplier system through transverse normal degree 8
has rank equal to augmented rank 2547 and a replayed rational solution.
Equivalently,

```text
r7 in (r1,...,r6) + m^9.
```

Nothing stronger is charged.

## Required independent attacks

1. Rehash and type-check the frozen tail source, V9 emitter, V9 exact D7
   result, V10 preregistration, and V10 freeze.  Re-expand the seven unloaded
   rows in the registered K00 transverse chart; do not consume serialized
   rows without reconstructing their source map.
2. Independently emit the complete cumulative D8 map: all multiplier
   monomials of degree at most 6 for each of rows 1--6, and every target
   equation in normal degrees 2 through 8.  Confirm the shape
   `2996 x 5544`, column/row ordering, denominator custody, and matrix SHA
   `15837b4e24431a61e4cc8f2498bc4cd27959b03b6150f76609b319c1dcbabc30`.
3. Over exact `Q`, independently compute or certify
   `rank(A)=rank([A|r7])=2547`.  Do not infer characteristic zero from the
   finite-field lane.
4. Parse the saved rational multiplier jet
   `0b29e3cc3485b39370ed59a8833328b51d469e104eed6edcfabc3d6f5fadb360`
   and replay all 2,996 equations coefficientwise against an independently
   emitted matrix.  Confirm 492 nonzero entries.  Check the D2--D7 prefix
   equations as a regression against reviewed V9.
5. Treat the byte-identical `p=65521` matrix, rank, and modular lift only as a
   software control.  Attack bad-prime leakage, a swapped RHS, truncated
   multipliers, row/column-order mistakes, false sparse-solution parsing, and
   rank-versus-augmented-rank confusion.
6. Reconcile the result with reviewed V8 global nonmembership.  Explicitly
   reject any inference from D8 compatibility to polynomial, local, or
   formal membership, or to existence/nonexistence of a finite obstruction.
   The failed V11--V13 local-transform producers are not evidence for V10.
7. Enforce the firewall: loads are zero and `C6=1`; no `Lambda`, load,
   target, `mu`, `Jdet`, closure-first incidence, Taylor realization,
   receiver, order-two, maximum-twelve, or JC2 conclusion is licensed.

## Charged paths and hashes

```text
cases/max12_812_order2_u2_62_k00_filtered_macaulay_d8_v10_20260827/RESULT.md
cases/max12_812_order2_u2_62_k00_filtered_macaulay_d8_v10_20260827/aws_q_box01_pass/
cases/max12_812_order2_u2_62_k00_filtered_macaulay_d8_v10_20260827/aws_p65521_box02_pass/

exact RESULT.json  cc2bed36104932b731c1408b3ab7af635cdc86a2162cf8026db0dc1c4a4b852a
mod-p RESULT.json  3f70961e92c6fbba2fe236cf6f06ae70ec762f3adb5c7675e7c98b5c0a238389
matrix             15837b4e24431a61e4cc8f2498bc4cd27959b03b6150f76609b319c1dcbabc30
exact lift         0b29e3cc3485b39370ed59a8833328b51d469e104eed6edcfabc3d6f5fadb360
V9 exact report    bd1c636827061f1506573487618e533f34cfe413eab042be65411bfaa2eef178
```

Return `PASS`, `REPAIR`, or `FAIL`; state the smallest failing identity or
missing hypothesis and the strongest exact statement that survives.

Write the complete report to exactly
`xmodel/max12-812-order2-k00-d8-hostile-review-opus5-20260827.md`.
Touch no other campaign artifact.  Do not enter, read, build, status-inspect,
or modify `jc2-lean`.  Desk-scale exact checks only; launch no AWS job, run no
heavy local CAS computation, perform no web sweep, and edit no canonical
ledger.
