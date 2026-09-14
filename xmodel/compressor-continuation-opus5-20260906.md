# Compressor continuation: R005 adoption, compression soundness, F4 telemetry

## Verdict

**The compression is SOUND and mechanically certified; it does NOT run to
completion; and the F4 telemetry does not decide whether it helps.**  No `[1]`,
no basis, no kill, at any depth.

- *Typed ratio, against the charged ordinary presentation* (307 unknowns / 484
  generators / 2,902,778 terms).  Recursive monic-linear substitution is a
  three-axis compression only for its first 13 pivots: `x0.958` variables,
  `x0.973` generators, `x0.899` terms.  After that it buys variables with
  terms: at 36 pivots (deepest certified artifact) `x0.883` / `x0.926` /
  `x3.672`; at 54 pivots (deepest exact-`Q`, no artifact) `x0.824` / `x0.888` /
  `x6.149`.
- *`<= 600` variables.*  Yes at every depth -- **and already at depth 0**, since
  the uncompressed system has 307.  The threshold is met but it does not
  discriminate, so it is not evidence for the compression.
- *F4 progresses?*  Yes, on all three presentations -- the patched binary no
  longer segfaults before its first F4 step.  But none terminated, and the
  three are not cleanly rankable; see S6.
- *Lemma.*  S4, with (H1)--(H4) asserted at every pivot plus an independent,
  demonstrably non-vacuous random-point lift certificate.

## 1. Custody and host-write boundary

An `awk` program joined the receipt's numbered `charged_input_<i>_basename` and
`_sha256` lines and piped its output to `sha256sum -c`: **10/10 `OK`**.  Receipt
`xmodel/compressor-continuation-opus5-20260906.run.v2`; frozen copies under
`/tmp/jc2-lane.mh1NYK/inputs/`.  `df -h /` ran on the worker before every write
(96 GiB total, 20 -> 18 GiB free) and on math-hq before the box write (12 GiB
free).  Host output is this report plus `box/compressor-continuation-20260906/`
(260 KiB, 25 files).  Generation, solver inputs, and solver logs stayed on the
worker.

## 2. What the adopted worker actually contained

Worker `i-0b019d96be51d78a4` (172.30.0.156, `r7i.8xlarge`, 32 vCPU, 247 GiB),
reached with the `jc2-fleet` key and adopted.

**The Singular chain was already gone.**  `systemctl list-unit-files 'classA*'`
showed only two transient units, `classA-driver-R006` and `classA-driver-R008`
-- no `classA-compress-R005-v2`, loaded or unloaded, and no such process.  Its
terminal state survives only in the charged `singular-superseded.json`: 6 pivots
(`A1_1_7, A1_2_5, A1_3_3, A1_4_1, A1_1_6, A2_5_8`), 478 generators, 2,598,694
terms, `MemoryPeak` 6.85 GB, `CPUUsageNSec` 1388 s, disposition
`SUPERSEDED_NO_COMPLETE_COMPRESSED_ARTIFACT`.

It had been superseded on the worker by `fast_compress.py` -- exact `fmpq`
sparse **block** regeneration rather than Singular substitution -- running on
R005 as PID 30032 since 08:02Z.  At adoption it stood at pivot 38 / 446
generators / 10,650,827 terms.  I left it running; it reached **pivot 54** (430
generators, 17,847,884 terms, 3506 s, peak RSS 7.37 GiB) and then terminated at
~09:00Z **without** writing `COMPRESSION_COMPLETE`, leaving no compressed
artifact.  `dmesg -T` and `journalctl -k` record no OOM kill and the log ends
mid-stream with no Python traceback, so I cannot attribute a cause; the
trajectory through pivot 54 is intact and is the fill-in evidence in S5.

R005 has 307 unknowns: `h` 29, `A1` 29, `A2` 70, `A3` 109, `B2` 69, `c` 1.  The
**208 `A*` coefficients are the arithmetic variables**; eliminating all of them
would leave 99 semantic variables and 276 generators.  Every pivot taken by
every run below is an `A*`; no `h`, `B2` or `c` pivot ever became available.

## 3. The continuation

`fast_compress.py` rebuilds all 484 rows from the substituted blocks at every
pivot, so its cost is `O(pivots x terms)` with `terms` rising.  Since step (4)
asks for a *modular* run, I mirrored it at `p = 1073741827 = 2^30+3`
(`fmpz(p).is_prime()` verified) as `modp_compress.py`: identical block
regeneration, identical pivot rule, `flint.nmod` coefficients, emitter in
`[0,p)`.  Two controls tie the mirror to the charged exact-`Q` object.

1. **Reduction control.**  The charged 84,916,356-byte exact-`Q` `ordinary.tsv`
   (SHA `c437d0a1...`, 484 rows, 2,902,778 terms) was parsed term-by-term,
   reduced mod `p`, and re-emitted; its digest equals the digest of the
   independently regenerated mod-`p` stream --
   `CONTROL_EXACT_Q_REDUCTION_EQUALS_MODP_REGENERATION=PASS`,
   `316e5b6200ff5b27f1cb2fe90c4c30ca62e9987f1562f11a3f7fd9e9326abaa0` (22.4 s).
   The mod-`p` system is the byte-exact reduction of the charged one, not a
   re-derivation.
