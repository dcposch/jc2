# Independent hostile audit: selected-Q8 sparse contact component

Date: 2026-08-25  
Reviewer: Codex producer-independent audit  
Verdict: **CONFIRMED WITH EXPLICIT EXPOSITION REPAIRS**

## Scope reviewed

I reviewed the narrow characteristic-127 claim only: the corrected selected-Q8
localized source has at least one irreducible curve component whose
cycle-theoretic image in the `(w,v)` plane is the geometrically irreducible
candidate curve `H`.

The numerical input reviewed is exclusively the self-contained moving-contact
count

```text
80 distinct order-8 fibres + the distinct w=25 order-64 fibre
= 80*8+64
= 704 > 658.
```

No order-one baseline fibre is used.  I did not use the superseded
`123+63+68*7` count, any later bidegree bound, or any high-order Q8-contact
successor.

## Load-bearing checks

### 1. Local dimension, the `w` uniformizer, and generic finiteness

At each charged geometric source point, invertibility of the Jacobian of the
six divided rows with respect to

```text
(c,d2,d4,x1,x3,x5)
```

identifies the completed local source ring with `kbar[[w-w_i]]`.  Adding the
ratio and localizer coordinates merely solves uniquely for `v` and `inv` on
the licensed chart.  Thus the point is on one reduced regular one-dimensional
branch, `w-w_i` is a uniformizer, and `w` is nonconstant on its irreducible
component.  The map to the `(w,v)` plane therefore has one-dimensional image
and is generically finite.

There is a useful characteristic-127 consequence that the producer report
should state explicitly: `dw` is nonzero at the charged point.  Hence
`k(C)/k(w)` is separable for every relevant component `C`; consequently the
intermediate extension from the plane image to `C` is separable.  This rules
out a purely inseparable generic projection, for which counting distinct
sparse roots would not recover the pushforward multiplicity.

### 2. Proper definition of the projected cycle and the generic line

For a completely formal definition, take the graph of the regular chart map

```text
C -> A^2_(w,v)
```

for every relevant component, close it in any projective compactification,
and push that proper graph cycle to `P^2`.  This graph-closure construction
removes any rational-map or properness ambiguity at `x5=0` or infinity.

A relevant curve is not contained in the localization boundary because it
contains a charged point at which the localization factors are units.  Its
intersection with that boundary, with another source component, and with the
singular/ramification locus is therefore finite.  Its projective plane image
also has finitely many points at infinity.  Over `Fbar_127`, a line can be
chosen outside the finite union of the corresponding dual-line conditions
and outside the coefficient-vanishing conditions for the three pulled-back
monomials.  Because the relevant maps are separable, a further generic choice
makes all relevant pullback intersections reduced and transverse.

The resulting points lie in the licensed affine chart and are isolated roots
of the full seven-polynomial sparse system.  Unrelated positive-dimensional
components elsewhere, including clearing-denominator boundary components, do
not make these local roots non-isolated because the line avoids their
intersections with the relevant cycle.

### 3. The affine sparse bound in characteristic 127

Rojas' isolated-root construction applies over an algebraically closed field
of arbitrary characteristic.  After adjoining the origin to every support,
the degree bound is the mixed volume of those augmented supports.  Here it is
exactly `658`, with independent AWS support computations and unit controls.

The theorem need only bound the number of distinct isolated roots: by the
separability/transversality check above, a generic pullback line realizes
`deg(pi_*Z)` as exactly that number.  Thus no unproved multiplicity version of
the sparse theorem is needed.

Reduction modulo 127 cannot enlarge any support.  Equivalently, the reduced
system still has support contained in the frozen characteristic-zero support
sets.  Mixed-volume monotonicity after origin augmentation therefore gives

```text
deg(pi_*Z) <= 658.
```

This use remains valid when some unrelated component of the seven-equation
system is positive-dimensional: only the charged isolated roots enter the
count.

### 4. What an order-`N` moving algebra proves locally

At a charged fibre, monicity, degree 190, and `gcd(H,H_v)=1` imply that after
base change to `Fbar_127`,

```text
F_127[s,v]/(s^N,H(w_i+s,v))
```

splits into 190 length-`N` Henselian branches, one above each distinct root of
`H(w_i,v)`.  Exact vanishing of the six source rows, ratio, and localizer gives
a length-`N` source section above every such branch.  The unit source Jacobian
makes it the truncation of the unique formal source branch at that point.

If the projected source component is not `H`, the pullback of a local equation
of `H` to that branch has valuation at least `N`.  The projection formula for
the proper graph closure identifies the sum of these valuations with the
corresponding local contribution to

```text
I(H,pi_*Z).
```

This remains true when a source component maps to its image with degree
greater than one: that degree is precisely the coefficient appearing in the
pushforward cycle, and the valuations over all source points supply the same
multiplicity.  Distinct fixed `w_i` give distinct plane points, so their
contributions add.

### 5. Bezout and the component conclusion

The projective closure of `H` is an irreducible degree-190 plane curve.  If no
component of `pi_*Z` equals `H`, the two effective cycles share no component,
so projective Bezout gives

```text
I(H,pi_*Z) = 190*deg(pi_*Z) <= 190*658.
```

The 80 frozen order-8 fibres are pairwise distinct and exclude `w=25`; the
separate order-64 fibre is therefore disjoint from all of them.  The exact
moving contact is at least

```text
190*(80*8+64) = 190*704 > 190*658,
```

a contradiction.  Hence at least one relevant source component has plane
image `H`.

## Required repairs and hidden assumptions

The mathematics is sound, but two points should be made explicit whenever
the lemma is consumed:

1. Define `pi_*Z` using the proper closure of the graph of the localized
   `(w,v)` map.  This supplies the precise cycle and projection-formula setting
   at the chart boundary and infinity.
2. Record that the relative Jacobian makes `w` a local parameter, hence makes
   every relevant generic projection separable.  This licenses the equality
   between pushforward degree and the number of distinct transverse sparse
   roots in characteristic 127.

These are exposition repairs from already frozen hypotheses, not new
computational or geometric assumptions.  I found no missing saturation,
equidimensionality, reducedness, or field-extension hypothesis at the charged
points.  Embedded or higher-dimensional components away from them are
irrelevant after the generic-line avoidance just described.

## Scope firewall

This audit confirms only existence of an `H`-supported projected component
over `F_127`.  It does not establish source degree one, a global coordinate
graph, coverage of all 190 branches or all eight Q8 contacts,
characteristic-zero no-merger, Taylor realization, the terminal differential
row, a rational trajectory, a max-12 exclusion, or any Jacobian-conjecture
conclusion.
