# TD6 exact three-center checkpoint `(c1,c2,c3)=(C,V,U)`

This separate freeze records the exact AWS V8/V9/V11/V12/V14/V15
three-center producer checkpoint.  It does not modify the earlier immutable
two-center package.

## Strongest established statements

Under the same frozen TD6 source typing, rhs normalization, F1 orbit, pole
data, and centering tail used by the reviewed two-center theorem:

1. Over `E(C,V,U)`, transport has rank `3470/3602`, the first band has rank
   `38/132`, and genuine P12 reduces through 28 original transported first
   rows (1,489 multiplier terms) to the constant unit

   ```text
   -k/50,  k=252-342S+144S^2-36S^3.
   ```

   The complete ascending certificate is localized by
   `U`, `H=C-3U^2`, and

   ```text
   B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
   ```

2. The entire raw divisor `U=0` is empty: `C != 0` is first-band
   inconsistent with chart `C^3`; `C=0,V!=0` has the same unit residual with
   chart `V^3`; the origin is transport-inconsistent by a 21-original-row
   unit-chart certificate and plus-one negative control.

3. The entire raw divisor `V=0` is empty.  The V11 certificate applies off
   `U H (C+U^2)(C+5U^2)`.  V15 rebuilds all three remaining non-origin
   curves: `V=H=0` and `V=C+5U^2=0` retain P12 `-k/50`, while
   `V=C+U^2=0` is first-band inconsistent.  Each residual chart is only
   `U`, and the origin was already rebuilt raw.

4. On `H=0`, the raw P12 certificate applies off

   ```text
   U V P3,  P3=V^4-32V^2U^3+128U^6.
   ```

   `U=0` and `V=0` are closed as above.  The exact raw `P3=0` quotient-field
   replay is deliberately not claimed here; it is the live V16 successor.

5. The corrected B3-local V14 source replay again gives P12 `-k/50`, but its
   actual denominator is not the precharged `T3`.  The exact resultant is

   ```text
   (4/9) V^16 U^32
   (V^2-16U^3)(V^2+2U^3)
   (9V^4-96V^2U^3-128U^6).
   ```

   Therefore this chart does **not** complete the generic cover.  The three
   non-`U,V` resultant components remain raw obligations, split more sharply
   in `B_LOCAL_RESULTANT_STRATA.md`.

## Custody

All six archives were extracted locally only for a short source-hash audit;
every archived `SOURCE.sha256` entry passed.  Their archive/SOURCE hashes are:

| Version | Archive SHA-256 | `SOURCE.sha256` SHA-256 |
|---|---|---|
| V8 | `140107242a5e88b5e76dd6727a8622d6d9656b81d21a26d1ab263dbc67d6003a` | `94c6cc7676c4413f7e8e848ce8409fd5f534ec604e1cf9c500b4e743a4e3d792` |
| V9 | `3faa76bbe24816b72a95d6f314c10064436ce5bb37e92ee112acf571aac38e1b` | `98d3db5c9cf670a3dd3c56a1f31bb4f5835ac846a127813021b4267d483bbb1b` |
| V11 | `26efce91f5521fee2dbb63527a417b52a8e672fca4c03220d187221bd85a76d6` | `fe29e4c8927ba3b48253f9f93d4481027a6740ae8f51ae19458054d197428bcd` |
| V12 | `66fc6a0d5c703ce0695c190922537f55716f3925eb6e2f4fb03194d0b55a7957` | `7f32330f9652af841e41a87f2e693920d2f671cde964f947ac35594844441eba` |
| V14 | `d37407c801f72c5a56d79de4ec839dfaacdd68fee765c1c3efc9619863abc2c0` | `e91833a494b7dce910bdbb5f3aa83bc50e64f7828eb0cf5331b2309ffeed9a4f` |
| V15 | `400b67c58cfc75f01ef6f45982c4c3a29b362bdc12a6f60742d2b6b7f51a60cb` | `c5694c2e3d1b2f57f765bb9002e1cfd7fcad2b9aa380338d39a0c44b4a8b4d8e` |

V11/V12/V14/V15 include on-host source-check output and run metadata.  V8/V9
were harvested before the hardened per-lane metadata wrapper; their custody
is softer: exact archives and empty stderr are pinned, and each stdout ends
in the PASS marker, but no separate on-host rc/meta file survives.  V9 is an
independent fast replay of V8's generic identity, not a hostile review.

V10's precharged-denominator assertion failure and V13's intentionally
aborted origin diagnostic are excluded from this positive checkpoint.  V14
supersedes both with the actual denominator and the full origin source lift.

## Scope

This package establishes only the listed generic opens and raw divisors of
the fixed source-typed three-center section.  It does not yet close `P3=0` or
the three B3-local resultant curves.  It makes no neighborhood, full
centering, boundary/dead-stretch, SP-2, maximum-degree, or JC2 claim.

