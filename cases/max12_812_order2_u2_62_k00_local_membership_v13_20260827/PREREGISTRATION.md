# Preregistration: syntax-safe tracked-basis repair for K00 local membership V13

Date: 2026-08-27

Status: **FROZEN IMPLEMENTATION REPAIR; NO MEMBERSHIP RESULT AT REGISTRATION.**

V11 was rejected because its tracked `liftstd` basis did not replay after
`option(redSB)`.  V12 removed that executable directive but its compiler then
mistook the same words inside a comment for a surviving directive and stopped
before algebra.

V13 repeats the identical V12 mathematical repair and changes only the
compiler's syntax sentinel: the generated source must contain zero exact
occurrences of the executable line `option(redSB);`.  The replacement comment
does not contain that token.  No row, coordinate, field, local order, target,
or endpoint criterion changes from frozen V11.

The four local-semantics toys and exact `G=I*T` basis replay remain mandatory.
Only then is `r7` reduced in the normalized `ds` local ring.  Membership is
accepted only with a replayed unit-denominator lift; nonmembership is accepted
only with a saved nonzero local residual.  Either outcome is limited to the
unloaded normalized K00 local ring and says nothing by itself about mixed
Lambda/load reachability, closure-first incidence, Taylor realization, or JC2.

