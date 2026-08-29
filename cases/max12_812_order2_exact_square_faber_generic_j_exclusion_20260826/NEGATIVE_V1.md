# V1 deployment-negative custody

Date: 2026-08-26

Both preregistered V1 AWS lanes are preserved in
`aws_q_v1_negative/` and `aws_p65521_v1_negative/`.  Their compilers and
Singular engines returned zero, but the validators correctly failed on the
missing affine-graph endpoint.  Singular had parsed expressions such as

```text
p^2/4-D
Kvec^2/16
```

as attempts to raise a polynomial to a nonintegral exponent.  The stdout
contains explicit `poly ^ number failed` diagnostics.  Therefore V1 has no
mathematical status and none of its partially printed identities is
consumable.

V2 changes only parenthesization of powers immediately before division,
for example `(p^2)/4-D` and `(Kvec^2)/16`.  It changes no ring, source tail,
coordinate substitution, proposed identity, open set, or scope statement.

V1 tags:

```text
max12_812_order2_faber_generic_j_20260826T131036Z_q
max12_812_order2_faber_generic_j_20260826T131036Z_p65521
```

