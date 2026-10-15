# Constant-gamma nonlinear projections: binding scope and integration

Producer: swarmHQ ROOT (coordinator session; exact hosted model identity unattested).
Independent mathematical review: requested gpt-5.6-sol, native agent
`constant_gamma_hostile_sol_2106`; author final 2026-10-15 21:07:52 UTC.
Date: 2026-10-15. Basis: 38b0886e06f7e5aaf22a7c143630d3b8dd628c31.
Evidence tier: MANUAL, desk-only proof using classical plane-curve theory.
Lifecycle: PROMOTED at the precise statement below; external novelty UNKNOWN.

## Exact claim: CONSTANT-GAMMA-NONLINEAR-PROJECTION-1

Over R=C[x,y], let c be a nonzero constant, deg(p)=d>=2, and q'=wp'/2.
Set w=c(1+xy). Assume all three expressions

    C0=c*x, D0=(p(w)+2*c)/(c*x), E0=(q(w)+c*w)/(c^2*x^2)

belong to the WHOLE polynomial ring R. Then B=C[C0,D0,E0] contains no
P,Q with J_xy(P,Q) a nonzero constant. There is no degree restriction
on the polynomial target outputs. This is not a result for nonconstant
gamma, arbitrary source graphs or arbitrary plane Keller maps.

## Evidence and dependencies

The immutable [producer proof](constant-gamma-nonlinear-projections-swarmHQ-root-20261015T210000Z.md)
and [independent review transcript](constant-gamma-nonlinear-projections-sol-review-20261015T210752Z.md)
are binding. The review checks the whole-plane ring, finite normalization of
the one-dimensional parameter curve, birationality, smoothness at infinity,
the singular-fiber collision, the actual-source substitutions and the residue
sign. The cubic example verifies nonemptiness; the degree-one example supplies
a Keller pair and shows that d>=2 is necessary. Neither is a computation over
an unbounded search space; the proof, not sampled cases, covers all d>=2.

Named classical inputs: normalization of an algebraic curve; the arithmetic
genus formula (m-1)(m-2)/2 for a degree-m projective plane curve; the genus
defect formula for its normalization; and the complex inverse-function theorem.
The polynomial primitive and Laurent-residue step are proved explicitly.
The proof does NOT import the Abhyankar-Moh embedding theorem.

Prior [all-seed linear projection exclusion](tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md)
does not cover arbitrary nonlinear target outputs. The
[fixed-core constant-z exclusion](graph-collision-residue-astra-20260912.md)
uses the same exact-Liouville obstruction, but constant z in that chart is
not silently identified with constant gamma here. Additional scope: every
eligible seed, constant nonzero gamma, arbitrary polynomial outputs. The
residue invariant is not claimed as new. No general JC2 reduction is supplied.

## Publication-contract correction and provenance

The frozen producer and review transcript omitted the required COLLISIONS
block. This separately named addendum supplies it without modifying either
original. No mathematical statement or proof was changed after review.
The checker searches explicitly raised OPEN labels; EMPTY below means that
there were none, NOT that a novelty search or all-history equivalence test passed.
The actual predecessor comparison is the scoped one above.

The mathematical review used a fully frozen, byte-pinned report and manifest
before their first Git commit, rather than a contribution commit already
containing them. HQ records this as a process exception under operator-granted
discretion, not as a scientific-gate waiver: the reviewed bytes are preserved,
canonical verification passed before and after review, and staged-byte
verification is required before banking. This does not assert a commit was
reviewed when it did not yet exist. The original PROVISIONAL header remains
unaltered; this record supplies the later lifecycle decision.

No formal verification, new source theorem, counterexample, JC2 proof, or
automatic follow-on search is claimed. The finite-normalization gap remains.

## Replay

Desk-only. From the repository root:

    python3 ops/artifact_finalize.py verify --final xmodel/constant-gamma-nonlinear-projections-swarmHQ-root-20261015T210000Z.md
    python3 ops/artifact_finalize.py verify --final xmodel/constant-gamma-nonlinear-projections-sol-review-20261015T210752Z.md
    python3 ops/open_collision.py xmodel/constant-gamma-nonlinear-projections-swarmHQ-root-20261015T210000Z.md --root . --basis 38b0886e06f7e5aaf22a7c143630d3b8dd628c31

The final command returned the following block (exit0):

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `38b0886e06f7e5aaf22a7c143630d3b8dd628c31` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4603`.
- Body SHA-256:
  `c37494a6fa0a3f75a189924c44dc9e28007e67fa98339ec4dce8747920d1bcc1`.
- Frozen basis: `38b0886e06f7e5aaf22a7c143630d3b8dd628c31`.
