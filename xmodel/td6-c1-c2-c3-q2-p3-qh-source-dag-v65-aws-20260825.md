# TD6 q2-beta P3/QH source-DAG gate — V65 AWS

Status: **producer-exact localized original-row theorem; hostile review
pending.**

## Result

In the fixed source-typed normalized A3 q2-beta section, V65 gives exact
source-DAG unit identities on the two exceptional-curve opens

```text
H=P3=0, D(U),
H=QH=0, D(U),
```

where

```text
H  = C - 3 U^2,
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 + 8 V^2 U^3 - 64 U^6.
```

Both exact curve fields have staged ranks

```text
3470/3602 -> 38/132 -> 38/94 -> 25/56.
```

On both components the source-replayed current row 13 is
`N13=(k/25) beta`.  It depends on exactly previous row `('X-1',14)` and
original first rows.  Previous row `('X-1',0)` is replayed only as an
independent quadratic positive control.  The genuine 2,885-term P12 relation
uses 28 nonzero original first rows and composes with N13 to the unit
`-k/50`.

The complete denominator ledger has radical `{U}` and chart `U^13`; no
other curve divisor is hidden.  Hence these are all-beta emptiness
certificates on `D(U)`, but not whole-curve certificates inside this package.
The raw `U=0` endpoint remains a separately sourced theorem.  In particular,
this report makes no whole-H or whole-A3 composition claim.

The QH execution independently checks, on `D(U)`, the exact normalized
Bezout identity

```text
((5T-136)(T^2+8T-64) - (5T+64)(T^2-32T+128))/512 = 1,
T=V^2/U^3.
```

Thus the P3 and QH divisors are disjoint on `D(U)`.  The identity is a cover
check; the two source-DAG unit identities separately exclude the two curves.

## Source fidelity

The frozen archive SHA is
`eb481ca9e686a5fec349c5ce42915cd032d0096aee53f7a33b156ec5598edb6f`.
The case manifest SHA is
`8cb2736e2bbd310bf5b2dbadce756c2e4513f38beb4bfb2fb43d1e378dd00b45`;
all entries and the lightweight portable verifier pass.
The exact curve source is hash-pinned at `f8c46d2c...`.  The producer retains
`q_beta=t+beta*t^2+t^25`, direct
`q_beta'=1+2 beta t+25 t^24`, `p=t^15`, frozen F1/pole/dead-stretch data,
and arbitrary-degree original source rows.  It applies no weighted source
scaling.

The two full runs on Box02 and r6d used identical source under 12-GiB caps.
After replacing only the absolute artifact directory, their stdout is
byte-identical:

```text
P3 normalized stdout SHA  2ab37f8da764f5b44df6c931897aa83bee077f1fd449f89d2617075e03d89b4a
QH normalized stdout SHA  bc5e95c35459ea96b628e4816e90bade0d2c81bbaa8eb78db3dd3f1a21e6c55c
```

The emitted proof-DAG/denominator-ledger SHAs are respectively
`52eada0a...` / `0befb53e...` for P3 and
`4efbee5f...` / `887f8ce6...` for QH, identical across hosts.  Maximum RSS
was about 3.06 GiB and every theorem run exited zero.

The direct-qprime omission control is preserved separately.  It prints
`direct_qprime_omission_changes_N13=true` and then exits one at a reporter
lookup because the N13 record is absent.  Its rc-one stream is a negative
control and is not used as theorem evidence.

## Exact scope and next gate

This package is eligible to compose with the separately hostile-reviewed
raw `U=0` theorem and the reviewed V64/V62D H-cover leaves only after its own
hostile source/denominator review.  Such a composition would be a theorem
about `H=0` in this fixed A3 q2-beta section, not TD6 generally.

Refused conclusions: whole P3 or QH curve in this package; whole H; whole
A3; another boundary, center, pole, F1, or dead-stretch modulus; TD6; SP-2;
landing; a cofinal complexity bound; or JC2.
