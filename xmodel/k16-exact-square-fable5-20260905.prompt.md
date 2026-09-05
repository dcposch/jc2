# K16 lane (your own round lever, 17(llllll)): stop chasing the radical — prove the EXACT SQUARE τ_t² ∈ I_{t,+} for all t ≥ 3, with cofactors supported on the top-tail rows T_{t,t..2t−1}. The banked membership exponent at t=3,4 is 2; the top-down ODE recursion is resonance-free ∀t≥3 except the banked failure fibre (t,d)=(2,−1)=y=1/5 (pivots p_j = 2ω(4t+1−j)+2α vanish only at j=6d(2d+1)). τ_t²∈I_{t,+} ⇒ τ_t∈√I_{t,+} = (8.1) ⇒ theorem (T) on the whole K=16 ray

OPERATIONAL: skeleton first; exact CAS foreground under timeout+stdbuf -oL;
box/lib/guided_gb.py available; ≤4 cores; never end the turn with a job running.
CHEAPEST TEST FIRST: lift(I_{t,+}, τ_t²) at t=3,4,5 and read the cofactor
support — is it confined to the top-tail rows, and is the identity uniform in t?
(the banked closed forms of T_{t,k}, τ_t=T_{t,0}, and the coefficient recursion
17(wwwww) are the material). Then attempt the UNIFORM identity τ_t² = Σ c_k(t)·
T_{t,k} with the cofactors c_k closed in t. Controls: t=2 y=1/5 (τ_2²∈I must
FAIL or hold-with-different-exponent — it is the fibre where V0 fails; report
exactly) and y=2/5. Verdict: τ_t²∈I_{t,+} PROVED ∀t≥3 (⇒ (8.1),(T) — full chain,
NOTIFY-WORTHY) / the cheap test result + the exact residual. FALLACY-v2
(modular→char0 via properness for the homogeneous membership; a mod-p identity
is evidence, lift exactly). ≤150 min; no ledger edits; no jc2-lean; no ideation-*.
Drivers to box/k16sq-20260905/.
Report: xmodel/k16-exact-square-fable5-20260905.md
Seal-at-completion (<!-- BODY-END -->; skeleton without it); 15-30KB; 150 min.
charged_input=xmodel/ideation-20260905T0200Z-fable5.md
charged_input=xmodel/k16-hsop-length-allt-opus5-20260903.md
charged_input=xmodel/k16-rank-criterion-fable5-20260903.md
charged_input=xmodel/k16-brcr-closedform-sol56-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-exact-square-fable5-20260905.run.v2` carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines; generate the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
2e1f5cf6d7fedcf12f4da44d87507723e32c845f6640938f303059cdefe3d1e0  {{LANE_INPUTS}}/ideation-20260905T0200Z-fable5.md
a2637d38f715334fec463d947c6be29d2efd93e9ee2175a57e9e6eda266edd83  {{LANE_INPUTS}}/k16-hsop-length-allt-opus5-20260903.md
7cfa230c0c9ec1b4124b9581b1c461cb19ef004e8a36c2820e7efece0fb185c5  {{LANE_INPUTS}}/k16-rank-criterion-fable5-20260903.md
84f2a9573a0e06867cedb969bd882a97fbb6a35a883f7731f38ffb619e587e9f  {{LANE_INPUTS}}/k16-brcr-closedform-sol56-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
