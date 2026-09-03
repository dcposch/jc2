# Rerun lane: the full symbolic partition strata of (33,22; 30; 8; k = 1) [parent (132,88)] and (45,30; 42; 11; k = 1) [parent (180,120)] with the CORRECTED support rule (Theorem-1.2 threshold B = V₂'δ₁' + u'δ₂', β cap deg_x ≤ k+1, deg_x J sanity gate) — are delta 17(vv)'s kills theorems or slices?

Context (banked, AUDIT deltas 17(rr), (vv), (uu), (bbb)): the two rows were killed
over all their partition strata ([3], [2,1] resp. [4], [3,1], [2,2], symbolic
slopes, Ω saturation) by topface_cases.py / strata_gate.py, which use the OLD
support rule of shape.py; the corrected generator (box/chartfix-20260903/,
charged) changes the β inventory of these two rows (33 → 28 and 55 → 40), which
is "not a superset after the k+1 cap", so the old kills may be slices. Task:
(1) determine PRECISELY the relation between the old and corrected monomial
supports for h and for each β_j on these rows (old ⊆ new? new ⊆ old?
incomparable? list the differing monomials) — if new ⊆ old the old kills are
supersets and stand (say so with the argument); (2) regardless, RERUN every
stratum of both rows with the corrected generator (port the strata emission of
topface_cases.py/strata_gate.py onto the corrected shape.py; keep the symbolic
slopes and the Ω non-degeneracy saturation; print deg_x J on the generic ansatz
per stratum — must reach k = 1); three primes then Q; report per stratum
unknowns/equations/verdict; (3) also rerun (21,14; 18; 5; k = 1) strata [2], [1,1]
and (15,10; 11; 2; k = 2) strata [3], [2,1], [1,1,1] with the corrected generator
(the restorations of delta 17(vv)) — persist?; (4) verdict per row: CONFIRMED
(kills stand under the corrected chart) / GAP / REFUTED (a stratum survives —
print the point and the direct Jacobian check, REPRESENTATIVE); type every
claim; FALLACY-v2 applies. ≤ 90 min; 2 cores; no ledger edits; no jc2-lean; no
ideation-* files; no in-progress lane reports (bigrows-preprocess, k16-t4-
normalizer-gate, xu-inequality-screen, k16-middle-spine, moh9966-B-lift).
Drivers to box/strata-rerun-20260903/.
Report: xmodel/strata-rerun-corrected-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 90 minutes.
charged_input=xmodel/chart-fix-d1zero-gpt55-20260903.md
charged_input=box/chartfix-20260903/shape.py
charged_input=box/chartfix-20260903/twopoint_order_batch.py
charged_input=xmodel/strata-gate-gpt55-20260903.md
charged_input=box/strata-gate-20260903/strata_gate.py
charged_input=xmodel/topface-license-sol56-20260903.md
charged_input=box/topface-20260903/topface_cases.py
charged_input=xmodel/twopoint-kills-gate-fable5-20260903.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/strata-rerun-corrected-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
0a8d1ba229ffeee3b8c6e89b103c35f5f57154c8be93edf3c06c8b498d200d4f  {{LANE_INPUTS}}/chart-fix-d1zero-gpt55-20260903.md
ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de  {{LANE_INPUTS}}/shape.py
16497553047222b6b16450f26286a65dc69b27b4c00f8fcd518f0cce0af6c8e5  {{LANE_INPUTS}}/twopoint_order_batch.py
4a2e31602ced3fe8799195ec9cb5cbb29fa0ba23f57e0df4d0403cc4a53ba36b  {{LANE_INPUTS}}/strata-gate-gpt55-20260903.md
e0e84581323f97bdee0df10290440548ed4474178cfaafebbd28e5e172df0898  {{LANE_INPUTS}}/strata_gate.py
53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae  {{LANE_INPUTS}}/topface-license-sol56-20260903.md
369bafb1341f96708f6886e79c93fb9bdad8e70abb1ae4c69ddd1dd6a9c62082  {{LANE_INPUTS}}/topface_cases.py
d68d13f6078172e955e9e987e60bd145e81ee0069c8b4f16181e64f7a558b681  {{LANE_INPUTS}}/twopoint-kills-gate-fable5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
