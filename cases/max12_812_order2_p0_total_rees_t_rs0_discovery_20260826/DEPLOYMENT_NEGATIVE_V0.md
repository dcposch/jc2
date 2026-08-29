# Deployment negative: `T-rs-0` discovery V0

Date: 2026-08-26

The first two-prime deployment stopped in the compiler on both Box02 and
Box03 before emitting a Singular input.  The expected SHA for the frozen raw
cusp V2 compiler had been transcribed as

```text
8abeda326406b789ad54e9692304884963567cb672b3f7a27b3e68344a90982b
```

while the locally and remotely identical file is

```text
8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d.
```

Both deployments returned `compiler_rc=1`; neither created a compiled
Singular file, invoked Singular, or produced any mathematical output.  The
failed tags are

```text
max12_812_order2_p0_total_rees_t_rs0_discovery_20260826T182200Z_p32003_v0
max12_812_order2_p0_total_rees_t_rs0_discovery_20260826T182200Z_p65521_v0.
```

V0 is therefore a deployment-only negative with no source-fidelity, support,
common-order, total-Rees, or campaign verdict.  V0R1 changes only the
expected hash literal and is launched from a fresh archive.
