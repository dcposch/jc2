# k=4-ray β-strata, round 2 — the wall moved from memory to F4 degree 6/7; K=8 and K=9 still 0-closed

Lane `k4ray-strata-r2-opus5-20260905`. Adapter Opus 5.
Drivers: `box/k4ray-strata-r2-20260905/`. No ledger edit, no `jc2-lean`, no `ideation-*`.

**VERDICT (headline).** Round 1's charts were reused byte-for-byte and re-solved
on three `r7i.16xlarge` (64 vCPU / 495 GiB) under a **400 GB address-space cap**
instead of round 1's 24 GiB — the cap that was round 1's dominant failure mode
(twelve charts died `MSOLVE_RC_-11`). **Round 2 recorded zero SIGSEGVs.** Memory
is no longer the wall, and removing it did **not** decide a single additional
`K=8` or `K=9` stratum. The wall is now measured exactly: msolve's F4 stalls at
**degree 6–7** on Macaulay matrices up to **3,858,207 × 8,907,561**
(`K=8 b=10 q1`), and no chart whose largest F4 matrix exceeded ≈1.5 M rows
finished inside any budget this lane could give it.

```text
K=8 no-split row DEAD for ALL deg β?    NO.  0 of 9 strata closed.
K=9 case (A) DEAD for all deg β?        NO.  0 of 10 strata closed.
D=108 no-split arm restored?            NO — still conditional on deg β = b_min = 6.
(99,66) configuration (A) restored?     NO — still conditional on deg β = b_min = 7.
K=7 (task 3, b = 6,7,8):                3 cover charts exact-Q; 0 strata closed.
```

**No chart anywhere returned a NONUNIT basis, in any characteristic, under any
linear-algebra variant.** There is no necessary-chart survivor to report loudly
and no sample point to publish; every negative entry below is a named engine
limit. Modular units are screens and are never promoted (FALLACY-v2). No new
exit-price assertion is made, so no `charge_basis=` line.

## 0. Custody

The manifest was built mechanically from
`xmodel/k4ray-strata-r2-opus5-20260905.run.v2` by joining its numbered
`charged_input_<i>_sha256` / `_basename` lines with `awk` and prefixing
`lane_inputs_dir=/tmp/jc2-lane.rzFqAw/inputs`; no digest was retyped.
`sha256sum -c` returned **5/5 OK** (`frozen-inputs.sha256`, `.check.log` in the
driver dir). No content mismatch.

**Chart reuse is byte-exact, and machine-checked.** `strata_chart.py` is round
1's file unmodified (`2fd608a3238e4520…`, identical hash on all three workers);
`strata_prelude` / `extra_generators` are imported from it, not re-implemented.
Control: the round-2 emitter's char-0 generator file for the banked `K=7 b=5 q0`
chart hashes to `7d9f8b62ba8fd654…`, **exactly** round 1's recorded `ms_sha256`
for `K7_B5_Q0_p0.ms`. Same ideal, same generators, same order — only the engine
schedule changed.

Repo reads were read-only at basis `6aa1cf4a`. Writes:
`box/k4ray-strata-r2-20260905/` and this report. Fleet: three `r7i.16xlarge`
(64 vCPU / 495 GiB) launched by this lane with
`Owner=k4ray-strata-r2-opus5-20260905`, msolve **0.10.1** installed by
`fleet.sh wait`; these three and no others are the instances it terminates (§9).

## 1. What round 2 changed (engine only)

1. **One formation per chart, not two.** Round 1 formed separately for char 0 and
   char 32003 and measured the cost as char-independent (`K7 b13 q0`: 2713 s vs
   2130 s). Round 2 forms once **over Q** with `cleardenom` (integral primitive
   generators) and writes two msolve files with an identical body, differing only
   in the characteristic header. The screen is therefore literally the reduction
   mod `p` of the exact-Q input: half the formation work, no provenance gap.
2. **400 GB address space, `-t 32`.** Round 1's `ulimit -v 24 GiB` produced
   twelve `MSOLVE_RC_-11`.
3. **Measurement.** Every msolve run is wrapped in `/usr/bin/time -v` and `-v 2`,
   so peak RSS, F4 degree and largest Macaulay matrix are recorded, not guessed.
