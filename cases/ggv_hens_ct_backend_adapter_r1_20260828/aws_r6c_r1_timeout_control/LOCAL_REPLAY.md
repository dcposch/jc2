# Local custody replay

Replay date: 2026-08-28.

The remote archive SHA-256 and the locally fetched byte SHA-256 agree:

```text
00963a460db79d21d152d2d3a47cf2aa1a3e6d23c6482714fdf500fc5f9e8891  JOB_ARCHIVE.tar.gz
```

The archive extracted to 231 frozen files.  Every extracted file replayed
against the remote `FILES.sha256` manifest.  Principal evidence hashes are:

```text
15df00260867a35b4faf83ff753c299f4c59ca4213bed6014dc034c1479040c2  output/TERMINAL
3a03c86f8abe6d8304311e176718a3c6dfab9695e56f6104c3f3c834e042f61f  output/UPSTREAM_PASS
8daac27d5f064381b4ee1066a8a4e3479294db3a694cbb67024ec2257d1c2969  output/upstream_certificate.json
8224986202d67e1ea07711d5cd59512b2303542ecc727ae1539d7dd288e751fe  output/bridge_probe.json
1447cced82b80e1b8fa5c370bb88e007f7d14120c62de9af46af33be06d88a77  output/run_metadata.json
e3f04796cbbe8e79fd80197b0c9c324bb06fb3375ac6484907f938ed32766638  records/FINAL_CENSUS.json
f2c12fec08c3ad5872e7cf64cc70670d383afcc5fa9f3dc0a24676b9706f1527  records/EVIDENCE.sha256
4d371e85b574eec164a580caa1419933db7a2fcf6168df275571c2c72414abc2  records/MUTATIONS.sha256
a7cd422fa3ca9ab2c6ef90ebea3277092bf5a037ae92e458a7fb4bd01f2d2f2b  records/ORE_MUTATIONS.diff
```

The certificate JSON records `exact_certificate=true`,
`ore_membership_remainder="0"`, and `direct_field_remainder="0"`.  No local
computer-algebra rerun was attempted; the exact AWS verification and its full
toolchain/mutation custody are preserved instead.

