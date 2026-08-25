# V2 source-smoke negative control

The first V2 AWS source smoke ran on Box03 in

```text
/home/ubuntu/jobs/max12_912_order3_d1_v2_20260825T203811Z_box03
```

The independent implementation completed rc 0 in 5.72 seconds with maximum
RSS 18,460 KiB:

```text
independent.stdout sha256 = 108b41da1f96b972ba06c1f5e5f5c3f72655f5620b0ffbfb9f89da43e3941992
independent.stderr sha256 = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The parent-comparison adapter then failed rc 1 in 0.16 seconds, maximum RSS
32,236 KiB, before any map comparison.  It called the frozen helper as
`inverse_root(ring,max_q)` although its exact signature is
`inverse_root(ring,m,max_q)`:

```text
source_rows.stdout sha256 = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
source_rows.stderr sha256 = 84dd3e5f7b36a9480a93a77a0cdb9bdfa82bc812a044f8b5dc535d5753ef1a9b
```

This is a source-adapter negative control only.  It supplies no equality,
component, Taylor, existence, or exclusion evidence.  The successor changes
only that call to `inverse_root(ring,m,max_q)` and must run under a fresh tag.
