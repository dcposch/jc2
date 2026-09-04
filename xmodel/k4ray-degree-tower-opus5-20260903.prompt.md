# STRUCTURAL derivation lane (bypass the k=4 ray compute wall 17(yyyyy) with a DEGREE-BOUND TOWER, not more Gröbner): the nonconstant arm of the unsplit-configuration lemma has TWO proved uniform bounds on β (the 2nd approximate root) — TOP-BAND 2 deg β ≥ K+1 (17(vvvvv)) and the sharper 3 deg β ≥ 2K+1 (17(yyyyy), kills the low stratum for all K ≥ 7) — and the COMPOSITE arm (17(vvvvv)) kills deg β < K (B₂ constant ⇒ h | J). The open gap is the middle stratum. ITERATE the valuation/order argument that produced 3 deg β ≥ 2K+1 to get a TOWER of bounds c·deg β ≥ (c−1)K + r_c, and determine whether the tower CLOSES the gap — i.e. whether the bounds force deg β into a range the composite arm or a finite residual already covers, killing the row for all K WITHOUT solving the ~55-parameter chart

OPERATIONAL: skeleton first; this is a DERIVATION (valuation/Newton-polygon/order
bookkeeping on the Jacobian J = f_x g_y − f_y g_x with f = h² + B₂, g = h³ + A₂h
+ A₃, h of degree K, deg_y B₂ = b); exact CAS only to CHECK bounds at small K
(sympy, foreground ≤ 15 min); do NOT run the big Gröbner charts (17(yyyyy)
showed the wall). Charged: the two proved bounds and their derivations
(17(vvvvv) TOP-BAND, 17(yyyyy) §3.3 the 3 deg β ≥ 2K+1 argument — study HOW it
was derived: which Jacobian coefficient's vanishing forced it), the composite
arm, the closed-form killing row, the ray coordinates. Task: (1) reconstruct
the derivation of 3 deg β ≥ 2K+1 exactly (which coefficient of J, at which
(x,y)-degree, must vanish and forces the bound); (2) ITERATE: the next Jacobian
coefficient (one band deeper) should force a sharper bound 4 deg β ≥ ? — derive
it; continue to a general c·deg β ≥ (c−1)K + r_c or find where the pattern
saturates; (3) the KEY question: do the tower bounds + the composite arm
(deg β < K dead) leave only a FINITE set of (K, deg β) pairs, uniformly in K? if
the tower forces deg β ≥ K for large enough c while the composite kills
deg β < K, the two meet and every row dies for K ≥ K₀ — find K₀ and handle
K < K₀ by the charged exact kills (K=4,5) + guided_gb on the small residual;
(4) if the tower SATURATES before closing the gap, report the exact residual
stratum and its width as a function of K (is it bounded? growing?); (5)
controls: the bounds must hold at K=4,5 where the row is known dead; a genuinely
composite pair (β constant) is consistent (survives as composite); FALLACY-v2
(a degree bound is a necessary condition on β — it kills a row only if it
EXCLUDES all β, i.e. leaves no admissible degree; state this). Verdict:
UNSPLIT-CONFIGURATION LEMMA PROVED for all K (the tower closes the gap ⇒ case
(A)/D=108/δ₁'=0 all DEAD — write the chain) / the gap CLOSES for K ≥ K₀ with a
finite residual / the tower SATURATES leaving an explicit residual stratum. ≤
150 min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports. Drivers to box/k4raytower-20260903/.
Report: xmodel/k4ray-degree-tower-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-30KB; 150 minutes.
charged_input=xmodel/k4ray-highK-opus5-20260903.md
charged_input=xmodel/k4ray-unsplit-lemma-opus5-20260903.md
charged_input=xmodel/g9966-chart-necessity-opus5-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/k4rayhighk-20260903/hint_control.py
charged_input=box/k4rayhighk-20260903/gen_certif.py
charged_input=box/k4rayhighk-20260903/gen_lemmas.py
charged_input=box/k4ray-20260903/gen_k4ray2.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k4ray-degree-tower-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
f421e458f32b4fd9b82b83dc89a188d2cb0dabc9400ce7b9a7a820428b392657  {{LANE_INPUTS}}/k4ray-highK-opus5-20260903.md
8cda501a0ea448fe4bbf0703930a2aa5d2ee8f7bfcbc70b34ea133bb650926bd  {{LANE_INPUTS}}/k4ray-unsplit-lemma-opus5-20260903.md
37beed7ace5aafced312725fcca2e43aa316c19cecc387ef5aafa1c0809bb628  {{LANE_INPUTS}}/g9966-chart-necessity-opus5-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
097680197664c43272c41f5f2120661160c380fdfd3702915b92a4e1d8bf79df  {{LANE_INPUTS}}/hint_control.py
65c592c5fd62cdcb92998599fd493842848880ac4e1763074bd5339dac9901ce  {{LANE_INPUTS}}/gen_certif.py
8117ed3ab010241eac28131b858e3e69950be77aba04d7549fe5241686a02fa1  {{LANE_INPUTS}}/gen_lemmas.py
5a7a509a61833105365d5a69b58bc0a4858d40b8b739eaf75c8881e78473f1c6  {{LANE_INPUTS}}/gen_k4ray2.py
```
