# K=7 b9 q0 decoupled long-solve launch

Lane `k7-b9q0-longsolve-opus5-20260906`; frozen input root
`/tmp/jc2-lane.FQCCMp/inputs`; machine record
`box/k7-b9q0-longsolve-20260906/custody.json`. This is a launch lane. It
states **no mathematical verdict** on b9 q0, which stays `STILL_SIGNAL_ONLY`
exactly as the frozen r3b custody left it. No ledger, `jc2-lean`, or
`ideation-*` file was read or written.

## Result

**LAUNCHED[b9 q0 long solve; harvest due ~+20 h]** — three capped exact
computations on a lane-owned `r7i.8xlarge`, started `2026-09-06T08:30:00Z`,
each with a 72,000-second wall and a 70 GiB RSS watchdog, expected to end by
`2026-09-07T04:30:00Z`. The worker is deliberately left running.

## 1. Frozen inputs

`awk` paired every numbered `charged_input_<i>_basename`/`_sha256` field in the
receipt into a manifest; `sha256sum -c` returned seven `OK` lines and no
mismatch. Host `/` before any write: 96 GiB total, 12 GiB available, 88% used;
unchanged after. Host writes are this report and the custody JSON (10,468 B).

## 2. Worker

The literal `sh ops/fleet/fleet.sh launch r7i.8xlarge` again failed in AWS
parameter validation before any instance was created — the frozen driver reads
the first positional as `COUNT` — so the documented explicit-count form was
used. One worker was created and provisioned:

```text
instance  i-0e5c65e66b8dc4dfc
private   172.30.0.73        public 18.232.84.6
type      r7i.8xlarge        32 vCPU, 247 GiB RAM, 23 GiB free disk
Owner     k7-b9q0-longsolve-20260906
launched  2026-09-06T08:22:17Z
```

Singular 4.3.2 binary SHA-256 is
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`,
identical to the r3b custody value. `fleet.sh wait` also installed msolve
0.10.1 (`c2722288d22c3a1eab00c0b818d0204d4a98104d059b2fd4ecb7343e8ef759fa`);
no launched job uses it. All lane files live under
`/home/ubuntu/k7-b9q0-longsolve`.

## 3. Chart regeneration and SHA verification

The chart was rebuilt from the recorded producer, not copied from any old
output:

```text
python3 box/k4ray-strata-solve-20260905/msolve_export.py 7 9 \
        --pin-index 0 --char 0 --outdir .../chart
