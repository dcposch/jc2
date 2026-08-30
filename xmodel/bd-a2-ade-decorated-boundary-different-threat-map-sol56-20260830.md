# ADE-decorated boundary and different: the exact finite threat map

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic-degeneracy-frontier`  
Frozen basis: `dca72076aa1615b0b1286fd4428a1acac7b65963`  
Lifecycle: **EXACT PROVISIONAL THREAT MAP / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint and charged predecessor

This is the finite successor to

```text
f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md
```

and retains its notation.  Thus `X` is an irreducible normal Cartier
hypersurface of class `2A+3B` in `P2 times P1`, `r:Xtilde->X` is the minimal
Du Val resolution, and

```text
A^2=3,       A.B=2,       B^2=0,
K_Xtilde=-A+B,             R=r^*R_X~2A+B,            (0.1)
```

where `R_X` is the source different of `pi:X->P2`.  The ruled marking proves

```text
(ZA+ZB)^perp = D9(-1).                               (0.2)
```

Assume, whenever the forest conclusions below are invoked, that the promoted
dominant-`A2` first-leg bridge puts the reduced infinity, reduced different,
and the exceptional curves over singular points missed by the first leg in
one resolved SNC boundary.  The exact result is:

> **ADE-DECORATED-THREAT.**
>
> 1. A connected exceptional Dynkin type embedded in (0.2) is necessarily
>    `A_r` with `1<=r<=8` or `D_r` with `4<=r<=9`.  Types `A9,E6,E7,E8`
>    are impossible already in the `D9` root coordinates.  This is stronger
>    than a rank count and is proved without assuming a root-subsystem list.
> 2. For any surviving connected tree with positive exceptional different
>    multiplicity vector `m`, the strict-transform attachment vector is
>    `n=Cm>=0`.  All solutions are classified exactly by the congruences in
>    Sections 3--4.  If a target-line pullback through the point meets the
>    different properly (as a projectively finite `pi` permits), then
>    `1<=sum n_i<=8`; if the `B`-fibre through the point also meets the
>    different properly, the sharper bound is `sum n_i<=4`.  Hence these
>    explicitly proper-intersection strata are literal finite sets.
> 3. Forest topology acts on **distinct physical germs**, not on the entries
>    or support of `n`.  A tangent contact of large numerical multiplicity is
>    one joining path.  A branch through an ADE node can contribute at both
>    adjacent graph vertices while still being one physical attachment.
> 4. No remaining connected type is eliminated by these numerical and local
>    forest tests.  Every `A_1,...,A_8` and `D_4,...,D_9` has an explicit
>    Cartier-lattice one-germ pattern with `sum n_i<=2`.  “Survives” here means only
>    that these necessary tests do not kill it; neither an embedding by
>    effective exceptional curves nor an incidence equation is constructed.

The actual finite successor is therefore not another unrestricted lattice
search.  It is the effectivity and physical-attachment test on the explicit
finite congruence sets, together with a separate treatment of nonfinite or
common-component strata where the intersection cap is unavailable.

## 1. Local Cartier equations on an ADE tree

Fix a singular point `p` and number the irreducible exceptional curves
`E_1,...,E_r`.  Let `C` be the positive ADE Cartan matrix, so

```text
E_i.E_i=-2,        E_i.E_j=1 for adjacent vertices,
(E_i.E_j)=-C.                                      (1.1)
```

Write the total different over `p` as

```text
R=R_str+sum_i m_i E_i,       m_i>=1,                (1.2)
```

and define

```text
n_i=R_str.E_i>=0.                                   (1.3)
```

Every `m_i` is positive because `pi o r` contracts `E_i`, so its Jacobian
determinant vanishes at the generic point of `E_i`.  Since `R.E_i=0`,

```text
n=Cm.                                               (1.4)
```

Conversely, at the level of necessary lattice data, (1.4) gives a bijection

```text
{m in Z_(>0)^r : Cm>=0}
  <--> {n in Z_(>=0)^r minus {0} : n in C Z^r},
