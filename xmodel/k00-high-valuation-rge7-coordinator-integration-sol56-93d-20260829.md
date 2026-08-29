# K00 valuation-at-least-seven exclusion through Lambda^19 — binding integration

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PROMOTED_EXACT_SOURCE_THEOREM / SCOPE_REPAIRED`

## 0. Binding disposition

Grok 4.6 independently reconstructed the frozen K00/V20R2 contraction,
minimum-degree census, boundary orders, and terminal coefficient, and returned
`CONFIRMED`.  The promoted result is:

> Over `Q`, in the exact normalized K00/V20R2 mixed source truncated modulo
> `Lambda^20`, no solution of all seven rows on `D(Jdet[0])` has
> `d_i in Lambda^7 Q[[Lambda]]/(Lambda^20)` for every `i=0,...,5`.

On the full V20R2 source open

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0] != 0,
k10[0] != 0,
```

composition with the separately reviewed valuation-one theorem leaves only
the possible positive transverse valuations

```text
2, 3, 4, 5, 6.
```

This is an exclusion list, not an occurrence or attainment assertion.

The producer's separate valuation-two, zero-odd-correction calculation is not
promoted by this integration; its different-model review is a distinct gate.

## 1. Exact proof core

The frozen seven rows have affine load decomposition

```text
Phi_i = R_i(d) + p10 A10_i(d) + p6 A6_i(d) + p2 A2_i(d)
        - Lambda^(12+i) delta_i,
p10=Lambda^2 k10,  p6=Lambda^6 k6,  p2=Lambda^10 k2,
delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

With the exact V14 multiplier `h=20+63 d4` and the six frozen `u_i`,

```text
h R_7 = sum_(i=1)^6 u_i R_i
```

holds as a polynomial identity.  Hence

```text
Rmix = h Phi_7 - sum_(i=1)^6 u_i Phi_i
     = p10 D10 + p6 D6 + p2 D2
       + Lambda^14 mu2 u2 + Lambda^16 mu4 u4
       + Lambda^18 mu6 u6 - Lambda^19 Jdet h/4.
```

Independent reconstruction gives minimum total `d`-degrees

```text
(D10,D6,D2,u2,u4,u6,-h/4) = (3,2,2,1,1,1,0),
(-h/4)(0) = -5.
```

The seventh serialized `K_VECTOR` component is `-h/4`, not `h`; this
notation repair does not change the contraction.

If every `d_i` is divisible by `Lambda^r`, `r>=7`, the nonconstant terms
begin no earlier than

```text
p10 D10:               2+3r,
p6 D6:                 7+2r,
p2 D2:                11+2r,
Lambda^14 mu2 u2:     15+r,
Lambda^16 mu4 u4:     17+r,
Lambda^18 mu6 u6:     19+r,
Lambda^19 Jdet(h-20): 19+r.
```

All are strictly above grade 19.  Thus

```text
[Lambda^19] Rmix = -5 Jdet[0],
```

contradicting `Jdet[0] != 0` over `Q`.  The hypothesis is divisibility,
so it also covers the zero transverse 19-jet.

The reviewer independently recovered the odd-row K6 identity

```text
A6_(1,3,5,7)^[1]
  = (3/4,-3/32,-3/512,-3/4096)
    (d1-d3/4+d5/16),
```

which yields the same contradiction for the weaker range `r>=10` without
using the contracted degree census.

## 2. Composition with valuation one

The high-valuation theorem itself needs `D(Jdet[0])`; it does not need
`D(k10[0])` or the five V20R2 boundary zeros.  Those conditions are retained
in the full source client.  The already reviewed valuation-one chain adds:

1. complete grade-three incidence on
   `ell(s,t)=(2s,t/8,s,t,s,2t)`;
2. grade-five projection to `s=t=0` on `D(k10[0])`; and
3. source typing that `s=t=0` is the higher-valuation leak, not a
   valuation-one point.

Therefore valuation one and every valuation at least seven are empty on the
displayed full source open.  No existence at valuations `2,...,6` follows.

## 3. Arc-scope repair

Two inherited phrasings are superseded.

- The provisional note said that the theorem did not imply absence of a
  formal arc.  The review repeated that sentence while correctly confirming
  the finite-jet theorem.  Literally, any formal solution of this same exact
  source type and with `Lambda^7 | d_i` would truncate to the forbidden
  19-jet.  Such same-source formal arcs are therefore excluded.
- This does **not** exclude a formal or algebraic arc outside the normalized
  V20R2 source, a different support, a convergent germ, a polynomial Keller
  map, an order-two or maximum-twelve configuration, K00 as a whole, a
  counterexample, or JC2.  Conversely, a surviving finite jet at valuation
  `2,...,6` would not by itself produce any kind of arc or map.

This scope repair is a direct truncation corollary and changes none of the
reviewed coefficient algebra.

## 4. Next exact gate

At valuation six the first contracted collision is

```text
p6 D6: 7+2*6=19,
```

while `p10 D10` starts at grade 20 and the remaining contracted slots start
later.  The cheapest next producer is therefore the exact associated-graded
seven-row system at valuation six, with a projective leading-vector cover,
the source boundary zeros substituted before solving, and

```text
k6[1] D6^[2](x) = 5 Jdet[0]
```

retained.  Any heavy CAS realization belongs on AWS.  Valuations
`2,3,4,5` remain separate source covers.

## 5. Custody

```text
e4ec4431d679f44b27d35cbdc3c195c2383f21a57adc63e879be632c13af8a31
  xmodel/k00-higher-valuation-contraction-and-r2-preflight-sol56-93d-20260829.md
efec8e4e94315afee74dc47f2658fccd9be1d99c078dadbc61f3f88b25235cf3
  producer body through BODY-END
8d3ec8fd4cca2432d5c2adcd3e79bfe75db3b00caaae37c4cf82302c29f666df
  xmodel/k00-high-valuation-rge7-coordinator-provisional-sol56-93d-20260829.md
338da9e8d5b6b4476321efc27c2c14c66abc04c3fa18fbf3fb7c4bb98cd241d6
  xmodel/k00-high-valuation-rge7-hostile-review-grok46-93d-20260829.md
f552ba471021bfe007070640d62362d6683ebfade6fa95c0371f80c9106fa519
  hostile-review body through BODY-END
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a
  K_VECTOR.txt
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c
  CONTRACTED_TARGET.txt
```

No exit price, occurrence, attainment, or map is asserted.  No
`charge_basis` declaration is present because no exit-price claim is made.
No canonical file, case source, AWS resource, or `jc2-lean` object was touched
while producing this integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5936`.
- Body SHA-256: `60afca1325b9885f999bbcc9bd94cd737428c93c1f2419fa4b832f4a2ac41243`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
