# Producer: exact bidegree-(2,3) rational-forest classification

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra coordinator sublane  
Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`  
Lifecycle: **EXACT DESK PRODUCER / DIFFERENT-MODEL HOSTILE REVIEW REQUIRED**

## 0. Dependency boundary and verdict

This packet classifies a curve-theoretic successor suggested by
`bd-a2-firstleg-rational-forest-multisection-producer-sol56-20260830.md`,
whose full-file hash is

```text
367d8ffa1a374b25ee27ca2a2079721c6b17bd71980a13687b11aa87e86f2986.
```

That predecessor is **provisional pending different-model review**.  Nothing
below promotes its logarithmic first-leg obstruction.  The curve
classification itself is independent of that obstruction.

Let `C` be a reduced divisor of bidegree `(2,3)` on
`S=P^1 times P^1`.  There is a single decisive invariant.  If `delta_p` is
the delta invariant and `r_p` the number of analytic branches at a singular
point `p`, put

```text
K(C)=sum_p (delta_p-r_p+1).
```

Then:

> **Bidegree-(2,3) criterion.**  The reduced total transform of `C` on an
> embedded log resolution has only rational components and forest dual graph
> if and only if `K(C)=2`.

Thus the desired locus is necessarily singular and non-generic, but it is
not necessarily reducible.  There are exactly nine possible reduced
component-bidegree partitions.  Seven have nonempty rational-forest
refinements, described explicitly below, and two have none.

## 1. The genus-budget identity

Use the convention

```text
(a,b).(a',b')=a*b'+a'*b.
```

Every effective `(2,3)` divisor is connected.  Indeed, from

```text
0 -> O_S(-2,-3) -> O_S -> O_C -> 0
```

and Kunneth,

```text
H^1(S,O_S(-2,-3))=0,
```

so `H^0(C,O_C)=C`.

Write

```text
C=union_(i=1)^c C_i,
g_i=genus(normalization(C_i)),
G(C)=sum_i g_i.
```

Let `Sigma` be the finite singular set and let `r_p` be the number of points
of the normalization over `p`.  The normalization exact sequence gives

```text
p_a(C)=G(C)+sum_(p in Sigma) delta_p-c+1.           (1.1)
```

Define the branch-incidence multigraph `I(C)` to have one vertex for every
irreducible component, one vertex for every singular point, and one edge for
each analytic branch at that point.  It is connected, and hence

```text
B(C):=b1(I(C))
     =sum_p(r_p-1)-c+1.                             (1.2)
