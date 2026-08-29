# Registration: discriminant half-weight K2 direct row identity V3

Date: 2026-08-26

Status: **PREREGISTERED IMMUTABLE DUAL AWS CLIENT; NO RESULT.**

The exact-Q V2 lane timed out only in its two-sided Groebner ideal
comparison.  This V3 client replaces that comparison with the stronger
coefficientwise identities

```text
16*source_l=sum_(j<=l) T_(l,j)(b,e)*analytic_j,  l=1,...,7,
```

where `T` is the unitriangular matrix defined by

```text
q^4+b*v*q^3+e*v^2*q^2=1,  q=A/w,  v=1/w.
```

Registered lanes:

```text
tag=max12_812_order2_disc_halfweight_v3rows_q_20260826T073000Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v3rows_q_20260826T073000Z_box03

tag=max12_812_order2_disc_halfweight_v3rows_p32003_20260826T073000Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v3rows_p32003_20260826T073000Z_r6d
```

Each lane uses one core, 16 GiB virtual-memory cap, 300-second compiler cap,
and 600-second Singular cap.  A timeout or any failed/nonunique sentinel is
no verdict.  This is an exact K2 source/analytic row-equality gate only; it
does not by itself assert a lift, Taylor compatibility, order two, `(8,12)`,
maximum twelve, or JC2.
