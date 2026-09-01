# Research lane: DOMRINA-II-REPLAY-2 — hostile replay of §§5-7 of Domrina II

Sibling of the charged REPLAY-1 (which repaired both censuses —
Lemma 3.12 exhausts all 35 raw signatures, Lemma 3.14 the ten
Fig. 11 quotient graphs — but left two named first-half gaps:
GAP-CANDIDATE[ROOT-U-LAST-CHAIN] (Cor. 3.8(b), p.10) and
GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION] (Lemma 3.15, pp.14-15)).
A parallel Opus lane attempts repairs of those two; your scope is
the SECOND HALF, §§5-7 of the official PDF:
`refs/domrina2000_izv64_four_sheeted_general_case.pdf`, SHA-256
`0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018`
(verify before reading; stop on mismatch).

Tasks, campaign hostile standard, typed verdicts
REPLAYED-SOUND / REPAIRED / GAP per check:
(1) Every claim in §§5-6, including the forward uses of Lemma
    3.15 — IMPORTANT: where a §§5-7 argument consumes Lemma 3.15
    or Cor. 3.8(b), track the dependency explicitly (tag
    DEPENDS[ROOT-DELTA-G2-APPLICATION] / DEPENDS[ROOT-U-LAST-CHAIN])
    so the final soundness graph shows exactly what the two
    first-half gaps infect.
(2) The omitted §7 calculations (the charged audit §4 lists
    them): reconstruct each one or type it GAP with the quote and
    page.
(3) Lemma 7.10's undisplayed case check: enumerate the cases
    yourself.
(4) Final soundness graph: with REPLAY-1's results charged, give
    the complete dependency map of Domrina's Theorem on: the two
    first-half gaps, any new §§5-7 gaps, and the D--O I bindings.
    State the minimal set of repairs that would make the whole
    chain sound, and whether each looks desk-repairable,
    lane-repairable, or structural.

Report: `xmodel/domrina-ii-replay2-sol56-20260901.md`.
Seal-at-completion contract; target 30-40KB; close at a clean
sub-boundary with OPEN[REPLAY2-CONT] rather than overrun.
charged_input=xmodel/domrina-ii-replay1-sol56-20260901.md
charged_input=xmodel/domrina-1999-audit-sol56-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  {{LANE_INPUTS}}/domrina-ii-replay1-sol56-20260901.md
5739b317366d0a3c8905fcdc642f823c7bb71d44b79c7101b2cac256512f4d01  {{LANE_INPUTS}}/domrina-1999-audit-sol56-20260901.md
```
