# COMPUTE proof lane (close the k=4 ray census rows now that the wall is removed, 17(zzzzz)): the LEVEL-4 pin forces the top band of the 2nd approximate root to ONE scalar — β_b = μ·y^{K−3}(y−x) at the wall rows — collapsing the previously ~55-parameter charts; combine this pin with the uniform theorem deg(g²−f³−λf) = K+6 and run box/lib/guided_gb.py on the RESIDUAL (small) nonconstant-arm chart at K = 7 (the δ₁'=0 row (21,14;15;6;4)), K = 8 (D=108 no-split (24,16;18;7;4)), K = 9 (case (A) of (99,66) (27,18;21;8;4)) — decide UNIT_IDEAL (row dead) / POSDIM (extract a point, test J=const directly) / TIMEOUT

OPERATIONAL: skeleton first; USE box/lib/guided_gb.py (import it; stdbuf -oL,
Hilbert hint, modular+CRT, control battery); ≤ 4 cores; per-call timeout; never
end the turn with a job running. NOTE (17(yyyyy)): the nonconstant-arm ideals
are dehomogenised/inhomogeneous localisations, so the properness char-0 scope
does NOT apply — use EXACT Q where feasible (the pin makes it small), and if a
modular run is used, type it F_p-only and confirm exactly. Charged: the pin and
the K+6 theorem (17(zzzzz), box/k4raytower2-20260903/), the ray coordinates and
the composite arm (17(vvvvv)), guided_gb + staged emitter (17(xxxxx)). Task:
(1) for K = 7, 8, 9: substitute the pinned top band β_b = μ·y^{K−3}(y−x) (ONE
scalar μ) and reduce the residual β = β_b + (lower-degree terms) — the LEVEL-4
divisibility H² | β_b³ and the K+6 theorem should further constrain the lower
terms; build the nonconstant-arm Jacobian coefficient system on this reduced
chart (should be FAR smaller than the 17(yyyyy) ~55 params — report the actual
parameter count); (2) run guided_gb to decide each row; the composite arm
(β ∈ k) is already dead so restrict to μ ≠ 0 (Rabinowitsch on μ); (3) if all
three UNIT_IDEAL: the UNSPLIT-CONFIGURATION LEMMA holds at K = 7,8,9 ⇒ case (A)
DEAD ⇒ the (99,66) SKELETON verdict is COMPLETE for all three configurations
modulo N1; D=108 no-split DEAD ⇒ D=108 CLOSED at skeleton level; the δ₁'=0 row
(21,14) DEAD — write the full dependency chain and NOTIFY-WORTHY flag in the
verdict; (4) if any POSDIM: extract the surviving point, rebuild (f,g), compute
J = f_x g_y − f_y g_x — is it a nonzero constant (a real Keller pair!) or does
J vary (not a counterexample)? report exactly; (5) push K = 10, 11 if cheap
(the pin makes them small) toward the K-uniform statement; controls: the pin
must reproduce the charged K = 4,5 kills; a tame two-point automorphism
survives; the guided_gb perturbed control fails as designed; FALLACY-v2.
Verdict per row + the chain if all dead. ≤ 170 min; no ledger edits; no
jc2-lean; no ideation-* files; no in-progress lane reports. Drivers to
box/k4raypinned-20260903/.
Report: xmodel/k4ray-pinned-chart-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-30KB; 170 minutes.
charged_input=xmodel/k4ray-degree-tower-opus5-20260903.md
charged_input=xmodel/k4ray-highK-opus5-20260903.md
charged_input=xmodel/k4ray-unsplit-lemma-opus5-20260903.md
charged_input=xmodel/sys-guided-gb-gpt55-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=box/lib/staged_band_emitter.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/k4rayhighk-20260903/hint_control.py
charged_input=box/k4rayhighk-20260903/gen_certif.py
charged_input=box/k4rayhighk-20260903/gen_lemmas.py
charged_input=box/k4rayhighk-20260903/gen_hk.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k4ray-pinned-chart-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
2befb3cac8e51305e65ab0e48de485a7098ba104a3620d8b174927791a896a2a  {{LANE_INPUTS}}/k4ray-degree-tower-opus5-20260903.md
f421e458f32b4fd9b82b83dc89a188d2cb0dabc9400ce7b9a7a820428b392657  {{LANE_INPUTS}}/k4ray-highK-opus5-20260903.md
8cda501a0ea448fe4bbf0703930a2aa5d2ee8f7bfcbc70b34ea133bb650926bd  {{LANE_INPUTS}}/k4ray-unsplit-lemma-opus5-20260903.md
3256f9599f92f5f7e2129d4164237296f2adbce8bcda8fd61f56474ecdd55e6c  {{LANE_INPUTS}}/sys-guided-gb-gpt55-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
7c2f88430158fc01b2aa4e1bc2af1902f92168d10cd48ee5095506beb149dce8  {{LANE_INPUTS}}/staged_band_emitter.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
097680197664c43272c41f5f2120661160c380fdfd3702915b92a4e1d8bf79df  {{LANE_INPUTS}}/hint_control.py
65c592c5fd62cdcb92998599fd493842848880ac4e1763074bd5339dac9901ce  {{LANE_INPUTS}}/gen_certif.py
8117ed3ab010241eac28131b858e3e69950be77aba04d7549fe5241686a02fa1  {{LANE_INPUTS}}/gen_lemmas.py
75ca67163867ca208ced7597685b08c181d9bdb3bb836b96f51fcc8894c668af  {{LANE_INPUTS}}/gen_hk.py
```
