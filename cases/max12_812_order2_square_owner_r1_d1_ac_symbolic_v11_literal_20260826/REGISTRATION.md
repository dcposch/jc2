# Registration: `r=1` / symbolic-`d=1` V11 literal recurrence sentinel

Date: 2026-08-26

V10's explicit ring maps passed both root orientations and the unmatched
double-pole identity over exact Q and `F_65521`.  Its only validator failure
was a Singular serialization diagnostic at
`string(D1AC_rec15)`, even though the following combined numerical guard
successfully evaluated `D1AC_rec15=1`; `rec16` also equals one.  V10 is a
producer-positive, presentation-negative control.

V11 pins V10 and changes only the two recurrence print statements.  It first
checks `D1AC_rec15==1 && D1AC_rec16==1` numerically and fails closed otherwise,
then prints the two literal PASS sentinels.  Every source polynomial, rational
coefficient, ring map, orientation, residue, and mathematical guard is byte-
identical to V10.

Dual exact-Q / `F_65521` AWS runs use 24-GiB virtual-memory, 600-second
compile, and 3600-second per-process caps.  PASS remains producer-tier only
for the normalized `r=1` receiver and symbolic unique-`AC`, `d=1` receiver on
`D(p*k0)`, pending hostile review.  No fan/square/order-two/JC2 claim follows.
