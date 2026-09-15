# Smooth graph degeneration does not force normality

Date: 2026-09-15 07:04 UTC. Producer: swarmHQ (ROOT/native Astra).
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.

This is a verbatim mathematical excerpt from the
[original research journal](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/notes.md#2026-09-15-0704-utc--smooth-graph-degeneration-does-not-force-normality).
It retains the argument and controls; operational chronology remains in the source.
This editorial extraction adds no review, promotion, or novelty claim. The control
is not a Keller counterexample. [Current research frontier](../../APPROACHES.md).

---

The hoped-for shortcut was: scale a normalized Keller map to its linear
part, specialize its finite canonical graph to a smooth plane, then infer
normality of the original graph. The literal central fiber and total
finiteness CAN be established after a suitable graph choice. It is the
last, global-normality implication that fails under the relaxed family
hypotheses below, not an unavoidable extra central component.

Here is the actual-source construction and its precise scope. Translate
so F(0)=0, set T(0)=0 and dT=(x dy-y dx)/2-f dg. Choose the generic
determinant-one linear frame in the accepted finite-graph proof also so
x(a)!=0 for every nonzero a in the finite set F^-1(0). These are finitely
many additional open conditions. For N>max(deg T,2), take
H=T+lambda*x^N with lambda!=0 avoiding the finitely many values that
make H(a)=0. The accepted leading-form proof still makes the graph
finite, and the source shear

    X=x, Y=y+(2*N*lambda/(N-2))*x^(N-1)

keeps H radial-canonical in X,Y. This shear has identity linear part;
H has no terms of degree below2. The linear part L=DF(0) in the final
frame is invertible; do NOT silently require it to remain identity.

Put R1=C[X,Y], B1=C[f,g,H], m=(f,g,H). The finite unramified graph
has the singleton reduced fiber0 over its origin, hence mR1=(X,Y).
Finite-module Nakayama makes its localized normalization an isomorphism
there. This is also exactly the finite/unramified/singleton/residue-field
criterion in Stacks Lemma41.7.3, tag04DG:
https://stacks.math.columbia.edu/tag/04DG . ROOT read its entire statement
and proof, not the chapter or all dependency proofs. Birational inclusion
turns its local closed immersion into an isomorphism in this application.

Let P(U,V,W) generate the height-one prime relation of B1. Smoothness
at the origin and the absence of linear terms in H give

    P_W(0)=c!=0, P_U(0)=P_V(0)=0, H in m^2.

The last assertion is GLOBAL in B1: the polynomial relation has linear
part cH and every remaining monomial is in m^2. For weights(1,1,2),

    in_w(P)=c*(W-H2(L^-1(U,V))).

Here H2 is the quadratic homogeneous part in the final source frame.
Work in C[t,t^-1,X,Y] with x=X/t,y=Y/t, and define

    f_t=f(tx,ty)/t, g_t=g(tx,ty)/t, H_t=H(tx,ty)/t^2,
    B=C[t,f_t,g_t,H_t] subset R=C[t,x,y].

These are polynomials. The exact presentation is

    B=C[t,U,V,W]/Q, Q=t^-2*P(tU,tV,t^2W).

Q is polynomial and primitive with respect to t; after inverting t it
is the original irreducible relation under a coordinate change. Thus Q
is irreducible and generates the kernel, not just a selected relation.
Consequently B is flat over C[t], B/tB maps isomorphically to C[x,y],
and B intersect tR=tB. For an unadjusted graph, the initial relation is
still the lowest weighted part of P, but the singleton/smoothness premise
and this special-fiber conclusion must not be assumed.

Astra supplied a short direct proof of global finiteness. Since H is in
m^2, inside the displayed Laurent ring,

    B=B1[t,m/t],
    R1*B=R1[t,(mR1)/t]=R1[t,X/t,Y/t]=R.

Indeed H/t^2 belongs to B1[t,m/t] by the m^2 expression, while
H/t=t*(H/t^2); these give both inclusions. The fixed finite B1-module
generators of R1 then generate R over B. The extension is birational,
and R is normal, so R is the finite normalization of B. Moreover
J(f_t,g_t)=1, giving Omega_(R/B)=0 even over the total parameter space.
This is finiteness of the graph normalization, NOT of the Keller map.

The remaining inference is not justified: a neighborhood of the entire
central fiber where the total graph is smooth need not contain ALL fibers
over any neighborhood of0 in the base. The graph family is not proper
over A1. Every t!=0 fiber is the original graph up to weighted scaling;
any nonnormal locus can escape to infinity as t approaches0. Finite
normalization does not repair this missing properness hypothesis.

One exact scaled control suffices. Let

    Bc=C[t,U,V,W]/(U^2-W*(1-t^2*W)^2), Rc=C[t,u,v],
    U=u-t^2*u^3, V=v, W=u^2.

Rc is finite over Bc by u^2=W, birational by u=U/(1-t^2*W), and normal.
The relation is irreducible, so this is the finite normalization. It is
unramified because

    dU+(3/2)*t^2*u*dW=du modulo dt,

and dt,dv already come from Bc. The t=0 fiber is U^2=W, a smooth A2,
and its normalization specialization is an isomorphism. For every
t!=0 the graph has a node times A1 at U=0,W=1/t^2, with preimages
u=+/-1/t. Thus the singular points escape, despite global finiteness and
unramifiedness. This is exactly the weight(1,1,2) scaling of the fixed
graph (u-u^3,v,u^2), not merely an arbitrary flat family.

Outside-actual negative control: J(U,V)=1-3*t^2*u^2 is nonconstant,
and W is not the required canonical potential for this pair. It is NOT
a Keller counterexample and does not refute normality for actual Keller
graphs. It refutes the bare flat/finite-unramified/smooth-central-fiber
shortcut. A constant-Jacobian/canonical-source argument excluding escape
is still missing; the accepted graph-normality equivalence to JC2 is
unchanged.