m=C^(-1)n.                                          (1.5)
```

Indeed every entry of the inverse of a connected finite ADE Cartan matrix is
strictly positive.  Thus a nonzero nonnegative integral `n` has positive
rational inverse, and it gives an integral `m` exactly when `n in C Z^r`.
This is a classification of the numerical solutions, not a converse
existence theorem for a Cartier prime or an incidence singularity.
In particular, (1.4) by itself kills no ADE type: at any vertex `j`, take
`n=k e_j` with `k` divisible by `det C` (or merely by the order of the
corresponding fundamental-weight class).  Then `m=C^(-1)n` is positive and
integral, and scaling `k` gives an unbounded ray.  Every finite conclusion
below therefore cites a separate global proper-intersection cap or the
explicit `D9` embedding.

Infinity has the same local arithmetic.  If `p in H`, write

```text
r^*H=H_str+sum_i h_iE_i,       h_i>=1,
a_i=H_str.E_i,                 a=Ch>=0.              (1.6)
```

Thus the boundary and different decorations are two points of the same
dominant root-lattice semigroup, with separately recorded physical branches.

## 2. Which connected ADE types can occur in `D9`

The roots of the lattice (0.2) are exactly

```text
plus-or-minus e_u plus-or-minus e_v,       u!=v.     (2.1)
```

There is a short coordinate proof that a connected root lattice generated by
such roots is classical.  Map a simple-root basis into (2.1), and form a
signed graph whose coordinate positions are vertices and whose simple roots
are edges.  Connectedness of the Dynkin diagram forces the used coordinate
graph to be connected.  Switch coordinate signs along a spanning tree so
that its edge roots are differences `e_u-e_v`.

If `s` coordinate positions occur, those spanning-tree roots generate the
full `A_(s-1)` lattice.  The image rank is between `s-1` and `s`.  In rank
`s-1`, every remaining edge is balanced and the generated lattice is exactly
`A_(s-1)`.  In rank `s`, some edge is unbalanced; adjoining its sum root to
the tree differences generates exactly `D_s`.  There is no third case.

Since only nine coordinates are available, every connected exceptional type
is therefore among

```text
A_1,...,A_8,        D_4,...,D_9.                    (2.2)
```

This excludes `A9,E6,E7,E8`.  Conversely the standard difference roots on
`r+1<=9` coordinates embed each `A_r` in (2.2), and the standard signed roots
on `r<=9` coordinates embed each `D_r`.  These are **lattice-eligibility**
statements only.  The actual exceptional curves may fail the effective-cone,
fibre-configuration, or simultaneous-embedding tests.

For a disconnected exceptional lattice, apply the argument to every
connected Dynkin component.  Orthogonal components can share coordinate
support in special ways, so their ranks alone do not certify a simultaneous
embedding.  One further exact gate is useful: if the total exceptional
lattice has rank nine, then

```text
det(Lambda_exc)=4*[D9:Lambda_exc]^2.                 (2.3)
```

Any proposed full-rank direct sum whose determinant is not four times a
square is impossible.  No primitivity is assumed in (2.3).

## 3. Exact `A_r` multiplicities

Number the `A_r` chain `1-2-...-r`.  The cokernel of its Cartan matrix is
cyclic of order `r+1`, and (1.5) becomes the explicit congruence

```text
sum_(i=1)^r i*n_i = 0 mod (r+1).                    (3.1)
```

This is exact: the displayed weighted sum kills every column of `C`, and it
is surjective because the first coordinate has weight one.  For every
nonzero `n>=0` satisfying (3.1), the unique positive multiplicities are

```text
m_j = ((r+1-j)*sum_(i<=j) i*n_i
       +j*sum_(i>j) (r+1-i)*n_i)/(r+1).             (3.2)
