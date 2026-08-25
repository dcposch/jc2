# Hostile bounded review: TD6 V71 fixed-A3 whole-H composition

Act as an adversarial algebraic-logic and scope reviewer.  This is a bounded,
read-only review.  Do not edit producer/canonical files, invoke CAS/solver/
Lean/heavy Python, or rerun the four substantive source producers.  You may
hash files, inspect text, and run the tiny V71 Boolean/custody verifier.

Read in full:

- `xmodel/td6-c1-c2-c3-q2-h-complete-cover-v71-20260825.md`;
- `cases/td6_c1_c2_c3_q2_h_complete_cover_v71_20260825/README.md`,
  `DEPENDENCIES.sha256`, `MANIFEST.sha256`, `FREEZE.sha256`, and `verify.py`;
- every producer and hostile-review report listed in `DEPENDENCIES.sha256`:
  V64, V62D, V65, and V70.

Verify or refute:

1. All dependencies are immutable/hash-correct and each hostile review ends
   `CONFIRMED` at the exact leaf scope consumed by V71.
2. The five leaves really cover every point of `H=0`:
   V70 on `U=0`; on `D(U)`, V62D on `V=0`, V65 on `P3=0` or `QH=0`, and
   V64 on `D(V*P3*QH)`.  Look for missing intersections, direction errors in
   `D(...)`, or an illegal specialization of a fraction-field certificate.
3. Every leaf uses the same fixed source-typed A3 `(C,V,U)` q2-beta section,
   retains direct q-prime/polynomial beta as required, and proves an
   original-row unit/incompatibility statement strong enough for the stated
   union.  Do not silently identify the internal curve parameter with raw U.
4. The P3/QH Bezout identity is correct but logically optional; V71 must not
   rely on disjointness to cover an intersection.
5. The old V33/V69 whole-U scope defect is genuinely repaired by reviewed
   V70 before the `U=0` leaf is consumed.
6. The conclusion is exactly: no normalized compatibility solution anywhere
   on `H=0` in this fixed A3 q2-beta section, for every beta.  It is not
   `H!=0`, whole A3, another modulus, TD6, SP-2, landing, or JC2.

Try hard to find mismatched H/P3/QH definitions, an unreviewed leaf, a field
or extension mismatch, a point omitted by the Boolean split, or scope drift.
Separate a mathematical failure from documentary/custody nits.

Write `xmodel/td6-c1-c2-c3-q2-h-complete-cover-v71-review-grok-20260825.md`
and end with exactly one verdict token on its own line: `CONFIRMED`,
`CONFIRMED_WITH_REPAIRS`, or `FAILED`.
