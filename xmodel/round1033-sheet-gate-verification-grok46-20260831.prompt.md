# Verification lane: SHEET-GATE report — countermodel hunt

You are the second, independent arm of a paired review (a different
reviewer runs the line-by-line gate; you do NOT coordinate with it).
Your lens is countermodels and sanity stress-tests, not line-editing.

charged_input=xmodel/round1033-sheet-gate-opus5-20260831.md
charged_input=xmodel/ideation-20260831T1033Z-synthesis.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb  {{LANE_INPUTS}}/round1033-sheet-gate-opus5-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
```

The charged report claims, for Keller `F` with irreducible `A_F` and
`A^1` normalization: identity (M') `a*(nu+s-1) - sum_p a_p = d*nu - 1`
with `1<=a<=d-2`; a covering lemma for `F^{-1}(D_0)->D_0` of degree
`a`; `a_p = s_p - b_p`; `e_j = 1+v_j(dx∧dy)` for dicriticals; a
`chi_c` identity (E); and a weighted budget
`sum_j delta_j e_j <= d-1`.

Stress-test with explicit maps and curves, exact arithmetic only:

1. Non-Keller controls where hypotheses fail ONE at a time: e.g.
   `F=(x,xy)` (etale fails on a curve), `F=(x, y^2)` (degree 2,
   non-etale), a non-injective etale endomorphism candidate of a
   punctured surface, proper maps with `A_F` empty. In each, compute
   `A_F`, `d`, the fibres, and check which of the report's lemmas
   correctly fail or survive with the failure traced to the exact
   hypothesis. A lemma that HOLDS in a control where its stated
   hypotheses fail is evidence its proof uses less than it claims — a
   finding either way.
2. The Euler identity (E): verify on at least two controls by direct
   `chi_c` computation (e.g. `F=(x,xy)`: `A_F = {u-axis? compute}`,
   `F^{-1}(A_F)`, both sides exactly).
3. Lemma 4.2's valuation formula: compute `v(dx∧dy)` for at least
   four explicit divisorial valuations at infinity (the line at
   infinity; one and two blowups, free and satellite), verify the
   stated `-3`, `-2` values and the claimed existence of `v` at
   infinity with `v(dx∧dy)=0`; then verify `e=1+v(dx∧dy)` on
   `F=(x,xy)` and one more explicitly resolvable map.
4. The `d=4` enumeration (Thm 4.4): re-derive the three profiles from
   scratch under `1<=a<=2`, `sum delta_j e_j = 4-a`, some `e_j>=2`;
   search for any profile the report missed (including `delta_j=2`
   options and their group-theoretic admissibility).
5. The claimed group theory: transitive subgroup of `S_4` generated
   by conjugate transpositions is `S_4`; by conjugate 3-cycles is
   `A_4`; the local-group claims `H_p` in each class (§6 item 4).
6. Try to break Cor 3.2 (`a_p = s_p - b_p`) with the disk countermodel
   family from the round (`q: Delta -> Delta` style) adapted to check
   the report's claim that the boundary points over `D_0` are exactly
   the covering components it says.

Verdict per target: HOLDS / BROKEN (with the explicit countermodel) /
UNTESTABLE-AT-DESK. No line-by-line commentary; countermodels and
computations only.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/round1033-sheet-gate-verification-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
