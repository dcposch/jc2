# D43 source-coordinate bridge audit — Fable 5

UTC: 2026-08-28T19:16:09Z  
Role: independent read-only audit, run through the authenticated `claude` CLI  
Scope: the eight omitted source directions, the two `uW` assembled coordinates,
and what those facts do and do not establish.

## Verdict

**CONFIRMED, with a scope boundary.**  The eight nominal source-tail directions
`tf1/tf2/tg1/tg2` at offsets `r=39,41` are structurally absent from every one
of the 184 selected source-row polynomials, over any coefficient ring.  The two
assembled coordinates `uW1,uW2` are inverse-chart auxiliaries with defining
rows `W1*uW1-1` and `W2*uW2-1`.  Hence the coordinate counts reconcile as

```
190 nominal source = 182 effective source + 8 inert
184 assembled      = 182 shared source + 2 inverse auxiliaries.
```

This closes the *column census in substance*.  It does not certify integral
normal-form/presentation equivalence, formal smoothness, a characteristic-zero
point, an all-depth object, a polynomial Keller map, or JC2.

## Structural proof of the eight zero columns

- All selected D43 Euler bands are even and at most 42.
- The relevant tail offset enters through its own slot.  Its possible
  companion contributions have smallest positive odd slot 5; slots 1 and 3 do
  not occur in the registered generator support.
- Thus an `r=39` or `r=41` tail can contribute only at 39 or 41 by itself, or
  at least at 44 or 46 after multiplication.  None is an even selected band at
  most 42.
- The alternate/other-block locations are at offsets at least 59 or 61 and
  are truncated before the selected bands.

Therefore each of the eight columns is identically zero as a polynomial
column, not just numerically non-pivotal at the banked witness.  The committed
one-prime replay corroborates this: full nominal and restricted essential
Jacobians both have rank 129 and augmented rank 129, and the same 24-coordinate
correction replays all 184 rows modulo `p^2`.

## The inverse coordinates and rank accounting

The two parked rows are dictionary-exactly `W1*uW1-1` and `W2*uW2-1` at both
banked primes.  Their `uW` derivatives are units on the declared chart.  The
source rows have zero `uW` columns, so these add exactly two independent
first-order pivots:

```
source rank 129 + inverse-chart rank 2 = assembled rank 131
tangent dimension: 190 - 8 - 129 = 184 - 131 = 53.
```

The tails-plus-x source submatrix has rank 125, so the eight fixed carrier
directions contribute four genuine rank dimensions and must not be discarded.
At this witness the remaining 32 non-inverse parked-row gradients lie in the
span of the source gradients and the two inverse pivots.  That is only
first-order redundancy; it is not an ideal-membership certificate.

## Consequences for current lanes

The pristine 184-row system is a self-contained 182-effective-coordinate
model for the **finite D43 source-existence lane**.  It can be lifted or solved
without the 32 non-inverse parked rows.  Those parked rows remain necessary
for claims about the banked cell/presentation, exact normal-form equivalence,
and reuse of the assembled 131-minor.

Existing evidence remains only a one-prime `p^2` source lift.  The 55-dimensional
left cokernel of the rank-129 Jacobian is the unresolved singular-lifting
obstruction.  Neither the source nor assembled presentation has a formal
smoothness certificate.

## Recommended cheap certificate

Before promoting the coordinate bridge itself, emit one fail-closed JSON that:

1. mechanizes the parity/slot census and the eight unreachable labels;
2. parses both parked-prime inputs and identifies the two inverse rows exactly;
3. replays tail, fixed, `alpha`, and `beta` column identifications at both
   banked primes; and
4. records the full `190 -> 182 shared + 8 inert` and
   `184 -> 182 shared + 2 inverse` dictionaries under hashes.

This certificate is useful for presentation provenance.  It is deliberately
separate from the current pristine-source high-order Hensel runner, which
should not inherit an assembled-218 or normal-form-equivalence claim.
