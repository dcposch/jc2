# A pentagon obstruction for one degree-five quotient cover

STATUS: UNPROMOTED / manual producer, awaiting independent FIRST.
OWNER: swarmHQ-root. Basis: 8e495d13faed71fb03966b2f7e297c41bdf8ee1c.
Scope: one fixed normal projective cover over C; not a JC2 proof or counterexample.

## Statement
Let S be the smooth degree-five del Pezzo surface identified with the stable
compactification of the moduli of five ordered distinct points of P1. Let
G=A5 act by labels, and H=A4 be the stabilizer of label 5. Set X=S/H, Y=S/G.
The finite map pi:X->Y has generic degree five. There do not exist open subsets
U of X and V of Y, both isomorphic to A2, for which pi(U) is contained in V
and pi restricted to U is everywhere etale. In fact no A2 open of X avoids
the particular irreducible ramification curve E constructed below.

## 1. One global curve
For a double transposition g in G, its fixed locus in the distinct-point moduli
has exactly one curve C_g^o, irreducible. For g=(12)(34), conjugate the unique
nonidentity Mobius involution implementing g to z->-z. Put marked point 5 at
infinity and point 1 at 1. The ordered configuration is then
(1,-1,t,-t,infinity), with t avoiding 0,1,-1 and infinity.
Conversely these configurations are fixed, and this parameterization is
surjective onto that fixed locus. The same argument applies after relabeling.
Write C_g for its irreducible closure in S.

Of the 15 double transpositions in A5, three lie in H and 12 do not.
For g outside H, its centralizer in A5 is a Klein four group fixing the unique
label fixed by g, which is not label 5, and acting regularly on the other four.
Consequently C_H(g) is trivial. Thus the 12 elements outside H form one
H-conjugacy orbit, and all their curves have the same irreducible image E in X.
We will verify ramification along E locally, without assuming that all boundary
fixed loci have been classified or that every configuration has generic stabilizer.

## 2. The pentagon and its local quotient
Take p to be the ordered five fifth roots of unity. Rotations and inversions
give a dihedral subgroup D5 of order 10 in its G-stabilizer; all these label
permutations are even. This is the full G-stabilizer. Indeed D5 is maximal in
A5 (orders 20 and 30 are excluded by simplicity and index-three/index-two
permutation actions). A5 cannot preserve a five-point set on P1: its point
stabilizer would be A4, whereas a finite subgroup of PGL2 fixing a point is
cyclic. The latter follows by conjugating to affine maps, averaging to obtain
a second common fixed point, then conjugating to multiplicative maps.
The H-stabilizer of p is the unique reflection s fixing label 5, of order two.

Finite-group linearization at the smooth point p identifies the completed
local action with its faithful tangent representation. Faithfulness follows
because a finite-order automorphism with identity tangent action is formally
the identity. The two-dimensional faithful D5 representation is irreducible:
every one-dimensional representation kills the order-five rotations.
Thus, after choosing coordinates and a generator, it is
r(u,v)=(zeta*u,zeta^(-1)*v), s(u,v)=(v,u), with zeta primitive of order five.

At q, the image of p in X, quotient coordinates are c=u+v, d=u*v.
At its image in Y they are a=u*v, b=u^5+v^5. Both quotients are smooth there.
The map on completed local rings is the map represented by
  (c,d) -> (d, c^5-5*c^3*d+5*c*d^2).
Its Jacobian determinant, up to sign, is
  5*(c^4-3*c^2*d+d^2).
The two distinct branches of its critical divisor are
  d=((3+sqrt(5))/2)*c^2,  d=((3-sqrt(5))/2)*c^2.
They are smooth and tangent, not an ordinary node.

Upstairs these are the four reflection axes other than that of s, paired by s.
Each such reflection belongs to G outside H. Its local fixed branch is a
branch of the corresponding C_g, since p lies in the distinct-point moduli.
Section 1 therefore puts BOTH critical branches on the SAME global irreducible
curve E. In particular E is a ramification curve and is locally multibranch
at the smooth point q of X. Additional ramification components are irrelevant.

## 3. The affine-plane boundary obstruction
Lemma. If X0 is a normal projective surface and E0 an irreducible curve having
at least two branches at a smooth point q0 of X0, no open A2 in X0 can have
E0 entirely in its complement.

Proof. Suppose U0 is such an open. Resolve X0 and its boundary outside U0,
including an embedded resolution of E0 at q0. In the resulting SNC boundary,
the strict transform of E0 attaches at least twice to the connected exceptional
tree over q0. These attachments and that tree create a cycle in the dual
multigraph. Further boundary blowups subdivide edges or attach leaves, and
cannot remove the cycle. On the other hand, take a common smooth resolution
with P2 which is the identity on U0=A2. Viewed over P2 it is obtained by
blowups supported over the line at infinity. Its boundary dual graph is a
tree: initially one vertex, with each blowup only subdividing an edge or
attaching a leaf. This contradiction proves the lemma.
Imports here are standard characteristic-zero surface resolution, resolution
of birational maps of smooth surfaces by point blowups, and finite-group
linearization; no classification of all affine-plane completions is used.

If pi|U were etale, U could not meet E: any nonempty open intersection would
meet its generic ramification locus. Thus E would lie in X\U, contradicting
the lemma at q. This proves the stated single-cover obstruction.

## Provenance and limits
The moduli/del Pezzo identification and natural S5 action are checked against
Bauer--Catanese, "S5-equivariant syzygies for the Del Pezzo surface of degree 5",
arXiv:1812.10715v3 (4 February 2020), selected PDF text on pages 1--2 and 5;
https://arxiv.org/pdf/1812.10715 . The web wrapper mislabels this PDF as
"Rigidity of the Kummer covering"; the actual PDF header has the title above.
Only these selected passages, not the full paper, were inspected. A page-1
screenshot failed with cache miss; no screenshot-based claim is made.
An independent Dolgachev--Iskovskikh author-PDF retrieval failed (500) and
is UNREAD; no statement here is attributed to that failed retrieval.
The D5 calculation, global curve argument and boundary application are ROOT's
manual synthesis. Novelty is unknown. No CAS, formalization or model experiment.
Earlier linear quotient and marked-pair quintic-chart obstructions are not
replaced or broadened. No claim for other covers, arbitrary birational target
changes, rationality of a general Galois closure, or actual Keller normalization.

OPEN(S) RAISED: None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `8e495d13faed71fb03966b2f7e297c41bdf8ee1c` (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6821`.
- Body SHA-256:
  `71b16dbf467ad4465f59a3ea6fb4fd77218cc541655f989266dbafcb35820abe`.
- Frozen basis: `8e495d13faed71fb03966b2f7e297c41bdf8ee1c`.
