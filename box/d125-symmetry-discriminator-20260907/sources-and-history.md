# Bounded source/history receipt

Scope: unequal/rational complete small receiver with accepted polynomial lift;
no source-family coverage, generic normalization, solve, production expansion,
live peer artifact or protected-project access.

Terminal local inputs read wholly in this task/context:

- `xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md`
- `xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md`
- `xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md`
- `xmodel/d125-lift-hermite-pivots-astra-20260906.md`
- `xmodel/d125-lift-hermite-gate-fable5-20260906.md`
- `box/d125-minimal-receiver-client-preflight-20260906/client.py`
- `box/d125-lift-hermite-pivots-20260906/check.py`

After the parent's bounded composition extension, the following additional
terminal items were read wholly. They underlie the separate 22-coordinate
slice count, not the standalone 81-coordinate Hermite count:

- `xmodel/d125-minimal-receiver-b-reconstruction-astra-20260906.md`
- `xmodel/d125-b-reconstruction-gate-fable5-20260906.md`
- `xmodel/d125-b-witness-exact-export-repair-astra-20260906.md`
- `xmodel/d125-b-a-hermite-composition-astra-20260907.md`
- `xmodel/d125-b-a-hermite-composition-gate-fable5-20260907.md`

The repaired exact witness v2, SHA256
`07b4ce881b4f90f9a41a3f8cb01fcd3a120ff64a4f04969e60126dbdb6e7f246`,
was hash-matched and its unequal rank table compared to fresh exact ranks
of all twelve odd-degree restricted B matrices. The original degraded
exact-witnesses.json is NOT used. Composition gate SHA256:
`601cbe68958556ca736ade77b5b849d1326835f2328a2b951d2413609ebdbe59`.

Targeted history checksum searched the explicitly named canonical text files
README.md, APPROACHES.md, AUDIT.md, PROGRESS.md, notes.md, and
ladder/REDUCTION.md for odd Keller/polynomial-map, equivariance, symmetry-fixed,
and mu12 synonyms. Named terminal report discovery did not yield this exact
fixed-client calculation. AUDIT around 17351 concerns a different necessary
high-z mu2 system, not this complete polynomial-lift source. Moskowicz hits in
the history concern the prime-degree theorem rather than the involution
conjugacy lemma. These are scoped search observations, not priority claims.
Observed mutable history hashes at intake (not frozen dependencies):

- AUDIT.md: `7e285ff780f593856f14b9a3d2b098cce7c5b545551d11b650c8b3f5a5a3d328`
- APPROACHES.md: `599bb12b6656520adc0d6db155e1fc78fd00df001b947852ebc88c3c23df45b0`

## Primary snapshots and statement interfaces

1. Vered Moskowicz, *Involutions and the Jacobian conjecture*, arXiv
   1410.7705v1 (2014-10-28), https://arxiv.org/pdf/1410.7705v1.
   PDF SHA256 `753b4bdf17a76e65bb0730bd3baef752d519fc006168e7c01c2b70b2cd99fa4a`;
   extracted text SHA256 `5ea9ae4365ed6d6c42e4e39ab3949cf0dd1153844fd22209fc1a198c9daec61b`.
   Read the definition and entire Lemma 2.1 proof on p.1, Theorem 2.3 proof
   on p.2, and relevant statements/proof dependencies of §§3–4 including
   Theorems 4.7 and 4.9 (pp.8–10). Lemma 2.1 explicitly treats every order-two
   polynomial automorphism as conjugate to exchange. Central inversion gives
   an exact determinant-invariant counterexample to THAT lemma. Therefore its
   dependency cannot justify excluding centrally odd Keller maps. This is not
   a counterexample to the Jacobian conjecture or to the theorem's conclusion.
   No complete audit of every result in the paper is claimed.

2. T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv
   2607.20210v2 (2026-07-25), https://arxiv.org/pdf/2607.20210v2.
   PDF SHA256 `66cbff919a7d8372f1ee4d53b9f887a249c53c91c9c1b79a02d3a67e7d2b06ec`;
   text SHA256 `4f7fbcbf2ed383049dab36c57a05f2dff980abb56085b5d6d9e7890c1bc48d70`.
   Read definitions and Lemma 2.1, and whole Theorem 3.4 statement/proof
   (pp.8–10). The theorem requires a nontrivial algebraic G_m action on the
   source and compatible target action for every t, not a finite mu2 action.
   The missing extension to such an action is not supplied here. No claims
   elsewhere in this preprint, including higher-dimensional ones, are imported.

Additional targeted public queries for odd/equivariant plane Keller maps
returned the exchange-involution paper and cyclic pseudoreflection material;
no applicable central-inversion exclusion was established. No exhaustive
literature absence or mathematical openness theorem is claimed.

## Exact replay

`python3 check.py` and `python3 -O check.py` emit identical raw witness bytes.
`--mutate-parity` inserts the actual free slot A_(0,2) into the mu2 list and
must fail the same witness character verifier. `--mutate-lambda-weight`
changes the claimed lambda2 weight from -3 to -2 and must fail literal
multinomial-term covariance. Both fail normally and under -O. There are no
Assert nodes. Frozen source import only constructs its small face/support
metadata; no full Jacobian coefficient or source residual is expanded.

The runner exports stdout bytes directly to exclusive files. No numeric
JSON.parse/JSON.stringify transport is used. The witnesses contain only
small integer indices/counts and rational-string field values/determinants.

`composition_check.py` independently constructs only the fixed Q matrices
at odd B degrees1..23, verifies exact total rank92 on94 actual columns,
checks H and H^3 in those free slots, and proves scalar character identities.
Its whole-gauge fixture changes the lower kernel coefficient as required.
Mutations add degree10 to the retained kernel list or omit the lower-kernel
term in the gauge inverse; each fails the same checker normally and under
-O. No A-dependent forcing, residual substitution, CAS or full-source row
is constructed. Twelve total subprocess controls are recorded across the
two receipts; each is bounded by30wall/25CPU seconds and512MiB.
