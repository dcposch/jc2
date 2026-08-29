# Preregistration: P/C8P02 quotient rank descent r6

Date: 2026-08-28

R5 gave complete exact quotient-normal-form rank certificates on four of six
branches.  On `P` and `C8P02`, the exact 11 by 10 residual support graph has
matching number 10, but the normal forms of both structurally matchable
10-minors are zero.  R5 stopped without descending, so those two branches
remain `NO_VERDICT`.

R6 changes no mathematical input and reuses the r5 normal-form matrix
reducer byte-for-byte.  It independently reconstructs each residual from the
original frozen 106 by 105 receiver matrix, using the same pinned
`BRANCH_SB=std(I)` and explicit normal form after every matrix entry/update.
It then performs the narrow missing descent:

1. enumerate all 11 formal 10-minor slots, preserving their signed row/column
   positions; nine must be structural zeros and the two matchable minors are
   preserved with raw determinant and normal form;
2. require the normal form of each matchable 10-minor to be exactly zero;
3. enumerate all 550 formal 9-minor slots, preserving the 378 structural
   zeros and all 172 matchable signed minors with raw determinant and normal
   form; and
4. require at least one explicit 9-minor with nonzero normal form.

Thus a clean branch certifies residual rank exactly 9: every size-10 minor
has zero normal form, while a size-9 witness has nonzero normal form.  With
the 95 exact rational-unit pivots independently replayed, the total receiver
rank is 104.  No gcd/factor parsing, cancellation, saturation, radical,
rank-locus decomposition, endpoint pullback, or endpoint verdict occurs.
Success is strictly `NO_VERDICT_QUOTIENT_NF_RANK_CERTIFICATE_ONLY`.

`P` and `C8P02` run as independent one-core AWS lanes on r6c and r6e.  Each
uses an identical tiny q2 negative/mutation control, exact EC2/resource-tag/
source/backend checks, 96-GiB address cap, 3,300-second algebra-stage cap,
7,200-second process-group cap, zero total swap, and starttime/no-orphan
custody.  Any disagreement quarantines only that branch.  r6d remains idle
for the reviewed root-aware pole census.

