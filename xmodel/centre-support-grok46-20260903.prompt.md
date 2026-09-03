# Research lane (fast, decisive): OPEN[CENTRE-SUPPORT] — can the centre of the bottom disc D₁ of a Moh tower carry a nonzero coefficient at a lattice exponent that is neither a tower radius nor an integer? The one hypothesis on which the Prop 5.6 zero-chain kill (288 of C_FULL_TREE's 598 kills; raw emptiness of D = 60, 81, 105) rests

From the charged second-gate review (Opus, whole-tree-review-opus5-20260903.md
§7.3–§7.4, §10): Def 1.3 (Moh p.146) writes a general point as σ = Σ_{j<δ}
a_j t^j + πt^δ with the sum over ALL exponents below δ in the Puiseux value
group; the centre of D_{j−1} is centre(D_j) + C_j t^{δ_j} + Σ_{δ_j<e<δ_{j−1}}
a_e t^e; the p.201 conjugation confines the support to (1/L_i)Z per window
(L_i = lcm(den δ_s, …, den δ_{i+1})); at s = 2, L₁ = 1 and the only integral
exponents in [−1, δ₁) are {−1, 0}, both removed by Moh's p.190 automorphism
y ↦ y − ax − b (PROVED-IN-SOURCE), which is why Prop 5.6 (σ₁ = πt^{δ₁} ⇒
degrees reducible) closes Prop 5.5; at s ≥ 3 the lattice is finer and the
free coefficients at non-radius non-integer exponents are pinned by nothing
in the tower data — the charged C_FULL_TREE assumes they vanish ("all edges
zero ⇒ σ₁ = πt^{δ₁}"). Free sets on the selected chains of Moh's six rows:
(64,48; 3,3): δ = (−1, 1/4, 9/16), free {1/2}; (75,50; 2,4): (−1, 1/5, 2/3),
free {2/5, 3/5}; (75,50; 3,4): (−1, 1/5, 1/2), free {2/5}; (84,56; 2,3):
(−1, 2/7, 16/21), free {3/7, 4/7, 5/7}; (84,56; 5,3): (−1, 1/4, 7/12), free
{1/2}; (99,66; 8,8): (−1, 1/3, 4/9), free ∅.
YOUR TASK (source open: refs/moh1983_jram340_configurations_of_roots.pdf,
page N = PDF page N−139, pdftoppm -r 300 — read pp.145–147 (Def 1.3 and the
tree data), 168–172 (Props 4.4–4.6), 176–185 (Props 5.1–5.4, Lemma 5.2),
188–190 (Prop 5.6 and its use), 201):
(1) THE CHEAPEST TEST, as charged: take (75,50; M = 55,73; V = 3,4) with free
    set {2/5}. After the p.190 removals, write the generic bottom general
    point σ₁ = C₂t^{1/5} + a_{2/5}t^{2/5} + πt^{1/2} (state exactly which
    earlier terms are fixed by the tower: the level-2 centre C₂t^{δ₂} with
    δ₂ = 1/5), substitute into the Prop 4.6 leading-coefficient computation at
    D₁ (the polynomials g_σ(π), T^ψ_{1,σ}(π) of degrees n*V₂ = 3·3 = 9 and
    m*V₂ = 6 in Moh's normalisation for this row — derive the degrees from
    Def 5.1(1)), and ask whether a_{2/5} ≠ 0 is compatible with (i) the
    degree conditions deg g_σ = n*V₂ (the coefficient of t^{ord} must be the
    stated polynomial in π, not lower), (ii) the r = 1 ODE D(n, −M₁, g_σ,
    T^ψ_{1,σ}) = nonzero constant (Prop 4.6 at r = 1), (iii) the Galois
    action of order A₁ = 2 on π. Do it as exact symbolic algebra over Q in
    the unknowns (a_{2/5}, the star coefficients) — a resultant / Gröbner in
    a handful of unknowns. VERDICT: a_{2/5} FORCED ZERO (the gap closes on
    this row; state the mechanism — is it the ODE, the degree count, or the
    Galois action, and is the mechanism uniform?) / FREE (the gap is real:
    give the value set and what it does to Prop 5.6's applicability) /
    UNDECIDED (why).
(2) Repeat on (64,48; 3,3) with free {1/2} and on (99,66) (free ∅ — the
    control on which Prop 5.6 must apply unconditionally).
(3) SOURCE: does Moh anywhere justify that the intermediate-exponent
    coefficients vanish (Prop 5.3's construction of the next general point,
    pp.181–183: what exactly does it say about the terms between δ_r and
    δ_{r−1}? Lemma 5.2? the "tree data" of §2, p.146–147?), or is p.201's
    "(11) can not always happen as established by Prop 5.6" an aside whose
    hypothesis is unverified for s ≥ 3? Quote.
(4) If (1)–(2) give FORCED ZERO with a uniform mechanism: state the LEMMA
    (with hypotheses) that closes OPEN[CENTRE-SUPPORT], rerun the gated vs
    ungated screens at n ≤ 100 with the lemma (the charged drivers in
    box/wholetree-drivers-20260903/ and box/mohprog-drivers-20260903/) and
    say whether 204 → 55 is restored. If FREE: state the corrected count.
Typed block: PROVED-IN-SOURCE / DERIVED / MEASURED per item; bounded
quantity + cheapest test of every OPEN. Desk-scale (< 15 min one core,
< 4 GB); no ledger edits; no jc2-lean; do not read ideation-20260903T1200Z-*
files or other running lanes' reports. Drivers to
box/centresupport-drivers-20260903/.
Report: xmodel/centre-support-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-20KB; 60 minutes.
charged_input=xmodel/whole-tree-review-opus5-20260903.md
charged_input=xmodel/whole-tree-review-grok46-20260903.md
charged_input=xmodel/moh-program-review-sol56-20260903.md
charged_input=box/wholetree-drivers-20260903/opus5_probe.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/tfe-drivers-20260902/bottomode.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096  {{LANE_INPUTS}}/whole-tree-review-opus5-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  {{LANE_INPUTS}}/whole-tree-review-grok46-20260903.md
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  {{LANE_INPUTS}}/moh-program-review-sol56-20260903.md
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  {{LANE_INPUTS}}/opus5_probe.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
