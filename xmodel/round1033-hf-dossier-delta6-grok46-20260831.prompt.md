# Research lane: HF-DOSSIER — the first attainment test at Delta_aff=6

You are a bounded primary research lane executing the round's merged
Heegaard-Floer attainment card (two independent derivations, Fable and
Sol; both frozen below). Do not edit canonical ledgers, any charged
file, or inspect `jc2-lean`.

charged_input=xmodel/ideation-20260831T1033Z-fable5.md
charged_input=xmodel/ideation-20260831T1033Z-sol56.md
charged_input=xmodel/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
charged_input=xmodel/ideation-20260831T1033Z-synthesis.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
9f70069c88730b2010cd22a72c276e32f71511715e8e0e7f30116242fad5e3f2  {{LANE_INPUTS}}/ideation-20260831T1033Z-fable5.md
7bf7502e43a6bdd344b1c177cf3c2e83afd9ca464b7aeab451b96e6db7528b46  {{LANE_INPUTS}}/ideation-20260831T1033Z-sol56.md
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  {{LANE_INPUTS}}/block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  {{LANE_INPUTS}}/ideation-20260831T1033Z-synthesis.md
```

Target: the smallest colourable `Delta_aff=6` survivor (conductor-12
rows `(6,4,9)` and `(9,6,4)` in the frozen census; start with one).
Protocol, fail closed:

1. Assemble ONE complete projective dossier for the candidate charged
   curve: projective degree `d` with
   `delta_infty=(d-1)(d-2)/2 - Delta_aff >= 0`, the infinity semigroup
   from the delta-sequence, EVERY affine singularity record typed as
   `UNIBRANCH_SEMIGROUP`, `TRANSVERSE_NODE`, or
   `UNLICENSED_MULTIBRANCH`, and the licensed theorem variant per
   record (Borodzik-Livingston 2014 for cuspidal; Borodzik-Hedden-
   Livingston 2017 for genus; Borodzik-Liu-Zemke 2024 for nodes;
   FLMN 2006 distribution where it applies). Literature-pin each at
   execution with exact statements — do not consume the submissions'
   citation lists as already typed. A missing field returns typed OPEN
   naming the exact absent dictionary; carry the charged-class
   interface (sole affine singularity, if that is what the census
   scope says) verbatim from the frozen inputs, not by assumption.
2. If a dossier completes: verify the genus identity, then evaluate the
   first nontrivial semigroup-counting/correction-term inequality by
   exact integer arithmetic. Controls: one named realizable rational
   cuspidal curve must pass; one hand-mutated semigroup must fail.
3. Verdict per `(d, S_infty)` pair actually enumerated: KILLED (named
   inequality), PASS_NECESSARY_ONLY (record as the first honest
   counterexample-side construction target), or OPEN (named missing
   lemma). CANDIDATE-kill only: row-level exhaustiveness claims are
   PROHIBITED without a proved degree cap. Stop after the first
   candidate regardless of outcome; write the replay-certificate
   arithmetic into the report so a verifier needs no code. Six hours
   hard budget.

Computation rules: desk-scale exact reasoning only; you may fetch and
hash primary literature (record exact sources). Never run Singular,
msolve, any CAS, or any computation of uncertain duration or memory on
this machine.

Write one report and no other file:

```text
xmodel/round1033-hf-dossier-delta6-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Include a `charge_basis` declaration only if you assert a genuinely new
exit price with a direct mathematical-source citation; otherwise omit
it entirely.
