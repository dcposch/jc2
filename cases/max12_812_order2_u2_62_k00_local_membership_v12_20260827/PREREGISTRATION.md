# Preregistration: tracked-basis repair for K00 local membership V12

Date: 2026-08-27

Status: **FROZEN IMPLEMENTATION REPAIR; NO MEMBERSHIP RESULT AT REGISTRATION.**

V11 passed its local-ring toy semantics and computed a proper `ds` standard
basis, but its mandatory `G=I*T` replay failed after the producer globally
enabled `option(redSB)`.  V11 was rejected before the target reduction.

V12 makes exactly one algebra-script change: generate the identical frozen
V11 script and remove its unique `option(redSB);` directive before execution.
No row, coordinate, field, order, target, or endpoint criterion changes.  The
returned `liftstd(I,T)` basis must replay exactly as `G=I*T`; otherwise V12
again fails closed.  The four V11 local-order toy controls remain mandatory.

If the basis replay passes, V12 asks the same exact local question

```text
r7 in (r1,...,r6) Q[d0,...,d5]_(d0,...,d5) ?
```

at the registered faithfully flat Kummer normalization `C6=1`.  A zero
normal form is accepted only with a replayed unit-denominator identity
`r7*U=I*L`, `U(0)!=0`.  A nonzero normal form is saved with its leading local
class.  Both outcomes concern only the unloaded normalized K00 local ring;
neither decides mixed Lambda/load reachability, closure-first incidence,
Taylor realization, or JC2.

