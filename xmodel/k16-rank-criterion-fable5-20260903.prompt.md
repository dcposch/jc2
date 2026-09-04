# STRUCTURAL proof lane (continues the 17(ppppp) breakthrough — the K16 ray's (V0)-for-all-t is now EXACTLY CRITERION RANK, a non-vanishing along a curve): prove, uniformly in t ≥ 3, (i) V(B_1..B_{t−1}, C_1..C_{t−1}) = {0} in Spec P_t (the b₃-coefficients of the split tail rows G_r = B_r b₃ + C_r have no common zero) AND (ii) on the rank-1 locus of the (t−1)×2 matrix N = (C_r, B_r) (expected dimension 1 — a CURVE), every point p ≠ 0 whose kernel has nonzero first coordinate satisfies W_r(p) ≠ 0 for some r (W_r = a₀C_r² − b₀B_rC_r + c₀B_r² the banked eliminant); together (i)∧(ii) ⟺ V(J_t^tail) = {0} ⟺ (V0) for all t ≥ 3 ⟺ (8.1) and theorem (T) on the whole K = 16 ray

Context (banked, USE the charged hsop report 17(ppppp) as the spec): TAIL-SPLIT
gives a₀ = −α_t (unit), G_r = a₀T_{t,2t−1−r} − a_r T_{t,2t−1} = B_r b₃ + C_r
(b₃-linear, weight 2t+2+r); B_r, C_r ∈ P_t = A_t[b₄, q_{2,0..t−1,0}]; the
truncated-spine forms a_r (r ≤ t−2) are computed by 2r+1 scalars (17(wwww)); the
degree-only and coprime-leaders routes are PROVED dead (do not retry them).
STRATEGY (desk algebra; small exact CAS to check, foreground ≤ 20 min): (1)
compute B_r, C_r EXACTLY as weighted forms in P_t at t = 3, 4, 5, 6 from the
charged generators (regenerate the tail via the banked driver; both roots of
H_t where split); tabulate their supports and leading terms; (2) part (i): show
B_1..B_{t−1}, C_1..C_{t−1} have no common zero — the simplest sufficient
structure is that some subset is already a system of parameters (e.g. the C_r
alone, or B_r alone, or a triangular mix); test at t = 3..6 and look for the
UNIFORM reason (a closed form in t for the leading terms of B_r, C_r that makes
a subset an sop); (3) part (ii): parametrise the rank-1 curve (kernel with
nonzero first coordinate ⇒ (C_r, B_r) all proportional to a single (γ:1)-type
vector; substitute and reduce the W_r to a one-variable non-vanishing) and
prove some W_r ≠ 0 on it — the W_r have weight 4t+4+2r, so their leading
behaviour along the curve is computable; find the uniform-in-t argument; (4)
KEY ENABLER: derive the closed form in t of b_r, c_r (equivalently B_r, C_r) —
17(ppppp) names this as the equivalent of the whole criterion; the truncated
spine gives a_r, and b₀, c₀ are the b₃-linear/constant parts of T_{t,2t−1}; push
to b_r, c_r for general r; (5) the t = 2 boundary MUST show (ii) failing at
y = 1/5 (the b₃-axis is exactly a rank-1 curve point with W_r = 0 there) and
holding at y = 2/5 — use it as the discriminating control; (6) verdict:
CRITERION RANK PROVED for all t ≥ 3 (⇒ (V0), (8.1), (T) on the ray — write the
full chain) / part (i) proved + part (ii) OPEN with the exact one-variable
residual / PARTIAL with the closed form of B_r, C_r and the exact remaining
statement. FALLACY-v2 applies (modular dim-0 → char-0 only via properness for
the dim-0 conclusion; a curve non-vanishing proved mod p is not yet char 0 —
say so). ≤ 180 min; no ledger edits; no jc2-lean; no ideation-* files; no
in-progress lane reports (the five ideation-20260904T1200Z-* are running).
Drivers to box/k16rank-20260903/.
Report: xmodel/k16-rank-criterion-fable5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-40KB; 180 minutes.
charged_input=xmodel/k16-hsop-length-allt-opus5-20260903.md
charged_input=xmodel/k16-toptail-quadratics-fable5-20260903.md
charged_input=xmodel/k16-dep-locus-fable5-20260903.md
charged_input=xmodel/k16-hilbert-regseq-sol56-20260903.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16hsop-20260903/eliminant_certificate.py
charged_input=box/k16hsop-20260903/tail_structure.py
charged_input=box/k16hsop-20260903/t4_ideal.py
charged_input=box/k16hsop-20260903/t2_boundary.py
charged_input=box/k16hsop-20260903/alpha_norm_audit.py
charged_input=box/k16toptail-20260903/norm_check.py
charged_input=box/k16toptail-20260903/singular_terminal_driver.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-rank-criterion-fable5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a2637d38f715334fec463d947c6be29d2efd93e9ee2175a57e9e6eda266edd83  {{LANE_INPUTS}}/k16-hsop-length-allt-opus5-20260903.md
638f5e2ed6755b32b92944830e32f6b4a67d321a9e442adca9a59f2f4ba5b05c  {{LANE_INPUTS}}/k16-toptail-quadratics-fable5-20260903.md
d564bc5c5b35a95ee146bca73e67f260e9b70600c9d6f9c931ae17263af085ae  {{LANE_INPUTS}}/k16-dep-locus-fable5-20260903.md
69ea2475c0471ff2254d39d177f35029068d31fea53b29ba7bd35565ec9c29e7  {{LANE_INPUTS}}/k16-hilbert-regseq-sol56-20260903.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
de342d767eeb577d4f2939dcecbb40202df87909294b43c8b3e44c1e5f954f10  {{LANE_INPUTS}}/eliminant_certificate.py
12621e1f99196b8e07eae6f3450f77dbd94d4f53088a546d0496eed4784de576  {{LANE_INPUTS}}/tail_structure.py
ea6b145a97a6a46344e80c12c9836b6fd2949e5c865890355fe369d0de2c2317  {{LANE_INPUTS}}/t4_ideal.py
7fd2a2ffaba20e9ac4d13d19f16af1bb627155aa1756f3fd16ab02058bab0153  {{LANE_INPUTS}}/t2_boundary.py
68aca09f3145ee63bbb73d09508c3cdf2d5082a68dafc2f73768a53382439df3  {{LANE_INPUTS}}/alpha_norm_audit.py
9370bfe7204975cd0b1b37e83de7bef0bb196fb4603f3d777210768063f6df39  {{LANE_INPUTS}}/norm_check.py
0cc821ff59adc955d2c6c33a572766b01569d578f1034f343c4f3661cebcf8ed  {{LANE_INPUTS}}/singular_terminal_driver.py
```
