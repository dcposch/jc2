# WITREVIEW1105 hostile mathematical review

Final status: **PASS_CONDITIONAL / COMPLETE**.  This is the sole independent
FIRST review requested from the existing Sol adapter/model gpt-5.6-sol; actual hosted
identity is unverified.  I did not author the Astra/ROOT candidate.

First action (manifest read and control-hash check): 2026-10-29T11:12:23Z.  All nine
standing governors were read whole by 2026-10-29T11:13:33Z, and HQ-STATE.md was read
whole by 2026-10-29T11:13:42Z, before any mathematical body.  Concrete provisional
partial written 2026-10-29T11:16:24Z, before the 11:25Z deadline.

## Verdict and exact hypotheses

**Elementary reduction: PASS_CONDITIONAL.**  Let
`H` be the same dominant generically finite rational map with
`H^*(dX wedge dY)=dx wedge dy`.  Suppose primitive divisorial infinity valuations
`ord_E,ord_D` satisfy

`ord_E|C(X,Y)=e ord_D`, `a_E<0`, and
`[kappa(E):kappa(D)]>1`,

where `a=1+ord(Omega)` is raw discrepancy and `e` is the normal index.  Then the
same `H` has primitive source/target infinity divisors with raw discrepancies
`a_source=a_target=-1`, normal index one, and residue degree greater than one.

The conditional label retains only the named standard characteristic-zero surface
foundations: divisors over the line at infinity are extracted by finite point
blowups and have rational residue curves; a rational surface map resolves by source
point blowups while preserving a strict divisor and its residue place; the boundary
and volume divisor have the stated SNC local form; monomial divisors are extracted
by point blowups; and raw discrepancies obey canonical transport for a separable
generically finite map.  These standard foundations were named, not freshly
source-audited.  No positivity, special algebraic compactification, or global
polynomial theorem is added.

**Conditional Keller application: PASS_CONDITIONAL.**  The published predecessor
supplies exactly the same normalized hypothetical Keller map with `N>1` and a
primitive negative divisorial residue fold, conditional on its stated
valuation-tree, inverse-end, principalization and canonical foundations.  Its
normalized negative thinness has the same sign as primitive raw `a_E`, because the
normalizing denominator is positive.  Applying the elementary reduction therefore
gives the claimed double-pole witness.  The predecessor foundations remain
unaudited here; co-research agreement was not used as proof.

## Hostile checks and proof

1. A target divisor over the line at infinity is obtained from a finite point-blowup
   chain.  Starting with either standard chart at infinity, every blowup chart
   replaces a generating parameter pair by `(U,V/U)` or `(U/V,V)`; translation of
   the exceptional coordinate handles any finite marked point, while the reciprocal
   chart handles its point at infinity.  Thus at the required marked point one can
   arrange `D=(U=0)`, `(U,V)` regular, and the *full* target field equal to
   `C(U,V)`.  Resolving the source rational map by source point blowups preserves the
   strict transform of `E`, its residue curve and the selected ramification place.
   The boundary and the volume divisor are SNC locally, giving
   `u^(a_E-1) z^(b-1) unit du wedge dz`, including at a boundary node.

2. In Stage 1 put `q=(n+c)/r`.  For weights `(n,1)`, all terms in `u^2 B`
   have weight at least `2n>n+c`, and all terms in `uD` have weight at least
   `n>r`; the nonconstant terms of `A,C` are also higher.  For a nonzero target
   polynomial, terms of least target weight `r(qi+j)` become, after division by
   that power of `z`, a nonzero polynomial in `s=res(u/z^n)`: at fixed `qi+j`
   distinct target monomials have distinct powers of `s`.  Hence no cancellation
   introduces another value.  The full restricted value group is exactly `rZ`,
   since it is contained in `rZ` and contains the value `r` of `V`.  Moreover
   `res(U/V^q)` is a nonzero constant times `s`; the source residue field is
   `C(s)`, so the residue degree is exactly one.  The raw discrepancy is
   `n a_E+b<0`, and canonical transport gives `a_nu=r a_w`.

