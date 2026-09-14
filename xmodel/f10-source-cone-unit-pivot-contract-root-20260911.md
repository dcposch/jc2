# Whole-B unit-pivot discovery contract for the r3 source identity

2026-09-11. MANUAL / UNREVIEWED algorithm and consumer contract, not an implementation, computation or source result. ROOT starts00:06UTC; original reserve00:19/HARD00:22, unchanged. Basis0d39df3c9fd69c939a8420c54d03228b9077777d. This task uses only the three pinned texts in section4, read fresh WHOLE; no live r3 code, schema, baseline or unreviewed boundary identity is a premise.

## 1. Accepted target and preserved full algebra

Import accepted cone17z and leading algebra17zzd at their exact scopes. At r3, B is the WHOLE finite-etale rank-seven rational algebra with a monic septic presentation Q[Z]/P. No irreducibility or factor selection is assumed. I_hom has all25 homogeneous slots F_j and g=H_q*ell of weight30 in X1..X4 of weights1..4, with all source forcing/guards carried by the accepted graph and faithful covers. Actual reconstructed coefficients are still missing.

Index the full weight30 monomial list by rows, and pairs(j,M) with wt(M)=30-wt(F_j) by columns. Let A's column(j,M) be the complete B-coefficient vector of M*F_j, and b the vector of g. This gives A:B^1453 -> B^297, with zero slots/columns retained. The accepted homogeneous projection proves that A*x=b is equivalent to exponent-one membership g in I_hom; it says nothing about whether a particular algorithm finds a solution.

A B-entry stores seven rational coordinates. The full B-matrix has431541 such entries if represented densely, equivalent to3020787 stored rational coordinates before overhead. Expanding every B-multiplication into its7by7 rational matrix yields2079by10171, or21145509 rational entries. These manual nominal counts explain the representation choice, NOT actual sparsity, allocated memory, coefficient heights or a7-fold runtime gain. Field-arithmetic cost, pivot inversion and fill-in may dominate; no measured speed is claimed.

## 2. Deliberately incomplete discovery algorithm

Use exact arithmetic over the WHOLE quotient Q[Z]/P. Unit testing/inversion uses polynomial Euclid: an entry a is invertible iff gcd(P,a)=1, and a prospective inverse must satisfy a*a_inverse=1 in ALL seven coordinates. A nonzero a with nontrivial gcd is not inverted and no factor is discarded.

The prospective deterministic discoverer keeps an augmented matrix[A|b], a column permutation and a pivot count k.

1. In the remaining rectangle with row/column indices>=k, search in a fixed documented order for an entry certified to be a unit. Skip zero and nonunit entries; preserve them in the matrix. Every attempted inversion has a checked full-product witness.
2. If a unit exists, swap its row with k and its column with k, recording the column permutation. Multiply pivot row and b_k by its inverse. For each row i>k subtract A_ik times the normalized pivot row, including b_i. This is an invertible elementary row operation; the column operation is only a permutation. Continue with k+1.
3. If no unit exists, or there are no remaining rows/columns, stop pivoting. Set all nonpivot unknowns to zero. If the remaining right-hand-side entries b_i,i>=k are all zero, solve the k unit-diagonal triangular equations backward and undo the column permutation. This gives a candidate x. If any remaining b_i is nonzero, return INCONCLUSIVE.
4. The discoverer itself then rechecks A_original*x=b_original in the original coordinates before emitting cofactors. Independent literal checking below is STILL required; no source outcome is assigned by discovery.

Proof of conditional success: elementary row operations over any commutative ring are invertible because the row multiplier is a proved unit; permutations are invertible. Prior pivot columns remain zero in later rows. After the free variables are set to zero, all unpivoted row equations are exactly0=b_i, even if the remaining matrix has nonzero NONUNIT entries. Their assumed zero b_i makes these rows true. Back substitution in the normalized triangular block solves each preceding row without any additional division. Undoing permutations gives a solution of the original matrix. No reducedness, equal component ranks or fieldness is used. The proof does not assert that failure to reach this form excludes a solution.

A zero target may legitimately produce zero cofactors; the literal identity, source authentication and guard semantics remain mandatory. A budget/parser/arithmetic refusal returns a separately typed NONDECISION, never a zero-ring or nonmembership verdict. No default rational expansion, prime, field factor, exponent, r-value or cap retry follows INCONCLUSIVE.

## 3. Independent witness checker and failure controls

For a proposed x, group coordinates by(j,M) to form all25 cofactor slots a_j. A separate checker reconstructs or charges an independently authenticated complete r3 coefficient baseline, verifies its exact source/interface/hash, and recomputes

    sum_(j=1)^25 a_j*F_j - g = 0

as a full polynomial over Q[Z]/P. Check ALL rational coordinates, polynomial supports and all25 row IDs, including zero cofactors/zero generators. This literal identity is the evidence; pivot history, discovery status or a characteristic-zero matrix header is not. The checker need not trust or replay the discoverer's elimination. It must not trust a target supplied only by the candidate: g and F_j come from the complete authenticated source/graph.

