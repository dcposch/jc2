# Chart fix for the delta1'=0 two-point lane

Lane: `chart-fix-d1zero-gpt55-20260903`.  Date: 2026-09-03.
Frozen inputs: `/tmp/jc2-lane.BFzCan/inputs`.  Drivers and outputs:
`box/chartfix-20260903/`.

## 0. Manifest

MEASURED.  I generated the manifest mechanically from
`xmodel/chart-fix-d1zero-gpt55-20260903.run.v2` with `awk` over the
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines, then ran
`sha256sum -c`.  Result: all 20 frozen inputs returned `OK`.  No digit from the
prompt hash block was retyped into the manifest.

No ledger files were edited.  No `jc2-lean` command was run.  Existing unrelated
dirty/untracked workspace files and unrelated pre-existing processes were left
alone.

## 1. Generator fix

IMPLEMENTED in `box/chartfix-20260903/shape.py` and
`box/chartfix-20260903/twopoint_order_batch.py`.

The old `h` support test

```text
-i + delta1' j >= -delta1'
```

was replaced by the Theorem-1.2/root-count threshold

```text
B = V2' delta1' + u' delta2'
-i + delta1' j >= B.
```

For coefficient inventories the same rule is used at h-deficit `r`:

```text
-i + delta1' j >= r B.
```

The beta inventory also has the requested endpoint cap `deg_x beta <= k+1`.
This cap changes some inventory counts for nonzero-delta rows with `u'>=3`;
see section 3.

The batch now has a mandatory pre-saturation sanity gate for every emitted
system.  It computes the generic `x`-degree of `J` before writing/running a
Singular saturation.  If `deg_x J < k`, `build_system` returns
`INSTRUMENT-FAIL` and no Singular script is emitted.  For the delta1'=0 forced
A/B family, the gate uses the symbolic identity from the prior audit:

```text
f_2 = h_1^2,  g_3 = -h_1^3,
D(2,3,h_1^2,-h_1^3) = 0,
so deg_x J = 2 in that family.
```

This is the intended refusal: the three old A/B "kills" cannot reach `x^4`.

Driver hashes after the patch:

```text
ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de  shape.py
16497553047222b6b16450f26286a65dc69b27b4c00f8fcd518f0cce0af6c8e5  twopoint_order_batch.py
43747e4347c08ca77378ae0f33da6381e21479895f975df0a8a08e041e8387ac  gate_ode.py
bafa4f75ec07ce20d0569d687a5cd525f87e0d39f2bcc3630543f2b7f2dc6953  gate_sing.py
```

## 2. Controls

MEASURED.  Command shape:

```text
python3 box/chartfix-20260903/twopoint_order_batch.py --run \
  --mod-timeout 180 --exact-timeout 900 --exact-unknown-limit 36 \
  --only 16_12_13_3_k1,15_10_11_3_k2,15_10_11_2_k2,21_14_18_5_k1,\
28_20_25_3_k1,21_14_15_6_k4,24_16_18_7_k4,27_18_21_8_k4,\
33_22_30_8_k1,45_30_42_11_k1
```

All four Moh controls still return saturated `[1]` over the three primes and
over `Q`; both wrapper controls pass in every emitted Singular ring.

| row | old chart | corrected chart | sanity `deg_x J` | result |
|---|---:|---:|---:|---|
| `(16,12;13;3;k=1)` | 18 unk / 23 eq | 18 / 23 | 5 | 3 primes `[1]`, Q `[1]` |
| `(15,10;11;3;k=2)` | 13 / 22 | 13 / 22 | 4 | 3 primes `[1]`, Q `[1]` |
| `(15,10;11;2;k=2)` | 16 / 42 | 14 / 34 | 6 | 3 primes `[1]`, Q `[1]` |
| `(21,14;18;5;k=1)` | 16 / 31 | 16 / 31 | 4 | 3 primes `[1]`, Q `[1]` |

The only Moh-control chart that changed is `(15,10;11;2;k=2)`: the corrected
threshold is stricter there (`B=-1/3` instead of the old `-delta1'=-4/3`), and
the beta endpoint cap also applies.  The kill still persists in the corrected
emitted chart.

The promoted `(28,20;25;3;k=1)` replay was also rerun for the tally:
27 unknowns / 37 equations, sanity `deg_x J=9`, three primes `[1]`, Q `[1]`
with `basis_size=1`.

