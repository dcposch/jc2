# Custody

```text
7c102bb2d00f957f64a198374f6614f5052cdf849ef106d345a89f2ada39431f  PREREGISTRATION.md
49f4140d21365aa566dcb6de8cb0200a74d02efa1d5e4182496cbe1e3404d214  PREREGISTRATION.sha256
fc2a5c2e723acbbbe39ebb2df4be14a2039b5af73c698ecfbab96f630336b2f6  SOURCE.sha256
f2e21770e9568ab19e5d5088d9dcf6dc36586bb461f99e946451fbb5da0ec990  custody/ggv_lambda0_quotient_nf_rank_r4_SOURCE.tar.gz
6fd7c8687e241bb1959b9a61c7f44702f1250bf4c5ec220d30968b9209bff3e5  custody/ggv_lambda0_quotient_nf_q1p03_r4_20260828T155000Z_r6g.terminal.tar.gz
3f54f3c65d816d922fbb9bc9ed43535246d431a1ad80d72da9bafe78c4c81b75  archived output/backend_selfcheck.stdout
```

The terminal archive replays 33 of 34 internal `EVIDENCE.sha256` entries.
The sole mismatch is `records/CUSTODIAN.stdout`: it was empty when the runner
hashed evidence, then received the runner's final five-line status after that
hash.  Expected empty-file SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
archived post-status SHA-256
`5bf59c3bb398654c7ec050e501efdd2a902763f8aaf776c2c20b818942da4a28`.
This custody-adapter defect is explicit and preserved.  The archive itself is
frozen by its exact SHA-256 above; the successor redirects custodian output
outside the evidence tree so no post-hash evidence member can mutate.

