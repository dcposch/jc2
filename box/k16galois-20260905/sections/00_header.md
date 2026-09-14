# K16 Γ-Galois lane: the Eagon–Northcott curve Γ_t is one Galois orbit over A_t at t = 3, 4, 5 (proved),
# the all-or-nothing lemma with its étale lift, the one-evaluation instrument through t = 8, and the
# exact residual of (V0) on the K = 16 ray

Lane `k16-gamma-galois-fable5-20260905`, basis `9aede103`, 2026-09-05.  Drivers and every transcript in
`box/k16galois-20260905/` (worker outputs mirrored under `w7/`, `w18/`, `w166/`, `w254/`, `w28/`).
Engines: Singular 4.3.3 (`std`, `finduni`, `factorize`, `quotient`; exact over `A_t = Q(yy)/(H_t)` with
`minpoly`, or `GF(p)` at a declared root of `H_t`), msolve 0.x on one worker (F4 + rational parametrization
mod p, t = 6 calibration and t = 8), python3/sympy/numpy (bookkeeping, root scan).  Foreground CAS under
`timeout` + `stdbuf -oL`; ≤ 5 desk cores; ≤ 4 processes per fleet worker (the fleet was shared with another
lane's jobs throughout).  No ledger, `jc2-lean`, `ideation-*` or in-progress lane report was read or written.
`FALLACY-v2` applies; no exit-price assertion is made, so no `charge_basis` line is due.
