# V1 fail-closed deployment record

The first AWS launch at
`/home/ubuntu/jobs/as_q5_q4_cartier_fitting_20260825T114757Z` on Box02
terminated with return code 1 before matrix extraction.  The exact frozen V1
analyzer SHA-256 was
`d4dc9bac3d6ca4cd2ae49c872b4ce9654716bf07604eb909c8bf7320f17a7685`.
Its outer source wrapper exposed the compiler state through nested `scope`
dictionaries, so the direct lookup of `solver` failed with `KeyError`.

The V1 remote source and stdout/stderr remain immutable in that job.  V2 only
unwraps nested dictionaries until it reaches the source-pinned compiler
scope, records the number of unwraps, and otherwise retains the preregistered
gate.  V1 is deployment-negative evidence and no mathematical evidence.
