# Affine-Faber `A`: H17 upper graph-load unit

Date: 2026-08-26

Status: **PRODUCER THEOREM; HOSTILE REVIEW PENDING.**

## Statement

In characteristic zero, work in the internal normalized H17 affine-Faber
moving-discriminant graph coordinates.  After a common ramified base change,
assume

```text
v(lambda)=17,
v(X)=v(Y)=q,
v(Ri)=v(Si)=2q,
v(a)=17-2q,
v(K10)=v(K6)=v(K2)=42,
v(J)=57,
v(E)=v(M)=0,
```

and the positive-contact affine load graph

```text
K10=t^42*kappa,
K6=t^42*((15/32)*kappa*E^2+d6),
K2=t^42*((15/256)*kappa*E^4+d2),
v(d6)>0, v(d2)>0.                                (1.1)
```

On `D(kappa*a*E)`, simultaneous vanishing of the seven raw ordinary-Faber
rows is impossible whenever

```text
7<q<17/2.                                         (1.2)
```

## Proof

For

```text
Hseries=2 E^2 P3+16 E P5+64 P7-E^3 P1/2,
```

substitution of the special fibre `d6=d2=0` into the complete exact 630-term
support yields 468 nonzero monomials.  Exact comparison of all of them shows
that throughout (1.2) the unique least term is

```text
(5/4)*kappa*a^3*E^7,                              (2.1)
```

of relative affine weight `93-6q`.

Now expand every occurrence of `K6,K2` using (1.1).  Any term containing at
least one `d6` or `d2` has strictly positive excess over the corresponding
special-fibre term because the substitution is polynomial and both
deviations have positive valuation.  Such a term cannot cancel or precede
the unique initial monomial (2.1).  Its coefficient is a unit on the stated
open, contradicting raw-row vanishing.

At `q=7`, (2.1) ties exactly

```text
-2 lambda^3 M^3 E^2;
```

that boundary is deliberately excluded.

## Custody

```text
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

## Firewall

This is an internal positive-contact graph theorem.  It assumes the affine
load congruences (1.1); it does not prove access to them from a literal source
or total-Rees chart.  It excludes neither `q=7` nor `q>=17/2`, `kappa*a*E=0`,
another graph receiver/load schedule, terminal/Taylor strata, order two,
`(8,12)`, maximum twelve, or JC2.
