# TD6 q2-beta generic-open unit certificate — AWS exact replay

## Verdict

**PRODUCER-EXACT: the fixed source-typed A3 q2-beta family is empty on
`D(U*H*B3)` for every beta.**

Independent r6d and Box03 V43 runs exited zero with byte-identical canonical
stdout (SHA256
`a53cc30d8d6d24988b94a3c3812da42c1ac8247205322df26c504e86797a0527`).
The genuine 2,893-term P12 source polynomial reduces, through 28 original
first rows, to `-k/50+beta*T`.  The separately source-lifted staged value
`N13=(k/25)beta`, multiplied by `(25/k)T`, cancels the beta tail without
dividing by beta.  The exact residual is the unit `-k/50`.

All raw denominators were emitted.  Their radical is contained exactly in
`U*H*B3`; hence this package makes no claim on those divisors.  The direct
q-prime term is retained, its omission is detected, and omitting N13 fails
the unit identity.  Legacy V37 outputs are preserved only as reporter-
custody negative controls; V43 uses canonical 18-coordinate E3 serialization
and agrees byte-for-byte across hosts.

The immutable package is
`cases/td6_c1_c2_c3_q2_beta_generic_open_aws_20260825/`.  This is one open
of the complete fixed-A3 atlas.  It does not vary a fourth source modulus,
kill whole TD6 or SP-2, prove a landing theorem, or resolve JC2.  Hostile
review of the composed atlas remains pending.