Actual-pair control:

```text
(f,g) = (pi, pi - gamma^2/2)
J = gamma
deg_x J = 1
monic in pi: true
tuple classifier: FAIL
```

DERIVED.  This confirms the wrapper is not an always-empty machine and that
the charged tuple classifier does not absorb this actual pair.

## 3. Support comparison on requested nonzero rows

MEASURED.  Old/new support was compared by importing the frozen `shape.py` and
the corrected copy.

| row | h support | beta inventory | emitted A/B chart | status |
|---|---|---|---|---|
| `(16,12;13;3;k=1)` | equal | equal | same K16 chart | `[1]` persists |
| `(15,10;11;3;k=2)` | equal | equal | same A/B chart | `[1]` persists |
| `(21,14;18;5;k=1)` | equal | equal | same A/B chart | `[1]` persists |
| `(33,22;30;8;k=1)` | equal | 33 -> 28 | A/B size remains 31 | COUNTING-BOUND |
| `(45,30;42;11;k=1)` | equal | 55 -> 40 | A/B size remains 48 | COUNTING-BOUND |

The last two are a change relative to the prompt's "kills persist" expectation:
the frozen charged batch report marks `(33,22)` as modular timeout/counting-bound
and `(45,30)` as pre-build count-only, not as `[1]` certificates.  I did not
promote them to kills here.  Their A/B chart sizes are unchanged because the
A/B ansatz does not consume `beta_all`, but the corrected beta inventory is not
a superset after the required `k+1` cap.

For the three delta1'=0 rows, the corrected supports are strict supersets of
the old broken supports:

| row | old/new h_all | old/new beta_all | old/new A/B unknowns | batch verdict |
|---|---:|---:|---:|---|
| `(21,14;15;6;k=4)` | 8 -> 15 | 7 -> 21 | 12 -> 18 | `INSTRUMENT-FAIL`, `deg_x J=2<4` |
| `(24,16;18;7;k=4)` | 9 -> 17 | 8 -> 24 | 13 -> 20 | `INSTRUMENT-FAIL`, `deg_x J=2<4` |
| `(27,18;21;8;k=4)` | 10 -> 19 | 9 -> 27 | 14 -> 22 | `INSTRUMENT-FAIL`, `deg_x J=2<4` |

## 4. R3 and honest-chart re-attack

Drivers patched/copied into `box/chartfix-20260903/`:

```text
gate_ode.py    R3 level-1 ODE scripts, std/slimgb, dp/elimination order
gate_sing.py   R2 honest chart scripts, std/slimgb/modStd hook, dp/elimination
```

The installed Singular is 4.3.2.  `slimgb` is available.  `modStd` is available
only after loading `modstd.lib`, but the exact `modStd` R3 run spawned a large
worker set, exceeding the two-core lane bound; I terminated that process tree
and do not count it as a verdict.

MEASURED R3/R2 runs:

| chart | char/alg/order | sanity | size | outcome |
|---|---|---|---:|---|
| R3 ODE | 32003 / slimgb / dp | `deg_x J=4` | 29 eq / 31 unk | TIMEOUT 1800.16s, maxrss 1855276 KB |
| R3 ODE | 32003 / slimgb / elim | `deg_x J=4` | 29 / 31 | TIMEOUT 1800.02s, maxrss 196320 KB |
| R3 ODE | Q / slimgb / elim | `deg_x J=4` | 29 / 31 | TIMEOUT 1800.06s, maxrss 338224 KB |
| R3 ODE | Q / modStd / dp | `deg_x J=4` | 29 / 31 | ABORTED[CORE-BOUND], no verdict |
| R2 honest | 32003 / slimgb / dp | `deg_x(f,g,J)=(2,3,4)` | 159 / 98 | TIMEOUT 1801.59s, maxrss 29773476 KB |

Every completed timed run reached its `MAIN_START` after controls and then
ended by timeout with Singular printing `halt 1`; no run printed `MAIN_DONE`.
Therefore there is no saturated-empty certificate and no survivor component
from which to extract dimension or a point.

The R3 run is the requested 31-unknown Moh Appendix-I level-1 chart
`D(21,14;p,q)=c` with degrees `(18,12)`.  Since it did not decide, it does not
re-kill any of the three delta1'=0 rows.