```

An embedded resolution replaces each singular-point vertex and its incident
star by a tree of exceptional curves, while subdivisions and attached leaves
do not change first Betti number.  Therefore `B(C)` is exactly the first
Betti number of the dual multigraph of the reduced total transform.  The
nonexceptional vertices on that resolution have genera `g_i`, and every
exceptional component is rational.

Adjunction on `P^1 times P^1` gives

```text
p_a(C)=(2-1)*(3-1)=2.
```

Subtracting (1.2) from (1.1) yields the exact nonnegative decomposition

```text
2 = G(C) + B(C) + K(C),
K(C)=sum_p(delta_p-r_p+1).                           (1.3)
```

Here `delta_p>=r_p-1`: separating the branch constants already contributes
`r_p-1` to the normalization quotient.  Thus all three summands in (1.3)
are nonnegative.  The rational-forest criterion follows immediately:

```text
all normalized components rational and resolution graph a forest
<=> G(C)=B(C)=0
<=> K(C)=2.                                         (1.4)
```

This also separates the three phenomena that raw discriminants conflate:

* normalization genus is recorded by `G`;
* distinct branch paths and self-identifications are recorded by `B`;
* cusps, tangency beyond transverse contact, and coalesced multiway contacts
  are recorded by `K`.

For reference, a unibranch singularity contributes its full `delta`; two
smooth branches of contact order `m` contribute `m-1`; and an ordinary
triple point contributes `3-3+1=1`.

## 2. The nine reduced factorization types

An irreducible effective class with a zero coordinate is a single ruling
fibre, of class `(1,0)` or `(0,1)`.  Enumerating unordered sums to `(2,3)`
therefore gives exactly:

```text
F1  (2,3)
F2  (0,1)+(2,2)
F3  (1,0)+(1,3)
F4  (1,1)+(1,2)
F5  (0,1)+(1,1)+(1,1)
F6  (0,1)+(1,0)+(1,2)
F7  (0,1)+(0,1)+(2,1)
F8  (0,1)+(0,1)+(1,0)+(1,1)
F9  (0,1)+(0,1)+(0,1)+(1,0)+(1,0).
```

All irreducible components displayed here are smooth rational curves except
possibly the `(2,2)` component in `F2` and the `(2,3)` curve in `F1`.
Indeed, an irreducible `(1,b)` or `(a,1)` curve is a graph over one ruling.

The following list is necessary and sufficient inside each factorization
type.  “Supported at one point with length `m`” means total local
intersection multiplicity `m`, not merely one set-theoretic branch label.

### F1: irreducible `(2,3)`

The normalization must be `P^1`, and every singularity must be unibranch.
Since the total delta is two, the only possibilities are

```text
two A2 cusps,                 or
one A4 cusp.
```

Both occur.  In affine coordinates, normalization maps with bidegrees
`(3,2)` are

```text
t |-> (x,y)=(t^3,t^2)                         (two A2 cusps),
t |-> (x,y)=(t^2/(1-t^3),t^2)                 (one A4 cusp).
```

The pairs are injective on closed points; their only failures to be
immersions have total delta two.  The second has local coordinates
`y=t^2`, `x-y=t^5/(1-t^3)` at `t=0`.

Equivalently, for a normalization parametrization

```text
nu:P^1 -> P^1 times P^1,       nu=(f_3,g_2),
```

the forest condition says that `nu` has no two distinct points with the same
ordered image and its common ramification defects have total delta two.

### F2: `(0,1)+(2,2)`

Let `H` be the ruling fibre and `Q` the irreducible `(2,2)` component.  Then
the condition is exactly:

```text
Q has one A2 cusp, and H intersect Q is supported at one point with length 2.
```

The contact may be a tangency at a smooth point of `Q`, separate from the
cusp, or the length-two intersection may occur at the cusp.  In the former
case the cusp and tangency contribute `1+1` to `K`; in the latter the one
combined local singularity contributes two.  A nodal rational `Q` has a
self-cycle and fails.

This stratum is nonempty.  For example parametrize `Q` by

```text
t |-> (x,y)=(t^2/(1-t),t^2)
```

and take `H={y=0}`.

### F3: `(1,0)+(1,3)`

The two smooth rational components have intersection number three.  The
condition is exactly that their intersection be supported at one point with
length three.  It is a cubic tangency and contributes `K=3-1=2`.

For example, take the fibre `{x=0}` and the graph `{x=y^3}`.

### F4: `(1,1)+(1,2)`

Again the intersection number is three, and the condition is exactly one
length-three contact.  One example is given by the two graphs

```text
x=y,                 x=y/(1-y^2).
```

Their coincidence divisor is supported at `y=0` with multiplicity three.

### F5: `(0,1)+(1,1)+(1,1)`

Call the components `H,Q_1,Q_2`.  Their pairwise intersection numbers are

```text
H.Q_1=H.Q_2=1,       Q_1.Q_2=2.
```

The condition is exactly that all three pass through one point and that
`Q_1,Q_2` are tangent there with intersection multiplicity two.  The one
three-branch singularity has

```text
delta=1+1+2=4,       r=3,       delta-r+1=2,
```

and its incidence graph is a star.  If any pairwise intersection is left at
another point, a dual cycle remains.  An example is `H={y=0}` together with
the graphs `x=y` and `x=y/(1-y)`.

### F6: `(0,1)+(1,0)+(1,2)`

Call the components `H,V,Q`.  The pairwise intersection numbers are

```text
H.V=H.Q=1,           V.Q=2.
```

The condition is exactly one common triple point at which `V` and `Q` have
intersection multiplicity two.  For example use

```text
H={y=0},             V={x=0},       Q={x=y^2}.
```

### F7: `(0,1)+(0,1)+(2,1)`

Let the distinct disjoint ruling fibres be `H_1,H_2`, and let `Q` be the
smooth `(2,1)` graph.  The condition is exactly that `Q` meet each `H_i` at
one point with length two.  These are two quadratic tangencies, each
contributing one to `K`.  The graph `y=x^2` together with its fibres over
`y=0,infinity` is an example.

### F8: `(0,1)+(0,1)+(1,0)+(1,1)` — impossible

All positive pairwise intersection numbers are one.  The two `(0,1)` fibres
are disjoint.  A triple point can merge the contacts of at most one of them
with the `(1,0)` and `(1,1)` components, because those latter components
meet only once.  Hence at most one unit can enter `K`; equivalently at least
one dual cycle remains.  Thus `K=2` is impossible.

### F9: three `(0,1)` fibres plus two `(1,0)` fibres — impossible

The six intersections are six distinct transverse grid points.  The
incidence graph is `K_(3,2)` and

```text
B=6-5+1=2,           K=0.
```

Thus this type never has forest dual graph.

This proves that the reduced rational-forest locus is the finite union of
the explicit equisingularity/contact refinements inside the seven viable
factorization types `F1`--`F7` above.  In particular it is a proper singular
sublocus of the eleven-dimensional complete linear system `|O(2,3)|`; the
generic smooth genus-two curve is not in it.  The two parametrizations in
`F1` show that reducibility is not forced.

## 3. Finite algebraic stratification and exact test

The preceding description is algebraic, not merely topological.  The
factorization loci are the constructible images of the finitely many
multiplication maps

```text
product_i P H^0(O(a_i,b_i)) -> P H^0(O(2,3))
```

for `F1`--`F9`, after removing further-factorization and diagonal loci.
Within each locus, support multiplicities of pairwise intersections are
given by subresultant/Fitting conditions.  The `A2` and `A4` conditions are
the standard delta-constant, one-branch equisingularity strata.  Thus the
list gives a finite algebraic stratification without constructing an
embedded resolution case by case.

For a concrete coefficient point the shortest exact decision procedure is:

1. verify squarefreeness and factor bihomogeneously;
2. compute the normalization quotient lengths `delta_p`;
3. count normalization points over each singular point to obtain `r_p`;
4. accept exactly when `sum_p(delta_p-r_p+1)=2`.

The same data independently reports the failure mode through (1.3): positive
`G` is normalization genus, while positive `B` is a genuine dual cycle.

No heavy local CAS was run for this desk theorem.  If coefficient ideals are
desired, the appropriate AWS-only packet is a twelve-parameter
multihomogeneous factor/subresultant job, one branch for each `F_i`, followed
by normalization-length and branch-count certificates.  It should output
the seven stratum ideals and explicit witnesses, not merely a numerical
discriminant.

## 4. Miranda infinity typing

For a quadratic-coefficient Miranda presentation, restrict the homogenized
binary cubic to the target line at infinity:

```text
F_infinity(s,t;X,Y)
 = b_2(s,t) X^3 - 3 a_2(s,t) X^2Y
   + 3 d_2(s,t) XY^2 - c_2(s,t) Y^3,               (4.1)