```

In particular, a contact supported numerically at a smooth point of vertex
`i`, so `n=k e_i`, is Cartier exactly when

```text
k is a multiple of o_i=(r+1)/gcd(i,r+1).            (3.3)
```

Under the cap `sum n_i<=8`, every vertex of `A_1,...,A_7` permits such a
one-vertex contact, while `A8` permits it only at vertices `3,6`.  Under the
sharper cap four, the vertices permitting at least one such contact are

```text
A1: {1}                 A2: {1,2}
A3: {1,2,3}             A4: empty
A5: {2,3,4}             A6: empty
A7: {2,4,6}             A8: {3,6}.                 (3.4)
```

An empty entry in (3.4) does **not** kill the singularity: it only kills a
one-germ contact at a smooth point of the minimal ADE divisor.  At the
numerical Cartier/curvette level there is a uniform one-physical-germ
survivor for every `A_r`:

```text
r=2k-1:  n=2e_k,
          m=(1,2,...,k-1,k,k-1,...,2,1);

r=2k:    n=e_k+e_(k+1),
          m=(1,2,...,k-1,k,k,k-1,...,2,1).          (3.5)
```

The odd-rank pattern is one order-two tangency at the smooth point of the
central exceptional curve.  The even-rank pattern is one irreducible branch
through the node between the two central exceptional curves, contributing
one to each adjacent entry of `n`.  Blowing up that node turns the contact
into one leaf path.  Both patterns have `sum n_i=2` and satisfy (3.1).

More generally, one irreducible physical branch meeting the node `i--(i+1)`
has

```text
n=u e_i+v e_(i+1),       u,v>=1,                    (3.6)
```

and is numerically Cartier exactly when
`i*u+(i+1)*v=0 mod (r+1)`.  This makes the distinction between graph support
and physical-point count explicit.

## 4. Exact `D_r` multiplicities

Use the numbering

```text
1--2--...--(r-2),
              |--(r-1)
              |--r,                                 (4.1)
```

and put `a=n_(r-1)`, `b=n_r`, and
`T=sum_(i=1)^(r-2) i*n_i`.  The condition `n in C Z^r` is exactly

```text
a=b mod 2,
2T+(r-2)a+r*b=0 mod 4.                              (4.2)
```

The inverse formulas are

```text
m_j=sum_(i=1)^(r-2) min(i,j)*n_i+j*(a+b)/2,
                                      1<=j<=r-2,
