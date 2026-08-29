# V82QSS typed-constructor erratum

The first dual-host V82QSS run reached exact transport, FIRST, PREVIOUS/POLE,
and the `F3_CONSTANT_AFFINE` dump, then failed before its q11/q16 symbol tests.
The wrapper attempted `E3(U**6)` where `U**6` is a bare FLINT
`fmpq_mpoly`.  The source field constructor accepts a `Rat3` rational-function
wrapper (or an existing `E3`/`EField`), so both hosts raised the same `TypeError`.

V82QSS2 changes only that typed boundary to `E3(Rat3(U**6))` and changes the
producer label.  The old four rc=1 streams are software/deployment negatives;
they carry no q11 or q16 CURRENT-symbol verdict.  Every mathematical assertion,
source parent, omission control, row order, and fail-closed scope remains
unchanged.
