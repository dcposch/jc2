# TD6 AWS handoff — 2026-08-24

Requirements: Python 3.14 (or compatible Python 3), `python-flint`, enough RAM
to avoid swapping, and the extracted directory layout rooted at `jc2/`.
All runs are deterministic exact arithmetic; no network access is used after
dependencies are installed.

Run from the directory containing `jc2`.

## Priority 1: portable eps^2 freeze replay

```sh
python3 jc2/cases/td6_c1_c3_first_ideal_eps2_20260824/replay.py \
  > jc2/cases/td6_c1_c3_first_ideal_eps2_20260824/replay.stdout \
  2> jc2/cases/td6_c1_c3_first_ideal_eps2_20260824/replay.stderr
```

Expected terminal marker:

```text
second-order reduction/source replay PASS
```

The final JSON must report transport rank 3470/3602, first rank 38/132,
base `-k/50`, zero eps and eps^2 remainders, 28 original rows/1489 slots,
nonzero raw eps^2, nonzero varying-pivot counts, and a nonzero frozen-first-
echelon eps^2 negative control.

## Priority 2: generic ascending and B-local two-center identities

These two commands may run on separate instances.

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/generic.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/generic.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  --b-local-pivots \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/b-local.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/b-local.stderr
```

Both must end in `TD6-C1-C3-MPOLY-P12-GENERIC PASS` and reduce the genuine
2,893-term P12 to `-k/50` with full original-row source replay.  The B-local
run additionally executes the denominator-resultant assertions and must emit
`B_local_denominator_unit_off_UH=true`.  Charged exact values are:

```text
B = 4*C^2*U^2 + 24*C*U^4 - 4*C*U + 20*U^6 - 20*U^3 + 1
H = C - 3*U^2
T = 4*C^2*U^2 + 28*C*U^4 - 4*C*U + 24*U^6 - 24*U^3 + 1
ascending multiplier denominator = (1/4)*B*U^2*H^2
ascending termwise clear         = (1/4)*B*U^3*H^3
B-local multiplier denominator   = (1/4)*U^2*T
B-local termwise clear           = (1/4)*U^3*H*T
Res_C(B,T) = 64*U^10
B(C,0) = 1
```

## Priority 3: raw exceptional strata

These three commands are independent and may run on separate instances.

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  --stratum=u-zero \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/u-zero.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/u-zero.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  --stratum=h-zero \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/h-zero.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/h-zero.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  --stratum=intersection \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/intersection.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/intersection.stderr
```

Each run must rebuild transport and the original first-band ideal after
specialization.  If that affine first band is consistent, it must continue
through the genuine P12 and the original-row source relation.  If it is
inconsistent (as the first intersection attempt indicated), the replay must
instead end with `TD6-C1-C3-FIRST-BAND-INCONSISTENT-STRATUM PASS` and emit an
exact nonzero left-null residual lifted back to the original first rows; P12
is then correctly skipped because the stratum is already empty.  Do not infer
a two-center kill unless all recursive pivot factors exposed by `u-zero` and
`h-zero` are either covered by the other chart or rebuilt exactly, including
their intersection.

For an inconsistent first band, the V6 replay prints every exact source-row
coefficient, rechecks the original-row identity, clears all coordinates of
the residual, and reports their common numerator gcd.  Its conservative
certificate chart includes every nonconstant transport pivot event, every
first-row source denominator, and every certificate/residual denominator.
`whole_stratum_empty=true` is emitted only when both the cleared residual gcd
and that complete chart denominator are units.  Otherwise the PASS marker
kills only the printed localization and every factor of the chart denominator
remains a mandatory raw rebuild.

## Priority 4: exact `H=B=0` quotient witness

Run only on the AWS host, after preserving the ordinary `h-zero` output:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  --stratum=h-zero --sparse-pivots \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/h-b-quotient.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/h-b-quotient.stderr
```

This is a fresh raw rebuild on `H=0`, not a specialization of the generic
`1/H` identity.  It must replay the genuine P12 through all original source
rows.  It then audits every transport/raw/first/relation/termwise denominator
against

```text
P(U)=B(3U^2,U)=128U^6-32U^3+1.
```

Only if each gcd with `P` is a unit does it emit an exact termwise-denominator
Bezout identity, reduce every source multiplier in `Q[U]/(P)`, replay the
specialized original-row identity, execute the omit-all-relations negative
control, and end in both `TD6-C1-C3-H-B-QUOTIENT PASS` and the ordinary P12
PASS marker.  A nonunit gcd is a failed cover and requires another raw chart;
it must not be read as a family kill.

## Quarantine

No command licenses a neighbourhood theorem, SP-2 kill, or JC2 conclusion.
The eps^2 and two-center packages retain separate custody.

## Priority 5: raw finite quotient after a failed localized cover

V6 established that both tested `H=0` source relations have a genuine `P`
denominator, so the localized identities do not cover `H=B=0`.  V7 therefore
contains a separate raw quotient producer.  Run it only on AWS:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/h_b_raw_quotient.py \
  > jc2/cases/td6_c1_c3_two_center_cover_20260824/h-b-raw-quotient.stdout \
  2> jc2/cases/td6_c1_c3_two_center_cover_20260824/h-b-raw-quotient.stderr
```

