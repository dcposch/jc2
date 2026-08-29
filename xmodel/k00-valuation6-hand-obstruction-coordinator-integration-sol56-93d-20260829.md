# K00 valuation-at-least-six hand obstruction — binding integration

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PROMOTED_EXACT_SOURCE_THEOREM / SUBSUMES_RGE7`

## 0. Binding theorem

Grok 4.6 independently reconstructed the frozen 569-tail source, V14
contraction, `K_VECTOR`, raw grade-12 quadrics, and every grade-19 order, and
returned `CONFIRMED` with mutation controls.

Over `Q`, in the exact normalized K00/V20R2 mixed source truncated modulo
`Lambda^20`, there is no solution of all seven rows with

```text
C6=1,
k6[0]=0,
Jdet[0] != 0,
d_i in Lambda^6 Q[[Lambda]]/(Lambda^20),  i=0,...,5.
```

This is the closed divisibility condition `Lambda^6 | d`, including the zero
transverse 19-jet.  The argument does not require `k10[0] != 0`, an
exact-valuation open, or the other four V20R2 boundary zeros, although all are
retained in the full source client.

Combined with the separately reviewed valuation-one theorem, every compatible
19-jet on

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0] != 0,
k10[0] != 0
```

has possible positive transverse valuation only in

```text
2, 3, 4, 5.
```

No one of those values is thereby attained.  This theorem mathematically
subsumes the separately reviewed `v_Lambda(d)>=7` exclusion while preserving
that earlier packet's provenance.

## 1. Exact three-row obstruction

After the K00 chart, write `Q1,Q3` for the quadratic parts of the unloaded raw
rows `R_1,R_3`.  Write `D_K6^[2]` for the quadratic part of the exact
contracted K6 component.  Independent coefficient extraction gives the
identity in `Q[d0,...,d5]`

```text
D_K6^[2] = -4 Q1 - 32 Q3.
```

If `Lambda^6 | d`, put `x=(d_0[6],...,d_5[6])`.  With `k6[0]=0`, the first
raw grade is 12, where rows 1 and 3 are literally

```text
Q1(x)=0,  Q3(x)=0.
```

This is before any quotient, localization, saturation, or projective leading
chart.  The exact scalar contraction is

```text
Rmix = Lambda^2 k10 D10 + Lambda^6 k6 D6 + Lambda^10 k2 D2
     + Lambda^14 mu2 u2 + Lambda^16 mu4 u4
     + Lambda^18 mu6 u6 - Lambda^19 Jdet h/4,
h=20+63 d4.
```

Its minimum transverse degrees are

```text
(D10,D6,D2,u2,u4,u6,-h/4)=(3,2,2,1,1,1,0),
(-h/4)(0)=-5.
```

At grade 19 the only live terms are therefore

```text
[Lambda^19] Rmix = k6[1] D_K6^[2](x) - 5 Jdet[0].
```

The two raw grade-12 equations make the first term zero, leaving
`-5 Jdet[0]=0`, contrary to the unit open.  Grades 13 through 18 need not be
solved.  No nonlinear CAS or AWS computation is warranted for this branch.

The boundary zero `k6[0]=0` is load-bearing: without it raw grade 12 and the
contracted grade-19 coefficient acquire additional K6 terms.  The other four
boundary zeros and `k10[0] != 0` are part of the full V20R2 source but are not
used by this three-row contradiction.

## 2. Scope

A formal solution of this same exact normalized source with
`Lambda^6 | d` would truncate to the forbidden 19-jet and is also excluded.
The converse and all broader readings fail: the theorem does not exclude a
different normalization or load support, an arc of another source type, a
convergent germ, a polynomial Keller map, K00 closure incidence, order two,
maximum twelve, a counterexample, or JC2.  A compatible finite jet at
valuation `2,3,4`, or `5` would not by itself be a formal arc or map.

## 3. Next source split

The remaining V20R2 valuation problem is finite but not homogeneous:

```text
v_Lambda(d)=2,3,4,5.
```

Each value needs its own source-faithful leading-vector cover and coefficient
window.  Do not infer existence from the list or normalize a leading
coordinate without a licensed action.  The separately reviewed status of the
old-plane valuation-two `d[3]=0` sublane is integrated only after its own
hostile review finishes.  Any heavy or uncertain solve remains AWS-only.

## 4. Custody

```text
c9563ced370809e0fe48843ac2ae768dc1decb880f8c8624804148236605ae6b
  xmodel/k00-valuation6-successor-design-sol56-93d-20260829.md
52ca8725c5ca7e8322a2ac8aaca81c69bce75a933ce0aa9151764638f8f23408
  producer body through BODY-END
a4795743902cadf823cec0c17c21af442f4511260da74ccf63364f60f832a346
  xmodel/k00-valuation6-hand-obstruction-hostile-review-grok46-93d-20260829.md
45a6b8d83df5fa99cc2762bef82fb1ed331bc7bca7aeac9ee59afcf38d63020a
  hostile-review body through BODY-END
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a
  K_VECTOR.txt
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c
  CONTRACTED_TARGET.txt
7e9e591672a9f1a6b1e8b5bc56053947fa3a665b8541d91e20d90894e465f546
  xmodel/k00-grade5-rank0-plane-coordinator-integration-sol56-20260829.md
11d0d69ddeff40ad7d26ee360fb7035b77c9909af06ad3507e5c3ba6c1510f6b
  valuation-one binding body through BODY-END
```

No exit price, occurrence, attainment, or map is asserted.  No canonical
file, case source, AWS resource, or `jc2-lean` object was touched while
preparing this integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4978`.
- Body SHA-256: `49f496bda741ca1032a6fa77c8a2ed8b6d3a8a63cc6bb8a4e2928800df85d931`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
