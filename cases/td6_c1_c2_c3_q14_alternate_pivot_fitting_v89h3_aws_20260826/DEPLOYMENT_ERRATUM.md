# V89H3 V1 deployment erratum

Date: 2026-08-26

Both V1 wrappers stopped before source import or algebra because
`launch_host.sh` omitted the frozen ancestry sentinel
`TD6_Q_EXPONENT=2`. The byte-identical pre-algebra failure is not
mathematical evidence.

V2 added only that environment export and rebuilt an immutable source archive,
but both wrappers again stopped before source algebra: V89H3 had reused the
ancestry sentinel name `TD6_PIVOT_POLICY=registered-single-exchange`, while
the imported literal V85 compiler correctly requires
`TD6_PIVOT_POLICY=ascending`.  This byte-identical import-time assertion is
also not mathematical evidence.

V3 restores the frozen ancestry sentinel to `ascending` and places V89H3's
bounded search policy in the distinct sentinel
`TD6_V89H3_PIVOT_POLICY=registered-single-exchange`.  It rebuilds a new
immutable source archive, but again stopped before source algebra because the
V89H3 scope value had reused the frozen ancestry name `TD6_PIVOT_SCOPE`,
which literal V85 correctly requires to equal `all-staged`.

V4 restores `TD6_PIVOT_SCOPE=all-staged` and uses the distinct
`TD6_V89H3_PIVOT_SCOPE=all-132-section-columns` for this bounded client.
It rebuilds a new archive and uses new AWS roots and tags.  None of V1--V3
is consumed as algebra.
