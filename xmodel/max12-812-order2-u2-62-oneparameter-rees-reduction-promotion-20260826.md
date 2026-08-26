# Promotion: exact one-parameter presentation of the order-two `U=2,[6,2]` Rees boundary

Date: 2026-08-26

Status: **PROMOTED ALGEBRAIC REDUCTION; NO SATURATION OR EMPTINESS VERDICT.**

## Frozen chain

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md
0fa0dc4afb160ae4b9ed6bc195e1158e44b92cdc5bb5ea1619a146e9d52aac96
  xmodel/max12-812-order2-u2-62-oneparameter-rees-runit-delta-review-grok-20260826.md
```

Both independent hostile reviews end `CONFIRMED`.

## Exact promoted statement

For the source-typed order-two `U=2`, `[6,2]` client, put

```text
R=1+tau,  C_even=B_even,  C_odd=R B_odd,
J=Rj,     Lambda=tau^3 varrho.
```

After localizing at `R`, the full seven-row V2 family, with all retained
loads `k10,k6,k2,mu2,mu4,mu6,J`, is the flat pullback of

```text
Phi_ell =
 r_ell(C,Lambda^2 k10,Lambda^6 k6,Lambda^10 k2)
 -Lambda^(12+ell) delta_ell,

(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4).
```

Saturating by the generic-chart product, taking the central fibre, and
saturating by the coefficient irrelevant ideal gives exactly the same
closed subscheme in the one-parameter and original two-parameter
presentations.  The equality is scheme-theoretic, so it preserves
nilpotents and embedded components.

The original V2 ring does not invert `R`.  The exact comparison is not the
false off-boundary identity `K=K_R cap S`.  If

```text
S = original polynomial ring,
h = tau varrho j,
K = I:h^infinity,
b = (tau,varrho),
R = 1+tau,
```

then localization contracts to `K:R^infinity`, and the load-bearing identity
is

```text
K+b = (K:R^infinity)+b.
```

Indeed, `R^N f in K` implies
`f=R^N f-(R^N-1)f in K+b`, since `R^N-1 in (tau)`.  This is equality of
ideals, not radicals.  Localization commutes with the stabilized
`h`-saturation; applying the same final irrelevant saturation preserves the
equality.

## Computational status and firewall

The dual exact-Q/good-prime AWS one-parameter saturations are experiments,
not evidence for this promotion.  This note does not claim that the boundary
is empty or nonempty, does not realize either Taylor family, does not exclude
the `[6,2]` profile, and does not close order two, `(8,12)`, maximum twelve,
or JC2.
