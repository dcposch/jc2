# Co-research: all target lines in the explicit Kulikov net

ROOT assignment2026-09-12 00:07UTC. Original reserve00:24/HARD00:27UTC,
never reset. Record actual first action. This TASK is the ONLY input;
current-pin before FRESH WHOLE read. No corpus/web/linked input.
ROOT proposals below are UNREVIEWED: derive or break, not promotion.

Question: a known non-plane degree-three etale donor may look like a short
route to a plane counterexample. Does EVERY target-line version below
instead admit a nonzero logarithmic two-form, thereby excluding ANY dominant
morphism A2 -> donor? This would stop this exact construction family,
not arbitrary JC2 or all cubic covers. Include special/reducible conics;
a generic-line argument alone is insufficient.

Let P=(1:1:1) in P2 with coordinates (X1:X2:X3), W=Bl_P P2=F1.
Put Qi=3Xi^2-X1X2-X1X3-X2X3, i=1,2,3. These define a morphism
phi:W->P2 after removing the one simple base point. Expected finite degree3
from the ample basepoint-free divisor2H-E. Its ramification divisor is
the strict transform Rbar of

    R=sum_(i!=j) Xi^2 Xj-6X1X2X3.

For alpha=(a,b,c)!=0, Qalpha=aQ1+bQ2+cQ3 and Lalpha is the corresponding
target line. Let Calpha=phi^*Lalpha (the TOTAL scheme pullback on W), and

    Xalpha=W minus (Rbar union support(Calpha)).

No affineness or simple-connectedness need be assumed to prove non-domination.
On Xalpha, phi is etale to P2-Lalpha=A2 if the asserted ramification checks.

Proposed exact coordinate calculation. Set u=X1-X3,v=X2-X3,w=X3,
q=u^2-uv+v^2. Then

    R=2w q+uv(u+v).

Rbar is a smooth section of the ruling pi:W->P1_(u:v), of class3H-2E.
On its dense chart w=-uv(u+v)/(2q),

    (Q1,Q2,Q3)|R = (3/q)*(u^2(u-v)^2,v^2(u-v)^2,u^2v^2).

Thus intersection with Calpha is controlled by the homogeneous quartic

    Falpha=a u^4-2a u^3v+(a+b+c)u^2v^2-2b uv^3+b v^4.

This is never zero and NEVER a fourth power of a linear form. Comparing
u^4,u^3v and v^4,uv^3 would require simultaneously s=-r/2 and r=-s/2
for a putative (r u+s v)^4; cases r=0 or s=0 also fail. Hence its
squarefree homogeneous radical Balpha has degree r>=2.

Main ROOT proposed construction: choose any homogeneous N(u,v) of degree2
divisible by Falpha/Balpha, possible since deg(F/B)=4-r<=2. The rational
projective form

    theta = N(u,v)*Omega/(R*Qalpha),
    Omega=X1 dX2 wedge dX3-X2 dX1 wedge dX3+X3 dX1 wedge dX2,

is expected nonzero, regular on Xalpha, and logarithmic on a smooth SNC
completion of Xalpha. Homogeneous degrees are 2+3-3-2=0. Generic exceptional
order at P is >=0 when multP(Q)=1; when multP(Q)=2 it is -1, and E is then
part of Calpha and removed. Do NOT omit this exceptional case.

Useful logarithmic proof on v!=0, t=u/v. R and Qalpha are affine-linear
in w. Their determinant r1*q0-r0*q1 should equal6Falpha(t,1). Thus

    theta=(N/(6Falpha))*dt wedge dlog(R/Qalpha).

The base one-form eta=N dt/(6Falpha) has only simple poles on the roots
of Balpha. Choose base infinity outside those roots to avoid spurious
infinity issues. Globally use R/(v Qalpha); its divisor on W is
Rbar-Calpha-F_infinity. Extra vertical fibres in the logarithmic
calculation are not automatically removed from Xalpha: verify theta is
regular at their generic points and that any needed blowups have centres
in the actual boundary. A wedge of logarithmic one-forms on an SNC
refinement is logarithmic. The local model with two sections z=0,z=t^k
has required numerator order k-1, and k if their fibre is also removed.

Check every Qalpha: its symmetric matrix has determinant
27abc-(a+b+c)^3, up to harmless scalar. There is no rank-one conic.
If a=b=c, Q is a scalar*q(u,v), and Calpha=E+two ruling fibres. Other
reducible Q is a line through P plus a line not through P, giving a
fibre plus a section. Their node must lie on ramification. It may be
cleaner to use the logarithmic-form identity uniformly instead of a
complete contact classification. Guard against tangencies and triple points.

Proposed conclusion from theta: there is NO dominant morphism A2->Xalpha.
Given one, resolve its rational extension from P2 to an SNC completion of
Xalpha using blowups outside A2. Pullback theta is nonzero (characteristic0,
dominant equal dimensions), polynomial on A2, and at most logarithmic along
its boundary. At the generic point of the original infinity line it has
at most a simple pole. But a nonzero polynomial form f(x,y)dx wedge dy
has pole order deg(f)+3 there. Contradiction. Explain the log pullback
inclusion and why resolution changes no generic infinity valuation.
No classification or external log-Kodaira theorem is needed if this works.

Give the strongest true exact conclusion even if one special alpha fails;
do not label a merely generic proof ALL. ROOT separately checks primary
history and strategy overlap. No novelty claim, no all-source theorem.

Write xmodel/kulikov-all-lines-log-obstruction-astra-20260912.md through
artifact_finalize begin/close/finalize/expected verify, basis
0d39df3c9fd69c939a8420c54d03228b9077777d; own box PINS/custody only.
Target <=2300words excluding custody; bounded writes<1500words. Own WHOLE,
pins, quantity/cheapest-test/scope/collision check before BODY-END LAST.
No new canonical OPEN. Cheapest test manual <=20min UNMEASURED.
Terminal handoff only ALL WRITERS IDLE, custody/report/manifest pins and times.
No scientific code/import/AST/tests/dummy/CAS, AWS/SSH/process/Git control,
protected project/mirror, outside input, new agent, Fable, shared changes,
automatic descendant or unreviewed promotion.
