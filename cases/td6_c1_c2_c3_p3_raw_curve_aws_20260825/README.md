# TD6 raw `H=P3=0` quotient-field gate

This immutable AWS evidence package records two deterministic exact pivot
orders for the last raw curve left by the three-center `H=0` certificate,

```text
H  = C - 3U^2,
P3 = V^4 - 32V^2U^3 + 128U^6.
```

The calculation is on the fixed, previously source-typed three-center TD6
section.  It makes no source scaling or weighted-projective identification.

## Exact result

On `D(U)` in `H=P3=0`, the coefficient field is represented as

```text
Q(U)[Z,V]/(Z^2-32Z+128, V^2-ZU^3).
```

The quadratic in `Z` is irreducible over `Q`, and `ZU^3` is not a square over
`Q(Z)(U)` because its `U`-valuation is odd.  Thus this degree-four tower is a
faithful model of `Frac(Q[U,V]/(P3))`, rather than a sampled point or a gauge
quotient.

Both ascending and reverse first-stage pivot orders independently give:

- transport rank `3470/3602` with no affine compatibility;
- first-band rank `38/132` with no affine incompatibility;
- the genuine 2,885-term P12 remainder equal to the constant unit `-k/50`;
- an exact lift through the original transported first rows and a plus-one
  negative control;
- every raw, first, relation, and termwise denominator a power of `U`.

The ascending lift uses 28 nonzero original rows and 1,540 multiplier terms;
its full certificate chart is `U^17`.  The reverse lift uses 38 rows and 2,152
terms; its chart is `U^19`.  The respective termwise audits check 31,976 and
60,121 cleared source slots.  Therefore the entire raw open
`H=P3=0, U!=0` is empty.

Inside `H=P3=0`, the complement `U=0` forces `V=0` and `C=0`, hence is only
the raw center origin.  The earlier immutable three-center checkpoint rebuilt
that origin directly and proved it first-band inconsistent with a unit chart
(`cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/evidence/v14/origin.stdout`,
SHA-256 `c31a0f60eef078150bf7dd59878456fd332d55273181635d5ead11da52f0fc18`).
Consequently, combining the two separately frozen certificates closes the
whole set-theoretic `H=P3=0` curve.  Together with the earlier `H=0` open and
its `U=0` and `V=0` raw rebuilds, this removes the final producer-exact debt
on the fixed-section `H=0` divisor.

## AWS custody

The two lanes ran with Python 3.12.3 and python-flint 0.9.0:

| Lane | AWS host | UTC interval | rc | stdout SHA-256 |
|---|---|---|---:|---|
| ascending | `ip-172-30-0-45` (r6d) | 02:30:29–03:09:33 | 0 | `c38471a004ac311ae01ae851bc98d6223829292ad74db20e2e6d9b7cd79c17b8` |
| reverse first | `ip-172-30-0-186` (Box02) | 02:30:29–03:14:44 | 0 | `900c38298b6dcaf8ed420afd3d947ca237b5581428d396b063de0875b595a30f` |

The archive SHA-256 is
`b207bbba13ee20d2719ef15504df632f66674d69072d97b83f4c9970d53e0e98`;
its `SOURCE.sha256` SHA-256 is
`7b00ab87e35ca9b2cff9d31d7e0e75cd5cd4fbf5fbe64d1ad68f300c39a2032f`,
and the producer SHA-256 is
`1b492ad26a2f1c0cdc3ae3983068639163118010ffba9e53c9e6d097d56c9a22`.
Both on-host source-closure checks passed with empty stderr.  The nonempty
lane stderr files are only `/usr/bin/time -v` resource reports and end with
exit status 0.

## Replay

Heavy replay is AWS-only under the campaign resource policy.  On an AWS host
with python-flint, extract the pinned archive and run from its payload root:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py --reverse-first
```

Each command must end in `TD6-C1-C2-C3-P3-QUOTIENT PASS`.  `SOURCE.sha256`
must be checked before either command.

## Scope

This is a raw-curve theorem only for the fixed source-typed three-center TD6
section.  It does not prove a neighborhood statement, cover other centering
or boundary/dead-stretch moduli, kill the full TD6 family or SP-2, or resolve
JC2.  The cross-package whole-curve and whole-`H` conclusions depend on the
separately frozen origin and earlier `H/U/V` certificates cited above.
