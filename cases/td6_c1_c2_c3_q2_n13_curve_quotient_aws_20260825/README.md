# TD6 q2-beta N13 gate on the three exceptional center curves

Frozen status: **producer-exact staged N13 theorem; exact cross-package
all-beta curve closure; hostile review pending.**

This package stays inside the fixed, previously source-typed normalized TD6
section

```text
y=s^-1,
x=C s+V s^2+U s^3+t s^4,
p=t^15,
q_beta=t+beta*t^2+t^25,
```

with frozen F1 orbit, pole normalization/data, zero dead stretch, and
coefficient field `E`.  The direct term
`q_beta'=1+2 beta t+25t^24` is retained.  There is no weighted scaling or
source normalization in the curve rebuilds.

## Exact staged result

Three independent AWS runs rebuild the complete transport, first,
previous/pole, and current systems on the exact function fields of:

1. `p3`: `H=C-3U^2=0` and
   `P3=V^4-32V^2U^3+128U^6=0`;
2. `b3tq`: the `B3=0` birational-chart fibre `t^2-4t+2=0`;
3. `b3half`: the `B3=0` birational-chart fibre `t=1/2`.

Every lane has ranks

```text
transport       3470/3602
first             38/132
previous/pole     38/94
current           25/56
```

and exactly one `('X0',13)` compatibility.  Its exact original-row
left-null replay is

```text
N13 = (k/25)*beta,
k = 252-342S+144S^2-36S^3.
```

The N13 value and left-null hashes agree in all three coefficient fields:

```text
N13                 3ec7708f32ee5817a81c6ad8f29a1c1030d8f558b29c9f0342e7029e3653eda9
left-null ancestry   9d7a330af2b61b3408af4a5d4d27abd8091452593ec3648780d3d4edab54a7a9
```

All transport norms and staged denominators are powers of the single curve
parameter: the full chart is `U^13` on `p3`, `w^23` on `b3tq`, and `w^27`
on `b3half`.  Thus the staged identity is exact off parameter zero and no
unlisted norm factor remains.

## Exact cross-package closure

The earlier hostile-confirmed coefficient-field certificate proves
`k in E^*`; hence on any of these function fields `N13=0` forces `beta=0`.
At `beta=0`, the separately frozen genuine-P12 packages prove the whole
`p3`, `b3tq`, and `b3half` curves empty.  The only locus omitted by the new
charts is parameter zero; on all three center maps that locus is the origin,
which lies in `U=0`.  The separately frozen q2-beta `U=0` theorem is empty
for every beta with a unit compatibility ideal.

Consequently each of the three whole set-theoretic exceptional curves is
empty for every beta in this fixed source scope.  This conclusion is a
composition of separately frozen exact certificates; the producer itself
correctly prints `component_all_beta_killed=false` because it does not load
or replay those dependency packages.

## AWS custody

All lanes used the same archive, SHA256

```text
a36475f22d64dc025bcda19867f8c603c90329f2c4a5ae9281404d4570017151
```

with producer SHA256
`6f2025f0ed76e91c1af154fd97609886cf1e602465381e2cc3fabc9e632ebfa6`
and V42 source-manifest SHA256
`cc866b10459b561b08a809014b6ac9826fab2a5a118140a554b49b384c94ec86`.
Every on-host source-closure check passed.

| component | AWS host/tag | UTC end | rc | stdout SHA256 |
|---|---|---|---:|---|
| `p3` | r6d `td6_v42_n13_p3_r6d_20260825T0637Z` | 06:53:04Z | 0 | `9a8d76fce77ee9d845e4e6ed58a8220a3764e0bfe300c1c7d92a6e9467cdeb9c` |
| `b3tq` | Box03 `td6_v42_n13_b3tq_box03_20260825T0637Z` | 06:54:01Z | 0 | `3980cc27f2cc293a399cf0b61eb0d17679126b2119aa5f2f0088596942887968` |
| `b3half` | r6d `td6_v42_n13_b3half_r6d_20260825T0637Z` | 06:52:08Z | 0 | `a26447dfca805e00fde7f19fe4a646594feba7a4de0e3ba67f3e3aaefc343aac` |

The nonempty stderr files contain only `/usr/bin/time -v`; extraction
warnings are retained separately and do not alter any extracted source byte.

## Scope quarantine

This package closes only these three exceptional curves in the fixed
source-typed A3 center section.  It does not yet close the generic `H=0` or
`B3=0` all-beta divisors, vary any fourth center/boundary/dead-stretch/F1/
pole modulus, kill whole TD6 or SP-2, prove a landing theorem, or resolve
JC2.
