You are the hostile different-model reviewer for one exact theorem-interface
composition in the JC2 campaign. Work in `/Users/dc/code/math/jc2`.

Producer under review:
`xmodel/as109-one-sided-prime4-composition-sol-20260827.md`
SHA-256:
`3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36`

Replay and manifests:

- `cases/as109_one_sided_prime4_20260827/replay.py`
  (`4413482ee6d518d85abaa85c609f1f3421c168496c2d40b6b9a9340a2d4ff73d`)
- `cases/as109_one_sided_prime4_20260827/HISTORY.sha256`
  (`569ee6510a581d89be3528681abeb48e890c005b52ad6b19c803a34b964fb986`)
- `cases/as109_one_sided_prime4_20260827/INPUTS.sha256`
  (`41d155803dd1bae23f060be5719152352247afd41b4098183a7b00083681ceb6`)

Do not accept the report by prose comparison. Recheck the load-bearing
interfaces independently:

1. Locate the hash-pinned primary source for Moskowicz,
   arXiv:1810.08202v2, Theorem 2.7. Verify the theorem's exact invariant,
   `{1,4} union primes` condition, constant-leading convention, and
   applicability over an arbitrary characteristic-zero field such as
   `Q_109`. Do not confuse this paper with the quarantined 2024 prime
   field-extension-degree manuscript.
2. Recheck that the cited reviewed Hensel result really makes every exact
   integral lift of `(x-x^109,y)` noninjective over `Q_109`, and that a
   polynomial automorphism over `Q_109` contradicts it.
3. Independently exhaust `n=deg_y Q=1,2,3,4,5` and the first residual
   `n=6`, including `deg_x(q_n)=0` and `gcd(n,0)=n`.
4. Recheck the claimed `n=6` consequences:
   `6|deg_x(q_6)`, `deg_y P>=12`, `3|deg_y P`, and the common-core
   translations `d=3 => 3|H`, `d=6 => 6|H`. Identify which charged theorem
   supplies each implication.
5. Run the producer replay, inspect whether it actually checks what the
   report says, and independently verify at least one arithmetic control.
6. Attack overreads: equality `deg_y Q=deg_y B`, coordinate/gauge
   dependence, arbitrary support, existence versus conditional obstruction,
   and any accidental JC2/counterexample claim.

Give separate `CONFIRMED`, `REFUTED`, or `GAP` verdicts for the one-sided
floor six theorem, the residual `n=6` classification, the source-gauge
statements, and the stop decision for `n=2`--`5`. If anything fails, preserve
the strongest sound subclaim and give the clean correction. State whether
the result is eligible for `AUDIT.md` promotion.

Write the complete report to exactly
`xmodel/as109-one-sided-prime4-composition-hostile-review-grok-20260827.md`.
Touch no other campaign artifact. Do not enter, read, build, status-inspect,
or modify `jc2-lean`. Use only short desk-scale exact checks; no heavy local
CAS, no AWS launch, no web sweep, and no canonical-ledger edits.
