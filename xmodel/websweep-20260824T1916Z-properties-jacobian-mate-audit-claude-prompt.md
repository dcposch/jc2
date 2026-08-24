# Primary-source audit — Makar-Limanov–Trakhtenberg, *Properties of a Jacobian mate*

You are an independent mathematical source auditor working in
`/Users/dc/code/math/jc2` on committed basis
`a04affb7247fb5e87cad4e87f5926ab440254b24`.  The campaign seeks a proof or
counterexample to the plane Jacobian conjecture.  Do not edit any existing
file, active prompt/log/run artifact, frozen case, or canonical state.

Read the complete primary preprint, not merely its abstract:

- L. Makar-Limanov and L. Trakhtenberg, *Properties of a Jacobian mate*,
  MPIM Preprint 2024 (33), submitted 2024-12-06:
  `https://archive.mpim-bonn.mpg.de/id/eprint/5148/1/mpim-preprint_2024-33.pdf`.
- It was published as São Paulo J. Math. Sci. 20, article 16 (2026), DOI
  `10.1007/s40863-025-00520-4`.  Determine from primary metadata whether the
  published version materially differs, but do not assume access if paywalled.

Then inspect the campaign's relevant foundations and avenue map, especially
`ladder/REDUCTION.md`, `APPROACHES.md`, `PROGRESS.md`, `AUDIT.md`,
`ladder/SHEET6.md`, the GGV source/transcription artifacts they cite, and the
current maximum-12 and finite-book reports.  Ignore unrelated active
working-tree artifacts.

Audit and report:

1. State every genuinely new theorem/restriction in the paper with exact
   hypotheses: Newton-resolution chain, integrality conditions, sub-expansion
   and polynomiality conditions, divisor/denominator descent, the claim that
   the leading total degree is a product of at least three primes, and the
   enumeration algorithm.
2. Re-derive the load-bearing identities independently.  Identify every use
   of an earlier source, especially `[ML2]`, Cassou-Noguès, GGV, or a claimed
   recoverability/normal-form theorem.  Mark theorem, conditional consequence,
   heuristic, and implemented enumeration separately.
3. Extract the complete enumerated output and its exact bound.  Check several
   rows arithmetically with an independent scratch program.  Search primary
   author/MPIM supplementary locations for the implementation mentioned in
   the paper; if absent, say so rather than inferring reproducibility.
4. Map the notation and restrictions precisely to the campaign's GGV
   rectangle/book notation.  Decide whether any current live family—especially
   `(72,108)`, the residue-A two-pole template, TD6, or maximum partial
   `y`-degree 12—is newly excluded or narrowed.  Total degree and partial
   `y`-degree must not be conflated.
5. Compare the algorithm with the existing finite-book compiler.  Propose the
   smallest typed software client that could cross-check or strengthen the
   campaign: exact inputs, outputs, invariants, positive controls, and a
   fail-closed gate.  Prefer a concrete one-day experiment over a broad rewrite.
6. Hostilely search for gaps, ambiguous notation, missing completeness
   arguments, and version drift.  In particular, test whether the `D is a
   product of at least three primes` language means primes counted with
   multiplicity and whether it applies to one shaped component or the full map.
7. Give an overall verdict (`ACTIONABLE`, `KNOWN/REDUNDANT`, `GAP`, or
   `MIXED`), exact promotion/quarantine language, and a ranked list of at most
   three campaign actions.  Do not claim a proof of JC2.

Use only primary technical sources.  You may write independent scratch files
under `/tmp`; do not launch AWS.  Write exactly one repository artifact:

`xmodel/websweep-20260824T1916Z-properties-jacobian-mate-audit-claude.md`