```

where the four displayed coefficients are binary quadratics.  Over `C`, the
factors `3` impose no restriction: (4.1) ranges over the full vector space
`H^0(O(2,3))`.  Consequently the incidence construction alone does not
force a reduced rational-forest curve to be reducible; the irreducible `F1`
strata are genuine boundary forms.  Extra normality, finiteness, and affine
etaleness hypotheses must be checked separately.

The exceptional presentation strata have different meanings and must not be
merged:

* **Projective coefficient base point.**  If the four quadratics have a
  common linear factor `ell(s,t)`, then `{ell=0} times P^1` is a `(1,0)`
  component.  This is the source of `F3`, `F6`, `F8`, and `F9` refinements.
  A squarefree quadratic common factor gives two such fibres; a repeated
  common factor is nonreduced.
* **Fixed fibre root.**  A constant linear factor in `(X,Y)` gives a
  `(0,1)` component.  After a fibre-coordinate change this includes the
  familiar leading-root or fibre-chart degree-drop condition.  It is not by
  itself a drop of the target coefficient degree.
* **Nonreduced infinity.**  If `F_infinity` has a repeated irreducible
  factor, the reduced support has a smaller bidegree and (1.3) with genus
  budget two no longer applies to that support.  Detect this in
  characteristic zero by the common factor of `F_infinity` and all of its
  bihomogeneous partial derivatives, take the squarefree support, and retype
  it before applying any log-boundary claim.
* **Actual target-degree drop.**  If all four quadratic leading forms in
  (4.1) vanish identically, then the degree-two homogenized incidence
  equation is divisible by the target homogenizing coordinate.  The
  `z=0` ambient surface is a projective component, not a bidegree-`(2,3)`
  curve.  Cancel and return to the degree-at-most-one analysis.

Projective base points, nonreduced factors, and actual degree drop therefore
are three distinct strata.

## 5. Conditional campaign consequence and nonclaims

Conditioned on later promotion of the provisional rational-forest first-leg
gate, a reduced quadratic Miranda infinity divisor can survive its
infinity-curve test only in the seven explicit strata `F1`--`F7`.  It need
not be reducible, but it must spend the entire arithmetic-genus budget in
cuspidal or excess-contact delta.  This is a finite successor: add the
ramification divisor on each of those seven strata and test the **full**
resolved boundary.

Passing this curve test is only necessary.  This packet does not show that
any survivor extends to a normal finite Miranda cover, admits an `A^2` first
leg, or survives after the ramification divisor is added.  It does not close
the quadratic Miranda family, prove a general cubic-block theorem, establish
primitivity, construct a map or counterexample, or resolve JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13761`.
- Body SHA-256:
  `b76971e671237b906d4c772ec4008e7153ca6f47705cc994839fef33c12a604e`.
- Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`.
