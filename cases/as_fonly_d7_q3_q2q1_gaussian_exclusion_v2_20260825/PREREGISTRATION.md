# Exact Gaussian exclusion V2: redundant obstruction support

Consume V1 certificate source SHA
`9a34970455d0844b4a4894dca34389fd2cc43704466d9ddf13e3c09d88cddcda`.
V1 correctly computed the branch systems and left-null witnesses but stopped
because it preregistered a one-row omission control; direct search found no
single row deletion consistent.  This is a negative control showing redundant
obstruction support, not a defect in the rank/augmented-rank result.

V2 retains the exact sparse left-null certificate on every branch.  For the
positive control, greedily remove certificate-supported rows until consistent,
then re-add every dispensable row to obtain an inclusion-minimal (not asserted
minimum-cardinality) omitted set.  Reconstruct raw digits and literally verify
all `/27` rows and every retained `/81` row; at least one omitted `/81` row must
remain nonzero.  Store full matrices/RHS for an independent verifier.

Strict scope remains one complete displayed Q3 affine fibre at fixed D7 and
finite precision; no whole-Q5, all-depth, counterexample, or JC2 inference.
