# Review lane: DOMRINA-REPAIR-REVIEW — gate the two root-gap repairs and close the fork question

Two charged inputs: (A) the gap-repair flagship claiming both
Domrina II first-half root gaps REPAIRED (Theorem R1/R1' for
ROOT-U-LAST-CHAIN; Theorem R2/R2' for ROOT-DELTA-G2-APPLICATION;
plus NEW-LEMMA[DET-LINF-NONPOS] unconditional, and a
no-countermodel proof), with one named residual
OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK] (companion inessentiality
clause at the single fork vertex h-tilde); (B) the §§5-7 replay
whose dependency graph tags every downstream consumer of the two
root gaps (DEPENDS[ROOT-U-LAST-CHAIN] /
DEPENDS[ROOT-DELTA-G2-APPLICATION]).

The official Domrina II PDF is
`refs/domrina2000_izv64_four_sheeted_general_case.pdf`, SHA-256
`0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018`
(hash-verify before reading).

Tasks, hostile standard:
(1) Replay Theorem R1/R1' completely (the endpoint/last-linear-
    segment determinant argument). Hunt: division by unproven
    nonzeros, off-by-one in chain indices, hidden use of the very
    conclusion being proved, sign conventions of splice
    determinants.
(2) Replay Theorem R2/R2' (delta-unit + corrected g2-essential
    hypotheses; the negative-branch determinant conversion).
    Verify the non-fork restriction is honest: does R2' quietly
    use anything at the fork?
(3) Replay NEW-LEMMA[DET-LINF-NONPOS] (properness + Hodge index +
    Grauert contraction). This is claimed UNCONDITIONAL and
    stronger than the paper's tooling — if it holds it banks
    independently; check each of the three ingredient uses.
(4) THE FORK QUESTION (decisive for the whole chain): intersect
    (B)'s dependency graph with (A)'s residual. For EVERY §§5-7
    consumer of Lemma 3.15, determine from the official PDF
    whether it consumes the inessentiality clause AT THE FORK
    VERTEX h-tilde, or only at non-fork vertices / only the first
    conclusion (v-tilde not in delta(a-tilde g2-tilde)). Verdict:
    FORK-CONSUMED-NOWHERE (chain closes modulo trust boundaries)
    or FORK-CONSUMED-AT[exact lemma list] (hole survives; name
    it).
(5) No-countermodel proof: check it is a proof over the full
    stated state space, not an enumeration of convenient cases.
(6) Final ledger line to propose, choosing among:
    DOMRINA-II = SOUND-AFTER-REPAIRS modulo
    {D-O-I-mu2-trust-boundary, structure packages (F1)/(F2)/
    (S1)/(S2)/(S4), [fork if consumed]} — or a weaker line;
    state exactly which.

Verdict per item: CONFIRMED / REPAIRED-DIFFERENTLY (supply it) /
REFUTED. Report:
`xmodel/domrina-repair-review-gpt55-20260901.md`.
Seal-at-completion contract; target 20-30KB.
charged_input=xmodel/domrina-gap-repair-opus5-20260901.md
charged_input=xmodel/domrina-ii-replay2-sol56-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
99fc1e5870fb74d48e3d14a156115ef625fa9ecbc5843f0d8dd4a138a920e9bf  {{LANE_INPUTS}}/domrina-gap-repair-opus5-20260901.md
89d794a7b79d4e43092e2dac1215272fced8a1aa0d3436adffc4ab07b87d3a71  {{LANE_INPUTS}}/domrina-ii-replay2-sol56-20260901.md
```
