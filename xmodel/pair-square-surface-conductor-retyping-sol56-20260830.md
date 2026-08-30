# Surface pair-square/QCS: conductor retyping and the pole-source exact sequence

Author: Sol 5.6 surface-successor lane  
Date: 2026-08-30 UTC  
Frozen repository basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: `SEALED INDEPENDENT REPORT / N2-N3 CONFIRMED / SURFACE TARGET SHARPLY RETYPED OPEN`

## 0. Verdict

The Opus N2 and N3 curve-layer no-go statements are correct.  In particular,
no rank-sum baseline-to-pole construction should be revived: full sheet blocks
usually do not land in the pole-moving space, while the canonical finite
inertia map runs onto that space with a forced kernel.

The actual surface card remains live, but its literal object is not yet a
mathematical definition.  Three corrections precede any attempted proof.

1. Use the canonical finite normalization of
   `P1_f times P1_g` in `C(x,y)`, rather than an unspecified product
   compactification.  The closure of the off-diagonal surface is then
   canonical.
2. Retain the conductor of its normalization **and** the marked pullback of
   the diagonal-contact locus.  Normalizing and then keeping only the
   unmarked normalized boundary separates exactly the branch identifications
   that a pair-event construction is supposed to remember.
3. Take a relative conductor/vanishing object modulo its generic boundary
   local system, and take cohomology.  Raw boundary chain ranks change under
   blowups and count persistent Kummer ramification even when the Section-7
   excess is zero.

At a boundary cluster `C` of physical places with local sheet sets `S_P`, the
correct local linear object is the augmentation of the **total local sheet
set**, not a chosen full block and not the direct sum of one vector per flag:

```text
0 -> direct_sum_(P in C) Qtilde[S_P]
  -> Qtilde[disjoint_union_(P in C) S_P]
  -> Qtilde[C] -> 0.                                  (0.1)
```

If `|S_P|=Lambda(P)` and `w=sum_P Lambda(P)`, its middle rank is `w-1`.
The internal-place part has rank `w-|C|`, and the inter-place augmentation
has rank `|C|-1`; no spanning tree or splitting is chosen.  At a generic
point of quotient line `i`, this rank is `b_i-1`, so a geometrically defined
specialization cokernel would have the desired rank `w_i(z)-b_i`.  Constructing
that specialization, with braid and conductor descent, is the first genuine
surface gate; the numerical inequality alone does not construct it.

If these local objects assemble to a finite pair-event graph `Gamma_F` whose
marked vertices are the **physical pole places** `P_infinity`, then the card's
map has a canonical and correctly directed source: it is the connecting map
in relative cohomology

```text
Qtilde[P_infinity] -> H^1(Gamma_F,P_infinity;Q).       (0.2)
```

When all pole marks lie in one connected event component, (0.2) is injective
and

```text
dim H^1(Gamma_F,P_infinity)=s-1+b_1(Gamma_F).          (0.3)
```

Thus, after an independent chain-level identification of this target with the
reviewed excess module of dimension `E_gen`, QCS becomes the nonnegativity of
an honest cycle rank.  Neither the graph, that identification, nor the marked
connectivity theorem is proved here.  The cheapest next object is the
conductor augmentation/vanishing sheaf for one actual quotient line, tested
first on the constant Kummer surface below.

## 1. Custody and exact scope

This report read the following complete sealed inputs:

```text
f6a8d6e1b21c588e34fd7788c28533eb00aa81ab653a5d7fa901573b54ee4552
  xmodel/pair-square-qcs-gate-hostile-review-opus5-20260830.md

c02c11732defca176da0ce63f71017eb497d1cf56f213a6fa2d6b6d9571f6bfa
  xmodel/pair-square-qcs-gate-sol56-20260830.md

2dbb4e9652939a7954c82fd45c2afbdad03a784731b13de4afb77e157c26a5a6
  xmodel/pair-square-qcs-coordinator-integration-sol56-20260830.md

cee4e1f8079b5a20ee6fca3c7fa58dda1d8c90aeb235cd411d5fc485b9eb7936
  xmodel/pcb-generic-collision-surplus-coordinator-integration-sol56-20260829.md
```

All displayed hashes are full-file SHA-256 hashes recomputed from the current
worktree.  The third input is a coordinator integration on the same frozen
basis; this report only sharpens its open surface successor and does not edit
it.  No canonical file, script, or formalization tree was read or changed, and
no CAS was used.

The typing register is binding:

```text
flag       = an index i of a Section-7 proper critical-value quotient line;
point      = z in that quotient line;
place      = a physical boundary point of a normalized generic fibre;
sheet      = a branch of a finite local cover over a geometric basepoint;
series     = a chosen local expansion representing a branch.
```

