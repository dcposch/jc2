# Adoption of the (99,66) δ=2 long-solve worker: inputs regenerated, both solves launched

## Disposition

The Sol launch lane died before starting either solve. I adopted its worker,
found the input regeneration still running, let it finish, verified both
required input SHA-256 digests **exactly**, and launched the two detached
20-hour solves. Both run under the requested caps.

| job | solver | input SHA-256 | wall cap | memory cap | start (UTC) |
|---|---|---|---|---|---|
| `d2-z55-msolve` | patched msolve 0.10.1 | `7f593b87…b572` | 72,000 s | 400 GiB `RLIMIT_AS` | 08:25:46 |
| `d2-z55-singular` | Singular 4.3.2 `slimgb`, exact ℚ | `354b9293…ab7c` | 72,000 s | 200 GiB PGID RSS | 08:25:49 |

No mathematical claim is made or changed here. `d2-z55` is a literal
466-generator subset of the direct ideal, so a **unit is conclusive** for the
full ideal, while a nonunit basis or timeout has no properness force and
leaves the chart `OPEN`. A modular unit would be a signal only.

## 1. Frozen input custody

I built the nine-line manifest mechanically from the indexed
`charged_input_<i>_basename=` / `_sha256=` fields of the run receipt with
`awk`, then ran `sha256sum -c`. All nine returned `OK`; no mismatch. I used no
`ideation-*` input, made no ledger edit, did not use `jc2-lean`, and modified
no charged input.

## 2. Adoption inventory

The authorized worker `i-07e1212591a6acae9` (`172.30.0.63`, `r7i.16xlarge`,
64 CPU, 532,326,535,168 B RAM) was up with `PROVISION_DONE`. Its state at
adoption resolves the stated unknown:

- The patched msolve **had** been built and installed
  (`/tmp/msolve-patched/bin/msolve`, `toolchain/` logs at 08:03Z).
- The input regeneration **had** been started and was **still running**:
  `focused_selector.py --case 99-delta2 --face-z 55`, launched 08:01Z, at
  53.9 GB RSS and 99.9% CPU.
- **Neither solve had been started.** `runs/` held only build receipts; there
  was no `d2-z55-msolve` or `d2-z55-singular` directory and no solver process.

I did not reuse any unowned instance and started no second worker.

## 3. Regeneration and exact input verification

I let the running build finish rather than restarting it. It exited `rc 0`
with `build_wall_seconds` 1,184.095 and `peak_RSS_KiB` 89,535,620 — an
independent reproduction of the frozen 1,185.54 s / 89,535,404 KiB. Its
metadata reports 466 generators, 449 variables, 6,448,959 terms, and canonical
generator-sequence SHA `a78c6a46…44fe`. The emitted artifacts hash thus:

| file | bytes | SHA-256 | required | verdict |
|---|---:|---|---|---|
| `99-delta2.ms` | 271,944,646 | `7f593b87…b572` | `7f593b87…b572` | **EXACT** |
| `99-delta2.sing` | 357,263,333 | `a604ed31…cbbc` | frozen `std` base | **EXACT** |

The builder emits the `std` base, not the executed `slimgb` script. Per
frozen harvest §2 the two differ only in the sole `ideal G=…(I);` line; I
found exactly one occurrence, at line 472, and rewrote it:

```text
sed 's/^ideal G=std(I);$/ideal G=slimgb(I);/' 99-delta2.sing > 99-delta2-slimgb.sing
```

The result is 357,263,336 bytes (the frozen byte count, three more than the
`std` base as `slimgb` is three characters longer) and hashes to
`354b9293d065035f4e3b7ca2c918eb27cb5dc2ac3407eea2f02e9e467ba3ab7c` — the
required digest, **exact**. No stop condition arose.

## 4. Patched msolve

The predecessor's binary is `/tmp/msolve-patched/bin/msolve`, SHA-256
`da552c7c21d5339973fa6cc2157a171555af6d359ad7a4a392199702d5837530`, matching
the frozen harvest's `da552c7c…530`. Rather than trust the build logs I
checked the tree `/tmp/msolve-src-0101 @ 185e7b9`: exactly
`src/msolve/iofiles.c` and `src/neogb/io.c` are modified; the int64 patch's
four `(int64_t)` `store_exponent` casts and widened `int64_t pos` signature
are present; the heap patch's four `hm_t **phm = malloc(…)` and four
`free(phm);` are present with **zero** residual `hm_t *phm[len];` VLAs, and
its reverse dry-run applies cleanly. I therefore did not rebuild. Singular is
`/usr/bin/Singular`, SHA `90ab699b…46f4`, as in the frozen record.

## 5. Launch, caps, and custody

