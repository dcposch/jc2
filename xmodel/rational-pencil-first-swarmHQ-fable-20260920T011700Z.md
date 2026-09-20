# FIRST hostile review: rational polynomial pencils preserved by Keller maps

Reviewer: swarmHQ FIRST seat (requested Fable5.1 effortmax; hosted identity
not independently attested). Date: September 20, 2026 UTC.
Reviewed contribution commit: 44652539d4099119b4dfdd1c5ba0059c382d4f7c
(parent is the producer basis fcf9df1d0c9260ec16e936568af842ee77cf3c97;
the commit adds exactly the two charged root files).
HQ governance basis: 87eee86e1f681d2025b9e8a28862ccdd36653aad (resolved once).
Evidence: MANUAL hostile review; no CAS, computation, network or delegation.

STATUS: COMPLETE (author completion measured at the end of this file). The
partial save landed at 01:29:27 UTC, about two minutes after the 01:27
checkpoint, because one apply_patch call omitted its terminator line; the
early DRAFT/INCOMPLETE was written at 01:20 UTC after two rejected forms.

## 1. Verdicts

| Attack | Verdict |
| --- | --- |
| 1. Generic finiteness over C(t)/Kbar, descent, denominator clearing | CONFIRMED |
| 2. Cohomological smooth-P1 fiber components | CONFIRMED |
| 3. Nonproper components, one puncture, no-A1, degree one | CONFIRMED, conditional on the two named Jelonek/Chau imports at statement scope |
| 4. Non-Keller control, same-pencil necessity, exclusions | CONFIRMED |

Overall: the Section 1 conditional theorem of the producer report is
CONFIRMED at its stated scope with its named imports. It produces no h for
an arbitrary Keller map and resolves nothing about JC2. Novelty is not
certified here (ROOT scope).

## 2. Attack 1: generic curve maps are finite

Reconstruction. Let s=h(x,y) on the source and t=h(u,v) on the target;
h composed F=psi(h) gives t=psi(s), so F carries the fiber psi(h)=t into
the fiber h=t. With K=C(t), the target generic fiber is Spec(A tensor_{C[t]} K)
and the source generic fiber is Spec(B tensor_{C[t]} K) with t acting as
psi(h(x,y)); the latter is S^-1 B for S the nonzero polynomials in the
target h pushed through F*. Over Kbar, psi(s)-t is irreducible and separable
over K (characteristic zero, t transcendental), so it has d=deg(psi)
distinct roots s_i, each transcendental over C. Then
B tensor_{C[t]} Kbar = product_i (B tensor_{C[s], s->s_i} Kbar): a disjoint
union of d copies of the geometric generic h-fiber. Relative algebraic
closedness of C(h) makes that fiber geometrically integral, so each copy is
P1 minus n points with the SAME n as the target fiber (n is the number of
places at infinity of the geometric generic fiber, independent of the
embedding of C(s) into an algebraically closed field). n>=1 because an
affine curve is not complete.

Etaleness (det DF=c in C*) is stable under base change, so F_Kbar is
quasi-finite and each component maps nonconstantly. Each restriction
f:P1-S_source -> P1-S_target extends to fbar of degree k>=1 with
fbar^-1(S_target) contained in S_source. Checked cases: n=1 gives a
polynomial map A1->A1 (finite); n=2 gives a regular map Gm->Gm whose
coordinate is a unit of Kbar[z,1/z], hence a z^m with m!=0 (finite);
n>=3: Riemann-Hurwitz gives total ramification 2k-2, while ramification
over S_target is kn-|fbar^-1(S_target)|>=kn-n, so (k-1)(n-2)<=0 and k=1;
equal cardinalities force fbar(S_source)=S_target, an isomorphism of affine
curves. A finite disjoint union of finite maps is finite, and finiteness
descends along the faithfully flat Spec Kbar -> Spec K. So S^-1 B is a
finite S^-1 A-module. This is generic finiteness only; it says nothing yet
about properness of F on A2. CONFIRMED.

Denominator clearing (producer Section 3). x and y satisfy monic equations
over S^-1 A; the finitely many denominators are polynomials in the target
h, so one nonzero q(t) makes x,y integral over A[1/q(h)]. Since
B[1/q(h composed F)] = A[1/q(h)][x,y] (the inverted element is the image
of the base inverse, and P,Q lie in C[x,y]), it is a finite
A[1/q(h)]-module. Hence F^-1(U)->U is finite for U={q(h)!=0}, so F is
proper at every point of U and the nonproper value set A_F lies in the
finite union of fibers q(h)=0. An irreducible curve inside a finite union
of irreducible curves equals one of them, so each component of A_F is an
entire reduced irreducible component of some h-fiber. The distinction
between fiberwise generic finiteness and global properness is kept
explicitly. CONFIRMED.

