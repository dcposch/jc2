# D1 a=8,d=3 moving-connection rank jump — exact negative route

Date: 2026-08-26

## Verdict

Exact Q and two independent prime controls agree: the corrected grade-38
`k6RC` column and the `k6A^2` column have rank two in odd rows 5 and 7 on
`D(p)`.  Therefore no normalized universal functional

```
Phi7 + alpha*p*Phi5 + beta*p^2*Phi3 + gamma*p^3*Phi1
```

can annihilate both columns.  This falsifies the one-functional a=8,d=3
order-three route; it is not a cell verdict.

## Exact certificate

For the independent source monomials `k60*a0*a1` and `k60*b0*c1`, the
rows `(Phi5,Phi7)` are respectively

```
k6A^2 : (-3/16, +3p/64),
k6RC  : (-3/16, -3p/64).
```

The first column forces `alpha=+1/4`; the second forces `alpha=-1/4`.
Their determinant is `9p/512`, a unit on `D(p)`.  More strongly,

```
e7 = (32/(3p))*col(k6A^2) - (32/(3p))*col(k6RC)
```

in the two-row coefficient space.  Thus a coefficientwise terminal-target
separator is impossible without imposing additional nonlinear source
equations or splitting the chamber.

## AWS custody

All jobs used source archive SHA-256
`640b2d2aba9c58b2208added780f6146dae6271970670ce83e955aea2da658b1`,
returned engine rc 0, validator `PASS_A8D3_CONNECTION_RANKJUMP`, and zero
swap.

| field | host | tag | stdout SHA-256 |
|---|---|---|---|
| Q | Box02 | `max12_812_order2_square_d1_a8d3_connection_rankjump_q_box02_20260826T2115Z` | `bf1966e2ce4308e7b997e525773d578a7106cf5eff8f52a894edcf27a98314e1` |
| F65519 | Box03 | `max12_812_order2_square_d1_a8d3_connection_rankjump_p65519_box03_20260826T2115Z` | `bd266ce03b325a531c57aeca93104c1052fa165eabe4c8b345417cc9405d5983` |
| F65521 | r6d | `max12_812_order2_square_d1_a8d3_connection_rankjump_p65521_r6d_20260826T2115Z` | `8d051356c66e7d87d49833ecaafb5d61f22e38418f69e7826bccb84819e8ead2` |

## Firewall and next gate

This is navigation/route falsification only.  It does not show that either
source monomial can take an arbitrary value on the complete earlier zero
locus, construct a point, or decide the a=8,d=3 cell.  The next decisive
test is chamberwise: adjoin the complete earlier equations and split on the
two products (or compute their exact saturation/rank on the earlier source
scheme), then test the terminal `J` target on each branch.