4. **Phase 2: exact-Q first.** When a modular screen hit its wall clock the
   chart was re-queued on its already-emitted `.ms` — no re-formation —
   **directly over Q**, since the screen is optional and only the exact-Q `[1]`
   certifies. A probabilistic-LA screen (`msolve -l 42`) ran alongside on the two
   bottom-of-band `K=8`/`K=9` pairs; it is a screen twice over, never promoted,
   and returned no verdict inside the window.

## 2. Dispatch

44 charts (all 22 open strata × 2 covers) were launched detached (`setsid
nohup … </dev/null`) at **18:15:55Z**, 6 min 48 s after lane start, with
160-minute outer watchdogs, a 5100 s Singular formation cap and a 2700 s msolve
cap per branch; 13 phase-2 jobs at 19:07:46Z and 8 more through 20:38Z. Polling
every 15 min (`poll.log`, `status-*.tsv`, `health-*.txt`).

K=8 was dispatched first and K=9 second, per the task. The deep tail of each band
(`K=8 b≥12`, `K=9 b≥11`, every one a `FORMATION_TIMEOUT` at 8700 s in round 1)
was launched `nice -n 19` under a 40 GB cap as re-confirmation only, and its
`K=9 b≥13` half was killed at 19:54Z to relieve memory — declared, not hidden.

## 3. The measured wall: F4 degree 6–7, not memory

This is the substantive result of the lane. `msolve -v 2` records every F4
Macaulay matrix; `f4deg.tsv` holds the max degree reached and the largest matrix
built, per chart.

```text
chart              maxF4deg   largest F4 matrix        outcome
K7 b=6 q1              6        292,502 x   484,251    EXACTQ_UNIT   153 s
K7 b=7 q0              6        568,750 x 1,108,487    EXACTQ_UNIT   473 s
K7 b=8 q0              6      1,188,472 x 2,047,062    EXACTQ_UNIT   712 s
K7 b=7 q1              6      1,500,429 x 2,258,156    wall clock
K7 b=8 q1              6      2,326,667 x 2,845,023    killed (memory pressure)
K8 b=7 q1              7      3,489,356 x 6,934,296    wall clock
K8 b=9 q1              7      3,653,033 x 7,498,305    wall clock
K8 b=10 q1             7      3,858,207 x 8,907,561    wall clock
K9 b=8 q0              7      3,055,664 x 4,116,239    wall clock (then preempted)
K8 b=7/8/9 q0, K9 b=8 q1, K9 b=9 q0/q1
                       6      0.23 M - 0.49 M rows     wall clock
```

Three consequences, each load-bearing for the next round.

* **Memory is solved and it was not the problem.** Peak RSS of the *completed*
  runs is 25.4 GB (`K7 b=8 q0`, exact Q); the largest live msolve resident set
  was **66.6 GB**, against a 400 GB cap and 495 GB of RAM. Round 1's twelve
  SIGSEGVs were an artefact of its 24 GiB cap.
* **The `b`-monotonicity from round 1 does not survive at `K=8`.** Round 1
  concluded "the band is hardest at the bottom" from `K=7`, where msolve time
  fell from 258 s at `b=b_min+1` to 5 s at `b=b_min+7`. At `K=8` the largest
  matrix *grows* with `b` on the `q1` cover (6.9 M → 7.5 M → 8.9 M columns at
  `b = 7, 9, 10`) and all of `b = 7…10` stalled. That extrapolation should not be
  carried across `K`.
* **Degree 7 is the cliff.** Every chart that finished did so at degree 6 with
  under 1.2 M rows; every chart that reached degree 7 built 3–3.9 M rows by
  4–8.9 M columns and did not finish in 2700–5100 s on 32 threads. The leverage
  is a chart with a smaller degree-7 step, not a bigger machine.

## 4. Controls (FALLACY-v2)

```text
POSITIVE, chart identity  K=7 b=5 q0 emitted char-0 .ms sha 7d9f8b62... ==
                          round 1's recorded ms_sha256, byte for byte
POSITIVE, full pipeline   K=7 b=5 q0 -> MODULAR_UNIT 0.23 s -> EXACTQ_UNIT
                          0.14 s, peak RSS 33 MB, basis length 1
PRELUDE, every chart      PRE__HOMOG_I 1, PRE__HOMOG_CST 1, PRE__CST_ZERO 0,
                          TARGET_FOUND 1 (weighted-homogeneous row block, and a
                          non-vacuous target, machine-checked)
NEGATIVE (round 1)        (v0*v1-v2^2) -> NONUNIT at basis length 1: the
                          classifier keys on CONTENT, not on basis length
```

