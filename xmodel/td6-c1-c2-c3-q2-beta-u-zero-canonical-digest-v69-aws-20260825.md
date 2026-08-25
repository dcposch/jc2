# TD6 raw `U=0` canonical-digest repair

V69 diagnoses and repairs a custody defect in the V33 raw `U=0` report.
The old digest function hashed Python's default `repr(E3)`, hence embedded
process-specific object addresses.  This explains the otherwise isolated
Box02/Box03 hash disagreement; ranks, row key, degree-zero unit obstruction,
denominator one, original-row replay, and verdict had agreed exactly.

The repaired serializer uses sorted exact `Rat3` coordinate data.  Independent
Box02 and Box03 runs returned rc 0 with byte-identical stdout SHA256
`9726fb09a9279c7c19c507eeafc5b541bfd2d89e9d34a7e972b73badde042734`.
The frozen supplement is
`cases/td6_c1_c2_c3_q2_beta_u_zero_canonical_digest_v69_aws_20260825/`.

This is a reporter/custody repair, not a new theorem.  It preserves the exact
narrow statement that the raw `U=0` divisor is empty for all `beta` in the
fixed source-typed A3 q2 family, subject to the still-pending hostile review
of that underlying source theorem.  No `U!=0`, whole-TD6, SP-2, landing, or
JC2 conclusion follows.
