# Preregistration: h-squared Q-R syzygy lift

Date: 2026-08-26 UTC

Reconstruct the exact V6 71-term witness from the frozen ordinary rows and
the scalar h correction
`(5/2,-25/18,0,1/4,-1/3,0,0,0)`.  Require its reviewed h=0 witness custody,
its V6 canonical hash, and exact vanishing of the h-linear Q-R and
R-square/Q-cubic pieces.

Extract the complete h-squared coefficient and then every monomial with one
Q and one R coefficient and no other factor.  These are the eight extremals
at eta infimum `15/4`.  Solve the complete exact system

```text
sum_i d_i * QR(E_i(0)) = -QR([h^2]W_V6)
```

by rational RREF, with free columns zero.  If inconsistent, emit and verify
a left-cokernel functional.  If solvable, set

```text
F_i^(7)=F_i^(6)+h^2*d_i
```

and require all lower h coefficients unchanged and the entire h-squared Q-R
piece zero.  Emit the full identity and recompute the exact eta threshold.

Run forward/reverse exact encodings on two registered AWS hosts under caps.
No local exact computation.  This is one filtered scalar correction only;
no general multiplier-support, h-adic, moving-source/load, fan, D1, or JC2
claim.
