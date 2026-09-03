# Hostile gate: PROP 5.5(k) lane (Opus) — verify the proof of Φ from Prop 4.1, the closed form, the r = 1 ODE invariance, the sharpness family, the CORRECTED Galois modulus 𝔄 = A'/gcd(A', L), the G2/G3 negative, and the residue counts

Charged claims (prop55k-opus5-20260903.md §0–§4; AUDIT delta 17(z) PROVISIONAL):
(1) SOURCE-READ p.164: the Jacobian enters Moh's radius system only through the
chain rule of Prop 4.1; J = cx^k replaces −1 by −(k+1) in Prop 4.4(3),(6) and
Prop 4.6(3) and nowhere else, so δ_i^{(k)} = (k+1)δ_i^{(0)} (a proof of the
rule Φ of delta 17(t)); (2) closed form δ₂' = −(k+1)/R, δ₁' = (k+1)(ΠU₂' − R)/
(R(ΠV₂' − 1)) with R = n' − M₂' − 1, Π = n* + m*, U₂' = d₂' − V₂', reproducing
10/10 p.207 rationals and 20 Newton–Puiseux measurements on existing pairs;
(3) the r = 1 ODE (Prop A.3 form) survives J = cγ^k with only the constant
changed; (4) PROP 5.5(k): d₂' ≤ (k+1)V₂', g₀ | (k+2)V₂' − d₂', g₀ ≥ V₂', sharp
via P = π^{k+1} − γ^{k+1}, Q = P^q + aπ; (5) CORRECTED-HERE: Moh's p.188 Galois
modulus A' = denom(δ₁') must be replaced by 𝔄 = A'/gcd(A', L), L the index of
the t-exponent lattice of the common part of σ₁ — evidence: two existing
control pairs killed by A', and Moh's own printed (21,14; 16; 2; X) killed by
A' at Prop 5.5 level; (6) G2/G3 not killed under 𝔄; (7) k = 0 kills 980/980 at
n' ≤ 60, k = 1..8 kills 88.4–95.5 %; (8) (T) does not follow; obstruction =
window degeneration V₂' > d₂'/(k+2); CONJ[APPII-UNIFORM]. Task: (a) open Moh
pp.164–166 (Prop 4.1), 168–172 (Props 4.4, 4.6), 176–179, 186–188 (Prop 5.5
and the Galois step) as page images (pdftoppm -r 200; name the pages) and
check (1), (3), (5) line by line against the print — in particular: is the
"common part in k((t))" hypothesis actually used at p.188, and is the claim
that A' would kill Moh's (21,14) row correct (replay it); (b) replay the
drivers: the closed form on the ten p.207 rationals, the 20 existing-pair
Newton–Puiseux controls (re-run at least 5 with independent code — construct
pairs with J = cγ^k yourself, e.g. from the sharpness family and from
compositions, and measure radii), the sharpness family's Jacobian and its
d₂' = (k+1)V₂', the G2/G3 residues, and the 980/980 and k = 1..8 counts;
(c) apply PROP 5.5(k) with 𝔄 to the K = 16 ray's descendants (12t+4, 8t+4;
M₂' = 12t+1, V₂' = 3, k = 1) for t = 1..6 and report whether any is killed
(expected: none — check); (d) verdict per item CONFIRMED / GAP / REFUTED,
promotability of Φ as a theorem (scope), and of the corrected modulus (is it a
correction to Moh's proof of Prop 5.5 itself, i.e. an ERRATUM candidate, or
only to the extension to k ≥ 1? — be precise, this matters for the source
ledger). Type every claim; FALLACY-v2 applies; no ledger edits; no jc2-lean;
do not read ideation-20260903T1200Z-* files or in-progress lane reports.
Drivers to box/prop55k-gate-20260903/. Desk-scale; ≤ 75 min.
Report: xmodel/prop55k-gate-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 75 minutes.
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=box/descentradii-drivers-20260903/phi_delta.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/prop55k-drivers-20260903/census55k.py
charged_input=box/prop55k-drivers-20260903/control_pairs.py
charged_input=box/prop55k-drivers-20260903/prop55k.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/prop55k-gate-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  {{LANE_INPUTS}}/phi_delta.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
c489df1685297552ed2f78b13823161b4ab4f5b2c06e59e38e392f794818fff1  {{LANE_INPUTS}}/census55k.py
9e0ea7b64cae7c2e5d46712520843139b040f4a17e11aa702991e453e8f13d44  {{LANE_INPUTS}}/control_pairs.py
802aaf1e3450fd460a9d5c0aa998720c8da2fabedfea3df3c69e0407869ee34d  {{LANE_INPUTS}}/prop55k.py
```
