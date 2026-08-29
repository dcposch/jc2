# Registration: `r=1` / symbolic-`d=1` V12 recurrence-product repair

Date: 2026-08-26

V10 and V11 both pass the four explicit root maps, both deck orientations,
and the unmatched double-pole identity over exact Q and `F_65521`.  Their one
diagnostic attaches to the first statement after the N16 recurrence block,
even when that statement is changed from a map evaluator to a literal print.
This identifies a delayed Singular exponent diagnostic in that preceding
block, not a root-evaluation or mathematical failure.

V12 pins V11 and changes only the N16/recurrence syntax: in the exact region
from `poly D1AC_N15` to the already passing ring maps, it replaces the single
`z^3`, single `z^2`, and three `p^2` tokens by explicit products.  The
polynomials, rational coefficients, flags, maps, and validators are unchanged.

Dual exact-Q / `F_65521` AWS runs use 24-GiB virtual-memory, 600-second
compile, and 3600-second per-process caps.  PASS is producer-tier only for
normalized `r=1` and symbolic unique-`AC`, `d=1` on `D(p*k0)`, pending hostile
review; no fan/square/order-two/JC2 conclusion follows.
