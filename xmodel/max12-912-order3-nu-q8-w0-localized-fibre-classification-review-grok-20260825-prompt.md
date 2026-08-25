Act as an independent hostile algebraic-geometry and computer-algebra referee.
The producer is GPT-family; you are the required different-model reviewer.
Read in full:

- `xmodel/max12-912-order3-nu-q8-w0-localized-fibre-classification-20260825.md`;
- `cases/max12_912_order3_nu_q8_w0_fibre_stratification_aws_20260825/PREREGISTRATION.md`;
- that case's `generate.py`, `run_remote.sh`, `aggregate.py`, `aggregate.json`,
  `MANIFEST.sha256`, and `FREEZE.sha256`;
- every exact Singular input/output and `run.meta` named by the manifest;
- the hash-pinned parent compiler and the reviewed scheme-identity discussion
  named by the producer.

Audit from source rather than trusting PASS strings.  Check the six divided
rows, graph/localizer, variable and monomial orders, open-stratum inverse
equations, exhaustive set-theoretic cover, all original-generator reductions,
the two characteristic-zero engine/order computations, both modular controls,
and the aggregate's 34-run inventory.  In particular, attack the inference

`dim_Q A=8` and `ker(Q[v] -> A)=(Q8)` of degree eight
`=> A ~= Q[v]/(Q8)`,

including the direction of the induced map, surjectivity/generation, and any
possibility that the eliminant and vector-space dimensions alone fail to give
the claimed scheme isomorphism.  Independently check irreducibility and
squarefreeness evidence over Q, the claims that `r6` and the full relative
8-by-8 determinant are units, and the absence of unloaded and loaded non-Q8
points.  Verify that the theorem is only the finite affine chart
`w=0, x5*(x3-2*x5)!=0`, and that boundary/projective escape, `p=0`, terminal
`r8`, Taylor provenance, arbitrary selected components, all `(9,12)`, max12,
and JC2 remain explicitly charged.

List every mathematical, source-fidelity, custody, or scope defect, even if
repairable.  Do not use Bash, CAS, network access, or write/edit any file;
disclose that limitation.  Return a self-contained review on stdout, at most
3,000 words.  End with exactly one verdict token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `BLOCKED`.
