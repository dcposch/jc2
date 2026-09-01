# Review lane: REP-96-HOSTILE-REVIEW — gate THEOREM CABLE-3 and the survives-verdict

The charged REP-96 report claims: both live (9,6) types SURVIVE
the S_4 representation gate at family 2, g=3 (its THEOREM
CABLE-3 / GATE-3), and survive EVERY other promoted gate (§6);
the surviving data is the explicit class list in §5; and §7's
fork analysis (BM-factorisation / source-is-C2 / M'-companion)
states what remains toward a Keller map. A false "survives" here
misdirects the campaign's heaviest resources; a false class list
poisons the downstream braid-monodromy computation; a missed
kill in §6 wastes everything downstream. Hostile standard.

Tasks:
(1) §2-§3 (CABLE-3): re-derive the family-2 block/cable structure
    at g=3 independently. The report's §2 winding argument and the
    ordered-product claim ("only the ordered product beta
    survives") are the load-bearing novelties — attack them.
    Check the exponent ledger e(delta_3^{k_*}) = 2k_* claims and
    the k_* values (-10, -8) in the §5 table against your own
    computation from the Puiseux data (§1). Verify §1's re-derived
    census for both types (beta_1=25/23, delta_inf=24/22, M_inf,
    delta_aff=4/6) from the Galindo conversion independently.
(2) §4's three routes and four controls: do the controls actually
    control? (the delta_aff=4 hypothetical row killed at E=-3 —
    check.)
(3) §5 class lists: verify by brute enumeration (sympy/python:
    tuples in S_4, the displayed relations, im=S_4, the parity
    fork Pi not in V_4) that the surviving classes are EXACTLY the
    listed 6 (144 tuples) for (9,6,2) and 3 (72) for (9,6,4) —
    no more, no fewer. This is a finite check; run it, print
    counts verbatim.
(4) §6 all-gates sweep: audit for any promoted gate NOT run
    (compare against the charged rowkill integration's theorem
    list). The N-A boundary claim for (9,6,4) — verify the
    boundary arithmetic.
(5) §7: check the (M') instantiation — the collapse to
    chi_2 + sigma_2 = 1 with s_1 cancelling identically; check
    the a_p cluster values (0/1/2) against the identity's
    definitions in the charged integration; check the Pi-tau pin
    (tau = Pi or disjoint — two of six transpositions).
(6) The two-symbols-b distinction (§7 R3): confirm no conflation.

Verdict: PROMOTE / PROMOTE-WITH-REPAIRS / BLOCKED, per claim:
CABLE-3, the survives-verdicts, the class lists, the §7 fork.
Report: `xmodel/rep-96-hostile-review-grok46-20260901.md`.
Seal-at-completion contract; target 20-30KB.
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
charged_input=xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  {{LANE_INPUTS}}/encoding-faithfulness-audit-r2-sol56-20260901.md
```
