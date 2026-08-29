# Lambda-zero fixed-q1 resume r3 result

The recovered 58,975,191-byte lambda-zero packet passed exact byte, canonical
JSON, record-hash, source-provenance, and regenerated-script validation.  Its
exact triangular reduction also passed, with 241 pivots, 77 free variables,
66 active free variables, 14 compatibility constraints, and no constant
obstruction.  Exact and `p=65521,65519,65497` ranks agreed at every gate.

The subsequent three reduced Gröbner screens each reached the registered
600-second timeout (about 10:01 wall including termination), after printing
only `QREDUCED variables=66 generators=14` and `START_GROEBNER`:

| prime | exit | max RSS | swap |
|---:|---:|---:|---:|
| 65521 | 124 | 41,501,924 KiB | 0 |
| 65519 | 124 | 41,500,396 KiB | 0 |
| 65497 | 124 | 41,769,180 KiB | 0 |

No unit, modular survivor, exact-Q result, or raw endpoint witness was
produced.  The strict verdict is
`NO_VERDICT_MODULAR_SCREEN_NONUNIT_OR_INCOMPLETE`; timeout is not a survivor.

Principal hashes:

```text
605af2ccc1f5229e38ba501fc7249a3ebfd4b750945fc7b5b83d42bab112c996  custody/JOB_ARCHIVE.tar.gz
5e7c69f92add6eb58ebf4be06b93ebc8eedfc88ca62e7d3a8c7f5f7b244edc26  validation/VALIDATION.json
bed63d0437c55ac2214b36640b3e28d33cbf0fab5c0dcbbe4505a80e0a24e13c  triangular/TRIANGULAR_REDUCTION.json
165bc67ad96bd8a3cb367b99d29473862b54d46f7bab3b6c9eb85cccc3663ff4  output/RESULT.json
5fcbba51876551a22e0a9caa112dfc07999746ec4c7fb287a67445fccc31238d  output/TERMINAL and VERDICT
d620b1daa0eb0f09af26ef4dc91f3135d20e64cde450657a5201f31f26b405a1  records/FINAL_CENSUS.json
cfbfe1e51b8d991d1df3c2e4c32032fc373a31a78fb35cee055f14e7ce152c91  EVIDENCE.sha256
```

All 89 files in the remote custody manifest replay locally.  Worker and
monitor exited zero; the final census has no group member and zero swap.  This
necessary q-gate screen proves nothing about the lambda-one slice, the full
branch, endpoint existence, JC2, HENS-CT, or `jc2-lean`.

