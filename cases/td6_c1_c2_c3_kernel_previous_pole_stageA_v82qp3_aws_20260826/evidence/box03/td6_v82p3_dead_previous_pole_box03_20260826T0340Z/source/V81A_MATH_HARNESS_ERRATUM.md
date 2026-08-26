# V81A square-zero dispatch erratum

The corrected-environment V81A launches at tags
`td6_v81a_corrected_joint_transport_{r6d,box03}_20260826T0214Z` both rebuilt
the symbolic-center rank-3470 base transport, then exited before propagating a
single q or dead derivative.  The expression `E3_scalar * AxisJet` invoked
`E3.__mul__`, which correctly refused to coerce an `AxisJet`.  This is a
Python operator-dispatch bug, not an algebraic inconsistency.

V81B reverses that one product to `AxisJet * E3_scalar`, the supported scalar
action.  V81A emitted no q propagation, dead column, compatibility table,
rank, kernel, or mathematical verdict and is retained as software-negative
custody only.
