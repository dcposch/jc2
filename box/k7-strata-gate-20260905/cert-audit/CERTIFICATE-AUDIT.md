# K=7, b=9..13 exact-Q certificate audit

Status: **all ten fresh chart inputs returned the literal reduced basis `[1]`
under both independently packaged msolve builds.** In addition, exact rational
cofactor identities were produced and directly multiplied out in Singular for
three charts: `K7_B13_Q0`, `K7_B13_Q1`, and `K7_B12_Q1`.

## Input and engine custody

The receipt-derived charged-input manifest is `charged-inputs.sha256`; its
mechanical `sha256sum -c` transcript is `charged-inputs.sha256.check` and says
`OK` for all seven inputs. The receipt SHA-256 is recorded in
`receipt.sha256`.

The ten inputs are the fresh files in `../chart-audit/emitted`. The chart audit
independently rebuilt them and its `structure-audit.json` (SHA-256
`008dceb7a026ec8bdd19bf1620d6687a6377e36904b4edfff6b336f3b43bb948`)
records a byte-for-byte match to all ten producer files. Each input begins with
the emitted variable order and characteristic `0`; the following rows are the
Singular-denominator-cleared integral generators in their original order.

Two separately packaged binaries were used:

- official upstream static msolve 0.10.1, SHA-256
  `0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`;
- Ubuntu msolve 0.6.5-1build2 extracted in isolation, binary SHA-256
  `c2722288d22c3a1eab00c0b818d0204d4a98104d059b2fd4ecb7343e8ef759fa`
  and package SHA-256
  `dbbca584ac7518ed3924e5614a5b83ace6f89de6ab561ca63b336499fb3f575d`.

The independent CAS used for cofactors and attempted full standard bases was
Singular 4.3.2, binary SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
Every Singular ring has coefficient field Q and every standard-basis/lift run
sets `option(redSB)`. See `engine-provenance.txt`.

## Exact-Q results

Each displayed solver output has rc 0 and its **entire non-comment,
whitespace-normalized basis body** is exactly `[1]:`; the classifier does not
infer unit status from basis length. All times are wall time and all memory
figures are maximum RSS in KiB.

| chart | nv/ng | fresh input SHA-256 | msolve 0.6.5 wall / peak KiB | msolve 0.10.1 wall / peak KiB |
|---|---:|---|---:|---:|
| K7_B9_Q0 | 72/241 | `15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275` | 23:03.20 / 34889000 | 16:53.78 / 34823016 |
| K7_B9_Q1 | 71/235 | `09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934` | 6:18.90 / 6370624 | 1:59.46 / 6353460 |
| K7_B10_Q0 | 79/261 | `273a1a0f65308af6019c3b8986fa921c76d4e27da30d0b675afc532bc3f3d434` | 0:16.97 / 1568980 | 0:15.69 / 1540656 |
| K7_B10_Q1 | 78/255 | `a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d` | 1:09.10 / 1726684 | 0:19.82 / 1700900 |
| K7_B11_Q0 | 86/281 | `e8e57139c2292f0535226e7fb8fc2fac90b459685e939b825abec31531b2367e` | 0:13.70 / 1616332 | 0:13.02 / 1578388 |
| K7_B11_Q1 | 85/275 | `42f96a5f916e94457887e933cb8cb3f8656537e1547e719e30851075990fd4f1` | 0:11.28 / 1366748 | 0:10.71 / 1330156 |
| K7_B12_Q0 | 93/301 | `3a3821db1511fa96096f627d5d5ed23b1b60a2c95022f33dfb90791a4c60561d` | 0:04.52 / 1347332 | 0:04.00 / 1294164 |
| K7_B12_Q1 | 92/295 | `875573726b784dc4700de3835f0130617279eb5bab451f712f77088c26cae4e2` | 0:04.04 / 1220692 | 0:03.63 / 1171284 |
| K7_B13_Q0 | 100/325 | `970026efbf5ffd1150def477d64de057b8212455527a15f6abbf18807d5cce2c` | 0:05.93 / 1785936 | 0:05.15 / 1717588 |
| K7_B13_Q1 | 99/317 | `570e241e4e2515d1c97c77f9b7696e5d519fb97697543da93410ca5eb2797a8b` | 0:05.56 / 1689276 | 0:04.78 / 1622864 |

Machine-readable records, including result-file hashes and rc values, are in
`results-summary.json`; its generating classifier is
`summarize_results.py`. Thus there are 20/20 successful literal-unit rows,
covering every requested chart with two binary builds.

The duplicate local two-thread 0.6.5 attempt on `B9/Q0` hit its exact
2400-second watchdog (rc 124, empty output). It is retained as
`results/K7_B9_Q0_msolve065_local_t2_timeout.*`. It is not consumed: the
separately executed eight-thread 0.6.5 run completed within budget in 23:03.20,
and the separate 0.10.1 run completed in 16:53.78. This is the explicit
second-build fallback requested by the gate.

## Explicit exact-Q cofactor identities

All generator numbers below are one-based positions in the complete fresh
integral generator list, including the final cover localizer.

### K7_B13_Q1

