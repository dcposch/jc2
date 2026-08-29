# V47R1: executable literal three-row contraction

Date: 2026-08-27

Status: **PRODUCER PASS.  THE V47 HOSTILE-REVIEW LITERAL-ROW GAP IS
REPAIRED EXECUTABLY FOR EXACTLY THE FROZEN 12 BASELINES AND 4 RAISED
SUBTAILS.  ENDPOINT REPLACEMENT REMAINS WITHHELD PENDING A DIFFERENT-MODEL
HOSTILE REVIEW OF THIS ADDITIVE REPAIR.**

## Frozen inputs and producer

```text
b895315acc241ca8542611cadefee0d4f29217f1ffecf8fbd3761b513b6aa908
  SCHEMA_R1.json
70085a3e2dadbc8d56605724880fa9ba0a2ff5b46258c0d60973d4a754b877d7
  verify_three_row_linker_r1.py
6c16224703cf79f35073bc41ac8f5cd5d1b8fa24d756aa2891b80df2870c8270
  run_v0_v10_r1/result.json
```

The schema additionally rehashes all six immutable V47 producer artifacts,
the V47 Grok review, the Fable three-row review, V46/V46R1 source and typed-map
authorities, the 569 frozen tails, and the frozen tail/load/target emitter.
The verifier also walks the five inner V47 freeze entries.

## Exact result

For each of the sixteen V47 manifests, the verifier:

1. derives and matches the finite support maxima from the V46 polar schema;
2. retains every corresponding `P`, `A`, `C`, `R`, `k10`, `k6`, and `k2`
   relative jet as an independent sparse-polynomial variable over `Q`, together
   with all four target symbols;
3. substitutes `P_0=-2*rho^2` and the contact shifts into the pinned V46 source
   formulas;
4. contracts the frozen tail rows of census
   `[36,54,58,81,89,120,131]` term by term; and
5. extracts exactly `Phi1[G]`, `Phi2[G]`, and `Phi4[T_C2]`.

All 48 extracted coefficients match the mapped-D1 triple

```text
Phi1[G]    = (3/4)*(AcD1_0*CzD1_0 + AzD1_0*CcD1_0),
Phi2[G]    = (3/4)*(AcD1_0*CcD1_0 + rho^2*AzD1_0*CzD1_0),
Phi4[T_C2] = (3/8)*(CcD1_0^2 + rho^2*CzD1_0^2).
```

Their common canonical coefficient digest is

```text
ad0c9b15ce394e554c178521fadb32b3c71318cf3a8d700a2311aceb9d12a850.
```

Every extra retained in-window jet has zero coefficient in all three slots.
The raw-total chart

```text
A0=AzRaw_0*z+AcRaw_0,
C0=(EzRaw_0*z+EcRaw_0)/2
```

gives the coefficient digest

```text
00720abb62b26d965c87a1ecce0aff5d593833bfa205a221c0cda8cb4687ff95,
```

and maps exactly to the displayed D1 triple under the reviewed typed map

```text
EzRaw_n,EcRaw_n -> 2*CzD1_n,2*CcD1_n.
```

The sixteen per-manifest records have canonical digest

```text
8ff50e047975e1a4b651c1e6af27b5874a3ac93856981bca2d9b8a5fe4609e48.
```

## Live mutations

Eight controls fire: raw/D1 `C` factor conflation; `Phi1` and `Phi4`
normalization changes; injection of `AzD1_1` into the charged slot; deletion of
frozen row-1 tail term 13 (zero-based); opening either target wall; and deleting
one of the sixteen coefficient manifests.

## Narrow interpretation

This repairs the smallest failing hypothesis in the V47 hostile review: endpoint
report hashes are no longer used as a surrogate for coefficient comparison.
Endpoint hashes remain only localization/theorem-type provenance.  V47R1 does
not cover the five `RA^2` contacts, exceptional `E`, the `a=7` load tie, either
target wall, `rho=0`, equality faces, or any broader Gate T/global conclusion.
No endpoint/allocation replacement is promoted by this producer result alone.
