# V89H7 V1 packaging-negative erratum

Date: 2026-08-26

Both V1 AWS replicas exited 1 before any algebraic construction.  The
minimized archive contained the pinned top-level `replay_shard.py` but omitted
its frozen nested import

```text
payload/jc2/cases/td6_c1_c2_c3_q2_beta_dual_20260825/replay.py
```

The failure is identical on Box02 and r6d and is classified strictly as a
source-packaging negative.  It provides no mathematical evidence and does
not alter V89H6 or the preregistered V89H7 functional.

V1 custody:

```text
source archive SHA256 = 47510931506c231b468636f4536bd211235a5a6e8940cc00c085c51eb72eda1e
SOURCE manifest SHA256 = 64f21a0a513b1a7a954443162af0e31e4c56043debd55eceecb934a6d037f88f
Box02 stdout SHA256 = 7df92a2ad82c06d544121aee58787768ad396cab15c237291ddb63b783b18ce3
r6d stdout SHA256 = 7df92a2ad82c06d544121aee58787768ad396cab15c237291ddb63b783b18ce3
```

The controlling repair includes the complete 56-file non-bytecode payload
closure under an independently checked `PAYLOAD_CLOSURE.sha256`; no source
formula or functional choice changes.