`sat()` is not used; the Rabinowitsch generators `CSTP-1` and `q_j q_j_inv - 1`
are in every chart (`extras` field of every payload); no `q_j = 1` slice was
used. Ring map, unchanged from round 1 and re-declared: `RR = Q[x,y,params]`
with `dp`; `SS = Q[params]` with `wp(K-i-j | 2K-i-j | 2K-b | 1)`;
`ROWS = imap(RR,I0)`, `CSTP = imap(RR,CST)`; msolve aliases
`h_i_j, B_i_j, q_j, q_j_inv -> v0..v_{n-1}` by one longest-first regex over the
declared name list.
## 5. Results — all 22 open strata, both covers

`Q-UNIT` = msolve `-g 2` reduced basis **over Q** equal to `[1]` on the
denominator-cleared integral generators (the certificate); `p-UNIT` = the same
over `F_32003` (a screen, never promoted); `MS-TO` = msolve wall-clock cap;
`MS-RC` = killed by a signal; `FORM-TO` = Singular formation cap. A stratum is
`DEAD over Q` only when **both** covers are `Q-UNIT`.

```text
K=7 b=6   q0 MS-TO      q1 Q-UNIT     partial (one cover exact-Q)
K=7 b=7   q0 Q-UNIT     q1 MS-TO      partial
K=7 b=8   q0 Q-UNIT     q1 MS-RC 137  partial
K=8 b=11  q0 Q-UNIT     q1 MS-TO      partial  <-- NEW, first K=8 above b_min
K=8 b=7,8,9,10          both covers MS-TO                        UNDECIDED
K=8 b=12..15            FORM-TO except b=12 q1 (formed, MS-TO)   UNDECIDED
K=9 b=8                 both covers MS-RC -9 (lane preemption)   UNDECIDED
K=9 b=9                 both covers MS-TO                        UNDECIDED
K=9 b=10                q0 FORM-TO 5100 s, q1 MS-TO              UNDECIDED
K=9 b=11..17            both covers not reached                  UNDECIDED
```

Per-chart record (`nv` GB variables, `ng` generators; one formation per chart,
over Q; walls in seconds; `TO` = wall-clock cap):

```text
chart        nv   ng    form       mod p         exact Q
K7 b=6  q1   50  174     0.3   UNIT   145.1   UNIT    152.9
K7 b=7  q0   58  200     3.9   UNIT   407.6   UNIT    472.9
K7 b=8  q0   65  221    22.7   UNIT   588.8   UNIT    712.0
K8 b=11 q0   98  336  4142.8   UNIT  1081.2   UNIT   1257.4  <-- new, first K=8 > b_min
K7 b=6  q0   51  180     0.5   RC137 4300.7   TO     5100
K7 b=7  q1   57  194     3.0   TO    5100     TO     5100
K7 b=8  q1   64  215    16.6   RC137 3212     RC137  3864
K8 b=7  q0/q1  66/65 243/237    5.7/3.0     TO 2700  TO 5100 (both)
K8 b=8  q0/q1  74/73 266/260   90.1/63.5    TO 2700  TO 5100 (both)
K8 b=9  q0/q1  82/81 290/284  427.1/309.9   TO 2700  RC137 3844 / TO 5100
K8 b=10 q0/q1  90/89 313/307 1550.9/1257.6  TO 2700  not reached
K8 b=11 q1     97   330     3492.7          TO 2700  TO 1800, then TO 1320
K8 b=12 q1     106  353     6985.7          TO 1200  not reached
K9 b=8  q0/q1  83/82 316/310  115.6/59.3    TO 2700  RC-9 3614 / 3612
K9 b=9  q0/q1  92/91 342/336 1402.3/903.7   TO 2700  TO 4300 (q1 only)
K9 b=10 q1     100  363     4579.5          TO 2700  not reached
K8 b=12 q0, b=13 q0/q1, K9 b=10 q0, b=11 q0/q1: FORMATION_TIMEOUT (5100-8000 s)
```

**22 of 44 charts were emitted**, and formation is genuinely cheaper with
contention relieved: `K=9 b=10 q1` formed in **4580 s** where round 1 recorded
6177 s and a timeout, and **`K=8 b=12 q1` formed at all** (6986 s), which round 1
never achieved. `K=9 b=10 q0` hit this lane's **5100 s** primary formation cap —
tighter than round 1's 8700 s, chosen to fit a 200-minute lane, and that cap, not
the chart, is its stated cause.

