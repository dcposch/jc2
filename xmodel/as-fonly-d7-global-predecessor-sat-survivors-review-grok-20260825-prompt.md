# Hostile review charge: three AS global-predecessor SAT survivors

Write the review to
`xmodel/as-fonly-d7-global-predecessor-sat-survivors-review-grok-20260825.md`.

Audit the producer report
`xmodel/as-fonly-d7-global-predecessor-sat-survivors-20260825.md` and the
frozen case
`cases/as_fonly_d7_global_predecessor_sat_survivors_20260825/` against its
pinned transitive source closure.  Do not infer correctness merely from SAT
or from the producer replay.

Charges:

1. Verify the 79-base structural pin decoding and, specifically, bases
   303/`0102020`, 513/`0201000`, and 519/`0201020`.
2. Inspect source-to-formula compilation of all 20 predecessor rows, corrected
   5/12/11 top rows, raw 23 Q9, 22 Q8, 19 Q7, and 46 degree-12-through-9
   terminal rows.  Check every exact division gate and bit-vector bound.
3. Independently parse at least one SAT model and reconstruct the literal
   integer source.  Verify all charged rows, recursive/literal `/243`
   agreement, and terminal zero.  Compare exact hashes with the frozen model
   and replay.
4. Determine whether the three SAT states are genuinely distinct and whether
   any model/parser default, omitted variable, modular wraparound, or stale
   source can create a false positive.
5. Enforce exact scope: these are filtered Q9/Q8/Q7 terminal-gate states.  The
   parent formula does **not** reimpose final G8 after Q7 and does not include
   Q6/H7,J7 or degrees 8/7.  Therefore SAT here is not a mod-81 map, a lower-row
   completion, an all-depth lift, a counterexample, or JC2 evidence.
6. Separately inspect the pointwise successor report
   `xmodel/as-fonly-d7-sat-survivor-q6-high-pointwise-20260825.md`: confirm the
   final-G8 rows on all three points and base519's 70-by-16 rank pair and
   sparse left-null certificate.  Do not turn those pointwise deaths into a
   whole-fibre/base theorem.

Return `CONFIRMED`, `CONFIRMED WITH NONBLOCKING CORRECTIONS`, or `BLOCKED`,
with exact defects and the smallest repair.  If running substantive replay,
stage it on AWS under an immutable tag and report host, source hashes, return
code, stdout/stderr hashes, runtime, and memory; do not run CAS locally.
