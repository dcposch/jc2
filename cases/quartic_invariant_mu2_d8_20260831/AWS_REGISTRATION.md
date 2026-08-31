# AWS registration: initial degree-eight reconnaissance

Frozen source basis: `d19c494ec2b8d0eb994089eafac8655e19e03195`.

```text
runner    2d26b0f1a2ca2e27d3bc055b07c7d38030fa16cb23ee1a67733dfb3d2a420545
generator 44f2d1a47fdd9ee7cfbf8916ab1bf224879f99f3f2f3d9b85efcb773c986be79
```

Initial independent lanes:

| host | instance | suffix | field | profile | engine | memory KiB | wall seconds |
|---|---|---|---:|---|---|---:|---:|
| r6a | `i-02cb2b4a379ffcc64` | `p32003_actual_slimgb_20260831T0550Z_r6a` | 32003 | actual | slimgb | 94371840 | 7200 |
| r6b | `i-0f089e64c378f5da3` | `p65521_actual_std_20260831T0550Z_r6b` | 65521 | actual | std | 94371840 | 7200 |
| r6c | `i-040b7a1c2ed72d4cc` | `p104729_actual_slimgb_20260831T0550Z_r6c` | 104729 | actual | slimgb | 94371840 | 7200 |
| r6d | `i-07eeaf8ba6f0bc419` | `p32003_target3_std_20260831T0550Z_r6d` | 32003 | target3 | std | 16777216 | 600 |

The dropped-equation control is registered for r6d only after the target-3
lane terminates and its evidence manifest is verified:

```text
suffix=p32003_drop_last_slimgb_20260831T0550Z_r6d
field=32003 profile=drop_last engine=slimgb memory_kib=100663296 wall=7200
```

Before every launch, `launch_host.sh` resolves the current IP from the pinned
instance ID, refreshes the SSH security-group rule, checks EC2 identity, and
refuses a worker already running Singular, msolve, or this D8 route. The
separately owned formalization instance is not queried or controlled.
