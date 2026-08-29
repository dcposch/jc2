# V86TFQ2 deployment erratum

Date: 2026-08-26

The first dual-host deployment, archive SHA-256
`4ab846246fdb23e8f49358b84966b85cbcf260698ce28890cc2997b26d602410`,
failed identically after transport construction and before FIRST or P12.
The wrapper reduced arbitrary coefficient rows in raw pivot-dictionary
insertion order.  For this explicitly ascending transport policy, the
reviewed q2 client reduces those rows by sorted pivot-variable order; the
dictionary is not promised to be inserted in that order.  Both endpoints
therefore stopped at the free-variable assertion (`rc=1`, about 13 seconds,
about 293 MiB RSS).  This is a harness failure and carries no mathematical,
denominator, or beta-family verdict.

The repaired deployment sorts the transport pivots, remains frozen to the
ascending policy, and leaves reverse/sparse policies outside scope.  The
failed archive and its output must not be consumed as evidence.

The second dual-host deployment, archive SHA-256
`9f7427346d6ef6b80426245791dbccccb94312715f77380f01c07c95198237f2`,
passed the repaired transport gate and remained healthy, but was left running
as a deliberately redundant replay after a latency-only successor was
launched.  It expands P12 for both omission controls and independently
rebuilds both V85 source fibres.  The successor instead uses FIRST-only path
omissions, expands P12 once, checks all 39 beta-zero source digests against
the frozen V85 inventory, and replays the literal special identity.  No
mathematical acceptance gate is removed.  V2 is not authoritative unless it
finishes and is separately harvested.
