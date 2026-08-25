# TD6 V52 independent reverse-unit diagnostic — AWS custody report

## Verdict

`V52: REVERSE UNIT-PIVOT COVER INCOMPLETE / FAIL-CLOSED DIAGNOSTIC`.

The exact independent-order AWS replay reaches the correct transport object,
then proves that its reverse/deferred schedule cannot parameterize the first
post-transport system using beta-independent unit pivots alone.  Six
source-provenanced `X-2` rows remain and every available coefficient is a
positive-degree polynomial in beta.  The producer aborts before any such
coefficient is inverted.

This narrows the denominator problem: an independent reverse chart must
either use polynomial/fraction-free row operations or explicitly localize at
the emitted nonunit pivots.  It does **not** show that the first-stage system
is inconsistent, does not refute V50, and does not cover any exceptional
divisor.

## Exact AWS evidence

- Host: r6d, run tag
  `td6_v52_reverse_unit_r6d_20260825T0849Z`.
- UTC interval: `2026-08-25T08:49:39Z` to
  `2026-08-25T09:10:13Z`.
- Source archive SHA-256:
  `53903f0e98e6f930bafdd865c320b257b699228f495da89c49c5bf4c7e5927cd`.
- Producer SHA-256:
  `ad09a4c3252ce848053c22882ad53ed092271839b32ed986265e78895de5e9fe`.
- Mathematical stdout SHA-256:
  `0bd254e0e114606867f159bc1480c17806e2319ea511167d320502eb18bd5739`.
- Timing/traceback stderr SHA-256:
  `cc38a80d5917703feff3dec93c11e6b2bbf21696f08a44711aa402cf59c839a4`.
- Exact rc file SHA-256:
  `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`.
- Maximum resident set size: 302,392 KB; wall time 20:34.

The frozen stdout includes each unresolved key, RHS beta degree, and the
complete list of surviving variable/coefficient beta degrees.  The traceback
ends only at the preregistered assertion
`reverse unit-pivot cover incomplete`.

## Scope firewall and successor

V52 is evidence about one exact pivot policy.  It is not evidence that a
different polynomial row combination cannot produce a unit, and it does not
license replacing a multivariate saturation/Bezout check by a gcd.  V54 is
the minimal successor: retain the reverse unit closure, fraction-free
eliminate the six unresolved rows, replay their original-row combinations,
and record each nonunit pivot/denominator as an exceptional factor.  Full
source composition and any generic-open claim still require V50 or an
equally complete independent replay.
