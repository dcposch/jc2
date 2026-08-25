# Registration: max12 `(9,12)` order-three double-`B` algebraicity

- Date: 2026-08-24
- Status: producer-exact; hostile different-model review required
- Report: `xmodel/max12-912-order3-double-b-q-algebraicity-20260824.md`
- Reviewed inputs: order-three terminal row; normalized root-free norm and double-`B` equation
- Frozen computation: corrected characteristic-zero saturated basis plus exact `p=0` decomposition

On the normalized `k=mu=0`, `nu=1` double-`B` coefficient leaf, the
nonzero-`p` saturation has an exact reconstructed characteristic-zero
Groebner basis whose initial ideal is zero-dimensional with 1,188 standard
monomials.  The `p=0` slice is exactly the intersection of two reduced
one-dimensional components of degrees two and three.  Therefore `p` is
algebraic over `Q` at every coefficient-field point.  On an actual trajectory
the relation `3*p+10*r8=0` then forces `r8` constant, contradicting
`9*r8'=j/u!=0`.

The equality of the reconstructed basis with the source ideal remains the
exact `msolve 0.10.1` trust boundary pending independent CAS confirmation and
hostile different-model review.  No other norm leaf, all-`(9,12)`,
maximum-twelve, counterexample, or JC2 conclusion is registered.
