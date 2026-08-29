# TD6 V82QST1R negative endpoint report

## Verdict

`FAILED_HARNESS_CONTROL`; no mathematical or denominator conclusion.

All eight dual-host cells (`reverse/sparse` times `q2/q10`) passed platform,
archive, source, q-prime, and exact transport-construction preflights.  Each
then ended `rc=1` at
`restrict_row_jet: assert all(variable in free_parameter for variable in row)`
before FIRST, previous/pole, or CURRENT denominator computation.

The exact cause is a source-typing boundary.  The trivariate raw transport is
a source-specific ascending echelon whose builder stops when its least
remaining variable is new; a normalized transport row may therefore retain
larger old pivots.  Treating that transport as a generic insertion-order DAG
does not eliminate every old pivot.  This is a presentation/harness failure,
not inconsistency and not evidence about `F`, `G`, or `L`.

The four per-cell stdout files are byte-identical across Box03 and r6d:

- reverse q2: `56374e97efdb68aa4e18c98b3450b8e71196b9880ebfe4a0e08afec64fbaa1cc`
- sparse q2: `d9f58024bef5c08ae4ecc32c2d3a6d7cc6f93d72198f653b860c369ae50bbbd4`
- reverse q10: `b836b49626ba35c736f26a6bf7a7a70bf110b2d85c262138cd95877d9420780b`
- sparse q10: `05dc40e0fe705fc8b88e9f9ef1be76f8681350a89e1751ff462cec19df02ebd8`

Stderr differs only in run-root/timing/resource custody fields; both hosts
report the same source assertion and traceback line.  V82QST1S is the
nonmutating successor: it preserves reviewed ascending raw transport,
restriction, and P12 division, and varies only the generic staged EJet
solvers.  This report must never be consumed as a factor-cover or fibre result.

