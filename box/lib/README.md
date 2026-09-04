# Guided GB Helpers

This directory contains reusable helpers for compute-bound Singular jobs.

## `guided_gb.py`

Primary API:

```python
from pathlib import Path
from box.lib.guided_gb import (
    HilbertHint,
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)

system = SingularSystem(
    name="tail_t6_b0",
    prelude="ring R=1009,(b4,q2_0,q3_0,q4_0,q5_0,b3),wp(1,2,3,4,5,7);\n"
            "poly T6=...;\n",
    generators=("T6", "T7", "T8", "T9", "T10", "T11"),
    characteristic=1009,
    homogeneous=True,
    positive_weights=(1, 2, 3, 4, 5, 7),
)

hint = HilbertHint.from_sequences(
    numerator=(1, 0, 0, ...),
    weights=system.positive_weights,
    predicted_length=23256,
)

result = guided_groebner(
    system,
    hint=hint,
    policy=PromotionPolicy.homogeneous_properness(),
    config=RunConfig(Path("box/some-lane/runs"), timeout_seconds=1800, total_cores=4),
)
```

`guided_groebner()` emits a standalone `.sing` replay and runs Singular through
`stdbuf -oL -eL Singular ...`, with `--cpus`, `--threads`, and
`--flint-threads` capped from `RunConfig.total_cores`.  Stdout and stderr are
streamed to files while the process is alive so a killed job can still leave
completed marker output.

When a `HilbertHint` is supplied, the emitted Singular call is:

```singular
ideal G=std(I,GG_HNUM_main,GG_WTS_main);
```

The helper returns one of:

```text
DIM0_CHAR0
UNIT_IDEAL_CHAR0
POSDIM
MODULAR_ONLY
INCONCLUSIVE_TIMEOUT
```

No accepted result is returned unless the control markers pass:

* every input generator has normal form zero against `G`;
* `dim(G)` is recorded;
* `lead(G)` is minimized and `vdim(std(minbase(lead(G))))` is checked against
  the predicted length when a length is supplied;
* a perturbed Hilbert-series run is rejected when `RunConfig.run_perturbed_control`
  is true.

The certificate JSON records every script/stdout/stderr path and hash, the
typed promotion policy, control values, and CRT/rational-reconstruction data
for small modular scalar invariants.  The CRT helpers are exported as
`crt_pair`, `crt_many`, and `rational_reconstruct`.

### Properness Scope

Modular promotion is deliberately narrow.  A modular dimension-zero result is
promoted to `DIM0_CHAR0` only when the caller declares:

```python
SingularSystem(..., homogeneous=True, positive_weights=(...))
PromotionPolicy.homogeneous_properness()
```

This encodes the properness lemma scope: for an ideal homogeneous in positive
weights, a closed special fibre whose affine cone is `{0}` gives the same
dimension-zero cone conclusion in characteristic zero.  A modular `dim > 0`
does not prove a characteristic-zero positive-dimensional result, and a
modular unit ideal is not promoted by default.  Exact-Q computations may return
`UNIT_IDEAL_CHAR0` directly when `reduce(1,G)==0`.

## `staged_band_emitter.py`

Primary API:

```python
from pathlib import Path
from box.lib.staged_band_emitter import emit_order_chart_bands

manifest = emit_order_chart_bands(
    Path("box/orderbasis-20260903/meta/25_15_21_2_k2_part_3_full.json"),
    Path("box/some-lane/bands"),
    characteristic=0,
    band_column="h_power",
    include_saturation=True,
)
```

The emitter reads the `order_basis_full.py` row TSV format and writes one
Singular file per `(band, weighted_degree)` pair.  It also writes a separate
`global_generators.sing` for shared localization generators such as
`T*(c)-1`.  The manifest records:

* band file paths and hashes;
* per-band row counts and labels;
* an order-independent checksum of the union of all emitted generators;
* the matching monolithic generator-set checksum.

This lets later solver lanes process completed bands incrementally without
depending on a single large monolithic ideal file.

## Regression Log

The required regression suite is:

```bash
python3 box/sysguidedgb-20260903/run_tests.py
```

The passing log is `box/sysguidedgb-20260903/test.log`, and detailed machine
results are in `box/sysguidedgb-20260903/test-results.json`.

