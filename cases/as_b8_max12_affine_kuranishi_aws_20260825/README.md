# B8 complete affine W2/W3 family

This frozen producer classifies the complete first nonlinear fixed-D12 lift
gate for the B8 `(8,12)` residue seed.

## Exact outcome

- complete W2 operator: 276 rows, 172 variables, rank 104, affine kernel 68;
- first W3 compatibility: an 81-dimensional polynomial span with genuine
  quadratic rank 42;
- 39 pure-linear consequences reduce the system from 68 to 29 variables;
- the full reduced ideal is
  `(s22,s26+2*s22*s26,s22^2,s26^2+s19*s22,s22*s27)`;
- exact mutual reductions prove that ideal equals `(s22,s26)`;
- compatible predecessor scheme: `A^27_F3`;
- fresh-digit fibre: `A^68_F3`;
- total modulo-27 family: `A^95_F3`.

The report is
`xmodel/as-b8-max12-affine-w3-kuranishi-solved-aws-20260825.md`.

## Evidence layout

- `evidence/box02`, `evidence/box03`: dual-host analytic/interpolation
  compilers;
- `evidence/reduce_box02`, `evidence/reduce_box03`: dual-host exact linear
  elimination, substitution, routing controls, and ten literal replays;
- `evidence/verify_std_v2_box02`, `evidence/verify_slimgb_v2_box03`: accepted
  independent Singular ideal-equality checks;
- `evidence/verify_std_v1_box02`, `evidence/verify_slimgb_v1_box03`:
  quarantined negative controls only; see `VERIFY_V1_NEGATIVE_CONTROL.md`.

All substantive computation ran on AWS.  Every accepted literal witness
replayed all 276 integer determinant rows modulo 27 and audited actual
partial and total degrees.  The entire family has exact partial `y`-degrees
`(8,12)` and total-degree cap D12; only the ten emitted witnesses are claimed
to have actual total-degree pair `(8,12)`.

## Firewall

Finite depth only.  No all-depth, `Z_3`, characteristic-zero,
counterexample, selected-Q8/TD6, maximum-twelve, or JC2 inference.

