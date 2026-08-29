# Promotion: affine-Faber `A`, fixed H16/q6/a4 grade-48 direct unit

Date: 2026-08-26

Status: **PROMOTED AFTER DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen custody

```text
4748f3f1666ec0753035c4a79f5aa59376647283223ec9c432e8d7b2b4b31b10
  xmodel/max12-812-order2-affine-faber-a-h16-q6-a4-grade48-direct-unit-theorem-20260826.md
f0e231cbbb82e24245de199ca13d4881cbbd50ffbc89c9c68dc23ea017c73fd0
  xmodel/max12-812-order2-affine-faber-a-h16-q6-a4-grade48-direct-unit-hostile-review-grok-20260826.md

3b99f6f198b8e149fbebac443ce4c59faed4fd2289275c6b4680cc673ed790bb
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/RESULT.md
922e10cab6f8b4b9ad9db45898721c68e4f6829b6e1e69ee2a51918cc4d89667
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/EVIDENCE.sha256
1a9411e67f2ef2efed48efffaf2afb066f2a5e8ab97d3ca5fe458693cbefaef6
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/FREEZE.sha256
4c9a9bebac582749688909c0048b960d2212e9563490b16f06278cbe135680ff
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/RESULTS.sha256

02a005dd4bac2db1ef891a55d4377148ce4a485ea0d61d9dd4bc73da541863af
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/RESULT.md
7524ed35265f551ea03034b16279bd219d243f3225e3764748166208e758c5c8
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/EVIDENCE.sha256
3b8c42ba206668298c65e725bc640461665c2aeacdf19128dc8499939f69ef94
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/FREEZE.sha256
32ffca9f138e9e8a9fe8178a923265c3238cb3f49ff04e92cb0f216657a8bcea
  cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_secondary_odd_dag_v6_20260826/RESULTS.sha256
```

The exact characteristic-zero proof uses the custom sparse polynomial/series
engine in V4 and V6.  It does not use Singular quotient-ring comparison.
The V5 ordinary-ring point controls corroborate the same identity but are not
the unspecialized proof.

## Promoted theorem

Let `R` be a complete DVR of residue characteristic zero.  In the registered
internal moving-discriminant affine-Faber graph family with fixed integral
weights

```text
(H,q,ord_s(a)) = (16,6,4)
```

and on `D(p*m)`, simultaneous vanishing of all seven raw ordinary-Faber row
coefficients through absolute grade 48 is impossible.

Indeed, with

```text
F = P7 - E^2 P3/32 + E^3 P1/64,
G = E^2 P3 + 16 E P5 + 96 P7,
```

complete exact sparse extraction gives

```text
G48 - 32 F48 = -2 p^2 m^3.
```

The right side is a unit on `D(p*m)`.  Because `F` and `G` are series-linear
combinations of raw rows with nonnegative-valuation coefficients, vanishing
of the raw rows through grade 48 forces `F48=G48=0`, a contradiction.  The
moving-`E` feed from grade-46 load terms cancels in the displayed identity;
the registered targets and `J=s^57` do not enter grade 48.  No predecessor
standard basis and no `D(x)/D(y)` split are required.

## Firewall

This promotion is only the fixed integral H16/q6/a4 internal graph family on
`D(p*m)`.  It does not provide rational regrading, neighboring equality-wall
coverage, a literal source/Cech/total-Rees atlas, factor-degenerate opens
`p=0` or `m=0`, arbitrary load slopes, terminal/Taylor closure, order two,
`(8,12)`, maximum twelve, or JC2.
