# V26R1C tracked-matrix validator erratum

Status: `VALIDATOR_FAILURE_PRESERVED_NO_VERDICT`.

The R1C rollback-tagged run reached the exact-Q preflight and emitted the
provisional markers `PROPER`, affine dimension `3`, generator count `9`, and
minor-mutation index `1`.  It then stopped at the tracked `liftstd` identity
validator.  Those markers are not consumed as a theorem result.

Independent inspection showed every entry of
`matrix(J)*T-matrix(G)` was exactly zero.  A frozen toy diagnostic showed the
cause: in Singular, comparing a multi-column zero matrix directly with scalar
`0` returns false equality semantics (`D!=0` fires for a zero `1 x 2`
matrix).  The R1C validator therefore rejected a valid identity before any
certificate was serialized.

R1D replaces every matrix-to-scalar zero comparison with explicit entrywise
polynomial checks.  It also makes the unit branch explicitly inspect its
`1 x 1` entries so both branches have uniform, typed semantics.  Transform
deletion mutations now require at least one nonzero residual entry.  No
matrix, ideal, minor, field, standard-basis algorithm, resource cap,
rollback tag, or mathematical endpoint changed.

R1C remains validator evidence only: no grade-seven stratum, jet, arc,
closure, or JC2 conclusion follows from it.
