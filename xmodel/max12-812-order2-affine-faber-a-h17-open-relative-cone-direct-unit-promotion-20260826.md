# Promotion: affine-Faber `A`, H17 open relative-cone direct unit

Date: 2026-08-26

Status: **HOSTILE-REVIEW CONFIRMED; PROMOTED AT THE EXACT INTERNAL SCOPE
BELOW.**

## Promoted statement

In characteristic zero, in the internal normalized moving-discriminant
graph coordinates on `D(E*M)`, impose

```text
v(lambda)=17,
v(X)=v(Y)=q,
v(R0)=v(R1)=v(S0)=v(S1)=2q,
v(a)=17-2q,
v(K10)=v(K6)=v(K2)=42,
v(J)=57,
v(E)=v(M)=0.
```

After a common ramified base change, for every rational

```text
17/4 < q < 7,
```

the exact 630-term functional

```text
Hseries=2*E^2*P3+16*E*P5+64*P7-(E^3/2)*P1
```

has unique least term `-2*lambda^3*M^3*E^2` of valuation 51.  Hence the
seven raw ordinary-Faber rows cannot all vanish through valuation 51.

The review independently reconstructed the exact-Q support, recovered all
630 monomials, checked the coefficient `-2`, and rederived the strict
interval from all 629 competing inequalities.  It also recovered the five
lower-boundary terms of line `34+4q` and the three upper-boundary loaded
terms of line `93-6q`.

## Custody

```text
513d11901c09046abbeb41f9c5f2441e023b27925fde861d4c873306c9fa1f63
  xmodel/max12-812-order2-affine-faber-a-h17-open-relative-cone-direct-unit-theorem-20260826.md
6644a940c0fcbf2d00dce490757146d4c1cbf17c7172d413770b493fbbb56e27
  xmodel/max12-812-order2-affine-faber-a-h17-open-relative-cone-direct-unit-hostile-review-grok-20260826.md
1244a648d3bc761ae6fe9dbc1be72cad3e09b650d3d98109ebd2b4081ac1bb15
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/RESULT.md
3c8f207fc7522b58835758126a1a15841e76c92e3bc8beacebb6e22c55c81f06
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/EVIDENCE.sha256
8bf9aa5e7485555fbeb0a19c0b9ae2dc106715b6c13da850c4bfdfe22925e237
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/FREEZE.sha256
6aec97c6b03eaca66e6a3df9d80da41884ae5225836b96a5ab269962dcfe4365
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/RESULTS.sha256
60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/evidence/Box02/aws_qcone/output/hseries_exact_support.json
```

## Exact firewall

This promotion excludes both endpoints, `E*M=0`, a unit kernel coordinate,
another normal or load schedule, graph accessibility from the literal
source, and normalized-Rees or total-Rees coverage.  It does not close the
whole exceptional `A` fan, order two, `(8,12)`, maximum twelve, or JC2.
