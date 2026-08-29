# Affine-Faber `A`: H17 open relative-cone direct unit

Date: 2026-08-26

Status: **PRODUCER THEOREM; HOSTILE REVIEW PENDING.**

## Statement

Work in characteristic zero in the internal normalized moving-discriminant
graph coordinates

```text
(J,K2,K6,K10,S0,S1,R0,R1,Y,X,a,lambda,M,E),
```

with `E`, `M`, and the leading coefficient of `lambda` units.  Give these
coordinates the H17 equality-wall valuations

```text
v(lambda)=17,
v(X)=v(Y)=q,
v(R0)=v(R1)=v(S0)=v(S1)=2q,
v(a)=17-2q,
v(K10)=v(K6)=v(K2)=42,
v(J)=57,
v(E)=v(M)=0.                                      (1.1)
```

Allow rational valuations after a common ramified base change.  If

```text
17/4 < q < 7,                                     (1.2)
```

then simultaneous vanishing of the seven raw ordinary-Faber rows through
valuation `51` is impossible.

This is a theorem only in the displayed internal normalized graph
coordinates.  It is not a literal source or total-Rees coverage statement.

## Exact functional and proof

Let `P1,...,P7` be the complete raw ordinary-Faber row series and form

```text
F = P7 - E^2 P3/32 + E^3 P1/64,
G = E^2 P3 + 16 E P5 + 96 P7,
Hseries = G - 32 F
        = 2 E^2 P3 + 16 E P5 + 64 P7 - E^3 P1/2.  (2.1)
```

The frozen exact sparse tail reconstruction gives 630 nonzero abstract
monomials in `Hseries`.  Exact-Q and `F65521` independently have identical
support and compatible coefficients.  Comparing all 630 affine functions
under (1.1) shows that throughout (1.2) the unique least term is

```text
-2 lambda^3 M^3 E^2,                              (2.2)
```

of valuation `51`.  Its coefficient is a unit.  Every moving coefficient
jet has positive excess and cannot lower another abstract monomial.

If all raw rows through valuation 51 vanished, then the coefficient of
every series-linear combination (2.1) through valuation 51 would vanish.
This contradicts (2.2).  The target `J` starts at 57.  All three loads at
42 are included in the 630-term comparison; none is omitted.

## Sharp support boundaries

Inside the mixed equality domain `4<q<17/2`, the exact strict interval is
(1.2).  At its lower endpoint `q=17/4`, five complement monomials of weight
`34+4q` tie (2.2).  At its upper endpoint `q=7`, the three loaded terms

```text
a^3 E^3*((155/16)K10 E^4 - 23 K6 E^2 + 40 K2)    (3.1)
```

of weight `93-6q` tie it.  Neither boundary is claimed here.

## Custody

```text
1244a648d3bc761ae6fe9dbc1be72cad3e09b650d3d98109ebd2b4081ac1bb15
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/RESULT.md
3c8f207fc7522b58835758126a1a15841e76c92e3bc8beacebb6e22c55c81f06
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/EVIDENCE.sha256
8bf9aa5e7485555fbeb0a19c0b9ae2dc106715b6c13da850c4bfdfe22925e237
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/FREEZE.sha256
6aec97c6b03eaca66e6a3df9d80da41884ae5225836b96a5ab269962dcfe4365
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/RESULTS.sha256
60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df
  cases/max12_812_order2_affine_faber_a_h17_direct_unit_relative_cone_v9_20260826/evidence/Box02/aws_qcone/output/hseries_exact_support.json
```

## Firewall

No claim is made at either endpoint, outside (1.2), on `E*M=0`, for a unit
kernel coordinate (`q=0`), for another normal/load schedule, for graph
accessibility from the literal source, or for Cech/normalized-Rees/total-Rees
coverage.  This does not prove the whole exceptional `A` fan, order two,
`(8,12)`, maximum twelve, or JC2.
