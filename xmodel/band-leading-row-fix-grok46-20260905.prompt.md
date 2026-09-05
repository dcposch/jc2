# BOUNDED INSTRUMENT FIX (≤ 45 min; finish and seal promptly): the cone-vertex gate (frozen, §6–§7) found a MATERIAL defect in the band engines: raw_minor_support emits the LEADING pole power (local n = 96/64 at D=108, 81/54 at (99,66) δ=2, 189/126 at δ=5/2) as a homogeneous "coefficient = 0" row with NO target subtraction; that row is unsatisfiable on the whole chart (it reduces to 1 = 0, the π⁸ coefficient of the forced target (π²−c)⁴), so the engines as coded would return a SPURIOUS UNIT at stage 92/60 (D=108) and 77/50 ((99,66) δ=2). TASK: (1) locate raw_minor_support (and any sibling emitter) in the three engines — box/d108-rekill-20260905/work/rekill_engine.py, box/g9966-repair-gate-20260905/corrected_face_engine.py, box/g9966band-20260903/band_engine.py (and the frozen g108 band_engine.py) — and the exact place the leading row is emitted without its target; (2) FIX: the leading pole row must be emitted as coefficient − target (the target being the forced leading term of F resp. G at that power, e.g. the coefficient of the appropriate power of the K₂/K₃ face — take the exact form from the gate's §6 and the rekill lane's §7 "leading target p¹² at 96 / p⁸ at 64"); keep every other row byte-identical; do the same for all three engines with a shared helper if practical; (3) CONTROLS (mandatory, all exact Q): (a) the old-radius D=108 stage-0 unit must still reproduce [1] (the pipeline can still kill); (b) at the corrected radius, running the D=108 schedule to the leading stage must NOT return a unit from the leading row alone — show the leading row is now satisfied on the Δ locus by the Δ-witness of the gate (direct substitution); (c) the (99,66) δ=2 corrected engine likewise at its leading stage; (4) commit the patches in place with header comments and list the diffs in the report. FALLACY-v2 (an instrument fix must not create or remove any verdict except the spurious one it targets; show every control). No fleet. ≤ 50 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/band-leading-fix-20260905/.
Report: xmodel/band-leading-row-fix-grok46-20260905.md
Seal (<!-- BODY-END -->); 5-12KB; 50 min.
charged_input=xmodel/cone-vertex-gate-opus5-20260905.md
charged_input=xmodel/joint-chart-degenerate-fable5-20260905.md
charged_input=xmodel/d108-delta3-rekill-opus5-20260905.md
charged_input=box/g9966band-20260903/band_engine.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/band-leading-row-fix-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
72dfcd371f338767e303c6da0eab02337f257ad29409a9fc6b60cd2e85c20ecd  {{LANE_INPUTS}}/cone-vertex-gate-opus5-20260905.md
078f179d36ba99d3069ded660b72f3f8bb8b28d4593b2d5c5c1f87a6c68bf0b8  {{LANE_INPUTS}}/joint-chart-degenerate-fable5-20260905.md
d26c3dd22893b474d70806f21474092ec55d8acfb7dd6be046ff208deb991b05  {{LANE_INPUTS}}/d108-delta3-rekill-opus5-20260905.md
3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9  {{LANE_INPUTS}}/band_engine.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
