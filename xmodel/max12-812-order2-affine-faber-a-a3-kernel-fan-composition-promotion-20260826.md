# Promotion: delayed affine-Faber `A`, `H=15,a=3` internal kernel fan

Date: 2026-08-26

Status: **PROMOTED AT THE REVIEWED INTERNAL DELAYED-CHART SCOPE ONLY.**

## Promoted statement

In characteristic zero, work in the normalized repeated-`A` coefficient
chart on `D(E*M)` with

```text
normal order H=15,
center order v(a)=3,
k10=sigma^42*K10
```

and with the leading loads on the corrected affine-Faber graph.  Let
`q=min(v(U),v(V))>0`, rational after finite ramification.  The complete
internal kernel fan is the disjoint partition

```text
(0,6):    the center-independent quadratic two-chart block occurs before
          the loads and is empty on D(E*M);

{6}:      the complete seven-row grade-42 graph/predecessor block is empty
          on both projective charts D(E*M*x) and D(E*M*y);

(6,∞]:   the graph-relative functional has the unique least term
          -E*lambda^3*M^3/16 once d6,d2,dm have strictly positive excess
          above the grade-42 graph.
```

For `q<6`, unequal kernel orders land on one of the same two projective
axes, and common ramification preserves `30+2q<42`.  At `q=6`, the full
grade-42 predecessor is imposed before inspecting the raw grade-45
support; hence the raw three-term grade-45 equality is unreachable, not a
direct-unit proof.  For `q>6`, uniqueness is certified from the complete
365-term support rather than a sampled cone.  The endpoint `q=∞` is the
kernel-zero slice of that same support.

The grade-42 identities and the intrinsic cubic do not algebraically
divide by `K10`.  Nevertheless `K10=0` is not promoted: `K10` is the
nonzero leading coefficient used to select the delayed affine-graph
neighbourhood and write its load ratios.  Its zero fibre is a different
support component and remains separately routed.

## Custody

```text
264033da9f60f7954a17d32f468e563838da310b7628ef21d06c1a0c6775c560
  xmodel/max12-812-order2-affine-faber-a-a3-q6-graph-predecessor-composition-20260826.md

5e8e82b3a29f2bdbb1d0c90130bbc7496808582ac0bc7148924b23df1a59bf25
  xmodel/max12-812-order2-affine-faber-a-low-kernel-center-independence-lemma-20260826.md

a5a876aee85a2249a9932bcab76875d94e7f450ea3ecaf32b68d98b8e29493c1
  cases/max12_812_order2_affine_faber_a_a3_q6_graph_predecessor_20260826/RESULT.md
16f2e56d6cac53cc20ca660a0c928f3d24e4cc1181fe6f40967909646a2a2bb9
  cases/max12_812_order2_affine_faber_a_a3_q6_graph_predecessor_20260826/EVIDENCE.sha256
0ca8d71a58caddcd48f3c72824049a600abd473cf8f016d02e71046d6c39b1e3
  cases/max12_812_order2_affine_faber_a_a3_q6_graph_predecessor_20260826/FREEZE.sha256

b0b25cf2134afc6e695b4a8a4b98ae49b6f0fd35b2bd57a760c049eb0a4e0bbc
  cases/max12_812_order2_affine_faber_a_graph_relative_cone_a3_v2_q6_face_20260826/RESULT.md
cb01e3c30042561558658557398d8390f895f4f15bc8e48c322d4e991c9d4581
  cases/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826/RESULT.md

da35a8c2b0876dcf54ded70a3b1a1e5c4af1e2626353481d2ceed5b4636d774f
  xmodel/max12-812-order2-affine-faber-a-a3-kernel-fan-composition-hostile-review-grok-v3-20260826.md
```

The different-model hostile review rehashed every charged pin and all 77
freeze/evidence paths, independently reconstructed the first polar block
and all seven grade-42 rows, parsed the full 365-term support, checked both
projective charts and rational ramification, and returned `CONFIRMED`.

## Scope firewall

This is an internal normalized/coefficient-chart theorem for the fixed
delayed load slope and graph neighbourhood.  It does not prove that a
literal source arc enters the chart, a two-sided source/Rees overlap,
total-Rees or saturation/base-change coverage, `q=0`, `v(a)<3`, `K10=0`,
`E=0`, `M=0`, another normal/load slope, terminal/Taylor closure, order
two, maximum twelve, or JC2.
