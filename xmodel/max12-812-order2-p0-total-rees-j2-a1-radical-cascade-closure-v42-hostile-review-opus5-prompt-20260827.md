You are the hostile different-model reviewer for a new exact ordered-`a1`
claim in the JC2 campaign. Work in `/Users/dc/code/math/jc2`.

Producer:
`xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-sol-20260827.md`
SHA-256:
`5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f`

Artifacts:

- replay
  `cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py`
  SHA `f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459`
- result in the same directory, SHA
  `01b8edd2b699d7c4b65452ea6eba47a98bf25c1cd5a18022a035e2346c973566`
- freeze manifest in the same directory, SHA
  `9de72b9261e12896f3c352f313b0788091616fc64c9ec9754c53eba196ed3ca5`

Read the prior reviewed cascade and symbol report named by the producer. Do
not accept a successful producer replay as review. Independently reconstruct
and attack:

1. source custody: verify the loader and all 70 frozen raw ordered-`a1`,
   `rho=0` rows through grade 19 used by the replay;
2. the inherited deductions
   `e0=e1=ee0=ell1=0`, `aa0*rs1=0`, carefully marking exact ideal identities
   versus radical/field-point steps and every localization;
3. the branch cover from `Tg14_3`;
4. the A2 identity
   `Tg16_6-(3/32)rs1*Tg13_2=(21/1024)a1^2rs1^2`
   after exactly the stated specialization, including its characteristic and
   `D(a1*rs1)` scope;
5. the A1 eliminations, four reduced rows, Laurent unit identity, lift through
   the eliminations, and denominator clearing to the claimed ordinary
   branch-ideal membership `a1^8`; recompute coefficientwise with an
   implementation independent of the producer if feasible;
6. the mutation control and whether all six row multipliers truly use raw
   rows rather than a dual-as-primal or quotient substitution error;
7. the combined logical conclusion: no algebraically closed characteristic-
   zero field point on `D(a1)` for the frozen raw `rho=0` prefix through g19.

Explicitly test the strongest tempting overreads. Does the result give a
global `a1^N` membership in the unsplit raw ideal, or only a radical result
after combining branches? Does it imply anything in the general-`rho` ring,
the saturated Rees chart, the honest total chart, or Gate T without a new
comparison/certificate? Preserve exact scope.

Return separate `CONFIRMED`, `REFUTED`, or `GAP` verdicts for A2, the A1
ordinary branch certificate, branch coverage, and the combined raw-field-
point theorem. Give the cleanest correction for any defect and state whether
the exact scoped result is eligible for `AUDIT.md` promotion.

Write the complete report to exactly
`xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-hostile-review-opus5-20260827.md`.
Touch no other campaign artifact. Do not enter, read, build, status-inspect,
or modify `jc2-lean`. Use only short desk-scale exact replay; no heavy local
CAS, no AWS launch, no web sweep, and no canonical-ledger edits.
