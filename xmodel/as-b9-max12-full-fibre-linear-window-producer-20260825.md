# B9 fixed-D12 full affine families survive through `3^10`

Status: **producer-exact / dual-AWS same-implementation replay / hostile
review pending**.

The complete fresh-D12 gate over the displayed B9 mod-243 point first gives a
rank-108 affine mod-729 fibre of dimension 74.  Its deterministic RREF
particular does not lift to mod 2187 (dual Box02/r6d result SHA
`b1e4ccbeb2126375f9d58f82b889abc0e43e1ea581da07ab128894f197b2b5d0`),
but that pointwise failure is not a fibre theorem.

The exact full-fibre Bockstein instead gives 70 nonzero left-cokernel affine
equations of rank 39.  They are consistent: the combined rank is 147, the new
kernel dimension is 109, and a 35-dimensional subset of the preceding 74D
fibre lifts.  A focused Box02/Box03 implementation replays this at result SHA
`edd34aea79057b5239d6ab47c86fa56cf9f0f24cfe9b1f751ba3060e196bf464`.

More generally, write the literal parent as

```text
F = F5 + 243*T.
```

The source identity is

```text
det J(F)-1 = D5 + 243*A*T + 243^2*det J(T),
243^2 = 3^10.
```

Therefore the complete families through determinant modulus `3^10` are
exactly linear congruence families.  The source-pinned solver retains all 182
fixed-D12 coefficient variables, all 276 determinant rows, and 8,281 exact
P/Q pair controls.  It obtains:

| determinant modulus | combined rank | affine kernel | projection to prior fibre |
|---:|---:|---:|---:|
| `3^6=729` | 108 | 74 | 0 |
| `3^7=2187` | 147 | 109 | 35 |
| `3^8=6561` | 162 | 129 | 55 |
| `3^9=19683` | 164 | 147 | 73 |
| `3^10=59049` | 164 | 165 | 91 |

Each stage has a literal integer witness with total and partial `y` degrees at
most twelve.  Box02 and Box03 produce byte-identical result JSON SHA-256
`6a2145187e5697890e9838bfb6370505329c01e905abd060310f8b73cd606168`
and stdout SHA-256
`d754ed5d97610f35f31241ec413072966ff6aa6d5c4acbb446cbccd98d7ae836`.
The solver source SHA is
`0bf4766d8e4840fb89661eaba6b8cb4661b554c7f8944f5eb55bac37298f2ac7`.
Runs were `/home/ubuntu/jobs/as_b9_d12_linear_window_3p10_20260825T1640Z`
on Box02 and Box03, both `rc=0`, about 3.5 seconds and under 23 MiB RSS.

The earlier mod-729 correction is independently reproduced by the TD6
owner's distinct zero-row-reduced implementation
`cases/as_b9_max12_w6_next_digit_aws_20260825/`; it finds the same 11-term
RREF particular and rank/kernel.  This is parallel corroboration, not an
independent mathematical solution or hostile review.

## Exact nonlinear boundary and refusal scope

The term `3^10 det J(T)` vanishes modulo `3^10`.  It first enters after
division by `3^10` when lifting a mod-`3^10` family to mod
`3^11=177147`.  That full 165-dimensional quadratic-carry gate is the next
task; no further linear Bockstein is licensed.

The theorem covers only the full staged affine families over one displayed
B9 mod-243 point.  It does not cover the complete earlier mod-243 fibre,
supply an inverse limit or `Z_3` point, produce a characteristic-zero map or
collision, prove a maximum-twelve statement, or settle JC2.
