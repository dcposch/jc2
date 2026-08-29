# TD6 V89K1 `K` modulo `F` unit gate

Date: 2026-08-26

Status: exact producer gate; no result claimed before dual AWS replay.

Using the literal V85 base definitions

```text
F  = C*U - V^2 + U^3,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6
```

and the exact H1 obstruction factor

```text
K = 2*C*V^2*U + 16*C*U^4 - V^4 - 14*V^2*U^3 + 16*U^6,
```

verify coefficientwise the proposed identity

```text
B3 = K + 2*F*(2*C*U - V^2 + 2*U^3).
```

Emit canonical formulas and SHA256 digests, verify the specialization
`F=0` gives `K=B3=V^4`, and require a nonzero coefficient-perturbation
control.  The only consequence is that on `D(B3)` the residue class of `K`
is a unit modulo every ideal containing `F`.  This is not a claim that `K`
is a unit modulo `(P12,FIRST)` without `F`, and it does not by itself consume
or repair H1's rational source multipliers.

Run byte-identically on two AWS hosts.  Do not invert `K`, `F`, or any q
expression.  Make no source-point, fixed-A3, TD6, SP-2, or JC2 claim.
