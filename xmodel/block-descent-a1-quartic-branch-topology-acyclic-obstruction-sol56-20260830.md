# Rank-four successor: branch quotient graph and acyclic obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`sectioned_two_support_universal` lane)  
Frozen basis: `63e4d141b54ceea9c6d2ed4bdb5c7f7c1d2619eb`  
Lifecycle: **EXACT PROVISIONAL THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

For an actual proper block of rank four, let

```text
A2 --g1--> Y --pi=g2--> A2,       deg(pi)=4,
R=NonEt_Y(pi),                    U=Y-R,
B=pi(R)_red.
```

The fixed-sheet theorem leaves four and only four branch-fibre partitions:

```text
T211: (2,1,1),  u=2;          T31: (3,1),  u=1;
S22:  (2,2),    u=0;          S4:  (4),    u=0.          (0.1)
```

The last two loci are finite.  Put `n22=|S22|`, `n4=|S4|`, and
`h=b0(R_red)`.  The finite map `R_red->B` is point-bijective except that
every point of `S22` has two reduced preimages.  The source rational-forest
theorem therefore gives the exact target topology and Euler ledger

```text
B  homotopy-equivalent to a finite multigraph Gamma;
e(B)=h-n22;
b0(B)=k,       b1(B)=beta=n22-h+k;                       (0.2)

e(U)=4-2e(B)-e(T31)-2(n22+n4)
    =4-2h-e(T31)-2n4.                                   (0.3)
```

Thus `(2,2)` fibres are precisely the new conductor identifications: they
create the possible target cycles, while cancelling completely from the
Euler number of `U`.  Comparing (0.3) with the promoted ruling gives

```text
C=A1:  2h+e(T31)+2n4+Q=3;
C=P1:  2h+e(T31)+2n4+Q=2,       Q=sum_t(q_t-1)>=0.       (0.4)
```

There is also a rank-four analogue of the cubic acyclic-branch obstruction,
and it is stronger than a residual normal form:

> **Quartic acyclic obstruction.**  Let `pi:Y->A2_C` be finite flat of
> degree four with `Y` integral and normal.  Assume every irreducible branch
> component has a generically unramified sheet.  If the reduced branch `B`
> is connected and simply connected, then `e_c(Y-R)<=0`.  In particular,
> such a cover cannot be an actual proper block, because its promoted
> `A1`-ruling gives `e_c(U)=e(C)+Q>=1`.

Consequently the exact proper-rank-four threat dichotomy is

```text
(D) B disconnected; or
(C) B connected with beta>=1, hence n22>=h.              (0.5)
```

This is not a quartic-block exclusion: both horns in (0.5) remain open.  It
does show that every connected survivor must contain enough `(2,2)` fibres
to turn the source forest into a cyclic target branch.  In fact its full
degree-four monodromy must be `S4`; the other transitive subgroups are
excluded in Section 7.

## 1. Charged inputs

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
b72e39220f9e8d75e94214d2e5669bda072fcbbd644cfed97f97d9a2b820ad57
  xmodel/block-descent-a1-euler-ledger-sol56-20260830.md
5be2e2af32c0f6201637a652d28a0ff5f6992c5ebde696b1198d7b94e4829cf7
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md
```

The last file supplies the already-audited use of the reduced acyclic-plane-
curve classification.  Its primary source remains

```text
Ivan Arzhantsev and Mikhail Zaidenberg,
"Acyclic curves and group actions on affine toric surfaces",
arXiv:1110.3028v2, Theorem 1.3(b), printed pages 3--4;
published in Affine Algebraic Geometry (2013), 1--41,
DOI 10.1142/9789814436700_0001.

