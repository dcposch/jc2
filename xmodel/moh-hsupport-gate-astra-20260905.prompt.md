# GATE lane (Astra; your own round §2-§3 — this GATES the Moh ≤100 finish, AUDIT 17(tttttt)): the corrected s'=3/s'=4 descended monomial-Jacobian order charts for the 12 residual u_s=1 rows still owe an h-SUPPORT LEMMA — h retains two caps and 8 of the 12 fibres OMIT D1-allowed h-monomials (you listed 76 coordinates in your round submission). Until this is settled, a Singular timeout (17(ssssss)) and any msolve UNIT (moh14-msolve, running) are NOT valid theorem-(T) kills. Prove the h-support theorem — that the emitted chart's h-support IS the full necessary D1 over-approximation for a descended monomial-Jacobian pair — OR identify the missing hypothesis and REPAIR the chart to include the omitted D1 h-monomials, per fibre

You are Astra. OPERATIONAL: source + algebra; the 76-coordinate desk comparison
is in your box/ideation1200-astra-20260905/; foreground; the fleet (ops/fleet/,
~/.ssh/jc2-fleet, workers 172.30.0.7/.18/.28/.166/.254) + msolve are available if
a repaired chart needs re-solving. Task: (1) state, from Moh Thm 1.2 / the D1
construction (order_basis_full.py 17(nnnnn); the s'=3 compiler 17(nnnnnn)), the
NECESSARY h-support for a descended monomial-Jacobian pair (P,Q), J=c·x^ℓ, at
descended depth s'∈{3,4}: which h-monomials (y^a x^b) are D1-allowed and MUST be
free coordinates; (2) compare against the emitted charts' h-support per fibre —
confirm your finding that 8 fibres omit D1-allowed h-monomials (the 76 coords);
is the omission a SOUND gauge/normalisation (WLOG — then the h-support lemma
HOLDS and the emitted chart IS complete) or an unsourced cap (then the chart is
a SUB-SLICE and its emptiness/timeout proves nothing — REPAIR it: add the
omitted monomials, re-emit the builder via the fixed builder_fix.py, and
re-solve that fibre with msolve on the fleet); (3) VERDICT per fibre: h-SUPPORT-
COMPLETE (chart is the full necessary over-approx — a msolve UNIT there IS a
valid kill) / REPAIRED (chart completed; give the new unknown count + re-solve
status) / OPEN (the support obligation cannot be discharged — state exactly);
(4) the consumption rule: for each of the 6 classes, state whether a msolve UNIT
(exact-Q confirmed) on its now-complete chart would be a valid (T)-kill; (5)
controls: a known-good fibre (V3_2, 425 gens) must be h-support-complete or
repaired without changing its generators; FALLACY-v2 (a cap is WLOG only with a
group element moving the omitted monomial; else it is a sub-slice). ≤ 180 min;
you MAY edit box/moh14-charts-20260905/; no other ledger edits; no jc2-lean; no
ideation-*.
Report: xmodel/moh-hsupport-gate-astra-20260905.md
Seal (<!-- BODY-END -->); 15-30KB; 180 min.
charged_input=xmodel/ideation-20260905T1200Z-astra.md
charged_input=xmodel/moh14-fullorder-grok46-20260905.md
charged_input=xmodel/moh14-fix-solve-opus5-20260905.md
charged_input=xmodel/order-basis-full-gpt55-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/moh14-charts-20260905/jacobian_check.py
charged_input=box/moh14-charts-20260905/sprime3_compiler.py
charged_input=box/moh14-charts-20260905/fullorder_audit.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/moh-hsupport-gate-astra-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
0c837c96b08bde6f42f2ae30554f5a71ad6ca4f2a10b7b0cd6bde2d1ddc55666  {{LANE_INPUTS}}/ideation-20260905T1200Z-astra.md
26ea98c552af9b7bb817cea598f2aa037672269db0fb79c340ffaac6a0716999  {{LANE_INPUTS}}/moh14-fullorder-grok46-20260905.md
2372687402bdb5b83a9ecd28d206f215abb834508f9a937b94c81350a54f42e2  {{LANE_INPUTS}}/moh14-fix-solve-opus5-20260905.md
a8f89e2cc9060d2008375c5bb689b935ef72abdd75b96b1c10d52edf3151c2b6  {{LANE_INPUTS}}/order-basis-full-gpt55-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
3865d138e98a0b78b325a2a7d7d3f19315c8bdb27d36108f897c2dd6346395c9  {{LANE_INPUTS}}/jacobian_check.py
e6fdaf819e105b51cde75ecd832b41b8d0be564db9f79bf2aaf09d6afc77d363  {{LANE_INPUTS}}/sprime3_compiler.py
f137e8a17eb86caf13296d5f3b7c90061bca3609da1fb3baf19cfe23917ea300  {{LANE_INPUTS}}/fullorder_audit.py
```
