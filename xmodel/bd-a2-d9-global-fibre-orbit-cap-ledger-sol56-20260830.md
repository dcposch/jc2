# The `D9(-1)` global fibre-orbit classification and typed cap ledger

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic-degeneracy-frontier`  
Frozen basis: `02572552f8f894ede08acb4a020a3af722b03e54`  
Lifecycle: **EXACT GLOBAL ROOT/FIBRE CLASSIFICATION / DECORATED CARRIER LAYER OPEN**

## 0. Endpoint, charged input, and scope

This packet charges the following frozen results:

```text
f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md

ab10ea83f443c93bdb87194ad0e42fe2c442984ba821c3ddf8ddf5cc3f796133
  xmodel/bd-a2-ade-decorated-boundary-different-threat-map-sol56-20260830.md

3846f7e2c861ebf5f399dbc9a729c3f1d35dc28c561891c8883a8a3328a7240f
  xmodel/bd-a2-ade-decorated-threat-map-coordinator-integration-sol56-20260830.md

03263fe7f7d97356f07291bb30ec38d5b4182a1ffc85fcbf57722d59cf3b50a9
  xmodel/bd-a2-ade-cartier-pair-enumeration-sol56-20260830.md
```

Thus `X` is an irreducible normal class-`2A+3B` incidence surface, its
minimal Du Val resolution

```text
r : Xtilde -> X
```

is a smooth rational surface obtained from a ruled surface by nine vertical
blowups, and

```text
A^2=3,       A.B=2,       B^2=0,       K_Xtilde=-A+B.       (0.1)
```

The marked orthogonal lattice is the actual geometric lattice

```text
L=(ZA+ZB)^perp
  =D9(-1)={c in Z^9 : sum_i c_i is even},                  (0.2)
