# All target lines in the explicit Kulikov net

Author: Astra geometry. MANUAL / UNREVIEWED attachment, not promotion.
First action2026-09-12 00:07:47 UTC; original reserve00:24/HARD00:27 unchanged.
Sole input TASK SHA5e6a1630bd7f838d9709ae13ab556553ebf3556e96e65a67e63076bb41c55d46,
current-pinned before fresh WHOLE. No external or linked source consumed.

## Whole net, ramification and all conics

Conclusion: over C, EVERY nonzero alpha has a nonzero logarithmic two-form
on an SNC completion of the exact Xalpha in TASK. Consequently no dominant
morphism A2 -> Xalpha exists. The general logarithmic obstruction is KNOWN;
this report independently derives its all-line attachment, not novelty or
promotion. Only standard smooth-surface resolution and divisor facts enter
besides the calculations below.

Write sigma=a+b+c and

    l=(2a-b-c)u+(-a+2b-c)v,
    A2=3au²+3bv²-sigma*uv,
    Qalpha=2lw+A2,   R=2wq+uv(u+v).

The common zero of the Qi is only P: their differences give Xi²=Xj²,
and the common equation then forces all three signs equal. At P, Q1,Q2
have independent linear parts 4u-2v and -2u+4v, determinant12. Thus one
blowup resolves the base scheme. The resulting system L=2H-E has square3
and intersects E by1, and every other irreducible curve dH-mE by2d-m>0.
It has no contracted curve, hence the proper morphism phi is finite of
degree3. Here m<=d is the elementary plane multiplicity bound;
basepoint-freeness at E follows from the two independent linear parts.

The homogeneous Jacobian is diag(6Xi) minus the rank-one matrix with every
row (X2+X3,X1+X3,X1+X2). Its determinant is -36R. The ramification class
on W is K_W-phi*K_P2=3H-2E. Off E its divisor is the strict transform of R;
that transform already has this class, leaving no exceptional component.
Thus ramification is exactly Rbar and phi is etale on Xalpha.

In blowup fibre coordinates (lambda:w), with (u,v)=lambda(U,V), the two
divisor equations after removing the fixed base multiplicity are

    Rbar: 2wq(U,V)+lambda*UV(U+V)=0,
    Calpha: 2l(U,V)w+lambda*A2(U,V)=0.

The two coefficients of the first equation have no common root on P1.
Consequently Rbar is a smooth section; its plane cubic is irreducible,
since it is primitive linear in w. This also verifies its class3H-2E.
Calpha here is the TOTAL pullback: if a=b=c, its equation includes lambda,
so Calpha=E+F1+F2, where F1,F2 are the distinct fibres q=0.

The symmetric matrix of Qalpha has determinant27abc-sigma³. A double
line would have multiplicity2 at P, forcing l=0, hence a=b=c; but then
Qalpha=3a q, which is not a square. Thus no rank-one conic occurs. Every
other reducible conic consists of one line through P and one not through P,
giving a fibre plus a section on W. Its node is on Rbar: a singular
pullback of a smooth target line cannot occur where phi is etale. Smooth
conics, these reducibles, and the exceptional equal-parameter case exhaust
all alpha. The following argument handles their contacts uniformly.

## Nonzero logarithmic form, including extra fibres

Put F=au⁴-2au³v+sigma*u²v²-2buv³+bv⁴. Direct expansion gives

    q*A2-uv(u+v)*l=3F.

This simultaneously verifies the stated restriction of the Qi to Rbar
and the determinant r1*q0-r0*q1=6F when R=r1w+r0, Qalpha=q1w+q0.
F cannot vanish identically: its extreme coefficients force a=b=0 and
then its middle coefficient forces c=0. Nor can F be a nonzero fourth
power. If F=k(ru+sv)^4 with rs nonzero, the adjacent extreme coefficient
ratios require s=-r/2 and r=-s/2, a contradiction. If r or s vanishes,
the opposite adjacent coefficient also rules out the putative power.

Let B be its homogeneous squarefree radical, of degree r>=2. Choose
nonzero homogeneous M of degree r-2 and N=(F/B)M, of degree2. Then

    eta = N(u,v)(v du-u dv)/(6F)

is a rational one-form on P1 with at most simple poles, supported on B.
This includes infinity: on u=1, v=s, it is -N(1,s)ds/(6F(1,s)).
Equivalently its local numerator cancels every root multiplicity except
one. No generic-root or squarefreeness assumption on F was made.

Define theta=N*Omega/(R*Qalpha). On v=1, t=u/v, the correct orientation is
Omega=-dt wedge dw. Hence the determinant identity gives

    theta = -pi*eta wedge dlog(h),   h=R/(v Qalpha).

This corrects the harmless plus sign in TASK. On that chart h=R/Qalpha;
globally its divisor is Rbar-Calpha-F_infinity. Indeed the total plane
pullbacks of R,Qalpha,v are respectively Rbar+2E, Calpha+E,
F_infinity+E, including the multiplicity-two conic case.

