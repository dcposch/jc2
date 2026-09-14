# Independent t = 6 controls for hostile t = 8 gate

All four controls passed on 2026-09-05. The two controls were regenerated from the exact terminal-row dump at each prime, with no change to the charged generator or row files. The p = 32003 exports were mechanically required to be byte-identical to the charged controls before msolve was run. The second t = 6 prime was 32009: unlike the t = 8 field, the t = 6 field splits there. The t = 8 replication prime 32027 is nonsplit for t = 6, so it cannot be used by this branch-specialization pipeline.

## Ring, generator, and map declaration

`gen.py` reads `box/k16rank-20260903/terminal_t6_exact_none.out` as rational expressions in `yy`, checks `RECURRENCE_PASS` and `DRIVER_DONE`, and emits top rows `T11,T10,...,T6` directly into Singular. For t = 6, `H6 = 2028 yy^2 - 1092 yy + 140`; the chosen branch roots are 27617 at 32003 and 13475 at 32009 (the other roots are 31466 and 23459). Every one of 6,490 literal rational-denominator occurrences in all 12 original rows is invertible at both primes.

The initial Singular ring is `S = F_p[b4,q2_0,q3_0,q4_0,q5_0,b3]` with `wp(1,2,3,4,5,7)`. The reduced coefficient ring is `P = F_p[b4,q2_0,q3_0,q4_0,q5_0]` with `wp(1,2,3,4,5)`. The generator checks are the unchanged charged prefix: quadratic split in b3, homogeneous top-row degree, `a0 != 0`, `G_r = a0 T_(11-r) - a_r T11`, and the eliminant identity for every W_r. The matrix row order is `(C1,B1),...,(C5,B5)`. `I2=minor(N,2)` is a Singular ideal with ten entries; `Ws=(W1,...,W5)` has five. No saturation or `sat()` wrapper is used.

The negative control is `SysY = subst(I2,b4,1)`, and the positive control is `SysW = subst(I2+Ws,b4,1)`. This is the canonical quotient map `P -> P/(b4-1) ≅ F_p[q2_0,...,q5_0]`; dropping b4 after substitution is legitimate because it no longer occurs. The actual polynomial images are independently checked to contain no b4. Generator order is retained, first the ten Singular minors and then W1 through W5. There are no zero or constant W-system input generators.

The text isomorphism is `qj_0 -> qj`, j = 2,...,5, with variable order `q2,q3,q4,q5`. Every renamed polynomial passes an allowed-variable check, a no-b3/no-b4/no-yy/no-underscore check, and exact inverse-renaming equality with its raw Singular polynomial. msolve declares `F_p[q2,q3,q4,q5]` in ordinary grevlex. Unit-ideal status is independent of monomial order.

## Fresh results

| Prime | Root yy | System | Generators | Reduced basis | Status | Wall seconds |
|---:|---:|---|---:|---:|---|---:|
| 32003 | 27617 | Y6 negative | 10 | 455 | nonunit, nonempty | 1.198 |
| 32003 | 27617 | W-locus positive | 15 | 1 | [1], empty | 2.089 |
| 32009 | 13475 | Y6 negative | 10 | 455 | nonunit, nonempty | 1.159 |
| 32009 | 13475 | W-locus positive | 15 | 1 | [1], empty | 2.33 |

Each invocation is `/usr/bin/time -v -o <stem>.time timeout -k 15s 600 <msolve> -f <input.ms> -o <gb.txt> -g 2 -t 4 -v 2`. All exits were 0. Each exporter had its own 60-second timeout. `run_controls.log` ends `ALL_FOUR_CONTROLS_PASS`. This is a fresh solver execution, not reuse of charged reduced bases. The 455-element negative result excludes a pipeline that always reports the unit ideal; the one-element positive result reproduces the intended emptiness test.

The binary is the static official Intel AVX512 msolve 0.10.1 already present at `box/moh14-charts-20260905/tools/msolve-0.10.1-official-intel-avx512/msolve`. Its CLI help identifies version 0.10.1. Singular is `/usr/bin/Singular`. All runs took place on this local host, without a fleet allocation.

## Audit trail and hashes

All generated files below are in `box/k16-t8-gate-20260905/controls/`. The reproducible driver is `run_controls.py`; the structured result is `summary.json`. Per-prime exporters are `t6_p<prime>_export.sing`, with `.out`, `.err`, `.time`, and `.status.json`. Per-system inputs and raw polynomials are `t6_p<prime>_<Y|W>.ms` and `_raw.txt`; bases are `_gb.txt`; solver outputs and resource data are `_msolve.out`, `_msolve.err`, `_msolve.time`, `_msolve.status.json`.

