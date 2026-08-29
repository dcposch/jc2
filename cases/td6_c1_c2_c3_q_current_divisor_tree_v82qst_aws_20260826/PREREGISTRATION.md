# V82QST q2..q10 CURRENT divisor-tree plan

## Frozen inputs

V82QSD found the exact reduced-coordinate common denominator

```text
(1/256) F G L U^a V^b
```

for every q2..q10 single-axis CURRENT presentation.  V82QSF then proved

```text
G = V^4+4F^2,
L = 4U^3G^2 + V^4(V^2+4U^3)(V^2+2F)^2.
```

This preregistration turns that nested divisor into a finite sequence of
presentation tests and, only where unavoidable, original-source raw-fibre
clients.  No client may reuse a generic pivot that vanishes on its target
stratum.

## Gate 0 — expose exact coordinate debt

Before any raw substitution, make a reporter-only successor to V82QSD.  Move
the already-computed CURRENT entry serialization ahead of the unchanged
fail-closed assertion.  For each exact reduced coordinate emit:

- source compatibility key and affine coordinate;
- numerator and denominator, their factorizations, and SHA-256;
- valuations along `F,G,L,U,V`;
- after multiplying by the exact pole power, the nonzero residue modulo the
  target factor.

The existing diagnostic files contain only coordinate count/rank/common
denominator, so they cannot decide numerator/presentation cancellation.  Since
each scalar is already a reduced `Rat3`, a denominator factor occurring in its
own reduced denominator cannot cancel within that scalar; Gate 0 instead
identifies which rows/pivots carry each pole and whether a change of conormal
basis could remove it.

Gate 0 remains single-axis diagnostic evidence.  It must not emit an accepted
CURRENT table while the localization assertion is false.

## Gate 1 — alternate-minor/principal-open cover

Recompute the same original CURRENT rows with at least two source-independent
pivot policies: reverse/deferred unit pivots and sparse/minimum-denominator
pivots.  Record the actual denominator ideals and every row-source combination.

Promotion requires more than multivariate gcd.  If denominators `d_i` differ,
prove an explicit localized cover

```text
sum_i a_i d_i = (licensed base product)^N
```

or its finite principal-open analogue, with exact source certificates.  A bare
gcd or selected-minor factor list is not a cover.  If an alternate presentation
removes `F`, `G`, or `L`, retain the superseded presentation as a negative
control and use exact Cech/Bezout glue.

## Gate 2 — raw original-source clients

Only factors surviving Gate 1 receive raw rebuilds.

1. **`F=0` on `D(UV)`.**  Work over `Q(U,V)` with
   `C=(V^2-U^3)/U`; rebuild transport, FIRST, PREVIOUS/POLE, and CURRENT from
   original source rows.  No inherited pivot containing `F` is allowed.
   Separate `U=0` and `V=0` intersections remain explicit.
2. **`G=0` on `D(UVF)`.**  Use the exact quadratic extension
   `w^2+1=0`, `F=(w/2)V^2`,
   `C=(V^2-U^3+F)/U`, with conjugation/descent checks.  The nested identity
   proves that the only noncollapsed `G=L=0` branch here is
   `V^2+4U^3=0`; rebuild that intersection separately.  The
   `V^2+2F` branch must carry the exact collapse certificate to `V=F=0`.
3. **Generic `L=0` on `D(UVFG)`.**  First try the alternate-minor cover.
   If it fails, use the normalized hypersurface
   `4g^2+x^2(x+4)(x+2s)^2=0`, never a point sample.  A quadratic normalization
   `y^2=-(x+4)` may split it into two source clients, but any resulting claim
   requires exact finite-extension descent and intersection coverage.

Every raw client must include original-row ancestry, direct-q-prime omission,
wrong-row/plus-one controls, exact denominator ledger, and dual independent AWS
replay.

## Stop conditions and scope

- Stop a branch immediately on a source-typed unit incompatibility, retaining
  an original-row certificate.
- Stop pivot proliferation once an explicit principal-open cover is proved.
- Fail closed on lower rank, a new factor, a non-field specialization, or host
  disagreement; recurse the emitted factor rather than absorb it.
- q15 remains only the combined lower-target-shear marker.

All results are restricted to the fixed source-typed A3 square-zero CURRENT
question.  The base CURRENT system is already inconsistent.  No q family,
neighborhood, TD6, SP-2, landing, or JC2 conclusion follows from affine tangent
data or from a generic fraction-field computation.
