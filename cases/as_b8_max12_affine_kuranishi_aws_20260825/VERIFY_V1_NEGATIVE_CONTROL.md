# V1 verifier negative control

The first `std`/`slimgb` verifier sources had a fail-closed defect: Singular
retains the generator count of an ideal whose reduced generators are all
zero, so the aggregate comparison `reduce(I,H)!=0` printed `FAIL` even when
every generator reduced to zero.  The scripts then continued because
`exit(91)` is not a Singular command, and the shell runner only required the
later PASS sentinel.  Both V1 AWS endpoints are therefore diagnostic only
and must not be cited as verification.

V2 tests every generator polynomial separately, emits PASS only in the
successful branch, and makes the runner reject any line beginning `FAIL`.
The V1 remote bytes remain immutable under their original tags.

