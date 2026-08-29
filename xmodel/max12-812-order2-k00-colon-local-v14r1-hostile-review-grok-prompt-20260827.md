# Hostile review request: K00 V14R1 exact local membership (Grok reroute)

Independently adjudicate the narrow exact-Q V14R1 theorem below.  Do not use
producer `PASS`, `ENDPOINT`, validator, or report prose as mathematical
evidence.  V14 is explicitly custody-failed; review only the regenerated R1
producer and its byte-frozen evidence.

## Charged theorem

Let `R=Q[d0,...,d5]`, `m=(d0,...,d5)`, and let `r1,...,r7` be the exact
unloaded frozen tails in the K00 transverse chart after the normalized slice
`C6=1`.  For `I=(r1,...,r6)`, V14R1 charges only

```text
r7 in I R_m.
```

The proposed unit-denominator identity is

```text
h = 63*d4+20,
h*r7 = u1*r1+u2*r2+u3*r3+u4*r4+u5*r5+u6*r6,
h(0)=20 != 0,
```

with the six exact `u_i` serialized at
`aws_q_box01_pass/run/artifacts/UNIT_MULTIPLIER_1.txt` through
`UNIT_MULTIPLIER_6.txt`.

## Mandatory independent attacks

1. Rehash and type-check the V14R1 preregistration, source freeze, producer,
   serializer/replay builder, validators, exact result, and both portable
   evidence manifests.  Confirm that the source map reconstructs the seven
   rows from the frozen one-parameter tail JSON, applies the K00 transverse
   coordinates, removes all loads literally, and normalizes `C6=1`.  Keep
   `Jdet` distinct from `J1/J2`; no Jacobian variable occurs in this unloaded
   local claim.
2. Independently parse or reconstruct `r1,...,r7,h,u1,...,u6` over exact
   rationals.  Replay **coefficientwise**, without trusting producer markers,
   the signed identity `-h*r7+sum_i ui*ri=0`; check that substitution
   `d0=...=d5=0` gives `h(0)=20`.  State the first nonzero coefficient if
   replay fails.
3. Verify that all 36 files `COLON_LIFT_i_j.txt` exist and match
   `EXACT_LIFT_ENTRIES.sha256`; verify that the six `UNIT_MULTIPLIER_i.txt`
   are byte-identical to column 1.  Audit the historical V14 gap: its single
   matrix serialization is not accepted as evidence and no missing R1 entry
   may be inferred from it.
4. Inspect the fresh replay construction.  Confirm that the second Singular
   script obtains `h,u1,...,u6` only from the serialized polynomial files,
   obtains the ring and rows from the frozen prelude, contains the correct
   sign, and has literal-zero residual.  Attack unsafe parsing, hidden reuse
   of an in-memory matrix, wrong column, truncated matrix, and false unit
   tests.
5. Independently check the algebraic inference: a polynomial identity
   `h*r7 in I` with `h notin m` implies `r7 in I R_m`.  Reconcile this with
   the separately reviewed V8 global theorem `r7 notin I`; do not mistake
   global nonmembership for local nonmembership or conversely.  Explain why,
   if the identity survives, every finite `(d)`-adic truncation is compatible
   and D9+ cannot discover a first filtered obstruction.
6. Treat the independently compiled `p=65521` lane as a software control
   only.  No characteristic-zero claim may be inferred from it.
7. Enforce the scope firewall.  This is an unloaded, normalized local-ring
   theorem only.  It says nothing by itself about mixed load/target or
   Lambda-order reachability, closure-first incidence, formal convergence,
   Taylor realization, order two, maximum twelve, or JC2.

## Evidence and hashes

```text
cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/RESULT.md
  039590c8524e98e0fce3f6ada46fdf338270ece56c3aea553644c83911b7f7d7
cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/EVIDENCE.sha256
  4e0ac1bb66c8c8fe16bb4b29f2cd43afae13f535a0949f55aa42827d501711de
cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/EXACT_LIFT_ENTRIES.sha256
  0e4159d5fe514da957b7963edb687583cbd97d76856d436c047505c2e0bddbdb
exact RESULT.json
  28be0ddf9d12529586817e6a7e96cb3ff2bc8e84e4983f7c2f25366f81b4f7e2
fresh exact replay input
  8f35f7dcad0e678e7ec6a430b54546017e0798b16d69e8491e86b183331ddc07
fresh exact replay residual (`0`)
  9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
exact unit witness
  87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04
```

Return `PASS`, `REPAIR`, or `FAIL`; identify the smallest failed identity or
missing hypothesis and state the strongest exact theorem that survives.

Write the complete report to exactly
`xmodel/max12-812-order2-k00-colon-local-v14r1-hostile-review-grok-20260827.md`.
Touch no other campaign artifact.  Do not enter, read, build, status-inspect,
or modify `jc2-lean`.  Use only desk-scale exact checks; launch no AWS job,
run no heavy local CAS computation, perform no web sweep, and edit no
canonical ledger.
