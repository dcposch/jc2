# STRUCTURAL flagship lane (the round's #1 object, 4/5): the UNSPLIT-CONFIGURATION LEMMA — case (A) of (99,66) = (27,18; 21; 8; k=4) is the K=9 member of the TWO-POINT RAY (n,m; M₂; V₂; k) = (3K, 2K; 3K−6; K−1; k=4) with (δ₂', δ₁') = (−1, 0); its K=7, 8 members are the OPEN rows (147,98)→(21,14; 15; 6; 4) and (168,112)→(24,16; 18; 7; 4) — the latter ALSO the D=108 no-split datum (17(fffff)) — so case (A), the D=108 no-split arm, and the three δ₁'=0 two-point rows are ONE OBJECT. Prove the lemma UNIFORMLY in K: for a u_s ≥ 2 skeleton in the UNSPLIT configuration, with minor reduction to (n', m') = ((n/d_s)u_s, (m/d_s)u_s) and (deg_h g, deg_h f) = (e', q'), the low coefficient B₂ is EITHER constant — in which case h | J and the pair is COMPOSITE (excluded) — OR lies in an explicitly bounded space on which the Jacobian coefficient system is INCONSISTENT

OPERATIONAL: skeleton first; every job in the FOREGROUND with `timeout 1800`;
never end the turn with a job running; ≤ 4 cores. Do NOT build the 110–256 MB
monolithic full-D1 Gröbner systems (17(nnnnn) timed out; that is the wrong
solver). Work uniformly in K on the SMALL members first. STRATEGY: (1) fix the
ray coordinates: at general K the pair is h of degree K (Moh p.209 top form for
case (A) at K=9: the 10-coefficient reduction), f = h² + B₂, g = h³ + A₂h + A₃
(the (27,18) shape; generalise the exponents to the (3K,2K) ray), J = f_x g_y −
f_y g_x; (2) the B₂ DICHOTOMY: prove B₂ constant ⇒ h | J ⇒ the pair is composite
(P = φ(h), Q = ψ(h)) hence NOT a Keller counterexample — write the identity;
(3) B₂ nonconstant ⇒ B₂ lies in a bounded space (deg_y B₂ < deg h = K, an
explicit finite chart): build the Jacobian coefficient system on THIS bounded
chart (small — the point of the lemma) at K = 4, 5, 6, 7, 8, 9 and test
inconsistency (unit ideal; independent Singular Rabinowitsch with the standard
controls dim −1, GB 1, reduce(1) 0, CTRL_RAW_DIM > 0, CTRL_UNIT, CTRL_ORIGIN,
and a tame two-point automorphism of the right degrees SURVIVING as a positive
control); (4) find the K-UNIFORM certificate — the killing row(s) as a closed
form in K (mirror the K16 ladder 9(99−3n−11i) and the D=108 three residues
r71=−2j₂, r81=2j₁², r80=−c−j₁⁴+9j₁j₂²; the (27,18) case is the K=9 instance —
compute its residues and fit the K-family); (5) the two independent instruments
must agree (the B₂-dichotomy chart AND the direct moh1612-style kill port to
(3K,2K)); (6) verdict: UNSPLIT-CONFIGURATION LEMMA PROVED uniformly in K (⇒
case (A) dead ⇒ the (99,66) SKELETON verdict is complete for ALL THREE
configurations; ⇒ D=108 CLOSED; ⇒ the δ₁'=0 two-point rows dead — write the
full dependency chain) / PROVED for K = 4..9 with the uniform certificate
conjectured / PARTIAL with the exact residual. FALLACY-v2 applies (a bounded
chart empty is a kill only if the bound is PROVED to contain every case — prove
deg_y B₂ < K covers all; modular unit → char 0 needs the unlocalised ideal or
properness). ≤ 180 min; no ledger edits; no jc2-lean; no ideation-* files; no
in-progress lane reports (k16-rank-criterion, h1-nonres-census, g9966-n2-closure
running). Drivers to box/k4ray-20260903/.
Report: xmodel/k4ray-unsplit-lemma-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-40KB; 180 minutes.
charged_input=xmodel/ideation-20260904T1200Z-opus5.md
charged_input=xmodel/ideation-20260904T1200Z-fable5.md
charged_input=xmodel/g108-nosplit-descent-grok46-20260903.md
charged_input=xmodel/g108-delta3-kill-gate-gpt55-20260903.md
charged_input=xmodel/g9966-chart-necessity-opus5-20260903.md
charged_input=xmodel/order-basis-full-gpt55-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=FALLACY-v2.md
charged_input=box/orderbasis-20260903/order_basis_full.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k4ray-unsplit-lemma-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a32a3eb996435facabb7a39baf3972178e289009967e29f45be2500960633aa0  {{LANE_INPUTS}}/ideation-20260904T1200Z-opus5.md
f14483311f72bdfff9faf8982f47123fd04ed254657a7f91823efb6a052811bd  {{LANE_INPUTS}}/ideation-20260904T1200Z-fable5.md
22678b422d57b66b5c9e9336c8fba97a61b5070cf87165bb7f5f0d3acbf3e742  {{LANE_INPUTS}}/g108-nosplit-descent-grok46-20260903.md
7c14a90a47485d8ac7461a2b0019989dc09cc580cd33fb23a67b08afae48fe3b  {{LANE_INPUTS}}/g108-delta3-kill-gate-gpt55-20260903.md
37beed7ace5aafced312725fcca2e43aa316c19cecc387ef5aafa1c0809bb628  {{LANE_INPUTS}}/g9966-chart-necessity-opus5-20260903.md
a8f89e2cc9060d2008375c5bb689b935ef72abdd75b96b1c10d52edf3151c2b6  {{LANE_INPUTS}}/order-basis-full-gpt55-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
f4e0e98e930f5b4ac9f54c8d3660fb8ca9c58dfd20a0500a456df77b47191639  {{LANE_INPUTS}}/order_basis_full.py
```