```

`msolve_export.py` (`601d3089…`) imports `strata_prelude`/`extra_generators`
from `strata_chart.py` (`2fd608a3…`), which differs from the frozen producer
copy `box/k4ray-beta-strata-20260905/strata_chart.py` (`7f9d0610…`) in exactly
one line, the output-root assignment, as the charged gate report states. The
`box/lib/guided_gb.py` actually imported was the worker's `501f3b1f…`, i.e.
the version pinned in the producer's own `source-charts.sha256`; the host's
newer `95d12f5b…` was not used.

Formation took 71.79 s and printed `DUMP__N 241`, `DUMP__VARS 72`,
`PRE__HOMOG_I 1`, `PRE__HOMOG_CST 1`, `PRE__CST_ZERO 0`,
`PRE__THEOREM_SKIPPED disabled`, `PRE__LOCALIZER q0*q0_inv-1`. The emitted
bytes are

```text
K7_B9_Q0_p0.ms   12,675,213 B   72 vars / 241 gens
sha256 15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275
```

which is **exactly** the frozen r3b §2 chart SHA — byte-identical, so no
regeneration divergence and no need to stop. The emitted 72-weight vector was
compared elementwise against `r3-custody.json` `sources[0].weights` and is
equal.

The ring map is declared, not assumed. The `.ms` header names *are* the
Singular variable names; the builder asserts the header is literally
`v0,…,v71` in order, the characteristic line is `0`, there are 72 names and
241 rows, and row 241 is literally `v69*v71-1`. The chart coordinate is
`v69 = q0`, with `v70 = q1` and `v71 = q0_inv`.

## 4. The three launched jobs

`mkjobs.py` (`3388baaf…`) rebuilds each script from those verified bytes and
aborts on any assertion above. All three set `option(redSB)` and `short=0`,
print `CERT__NGEN`, and delimit the basis with a single
`CERT__GB_BEGIN`/`CERT__GB_END` pair followed by `CERT__GB_SIZE`,
`CERT__UNIT`, `CERT__DONE`.

| job | route | `job.sing` SHA-256 |
|:--|:--|:--|
| `a_slimgb_dp` | exact-Q `slimgb`, `dp`, full 241 rows | `308e6198…` |
| `b_std_wp` | exact-Q `std` under the frozen chart bigrading `wp` vector | `4435caf9…` |
| `c_tri_qv69_slimgb` | exact-Q(v69) triangular pre-reduction, then `slimgb` | `50dee169…` |

Job (b)'s order is the authoritative 72-entry positive `wp` vector frozen in
the strata metadata, not an invented block. Job (c) reproduces the route of
r2 §3 and r3b §5 literally: ring `(0,v69),(71 remaining vars),dp`, with source
rows 1,2,3,4,8,9,10,11 solving successively for `v6,v12,v35,v43,v5,v11,v16,v20`
— the exact rows and pivots those reports name. Each pivot prints its own
checks (`LINEAR`, `COEF_IS_FIELD`, `NONZERO`, `EXACT_DIV`, `ROW_VANISHES`,
`NO_PIVOT_LEFT`) so the harvest lane can audit exactness rather than trust it.

Before launch, parse-only truncations of all three ran to completion: (a) and
(b) returned rc 0 with `CERT__NGEN 241` and `CERT__PARSED 1`; (c) returned
rc 0 with `CERT__NPARS 1` and pivots 1–2 reporting every check `1`, the row
count falling 241 → 238 → 233.

## 5. Caps, detachment, confirmation

Each job runs `setsid nohup runner.sh <job> </dev/null`, which wraps
`/usr/bin/time -v` around
`timeout -s TERM --kill-after=120 72000 nice -n 4 Singular --no-rc -q job.sing`,
writing `stdout.txt`, `stderr.txt`, `time.txt`, `start.utc`, `end.utc` and
`runner.rc`. A per-job `watchdog.py` (`a724775f…`) polls the summed `VmRSS` of
the whole descendant tree every 15 s, records the peak into `caprun.json`
continuously, and `SIGKILL`s the tree above 73,400,320 KiB (70 GiB). Address
space is deliberately not limited, so RSS is the binding cap; three jobs at
the cap total 210 GiB against 247 GiB of RAM.

At `08:30:28Z`, after the launching SSH session had exited, all three Singular
processes and all three watchdogs were alive, each job had printed
`CERT__PARSED 1` with `CERT__NGEN 241`, and the worker had 23 GiB free disk.
At `08:32:17Z` all three were still running with no `runner.rc`, peak RSS
630 MiB / 1.78 GiB / 2.66 GiB and no RSS kill; job (c) had reduced to
`CERT__NGEN 220`.

## 6. Handoff and FALLACY-v2

The harvest lane must read, per job, `stdout.txt`, `stderr.txt`, `runner.rc`,
`time.txt`, `caprun.json`, `start.utc`, `end.utc`, `runner.log` and `job.sing`
under `/home/ubuntu/k7-b9q0-longsolve/runs/<job>/`, plus the chart and
`jobs-manifest.json`. Acceptance stays literal: exit 0, exactly one delimiter
pair, body bytes exactly `31 0a`, `CERT__GB_SIZE 1`, `CERT__UNIT 1`,
`CERT__DONE 1`. `rc=124` and `rss_killed: true` are resource walls and never
non-unit results; if `size(G) > 25` the delimited body holds lead terms only,
flagged `CERT__GB_LEADS_ONLY 1`, and is not a certificate. The worker is
**not** terminated here; the harvest lane terminates
`i-0e5c65e66b8dc4dfc` after checking its Owner tag.

Two things are declared rather than inferred. First, job (c) computes in the
localization `Q(v69)[rest]`: a unit there is a unit of the localization only,
and promoting it needs the r2 §3 step of clearing the `v69`-power denominators
and re-closing with the original Rabinowitsch generator `v69*v71-1` in the
source ring — a floor-to-attainment gap this lane does not cross. Second, no
modular or msolve signal is used anywhere; the existing msolve unit for this
chart remains a first-prime signal. No `sat()` wrapping, raw-remainder
shortcut, flag/place/series identification, pole identity, or merge/M-descent
step occurs. No exit-price assertion is made, so no `charge_basis` line applies.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7531`.
- Body SHA-256:
  `7b883610a24281654337b5e6ab41076fde126ad514aef9630301429821c82b94`.
- Frozen basis: `911f852ee1464f49879a82a0acce70a819a6e32c`.
