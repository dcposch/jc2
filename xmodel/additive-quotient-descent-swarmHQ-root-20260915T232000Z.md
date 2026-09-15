# Additive quotient descent and a failed concrete action

Producer: swarmHQ ROOT and native co-researcher, both gpt-6-astra.
Date: September15,2026 UTC.
Basis: 23629da4480a544e16cb85675b1c5a7f93655c92.
Evidence: MANUAL, PRODUCER-CHECKED, UNPROMOTED. Same-model co-research
is not different-model FIRST. No literature-priority claim or JC2 solution.

## Exact conditional bridge

Let R=C[x,y,z] and let D be a nonzero locally nilpotent derivation whose
three coefficients have greatest common divisor1. Assume its ENTIRE
kernel is A=C[u,v], a polynomial algebra. Let F:A3->A3 be a polynomial
map with constant nonzero Jacobian and

    D F* = F* D.

Then F* restricts to a plane Keller map G on A, and

    det DG = det DF,
    [Frac(R):F*Frac(R)] = [Frac(A):F*Frac(A)].

In particular an F of geometric degree greater than1 satisfying these
hypotheses would supply a plane counterexample of the same geometric degree. The compatible
action and its full polynomial kernel are hypotheses, not conclusions
about an arbitrary three-dimensional map. The bridge does not itself
prove invertibility: it includes EVERY stabilized plane Keller map
F=(G(x,y),z), with D=partial_z.

This is different from the accepted
[volume-neutral torus obstruction](volume-neutral-torus-quotient-swarmHQ-root-20260915.md).
That proof also supplies a product coordinate and an injective line in
its plane quotient. No such additional condition is supplied here.

## 1. A primitive additive action gives a constant quotient volume

Put Omega=dx wedge dy wedge dz and beta=i_D Omega. Over Frac(R), the
two-form du wedge dv is a nonzero multiple h beta: both span the top
exterior power of the two-dimensional annihilator of D. Primitivity of
the coefficients of beta implies h belongs to R. Indeed any irreducible
factor in a reduced denominator for h would divide all three coefficients
of beta, contrary to their greatest common divisor1.

The additive action exp(tD) has polynomial inverse exp(-tD); hence its
Jacobian is a unit in R[t], and equals1 at t=0. Therefore div(D)=0.
Taking Lie derivatives in du wedge dv=h beta gives D(h)=0, so h belongs
to A. We show h is a constant unit.

The kernel of a locally nilpotent derivation in characteristic zero is
factorially closed: the D-degree of a product of nonzero polynomials is
the sum of their D-degrees. Thus an irreducible element a of A stays
irreducible in R. Also

    aR intersect A = aA:

if b=ac belongs to A with c in R, then 0=D(b)=aD(c), so c belongs to A.

Suppose an irreducible a in A divides h. Choose b in A whose image is
transcendental over C in A/(a). The injection A/(a)->R/(a) preserves this
property. At the generic point of the reduced hypersurface a=0 in A3,
da is nonzero, and db is nonzero on that hypersurface. Characteristic
zero guarantees the latter differential assertion. Consequently
da wedge db is nonzero there. But

    da wedge db = J_(u,v)(a,b) du wedge dv

vanishes there because du wedge dv=h beta and a divides h. Contradiction.
Thus h has no irreducible factor in A=C[u,v], so h is a nonzero constant.
Equivalently beta=c du wedge dv with c in C*.

Equivariance gives F*beta=i_D(F*Omega)=(det DF)beta. On the other hand,
pulling back c du wedge dv multiplies it by det DG. The injection A->R
and the nonzero form yield det DG=det DF in A. No quotient smoothness at
every special fiber, properness, or freeness of the action was assumed.

## 2. Generic degree is preserved

Write K=Frac(A), L=Frac(R). The rational-slice argument gives L=K(t)
with Dt=1. Explicitly, choose an element of positive D-degree, put its
last nonzero derivative a in A and its preceding derivative b in R,
and set t=b/a. After inverting a, the slice induction gives
R_a=A_a[t]; applying D and subtracting powers of t proves that statement
by induction on D-degree.

Equivariance extends to fractions, so

    D(F*t)=F*(Dt)=1,     F*t=t+c0,     c0 in K.

Therefore F*L=(F*K)(t+c0), and

    [K(t):(F*K)(t+c0)] = [K:F*K].

Here t+c0 remains transcendental over K; adjoining it does not change
the finite extension degree. This proves the claim. Special fibers with
several orbits or fixed points do not alter this generic field identity.

