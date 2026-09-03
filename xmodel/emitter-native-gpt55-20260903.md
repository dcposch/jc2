# Native Singular Emitter For Corrected Two-Point Charts

Date: 2026-09-03 UTC.

Lane scope: build a fast emitter under `box/emitter-20260903/`, validate it against charged charts, then run the large corrected two-point strata requested in the prompt. No ledger files, `jc2-lean`, `ideation-*`, or in-progress lane reports were edited.

## Frozen Inputs

MEASURED: I generated `/tmp/emitter-native-inputs.sha256` mechanically from `xmodel/emitter-native-gpt55-20260903.run.v2` by pairing its `charged_input_<i>_basename=` and `charged_input_<i>_sha256=` lines under `lane_inputs_dir=/tmp/jc2-lane.wRUQfg/inputs`, then ran `sha256sum -c`. All 11 charged inputs were `OK`.

MEASURED environment:

- `python3 -c "import flint"` failed with `ModuleNotFoundError: No module named 'flint'`.
- Singular used for all native polynomial arithmetic: `Singular 4.3.2`, linked with `GMP 6.3.0`, `NTL 11.5.1`, `FLINT 3.0.1`.
- New driver hashes:
  - `28cf67fd5386a9fef69094f3f00c4944a4930c79d4c464df170a9513a1224e66  box/emitter-20260903/emit_chart.py`
  - `3c8075b59d81ec996cfb553df2edd4f1fb55f92d33fb9cec5ee1e3e7dd999f2f  box/emitter-20260903/emit_chart.sing`
  - `ddc23e03e84e3462add743862bf5af459db7cd1d993d4c6f73b7a5f2799d3299  box/emitter-20260903/validation.json`

## Implementation

MEASURED: `box/emitter-20260903/emit_chart.py` is the Python driver. It reads the frozen `shape.py`, enumerates finite supports, writes concrete Singular builders, runs Singular, parses row metadata, and writes final standard-basis scripts over `Q` and over primes `32003`, `32009`, `32027`.

MEASURED: `box/emitter-20260903/emit_chart.sing` supplies the Singular-side helpers:

- `native_coeff_xy` and `native_coeff_y` for coefficient extraction by explicit `x,y` degrees.
- `native_y_div` for the validation-compatible monic univariate-in-`y` division path.
- `native_append_coeffs` for appending coefficient rows as `source_index|h_power|x_power|y_power|expr`.

MEASURED: for K16 and `(d',e')=(2,3)` A/B validations, the build ring keeps parameters as polynomial variables and uses the explicit univariate `y` division. That keeps the validation branch byte-compatible up to ordering with the charged emitters.

MEASURED: for the large generic top-face systems, the build ring is `Q(parameters,c)[y,x]` and the h-adic reduction uses Singular's `division(H, ideal(h))`. This is the fast path that avoids SymPy polynomial arithmetic and also avoids direct reconstruction of the full `J(f,g)` polynomial.

MEASURED saturation controls: every final `.sing` system includes a Rabinowitsch equation `T*(c*Omega)-1`, an empty-control ideal `<sat, T*sat-1>` that must reduce `1`, and a nonempty-control ideal `<sat-1, T*sat-1>` that must not reduce `1`. The controls printed `CONTROL_RING_PASS R`, `CONTROL_EMPTY_PASS`, and `CONTROL_NONEMPTY_PASS` for every modular run that reached `MAIN_START`.

OPEN guard: the small validation charts measure direct `deg_x J`. The large generic fast path does not reconstruct direct `J(f,g)`, so its direct degree gate is `SKIPPED_FOR_GENERIC_EMIT`. It still measures the h-adic normal-form gate: `level0_deg_x_before_minus_c`, `target_xk_level0_nonzero`, and `max_nf_deg_x_after_minus_c`. This is not promoted as a full direct-degree theorem.

## Validation

VALIDATED: native emission matches the charged chart ideals by mutual standard-basis normal-form comparison, not by text comparison.

| case | chart | emit s | unknowns | equations | direct deg_x gate | normal-form max | comparison |
|---|---:|---:|---:|---:|---:|---:|---|
| `(16,12;13;3;k=1)` | K16 | 0.016 | 18 | 23 | 5 | 1 | PASS, basis sizes 1/1, 0.038 s |
| `(28,20;25;3;k=1)` | K16/chartfix replay | 0.040 | 27 | 37 | 9 | 1 | PASS, basis sizes 1/1, 110.103 s |
| `(33,22;30;8;k=1)` part `[3]` | A/B | 0.199 | 28 | 62 | 6 | 4 | PASS, basis sizes 1/1, 0.029 s |
| `(33,22;30;8;k=1)` part `[2,1]` | A/B | 0.258 | 29 | 62 | 6 | 4 | PASS, basis sizes 1/1, 0.043 s |

