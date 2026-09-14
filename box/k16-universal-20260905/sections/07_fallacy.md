## 7. FALLACY-v2 check

- **Prime label/derivative.** `P', L', W'` are x-derivatives (charged §7.1); `theta = x d/dx` is declared; `L̃, l̃_2`
  are labels (the second branch), not derivatives; Astra's `H` of (RC1) is `Hdiff`, distinct from the slice
  determinant `H`.
- **Variable/ring map.** Every Singular ring is declared with generator order, weights and coefficient field
  (`(0,d)` with `minpoly 3d²−N`, or `GF(p)` at a declared root); the ray specialisation is `l_j ↦ c_{N−j}/y`,
  `l_N ↦ 1/y`; frozen rows are compared by `imap` under the identity map on `(c_i, b)`, never by name.
- **Floor/attainment.** `deg P = 2N` is charged (exact); `deg D = 3N` is exact by its leading coefficient; the
  minimal b-powers of §5 are minima found by search, reported as such.
- **Raw remainder / `sat()`.** No `sat`; memberships are `reduce` against a reduced `std`, with the multiplier
  power reported; radicals via `primdec.lib` only at t = 2 (dimension ≤ 1).
- **Modular → char 0.** The t = 5 membership and the dual-chart units are modular controls, labelled so; the t = 3
  and t = 4 memberships are exact over `Q(d)`; no modular statement is promoted.
- **Number vs degree; generic-coefficient theorems.** No counting theorem is applied. Briot–Bouquet is applied to
  ONE equation at a time with its exponent computed (`3` at 0, `4N + 6d` at ∞) and its case named; nothing is
  inferred across t from it.
- **Flag/place/series, exit sets, pole identities, 8.5, arrival index:** not touched. No exit-price assertion is
  made; the `charge_basis` line is inapplicable.
