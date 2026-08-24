# Freeze registration — `GCD3-69-COMMON-CUBIC-FIRST-GATE-20260824`

Frozen: `2026-08-24T13:31:44Z`  
Charged bank: `6f2e49e63d74493910fa357a8adc82f0e40d219a`

## Chronology disclosure

Exploratory derivation and private scratch replays preceded this file.  This
registration freezes the final banked replay, claim perimeter, and verdict
taxonomy before materialization and the registered final replay.  It is not
represented as a blinded preregistration of the discoveries.

## Frozen inputs

```text
6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe  xmodel/as109-partial-y-history-stop-20260824.md
f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd  xmodel/as109-partial-y-history-review-grok-20260824.md
9adbbf0326610b455497e1bbefc43933bdb5cae7e3de9bb8f4ab5128deed9834  xmodel/ideation-20260824T1205Z-event-synthesis.md
```

The reviewed input licenses the first unknown actual partial-degree residue
`(6,9)` with `3 | deg(h)` and leading common powers `h^2,h^3`.  It does not
license a full filtered common root or nonlinear closure.

## Registered questions

1. Does the first source row align the two Kummer depressions, and under
   exactly which field hypothesis?
2. What are the squarefree, double-root, and triple-root strata of the
   depressed common cubic?
3. Does one source boundary root justify reduction modulo the full cubic?
4. What do the linear and first quadratic component residues actually prove?
5. What is the complete reduced normalized constant-W scheme at degrees
   `(6,9)`?
6. How many integration constants survive the eight high source rows after
   nontrivial Kummer descent and constant target gauges?
7. If the source path enters the unique Davenport--Stothers component
   purely, can the Keller ODE and polynomial boundaries exclude it?

## Frozen claim perimeter

Allowed positive conclusions are exact polynomial identities, component
decompositions over characteristic zero, conditional local-valuation
exclusions, and explicit controls.  A chosen-root boundary may be promoted
to full-cubic divisibility only with a separately proved orbit-degree-three
hypothesis.  The constant-W component calculation may be applied to a source
trajectory only after pure-component entry is derived from the lower source
rows.

No result from this gate may claim an actual `(6,9)` Keller pair, nonlinear
`(6,9)` exclusion, or a JC2 inference.  The cube-core mismatch `delta != 0`
remains separate.

## Registered replay and verdict markers

Run without network:

```text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/gcd3_69_common_cubic_first_gate_20260824/replay.py
Singular -q \
  cases/gcd3_69_common_cubic_first_gate_20260824/verify_constant_w_scheme.sing
```

The Python replay must terminate with `PASS-GCD3-69-FIRST-COMMON-CUBIC-GATE`
and explicitly print:

```text
full_cubic_boundary_reduction=TYPE-FAIL-WITHOUT-ORBIT-DEGREE-3
high_row_reduction=FIVE-COEFFICIENTS-PLUS-KAPPA
nonlinear_constant_w_bypass=UNIQUE-ORDER3-DS-CURVE
pure_ds_source_ode=(lambda^7)'=j/(81s)
nonlinear_69_closure=false
keller_pair_found=false
jc2_inference=false
```

The Singular replay must terminate with
`PASS-GCD3-69-CONSTANT-W-SCHEME` and identify exactly the common-cubic prime
and unique DS prime, meeting only at the triple-cubic origin.  Any assertion
failure, component-count mismatch, hash mismatch, or omitted negative-scope
marker fails closed.
