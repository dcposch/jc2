Hostile-review the producer result
`xmodel/as-b8-max12-w3-survivor-aws-20260825.md` against the frozen package
`cases/as_b8_max12_w3_gate_aws_20260825/` and terminology erratum
`xmodel/ideation-20260825T1550Z-cube-terminology-erratum.md`.

Independently recompute and audit:

1. the exact integral source map `B8`, target orientation `T8`, residue map
   `G8`, its determinant/fibre collision, and right-composition rather than
   group-conjugation terminology;
2. completeness of the coordinate envelope
   `R: total<=12,y<=8` (81 slots),
   `S: total<=12,y<=12` (91 slots), with all 276 determinant positions;
3. the transported operator
   `D8(R,S)=-y^3 R_x+R_y-(1+2uy^3)S_x+2uS_y` over `F_3`, including
   equality with every direct-Jacobian basis column and rank/nullity 104/68;
4. the W2 correction and exact divided residual, its negative reduction
   `u^4`, the W3 correction, and literal integer determinant modulo 27;
5. actual total and partial-`y` degree pair `(8,12)`, source reduction,
   special-fibre collision, parent-without-W3 negative control, and the
   preserved V1 degree-overflow failure;
6. source/manifest/freeze hashes, dual-AWS rc/resource records, identical
   stdout and payload;
7. scope: one finite point in the fixed envelope, not the whole kernel,
   `Z/81`, all depth, `Z_3`, characteristic zero, nonautomorphy,
   counterexample, selected Q8/TD6, max-12 theorem, or JC2.

Search specifically for a sign error caused by the target orientation,
incorrect derivative after `u=x+y^4`, omitted determinant rows, a false
81-slot count, degree overflow hidden in `u`, characteristic-three Frobenius
used over `Z`, or an invalid inference from one deterministic representative.

Return `CONFIRMED`, `CONFIRMED WITH FIXES`, or `REJECTED`; separate
mathematical defects from terminology, custody, and exposition.  State the
strongest exact claim and sharpest non-claim.
