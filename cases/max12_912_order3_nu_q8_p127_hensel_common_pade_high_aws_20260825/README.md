# Higher-order simultaneous Padé for the selected-Q8 moving-v lift

This successor imports the frozen parser and exact linear solver from
`max12_912_order3_nu_q8_p127_hensel_common_pade_aws_20260825` without
modifying that package.  It compares any independently computed lower and
upper moving-v Hensel orders, then searches scalar common-denominator pairs
in increasing total degree up to the full bounds permitted by the available
upper truncation.  It stops at the first total degree carrying a unique
full-rank denominator; if none exists, the complete rectangle has been
exhausted.  Rank-deficient affine fits are not promoted to reconstructions.

The search is hierarchical: seven separate 190-sequence coordinate groups;
the normal triple `(c,d2,d4)`; the invariant triple `(x1,x3,x5)`; the six
true-centre coordinates; and finally all seven coordinates including the
localizer inverse.  If every per-coordinate group has a unique candidate,
their exact polynomial LCM is also constructed and revalidated.  A common
denominator that appears only at the upper order remains an unvalidated
candidate, not an accepted reconstruction.

The first intended run uses order 32 as the lower prefix and order 64 as the
upper series.  A recurrence, if found, is provisional: it must survive an
independent order-128-or-higher holdout and the reconstructed coordinate
functions must reduce every original quotient row to zero modulo `H(w,v)`.
No local substantive computation is licensed; the runner is AWS-only.
