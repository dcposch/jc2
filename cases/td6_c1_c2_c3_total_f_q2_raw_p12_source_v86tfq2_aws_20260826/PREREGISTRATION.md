# TD6 V86TFQ2 literal total-`(F,q2)` raw P12 source lift

Date: 2026-08-26

Status at freeze: producer preregistration; no result claimed.

## Exact question

On the normalized three-center source chart put

```text
F = C*U - V^2 + U^3,
q_beta(t) = t + beta*t^2 + t^25,
q_beta'(t) = 1 + 2*beta*t + 25*t^24.
```

Retain all 132 transport-free section coordinates.  Rebuild the transport
with the literal affine `beta` contribution to the source RHS at
`('g','X',0,2)`, and rebuild the raw receiver with literal `B=beta` and the
displayed `q_beta'`.  Determine whether the frozen V82QST3 special-fibre
certificate lifts to an exact identity

```text
U^12*H^3*B3
  = a_P*P12(C,V,U,beta)
    + sum_i a_i*FIRST_i(C,V,U,beta)
    + F*h_F + beta*h_beta                            (1)
```

in `Q[C,V,U,beta]_{U*H*B3}`, where

```text
H  = C - 3*U^2,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6.
```

The coefficient ring in `beta` must be an untruncated sparse polynomial
ring.  A square-zero jet or a fixed beta-degree truncation is forbidden.

## Frozen inputs

- V85TF1 client, which pins the original generic compiler and the V82QST3
  certificate;
- original generic compiler SHA-256
  `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`;
- V82QST3 cleared multiplier table SHA-256
  `8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`;
- V85TF1 beta-zero quotient SHA-256
  `7434b0a7434288e421ad300e93c5da8084f69f19a801298ec6ec05bf9b85bb70`.

Only genuine raw P12 and packed raw FIRST rows are licensed.  PREVIOUS/POLE,
staged CURRENT, and any post-reduction row keyed only by `('X0',12)` are
forbidden.

## Acceptance gates

1. Rebuild the beta-polynomial transport from original source rows.  Its
   matrix is beta-independent; its affine RHS must include the exact source
   vector at `('g','X',0,2)`.  No transport compatibility may be discarded.
2. Configure the raw receiver with literal `B=beta` and the exact
   `q_beta'`.  Omitting either the transport-RHS beta term or the direct
   `2*beta*t` term must change the emitted raw source family.
3. At `beta=0`, every raw FIRST row and genuine 2,893-term P12 must agree
   exactly with V85TF1.  After also setting `F=0`, replay the frozen V82QST3
   identity and parameter labels `0..131` exactly.
4. Form the total residual of (1).  Its beta-zero coefficient must divide
   exactly by `F` and reproduce the frozen V85TF1 quotient hash.  Every
   positive beta coefficient must divide exactly by `beta` by an exponent
   shift, with no beta truncation.
5. The common coefficient denominator of sources, multipliers, products,
   `h_F`, and `h_beta` may have irreducible factors only among `U,H,B3`.
   Neither `F` nor `beta` may be inverted.  After one registered clearing,
   replay (1) coefficientwise and require all coefficients polynomial.
6. Omitting P12 or one active FIRST source row must break the replay.
7. Run independent q2-labelled clients on two registered AWS hosts and
   require byte-identical mathematical result and certificate hashes.

Any source mismatch, lost beta path, truncation, failed exact division,
outside denominator, implicit `F`/`beta` inversion, or failed omission
control is a closed failure.

## Scope firewall

A pass excludes DVR arcs in this normalized source chart for which both
`F` and `beta` lie in the maximal ideal, on `D(U*H*B3)`, while all 132
section coordinates remain free.  It does not totalize the other q jets,
dead stretch, correction, orbit/pole, centering, or boundary moduli; cover
unit-beta fibres; prove a full total chart; or prove fixed A3, TD6, SP-2, or
JC2.

