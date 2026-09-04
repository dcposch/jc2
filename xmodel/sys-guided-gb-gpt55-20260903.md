# Systems Guided GB Helper Lane

Lane: `sys-guided-gb-gpt55-20260903`  
Date: 2026-09-04  
Verdict: **SHIPPED**

This lane built the shared compute unblock requested for later proof-frontier
lanes.  It did not attempt to prove any open mathematical claim.  The output is
a reusable guided Singular standard-basis helper plus a staged weighted-band
file emitter, both under `box/lib/`, with a passing regression log under
`box/sysguidedgb-20260903/`.

## 1. Input custody

The frozen input directory for this lane is:

```text
/tmp/jc2-lane.RZOERU/inputs
```

Before reading charged source material, I generated the checksum manifest
mechanically from `xmodel/sys-guided-gb-gpt55-20260903.run.v2` using the paired
`charged_input_<i>_basename=` and `charged_input_<i>_sha256=` lines and ran
`sha256sum -c`.  No hash was retyped into the command.

Result:

```text
/tmp/jc2-lane.RZOERU/inputs/FALLACY-v2.md: OK
/tmp/jc2-lane.RZOERU/inputs/controls.py: OK
/tmp/jc2-lane.RZOERU/inputs/descent_engine.py: OK
/tmp/jc2-lane.RZOERU/inputs/g108-delta3-kill-gate-gpt55-20260903.md: OK
/tmp/jc2-lane.RZOERU/inputs/k16-properness-gate-opus5-20260903.md: OK
/tmp/jc2-lane.RZOERU/inputs/k16-rank-criterion-fable5-20260903.md: OK
/tmp/jc2-lane.RZOERU/inputs/k16-square-tail-stdhilb-gpt55-20260903.md: OK
/tmp/jc2-lane.RZOERU/inputs/linear-free-cutoff43.sing: OK
/tmp/jc2-lane.RZOERU/inputs/order-basis-full-gpt55-20260903.md: OK
/tmp/jc2-lane.RZOERU/inputs/order_basis_full.py: OK
/tmp/jc2-lane.RZOERU/inputs/outer_order_bands.py: OK
/tmp/jc2-lane.RZOERU/inputs/validate.py: OK
```

The regression harness repeats this custody check and writes:

```text
box/sysguidedgb-20260903/charged_inputs.from_receipt.sha256
box/sysguidedgb-20260903/charged_inputs.sha256sum.log
```

## 2. Delivered files

Primary library files:

```text
box/lib/__init__.py
box/lib/guided_gb.py
box/lib/staged_band_emitter.py
box/lib/README.md
```

Regression and sealed evidence:

```text
box/sysguidedgb-20260903/run_tests.py
box/sysguidedgb-20260903/test.log
box/sysguidedgb-20260903/test-results.json
box/sysguidedgb-20260903/runs/
```

Artifact checksums at seal time:

```text
dc127b2f29405a4a9ec8077b7831d23a085f657d32dd161fe02fa6653ef46623  box/lib/__init__.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  box/lib/guided_gb.py
7c2f88430158fc01b2aa4e1bc2af1902f92168d10cd48ee5095506beb149dce8  box/lib/staged_band_emitter.py
35cddc81b2a88e48f21748741eccd421dbd22b198632867519bbb705da316117  box/lib/README.md
67c9aab1fa345a43715f4ca3baf17c26f74dcb333c70e591288f85f36a403b4f  box/sysguidedgb-20260903/run_tests.py
56251bef26548f7a1efd5c8080d76c5548e7d669d49b5f75b387ad6f2cd6594e  box/sysguidedgb-20260903/test.log
efe136f0ef5e6fcf900baccc801db87cbb63ed63244775feb7cc42ccc97d21c9  box/sysguidedgb-20260903/test-results.json
```

No ledger files, `jc2-lean` files, or `ideation-*` files were intentionally
edited by this lane.

## 3. Guided GB helper

`box/lib/guided_gb.py` exposes:

```python
SingularSystem
HilbertHint
PromotionPolicy
RunConfig
guided_groebner
prelude_from_script
crt_pair
crt_many
rational_reconstruct
```

The helper emits a standalone Singular script from a caller-supplied prelude
and generator list.  The prelude declares the ring and generator polynomials;
the helper appends its own ideal, `std` call, and control battery.

When a Hilbert hint is supplied, the emitted Singular call has the required
Card A shape:

```singular
ideal GG_G_main=std(GG_I_main,GG_HNUM_main,GG_WTS_main);
```

The helper always runs Singular through `stdbuf`:

```text
stdbuf -oL -eL Singular --cpus=<n> --threads=<n> --flint-threads=<n> --no-rc -q <script>
```

The certificate for both T1 and T2 records this exact command prefix.  Stdout
and stderr are streamed into files while the process runs, so marker output is
not held only in a block-buffered parent process.

