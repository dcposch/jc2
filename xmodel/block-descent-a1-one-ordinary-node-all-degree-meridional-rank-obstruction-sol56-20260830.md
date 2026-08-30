# One-place A1 branch with one ordinary node: all-degree meridional-rank obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle_m0` lane)  
Frozen basis: `65d42c3468f115359ada65ce84ad2196c7630939`  
Lifecycle: **FINAL+VERIFIED ALL-DEGREE THEOREM / CONNECTED SIMPLE DEGREE d>=4 EXCLUDED / BROADER HORNS OPEN**

## 0. Theorem and verdict

Let `B` be an irreducible reduced affine plane curve satisfying

```text
normalization(B)=A1;
B has exactly one affine singularity;
that singularity is one ordinary two-branch node.        (0.1)
```

Suppose there is a monodromy representation

```text
rho:pi1(A2-B) -> S_d                                     (0.2)
```

such that every positively oriented generic meridian of `B` maps to a
transposition and the image acts transitively on `{1,...,d}`.  Then

```text
d <= 3.                                                  (0.3)
```

In particular, no connected generically simply ramified cover of degree
`d>=4` can have (0.1) as its complete branch curve.  For `d=4` this contains
the universal minimal-packet obstruction of the predecessor, but the proof
does not mention four projection strands, quasipositive factorization,
Hurwitz orbit, or an `S4` packet.

The argument is exact.

1. The corrected Neumann--Rudolph knot-at-infinity lemma and ordinary-node
   smoothing make the link at infinity a genus-one graph knot, hence a
   trefoil or its mirror.
2. The infinity-knot group surjects onto the affine curve-complement group.
   Composing with (0.2) gives a transitive meridian-transposition image of the
   trefoil group.
3. The trefoil has two meridional generators.  Two transpositions satisfying
   its braid relation move at most three letters, so their image cannot be
   transitive in degree at least four.

The degree-three `S3` coloring is a sharp control for the last group-theory
step only.  It does not realize the local `(2,2)` node inertia, which already
requires four letters.

## 1. Charged theorem and replay inputs

```text
e72a78f7dd027626b38ace5d770bf3b9be386b6626a2033fbb9d3ef81d79a444
  xmodel/block-descent-a1-quartic-cycle0-all-minimal-packets-graph-knot-obstruction-sol56-20260830.md
e1d0472bfbd5203d1e75582c3be5b44b50d9db4987d27b97b2864cee4931522f
  ops/block_descent_a1_quartic_cycle0_all_minimal_packets_replay.py
43c83d47d864537aae6fec7203111aaa3c6c52fa4bbc0e95c6877c61aa86ad57
  xmodel/block-descent-a1-quartic-cycle0-polynomial-link-obstruction-sol56-20260830.md
a6b000430e872e372c6c4cad9d694baa522746717eeef837e52884b206eff6fa
  ops/block_descent_one_node_all_degree_meridional_rank_replay.py
```

The primary topology interfaces, audited in the predecessor, are:

```text
David Eisenbud and Walter D. Neumann,
Three-Dimensional Link Theory and Invariants of Plane Curve Singularities,
Annals of Mathematics Studies 110, Princeton University Press, 1985.

Walter D. Neumann,
"Complex algebraic plane curves via their links at infinity",
Inventiones Mathematicae 98 (1989), 445--489,
DOI 10.1007/BF01393832; especially Theorem 1.

Walter D. Neumann and Lee Rudolph,
"Unfoldings in knot theory",
Mathematische Annalen 278 (1987), 409--439,
DOI 10.1007/BF01458078;
with "Corrigendum: Unfoldings in knot theory",
Mathematische Annalen 282 (1988), 349--351,
DOI 10.1007/BF01456981; corrected Lemma 7.1.

Horst Schubert,
"Knoten und Vollringe",
Acta Mathematica 90 (1953), 131--286,
DOI 10.1007/BF02392437.
```

The corrigendum is essential: it corrects the definition of a good
polynomial and explicitly restates and reproves the knot-at-infinity lemma.
No false implication from quasipositivity to strong quasipositivity is used.

## 2. The infinity knot is a trefoil

Choose a reduced polynomial equation

```text
B=f^(-1)(0).                                             (2.1)
```

Because the normalization is `A1`, its compactification adds one point.
Thus `B` has one normalization place at infinity and its link at infinity
`K_infinity` is a knot.  Corrected Neumann--Rudolph Lemma 7.1 says that a
reduced fibre with knot link at infinity makes `f` good: every fibre is
regular at infinity.

Choose a small disk about zero containing no other critical value and a
nonzero regular value `epsilon` in it.  Goodness identifies the links at
infinity of `f^(-1)(0)` and `f^(-1)(epsilon)` and prevents vanishing cycles
at infinity.  On the complement of a Milnor ball around the sole node,
Ehresmann triviality shows that the nearby fibre changes only by the local
node smoothing.

A compact core of the normalization is a disk.  Delete small disks around
the two node preimages; the Euler characteristic becomes

```text
1-2=-1.                                                  (2.2)
```

The ordinary-node Milnor fibre is an annulus, of Euler characteristic zero.
Gluing it to the two new boundary circles leaves Euler characteristic `-1`
and leaves only the boundary `K_infinity`.  The nearby regular fibre core
therefore has genus one.

Neumann's regular-curve theorem identifies this core with the unique minimal
Seifert surface of `K_infinity`.  Hence

```text
g_3(K_infinity)=1.                                       (2.3)
```

The link at infinity of an affine algebraic plane curve is a toral graph
link.  A graph knot in `S3` is generated from the unknot by connected sums
and cabling.  Schubert's formulas

