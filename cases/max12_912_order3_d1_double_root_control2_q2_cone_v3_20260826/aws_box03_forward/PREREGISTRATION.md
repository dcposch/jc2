# Preregistration: symbolic cone of the corrected full-q2 witness

Date: 2026-08-26 UTC

Hash-pin the V2 syzygy-lift compiler and reconstruct its exact full polynomial
`W'` without reading a printed CAS expression.  Require canonical SHA-256
`ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`
and exactly 37 terms.

For every monomial, emit the normalized affine difference from `la^20`:

```text
e_q2*delta + (e_q1+e_q0)*beta
  + (e_r2+e_r1+e_r0)*alpha + e_la - 20
  + e_tau*t + e_rho*h.
```

Here `wt(la)=L`, `t=T/L>0`, `h=H/L>0`, `alpha=wt(r_i)/L`,
`beta=wt(q1)=wt(q0) over L`, and `delta=wt(q2)/L`.  Group all distinct
forms, but retain every coefficient and monomial so vanishing support cannot
be silently discarded.

At `alpha=15/2`, substitute `beta=5+u`, `delta=5+v`.  Require exact rational
verification that every non-target, non-`la^20*tau` difference is

```text
c + q*u + d*v,
```

with `c,q,d >= 0`, and that either `c>0` or `q+d>0`.  This proves unique
least term `la^20` for `u>0,v>0`; `la^20*tau` is higher because `t>0`.
Separately enumerate exactly the terms tying on beta=5/delta>5,
delta=5/beta>5, and their corner beta=delta=5.  Do not infer any equality
face saturation from this witness-only calculation.

Run forward and reverse exact traversals on distinct registered AWS hosts;
require identical canonical records and boundary sets.  The charged
control-2 interpretation says a later q2 activation has `delta>beta`, so the
open quadrant theorem would cover every such activation when `5<beta<6`.
This semantic mapping must remain a separately charged premise.

No moving axis/cusp or load, next support, equality-face, whole fan, D1, or
JC2 claim is licensed.