m_(r-1)=T/2+r*a/4+(r-2)*b/4,
m_r    =T/2+(r-2)*a/4+r*b/4.                        (4.3)
```

Thus (4.2), nonnegativity, and nonzero `n` classify all positive integral
solutions of (1.4).  For a smooth-vertex contact `n=k e_i`, the least
possible `k` is

```text
i<=r-2:  1 if i is even, 2 if i is odd;
i=r-1,r: 2 if r is even, 4 if r is odd.             (4.4)
```

Every value in (4.4) is at most four, so every vertex of every
`D_4,...,D_9` remains available under the sharper cap.  More strongly, at
the numerical Cartier/curvette level all these types have the uniform
transverse one-germ pattern

```text
n=e_2,
m=(1,2,2,...,2,1,1),                                (4.5)
```

where the string of twos runs from vertex `2` through vertex `r-2`.
This has `sum n_i=1` and gives a locally tree-shaped attachment.

## 5. The global intersection caps

The semigroups in Sections 3--4 are infinite without a global proper-
intersection input: scaling either (3.5) or (4.5) gives an infinite ray.
The class calculation supplies an exact finite cap in the finite stratum.

Suppose there is a target line through `pi(p)` whose pullback `L~A` and
`R_X` have no common curve.  A projectively finite `pi` guarantees such a
choice: the finitely many images of different components exclude only
finitely many lines through `pi(p)`.  Over every singular point `q in L`,
write

```text
r^*L=L_str+sum_i ell_(q,i)E_(q,i),       ell_(q,i)>=1. (5.1)
```

The lower bound holds because the divisorial valuation of every exceptional
curve centred at `q` is positive on the maximal ideal, and the local line
equation belongs to that ideal.
The same orthogonality calculation gives a nonnegative attachment vector
`b_q=C_q ell_q` for `L_str`.  Put `n_q=C_qm_q` for the different.  The three
exceptional cross-terms cancel to one copy:

```text
L_str.(m_q E_q)       =ell_q^t n_q,
(ell_q E_q).R_str     =ell_q^t n_q,
(ell_q E_q).(m_q E_q)=-ell_q^t n_q.                 (5.2)
```

Consequently the exact proper-intersection identity is

```text
8=L.R=L_str.R_str+sum_(q in L intersect Sing X) ell_q^t n_q. (5.3)
```

The first term and every summand are nonnegative, and every
`ell_(q,i)>=1`.  Therefore, for the chosen point `p`,

```text
1<=sum_i n_i<=8.                                    (5.4)
```

There is a sharper conditional slice.  Let `F_p~B` be the `P1`-base fibre
through `p`.  If `F_p` and `R_X` have no common irreducible component, write
`r^*F_p=F_str+sum beta_(q,i)E_(q,i)` at the singular points of that fibre.
The coefficients over `p` are at least one.  The identical cross-term
calculation gives

```text
4=F_p.R=F_str.R_str+sum_(q in F_p intersect Sing X) beta_q^t n_q,
```

and properness makes all terms nonnegative.  Hence

```text
sum_i n_i<=4.                                       (5.5)
```

Neither cap is asserted when the chosen slice shares a different component.
In particular, projective coefficient basepoints can force every target line
through their image to contain a contracted different carrier.  Those
nonfinite cases remain outside (5.4), although (5.5) can still apply when the
base fibre is proper.

The fixed infinity divisor gives a coupled boundary/different constraint.
Assume `H` and `R_X` have no common irreducible curve.  At every singular
point `p in H`, use the vectors `(h,a)` from (1.6) and `(m,n)` from (1.2).
Expansion on the resolution gives the exact global identity

```text
8=H.R=H_str.R_str+sum_(p in H intersect Sing X) h_p^t n_p.  (5.6)
```

All terms are nonnegative under the no-common-curve hypothesis.  Hence

```text
sum_p h_p^t n_p<=8,
sum_p sum_i n_(p,i)<=8.                             (5.7)
```

If `H` and `R_X` share a nonexceptional curve, the proper-intersection
argument behind (5.6)--(5.7) is unavailable.  That common-carrier stratum is
an explicit surviving threat, not silently discarded.

## 6. Forest topology uses physical germs, not `n`

Take a full embedded log resolution of the reduced first-leg boundary.  Over
one singular point, include in `T_p` the ADE tree and every additional
exceptional vertex introduced to resolve its boundary contacts.  It is a
connected tree.  Delete the interior of `T_p` from the resolved dual graph.
Then the exact forest criterion is:

> Every connected component of the remaining graph may meet `T_p` by at
> most one edge.                                                   (6.1)

Indeed two such edges, together with the unique path inside `T_p` and a path
inside that outside component, form a cycle.  Conversely, attaching forest
components once to a tree preserves a forest.

The edges in (6.1) are distinct **physical branch contacts after log
resolution**.  They are not the integers `n_i`.

Consequently the forest kills:

* two distinct physical branches of one irreducible strict different
  component attaching to the same exceptional tree;
* attachments from two vertices or points whose carriers are already joined
  by a boundary path outside that tree; and
* two disjoint connector loci between the connected total transforms of
  infinity and of the different, unless those supports share a component
  that changes the quotient graph.

It does not kill:

* one tangent branch with `n_i>1` at a single physical point;
* one branch through an ADE node, with `n` supported on the two adjacent
  vertices; or
* several branches on distinct outside components which are connected only
  through `T_p`, producing a star rather than a cycle.

There is a useful global formulation.  In a forest, two connected subgraphs
have connected intersection after subdividing physical intersection points
as vertices.  The support of `H` is connected because it is an effective
ample `(2,3)` divisor on the infinity surface `P1 times P1`; the support of
`R_X` is connected because `2A+B` is ample on `X`.  Their total transforms
are therefore connected.  A survivor with no shared nonexceptional carrier
has only one graph-theoretic connector between them.  The eight units in
`H.R=8` may nevertheless concentrate at that connector as tangency or ADE
Cartier multiplicity.  Numerical weight eight is not eight graph edges.

## 7. Exact killed/surviving threat table

The deductions can now be stated without mixing levels.

```text
KILLED UNCONDITIONALLY BY THE D9 ROOT MODEL
  connected A9, E6, E7, E8;
  any rank-nine direct sum failing det=4*square.

