# V43C3D preregistration: no-expansion final-assumption diagnostic

This additive diagnostic does not claim an ideal-membership result.  It loads
the immutable V43C3 producer at SHA-256
`aece88b6a74ac207a031c5b996e8e8d804d2efd464c83a889a91114177aedeed`,
runs its unchanged proof construction through every rebasing, ClearPower, and
CombineBranches guard, and intercepts only the final `PruneZeroTerms` call.

The registered output is the exact list of surviving assumption labels, their
arithmetic-DAG root indices, and structural (non-expanding) DAG statistics.
It must stop before deleting or expanding any assumption multiplier.  Thus a
PASS marker means only that the diagnostic was captured; it is not an
`a1^104` certificate and cannot promote the M=104 or total exponent-628 route.

Run on AWS only, one core, at most 4 GiB virtual memory and ten minutes.  The
source bundle, wrapper, V43C3 producer, preregistration, and generated output
must be hashed.  Any V43C3 source mismatch, absent final labels, attempted
ordinary return from the intercepted rule, or missing terminal marker fails
closed.