## 3. Controls on the hypotheses

- The ENTIRE kernel is essential: for D=partial_z, the smaller polynomial
  algebra C[x,xy] consists of invariants, but d(x) wedge d(xy) equals
  x dx wedge dy and the divisor x=0 contracts to a point. The alternative
  invariant subalgebra C[x^2,y] introduces a divisorial differential factor
  as well. Neither subalgebra is ker D.
- Primitive but nonfree action: D=x partial_y+2y partial_z,
  u=x, v=xz-y^2. Its kernel is C[u,v] and beta=-du wedge dv. It has a
  fixed line x=y=0; fibers u=0,v!=0 have two orbit components. These
  degenerations are compatible with the asserted generic degree equality.
- Dropping primitivity: D=x partial_z has kernel C[x,y], but
  beta=x dx wedge dy, not a constant multiple. For a in C*,
  F=(a x,y,a z) commutes with D, while det DF=a^2 and det DG=a.
  Choosing a!=1 disproves the asserted determinant equality without
  primitivity. This does NOT claim that every nonprimitive quotient fails
  to be Keller.
- Stabilization F=(G(x,y),z), D=partial_z, preserves every original
  plane Keller problem. No torus-style automatic invertibility follows
  from an additive quotient alone.

## 4. The first literal action does not descend

Use only the polynomials displayed in the earlier
[graph report](equivariant-graph-nonlinear-obstruction-root-20260912.md),
reordering the outputs as F=(R0,Q,P):

    P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
    Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
    R0=2x-3x^2 y-x^3 z.

No claim about the ambient triple's Keller or counterexample status is
needed for the following negative test. Consider the primitive locally
nilpotent derivation

    E=x partial_y-3 partial_z.

Its full kernel is C[x,3y+xz], and i_E Omega=-dx wedge d(3y+xz).
It has a global slice -z/3, and E(R0)=0. These are favorable source
properties, but compatibility with F still has to be checked.

Put w=xy. Direct differentiation gives

    E(Q)=4x-6(1+w)R0.

The two source points

    a=(0,0,-1),             b=(1/2,-3,26)

have the same ordered image F(a)=F(b)=(0,0,-1). At b, the exact sums are

    R0=1+9/4-13/4=0,
    Q=-3+39/4-27/4=0,
    P=-13/4+9/4=-1.

But E(Q)(a)=0 and E(Q)(b)=2. Hence E(Q) is not a function of the target
coordinates. No single-valued target vector field E' can satisfy
dF(E)=E' composed F, even before requiring E' to be locally nilpotent.
In particular this natural source action does not give a plane quotient
of F through the conditional bridge.

This rejects only E. It neither excludes all nonlinear additive actions
nor produces another one. The cheapest actual compatibility test is
complete; no coefficient search or enlarged symmetry family is selected.

## Scope, comparison and provenance

The earlier equivariant graph exclusions concern different source planes
and a torus grading, not this additive action. The present condition is
an exact possible descent mechanism, not a new actual-source realization.

ROOT derived the contraction/degree argument and the literal two-point
test; the native co-researcher independently reconstructed the former
and checked the latter manually. The native terminal submission was
collected and independently observed COMPLETED before final authoring.
No scientific code was executed.
No external theorem from an inaccessible paper was imported; kernel
polynomiality is explicitly assumed, and the slice argument is supplied.

Nearest whole-read report hashes:

- volume-neutral-torus-quotient-swarmHQ-root-20260915.md:
  181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80.
- equivariant-graph-nonlinear-obstruction-astra-20260912.md:
  4c253ddf7fd1cc6c5cfad90dbefec5f609a5ea2d4dcdb5a300b2feb35a94200d.
- equivariant-graph-nonlinear-obstruction-root-20260912.md:
  8ae6ee53450d7a7ef4e688cf768903ca9900f8e4f176088076c3c8bf9cdde828.

This report is not a general additive-equivariant Jacobian theorem or a
new complete construction. No stronger unreviewed claim is used, no
promotion follows, and no dependent task is licensed. The missing item
is an actual compatible action for a relevant map, not another derivation
of the conditional degree identity. JC2 remains unresolved.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Canonical scan completed exit0 after native terminal collection. All three
nearest-report pins matched again before closure. This lexical scan is
not a novelty certificate or mathematical verification.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8643`.
- Body SHA-256:
  `d278cd733edf602e8fdb6d6d21ae60d8c1b55003a70686ef3dba4fc7df7f17d7`.
- Frozen basis: `23629da4480a544e16cb85675b1c5a7f93655c92`.
