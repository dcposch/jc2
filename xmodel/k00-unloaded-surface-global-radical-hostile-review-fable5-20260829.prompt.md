# Hostile review: exact global radical of the unloaded K00 rows

You are Fable 5, an independent hostile reviewer in the plane Jacobian-
conjecture campaign. Write only
`xmodel/k00-unloaded-surface-global-radical-hostile-review-fable5-20260829.md`.

Read `COORDINATION.md` and the artifacts below. Do not inspect, list, search,
stat, build, modify, or control `jc2-lean`. Use scoped git commands excluding
it. Do not launch any local CAS process; heavy or uncertain computation is
AWS-only. Seconds-scale exact Python-stdlib checks are allowed. Use
`apply_patch` for the deliverable.

Pinned claim and evidence:

```text
producer report full/body:
  xmodel/k00-unloaded-surface-global-radical-sol56-20260829.md
  body 41d6460a0f1228f192f67c98c75accdfa3d7ccb29d6dda080015ea8393f50959
portable case:
  cases/max12_812_order2_u2_62_k00_unloaded_surface_local_v1_20260829/
source prelude:
  5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a
V4 producer:
  bb95d104e6d5ddfb31a59c88a782a584c3a836134b041ad0d4a5ea6caede53ef
V4 custody manifest:
  8f307a03fadc8d610fda151f671d815ae8bc3dd7ceee233593743018e65b81f4
independent replay script/stdout:
  a14e3f84ff95adbb6e799aaa663fd16f2152fbcac0e439547c6aba4ef8354f4e
  d8c59b0e86d88557b30511648dff1279fc5b5535779f6028a6165d74fe2a9614
```

The claim is `sqrt(I)=J` in `Q[d0,...,d5]`, where `I` is the seven frozen
unloaded rows and

```text
J=(d0-2d4-d4^2, 8d1-(1+d4)d3,
   d2-d4-16d3^2, d5-2d3).
```

Required attacks:

1. Verify every seal and custody hash, including all 28 multiplier files.
   Confirm the producer/replay stdout markers and that no zero-byte or live
   output is read as a verdict.
2. Independently check the two-containment proof. Establish `I subset J`
   directly from the frozen rows, establish that `J` is prime without using
   `minAssGTZ`, and check that the four serialized identities really are
   `f_i^5=sum_j c_ij*r_j` in the original seven-row presentation. Do not use
   the producer's in-memory `liftstd` replay as a substitute for this check.
3. Inspect the V1--V4 repair ledger. In particular verify that V3's matrix
   serialization contains only the first vector entry and that V4 plus the
   fresh replay genuinely repairs this rather than merely restating the
   in-memory result. Add independent input and certificate mutations.
4. Decide whether exponent five is proved only sufficient or also the first
   power for each displayed generator, and keep that issue separate from the
   radical equality.
5. Audit the exact functor-of-points consequence: fields, reduced
   Q-algebras, and formal-series domains. Attack any illicit inference to a
   nonreduced ring, a mixed loaded source equation, an associated-graded
   step, ramification reduction, attainment, maps, or JC2.
6. Compare the independent minimal-prime output only as corroboration; the
   verdict must stand or fall on the direct identities and primality proof.

Give a crisp `CONFIRM`, `CONFIRM_WITH_CORRECTIONS`, or `REJECT` verdict and a
promotion recommendation. End with standalone `<!-- BODY-END -->`; do not add
a seal block.
