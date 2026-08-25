# Max12 `(9,12)` order-one squarefree Poisson recurrence, rows 18–12

Status: **PRODUCER-EXACT; REVIEW PENDING.**  Strict total-degree scope is
method-only and classically counterexample-closed.

## Result

For the squarefree cubic `K=x*y*(x-y)`, exact original-bracket replays now
cover every positive homogeneous determinant row from degree 18 through
degree 12 on the displayed reduced families.

1. Rows 18–15 reproduce the triangular recurrence and give the reduced
   squarefree degree-15 family with base/fresh dimensions `16+6=22`.
2. Row 14 packages exactly as `E14=3*K*[K,Z10]`.  Its corrected solution has
   the sole pole `(4/9)C*W/K`; equivalently `729*R=324*C*W`.  Thus reduced
   polynomial points satisfy `K|C*W`, the union of eight root allocations.
3. Row 13, checked both after rational denominator clearing and by direct
   polynomial substitution, collapses those allocations: rootwise
   squarefreeness gives `K|C` and `K|W`.  Write `C=K*L`, `W=K*M`.
4. Row 12 has the exact pole factor

   ```text
   3*N*R-A*K*L^3,
   N=M-A*L/3,
   R=9*U-A^2*L-3*A*N-3*K*L^2.
   ```

   Its only nonpolynomial part is a scalar multiple of `N*R/K`, so reduced
   points satisfy the next eight-way condition `K|N*R`.

The corresponding predicted reduced dimensions are `19+5=24` at row 14,
`21+5=26` at row 13, and `23+3=26` at row 12.  These are dimensions of the
displayed reduced parameterizations, not declarations about nilpotents in
the compiler's incidence ideals.

## Exact identity and divisibility separation

The AWS/Singular statements are polynomial identities in the complete
original homogeneous determinant rows, with every displayed denominator
cleared explicitly.  The implications from those identities to divisibility
by the three linear factors of `K` are separate reduced-geometric-point/UFD
arguments.  In particular, this package does not claim radical equality
without that argument and does not discard the seven mixed root-allocation
branches at rows 14 or 12.

The degree-14 replay also provides an executable negative control for the
first preregistration's mistyped `(lambda/3)*V`: it is nonzero.  The correct
target-shear term is `(lambda/3)*K*B=(lambda/3)*P7`.

## AWS custody

Every accepted computation ran on r6d `ip-172-30-0-45` and Box02
`ip-172-30-0-186`, under fail-closed Linux/AWS/hostname/tag checks.  Accepted
algebraic stdout is byte-identical across hosts; timing stderr differs.  The
hosts are two executions of the same sources, not two algorithms.

Cases:

- `cases/max12_912_order1_binary_cubic_squarefree_poisson_recurrence_aws_20260825/`;
- `cases/max12_912_order1_binary_cubic_squarefree_degree14_poisson_aws_20260825/`;
- `cases/max12_912_order1_binary_cubic_squarefree_degree13_poisson_aws_20260825/`;
- `cases/max12_912_order1_binary_cubic_squarefree_degree12_poisson_aws_20260825/`.

Each case has a hash-only frozen replay.  V1/V2 parser failures and the V4
permission failure are quarantined and cannot contribute positive evidence.

## Classical-closure firewall and transfer target

The strict total-degree `(9,12)` stratum is not a possible two-dimensional
Jacobian-conjecture frontier: `gcd(9,12)=3`, whereas the classical Heitmann
bound requires the degree gcd of any counterexample to be at least 16.  The
frozen routing correction is
`xmodel/sol-fixed-total-d12-classical-closure-20260825.md`, SHA-256
`71a8c83b923a077b733412fadaae2f03c1c4e50e91fab1249189c6a33eaabf9a`.

Accordingly, no large strict-cap Groebner continuation is warranted.  The
recurrence remains useful as a self-contained source-row mechanism and as a
candidate for weighted or partial-`y` filtrations with unbounded total
degree.  Such a transfer must independently prove bracket homogeneity,
existence of the completed cube root, and the appropriate rational
centralizer theorem; none is inferred here.

## Firewall

No endpoint proves a full Keller pair, all lower rows, an integral or p-adic
lift, selected-Q8 or TD6 landing, maximum twelve, a counterexample, or JC2.
