# Sparse T2/T3 projection prototype status

This prototype is **not a branch decision**.  It never ran a Groebner basis.

The exact checks are:

- Proposition 3.1 monomial enumeration and shifts.  Through the requested
  defect, the 99 charts retain shifts `0,11`; D108 retains `0,9,18`.
- The equality-weight cancellations
  `T2^3-lambda2^3*F*G` and
  `T2^4-lambda2^4*F*G^2` at the two-point top.
- The formal leading two-row determinants reduce, using `F^2=G^3`, to
  `-5*lambda2^3*G^3` and `-7*lambda2^4*G^4`.  Their leading-z scalars are
  units after the required `lambda2` localization.

The sparse dependency run found support-incidence matchings covering every
outer `A3c/B2c` coordinate: 374/374 on each 99 chart and 371/371 on D108.
The resulting candidate cores are 73, 71, and 134 variables; allowing all
coefficient-coordinate incidences gives candidates 17, 15, and 18.  These
are only combinatorial occurrence matchings.  They do not prove that the
matched coefficients remain constant/unit leaders after preceding
substitutions.  Exactly **0** of those matched coordinate pivots received a
complete triangular quotient-map certification.

Therefore the proposed under-100 reduction is **unproved** and no exact-Q
Singular decision was launched from it.  The correct status from this
prototype is `COMPUTE-BOUND/CONSTRUCTION-BOUND OPEN`, never UNIT or PROPER.

Files:

- `prototype_support_projection.py`
- `prototype-support-results.json`