Typed verdicts are:

```text
DIM0_CHAR0
UNIT_IDEAL_CHAR0
POSDIM
MODULAR_ONLY
INCONCLUSIVE_TIMEOUT
```

The mandatory controls in every accepted helper result are:

* `NF(generator_i,G)=0` for every submitted generator;
* `reduce(1,G)=0` recorded as the unit-ideal test;
* `dim(G)` and basis size recorded;
* `lead(G)`, `minbase(lead(G))`, and `std(minbase(lead(G)))` computed;
* `vdim(std(minbase(lead(G))))` compared with the predicted length when a
  predicted length is supplied;
* a perturbed Hilbert-series negative control run rejected when
  `RunConfig.run_perturbed_control=True`.

The perturbed control deliberately changes the Hilbert numerator and, when a
predicted length exists, the acceptance target.  This is stricter than simply
asking whether Singular can still recover the true basis from a poor hint: a
bad hint must not pass the bad certificate.

Parallel good-prime support is by passing multiple `SingularSystem` objects to
`guided_groebner`.  The runner uses a `ThreadPoolExecutor`, divides the
configured total core budget over active jobs, and stores per-prime/fibre
scripts and logs separately.  The certificate also records CRT plus bounded
rational-reconstruction data for small modular scalar invariants when at least
two modular runs are present.  The exported CRT functions are available for
future lanes that want to lift named modular scalar residues explicitly.

## 4. Promotion scope

The helper encodes FALLACY-v2's modular-promotion guard as an explicit
`PromotionPolicy`.  Modular evidence is not silently promoted.

The only modular promotion enabled by `PromotionPolicy.homogeneous_properness()`
is:

```text
homogeneous ideal + positive weights + accepted modular dim=0
  => DIM0_CHAR0
```

This is the properness scope from the charged `k16-properness` audit: for an
ideal generated by positive-weight homogeneous polynomials over the local base,
an empty projective special fibre, equivalently affine cone `{0}`, promotes to
the characteristic-zero dimension-zero cone conclusion.

Explicit non-promotions:

```text
modular dim > 0  => no characteristic-zero conclusion
modular unit     => no characteristic-zero unit conclusion by default
inhomogeneous modular unit => MODULAR_ONLY unless exact-Q evidence is supplied
```

Exact-Q computations may return `UNIT_IDEAL_CHAR0` directly when
`reduce(1,G)==0`.  T2 uses this exact-Q route for the D=108 stage-0 common-h3
unit replay.

## 5. Staged band emitter

`box/lib/staged_band_emitter.py` exposes:

```python
BandRow
BandEmitConfig
read_order_rows_tsv
emit_staged_band_files
emit_order_chart_bands
generator_checksum
```

The emitter consumes the `order_basis_full.py` row TSV format:

```text
source_index|h_power|x_power|y_power|expr
```

Rows are assigned to a staged band and weighted degree.  For the order-basis
regression, the grouping is `(h_power, x_power + y_power)`.  Each group is
written as a separate `.sing` file with the same ring declaration and only that
band's generators.  Shared localization generators, such as `T*(c)-1`, are
written once to `global_generators.sing`.

The manifest records:

```text
band file paths and SHA-256 hashes
per-band row counts and row labels
global-generator file hash
generator_union_checksum
monolithic_generator_checksum
union_equals_monolithic
```

The checksum is order-independent over labelled generator text.  This lets a
later solver consume completed band files incrementally and still verify that
the union is the same generator set as the monolithic ideal would have used.

## 6. Tests

Command:

```text
python3 box/sysguidedgb-20260903/run_tests.py
```

Environment:

```text
Singular 4.3.2 at /usr/bin/Singular
foreground Python harness
per-Singular timeout: 1800 seconds
total core budget: 4
```

Passing log:

```text
sysguidedgb regression run started
inputs START
INPUTS PASS: 12 charged inputs verified via box/sysguidedgb-20260903/charged_inputs.sha256sum.log
T1_card_a START
T1 t=5 PASS: both fibres DIM0_CHAR0, length=3640, perturbed controls failed, wall=3.03s
T1 t=6 PASS: both fibres DIM0_CHAR0, length=23256, perturbed controls failed, wall=103.88s
T2_g108_unit START
T2 PASS: D=108 stage-0 common-h3 exact-Q UNIT_IDEAL_CHAR0, wall=0.02s
T3_t2_negative START
T3 PASS: t=2,y=1/5 exact-Q POSDIM dim=1, wall=0.02s
T4_staged_emitter START
T4 PASS: staged (25,15) emitted 142 band files, rows=598, checksum=1c80dde35eff8a0b03f3e6803de549b5dd33626493c6dd9e5a35832d2b78a612, wall=2.93s
ALL TESTS PASS wall=111.33s
```

### T1: Card A controls

