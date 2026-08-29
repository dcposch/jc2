# V43C2 preregistration: exact constructive `rho=0` certificate circuit

Date: 2026-08-27

## Frozen question

Can the reviewed V42 branch cascade be compiled into an exact, global
ordinary-ideal certificate

```text
a1^104 in I0
```

for the complete frozen raw ordered-`a1`, `rho=0`, grade-through-19 corpus,
without expanding the very large row multipliers?

This is a representation change for the already registered V43C1 proof tree,
not a different algebraic argument.  The coefficient multipliers are honest
polynomials over `Q`, represented by a shared arithmetic DAG with typed
`Sparse`, `Add`, `Mul`, `Scale`, and nonnegative-integer `Pow` nodes.

## Exact acceptance predicate

Accept only if a fail-closed verifier, from the frozen literal row bytes:

1. rehashes the V43C1 source (`af590ff872552944528dda41497329e1b1534cc211290d622034defd70bac2ca`),
   V42 replay (`f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459`),
   V42 report (`5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f`),
   V42 hostile review (`a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439`),
   and all 70 frozen row files;
2. checks the 51-nonzero-row/70-file census and the exact 65-variable
   `rho=0` alphabet;
3. verifies every row-specialization leaf coefficientwise using the exact
   divided-difference identity;
4. typechecks every arithmetic-DAG node and forbids negative exponents;
5. replays every certificate derivation node in topological order, including
   `Add`, `Scale`, polynomial `Mul`, `clear_power`, and `combine_branches`;
6. checks the `clear_power` and `combine_branches` rule schemas as exact
   universal polynomial identities for every exponent used;
7. obtains final target exactly `a1^104`, with no assumption generator and
   only literal frozen row labels in its multiplier map; and
8. rejects both (a) omission of a nonzero final literal-row multiplier and
   (b) a changed clearing exponent in a derivation node.

The derivation DAG itself is the exact certificate.  Modular point evaluation
may be recorded only as telemetry; it is never an acceptance predicate.

## Scope and firewalls

- Ambient ring: `Q[X19_rho0]`, the 65-positive-variable frozen ordered-`a1`
  raw ring after `rho=0` and after the ordered chart specialization
  `rs=cs=c0=c1=a0=0`.
- Ideal: all 51 nonzero literal raw rows through grade 19 (the output
  certificate may use a subset).
- No localization, radical, field-point split, or division survives in the
  final certificate.  All DAG powers are nonnegative.
- This does not by itself prove an unspecialized-`rho`, saturated-Rees,
  Gate-T, bounded-degree, order-two, maximum-twelve, or JC2 statement.
- The successor converter may use this only after lifting it to an exact
  same-row total identity `a1^104-B=tH`.

## Registered execution

Heavy execution is AWS-only.  Initial cap: one core, 16 GiB RSS, one hour.
The expanded V43C1 run remains live as independent corroboration.  V43C2 may
not stop or mutate it.
