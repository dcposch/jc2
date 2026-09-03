# Hostile gate (page images): the zero-factor centre-support lemma — does it close OPEN[CENTRE-SUPPORT] and justify the ungated Prop 5.6 zero-chain kill in the whole-tree screen?

Charged claim (centre-support-grok46-20260903.md §1, §5; AUDIT delta 17(cc)
PROVISIONAL): Lemma (zero-factor centre support): with the chart at D_r
centred at 0 and π a factor of the Prop 4.6 polynomial p(π), the p.201(8)
Galois action t̄ ↦ ωt̄ (ω primitive A_{r−1}-th root of unity, t̄^{LA_{r−1}} = t)
moves every non-fixed exponent e ∈ (δ_r, δ_{r−1}) of the centre of the unique
zero-factor child; a moved term a·t^e with a ≠ 0 would give an orbit of
distinct centres at logarithmic distance e, which by Lemma 1.1 cannot lie in
one disc of radius δ_{r−1} > e, contradicting uniqueness of the zero root of p
(Moh p.184's "a noninteger exponent produces different roots"); the fixed
exponents are integers, removed by p.190; hence on a still-centred chain
σ₁ = π t^{δ₁} and Prop 5.6 applies to every all-(11) major path reaching D₁.
Consequence: the UNGATED C_FULL_TREE (delta 17(r)) is the correct screen and
the gap-free/gapped split of delta 17(u) collapses (204 → 55 at n ≤ 100).
The second gate (whole-tree-review-opus5, charged) had flagged this step as
GAPPED: Prop 5.6 needs the zero child's centre to have no free coefficients
below δ₁, and Moh's proof (p.189) is written for a specific centred chart.
Task: (1) open Moh pp.147–150 (Def 1.3, Lemma 1.1), 183–184, 189–190, 200–201
(p.201(8)–(11)) as page images (pdftoppm -r 200; name the pages) and check
each hypothesis and each step of the lemma against the print: is the p.201(8)
automorphism defined on the coefficient field of the child's centre as the
lemma uses it; does "uniqueness of the zero root of p" hold in the sense
needed (p has π as a SIMPLE factor? or a factor of multiplicity b — what if
b ≥ 2, i.e. the forced-zero multiplicity, the very case the screen kills?);
does Lemma 1.1 apply to centres at logarithmic distance e vs disc radius
δ_{r−1} exactly as stated (sign/order conventions of Moh's logarithmic
radii — check with Def 1.3); does the p.184 argument require the root to be
Galois-fixed, and is π = 0 fixed under the action as claimed; does the
argument need L = 1 or does it hold for general L; (2) replay
box/centresupport-drivers-20260903/ and opus5_probe.py: the (75,50; 55,73;
3,4) cheapest test (the three D₁ tests do not cut a_{2/5}; the parent A₂ = 5
kill), and the 204 → 55 / 21 → 11 table; (3) verdict: CONFIRMED (the ungated
screen is promotable; state the scope: which paths — all still-centred
zero chains? — and whether OPEN[NONZERO-PARENT-TWIST] is correctly
separated), GAP (name the step and the cheapest test), or REFUTED. Type
every claim; FALLACY-v2 applies. Desk-scale; no ledger edits; no jc2-lean;
no ideation-20260903T1200Z-* files; no in-progress lane reports. Drivers to
box/centre-gate-20260903/.
Report: xmodel/centre-support-gate-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-14KB; 60 minutes.
charged_input=xmodel/centre-support-grok46-20260903.md
charged_input=xmodel/whole-tree-review-opus5-20260903.md
charged_input=box/wholetree-drivers-20260903/opus5_probe.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/centresupport-drivers-20260903/centre_support_test.py
charged_input=box/centresupport-drivers-20260903/full_tree_partition.py
charged_input=box/centresupport-drivers-20260903/moh_skeleton_full.py
charged_input=box/centresupport-drivers-20260903/moh_skeleton_full_frozen.py
charged_input=box/centresupport-drivers-20260903/opus5_probe.py
charged_input=box/centresupport-drivers-20260903/rerun_screens.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/centre-support-gate-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
c6acd87403180ca492cae9479c0dc2ec54f359aaa46aa453e28a4ce40fefdc00  {{LANE_INPUTS}}/centre-support-grok46-20260903.md
27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096  {{LANE_INPUTS}}/whole-tree-review-opus5-20260903.md
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  {{LANE_INPUTS}}/opus5_probe.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
ab27af0349154c2d3455366255c5a4978aec2140c10066ee26951c1c28d2d969  {{LANE_INPUTS}}/centre_support_test.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full_frozen.py
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  {{LANE_INPUTS}}/opus5_probe.py
1150ec4416bb690a2fcf4ed3b0983f389d2c400e5fefe8cda4612b55e1cf9372  {{LANE_INPUTS}}/rerun_screens.py
```
