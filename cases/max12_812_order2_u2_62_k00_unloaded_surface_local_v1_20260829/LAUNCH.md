# AWS launch registration

Coordinator basis at launch: `9b64db89` (`master`; full commit available from
the repository). Both hosts were directly audited immediately before launch:
no campaign algebra process, zero swap, and more than 120 GiB available RAM.
Box02 and Box03 were explicitly left free for the independent R4-00 deciders.

## `K00-SURFACE-LOCAL-POWER-V1`

```text
instance  i-02cb2b4a379ffcc64  (r6a, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-34
run dir   /home/ubuntu/jc2runs/k00_surface_local_v1
start     2026-08-29T22:11:27Z
wrapper PID 18321; Singular PID 18329 at first post-launch audit
```

This independent local-order screen was resource-cancelled at
`2026-08-29T22:41:14Z` after 1,786 seconds (wrapper rc 1) once the stronger
global power identities had been fully serialized and independently replayed.
It had completed its preflight and local standard basis but emitted no first-
power marker, so it is a non-verdict. Its last audited RSS was about 746 MiB,
with zero swap. No local-radical claim relies on it.

## `K00-SURFACE-GLOBAL-MINASS-V1`

```text
instance  i-0f089e64c378f5da3  (r6b, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-106
run dir   /home/ubuntu/jc2runs/k00_surface_minass_v1
start     2026-08-29T22:11:27Z
wrapper PID 29585; Singular PID 29593 at first post-launch audit
```

## Shipped bytes

```text
ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b  aws_exact_lane.sh
66ce86a51203c04de75a6d7c0f225646a79510e74374c7bf0462706982b7b3f5  run_exact.sh
83eb1ce7fee72e0356fae710ef440fe9cdf7b18b8b3cb6db81ba9ea484b2eafa  local_power.sing
8fd2faa1dcd7feaf149bdf027d7231e374a783039ea99d4d2ce81e0d6a66cdf0  global_minass.sing
5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a  prelude_Q.sing
```

## `K00-SURFACE-GLOBAL-POWER-V3` (early-exit twin)

V2 was initially left untouched on r6c. Its search continued multiplying
each target through power 64 even after discovering a first zero normal form.
V3 is the same exact-Q tracked-certificate route with only that inefficiency
removed: after a first power is found, later loop iterations do no reduction
or multiplication. It runs independently on the now-drained r6b host.

```text
instance  i-0f089e64c378f5da3  (r6b, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-106
run dir   /home/ubuntu/jc2runs/k00_surface_global_power_v3
start     2026-08-29T22:22:27Z
wrapper PID 30529; Singular PID 30537 at first post-launch audit
```

The host was directly audited immediately before launch: no campaign algebra
process, zero swap, and more than 122 GiB available RAM. Shipped V3 bytes:

```text
ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b  aws_exact_lane.sh
f6ba8d1941c93eba783a8f1a8ae233436c7d308eba1a9b4e26b591faa40fd111  run_exact.sh
903d2c3559084f899ed4a77e0f24fe1f2f84325c774c0d99f5c9ed9a81412d3e  global_power.sing
5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a  prelude_Q.sing
```

Both use Singular 4.3.2 and the shared 12-hour fail-closed AWS wrapper. A
running process or zero-byte output is not a verdict. No result is promoted
until output custody, exact containment, and an independently replayable
certificate are checked.

## `K00-SURFACE-GLOBAL-POWER-V1` (harness failure)

```text
instance  i-040b7a1c2ed72d4cc  (r6c, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-150
run dir   /home/ubuntu/jc2runs/k00_surface_global_power_v1
start     2026-08-29T22:17:43Z
end       2026-08-29T22:17:44Z; wrapper rc 0
```

The script stopped at `K00_SURFACE_GLOBAL_POWER_FAIL=BASIS_REPLAY` because
the harness compared a Singular matrix object directly with scalar zero.
This was a harness-only false failure before any power conclusion. The input
containment, mutation, and dimension preflight all passed. V2 replaces every
such check with entrywise polynomial comparison; V1 is retained as negative
custody and is not evidence for or against radical equality.

## `K00-SURFACE-GLOBAL-POWER-V2`

