# TD6 V89H1 high-tail triangular integrability result

Date: 2026-08-26

Producer verdict: **FAIL CLOSED at the denominator gate on both AWS hosts.**
The calculation found a useful exact triangular reduction, but no theorem on
the registered `D(U H B3)` open.

## V1 deployment-only failure

The V1 wrappers omitted the frozen ancestry sentinel `TD6_Q_EXPONENT=2`.
Both runs stopped before source import or algebra with rc=1. The immutable V1
failure is documented in `DEPLOYMENT_ERRATUM.md` and is not mathematical
evidence.

## V2 exact algebra

Set `q2,...,q14=0`, retain independent untruncated
`q16,...,q24`, and keep q15 absent under its separately reviewed target
shear. The V2 client rebuilt literal V87 transport, 38 packed raw FIRST maps,
and genuine raw P12. It reproduced every frozen V85 q-zero source digest.

For the reviewed q-zero FIRST pivot block,

```text
B(q)=A0^(-1) A(q)=I+N(q),
```

the exact graph has 242 edges and is acyclic. All edges run from rows 14
through 36 to columns 0 through 13, so `N^2=0`; the finite inverse is exactly
`I-N`. Both sides of that inverse and the normalized FIRST combinations of
the original sources replayed exactly.

Reducing literal P12 by these normalized FIRST rows left exactly the reviewed
q-zero term and no positive high-q term. The remainder file is byte-identical
on both hosts. Reconstruction from the original FIRST sources, an active
FIRST omission, and P12 omission all passed.

These checks are algebraically informative but not sufficient for a source
certificate.

## Load-bearing failure

The final audit found the unregistered factor

```text
K = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6
```

in the common denominator. The exact factorization is

```text
(1/8) * K * B3 * U^2 * H^2.
```

Because K is not one of `U,H,B3`, both runs deliberately raised at the
denominator gate and returned rc=1. They did not run the post-clear scalar
coordinate audit, did not emit a final exact-result record, and did not print
a PASS banner. The proposed high-tail collapse on `D(U H B3)` is withdrawn.

K is exactly twice the `R38` selected-minor factor frozen in V83. V83's
certified FIRST-rank open is `D(U H B3 R38)` and its README explicitly leaves
`R38=0` as alternate-minor/raw-fibre debt. H1 therefore rediscovers that
known FIRST pivot-open boundary; it does not license or remove it. The V83
custody has `MANIFEST.sha256` SHA256
`355686c91424b05d21a7a03f8052028b7d32a67b1dbfe948c0d7c3c00121227e`;
the V83 `FREEZE.sha256` file itself has SHA256
`dfafe95a1c993e6181398eab8c84e0699ac4f8785e96e5adb36660e42f6d74f1`.

## Frozen partial artifacts

- source archive:
  `6869022c70203f1ec7559a599d935f14f425e7ca7663749b000b3e0c55ccdff1`;
- source manifest:
  `69523a341e8ec9b2f0ab02c5e0d1dbd52ee626270b1004dd645aeabb56b5493d`;
- client:
  `0cef7dfe63768c3bc4d9bb9ec99639768b08fd16a8eaecced42d0d6dca469697`;
- triangular graph:
  `318e11dfaa06cd99d82cc4e707b99c57374a17dcdc7c5b9442c7590c395cc45f`;
- P12 remainder:
  `763e0d82ebf5e59c58cf0b91914b0d84e27190b75c63b0bfa73ede9a042e0a41`;
- original-source multiplier inventory:
  `bd94a9036ff549115f72cb6ed66032478796d1c17a61a492db6966710ce5e6f6`;
- byte-identical V2 mathematical stdout:
  `dcd5b4d53174bd13735f13b37eee007e33e9b89f99ea83ad48dd09504935725f`;
- K formula:
  `2db6935d74924896248fa192120888d8067004a314e4f8fc41c581a7675c2f87`.

The host stderr differs only in paths and timing. Both contain the same exact
factorization and fail at the same assertion.

## Scope firewall and next gates

This negative result concerns only the high-tail reduction on the retained
normalized source slice. It does not prove a source point or
nonintegrability. The smallest next gates are to determine whether K is a
known licensed chart factor, prove K is a unit modulo the literal q-zero
source ideal, cover K=0, or find a registered alternate pivot/certificate.
No fixed-A3, TD6, SP-2, or JC2 conclusion follows.