**Three entries are lane-inflicted, and are declared.** `K=7 b=8 q1` and
`K=8 b=9 q0` returned `rc 137` (3212–3864 s) on workers that reached 448–453 GB
of 495 GB; no kernel OOM record was found, so these are recorded as "killed under
memory pressure, cause not established", not as verdicts. `K=9 b=8 q0/q1` were
**killed by this lane at 20:08Z** (`rc -9`, 3612 s) to free ~154 GB for the
`K=8 b=11 q1` exact-Q run; both had reached degree 7 with a 3.06 M x 4.12 M matrix
and were the least likely live jobs to converge. The `K=9 b≥13` deep-tail
formations were killed at 19:54Z for the same reason. Resource decisions, not
results.

## 6. Verdict (task 5)

```text
K=8: DEAD for all deg beta?  NO. 0 of 9 closed over Q. Surviving: b = 7..15 (all).
  b=7,8,9,10  msolve F4 wall clock (2700 s screen, then 5100 s exact-Q); the q1
              covers of b=7,9,10 reached degree 7 with 3.5-3.9 M row matrices
  b=11        q0 CLOSED over Q in 1257 s; q1 is the only chart in the lane that
              is one run short (2700 s modular, then 1800 s exact-Q, both wall
              clock, on a chart whose sibling needed 1257 s)
  b=12..15    Singular formation (8000 s cap). b=12 q1 formed at 6986 s - the
              first time any of these thirteen has - then hit a 1200 s msolve cap
K=9: DEAD for all deg beta?  NO. 0 of 10 closed. Surviving: b = 8..17 (all).
  b=8         degree 7, 3.06 M x 4.12 M; preempted by this lane at 3612 s
  b=9         msolve F4 wall clock (2700 s, then 4300 s exact-Q on q1)
  b=10        q0 formation cap 5100 s; q1 formed at 4580 s, msolve wall clock
  b=11..17    formation; round 1 measured 8700 s
K=7 (task 3): b=6,7,8 all partial, one exact-Q cover each (b=6 q1, b=7 q0,
  b=8 q0). With round 1's b=9..13 the K=7 row has 5 strata DEAD over Q and 3
  with exactly one certified cover.
```

**Nothing is promoted from a modular unit.** The lane's only new exact-Q facts
are four cover charts: `K=7 b=6 q1`, `b=7 q0`, `b=8 q0` and `K=8 b=11 q0`. The
first three re-certify round 1 covers (`b=6 q1` was modular only there) on a
second, independent schedule; **`K=8 b=11 q0` is new** — the first
characteristic-zero `[1]` for any `K=8` chart strictly above `b_min`, where round
1 had only a modular screen. It does **not** close `K=8 b=11`: the cover
`{q0=0, q1≠0}` is undecided, so `deg β = 11` at `K=8` stays open and the `D = 108`
no-split arm stays conditional on `deg β = b_min = 6`.
## 7. FALLACY-v2

- **Modular unit is a screen.** `1 ∈ I_p` does not give `1 ∈ I_Q`. Only the four
  `Q-UNIT` charts carry a certificate, each an msolve `-g 2` reduced basis `[1]`
  over Q on the denominator-cleared integral generators.
- **`I_light` drops rows only.** The MASTER `E`-cutoff rows are omitted
  (`theorem_cut=False`); dropping rows enlarges the variety, so a unit of
  `I_light` kills the theorem-cut ideal. The converse is not used.
- **Resource failure vs verdict.** `MS-TO`, `rc 137`, `rc -9` and `FORM-TO` are
  engine limits, never counted as non-units, dimensions or survivors. Round 1's
  `SEGV*` entries were the same; this lane shows their cause was the 24 GiB cap.
- **Carrier/attainment.** `K=8 b=11 q0` being `[1]` over Q decides that *chart*:
  not the stratum (`q1` is open), not the band, not the row. The `K=7` closures
  do not transfer; §3 shows the `K=7` cost curve does not predict the `K=8` one.
- **Cover.** `{q0≠0} ∪ {q0=0, q1≠0}` covers `deg β = b` exactly; a stratum is
  DEAD only when both charts are exact-Q units. Four strata have one certified
  cover and are reported `partial`, never as kills.
