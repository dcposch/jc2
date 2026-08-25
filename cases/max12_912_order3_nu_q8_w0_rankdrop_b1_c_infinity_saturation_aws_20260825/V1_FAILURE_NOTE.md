# V1 fail-closed source-preflight negative

Both initial `v1` endpoints generated a nine-variable ring with order-block
sizes summing to ten.  Singular rejected the ring, then continued with rc zero
and printed the final literal PASS marker despite undefined downstream ideals.
The outer runner did not accept the jobs because its diagnostic grep caught
`not defined`; these endpoints are software negative controls only.

V2 corrects the block sizes to `1+8` and `1+2+6` and expands the diagnostic
ban to include ring-count/undefined/expression errors.  No mathematical result
is taken from V1.
