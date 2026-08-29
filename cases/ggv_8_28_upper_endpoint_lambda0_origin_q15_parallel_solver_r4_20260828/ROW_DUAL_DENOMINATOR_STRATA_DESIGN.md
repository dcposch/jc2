# Exact endpoint row-dual and denominator-strata design

Date: 2026-08-28

Status: design only; no CAS or solver execution authorized

## Frozen linear system and typing

The authoritative compiler produces a homogeneous linear system

```text
M(p) x = 0,
p = (q0,q1,q2,c4,c6,c8),
M in Mat_{106 x 105}(Q[p]).
```

The 106 rows are the 50 exactness gates
`q7,q9,q11,q13,q15` (6, 8, 10, 12, 14 rows) and the 56 receiver rows
`G9,G11,G13,G15` (16, 14, 12, 14 rows).  The ordered unknowns consist of the
odd F/primitives/receiver coefficients.  The four endpoint carriers have
indices

```text
x_1   = f_0,
x_14  = f11_1,
x_72  = g11_0,
x_97  = g15_1.
```

The reviewed origin endpoint is the homogeneous quadratic form

```text
E(x) = x_14*x_72 + x_1*x_97.
```

This typing is mandatory.  `E` is not a linear functional and no statement
of the form `w^T M = E` is meaningful.  A valid endpoint certificate uses
linear forms in `x` as multipliers of the linear equations, or equivalently
tests the pulled-back quadratic form on `ker M`.

Frozen source anchors:

```text
58a26a4bf2c2045b96ea8c91de92648d21bda2712840e74b1ea0f09b872ccfa7  compile_symbolic_quadratic_q.py
56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c  symbolic_quadratic_q_rankdrop.sing
8d476d225af6c9c35f737d858dfc613913c727fc71ddb9e275d9509cfde86dd5  equation_names.txt
7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1  branch-P compile_endpoint.py
6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a  verify_lambda0_q15.py
```

## Smallest generic certificate

Work first over the fraction field `K=Q(p)`.  A row-dual for coordinate `j`
is a vector `y_j in K^106` satisfying

```text
y_j^T M = e_j^T.
```

After primitive denominator clearing, retain the exact polynomial identity

```text
u_j^T M = d_j e_j^T,
u_j in Q[p]^106,  d_j in Q[p].
```

Only two coordinate duals are needed to kill `E`: choose one factor from each
of its two monomials.  There are four candidate pairs

```text
{14,1}, {14,97}, {72,1}, {72,97}.
```

Choose the pair whose fraction-free duals have the smallest combined support
and denominator ideal.  For example, duals for coordinates 14 and 1 give,
with `F=Mx` and `D=lcm(d_14,d_1)`,

```text
D*E = (D/d_14)*x_72*(u_14^T F)
    + (D/d_1) *x_97*(u_1^T F).
```

This is a correctly typed, directly replayable membership certificate with
degree-one multipliers in `x`.  On the chart `D != 0`, it proves `E=0` on
`Mx=0`, contradicting the endpoint equation `E=1`.  With a chart inverse `z`,
the explicit unit replay is

```text
1 = z*(right-hand side above) - z*D*(E-1) - (z*D-1).
```

The extractor should emit sparse JSON records for `u_j`, `d_j`, the chosen
coordinate pair, the combined endpoint multipliers, and coefficient-wise
zero replays over `Q[p,x]`.  A printed normal form or rank number is not a
certificate.

## Extraction without a full Groebner basis

1. Emit `M` once as a sparse exact matrix with row and column labels.  Replay
   every entry against the frozen compiler before using it.
2. Use structural bipartite matching and the gate/receiver weight order to
   find a block-triangular pivot pattern.  The endpoint dual only needs the
   reverse dependency cones of columns 1, 14, 72, and 97.
3. Over a preregistered prime, scout several 105-row pivot selections and the
   four endpoint-coordinate pairs.  Modular work may select a sparse pattern
   but proves nothing.
4. Replay the selected solves exactly over `Q(p)` using fraction-free block
   elimination.  At every block, remove polynomial content and record all row
   operations.  Verify `u_j^T M-d_j e_j^T=0` coefficient by coefficient.
5. Prefer several sparse pivot charts to one enormous determinant.  The
   106-by-105 shape supplies alternative 105-row submatrices; different
   charts can avoid spurious components introduced by one unlucky minor.

The current all-maximal-minors command computes much more than is required.
The targeted duals recover only the adjugate rows relevant to `E`, and the
block structure avoids forming a dense 105-by-105 determinant when possible.

### First AWS target: one calibrated left cofactor vector

Because `M` has exactly one more row than column, the first exact AWS job
should extract all maximal minors through one fraction-free solve, not invoke
`minor(M,105)`.  Choose a 105-row submatrix `B` that is nonsingular at the
preregistered modular scout point, and let `m_o` be the omitted row.  Compute

