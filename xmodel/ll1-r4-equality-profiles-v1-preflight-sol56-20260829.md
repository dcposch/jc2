# LL1-R4 equality profiles — coordinator preflight bank

Date: 2026-08-29 UTC  
Lifecycle: `DEFER_ACTIVE_LANE / BANK_CONDITIONAL_PROFILE`

## 0. Custody and disposition

The promoted R4 book and summary are frozen as

```text
7715083c811a3d9fd011aeed245c23ede31c56d9fbf055a571c11bfe08aaef04
  cases/landing_ledger_ll1_r4_20260829/out/ll1_book.json
29bc125bea86dc35d9d181d445b4927babb154ce88e9c9720efb60d0ee33c689
  cases/landing_ledger_ll1_r4_20260829/out/ll1_summary.json
```

The software review is Fable 5 `PASS` `d00a8eab...`; the full-carrier theorem
is `82d2f6c3...` with Grok review `1b3be27d...`; and the safe-floor audit is
`05f68f4b...` with Fable review `56e95db5...`.

Disposition: defer `LL1-R4-EQUALITY-PROFILES/v1` as an active proof or
Eisenbud--Neumann lane. Five zero-slack terminal states encode six route
profiles, and all six are scalar-consistent. There is no new kill. Bank a
tiny exact-arithmetic consumer only if an occurrence, source, or decoration
client appears.

## 1. Conditional equality statement

Assume an actual Keller configuration realizes one named R4 route on the
fixed fibre, with the inherited jump/max reading of `kappa`. For each of the
six profiles below, the displayed full-carrier lower floors plus the x-side
floor `psi` sum to `td-1=5`. Since the actual C7.1 union has weight at most
five and every summand is nonnegative, every named aggregate weight must
equal its floor, the x-side witness must have weight exactly `psi`, and no
additional distinct cv flag can occur on that fibre.

This is a conditional implication, not an assertion that any route occurs or
that any lower floor is attained. It supplies no puncturewise `Lambda`
equality.

## 2. Six route profiles

Notation `d;m/L` records defect `d`, multiplicity `m`, and full-actual lower
floor `L` for one direction. Refinements by `q` and `tau-kbar` use the
inherited fixed-`kappa` convention.

1. State `(3/4,4,2)`: two `(20,16)` directions, each `1;1/1`. Each is a
   singleton of weight one with `q=1`, `tau-kbar=1`; x-side weight is three.
2. State `(2/7,7,4)`, route A: the preceding two `1;1/1` directions plus
   `(119,35)` with `2/3;3/2`. The last aggregate is either one weight-two
   flag with `(q,tau-kbar)=(2,1)` or `(3,2/3)`, or exactly two weight-one
   flags with `(q,tau-kbar)=(1,1)`; x-side weight is one.
3. State `(2/7,7,4)`, route B: `(21,15)` has `2;1/2`, hence one weight-two
   flag with `(q,tau-kbar)=(1,2)`; `(35,15)` and `(21,7)` each have
   `1/2;2/1`, hence one weight-one flag with `(q,tau-kbar)=(2,1/2)`;
   x-side weight is one.
4. State `(2/9,9,4)`: `(21,15)` and `(35,15)` are as above; `(117,27)` has
   `1/4;4/1`, hence one weight-one flag with `q in {2,3,4}` and
   `tau-kbar=1/q`; x-side weight is one.
5. State `(3/10,10,4)`: two `(20,16)` directions are `1;1/1`; two
   `(130,40)` directions are `1/3;3/1`, each a singleton of weight one with
   `q in {2,3}` and `tau-kbar=1/q`; x-side weight is one.
6. State `(3/8,8,4)`: two `(20,16)` directions are `1;1/1`; two `(40,16)`
   directions are `1/2;2/1`, each a singleton of weight one with
   `(q,tau-kbar)=(2,1/2)`; x-side weight is one.

All six profiles have no epsilon/zero representative term. Every scalar
profile is nonempty, so scalar equality yields no contradiction.

The state `(2/7,7,4)` has two incoming histories. A future consumer must
reconstruct paths from `sections.residue_steps`; it must not trust the single
canonical `path` stored on the terminal-state record.

## 3. Novelty and missing client

The implication “zero C7.1 slack forces equality in every displayed
nonnegative term” was already known from `SHEET6-LROOT`, the corrected
Section-7 audit, and the 1224 Grok cross-pollination. New here is only the
R4-specific six-route instantiation and the fine flag/`q` branch list. D73
already blocks any strictness inference from multiplicity alone.

The earlier `SHEET6-CLASSICAL` pass concerned the old residue-A genome and
does not transfer. R4 contains reduced physical-prefix/cell data, not the EN
splice decorations needed for a splice audit: Newton pairs/contact matrix,
arrowhead and component multiplicities, edge/linking weights and signs,
compactification gluing, and B/x tails are absent. Do not manufacture an EN
diagram or infer a kill.

## 4. Smallest honest future consumer

If a typed client appears, one exact-`Fraction` script should pin the book,
theorem, and reviews; enumerate every zero-slack graph path; identify each
direction by `(route,step,orbit_index)`; and emit the aggregate/branch
profiles above with explicit flags

```text
OCCURRENCE_UNPROVED
ATTAINMENT_FALSE
PUNCTURE_EQUALITY_FALSE
EN_DECORATION_ABSENT
```

It must fail closed on a representative epsilon term, a missing alternative
path, or an absent H5a convention. This is desk-scale and licenses neither
CAS nor AWS.

## Seal

- Body length: `4835` bytes (all bytes before this heading).
- Body SHA-256:
  `d60ab52263024ce26871808fc687ceb3e28b5b31a889172c3d29833b00ec00fd`.
