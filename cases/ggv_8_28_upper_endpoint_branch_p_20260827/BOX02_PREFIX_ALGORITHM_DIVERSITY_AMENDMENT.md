# Box02 exact prefix algorithm-diversity amendment

Frozen before launch on 2026-08-28 UTC.  This amendment licenses exactly one
new Box02 computation after the capped `std` computation ended without a
verdict.  The old namespace and its evidence are immutable and are not inputs
to this run.

## Exact system and distinct computation

The input ideal is byte-for-byte the same exact-Q 466-original-generator
quotient ideal in `PREFIX_QUOTIENT_SYSTEM.json`: 303 raw variables, ordering
`(lp(202),dp(101))`, and all 18 retained row-22 affine endpoint coefficients.
The 47 omissions have their exact polynomial cofactor replay into the retained
original raw generators.  There is no specialization, modular computation,
new equation, D23/G22/q1 condition, or generator-set replacement.

The sole algorithmic change is Singular `slimgb(I)` in
`prefix_quotient_q_slimgb.sing`, replacing the capped predecessor's `std(I)`.
This is a genuinely distinct reducer on the same presentation, not a rerun of
the capped standard-basis algorithm and not the row-RREF generator
presentation running on Box03.

## Box02-only custody and caps

- Host: `i-010201a5da47795c4` (`x2idn.32xlarge`, audited Box02), exact DMI and
  `/usr/bin/Singular` binary gates in the launcher and runner.
- Exactly one core, 134217728 KiB virtual-memory cap, 7200-second global wall
  cap including compile/replay, then TERM and a 120-second KILL grace.
- Start only with zero swap, load1 at most 16, and available memory at least
  the requested 128 GiB cap plus 150 GiB host headroom.
- Fresh UTC-tagged immutable source tree and fresh output namespace.  Exact
  source-set coverage and `SOURCE.sha256` verification are mandatory locally
  and remotely before CAS starts.
- Stop without launch if any authoritative upper-endpoint result has appeared,
  identity, source, binary, capacity, swap, load, freshness, or replay checks
  fail, or another copy of this lane exists.

## Decision and promotion firewall

`UNIT=1` is only a candidate exact-Q emptiness result for the 466-generator
ideal and requires complete terminal custody plus independent verification and
an exact certificate lifted/replayed against all 513 authoritative raw
generators before promotion.  `UNIT=0`/proper output is only a candidate point
search lead and cannot prove existence without an explicit exact raw witness
replaying all D7..D21=0 and D22=1.  Timeout, memory cap, signal, malformed
output, missing terminal marker, or incomplete evidence is
`RESOURCE_CAP_NO_VERDICT`.  The literal raw direct lane remains authoritative.