```text
instance  i-040b7a1c2ed72d4cc  (r6c, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-150
run dir   /home/ubuntu/jc2runs/k00_surface_global_power_v2
start     2026-08-29T22:19:13Z
wrapper PID 13543; Singular PID 13551 at first post-launch audit
```

The host was directly re-audited immediately before launch: no campaign
algebra process, zero swap, and more than 122 GiB available RAM. Shipped V2
bytes are:

```text
ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b  aws_exact_lane.sh
dcb3393daad83ac92cbbdfd63329616024b565bca65c2f7adbf798d788874dab  run_exact.sh
20f859f0fe6f251fd581100f9c4e0d35ead35cf2c8f4ad7340bc0923229e7b0d  global_power.sing
5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a  prelude_Q.sing
```

V2 was deliberately terminated at `2026-08-29T22:31:07Z` after V4 had
superseded it with a fully serialized, independently replayed certificate.
It had spent 713 seconds in the inefficient post-hit loop and had emitted no
power marker. Wrapper rc 1 is therefore a resource-cancelled non-verdict, not
a mathematical failure.

## V3 outcome and serialization repair

V3 finished at `2026-08-29T22:22:30Z` in three seconds and found first power
five for every `f0,f1,f2,f5`; all four in-memory identities and the mutation
control passed. Its `write(matrix)` calls serialized only the first entry of
each seven-row multiplier vector (the byte counts agree exactly with V4's
first entries, minus their final newline). Thus V3 is valid producer-screen
evidence but not a portable certificate. V4 repairs serialization explicitly.

## `K00-SURFACE-GLOBAL-POWER-V4` (portable producer)

```text
instance  i-0f089e64c378f5da3  (r6b, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-106
run dir   /home/ubuntu/jc2runs/k00_surface_global_power_v4
start     2026-08-29T22:26:03Z
end       2026-08-29T22:26:06Z; wrapper rc 0
wrapper PID 31362; Singular PID 31370 at first post-launch audit
```

V4 serializes all 28 row multipliers separately and reports exact first power
five for all four surface generators, four successful in-memory identities,
and a successful coefficient mutation. Frozen bytes:

```text
bb95d104e6d5ddfb31a59c88a782a584c3a836134b041ad0d4a5ea6caede53ef  global_power.sing
81c1af14dc0da68a393d926cd70f5f5eab9a0c0955ce29601c07d2350f1630de  run_exact.sh
e7b23ec573d9a72112977e69ec533f5585f575b3931c2ee8e214f2b901ffd87c  K00-SURFACE-GLOBAL-POWER-V4.stdout
8f307a03fadc8d610fda151f671d815ae8bc3dd7ceee233593743018e65b81f4  CUSTODY.sha256
```

The custody manifest fixes the exact prelude, producer, wrapper, metadata,
stdout/stderr, lane log, and all 28 multiplier polynomials.

## `K00-SURFACE-POWER-REPLAY-V1`

```text
instance  i-0f089e64c378f5da3  (r6b, r6i.4xlarge, 16 vCPU / 128 GiB)
host      ip-172-30-0-106
run dir   /home/ubuntu/jc2runs/k00_surface_power_replay_v1
start/end 2026-08-29T22:30:33Z; wrapper rc 0
```

The fresh replay performs no Groebner-basis or lift computation. After
checking every frozen byte, it parses the 28 independent polynomial files,
directly expands all four identities

```text
f_i^5 = sum_(j=1)^7 c_(i,j) r_j,
```

checks `I subset J`, `dim(J)=2`, and rejects both an input mutation and a
certificate mutation. It reports `PASS_K00_SURFACE_EXACT_GLOBAL_RADICAL_J`.

```text
a14e3f84ff95adbb6e799aaa663fd16f2152fbcac0e439547c6aba4ef8354f4e  replay_global_power.sing
3d3fc6cb6462c24238e9d701a3a9f2ef081e7b467c8b06a393f83cdb24c0de75  run_replay.sh
d8c59b0e86d88557b30511648dff1279fc5b5535779f6028a6165d74fe2a9614  replay stdout
2465661920b2da64985175ebf77e394ab08f62d5d049665c9aada263f68571c6  replay stderr
```
