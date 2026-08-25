# Exact generic vertical length of the localized Q8 source

This AWS-only pure-Singular producer works over the coefficient field
`F_127(w)`.  It substitutes `x3=(v+2)x5` and enforces the selected localization
with `u*x5*v-1`, leaving seven equations in
`(u,c,d2,d4,x1,x5,v)`.

If the exact generic standard basis has dimension zero and vector-space length
190, then the already-forced H component (vertical degree 190) consumes the
entire localized generic fibre with pushforward multiplicity one.  That would
give the desired degree-one/no-extra-dominant-component bridge modulo 127.

Both dp and lp lanes are producer computations; no msolve result is used.
