# Boundary-contact constraints for an actual divisorial Keller compactification

Producer: swarmHQ ROOT/Astra. Date: October 25, 2026 (UTC).
Basis: `2ead4a746396b8a5ec0cb5793c3ef66658bae2b6`.
Evidence tier: MANUAL / CONDITIONAL; [independent hostile review](boundary-contact-review-swarmHQ-sol56-20261025.md).
Lifecycle: independently reviewed; the public evidence ledger records adoption.

The conclusions below assume the adopted [actual divisorial attachment](divisorial-keller-compactification-swarmHQ-root-astra-20261024.md)
and [projectivity package](divisorial-projectivity-swarmHQ-root-astra-20261025.md), including their named dependencies and the dynamical inequality lambda1>=N.
The map h on the whole marked polynomial source is the relevant Keller iterate; P,Q denote its coordinate polynomials.
The [marked-curve obstruction](marked-curve-lift-obstruction-swarmHQ-root-astra-20261025T151400Z.md) is an earlier special-filtration application of the local covering method.
These necessary conditions concern every index n in this adopted divisorial package. They do not settle the infinitely singular branch or JC2.

## Reviewed argument

1. Exact hypotheses and dependency boundary
Use the adopted ACTUAL divisorial package on fixed projective Y: U=Y\B is the whole marked A²;
B is an ordinary cuspidal rational curve, and Y is singular only at its cusp q.
Pic(Y)=Z[L], L~nB is ample Cartier, L.B=1 and B²=1/n.
For e=N^j>1, h:W→Y is finite degree e, k:W→Y is proper birational and the identity over U,
h*B=eC, both h_C and k_C identify C with B, C is Q-ample, and k*B=C+Z with Z≥0 exceptional.
The surfaces have rational singularities; C²=1/(ne). No W\C=U or target-map descent is assumed.
The existence step below names standard Serre vanishing and eventual global generation for coherent I_B;
these remain explicit conditional dependencies, not newly read external source proofs.
Covering/normal-extension and rational-fibre tools have the same conditional scope as the published marked-curve proof.

2. Candidate A: a canonical smooth boundary point
In fact it suffices that an integral curve D≠B has set intersection D∩B={p}⊂B_smooth;
one normalization place is not required for this first implication.
D avoids the sole singular point q of Y, so D is Cartier along its support and trivially Cartier off it.
Write D~lL. Ampleness gives l>0, and D.B=l. Restricting its section to B gives exactly the Cartier divisor l[p].
The cuspidal normalization sequence identifies Pic0(B) with (C,+): at the cusp the unit quotient is
the coefficient of u in C[[u]]* modulo C[[u²,u³]]*. Constants cancel in the global unit sequence.
Thus it has no nonzero torsion. The smooth-point Abel map identifies B_smooth with Pic1(B):
for points p,r the function (t−p)/(t−r) has first coefficient r−p at u=1/t, giving the additive parameter.
Let p0 be the unique smooth point with L_B=O_B(p0). Since O_B(lp)=L_B^l, torsion-freeness gives p=p0.
This fixes a point, not the number of curves, their normalization genus, tangency order, or singularity type.

3. Existence and ACTUAL fixation of p0, without formal algebraization or Bertini
Choose m≥2 sufficiently large that H1(Y,I_B⊗L^m)=0 and I_B⊗L^m is globally generated.
Lift the section of L_B^m with divisor m[p0] to a section s0 of L^m.
At p0 choose smooth coordinates with B=(u=0) and tangent coordinate v. A local equation of s0 is
v^m times a unit plus u g. Global generation supplies a kernel section s1=u g1 with g1(p0)≠0.
Choose a scalar c so s0+c s1 has nonzero normal derivative. Its effective divisor D_m is smooth and reduced at p0,
has intersection with B exactly m[p0], and avoids q. It contains no component B.
Every component of D_m meets ample B, hence every component would pass through p0.
Local smoothness therefore forces exactly one global component, with multiplicity one. D_m is integral.
Its normalization has exactly one infinity point. Its genus is unrestricted; no A1 parametrization is claimed.
Lift that normalization to W using proper k. At infinity its k-image is p0.
The polynomial coordinate functions of F|D_m cannot both extend across infinity: otherwise they are constant
on the complete normalization, contradicting quasi-finiteness of F on the affine curve.
Thus its h-image at infinity lies on B, and the lifted point is a=(k_C)^−1(p0) on C.
The image curve has no other boundary point, and that point is σ(p0), where σ=h_C∘k_C^−1.
It is smooth on B; candidate A forces σ(p0)=p0. The cusp q is also fixed by this curve automorphism.
This is a global section construction on the ACTUAL Y, not extension of a merely local invariant curve.
It also shows why A alone cannot force transversality of arbitrary one-place curves: D_m has contact m≥2.
That observation does not refute a stronger restriction on the special rational images h(E).

4. Candidate B: every exceptional contact is non-Cartier
The old AMPLE identity is C.Z=−Z²=(e−1)/(ne). Hence C.(nZ)=(e−1)/e<1.
Moreover nZ=k*(nB)−nC is an effective integral Weil divisor supported on all k-exceptional primes.
Its coefficient a_E is a positive integer: a local equation of the effective Cartier nB vanishes at k(E).
Every E meets C, because C is Q-ample; the set intersection is the singleton (k_C)^−1(k(E)).
If C were Cartier at that point, it would be Cartier on an open neighborhood of the entire chosen E:
away from that point the effective divisor C is absent, so O(C) is canonically trivial.
Its restriction to E is then a genuine line bundle with a nonzero effective section having a zero.
Thus C.E is a positive integer, also under the Q-Cartier definition of surface intersection.
All other terms in C.(nZ)=Σa_E(C.E) are positive. One Cartier contact would give C.(nZ)≥1, a contradiction.
Therefore C is non-Cartier at EVERY exceptional contact; the ambient W is singular there.
At a contact above a smooth target boundary point, h*B=eC is locally Cartier, so the local index of C divides e.
No bound independent of e, or assumption that E or W is smooth at the contact, is used.