```

whose roots are the vectors `+-e_i+-e_j`.  Every `r`-exceptional curve is
vertical for the resolved conic fibration `Xtilde->P1`.

The exact endpoint proved here has three layers.

1. It classifies **all simultaneous full reflection subsystems** of the
   root system in (0.2), including disconnected ones, modulo `W(D9)`.
2. Under projective finiteness it identifies those signatures bijectively
   with **unmarked weighted singular-fibre-forest combinatorial types** for
   the nine blowups.
3. It proves a typed ledger of target-image, actual-fibre, fixed-infinity,
   and reduced-boundary genus caps for local pairs

   ```text
   n=Cm,             a=Ch.                                (0.3)
   ```

Here `m` is the exceptional coefficient vector of the total different and
`h` is the exceptional coefficient vector of the infinity curve.  The
vectors `n` and `a` are their respective strict-transform intersection
vectors and are never identified.

The word “bijection” below is only a bijection of weighted fibre-forest
combinatorial types.  It is not a classification of blowup positions,
projective configurations or moduli, marked effective exceptional curves,
carrier divisors, analytic germs, or incidence equations.  Common strict
carriers are outside every proper-intersection cap.  Those firewalls are
part of the theorem, not qualifications to be removed in use.

> **GLOBAL ROOT/FIBRE THEOREM.**  In the scope above:
>
> 1. Every `W(D9)`-orbit of full reflection subsystems has a unique signature
>    ```text
>    sigma=(u; b_2,...,b_9; d_2,...,d_9),
>    u+sum_(j=2)^9 j(b_j+d_j)=9.                           (0.4)
>    ```
>    It represents
>    ```text
>    direct_sum_(j=2)^9 A_(j-1)^(b_j)
>      + A1^(2d_2) + A3^(d_3) + direct_sum_(j=4)^9 D_j^(d_j).
>                                                                  (0.5)
>    ```
>    There are exactly `115` signatures: one zero, `15` with connected
>    nonzero root system, and `99` with disconnected root system.
> 2. The same signature is exactly the unmarked weighted fibre forest made
>    of `u` one-blowup blocks `B_1`, `b_j` smooth-only blocks `B_j`, and
>    `d_j` node-second blocks `U_j`.  The exceptional roots of `B_j` are
>    `A_(j-1)`; those of `U_2,U_3,U_j` are respectively `A1+A1,A3,D_j`.
>    The assertion is combinatorial and does not assert that a class-`2A+3B`
>    equation realizes the configuration.
> 3. A target-line cap is shared by all singular points over the same target
>    image, an infinity cap by all relevant points on the one fixed infinity
>    divisor, and a `B` cap by all singular points on the same actual source
>    fibre, with its exact fibre multiplicities.  None is a free per-point
>    budget.  Equations (5.5), (5.7), and (5.8) below are the binding forms.
> 4. If `H` is reduced, its local crepant genus drop at a Du Val point is
>    exactly `h^t a/2`.  In the proper `B/H` stratum this rules out every row
>    with `h^t a=8`; a row with `h^t a=6` requires `sum a_i=2` and consumes
>    the entire global genus-two defect budget.

The first two assertions are an exact global discrete classification.  The
last two are exact necessary filters on decorations, not a converse
effectivity theorem.

## 1. Signed-support classification modulo `W(D9)`

Attach to a set of roots `+-e_i+-e_j` its signed support graph on the nine
coordinate positions.  On a connected support of size `s`, switch coordinate
signs along a spanning tree.  All spanning-tree roots then become differences.
There are exactly two reflection closures:

```text
B_s: all differences on the support,             type A_(s-1);
U_s: all +-e_i+-e_j on the support,               type D_s. (1.1)
```

The first case occurs when every signed cycle is balanced.  One unbalanced
cycle produces a sum root; reflecting it by the difference roots gives all
sum roots and hence the second case.  Conversely the displayed root sets are
closed under their generated reflections.  The low-rank aliases are essential:

```text
U_2=D_2=A1+A1,             U_3=D_3=A3.                   (1.2)
```

Disjoint coordinate-support components are orthogonal.  Permuting components
of equal tag and size leaves only their multiplicities, giving (0.4).

It remains to check that passage from all signed permutations to the
index-two even-signed group `W(D9)` does not split an orbit.  Every signature
has an odd-signed stabilizer:

* if a coordinate is unused, flip its sign;
* if a `U_s` block occurs, flip one sign inside that full `D_s` root set;
* otherwise balanced blocks cover all nine coordinates, so one block has
  odd size; flipping every sign in that block fixes its difference root set.

Thus (0.4) is also the exact `W(D9)` orbit key.  Its generating function is

```text
1/(1-x) product_(s=2)^9 1/(1-x^s)^2.                    (1.3)
```

The coefficients through degree nine by used support are

```text
s:       0  1  2  3  4  5   6   7   8   9
count:   1  0  2  2  5  6  13  16  30  40,              (1.4)
```

and sum to `115`.  A nonzero signature is connected only for one `B_s`,
`2<=s<=9`, or one `U_s`, `3<=s<=9`.  Hence there are `8+7=15` connected
and `115-1-15=99` disconnected signatures.  Notice that `U_2` is one
signed-coordinate block but two disconnected `A1` root components.

This uses the reflection-subsystem convention, not saturation of the direct
sum inside its rational span.  If saturation is imposed, at most one `U`
block is allowed: with `k` unbalanced blocks, the ambient intersection asks
only that the sum of their coordinate sums be even, whereas their direct sum
asks that each sum be even, an index `2^(k-1)` condition.  The saturated
diagnostic has `75` signatures, `59` disconnected.  No saturation hypothesis
is charged in the theorem.

## 2. Fibre normal form

Let `C` be a final smooth rational component of a fibre affected by the nine
blowups.  Since `B.C=0`, adjunction and (0.1) give

```text
-2=(K_Xtilde+C).C=-A.C+C^2,
A.C=C^2+2.                                             (2.1)
```

The class `A` is nef.  Hence `C^2>=-2`.  The first blowup changes the original
square-zero fibre component to `-1` and creates a `-1` exceptional component;
every later component is born with square `-1`.  Consequently every component
of an affected final fibre has square `-1` or `-2`.

Write the scheme fibre as

```text
F_t=sum_v beta_v C_v.                                  (2.2)
```

Using `A.B=2` and (2.1),

```text
2=A.F_t=sum_(C_v^2=-1) beta_v.                         (2.3)
```

No component already at `-2` can contain a later blowup centre.  After the
first blowup on a fresh fibre, the unique new edge has two `-1` endpoints.
Every smooth blowup thereafter changes its chosen `-1` to `-2` and appends a
new `-1`; every other edge has a frozen `-2` endpoint.  Therefore a node
blowup, if any, is uniquely the second blowup on that fibre.  There can be
at most one node blowup per fibre.

This gives exactly two blocks using `s` blowups.

### 2.1 Smooth-only block `B_s`

The reduced fibre is the chain

```text
(-1)-(-2)-...-(-2)-(-1),       beta=(1,...,1),           (2.4)
```

with `s-1` internal `-2` vertices.  They form `A_(s-1)`.  For `s=1` there
is no root; this is the unused coordinate `u` in (0.4).  If the original
square-zero component is marked, its position modulo reversal has
`floor(s/2)+1` possibilities.  The unmarked tree forgets that position.

### 2.2 Node-second block `U_s`

For `s=2` the fibre is

```text
(-2)_1 - (-1)_2 - (-2)_1,                              (2.5)
```

where subscripts are `beta`.  Its two `-2` vertices give two distinct `A1`
singular points separated by the `-1` carrier.  For `s>=3`, the contracted
tree is `A3` when `s=3` and `D_s` when `s>=4`.  The two short leaves have
`beta=1`; the fork, every vertex on its long arm, and the terminal
nonexceptional `-1` component have `beta=2`.  The original component is one
of the two symmetric short leaves, so its marked orbit is unique.

In both families the full fibre intersection matrix `Q_t` satisfies

```text
Q_t beta=0,       gcd(beta_v)=1,
sum_(C_v^2=-1) beta_v=2.                               (2.6)
```

These identities independently check every displayed weight.

The charged reduction already proves that every `r`-exceptional curve is
vertical.  Conversely, in the projectively finite scope `A` is the pullback
of a target hyperplane under `Xtilde->X->P2`.  If a fibre component is `-2`,
(2.1) says `A.C=0`, so its target image is a point.  If `r(C)` were a curve,
the finite map `X->P2` would send it to a curve, a contradiction.  Hence
`C` is `r`-exceptional.  Thus the final `-2` fibre vertices are exactly the
Du Val exceptional curves.  Without projective finiteness, extra `A`-null
nonexceptional curves can occur and this converse must not be used.

Doing the blocks prescribed by (0.4) on distinct fibres constructs the
corresponding weighted blowup forest; different fibres have orthogonal root
supports.  Sections 1 and 2 therefore prove the stated bijection of unmarked
weighted combinatorial types.  Marking the original fibre components refines
the generating function to

```text
1/(1-x) product_(s=2)^9
  1/(1-x^s)^(floor(s/2)+2),                             (2.7)
