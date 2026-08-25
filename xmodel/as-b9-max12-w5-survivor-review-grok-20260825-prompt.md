Hostile-review the producer result
`xmodel/as-b9-max12-w5-survivor-aws-20260825.md` against its frozen package
`cases/as_b9_max12_w5_survivor_aws_20260825/` and the parent package
`cases/as_b9_max12_w3_survivor_aws_20260825/`.

Independently recompute, without trusting the producer implementation:

1. for `u=x+y^3`, the exact determinant of the displayed `P,Q` through
   modulo 243, including every integer mixed term;
2. the `Z/81` parent determinant
   `1+81(-u^4+2y-6u^2y+32y^2)` and its divided residual modulo three;
3. the linearized operator
   `D(R,S)=R_x-u^3 R_y+S_y` at the B9 special fibre and both claimed
   primitives
   `D(2uy,y^2)=u^4+y` and
   `D(xy^2,x^4y^2+xy^11)=y^2` over `F_3`;
4. source reduction, exact total and partial-`y` degrees `(9,12)`, full
   fixed-D12 support, and the parent-without-new-digit negative control;
5. manifests, freeze hashes, rc/status, dual-AWS custody, and byte-identical
   stdout;
6. exact scope: one branch through one finite modulus is not completeness of
   the D12 predecessor scheme, an inverse limit, `Z_3` point,
   characteristic-zero map/collision, counterexample, max-12 theorem, TD6
   result, or JC2 resolution.

Search specifically for a sign or factor error in the divided residual,
using the wrong derivative operator after the tame source transform,
characteristic-three Frobenius used over `Z`, degree overflow hidden by `u`,
or a claim that a selected branch represents the full affine family.

Return verdict `CONFIRMED`, `CONFIRMED WITH FIXES`, or `REJECTED`; separate
mathematical errors from custody, terminology, and exposition defects.  State
the strongest exact claim and sharpest non-claim.
