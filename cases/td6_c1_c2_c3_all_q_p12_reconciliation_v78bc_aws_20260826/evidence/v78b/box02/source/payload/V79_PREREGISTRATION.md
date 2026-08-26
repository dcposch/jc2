# V79 corrected TD6 q3/all-q audit preregistration

This wave supersedes only the quarantined q3-specific V77 evidence and the
failed V78 P12 launch.  It consumes no V77 q3 values.

## V77R pure q3 scalar audit

The source is `q=t+gamma*t^3+t^25` at beta zero on the fixed-A3 generic
open.  It imports the pinned V32 source-valid infrastructure.  Required
positive support is exactly the original transport key `('g','X',0,3)` and
the direct q-prime term `3*gamma*t^2`.  The legacy q2 compiler coordinate
`qd.B` must have exact value and derivative zero.  Omission of the q3
transport source, omission of direct q-prime, deliberate q2 leakage,
lambda-prime omission, and original-source-row omission must all be detected.
The selected first-minor derivative is asserted to be exact zero; the digest
`c0730f...` is explicitly asserted to serialize zero rather than nonzero.

## V78B simultaneous P12 audit

All 22 licensed q coordinates `2..14,16..24` are retained in one square-zero
jet.  `qd.B` is exactly the q2 direction and has no other derivative support.
Every direction has a singleton original transport source and its own direct
q-prime term.  The genuine P12 is replayed from original first rows with all
varying multipliers, denominator support, source-row omission, lambda-prime
omission, and derivative-column permutation controls.  The q2 projection is
matched to V32; the q3 projection is emitted for exact comparison to V77R.

Both producers run byte-identical source on two independent AWS hosts.  They
are first-order/source-support audits at an already empty fixed-A3 base, not
family, neighborhood, full-TD6, SP-2, or JC2 theorems.