Neither a flag nor a quotient point is a pole place.  A sheet is not a place:
one place of local degree `lambda` supports `lambda` nearby sheets.  A series
is presentation data and is not used as a vertex.

## 2. Independent verification of N2

Let `Omega` be a `d`-element sheet set, let `sigma` have pole cycles
`C_1,...,C_s` of lengths `e_j`, and put

```text
E=Q[Omega],       V=E/Q*1,       W=im(sigma-1) subset V.
```

In `E`, `im(sigma-1)` consists exactly of vectors whose coordinate sum on
each cycle is zero.  For a nonempty support `S subset Omega`, the class
`[1_S]` lies in `W` exactly when there is a scalar `lambda` such that

```text
1_S-lambda*1 in im(sigma-1).
```

Taking the coordinate sum on `C_j` gives

```text
|S intersect C_j|=lambda*e_j.
```

Summing over `j` gives `lambda=|S|/d`.  Therefore

```text
[1_S] in W
 iff |S intersect C_j|=|S|*e_j/d for every j.          (2.1)
```

This proves N2.  It is an exact obstruction, not a generic-position warning.
In particular, a full coordinate block cannot simply be projected and then
declared to land in the pole-moving space.

## 3. Independent verification of N3

Let `tau_1,...,tau_r` be the finite branch monodromies of the connected curve
cover and suppose

```text
tau_1 ... tau_r sigma_infinity=1.
```

For linear operators `alpha,beta`,

```text
im(alpha*beta-1) subset im(alpha-1)+im(beta-1),
im(alpha^(-1)-1)=im(alpha-1).
```

Iteration gives

```text
W_infinity=im(sigma_infinity-1)
          subset sum_c im(tau_c-1).                   (3.1)
```

Make the source an **external** direct sum

```text
A_fin=direct_sum_c im(tau_c-1),
```

sum its components in `V`, and apply the canonical pole-moving projector
`1-(1/ord(sigma))*sum_k sigma^k`.  Equation (3.1) makes the resulting map
`A_fin -> W_infinity` surjective.  Its source rank is the total finite
ramification length

```text
sum_c dim im(tau_c-1)=sum_i d_i(b_i-1)=2G-2+d+s,
```

whereas `dim W_infinity=d-s`.  Hence

```text
dim ker(A_fin -> W_infinity)=2G-2+2s.                 (3.2)
```

This is zero only for `(G,s)=(0,1)`.  When `s=1`, the desired increment
`s-1` is already zero.  Thus the canonical curve-inertia construction is a
surjection with a structural kernel precisely in the nontrivial range.  This
proves N3 with the external-direct-sum and projector conventions made explicit.

## 4. The canonical surface ambient object

Let

```text
T=A2_(f,g),       S=A2_(x,y),       K=C(x,y),
d=[K:C(f,g)].
```

Let `Y` be the normalization of `T` in `K`.  It is finite over `T`.  The
Keller map factors as

```text
S --j--> Y --pi--> T.                                 (4.1)
```

The first arrow is a birational quasi-finite morphism to a normal surface,
hence an open immersion by Zariski Main.  Indeed, an element of `K` integral
over `C[f,g]` is integral over `C[x,y]` and therefore lies in the normal ring
`C[x,y]`, which gives the factorization.  Keller etaleness gives
quasi-finiteness.  Since a normal surface is Cohen--Macaulay and `T` is
regular, the finite map `pi` is flat of degree `d`.

Put `R=Y-j(S)`.  The canonical finite-etale locus is

```text
U=T-pi(R),       X=F^(-1)(U)=Y times_T U.              (4.2)
```

This is the card's actual surface cover.  To include the physical pole
places without choosing a source compactification, let

```text
Tbar=P1_f times P1_g
```

and let `Ybar` be its normalization in `K`.  This is a canonical finite
normal surface over the fixed ordered target compactification.  The pole
places are the geometric points over `g=infinity` on the normalization of a
geometric generic `f`-fibre.  They need not be in bijection with irreducible
components of the surface boundary: one horizontal component can be a
multisection and contain several geometric generic places.

Now form

```text
Z=(X times_U X)-Delta,
W=scheme-theoretic closure of Z in Ybar times_Tbar Ybar. (4.3)
```

Both `W` and its factor-swap involution are canonical.  Let
`nu:W^nu->W` be the normalization, let `D_Delta` be the marked inverse image
of the locus where `W` meets the diagonal component of the full fibre square,
and retain the conductor diagram

```text
C^nu  --> W^nu
 |          |
 v          v
C     -->   W.                                         (4.4)
```

The tuple `(W^nu,C^nu->C,D_Delta)`, not the unmarked surface `W^nu` alone, is
the minimum surface pair-event datum.
Over `U`, `Z` is already smooth and the conductor is supported on the
boundary.  Intersections of closures of different off-diagonal sheets occur
in `C`; normalization separates them into `C^nu`.  Discarding (4.4) discards
the desired identifications.