```text
8a29afeacf93ed66209f5d30803c569562e8ffc7875043e65a5acd02063ea794  source:gen.py
7d5bd018a0280f87008f4fb9d47d814449aa2841f94122e72a6f464e89a6864a  source:terminal_t6_exact_none.out
f3862ecd62e9a840d3c2625812908981120adca2923fc380729b144a2d545ee2  source:ctrl_t6_affinew_ms.sing
0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f  source:msolve
d540132fc36fc6bc070fd755516cc5446e20b3d85889611488159716508ce65f  run_controls.py
69384156e7bd9078dcca31cd8a9743a60b59f73123077b16fd567bb340054b8e  t6_p32003_export.sing
addafd0be05220f3d7460682010a182dd5519390a857678f7256ba85451acc4c  t6_p32003_Y_raw.txt
380ffcb0bad1832df4d4d812e6f02a04de1e53c65ee587f2f75a246322c8c4fa  t6_p32003_Y.ms
33b8cb32cffeb66fbc3e27de5b592458b39eab216b90da12930cf91322577048  t6_p32003_Y_gb.txt
ae560ff3f4536a4f271a432fd201b195f17269b9d63ded07dd5f8baef537db2f  t6_p32003_W_raw.txt
0e344b225d1db05f27d6041d8410761aca5e06fb15417cb85fce39bd4bb8834f  t6_p32003_W.ms
11fc9cc1ac31ce3a8edd9787147e211f02c89bafb23af41e909d50d39a3cff79  t6_p32003_W_gb.txt
d41f5f180e09c1c31022c2de408a384c7f9386429c20ac0cc76066ed80116d58  t6_p32009_export.sing
8a7a541de2352c4d3e0fef15ee4bdd6e400a180195f727f8337075318172dcd8  t6_p32009_Y_raw.txt
b8d9c637d0459891f36fa47b551bc3fe5992542eb902cb968bb07ed3a943fb89  t6_p32009_Y.ms
a395519a24217e83921a43d3862b0bc7aa58ae1d5994c053c121e320ef920a8a  t6_p32009_Y_gb.txt
7170addc48c2a6b888cf7638e7686a2ba068c36a8cce2ee1556d368792894095  t6_p32009_W_raw.txt
b8a6aa162b1c907cb00bd25f7d1aa6fbf403010f687f737b827f626dae66f95b  t6_p32009_W.ms
f180ba00a867f910ae0fbd999b0fc2ae9d3fd889f64e2aca8995cd13e0f80b29  t6_p32009_W_gb.txt
```

## Independent t = 8 source check

`t8_source_audit.json` records that the charged 32003 msolve system has SHA-256 `d6401d43c62af47b17b67a1fd91221e31b9bbfbb775f092bda1d839057749e6c`, exactly the hash printed in the frozen harvest. It has variables q2,...,q7, characteristic 32003, and 28 generators. Its coefficient numerals are already finite-field representatives, with no rational denominators. Changing only its characteristic line would change the mathematical ideal and would not constitute replication.

The antecedent Singular exporter `box/k16t8-20260905/affinewms2_t8_mod_p32003_b0.sing` has SHA-256 `4c8684cda0e18f0fa8cf5e97af0b460fe443b265961092667de2bbe1307cacf3` and contains 9,584 literal rational-denominator occurrences in the eight top rows. A second-prime replication must regenerate those rational expressions in the second residue field, with the new root of H8, before reconstructing B,C,I2,W and substituting b4=1. The main replication lane is responsible for recording that regeneration audit.

The exact H8 discriminant is `48*17^2*9`; its field is Q(sqrt(3)). Thus 32009, although good for the t = 6 control field Q(sqrt(21)), is nonsplit for t = 8. Direct root enumeration gives no roots of H8 at 32009. At 32027 it gives `[23825,25158]`, and all 45,806 literal denominator occurrences in the full 16-row t = 8 exact dump are invertible. This is a denominator/root audit only; it does not certify a full recurrence pivot spine or a characteristic-zero specialization theorem.

## Scope

These controls validate the concrete generation/export/solver path and reproduce both expected signs at two residue characteristics. They do not replace the t = 8 computation, do not establish the rank-lane p-integrality hypothesis, and do not themselves justify lifting finite-field emptiness to characteristic zero. No new exit-price assertion is made; no charge_basis line applies. No ledger, jc2-lean, ideation path, or original source file was edited.

## Additional independent t = 8 image verification

`t8_images.md` records the pure-Python direct exact-row modular-evaluation audit of both t = 8 `.ms` systems. It passed 308 holdout indexed image comparisons at 32003 and 32027, with an explicit fixed signed minor-order map, five nonzero holdout points per prime, and no CAS call. Script, residue vectors, and hashes are `check_t8_images.py`, `t8_images.json`, and `check_t8_images.log`. These are sample checks, not a claim of formal polynomial identity.
