# Result: `r=1` V13 standard-basis repair

Date: 2026-08-26

Status: **DUAL-AWS FAIL-CLOSED SOFTWARE CONTROL; NO VERDICT.**

V13 correctly replaced the unstandardized radical by
`std(radical(R1_I))`, and the former `// ** R1_rad is no standard basis`
warning disappeared.  Its newly inserted hand-remainder check was placed
before `R1_e1,R1_e0` were declared.  Exact Q and `F_65521` therefore emitted
the same undefined-symbol diagnostic and the fail-closed validator rejected
the missing `R1_REMAINDER_FORMULA=1` marker.  Both engines returned `rc=0`,
which is not a verdict in the presence of a Singular diagnostic.

Evidence manifests are frozen by `EVIDENCE.sha256` (SHA-256
`e65a6912425c788aa7b756d991072eca68f17d2d5004092f334c3acbefa517e5`).
V13 contributes only a negative software control and the observation that
standardizing the radical removes the V12 warning.