Both jobs were started with `setsid nohup … </dev/null &` through the staged
`run_longsolve.sh` (`a2e4779e…5ac2`) and `run_capped.py` (`4435279d…96c2`),
each into a fresh run directory with its own `TMPDIR`. The charged wrapper
`msolve_m5000_wrapper.sh` (`324f4e8c…f9b9`) was supplied as `MSOLVE_BIN`, so
the effective command is

```text
/tmp/msolve-patched/bin/msolve -m 5000 -g 2 -t 64 -v 2 --random-seed 0 \
  -f …/99-delta2.ms -o …/basis.ms
```

and, for the exact-ℚ side,

```text
/usr/bin/Singular -q --no-rc --no-warn --no-shell --threads=1 \
  --flint-threads=1 …/99-delta2-slimgb.sing
```

Each run directory carries a pre-execution `custody.txt` plus `caprun.json`,
`time.txt`, `limit.txt`, `runner.rc`, `postflight.sha256` on completion. Caps
are 72,000 s wall with 60 s TERM grace on both; `RLIMIT_AS`
429,496,729,600 B for msolve, verified in `/proc/self/limits` before `exec`;
sampled aggregate-PGID RSS 214,748,364,800 B for Singular. The recorded
`input_sha256` in each `custody.txt` is the required digest above.

Host custody is `box/t2t3-longsolve-20260906/custody.json` (7,133 B); the
worker was **not** terminated. Expected end ≈ 2026-09-07T04:25:46Z.

## 6. Running confirmation

Both jobs are confirmed running by `ps`, growing RSS, and live solver output.
No `runner.rc` exists in either run directory — this runner's completion
signal.

```text
  PID  ELAPSED   RSS(KiB) COMMAND   (worker clock 08:33:24Z)
20597    07:37   36892904 msolve
20637    07:34  104656596 Singular
```

Singular printed `ALL_ROWS_PARSED` then `BEGIN_STD` at 08:30:59Z, so all 466
generators parsed and the exact-ℚ `slimgb` is under way; its ~105 GB matches
the predecessor's ~108–111 GB plateau.

msolve emits its `-v 2` stream on **stderr**, not stdout. Its header confirms
the presentation independently of my hashes: 449 variables, 466 equations,
**0 invalid equations**, characteristic 1,073,741,827, DRL, max pair selection
5000, 64 threads. The first F4 rounds are

```text
deg  sel  pairs       mat         density  new data       time(rd) real|cpu
  2    5   2522      6 x 8        100.00%    2 new   3 zero    0.03 |    2.20
  3  208   2522   1602 x 6023       0.30%  167 new  41 zero    0.58 |   32.75
  3  606   4702   5864 x 29723      0.12%  368 new 238 zero    2.86 |  140.23
  3  275  13795   3458 x 19971      0.23%  248 new  27 zero    2.12 |   95.25
  4 5000  22214 216034 x 913997     0.01% 2489 new 2511 zero  68.92 | 1293.68
  3   79 102933   3012 x 35555      0.28%   53 new  26 zero    2.93 |   32.05
  4 5000 108090 235430 x 1469877    0.01% 2943 new 2057 zero 258.09 | 1836.23
  4 5000 323694  (round 8 selecting)
```

Every matrix dimension, density, and `new`/`zero` count reproduces the frozen
harvest's table exactly; only timings differ. This corroborates the byte-hash
match rather than substituting for it.

## 7. FALLACY-v2 typing and honest limits

This lane asserts no exit price and consumes none, so it carries no
`charge_basis` line. Three limits are stated rather than smoothed over:

- **Carrier/attainment.** Nothing here converts the pending chart into a
  result; the launch is custody, not evidence.
- **Compressed presentation.** The `slimgb` script is not a new presentation:
  it is the byte-identical `std` base with one solver call substituted, and
  the identity is discharged by the exact 357,263,336-byte / `354b9293…`
  match, not by analogy.
- **Co-run headroom (unmitigated).** Physical RAM is 495 GiB but the caps sum
  to 600 GiB; at the predecessor's 9,000 s stop the pair held ~111 and
  ~130 GB. Over a cap eight times longer the OOM killer could fire before
  either configured cap, and root has 22 GB free. I did not alter the caps,
  which are the lane specification; the harvest must read `runner.rc` and
  `caprun.json` to tell a cap stop from an OOM kill.

Local `df -h /` before writes: 96G/85G/12G, 88%. Host writes are this report
plus the 7,133-byte custody JSON, far below 2 MB.

LAUNCHED[(99,66) δ=2 long solve; harvest due ~+20 h]

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8151`.
- Body SHA-256:
  `db81480f272f58d14e8893058fcd7a67cda191910efdcc9a172852ee643dc0b6`.
- Frozen basis: `911f852ee1464f49879a82a0acce70a819a6e32c`.
