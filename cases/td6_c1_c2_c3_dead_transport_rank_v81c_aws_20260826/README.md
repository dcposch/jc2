# TD6 V81C generic dead-transport rank certificate

Status: **producer-exact; hostile review pending**.

This case freezes dual-AWS exact source replays for every dead-stretch axis
`d6,...,d16` at symbolic center `(C,V,U)`.  Every one of the 22 executions
returned `rc=0`, replayed all 3,470 original transport pivot rows, reproduced
the frozen V80B point table after `(C,V,U)=(1,1,1)`, and emitted byte-identical
generic tables across r6d and Box03.

## Exact result

The `d10` and `d15` generic compatibility tables are identically empty.  The
other nine columns have an exact lower-triangular minor on the original
source rows

```text
('f','F0',m-20,0),  m=6,7,8,9,11,12,13,14,16,
```

with common nonzero diagonal represented exactly by

```text
(('0','1'),...,('15625/3','1'),...,('0','1')).
```

Its determinant is the ninth power of that nonzero field element.  Since
only those nine dead columns are nonzero, the dead block has exact rank
`9/11` over `E(C,V,U)` and kernel `span(d10,d15)`.  Consuming the separately
hostile-reviewed V78 fact that all 22 q transport compatibility columns are
zero gives the full 33-axis transport rank `9/33` and kernel dimension `24`.

This is a fraction-field transport source-incidence result.  It does not yet
give a denominator-cleared constructible atlas, first/previous/current
compatibility, a nonlinear q/dead neighborhood, a family kill, full TD6,
SP-2, or JC2.  V81B is an independent one-ring aggregate replay; V82/V82S
advance the exact kernel to the first stage without blocking on review.

## Custody

- V81C source archive SHA256:
  `acc26126c64ef0e7746d0abaec8550d0d806a562be6e92bb8b8680383b9f9ff0`.
- r6d run root:
  `/home/ubuntu/runs/td6_v81c_dead_shards_r6d_20260826T0225Z`.
- Box03 run root:
  `/home/ubuntu/runs/td6_v81c_dead_shards_box03_20260826T0225Z`.
- V78 hostile-review dependency SHA256:
  `a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861`.

Run the lightweight custody/triangular checker with:

```bash
python3 cases/td6_c1_c2_c3_dead_transport_rank_v81c_aws_20260826/verify.py
```
