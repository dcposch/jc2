# Cubic-scroll donors: a complete source obstruction on F1

ROOT, September12 2026. MANUAL / UNPROMOTED candidate and integration.
Original own reserve00:35/HARD00:38UTC; basis
0d39df3c9fd69c939a8420c54d03228b9077777d. JC2 remains unresolved.

## Exact claim and why this test was selected

Let W=F1 be the blowup of P2 at one point. For ANY finite morphism
phi:W->P2 of geometric degree3 and ANY target line L, set

    X(phi,L)=W minus (support(Ram(phi)) union support(phi^*L)).

Claim CUBIC-SCROLL-DONOR-1: there is NO dominant everywhere-defined
morphism A2->X(phi,L). In particular a plane Keller map cannot factor
through this etale donor, even with a first leg of arbitrary degree.
The claim covers every net and every target line on this fixed surface;
it is not an assertion about all finite cubic maps on other surfaces,
all cubic block quotients, arbitrary target open embeddings, or all JC2.

The classical Kulikov example supplies a nontrivial etale map from a
different rational affine surface to A2. Trying to find a first leg from
A2 is a concrete possible construction route. The old campaign check
only recorded its generic Euler characteristic4; special target lines
could not be discarded by that generic computation. Here the entire
fixed-compactification donor family is tested, including a second net
type with a double-root degeneration.

## 1. Exhaustive reduction to two net types

Write E for the negative section of W and f for a ruling fibre, with
E^2=-1, E.f=1, f^2=0. The ample divisor D=phi^*O_P2(1)=aE+bf has
a>0 and b>a. Since D^2=deg(phi)=3,

    a(2b-a)=3.

The alternative a=3,b=2 is not ample. Thus D=E+2f=2H-E.
Every such morphism is given by a three-dimensional basepoint-free net
of conics through P=(0:0:1), in coordinates(u:v:w).

Restriction to E has rank2: rank1 would give a common zero of the three
sections of O_E(1). After a target change the conics have the form

    Q1=wu+q1(u,v), Q2=wv+q2(u,v), Q3=q3(u,v)!=0.

The nonzero binary quadratic q3 has either two distinct roots or a double
root over C; the root at infinity is included. Source GL2 changes and
w-shifts by a linear form are projective automorphisms fixing P, so lift
to W. Target combinations preserve the complete family of target lines.

If q3 has distinct roots, arrange q3=uv. Subtract its multiples from
Q1,Q2 and shift w to obtain

    Q1=wu+a v^2, Q2=wv+b u^2, Q3=uv, a*b!=0.

If a or b vanished, an additional base point would remain. Scaling u,v,w
and the target coordinates makes a=b=1: choose (scale(u)/scale(v))^3=a/b.
Consequently this is a single source/target equivalence class. The explicit
Kulikov net in section2 belongs to it, since the unique combination with
zero linear part at P is a squarefree binary quadratic.

If q3 has a double root, arrange q3=u^2. Removing u^2 terms and shifting
w gives

    Q1=wu+C v^2, Q2=wv+G v^2, Q3=u^2, C!=0.          (1)

Here C=0 would leave a base point on u=0. Both types genuinely define
basepoint-free systems on W; their divisor is ample, so the resulting
proper morphisms are finite of degree3. No double-root stratum is omitted.

## 2. Squarefree type: every target line has a log-form obstruction

Use the equivalent classical coordinates P=(1:1:1) and

    Qi=3Xi^2-X1X2-X1X3-X2X3.

The common base point is P alone, with full-rank linear parts. The
homogeneous Jacobian determinant is -36R, where

    R=sum_(i!=j)Xi^2 Xj-6X1X2X3.

Its strict transform Rbar is the full ramification divisor. Put
u=X1-X3, v=X2-X3, w=X3 and q=u^2-uv+v^2. Then
R=2wq+uv(u+v); Rbar is a smooth section of the ruling. For target
line coefficients alpha=(a,b,c), the intersection with its full pullback
Calpha is the homogeneous quartic

    Falpha=a*u^4-2a*u^3v+(a+b+c)*u^2v^2-2b*u*v^3+b*v^4.