## 5. Per-row verdicts

| row | batch sanity | R3/R2 attack | verdict |
|---|---|---|---|
| `(21,14;15;6;k=4)` | A/B refused, `deg_x J=2<4` | R3 and R2 timed out | `COUNTING-BOUND` |
| `(24,16;18;7;k=4)` | A/B refused, `deg_x J=2<4` | common R3 gate timed out | `COUNTING-BOUND` |
| `(27,18;21;8;k=4)` | A/B refused, `deg_x J=2<4` | common R3 gate timed out | `COUNTING-BOUND` |

No `SATURATED-EMPTY` certificate was produced for these three rows.  No
`SURVIVES` representative is claimed; there was no `MAIN_NONTRIVIAL` output and
no point extraction.

Corrected row-entry tally for the 17-source/18-row list:

```text
SATURATED-EMPTY with corrected certificates: 5 / 18 rows
  (16,12;13;3;k=1), (15,10;11;2;k=2), (15,10;11;3;k=2),
  (21,14;18;5;k=1), (28,20;25;3;k=1)

delta1'=0 rows formerly killed by the bad A/B slice: 3 / 18
  all now COUNTING-BOUND after INSTRUMENT-FAIL plus R3/R2 timeouts

other COUNTING-BOUND row entries: 10 / 18
```

Equivalently at source-group granularity: 4 of 17 source groups have corrected
saturated-empty row certificates, 3 source groups are the delta1'=0 open/counting
rows, and 10 source groups remain count-bound.

## 6. FALLACY-v2 check

`sat()` wrapping: every emitted Singular ideal declares its coefficient field,
ring variables, and includes `T*c-1`.  Each emitted ring ran both controls:
`<c,T*c-1>` reduced to `[1]`, while `<c-1,T*c-1>` stayed nonunit.

Raw remainder degree: the corrected batch gate computes `deg_x J` before any
saturation.  R2 prints `deg_x(f,g,J)=(2,3,4)` before coefficient extraction and
standard-basis work.  R3 is level-1 only and declares `deg_x J=4` as the
coefficient chart being tested.

Variable/ring map: in the batch and R2/R3 scripts, `x=gamma`, `y=pi` except the
K16 branch names them `gamma,pi` directly.  Coefficients are over `Q` or
`GF(32003/32009/32027)` as stated in each script; variable names are not used as
proof of a map.

Carrier/attainment and floor/attainment: no representative, actual pair, or
attainment claim is made for the three delta1'=0 rows.  Runtime timeout is typed
only as `COUNTING-BOUND`.

Prime label/derivative: prime marks in row data are labels.  The derivatives in
the R3 ODE are ordinary `y` derivatives inside the declared univariate
coefficient chart.

No new exit-price assertion is made, so no `charge_basis` line is emitted.

## 7. Files

Primary outputs:

```text
box/chartfix-20260903/results.json
box/chartfix-20260903/summary.tsv
box/chartfix-20260903/systems/*.sing
box/chartfix-20260903/indep/*.sing
box/chartfix-20260903/indep/*.out
box/chartfix-20260903/indep/*.time
```

Result artifact hashes:

```text
1dc445beeb238cb8262077bf0fb34c65d1b9298f3cb27e322a56d2c5d5c34728  results.json
6a297a935c21d63031be9f29241d8d3834e236a9282fff22cbb6b45b1679caa4  summary.tsv
```

Typed close:

```text
MEASURED      frozen manifest 20/20 OK; controls passed; R3/R2 timeouts as listed.
IMPLEMENTED   Theorem-1.2 support threshold B and beta k+1 cap in chartfix copy.
IMPLEMENTED   pre-saturation sanity gate; delta1'=0 A/B charts now refuse.
MEASURED      four Moh controls and (28,20) replay remain saturated-empty [1].
MEASURED      R3/R2 did not decide; no survivor point exists from these runs.
OPEN          the three delta1'=0 rows remain COUNTING-BOUND, not kills.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10187`.
- Body SHA-256:
  `d33d31eb6e41c0bd1023ef19d7d03994069799cacfd1f107fd24a9801089cd2a`.
- Frozen basis: `2e255fc0a12925dd895193e1d0fa63e0c4cd8ad3`.
