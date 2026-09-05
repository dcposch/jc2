# K16 STRUCTURAL lane (your own round Card A — the new mechanism, AUDIT 17(tttttt)): reduce the K16 atom (V0)-tail / T_{t,2t−1} nonzerodivisor on the Eagon-Northcott curve Γ_t to a GALOIS ALL-OR-NOTHING statement. MEASURED (your round): Γ_t is REDUCED on b₄≠0 at t=3,4,5 (simple points); at t=3 its 7 points form ONE irreducible Galois orbit over A_3 (deg-7 univariate irreducible over Q(√3), Frobenius (2,5) at p=32003). IF the points of Γ_t∩{b₄≠0} are ONE Galois orbit over A_t for all t, then T_top (defined over A_t) vanishes at all or none ⇒ (V0)-tail at fixed t = ONE nonvanishing at ONE simple point ⇒ the all-t problem SPLITS into (I) irreducibility of Γ_t over A_t ∀t and (II) one uniform point with T_top≠0

OPERATIONAL: exact CAS foreground + stdbuf; box/lib/guided_gb.py; the fleet
(~/.ssh/jc2-fleet, workers 172.30.0.7/.18/.28/.166/.254) for the bigger point
polynomials; ≤ 5 cores. Task: (1) exact factorization of the Γ_t point
polynomial (the univariate over A_t whose roots are the b₄≠0 points of Γ_t):
t=4 (46 points, desk), t=5 (265 points, worker) — is it IRREDUCIBLE over A_t
(=Q(√(3(t+1))))? report the factorization + Frobenius cycle types; (2) write the
ALL-OR-NOTHING LEMMA with its Hensel/étale step: Γ_t reduced + T_top ∈ A_t[chart]
⇒ T_top vanishes on the whole orbit or none, so clause (ii) ⇔ T_top(one point)≠0;
(3) the ONE-EVALUATION instrument: at t=3,4,5,6,8 evaluate T_top at ONE Γ-point
(modular at a good prime, a single point — no number-field std) and check ≠0 —
this replaces the timed-out radical/std; (4) the UNIFORM problem (I): is Γ_t
irreducible over A_t for ALL t? attack via the determinantal structure (Γ=V(I₂(N)),
N the (t−1)×2 matrix (C_r,B_r)) — is there a uniform reason the EN curve is
irreducible (a monodromy/Bertini-type or an explicit resultant-irreducibility
argument in t)?; (5) the COMPLEMENTARY liaison check: Γ is arithmetically CM (EN
resolution) — compute the colon ideal (G_1..G_{t−1}):T_top at t=3,4 and test if
it equals (G) (⇔ T_top nonzerodivisor) as a cross-check; (6) VERDICT: (V0) for
all t reduced to (I)+(II) with (II) verified t≤6/8 and (I) PROVED/OPEN; if both
close ⇒ (V0) ⇒ (8.1) ⇒ (T) on the whole K16 ray (MAJOR — say so); else the exact
residual (likely (I) irreducibility). FALLACY-v2 (a modular one-point nonvanishing
is char-0 only if the point is a good reduction of a char-0 Γ-point; state the
lift). ≤ 180 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to
box/k16galois-20260905/.
Report: xmodel/k16-gamma-galois-fable5-20260905.md
Seal (<!-- BODY-END -->); 20-40KB; 180 min.
charged_input=xmodel/ideation-20260905T1200Z-fable5.md
charged_input=xmodel/k16-rank-criterion-fable5-20260903.md
charged_input=xmodel/k16-exact-square-fable5-20260905.md
charged_input=xmodel/k16-brcr-closedform-sol56-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=FALLACY-v2.md
charged_input=box/k16rank-20260903/singular_terminal_driver.py
charged_input=box/k16rank-20260903/killmine.py
charged_input=box/k16rank-20260903/en_degree.py
charged_input=box/k16rank-20260903/tail_structure.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k16-gamma-galois-fable5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
da0c46feb48840b8e8d48842ba12fadc9da829aacdee058423fe873fa0a1327f  {{LANE_INPUTS}}/ideation-20260905T1200Z-fable5.md
7cfa230c0c9ec1b4124b9581b1c461cb19ef004e8a36c2820e7efece0fb185c5  {{LANE_INPUTS}}/k16-rank-criterion-fable5-20260903.md
fb2be9f86f5dca40912005b92603aedcb36a195cffbe34c3bc50ce9afdf370f6  {{LANE_INPUTS}}/k16-exact-square-fable5-20260905.md
84f2a9573a0e06867cedb969bd882a97fbb6a35a883f7731f38ffb619e587e9f  {{LANE_INPUTS}}/k16-brcr-closedform-sol56-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
0cc821ff59adc955d2c6c33a572766b01569d578f1034f343c4f3661cebcf8ed  {{LANE_INPUTS}}/singular_terminal_driver.py
cb3bb83a0ee477093abc0df9581050e6803679ac455ba07e1f76889bee1bb6b2  {{LANE_INPUTS}}/killmine.py
a6c2a657132cb8da333ea7763c1a8185deaeb3e48e4925e02d222ae6e5b0bea7  {{LANE_INPUTS}}/en_degree.py
21908d554bd41347fc651faf03093a43d97e9a44aab82245d54b2e129d6a8a75  {{LANE_INPUTS}}/tail_structure.py
```
