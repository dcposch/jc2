# TD6 q2-beta family on the raw `U=0` center divisor

Frozen status: **producer-exact narrow theorem; hostile review pending.**

This package concerns only the previously source-typed normalized TD6
section

```text
y=s^-1,
x=C s+V s^2+U s^3+t s^4,
p=t^15,
q_beta=t+beta*t^2+t^25,
```

with the frozen F1 orbit, pole normalization/data, zero dead stretch,
fixed p-boundary, and coefficient field `E`.  It rebuilds the whole
transport and first-J band after the exact raw specialization `U=0`; beta
is a genuine polynomial parameter and the direct term
`q_beta'=1+2 beta t+25t^24` is retained.

## Exact result

The AWS V33 replay gives transport rank `3470/3602`.  The first-J system has
rank `36/132` and one dependent original row, keyed `('X-2',14)`.  Its exact
compatibility has beta-degree zero.  The producer replays its 14-row source
combination against the original first-J rows, computes the monic
compatibility-ideal generator with an exact Bezout coefficient, and asserts
the identity.  The result is

```text
compatibility gcd = 1,
complete certificate denominator = 1.
```

Thus no beta specialization can repair the incompatibility, and there is no
residual `C`- or `V`-factor: the entire raw `U=0` center divisor is empty in
this fixed source-typed q2-beta family, over every extension of `E`.

This is stronger than the earlier beta-zero raw certificate, but it remains
a theorem only about this fixed normalized section.  It is not a
neighborhood theorem in the other TD6 moduli.

## AWS custody and replay

Host/tag:

```text
r6d / 100.26.198.153
td6_v33_n13_u-zero_r6d_20260825T0528Z
```

The source archive is `archives/td6-aws-handoff-20260825-v33.tar.gz`, SHA256

```text
718457551eab373d043e9b711aa8df06fc18fccecb31bb97c2250284f55c48e2
```

Its V33 source manifest has SHA256
`dbca25673571f125cd949617f9879721db45541368a25b4b9b94042357782350`.
The recursive, V31, and V33 source checks all passed on the AWS host with
empty check stderr.

The theorem output `evidence/n13-u-zero.stdout` has SHA256
`94e2267d62b162f44abaf32d36405440dd213e1efb4f446cc281ace08b47d0da`.
The run exited zero in 22.78 seconds with maximum RSS 201132 KB.  Its stderr
SHA256 is
`63de97c9cac23252a736da9d02b14f874ee0e9e30ec0e4c3373f5c5d25fb6791`;
it contains only archive xattr warnings and `/usr/bin/time -v`, ending in
`Exit status: 0`.

After extracting on AWS with python-flint 0.9.0:

```sh
sha256sum -c SOURCE.sha256
sha256sum -c V31_SOURCE.sha256
sha256sum -c V33_SOURCE.sha256
python3 jc2/cases/td6_c1_c2_c3_q2_n13_raw_20260825/replay.py \
  --stratum=u-zero
```

## Scope quarantine

No claim is made about `U!=0`, the H or B3 center divisors, other center
coefficients, p-boundary strata, dead-stretch coefficients, F1 orbit, pole
scale/data, the whole TD6 family, SP-2, degree landing, or JC2.
