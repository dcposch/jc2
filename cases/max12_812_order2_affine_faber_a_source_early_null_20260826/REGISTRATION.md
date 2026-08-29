# Affine-Faber `A` face: source early-null and repeated-root replay

Date: 2026-08-26

This is a dual-AWS, complete-frozen-tail replay for the delayed-load source
ray.  It emits the unloaded coefficients through `t^9`, checks the
correction-complete repeated-root coefficient at `t^7`, and checks two
exact normalized cubic identities.  In particular it distinguishes the
monomial-slice obstruction from the cancellation supplied by a general
next square-normal coefficient.

Exact Q is the producer and characteristic 65521 is a software control.  The
client does not assert a total-Rees chart map, terminal/Taylor compatibility,
order two, or a JC2 verdict.  It never runs on the local workstation.