```

whose degree-nine coefficient is `362`.  This is still discrete tree data,
not a configuration or moduli count.

## 3. What the orbit key does and does not quotient

The signature (0.4) is the `W(D9)` orbit key for the **unmarked root image**.
It is only a coarse bucket after adding any of the following:

```text
beta and actual-fibre identity;
the marked original component and proximity history;
attachment vertices and physical attachment points;
(m,n,h,a), target-image labels, or H/R carrier labels.   (3.1)
```

Such decorations can destroy the odd stabilizer used in Section 1.  Exact
decorated canonicalization fixes one coordinate representative of (0.4) and
then minimizes under its actual stabilizer, together with permutations of
genuinely indistinguishable fibres and carrier atoms.  It must not quotient
by an abstract diagram symmetry that the fibre marking breaks.  In particular,
the `U_4` multiplicities distinguish one `D4` arm from the two short arms;
only their transposition survives, not full triality.

Nor is a root embedding an assertion that its simple roots are simultaneously
effective exceptional curves of the incidence surface.  The fibre-normal-form
construction realizes the abstract blowup forest, while effectivity with the
classes `A,H,R`, target images, and an incidence equation remains a separate
condition.

## 4. Paired local Cartier data and physical germs

At a connected exceptional tree with positive Cartan matrix `C`, write

```text
r^*R_X=R'+sum_i m_iE_i,       n_i=R'.E_i,       n=Cm,
r^*H  =H'+sum_i h_iE_i,       a_i=H'.E_i,       a=Ch.   (4.1)
```

For a divisor passing through the point, `n` or `a` is nonzero and the
inverse finite ADE Cartan matrix is strictly positive.  Cartier integrality
therefore makes `m=C^(-1)n` or `h=C^(-1)a` a positive integral vector.  The
congruence tests and inverse formulas of the charged local table apply to
`a` exactly as they apply to `n`, but the two records remain paired and
distinct.  A point off `H` has `(h,a)=(0,0)`.

Neither the support nor an entry of `n` or `a` is a list of physical germs.
On the minimal ADE resolution, the restricted numerical atom grammar is:

```text
k e_i                         one branch at a smooth point of E_i;
u e_i+v e_j,  i--j,           one branch at the node E_i intersect E_j,
                              k,u,v>0.                    (4.2)
