# V8 explicit-normal-form `T-rs-0` discovery results

Date: 2026-08-26

Status: **PROVISIONAL EXACT-Q PLUS THREE-PRIME PASS; HOSTILE SOFTWARE/SOURCE
REVIEW PENDING.  DISCOVERY ONLY—NO REES, CHART, ORDER-TWO, MAXIMUM-TWELVE,
OR JC2 VERDICT.**

## Semantic repair

The predecessor clients used a Singular `qring` as if every assigned
polynomial were automatically stored in quotient normal form.  An exact
canary disproved that operational assumption: a stored multiple of
`sigma^13` and its substitution difference/derivative compared nonzero.
V0R1, V2, V5, and V7 are therefore software no-verdicts.

V8 uses the ordinary parent ring, `PrefixNF=std(ideal(sigma^13))`, and
explicit reduction after every source multiplication and accumulator
addition.  It retains the frozen 569 tail monomials, 85-name ambient ring,
76 candidate names, seven inactive controls, and all original source-map,
deck, extraction, coefficient-map, recombination, and negative controls.

## Four-lane result

The two discovery primes `32003`, `65521`, exact `Q`, and the fresh prime
`1000033` all completed with compiler, seven row engines, aggregation,
ordinary-ring recombination certificate, and final validator at `rc=0`.
After removing characteristic and evidence-path fields, every mathematical
field in the four `DISCOVERY.json` files agrees exactly.

- Common sigma order: `10`.
- Discovered finite-prefix manifest (23 names):
  `ell1, ell2, cs, cs1, cs2, rs, rs1, rs2, a1, aa1, aaa1,
  a0, aa0, aaa0, c1, e1, ee1, c0, e0, ee0, k, k1, k2c`.
- Every other candidate bit is zero through grade 12.
- All seven inactive controls `k6_1, k2, k2_1, mu2, mu4, mu6, J` are zero.
- The frozen cusp recombination and its omit-`g10_3` negative control pass.
- The total correction is nonzero and exactly divisible by `rho^2`.

The exact-Q certificate gives

```text
Delta/rho^2
 = 5120*rho^2*cs^4*k + 2640*cs^2*rs^2*k
   - 4608*cs*a0*c1 - 4608*cs*a1*c0
 = 16*cs*(320*rho^2*cs^3*k + 165*cs*rs^2*k
           - 288*(a0*c1+a1*c0)).
```

Thus the total lift is not the frozen identity itself: its first correction
is a four-term, even, nonzero `rho^2` multiple.  This is navigation for the
actual saturated `D_+(rs)` Rees/base-change client, not yet an ideal or
chart obstruction.

## Critical evidence hashes

| lane | `DISCOVERY.json` | `EVIDENCE.sha256` | compiler result |
|---|---|---|---|
| p32003 | `a2f4c9c16b07ba9e156ab7076100a245003b25a9b2d82c387a2fd2adec71ed02` | `3880363818681e83711e61d615333b9afe4b63e51788871f875065575bad0b73` | `84a6d91f2dfd19480cbe1611652bb53b93583572194702184399fac7cc31b900` |
| p65521 | `75718cd651e6b80cf36d73b4ce6949b0934005c540c4ba8cb47a61b724e6e795` | `74c9f6aab3cea1d431b4a9ea04e245b13f0969b3b819789a2c2a05cb7f640828` | `f296b519d0d697bdd18730c1ca85f39e774310a06dcbbe79b2e6ecabfabcd6b0` |
| exact Q | `9fa0f599293cea4a03644e99e0e2b0e036f8e37c55ffab9dc91a4a7fb9959756` | `7b49399500a9473e6d52ba56ec63bbe958bfbc1f2d2b29296af4185fcc846c11` | `368e5edf112dce5e122cd9a5918545b9462158dd523d6636a886909b4cf7bac4` |
| p1000033 | `f6537f3622acad18ed82806ca951b3ad0f974fab9c1b388d94f950df3740d266` | `c4abb341e5335b8a686bc50168aa4e598510a6a1e7bda753f04ab40784ee5743` | `80302ceea256e99396c7f8f15bc80978fbfc560b3e5a92cebd1b3721e0956f36` |

The controlling V8 source freeze manifest is
`508c7cc0aeaf26385b5954173ca366b362c697540879822327db3d75367ccc26`.
