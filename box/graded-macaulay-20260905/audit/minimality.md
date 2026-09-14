# Full affine presentation minimality — independent exact audit

audit_minimality.py independently parses the complete original direct coefficient
rows, using its own rational sparse-polynomial parser. It binds every source file
to the hash in the new reduced-presentation custody. It does not import the root
reduction/count driver, invoke a Gröbner algorithm, or use a modular rank.

The exact constant-linear coefficient matrix is the Jacobian of the complete
original generator list at the cone origin. Sparse Gaussian elimination over
Python Fraction gives:

| Fibre | Original coordinates | A pivots | c pivot | Exact linear rank | Cotangent dimension | Achieved polynomial presentation coordinates |
|---|---:|---:|---:|---:|---:|---:|
| 77 | 77 | 27 | 1 | 28 | 49 | 49 |
| 111 | 111 | 57 | 1 | 58 | 53 | 53 |
| 129 | 129 | 57 | 1 | 58 | 71 | 71 |
| 136 | 136 | 71 | 1 | 72 | 64 | 64 |

The audit retains the exact echelon basis, its pivot columns and originating row
indices in minimality.json. Thus this is a computed exact rank, not an inference
from the announced pivot count.

All full source equations have zero constant term. For each root-selected A pivot
v, the auditor checks that the original row contains v exactly once, as qv with
q a nonzero rational; every other pivot dependency is earlier in the declared
sequence. Every nonpivot coordinate is initially fixed. Consequently each recursive
substitution maps the origin to the origin and is a global polynomial map over Q.
The audited pivot set is exactly the set of all positive-charge A coordinates.

The auditor then computes the derivative of this complete recursive map exactly.
Because the map fixes the origin, nonlinear monomials contribute no linear term.
It verifies every pivot row has zero derivative after substitution. It finds
exactly one c-containing monomial in the entire original source list: the scalar
multiple of c in the unique target row. That row has no other original linear
term. Eliminating c therefore sends its first derivative to zero. After the A
and c substitutions, the derivative of **every** original generator is zero.
The remaining coordinates have identity derivative.

Let A=R/I and let m be the maximal ideal of its rational cone origin. The original
linear matrix identifies the relations in m/m², hence

    dim_Q(m/m²) = #original coordinates − exact constant-linear rank.

The unit triangular quotient isomorphism, followed by the target unit equation,
gives a presentation A=Q[u_1,…,u_k]/J with the k values in the last table column.
The derivative check gives J⊆(u_1,…,u_k)², agreeing with the computed tangent
dimension.

This presentation attains the minimum possible number of polynomial generators
of the full affine Q-algebra A. Indeed, any surjection Q[t_1,…,t_s]→A pulls the
chosen rational origin back to (t_1−a_1,…,t_s−a_s), and its induced cotangent map
surjects Q^s onto m/m². Therefore s≥dim_Q(m/m²)=k, while the displayed
presentation achieves s=k.

This is an N-independent minimality statement about polynomial presentations of
the full affine quotient. It does not bound the number of coordinates after
localization or on the c=1 section. It does not claim that the ring is polynomial,
that its Krull dimension is k, or that further equations disappear. In particular,
it does not decide c²/c³ membership or their quotient Hilbert dimensions.

The new 57/57 full-ring A eliminations refine the frozen 42/37 N=1 selected-ring
substitutions for the 111/129 fibres; the newly checked full-row custody is what
licenses the larger counts.

Review of reduced/reduce_counts.py found no mathematical correctness bug in its
classification/counting method:

- A nonzero value under a declared valid modular evaluation proves that the
  reduced polynomial over Q is not identically zero. This use of modular
  arithmetic is exact and does not invoke modular ideal membership.
- Candidate zero rows are composed over exact fmpq_mpoly rational arithmetic;
  root assertions reject any accidental modular-zero candidate that expands
  nonzero. No polynomial is discarded solely from vanishing at sample points.
- Homogeneous triangular substitutions preserve row bidegrees, so a surviving
  generator's multiplier count uses its original row degree.
- The unique target row is the only c-containing row; its elimination leaves all
  other reduced generator polynomials unchanged. The c-free row counts therefore
  correctly remove that row and use the remaining variable grading.
- The driver indexes its source-row array by the declared source index. The
  independent parser explicitly verifies that these four source indices are
  contiguous and equal their positions, so that implementation assumption holds.

Artifacts: audit_minimality.py, minimality.json, and minimality.log. Every
recorded original row and its complete variable order are bound by source hashes;
the new root reduced-counts files are also hashed in the independent result.
