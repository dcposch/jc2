# (1) The KJ identity on Delta -- hand derivation, engine conventions

Engine (rekill_engine.py:385-392, band_engine.py analogue):
  KF = K2^3 + t*KA2*K2 + t*KA3 ,  KG = K2^2 + t*KB1*K2 + t*KB2
  outer_effective_tz shifts (r,q)->(r+1,q)  [the explicit factor t]
Block degrees (outer_specs, rekill_engine.py:311-322):
  A2: nF-degh2-1 = 71   A3: nF-1 = 107   B1: nG-degh2-1 = 35   B2: nG-1 = 71
A block constant a00 of a degree-D block sits at t^D z^0 in K(block)
  (since t^D*A(1/t,(1+z)/t) = sum a_ij t^{D-i-j}(1+z)^j), hence at t^{D+1} after the shift.
So on Delta (all outer coords 0 except the four constants b,c',d,e):
  KF = u^3 + b t^72 u + c' t^108 ,  KG = u^2 + d t^36 u + e t^72    (u := K2)

KJ := n*KF*(KG)_z - t(KF)_t*(KG)_z - m*(KF)_z*KG + (KF)_z*t(KG)_t
    = (KG)_z*[n*KF - t(KF)_t]  +  (KF)_z*[t(KG)_t - m*KG]
With n=108, m=72, deg h2 = 36:
  n*KF - t(KF)_t   = (3u^2 + b t^72)(36u - t u_t)
  t(KG)_t - m*KG   = -(2u + d t^36)(36u - t u_t)
  (KF)_z = (3u^2 + b t^72) u_z ,  (KG)_z = (2u + d t^36) u_z
=> KJ = (3u^2+b t^72)(2u+d t^36) u_z (36u - t u_t) - (3u^2+b t^72)(2u+d t^36) u_z (36u - t u_t) = 0.

IDENTICALLY ZERO -- exact, no truncation needed.  The cancellation is forced by
n = 3*degh2, m = 2*degh2 (2n = 3m = 6*degh2) and by the block degrees being
exactly nF-degh2-1, nF-1, nG-degh2-1, nG-1.  Same at (99,66): 2*99 = 3*66 = 198,
degh2 = 33, blocks 65, 98, 32, 65 -> t^66 u, t^99, t^33 u, t^66.