VALIDATED direct charged-script check: I also emitted the native `(28,20)` K16 system with the standalone `t2_order_system.py` variable naming (`q` beta prefix) and compared it against `/tmp/jc2-lane.wRUQfg/inputs/t2_order_system.py --gauged --emit-singular`. Result: PASS, 27 unknowns, 37 equations, both standard bases size 1, comparison time 168.780 s. The charged SymPy audit for that baseline reported `alpha=15 beta=7 h=4 c=1 -> unknowns=27` and `coefficient equations=37`.

VALIDATED controls: the two `(33,22)` A/B validation strata reduce to `[1]` in the charged sense because both comparison ideals have standard basis size 1.

## `(25,15;21;2;k=2)` Large Strata

DERIVED support counts for all three strata: corrected `h` lower count 9; alpha dimensions `[12,19,20,21,22]`; beta dimensions `[15,16]`; 517 coefficient equations after h-adic normal form.

MEASURED emission and row artifacts:

| partition | top face | unknowns | emit s | equations | h-adic gate | TSV bytes | TSV sha256 |
|---|---|---:|---:|---:|---|---:|---|
| `[3]` | `y^2*(y-x)^3` | 135 | 27.831 | 517 | level0=18, max=18, target=true | 42,437,286 | `9273f538d8954f49b7529e79c848391eccd2e1a169adc20b191404e5ea65d742` |
| `[2,1]` | `y^2*(y-x)^2*(y-s2*x)` | 136 | 54.717 | 517 | level0=18, max=18, target=true | 91,503,963 | `692905e95e195a1ad76cc6e2075403f607005c8ed22f3b1e6b25472d472586d4` |
| `[1,1,1]` | `y^2*(y-x)*(y-s2*x)*(y-s3*x)` | 137 | 100.073 | 517 | level0=18, max=18, target=true | 180,365,749 | `88dfc843516b61d63c3635f74a4a6e2ccb6d2e3999b617c5e00726f0722645ba` |

MEASURED modular standard-basis results, three primes each, 1200 s cap per prime:

| partition | p=32003 | p=32009 | p=32027 | modular verdict |
|---|---|---|---|---|
| `[3]` | TIMEOUT 20:00.41, RSS 2,353,548 KB | TIMEOUT 20:00.44, RSS 2,419,012 KB | TIMEOUT 20:00.29, RSS 2,381,580 KB | COUNTING-BOUND: controls passed; no `[1]` or survivor verdict before timeout |
| `[2,1]` | TIMEOUT 20:00.84, RSS 4,084,980 KB | TIMEOUT 20:01.02, RSS 4,129,376 KB | TIMEOUT 20:01.08, RSS 4,016,572 KB | COUNTING-BOUND: controls passed; no `[1]` or survivor verdict before timeout |
| `[1,1,1]` | TIMEOUT 20:01.70, RSS 4,529,936 KB | TIMEOUT 20:01.62, RSS 4,608,548 KB | TIMEOUT 20:01.52, RSS 4,570,868 KB | COUNTING-BOUND: controls passed; no `[1]` or survivor verdict before timeout |

MEASURED exact/preprocessing: for `[3]`, `preprocess-meta` from the compact native metadata timed out after 20:00.09 before writing a result JSON. Peak RSS was 316,792 KB and stdout/stderr were empty, so the blocker is the Python parse/simplification path over the 42 MB native row TSV before exact Singular is reached. The `[2,1]` and `[1,1,1]` preprocessing runs were not launched because their TSVs are 91 MB and 180 MB; this is a typed resource decision, not a mathematical verdict.

COUNTING-BOUND verdict for `(25,15)`: native emission is no longer the primary blocker for these three strata; the current blockers are (1) standard-basis timeouts on the 517-row saturated systems over three primes, and (2) the charged SymPy preprocessing parser on the native row TSVs.

## `(24,16;17;2;k=5)` Seven Strata

DERIVED inventory, in requested unknown-count order:

