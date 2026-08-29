# ACT-TOT-G20 V44R2 validation-only repair

Date: 2026-08-27

The frozen V44R1 producer completed independently on `r6a` over exact Q and
on `r6b` over `F_65521`.  Both runs emitted the compiler PASS banner after
constructing all seven unspecialized general-`rho` rows through grade 20 and
passing the 140 prefix, fourteen face-bridge, 569-tail, homogeneity, parity,
source-depth, and receiver-free gates.  Their post-compiler validator then
failed before inspecting the large rows because its recursive parser kept
Python's default recursion limit.

V44R2 is an additive validation-only repair.  It pins the two immutable
V44R1 compiler results, all fourteen serialized rows, and both successful
compiler resource transcripts.  It raises only the parser recursion limit,
reruns full row custody/homogeneity/parity checks on registered AWS hosts,
recomputes every exact-Q canonical polynomial hash, and checks the second-host
rows coefficientwise modulo 65521.  It does not rerun or alter either
compiler output.

A pass promotes the V44R1 compiler outputs only as the minimal
`ACT-TOT-G20` custody lemma.  It proves no contact identity, finite-jet
factorization, endpoint, coverage, ramified-fibre result, `G2` obligation,
Gate T, order two, maximum twelve, JC2, or counterexample verdict.