3. In Stage 2 choose a general point avoiding nodes, zeros of the normal leading
   coefficient and residue critical points.  Since the residue derivative is
   nonzero, `w=H^*V` is exactly a source local parameter and
   `H^*U=u^e B(u,w)`, `B(0,0)!=0`.  With `m=ek-1`, weights `(1,m)` give
   `a_source=a_E+m=-1`.  The target weights are `(e,m)` and have gcd one, so the
   full normal index is one.  If `t=res(w/u^m)`, then the target residue generator
   `U^m/V^e` maps to `B(0,0)^m t^(-e)`.  A regular two-dimensional local ring has
   the global surface function field as its fraction field, and its weighted
   associated graded ring shows that the full source residue field is `C(t)`,
   not a hidden algebraic extension.  Thus the residue degree is exactly `e>1`.
   Directly, `a_target=e a_D+m=-1` as well.

4. If the initial normal index is one, characteristic-zero ramification of the
   degree-greater-than-one residue map supplies Stage 1 and its new normal index
   `r>1`; Stage 2 then applies.  If the initial index is already greater than one,
   Stage 2 applies directly.  Both extractions are over boundary points, all
   weight pairs are primitive, and the rational map `H`, its target/source fields,
   and the volume identity are never changed.

## Stage and attack status

- **Attack 1 / target coordinates: PASS.**  The explicit blowup-chart induction
  supplies a full rational-coordinate pair, including boundary nodes and either
  chart of the exceptional `P1`.  Source-only resolution preserves the strict
  divisor and ramification place.  The SNC volume expression permits arbitrary
  integer `b`; it does not assume a free source point in Stage 1.
- **Attack 2 / Stage 1: PASS.**  Every transverse term is above the selected
  weight threshold.  The associated-graded calculation covers every polynomial
  and hence every rational function in the full field `C(U,V)`, proving value
  group `rZ` and residue degree one, not merely values of two generators.
- **Attack 3 / Stage 2: PASS.**  `w=H^*V` is a genuine source parameter by the
  nonzero residue derivative.  The fraction field of the local ring is the full
  source function field, and its weighted graded ring proves residue field
  `C(t)`.  The final degree is exactly `e`, with no hidden factor and no
  multiplication by the old residue degree.
- **Attack 4 / composition: PASS for the elementary reduction; PASS_CONDITIONAL
  for the Keller client.**  Stage 1 followed by Stage 2 uses only point blowups and
  valuations of the original two function fields.  There is no source cover,
  target-map replacement, coordinate change of the global polynomial map, or
  positivity/ruling assumption.  The same volume-preserving `H` is retained.

The stage statuses are therefore: Stage 1 **PASS** when the initial normal index is
one; Stage 2 **PASS** for every negative input of normal index greater than one;
their composition **PASS_CONDITIONAL** at the named standard-foundation tier.

## What remains open

This is a normal-form reduction, not an exclusion.  For an actual hypothetical
polynomial Keller map one must still rule out every raw-`a=-1`, normal-index-one
divisorial infinity pair having residue degree greater than one (or prove another
global no-fold theorem).  Neither stage supplies that polynomial/global input.
Rational volume-preserving pole-bearing donors remain compatible.  There is no
properness, `N=1`, or JC2 conclusion, and no exit-price assertion; a
`charge_basis` object is inapplicable.

## Custody, hashes and coverage

The control manifest was read first.  Its pre/post SHA-256 is
`2023d80a3d4dc0820fa4233f4afe8e21167e1b10f240e440b216487565170882`
(6,487 bytes, 180 LF, mode 0400), matching the supplied pin.  Before any declared
input body, all fourteen declared files passed one metadata-only gate: every leaf
was a regular nonsymlink, the shared physical ancestor chain contained no symlink,
and SHA-256, bytes, LF and launcher-snapshot mode 0400 matched the manifest.  The
manifest's original-packet mode 0444 entries were provenance only and were not used
as permission to inspect the originals.  Terminal postpins after all body reads
were unchanged:

