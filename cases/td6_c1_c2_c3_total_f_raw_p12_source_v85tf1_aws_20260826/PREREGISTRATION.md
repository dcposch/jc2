# TD6 V85TF1 literal total-`F` raw P12 source lift

Date: 2026-08-26

Status at freeze: producer preregistration; no result claimed.

## Exact question

Let

```text
F = C*U - V^2 + U^3,
H = C - 3*U^2,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6.
```

In the one-base-parameter total slice obtained by allowing `F` to vary while
retaining all 132 transport-free section coordinates, determine whether the
frozen V82QST3 special-fibre certificate lifts to an identity in
`Q[C,V,U]_{U*H*B3}`:

```text
U^12*H^3*B3 = a_P*P12(C,V,U)
              + sum_i a_i*FIRST_i(C,V,U) + F*h.
```

The map to the special fibre is the literal localization isomorphism

```text
Q[t,U,V,U^-1] -> Q[C,U,V,U^-1],
t |-> F,  C |-> (V^2-U^3+t)/U.
```

At `F=0`, the left side must specialize exactly to the V82QST3 clearer
`U^9*V^4*(V^2-4U^3)^3`.

## Frozen inputs

- generic original compiler: V82QST1C `replay_shard.py`, SHA-256
  `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`;
- V82QST2 source archive, SHA-256
  `731eed3fdbaaf17b9f14468ca885f16bf4008f1b43bb8b276a99a530966a6d5c`;
- V82QST3 cleared multiplier table, SHA-256
  `8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`.

Only the original generic transport, raw FIRST rows, and genuine raw P12 are
licensed.  PREVIOUS/POLE, staged CURRENT, and the later row merely keyed
`('X0',12)` are forbidden.

## Acceptance gates

1. Rebuild generic and `F=0` transport independently from the original
   compiler.  After coefficientwise specialization `C=(V^2-U^3)/U`, every
   raw FIRST source polynomial and genuine P12 must agree exactly, with the
   same parameter labels.
2. Parse the frozen V82QST3 multiplier table and replay its special identity
   against the newly rebuilt `F=0` rows.  The table must use only P12 and
   exact keyed FIRST rows.
3. Lift those multipliers without introducing `C` or `F`, form the total
   residual, and divide every scalar coordinate exactly by `F`.  The quotient
   must have no `F` denominator.
4. The common denominator of source terms, lifted multipliers, and `h` may
   have irreducible factors only among `U,H,B3`.  After this one clearing,
   every scalar coordinate of every emitted multiplier, quotient, and
   termwise product must be polynomial.
5. Replay both the localized and cleared total identities exactly.  Omission
   of P12 and omission of one active FIRST row must each fail.
6. Require all 132 transport-free parameter labels to occur in the retained
   raw source family.  Report, rather than hide, that the boundary polynomial,
   dead stretch, F1 orbit/pole data, and non-`F` base directions remain frozen.
7. Run q2 and q10 on two AWS hosts.  Exact mathematical result streams and
   emitted certificate hashes must agree across all successful lanes.

Any base-change mismatch, missing source label, nondivision by `F`, outside
denominator factor, implicit `F` inversion, or failed omission control is a
closed failure.

## Scope firewall

A pass proves only a literal total-`F` identity on this normalized,
source-typed A3 slice and the registered open `D(U*H*B3)`.  It is not a total
chart in the q, dead-stretch, correction, orbit, pole, centering, or boundary
moduli.  It does not by itself prove an open cover, whole fixed A3, TD6,
SP-2, or JC2.