The harness used the banked Card A t=5/t=6 prelude scripts from
`box/k16stdhilb-20260903/`, cut before their old `TARGET_HNUM`, and reran the
systems through `box.lib.guided_gb`.  Both fibres were submitted for each `t`
with the predicted Hilbert numerator and positive-weight homogeneous
properness policy.

Results:

```text
t=5, b0/b1: DIM0_CHAR0, lead_vdim=3640, controls accepted
t=6, b0/b1: DIM0_CHAR0, lead_vdim=23256, controls accepted
perturbed runs: rejected for all four fibres
```

The T1 t=6 aggregate certificate states:

```text
DIM0_CHAR0
modular dimension zero promoted only for a homogeneous positive-weight ideal by the properness scope
accepted_run_count=2
command prefix: stdbuf -oL -eL Singular
```

### T2: D=108 stage-0 unit

The harness used the exact-Q common-h3 stage-0 replay prelude:

```text
box/g108gate-20260903/runs/delta3/stage0/death_replay.sing
```

Submitted generators:

```text
minor_n6_pi0
minor_n7_pi0
minor_n7_pi1
minor_n8_pi0
minor_n8_pi1
L
```

Result:

```text
UNIT_IDEAL_CHAR0
dimension=-1
basis_size=1
reduce(1,G)=0
stderr empty
```

This is exact over Q.  No modular unit promotion was used.

### T3: t=2, y=1/5 negative control

The harness replayed the exact-Q t=2, `y=1/5` full-cone negative control through
the helper without a Hilbert acceptance target.  It returned:

```text
POSDIM
dimension=1
unit=False
```

This confirms the helper does not type the discriminating boundary fibre as
dimension zero.

### T4: staged emitter

The harness used:

```text
box/orderbasis-20260903/meta/25_15_21_2_k2_part_3_full.json
box/orderbasis-20260903/rows/25_15_21_2_k2_part_3_full_rows.tsv
```

It emitted:

```text
142 band files under box/sysguidedgb-20260903/runs/T4_25_15_bands/
1 global generator file for T*(c)-1
598 row generators
```

The staged union checksum and monolithic generator-set checksum matched:

```text
1c80dde35eff8a0b03f3e6803de549b5dd33626493c6dd9e5a35832d2b78a612
```

So the staged files preserve exactly the same labelled generator set as the
monolithic ideal source, without writing a monolithic ideal file.

## 7. Seal

Machine artifact index:

```text
box/sysguidedgb-20260903/runs/T1_t5/
  T1_t5_b0_p1009.sing/.out/.err/.guided.json
  T1_t5_b1_p1009.sing/.out/.err/.guided.json
  guided_gb_result.json

box/sysguidedgb-20260903/runs/T1_t6/
  T1_t6_b0_p1009.sing/.out/.err/.guided.json
  T1_t6_b1_p1009.sing/.out/.err/.guided.json
  guided_gb_result.json

box/sysguidedgb-20260903/runs/T2_g108_unit/
  T2_g108_delta3_stage0_common_h3_Q.sing/.out/.err/.guided.json
  guided_gb_result.json

box/sysguidedgb-20260903/runs/T3_t2_negative/
  T3_t2_y1over5_negative_Q.sing/.out/.err/.guided.json
  guided_gb_result.json

box/sysguidedgb-20260903/runs/T4_25_15_bands/
  band_h*_d*.sing
  global_generators.sing
  bands-manifest.json
  bands-manifest.sha256
```

The generated T1 scripts are intentionally small wrappers around the banked
Card A polynomial prelude.  They do not alter the polynomial rows; they replace
only the old acceptance block with the reusable helper's marker protocol and
its independent perturbed-series run.  The T2 and T3 exact-Q scripts likewise
reuse banked prelude material and then apply the same typed control protocol.

The helper result JSON is deliberately redundant: each per-run
`.guided.json` stores the command, timings, stdout/stderr hashes, parsed
controls, and script hash; each aggregate `guided_gb_result.json` stores the
promotion policy, properness text, accepted-run count, Hilbert-hint digest, and
CRT/rational reconstruction section.  This is meant to make later lane failures
diagnosable without rerunning the expensive Singular foreground job.

The staged emitter manifest gives downstream solvers a durable resumption
point.  If a later computation is killed after finishing some bands, completed
band files remain valid independently, and their union can be rechecked against
the manifest checksum before resuming.

The deliverable is shipped.  Later lanes can import `box.lib.guided_gb` for
typed guided Singular runs and `box.lib.staged_band_emitter` for durable staged
band emission.  All requested tests passed in the foreground within the stated
limits.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12566`.
- Body SHA-256:
  `5f503cb8dfeb4e73f7d7e96b594455db5d35e7ccd26bf7ca536182aa66492115`.
- Frozen basis: `ed1a4fcc5e6146789c3b1ca3ec95cbac024d2dd0`.
