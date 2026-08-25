# Q9-rank-class Q8 sample discriminator

Partition the 2,187 structural bases into 27 disjoint deterministic ranges.
Within each range, scan accepted corrected-Q10 predecessor states in the
frozen order and retain at most four representatives of each exact Q9
rank pair `(13,13)`, `(13,14)`, `(15,15)`, `(16,16)`, `(16,17)`, and
`(17,18)`.

For each compatible Q9 class, reconstruct its canonical Q9 witness and test
the 22-row Q8 transition.  Emit canonical RREF/matrix hashes, Q8 rank pairs,
the first left-null obstruction if incompatible, or a substituted witness if
compatible.  The aggregate must cover all six Q9 rank pairs and all three
compatible ranks.  This is deterministic sampling, not a census of Q8 over
all Q9 states or fibres.
