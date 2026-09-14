# `(99,66)` precise gauge-payment replay

This directory is the self-contained driver and evidence bundle for the
2026-09-05 replay.  It deliberately preserves the sound D2 radius, cutoff,
D1 row definitions, raw minor supports, and stage schedule of the charged engine;
the instantiated rows are recomputed from the repaired `h3`.  The
only mathematical chart enlargement is one free minor constant `jet0` on
each branch.  On `delta52`, `Hc_11_0=0` (`b0=fixed_zero`) remains imposed, so
exactly one of the two competing pins is released.

Pinned engines:

- `original_band_engine.py` is the byte-identical charged control engine,
  SHA-256 `3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9`.
- `band_engine.py` is the precise replay engine, SHA-256
  `76d8c7206f70ba190d1a21fff812c016cbde497cd64071c29c91cfe8089f3c06`.

Custody and local patch validation:

```bash
bash verify_charged_inputs.sh
bash verify_inputs.sh
python3 validate_patch.py > certificates/patch-validation.json
```

The first command mechanically rebuilds and checks the receipt-derived
manifest against the lane-owned `/tmp` source paths.  The second checks the
eight copied inputs, the twenty transitive inputs required by the pristine
engine, and the pristine-engine pin.

Pristine controls, run before any enlarged replay:

```bash
bash jobs/controls_fleet.sh
python3 validate_controls.py > certificates/control-validation.json
```

The validator requires the original `delta2` stage-4 constant generator
`stage4_J_d159_k35=6264` and the original `delta52` stage-8 constant generator
`stage8_G_local16_coord0=64`, both with exact-Q Singular unit confirmation.

Enlarged replays:

```bash
bash jobs/replays_fleet.sh
python3 analyze_results.py > certificates/replay-summary.json
```

`jobs/replays_fleet.sh` refuses to start unless the pristine control
certificate says `PASS`.  It runs cumulative stages 0--4 for `delta2` and
0--8 for `delta52` as isolated processes.  `run_one.sh` fixes deterministic
hashing and one thread per algebra process, enforces a timeout, and records
GNU-time, stderr, exit status, and UTC boundaries beside every JSON and
Singular script.

All linear elimination is `qstar_reduce` over `Q`: only nonzero rational
coefficients may pivot, and the localizers `rho` and `c` are excluded.  A
nonunit terminal chart is promotable to “gauge payment was load-bearing” only
when its `necessary_chart_rational_point` is `FOUND`; that certificate assigns
all free variables over `Q`, has nonzero localizer and nonzero `jet0`, and
checks every cumulative raw row exactly.  Failure of the bounded point search
is not a nonexistence proof.

`band_engine.patch` is the complete unified diff from the charged engine.
The final report classifies every changed hunk and records the fleet lifecycle,
polls, resource custody, and branch verdicts.
