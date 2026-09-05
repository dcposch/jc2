# DEEP-KILL lane (the D=108 δ=3 split branch is a NECESSARY-CHART SURVIVOR at the proved radius — frozen re-kill report: stages 0–4 and the saturated depth-8 system (1,420 rows) leave a 7-dimensional locus in 9 active variables, codimension 2, radical ⟨K2c_3_26 + 8·jet2, K2c_4_25 − K2c_4_26 − 20·jet1²⟩, with a rational point satisfying every expressed row, c ≠ 0, D₂-minimal). The chart's DEEP obligations are untested: F's pole rows at local powers 9..95 and its leading target p¹² at 96; G's at 9..63 and p⁸ at 64 (stage s reaches local power 4+s); Jacobian bands at t-power ≥ 5 (degrees ≤ 173) and the degree-0 normalization J = 1; outer D1 offsets beyond 4 (A2/A3/B2 blocks start at r ≥ 26, 61, 26). TASK: (1) using the rebuilt engine in box/d108-rekill-20260905/ (correct radius, the corrected K₂ face, jet0 free, the gauge ledger of §8), extend the schedule RESTRICTED TO THE SURVIVING LOCUS: substitute the stage-4/saturated radical (work in the quotient by the two forms, or parametrize the 7-dim locus rationally) and add rows in order of local power 9, 10, … — each stage exact-Q (sympy qstar_reduce or Singular std over Q on the reduced ring) — recording the dimension after each; the locus is small (9 active variables) so each stage should be fast; continue until the dimension hits −1 (KILL) or the rows are exhausted (SURVIVOR of the full chart); (2) simultaneously test the Jacobian bands t = 5..12 and the degree-0 normalization J = 1 on the locus, and the outer blocks A2/A3/B2 at their first visible offsets; (3) at every stage keep the rational point of §6 as a control: if it survives a stage it must annihilate the new rows; when it fails, find a new point on the reduced locus (msolve/Singular rational points on a low-dimensional variety) or record that no rational point was found (dimension-only); (4) VERDICT: D108-DELTA3 branch DEAD on the full chart (unit at stage k with the gauge ledger — RE-CERTIFICATION on the correct radius, PROVED-HERE for gate) / SURVIVOR of the FULL chart (a point satisfying ALL pole rows to power 96 and all bands — report loudly: what it means is that the necessary chart cannot kill this branch and a genuinely different instrument (the joint chart / the outer accounting theorem) is required; it is NOT a Keller pair) / compute-bound at stage k (state the dimension there). A fleet worker is allowed if needed (`bash ops/fleet/fleet.sh launch 1 r7i.8xlarge`; TERMINATE before sealing). FALLACY-v2 (a unit on the LOCUS proves the branch dead only if the locus restriction was licensed — it is, since the locus is the exact stage-4 survivor set — record that argument; never drop unknowns by a floor). ≤ 200 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/d108-survivor-deep-20260905/.
Report: xmodel/d108-survivor-deep-opus5-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 200 min.
charged_input=xmodel/d108-delta3-rekill-opus5-20260905.md
charged_input=xmodel/d108-center-opus5-20260905.md
charged_input=box/g108gate-20260903/band_engine.py
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/d108-survivor-deep-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
d26c3dd22893b474d70806f21474092ec55d8acfb7dd6be046ff208deb991b05  {{LANE_INPUTS}}/d108-delta3-rekill-opus5-20260905.md
36ceadb6638131aacd53ba80559e99dd1f6f78c05ce13ba42f6a344c9370e504  {{LANE_INPUTS}}/d108-center-opus5-20260905.md
24643ec64fd98d14eddae67c5f4f17f63e23998a97a4911603c23f7ebfb94ce2  {{LANE_INPUTS}}/band_engine.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
