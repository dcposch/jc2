# TD6 V89K1 V1 deployment erratum

Date: 2026-08-26

Both V1 wrappers stopped before emitting any result because the diagnostic
incorrectly asserted that substituting
`C=(V^2-U^3)/U` required the same clearing power of `U` for `K` (degree one
in `C`) and `B3` (degree two in `C`).  The load-bearing identity
`B3-K-2FG=0` had already passed, but no V1 output is consumed as evidence.

V2 separately records clearing powers one and two, checks the cleared forms
`U*V^4` and `U^2*V^4`, and states the common un-cleared specialization
`K=B3=V^4`.  It uses a new source archive, roots, and tags.
