# Selected delta2 stage8 SLIMGB trial

This uses the independently replayed complete 99 stage-8 circuit input, the
audited jet0 translation slice, strongest stage-specific front consequences,
all retained source images, all five target scalars, and both localizers.

The frozen coefficient-circuit v2 emitter produced 2537 generators and 3836
rows. `slimgb_variant.py` changes exactly one string, `std(I)` to `slimgb(I)`.
An independent full-byte comparison confirms that every generator, equation,
target subtraction and control remains identical. Both positive and negative
exact-Q algorithm controls passed before launch.

The full production leading-row audit reconstructs source H0 and checks all
16 coefficients of lambda*z^40*(1+z)^15 at t-depth 141. Every coefficient is
subtracted, and Z55*leader55-1 is retained. The leader occurs in no source or
graph defining row. See `target-subtraction-check.json`.

`custody.json/.sha256` bind the input, independent input replay, emitter,
algorithm helper, bounded runner and control receipt. All six hashes passed
mechanically on the existing fleet worker before launch. The base and variant
hashes are additionally checked by `independent-variant-check.json`.

The selected job has a 32 GiB address-space limit and a 1200-second wall limit.
Its emitted 3836 rows parsed completely before entering the Gröbner calculation.
It ended **COMPUTE-BOUND-OPEN** at 1200.467 seconds, still in that calculation,
with no parser/CAS error and an unchanged script hash. No result or terminal
control block completed, so it proves neither a unit nor a proper ideal.
At elapsed 17m34s its RSS snapshot was 13,976,228 KiB; this is not a maximum-RSS
measurement. `result.json` and `memory-samples.jsonl` retain the exact evidence.
Both owned processes and their process group were confirmed absent after the
timeout; `closure.json` records that check. All final output was pulled locally.

This trial owns only its runner and Singular process. The coordinator owns
the fleet instance and must terminate it before sealing the campaign report.
