# LOW-WEIGHT λ lane (the coordinator's Q1 proposal from the sealed 00:00Z round, charged; the ORDER-chart side, complementary to the split-chart lanes running): in the source-support order chart (17(fffffff): h monic of degree K, P = h^e + Σ α_i h^{e−i}, Q = h^q + Σ β_i h^{q−i}, α_i, β_i on G_i), the second characteristic polynomial T₂ (Prop 3.1 p.157 family) has an h-adic expansion whose coefficients are polynomials in the α_i, β_i; the cone vertex Δ (17(nnnnnnnnn)) is {α_i, β_i constant}, where deg_y T₂ ∈ K·Z; Theorem A (charged char-degree report) says a realized pair has deg_y T₂ = D₂ exactly with a UNIT leader λ, and λ is a polynomial in the TOP y-coefficients of the α_i, β_i blocks — coordinates of SMALL bidegree in the grading of 17(lllllll) (x-charge 0, tiny y-deficit), unlike c at weight (ℓ+1, n+m−1). TASK: (1) derive λ explicitly in the h-adic coordinates for the six Moh ≤100 classes (charts in box/gi-only-20260905/classes/, 70–455 unknowns; D₂ from the class data) and for the four cheapest roster receivers R001–R004 (193–241 unknowns; box/residual66-20260905/); compute wt(λ) in the bigrading and the bidegree at which λ^N would have to lie in I for N = 1, 2, 3; (2) run the WEIGHT-TRUNCATED exact-Q Gröbner (Singular std with a wp block and the declared cutoff; the truncated computations of 17(lllllll) finished in minutes at cutoffs ~120) of I + (Zλ − 1) to cutoff N·wt(λ) + margin, N = 1, 2, 3, on the 70-unknown class first, then the others (local; RSS cap 16 GiB; ≤ 40 min per run; a fleet r7i.8xlarge if needed — TERMINATE before sealing); (3) READ the result correctly: a UNIT of the truncated system is a genuine unit (dropping rows is safe — a truncation keeps a SUBSET of rows) ⇒ the class is DEAD (no realization attains its characteristic degree) — PROVED-HERE for gate with the cofactor identity; a non-unit at cutoff w proves only "no relation of weight ≤ w" — report the weight reached; (4) also test the λ-localizer on the cone-vertex control: the Δ point must be excluded (λ = 0 there). FALLACY-v2 (a truncated non-unit is not a survivor; the leader must be the ACTUAL attained leader per Theorem A, with its printed derivation). DISK DISCIPLINE: ~3 GB free — report + notes ≤ 2 MB; no artifact trees. ≤ 200 min; no ledger edits; no jc2-lean; no other ideation-* input. Drivers to box/lambda-lowweight-20260906/.
Report: xmodel/lambda-lowweight-astra-20260906.md
Seal (<!-- BODY-END -->); 12-25KB; 200 min.
charged_input=xmodel/ideation-20260906T0000Z-fable5.md
charged_input=xmodel/char-degree-instrument-astra-r2-20260905.md
charged_input=xmodel/graded-moh-astra-r2-20260905.md
charged_input=xmodel/source-support-closeout-opus5-20260905.md
charged_input=xmodel/gi-only-charts-sol56-20260905.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=box/lib/guided_gb.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/lambda-lowweight-astra-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
9747bea7d68c83e7b46905e3ae767661bc9ded4cd9e3d77f43d90bf4eb718b87  {{LANE_INPUTS}}/ideation-20260906T0000Z-fable5.md
d9b95ce9c4588104c9f306d987f91957988611b80d2025a05f14c40568e33b45  {{LANE_INPUTS}}/char-degree-instrument-astra-r2-20260905.md
31b1a6a8a94a61968d88f4b92713b6a5eb15d6da1df041f37d055e933ba1deb6  {{LANE_INPUTS}}/graded-moh-astra-r2-20260905.md
a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c  {{LANE_INPUTS}}/source-support-closeout-opus5-20260905.md
0a273aba609bc695f49e1c0db2a1b4cd0a4bb593cbd6a69226891cd2f3dc1279  {{LANE_INPUTS}}/gi-only-charts-sol56-20260905.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826  {{LANE_INPUTS}}/guided_gb.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
