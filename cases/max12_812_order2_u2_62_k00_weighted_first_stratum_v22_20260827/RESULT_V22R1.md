# V22R1 exact first weighted K00 stratum

Date: 2026-08-27

Status: **EXACT PRODUCER PASS; PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE REVIEW.**

## Exact result

In the normalized unloaded K00 chart at `C6=1`, write a valuation-one
coefficient prefix and a unit `k10` prefix as

```text
d_i=Lambda*x_i+O(Lambda^2),  k10=kappa+O(Lambda),  kappa!=0.
```

Let `Q1,...,Q6` be the quadratic unloaded initials; the exact frozen profile
is `Q1,...,Q5 != 0` and `Q6=0`.  Replaying the frozen complete D3 lift for
the K10 load target cancels all transverse degrees at most three.  Its
degree-four residual is the homogeneous 30-term polynomial `F10` serialized
in `aws_r6b_r1_pass/output/F10_QUARTIC.txt`, SHA-256
`c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8`.
The frozen D4 exact dual pairs with it as `25/45056`, so
`F10` is nonzero modulo the tangent ideal `T=(Q1,...,Q6)`.

Under the honest weight `p10=Lambda^2*k10`, the first canonical contracted
equation on this prefix is therefore

```text
kappa*F10(x)=0                       (weighted grade 6).
```

Because `kappa` is a unit, the open prefix `F10(x)!=0` is excluded.  Exact
Singular computation over `Q` gives

```text
L=(Q1,...,Q6,F10) proper,  affine dim Q[x0,...,x5]/L = 3.
```

Thus the homogeneous closed prefix stratum `V(L)` remains projectively
nonempty; it is the exact next relation/stratum variable for the honest
weighted compiler.

## Controls and custody

- R0 is preserved as a pre-algebra failure: it incorrectly required
  `Q6 != 0`.  R1 requires the exact profile and detects both a nonzero-Q6
  mutation and a zero-Q1 mutation.
- The complete D3-lift sign mutation exposes a lower-degree residual.
- The D4 dual pairing is replayed exactly as `25/45056`.
- R1 AWS cost: 1.47 seconds, maximum RSS 35,512 KiB, zero swap.
- `RESULT.json` SHA-256:
  `920c31841cd96ea4cbac0172f14923b209c3e2a3d00ad8a264299ff592bdd9c4`.
- Evidence manifest SHA-256:
  `99d6b1e6274a30cbffdae87a72e8a42011fe2059a499684c6ac1f28774512ad9`;
  all 14 entries independently rehashed and the manifest is self-excluded.
- R1 source-freeze manifest SHA-256:
  `19c5a44190f685438240fc418fe0a99e419abf71c8d055133e3f14fb05a7751b`.

## Firewall

This is only the grade-6 equation on the valuation-one, `k10(0)!=0`
prefix.  It does not decide the closed `F10=0` branch beyond that grade,
grades 7--19, another coefficient valuation, a full finite jet, an arc,
K00 closure incidence, order two/max twelve, or JC2.  A bare nonzero class
in the contracted quotient is not an arc-exclusion theorem.
