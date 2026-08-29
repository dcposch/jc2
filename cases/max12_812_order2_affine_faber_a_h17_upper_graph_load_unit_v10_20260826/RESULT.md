# Result: H17 upper affine-graph load unit V10

Date: 2026-08-26

Status: **PASS/PASS producer evidence; graph-special-fibre scope.**

After the exact substitutions

```text
K6=(15/32)K10 E^2,
K2=(15/256)K10 E^4,
```

the complete 630-term exact support of `Hseries=G-32F` combines to 468
nonzero monomials.  Exact Q and the independent `F65521` reduction agree in
support and coefficient reduction.  The graph-reduced support SHA-256 is
`ae18b65c01e0b7381c6944754a1bb9690ed006255a922399716ef2cc99bc550e`.

On the H17 equality wall, the unique least term for the whole strict upper
domain

```text
7<q<17/2
```

is

```text
(5/4) K10 a^3 E^7,
```

of affine weight `93-6q`.  Hence it is a unit on the internal graph open
`D(K10*a*E)`.  At `q=7` there are exactly two ties:

```text
-2 lambda^3 M^3 E^2 + (5/4) K10 a^3 E^7.
```

No third support monomial ties.  The boundary equation is not resolved by
this run.

Positive-order load-graph deviations are not included in the special-fibre
support.  They cannot cancel the strict leading unit if their order is
indeed positive, but that valuative graph-composition statement remains a
separate gate.  There is no literal source, total-Rees, factor-degenerate,
order-two, max12, or JC2 conclusion.

Exact-Q Box02 and `F65521` r6d both passed in 0.06 seconds with at most 20 MiB
and zero swap under tags
`max12_812_order2_affine_faber_a_h17_upper_graph_v10_20260826T200518Z_qgraph`
and
`max12_812_order2_affine_faber_a_h17_upper_graph_v10_20260826T200518Z_pgraph`.
