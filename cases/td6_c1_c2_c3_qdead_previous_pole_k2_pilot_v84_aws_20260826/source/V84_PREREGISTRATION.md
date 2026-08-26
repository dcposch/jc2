# V84 preregistration — TD6 previous/pole quadratic Kuranishi shards

Stage-A input is the exact 24-dimensional kernel

```text
Q_prev = span(q2..q14,q16..q24,d10,d15).
```

The target is the complete quadratic coefficient map from
`Sym^2(Q_prev)` to every source-replayed previous/pole dependent coordinate,
on the intersection with V83's explicit generic FIRST principal open.  The
24 axes are split into six ordered four-axis blocks; the 21 unordered block
pairs partition all 300 symmetric monomials exactly once.

Each shard must rebuild the original 3,470-row transport, retain correct
first and second dead-stretch matrix variation, solve FIRST through quadratic
order, replay every FIRST and previous/pole source combination, and emit an
exact canonical table and complete denominator factorization.  Diagonal
entries are Taylor coefficients, not classical second derivatives.

Controls: Amazon-EC2/Linux and registered-tag refusal; complete recursive
source hash; symbolic centers; exact licensed axes and q15 exclusion; mixed
and diagonal quadratic multiplication; second-order inverse; pair-swap
symmetry; dead second-matrix sentinel; source omission inherited from the
first lifts; linear Stage-A specialization; original-row replay; canonical
serialization.

The bounded checkpoint wave launches only block `(0,0)` on independent r6d
and Box03 hosts under 8-GiB/6-hour caps.  It is a correctness/cost pilot, not
the 21-block union and not a K2 theorem.  No current-row, nonlinear family,
full TD6, SP-2, or JC2 conclusion is licensed.

