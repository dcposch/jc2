# Registration erratum: K3 receiver retry 1

Date: 2026-08-26

The first launcher invocations used relative `source` and `output` arguments.
Both failed before compilation or Singular because `run_aws.sh` changes into
the source root before writing a later output file.  The preserved failed
launcher PIDs were Box03 `172964` and r6d `239970`; neither launched a heavy
payload.

Retry 1 changes only the launcher arguments to absolute paths:

```text
tag=max12_812_order2_disc_triple_k3_q_retry1_20260826T071000Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_triple_k3_q_retry1_20260826T071000Z_box03

tag=max12_812_order2_disc_triple_k3_p32003_retry1_20260826T071000Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_disc_triple_k3_p32003_retry1_20260826T071000Z_r6d
```

The immutable source archive remains SHA-256
`1f9b5dc9565db7886451ca0060e3accf2a62e3d28453855fc36f6da0237fb23d`.
Each retry remains one core, 64 GiB, compiler cap 600 seconds, engine cap
3600 seconds.  No result is preregistered.