This construction removes the card's arbitrary-compactification ambiguity.
If a log resolution is later used to turn (4.4) into a cellular object, its
output must live in a homotopy/derived category.  Individual cellular chain
ranks are not blowup invariants.

## 5. The exact local pair-event linearization

Fix a quotient point `z` but do not identify it with a place.  Let
`C(i,z)` be its finite set of physical finite-value places.  For each
`P in C(i,z)`, let `S_P` be the finite set of nearby local sheets in a
source-labelled proper tube and write

```text
|S_P|=Lambda(P),       S_C=disjoint_union_P S_P,
w_i(z)=|S_C|=sum_P Lambda(P).
```

For a finite set `A`, write

```text
Qtilde[A]=ker(Q[A] -> Q),
```

where the arrow sums coefficients.  Sending every sheet in `S_P` to the
basis vector `[P]` gives the canonical exact sequence

```text
0 -> direct_sum_P Qtilde[S_P]
  -> Qtilde[S_C]
  -> Qtilde[C(i,z)] -> 0.                              (5.1)
```

No splitting of (5.1) is canonical or needed.  If `r=|C(i,z)|`, its ranks
are

```text
internal-place rank = sum_P(Lambda(P)-1)=w_i(z)-r,
inter-place rank    = r-1,
total event rank    = w_i(z)-1.                       (5.2)
```

The first term is the local residual-diagonal/moving contribution.  The
last term is the canonical linear rank that a conductor construction must
recover from identifications among distinct **physical places**; it is an
augmentation module, not the vector space on every ordered pair and not a
chosen spanning tree.  Formula (5.2) is the exact candidate local boundary
matrix.  Identifying it with a stalk constructed from (4.4) remains part of
gate (5.5), rather than being inferred from the rank calculation.

At a generic point of quotient line `i`, there is one place of local degree
`b_i`, so the generic event rank is `b_i-1`.  Consequently a geometrically
defined injective cospecialization

```text
A_i,generic -> Qtilde[S_C(i,z)]                        (5.3)
```

would have cokernel rank

```text
(w_i(z)-1)-(b_i-1)=w_i(z)-b_i.                        (5.4)
```

Summing (5.4) would give `E_gen`.  But (5.3) is not supplied by the rank
inequality `w_i(z)>=b_i`: it must be constructed from (4.4), nearby/cospecial
paths, and the actual source labels, and it must descend under the root braid.
A chosen nearby root or a chosen subset of sheets is forbidden.  Thus (5.1)
types the target without positing the missing map by dimension.

The provisional local surface gate is therefore:

```text
construct a conductor augmentation complex A_i on U_i;
identify its generic local system with rank b_i-1;
prove its special quotient is concentrated in degree zero with rank w_i-b_i.
                                                               (5.5)
```

Only after (5.5) may one define the direct sum of special quotients as an
excess module of dimension `E_gen`.

## 6. The correctly directed pole-source map

Suppose the conductor augmentation complexes assemble, after the factor-swap
quotient and without identifying flags with places, to a finite event graph
`Gamma_F`.  Its vertices must be physical boundary-place labels (or their
monodromy-equivariant local system), and its weighted incidence data must come
from (5.1).  Mark the geometric generic pole-place set

```text
P_infinity subset Gamma_F,       |P_infinity|=s.
```

For any finite graph and marked vertex set, the cohomology exact sequence is

```text
H^0(Gamma_F) -> H^0(P_infinity)
 -> H^1(Gamma_F,P_infinity) -> H^1(Gamma_F) -> 0.      (6.1)
```

If all pole marks lie in one connected event component, the image of the
first arrow on those marks is exactly the constants.  Hence (6.1) gives a
canonical injection

```text
Htilde^0(P_infinity;Q) -> H^1(Gamma_F,P_infinity;Q).  (6.2)
```

Using the canonical permutation pairing of the finite pole set identifies
the source with `Htilde_0(P_infinity;Q)=V^sigma`.  This is the card's arrow,
now with its direction and construction explicit.  If `Gamma_F` is connected,

```text
dim H^1(Gamma_F,P_infinity)=s-1+b_1(Gamma_F).          (6.3)
```

More generally, if the pole marks meet `c` event components, (6.1) supplies
only rank `s-c`; the restriction of (6.2) to the full reduced pole module has
kernel rank `c-1`.  Thus **marked connectivity**, not abstract dimension, is
the first global injectivity discriminator.

The remaining identification

```text
H^1(Gamma_F,P_infinity;Q) ~= C_coll(F),
dim C_coll(F)=E_gen                                      (6.4)
```

