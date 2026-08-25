Hostile-review the narrow producer result in
`xmodel/as-b9-max12-w3-survivor-aws-20260825.md` against the frozen package
`cases/as_b9_max12_w3_survivor_aws_20260825/`.

Independently recompute and audit:

1. the exact integer expansion for `u=x+y^3`,
   `P=u-u^3+18uy`, and
   `Q=y+u^4+3u^2y+18y^2`;
2. the claimed determinant
   `1-81u^4+54y-162u^2y+648y^2`, coefficientwise in `Z[x,y]`, and its
   reduction to one modulo 27;
3. the intermediate modulo-nine identity, actual partial-`y` and total
   degrees `(9,12)`, unit leading faces, source reduction, and explicit
   collision;
4. both omission controls, source/manifest/freeze hashes, two AWS rc/status
   records, and byte-identical replay output;
5. terminology and scope: `G9=A∘B9` is a tame right-composition/source
   transform, not a group conjugate; one point modulo 27 is not an all-depth
   lift, characteristic-zero map, counterexample, max-12 theorem, TD6 result,
   or JC2 resolution.

Search actively for a missing determinant term, illicit characteristic-three
Frobenius simplification over the integers, support/degree overflow, false
collision claim, or stronger inference than the evidence licenses.

Return a concise report with verdict `CONFIRMED`, `CONFIRMED WITH FIXES`, or
`REJECTED`.  Separate mathematical defects from terminology, custody, and
exposition defects.  State the strongest exact claim and sharpest non-claim.
