# Research lane (proof attack, bounded): theorem (T) on the descended K = 16 ray — a t-uniform Newton-polygon / Lemma 2.1 obstruction for monomial-Jacobian pairs of π-degrees (12t+4, 8t+4) with M₂' = 12t+1 = n'−3, V₂' = 3, J = cγ

Context (banked, AUDIT delta 17(v); Grok's blind 1200Z submission
§2.2/§4.2/Card III; do NOT read other ideation-20260903T1200Z-* files):
the screened census is cofinally nonempty — for every t ≥ 1 the skeleton
n = 48t+16, m = 32t+16, M = (n−12, n−2), V = (3,3), s = 3, d = (n,16,4,2),
u_s = 1 survives PATH-ARITH(1)–(13) + whole-major-tree (gap-free) + ODE +
nested packing, with t = 1 Moh's printed (64,48). By Prop 6.3/6.4 (m2-descent
§4; descent-radii; delta 17(q),(t)) each member descends to a
monomial-Jacobian pair in k[γ,π]: π-degrees (n', m') = (12t+4, 8t+4),
[P,Q] = cγ^{V_s−u_s−1} = cγ (k_jac = 1), with inherited descended tower data
s' = 2, M₂' = M₂/d_s = 12t+1 = n'−3, V₂' = 3, and radii by Φ:
δ' = (k_jac+1)·Def 5.1(3)(descended data). At t = 1 this is Moh's p.207 row
(16,12; 13; 3; X), which Moh kills in Appendix II by hand (and which the
campaign has re-killed mechanically, SATURATED-EMPTY, m2-descent §4 controls).
Theorem (T) on this ray = no such pair exists for any t ≥ 1 — a proof of JC2
along the only known cofinal screened family. Lemma 2.1 (Moh p.151,
source-read in m2-descent §4.3): for a monomial-Jacobian pair with J = cγ^k
(here k = 1), writing g = Σ g_j(γ)π^j (or in Moh's (x,y) of Appendix II), the
coefficients g_j ∈ k are constants for j < m'−1 and deg_x g_{m'−1} = k+1 = 2;
same for f with n'. Task: (1) SOURCE-READ Lemma 2.1 and Appendix II (refs/
moh1983 pp.151, 205–212) and state precisely what Lemma 2.1 pins for
(f,g) with J = cγ; (2) compute the Newton polygon / characteristic data
(Puiseux slopes, the Moh M₂', V₂' of the descended tower per Def 5.1 and
Prop 5.3 restricted to the descended s' = 2 data) of a Lemma-2.1-shaped pair
of degrees (12t+4, 8t+4) as a function of t, and test compatibility with
M₂' = 12t+1, V₂' = 3 — do it symbolically in t with sympy, and check the
t = 1 control (must be incompatible / empty by Moh, or the derivation is
wrong); (3) if the polygon alone does not obstruct, push one step further
along Appendix II: approximate-root truncation with Φ-radii on the t = 2
instance (28,20; M₂' = 25, V₂' = 3, J = cγ) — count unknowns after Lemma
2.1 + order conditions, and if ≤ ~200 unknowns run the saturation
(sympy/Singular if present; ideal + saturation by the leading coefficient),
positive control Moh (16,12), negative control an actual monomial-Jacobian
pair without the 4-tuple, e.g. (y, x²/2)-type with J = x — must SURVIVE the
Lemma-2.1 shape but must FAIL the 4-tuple; (4) verdict: T-K16 PROVED for all
t (with the obstruction stated as a theorem with proof), or PROVED at t = 2
only (SATURATED-EMPTY, with the certificate size), or COUNTING-BOUND, or
SURVIVES (a candidate pair — type REPRESENTATIVE, print it); type every
claim (SOURCE-READ / DERIVED / MEASURED / PROVED-HERE), bounded quantity +
cheapest test of every OPEN; state explicitly whether the Φ radii and the
descended (8)–(13) were used and where OPEN[DESCENT-ANCHOR] (n' − M₂' − 1 =
2 ≠ 0 here — check) bites. FALLACY-v2 applies: no over-read of a screen as
attainment, no promotion of a control. Drivers to box/k16T-drivers-20260903/.
Bounded: one core, ≤ 90 min wall; no ledger edits; no jc2-lean.
Report: xmodel/k16-ray-T-newton-sol56-v3-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 90 minutes.
charged_input=xmodel/ideation-20260903T1200Z-grok46.md
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=box/descentradii-drivers-20260903/phi_delta.py
charged_input=box/m2descent-drivers-20260903/moh_1510_control.py
charged_input=box/m2descent-drivers-20260903/moh_1510_control2.py
charged_input=box/descentradii-drivers-20260903/g2_fullh_mohbeta.py
charged_input=xmodel/screened-census-grok46-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-ray-T-newton-sol56-v3-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk (e.g. paste the sha256 and basename fields prefixed by the {{LANE_INPUTS}} directory) and run `sha256sum -c`; if you cannot read the receipt, write the block below to a file with a heredoc copied verbatim (do not paraphrase or abbreviate); stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
8d98cf8886304fd8e68f86b31c813013eb4ab495fd983ceaff9ec38128dff618  {{LANE_INPUTS}}/ideation-20260903T1200Z-grok46.md
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  {{LANE_INPUTS}}/phi_delta.py
fe4acde9abf6661c85425fdc58f6f9308b3e6269e5506f0c6252284bd3de335f  {{LANE_INPUTS}}/moh_1510_control.py
5ea3845b6e6f7022a59b0620b22f017c632ef08e6e5d0675f9c3d0274032566b  {{LANE_INPUTS}}/moh_1510_control2.py
69a884c81cdc1d68f45e9b75aa2c9ee4f64bd24cdb49f90bc7c7d43784bdfdd6  {{LANE_INPUTS}}/g2_fullh_mohbeta.py
29a6f54dff3dbe2e2ad4cbb07dfdb7b18168e86848d5abb4644f2024f766b82d  {{LANE_INPUTS}}/screened-census-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
