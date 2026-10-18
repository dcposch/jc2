# Independent FIRST: the A5 pentagon chart obstruction

VERDICT: CONFIRMED / PROMOTED-MANUAL at the exact fixed-cover scope below.
REVIEWER: retained Sol5.6-assigned native seat affine_radial_first_sol56_2157.
Hosted model identity is unverified; no paid-adapter receipt is claimed.
AUTHORSHIP: ROOT transcribes the terminal independent review; ROOT produced the proof.
Reviewer verdict: 2026-10-18T22:21:55Z; ROOT received it by 22:22:07 UTC.
Frozen public basis: 99aaaeba0dac1e0e4c6cd64e58762f1e12aff438.

## Reviewed artifact and explicit imports

[Producer](a5-pentagon-chart-obstruction-swarmHQ-root-20261018T221810Z.md)
has 127 lines,7153 bytes,mode0444;full SHA256
1fc06a1cd68e1c4c2976322c32f4b9ed4f582c5af095f66eab918f4bf4759bb8.
Body6821 bytes,SHA71b16dbf467ad4465f59a3ea6fb4fd77218cc541655f989266dbafcb35820abe.
Its manifest is698 bytes,0444,SHA
28f9ea2b2ebf412f673592e5f922bd8f5c1f863aa10c97bad1b28e055cef4a0b.
The sealed producer's historical UNPROMOTED label is not rewritten; this
separate review supplies its promotion at precisely the following scope.

The imported identification is S=bar(M_0,5), the smooth degree-five del Pezzo
surface with label action S5. Standard finite-group linearization and
characteristic-zero surface resolution/factorization are also explicit imports.
ROOT checked selected Bauer--Catanese arXiv:1812.10715v3 passages, not a whole
paper. Reviewer did not independently browse sources and makes no source-audit
claim. The failed Dolgachev PDF retrieval is UNREAD and unused.

## Exact confirmed result

For G=A5 and its label-5 stabilizer H=A4, let X=S/H,Y=S/G and pi:X->Y.
There are no opens U in X,V in Y, each isomorphic to A2, with pi(U) contained
in V and pi|U everywhere etale. More strongly, a specific irreducible
ramification curve E cannot be contained in the complement of any A2 open of X.

## Independent mathematical checks

1. A double transposition has one fixed label. Its A5-centralizer is the V4
fixing that label and acting regularly on the other four. For one outside H,
the fixed label is not5, so the centralizer intersects H trivially.
The12 outside H consequently form one H-conjugacy orbit. Normalizing an
involution to z->-z gives the surjective configuration family
(1,-1,t,-t,infinity); each interior fixed locus is one irreducible curve.
The12 curves therefore have the same irreducible image E in X.

2. The fifth-root configuration has G-stabilizer D5. It contains rotations
and reflections, D5 is maximal proper in A5, and full A5 is impossible:
the stabilizer of a point in its five-point orbit would be A4, but a finite
PGL2 subgroup fixing a point is cyclic. The intersection with H is the
single reflection s fixing label5. Finite-group tangent linearization is
faithful, and a faithful2D representation of D5 is irreducible.

3. With r(u,v)=(zeta*u,zeta^(-1)*v),s(u,v)=(v,u), the invariants for H_p
are c=u+v,d=uv and those for G_p are a=uv,b=u^5+v^5. Hence both local
quotients are smooth, and the finite map is
  (c,d)->(d,c^5-5*c^3*d+5*c*d^2).
Its determinant is plus or minus5*(c^4-3*c^2*d+d^2), giving the two smooth
tangent branches d=((3+sqrt(5))/2)*c^2 and d=((3-sqrt(5))/2)*c^2.
The four reflections other than s produce these branches in pairs under s.
All four lie outside H; check1 puts both branches on the SAME global E.
Thus E is genuinely a generically ramified curve, multibranch at a smooth
point of X. No classification of all boundary fixed loci is needed.

4. On resolving a smooth multibranch point of one irreducible boundary curve,
its strict transform meets the connected exceptional tree at least twice.
Even when both contacts lie on one component, parallel edges give a cycle
in the dual multigraph. Further boundary blowups preserve this cycle.
An A2 completion, however, admits a common resolution with P2 which is the
identity on A2. Over P2 its boundary is the total transform of the line at
infinity, so point blowups make its boundary dual graph a tree. Contradiction.
Normality of X is sufficient: resolve singularities outside the A2 open;
the multibranch point used in the proof is already smooth on X.

5. If pi|U were etale and U met E, the nonempty intersection would be open
dense in irreducible E and meet its generic ramification locus. Therefore
E must lie in X\U, contrary to check4. This proves the exact statement.

## Gates and limits

Reviewer ACK22:21:08 verified codex,node,apply_patch,python3,git executable paths.
Whole-set metadata matched before body reads. Reviewer newly read frozen
HQ3f4ef799ec6da2cf1fcf9a8099d9a29dc8e64ca9:STATE1--204,RUNBOOK1--428,
RESTRICTIONS1--239,publicAPPROACHES1--932; other governing whole-reads reused
only at the reviewer's own exact pins. Producer1--127 and manifest were read
whole; artifact_finalize verify passed. Reviewer postpins/modes all matched.
No reviewer deviations,writes,network,CAS,descendants,Git mutation or protected
tree access. ROOT producer source/display deviations are recorded in the HQ
journal, not concealed by this clean reviewer receipt.

This is a single-cover obstruction, not an exclusion of other nonlinear
quotients, arbitrary birational target models, general Galois closures or
actual Keller normalization. No JC2 proof or counterexample results.
The method is manual, not formalized; novelty is unknown. No new OPEN is raised.

OPEN(S) RAISED: None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `99aaaeba0dac1e0e4c6cd64e58762f1e12aff438` (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5553`.
- Body SHA-256:
  `055a55a1774972020e28cc701d57710c4f8df191bb16386befa10dbe4aac1cce`.
- Frozen basis: `99aaaeba0dac1e0e4c6cd64e58762f1e12aff438`.
