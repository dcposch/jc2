# Independent final-artifact review: divisorial projectivity

Reviewer: configured Sol5.6 role; actual hosted identity and cost unmeasured.
Date: 2026-10-25 UTC
Artifact basis: `3e88add27a747c67f49fe1f8729147bc5c6b7f7c`
Verdict: **CONFIRM_CONDITIONAL_PACKAGE**
Lifecycle: REVIEW / UNPROMOTED; ROOT alone records promotion.

## Scope reviewed

I reviewed the complete canonical producer
[`divisorial-projectivity-swarmHQ-root-astra-20261025.md`](divisorial-projectivity-swarmHQ-root-astra-20261025.md)
at full SHA-256 `503833d453e0b790ee8e3b2783bd39dfdb01e3f0ae5225e9e2ea108ec060cbaf`
and predecessor basis `8b1fb2c39449ccaeb8f3399c22b6ddb96c7acf52`, together with the proposed
APPROACHES/PROGRESS delta. The producer's manifest verified before its body was read.
This review rechecked the prior projectivity proof and independent review at their exact
canonical pins and retained the three complete public premise-producer baselines at fresh pins.

## Hostile checks

The topology step is sound at the stated hypotheses. Rational singularities and Leray give
`H^1(Y,O_Y)=H^2(Y,O_Y)=0`; the compact-support sequence for
`U=Y-B` with `U` the marked whole affine plane identifies `H^2(Y,Z)` with
`H^2(B,Z)=Z`. The analytic exponential sequence therefore supplies the degree-one
line bundle `L`, whose pullback has the integral class `L_E`.

The boundary arithmetic is also sound. In each connected negative-definite block,
the inverse-M-matrix argument makes every coefficient of `L_E` positive. Hence `L_E`
is nef and big and has null locus exactly the contracted divisor `D`. Choosing
`H ~ aL_X-Z` with `Z` an integral fat cycle supported on all of `D`, Kodaira vanishing
on the already projective smooth surface `X` gives the required section surjection.
Trivializing `L` near each contraction point trivializes its pullback on the full
nonreduced cycle, so independent constants on the fat connected components lift.
Together with `s_Z H^0(X,H)`, these sections are basepoint-free, separate outside
`D`, and have fibers exactly the contraction fibers.

The resulting map has projective integral image and the induced map from normal compact
`Y` is finite and birational. Analytic normalization agrees with analytification of the
finite algebraic normalization, proving that `Y` is projective. Only after that step does
GAGA algebraize `L`; finite pullback then proves ampleness. Thus the proof does not assume
the desired projectivity or ampleness in its construction.

Pushing forward the boundary expression gives `L ~ nB`, with `n=L_E^2>0`.
Localization over the marked algebraic `A^2` makes `Cl(Y)=Z[B]`; units on `A^2`
exclude torsion, while the degree-one generator gives `Pic(Y)=Z[L]` and
`B^2=1/n`. For each actual finite iterate of degree `e=N^j`, GAGA algebraizes the
finite coherent algebra and the projective graph algebraizes `k_j`; finite pullback and
intersection theory give `ne C_j` Cartier ample and `C_j^2=1/(ne)`.

## Package and ledger verdict

The proposed ledger wording accurately records the conditional result and does not strengthen
it. In particular, `ne` is only a Cartier multiple, not the exact Cartier index; neither `n`
nor `e` is uniformly bounded. The package proves no residual-ramification vanishing,
target-map descent, finite self-germ, properness of the original polynomial map, equality
`W_j-C_j=U`, result for the infinitely singular branch, or JC2 conclusion.

The named Kodaira statement was previously checked only at statement level; its proof was not
audited here. Earlier attachment corrections, source-scope limits, and this reviewer's historical
nonblind/baseline-display qualifications remain binding. No new source, history preview,
classification, example, or mathematical branch was used.

## OPENS RAISED

None. Existing omitted-boundary, descent, uniform-index/degree, properness, and infinitely
singular gaps remain open at precisely their prior scopes.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `3e88add27a747c67f49fe1f8729147bc5c6b7f7c` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4111`.
- Body SHA-256:
  `4f2dc85d60dd509cd66107fad488ef0d382fe37caeead8940da3f60f5cfd2c67`.
- Frozen basis: `3e88add27a747c67f49fe1f8729147bc5c6b7f7c`.