| Declared input | bytes/LF | pre SHA-256 | post SHA-256 |
| --- | ---: | --- | --- |
| HQ-AGENTS.md | 1520/23 | `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f` | `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f` |
| HQ-POLICY.md | 6755/112 | `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634` | `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634` |
| HQ-RESEARCH_POLICY.md | 9551/162 | `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62` | `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62` |
| HQ-RESTRICTIONS.md | 18817/259 | `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed` | `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed` |
| HQ-RUNBOOK.md | 34745/507 | `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06` | `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06` |
| HQ-STATE.md | 45934/200 | `464bf2d108c3bc118e685cf23a88850c6c9cad1cf7170ac06530c45ab7ef079a` | `464bf2d108c3bc118e685cf23a88850c6c9cad1cf7170ac06530c45ab7ef079a` |
| PUBLIC-AGENTS.md | 1229/22 | `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f` | `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f` |
| PUBLIC-README.md | 5391/102 | `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf` | `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf` |
| PUBLIC-COORDINATION.md | 6042/107 | `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e` | `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e` |
| PUBLIC-FALLACY-v2.md | 1985/36 | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |
| integration-receipt.json | 3252/61 | `b03fc1599c903e21c6bb55660f55fbd4b058bd2b2c42ef38d4200286a79df13e` | `b03fc1599c903e21c6bb55660f55fbd4b058bd2b2c42ef38d4200286a79df13e` |
| candidate-root.md | 4031/15 | `1a344981e481e4db1aa4ab87cbf72cd4e2757f3b4ba7c436a3ff0aacbb7c9225` | `1a344981e481e4db1aa4ab87cbf72cd4e2757f3b4ba7c436a3ff0aacbb7c9225` |
| candidate-astra.md | 5720/14 | `7b36fc5fc07087afa183456cbee1cf59ac05b4ed4cf6939d270e984b7cb894fa` | `7b36fc5fc07087afa183456cbee1cf59ac05b4ed4cf6939d270e984b7cb894fa` |
| predecessor-negative-witness.md | 11618/220 | `0f09eb10318e4e7f966b7a0360fe0bb0b3e974ee39f9164b7d636bd3925d4510` | `0f09eb10318e4e7f966b7a0360fe0bb0b3e974ee39f9164b7d636bd3925d4510` |

Whole-body ranges were: `input-manifest.json` 1-180; HQ-AGENTS 1-23,
HQ-POLICY 1-112, HQ-RESEARCH_POLICY 1-162, HQ-RESTRICTIONS 1-259,
HQ-RUNBOOK 1-507, PUBLIC-AGENTS 1-22, PUBLIC-README 1-102,
PUBLIC-COORDINATION 1-107, and PUBLIC-FALLACY-v2 1-36 (nine governors,
1,330 LF); HQ-STATE 1-200 (200 LF separately); then, receipt first,
integration-receipt 1-61, candidate-root 1-15, candidate-astra 1-14, and
predecessor-negative-witness 1-220 (science 310 unique LF).

Before the predecessor body, its outside-seal lines 213-220 were displayed and its
seal was checked: exactly one standalone body marker at body line 211, body length
11,285 bytes, and body SHA-256
`6723d10cd6a6fd521d9e6951820f0a7ba2313f4d5501b6dc6211fca60524050d`.
Those eight seal lines were then repeated in the whole-file read.  Thus unique
non-STATE coverage was 1,820 LF (180 manifest + 1,330 governors + 310 science),
displayed non-STATE coverage was 1,828 LF including the eight repeats, and STATE
coverage was 200 LF separately.  Every body window was contiguous and at most 24 LF
and 8,192 serialized bytes; no window was clipped or cropped and no omitted clipping
was treated as read.

Primary-source body LF: 0.  New source queries: 0.  New history queries: 0.  No
archive body, whole APPROACHES, unlisted source, download, CAS, control family,
agent/job, protected tree, authentication/configuration, operational tick, or
automatic-memory output was used.  The failed-wrapper interval 0.746667724s is
retained as charged per the launch correction; it made no model request and changed
no scientific pin.  The only authored path is this report.

## Timing

- first action: 2026-10-29T11:12:23Z
- whole standing governors complete: 2026-10-29T11:13:33Z
- whole HQ-STATE complete: 2026-10-29T11:13:42Z
- concrete unsealed partial: 2026-10-29T11:16:24Z
- terminal body completion: 2026-10-29T11:18:20Z

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12661`.
- Body SHA-256:
  `941ea5668df20f28176de2cb741a28f668f468a8c5dd146ea4770879abd0b7c3`.
- Frozen basis: `9e6382326255f300b1f13419078ee03a01fabaad`.
