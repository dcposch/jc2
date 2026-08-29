# `Q(t)` to `Q(rho)` field bridge

Date: 2026-08-27

The frozen total rows are even in `rho`, and the compiler verifies this term
by term before replacing `rho^(2j)` by `t^j`.  Hence the dehomogenized ideal
is defined over `K=Q(t)`.

The map

`Q(t) -> Q(rho),  t |-> rho^2`

is an injective degree-two field extension.  It is faithfully flat, so for
the 64-variable reduced ideal `I` obtained after the exact `ez9` pivot,

`I=(1) in Q(t)[X']`

if and only if

`I Q(rho)[X']=(1) in Q(rho)[X']`.

Indeed, the forward direction is scalar extension.  Conversely, if `I` were
proper, the nonzero `Q(t)`-vector space `Q(t)[X']/I` would remain nonzero
after tensoring with the field `Q(rho)`.  Thus the exact `Q(t)` computation
decides precisely the required generic `Q(rho)` conjunct; it is not a
smaller rational-specialization screen.

This is an additive explanation of the preregistered coefficient field and
does not alter the already frozen AWS input.

