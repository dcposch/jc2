# CORRECTNESS GATE (highest priority — a round submission flags that a banked closure may rest on an undischarged hypothesis, AUDIT 17(eeeeee) §2): Moh Prop 6.3's DESCENT is licensed only when the minor radius δ* ≥ v_s/u_s; this is AUTOMATIC when u_s = 1, but for u_s ≥ 2 it is a real hypothesis. Every u_s ≥ 2 kill that used a Prop 6.3 DESCENT — in particular D=108 no-split (K=8, the (24,16;18;7;4) descent) and the k=4-ray no-split rows (K=7 (21,14), K=9 case (A)) — may be sitting on it undischarged. Determine, for each such banked kill, whether the radius hypothesis IS discharged; if not, downgrade the affected verdict to CONDITIONAL and state exactly what must be proved

OPERATIONAL: skeleton first; pure algebra + small exact checks (foreground);
≤ 3 cores; no background jobs. Task: (1) state Prop 6.3's hypothesis EXACTLY
from the source (Moh p.N; page = PDF page N−139; pdftoppm for images) — the
radius condition licensing the descent, and prove it is automatic for u_s = 1
(so the (99,66) case (A) descent to (27,18), which is u_s=? — check: is case (A)
u_s=1 or ≥2 after descent? — and the 14 excess ≤100 rows which are u_s=1, are
SAFE); (2) for each u_s ≥ 2 kill that used a descent — D=108 no-split (K=8), the
k=4-ray rows — identify whether the descent step invoked Prop 6.3 with δ* ≥
v_s/u_s and whether that inequality was DISCHARGED (proved for the actual skeleton)
or ASSUMED; the banked reports to check (charged): g108-nosplit-descent (17(fffff)),
k4ray-K89 (17(bbbbbb)), k4ray-unsplit-lemma (17(vvvvv)); (3) if DISCHARGED
everywhere: the flag is CLEARED, D=108 and the k=4-ray kills stand unconditional
— write the discharge per row; if NOT: downgrade the affected kills to
CONDITIONAL[PROP63-RADIUS] and state the exact inequality to prove per row, and
whether it is cheap (a radius computation from the skeleton data) or a real
obstruction; (4) IMPORTANT distinction: the SPLIT kills ((99,66) branches B/C
via the joint chart, D=108 δ=3 incidence) do NOT use Prop 6.3 — confirm they are
unaffected; (5) verdict: FLAG CLEARED (all discharged) / D=108 and/or k=4-ray
kills CONDITIONAL[PROP63-RADIUS] with the exact residual per row; if the radius
is a cheap computation, DO it for each affected row and discharge on the spot.
FALLACY-v2 (do not assume the hypothesis; either cite its discharge or compute
δ* and compare to v_s/u_s exactly). ≤ 120 min; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports. Drivers to box/prop63gate-20260905/.
Report: xmodel/prop63-radius-gate-opus5-20260905.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 120 minutes.
charged_input=xmodel/ideation-20260905T0000Z-opus5.md
charged_input=xmodel/g108-nosplit-descent-grok46-20260903.md
charged_input=xmodel/k4ray-K89-sol56-20260903.md
charged_input=xmodel/k4ray-unsplit-lemma-opus5-20260903.md
charged_input=xmodel/g108-minor-classification-opus5-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/prop63-radius-gate-opus5-20260905.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
6bc47cea64909ec7cc8fc2f6e0da03b52a5d57fd9250323d1326e7ff251d8b47  {{LANE_INPUTS}}/ideation-20260905T0000Z-opus5.md
22678b422d57b66b5c9e9336c8fba97a61b5070cf87165bb7f5f0d3acbf3e742  {{LANE_INPUTS}}/g108-nosplit-descent-grok46-20260903.md
4797dbe918a855ffb6f71ba6608685347b0c1fc502e435c01a1bcfb1bb8adb98  {{LANE_INPUTS}}/k4ray-K89-sol56-20260903.md
8cda501a0ea448fe4bbf0703930a2aa5d2ee8f7bfcbc70b34ea133bb650926bd  {{LANE_INPUTS}}/k4ray-unsplit-lemma-opus5-20260903.md
8b97a8972cff0dfccfa9396bae8849dbda4318fb47150645e76d55785d9decd3  {{LANE_INPUTS}}/g108-minor-classification-opus5-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
