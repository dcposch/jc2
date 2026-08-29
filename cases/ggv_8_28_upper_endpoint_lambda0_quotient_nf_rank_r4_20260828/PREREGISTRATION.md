# Preregistration: reducer-safe quotient rank certificates r4

Date: 2026-08-28

R2/R3 used direct Singular qring representatives for rank, zero, gcd, and
factor tests.  The adversarial q2=0 branches exposed the defect by returning
a rank-4 block whose reported common gcd was q2^2.  Therefore all quotient
outputs for P, C8P02, Q1P02, Q1P03, TRIPLE02, and TRIPLE03 are frozen as
`ADAPTER_FAILURE/NO_VERDICT`.

R4 recomputes these six strata from the original frozen 106 by 105 matrix in
an ambient polynomial ring.  It pins `BRANCH_SB=std(BRANCH_FACTOR)` and never
enters a qring.  Every original matrix entry is reduced by `BRANCH_SB`; every
arithmetic row/column update is immediately reduced; every residual entry is
reduced again; and every determinant used as a rank witness is reduced after
determinant computation.  Only nonzero rational constants may be inverted.

For each branch, the displayed defining factor must be nonzero as an ambient
polynomial, have normal form zero, and its `+1` mutation must have nonzero
normal form.  In particular q2 on q2=0 is an explicit adversarial fixture and
must disappear before support, rank, or later factor parsing.

Rank r is certified by both:

1. a complete exact support/Hall census proving every (r+1)-minor is
   structurally zero after normal-form reduction (with every formal slot
   recorded); and
2. at least one exact r-minor whose determinant normal form is nonzero.

All structurally matchable r-minors are preserved with both raw determinant
and normal form.  No gcd or factor result is used or produced.  A clean job
is a genuine exact coordinate-ring rank certificate but remains strict
`NO_VERDICT_QUOTIENT_NF_RANK_CERTIFICATE_ONLY`: endpoint pullback and deeper
Fitting strata are pending.

Six independent one-core AWS lanes use r6c and the five new r6i.4xlarge
workers; r6d remains idle/zero-swap for the reviewed root-aware pole engine.
Each lane has a 96-GiB address cap, 3,600-second stage cap, 7,200-second
process-group cap, exact source/Singular/EC2/tag checks, zero total swap, and
starttime/no-orphan custody.  Stop on every reducer, adversarial, support,
rank, resource, or custody disagreement.  No HENS namespace is touched.

The first execution is the `Q1P03` q2 adversarial pilot on r6g.  It must pass
the stdlib selfcheck, literal-q2 backend negative/mutation control, complete
ambient matrix build/reduction, structural upper-bound replay, and exact
nonzero-normal-form minor witness before any other lane is launched.  A
failure remains `ADAPTER_FAILURE/NO_VERDICT` and blocks fanout.  After a
clean pilot, the remaining five frozen mathematical payloads may fan out
unchanged on their registered idle hosts.