41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
```

The proper-block inputs give `Y` integral normal affine, `pi` finite flat,
`R` a nonempty pure divisor, and the actual morphism `A2->U`.  They also give
a generically unramified block sheet above every target divisor, a source
strict-SNC boundary forest, the ruling identity, and non-Galoisness of
`C(Y)/C(A2)`.

## 2. Exact fibre census

At a geometric closed point, write the finite-flat fibre as the list of the
lengths of its local factors.  A local factor has length one exactly when
`pi` is etale at its point; a non-etale point consumes length at least two.
The partitions of four at a branch value are therefore exactly

```text
(2,1,1), (3,1), (2,2), (4).                            (2.1)
```

On the generic point of every branch component, the fixed-sheet theorem
rules out `(2,2)` and `(4)`.  Hence `S22` and `S4` are zero-dimensional and
finite.  Moreover

```text
B=T211 disjoint_union T31 disjoint_union S22 disjoint_union S4, (2.2)
```

as constructible sets.  This is the complete rank-four census; no reducedness
or smoothness of the fibres is being assumed beyond the displayed local
factor lengths.

## 3. From the source forest to the target quotient graph

Each irreducible component `B_i` is an irreducible component of the Keller
nonproper-value curve, so Chau's polynomial-parametrization theorem makes
its normalization `A1`.  The generic partitions in (2.1) have exactly one
ramification point.  Thus exactly one component `R_i` dominates `B_i`, the
map is birational, and the normalization of `R_i` is also `A1`.

The promoted morphic forest theorem, applied to the actual `A2->U`, makes the
affine incidence multigraph of `R_red` a forest, with self-branches and
parallel branches retained.  Consequently every connected component of
`R_red(C)` is contractible and

```text
e_c(R_red)=b0(R_red)=h.                                (3.1)
```

For a point of `T211`, `T31`, or `S4`, the reduced ramification fibre has one
point.  For a point of `S22`, it has two.  Constructible Fubini immediately
gives

```text
e_c(R_red)=e_c(B)+n22,                                 (3.2)
```

which proves the Euler part of (0.2).

There is no hidden scheme-isomorphism claim.  Analytically, a finite
surjective map is a closed quotient map.  Its equivalence classes here are
singletons except for the `n22` disjoint two-point classes.  A complex
algebraic curve is triangulable; identifying one pair of points in a union
of contractible components has the homotopy effect of adding one graph edge,
including a loop when the points lie in the same component.  Iterating gives
the multigraph `Gamma` with `h` vertices and `n22` edges.  If it has `k`
connected components, then

```text
beta=b1(Gamma)=n22-h+k,       e(B)=k-beta=h-n22.        (3.3)
```

In particular a connected `B` is simply connected exactly when
`n22=h-1`; it has a cycle exactly when `n22>=h`.

## 4. The rank-four Euler cancellation

Let `u(z)=#(pi^-1(z) intersect U)`.  The four rows of (0.1), together with
`u=4` off `B`, give

```text
e(U)=4e(A2-B)+2e(T211)+e(T31)
    =4-2e(B)-e(T31)-2(n22+n4).                         (4.1)
```

Substituting (3.2) gives (0.3).  This is the exact reason that arbitrarily
many `(2,2)` conductor identifications cannot be seen by the ruling Euler
number: each lowers `e(B)` by one and simultaneously contributes a two-sheet
loss.  Only the signed Euler number of the `(3,1)` locus and the number of
totally supported `(4)` fibres remain in (0.3).

The ruling identity now gives (0.4).  Since `e(T31)` is a signed Euler number
of a constructible curve locus, (0.4) alone is not a positivity argument.

## 5. Connected acyclic branch: classification and monodromy

Assume now that `B` is connected and simply connected.  Arzhantsev--
Zaidenberg Theorem 1.3(b) puts every reduced such plane curve, after an
algebraic automorphism, into one of

```text
(I)  y^epsilon p(x)=0;
(II) x^epsilon_x y^epsilon_y
     product_i(y^a-kappa_i x^b)=0.                     (5.1)
```

The etale cover over `A2-B` has transitive monodromy in `S4` because `Y` is
integral.

In a nontrivial comb of type (I), the horizontal meridian is central in
`pi1((C-roots(p)) x C*)`.  Its generic inertia is either a transposition or a
three-cycle.  Their centralizers in `S4` have orders four and three,
respectively, and both are intransitive.  Coordinate-line degenerations have
cyclic image generated by the same intransitive cycle type.  Hence type (I)
is impossible.  This argument does not identify companion labels on
different teeth.

In type (II), weighted radial scaling identifies the global complement group
with the local complement group at the origin.  Every henselian local factor
gives an invariant subset of sheets of its rank.  The partitions `(2,1,1)`,
`(3,1)`, and `(2,2)` therefore put the local image inside `S2`, `S3`, and
`S2 x S2`, respectively, all intransitive.  Global transitivity forces

```text
the fibre at the weighted-cone vertex to have partition (4). (5.2)
```

In particular, two rank-two factors at a `(2,2)` vertex do not help: their
idempotents are defined over the henselian base, so local monodromy preserves
the two pairs rather than exchanging them.

## 6. Why the remaining weighted-cone row has nonpositive Euler number

Write the irreducible components of the weighted cone as `B_i`.  Each

```text
B_i minus {0} is isomorphic to C*,
```

and different components are disjoint there.  The generic ramification index
`e_i` is two or three, and its generic number of unramified points is
`u_i=4-e_i`.

We need one specialization lemma.  Let `z` be a smooth point of `B_i`, let
`y` lie on its dominating ramification divisor `E_i`, and choose regular
parameters `(p,q)` at `z`, with `p=0` defining `B_i`.  The local ring
`C=O_(Y,y)` is Cohen--Macaulay because it is finite flat over the regular
two-dimensional base.  In the height-one DVR `C_(E_i)`, one has
`p=unit*t^(e_i)`.  The associativity formula for the parameter multiplicity
of the one-dimensional Cohen--Macaulay ring `C/pC` gives

