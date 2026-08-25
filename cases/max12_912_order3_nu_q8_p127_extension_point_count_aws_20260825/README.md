# Candidate-H exact extension-field point count

This AWS-only case proves that the smooth projective normalization of the
pinned, reviewed geometrically integral plane curve `H(w,v)=0` over `F_127`
has positive genus.

For every `w` in `F_(127^2)`, `count_shard.py` computes

```text
R_w = gcd(H(w,v), v^(127^2)-v),
S_w = gcd(R_w, H_v(w,v), H_w(w,v)).
```

Because `v^(127^2)-v` is squarefree and has precisely the elements of
`F_(127^2)` as roots, `deg R_w` counts affine rational points in the fibre
and `deg S_w` counts its singular rational points.  The shards partition all
`127^2=16129` values of `w` exactly.  Two independent AWS partitions give

```text
affine points:        16174
singular affine:          6
smooth affine:        16168
P1(F_(127^2)):        16130
```

The 16,168 smooth affine points inject into the normalization.  Were that
normalization genus zero, its reviewed `F_127`-rational smooth point would
identify it with `P1`, which has only 16,130 `F_(127^2)`-points.  Hence its
genus is positive.

## AWS custody

- Box02, tag family `q8_p127_fq2_points_box02_v1_i00..i15`: 16/16 shards
  exited zero; fail-closed aggregate tag
  `q8_p127_fq2_points_box02_v2_aggregate` exited zero.
- r6d, tag family `q8_p127_fq2_points_r6d_v1_i00..i07`: 8/8 shards exited
  zero; fail-closed aggregate tag `q8_p127_fq2_points_r6d_v2_aggregate`
  exited zero.
- The Box02 and r6d partitions use different interval widths but return the
  same three counts.  Maximum shard RSS was 33,508 KiB and 33,664 KiB,
  respectively.
- r6d direct-control tag `q8_p127_fq2_points_direct_control_r6d_v1`
  exhaustively enumerates `v` on fibres `w=0,39,71,a+1` and agrees exactly
  with the gcd-root count on each, including both singular fibres.

The first aggregate wrapper version had an over-strict indentation-sensitive
JSON grep and stopped before aggregation.  Those empty, non-evidentiary V1
aggregate directories remain only inside the raw custody tarballs.  The V2
aggregates repair that software-only defect and are the accepted endpoints.

## Scope

The exact theorem is positive genus of the standalone pinned curve `H` over
`F_127`, conditional only on the separately reviewed geometric-integrality
input.  This case alone proves no quotient membership, source-component
identity, characteristic-zero specialization, trajectory exclusion,
maximum-twelve statement, or Jacobian conjecture conclusion.
