# Max12 `(9,12)` selected-Q8 candidate: exact positive genus over `F_127`

Date: 2026-08-25  
Status: **producer-exact; hostile different-model review required**

## 1. The exact theorem

Let `H(w,v)` be the pinned polynomial of SHA-256

```text
9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce.
```

The report
`max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
and its CONFIRMED hostile review prove that `H=0` is a geometrically integral
affine plane curve over `k=F_127` and that `(w,v)=(71,50)` is smooth and
`k`-rational.  Let `C` be its smooth projective normalization.

**Theorem.** `g(C)>0`.

## 2. Exact count

Put `K=F_(127^2)` and `Q=127^2=16129`.  Python-FLINT chose

```text
K = F_127[a]/(a^2-a+3).
```

Its discriminant is `1-12=116`, and `116^63=-1 mod 127`, so this is indeed
the quadratic field.  For each `w in K`, define in `K[v]`

```text
R_w = gcd(H(w,v), v^Q-v),
S_w = gcd(R_w, H_v(w,v), H_w(w,v)).
```

The derivative of `v^Q-v` is `-1`, so it is squarefree and its roots are
exactly `K`.  Consequently:

- `deg R_w` is the number of distinct `K`-points in the affine fibre over
  `w`;
- `deg S_w` is the number of those points at which both partial derivatives
  vanish;
- `deg R_w-deg S_w` is the number of smooth affine `K`-points in that fibre.

Summing over all `Q` field elements gives exactly

| quantity | exact count |
|---|---:|
| affine `K`-points of `H=0` | 16,174 |
| singular affine `K`-points | 6 |
| smooth affine `K`-points | 16,168 |
| `#P1(K)` | 16,130 |

The 16,168 smooth affine points lift uniquely and distinctly to `C(K)`, so
`#C(K)>=16168`.  If `g(C)=0`, the smooth `k`-rational point over `(71,50)`
would make `C` isomorphic to `P1` over `k`, hence `#C(K)=Q+1=16130`.
This contradicts `16168>16130`; therefore `g(C)>0`.

## 3. Independent exact execution

The portable case is
`cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825/`.

Two complete, independently partitioned AWS runs agree:

| host | tags | shards | aggregate result SHA-256 |
|---|---|---:|---|
| Box02 `ip-172-30-0-186` | `q8_p127_fq2_points_box02_v1_i00..i15` | 16 | `031da7561db2eaffad4ec12310b79ded986964accd35b65e356da4b3b7ac7614` |
| r6d `ip-172-30-0-45` | `q8_p127_fq2_points_r6d_v1_i00..i07` | 8 | `528de912e52df836de5d65219cbb8b29fcdd513817bd88b86777ce7bc01f66bd` |

The JSON differs only in the recorded shard count; the mathematical counts
and field representation agree.  Every one of the 24 shards exited zero.
Maximum shard RSS was below 34 MiB.  A separate r6d direct-enumeration
control checked every `v in K` in the four fibres `w=0,39,71,a+1` and
matched the gcd-root counts exactly; its result SHA is
`9cc104c5d826c607c8e134cbaaf0a187220a0b42fdcc9e54863bf721d1bc24b3`.

The base-field stdlib direct enumerator independently gives 126 affine
`F_127`-points, 124 smooth and two singular; its two-host result SHA is
`e5c9d9bcdca1a568ab2dba6f9fa123573b5e2a8477920f7896d054770bd33777`.
That base-field count is a consistency control only: `124<=128` does not by
itself prove positive genus.

## 4. Scope and composition firewall

This report proves positive genus only for the standalone explicit candidate
curve `H` over `F_127`.  It consumes the reviewed geometric-integrality
theorem but does **not** prove that `H` is a component of the selected-Q8
source quotient or that any characteristic-zero component specializes to it.

The already-frozen positive-genus specialization bypass may consume this
theorem only after its own proper-model, component-membership, and
cross-characteristic attachment hypotheses are mapped exactly.  Until that
composition is reviewed, no `(9,12)` trajectory, maximum-twelve, or JC2
exclusion is asserted here.
