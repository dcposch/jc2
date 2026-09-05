# LONG-SOLVE lane (one chart, hours, every trick; the honest compute question for the SMALLEST proved Moh chart): the frozen gi-only report emitted the class-uniform G_i-only chart of the s'=4 control class C_n24m16_Mm12_m2_5_ell1_s4 — 70 unknowns (+T), 66 coefficient generators + (Tc−1) — the smallest chart any (T)-kill of a Moh ≤100 class can use (exact-Q UNIT on it kills the class by the source-support theorem's consumption rule); every run so far had a 600 s watchdog and none finished. TASK: launch ONE r7i.16xlarge (512 GB; `bash ops/fleet/fleet.sh launch 1 r7i.16xlarge`; wait installs msolve 0.10.1; TERMINATE before sealing) and run, detached via dispatch.sh, IN PARALLEL with a 170-minute watchdog each: (a) Singular exact-Q `std` on the chart from box/gi-only-20260905/classes/C_n24m16_Mm12_m2_5_ell1_s4/ with the bihomogeneous weight order (the chart ideal is N²-graded, 17(lllllll): x-charge b and y-deficit iK−a; use a weighted `wp` block order compatible with the grading — homogeneous std is far faster than dp on a non-homogeneous presentation); (b) guided_gb Hilbert-driven modular+CRT (box/lib/guided_gb.py) with `hilb`-driven std after a modular Hilbert series (compute the Hilbert series mod p first — it is a bigraded ideal, so `hilb` with the weight vector); (c) msolve modular F4 (-t 32) on the c = 1 torus section (drop T: set c = 1, which is licensed by the cone lemma — UNIT of I + (Tc−1) ⟺ UNIT of I|_{c=1}) with the 32-bit size guard checked first; (d) Singular `slimgb` on the same c = 1 section; poll every 15 min, log RSS. Any UNIT: exact-Q confirmation or the rational identity in the ORIGINAL ring before it is called a kill (a c = 1 modular unit must be lifted to a c^N identity — record the lift). A completed NONUNIT basis: dimension, degree, a sample point (a necessary-chart survivor: report loudly). FALLACY-v2. ≤ 200 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/gi70-longsolve-20260905/.
Report: xmodel/gi70-longsolve-sol56-20260905.md
Seal (<!-- BODY-END -->); 8-16KB; 200 min.
charged_input=xmodel/gi-only-charts-sol56-20260905.md
charged_input=xmodel/graded-moh-astra-r2-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/gi70-longsolve-sol56-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
0a273aba609bc695f49e1c0db2a1b4cd0a4bb593cbd6a69226891cd2f3dc1279  {{LANE_INPUTS}}/gi-only-charts-sol56-20260905.md
31b1a6a8a94a61968d88f4b92713b6a5eb15d6da1df041f37d055e933ba1deb6  {{LANE_INPUTS}}/graded-moh-astra-r2-20260905.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
