# V82QSS3 empty-map denominator erratum

V82QSS2 completed the exact q11/q16 source, FIRST, PREVIOUS/POLE, CURRENT,
direct-q-prime omission, pivot-schedule, original-row, and production-packing
computations identically on Box03 and r6d.  It then failed before the final
denominator and result assertions.  The reporter used `tri.CTX(1)` for the
common denominator of an empty obstruction map.  In python-flint 0.8.0,
`tri.CTX` is an `fmpq_mpoly_ctx` object and is not callable.

V82QSS3 changes only that reporting boundary to the typed unit `tri.ONE`.  It
also asserts before the expensive transport that `tri.ONE` equals
`tri.CTX.constant(1)` and has total degree zero.  This is a positive control for
the q11 omission map and all three q16 maps, which are expected to be empty.

The four V82QSS2 rc=1 streams remain immutable software-negative evidence.
Their identical exact map tables are not a theorem until V82QSS3 reaches all
post-map assertions and rc=0 independently on both hosts.  Scope remains the
fixed source-typed A3 square-zero generic section; there is no neighborhood,
family, TD6, SP-2, landing, or JC2 inference.
