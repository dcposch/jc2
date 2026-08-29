# V1 fail-closed custody

Both initial AWS engines returned `rc=0` and independently computed the
proposed three-component reduced support, but the validators correctly failed
closed.  Loading `elim.lib` immediately before `primdec.lib` caused a long
sequence of deterministic `// ** redefining ...` diagnostics.  No algebraic
error occurred, but diagnostic-bearing output is not evidence-grade.

The retrieved directories `aws_q_v1_negative` and
`aws_p65521_v1_negative` are immutable negative custody.  V2 removes only the
redundant explicit `elim.lib` load; `primdec.lib` supplies the required
procedures.  The recurrence, seven equations, ideals, proposed components,
term order, and every endpoint check are unchanged.

