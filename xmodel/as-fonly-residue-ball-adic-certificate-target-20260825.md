# AS fixed-support: exact adic-local certificate target after residue-ball Hensel

Status: **POST-CUTOFF STRATEGY NOTE; NO NEW COMPUTATION**

Date: 2026-08-25

Input: the producer-exact residue-ball theorem in
`xmodel/as-fonly-residue-ball-collision-compactness-theorem-20260825.md`.

## 1. Correct local object

Fix a total-degree/support cap and write the complete map in its AS residue
tube as

```text
P=x-x^3+3A,       Q=y+3B,
```

where every coefficient of `A,B` is an integral variable and the supports
are fixed once and for all.  Let `E_mu(A,B)` be **every** coefficient of
`det J(P,Q)-1`.  Divide only common, source-proved powers of three, obtaining
integral generators `e_mu`.  The relevant analytic algebra is

```text
T = Z_3<all coefficient variables> / (e_mu),
```

or a finite disjoint cover by explicitly reconstructed residue charts of
this tube.

The target is

```text
T[1/3]=0.
```

It is not global membership `3^N in (E_mu)` inside the raw polynomial ring.
After inverting three, the parametrization `P=P0+3A` also sees rational maps
far outside the integral residue tube; the elementary ideal `(3x-1)` is the
control showing why zero adic completion does not imply global `3^N`
membership.

## 2. Smallest exact analytic certificate

A portable exact certificate for `T[1/3]=0` is a finite polynomial identity

```text
sum_mu H_mu e_mu = 3^M (1+3G),               (2.1)
```

with `M>=0` and `H_mu,G` integral polynomials (or explicitly finite
restricted-series truncations whose omitted tail has a certified extra
factor of three).  The factor `1+3G` is a unit in the restricted Tate
algebra by its convergent geometric inverse.  After inverting three, (2.1)
makes the determinant ideal the unit ideal.

This target is complete and source-honest:

- the identity is checked coefficientwise over `Z`;
- all determinant rows occur among the `e_mu`;
- every division by three is justified before reduction;
- the unit claim uses only the Gauss-norm inequality `|3G|<1`;
- no rational automorphism outside the integral tube is accidentally killed.

If the affinoid generic fibre is empty, Tate-algebra Nullstellensatz gives an
analytic unit combination.  Clearing finitely many powers of three and
approximating its restricted coefficients one further 3-adic digit yields a
finite identity of the form (2.1).  Thus this is not merely sufficient; it
is the natural finite target for the empty residue tube.

## 3. Computationally cheaper equivalent: finite covered transition DAG

Before attempting a global Tate reduction, use the chronological compiler to
build a finite rooted DAG of accepted coefficient cylinders.  Every node
must carry:

1. an exact reconstruction of one complete fixed-support map modulo its
   stated power of three;
2. every determinant coefficient row at that precision;
3. the next-digit affine/source matrix `L` and divided carry `r` over `F_3`;
4. a disjoint and exhaustive description of its children.

An obstructed leaf is certified by a sparse left-cokernel row

```text
lambda L = 0,          lambda r != 0,
```

or by a proof-checked finite-field ideal certificate on every rank-minor
chart.  A surviving node records its affine particular and full kernel, not
only a representative.  Coverage is a theorem only when the child charts
form a disjoint exhaustive partition of the parent, including pivot-zero and
embedded/nonreduced strata.

An empty finite DAG is the most direct finite-precision consequence of
compactness.  Conversely, arbitrarily deep nodes in this finitely branching
tree give an infinite compatible branch by Koenig, hence a fixed-support
`Z_3` Keller map.  The residue-ball theorem then supplies its moving
collision automatically.

The sparse leaf identities can later be lifted and telescoped into (2.1): a
left-cokernel unit at the last digit is the finite-chart shadow of the Tate
unit factor.

## 4. Effect on the current Q5/H6 gate

The unpinned 142-trit/197-row Q5/H6 formula remains the immediate priority
because it is the current complete chronological chart, not because it lacks
collision variables.

- **SAT:** run corrected V2 literal reconstruction first.  If it proves the
  determinant is one modulo the stated precision, the residue-ball theorem
  already gives three moving preimages of every target in the common ball.
  Do not spend a separate main slot solving collision coordinates.  Freeze
  the full affine fibre, compute its divided next-carry Jacobian/cokernel, and
  test whether a source-licensed regular minor or finite repeating state gives
  singular-Hensel/all-depth continuation.  A single representative is not
  fibre continuation.
- **UNSAT:** solver output is not enough.  Finish the current bit-blast,
  CaDiCaL/DRAT, and independent checker path, then translate the core back to
  named source rows.  The ideal deliverable is a covered left-cokernel/Fitting
  certificate that can become one leaf of the finite DAG or one summand of
  (2.1).
- **Pinned-base endpoints:** consume SAT immediately as falsifiers and direct
  controls.  Treat pinned UNSAT without a checked proof only as navigation;
  it does not cover the unpinned fibre.

The five-row pointwise Q5/H6 obstructions are therefore valuable as candidate
analytic unit cores, but their coefficients must be promoted over entire
rank charts.  Pointwise sparse rows alone neither prove a leaf empty nor
construct (2.1).

## 5. Firewall

Neither certificate target may consume:

- high-band or filtered rows that do not reconstruct the full determinant;
- a state reset at each precision rather than a reduction-compatible map;
- support growth, newly introduced coefficient variables, or changing
  normalization;
- a global rational ideal after inverting three;
- a module nonmembership statement where only pointwise solvability was
  required;
- solver UNSAT without source translation and proof checking.

The residue-ball theorem removes collision bookkeeping only after complete
map reconstruction.  It does not turn an incomplete carry state into a
counterexample candidate.
