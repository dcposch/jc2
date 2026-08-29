# V26R1B exact-prepass mutation-syntax erratum

Status: `PRE_ALGEBRA_FAILURE_PRESERVED_NO_VERDICT`.

The first rollback-tagged exact prepass was launched on Box02 at
`2026-08-27T16:15:57Z` under job directory
`max12_812_order2_u2_62_k00_v26r1_exact_prepass_20260827T162300Z_box02`.
It exited at `16:15:59Z`, before the `B+I5(A)` standard-basis computation,
because Singular does not define direct equality between two ideals.  The
negative control had used `I5M==I5A`.  Singular emitted
`` `ideal` == `ideal` failed ``; the runner failed closed with exit status 1.
Runtime was 2.20 seconds, maximum RSS 527,768 KiB, and swap usage zero.

The R1C repair changes only that control.  The frozen nonzero entry
`I5A[ipick]` is deleted, and the mutation now checks polynomial entries:
`I5M[ipick]!=0` must be false and `I5A[ipick]==I5M[ipick]` must be false.
The mathematical matrix, base ideal, minors, field, algorithms, resource
caps, rollback tag, and firewalls are unchanged.

The failed R1B run is infrastructure evidence only.  It supplies no rank,
stratum, jet, arc, closure, or JC2 conclusion.
