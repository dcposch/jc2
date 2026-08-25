# V1 status: affine-assumption failure, no mathematical endpoint

All three AWS runs stopped at the same fail-closed assertion in
`extract_affine(stage2_function, ...)`: the restricted exact `/81` carry map
does not obey the pure `2e_i` affine identity.  Exit code was one after about
19–21 seconds with 33–34 MiB peak RSS.

This establishes neither SAT nor UNSAT.  It retracts only the V1 assumption
that the full accepted-digit tower could be handled as consecutive affine
systems in canonical `0,1,2` representatives.  The first `/27` layer passed
its affine design; canonical representative wrap creates a genuinely
nonlinear next carry.  V2 consumes these bytes as a deployment/source-typing
negative control and must solve the exact nonlinear function on the full
first-layer affine kernel.

AWS custody: `/home/ubuntu/jobs/as_q3_two_level_q2_q1_20260825T122013Z` on
Box02.  Copied logs are under `aws_run_v1/`.
