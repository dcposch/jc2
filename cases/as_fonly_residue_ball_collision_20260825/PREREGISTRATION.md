# AS residue-ball collision theorem: preregistration

Date: 2026-08-25

This case checks only the finite-ring positive controls for the following
mathematical lemma.

Let `R_n=Z/3^n Z`, and let `F=(P,Q)` be a polynomial map over `R_n` whose
Jacobian determinant is the constant one.  If the reduction of `F` is
`(x-x^3,y)`, then the three source residue balls over `(0,0)`, `(1,0)`, and
`(2,0)` map bijectively to the same target residue ball.  In particular, `F`
has moving collisions whose x-coordinates differ by units.

The deterministic replay must:

1. expand the displayed integral cap-seven triangular control exactly;
2. check its full determinant coefficient support modulo `9` and `27`;
3. recover the target-zero preimage in each of the three residue balls by the
   one-digit-at-a-time finite Hensel induction, with uniqueness at every
   digit;
4. check all three image equalities and pairwise unit separation directly;
5. check the explicit representatives `(0,0)` and `(7,0)`, with `u=5`
   modulo `9` and `u=23` modulo `27`;
6. include a non-unit-Jacobian control for which residue-ball surjectivity
   fails.

The replay is a positive control and a theorem regression.  It is not a
search, an all-depth lift, a fixed-support existence proof, or a Jacobian
conjecture counterexample.

Under the campaign compute policy, execute the replay on AWS only.  Local
work is limited to source editing, hashing, and custody.
