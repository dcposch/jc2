# TD6 q2-beta raw `U=0` theorem

## Verdict

**PRODUCER-EXACT PASS; hostile review pending.**

For the fixed source-typed normalized TD6 section with
`q_beta=t+beta*t^2+t^25`, the full raw `U=0` rebuild is inconsistent already
in the first-J band.  After transport rank `3470/3602`, the first system has
rank `36/132`; its dependent `('X-2',14)` row has beta-degree zero and an
exact 14-row original-source certificate.  The compatibility ideal has
monic gcd `1`, and the complete Bezout/certificate denominator is `1`.
Therefore the entire `U=0` center divisor is empty for every beta over every
extension of `E` in this fixed section.

The frozen producer package is
`cases/td6_c1_c2_c3_q2_beta_u_zero_aws_20260825/`; archive SHA256
`718457551eab373d043e9b711aa8df06fc18fccecb31bb97c2250284f55c48e2`,
theorem stdout SHA256
`94e2267d62b162f44abaf32d36405440dd213e1efb4f446cc281ace08b47d0da`.

This does not cover `U!=0` or vary any other TD6 modulus, and it makes no
whole-TD6, SP-2, landing, or JC2 claim.
