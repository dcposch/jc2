# Preregistration: explicit-normal-form incremental `T-rs-0` row shards V8

Date: 2026-08-26

Status: **SOFTWARE-SEMANTICS REPAIR AND DISCOVERY ONLY.  NO REES, CHART,
MOVING-`p`, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## Failure being repaired

An exact Singular 4.3.2 canary showed that a polynomial assigned in a
`qring` need not be stored in canonical quotient normal form.  In
`R/(sigma^13)`, the assigned polynomial `sigma^13*x`, its substitution
difference, and its formal derivative all compared nonzero, whereas
explicit reduction by `std(ideal(sigma^13))` returned zero.  Therefore the
V0R1/V2/V5/V7 quotient-ring equality and dependency sentinels are
quarantined as software no-verdicts.  This does not change the frozen
source mathematics.

## Frozen successor

V8 imports the frozen V7 compiler and its complete transitive source, but
emits the computation in the ordinary parent polynomial ring.  It never
declares a `qring`.  Every source atom is explicitly reduced by
`PrefixNF=std(ideal(sigma^13))`.  Each tail monomial is built one factor at
a time, with explicit normal-form reduction after every multiplication and
after every addition to the row accumulator.  Powers of every `F_i` are
also built by reduced recurrence.  This is algebraically the same image in
the quotient `R/(sigma^13)`, while avoiding both noncanonical comparisons
and high-degree intermediate growth.

The compiler reconstructs every one of the 569 frozen tail terms from the
literal exponent/coefficient data, checks the legacy formula text exactly,
and records per-row formula hashes and update counts.  Runtime clients must
print and pass an explicit-normal-form canary, the original specialization,
deck, extraction, coefficient-map, negative-control, and dependency
sentinels.  The 76 candidate names and seven inactive names are unchanged.

V8 first runs at the two discovery primes 32003 and 65521.  Agreement is
navigation only.  A discovered manifest is not frozen until both validated
lanes agree.  It then requires exact Q and a fresh good prime before any
promotion.  Any hash mismatch, compiler/engine timeout, Singular diagnostic,
missing or duplicate sentinel, transcript disagreement, inactive-name hit,
or validator error is `FAIL/UNRESOLVED`.

