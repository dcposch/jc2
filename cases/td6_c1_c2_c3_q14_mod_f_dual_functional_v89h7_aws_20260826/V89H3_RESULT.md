# TD6 V89H3 q14 alternate-pivot/Fitting result

Date: 2026-08-26

Producer verdict: **DIAGNOSTIC PASS on Box02 and r6d; no q14 collapse
theorem is claimed.**

## Exact result

The V4 client rebuilt literal FIRST with independent
`q14,q16,...,q24`, with `q2,...,q13=0` and q15 absent under the separately
reviewed target shear.  On the reviewed 38-column q-zero pivot basis the
only cyclic support component is

```text
S = {0,1,2,3,4,5,6,13}.
```

The division-free determinant of its exact 8 by 8 q14 block is the constant
polynomial `1`.  In particular, the cycle does not itself require a
q-dependent denominator.  The determinant coefficient file has SHA256
`6d618994ff0f15810466984f8a01c866299024766baa80266e4878487ee44a59`.

The bounded scan then tested all single constant exchanges between the 38
reviewed pivot columns and the other 94 retained section columns.  Of 1,004
invertible exchanges, 62 met the registered-denominator gate.  None made the
support graph acyclic.  The best registered exchange was position 6,
column 7 to column 9; it retained eight cyclic nodes, eight self-loops, and
368 edges, with graph SHA256
`523cee369bffd0ac6e64df7571eaa0c95b40e9060609c4e43f1b2c2cc87b847f`.

The diagnostic common denominator factors as

```text
(1/4) * B3 * H^3,
```

so its radical is contained in the registered `U,H,B3` open.  The client
inverted no `F`, q expression, or unregistered factor.

## What this does and does not prove

The constant-unit SCC determinant is a strong lead: it suggests an explicit
polynomial inverse may exist despite the cyclic dependency graph.  V89H3 did
not construct that inverse, verify both matrix products, reduce literal P12,
or replay original-source multipliers.  Those are mandatory gates for the
successor V89H5 client.

The single-exchange result is only a bounded negative diagnostic.  It does
not exclude multi-column changes, a Fitting cover, or the current unit-SCC
inverse.  No radical-membership, source-point, nonintegrability, fixed-A3,
TD6, SP-2, or JC2 claim follows.

## Custody

- V4 source archive:
  `a1c6eb18828897ac16b5af2c433553e54bfbe5318d4cae559d0b35aa9a465494`;
- source manifest:
  `4b825d6b759d6602d19dc71a796a0b8907fe43573e217659137033126949fd8b`;
- client:
  `3f3bac382abed09d6cdad8f0b69f1c3b4ba852dba45ee18152429a737a54f84f`;
- exact result:
  `5c7623252d67cb2786f5f2b52db5b5060505292f771c0a65c4e8e2b570cd684f`;
- exchange inventory:
  `1e87d5fcd576b40ce7b32e92d18a08aa3c8257dcc74a9a6e74eb8b0dab417147`;
- byte-identical mathematical stdout:
  `d1a4b02c16650edad60e84e5d17f6a3eda49667e6468067a2e52a11135b5c66e`.