```text
length_C C/(p,q) >= e_i.                               (6.1)
```

Equivalently, the local ramified factor cannot lose rank under specialization.
Thus every special point on `B_i-{0}` satisfies

```text
u(z)<=4-e_i=u_i.                                       (6.2)
```

Choose a finite exceptional set `P_i` outside which `u=u_i`.  Since
`e(C*)=0`, the contribution of `B_i-{0}` to `e(U)` is

```text
u_i e(C*-P_i)+sum_(z in P_i)u(z)
  =sum_(z in P_i)(u(z)-u_i)<=0.                        (6.3)
```

For the whole weighted cone, `e(B)=1`, hence `e(A2-B)=0`; and (5.2) gives
`u(0)=0`.  Summing (6.3) proves

```text
e_c(U)<=0.                                             (6.4)
```

This contradicts the proper-block ruling value `e(U)=e(C)+Q>=1` and proves
the quartic acyclic obstruction in Section 0.

The inequality (6.1) is load-bearing.  Allowing an illegal specialization
from generic `(3,1)` to special `(2,1,1)` would create the only positive
Euler correction on a punctured cone component.  The local multiplicity
argument rules out exactly that escape.

### 6.1 The vertex threat is genuinely realizable before the Euler gate

The total vertex in (5.2) is not a fictitious group-theoretic row.  Consider

```text
Y={w^4+a*w+b=0} subset A3_(a,b,w)  -->  A2_(a,b).       (6.5)
```

This is finite flat of degree four, and eliminating `b` identifies
`Y` with the normal integral plane `A2_(a,w)`.  Its ramification and branch
are

```text
R: a=-4w^3, b=3w^4;
B: 256b^3-27a^4=0.                                    (6.6)
```

Away from the origin, putting `(a,b)=(-4t^3,3t^4)` factors the fibre as

```text
w^4-4t^3w+3t^4=(w-t)^2(w^2+2tw+3t^2),
```

so its partition is `(2,1,1)`.  At the origin it is `w^4`, of partition
`(4)`.  Thus (6.5) realizes the irreducible weighted-cone branch, fixed
generic sheets, transitive `S4` monodromy, and the total vertex.  It also
shows why the ruling input is decisive:

```text
U=Y-R isomorphic to A1_w x Gm_(a+4w^3),       e(U)=0.  (6.7)
```

The example saturates (6.4); it is a cover-side control, not a Keller block.

## 7. Full monodromy is forced to be `S4`

The transitive subgroups of `S4` are `C4`, `V4`, `D4`, `A4`, and `S4` in
their degree-four actions.  Because `A2` is simply connected, meridians of
the irreducible branch components normally generate the complement group;
their inertia images therefore normally generate the monodromy group.  The
fixed-sheet theorem makes every such image a transposition or a three-cycle.

The regular groups `C4` and `V4` contain neither cycle type (and are also
excluded by the promoted non-Galois theorem).  A transitive `D4` contains two
transpositions, but their normal closure is the intransitive subgroup

```text
{1,(13),(24),(13)(24)},
```

so they cannot normally generate `D4`.  Hence only `A4` and `S4` remain.

The `A4` row is also empty.  It contains no transposition, so every branch
meridian is a three-cycle and `T211` is empty.  At a point of `S22`, however,
the local group preserves two rank-two factors and lies in

```text
(S2 x S2) intersect A4 = {1,(12)(34)}.                 (7.1)
```

Every local branch through that point contributes a conjugate three-cycle to
the same local group, contradicting (7.1).  Thus `n22=0`.  The quotient-graph
ledger then gives `e(B)=h` and makes every connected component contractible.
If `h=1`, the acyclic theorem already contradicts the ruling.  If `h>=2`,
then `T31=B-S4` and

```text
e(U)=4-3h-n4<=-2,                                      (7.2)
```

again contradicting `e(U)>=1`.  Therefore

```text
the full quartic monodromy of every proper-block survivor is S4. (7.3)
```

At an `S22` point, a `(3,1)`-generic branch component is also impossible:
its three-cycle meridian cannot lie in the pair-preserving local group
`S2 x S2`.  Thus every conductor pairing in the connected cyclic horn is
supported only on `(2,1,1)`-generic branch components.

## 8. Exact residual threat and cheapest next test

After Sections 5--7, the complete live rank-four rows are

```text
B disconnected, with global S4 companion mixing; or
B connected, beta>=1, n22=h-1+beta>=h, with global S4. (8.1)
```

