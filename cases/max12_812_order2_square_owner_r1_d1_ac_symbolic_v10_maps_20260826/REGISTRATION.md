# Registration: `r=1` / symbolic-`d=1` V10 ring-map evaluator

Date: 2026-08-26

V8 isolated the two Singular processes and V9 replaced quotient-ideal
evaluation by sequential substitution.  Both passed the complete source,
Faber-row, scaling, and recurrence layers, but both failed closed at the first
D1 root evaluator with the same `poly ^ number` diagnostic.  Thus neither
failure is mathematical; together they isolate a Singular evaluator/API
pathology.

V10 pins V9 and changes only this terminal evaluator.  It preserves the D1
source ring as `Rd1`, creates a fresh target ring, and evaluates
`D1AC_N15,D1AC_N16` with four explicit maps: the two deck root allocations
and their evaluations at the allocated roots.  This uses neither `subst` nor
`std`.  The compiler asserts all maps have exactly the 27 source-variable
images, and the fail-closed validator rejects diagnostics with leading spaces.

Dual exact-Q / `F_65521` runs are registered on Box03/r6d with 24-GiB virtual
memory, 600-second compile, and 3600-second per-process caps.  PASS remains a
producer result only for normalized `r=1` and symbolic unique-`AC`, `d=1` on
`D(p*k0)`.  No fan, square/order-two, maximum-twelve, or JC2 claim follows.
