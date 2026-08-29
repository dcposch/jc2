# Display-only correction

Date: 2026-08-26

While monitoring the controlling R1 deployment, two overlapping source
windows (`220,460` and `460,690`) printed line 460 twice.  This was briefly
misread in live status as a duplicated normalization loop.  Numbered source
inspection immediately showed that the deployed client contains exactly one
loop at lines 457--463.

No source was patched, no AWS job was cancelled or superseded, and no
deployment-negative status attaches to R1.  The controlling client remained
byte-for-byte SHA256
`1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757`
inside archive SHA256
`4771017f87523ae6d20cd82a8d81905e02b9fea6ecd70db1c5cb793375ddf12d`.
Both R1 deployments subsequently exited zero and are the evidence used by
this package.

