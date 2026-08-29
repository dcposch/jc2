# Hostile review charge: TD6 V89H10T all-q simultaneous triangular flag

Date: 2026-08-26

Independently audit the frozen producer package

```text
cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/
```

with controlling hashes

```text
FLAG_RESULT.md              612b57bcfc20228152d37e5acef08ea41539481be99dff5878af8a790e4c6d1f
FLAG_EVIDENCE.sha256        69ebde85ff4ea117f887d9f56d9ef53da3a3676b0b4726bb653efa3bb6be022c
FLAG_FREEZE.sha256          a156f8394a2966effb006cdfdbb7e64a7da5cefa6e586022a67d29776167d2d9
SOURCE_FLAG.sha256          67a94374f3ca2585713480477f7aa93caf82c1a79192ecd3d33773c9bc2cdcde
source_flag.tar.gz          6fb15850c4e6c4b92039c584c30700295602f2a1c65f048724789cda8a19cb9c
client                      9c7a5eeede117568aa76d4c26bae11f6e78640313cad6ad559b414ee2cf5098c
GRAPH_RESULT.md             d07b2258d83cb0dfe48193abcf773ccc8a2d943001873858ae0cad58cd5292f0
GRAPH_FREEZE.sha256         39973cb2bd9a215b5dda1d1c32837855aaa08f4c4edaf3bb75aea811fdd09cd4
```

Charge every load-bearing point:

1. Verify all frozen hashes, both AWS rc files, byte agreement of stdout and
   all six mathematical artifacts, and source/archive custody.
2. Confirm the client rebuilds all 38 literal FIRST rows with exactly the 22
   licensed independent variables `q2,...,q14,q16,...,q24`, imposes only the
   stated exact `F=0` specialization, and never truncates q degree or assigns
   a numeric q value.
3. Audit the construction and orientation of `A(0)`, `A(q)`,
   `B=A(0)^(-1)A(q)`, and `N=B-I`, including the frozen N digest and the claim
   that N is affine-linear in q.  Look for a row/column or left/right module
   reversal that would invalidate the basis conjugations.
4. Audit the recursive common-invariant-flag algorithm, especially its use
   of a completed basis at each step, the lower-right quotient action, the
   common-kernel nullspace, independence of lifted vectors, and the assertion
   that previously built subspaces remain invariant.  Seek an exact smallest
   counterexample to the claimed 14-step flag rather than trusting telemetry.
5. Verify the emitted 14-by-14 `S` and `S_inverse` are exact two-sided
   inverses and conjugate each of the thirteen low-q coefficient matrices to
   strict upper form.  Confirm all SCC entries really involve only q2..q14.
6. Verify extension by identity to 38 coordinates, the emitted topological
   permutation, and direct entrywise strict-upper check for the full all-q
   N.  Confirm this proves `N^38=0` and the finite two-sided Neumann inverse
   of `I+N` over the stated q-polynomial coefficient ring.
7. Hostile-audit the denominator ledger.  Confirm all entries of S and its
   inverse use only the registered factors `U`, `V`, and `V^2-4U^3`, and
   that no determinant, pivot, or hidden simplification inverts another
   factor.  Keep the theorem restricted to the frozen specialized
   `D(U*H*B3)` context.
8. Confirm the proof does not depend on Singular qring `==0`, `subst`, or
   `diff` semantics without explicit reduction.  The producer says it uses
   Python/custom exact polynomial-field arithmetic only.
9. Enforce scope: the package skips P12 compilation/division.  It does not
   extend the H7/H8 functional to arbitrary low q, prove a unit ideal or
   source exclusion, license q15 as a source coordinate, supply a total-Rees
   map, close TD6, or resolve JC2.

Return exactly one verdict: `CONFIRMED`, `CORRECTED`, or `FALSIFIED`, with
the smallest repair if applicable.  Report exact file/line evidence for every
material issue.

Write the complete report only to

```text
xmodel/td6-v89h10t-allq-simultaneous-triangular-flag-hostile-review-report-20260826.md
```

Do not edit the producer package, campaign ledgers, or `jc2-lean`.
