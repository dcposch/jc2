# TD6 V78C: dual-AWS all-q first/P12 source-support shards

Status: **producer-exact; hostile review pending**.

This immutable case is the proof-carrying, latency-sharded companion to the
simultaneous V78B run.  It audits every licensed higher coefficient of

```text
q(t) = t + sum(q_e t^e) + t^25
```

at the fixed source-typed A3 center `(C,V,U)`.  The licensed exponents are

```text
2,3,...,14,16,17,...,24.
```

Exponent 15 is not a source modulus here: it is the lower target-shear gauge
and is explicitly excluded.  Each shard uses one square-zero coordinate and
runs the same exact transport, first-stage reduction, genuine P12 compiler,
original-row source lift, varying-multiplier/lambda-prime calculation,
denominator audit, and omission controls.  The 22 basis calculations were
run independently on Box02 and r6d from one hash-pinned archive.

## Exact result

All 44 AWS executions returned `rc=0` and the standalone marker
`TD6-A3-ALL-Q-VECTOR-AD-P12-SHARD PASS`.  On each host the 22 one-row tables
assemble to the same 23-line table, and the two assembled tables are byte
identical:

```text
e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef
```

The first-stage conormal is zero in every basis direction, hence the joint
22-column first-stage conormal map is zero.  At genuine P12:

- `q2,...,q14` have nonzero exact reduced derivatives;
- every licensed direction `q16,...,q24` has exact zero reduced derivative;
- every direction has 14 nonzero lambda-prime rows, so the zero high-jet
  remainders are source syzygies rather than omitted coefficient variation;
- every computed coefficient denominator has radical contained in
  `U`, `H=C-3U^2`, and
  `B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6`;
- q2 agrees with V32 and q3 agrees with the corrected, hostile-reviewed V77R
  source identity.

Thus the P12 adjoint/source-support tensor has a sharp cutoff after degree
14 on this fixed generic chart.  This does **not** say that higher q jets are
absent from other current rows.

## Scope firewall

The result is only an exact first-order/source-support discriminator on the
fixed source-typed A3 generic open

```text
D(U * (C-3U^2) * B3).
```

The base ideal there is already the unit ideal, so square-zero emptiness is
automatic.  This package proves no nonlinear q-neighborhood, q-family,
all-beta extension away from the fixed A3 source, full TD6 exclusion, SP-2,
or JC2 statement.  V78B simultaneous reconciliation remains a separate
promotion gate.

## Custody

- Source archive: `archives/td6-v78c-sharded-source-20260826.tar.gz`, SHA256
  `b566a57ea50c3f4d24c091f006fe321aa9bb813368049773ee89b347d1284be4`.
- Source manifest: `source/SOURCE.sha256`, SHA256
  `0759921830692966a3e093dcf7eaabd44bbdad5a377e1541dbc742746cb44e03`.
- Shard producer: `source/.../replay_shard.py`, SHA256
  `792f42de85a935a7a09b799caefe6f5a0aeccec104f303dd21cfd43050116493`.
- Box02 run root:
  `/home/ubuntu/runs/td6_v78c_shards_box02_20260826T0030Z`.
- r6d run root:
  `/home/ubuntu/runs/td6_v78c_shards_r6d_20260826T0030Z`.
- Each launch used a 12 GiB virtual-memory cap and a 14,400-second timeout.

The shard source inherits a stale top-level docstring saying “simultaneous”
although `Q_EXPONENTS` is reduced to the requested singleton immediately
after import.  The code, preregistration, launch metadata, stdout, and output
tables all identify the runs as one-coordinate shards; the phrase is prose,
not a mathematical or custody premise.

Run the lightweight custody/union checker with:

```bash
python3 cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/verify.py
```

It reads hashes and text only; it does not execute the producer algebra.
