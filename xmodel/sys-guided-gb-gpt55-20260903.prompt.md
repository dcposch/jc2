# SYSTEMS lane (build the shared compute unblock — both proof frontiers are now compute-bound at the next index: K16 t≥8 (the b₄=1 z-chart timed out, 17(uuuuu)), the k=4 ray K≥6 (17(vvvvv)), and the (H1) full-basis census (1800s timeouts, 17(nnnnn))): build and TEST a reusable guided-modular-Gröbner helper box/lib/guided_gb.py plus a staged band-file emitter, so that later lanes can decide dim-0 / unit-ideal on systems that overflow a naive foreground Q Gröbner run

OPERATIONAL: this is an ENGINEERING lane — write code, TEST it against banked
ground truth, seal with the passing test log; foreground, ≤ 30 min per test,
≤ 4 cores. Build (all in box/lib/, importable): (1) guided_gb.py — a function
that runs Singular `std` (a) under `stdbuf -oL` (17(rrrrr): block-buffering lost
killed jobs' output — MANDATORY), (b) with a Hilbert-series hint when supplied
(std(I, hilb, weights) — the Card A method cut t=6 to 33s, 17(mmmmm)), (c)
modulo several good primes in parallel, (d) with CRT + rational reconstruction
to lift a modular dim-0 / unit-ideal decision to Q (via the properness
instrument 17(kkkk): a modular dim-0 of a HOMOGENEOUS ideal is a char-0
certificate; state this scope), (e) with the Card A CONTROL BATTERY built in
(NF(gens, G)=0 check, vdim(lead(G)) vs a predicted length, a perturbed-series
negative control that MUST fail) so no guided result is returned without its
controls; return a typed verdict {DIM0_CHAR0, UNIT_IDEAL_CHAR0, POSDIM,
MODULAR_ONLY, INCONCLUSIVE_TIMEOUT} with the certificate. (2) A staged
band-file emitter (17-round Fable systems upgrade): emit an order/joint chart as
SEPARATE weighted band files (one per band/degree), not one 58–256 MB monolith
(17(nnnnn), 17(ttttt)), so a solver can process bands incrementally and a killed
job's completed bands survive. TESTS (must all pass, logged): (T1) reproduce
Card A lengths 3640 (t=5), 23256 (t=6) on both fibres via guided_gb with the
predicted Hilbert series — and the perturbed-series control FAILS; (T2)
reproduce the D=108 δ=3 stage-0 common-h₃ unit ideal (17(ddddd)) via
guided_gb (UNIT_IDEAL verdict, controls pass); (T3) the negative control
t=2,y=1/5 returns POSDIM (dim 1), NOT dim 0; (T4) the staged emitter on a
small (25,15) order chart produces band files whose UNION equals the monolithic
ideal (checksum the generator set). Deliverable: the two modules + a README in
box/lib/ documenting the API and the properness scope, and the test log.
VERDICT: SHIPPED (all tests pass, API documented) / PARTIAL (which tests pass,
what remains). Do NOT try to prove any math OPEN with it here — this is the
tool, its first clients are later lanes. FALLACY-v2 applies (a modular unit is
char-0 only via properness for the dim-0/unit conclusion on a homogeneous
ideal — the helper must TYPE this, not assert char-0 from a single prime). ≤ 150
min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports. Build under box/lib/ and box/sysguidedgb-20260903/.
Report: xmodel/sys-guided-gb-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-24KB; 150 minutes.
charged_input=xmodel/k16-square-tail-stdhilb-gpt55-20260903.md
charged_input=xmodel/k16-rank-criterion-fable5-20260903.md
charged_input=xmodel/order-basis-full-gpt55-20260903.md
charged_input=xmodel/g108-delta3-kill-gate-gpt55-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/orderbasis-20260903/order_basis_full.py
charged_input=box/g108gate-20260903/validate.py
charged_input=box/g108gate-20260903/linear-free-cutoff43.sing
charged_input=box/g108gate-20260903/outer_order_bands.py
charged_input=box/g108gate-20260903/descent_engine.py
charged_input=box/g108gate-20260903/controls.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/sys-guided-gb-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
9b42f72d9d04b404865ab28fe9374839fe0a65a961620007a686e0fb22596afa  {{LANE_INPUTS}}/k16-square-tail-stdhilb-gpt55-20260903.md
7cfa230c0c9ec1b4124b9581b1c461cb19ef004e8a36c2820e7efece0fb185c5  {{LANE_INPUTS}}/k16-rank-criterion-fable5-20260903.md
a8f89e2cc9060d2008375c5bb689b935ef72abdd75b96b1c10d52edf3151c2b6  {{LANE_INPUTS}}/order-basis-full-gpt55-20260903.md
7c14a90a47485d8ac7461a2b0019989dc09cc580cd33fb23a67b08afae48fe3b  {{LANE_INPUTS}}/g108-delta3-kill-gate-gpt55-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
f4e0e98e930f5b4ac9f54c8d3660fb8ca9c58dfd20a0500a456df77b47191639  {{LANE_INPUTS}}/order_basis_full.py
ccc47eddd51bfa07c118bedbce9eec3d6367052ae4175d1fe98546a96826b552  {{LANE_INPUTS}}/validate.py
ae1b5c2c52452552f364c46ceeea224f2d63f54b3f3c547ab2172be376795b46  {{LANE_INPUTS}}/linear-free-cutoff43.sing
de28e2e5f5234e1f6c2ceb66fe30e2e6a8a148b94fa2f941f27e6e8a11dd8eb8  {{LANE_INPUTS}}/outer_order_bands.py
768ba726284f71d375c00f81ce84d58e417dba8dab7ac765760da97157f24259  {{LANE_INPUTS}}/descent_engine.py
d30de9dd2f8eec29746e3ceef8367872fe7427ee0c9908999e231c76111258ad  {{LANE_INPUTS}}/controls.py
```
