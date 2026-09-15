# Hostile review of the tangent-graph first-pair obstruction

Reviewer: swarmHQ Sol (gpt-5.6-sol), September 15, 2026. Startup
2026-09-15 18:06:49 UTC. MANUAL review.

Reviewed contribution commit:
`a5431f85d9522b569109209badf05a1b32e11a65`. Producer full SHA256
`4a2b0b3b92ca94b54c8807c39fa1afed0fd6bf60e3b866fdb4fa588a0ab2de3d`,
manifest `49a6a3e610bf6d7aa301605747b88d4679981dc9b8a7cc76f2a035e36f4cdcbf`.
The sealed producer was verified and whole-read after checking its commit blobs,
mode, basis, and hashes. Its pre/post-review hashes agree.

## Verdict

**CONFIRMED**, at exactly the producer's scope. For every nonzero polynomial
gamma and degree-d polynomial p with d>=2 for which C and D are polynomials
on the whole plane, the stated y-degree and leading coefficient of J(C,D)
are correct. Consequently no two elements of C[C,D] form a Keller pair.
This applies on every polynomial graph of the literal whole tangent triple,
but says nothing about a pair involving E, rational changes, other source
orientations, or arbitrary JC2 maps.

## Independent derivation and attacks

Write g=gamma and u=1+xy. From CD=p(w)+2g,

    dC wedge dD=(p'(w)dC wedge dw+2dC wedge dg)/C.

Here `dC=g dx+x dg` and `dw=u dg+g(y dx+x dy)`. Direct expansion gives

    dC wedge dw=g(g_y+xg+x^2 g_x) dx wedge dy,
    dC wedge dg=g g_y dx wedge dy.

Division by C=xg therefore gives exactly

    J(C,D)=p'(w)(g+xg_x+g_y/x)+2g_y/x.

This identity is first in C(x)[y]. Whole-source polynomiality of C,D makes
its left side, hence the complete right side, polynomial; the degree argument
does not assume the displayed summands are individually regular at x=0.

Let n=deg_y g and h be its nonzero leading coefficient. Then w=gu has
y-degree n+1 and leading coefficient xh. The degree-n coefficient of
`g+xg_x` is h+xh'. This cannot vanish in characteristic zero: on each
monomial x^i the operator h -> h+xh' multiplies its coefficient by i+1.
Meanwhile g_y/x has y-degree at most n-1, including zero when n=0. Thus
the first summand has degree

    (d-1)(n+1)+n=d(n+1)-1

and leading coefficient `d p_d (xh)^(d-1)(h+xh')`. The second summand is
strictly lower degree. No cancellation or x-localization loophole remains.
For n=0 the formula specializes to degree d-1 with coefficient
`d p_d (xh)^(d-1)(h+xh')`, still nonzero.

For H,K in C[s,t], the chain rule factors their pulled-back Jacobian as
`J_st(H,K)(C,D) J(C,D)`. If it were a nonzero constant, both polynomial
factors would be units in C[x,y], contradicting the positive y-degree of
J(C,D). This proves precisely the subalgebra conclusion, without an
unjustified extension to pairs using E.

The controls agree. With g=1,p=-2w^2 the formula yields
`J=-4-4xy`; with g=1+xy it yields the displayed degree-three polynomial
and leading term -8x^3. At d=1, g=1,p=-2w gives (C,D)=(x,-2y), showing
the degree hypothesis is load-bearing.

Finally, the full-triple attachment is valid. Regularity along g=0 with
x nonzero forces p(0)=q(0)=0, so p=wA and the differential relation gives
q=w^2B. Regularity at x=0 gives A(gamma0)=-2 and B(gamma0)=-1. If A were
constant, it would equal -2, while q'=wp'/2 and q(0)=0 would force
B=-1/2, a contradiction. Hence every literal admissible triple has d>=2,
and restriction to any polynomial graph preserves polynomiality of D.

The result is genuinely narrower than the one-sided all-output graph theorem
and the FULL-output embedded-plane transfer, while stronger in graph and p
generality for the first-pair subalgebra. The component-fibre result does not
already supply this arbitrary-graph statement. No accepted degree bound or
foundation was re-audited.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3760`.
- Body SHA-256:
  `aa047db75c7c8a279265b9ef42da626998a486f64eaedfc4fc5344e400a3f576`.
- Frozen basis: `a5431f85d9522b569109209badf05a1b32e11a65`.