This follows by substituting w=-uv(u+v)/(2q): the three conics become
(3/q)*(u^2(u-v)^2,v^2(u-v)^2,u^2v^2). No nonzero alpha gives Falpha=0.
Nor can Falpha be a fourth power: coefficient comparison for
lambda*(r*u+s*v)^4 forces s=-r/2 and r=-s/2 when both are nonzero;
each zero case also contradicts the adjacent coefficient. Its homogeneous
radical Balpha therefore has degree at least2.

Choose a nonzero binary quadratic N divisible by Falpha/Balpha, possible
because deg(Falpha/Balpha)<=2. The homogeneous rational two-form

    theta=N(u,v)*Omega/(R*Qalpha),
    Omega=X1 dX2 wedge dX3-X2 dX1 wedge dX3+X3 dX1 wedge dX2

is regular on X(phi,Lalpha) and logarithmic on an SNC completion.
Here is the needed degeneration control, not merely a generic-line claim.
On v=1 the determinant of the two affine-linear fibre equations R,Qalpha
is6Falpha, so

    theta=-N/(6Falpha) dt wedge dlog(R/Qalpha).

The base differential has only simple poles at the distinct roots of Balpha.
Globally R/(v Qalpha) has divisor Rbar-Calpha-F_infinity; its logarithmic
differential is legitimate, and wedging with a base differential removes
the change of local trivialization. Resolve the actual boundary together
with these extra vertical fibres. Outside the actual boundary those fibres
are disjoint smooth curves, so all necessary blowups have centres in the
actual boundary. The log wedge has at most simple poles on this refinement.
At any unremoved strict fibre theta was already regular by its original
formula; no artificial deletion of that fibre is allowed or needed.

At E the numerator has order2. If Qalpha has multiplicity1 at P, theta
has order0 there. If its multiplicity is2, the order is -1 but E belongs
to Calpha and is removed. No rank-one conic occurs in this net; reducible
Calpha is either a fibre plus a section, or E plus two distinct fibres.
Thus no doubled boundary component invalidates the logarithmic argument.

For completeness, reducible cases also have a shorter obstruction. For
Calpha=F+M, the class relation Rbar=2F+M supplies a nonconstant unit with
divisor Rbar-2F-M. In the E+F1+F2 case the ratio of the two fibre equations
is a nonconstant unit. These cases cannot receive a dominant A2 morphism.

If a dominant A2->X existed, resolve its extension from P2 to the SNC
completion by blowups outside A2. Pullback of theta is nonzero in
characteristic0 and logarithmic along the source boundary. On A2 it is a
polynomial form h(x,y)dx wedge dy. Its pole at the generic point of the
original infinity line is deg(h)+3, at least3, whereas a log form has
pole order at most1. Blowups at boundary points do not change that generic
valuation. This contradiction proves the squarefree case for every line.

## 3. Double-root type: the whole etale locus and its units

For (1), the ramification is the ruling fibre f0={u=0} plus the section

    R1={wu+2Guv-2Cv^2=0}.

There is no E component. Over the base chart u=1 the fibre coordinate w
includes infinity, namely E. Removing R1 gives the full affine coordinate

    r=1/(w-2Cv^2+2Gv).

Hence W-(f0 union R1)=A2_(v,r), including E-f0 as r=0. The morphism is

    [1+r(3Cv^2-2Gv): v+r(2Cv^3-Gv^2): r].

For an arbitrary target line, its pullback is

    L(v,r)=alpha+beta*v
      +r[alpha(3Cv^2-2Gv)+beta(2Cv^3-Gv^2)+gamma].

It cannot be a constant: then beta=0 and the r coefficient is zero, which
forces alpha=0 because C!=0, and then gamma=0. Nor is it identically
zero for a nonzero line. Thus X(phi,L) is exactly the principal open D(L)
in this A2, with a nonconstant unit L. A dominant A2->D(L) would inject
function fields but pull L back to a constant unit, impossible. This proves
the double-root case and completes the two-case implication.

## 4. History, source boundary and decision

