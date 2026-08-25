# Registration

Date: 2026-08-25

Objective: count all smooth affine `F_(127^2)`-points of the pinned candidate
`H` exactly, independently on two AWS hosts, and compare with
`#P1(F_(127^2))`.

Acceptance gates:

1. candidate SHA is exactly
   `9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce`;
2. shard intervals are disjoint and cover `[0,16129)` exactly;
3. each shard is rc0 and internally reconciles per-fibre and total counts;
4. independent host aggregates agree on affine/smooth/singular counts;
5. at least one direct-enumeration fibre control agrees with the gcd method;
6. the smooth count is strictly greater than `16130`.

Accepted result: all gates pass, with smooth count `16168`.

Forbidden inference: no statement about quotient membership, component
grouping, good-reduction specialization, or rational trajectories follows
from this registration alone.
