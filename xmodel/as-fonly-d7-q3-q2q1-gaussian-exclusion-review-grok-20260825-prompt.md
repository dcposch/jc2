# Hostile review prompt: normalized Q2/Q1 Gaussian exclusion

Review the producer report and complete frozen case below.  Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`.  This is a source/compiler audit, not merely a check of stored Gaussian certificates.

Use read/search/glob operations only.  Do not use Bash, Python, a CAS, a
solver, web access, or network access; all substantive replay belongs on AWS.
Do not edit the producer, case, shared ledgers, or this prompt.  Write only
`xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-review-grok-20260825.md`.

## Inputs

- producer report: `xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-producer-20260825.md`
- case: `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/`
- reviewed Q3 parent report: `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-producer-20260825.md`
- reviewed Q3 parent review: `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-review-grok-20260825.md`
- exact transitive compiler anchors pinned by hash:
  - `cases/as_fonly_d7_q3_two_level_q2_q1_20260825/solve_two_level.py`
  - `cases/as_fonly_d7_q3_two_level_q2_q1_v3_branches_20260825/classify_branches.py`
  - `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_20260825/certify_all.py`

## Mandatory charges

1. Reconstruct the source formula and orientation from the literal integer determinant.  Check every exact division by 27 and 81 and the fixed 91-slot order.  Confirm that row 8 is `x^2 y`.
2. Verify that the parent entire-Q3-fibre parametrization is consumed, rather than one Q3 particular, and that the 63 over-cap rows of degrees 7 through 12 are retained among the 91 rows at each reached stage.
3. Verify the eight active first-carry coordinates, rank 5, and exact 27 accepted assignments.  Check that branching on those assignments and retaining every inactive coordinate is exhaustive for the displayed family.
4. Audit the complete quadratic design used to assert branchwise affineness at `/81`; check both pure `2e_i` and mixed `e_i+e_j` tests and the design counts 630/496.
5. Independently verify the 81 matrices/right sides and singleton row-8 left-null obstructions.  Check residual constants `2,2,1` in the report's convention.
6. Verify the V2 inclusion-minimal multirow omission controls by literal raw-digit reconstruction.  Confirm all `/27` rows and all retained `/81` rows vanish and at least one omitted row does not.  Preserve the V1 one-row-control failure as a negative control rather than silently weakening it.
7. **Load-bearing source-normalization charge:** determine whether arbitrary homogeneous degree-3/2 order-27 and order-81 digits really form the complete source-normalized derivative-effect cone.  In particular, decide whether degree-1 and constant digits at those orders are absent by a proved source/symplectic affine normalization, or whether they could alter the row-8 obstruction.  If this is not source-licensed, require theorem wording to remain “selected normalized digit family,” not “complete Q3 fibre exclusion.”
8. Check scope: the inputs are three fixed Q5 predecessor points, with all downstream displayed Q4/Q3 fibre coordinates.  They are not three whole structural bases and do not reduce the 79-base remainder to 76.

## Required output

State separately:

- correctness of the finite Gaussian/certificate theorem for the displayed family;
- correctness or failure of the claimed source normalization;
- the strongest licensed scope after that decision;
- any source, arithmetic, coverage, or custody defect;
- exact commands and hashes for any independent replay.

Do not infer an all-depth lift/no-lift, a characteristic-zero point, a counterexample, or JC2.
End with exactly one verdict token on its own line: `CONFIRMED`,
`CONFIRMED_WITH_REPAIRS`, or `REJECTED`.