- **Variable/ring map.** Declared in §4; the alias map is stored per chart.
  `PRE__CST_ZERO 0` and `TARGET_FOUND 1` on every chart rule out a vacuous
  `CSTP ≡ 0` unit.
- **`sat()`** unused. `3b ≥ 2K+1` stays a floor and LEVEL 4 a necessary shape;
  neither is used as a kill. The Rabinowitsch generators are named and present;
  no `q_j = 1` slice was consumed.
- **No survivor.** No chart returned a NONUNIT basis in any characteristic or
  linear-algebra variant, so there is no dimension or sample point to publish.
- **Report discipline.** No ledger edit, no `jc2-lean`, no `ideation-*`; no
  exit-price assertion, so no `charge_basis=` line.

## 8. What the next round should do

The lane's own evidence says a third brute-force sweep is not worth buying.

1. **`K=8 b=11 q1` is one run short.** Its `q0` sibling closed over Q in 1257 s
   on a quiet machine; `q1` got 1800 s under contention, then 1320 s at the end.
   One uncontended `-t 64` exact-Q run on the emitted `K8_B11_Q1_p0.ms` (sha
   `66bb78cf…`, 330 generators, 97 variables) is the cheapest open item in the
   campaign and would close the first `K=8` stratum. **Do this first.**
2. **Do not buy memory.** 66.6 GB was the largest resident set observed; no
   single job came near the 400 GB cap. The pressure came from running 6–9 jobs
   per worker, not from any one of them.
3. **The remaining wall is the degree-7 F4 step.** Attack the chart, not the box:
   the `G_m` dehomogenisation `q_j = 1` both rounds noted and declined; a partial
   elimination of the `h` block before msolve; or putting the theorem-cut rows
   *back* to shrink the variety, which raises `ng` but may drop the degree.
4. **Formation is no longer binding below `b = 12`**, but `K=8 b≥13` and
   `K=9 b≥11` still never form. Those eleven strata need a cheaper emitter —
   `coef(JJ,x*y)` and the incremental `ideal + ideal` accumulation in the ρ/J
   loops are the candidates — before any solver question arises.

## 9. Artifacts and fleet termination

```text
box/k4ray-strata-r2-20260905/
  frozen-inputs.sha256 .check.log  5/5 OK
  r2_solve.py    one-formation-over-Q emitter + modular screen + exact-Q
  phase2.py      re-solve an emitted .ms (longer budget, optional -l 42)
  mkbatch.sh batch-{A,B,C}-{P,S}.sh   per-worker detached launchers
  collect.sh status.py merge.py final_table.py f4deg.sh
  merged.json    per-chart record;  FINAL-TABLE.txt  the §5 table
  f4deg.tsv      max F4 degree and largest Macaulay matrix per run
  status-*.tsv health-*.txt poll.log dispatch.log live-rss.txt
  pull/<ip>/     every JSON payload (ms_sha256, rows, vars, rc, wall, peak RSS,
                 F4 trace, PRE__ markers, alias map)
```

Grep: `EXACTQ_UNIT`, `MODULAR_UNIT`, `EXACTQ_TIMEOUT`, `FORMATION_TIMEOUT`,
`TARGET_FOUND 1`, `PRE__HOMOG_I`.

Reproduction — `r2_solve.py 8 11 --pin-index 0 --threads 32` (~69 min formation,
~21 min msolve, the new `K=8` certificate) and `r2_solve.py 7 5 --pin-index 0`
(the banked control, `EXACTQ_UNIT` in 0.14 s).

The three workers this lane launched were terminated at **21:04Z** and confirmed
`shutting-down` by an explicit `describe-instances` on those three IDs
(`terminate.log`). `fleet.sh term` was called with those IDs only; `term-all` was
never used and no other `jc2fleet` instance was touched.

```text
i-0024ff9a04ae0afbd  172.30.0.11   r7i.16xlarge  shutting-down
i-0f1a4335e5dab4a7e  172.30.0.119  r7i.16xlarge  shutting-down
i-0c82d1e5d2ed72ced  172.30.0.5    r7i.16xlarge  shutting-down
```

Wall clock: launch 18:10Z, 44 charts dispatched 18:15:55Z, last job 21:01Z,
termination 21:04Z. The final `K=8 b=11 q1` attempt (`-t 48`, whole machine,
1320 s) also hit its cap; that stratum is `partial`, not closed.

<!-- BODY-END -->
