# Preregistration: K00 filtered first-load obstruction V18

Date: 2026-08-27

Status: **DESIGN FROZEN BEFORE ANY FILTERED-RANK OUTPUT; ALL CUTOFFS OPEN.**

## Charged invariant

Work in the normalized K00 coefficient-local ring

```text
R=Q[d0,d1,d2,d3,d4,d5],  m=(d0,...,d5)
```

and consume a completed V17 lane.  For each
`X in {k10,k6,k2}`, V17 supplies

```text
I=(r1,...,r6),
E_X=(sum_i s_i*a_i^X : s in Syz_R(r1,...,r6)),
J_X=I+E_X,
D_X=h*a_7^X-sum_i u_i*a_i^X.
```

V18 is applicable only when the consumed V17 lane has replayed the full
six-row syzygy module and returned `D_X notin (J_X)_m`.  It must not replace
`Syz(r1,...,r6)` by the seven-row module.

For every cutoff `2<=D<=6`, form the complete truncated multiplication map

```text
M_X,D : direct_sum_{g in G_X} R_{<=D-ord_m(g)} -> R/m^(D+1),
        (q_g) |-> sum_g q_g*g mod m^(D+1),
G_X=(r1,...,r6, all 66 frozen generators of E_X).
```

All monomial multipliers through the displayed bound are mandatory.  The
decisive question is

```text
D_X in J_X+m^(D+1)  iff  rank(M_X,D)=rank([M_X,D | D_X]).
```

The first incompatible cutoff, if at most six, is the first nonzero
associated filtered order of the V17 class.  Its numerical value and all
three direction outcomes are open at freeze time.  If no cutoff fails, the
only allowed endpoint is `NO_FAILURE_THROUGH_D6`.

## Evidence and compatibility

For every compatible cutoff the producer must serialize an exact/modular
multiplier vector and replay every coefficient of the truncated identity.
At the first exact-Q incompatible cutoff it must serialize a nonzero left
functional annihilating every column and pairing nontrivially with the
target.  The highest compatible lift automatically replays every lower
cutoff; conclusions must not depend on extending a previously chosen RREF
representative.  Matrices, row/column maps, source hashes, and solutions or
dual certificates are immutable evidence.

`p=65521` is navigation/software control only.  Exact-Q conclusions require
the exact V17 lane and an exact rational certificate replay.

## Both-outcome scope and firewall

A first filtered load class is a coefficient-local deformation obstruction.
It is not an arc obstruction by itself: a nonzero germ may vanish to high
order on a constrained transverse arc.  V18 does not couple load directions,
restore their honest `Lambda` weights `2,6,10`, impose the
`mu2,mu4,mu6,Jdet` targets through order 19, restrict to the honest source
image, or decide closure incidence, Taylor realization, order two, maximum
twelve, or JC2.