Only generators 1 and 317 have nonzero cofactors. They are
`g1=v97^3` and `g317=v97*v98-1`, and Singular produced and checked

```
v98^3*g1 + (-v97^2*v98^2-v97*v98-1)*g317 = 1.
```

The full 317-entry `liftstd` column, with zeros printed at every omitted
position, is `lifts/K7_B13_Q1_lift_indexed.out`; it reports `UNIT=1` and
`DIRECT_CHECK=1` (29.33 s, 2207476 KiB). The compact independent multiplication
is `lifts/K7_B13_Q1_sparse_identity.sing/.out` and also reports value exactly
1. Full-source SHA-256:
`570e241e4e2515d1c97c77f9b7696e5d519fb97697543da93410ca5eb2797a8b`.

### K7_B13_Q0

Only generators 2, 8, and 325 have nonzero cofactors:

```
g2   = v97^3-3*v97^2*v98
g8   = 106*v97^3-143*v97^2*v98
g325 = v97*v99-1

(-143/175*v99^3)*g2 + (3/175*v99^3)*g8
  + (-v97^2*v99^2-v97*v99-1)*g325 = 1.
```

The full 325-entry exact-Q `liftstd` column is
`lifts/K7_B13_Q0_lift_indexed.out`; it reports `UNIT=1` and
`DIRECT_CHECK=1` (29.48 s, 2324612 KiB). The compact direct multiplication is
`lifts/K7_B13_Q0_sparse_identity.sing/.out`. Full-source SHA-256:
`970026efbf5ffd1150def477d64de057b8212455527a15f6abbf18807d5cce2c`.

### K7_B12_Q1

A deterministic deletion search retained the exact full-source indices
`S={12,13,15,17,18,295}`. Its custody chain is:

```
full 295 generators, SHA 875573726b784dc4700de3835f0130617279eb5bab451f712f77088c26cae4e2
 -> 122 generators, SHA 98bb81c8984f613af649310edee31da002f542113825070ac16cb5d3c1d732d9
 -> 6 generators, SHA 13573e732ffa4c0dfb555d9f5fd566a41f48a1b07f9a20da19fe98e10c41b228
```

The first five retained generators were lifted over the exact rational
function field Q(`v90`). After normalizing the singleton constant basis, direct
multiplication returned 1. Clearing the largest denominator power gives
explicit polynomial cofactors `c_i` printed in full in
`lifts/K7_B12_Q1_core_localized_clear25.out` with

```
sum(i in {12,13,15,17,18}, c_i*g_i) = v90^25.
```

Generator 295 is the original localizer `g295=v90*v91-1`. Therefore a full
polynomial-ring identity is

```
v91^25 * sum(c_i*g_i)
 - (sum(k=0..24, (v90*v91)^k))*g295 = 1.
```

This is not merely a localization inference. The 3.0 MiB file
`lifts/K7_B12_Q1_core_polynomial_check.sing` contains all six explicit
polynomial cofactors and the six original generators, forms `matrix(I)*T`, and
checks the result in Q[`v6,v12,v17,v21,v24,v26,v38,v49,v59,v68,v76,v90,v91`].
The first run and a separate rerun both report
`DIRECT_CHECK_POLYNOMIAL=1`, `CHECK_VALUE=1`; the rerun took 0.67 s and 31636
KiB. The localized lift itself took 2.14 s and 48660 KiB.

## Controls and incomplete Singular attempts

Both msolve builds returned `[1]` on `controls/unit_p0.ms`; both returned the
two-polynomial nonunit basis on `controls/nonunit_p0.ms`; and both returned a
**one-element but nonunit** basis on `controls/nonunit_length1_p0.ms`. The last
control specifically checks that basis length one is not confused with basis
content `[1]`.

Full Singular `std` over Q was attempted on B9--B12 using syntax-only
translations of the identical generators. Those eight processes were
resource-preempted, before the 40-minute chart cap, to protect the concurrent
B8 negative control and then to reserve memory for cofactor generation. No
partial output is treated as a verdict. B13's two full exact-Q `liftstd` runs
did complete; B12/Q1 has the stronger checked identity above. The exact
preemption wall times, peak RSS, rc values, and reasons are in
`preemption-ledger.tsv`.

The gate's permitted fallback is therefore explicit: for charts without a
completed Singular basis, consume the fresh-input characteristic-zero `[1]`
from the official 0.10.1 execution together with the independent Ubuntu 0.6.5
execution. All 20 such executions completed successfully; none timed out or
returned a nonunit basis. The one duplicate timeout is retained but superseded
as described above.

## Reproduction

The conversion and checking scripts are `make_singular.py`,
`summarize_results.py`, and `run_remote.sh`. Representative commands are:

```
python3 cert-audit/summarize_results.py > cert-audit/results-summary.json
msolve -g 2 -t 8 -f chart-audit/emitted/K7_B10_Q0_p0.ms -o result.out
Singular --no-rc -q cert-audit/lifts/K7_B13_Q0_lift_indexed.sing
Singular --no-rc -q cert-audit/lifts/K7_B12_Q1_core_polynomial_check.sing
```

At closeout there are no local or fleet processes belonging to this audit.
The fleet worker is termination-safe; termination remains with the root gate
agent that launched it.