The generic donor and its rational degree-three morphism are classical:
see [Adjamagbo's account of Kulikov's construction](https://arxiv.org/pdf/1210.5281),
construction and Theorems1--2. ROOT read those selected passages, not the
whole original Kulikov paper. Generic affineness, factoriality, simple
connectedness and fundamental-group statements are not needed for the
non-domination proof. Special target lines are handled here explicitly,
not imported from a statement restricted to a generic conic.

The campaign already recorded the generic donor and chi=4 in
[Bass annihilator selection](bass-annihilator-selection-root-20260911.md),
SHA8365376e7148c936d87ae7333dcfe2c55116ecb9d02e540a410f69dbe51245f4,
read WHOLE. The general morphic first-log-plurigenus obstruction is already
promoted in AUDIT's August30 03:46 entry; it is not a new proof mechanism.
The present contribution is the all-line attachment, the exhaustive net
split and its second-case unit obstruction. No corpus-wide novelty claim.

The branch-type dichotomy is also classical. ROOT separately read section4,
Propositions12--13 and the beginning of4.2 in Ciliberto--Miranda,
[Non-cyclic triple planes with branch curve of degree at most10](https://www.math.colostate.edu/~miranda/preprints/TripleplanesJ.pdf).
They describe the tricuspidal-quartic and cuspidal-cubic-plus-flex-line
alternatives on the smooth cubic scroll. That selected primary comparison
supports the history check, not a new all-line theorem imported from it.
The remaining paper and its classifications on other surfaces were not
audited; none is a premise of the explicit proof above.

This is a genuine complete exclusion of the stated donor family if the
proof passes independent review. It does NOT establish that an arbitrary
plane Keller normalization compactifies to F1 with a finite map to P2.
It also does not treat nonlinear changes of the chosen target affine open,
higher degree covers, other compactifications or the separate S/T source.
Those scope restrictions are part of the claim, not exceptions silently
removed from a universal JC2 proof. No counterexample has been produced.

Decision: do not fund a search for A2 first legs into this cubic-scroll
family. A different donor needs a genuinely different source geometry,
not just another target line or conic-net coefficient in the classified
family. One independent different-model gate is the intended promotion
step; same-family derivations alone do not enter AUDIT as proved.

QUANTITY: existence of a dominant regular A2 first leg into X(phi,L),
uniformly over finite degree-three morphisms on F1 and all target lines.
CHEAPEST TEST performed: manual net normal forms, quartic multiplicity,
logarithmic two-form and explicit affine/unit charts. No scientific
subprocess, enumeration, coefficient payload or measured compute runtime.
COLLISIONS: classical Kulikov donor and known log/units obstructions;
all-line/two-net attachment checked separately. No new canonical OPEN.

## Terminal co-research intake

Both independent Astra tasks are COMPLETE with all writers idle. ROOT
collected terminal custody FIRST, checked TASK/owned pins, read complete
reports/PINS/manifests, and obtained expected-basis/manifest VERIFIED.
These are same-model co-research checks, not the different-model gate.

[All-line logarithmic proof](kulikov-all-lines-log-obstruction-astra-20260912.md):
report fcd4a4991541d232066ee1154cbcc760aa8bad9e00589310dbd9d37e8a6456a0;
manifest d5cbb2d4f2ec5599ce39e6c2d70693a9beb0d8cca2e50be7077d142b21aca931;
custody 53702c12be39902f1d8660b9deea641b1ed5b99848afb96cef4f70cfb708fda4.
Actual00:07:47--00:18:48,661 author-wall seconds; original clocks met.

[Net classification and double-root chart](cubic-scroll-net-classification-astra-20260912.md):
report c9dca0f52fe4a26e45782fb6a70a7d12e8c7890110a74a7587e9e3d4278c1e32;
manifest 0fdc94f07b0adcec191caf213361089007b2571d781ad754cc4c6127f86c9954;
custody 0b4311fa6191e62e5b4192d9ab729156b9d02a356f6edfc514935852d9e9704e.
Actual00:13:37--00:20:16,399 author-wall seconds; original clocks met.
Its optional elimination of G strengthens the normal form but is not
needed by the arbitrary-G obstruction proved here.

Each task used its own frozen TASK, not the other report. ROOT's in-scope
algebra/orientation hints were independently derived; no peer-body input
was added. This integration uses both completed reports. Standard surface
resolution and divisor/logarithmic-form facts remain explicit mathematical
imports; no formal proof or fresh audit of those foundations is asserted.
Resource seconds above are not billing, token, CPU or rolling24h totals.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12183`.
- Body SHA-256:
  `37fd0cbf08d0839c04ef67fb40a09bc048e9a72746ef682b8fccb27aaa479cae`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