The producer first certifies that
`P=128U^6-32U^3+1` is irreducible and squarefree over `Q`, constructs exact
`K=Q[U]/(P)`, and then rebuilds the entire transport at center
`(3u^2,1,u)`.  It does not specialize any generic echelon or relation.  Every
nonzero quotient pivot is inverted with an exact Bezout check.  It then
rebuilds the first affine band.  An inconsistent first band is accepted only
with an exact original-row witness whose residual has an explicitly checked
inverse.  Otherwise it computes genuine P12, reports the full quotient
remainder without assuming rank 38, lifts it to the original rows, and runs a
negative control.  `H_B_stratum_empty=true` is emitted only for a unit first-
band residual or a constant-unit P12 remainder.  A nonconstant remainder is
an open successor, not a kill.

## Priority 6: generic third center coefficient

The two-center cover does not normalize away `c2`; the reviewed orbit quotient
has three independent center directions.  V8 therefore adds the generic-open
producer

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  > c1-c2-c3-trivariate.stdout 2> c1-c2-c3-trivariate.stderr
```

It rebuilds transport, the first band, and genuine P12 over `Q(C,V,U)` at
center `(C,V,U)`.  It records every nonconstant transport pivot, the selected
transport and first minors with exact factorization, all raw/source/relation
denominators, a full original-row source replay, and a negative control.  A
constant-unit remainder kills only the printed generic open.  Every factor of
every printed pivot or denominator remains a raw-rebuild obligation; the
three-center family is hard-coded as not killed.

V9 is the producer-fast variant: it records exact event polynomials and
canonical SHA/degree/term summaries for accumulated minors and denominators,
but defers their optional global factorization until after the first/P12
verdict.  The V8 factorization lane may continue independently; absence of a
factorization in V9 does not license an exceptional-stratum claim.

## Priority 7: generalized `B3`-local trivariate chart

V10 adds the second generic chart for the full three-center family.  Run only
on the AWS host:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --b-local-pivots3 \
  > c1-c2-c3-trivariate-b-local.stdout \
  2> c1-c2-c3-trivariate-b-local.stderr
```

This rebuilds transport, the first band, and genuine P12 over `Q(C,V,U)`
using a deterministic pivot chooser localized at the V8 first-minor factor

```text
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6.
```

The run must reproduce transport rank 3470/3602 and first rank 38/132,
reduce genuine P12 to `-k/50`, and replay it through 28 original rows.  V10
tested the following extrapolation from the two-center chart:

```text
T3 = 4*C^2*U^2 - 4*C*V^2*U + 28*C*U^4
     + V^4 - 24*V^2*U^3 + 24*U^6
multiplier denominator = (1/4)*U^2*T3
termwise clear         = (1/4)*U^3*(C-3*U^2)*T3
Res_C(B3,T3) = 64*V^4*U^10
B3(C,V,0) = V^4.
```

The source replay reached this final check and showed that the precharged
denominator equality was false.  Therefore these formulas are scheduling
hypotheses, not evidence.  V14 preserves the valid exact source relation,
prints and factors its actual multiplier and termwise denominators, and
computes `Res_C(B3, actual_multiplier_denominator)` directly.  It emits
`B3_local_denominator_unit_off_UHV=true` only if every irreducible resultant
factor is `U` or `V`; no charged equality is required for PASS.

Only after every assertion passes may this chart be combined with the V8
ascending chart to cover the generic locus off `U*(C-3*U^2)*V=0`.  The raw
strata `U=0`, `C-3U^2=0`, and `V=0`, together with all intersections and any
new factors exposed by their rebuilt echelons, remain mandatory.  This run
does not kill the three-center family, a neighborhood, SP-2, or JC2.

## Priority 8: raw three-center exceptional divisors

