# V1 fail-closed parser custody

Both V1 validators rejected the run before any algebraic endpoint could be
consumed.  The generated connection controls wrote terms such as
`p^2/32`; Singular parsed the denominator as part of the exponent and
reported `poly ^ number failed`.  Subsequent undefined-symbol diagnostics
made the exact-Q output unusable and caused the finite-field engine to
segfault inside a library call on malformed state.  The V1 failure branches
also used the unsupported forms `quit(81)` and `quit(82)`.

The retrieved directories `aws_q_v1_negative` and
`aws_p65521_v1_negative` are immutable software-negative custody.  V2 adds
parentheses around powers before rational division and uses plain `quit;` in
failure branches.  It changes no Faber tail, Laurent coefficient, connection
identity, affine equation, proposed component, ring, term order, or ideal
operation.  V1 establishes no mathematical result.
