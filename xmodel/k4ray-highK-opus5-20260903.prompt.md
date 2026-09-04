# COMPUTE proof lane (first client of the new box/lib/guided_gb.py; closes the ACTUAL open (H2) rows): prove the nonconstant arm of the UNSPLIT-CONFIGURATION LEMMA (17(vvvvv)) — B₂ nonconstant ⇒ the Jacobian coefficient system is INCONSISTENT — at K = 7, 8, 9 (the census rows: K=7 = the δ₁'=0 two-point row (21,14; 15; 6; 4); K=8 = D=108 no-split (24,16; 18; 7; 4); K=9 = case (A) of (99,66) (27,18; 21; 8; 4)), on the FULL stratum deg β ≤ 2K−1, using guided_gb (Hilbert-hinted, modular+CRT, properness-scoped) — the previous lane closed only K=4,5 on deg β ≤ K−1

OPERATIONAL: skeleton first; USE box/lib/guided_gb.py (import it; it runs
Singular under stdbuf -oL with a Hilbert hint, modular+CRT, and the control
battery — do NOT hand-roll a naive foreground Q std, that is what timed out);
≤ 4 cores; every guided_gb call has its own timeout; never end the turn with a
job running. Charged: the unsplit-lemma report (17(vvvvv)) gives the ray
(3K,2K; 3K−6; K−1; k=4), the composite arm (PROVED, B₂ const ⇒ h|J ⇒ dead —
assume it, do not redo), the bound deg_y B₂ < K (PROVED), the TOP-BAND LEMMA
(β∉k ⇒ y^⌈(K−1)/2⌉(y−x)|β_b — USE it to cut the chart), and the CLOSED-FORM
KILLING ROW (verified K=4,5,7,9 — use it as the Hilbert hint / the row to
certify). Task: (1) for K = 7, 8, 9 build the nonconstant-arm Jacobian
coefficient system on the bounded chart deg β ≤ 2K−1 (the honest full stratum;
the TOP-BAND lemma constrains β_b — apply it to shrink the chart before
solving); use the staged_band_emitter if the system is large; (2) run guided_gb
to decide UNIT_IDEAL_CHAR0 (inconsistent ⇒ the row dead) / POSDIM (a surviving
component — extract a point and check it against the Keller/Jacobian condition
directly) / INCONCLUSIVE_TIMEOUT (report the deepest stage); the closed-form
killing row is the certificate to look for; (3) if all three are
UNIT_IDEAL_CHAR0: the UNSPLIT-CONFIGURATION LEMMA holds at K=7,8,9 ⇒ case (A)
of (99,66) is DEAD (⇒ the (99,66) SKELETON verdict is complete for ALL THREE
configurations modulo N1 — write the chain), D=108 no-split is DEAD (⇒ D=108
CLOSED at skeleton level), and the δ₁'=0 two-point row (21,14) is DEAD; (4)
attempt the K-UNIFORM killing COMBINATION (17(vvvvv) left the killing row
closed-form but not the combination): from K=4,5,7,8,9 fit the combination of
rows that gives the unit — if found, the lemma is PROVED for all K ≥ 4 (state
it); (5) controls: the composite arm on a genuinely composite pair survives as
composite (not a Keller counterexample); a tame two-point automorphism of
degrees (3K,2K) survives; the guided_gb perturbed-series control fails as
designed; FALLACY-v2 (a POSDIM component is not a counterexample until a point
is exhibited AND satisfies J=const; modular unit → char 0 only via properness).
≤ 180 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress
lane reports. Drivers to box/k4rayhighk-20260903/.
Report: xmodel/k4ray-highK-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 18-36KB; 180 minutes.
charged_input=xmodel/k4ray-unsplit-lemma-opus5-20260903.md
charged_input=xmodel/sys-guided-gb-gpt55-20260903.md
charged_input=xmodel/g108-nosplit-descent-grok46-20260903.md
charged_input=xmodel/g9966-chart-necessity-opus5-20260903.md
charged_input=xmodel/order-basis-full-gpt55-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=box/lib/staged_band_emitter.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/k4ray-20260903/gen_k4ray2.py
charged_input=box/k4ray-20260903/gen_k4ray3.py
charged_input=box/k4ray-20260903/gen_k4ray.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k4ray-highK-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
8cda501a0ea448fe4bbf0703930a2aa5d2ee8f7bfcbc70b34ea133bb650926bd  {{LANE_INPUTS}}/k4ray-unsplit-lemma-opus5-20260903.md
3256f9599f92f5f7e2129d4164237296f2adbce8bcda8fd61f56474ecdd55e6c  {{LANE_INPUTS}}/sys-guided-gb-gpt55-20260903.md
22678b422d57b66b5c9e9336c8fba97a61b5070cf87165bb7f5f0d3acbf3e742  {{LANE_INPUTS}}/g108-nosplit-descent-grok46-20260903.md
37beed7ace5aafced312725fcca2e43aa316c19cecc387ef5aafa1c0809bb628  {{LANE_INPUTS}}/g9966-chart-necessity-opus5-20260903.md
a8f89e2cc9060d2008375c5bb689b935ef72abdd75b96b1c10d52edf3151c2b6  {{LANE_INPUTS}}/order-basis-full-gpt55-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
7c2f88430158fc01b2aa4e1bc2af1902f92168d10cd48ee5095506beb149dce8  {{LANE_INPUTS}}/staged_band_emitter.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
5a7a509a61833105365d5a69b58bc0a4858d40b8b739eaf75c8881e78473f1c6  {{LANE_INPUTS}}/gen_k4ray2.py
b3185f897b08871b2116c057b349bf8c999dd304cae1eceeb1aaaa3e863c946e  {{LANE_INPUTS}}/gen_k4ray3.py
8aedd50b96c2f3339dec2c4b4addd7270eaac07d0c97960919853742bf240f21  {{LANE_INPUTS}}/gen_k4ray.py
```
