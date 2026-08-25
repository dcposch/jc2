# Whole-Q5 Q4 Cartier/Fitting V5: full-state symbolic checkpoint

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

V4 correctly passed this affinity certificate but then failed closed: the
`63 x 30` coefficient matrix is not a function only of the seven structural
and six Frobenius controls.  Its exact coefficients also depend on Q9, Q8, Q7,
and selected C5/D5 predecessor coordinates.  Preserve V4 as a negative control.

V5 must retain that complete dependency state, emit the exact symbolic matrix,
right column, Q4 Cartier scalar, independent assertions, dependency-incidence
table, and sparse-AST certificate.  It must not enumerate a false `79*3^6`
base or report rank strata before the full predecessor scheme is imposed.
This is a source checkpoint for a later componentwise Fitting/projection gate,
not a zero-locus, Q3/Q2/Q1, all-depth, counterexample, or JC2 inference.  All
substantive execution is AWS-only.
