# Different-model hostile review: V43C4 exact rho-zero `a1^104`

Act as an adversarial algebra/custody reviewer.  Work independently from the
producer's conclusions.  You may use desk-scale shell/Python checks, but do not
run Singular/Macaulay2, launch AWS, edit canonical ledgers, touch `jc2-lean`,
perform a web sweep, or read unrelated same-round model reports.  Write exactly
one report:

`xmodel/max12-812-order2-p0-total-rees-j2-a1-constructive-circuit-rebased-factor-v43c4-hostile-review-grok-20260827.md`

Charged case:

`cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_factor_v43c4_20260827/`

Charged pins:

- `FREEZE.sha256` SHA-256
  `67c1bb917506a01ee23101f652da0bba747480c6c576877a111b942aefc068f6`;
- producer SHA-256
  `cd3e17b8b08617fb6d576d36313e8d08ec0d488bc63f375d62d11da321c7d633`;
- proof SHA-256
  `3e0e80c0c9ab07803d60ea6b3284daeae6dbdeb858c6af875a1457174f5b0862`;
- result JSON SHA-256
  `629a0763f784e2d18c5acc433313c486d51b141a91d933b01303fb7d7959393c`;
- precursor factor diagnostic SHA-256
  `b9ebbaa4d73c12705096cad73a1c9e3b5b7a4c633a9dc94d7eaa86ff3d42b0cc`;
- reviewed predecessor invalidation report
  `xmodel/max12-812-order2-p0-total-rees-j2-a1-constructive-cascade-invalidation-v43c2-hostile-review-grok-20260827.md`
  SHA-256
  `008e0d524147c1b28af00b9b2d6f1f099750d6f0ea2aebfeb80e1a0aee6fd8cb`.

Review the exact theorem only at its claimed scope: in ordinary
`Q[X19_rho0]`, the frozen 51 named raw ordered-a1 rows through grade 19 contain
`a1^104`.  Do not infer a total-rho, saturated-Rees, or exponent-628 theorem.

Required attacks:

1. Rehash every freeze line and the full V42/V37 row-loader custody chain.
   Identify any missing producer/source snapshot or mutable dependency.
2. Independently replay the serialized proof from the frozen record, ideally
   without calling the producer `main`.  Confirm all 732 expression nodes and
   71 derivation nodes are canonically reconstructed from the 51 frozen rows,
   all 29 checkpoint targets hold, the final target is exactly `a1^104`, and
   the 16 final labels are literal rows only.
3. Re-derive `RebaseAssumptions` coefficientwise:
   `e1=G+4*a1*ell1` and `ee0=Q0-4*aa0*ell1`.  Confirm the inherited
   multiplier update has both correct signs and that old `e1,ee0` labels are
   absent before the exponent-three ClearPower.  Attack the two sign
   mutations.
4. Audit `PruneZeroFactor` as a universal exact rule.  For roots
   721/723/722 and factors 427/401/399, verify literal direct-child containment
   and independently expand each factor to exact zero over Q.  Confirm no
   assumption term is deleted on a hash, modular test, numerical test, or
   merely diagnostic assertion.  Attack replacement by direct nonzero factor
   371.
5. Recheck every ClearPower and CombineBranches guard, especially the repaired
   right branch and final split.  Look for any new crossed assumption,
   localization, negative exponent, implicit division, or set-theoretic step.
6. Audit mutations and scope precisely.  Important hostile note: the recorded
   Tg19_7 "omission" mutation deletes the term only from the serialized
   `final_certificate` commitment; it is a commitment-integrity check, not an
   independent source-row deletion test.  State this accurately and decide
   whether it affects the exact theorem (which should instead rest on complete
   replay).  Do not silently promote that control into a row-dependency test.
7. Check whether the claimed final row count/list, runtimes, and hashes match
   evidence, and whether any AWS transcript is being substituted for algebra.

End with exactly one token on its own line:

- `GROK_CONFIRMED_A1_104_V43C4` if the exact theorem and custody pass, with any
  nonblocking documentation/control repairs separated clearly;
- `GROK_REPAIRABLE_A1_104_V43C4` if the theorem is likely correct but a
  load-bearing replay/custody gap must be repaired before promotion;
- `GROK_REJECTED_A1_104_V43C4` if you find a mathematical countercheck.
