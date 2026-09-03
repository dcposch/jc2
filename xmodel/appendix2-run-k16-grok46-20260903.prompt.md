# Compiler run (decisive experiment): the Appendix II compiler on the K = 16 ray's descendants (28,20; M₂' = 25; V₂' = 3; k = 1) and (40,28; 37; 3; 1), with the (16,12) member as positive control — and on the rows that become s_eff = 2 after Moh's p.174 drop

Context (banked): the compiler box/appendix2/compile.py (delta 17(bb), charged
with its report) is fail-closed on Moh's six and SATURATED-EMPTY on every
in-budget two-point printed descended row: (15,10) V₂ = 3 and 2, (21,14) V₂ = 5,
(16,12). The K = 16 ray (delta 17(w), PROMOTED, for all t ≥ 1: n = 48t+16,
m = 32t+16, M = (n−12, n−2), V = (3,3), d = (n,16,4,2), u_s = 1, k = 1) descends
by Prop 6.3 to (n', m', M₂', V₂', k) = (12t+4, 8t+4, 12t+1, 3, 1), s' = 2,
R = n' − M₂' − 1 = 2, so δ₂' = −(k+1)/R = −1 (TWO-POINT class, δ₂' = −1) and
δ₁' by the closed form of delta 17(z) / Φ (t = 1: (16,12; 13; 3; X) with
δ₁' = 1/4). t = 1 is Moh's (16,12), already SATURATED-EMPTY by this compiler
(18 unknowns). Task: (1) run the compiler unchanged on t = 1 (control: must
reproduce SATURATED-EMPTY, 18 unknowns, same certificate), t = 2 = (28,20;
25; 3; 1) and t = 3 = (40,28; 37; 3; 1): report unknown counts, the SHAPE
(leading form y^{V₂}(y − x) since u' = d₂' − V₂' = 4 − 3 = 1; D1 order bounds
from δ₁'), the emitted system, the exact Gröbner/saturation verdict at c ≠ 0
(SATURATED-EMPTY with certificate size, or SURVIVES with a point and a
direct-differentiation check J = cx, or COUNTING-BOUND with the exact count
and the resource that exceeds one core — try modular Gröbner (Singular/M2 if
present, else sympy over GF(p) with rational reconstruction only for a
witness), a Newton-tight slice, and elimination ordering before declaring
COUNTING-BOUND); (2) if t = 2 and t = 3 both die, state whether the
certificate has a t-uniform SHAPE (which generators are used; does the
unsaturated ideal at c = 0 stay non-trivial; is the kill "at the Jacobian"
as in §5.1 of the charged report) — this is the data theorem (T) on the
ray needs; if either SURVIVES, that is a REPRESENTATIVE counterexample
candidate: print the pair, type it, do NOT claim a pair in k[x,y] for the
original degrees; (3) implement Φ_eff (delta 17(y), charged audit): after
descent, if M'_{s'} = n' − 1 drop it and set V_{s*+1} = d_{s*+1}; re-run the
descent on the 52 C_FULL_TREE_ODE excess rows at n ≤ 100 and the 19 D = 108
u_s = 1 rows; list the rows that become s_eff = 2 (expected 24 and 12) and
run the compiler on every one within a 40-unknown budget; table of verdicts;
(4) verdict + bounded quantity + cheapest test per OPEN; type every claim
(MEASURED / PROVED-HERE / DERIVED); FALLACY-v2 applies (a kill on the ray's
members is a theorem for those members, not (T) for all t, unless the
certificate is shown uniform). Drivers to box/appendix2-k16-20260903/ (do not
modify box/appendix2/ in place; copy). ≤ 90 min; one core (two if a modular
run needs it); no ledger edits; no jc2-lean; no ideation-* files; no
in-progress lane reports.
Report: xmodel/appendix2-run-k16-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 90 minutes.
charged_input=xmodel/appendix2-compiler-grok46-20260903.md
charged_input=box/appendix2/compile.py
charged_input=box/appendix2/descent_core.py
charged_input=box/appendix2/shape.py
charged_input=box/appendix2/solve.py
charged_input=box/appendix2/solve_worker.py
charged_input=box/appendix2/test_replay.py
charged_input=xmodel/k16-ray-gate-gpt55-20260903.md
charged_input=xmodel/descent-anchor-audit-grok46-20260903.md
charged_input=box/anchor-audit-20260903/measure_anchor.py
charged_input=xmodel/prop55k-opus5-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/mohprog-drivers-20260903/full-tree-ode-excess-witnesses.json
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/appendix2-run-k16-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
dea9f5be619b9507b5ca30db51ddd88401b293e7ab7a0e75c8ae8083a5c79c27  {{LANE_INPUTS}}/appendix2-compiler-grok46-20260903.md
9ed38dbec004b4aab5f381e0cec4b1127446f6bc02297907022305ce4fa1eb41  {{LANE_INPUTS}}/compile.py
276a3088d9231aad977ff25c3a3c1b9316f9b22a77a68537d118138ddbcb7176  {{LANE_INPUTS}}/descent_core.py
d8750d4e512645366e9e0c53153484eb5daa9c785434c1cc59658986d0ab138c  {{LANE_INPUTS}}/shape.py
fec62e04a085aaedb9d9a22e399a7741d9dd28bc8752d22de2b106809472b8ce  {{LANE_INPUTS}}/solve.py
e1547fcc12e97d8dec6a6f23e2d385f9928f96c2589e297438974779ee6d936c  {{LANE_INPUTS}}/solve_worker.py
54eae6a60c4c11160f07c18b7d1d3e1ecc80b1be7b79da105ebda1ba80c4732d  {{LANE_INPUTS}}/test_replay.py
b051a0786091f0219b7bb774d9a188a0765c2080ee17640efc7955616c06653a  {{LANE_INPUTS}}/k16-ray-gate-gpt55-20260903.md
5c5d0e132196b3110c9027d220244534b5763a7d311bcc8efb7219ac596bfa77  {{LANE_INPUTS}}/descent-anchor-audit-grok46-20260903.md
4a5866d5e655add9ee37c6d684e2e12b017da3d8d5a52040d5b4e89a2ac372f6  {{LANE_INPUTS}}/measure_anchor.py
cb8244260483c3722569966053e11e7e13e8bd396d3e5a2ea0b800c17a4c3c3b  {{LANE_INPUTS}}/prop55k-opus5-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5  {{LANE_INPUTS}}/full-tree-ode-excess-witnesses.json
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
