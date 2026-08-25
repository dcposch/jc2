# Hostile bounded review: TD6 V67 finite B3 factor source DAGs

Act as an adversarial algebra/source/custody reviewer.  This is bounded and
read-only.  Do not edit producer/canonical files or rerun the substantive
CAS/Python replay.  You may hash files, extract the 100-KiB source archive in
private `/tmp`, inspect source/text, and run the tiny custody verifier.

Read in full:

- `xmodel/td6-c1-c2-c3-q2-b3-finite-factors-v67-aws-20260825.md`;
- `cases/td6_c1_c2_c3_q2_b3_finite_factors_v67_aws_20260825/README.md`,
  `MANIFEST.sha256`, `FREEZE.sha256`, `verify.py`, all evidence, and the
  portable source archive;
- the V66 and V68 producer/review reports named by the V67 report, only as
  needed to audit factor provenance and scope.

Verify or refute:

1. The exact source components are `2t-1=0` and `t^2-4t+2=0` in the fixed
   source-typed A3 q2-beta section.  Check the center parameterization and
   its inverse, raw B3 identity, coefficient-field degrees, and that `t` is
   nonzero and not 2 on both components.
2. Distinguish the curve parameter `w=V0/U0` from raw center `U0`.  The
   implementation's polynomial generator `x` and legacy `U_POLY` denote
   `w`.  Confirm that the asserted scope is D(w), not a secretly enlarged
   raw-U chart, and that w=0 maps to the origin without the package consuming
   an origin theorem.
3. Source fidelity: polynomial beta, direct
   `q_beta'=1+2 beta t+25 t^24`, fixed p-boundary/dead stretch/F1/pole data,
   and no weighted scaling.  Check staged ranks and exact component-field
   use rather than point sampling.
4. N13 ancestry: current row 13 goes through exactly previous row
   `('X-1',14)` and original first rows.  `('X-1',0)` may appear as a cache/
   quadratic control only, never as a second N13 edge.  Audit omission
   controls and source-row versus echelon provenance.
5. Genuine P12: 28 original first rows; 2,893 raw terms on `2t-1`, 2,885 on
   the quadratic factor; exact P12/N13 glue to `-k/50`.  Check direct-q-prime
   and varying-echelon contributions and sign conventions.
6. Denominators: inspect every emitted DAG leaf and staged/chart factor.
   Confirm radical support only w, stage w^11, complete charts w^27/w^23,
   with no hidden t/factor/norm/pivot divisor.
7. Custody: source closure, four rc-zero theorem runs, dual Box02/Box03 DAG/
   ledger equality, normalized whole-stream equality, manifests/freeze, and
   both rc-one q-prime omission controls.  The reporter IndexErrors are
   negative controls only.
8. Scope: exactly the two factor opens D(w), for all beta, in fixed A3 q2.
   No whole factor, whole B3, whole A3, TD6, SP-2, landing, or JC2 claim.

Try to flip the theorem through an incorrect curve field, missing point at
infinity, invalid inverse, w/raw-U confusion, hidden norm denominator,
forbidden row0 ancestry, synthetic P12, path-only normalization hiding a
real difference, failed-control contamination, or scope drift.  Separate
mathematical defects from custody/expository nits.

Write `xmodel/td6-c1-c2-c3-q2-b3-finite-factors-v67-review-grok-20260825.md`
and end with exactly one verdict token on its own line: `CONFIRMED`,
`CONFIRMED_WITH_REPAIRS`, or `FAILED`.