```text
Delta = det(B),
a_num = adj(B^T) * m_o^T.
```

With a consistent sign convention, the 106-vector

```text
ell_R = -a_num,
ell_o = Delta
```

satisfies the polynomial identity `ell^T M=0`.  Its entries are precisely the
signed 105-by-105 maximal minors: `Delta` is the selected minor and each other
entry is a single row-replacement minor.  The exact rank-drop locus is
therefore `V(ell_1,...,ell_106)`.

The emitted `ell` must remain the raw calibrated cofactor vector.  Dividing a
common polynomial factor would preserve the left relation but could delete a
true rank-drop component, so primitive cancellation is forbidden for this
purpose.  Exact replay must check `ell^T M=0`, `ell_o=Delta`, and at least one
fraction-free determinant transcript.  The same factorization of `B` can then
produce the four targeted coordinate row-duals described above.

This left kernel of `M` records row dependence and rank-drop minors.  It is
distinct from the right kernel of `M` used below to pull back the quadratic
endpoint on a rank-drop stratum.

## Denominator/Fitting strata

For a coordinate `j`, define its row-denominator ideal

```text
I_j = { d in Q[p] : d*e_j lies in Row_{Q[p]}(M) }.
```

Each exact dual contributes a generator of `I_j`.  Combining the four
possible endpoint-coordinate pairs produces an endpoint denominator ideal
`I_E` consisting of polynomials `D` for which a replayed identity
`D*E in <Mx>` is available with linear multipliers.

The chart union is `D_k != 0` for the collected generators.  Its complement
is the common zero locus

```text
V(I_E) = V(D_1,...,D_s),
```

not `V(product D_k)`.  This distinction prevents an unnecessary union of
single-denominator hypersurfaces.  If an exact Bezout identity
`sum a_k D_k = 1` is found, summing the replayed endpoint identities gives a
global certificate and there is no residual stratum.

Otherwise, decompose the radical of `I_E` only as far as needed to obtain
domain components.  Every inequation must be represented by an explicit
localizing inverse or saturation.  On each component `S`:

1. Reduce `M` modulo `S` and compute its generic rank over `Frac(Q[p]/S)`.
2. Recompute targeted row-duals.  New denominators give open charts inside
   `S`; their common vanishing ideal defines the next closed residual.
3. Continue recursively until the endpoint restriction is classified or a
   preregistered resource cap is reached.  Further denominator vanishing is
   never silently divided out.

This is a targeted Fitting/row-module stratification.  The full maximal-minor
ideal remains a checksum for true rank drop, not the first computational
object.

## Kernel test on residual strata

Let `N` be a matrix whose columns generate the generic kernel of `M` on a
stratum, so `x=N t`.  Pull back the endpoint:

```text
E_S(t) = E(N t).
```

- On a rank-104 chart, the kernel is generated by one vector `v`; the test is
  the exact scalar polynomial `E(v)` after denominator clearing.
- On higher-nullity strata, compute and retain the full quadratic form
  `E(Nt)`, including every cross term.  Testing only basis-vector values is
  insufficient.
- If `E_S` is identically zero in the component fraction field, the entire
  stratum is endpoint-dead.  Emit either the zero pulled-back coefficient
  list or, preferably, the corresponding degree-one-multiplier certificate
  for `D*E` modulo the stratum equations.
- If `E_S` is nonzero over `C`, choose an exact kernel vector with nonzero
  endpoint value.  Homogeneity then supplies `E=1` after scaling by a square
  root.  Emit the parameter/kernel vector and its explicit quadratic field
  (or algebraic closure) scaling, and replay `Mx=0` and `E=1`.  This is a real
  survivor for this linear reduced slice, not an emptiness certificate.

All component conclusions require exact characteristic-zero replay.  Modular
rank, factorization, or nonzero endpoint restriction is navigation only.

## Stop and custody rules for any later implementation

- Keep the baked-in `c2 != 0` normalization explicit; do not divide by any
  `q_i` or `c4,c6,c8` without a registered complementary stratum.
- Stop `NO_VERDICT` on source drift, matrix-entry disagreement, fraction-free
  replay failure, modular-versus-exact pivot disagreement, a nonzero
  `ell^T M`, failure to calibrate `ell_o` to the raw `Delta`, accidental
  cofactor cancellation, reducer disagreement, unproved radical/component
  claims, or resource cap.
- Run all uncertain elimination, factorization, and kernel work on audited
  zero-swap AWS only.  Local work is limited to hashing and small exact replay.
- Freeze the sparse matrix, pivot charts, row-operation transcript,
  denominator generators/factors, stratum ideals and inequations, kernel
  bases, pulled-back quadratic coefficients, witnesses or unit certificates,
  logs, resource census, and full SHA-256 custody.
- Do not restart any held nearby block/order input unless round synthesis
  explicitly selects it as a distinct registered control.
