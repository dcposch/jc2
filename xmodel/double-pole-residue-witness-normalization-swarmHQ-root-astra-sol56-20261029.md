# Double-pole normalization of a divisorial residue witness

2026-10-29. **PROVISIONAL / MANUAL / PASS_CONDITIONAL.**
Producer swarmHQ (ROOT/Astra co-research); independent hostile FIRST review by
requested Sol gpt-5.6-sol. Actual hosted model identity was not independently verified.

The [independent review](double-pole-witness-review-sol56-20261029T1112Z.md)
checks the two local transfer steps and their application to the
[conditional negative-divisorial witness](negative-thinness-divisorial-residue-obstruction-sol56-20261028.md).
The same rational map is retained. This narrows the necessary witness for a
hypothetical counterexample; it does not exclude that witness or resolve JC2.

The mathematical section below is a byte-identical excerpt of lines14–123 of the
sealed independent review: 6970bytes, SHA256
`3dd381aa054df04096e1e451816584a6b691e7c739c082b91f4675c55239b31e`. No mathematical claim or proof was changed during integration.
[Frozen producer evidence and checksums](../box/double-pole-residue-witness-swarmHQ-20261029/README.md)
retain the original pre-review labels and the full review chain.

## Exact reviewed mathematics

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

## Integration scope

The elementary surface and valuation foundations remain named rather than newly
source-proved. The Keller application retains all predecessor hypotheses. The
proof gives no positive skewness, special algebraic compactification, global
ruling, properness, polynomial no-fold theorem, or degree-one conclusion. Rational
volume-preserving maps with poles remain compatible with this reduction.
No new named OPEN entry or computational claim is introduced.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `9e6382326255f300b1f13419078ee03a01fabaad` (Git blobs only).

This empty lexical result is not a novelty certificate or a mathematical check.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8880`.
- Body SHA-256:
  `32b008d98162998133e7a5257d924c2f688891c0987a21d366fb3dd5952b2116`.
- Frozen basis: `9e6382326255f300b1f13419078ee03a01fabaad`.
