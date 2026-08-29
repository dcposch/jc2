# K00 valuation-at-least-seven exclusion through Lambda^19 — coordinator provisional

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PROVISIONAL_EXACT_DESK_THEOREM / HOSTILE_REVIEW_REQUIRED`

## 0. Result

In the exact V20R2 normalized K00 source, there is no compatible
`Lambda<=19` jet on

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0] != 0,
d_i in Lambda^7 Q[[Lambda]]  for i=0,...,5.
```

Equivalently, every compatible nonconstant K00 jet in this source would
have transverse valuation at most six. Combined with the separately
reviewed grade-five theorem, valuation one is already empty on the frozen
client open `D(k10[0]) intersect (D(s) union D(t))`; the only remaining
positive transverse valuations in this source are therefore `2,...,6`.

The proof is a one-row contracted coefficient argument, not a Groebner-basis
calculation. It uses only the exact affine load decomposition, contracted
syzygy, and boundary orders already reconstructed and mutation-tested by
V20R2. It does not exclude valuations `2,...,6`, change the closed
valuation-one theorem, or
imply absence of a formal arc, algebraic arc, polynomial map, order-two
configuration, maximum-twelve configuration, counterexample, or JC2.

## 1. Exact contracted source and order ledger

Write the seven V20R2 equations as

```text
Phi_i = R_i(d)
      + p10 A10_i(d) + p6 A6_i(d) + p2 A2_i(d)
      - Lambda^(12+i) delta_i,
```

where

```text
p10=Lambda^2 k10,
p6 =Lambda^6 k6,
p2 =Lambda^10 k2,
delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

The frozen tails are affine-linear in the three loads. They also satisfy the
exact K00 relation

```text
h R_7 = sum_(i=1)^6 u_i R_i,       h(0)=20.
```

Consequently the scalar contraction

```text
Rmix = h Phi_7 - sum_(i=1)^6 u_i Phi_i
```

is exactly

```text
Rmix = p10 D10 + p6 D6 + p2 D2
     + Lambda^14 mu2 u2 + Lambda^16 mu4 u4
     + Lambda^18 mu6 u6 - Lambda^19 Jdet h/4.
```

This is the V20R2 `D_p` identity, not a quotient or leading-form
approximation. The exact serialized `K_VECTOR` has minimum transverse
`d`-degrees

```text
(D10,D6,D2,u2,u4,u6,h) = (3,2,2,1,1,1,0),
```

and the degree-zero part of `h` is `20`. Exact expansion of the uncontracted
source additionally gives:

- every `R_i` has transverse `d`-degree at least two;
- every `A10_i` has `d`-degree at least two;
- every `A6_i` has `d`-degree at least one;
- every `A2_i` has `d`-degree at least one;
- all load-sector constant terms vanish.

The boundary conditions give

```text
ord_Lambda(p10)=2,     because k10[0] is a unit in the frozen client;
ord_Lambda(p6)>=7,     because k6[0]=0;
ord_Lambda(p2)>=11,    because k2[0]=0.
```

Suppose all six `d_i` are divisible by `Lambda^r`, with `r>=7`. The seven
positive-order terms in the contracted identity start no earlier than

```text
p10 D10:                 2+3r,
p6 D6:                   7+2r,
p2 D2:                  11+2r,
Lambda^14 mu2 u2:       15+r,
Lambda^16 mu4 u4:       17+r,
Lambda^18 mu6 u6:       19+r,
Lambda^19 Jdet(h-20):   19+r.
```

Every displayed order is strictly greater than 19 when `r>=7`. The only
grade-19 term in `Rmix` is therefore

```text
-Lambda^19 Jdet[0] h(0)/4 = -5 Jdet[0] Lambda^19.
```

The grade-19 contracted equation forces `Jdet[0]=0`, contradicting the
frozen unit open. This proves the result.

## 2. Independent raw-row check at valuation at least ten

Let

```text
L(d)=d1-d3/4+d5/16.
```

Direct exact extraction from the frozen K6 load sector gives its linear
parts on rows `1,3,5,7`:

```text
A6_1^[1] =  (3/4)    L(d),
A6_3^[1] = -(3/32)   L(d),
A6_5^[1] = -(3/512)  L(d),
A6_7^[1] = -(3/4096) L(d).
```

The remaining linear K6 coordinate lies in row 2; rows 4 and 6 have no
linear K6 term. Only the displayed odd-row identity is needed.

Define

```text
theta = [Lambda^19] (p6 L(d)).
```

If all `d_i` are divisible by `Lambda^10`, then through grade 19 the only
nontarget term in the seven raw equations is `p6 A6^[1](d)`. At grade 19,
row 1 has no target and no other surviving source term, so

```text
(3/4) theta = 0,
```

hence `theta=0` in characteristic zero. Row 7 at the same grade is

```text
-(3/4096) theta - Jdet[0]/4 = 0.
```

It again follows that `Jdet[0]=0`, contradicting the frozen unit open. This
is a weaker but independent raw-row verification of the contracted proof's
high end. Notice that the free `mu`
coefficients occur only in rows 2, 4, and 6 and therefore cannot alter the
two-row argument.

## 3. Scope and next exact split

This result is specific to the normalized K00/V20R2 source and its
`Lambda^19` target. It is stronger than a leading-vector assertion: it
also covers the zero transverse series, because the hypothesis is simply
`Lambda^7 | d_i` for every `i`.

The remaining valuation problem is finite:

```text
r=2,3,4,5,6.
```

Those values are not equivalent. Their first possible collisions are
controlled by

```text
contracted K10:       2+3r,
contracted K6:        7+2r,
contracted K2:       11+2r,
contracted mu2:      15+r,
contracted mu4:      17+r,
contracted mu6:      19+r,
Jacobian target:        19.
```

This table is only a preflight. On leading loci, earlier equations can
raise the effective order, as occurred in the valuation-one analysis.
The next producer should therefore compile the exact associated-graded
coefficient systems separately for `r=2,...,6`, with valuation exactness
encoded by a projective leading-vector cover and with all five boundary
zeros substituted before solve or saturation. It should run on AWS if it
uses CAS. No broad common-source elimination is licensed by this note.

## 4. Custody

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
9e304f58310fda008a3930b21bf0f49bc198322ee5dd98d805af04068ed5b3c8
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/RESULT_V20R2.md
6c4ebd6d61189e0f80fd9021edd509cbb323826774644d92828a0badd0943a29
  xmodel/max12-812-order2-k00-v8-v9-hostile-review-grok-20260827.md
```

No AWS resource, heavy CAS, canonical campaign file, external source, or
`jc2-lean` object was touched in deriving this provisional theorem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6464`.
- Body SHA-256: `3c3a3f98bc86939b293e6f03dfe9f2cff406fdbb97eab511b294e7314f04bf03`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
