# V16 producer failure

Date: 2026-08-27

Status: **CUSTODY-PRESERVED FAILED DESIGN; NOT A MATHEMATICAL ENDPOINT.**

Both the exact-Q lane and the independent `p=65521` software-control lane
replayed all 87 frozen polynomial syzygy generators and serialized all 609
origin constants.  They then reached

```text
K00_SYZPROJ_FAIL=NO_COORD6_FREEDOM
```

The preregistration correctly said that either mathematical outcome was in
scope, but the producer incorrectly made the no-freedom branch a process
failure and therefore could not emit a complete endpoint or fresh serialized
replay.  Nothing from V16 is promotable as a theorem.  The harvested partial
artifacts are retained under `aws_q_box01_failed/` and
`aws_p65521_r6a_failed/`; V16R1 is a new, immutable, genuinely both-outcome
producer.

