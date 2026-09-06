# HOSTILE GATE (promotion gate; different model from the producer Sol): the frozen t2t3-direct report claims two theorem-tier results that the campaign now relies on for the split class ((99,66) δ=2, δ=5/2; D=108): (A) COMPRESSOR THEOREM — in Moh's order (f,g) = (G,F), attained T₂ lowers the possible degree of a nonzero j = J(F,G) to 20 for (99,66) and 25 for (108,72); attained T₃ with Prop 3.2's exact derivative degree forces such a nonzero j to be a SCALAR; the charged Theorem B excludes j = 0 on the actual source faces with attained T₂; hence a compatible canonical attained-T₂+T₃ datum has j ∈ k^× as a THEOREM (no j variable, no j-localizer, no gauge spent on j = 1); (B) DIRECT PRESENTATION — recursive exact substitution turns the 7,136-variable circuit presentations into direct semantic ideals in 449 / 447 / 507 variables with 2,754 / 2,754 / 3,196 generators, no constraint variable pivoted, and the literal certificate subset d2-z55 (462 upper rows + face row T2_face_55 + 3 localizers; 449 vars; 466 generators; 6,448,959 terms; stream SHA a78c6a46…) is a LITERAL SUBSET so that a unit basis on it kills the full chart. GATE: (1) re-derive (A) from Moh pp.150–157 (Prop 2.2 attainment, Prop 3.1 T₂ family, Prop 3.2 derivative degree) — check the degree bounds 20 and 25 and the scalar conclusion; check what "Theorem B" is (charged source-support closeout / char-degree instrument) and whether it really excludes j = 0 on the faces used; (2) audit (B): read build_direct.py and make_sound_prefix.py; verify on the (99,66) δ=2 chart that every substituted variable is defined by a row linear-monic in it (the isomorphism lemma), that no constraint row was consumed as a pivot, and that the 466-generator subset is literally a subset of the 2,754 direct generators (recompute a sample of generator hashes from the frozen drivers on a worker if needed: you may launch your own r7i.8xlarge via ops/fleet/fleet.sh and must terminate it); (3) state exactly what a Singular exact-Q {1} on d2-z55 would prove (kill of which chart, under which hypotheses — attained T₂ and T₃, canonical datum, minimal counterexample?) and what it would NOT prove; (4) VERDICT per claim: CONFIRMED / CONFIRMED-WITH-FIX / REFUTED; promotable or not. FALLACY-v2. DISK: host writes ≤ 2 MB; `df -h /` before writing; scratch on a worker. No ledger edits; no jc2-lean; no ideation-* input. Notes to box/t2t3-compressor-gate-20260906/.
Report: xmodel/t2t3-compressor-gate-astra-20260906.md
Seal (<!-- BODY-END -->); 8-16KB; 150 min.
charged_input=xmodel/t2t3-direct-sol56-20260906.md
charged_input=xmodel/t2t3-harvest-sol56-20260906.md
charged_input=box/t2t3-direct-20260906/build_direct.py
charged_input=box/t2t3-direct-20260906/make_sound_prefix.py
charged_input=box/t2t3-direct-20260906/build_t2_certificate.py
charged_input=xmodel/char-degree-instrument-astra-r2-20260905.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/t2t3-compressor-gate-astra-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
a0c3c3a0810e1765924ea06a8fdb6b0665feb3884195ea1514f01303eca8817c  {{LANE_INPUTS}}/t2t3-direct-sol56-20260906.md
f3fce66b5412fd80c5cc0f882c6f531b18f2a22ee39e6f597d54f1a28d32852c  {{LANE_INPUTS}}/t2t3-harvest-sol56-20260906.md
77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e  {{LANE_INPUTS}}/build_direct.py
92710ff81699850cd2b9fa93363bdda6d16b796db80f13365bd32e13c0174af2  {{LANE_INPUTS}}/make_sound_prefix.py
db7a83d6ec34c92c6c754c2b2a973da22aeac6b6c2847d2af141fc8e714add79  {{LANE_INPUTS}}/build_t2_certificate.py
d9b95ce9c4588104c9f306d987f91957988611b80d2025a05f14c40568e33b45  {{LANE_INPUTS}}/char-degree-instrument-astra-r2-20260905.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
