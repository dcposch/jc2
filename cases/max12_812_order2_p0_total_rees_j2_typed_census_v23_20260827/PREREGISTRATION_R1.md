# V23R1 point-control repair

Date: 2026-08-27

R1 retains every V1 input, parser, exact arithmetic rule, chart substitution,
negative control, and scope firewall.  It pins the V1 implementation at
SHA-256 `14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501`.

The sole repair is to compare the reviewed `A00` control only after the
additional point specialization `qa1=0`.  The unspecialized pure
`(a0,qa1,rho)` terms remain census output and are not predetermined.  The
ordered `A10` control is unchanged.