```

One irreducible strict-transform carrier can meet the exceptional divisor at
several physical points, so its total vector can be a sum of atoms.  Conversely,
a numerical atom or atom partition does not construct a principal analytic
germ.  A carrier-labelled state must retain separately:

```text
source point and infinitely-near/proximity ID;
actual fibre and component attachment;
physical attachment-cluster ID;
global carrier ID and divisor multiplicity;
target-image label and base contact vector.             (4.3)
```

Carrier IDs may be canonicalized by restricted-growth strings only after
physical attachment clusters have been formed.  If two atoms share an
exceptional crossing or one carrier, they cannot be counted as independent
outside leaves in a forest argument.  Connectedness downstairs is likewise
not enough: a cycle contradiction requires the connected resolved outside
carrier graph and two distinct attachment paths on the same resolved graph.

## 5. Total-transform identities and correctly shared caps

Let `E_i.E_j=-C_ij`.  For two Cartier divisors with total transforms

```text
r^*D=D'+xE,             r^*G=G'+yE,                     (5.1)
```

orthogonality gives `D'.E=Cx` and `G'.E=Cy`.  Expanding all four terms gives
the exact cancellation

```text
D.G=D'.G'+x^t C y.                                     (5.2)
```

All caps below are instances of (5.2).  They require that the named strict
transforms have no common curve, so their remaining intersection is
nonnegative.

### 5.1 Per-target-image caps

Fix a target point `q` and choose a generic target line `L_q` through `q`.
Projective finiteness lets it avoid the images of all named ramification
components and all other singular images.  At every singular point `p` over
`q`, write

```text
r^*L_q=L'_q+ell_p E_p.                                 (5.3)
```

The line equation lies in the maximal ideal at `p`, hence vanishes along
every exceptional component and `ell_(p,i)>=1`.  Since

```text
R~2A+B,       H~A,
A.R=8,        A.H=3,                                   (5.4)
```

(5.2) gives

```text
8=L'_q.R'+sum_(p over q) ell_p^t n_p,

