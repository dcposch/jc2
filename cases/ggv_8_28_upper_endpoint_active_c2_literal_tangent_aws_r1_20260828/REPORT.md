# Exact-Q tangent certificate: AWS R1 report

UTC execution: 2026-08-28 08:47:19--08:47:29

Verdict: **`TANGENT-OBSTRUCTED-AT-THIS-POINT`**.

The unchanged frozen producer built the preregistered 510-by-308 sparse
system and performed exact sparse elimination over `Q`.  It found rank 291
and a contradiction at source row 494, whose label is `D22[X^0]`.  Before
writing the certificate, the producer replayed the returned left dual and
asserted both `y*A = 0` column by column and `y*b = 1` exactly.  The dual has
support 19: rows `D4[X^0]` through `D22[X^0]`, with coefficients
`1/8^18, 1/8^17, ..., 1/8, 1`.

All three navigation primes `65521`, `65519`, and `65497` independently had
rank 291 and rejected the target at the same row with residual 1.  The
homogeneous zero-target control is satisfied by the literal zero tangent.

## Frozen inputs

- Tangent producer:
  `ddcd7b5d9cc5dd37e56412f606eb4b0fb37bc976280b224ac9dcf91a04be20a1`
- Preregistration:
  `c930cd3570892a56b30140e6436d6903dabc443dac91799ebd81b47da20081e5`
- Tail checker:
  `f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45`
- Upstream checker:
  `112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26`
- Raw compiler / raw source:
  `7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1` /
  `ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`
- Remote frozen-source manifest:
  `9a8727cf34837175326f2c9aa3a68c1567bd3150142d5893c69fe9244051464e`

## Execution custody

Successful immutable namespace:

`/home/ubuntu/jobs/ggv_active_c2_tangent_exact_q_r1_20260828T084624Z_r6i`

Registered PID=PGID=SID was 73832 with Linux start time 29804757.  The
charged command was pinned to CPU 1, nice level +10, a 3,600-second inner
timeout, a 3,700-second outer timeout, 64 GiB address-space limit, and 8 GiB
file-size limit.  It completed in 5.99 seconds wall / 5.97 seconds user,
using 23,760 KiB maximum RSS and zero swaps.  Worker, monitor, probe, and
postcheck return codes were all zero.  The final validated census had zero
members.  The concurrent HENS process group was neither signalled nor
reprioritized.

Two prelaunch namespaces were rejected without registering any process:
the first because the remote AWS CLI was unavailable and instance tags were
not exposed through IMDS; the second because BSD tar had introduced
unrequested AppleDouble sidecars.  The successful source was restaged with
those sidecars excluded, replayed against all 17 content pins, and made
read-only before registration.  EC2 identity/type/region came from DMI and
IMDS; the exact per-job `AWS_RUN_TAG` was enforced.  The campaign's prior
host authorization was not misrepresented as a fresh instance-tag query.

## Artifact hashes

- Exact certificate:
  `d21fc8538e908f9a1bc6705fd9e5cf99a2c3d0be3f3b8a82318906ef817c0a8b`
- Producer stdout / empty stderr:
  `78893e1cb75200ae18ef10a74dac60d6d3ee9f8fb972f1b08f844b8c1199f7cd` /
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- GNU time record:
  `4dbb64ccf4985f27e5d95b8c9d1b72819c3b36e3d98d83e5b31bde14f7fb6888`
- Independent harness postcheck:
  `ed07a2f3d92664e1a7b81978a357b34f31c810b2dfa1129b0c43a54027b8e48d`
- Terminal marker:
  `bb724262debe2e4ada8fbd535d21fe5c0e67776b898d000be39e77f72eab1eda`
- Output manifest / complete evidence manifest:
  `b27b5b12304ddafaebd17cb2ffe3febda01bf7e435b9cade542b12bbd531cbba` /
  `c05ecfff8ddc0af6ecaabbf1209bf770f02ff089b340ae1e56a0d1de17882a85`

The complete read-only remote packet was copied byte-for-byte to
`evidence/remote_job/` beneath this report.

## Scope firewall

This certifies only that the single frozen homogeneous point has no
first-order direction to the affine endpoint inside the complete specified
reduced-prefix/raw-window tangent space.  It does not show scheme isolation,
exclude nonlinear arcs or other base points, settle the deep locus or the
general-`V0` landing bridge, prove a Keller theorem, or resolve JC2.

