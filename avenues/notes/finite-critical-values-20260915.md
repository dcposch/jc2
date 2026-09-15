# Finite critical values do not control infinity or genus

Date: 2026-09-15 03:48 UTC. Producer: swarmHQ (ROOT/native Astra).
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.

This is a verbatim mathematical excerpt from the
[original research journal](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/notes.md#2026-09-15-0348-utc--finite-critical-values-do-not-control-infinity-or-genus).
It retains the argument and controls; operational chronology remains in the source.
This editorial extraction adds no review, promotion, or novelty claim. The control
is not a Keller counterexample. [Current research frontier](../../APPROACHES.md).

---

ROOT tested the necessary fact that, for an actual plane Keller pair
F=(f,g), h=(f-a)(g-b) has critical locus exactly F^(-1)(a,b):
dh=(g-b)df+(f-a)dg and df,dg are a coframe. Each such point is an
ordinary node/nondegenerate critical point at value0. The set can be
empty when (a,b) is omitted. For generic (a,b) its cardinality is the
mapping degree. The proposed leap from this FINITE critical data to
generic genus zero is false; no theorem controlling infinity was supplied.

Exact countercontrol, ROOT/native Astra, MANUAL/PRODUCER-CHECKED,
UNPROMOTED (not different-model FIRST):

    P=y(y-1), u=xP, h=u+u^2*y^3.
    h_x=P*(1+2u*y^3),
    h_y=x*P'*(1+2u*y^3)+3u^2*y^2.

If P!=0 and h_x=0, then u,y!=0 and h_y=3u^2*y^2!=0. If P=0,
y=0 or1 and h_y=xP', so the only critical points are(0,0),(0,1).
At(0,a), a=0,1, the quadratic term is P'(a)*x*(y-a); Hessian
determinant is -P'(a)^2=-1. Both values are0.

For t!=0, h=t forces P!=0. The coordinate change (x,y)->(u,y) is
an isomorphism on this open set; with w=1+2u*y^3 it gives

    w^2=1+4t*y^3,   x=(w-1)/(2P*y^3).

The smooth projective cubic has genus1 for every t!=0. The original
fiber is exactly this curve minus infinity and the points over y=0,1.
There are GENERICALLY five punctures. At t=-1/4 the two points over y=1
coincide, leaving four. This is an additional atypical value at infinity,
NOT a finite critical value: every point of that affine fiber is smooth.
This exception was found by the native check and incorporated here.
No cancelled genus chart is used at t=0.

The polynomial also factors as f0*g0 with
f0=x, g0=P*(1+xP*y^3). Both zero fibers are smooth, although g0=0 is
disconnected: it comprises y=0, y=1, and the disjoint graph
x=-1/(y^4*(y-1)), y!=0,1. On the first two components (g0)_y=P'=+/-1;
on the graph (g0)_x=P^2*y^3!=0. They meet f0=0 transversely at exactly
the two nodes above. The t=0 fiber has three lines with two crossings
and the disjoint graph; its Euler characteristic is0. Generic fibers
have Euler characteristic -5 and the -1/4 fiber has -4, giving the
consistency check (-1)*(-5)+0+(-4)=1 for the total plane.

This pair is NOT Keller:
J(f0,g0)=P'+x*(2PP'*y^3+3P^2*y^2) vanishes at(0,1/2).
The control does NOT satisfy the simultaneous translated-product
hypotheses of an actual Keller pair, nor does genus1 refute an unspecified
higher genus bound. It refutes only the stated genus-zero inference,
even with smooth transverse factor zero fibers. It is no JC2 counterexample.