```text
g(J#K)=g(J)+g(K),
g(C_(p,q)(J))=p g(J)+(p-1)(|q|-1)/2                    (2.4)
```

show that the only genus-one graph knot is `T(2,+/-3)`, equivalently the
right or left trefoil.  Therefore

```text
K_infinity = trefoil or mirror trefoil.                 (2.5)
```

## 3. The infinity group surjects onto the affine group

This step is independent of the number `d` in (0.2).  Choose any generic
finite projection of `B`, with regular-fibre meridians
`x_1,...,x_N`, and based finite braid monodromies
`beta_1,...,beta_s`.  Zariski--van Kampen gives

```text
G_aff=pi1(A2-B)
 = F_N / <<x_j^(-1) beta_v(x_j): all j,v>>.             (3.1)
```

Let `beta_infinity=beta_1...beta_s`, up to the harmless inverse convention.
The Artin presentation of the closed boundary braid gives

```text
G_infinity=pi1(S3-K_infinity)
 = F_N / <<x_j^(-1) beta_infinity(x_j): all j>>.        (3.2)
```

The individual relations in (3.1) imply the product relation in (3.2).
Consequently the identity on fibre meridians induces a meridian-preserving
surjection

```text
G_infinity ->> G_aff.                                   (3.3)
```

Composing (3.3) with (0.2) preserves the image.  Thus the trefoil group has
a transitive degree-`d` representation in which every meridian maps to a
transposition.

## 4. Trefoil meridional rank bounds the degree

Either trefoil orientation has the two-meridian presentation

```text
G_3_1=<a,b | aba=bab>.                                  (4.1)
```

Put `A=rho(a)` and `B=rho(b)`.  Both are transpositions in `S_d`.  There are
only three possibilities.

1. If `A=B`, their image is `C2` and their nontrivial orbit has size two.
2. If `A` and `B` are distinct and disjoint, they commute, so
   `ABA=B` and `BAB=A`; relation (4.1) would force `A=B`.  This case is
   impossible.
3. If `A` and `B` are distinct and overlap in one letter, they satisfy (4.1)
   and generate `S3` on exactly three letters.

Hence every meridian-transposition image of the trefoil group has

```text
largest orbit <=3,
image order in {2,6}.                                   (4.2)
```

It cannot be transitive on `d>=4` letters.  This contradicts (0.2) and proves
(0.3).

Equivalently, a transitive graph of transposition generators on `d` letters
needs at least `d-1` edges, whereas the trefoil group has meridional rank two.
The direct relation analysis above is slightly sharper because it also
classifies the two-generator images.

## 5. Scope and campaign consequence

The theorem applies simultaneously to every projection degree and every
based braid/Hurwitz presentation of a branch satisfying (0.1).  No Alexander
calculation is necessary once the exact affine singularity census is known.
In the plane-Jacobian campaign it excludes the irreducible ordinary-node
control for every connected transposition cover of degree at least four, not
only the frozen quartic packet.

The following remain outside its scope.

1. A tangential two-point conductor has delta invariant greater than one;
   its nearby regular fibre has higher genus.
2. A point-bijective unibranch singularity contributes additional delta even
   though it is invisible to the two-point-fibre count.
3. A reducible connected source forest is not normalized by one `A1`; node
   smoothing can connect components without creating the same genus.
4. Additional branch components give the affine monodromy image additional
   meridional generators.
5. Non-transposition generic inertia and disconnected covers do not satisfy
   (0.2).

The theorem therefore closes an all-degree **irreducible, sole ordinary-node,
one-place, connected simple-cover lane**, not the full charged
`R4-CYCLE-0` horn.  The proper-block ruling data are not used.

## 6. Deterministic replay and firewalls

```text
a6b000430e872e372c6c4cad9d694baa522746717eeef837e52884b206eff6fa
  ops/block_descent_one_node_all_degree_meridional_rank_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical, with

```text
stdout SHA-256:
583da5d653ad234c9d642c3c7cc8d8ad31b30ab61f417c12df8fbdb7fa32831d

status=PASS-ONE-NODE-ALL-DEGREE-MERIDIONAL-RANK
payload_sha256=c4593ac35230962ea90bc535534fb9fa77abe0e409d18158743b660a0f1c1cd1
```

The replay exhausts all ordered transposition pairs satisfying the trefoil
relation in `S_d` for `2<=d<=10`, verifies the symbolic equal/overlap/disjoint
census, finds maximum orbit size three and maximum image order six, and
checks the exact formulas

```text
equal pairs:                d(d-1)/2;
overlapping distinct pairs: d(d-1)(d-2).                (6.1)
```

The mutation `--mutate-allow-degree-three` exits nonzero because the standard
`S3` trefoil coloring is transitive in degree three.  This is a group-level
control only; it does not assert `(2,2)` inertia in degree three.

The replay does not encode the corrected Neumann--Rudolph lemma, local node
smoothing, Neumann's minimal-Seifert theorem, graph-knot classification,
Schubert's genus formula, Zariski--van Kampen, the closed-braid Artin
presentation, or the boundary-to-affine quotient.  Those are the written
theorem interfaces above.

Nothing here constructs a finite cover or Keller map, resolves a tangential,
unibranch, or reducible horn, proves JC2, or touches the formalization tree,
top ledgers, sealed lanes, or the campaign pilot log.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10646`.
- Body SHA-256:
  `bf9dfc3740dc88e6865b7f8a49b47c12a2b49d0f1da71b3411d07ea86d3d0dec`.
- Frozen basis: `65d42c3468f115359ada65ce84ad2196c7630939`.
