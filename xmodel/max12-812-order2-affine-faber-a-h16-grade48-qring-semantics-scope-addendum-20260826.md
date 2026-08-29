# H16 grade-48 direct unit: qring semantics scope addendum

Date: 2026-08-26

The Singular 4.3.2 quotient-ring comparison issue does not affect the charged
H16 direct-unit theorem or its live hostile review.  V4 and V6 use a custom
exact-`Q` sparse polynomial/series engine with canonical coefficient-dictionary
collection and no Singular quotient ring.  V5 uses an ordinary Singular
polynomial ring.  The only H16 artifact using `qring (s^49)` is the earlier
`odd_series_qring_v3` navigation/timeout control; it supplied no verdict and
is neither cited by the theorem nor charged in the review.

Accordingly, that qring artifact remains quarantined as navigation-only unless
all comparisons are explicitly reduced modulo `(s^49)`.  No scope or formula
change to the V4/V6 identity follows.
