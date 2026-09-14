# Manual whole-source review

This is the producer's static review, not independent approval or execution.
The sole changed production module is solver.py. Its new nested arithmetic
uses only the frozen exact Q-polynomial helpers and monic T division. No
coefficient of a general finite product algebra is inverted without an exact
rational-polynomial gcd identity. No element of the possibly nonreduced
T-remainder algebra is inverted.

Input boundary: the internal generic API requires a dense monic squarefree
rank-seven Fraction modulus, nine polynomials and guard of T degree at most
five, and all seven rational coefficient coordinates. The actual parser
first requires the literal frozen nonmonic source modulus, exact nine IDs,
envelopes and all dense slots; only then normalizes its rational leading
coefficient for the internal API. The unchanged checker independently binds
the full modulus and reconstructs q=r*h0. Generic inputs cannot replace a
genuine source in main().

Partition: every node projects and rescans all nine generators. Maximal
T degree and first index select the pivot. Only its leading coefficient is
tested; a nonunit splits the current squarefree modulus into both coprime
children. It is not assumed that the whole generator vanishes on a child.
The explicit limits are six splits/thirteen visits; leaf degrees sum to
seven and their product is checked against the original p.

Exceptional leaves: all-zero generators with nonzero q^5 give a rational
coordinate-functional separator pulled through the projection of the entire
old coefficient basis. All-zero target leaves retain zero multipliers. A
unit constant pivot is solved by its certified inverse. These branches need
no RREF. Nonzero q cannot have q^5=0 in a squarefree coefficient algebra,
but the implementation inspects q^5 directly rather than inventing a root.

Positive-degree leaves: all eight other generators, including zeros and
duplicates, enter their complete local A[T]_<d multiplication maps. One
direct sum uses the complete C basis, and the appended identity records all
row operations. In the separator branch, mu therefore exists on the whole
C, not merely the span of multiplier images. Pullback evaluates mu*rho on
every old T^k v^l coordinate, k=0..30,l=0..6; the unchanged checker later
tests every original multiplier column and target normalization.

The UNIT branch reads all local multipliers of degree below d, checks exact
monic divisibility of N, then uses (N/fhat)/lc(raw) for the raw pivot. Its
degree is at most 25-d. CRT idempotents are checked on every leaf, all nine
raw multipliers are recombined without raising T degree, and all 1638
coordinates are emitted with degree-25 zero padding. No factor is discarded.

The complete main() tail is text-identical to the old source. authorize
precedes arithmetic imports and allocations on the production entrypoint.
The internal function itself has the documented separately authorized-child
precondition; it is not a second CLI or a local-test authorization. There
is one .rref() call site and no full search-matrix constructor. Certificate
status remains CANDIDATE-ONLY. The bounded trace is diagnostic metadata,
not trusted by the unchanged checker. Future unsupported FLINT output or
failed internal identities fail closed; there is no fallback algorithm.

No assertion here reports a compiled, imported, syntactically tested or
executed program. No new harness or actual fixture has been authored.
