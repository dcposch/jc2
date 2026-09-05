# CENSUS SWEEP lane (the compute half of the all-degree program; round 1200Z Q4): run the u_s ≥ 2 census kill sweep on the fleet, SMALLEST descended classes first. The per-row kill method is validated (top pin + exact lower-band parametrization → guided_gb/msolve; K=7,8,9 and S5/S6 died this way, 17(bbbbbb)/(dddddd)); the u_s≥2 census at 16 ≤ n ≤ 200 compresses to 132 sharpened keys / up to 1359 descended classes (17(eeeeee), Astra-corrected 296→132). Build a reusable box/lib/census_sweep.py (enumerate admissible skeletons per degree → descended class → chart via the FIXED builder (builder_fix.py) → msolve/guided_gb → typed certificate) and RUN it on the smallest classes, killing as many as the budget allows

OPERATIONAL: Grok — FOREGROUND only (setsid/nohup on workers, then poll; never an
unwaited background job). Fleet: ~/.ssh/jc2-fleet, c7i workers 172.30.0.7/.18/.28
(64GB); msolve + Singular + guided_gb + builder_fix.py on them; rsync as needed.
LESSONS (apply): the s'≥3 Moh charts at 88–378 unknowns are compute-bound for
BOTH Singular and msolve (17(ssssss)/(uuuuuu)) — so SORT BY SIZE and sweep the
SMALL classes (≤ ~120 unknowns) where kills complete in seconds–minutes; the
chart must be the FULL necessary over-approximation (h-support incl., 17(tttttt)
— for u_s≥2 SPLIT rows this is the joint chart: order + minor-incidence + pole +
Jacobian rows, as at (99,66)/D=108); a class dies only if EVERY fibre/stem is
UNIT (conjunctive). Task: (1) write census_sweep.py (enumerate → descend →
classify split/unsplit → build the right chart → solve → certificate JSON per
class); (2) enumerate the u_s≥2 census (moh_skeleton_full.py), compute descended
classes, SORT by chart size; (3) sweep the smallest N classes (as many as fit
in budget, in parallel across the 3 workers): per class report UNIT (dead, exact-
Q or 3-prime + exact confirm) / NON-EMPTY (a surviving point — extract, test
J=const; not a counterexample unless it lifts) / TIMEOUT; (4) tally: k classes
DEAD of the swept N, plus the size threshold where the sweep becomes compute-
bound; (5) controls: reproduce the D=108 δ=3 kill (17(ddddd)) and the (99,66)
δ=2 stage-4 unit via the sweep; a tame automorphism survives. FALLACY-v2 (a
class kill needs the FULL necessary chart + every stem UNIT + exact-Q confirm).
Commit census_sweep.py. ≤ 200 min; you MAY edit box/lib/ and box/census-*; no
other ledger edits; no jc2-lean; no ideation-*.
Report: xmodel/census-sweep-grok46-20260905.md
Seal (<!-- BODY-END -->); 15-30KB; 200 min.
charged_input=xmodel/ideation-20260905T1200Z-synthesis.md
charged_input=xmodel/moh14-fix-solve-opus5-20260905.md
charged_input=xmodel/k4ray-K89-sol56-20260903.md
charged_input=xmodel/h1-nonres-census-sol56-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=box/lib/staged_band_emitter.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/moh14-charts-20260905/builder_fix.py
charged_input=box/k4rayk89-20260903/consolidate_k9a_authoritative_sol56.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/census-sweep-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
f72510a27816d72cfea467b5cdd126b13ade765fcb3fbee829e731e262a858f4  {{LANE_INPUTS}}/ideation-20260905T1200Z-synthesis.md
2372687402bdb5b83a9ecd28d206f215abb834508f9a937b94c81350a54f42e2  {{LANE_INPUTS}}/moh14-fix-solve-opus5-20260905.md
4797dbe918a855ffb6f71ba6608685347b0c1fc502e435c01a1bcfb1bb8adb98  {{LANE_INPUTS}}/k4ray-K89-sol56-20260903.md
ad07e1d621824cceec94b31866821cbe0a7dde83a6a4480a690ed9c90507a7ca  {{LANE_INPUTS}}/h1-nonres-census-sol56-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
7c2f88430158fc01b2aa4e1bc2af1902f92168d10cd48ee5095506beb149dce8  {{LANE_INPUTS}}/staged_band_emitter.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b  {{LANE_INPUTS}}/builder_fix.py
425038683c3941b6030a646974d7c1f7159536ebfa0e05a974d63843fa363ebc  {{LANE_INPUTS}}/consolidate_k9a_authoritative_sol56.py
```