2. **Chain agreement.**  Comparing the exact-`Q` and mod-`p` pivot audits on
   `(row_slot, variable, unit, row_terms, rhs_terms)` over their common
   prefixes gives **0 mismatches** (21, 20 and 13 steps against exact-`Q`'s 44
   recorded).  No pivot selection degenerated mod `p`.

Three `c=1` presentations were produced and written as msolve input:

| presentation | pivots | vars (`c=1`) | gens | terms | bytes | SHA-256 head |
|---|---:|---:|---:|---:|---:|---|
| `P0` charged, uncompressed | 0 | 306 | 484 | 2,902,778 | 97,134,516 | `967e7dd2` |
| `P13` term optimum | 13 | 293 | 471 | 2,610,428 | 88,782,276 | `2de65144` |
| `P36` deepest certified | 36 | 270 | 448 | 10,659,629 | 496,308,298 | `d3e244d2` |

Setting `c=1` changes no term count: `c` occurs in exactly one row, as the lone
monomial `-c` in the `(ell,0)` slot.

## 4. Soundness

**Lemma (pivot substitution).**  Let `k` be a field, `R = k[v, w_1..w_n]`, and
let `I <= R` have a generator `r = u*v - q` with `u` a nonzero **constant** of
`k` and `q` free of `v`.  Let `phi: R -> k[w]` be the `k`-algebra map
`v |-> q/u`, `w_i |-> w_i`.  Then `phi(I)` is generated by the images of the
remaining generators, and `V(I) -> V(phi(I))`, `(a,b) |-> b`, is a bijection
with inverse `b |-> (q(b)/u, b)`.  *Proof.*  `R = k[w][v]`, and after scaling by
the unit `u` the row `r` is monic-linear in `v`, so `k[w][v]/(r) ~= k[w]` via
`phi`.  The quotient map carries `I` to `phi(I)`, and `V(I)` is exactly the
graph of `q/u` over `V(phi(I))`.  A pivot row containing `v` nonlinearly breaks
this: `r` is then not monic-linear and `k[w][v]/(r)` is not `k[w]`.  Pivot order
is immaterial because each `phi_i` is an isomorphism onto its own polynomial
ring, so the composite depends only on the *set* of pivots -- provided no
eliminated variable survives anywhere, which is (H4).  `[]`

The hypotheses are asserted **at every pivot**, not sampled:

- **(H1) linear-monic.**  `assert unit and derivative(poly, v) == {(): unit}`:
  the formal `d r / d v` is the *constant* `unit`, i.e. `deg_v r = 1` with
  constant leading coefficient.  This is the mechanical check the task asks
  for; it fired 13/13 in `P13`, 34/34 in the certificate run, 36/36 in `P36`,
  54/54 in exact-`Q`.  Every unit is `18k` for `k = 1..13`
  (`18, 36, ..., 234`) -- invertible in `Q`, and nonzero mod `p` since `p` is
  prime and `p > 234`.  So the identical chain is legal over `Q` and `F_p`.
- **(H2) row vanishes.**  `assert not substitute(poly, v, rhs)`.
- **(H3) `rhs` is `v`-free.**  `assert not derivative(rhs, v)`.
- **(H4) closure.**  After the last pivot no eliminated index occurs in any
  block, row, or image; every surviving variable has image itself and
  `images[c] == c`.  `CLOSURE_H4=PASS` on every mod-`p` run.
- **Negative controls, printed before any pivot.**  `candidate()` rejects a
  quadratic occurrence, a mixed monomial, and the reserved `c`; regeneration
  from substituted blocks equals the row-wise map on an exact toy
  (`CONTROL_*=PASS`).

**Independent lift certificate** (added by me; the running engine had none).
Draw a random `w` on the live coordinates, lift through the recorded images to
`z` on all 307 coordinates, and evaluate the *original* regenerated rows at `z`:

```
depth 34: CERT_LIFT rows=484 consumed=34 original_vs_compressed_mismatch=0
          pivot_rows_nonzero=0 original_rows_nonzero=450
depth 13: CERT_LIFT rows=484 consumed=13 original_vs_compressed_mismatch=0
          pivot_rows_nonzero=0 original_rows_nonzero=471
CERT_GRAPH_IN_ORIGINAL_ZERO_SET=PASS
```

Every consumed pivot row vanishes identically on the graph, and every surviving
original row takes exactly its compressed value there.  It is **not vacuous**:
`450 = 484 - 34` and `471 = 484 - 13` rows are nonzero at that same point, so
the test separates the eliminated equations from the rest instead of passing on
a degenerate point.

## 5. Why "to completion" is out of reach

Term count is not monotone under this compression.  It falls to a minimum at
pivot 11 and then climbs (exact-`Q`, generators/terms):

```
  1 483  2,830,514 | 11 473  2,559,345 | 21 463  3,529,326 | 31 453  7,501,637
 41 443 13,215,334 | 46 438 16,812,798 | 51 433 17,066,776 | 54 430 17,847,884
```