A verified identity then implies E3=0 by accepted cone17z. This is conditional on actual reconstruction/checker/custody evidence; no such evidence exists now. No REG, finite compatibility basis or field decomposition is required. Failure of this discovery algorithm is weaker than complete exponent-one nonmembership, which itself is weaker than nonzero localization.

Changed-base obstruction control: in B'=Q×Q let e=(1,0), f=(0,1), and

    A'=[[e,f],[f,e]], b'=(1_B',0_B').

Every matrix entry is a nonunit, so the proposed unit-pivot method stops immediately with a nonzero right side and returns INCONCLUSIVE. Nevertheless (A')^2=I, and x'=(e,f) solves A'x'=b'. Thus the refusal branch MUST NOT say inconsistent/nonmember. This is an abstract algorithm control over a changed finite-etale base, not an actual source or leading component. If matching rank7 is useful, take B'=Q^7 with e one coordinate idempotent and f=1-e; the same identities hold.

Changed-entry controls: replacing a checked inverse by its inverse+1 changes a*a_inverse by the nonzero unit a, so a whole-product rejection is guaranteed. For a nonzero actual generator F_j, adding an allowed monomial M with coefficient1_B to its cofactor changes the literal sum by M*F_j, nonzero even when F_j has zero-divisor coefficients. Polynomial monomial shifting is injective over any B. Choose and freeze a demonstrably nonzero row before the run; if all F_j vanish, a separately specified nonzero changed-target control is needed. No zero-to-zero mutation counts, and no current fixture or rejection is claimed.

## 4. Scope, next gate and custody

Classification: KNOWN linear-algebra mechanism, NEW bounded r3 discovery contract/representation choice. This is not a new theorem about JC2. The bounded canonical checksum found old unit-pivot eliminations, homogeneous Macaulay certificates and changed-base warnings on other clients. Those establish no outcome for this matrix and do not authorize a retry of closed r1/r2, K16 or Moh source jobs. No load-bearing literature claim was introduced.

The exact unit-pivot algorithm is deliberately incomplete over a disconnected leading algebra. Its attraction is avoiding the sevenfold coordinate redundancy of explicit rational multiplication matrices without requiring a factorization. Feasibility and comparative cost remain UNKNOWN. It is one possible first positive-witness search, not an obligatory replacement of a complete exact solver. Rejecting a nonunit pivot is safe only with the stated INCONCLUSIVE semantics.

Cheapest next validation: one different-model manual FIRST of sections1–3, estimated8–12minutes, before this contract is used as a mathematical premise for a solver implementation. Intended questions: exact whole-B module map and slot inventory; invertible operations and back-substitution proof; changed-base false-negative control; independent full-identity acceptance and actual-source authentication; no fieldness, factor loss, runtime claim or negative-source verdict. This is an actual planned consumer gate, not optional re-hardening of an already accepted source theorem. The separate LIVE r3 reconstruction is independent of this contract and is NOT a descendant or input.

If accepted, a later independently gated source-bound implementation may attempt this one search only AFTER actual reconstruction and runtime readiness. No code, new schema, callback to live code, coefficient payload, solver launch or worker is supplied now. Its eventual interface must bind exact source baseline hashes and reconstruct every F_j and g; a convenient selected row/field target is forbidden. A successful candidate still waits for independent literal verification and separate result/source composition. A stall is banked once; no automatic Q-matrix/prime/N/r/RAM/cap escalation.

Exactly three scientific texts were hash-checked before fresh WHOLE reads in this task:

- xmodel/ideation-20260910T2300Z-astra-source.md — bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986.
- xmodel/ideation-20260910T2300Z-cross-fable5.md — 7dae0ba7c0c03418676d55a93b7deebcd01805b212ab13e284ce59b3bebf691a.
- xmodel/f10-middle-univariate-unit-astra-20260910.md — 890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5.

Read scope is complete through EOF/Seal, no clipping/reuse. Historical producer headers are superseded only at the accepted cone/leading scopes stated above. The first gate's claim that reconstruction is the entire cost is explicitly NOT imported. ROOT's unrelated readiness and early-band symmetry search are not mathematical premises of this report. Canonical checksum/readiness observations and operational adapter texts are documentary only, not fourth scientific inputs.

No new canonical OPEN ID. Quantity: whether one source-authenticated whole-B unit-pivot search yields a literal exponent-one certificate at r3. The cheapest present test is the manual FIRST above; actual search cost/data availability remains unknown. Raised issue is explicitly not promised to be resolvable within that proof-review budget. All authored bytes are separate bounded apply_patch writes; existing documentary transaction only. ZERO mathematical subprocess/import/AST/syntax/compile/test/CAS ANYsize, coefficient/candidate/fixture BODY or generation, code implementation, network, AWS, protected-project/infrastructure access, shared science edit or live report consumption.

Full own WHOLE, exact three postpins and documentary collision check precede markerLAST, close/finalize/expected VERIFY. Original00:19/00:22 publication clocks unchanged. JC2 remains unresolved.

## COLLISIONS

status: EMPTY

- NONE — the documentary tool found no explicitly raised canonical OPEN entries. The manual method/target-history qualifications above still govern.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11232`.
- Body SHA-256:
  `fe98149fe9e03917365bfcb1ea04c07c7a184ebaf0b9edbfa2c37111d5808af3`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
