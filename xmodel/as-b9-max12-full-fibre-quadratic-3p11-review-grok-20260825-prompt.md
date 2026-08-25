# Hostile review prompt: B9 first quadratic full-family gate

Audit the producer report
`xmodel/as-b9-max12-full-fibre-quadratic-3p11-producer-20260825.md` and case
`cases/as_b9_max12_full_fibre_quadratic_3p11_20260825/` without trusting its
claims.

Charge, independently and fail-closed:

1. the transitive source hashes and the exact `3^10 -> 3^11` divided equation,
   including why the stored divisor is `3^5` after the outer `243`
   predivision;
2. completeness of all 165 predecessor parameters, 182 fresh digits, and
   276 determinant rows;
3. invertibility of the active/spectator coordinate change and ranks
   18, 56, 108;
4. construction of the fresh left cokernel and the coefficientwise
   containment certificate (raw coefficient rank 16; augmented rank 56;
   zero residual equations);
5. the exact cardinalities `3^109` and `3^183`, distinguishing finite-set
   parameter counts from any unproved scheme/global statement;
6. literal integer replay modulo `177147`, actual degree pairs `(12,12)`,
   and the Z3/Boolector model cross-check;
7. the V2/V3 negative controls and strict one-parent/full-D12 refusal scope.

Do not run heavy computation locally.  Any substantive replay must run on
AWS with exact custody.  Distinguish source/compiler correctness from two
source-identical host replays and from solver agreement on the already
eliminated formula.

Write the verdict to
`xmodel/as-b9-max12-full-fibre-quadratic-3p11-review-grok-20260825.md`.