Fitted over 11 -> 54 the fill-in factor is **1.046 per pivot**; over the slower
recent window 41 -> 54 it is 1.023.  Reaching 208 arithmetic pivots needs 154
more from depth 54: `~6e8` terms at the *slower* measured rate, `~2e10` at the
fitted one.  Seconds per pivot rose from 11.7 to **175.7** across the same
range, and `t_regen` is 858 s of the 957 s of wall at depth 36 -- block
substitution and image maintenance are free; the full per-pivot rebuild is the
entire cost.  Completion to the 99-variable semantic floor is unreachable by
full regeneration on any hardware in this budget.  The lever is an
**incremental** regenerator, not a faster coefficient field or a bigger box:
the mod-`p` mirror cost the same per pivot as exact `Q` at equal depth.

## 6. F4 telemetry

Patched msolve 0.10.1 from the charged provenance (source commit `185e7b92`,
both frozen patches, `make check` 64/64).  Both provenance controls replayed at
`p = 2^30+3` before use: `{xy-1, y^2-x}` returned its 3-element basis,
`{xy-1, x}` returned `[1]`.  All runs `-g 2 -v 2`.

| run | pivots | vars | thr | wall | matrices | F4 degrees | largest matrix | basis | peak RSS |
|---|---:|---:|---:|---|---:|---|---|---:|---:|
| `P0` | 0 | 306 | 12 | 45:00 stopped | 45 | 2--5 | `538968 x 4615336` | 915,780 | 80.8 GiB |
| `P13` | 13 | 293 | 8 | 31:12 stopped | 48 | 4--6 | `490513 x 4170220` | 1,934,828 | 120.8 GiB |
| `P36` | 36 | 270 | 32 | 60:02 timeout | 46 | 5--10 | `314045 x 5601143` | 950,693 | 76.7 GiB |

`P36` is the required run and it consumed its full 60-minute cap (`exit 124`,
empty `.out`).  `P0` and `P13` were stopped early by me for memory pressure
(183 of 247 GiB with three solvers live), `P13` at 120.8 GiB and still climbing.

**What this does and does not show.**  It shows the patched binary reaches and
sustains F4 on all three presentations -- the previously reported segfault
before the first F4 step does not recur.  It does **not** rank them.  F4 degree
is not a common index here: substitution raises generator degree, so the runs
open at degrees 2, 4 and 5 respectively and "degree 10 in `P36`" is not "past
degree 5 in `P0`".  Matrix size is mixed rather than ordered -- `P36`'s largest
has 1.7x fewer rows but 1.2x more columns than `P0`'s.  Thread counts differ
(12/8/32), so wall-clock and memory-per-minute are not comparable either.  The
one clean fact is the endpoint: `P36` sustained the full hour at the lowest peak
memory of the three, while `P13` -- the presentation that is strictly smaller
than `P0` on all three axes -- was the *worst* on memory.  On this evidence the
compression is not established as a solver win, and no `[1]` appeared to be
read as a signal in either direction.

## 7. Next-worker sizing

- **Solver.**  One msolve per worker; do not co-schedule.  247 GiB was not
  comfortable for three.  Budget `>= 128` GiB for a `P0`- or `P13`-class input
  and `~ 96` GiB for `P36`-class.  `-t 32` is not the constraint: msolve sat at
  160--364% CPU for long stretches, so it is memory- and latency-bound.
- **Compressor.**  Single-threaded Python, `t_regen ~ 90%` of wall, peak RSS
  7.4 GiB at depth 54.  A 32-vCPU box is wasted; `c7i.2xlarge` suffices.  Depth
  beyond ~60 needs incremental regeneration (rebuild only rows whose blocks
  changed) before a larger instance is worth buying.
- **Do not** re-run the exact-`Q` chain to feed a modular solver: the mod-`p`
  mirror is byte-identical on the source stream and step-identical on the chain,
  at the same cost per pivot, with no coefficient growth.

## 8. Box and worker disposition

`box/compressor-continuation-20260906/` holds `summary.json`, engine JSONs for
all three depths plus the certificate run, pivot and coordinate audits
(exact-`Q` and mod-`p`), the image digest table, live-variable lists, the
control transcript, the `.ms` input digests, msolve log heads, and both driver
scripts.  Worker `i-0b019d96be51d78a4` is terminated with
`sh ops/fleet/fleet.sh term i-0b019d96be51d78a4`; the 496 MB and 97 MB `.ms`
inputs and full solver logs die with it and are reproducible from the charged
inputs plus `tools/modp_compress.py`.

Open, typed.  `OPEN[R005-COMPRESSION-DEPTH]`: completing the 208-pivot
arithmetic elimination requires an incremental regenerator.  `OPEN[R005-GB]`:
no Groebner basis and no `[1]` at any depth, so R005 remains compute-bound.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13159`.
- Body SHA-256:
  `bcff96e38ba81a800390d4f5942f3ade33886ce410c80f77eaccbf4948056f79`.
- Frozen basis: `911f852ee1464f49879a82a0acce70a819a6e32c`.
