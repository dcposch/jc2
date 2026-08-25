# Whole-Q5 Q4 Cartier/Fitting V4: sparse-AST affinity certificate

Consume the exact V2 analyzer at SHA-256
`dd779edff09d5a7c17a1ac79f6b688879da4cf6993d8263a6f06b65755e864aa`
and the V3 source correction that exactly 63, not 76, assertions depend on
the 30 Q6/Q5 restoration digits.

Replace the whole-cube SMT affineness query, which exhausted a 16-GiB cap,
by a fail-closed sparse-AST certificate.  For each of the 63 exact row
expressions:

1. traverse the complete Z3 expression DAG;
2. prove no `UDiv` node contains a restoration digit;
3. prove no multiplication node has restoration-dependent input on both
   sides;
4. allow only addition, subtraction, negation, and remainder by a
   restoration-independent modulus on dependent paths;
5. derive the affine coefficient matrix by zero/unit substitution only after
   this structural proof.

The certificate is source-licensed because Q6/Q5 fourth digits are introduced
after all exact division gates and enter the determinant gate through linear
derivatives and the linear `S_HJ` cross term.  Bitvector residues are reduced
modulo 729 at the source operations, so wraparound cannot create a hidden
restoration product; the AST traversal nevertheless fails closed on any such
node.

Then retain the V3 independent-assertion custody and enumerate the 79
compatible structural bases times all `3^6` Frobenius controls for exact
matrix/rank strata.  Preserve every rank-drop stratum and make no zero-locus,
Q3/Q2/Q1, all-depth, counterexample, or JC2 inference.  All substantive
execution is AWS-only.
