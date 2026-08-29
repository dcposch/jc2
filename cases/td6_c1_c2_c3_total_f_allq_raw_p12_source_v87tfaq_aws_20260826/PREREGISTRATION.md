# TD6 V87TFAQ literal total-`(F,all licensed q)` raw P12 source lift

Date: 2026-08-26

Status at freeze: producer preregistration; no result claimed.

## Exact question

On the normalized three-center source chart put

```text
F = C*U - V^2 + U^3,
q(t) = t + sum_{e in E} q_e*t^e + t^25,
E = {2,...,14,16,...,24}.
```

The normalized target-shear coordinate `q15` remains fixed at zero; it is not
silently discarded by a tangent gauge.  Retain all 132 transport-free section
coordinates and rebuild the literal transport and raw receiver over the
untruncated multivariate polynomial ring in the 22 variables `q_e`.

Determine whether the frozen V82QST3 special certificate lifts to

```text
U^12*H^3*B3
  = a_P*P12(C,V,U,q)
    + sum_i a_i*FIRST_i(C,V,U,q)
    + F*h_F + sum_{e in E} q_e*h_e                 (1)
```

in `Q[C,V,U,q_e:e in E]_{U*H*B3}`.

## Acceleration and source typing

The client may extract only degree 12 from the frozen raw CURRENT compiler,
but the extracted formula must be a literal copy of that degree and its
all-q-zero P12 digest must equal the frozen 2,893-term V85 P12 digest.  No
post-reduction CURRENT, PREVIOUS, or POLE row is licensed.

The homogeneous transport matrix is q-independent.  Every `q_e` must enter
its exact affine source RHS at `('g','X',0,e)` and its direct derivative term
`e*q_e*t^(e-1)` in `q'`; `q2` must additionally remain assigned to the
legacy `B` coordinate even though this raw FIRST/P12 compiler does not consume
the pole-only `R3/R5` rows.

## Acceptance gates

1. Use a sparse multivariate polynomial coefficient type with no degree cap.
   Any inverse of a q-dependent value is a closed failure.
2. Require exactly one registered transport source path for each of the 22
   q variables.  Omitting either the transport or direct-`q'` path for each
   variable must change the raw FIRST family.
3. At all q variables zero, reproduce every frozen V85 FIRST/P12 digest, the
   2,893-term P12 support, and labels `0..131`.
4. Replay the frozen special identity, divide the q-zero residual exactly by
   `F`, and reproduce the frozen V85 `h_F` hash.
5. Decompose the remaining residual by an ordered, exact monomial partition
   `sum q_e*h_e`; replay (1) without dividing by any q variable in the
   coefficient ring.
6. The common denominator may have irreducible factors only among `U,H,B3`.
   Neither `F` nor a q variable may be inverted.  One common clearing must
   make every audited scalar coordinate polynomial and replay the identity.
7. Omitting P12 or an active FIRST row must break replay.
8. Run two registered AWS clients and require byte-identical mathematical
   stdout and result/inventory hashes.

## Scope firewall

A pass excludes arcs on this normalized source slice for which `F` and all 22
licensed q coordinates have positive valuation.  It does not cover `q15`, a
unit q coordinate, dead stretch, correction, orbit/pole, centering,
deck/torsion, other boundary moduli, a total-Rees chart, whole TD6, SP-2, or
JC2.
