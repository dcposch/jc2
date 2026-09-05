# COVERAGE lane (repair of 17(zzzzzz) §2.1; the k=4-ray kills K=7,8,9 [17(aaaaaa)/(bbbbbb)] chart the β block at deg β = b_min ONLY): the h block of the k=4-ray charts is SOUND (ℓ=4 ⇒ δ_s=−1, total-degree cap = the gate's G₁), but the β strata b_min < b ≤ b_max are UNCOVERED: (K, b_min, b_max) = (7,5,13), (8,6,15), (9,7,17); the composite arm kills deg β=0, the 3b≤2K argument kills b<b_min, the pinned chart kills b=b_min; nothing covers the 8/9/10 higher strata (β block 70/92/117 coefficients at b_max vs 15/21/28 charted; the LEVEL-4 one-scalar pin is proved only at b=b_min — k4ray-degree-tower-opus5-20260903.md:368-378). TASK: (1) FIRST try to extend the ARGUMENT: does the 3b≤2K degree argument or the degree-tower analysis (k4ray-degree-tower) extend to exclude b>b_min outright (a degree/order count on J=cx⁴ with deg β=b)? if a clean proof exists, that closes all strata at once — state and prove it; (2) otherwise BUILD the per-stratum pinned charts for K=8 (9 strata) and K=9 (10 strata), then K=7 (8), using the exact lower-band parametrization of 17(bbbbbb) (box/ from k4ray-lowerband) with the top band UNPINNED (the one-scalar pin is not available above b_min — chart the full top band or prove its pin for each b), and SOLVE (guided_gb / msolve on fleet workers; the K=8/9 charts previously needed the lower-band parametrization to fit in 36 variables — report the sizes honestly); (3) VERDICT: K=8 no-split row DEAD for ALL deg β (⇒ D=108 no-split arm restored) / K=9 case (A) DEAD for all deg β (⇒ (99,66) configuration (A) restored) / list of surviving strata with sizes. FLEET (for heavy solves): `sh ops/fleet/fleet.sh launch 1 r7i.8xlarge` (or c7i.4xlarge), `fleet.sh ips`, `ops/fleet/dispatch.sh run <IP> <CLASS> <STEM>`, `dispatch.sh poll`; TERMINATE what you launch (`fleet.sh term <ID>`); never touch workers you did not launch. FALLACY-v2 (dropping ROWS is safe, dropping UNKNOWNS by a weight floor is not; every normalization needs its group element; a modular UNIT needs exact-Q confirmation). No ledger edits; no jc2-lean; no ideation-*. ≤ 240 min. Drivers to box/k4ray-beta-strata-20260905/.
Report: xmodel/k4ray-beta-strata-grok46-20260905.md
Seal (<!-- BODY-END -->); 10-25KB; 240 min.
charged_input=xmodel/support-regression-gate-opus5-20260905.md
charged_input=xmodel/k4ray-pinned-chart-gpt55-20260903.md
charged_input=xmodel/k4ray-degree-tower-opus5-20260903.md
charged_input=box/k4raypinned-20260903/pinned_chart.py
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k4ray-beta-strata-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
e08f6e40f817e5bf354073e0fb685b4e6b3625c6a7442b1d90ac6ef4dffa0990  {{LANE_INPUTS}}/support-regression-gate-opus5-20260905.md
db150d8b078b9626348dd75dc21f966b20671e070e2c2349c1224bf2a46f130f  {{LANE_INPUTS}}/k4ray-pinned-chart-gpt55-20260903.md
2befb3cac8e51305e65ab0e48de485a7098ba104a3620d8b174927791a896a2a  {{LANE_INPUTS}}/k4ray-degree-tower-opus5-20260903.md
eed2cdf5cc5b85e3358013416bca7f6f6bd272138533ff0c065a86afb4c47e43  {{LANE_INPUTS}}/pinned_chart.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
c0ea96034bf12b7445aa123f00cf600baaca81751f36a91855987f44fd6311e3  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
