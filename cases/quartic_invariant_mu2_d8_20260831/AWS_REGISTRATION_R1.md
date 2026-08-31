# AWS registration R1: fail-closed equation-count diagnostic

The initial four lanes at basis `d19c494e...` all failed closed before
Singular because the generated equation count differed from the packet's
advertised `57` (and `58` for the target-3 mutation). Their verified evidence
is retained separately. No mathematical output was produced.

R1 changes only the refusal message so that the independently generated
observed count is recorded:

```text
basis     f4f5fb2f77f9cb9048572c49d162a131b121245a
runner    2d26b0f1a2ca2e27d3bc055b07c7d38030fa16cb23ee1a67733dfb3d2a420545
generator 3c9a4495bbd757373340da9f614fae43cee5265d0473294c14f534f40a772841
```

Registered sequential diagnostic lanes on audited r6d:

```text
quartic_inv_mu2_d8_p32003_actual_count_r1_20260831T0600Z_r6d
  instance=i-07eeaf8ba6f0bc419 field=32003 profile=actual engine=std
  memory_kib=16777216 wall=600 expected=FAILED_CLOSED_GENERATOR_WITH_COUNT

quartic_inv_mu2_d8_p32003_target3_count_r1_20260831T0600Z_r6d
  instance=i-07eeaf8ba6f0bc419 field=32003 profile=target3 engine=std
  memory_kib=16777216 wall=600 expected=FAILED_CLOSED_GENERATOR_WITH_COUNT
```

These are diagnostics, not searches. After both counts agree with the exact
relation `target3=actual+1`, update the registered count in a new frozen source
basis and relaunch the actual modular shards. Do not weaken the guard in place.