5. Two centres, with no stabilization conclusion
The exceptional-P1 assertion can be proved inside the package. Resolve W by π:X→W;
rationality of Y and Leray give R1k_*O_W=0. For the reduced fibre F_p, the ideal sequence and
R2k_*I_Fp=0 (projective fibres≤1) give H1(F_p,O)=0. Quotienting to each reduced component E gives H1(E,O)=0.
Normalization genus plus defect length is zero, so E is intrinsically smooth P1 even if W is singular.
Its sole C-contact gives E\C=A1. Finite h maps E onto D≠B with exactly one boundary point.
The normalization of D has one place there: every such place has a preimage on E, and E has only one point above B.
If that boundary point is smooth, A makes it p0; otherwise it is q.
Since σ fixes both p0 and q and k_C,h_C are isomorphisms, EVERY k-exceptional centre lies in {p0,q}.
This neither bounds the number/depth of exceptional curves nor supplies a common finite resolution for iterates.
The old GLOBALCOUPLING stabilization gap is not reopened by support at two fixed points.

6. What the WHOLE polynomial source really supplies to the local cover
Suppose an exceptional contact lies over p0, and shrink a smooth target bidisc there.
Its reduced affine branch-image curves come from h(E); those through p0 may be distinct, singular or tangent to B.
The fibre over p0 is one point a, since h^−1(B)=C and h_C is an isomorphism.
Remove the FULL inverse of B and all these image germs. The resulting normal-germ cover is connected of degree e.
A B-meridian has permutation τ equal to an e-cycle, from the unique boundary extension with residue degree one.
For each irreducible affine image D°=(f=0), f(P,Q) is nonconstant and has a source curve T°.
Quasi-finiteness makes some T° dominate D°. Its closure T in W is finite onto the complete image D.
The finite map of normalizations covers every place of D over p0, and all corresponding points of T lie over a.
Since T is not a boundary component, each such branch is generically in U. Thus each selected D-branch near p0
has an ambient-étale U-preimage. Its meridian σ_β fixes at least one sheet of this same local cover.
This is an actual local fixed sheet, not a choice of compatible global labels; different meridians may fix different sheets.
If σ_β commuted with τ, it would lie in the cyclic centralizer of an e-cycle; a power of τ with a fixed point is identity.
If this commutation held for every affine branch meridian, their inertia would all be trivial.
The cover would extend unramified across those punctured branches, leaving only B; its connected cyclic cover
and unique normal finite extension are (s,t)↦(s^e,t). Then C would be Cartier at a, contradicting section4.
Consequently an ACTUAL exceptional contact over p0 requires a nontrivial branch meridian not commuting with τ.
The two-transverse-axis case is excluded, but multiple, singular and tangent branch configurations remain unexcluded.

7. Exact gap and discriminating next test — no successor launched
A/B, point fixation, and two-centre support do not control that commutator. Period classes and positive fractional
intersections are not relations in the local fundamental-group representation; no implication between them was proved.
The precise additional actual-source assertion would be [τ,σ_β]=1 for every reduced affine branch at p0.
Its test must concern the monodromy of the ACTUAL finite normalization of the Keller graph and use its global polynomial source;
fixed sheets alone, an abstract finite cover, a local index bound, or a mixed-image degree sum do not establish it.
A proof would exclude p0-centred escape via section6; a surviving actual noncommuting inertia identifies exactly the obstruction.
This is a falsifiable proposed discriminator, not an asserted theorem or authorization for another tranche.
Cusp-centred escape over q remains separate and is not tested by the smooth bidisc argument.
The final verdict is necessary constraints plus GAP, not a proof of JC2, a uniform degree bound, or a general no-go theorem.

## Provenance and limits

The seven sections above are byte-identical to lines 6–103 of the independently reviewed producer artifact
(full SHA256 `4b945bf26afcc4e587c737aea613ee77bd8b033b4f77cc879a376ce160ca646c`).
The fractional intersection identity and boundary Picard arithmetic were already available; the additional conclusions concern actual curves, contacts and centre support. No novelty claim is made.
Section 7's proposed commutation condition is a sufficient missing implication, not an executable test on an available actual Keller counterexample.
Noncommuting affine inertia, cusp-centred escape, and the lack of a uniform common resolution remain explicit gaps.
Standard Serre, rational-fibre and finite-cover extension tools retain their named conditional scope; no new external source verification is claimed.

The following is ROOT's actual generated collision output for the terminal producer source and the stated frozen public corpus.
Its EMPTY result concerns explicitly raised OPEN entries only; it does not establish novelty.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `2ead4a746396b8a5ec0cb5793c3ef66658bae2b6` (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11371`.
- Body SHA-256:
  `8dd0d1740bcd42c58cfe645dd1f922562dc43c4bceed4bc1ba6bd7ed09f5df4f`.
- Frozen basis: `2ead4a746396b8a5ec0cb5793c3ef66658bae2b6`.
