You are the hostile different-model reviewer for the provisional campaign
claim `D43-NF-FID`. Work in `/Users/dc/code/math/jc2` and independently audit
the exact, narrow scope below. This review runs in the background while new
research proceeds; do not read or summarize the current ideation-round reports.

Primary claim to adjudicate:

- At both `p=105337` and `p=105673`, the recovered D43 checkpoint family is
  exactly the stated 184-variable, 218-row modular presentation (34 parked,
  95 old graph, 89 late graph rows), with the recorded canonical hashes.
- At `p=105337`, all 184 pristine source rows independently replay as
  `R_raw = R_NF + sum_j Q_j G_j` over the finite field and the recomputed normal
  forms agree dictionary-exactly with the recovered checkpoints.
- This establishes only modular source-to-normal-form fidelity. It does not
  establish a common integral presentation, all-row mod-p-squared lift,
  flatness, standard smoothness, a characteristic-zero point, a compatible
  germ, or a polynomial Keller pair.

Read `xmodel/sol-d43int.md`, the D43 sections of `AUDIT.md`,
`xmodel/sol-clift.md`, and the referenced scripts/artifacts under `cases/`.
Audit producer/code/data provenance rather than trusting the prose. Check for
variable-count, row-count, band, fiber, prime, stale-checkpoint, canonical-row,
source-model versus parked-model, and normal-form/tracer circularity errors.
Rerun the bounded recovery audits. Independently inspect and, where practical,
recompute or spot-check the trace identity using a separate code path or
direct coefficient evaluation. Use a fresh `mktemp -d` for new outputs; do not
overwrite banked artifacts. Record exact commands, hashes, versions, and any
limits that prevent full replay. A timeout is not a mathematical failure.

Return one scoped verdict: `CONFIRMED`, `CONFIRMED WITH GAPS`, `GAPS`, or
`REFUTED`. State exactly which clauses survive, whether the live evidence tier
may be promoted from producer-checked provisional, and which downstream work
must be quarantined if anything fails. Do not silently enlarge the claim.

Write only `xmodel/review-d43-nf-fid-grok.md` in the repository. Do not edit
shared ledgers, source code, or banked data. Put model/CLI/version, basis, UTC,
artifact hashes, and the final verdict near the top.
