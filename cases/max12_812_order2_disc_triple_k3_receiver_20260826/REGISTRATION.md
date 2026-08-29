# Registration: correction-aware discriminant triple-root K3 receiver

Date: 2026-08-26

Status: **PREREGISTERED AWS-ONLY DUAL LANE; NO RESULT.**

```text
tag=max12_812_order2_disc_triple_k3_q_20260826T071000Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_triple_k3_q_20260826T071000Z_box03

tag=max12_812_order2_disc_triple_k3_p32003_20260826T071000Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_disc_triple_k3_p32003_20260826T071000Z_r6d
```

Each lane is one core, at most 64 GiB virtual memory, with a 600-second
compiler cap and a 3600-second Singular cap.  The exact-Q lane must wait for
or avoid contention with the still-live full-source exact-Q V2 process on
Box03.  The modular lane may launch independently once the immutable package
is frozen and copied.

The endpoint is a K3 necessary gate only.  Taylor is charged but not
compiled, and full-source promotion remains conditional on the separate
exact-Q V2 source/analytic ideal comparison.
