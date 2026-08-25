# TD6 raw `B3=0` divisor and fixed three-center closure

Frozen status: **producer-exact set-theoretic closure; hostile review
pending.**  This package concerns only the fixed, previously source-typed
normalized three-center TD6 section

```text
y=s^-1,  x=C s+V s^2+U s^3+t s^4,
p=t^15,  q=t+t^25,
```

with the frozen F1 orbit, pole normalization, zero dead stretch, and
degree-18 coefficient field `E`.  Put

```text
H  = C-3U^2,
B3 = 4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
```

## Exact birational cover of `B3=0`

On `U V != 0`, set `x0=C/U^2`, `y0=V^2/U^3`, and `w=V/U`.  Then
`B3=U^6 b(x0,y0)`, where

```text
b(x0,y0)=4x0^2-4x0y0+24x0+y0^2-20y0+20.
```

The line `y0=tau(x0+5)` through `(-5,0)` gives

```text
x0=(-5tau^2+20tau-4)/(tau-2)^2,
y0=16tau/(tau-2)^2,
U=w^2(tau-2)^2/(16tau),
V=w^3(tau-2)^2/(16tau),
C=w^4(tau-2)^2(-5tau^2+20tau-4)/(256tau^2).
```

The inverse is `w=V/U`, `tau=y0/(x0+5)`.  The producer verifies the raw
`B3` identity, inverse formulas, a plus-one control, and the exact line
factorization

```text
b(x0,tau(x0+5))
 = (x0+5)((tau-2)^2 x0+5tau^2-20tau+4).
```

Thus the only missed affine base point is `(-5,0)`, which lies on `V=0`;
`tau=0` is also on `V=0`; `tau=2` contributes no additional affine point
and the displayed center map collapses it to the origin.  The already frozen
whole `U=0` and `V=0` certificates close these chart boundaries.  No source
scaling or weighted-projective identification is used.

The strengthened V27 replay over `E(tau,w)` has transport rank `3470/3602`,
first-band rank `38/132`, and reduces the genuine 2,893-term P12 through 28
original transported first rows and 1,530 multiplier terms to the constant
unit

```text
-k/50,  k=252-342S+144S^2-36S^3.
```

All 31,874 source-product slots pass explicit polynomial denominator
clearing and a plus-one negative control.  The complete certificate divisor
is

```text
tau^51 w^19 (tau-2)^16 (2tau-1) (tau^2-4tau+2)^6.
```

After the frozen `U=0,V=0,origin` closures, only two new raw factors remain:

1. Over `Q(tau)(w)/(tau^2-4tau+2)`, V22 gives exact ascending and reverse
   replays.  Both have the same ranks and constant P12.  Ascending lifts
   through 28 rows/1,540 terms, checks 31,976 source slots, and has chart
   `w^26`; reverse lifts through 38 rows/2,152 terms, checks 60,121 slots,
   and has chart `w^30`.  Both auxiliary field directions descend.
2. At `tau=1/2`, clean V26 reverse replay over `Q(w)` gives the same ranks,
   reduces the genuine 2,893-term P12 to `-k/50`, lifts through 38 original
   rows/2,152 terms, checks 60,343 source slots, and has complete chart
   `w^34`.  Both dummy auxiliary field directions descend, and the plus-one
   control passes.

Each raw factor is therefore empty off `w=0`; its `w=0` endpoint is the
already frozen origin.  Consequently the whole set-theoretic divisor
`B3=0` is empty in this fixed section.  A clean V26 ascending calculation is
running as an independent mirror; it is not a missing mathematical locus,
because V26 reverse already verifies the cleared identity against original
rows on the complete chart `D(w)`.

## Fixed three-center consequence

The earlier generic three-center certificate kills `D(U H B3)`.  The whole
`U=0` divisor is frozen empty.  The whole `H=0` divisor is frozen empty after
the two independently hostile-confirmed P3 raw-curve closure.  This package
closes the whole `B3=0` divisor.  Hence

```text
A^3_{C,V,U}=D(U H B3) union V(U) union V(H) union V(B3)
```

has no point, over any field extension of `E`, satisfying the transported
first-band/genuine-P12 necessary equations.  This eliminates the entire
fixed source-typed normalized three-center affine section.

## AWS custody and replay

The theorem-producing archive hashes are:

```text
V22  6bdac10742b87029796bab6eee1e4c09754d4dedf68bc90ce63ea41be267cc69
V26  b96ebc627c1be7a07691428aa7d8eca10fe70af0e2599f62929989080517e053
V27  7dc12cbb62da27fedb412a2bb7578a98b04f7a46e006ba1ca28b73a2127899fd
```

Their `SOURCE.sha256` hashes are respectively
`11398d2f03c148cde4fc8fdf438e3ceb0f45ccff6cb267ea5ff7961856f6f51f`,
`93cf77eaf4805b562c1fc6a862fde317538781555b1de5cf0c8d8fef0c3853cb`,
and `7e16abea9a7dc0a62a09a9442b0a066b9ea7bc9f8645ea9f1c9d9e4d162ee8d2`.
Every on-host source check passed with empty stderr.  The nonempty lane
stderr files are `/usr/bin/time -v` reports ending with exit status zero.
The superseded V24 generic archive/evidence is retained as a precursor, not
used as the strengthened per-slot proof step.  Dirty-custody V25 is absent
from this package.

After verifying each archive's `SOURCE.sha256`, run on AWS with
python-flint 0.9.0:

```sh
# V27 payload
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py \
  --stratum=b3-param

# V22 payload
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py \
  --component=b3tq
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py \
  --component=b3tq --reverse-first

# V26 payload
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py \
  --component=b3half --reverse-first
```

## Scope quarantine

This is a theorem only about the fixed source-typed normalized
three-center section.  It does not vary the q-boundary, p-boundary stratum,
the eleven dead-stretch coefficients, F1 orbit, pole scale/data, or other TD6
moduli.  It is not a neighborhood theorem, a whole-TD6 or SP-2 kill, a
maximum-degree theorem, or a proof/disproof of JC2.