must be proved from the local conductor complex (5.5).  It may not be made by
declaring enough edges.  If (6.4) and marked connectivity both hold, then

```text
E_gen=s-1+b_1(Gamma_F),
Xi=E_gen-(s-1)=b_1(Gamma_F)>=0.                         (6.5)
```

This would prove QCS at actual-map scope.  Equation (6.5) is a consequence
of two geometric theorems, not a definition of `Gamma_F`.

## 7. Honest constant-Kummer surface control

For `b>=2`, consider the polynomial surface map

```text
F_b:A2_(a,x) -> A2_(a,t),       F_b(a,x)=(a,x^b).
```

Over `U=A1_a times Gm_t`, its restriction

```text
X=A1_a times Gm_x -> U
```

is finite etale of degree `b`.  The off-diagonal closure in the affine fibre
square is

```text
W_b=union_(zeta^b=1,zeta!=1) {x_1=zeta*x_2}.
```

All `b-1` components meet the diagonal along the persistent boundary line
`x_1=x_2=0`; when `b>=3`, they also meet one another there.  The normalization
is the disjoint union of `b-1` affine planes.  For `b>=3` its conductor
remembers the mutual identification, while for every `b>=2` the marked
diagonal-contact pullback remembers the residual/diagonal event.  Thus the
unmarked normalization loses required pair data.

Along the parameter `a`, there is one physical boundary place of local degree
`b`.  Its local pair-event augmentation has rank `b-1` at every point, so

```text
w(a)=b identically,       w(a)-b=0.                    (7.1)
```

The required special-minus-generic event complex is therefore zero.  Any raw
complex that counts the `b-1` normalized residual components or the persistent
conductor line as excess fails this control.  Blowing up one point of that
line adds boundary cells but cannot change (7.1), proving that chain-group
dimension is the wrong invariant; relative vanishing cohomology is the right
type.

This is an honest polynomial surface and an honest finite-etale cover over
`U`, but it is not a Keller map:

```text
Jac(F_b)=b*x^(b-1).
```

It is therefore a typing and blowup control only, not a QCS or JC2 falsifier.
For the ordered generic fibre `a=constant`, the map `x -> x^b` has one pole
place, so the pole-source rank is also correctly zero.

## 8. Cheapest next gates

The surface avenue should proceed in this order.

1. **CONDUCTOR-STALK.**  On one actual Section-7 quotient line, construct the
   local sheet augmentation (5.1) directly from the canonical closure and
   conductor (4.3)--(4.4).  Do not choose a representative root, series, or
   sheet block.
2. **GENERIC-QUOTIENT.**  Construct (5.3) geometrically and prove the quotient
   is degree-zero of length `w_i(z)-b_i`.  The constant-Kummer family must
   return zero.  A failure here stops `dim C_coll=E_gen` before topology.
3. **BLOWUP/DESCENT.**  Express the object in a derived or simple-homotopy
   category, retain the conductor equivalence relation, and prove root-braid,
   factor-swap, and admissible-blowup descent.
4. **PLACE-GRAPH.**  Assemble physical-place vertices and event incidences.
   A surface component is not substituted for its geometric generic places.
5. **MARKED-CONNECTIVITY.**  Prove all physical pole marks lie in one event
   component using the `A2` filling and Keller Jacobian.  Curve monodromy and
   local inertia cannot prove this by N2--N3.
6. **IDENTIFICATION.**  Prove (6.4) by an explicit quasi-isomorphism, then use
   the connecting map (6.2).  Do not define the graph by demanding its first
   Betti number equal `Xi`.

The cheapest next object is therefore not a resolution or a large
normalization computation.  It is the conductor augmentation sheaf and its
generic-to-special cone on one quotient line, together with the exact Kummer
zero test.  This is desk algebraic topology/local normalization; no heavy CAS
is licensed yet.

## 9. Maximum safe scope

Safe exact outputs are:

```text
N2 support proportionality:                    PROVED;
N3 canonical inertia surjection/kernel:        PROVED;
canonical finite surface completion Ybar:      PROVED;
normalization-without-conductor is insufficient: PROVED by Kummer control;
local cluster augmentation exact sequence:     PROVED;
pole-source relative-cohomology arrow:          PROVED conditional only on
                                                an assembled marked graph;
surface event sheaf, graph, dimension match,
marked connectivity, injectivity, and QCS:      OPEN.
```

No formal quotient flag is identified with a physical place; no place with a
sheet; no sheet with a series.  This report constructs no actual
counterexample, selector, `PairRef`, QCS proof, PCB proof, or JC2 conclusion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18318`.
- Body SHA-256:
  `cbe0b53c1af0ee738bdfb6475abdb09fb49d203e3706514a812a2863fa5a52f2`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