| partition | unknowns | h lower | alpha dims | beta dims | status |
|---|---:|---:|---|---|---|
| `[2,2,2]` | 273 | 26 | `[32,70,93]` | `[49]` | MEASURED emitter resource block |
| `[4,1,1]` | 273 | 26 | `[32,70,93]` | `[49]` | NOT_RUN_RESOURCE_BOUND |
| `[3,2,1]` | 273 | 26 | `[32,70,93]` | `[49]` | NOT_RUN_RESOURCE_BOUND |
| `[3,1,1,1]` | 274 | 26 | `[32,70,93]` | `[49]` | NOT_RUN_RESOURCE_BOUND |
| `[2,2,1,1]` | 274 | 26 | `[32,70,93]` | `[49]` | NOT_RUN_RESOURCE_BOUND |
| `[2,1,1,1,1]` | 275 | 26 | `[32,70,93]` | `[49]` | NOT_RUN_RESOURCE_BOUND |
| `[1,1,1,1,1,1]` | 276 | 26 | `[32,70,93]` | `[49]` | NOT_RUN_RESOURCE_BOUND |

MEASURED first stratum attempt: `[2,2,2]` was started with the same generic Singular-native path and a 900 s emit cap. I terminated only the Singular child at 584.836 s because it had emitted zero coefficient rows, the rows file still contained only the 42-byte header, and Singular RSS had reached about 48 GB with no swap on the host. The wrapper recorded `emit_status=ERROR`, `unknowns=273`, `equations=0`, row SHA-256 `7f2d716d35087e97752089d9d8041944bd5a49fe5c1c4b1118591e1f3d587130`.

INFERENCE, not promoted: because `[2,2,2]` is the first and one of the minimum-unknown `(24,16)` strata, the remaining six were not launched in this run. Their support counts are at least as large in the same tower family, but no claim is made that their runtimes or memory curves are identical.

COUNTING-BOUND verdict for `(24,16)`: the generic fast path still has a pre-row expansion blocker for this row. No modular or exact verdict exists for the seven `(24,16)` strata from this lane.

## Artifacts

MEASURED generated artifact footprint:

- `box/emitter-20260903/rows`: 300 MB.
- `box/emitter-20260903/systems`: 1.2 GB.
- `box/emitter-20260903/results`: 80 KB.
- `box/emitter-20260903/meta`: 144 KB after compacting metadata to row paths/hashes instead of inlining row text.
- Total `box/emitter-20260903`: 1.5 GB.

Key records:

- `box/emitter-20260903/validation.json`
- `box/emitter-20260903/comparisons/k16_28_20_q_vs_frozen_t2_order_system_compare.json`
- `box/emitter-20260903/meta/25_15_part_3_generic.json`
- `box/emitter-20260903/meta/25_15_part_2_1_generic.json`
- `box/emitter-20260903/meta/25_15_part_1_1_1_generic.json`
- `box/emitter-20260903/meta/24_16_part_2_2_2_generic.json`

## Verdict And Next Enabled Work

VALIDATED: the Singular-native emitter is correct on the requested small controls and directly matches the charged standalone `(28,20)` `t2_order_system.py` ideal under mutual normal-form comparison.

MEASURED: for `(25,15;21;2;k=2)`, native emission is fast enough to produce all three saturated systems: 27.831 s, 54.717 s, and 100.073 s. This removes the prior SymPy emitter >600 s blocker for these strata.

COUNTING-BOUND: no `(25,15)` modular or exact emptiness claim is promoted. All nine modular runs timed out after controls, and exact/preprocessing timed out before the first `[3]` system reached a result.

OPEN: for `(24,16;17;2;k=5)`, the current generic emitter architecture still expands too much before any rows are emitted. The next emitter improvement should avoid constructing the full h-adic coefficient-field expressions for this tower in one Singular process; likely directions are streaming/truncated coefficient extraction by `(h_power,x_degree,y_degree)`, modular row emission before rational text serialization, or a compiled sparse-polynomial backend with explicit h-adic truncation.

OPEN: the remaining five large rows and the joint `(99,66)` systems are enabled only after the row-size and standard-basis blockers are addressed. This lane provides a validated native emitter foundation and concrete artifact sizes/timing limits, not a final Groebner verdict for those larger systems.

FALLACY-v2 audit: no new exit-price assertion is made in this report, so no `charge_basis=...` line is applicable. Saturation claims are limited to the printed control ideals in the declared Singular ring; no survivor, attainment, or equality claim is inferred from a timeout.

<!-- BODY-END -->
