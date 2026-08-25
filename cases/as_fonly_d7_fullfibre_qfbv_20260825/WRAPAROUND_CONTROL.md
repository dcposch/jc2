# Rejected narrow-width control

A 5-bit multiplication is unsound: the legal residues `26*26=676` wrap to
`4`, and then `URem 27` gives `4` instead of the correct `1`.  The producer
therefore uses 32-bit gates, reduces after every product/sum, and asserts the
global gate bound `728^2 < 2^20` before constructing the solver.

