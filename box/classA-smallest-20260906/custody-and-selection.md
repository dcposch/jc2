# Class-A smallest-receiver custody notes

## Charged inputs

The receipt-driven `awk` manifest and `sha256sum -c` check returned `OK` for
all five files in `/tmp/jc2-lane.Yhc8AP/inputs`:

| input | SHA-256 |
|---|---|
| `chart-counts.json` | `4f9382b1c39e2a0b39e2dc14757607f0051969aefc331f3eb2efacd2c1a61d44` |
| `roster.jsonl` | `cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf` |
| `guided_gb.py` | `95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826` |
| `fleet.sh` | `a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

## Selection

The literal frozen predicate (nonempty own route, licensed descent,
`u_s=1`, and `100<n<=200`) selects 41 rows.  There are 46 such `u_s=1`
rows without the degree window; `R001`--`R004` and `R007` are the five
`n<=100` controls.  Removing the already killed `R058` and `R063` gives the
prompt-state totals 44 without the window and 39 with it.

Sorted by `(unknowns_without_T, coefficient_generators, source_n, source_m,
row_id)`, the first five eligible rows are:

| rank | row | receiver key | unknowns excl./incl. T | generators coeff./incl. `Tc-1` |
|---:|---|---|---:|---:|
| 1 | `R005` | `n27_m18_Mlast20_ell2` | 307/308 | 484/485 |
| 2 | `R006` | `n39_m26_Mlast30_ell1` | 322/323 | 495/496 |
| 3 | `R008` | `n21_m14_Mlast15_ell4` | 370/371 | 595/596 |
| 4 | `R009` | `n48_m32_Mlast37_ell1` | 388/389 | 600/601 |
| 5 | `R010` | `n35_m14_Mlast30_ell1` | 403/404 | 576/577 |

The unique minimum is `R005`, source `(n,m)=(135,90)`,
`M=(-90,100,133)`, `V=(4,4)`.  Its receiver is
`(n',m',M'_last,ell)=(27,18,20,2)`.  The V-independent class identifier is
`C_n27m18_M20_ell2_s2`; the frozen historical fibre label is
`C_n27m18_M20_ell2_s2_V4`.  It covers `R005` only.  The charged printed row
is `/tmp/jc2-lane.Yhc8AP/inputs/roster.jsonl:5`; the stable human-readable
printed line is `box/residual66-20260905/roster.md:27`, and upstream own-route
line is `box/child-own-v-20260905/own-rows.jsonl:95`.

The frozen coordinate digest is
`9758dedb763696c99ee72d3cd7345d7dc336637fb65909731811a6e5afe37c89`.
The frozen count-only production record gives fixed emitted-program digest
`8353325956564822d62c676bb8776f09bad015be709e966d58fa48767f632bd5`
(19,571 bytes) and raw digest
`3cefe3b7f3b1be28c2c446021360cfa5ce8eb787af9ed4e1c5d061ef8a7654ce`.

## Missing path and worker-only reconstruction

The requested expected row path
`box/gi-only-20260905/classes/C_n27m18_M20_ell2_s2/rows/C_n27m18_M20_ell2_s2_G_rows.tsv`
is absent.  The class tree contains only six materialized `n<=100` class
programs, and no file there has either target digest.  No host-side substitute
was made.

For the compute probe only, the worker mechanically replayed the producer
chain whose source hashes and setup are pinned inside the charged
`chart-counts.json`.  Before transforms, the gate required the fixed-program
digest and the coordinate digest above, 307 coefficient unknowns, 484 rows,
and bihomogeneity.  The accepted exact-Z row stream has 485 physical lines
including its header, 53,209,262 expanded terms, 2,179,919,994 bytes, no NULs
or sparse holes, and SHA-256
`b4a4160ccef95d28490da264704ec8b272110222f8438d62d91ef62a9eccaf78`.
It remains an ephemeral reconstruction, not retroactive provenance for the
missing class-tree path.

An earlier duplicate-writer intermediate failed the physical-allocation,
NUL, header, and line-count gate, was deleted, and was never transformed or
supplied to a solver.

## Worker and derived inputs

The existing worker was `i-0cd415bd9d3abed39`, `172.30.0.163`, an idle
`r7i.8xlarge` with 32 vCPUs, 247 GiB visible RAM, no swap, and 23 GiB free on
`/` before scratch writes.  No instance was launched.  Scratch root:
`/home/ubuntu/classA-smallest-20260906.xpXroy`.

| derived input | bytes | SHA-256 |
|---|---:|---|
| exact saturation, Q | 2,179,920,216 | `9942a0c4361dadf878104295b797b7013a80b203607ed1cd7289e0c0b194faea` |
| Hilbert seed, p=32003 | 2,179,920,220 | `c758622ed2d37c777f3a081e108e75ace33571851aefa5a108f88ce9678cef68` |
| c=1 msolve | 1,404,553,226 | `41bcb588c28ccbc37939c3d84825c9992ed61b811ac9f7436666a2640f8783bf` |
| exact Q with T block | 2,179,920,284 | `5a2fdef7de7fc05ab55397471310b6efce87cb197d20da42bb2db282b8f1ebae` |

The launch time for all three jobs was `2026-09-06T04:36:20Z`.  Each had an
8,940-second inner GNU timeout and a 9,000-second systemd hard ceiling.

```text
(a) /usr/bin/time -v -o results/a_guided/time.txt timeout --signal=TERM
    --kill-after=30s 8940s python3 jobs/run_guided_r005.py
(b) /usr/bin/time -v -o results/b_msolve/time.txt timeout --signal=TERM
    --kill-after=30s 8940s /usr/local/bin/msolve -g 2 -t 16 -v 2 -l 44
    -m 1000 -f data/R005_c1_p1073741827.ms -o results/b_msolve/basis.out
(c) /usr/bin/time -v -o results/c_singular/time.txt timeout --signal=TERM
    --kill-after=30s 8940s /usr/bin/Singular --no-rc --cpus=8 --threads=8
    --flint-threads=8 -q data/R005_full_Tblock_Q.sing
```

The guided runner has an 8,880-second total budget.  It first computes a
p=32003 Hilbert seed for `(I:c^infinity)` and, only if that stage completes,
runs the exact-Q standard basis with the returned numerator and remaining
time.  It uses exact-Q promotion policy, required controls, no perturbed run,
and `allow_modular_unit_promotion=false`.

The worker msolve SHA-256 is
`0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`,
byte-identical to the named official Intel AVX-512 0.10.1 artifact.  The banner
reports 0.10.1; ISA custody comes from that digest match plus the worker's
AVX-512 CPU flags, not from a banner string.

## Terminal job results

| job | disposition | start/end UTC | wall | process-tree peak RSS | basis/F4 |
|---|---|---|---:|---:|---|
| guided saturation | `TYPED_TIMEOUT_OUTER_DURING_HILBERT_SEED` | 04:36:20 / 07:05:20 | 8,940.126 s | 109,918,196 KiB | no seed contract, exact-Q stage, or basis |
| msolve c=1 | `FAILED_SIGSEGV_BEFORE_F4` | 04:36:20 / 04:37:09 | 48.319 s | 8,458,580 KiB | 0 completed F4 rounds; empty basis file |
| exact-Q full ideal | `TYPED_TIMEOUT_EXACT_Q_STD` | 04:36:20 / 07:05:24 | 8,943.596 s | 124,433,724 KiB | no basis/unit marker |

Guided returned rc 124.  The p=32003 saturation/Hilbert seed did not finish;
there was no Hilbert numerator or guided result JSON, and the exact-Q stage
never began.  GNU maximum RSS was 105,619,632 KiB and cgroup peak was
112,742,891,520 bytes.  Final memory events were
`high=1718066,max=0,oom=0,oom_kill=0`.

msolve returned wrapper rc 139 and GNU signal 11 after 48.26 seconds.  It
emitted no F4 line.  GNU maximum RSS was 8,439,088 KiB; cgroup peak was
8,662,831,104 bytes.  `basis.out` is zero bytes with SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Exact-Q Singular returned rc 124.  Controls passed and `R005__STD_BEGIN`
printed, but no `BASIS_SIZE`, `UNIT`, or completion marker did.  GNU maximum
RSS was 124,414,112 KiB and cgroup peak 127,647,522,816 bytes; final events
were `high=2686266,max=0,oom=0,oom_kill=0`.  The supplemental Singular std
protocol reached live degree 55, with degree 54 closed and last `s` counter
149,360; it emitted no F4 matrix dimensions.

No job completed a basis.  There is no modular signal, exact-Q kill, or
nonunit screen survival.  The msolve F4 degree wall is unavailable: zero
rounds completed before the crash.  Singular's closed degree 54 is retained
only as non-F4 protocol telemetry.

At `04:56:17Z`, safety controls set guided High/Max to 95/105 GiB and exact
High/Max to 110/120 GiB, with swap disabled and combined hard Max 225 GiB.
At `05:52:04Z`, only the soft highs rose to 100/115 GiB after severe reclaim;
the hard maxima never changed.  Neither job incurred a hard-charge or OOM
event, so both long dispositions remain wall-clock timeouts.

Worker summaries before cleanup:

- `results/terminal_summary.json`: 7,236 bytes,
  SHA-256 `50108340cf9abe642cb37f945666b38bb10c9d0c3f82347aecbc0d1eb69f1b15`.
- `results/terminal_summary.txt`: 499 bytes,
  SHA-256 `3139eab254ff06fc7eff7189197e2bed01ab49631b1a6ebd4a4ea8d6dd6345a8`.
- `results/harvest.json`: 32,149 bytes,
  SHA-256 `3fa4d4182e525e7aa90e9f8fdafcfcb0079dbe461f2132774fef7ccce89c563d`.

## Cleanup

After remote inspection of the terminal summary and its SHA-256, the resolved
scratch tree `/home/ubuntu/classA-smallest-20260906.xpXroy` and row stream
`/dev/shm/lambda-lowweight-R005-rows.tsv` were removed at
`2026-09-06T07:09:33Z`.  Both paths are absent; the three transient services
are unloaded and no related process remains.  Worker `/` had 23 GiB free and
245 GiB memory available afterward.  Fleet state still shows
`i-0cd415bd9d3abed39`, `172.30.0.163`, `r7i.8xlarge`, `running`.  No instance
was launched or terminated.
