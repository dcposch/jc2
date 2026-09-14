
## 11. OPENs

OPENS RAISED

- `OPEN[K16-GAMMA-IRREDUCIBLE]` (re-scoped) — for t ≥ 7, is `Γ_t ∩ {b4 ≠ 0}` one Galois orbit over `A_t`?
  QUANTITY: `k_t = 1` is PROVED for t = 3, 4, 5, 6 (this lane; `Gal = S_{n_t}` for t ≤ 6); the first undecided
  index is t = 7 (`n_7 = 35805/4 − boundary`), decidable by the subset-sum criterion 3.6 from ≤ 20 modular `finduni` jobs of the t = 7 chart
  (`finduni` is cubic in the point count: 150 s at n = 1548 extrapolates to ≈ 8 h per prime at n ≈ 8950, a
  fleet-day, not a desk job); a uniform proof needs a t-indexed prime with an
  irreducible reduction and none is in sight (§7).
- `OPEN[K16-ONE-POINT-T8]` — clause (ii)_8 by the instrument.  QUANTITY: the number of verified simple
  `F_p`-points of `Γ_8 ∩ {b4 ≠ 0}` with `W ≠ 0` is `= 0` today and `≥ 1` closes the affine part (52140 points;
  the msolve F4 run at 4 threads on a shared worker was at degree 14 of the CI system, 45739 × 81237, at seal);
  with the point the check is a 1 s `verifypoint` job; the flat-model hypothesis at t = 8 (`CONE dim = 1`,
  i.e. chart dim 0 + slice dim 1) is the other printed item still owed.
- `OPEN[K16-UNIFORM-POINT]` (= problem (II), unchanged) — a t-indexed point `P_t ∈ Γ_t` with a closed-form
  `T_{t,2t−1}(P_t, β_t)`; QUANTITY: `#{t : a formal/closed-form point of Γ_t is known} = 0`.  This is the binding
  uniform gap; Proposition 7.1 shows problem (I) is not logically necessary for it.

OPENS ANSWERED HERE

- `OPEN[K16-GAMMA-IRREDUCIBLE]` for t = 4, 5, 6: YES (§4); `OPEN[K16-ONE-POINT-CERTIFICATE]` for t = 3..6: the
  instrument runs and certifies clause (ii) at each (§5); `OPEN[K16-GAMMA-REDUCED-T6]`: YES, `Y_6` is reduced with
  1548 simple points (`deg m̄ = vdim = 1548`, squarefree, at 8 primes).
