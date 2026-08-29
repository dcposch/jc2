# TD6 V82QST3 raw `F=0` genuine-P12 source certificate

Date: 2026-08-26

## Question

The V82QST2 staged-CURRENT client found ten exact base incompatibilities over
`Q(U,V)` after the raw substitution

```text
C0=(V^2-U^3)/U,  hence F=C0*U-V^2+U^3=0,
```

but its deliberately global chart denominator contains thirteen factors not
registered in

```text
D(U*V*(V^2-4U^3)*(V^2+8U^3)).
```

Determine whether the earlier genuine-P12 division against the original
FIRST rows gives a divisor-safe localized source identity on this same fixed
source-typed A3 specialization.

## Frozen source and exact method

Import the frozen V82QST2 source file with SHA-256
`5a1054269237d9a2da5c7f5e51ae001ad59f61607ac36f2e7a9b059c972c74d5`.
That file itself pins the original compiler `replay_shard.py` at
`a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`.

Rebuild transport and FIRST only after `F=0`.  Compile the genuine raw P12
polynomial directly from the six unreduced section lists
`f1,f2,f3,g1,g2,g3`; the later staged row merely keyed `('X0',12)` is not the
certificate object.  Divide genuine P12 by the exact 38 FIRST pivots, lift
the quotients to the packed FIRST source rows, and replay

```text
P12 - remainder = sum_i lambda_i FIRST_i.
```

If the remainder is a nonzero scalar in the frozen degree-18 coefficient
field, multiply by its inverse.  Let `s` be the common denominator of the
raw P12, FIRST rows, lifted multipliers, inverse, and every termwise source
product.  Emit and verify the cleared identity

```text
s = (s/remainder)*P12 - sum_i (s/remainder)*lambda_i*FIRST_i.
```

Every coordinate of every cleared multiplier and termwise product must lie
in `Q[U,V]`.  Acceptance additionally requires that the radical of `s` be a
subset of `U,V,V^2-4U^3,V^2+8U^3`, exact source replay, an omission-negative
control, no formal `C`, and agreement of the q2 and q10 base projections.

## Decision and scope

Passing closes only the registered raw `F=0` open for the **fixed A3 base
system** at the genuine-FIRST/P12 gate.  It adjudicates the over-conservative
V82QST2 denominator reporter; it does not certify its staged CURRENT tangent
table.

This is not yet a valuative-propagation certificate for a total TD6 family.
In particular, q/dead-stretch/correction variables remain frozen, and the
transport parameterization is not lifted here to a single total-family raw
ideal with an independent parameter `t=F`.  Therefore this client does not
emit or claim a total-family identity
`s=sum h_i f_i+F*h`, a positive-`F` arc exclusion, TD6, SP-2, or JC2.
