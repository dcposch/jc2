# Preregistration: first graded transverse-cusp syzygy lift

Date: 2026-08-26 UTC

Consume the frozen V4 first-cusp transport only through its hash-pinned exact
source.  Retain `a=1`, `p=-3`, `c=2+h`, full Q and R, fixed
`k=nu=0,mu=2/3`, all eight exact charged rows, and the reviewed q2-corrected
multipliers.

Let

```text
W_h=sum_i F_i' E_i(h),
C_1=[(W_h-W')/h]_(h=0).
```

On the closed corner `alpha=15/2,beta=delta=5`, extract the complete worst
graded piece of `C_1`: every monomial with exactly one Q coefficient and one
R coefficient and no other factor.  V4 predicts eight such terms, whose
normalized difference from target before the h charge is `-15/2`.

From every row `E_i(0)`, extract the same complete Q-R graded component and
solve over Q

```text
sum_i g_i * QR(E_i(0)) = -QR(C_1)
```

by exact RREF with free columns set to zero.  Record all monomial equations,
rank, pivots, solution and literal residual.  If inconsistent, emit an exact
left-cokernel functional `y` with `y*A=0` and `y*target!=0`; do not call a
bare solver failure an obstruction.

If solvable, set

```text
F_i''=F_i'+h*g_i,  W_h'=sum_i F_i'' E_i(h).
```

Require `W_h'|h=0=W'`, exact cancellation of the entire h-linear Q-R piece,
and emit the complete corrected polynomial and affine weight records.  Then
compute the new exact uniform eta threshold on
`alpha=15/2,beta=5+u,delta=5+v`, distinguishing `eta=eta_0` strictness in
the open quadrant from a genuine equality tie.  Any remaining low layer is
the next syzygy-ladder input, not a surviving branch.

Run forward/reverse exact rational encodings on two registered AWS hosts
under explicit caps.  No local exact execution.  This is one filtered
homological-perturbation step only: no full h-adic lift, moving axis/load,
whole fan, D1, or JC2 claim.