Both retain the exact ruling equations (0.4), and all `(2,2)` pairing points
in the connected row involve only transposition-generic components.

### 8.1 The cubic resolvent lever

Let `L` be the Galois closure of the quartic function field.  By (7.3), its
group is `S4`.  The action on the three unordered pairings

```text
12|34, 13|24, 14|23
```

is the quotient `S4->S3` with kernel the normal Klein four group.  The field
fixed by a pairing stabilizer `D4` has degree three.  Let `Z` be the
normalization of `A2` in that field.  Then `Z` is integral and normal and
finite over `A2`.  It is also flat: locally its normal two-dimensional ring
is Cohen--Macaulay over the regular two-dimensional base, hence a finite
maximal Cohen--Macaulay module and therefore free.  Thus

```text
Z -> A2 is a connected finite-flat normal cubic resolvent.            (8.4)
```

Generic transpositions and three-cycles remain a transposition and a
three-cycle in the quotient, so the reduced branch support of (8.4) is
exactly `B`.  At special values one must use the local decomposition group,
not the roots of a possibly nonnormal classical resolvent polynomial.  The
normalized fibre table is

```text
quartic fibre   quartic local group H       cubic-resolvent fibre
(2,1,1)         C2 transposition             (2,1)
(3,1)           C3 or S3, fixing one letter  (3)
(2,2)           full pair C2 x C2            (2,1)
(4)             D4                           (2,1)
(4)             A4 or S4                     (3).       (8.5)
```

For the `(2,2)` row, the two local rank-two factors make both coordinate
characters nontrivial.  The diagonal subgroup generated only by the double
transposition would map trivially to `S3`, but it cannot contain the
transposition meridian of a local branch; the promoted fixed-sheet input
therefore forces the full pair group and the displayed `(2,1)` resolvent
fibre.  For `(4)`, transitivity and the presence of allowed divisorial
inertia leave `D4`, `A4`, or `S4`; their quotient images are `C2`, `C3`, or
`S3`.

No live horn falls immediately to the cubic theorem.  In the connected horn
the resolvent branch is the same connected but cyclic `B`; in the disconnected
horn it is still disconnected.  Moreover any `T31` value becomes a cubic
triple fibre.  Hence normalization neither repairs the branch topology nor
turns all fibre collisions automatically into `(2,1)`.

The cheapest next test is consequently the minimal connected cycle

```text
h=1, k=1, beta=n22=1, n4=0.                            (8.2)
```

Topologically this asks the normalization `A1` of one branch component to
identify one pair of finite points.  A concrete one-place target control is
the nodal polynomial curve

```text
y^2=x^2(x+1),       x=t^2-1, y=t(t^2-1),               (8.3)
```

whose node identifies `t=1` and `t=-1`.  The decisive desk test is to compute
based `S4` representations of its complement with transposition meridians and
a pair-preserving `(2,2)` node.  Equivalently, pass first to (8.4) and ask
whether the cubic acyclic theorem extends to this first Betti-one branch with
all fibres `(2,1)`.  Either an infinity relation excludes the representations,
or the survivors can be fed into a finite-flat quartic algebra construction.
This tests the first possible conductor loop before attempting an unbounded
curve classification.  In parallel, the minimal disconnected row has two
acyclic components and should be tested against the same based-companion
warning that was essential in the cubic control.

## 9. Desk replay and firewalls

The finite group and ledger calculations are replayed by

```text
6326c5821a9b011f60021da54c133c19863b3593f75f91c211814335a1455b5b
  ops/block_descent_a1_quartic_branch_topology_replay.py
```

Ordinary, `-O`, and `-OO` runs have payload hash

```text
f5cebda8549f140000fba45d3e569b524a7a82667a8c683d96d6c1c2bc7c6081.
```

The mutation `--mutate-allow-cone-rank-drop` is rejected.  The replay checks
9,555 bounded graph/Euler rows, `S4` centralizers, local-factor subgroups, and
the fixed-inertia closures of all transitive subgroups, including the `A4`
pair-local intersection.  It does not encode Chau's theorem, the morphic
forest theorem, local intersection multiplicity, the acyclic-curve
classification, weighted radial equivalence, cubic-resolvent normalization,
or existence of any cover.

Nothing here excludes the primitive/no-proper-block horn, constructs a
Keller map, proves that a proper rank-four block exists, or proves JC2.  The
new closures are exactly the connected simply connected target-branch row
and the non-`S4` quartic-monodromy rows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18735`.
- Body SHA-256:
  `3585d344b20ae2ac7a307d719d87746bd37e4c471a6a20b8e3b2e2e8db0cee48`.
- Frozen basis: `63e4d141b54ceea9c6d2ed4bdb5c7f7c1d2619eb`.
