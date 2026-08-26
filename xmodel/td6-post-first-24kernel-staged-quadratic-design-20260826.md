# TD6 post-FIRST 24-kernel staged and quadratic design

Date: 2026-08-26

Status: **PREREGISTERED DESIGN; LINEAR AWS PRODUCERS LIVE; NO QUADRATIC
VERDICT YET.**

## Reviewed input

The generic FIRST presentation is now a reviewed surjection
`K^132 -> K^38`, `K=E(C,V,U)`.  Together with reviewed V81C transport, its
cumulative transport-plus-FIRST kernel is exactly

```text
Q = span(q2..q14, q16..q24, d10, d15),   dim_K Q = 24.
```

Promotion/review SHAs are

```text
7786868ef36b57fc9a8ae6f166373f61403ac11251bf9c0377aca12e5f64620d
  xmodel/td6-first-generic-surjectivity-promotion-20260826.md
b24ab0d33b2c0fd82b6ba49a8b845e3e73af822e926f4f07f507dfcc684c3c83
  xmodel/td6_first_generic_surjectivity_corollary_hostile_review_20260826.md.
```

No further generic FIRST-axis computation is scheduled.

## Stage A — complete previous/pole linear map

The linear map to compute is the direct sum of every dependent coordinate in
the packed `X-1` and pole-previous rows after exact transport and FIRST source
lifts:

```text
L_prev : Q -> C_prev.
```

V82Q computes the 22 q columns simultaneously.  Dual hosts already agree that
their FIRST and previous/pole tables are header-only, with unit denominator;
the current stage remains live.  V82P3 independently computes the `d10,d15`
columns with full `AxisJet` typing and source replay.  Promotion requires both
V82P3 hosts to close rc0, exact table equality, unit/allowed denominator, and
the two-axis union to agree with the q table's row/coordinate convention.

If all 24 columns vanish, linearity proves `ker(L_prev)=Q`; a one-ring 24-axis
execution is useful corroboration but not logically required.  If either dead
column is nonzero, compute the exact joint rank/kernel before any axis or
subspace claim.  Any rank-drop denominator factor becomes a raw-fibre debt.

## Stage B — current adjoint symbol, not a tangent kernel

The base current system is already inconsistent and carries the reviewed unit
obstruction on the fixed A3 section.  Consequently its differentiated
dependent rows define an adjoint-sensitivity map

```text
S_cur : ker(L_prev) -> C_cur,
```

not the tangent map of a solution scheme.  V82Q supplies the q columns; V82P4
supplies `d10,d15`, including varying-echelon terms and original-row replay.
The combined exact rank/kernel is scheduling data for reconstructing a
parameter-dependent obstruction identity.  Neither a nonzero column nor a
kernel vector is a family kill or survivor.

A source-lifted polynomial identity with nonzero constant term would exclude
a principal formal/Zariski neighborhood on the chart where its denominators
are units.  A finite Taylor table alone does not supply that identity and can
acquire zeros away from the base.  Global transverse exclusion therefore
requires either a denominator-free identity or a complete constructible
cover, not extrapolation from `S_cur`.

## Stage C — first genuine quadratic object

Assuming Stage A leaves a linear kernel `Q_prev`, compute the complete
quadratic coefficient of every previous/pole dependent source row on
`Q_prev`:

```text
K2_prev : Sym^2(Q_prev) -> C_prev.
```

This is the first genuine Kuranishi-type gate because the previous/pole base
is consistent and its linear compatibility vanishes on `Q_prev`.  Current-row
quadratic coefficients are recorded separately as obstruction-identity
reconstruction data, not as a solution Kuranishi map at an empty base.

### Source ring and normalization

Use the full licensed source expressions, truncated only after multiplication:

```text
q(t) = t + t^25 + sum_{e in Q22} a_e t^e,
y(r) = r^5 + d10 r^10 + d15 r^15 + zeta r^17.
```

The quadratic jet ring must retain all linear axes and all symmetric products
through degree two.  For diagonal slots the stored `eps_i^2` coefficient is
the Taylor coefficient, i.e. half the classical second derivative.  Mixed
slots store the `eps_i eps_j` coefficient.  No quadratic dead-stretch term may
be inferred from the old linear formula `j*binom(j-1,k)`: the producer must
expand the full `y(r)^j`, so dead/dead and q/dead products enter with the
correct binomial coefficients.

### Exact staged replay

1. Rebuild the original 3,470-row transport matrix and RHS over the quadratic
   jet ring; replay every pivot identity, including matrix variation.
2. Solve all 38 FIRST rows through degree two.  Generic surjectivity removes
   compatibility but does not permit dropping the quadratic lift.
3. Compose the lifted global forms into the previous X-band and pole rows,
   replay every pivot and dependent combination, and extract all quadratic
   dependent coefficients.
4. Emit a canonical symmetric table, its exact rank and kernel over `K`, the
   denominator and factor ledger, and raw source identities for every nonzero
   output coordinate.

### Parallelization

Use one aggregate 24-axis quadratic run as authority and a proof-carrying
block cover as an independent implementation.  A practical block cover splits
the ordered axes into six four-axis blocks and runs the 21 unordered block
pairs independently; each block-pair retains its diagonal slots.  Exact union
requires every one of the 300 symmetric axis pairs exactly once.  Blocks may
run concurrently on r6d/Box03 under explicit memory caps; the aggregate may
use the host with the largest live headroom.

### Mandatory controls

- specialize all quadratic terms to zero and reproduce the frozen linear
  q/dead tables;
- omit each source axis and reproduce a zero column only where source typing
  predicts it;
- swap `(i,j)` and `(j,i)` and require equality;
- split one axis as `eps+eta` and require the mixed coefficient to be twice
  the diagonal Taylor coefficient;
- include a synthetic nonzero quadratic multiplication/inverse control that
  fails if cross terms or the second-order inverse term are omitted;
- assert q15 remains absent, symbolic centers remain symbolic, and the dead
  exponents are exactly 10 and 15;
- replay original rows before interpreting any pivot/Fitting output;
- canonicalize exact expressions independently of hostname, traversal order,
  and dictionary order.

## Interpretation and stop rules

- `K2_prev != 0` cuts only the quadratic tangent cone.  Compute its exact
  projective zero locus/Fitting strata; do not call it a family kill.
- `K2_prev = 0` freezes second-order persistence and moves to the lowest
  source-licensed cubic weight, not to a survivor theorem.
- A denominator factor is a new stratum, not a harmless pivot artifact, until
  an independent chart or explicit localized Bezout identity covers it.
- A current identity with a parameter-independent unit and full source replay
  can exclude a chart; a sampled/finite-order current sensitivity cannot.

All statements remain on the fixed source-typed A3/F1 chart and its licensed
transverse q/dead moduli.  There is no full-TD6, SP-2, family, counterexample,
or JC2 conclusion.
