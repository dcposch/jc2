# Hostile bounded review charge: TD6 q2-beta raw `u-h-zero` and origin V70

Act as an adversarial algebra/source/custody reviewer.  This is a bounded,
read-only audit.  Do not edit any producer or canonical file, do not run the
substantive replay, and do not invoke CAS, solver, Lean, or heavy Python.  You
may hash files, extract the 125-KiB source archive to private `/tmp`, inspect
source, and perform short hand/stdlib checks.  Write only the requested
review report.

Read in full:

- `xmodel/td6-c1-c2-c3-q2-beta-u-zero-scope-erratum-20260825.md`;
- `xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-prereg-20260825.md`;
- `xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-aws-20260825.md`;
- `cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_aws_20260825/README.md`;
- that case's `DEPENDENCIES.sha256`, `MANIFEST.sha256`, `FREEZE.sha256`,
  `verify.py`, all evidence, source wrapper/manifest/runbook, and portable
  dependency archive;
- the prior hostile review
  `xmodel/td6-c1-c2-c3-q2-beta-u-zero-review-grok-20260825.md` and the exact
  archived V69/parent source portions used by V70.

Adversarially verify or refute:

1. Source typing.  The main raw branches are exactly `C=U=0` over `Q(V)` and
   `C=V=U=0`, inside the fixed normalized A3 q2-beta source, with beta
   polynomial and direct `q_beta'=1+2 beta t+25 t^24` retained.  No V33
   fraction-field echelon is specialized through `C=0`.
2. Wrapper fidelity.  `replay_v70.py` hash-pins V69 and changes only
   observability: transport-event/chart display, complete-localization
   composition, and exact wrong-row controls.  Check monkeypatch dispatch,
   especially the distinct transport and affine-stage replay paths.
3. `u-h-zero`.  Check the dual-host byte identity, rc zero, source closure,
   ranks `3470/3602` and `36/132`, events `-V,-V`, transport chart `V^2`,
   first-source denominator `V`, unique original row `('X-2',14)`, 14-row
   original combination, beta-degree-zero unit/gcd, and exact complete
   denominator `V^3`.  Confirm this proves only `C=U=0,D(V)`.
4. Origin.  Check the dual-host byte identity, rc zero, source closure,
   transport rank `3468/3602`, dependent original row 6460 / key
   `('g','X',-19,20)`, 21-row original ancestry, beta-degree-zero unit,
   no nonconstant pivot events, and complete denominator one.  Verify the
   source sign/replay and that the wrong-row control really detects a change.
5. Controls and custody.  Audit both direct-q-prime omission controls without
   turning them into a broader theorem.  Distinguish the preserved rc-one
   initial wrapper/reporter KeyError from the math-bearing lines printed
   before it; only the repaired rc-zero runs are theorem evidence.  Recompute
   manifests/freeze/source hashes and inspect whether the portable bundle
   really contains the executed ancestry.
6. Cover logic.  Together with the corrected prior theorem on
   `U=0,D(C)`, verify the exact union

   `V(U)=[V(U)∩D(C)] ∪ [V(C,U)∩D(V)] ∪ V(C,V,U)`.

   Decide whether V70 restores a whole raw-`U=0` theorem in this fixed
   q2-beta section, but no more.  It must not automatically discharge the
   separately quarantined staged-N13 denominators or imply whole H/B3/A3,
   other TD6 moduli, TD6, SP-2, landing, or JC2.

Try to flip the claim through hidden denominator factors, source-row versus
echelon ancestry, wrapper monkeypatch error, wrong sign/RHS convention,
beta specialization, q-prime omission, nonportable digests, failed-run
contamination, incomplete union, or scope overreach.  Separate theorem
defects from custody/expository nits.

Write
`xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-review-grok-20260825.md` and end
with exactly one verdict token on its own line: `CONFIRMED`,
`CONFIRMED_WITH_REPAIRS`, or `FAILED`.