V11 adds three independent, source-level raw rebuilds.  They may run in
parallel on separate AWS lanes:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=u-zero > tricenter-u-zero.stdout 2> tricenter-u-zero.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=h-zero > tricenter-h-zero.stdout 2> tricenter-h-zero.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=v-zero > tricenter-v-zero.stdout 2> tricenter-v-zero.stderr
```

Here `H=C-3U^2`.  Each command specializes the center before rebuilding the
entire transport matrix; no generic echelon or source relation is
specialized.  An inconsistent first band emits its exact left-null residual,
every original source-row multiplier, the complete denominator chart, and a
PASS marker before skipping P12.  A consistent first band proceeds through
the genuine P12 and exact original-row source replay.  A constant-unit
remainder kills only the printed localization unless the complete
certificate chart is itself a unit.

Transport rank is charged at 3470/3602, but any changed rank or affine
transport compatibility fails closed.  Every nonunit factor in a printed
certificate chart is a new raw-rebuild obligation, including pairwise and
triple intersections.  None of these commands alone licenses a full
three-center, neighborhood, SP-2, or JC2 claim.

## Priority 9: raw `U=H=0` intersection

The U-zero certificate is localized at `C != 0`; because `H=C-3U^2`, its
only uncovered divisor inside `U=0` is the raw intersection `C=U=0`.  V12
rebuilds that intersection over `Q(V)`:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=u-h-zero \
  > tricenter-u-h-zero.stdout 2> tricenter-u-h-zero.stderr
```

The same fail-closed source-certificate rules apply.  This run may complete
the `U=0` divisor only if its exact certificate chart is a unit; otherwise
every printed factor remains a further raw obligation.

## Priority 10: raw center origin

V12 leaves only `V=0` inside its `C=U=0` chart.  V13 rebuilds the triple
intersection from raw source data:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=origin \
  > tricenter-origin.stdout 2> tricenter-origin.stderr
```

An origin kill is valid only if the raw transport/first-band certificate is
exact and has no nonunit chart divisor.  No generic echelon is specialized.

V13 found a constant transport compatibility at the origin but deliberately
failed because it did not retain a source-row lift.  V14 reconstructs the
dependency DAG of that row, replays the exact combination against every
original transport coefficient and RHS coordinate, records the full source
certificate, and executes a plus-one negative control.  Only a unit residual
with a unit complete chart emits `whole_stratum_killed=true`.

## Priority 11: residual curves in the raw `V=0` divisor

The V11 `V=0` source identity has complete chart divisor

```text
U*(C-3U^2)*(C+U^2)*(C+5U^2).
```

The U-zero/origin chain is handled separately.  V15 raw-rebuilds the other
three curves before transport elimination:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=v-h-zero > tricenter-v-h-zero.stdout 2> tricenter-v-h-zero.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=v-cplus1-zero \
  > tricenter-v-cplus1-zero.stdout 2> tricenter-v-cplus1-zero.stderr

python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=v-cplus5-zero \
  > tricenter-v-cplus5-zero.stdout 2> tricenter-v-cplus5-zero.stderr
```

Each curve is over `Q(U)` and meets the already separate U-divisor at the
origin.  Any additional nonunit chart factor exposed by a raw rebuild remains
mandatory; no specialization of the V11 echelon or relation is permitted.

## Priority 12: exact `H=P3=0` quotient-function-field discriminator

V16 adds a source-valid generic replay on the outstanding H-zero divisor

```text
P3 = V^4 - 32 V^2 U^3 + 128 U^6.
```

Run only on an AWS host with python-flint:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py \
  > p3-quotient.stdout 2> p3-quotient.stderr
```

An independent first-stage pivot order is available as

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py \
  --reverse-first > p3-quotient-reverse.stdout 2> p3-quotient-reverse.stderr
```

The field is represented exactly as

```text
Q(U)[Z,V] / (Z^2-32Z+128, V^2-ZU^3).
```

This is an algebraic model of `Frac(Q[U,V]/P3)`, not a weighted scaling:
`Z^2-32Z+128` is irreducible over `Q` and `ZU^3` has odd U-adic valuation,
so the tower and the monic P3 quotient both have degree four over `Q(U)`.
The producer asserts the relations and a plus-one negative control, rebuilds
transport/first/P12, lifts the genuine P12 relation to original transported
first rows, and emits every conservative Q[U] norm/denominator divisor.  A
PASS kills only the printed generic open.  Every remaining U-factor must be
rebuilt raw; no whole-P3, three-center, SP-2, or JC2 claim is encoded.
