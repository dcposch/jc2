# Result: H18/q6/a6 grade-54 direct unit

Date: 2026-08-26

Status: **DUAL-AWS PASS; FIXED NORMALIZED GRAPH PRODUCER EVIDENCE.**

The exact-Q r6d lane and independent F65521 Box03 lane both passed the
preregistered complete-tail sparse extraction.  For the normalized
valuations

```text
lambda:18, a:6, X,Y:6, complements:12,
K10,K6,K2:42, J:57, E,M:0,
```

and the exact affine load graph

```text
K10=s^42*kappa,
K6=s^42*((15/32)*kappa*E^2+s^6*d6),
K2=s^42*((15/256)*kappa*E^4+s^6*d2),
```

the raw odd-row functional

```text
H=2*E^2*P3+16*E*P5+64*P7-(E^3/2)*P1
```

has no coefficient below grade 54 and satisfies exactly

```text
[s^54]H=-2*m^3*p^2.
```

Thus the fixed normalized `H=18,q=6,a=6` graph cell is empty on
`D(p*m)`: the grade-54 coefficient is a registered unit there.  Both
fields report one surviving monomial at grade 54; the characteristic-zero
and modular serialized coefficient files differ only through coefficient
encoding, as expected.

## Evidence

- immutable source/input manifest SHA:
  `f1a463578cf622c9082241858e4ea56a74055a361ed9894a37efa8c5fbdf9382`;
- exact-Q coefficient-series SHA:
  `1c761b1aac81006bdbbcb3fbec1fd476b7749c0b8ea64875234a9bf1b8c9676c`;
- F65521 coefficient-series SHA:
  `35763b3650ef00a041570d48ca4abcd2fc9e14e00e82be3d8be237638cd02e8c`;
- both external validators say
  `PASS_A_H18_Q6_A6_G54_DIRECT_UNIT_V1`.

## Scope firewall

This is a fixed normalized graph result, not yet a full ramified fan or
literal rational-source theorem.  The leading orders `(H,q,a)=(18,6,6)`
pass the necessary slope-four congruence, but descent of the entire series
still requires the separate `mu_3` fixed-locus condition on every jet.
Nothing here proves a total-Rees/Taylor realization, order two, maximum
twelve, or JC2.