## 3. Attack 2: cohomological smooth-P1 components

Reconstruction. The base locus of the pencil [H:Z^m] on P2 is H=Z=0, on
the line at infinity; all blowup centers, including infinitely near ones,
lie over that line, so X contains the original A2 unchanged and
pi|_A2 = h. Stein: the generic fiber of pi is the generic fiber of h,
geometrically integral by relative algebraic closedness (char 0 gives
separability), so the finite part of the Stein factorization is birational
onto the normal P1, hence an isomorphism, and pi_* O_X = O_P1. A general
closed fiber G is smooth (generic smoothness), connected, and has genus
equal to the generic fiber's genus 0 (pi flat, Euler characteristic of
fibers constant), so G is P1.

Step check, each verified: D=pi^*(c) is an effective Cartier divisor,
possibly nonreduced; D~G because any two points of P1 are linearly
equivalent; G nef because an irreducible curve C' either differs from G
(proper intersection, C'.G>=0) or equals G (G^2=0); adjunction on the
smooth G gives K_X.G=-2; (K_X+D).G=(K_X+G).G=-2; an effective divisor has
nonnegative intersection with the nef G, so H^0(O_X(K_X+D))=0; Serre
duality on the smooth projective surface gives H^2(O_X(-D))=0;
H^1(O_X)=0 because X is an iterated point blowup of P2; the sequence
0->O_X(-D)->O_X->O_D->0 gives H^1(O_X)->H^1(O_D)->H^2(O_X(-D)), so
H^1(D,O_D)=0. For C a reduced irreducible component with its reduced
structure, O_D->O_C is surjective with kernel a coherent sheaf supported
in dimension <=1, so H^2 of the kernel vanishes (Grothendieck vanishing)
and H^1(O_D) surjects onto H^1(O_C). With H^0(O_C)=C (reduced, irreducible,
projective over C), p_a(C)=0; the normalization formula
p_a=g(normalization)+sum of delta invariants forces g=0 and all delta=0,
so C is normal, hence smooth, hence P1. Every reduced irreducible component
Z of the affine fiber h=c has closure an irreducible curve inside D_red,
hence equal to some C, and Z=C intersect A2, an open subset of a smooth
curve. No relative-minimal model, section, Tsen, or C-star classification
is used; multiplicities never enter. CONFIRMED.

## 4. Attack 3: nonproper components and degree one

Reconstruction. Let D be a component of A_F. By attacks 1-2, D is an
entire reduced irreducible h-fiber component, smooth, and D=C intersect A2
with C isomorphic to P1; T=C-D is finite and nonempty because a closed
curve in A2 is affine, not complete. Jelonek's theorem (import) supplies a
nonconstant polynomial map phi:A1->A2 with image in the closed set D, so
a nonconstant morphism A1->D. If |T|>=2, pick a coordinate z on C with
two points of T at 0 and infinity; z and 1/z are regular on D, their
pullbacks are mutually inverse elements of C[t], hence constants, so phi
lands in one point of C, contradiction. So |T|=1 and D is isomorphic to
A1 as an abstract curve, exactly the object excluded by the Keller no-A1
component theorem (import, statement scope). So A_F is empty and F is
proper. Proper plus quasi-finite gives finite; finite etale onto A2 with
connected source is a finite etale cover; A2_C is simply connected, so the
degree is one; a finite birational morphism onto the normal A2 is an
isomorphism. CONFIRMED conditional on the two imports exactly as named. I
did not audit the imports' proofs or read the cited arXiv paper (no
network; out of scope); I only checked that they are applied at the scope
the producer states: a dominant polynomial plane map with nonempty A_F,
and a Keller map's A_F component isomorphic to A1.

## 5. Attack 4: control, same-pencil necessity, exclusions

Control F=(x,xy), h=x, psi=t: h composed F=x, generic fiber map
(s,y)->(s,sy) is an isomorphism for s!=0 (attack 1 passes), det DF=x is
not constant, and A_F is the line u=0 (limits of (1/k, vk)), a smooth A1.
So attacks 1-2 alone never give properness; the no-A1 import is the only
place the Keller hypothesis enters beyond etaleness. Verified.
Same pencil: the n>=3 count uses |S_source|=|S_target|; two different
polynomials h1 composed F=psi(h2) give unequal puncture counts and the
inequality (k-1)(n_t-2)<=n_s-n_t no longer forces k=1. Necessity as a
proof ingredient is real; the report does not claim the theorem is false
for different pencils, which is correct. Verified.
Exclusions checked: rational h with affine base points (blowups would
alter A2, Section 4 does not transfer); no split Gm coordinates, no
coordinate h, no reduced-fiber or submersion assumption are used; c is
used only for etaleness; deg(psi)>=1 is automatic since F is dominant and
h nonconstant; deg(psi)=1 is allowed (d=1). No hidden hypothesis found.
CONFIRMED.

