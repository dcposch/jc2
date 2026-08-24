# Primary-source audit — Makar-Limanov shape and mate-recovery papers

Work independently in `/Users/dc/code/math/jc2` at committed basis
`a04affb7247fb5e87cad4e87f5926ab440254b24`.  The goal is progress toward the
plane Jacobian conjecture.  Do not edit existing files, frozen cases, canonical
state, or active prompt/log/run artifacts.

Read both primary papers in full:

1. L. Makar-Limanov, *On the shape of a counterexample to the
   two-dimensional Jacobian conjecture*, Serdica Math. J. 51 (2025), 299–314,
   DOI `10.55630/serdica.2025.51.299-314`, official PDF:
   `https://serdica.math.bas.bg/index.php/serdica/article/download/300/153/862`.
2. L. Makar-Limanov, *A Jacobian mate defines the Jacobian pair*, MPIM
   Preprint 2022 (48), official PDF:
   `https://archive.mpim-bonn.mpg.de/4771/1/mpim-preprint_2022-48.pdf`, now
   published in Israel J. Math. (2025), DOI `10.1007/s11856-025-2863-6`.

Inspect the campaign's relevant files: `ladder/REDUCTION.md`, `APPROACHES.md`,
`PROGRESS.md`, `AUDIT.md`, the GGV/transcription artifacts those cite, current
maximum-12 Faber/Kummer reports, and the finite-book/tower software.  Use only
primary technical sources.

Tasks:

1. State every theorem from both papers with exact quantifiers and
   hypotheses.  Re-derive each load-bearing identity; separate published
   theorem, source-dependent implication, heuristic, and normal-form choice.
2. For the shape paper, map its Newton-polygon notation exactly to GGV's
   standard/minimal-pair notation.  Decide what is strictly stronger than the
   campaign's current GGV foundation and whether it narrows `(72,108)`, the
   residue-A two-pole template, TD6, or any maximum-partial-degree branch.
3. For the recovery paper, reconstruct the algorithm that determines
   `C[f,g]` and recovers `g` modulo `C[f]`.  Identify all choices, termination
   arguments, field assumptions, and reliance on formal/Puiseux expansions.
   Determine whether it is constructive enough to compile exactly.
4. Test the recovery method on at least two explicit controls: a nontrivial
   polynomial automorphism pair and one of the campaign's formal/truncated
   candidate pairs.  Do not confuse finite-precision data with a polynomial
   mate.
5. Propose the smallest fail-closed software client that could replace or
   reduce pair-variable systems in one active campaign branch.  Specify exact
   input/output, certificate, negative and positive controls, and estimated
   complexity.  If no active client is sound, say so.
6. Hostilely search for gaps, overreads, version drift, and missing
   effectiveness.  In particular, a uniqueness statement modulo `C[f]` must
   not be reported as existence of a mate or as JC2.
7. Give an overall verdict (`ACTIONABLE`, `KNOWN/REDUNDANT`, `GAP`, or
   `MIXED`), precise promotion/quarantine wording, and at most three ranked
   next actions.

You may use scratch files under `/tmp`; do not launch AWS.  Write exactly one
repository artifact:

`xmodel/websweep-20260824T1916Z-makar-shape-recovery-audit-codex.md`

