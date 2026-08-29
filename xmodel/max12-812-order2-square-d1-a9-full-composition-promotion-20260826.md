# Promotion: complete D1 `a=9` fixed-contact exclusion

Date: 2026-08-26

Status: **PROMOTED AFTER DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen custody

```text
3679d0dbd883c74a4d1d7d1175daf9461c123dd83272bdf2e713ebd7c3412a88
  cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_v2_target_precedence_20260826/RESULT.md
f878c18a4163e1b94bb150e3a84e626ff3eb9d13382da8d03694b200101c2a0d
  cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_v2_target_precedence_20260826/EVIDENCE.sha256
be2a611f119900400b7bb5a8c0fc7e9cb66815c8b3c23a70feb565b209092c48
  cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_v2_target_precedence_20260826/FREEZE.sha256
eb1b77e1731e438e732ac5f704a99d63f95f10a172855d0e5c2ca67eb39e9f47
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade28_29_collision_v2_syntax_20260826/RESULT.md
e4625f8e09e1ffa09cc3267798e19b8333d9c16d7b1b9530f141b094540f64ca
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade28_29_collision_v2_syntax_20260826/FREEZE.sha256
bbb1d718a08247d7ff344033e51c988ee52f7ae88a19e98cb059b0ebd8d7cf1c
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/RESULT.md
dc223883009026a2e242735563170a51f081b0c049a966751521e4fff8396f52
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/EVIDENCE.sha256
6881229bb9d8f89fe1be3314a7e7a8b654cf2e8f7f101a9b6a5936add1ba3570
  cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/FREEZE.sha256
8524bd1e20ecfc3931df5c9df9e88f6673de5a7f348b015954884acdddd558eb
  xmodel/max12-812-order2-square-d1-a9-full-composition-hostile-review-grok-v3-20260826.md
```

Exact Q is the theorem endpoint. The separately compiled `F_65521` lanes
are software controls. The final hostile review rehashed the full grade-30
freeze/evidence trees and independently rederived grades 27--30 from the
frozen literal Faber tails.

The grade-27 review digest printed in the final review prompt was mistyped.
The unique on-disk review has SHA-256

```text
95e9990b2acbaaf0cb80afd5722d202f6874dbe10918002c5bdb6353bbb0b9fd
```

and is exactly the file pinned by the earlier grade-27 promotion. The final
review rederived those identities from the tails, so this is a custody
transcription correction, not a mathematical defect or a second review.

## Promoted theorem

In characteristic zero, after the registered upstream square/D1 gates, the
fixed-contact cell

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9
```

is empty on `D(p*k0)` for the complete seven literal-Faber source equations.

The proof is the exhaustive scheme-theoretic split

```text
D(k60)  union  V(k60) intersect D(k60_1)
          union V(k60,k60_1).
```

- On `D(k60)`, the first grade-27 rows are `(3/4)c1*k60` and
  `(3/4)c0*k60`; exact contact of `C` makes this impossible.
- On `V(k60) intersect D(k60_1)`, the grade-28 leader forces `c1=0`
  and the unrestricted grade-30 row forces `c0^2=0`; the exact-order-ten
  Bezout equation gives the unit ideal.
- On `V(k60,k60_1)`, the full grade-27--30 ideal equals, before radicals,
  the compact ideal containing

  ```text
  c1*c0,  2*c0^2-p*c1^2.
  ```

  On `D(p)`, it contains `c0^3,c1^3`; cubing the exact-contact Bezout
  equation yields the unit ideal.

No intermediate valuative cell is omitted: if `k60` or `k60_1` has positive
finite valuation, the generic point of the corresponding DVR lies in the
already empty open branch. All higher normal corrections, the moving
connection, delayed `k20/k0_1/k60_4`, and the terminal `mu4,mu6,J` targets
remain in the complete source at their licensed grades.

## Firewall

This promotion removes only the named fixed `a=9` cell on `D(p*k0)`. It
does not cover `a>=10`, `p=0`, `k0=0`, other D1 cells, the whole square
component, order two, `(8,12)`, maximum twelve, or JC2.
