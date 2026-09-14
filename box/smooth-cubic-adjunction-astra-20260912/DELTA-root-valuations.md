# ROOT bounded valuation alternative, original clocks unchanged

Separately frozen permitted input, September12,2026. Original TASK
unchanged. Check the proof, do not assume it. No peer body or new scope.

For the Weierstrass form r=t^2+a(s), try avoiding the A_m/log-canonical
import entirely. On a smooth model of any divisorial valuation v over a
point, write a0=v(s), b0=v(t), and A_v=1+v(ds wedge dt), with base
coordinates regular and centered at that point. At a generic divisor
point, expansions in a uniformizer give

 v(df wedge dg)>=v(f)+v(g)-1

for regular f,g, and thus A_v>=a0+b0. The exact identity
 dr wedge ds=2t dt wedge ds
then gives

 v(r)+a0-1 <= b0+A_v-1,
 v(r)<=A_v+b0-a0<=2A_v.

Units in a Weierstrass equation do not change v(r), and completing the
square is an analytic coordinate change. This includes a(s)=0. Strict
divisors on the base already satisfy r multiplicity<=2. Hence the
log-discrepancy of (Y,R/2) is nonnegative for every divisor, if all
valuation inequalities above are valid; this is exactly log canonicity.
For the smooth simple-ramification case the same standard coordinate
inequality suffices. No need to resolve each A_m by hand.

Please check orientation, possible cancellation, centres not at the
origin, and the tensor-square pullback inequality from the original TASK.
If this is wrong, reject it and retain your own argument. Original
reserve02:51/HARD02:54 unchanged; no task extension or descendant.
