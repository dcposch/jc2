# K3 receiver V3: target literal and elimination API repair

Date: 2026-08-26

Status: **IMMUTABLE AWS-ONLY V3; NO RESULT.**

V2 compiled and printed all seven K3 rows, but failed closed on two further
software/API points:

1. Singular parsed `-rho^38/4` as a nonintegral exponent in the terminal
   target comparison.  V3 emits `(-1/4)*rho^38`.
2. Fleet `eliminate` accepts a polynomial product or `intvec`, not an ideal,
   as its second argument.  V3 passes the product of all ten correction
   variables.

V3 retains V2's `(-3/16)*b^2` repair and changes nothing mathematical.
V1 and V2 failed endpoints remain immutable controls.
