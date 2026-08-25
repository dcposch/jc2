# Hostile review prompt: global Q9 projection of the AS row-8 scalar

Review the frozen producer and case adversarially.  Do not trust report prose,
hard-coded expected totals, stored ranks, or producer assertions.  Do not edit
producer/case/ledger bytes.

Primary report:

`xmodel/as-fonly-d7-global-row8-q9-projection-producer-20260825.md`

Case:

`cases/as_fonly_d7_global_row8_projection_20260825/`

Required output:

`xmodel/as-fonly-d7-global-row8-q9-projection-review-grok-20260825.md`

## Charges

1. Pin the consumed corrected Q10-to-Q9 compiler at SHA-256
   `54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2`.
   Check that the 79 compatible structural bases and every accepted Q10
   source state are covered; the old one-predecessor 13-trit chart must not be
   substituted.
2. Audit the preregistration erratum.  From
   `(q1,q2,q3,q4)=(c2_1,c2_2,d2_0,d2_1)` and `C_x+D_y`, derive independently
   which carry is the `x` coefficient and which is the `y` coefficient.  Check
   the corrected formula
   `omega=carry(q1+2q3)+2h*carry(2q2+q4) mod 3`.  Classify the frozen V1
   swapped-label run as a negative control, not evidence.
3. Inspect corrected V2 source SHA `8d1b070c...` and V3 source SHA
   `c0951aaf...`.  Check that on every projected tuple each reconstructs the
   literal integer source expression `E/3+M`, reads its two linear
   coefficients with the stated monomial orientation, and asserts agreement
   with the closed formula before counting.
4. Audit the affine projection and multiplicity calculation.  Verify exact
   Q9 RREF/kernel construction, projection to four coordinates, image-basis
   enumeration of at most 81 points, and the factor
   `3^(kernel_dimension-projection_rank)`.  Look for multiplicity loss,
   duplicated image points, inconsistent-system leakage, or wrong rank keys.
5. Independently aggregate the frozen 27 V2 and 27 V3 shard payloads.  Require
   27/27 rc zero for each, disjoint ordered structural ranges, equal ordered
   stream digest, 79 compatible bases, and exact reproduction of Q10 count
   33,225, nonempty Q9-state count 11,881, and completion total
   8,096,356,425,843.  Do not accept these merely because the aggregate script
   hard-codes them as assertions.
6. Check V3 rank-pair/fibre-size controls and the exact uniform histogram
   `omega=0,1,2 = 2,698,785,475,281` each.  Verify that every one of the
   11,881 nonempty fibres is classified `zero-partial`, not only that the
   global histogram is uniform.
7. State the strongest licensed conclusion plainly: `omega` is no obstruction
   at Q9 alone and each current nonempty Q9 fibre has `omega=0` completions.
   Refuse any claim that those completions satisfy Q8 through Q3 restoration,
   give a complete mod-243 map, lift all-depth, yield a counterexample, or
   affect JC2.
8. Audit custody and distinguish separate corrected executions from a truly
   independent implementation.  Note any self-hash/snapshot noise or
   incomplete transfer bytes, but do not elevate non-load-bearing custody
   nits to mathematical defects.

Do not run Bash, Python, CAS, or solvers on the local Mac.  A no-shell
source/mathematical review is preferred.  If substantive replay is needed,
run it only on AWS and record host, immutable job path, source hashes,
commands, rc, stdout/stderr hashes, and resource use.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`, classifying each
issue as mathematical, source-typing, software, custody, or wording/scope.
