# `(8,12)` order two, `U=2,[6,2]`: V2 dual strict-Rees timeout

Date: 2026-08-26

Status: **EXACT DUAL TIMEOUT CONTROL; NO ALGEBRAIC VERDICT.**

## 1. Frozen inputs and launches

Both AWS lanes consumed the byte-identical, source-reviewed V2 input

```text
021654e753f1186874f10110d4338e7d9f9457afbfed75419407e87e3b00982c
  strict_rees_v2.sing
```

from source archive

```text
4d084b2116f193938078f652f2e169ca898689be1f0837b6a4b55fdd44e3c302.
```

The input saturates the exact seven strict-Rees rows successively by
`tau`, `rho`, and `j`, then adds the `tau=rho=0` boundary and saturates by
the irrelevant coefficient ideal.  In particular this is the repaired
`j!=0` client, not either quarantined V1 endpoint.

The registered lanes were:

```text
r6d / ip-172-30-0-45
  max12_812_order2_u2_62_strict_rees_sat_v2_jsat_20260825T231400Z_r6d
  launcher PID 178772, cap 268435456 KiB, timeout 14400 s

Box03 / ip-172-30-0-249
  max12_812_order2_u2_62_strict_rees_sat_v2_jsat_20260825T231400Z_box03
  launcher PID 123062, cap 201326592 KiB, timeout 14400 s
```

All retrieved bytes are frozen by
`cases/max12_812_order2_u2_62_strict_rees_20260825/RESULTS_V2_TIMEOUT.sha256`.

## 2. Exact endpoints

Both jobs started at `2026-08-25T23:15:16Z` and ended at
`2026-08-26T03:15:19Z` with wrapper `rc=124`.  Their stdout files are
byte-identical:

```text
d9fd3452b5eaf244f200e55afd7cbed6cd8d5828c3a1f5b918ebd21ed5599055.
```

They contain only the Singular banner/library loads followed by `halt 1`.
No strict-Rees sentinel, ideal size, or unit/nonunit answer was reached.
The independent resource records agree closely:

```text
                 user s     system s     max RSS KiB   swaps
r6d             14367.36       35.74       86110316       0
Box03           14366.81       36.55       86104416       0
```

Thus the runs were one-core, compute-bound Groebner/saturation attempts,
not swap failures.  The identical endpoint does not independently confirm
any mathematical answer: it confirms only deterministic failure to pass
the very first uninstrumented saturation boundary within four hours.

## 3. Failure analysis

The monolithic source prints nothing between library loading and the final
endpoint.  It asks for three successive full saturations of a 16-variable,
seven-row, high-degree ideal in a global `dp` order, followed by another
irrelevant saturation.  Since neither host reached the first print and the
resource curves agree to within 0.01%, simply adding more wall time would
repeat an opaque computation with no evidence about which of `tau`, `rho`,
`j`, the boundary standard basis, or the irrelevant saturation is dominant.

The result therefore gives no evidence for emptiness or existence and must
not be used as a proof endpoint.

## 4. Prioritized successor gates

Do not rerun the monolith.  The smallest informative AWS redesign is staged
and checkpointed:

1. Replace principal saturation calls by localization variables
   `s_tau*tau-1`, `s_rho*rho-1`, and `s_j*j-1`, eliminate one localizer at a
   time, and print/checkpoint size, dimension, leading-ideal checksum, time,
   and memory after each stage.  Race characteristic-zero and two good-prime
   images.  A failed stage is diagnostic only.
2. Before full saturation, exploit that `j` occurs only in the terminal row
   and is nonzero.  On the localized chart solve the terminal equation for
   `j`; eliminate `j` by substitution rather than Groebner saturation.  This
   removes one variable and one expensive localization exactly.
3. Compile the two finite Taylor clients at the branch points `x=0,1`
   (`t^2=(x-1)/x`) and impose the first unresolved coefficient row before
   the global boundary.  Shard by the discrete lower-load pattern
   (`k10,k6,k2,mu2,mu4,mu6`) and stop at the earliest nonzero constant/unit
   witness.  These are necessary filters, not existence tests.
4. Run an all-lower-load-zero divisor-19 gate separately.  For this
   `[6,2]` source, `r7=(j/4)t` has divisor orders `+1,-1`, so the Hall/Shioda
   Davenport--Stothers sub-stratum is impossible without any Groebner
   saturation.  Remove it before the loaded shards; do not mistake this for
   elimination of the loaded order-two leaf.

Highest-value first experiment: exact `j` substitution plus the first
branch-point Taylor row, sharded by which lower load is first nonzero, with
each shard capped and independently replayed at one good prime.  It should
either produce an immediate unit witness or identify the smallest surviving
load stratum for a much smaller exact-Q lift.

## 5. Firewall

This packet records a timeout, not a theorem.  It neither eliminates the
`U=2,[6,2]` client nor establishes a surviving source, order-two closure,
all `(8,12)`, maximum twelve, or JC2.