## 6. Minor exposition notes (nonbinding)

- Section 4 asserts the general closed fiber is P1 without saying why its
  genus equals the generic one; constancy of the Euler characteristic in
  the flat family pi (or specialization) is the missing half-line.
- Section 5 should say D is isomorphic to A1 as an abstract curve; the
  no-A1 import is applied to that abstract statement.
- The cited primary paper's own main results may overlap this theorem;
  ROOT owns intake and novelty, and I make no novelty claim either way.

## 7. Imports, scope, limitations

Imports used, all standard characteristic-zero scope: resolution of pencil
indeterminacy by point blowups; Stein factorization; generic smoothness;
adjunction and Serre duality on smooth projective surfaces; invariance of
H^1(O) under point blowups; Grothendieck vanishing above support
dimension; normalization genus formula; Riemann-Hurwitz; fpqc descent of
finiteness; proper+quasi-finite=finite; simple connectivity of A2_C;
finite birational onto normal is an isomorphism; Jelonek nonproper-set
parametrization; Keller no-A1-component theorem (Chau) at statement scope.

Read scope: whole-read of the seven charged snapshots (hashes verified
pre-read, all seven matching; post-read check recorded below) and of the
four frozen HQ documents via git show at 87eee86 (hashes matching).
APPROACHES.md was clipped once by the tool and re-read in two halves.
No STATE, other-seat report, source discovery, history search, network,
jc2-lean or jc2-web access. Only the two authorized outputs were written;
the startup ACK is chmod 444. apply_patch rejected the stdin-heredoc and
plain-argument forms; the argument form with a trailing newline succeeded
and was used for every authored edit. No memory, index, settings, notes,
credential, shared-doc or Git mutation was performed. Hosted model identity
is not attested by me. Same-model Astra co-check was not used as evidence.

## 8. Read manifest

- /tmp/jc2-lane.MuaPeM/inputs/README.md 7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf
- /tmp/jc2-lane.MuaPeM/inputs/AGENTS.md 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f
- /tmp/jc2-lane.MuaPeM/inputs/COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
- /tmp/jc2-lane.MuaPeM/inputs/APPROACHES.md 9939d0091bdad87f6d2a8959b4a7e33653a04ef567190cb64f80f5dedd3bb395
- /tmp/jc2-lane.MuaPeM/inputs/FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
- /tmp/jc2-lane.MuaPeM/inputs/rational-polynomial-pencil-swarmHQ-root-20260920T011100Z.md f06a1d0c931f1e7270f6b63132dbfd5b01588928e0f9e5e2ee8f115665367e88
- /tmp/jc2-lane.MuaPeM/inputs/rational-polynomial-pencil-swarmHQ-root-20260920T011100Z.md.artifact.json f96995f75d6a28c9f9be26d7dab54f584f12168bf9df338509e610ee54e6f91a
- swarmHQ 87eee86:AGENTS.md 06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f
- swarmHQ 87eee86:POLICY.md 29d6bcea7ed4fa1031846705c765ce27f487f76ea330c6312cbad6ca38c42393
- swarmHQ 87eee86:RESEARCH_POLICY.md 710fcf0c3b2bfca649677365fb4094b6527f172981016696ee67095fca910778
- swarmHQ 87eee86:RUNBOOK.md 67f2cbffb19b407f7c9094de193f43ba28fd4c960b9509745d4c007b73557c81
- Post-read hash check at 01:29:34 UTC: all seven charged inputs MATCH the
  expected SHA256 values (pre-read check at about 01:19 UTC also matched).
- Producer body check: bytes through the standalone BODY-END line hash to
  54e8fb878663ac88bb81ac068c96323c28fc4a8c9db6b46cb17f13fd8f7fb08a,
  12125 bytes, matching the producer seal and the artifact JSON.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

## 9. Completion

Review outcome: all four attacks CONFIRMED; no REFUTED or GAP item. The
conditional theorem is sound at its stated scope with the named imports,
and supports PROMOTED/MANUAL integration by ROOT with those imports
recorded; that integration decision is ROOT's, not mine. The trusted
collision checker run on this report alone (bounded, 01:30 UTC) returned
the EMPTY block above. Whole author readback of this report was completed
before this section was written. No seal or finalize step is performed
here; the legacy parent handles custody.

Author completion (measured): 2026-09-20T01:30:31Z

<!-- BODY-END -->
