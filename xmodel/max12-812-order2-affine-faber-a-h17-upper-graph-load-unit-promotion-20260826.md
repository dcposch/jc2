# Promotion: affine-Faber `A`, H17 upper graph-load unit

Date: 2026-08-26

Status: **HOSTILE-REVIEW CONFIRMED; PROMOTED AT THE EXACT INTERNAL SCOPE
BELOW.**

## Promoted statement

In characteristic zero, in the internal normalized H17 moving-
discriminant graph coordinates, impose

```text
v(lambda)=17,
v(X)=v(Y)=q,
v(Ri)=v(Si)=2q,
v(a)=17-2q,
v(K10)=v(K6)=v(K2)=42,
v(J)=57,
v(E)=v(M)=0,
```

and the positive-contact load congruences

```text
K10=t^42*kappa,
K6=t^42*((15/32)*kappa*E^2+d6),
K2=t^42*((15/256)*kappa*E^4+d2),
v(d6)>0, v(d2)>0.
```

On `D(kappa*a*E)`, for every rational `7<q<17/2` after a common
ramification, the exact functional

```text
Hseries=2*E^2*P3+16*E*P5+64*P7-(E^3/2)*P1
```

has unique least term `(5/4)*kappa*a^3*E^7`, of weight `93-6q`.
Consequently the seven raw ordinary-Faber rows cannot vanish
simultaneously.

The review independently reconstructed the 630-term parent support and
the 468-term graph specialization, checked every cancelled cluster and
moving-jet/load term, and confirmed that `q=7` is exactly the two-term tie
with `-2*lambda^3*M^3*E^2`.

## Custody

```text
773b4d773cee9cc967645b6c67417d7d60c3058d2e5ae898f06d12b4863800fc
  xmodel/max12-812-order2-affine-faber-a-h17-upper-graph-load-unit-theorem-20260826.md
2aef1cd7aa844efec10a12068620a30c7aaa200f3a6bca622fed1629b6923312
  xmodel/max12-812-order2-affine-faber-a-h17-upper-graph-load-unit-hostile-review-grok-20260826.md
37d43ffdf7098028e02a79509461b6e06777e203ab04b57ee1d0c5f3801d5f57
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/RESULT.md
b9c11be5a6821d31826a947f8c73562c1f6447423894d2718ff7020fb178e909
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/EVIDENCE.sha256
7b2534e945398a31e8ce5111786e0bad45fc0ca125354178242189de4227891c
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/FREEZE.sha256
34d701dc7b33125774a89a11e47bd1284c21f8650cffaaf085c14e589f189553
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/RESULTS.sha256
ae18b65c01e0b7381c6944754a1bb9690ed006255a922399716ef2cc99bc550e
  cases/max12_812_order2_affine_faber_a_h17_upper_graph_load_unit_v10_20260826/evidence/Box02/aws_qgraph/output/hseries_affine_graph_support.json
```

## Exact firewall

This promotion is internal to the positive-contact normalized graph.  It
does not include `q=7`, `q>=17/2`, `kappa*a*E=0`, other graph or load
receivers, literal-source or total-Rees accessibility, terminal/Taylor
strata, order two, `(8,12)`, maximum twelve, or JC2.
