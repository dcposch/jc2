# Individual-coefficient Hermite reconstruction shards

Seven AWS shards independently treat `c,d2,d4,x1,x3,x5,inv`.  Within one
coordinate, each of its 190 moving-v coefficients gets its own minimal unique
Hermite-Padé denominator from the 123 exact fibres plus a Hensel jet.  The
shard then forms the exact polynomial LCM of those 190 denominators.

This is deliberately distinct from the simultaneous common-denominator
search: it can expose a rational coordinate whose LCM degree exceeds the
available simultaneous reconstruction window.  A coefficient candidate from
the lower jet must survive the independent upper jet; candidates first seen
at the upper jet are provisional.  No LCM or scalar fit is accepted as a
coordinate graph until a later jet validates it and all reconstructed
coordinates pass exact substitution in every original row modulo `H(w,v)`.

All substantive execution is AWS-only.

