# AS F-only D7: three pointwise chronological Q4 lifts

Status: **PRODUCER-EXACT / PROVISIONAL PENDING DIFFERENT-MODEL REVIEW**.

## Result

Three exact Boolector models of the complete displayed 197-row Q5 formula
were first replayed through the source-pinned nested-integer parent.  At each
model, the complete chronological Q4 system has 68 equations in the twelve
coefficients of homogeneous `(H5,J5)`:

- five degree-four divergence rows;
- all sixty-three recomputed terminal rows in degrees 7 through 12.

Exact F3 elimination and literal-integer replay give:

| structural base | rank | augmented rank | kernel dim | particular `(H5 | J5)` | result JSON |
|---|---:|---:|---:|---|---|
| 0000 | 4 | 4 | 8 | `011000 | 000000` | `2641dc2946aa...` |
| 0270 | 8 | 8 | 4 | `022000 | 210000` | `c801d191e472...` |
| 0513 | 8 | 8 | 4 | `001001 | 120120` | `96dcf7fa7b9d...` |

For every particular, the reconstructed integer map passes all five Q4 rows
modulo 243 and all 63 terminal rows modulo 729, after the parent replay has
checked the 197 predecessor rows.  The displayed affine fibres therefore
contain respectively `3^8`, `3^4`, and `3^4` chronological Q4 lifts.

## Controls and interpretation

The earlier J-only divergence section is a correct five-row Q4 control, but
it violates two terminal rows at base0270 and four at base0513.  This is the
load-bearing omission control showing why five-row restoration alone is
insufficient.  At base0000 that particular happens to satisfy the terminal
rows too, so it is not used as the negative control.

This is pointwise evidence at three exact Q5 models, not coverage of their
full Q5 fibres.  It licenses a source-complete Q3 successor only when the
whole H5/J5 affine kernel is retained.  It does not restore Q3 through Q0,
produce a complete finite-depth map, prove an all-depth lift, or imply a
counterexample/JC2 result.

## Custody

- case: `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/`
- producer SHA: `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4`
- source manifest SHA: `e8f7e1c0921d83415379f59307087edda9e3c9c9edf5103fec09411ab3de9a50`
- source freeze SHA: `c4413e46ee76e8ebe6c023ddca419a6b7106f64ee67ff159f87446fdb4886ceb`
- AWS host/tag: Box02,
  `/home/ubuntu/jobs/as_q5_sat_q4_full68_20260825T120159Z`

