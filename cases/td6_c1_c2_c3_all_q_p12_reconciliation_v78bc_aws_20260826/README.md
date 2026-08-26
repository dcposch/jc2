# TD6 V78B/V78C simultaneous–shard reconciliation

Status: **producer-exact reconciliation PASS; V78C hostile review live**.

This immutable supplement closes the preregistered agreement gate between:

- two simultaneous 22-coordinate square-zero V78B calculations; and
- the two-host, 44-run proof-carrying V78C basis-shard package frozen at
  `cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/`.

Both simultaneous V78B runs returned `rc=0` and the standalone marker
`TD6-A3-ALL-Q-VECTOR-AD-P12 PASS`:

| Host | Runtime | max RSS | stdout SHA256 |
|---|---:|---:|---|
| Box02 | 1:12:39 | 505,184 KiB | `410bacc38d39f7987c39d351dd8b55679fecc4d77cafa49e77d48249e2d95644` |
| r6d | 1:05:14 | 504,608 KiB | `118dcb50d003b24b445cb1968111fef4073d91f33725f6f77927e23105a6f5eb` |

The Box02 simultaneous table, r6d simultaneous table, Box02 assembled shard
union, and r6d assembled shard union are byte identical.  Their common SHA256
is

```text
e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef.
```

This confirms that restricting the joint square-zero source calculation to
the 22 standard basis vectors loses no cross-coordinate linear term.  It also
independently corroborates every row of the shard union.

The exact mathematical scope is unchanged from V78C: first-order conormal and
genuine-P12 source-support data on the fixed source-typed A3 generic open
`D(U*(C-3U^2)*B3)`.  The base ideal is already the unit ideal.  There is no
nonlinear q-neighborhood, family, other-current-row, full-TD6, SP-2, or JC2
claim.

Source archive SHA256:
`cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579`.

Run `python3 verify.py` from this directory or the repository root.  The
checker only reads frozen text and hashes; it does not execute producer
algebra.