KILLED IN A CAPPED PROPER-INTERSECTION STRATUM
  every n violating (3.1) or (4.2);
  every n with sum n_i>8 under (5.4);
  every n with sum n_i>4 under (5.5).

KILLED BY THE RATIONAL-FOREST GRAPH
  precisely the repeated physical joining patterns in (6.1),
  including two contacts from the same outside connected carrier.

NOT KILLED BY THESE TESTS
  A1,...,A8 via (3.5);
  D4,...,D9 via (4.5);
  high contact concentrated at one physical germ;
  nonfinite/common-carrier cases where no cap has been proved.
```

The word “survivor” is deliberately negative: it means that the displayed
necessary tests have not contradicted the decoration.  Standard coordinate
roots exhibit an abstract lattice embedding, but do not prove simultaneous
effectivity, realization by vertical curves in the nine-blowup marking, or
compatibility with a quadratic Miranda incidence.

## 8. Hostile checks, exact remaining gap, and scope firewall

The following tempting shortcuts are false and have been excluded from the
theorem.

* **Rank at most nine allows `E6` or `E7`.**  The signed-coordinate proof in
  Section 2 uses the actual roots of `D9`, not rank alone, and removes them.
* **`n_i=4` means four boundary edges.**  It can be one order-four physical
  contact.  Forest topology sees the resolved branch path.
* **Support on two ADE vertices means two physical points.**  A branch
  through their node gives one point, as in the even `A_r` survivor (3.5).
* **Every congruence solution occurs.**  Equations (3.1) and (4.2) are only
  the Cartier-lattice gate.  The effective cone and analytic incidence map
  remain unproved.
* **`A.R=8` always bounds `sum n`.**  The proof needs a pullback line meeting
  the different properly.  It can fail at a nonfinite coefficient basepoint.
* **Connected infinity and different must meet transversely many times.**
  In a forest their entire intersection must instead collapse to one
  connector; all eight intersection units may be concentrated there.
* **A common infinity/different carrier has nonnegative residual
  intersection.**  Proper intersection has failed, so (5.6) cannot be used.

The exact remaining finite task in the projectively finite,
no-common-carrier stratum is to enumerate the pairs

```text
(a,n) in (C Z^r intersect (Z_(>=0)^r minus {0}))^2,
sum n_i<=8,       a^t C^(-1)n<=8,                   (8.1)
```

together with their partitions into physical analytic branches, the single-
connector forest condition, simultaneous embeddings of all singular trees
in `D9`, and effectivity of the strict carrier classes in the ruled
nine-blowup marking.  Formula (8.1) is finite and exact, but this packet does
not assert that every pair is realized.

Separately unresolved are: a different component contained in infinity; a
vertical/base fibre contained in the different; projective or affine
coefficient-basepoint nonfiniteness; the local analytic restriction imposed
by an actual bidegree-`(2,3)` equation; and simultaneous effective
realization of the allowed root embeddings.  Nonnormal incidence closures
remain governed by their normalization and conductor packet and are not
mixed into this theorem.

Also outside are a proof that an arbitrary cubic block has a quadratic
presentation, basis minimization, higher coefficient degree, another block
degree, primitivity, a polynomial map, a counterexample, and JC2.  No CAS,
finite-field sampling, AWS, or `jc2-lean` operation enters this packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19667`.
- Body SHA-256:
  `5a1985f48f6b61d4f12b288942b3bbb753b45f3e18a6e31b85cbc077ccd8e2ef`.
- Frozen basis: `dca72076aa1615b0b1286fd4428a1acac7b65963`.
