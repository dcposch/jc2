# Frozen V3 result custody

The two `portable_result.tar.gz` files are AWS custody bundles for the exact
`3^13` V3 census.  They deliberately omit the 204 MB fixed-record bytes while
retaining a complete SHA-256 manifest of those bytes at each pinned remote job.

Canonical Box02 run:

```text
/home/ubuntu/jobs/as_q9_signature_census_v3_20260825T0512Z_b
48 shards; exit status 0 in /usr/bin/time output
portable archive SHA-256 526aea430fb2cdea49441667d7b72f3200cf8d4753fb982ccc8a8f6a70ded8d8
remote full-output manifest SHA-256 d816cf2100d4250d83513f507fc94ccc85bd4611b5d37a614d1f2b5ab92c0b08
```

Independent r6d run:

```text
/home/ubuntu/jobs/as_q9_signature_census_v3_independent_20260825T0510Z
37 shards; exit status 0 in /usr/bin/time output
portable archive SHA-256 f864be31e7568a077509ed7205022817a9c166f401b3cc6b65d6b92f2608d488
remote full-output manifest SHA-256 5b384966e7e592a54535ddf5a80d23075774eb2eb0a747d178ec1ade9d2da00c
```

Shard-layout-independent agreement:

```text
record stream     49a563074021509150c03446b1b2257f564c1fa839d57504be12006776206a14
classes table     c42e62a1fc485874ba820912fb5ae7a3cf366f2cf6de9e261dc90d40e8acea72
representatives   cb21c2768374bb003b0b300587b8a6368c6536eb9ff25a49365dfa9435464846
```

Extraction is not required for repository verification: hash both portable
archives against `MANIFEST.sha256`.  Full replay remains an AWS-only operation.