3=L'_q.H'+sum_(p over q) ell_p^t a_p,   q in L_infinity. (5.5)
```

The second line uses a line distinct from `L_infinity`.  Its pullback and
`H` share no curve because the target lines are distinct and the map is
finite.  Thus the coarse necessary bounds are

```text
sum_(p over q) sum_i n_(p,i)<=8,
sum_(p over q) sum_i a_(p,i)<=3.                        (5.6)
```

They are shared per target image.  If several singular points have the same
target image, they do not each receive a fresh budget.  The normal surface
`X` is Cohen--Macaulay and the target is regular, so a finite degree-three
map is flat; consequently a target-image label block has at most three
source points.

### 5.2 Per-actual-fibre caps

For one actual source fibre `t`, use (2.2).  If its nonexceptional strict
fibre has no component in the named divisor, (5.2) gives

```text
4=B.R=F'_t.R'+sum_(p on t) beta_p^t n_p,
2=B.H=F'_t.H'+sum_(p on t) beta_p^t a_p.                (5.7)
```

These budgets are shared only among the singular points on that actual
fibre and use their exact `beta` weights.  In particular the two `A1` points
inside one `U_2` block share one fibre budget.  Both identities remain
conditional on the absence of the corresponding nonexceptional fibre
carrier; projective finiteness alone is not used to remove that condition.

### 5.3 Fixed-infinity cap

If `H'` and `R'` share no nonexceptional carrier, the one fixed infinity
divisor gives

```text
8=H.R=H'.R'+sum_(p in H) h_p^t n_p.                    (5.8)
```

This is one global budget along `H`, not a budget repeated at every point.
The term `h^t n` is the exact exceptional contribution from (5.2); no
transversality or coordinatewise interpretation is being assumed.

### 5.4 Common-carrier firewall

If two divisors share `Gamma`, write `D=d Gamma+D_0` and
`G=e Gamma+G_0`.  Then

```text
D.G=de Gamma^2+d Gamma.G_0+e Gamma.D_0+D_0.G_0.         (5.9)
```

The first term can be negative.  Therefore suppressing a cap preserves a
necessary search but does not produce an exact finite common-carrier
enumeration.  That stratum must retain the carrier class, self-intersection,
multiplicity in every divisor, residual divisor classes, and residual proper
intersections.  No formula in (5.5), (5.7), or (5.8) is charged across a
common strict carrier.

## 6. Reduced-infinity genus defect

Assume in this section that `H` is reduced.  It is the bidegree-`(2,3)` curve
on `L_infinity x P1`, hence

```text
p_a(H)=2,                                               (6.1)
```

and it is connected.  Indeed, two disjoint nonzero effective summands of
bidegrees `(c_1,d_1)` and `(c_2,d_2)` would have intersection
`c_1d_2+c_2d_1=0`; nonnegativity and total bidegree `(2,3)` make this
impossible.  Put `Z=sum_p Z_p`, where
`Z_p=sum_i h_(p,i)E_(p,i)` is supported over one Du Val point.  Crepancy
gives `K_Xtilde.E_(p,i)=0`, while total-transform orthogonality gives

```text
H'.Z_p=-Z_p^2=h_p^t C_p h_p=h_p^t a_p.                 (6.2)
```

Adjunction for `r^*H=H'+Z` and for `H'` therefore yields the sum of the
local genus differences; crepancy and preservation of intersections identify
`p_a(r^*H)` with `p_a(H)`:

```text
p_a(r^*H)-p_a(H')=sum_p h_p^t a_p/2.                   (6.3)
```

More intrinsically, `H` and `H'` have the same normalization.  Localizing
the normalization exact sequence over `p` refines (6.3) to

```text
delta_p(H)=h^t a/2
             +sum_(q in H', r(q)=p) delta_q(H').        (6.4)
```

In particular `h^t a` is even.  If `r_p` is the number of analytic branches
of `H` at `p`, every lifted branch meets the exceptional set with positive
total intersection; a branch through an exceptional node can be counted
twice, never zero.  Hence

```text
r_p<=sum_i a_i.                                        (6.5)
```

Define `k_p=delta_p-r_p+1>=0`.  From (6.4)--(6.5),

```text
k_p>=h^t a/2-sum_i a_i+1.                              (6.6)
```

Let the normalization components of `H` have total genus `g`, and let the
bipartite component/singular-point incidence graph have first Betti number
`b_1`.  The normalization exact sequence and connectedness give

```text
sum_(all singular p) k_p=2-g-b_1<=2.                   (6.7)
```

Thus, summing only the Du Val points,

```text
sum_p max(0,h_p^t a_p/2-sum_i a_(p,i)+1)<=2,           (6.8)
```

and individually

```text
h^t a<=2(sum_i a_i+1).                                 (6.9)
```

When the proper `B/H` identity (5.7) applies, every exceptional fibre
multiplicity is at least one, so `sum a_i<=beta^t a<=2`.  Equation (6.9)
then gives `h^t a<=6`: every `h^t a=8` local row is impossible.  Equality
`h^t a=6` forces `sum a_i=2` and equality `k_p=2`, so that one point consumes
the entire budget in (6.7).  This corollary is not used for nonreduced `H`,
and (5.7) is not used across a common fibre carrier.

## 7. Exact finite algorithm and complexity gate

The exact root/fibre layer is the following deterministic algorithm.

1. Enumerate the nonnegative solutions of (0.4).
2. Replace each `B_s` or `U_s` by the block in Section 2 and verify (2.6).
3. Record `U_2` as one fibre but two physical ADE points; record all other
   nonzero blocks as one ADE point.
4. Canonicalize only by the signature (0.4).  If the original fibre component
   is marked, refine `B_s` by its position modulo reversal and use (2.7).

The replay examines `115` records, takes `0.03` seconds locally, and uses no
external package.  The archived outputs are

```text
38d0d6cd6af0e76d0bddf30018effb3c3a2c8a4ebb511945fa771f3c888b166b
  ops/d9_fibre_signature_enumerate.py

88d30955fc6017770fe02cb381ab25cbcd2ce8263f7403864e8c2dc862530d96
  xmodel/bd-a2-d9-fibre-signatures-sol56-20260830.json
```

For comparison, a naive chronological fibre search has the conservative
upper bound

```text
product_(j=0)^8 (3j+1)=608,608,000                     (7.1)
```

before pruning, and direct minimization under all
`|W(D9)|=2^8 9!=92,897,280` elements would be wasteful.  The signed-block
normal form is the required theoretical orbit compression.

A finite **carrier-disjoint numerical-decoration** successor can now be
specified, but was deliberately not materialized:

1. expand a signature into at most eight physical ADE points (`U_2` realizes
   the maximum), retaining actual-fibre and `beta` labels;
2. partition those points into target-image blocks of size at most three and
   mark each block as lying on or off the fixed target line at infinity;
3. assign `(m,n)` by exact Cartan inversion, assign nonzero `(h,a)` precisely
   at the points in infinity blocks and `(h,a)=(0,0)` off them, and apply the
   shared inequalities (5.5), (5.7), (5.8), and (6.8) only in their typed
   proper-intersection strata;
4. enumerate the restricted atoms (4.2), then physical-point clusters and
   carrier restricted-growth labels (4.3), forbidding a common `H/R` carrier
   in this declared subproblem;
5. test the fully resolved colored incidence graph for the desired forest
   property, and canonicalize inside the actual stabilizer of the root/fibre
   representative rather than by an abstract diagram group.

The root forest has at most eight physical ADE points, so target-image
partitions contribute at most the Bell number `B_8=4,140`.  The coarse target
caps allow at most `64` positive-weight `R` atoms and `24` positive-weight
`H` atoms.  A raw carrier partition could therefore reach `B_88`, far beyond
the one-second local envelope.  In a forest, however, with at most eight
singular-tree vertices there are at most seven outside connector components
of degree at least two; degree-one leaves can be aggregated by local type.
That is the correct next theoretical compression.  Any materialization of
the fully decorated state space must follow a source-reviewed carrier grammar
and run on AWS, not locally.

The preceding five-stage procedure is exact for its explicitly restricted
numerical atom grammar; it is not an analytic-realizability algorithm.
Common carriers require the residual data in (5.9), and arbitrary fibre or
target locations carry continuous moduli.  Neither can be repaired by a
larger discrete enumeration.

## 8. Hostile attacks and scope firewall

1. **`U_2` is not one singular point.**  It is one signed-coordinate and
   actual-fibre block but two `A1` exceptional trees.  Target labels are
   separate; fibre caps are shared.
2. **`A3` has two embedding orbits.**  `B_4` uses four coordinates, while
   `U_3` uses three.  Abstract Dynkin type alone loses this distinction.
3. **`D4` triality is broken.**  The `U_4` fibre weights retain only the
   short-leaf transposition.
4. **Reflection closure is not saturation.**  Multiple `U` blocks are
   allowed in the charged `115`; the separate saturated diagnostic is `75`.
5. **Root orbits are not decorated orbits.**  Positivity, fibre markings,
   carrier labels, and physical attachments are not invariant under an
   unlicensed Weyl reflection.
6. **A formal vector is not a germ.**  Atom partitions are numerical
   signatures.  They neither produce global carriers nor prove that distinct
   atoms live at independent physical points.
7. **A tree is not a configuration count.**  Original-component positions,
   proximity data, fibre/target locations, and cross-ratio moduli are absent
   from the `115` unmarked forest types.
8. **Projective finiteness is essential.**  It is what identifies every
   final `-2` fibre component with an `r`-exceptional curve.  Without it,
   extra `A`-null nonexceptional curves may appear.
9. **Caps have owners.**  Target budgets are per target image, `B` budgets
   per actual fibre with `beta`, and `H.R=8` belongs to the one fixed infinity.
   None may be duplicated at each singular point.
10. **Common carriers are not large capped rows.**  Equation (5.9), not a
    nonnegative local partition, governs them.
11. **No ADE effectiveness converse.**  The theorem classifies simultaneous
    root subsystems and blowup forests, not incidence equations realizing them.
12. **No nonnormal or nonfinite extension.**  Nonnormal surfaces and the
    projectively nonfinite infinity strata remain outside this packet.

The exact remaining global gap is the residual class/intersection theory for
shared carriers, followed by a fully decorated stabilizer key and an
effectivity/incidence-realizability test.  A sharper geometric successor may
first collapse the reduced projectively finite infinity divisor to boundary
type `F5`; that would constrain the unique `F5` boundary point but would not
remove ADE trees on missed affine branch or singular loci.  No affine
smoothness, no assertion that every ADE point lies on `H`, and no such `F5`
bridge is assumed here.

No shared ledger was edited.  No staging, commit, AWS job, heavy local CAS,
Singular operation, or `jc2-lean` access was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26016`.
- Body SHA-256:
  `08484e2866fffda5ce9d2fd109f04e2f05dee3d1f4958ea28d4a08b69e8563ca`.
- Frozen basis: `02572552f8f894ede08acb4a020a3af722b03e54`.
