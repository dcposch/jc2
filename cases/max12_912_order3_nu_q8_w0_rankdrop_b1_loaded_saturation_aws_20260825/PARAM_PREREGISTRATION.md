# Polynomial-parameter exceptional-`c` route

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Repeat the full `b=1` selected saturation over `Q`, retaining `c` as a
polynomial variable.  After adding the landing centre, eliminate the five
normal variables and print the resulting ideal in `Q[c]`.  A unit ideal
excludes every finite `c`; a nonunit polynomial is only the exact list of
exceptional candidates, each of which must be rebuilt.  This route prevents
a generic `Q(c)` unit certificate from silently discarding denominator
specializations.

