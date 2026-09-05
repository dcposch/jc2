# KILL lane (re-attack the D=108 δ=3 split branch at the CORRECT D2 radius; the old kill 17(ddddd) is REFUTED at stage 0 — frozen d108-center report: the engine used z = πs⁶ where Moh Def 5.1(3) gives δ₂ = 1/4 ⇒ z = πs⁵, weight 4r+5q, face weight 35; on that chart the stage-0 common-h₃ incidence block is VACUOUS (twelve pivots on twelve distinct coordinates, explicit rational witness) — so D=108 is OPEN on its split arm). The vacuity of the NECESSARY stage-0 block does not mean the branch survives: 17(ddddd)'s certificate never used the higher band stages, the outer accounting, or the D1 block jointly. TASK: (1) rebuild the D=108 δ=3 band engine at the proved radius (box/d108-center-20260905/work/center_incidence.py + radius-ledger.json give the correct weights; box/g108gate-20260903/band_engine.py is the frozen engine — patch the transplanted exponent, keep the minor constant FREE (jet0), keep the local_power truncation only where typed safe, i.e. dropping ROWS not unknowns); (2) run the FULL staged elimination the (99,66) sibling runs (stages 0–4 style: the h₃ incidence, the h₂ major block, the D1 block, the outer accounting, joint) — exact sympy qstar_reduce with rational pivots, or guided_gb/Singular on the joint chart; a fleet worker (r7i.8xlarge, launch via `bash ops/fleet/fleet.sh launch`; TERMINATE before sealing); (3) if the branch dies at some stage: full custody (chart, radius, gauge ledger with every spent group parameter, stage, generator/cofactor identity, exact-Q) — that RE-CERTIFIES D108-DELTA3-DEAD on the correct chart; if it survives all stages: report the surviving locus (dimension, a rational point, and whether the point extends to a Jacobian pair modulo the outer obligations) — that is the biggest news possible and must be typed as "necessary-chart survivor", not a counterexample; if compute-bound: exactly where. (4) Cross-check: the witness of the frozen report must satisfy stage 0 in your rebuilt engine (control), and the OLD radius must reproduce [1] (control). FALLACY-v2 (dropping rows is safe, dropping unknowns by a floor is not; every normalization needs its group element and may be spent once; a modular unit needs exact-Q confirmation). No ledger edits; no jc2-lean; no ideation-*. ≤ 180 min. Drivers to box/d108-rekill-20260905/.
Report: xmodel/d108-delta3-rekill-opus5-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 180 min.
charged_input=xmodel/d108-center-opus5-20260905.md
charged_input=xmodel/support-regression-gate-opus5-20260905.md
charged_input=xmodel/g108-delta3-kill-gate-gpt55-20260903.md
charged_input=box/g108gate-20260903/band_engine.py
charged_input=box/lib/guided_gb.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/d108-delta3-rekill-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
36ceadb6638131aacd53ba80559e99dd1f6f78c05ce13ba42f6a344c9370e504  {{LANE_INPUTS}}/d108-center-opus5-20260905.md
e08f6e40f817e5bf354073e0fb685b4e6b3625c6a7442b1d90ac6ef4dffa0990  {{LANE_INPUTS}}/support-regression-gate-opus5-20260905.md
7c14a90a47485d8ac7461a2b0019989dc09cc580cd33fb23a67b08afae48fe3b  {{LANE_INPUTS}}/g108-delta3-kill-gate-gpt55-20260903.md
24643ec64fd98d14eddae67c5f4f17f63e23998a97a4911603c23f7ebfb94ce2  {{LANE_INPUTS}}/band_engine.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
