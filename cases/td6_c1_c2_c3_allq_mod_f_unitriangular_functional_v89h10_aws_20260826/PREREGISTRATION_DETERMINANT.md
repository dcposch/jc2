# TD6 V89H10D exact all-q SCC determinant gate

Date: 2026-08-26

Status: producer gate; no result claimed before dual AWS replay.

Rebuild the exact V89H10G relative FIRST pivot matrix with all 22 licensed
independent q variables after exactly `F=0` on `D(U)`.  Require the frozen
V89H10G graph and N digests, then isolate its unique cyclic component
`(0,...,13)`.

First emit the exact trace of `N=B-I`.  A nonzero trace is a rigorous negative
certificate for the finite-Neumann/nilpotence route, but not for
unimodularity.

Then compute the 14-by-14 SCC determinant by exact division-free subset DP
over the full untruncated polynomial ring.  Emit per-row state, term, and
q-degree telemetry.  Accept unimodularity only if the final determinant is
literally one; otherwise emit the complete nonunit polynomial and stop.  No
unregistered factor may be inverted.

This gate does not construct the adjugate, divide P12, extend the q14
functional, prove a unit ideal/source exclusion, totalize q15, supply a
total-Rees chart, close whole TD6, or resolve JC2.
