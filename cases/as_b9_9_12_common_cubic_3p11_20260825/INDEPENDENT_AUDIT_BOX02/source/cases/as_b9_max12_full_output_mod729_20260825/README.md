# B9 complete fixed-D12 output digit modulo 729

`solve_full_output_mod729.py` source-pins the frozen B9 `Z/243` replay,
introduces both complete total-degree-12 output digits, solves all determinant
rows exactly over `F_3`, and directly replays any witness over the integers.

Run only on AWS.  Set `JC2_ROOT` to the frozen source closure and
`OUTPUT_JSON` to the desired result path.

## Producer endpoint

The source ran byte-identically on Box02 and Box03 under a 4 GiB address-space
cap.  Both runs returned `rc=0` in 0.08 seconds with less than 19 MiB RSS.
The complete `276 x 182` affine system has rank 108 and a 74-dimensional
solution fibre.  The reconstructed pair has actual total degrees `(11,12)`,
actual partial `y`-degrees `(9,12)`, and determinant one modulo 729 in every
row.  See `evidence/box02` and `evidence/box03`.

This producer endpoint awaits hostile source review.  It is one full fresh
digit over one displayed mod-243 point, not the complete earlier fibre.
