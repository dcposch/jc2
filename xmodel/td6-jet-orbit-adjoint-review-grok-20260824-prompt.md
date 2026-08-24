# Hostile different-model review — TD6 jet-orbit adjoint gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`, with frozen uncommitted
artifacts on top. Read in full:

- `xmodel/td6-jet-orbit-adjoint-gate-20260824.md`;
- every payload named in
  `cases/td6_jet_orbit_adjoint_20260824/FREEZE.sha256`;
- the frozen parent producer/review
  `xmodel/td6-boundary-q2-deformation-gate-20260824.md` and
  `xmodel/td6-boundary-q2-deformation-review-grok-20260824.md`;
- the imported q2 compiler and uniform-third-band replay named by the
  producer.

Frozen hashes:

- producer report:
  `28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`;
- exact dual replay:
  `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198`;
- canonical dual stdout:
  `cd87743d3859a5fa5d4275f7e599a43a9565d0a16a01de4c133bd925b7df0ebf`;
- orbit/source audit:
  `90bd44ebd6ed810e6d686d44bd84f2f852d623b22a371f137e215436394b967b`;
- canonical orbit stdout:
  `e158eba810deac8334ec408d1acad313a677fe37552a36006d152f6b45718eb5`;
- dual-syzygy certificate digest:
  `9527d18e4fbd48d0e6771cb9a45e1c4ffd6e33dfdc9c5cdc052fa6e37c883272`;
- imported q2 compiler:
  `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357`;
- imported uniform-third replay:
  `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8`;
- parent q2 point-probe report/review:
  `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0` /
  `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c`;
- freeze manifest:
  `9d94e4f011584f5a6718e7bdb94609788faf76d87ec6455a2c9dd6ee34715378`.

Verify the freeze from the repository root and rerun both registered exact
programs. Then independently attack every load-bearing claim:

1. **Source-orbit quotient.** Reconstruct the infinitesimal action of
   `t -> t+epsilon*t^2` on the chart and both boundary polynomials. Check that
   its full tangent is
   `(delta T,delta p,delta q)=(t^2,15t^16,t^2+25t^26)`, not q2 alone. Audit
   the seven source-orbit vectors and verify that adjoining q2 raises rank
   from seven to eight after the stated section. Decide whether q2 really is
   the sole transverse class at the smallest registered boundary-jet order.
2. **Other gauges and omitted moduli.** Independently verify rank four and
   zero Jacobian sensitivity for the two target translations, reciprocal
   scaling, and lower shear. Verify the `4/4` source tangent rank in
   `(S,D,L,A)`, including `F(7/4)=-53875/512`. Check that common centering and
   dead-stretch parameters are explicitly licensed but not silently called
   gauges or covered by this smallest quotient.
3. **Differentiated elimination.** Rebuild the dual-number staged solve by a
   second exact implementation or independently reconstructed row
   reductions. In particular, attack the common invalid shortcut that keeps
   the base left syzygy fixed. Verify the derivative of the normalized left
   syzygy, the identities
   `lambda(epsilon)^T A(epsilon)=0` and the full decomposition
   `c'(0)=lambda_0^T b'(0)+lambda'(0)^T b_0`.
4. **Ranks, residue, and derivative.** Verify the exact stages
   `3470 -> 132`, `38 -> 94`, `38 -> 56`, current homogeneous rank `25/56`,
   and absence of first-order rank-change flags. Recompute the base residue
   in the degree-18 field and prove
   `c'(0)=-4720/29 != 0`. Confirm the stated support sizes of the base and
   differentiated syzygies and independently check that the old secant
   `c(1)-c(0)=-14012/145` is not being substituted for the derivative.
5. **Gauge negative controls.** Check directly that the full t2
   reparametrization has zero t4 compatibility sensitivity and that every
   listed target gauge has zero sensitivity. Look for a missing chart,
   p-boundary, target, or F1-orbit direction that would make the claimed q2
   class gauge-trivial.
6. **Logical meaning.** Decide whether nonzero derivative at an already
   inconsistent base point proves only that the obstruction moves. Attack
   every possible inference to absence of a root, generic rank, emptiness of
   the full B-family, centering/dead-stretch families, SP-2, a terminal
   class, or JC2.
7. **Successor audit.** Assess the proposed staged fraction-free `E[B]`
   compatibility calculation. Require certified numerator/denominator
   degree bounds, symbolic or deterministically sufficient identity replay,
   and separate treatment of every pivot/resultant root. State any cheaper
   exact method, but do not license point sampling or interpolation without
   a proved bound.

Use exact arithmetic throughout; a producer replay plus prose comparison is
not independent evidence. Do not edit producer, case, canonical, ladder, or
erratum files and do not launch AWS. Write exactly one report:

`xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
