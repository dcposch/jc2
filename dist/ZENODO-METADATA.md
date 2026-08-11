# Zenodo upload metadata — jc72108-paper1-artifact-v1

Suggested fields for the Zenodo deposit of `jc72108-paper1-artifact-v1.tar.gz`.

- **Upload type:** Software
- **Title:** Artifact for: A Vertex-Gap Obstruction for Low-Degree Strip Pairs in the Plane Jacobian Conjecture
- **Authors:**
  - Clemens, Dan
  - Fable (AI system, Anthropic)
- **License:** MIT License
- **Version:** v1
- **Publication date:** 2026-08
- **Keywords:** Jacobian conjecture; Newton polygon; strip pairs; vertex-gap obstruction; computer-assisted proof; Lean; mathlib; exact rational arithmetic; resultant certificates

## Description (suggested)

Computational artifact for the paper "A Vertex-Gap Obstruction for Low-Degree
Strip Pairs in the Plane Jacobian Conjecture" (D. Clemens and Fable, 2026).
The bundle contains every certificate the paper's unconditional theorems rest
on: (1) a block-local surplus engine re-deriving the counting propositions and
the (2,2) pinning obstruction from corner data alone; (2) a column-ODE layer
carrying the support-rigidity proofs at types (2,3) and (2,4), the Sylvester
resultant certificates at (3,3), (4,3), (5,3) (exponents (15,12), (26,34),
(40,44)), and the machine checks for k <= 10 of the k >= 3, d2 = 2
impossibility theorem; (3) a full-pipeline replay of the (8,28) worked
example with per-equation provenance (92 keys, ten-event collapse to
(-1/5) a2^2 a6 a1^{-2}, census 51/40/1, final constant -1); (4) exact
verification of the log-residue functional R_{k,d2} over an 11-cell grid; and
(5) a Lean 4 + mathlib development machine-checking the two central
identities of the worked example (no sorry; axioms: propext,
Classical.choice, Quot.sound). All certificate scripts are pure Python 3
standard library (exact fractions.Fraction arithmetic; python-flint is an
optional cross-check backend), run in about one minute total, and were
self-containment tested from inside this bundle: each command in README.md
produces its documented PASS/verdict line with exit status 0. The Lean
project builds with `lake build` (toolchain leanprover/lean4:v4.32.2, mathlib
pinned; first build downloads mathlib, ~10 minutes). The paper (LaTeX source
and PDF), the derivation documents, and the adversarial review documents
cited in the paper's "Computational verification" section are included. The
msolve Groebner-basis discard of the remaining (72,108) strata (the paper's
conditional "companion claim") is a separate computation and is not part of
this artifact.

## Related / referenced works (from the paper's bibliography)

- arXiv:1401.1784 — Guccione, Guccione, Valqui, "On the shape of possible counterexamples to the Jacobian conjecture" (J. Algebra 471 (2017) 13-74)
- arXiv:1605.09430 — Guccione, Guccione, Valqui, "The two-dimensional Jacobian conjecture and the lower side of the Newton polygon"
- arXiv:1406.0886 — Guccione, Guccione, Valqui, "A system of polynomial equations related to the Jacobian conjecture"
- arXiv:1708.07936 — Guccione, Guccione, Horruitiner, Valqui, "Some algorithms related to the Jacobian conjecture"
- arXiv:2204.14178v1 — Guccione, Guccione, Horruitiner, Valqui, "Increasing the degree of a possible counterexample to the Jacobian conjecture from 100 to 108" (version pinned: v1)
- arXiv:2607.20210v2 — Shaska, "Graded Keller maps and the Jacobian conjecture"
- arXiv:2608.02634 — Mondello, "A separable counterexample to the two-dimensional Jacobian conjecture in characteristic two"
- msolve (ISSAC 2021) — referenced Groebner engine of the companion campaign (not bundled)
- Repository: github.com/dcposch/jc72108

## File

- `jc72108-paper1-artifact-v1.tar.gz` — 258277 bytes
- SHA-256: `2e6d8f596fe14a6a50e62fb5fe07cb330bdf74fb959ef79b1e2ad7c9845b2c8e`