First theta is regular on the EXACT Xalpha, independently of this log
identity. Away E its only possible poles are Rbar and Calpha. Near P,
in w=1 with u=lambda*t,v=lambda, Omega=lambda*dt wedge d lambda.
The generic orders of N,R,Qalpha are2,2,k, where k=1 or2. Thus theta
has exceptional order1-k. For k=1 there is no exceptional pole; for k=2,
E is a removed component of Calpha. There is therefore no codimension-one
pole on Xalpha, so smoothness makes theta regular everywhere there.
It is nonzero because N and the rational volume form are nonzero.

Now let D=Rbar union support(Calpha), and temporarily enlarge it by the
fibres over B and by F_infinity. Outside D these extra fibres are smooth
and mutually disjoint. Therefore an embedded resolution of the enlarged
divisor can be performed with every centre in D or over D. Write W' for
the resulting smooth projective surface, D' for the reduced inverse image
of D, and D'_big for the enlarged reduced total divisor. Both are SNC,
and W' minus D' is still precisely Xalpha.

On W', pi*eta and dlog(h) are logarithmic along D'_big. Locally a base
parameter at a pole pulls back to a unit times a product of boundary
parameters, so its logarithmic differential has only simple log poles.
The same argument applies to h, whose divisor has the displayed support.
Their wedge is consequently a section of omega_W'(D'_big).

The strict transforms of the additional fibres are NOT silently removed
from Xalpha. At their generic points the modification is an isomorphism
on Xalpha, where theta was already proved regular. Since top log forms
are exactly sections of omega_W'(D'_big), the absence of these divisorial
poles removes their coefficients from the allowed pole divisor. All
exceptional components belong to D'. Thus theta belongs to omega_W'(D'),
the sheaf of logarithmic two-forms for the ACTUAL completion. This
divisorial argument has no residual codimension-two condition for a line
bundle on a smooth surface. It includes every tangency and triple point.

Changed-object control: for two sections z=0,z=t^k, the uncorrected form
dt wedge dz/[z(z-t^k)] has order -k along the final separating exceptional
component, hence is not logarithmic for k>=2. The numerator t^(k-1)
is necessary there; if the fibre is also a denominator, t^k is necessary.
Thus omitting the multiplicity cancellation in N/F would not justify
the all-special-line claim. The global log identity and removal argument
above supply the required cancellations without assuming only transverse
or irreducible intersections.

## Non-domination and scope

Suppose a dominant morphism A2 -> Xalpha existed. Resolve its rational
extension from P2 to W' by point blowups outside A2, obtaining a morphism
S -> W' with SNC source boundary B_S. The inverse image of D' is supported
on B_S. Pullback preserves logarithmic forms: each target boundary
parameter becomes a unit times a monomial in source boundary parameters,
and its dlog is a sum of their dlogs plus a regular differential.
Dominance in characteristic zero makes the pullback of theta nonzero.

On A2 this is f(x,y)dx wedge dy for a nonzero polynomial f. At the generic
point of the original infinity line its pole order is deg(f)+3, as seen
from x=1/t,y=s/t. Point blowups do not change this generic divisorial
valuation. But a logarithmic two-form has pole order at most1 there,
a contradiction. This proves the stated non-domination for ALL alpha.

Independent degeneration check: if Qalpha=L_P*M, with L_P through P and
M not, the rational function R/(L_P² M) has divisor Rbar-2F-M on W.
It is a nonconstant unit on Xalpha. For a=b=c the ratio of the two
ruling-line equations has divisor F1-F2 and is again a nonconstant unit.
A dominant A2 map would pull either unit to a constant polynomial unit,
contradicting injectivity on function fields. These controls independently
exclude reducibles; the log proof above is stronger and is not replaced
by a claim about units on the remaining cases.

QUANTITY: existence of a nonzero section of omega(D) on an SNC completion
of each exact Xalpha; obtained by the displayed N, not a numerical test.
CHEAPEST TEST: manual quartic multiplicity and divisorial-pole audit,
planning ceiling20 minutes, UNMEASURED computational wall or feasibility.
The only mathematical imports not rederived are standard surface
resolution, divisor/log-form facts, and proper quasi-finite finiteness;
no classification or log-Kodaira theorem is used as a black box.

OPEN: none in this explicit all-alpha deduction, subject to independent
review. No new canonical OPEN, gate, computation or descendant is created.
The proof excludes domination of this exact donor family, not arbitrary
Keller maps, all cubic covers, or JC2. It asserts neither affineness nor
simple connectedness. ROOT reports historical overlap of the GENERAL
logarithmic obstruction; no extra history was read and no novelty is
claimed. ROOT's sign and reducible-unit suggestions were independently
checked here, not adopted as additional input premises.

Own-scope collision check: only the designated leased partial, final
report/transaction and own PINS/custody are authored; TASK and all existing
files remain untouched. No scientific process, external lookup, worker,
peer report, protected tree or shared edit was used. Final pins, WHOLE
readbacks, original clock and transaction verification are recorded in
the terminal custody packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9965`.
- Body SHA-256:
  `2d7a79e48b9c382ac265eda8346b4ddde071f6560bd060d8207d12b58b4b3320`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
