# TD6 V54D reverse first-stage denominator diagnostic

Frozen status: **producer-exact AWS diagnostic; no cover claim**.

Two independent AWS executions (Box03 and r6d) of the pinned V54D source
archive exited zero and produced byte-identical mathematical stdout and
canonical artifacts.  The calculation preserves the arbitrary-degree
original rows, replays every one of the six unresolved first-stage rows, and
uses an independent reverse/deferred fraction-free order after the fixed
rank-3470 transport.

The exact diagnostic endpoint is:

```text
unit first-stage rank       32 / 132
remaining nonunit pivots     6
fraction-field rank         38 / 132
rowwise center denominators U^4 H, U^4 H, U^5,
                            U^4 H^2, U^3 H^4, H^8
final emitted coefficient denominator U H^8
```

Here `H=C-3U^2`.  The last line reports the producer's final canonical
coefficient denominator; it is not asserted to be the least common multiple
of the six rowwise expressions.  The beta-dependent pivot product is a
nonunit and defines only this reverse chart.  It was recorded, not inverted
or promoted into an open cover.

The source archive SHA256 is
`0386b2c7d6b199cf5a287c0826540cf48f853b3b926bcf1d9ddb8a6c80d67983`.
The two mathematical stdout files are byte-identical with SHA256
`01112ab9578ce9737eba99ab7ebd0f482a007579ab3e0df76da7841635a94450`.
The canonical nonunit-pivot table and pivot-product files are also
byte-identical, with SHA256 values `77cafdf8...` and `d9b1a001...`.

`verify_v54d_custody.py` is deliberately lightweight: it verifies source and
evidence hashes, archive members, duplicate byte identity, exact markers,
canonical address-free serialization, and every negative scope flag.  It
does not rerun the exact algebra on the local machine.

For a full replay, unpack the source archive on an AWS host, verify
`SOURCE.sha256` and `V54D_SOURCE.sha256`, then follow `V54D_RUNBOOK.md`.  The
recorded jobs were:

- Box03: `/home/ubuntu/runs/td6_v54d_canonical_box03_20260825T1053Z`
- r6d: `/home/ubuntu/runs/td6_v54d_canonical_r6d_20260825T1105Z`

Strict scope: this is a reverse first-stage denominator and pivot diagnostic
inside the fixed source-typed A3 q2-beta calculation.  It is not a second
chart cover, a full V50 source identity, a generic-open obstruction, an
all-beta fixed-A3 theorem, a whole-TD6 theorem, SP-2, or JC2.
