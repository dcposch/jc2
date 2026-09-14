# Radial action does not automatically descend to the finite graph ring

ROOT manual producer, September12,2026. MANUAL/PRODUCER-CHECKED,
UNREVIEWED. Independent elementary control, no prior field-generation
theorem or live review is a mathematical premise. Basis
0d39df3c9fd69c939a8420c54d03228b9077777d; operating protocol pin
33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.

## Exact question and scope

Does a radial canonical potential, with J=1, field generation and a finite
birational graph, automatically make its graph ring or conductor invariant
under the radial Euler derivation? NO on the explicit open-plane example
below. This tests the proposed field-to-ring Euler descent step, not the
full-plane Jacobian conjecture. All maps, the conductor ideal and its failed
invariance are computed literally. Full-plane polynomiality is dropped.

## The actual radial canonical map

Let R=C[x,x^-1,y], alpha=(x dy-y dx)/2, and set

    p=x^3,
    q=y/(3x^2)+(4/3)x+(10/9)x^2,
    T=xy/6-x^4/3-4x^5/9.

Then J(p,q)=3x^2/(3x^2)=1. Directly,

    p dq=(-2y/3+4x^3/3+20x^4/9)dx+(x/3)dy,
    alpha-p dq=(y/6-4x^3/3-20x^4/9)dx+(x/6)dy=dT.

Thus T is RADIAL canonical, not the distinct x dy potential. It is even
a polynomial on all A2, but q is not: 3x^2 q=y+4x^3+(10/3)x^4 restricts
to y at x=0. No polynomial Keller map on the full plane is constructed.

Put A=C[p,p^-1,q], embedded in R by these formulas. Nonzero Jacobian
gives algebraic independence of p,q. The inverse formulas are

    y=3x^2 q-4p-(10/3)p x,       x^-1=x^2/p.

Consequently R=A[X]/(X^3-p), X maps to x. Surjectivity follows from
these inverse formulas. Injectivity follows from the monic free A-module
and irreducibility over Frac A: the p-valuation of p is1, so p is not a
cube, and a cubic with no root is irreducible. The extension is finite
free rank3 and etale, since 3X^2 is a unit. In particular R is also
C[x,x^-1,q], a useful coordinate description for the conductor check.

## Exact graph ring and field recovery

Define

    tau=(pq/2-T)/p=x+x^2.

Because p is a target unit, B=A[T]=A[tau]. The identity

    x(tau+1)=tau+p

recovers x in Frac B; tau+1 is nonzero, e.g. it is3 at x=1. Recovering
y then gives Frac B=C(x,y). This is proved directly, not by a full-plane
theorem. Expanding the cube gives

    W=tau^3-3p tau-p-p^2=0.

Since tau generates the degree3 field over Frac A, this monic cubic is
minimal. Division by W shows the kernel A[Z]->R, Z maps to tau, is
exactly (Z^3-3pZ-p-p^2). Thus B is the actual graph ring. The same
A-basis1,x,x^2 makes R finite over B. It is the normalization of B in
the common fraction field, and j:Spec R->Spec B is finite birational
surjective. Omega_(R/B)=0, since Omega_(R/A)=0. F:Spec R->Spec A is
itself etale of degree3 on this OPEN plane; neither map is a full-plane
Keller counterexample.

## The actual singular curve and conductor

The Jacobian derivatives are W_tau=3(tau^2-p), W_p=-3tau-1-2p,
W_q=0. W_tau=0 gives p=tau^2, and W then becomes
-tau^2(tau+1)^2. Since p is a unit, tau is nonzero, and singular points
can only have tau=-1,p=1. W_p vanishes there. Therefore Sing Spec B
is exactly this line times the free q-coordinate.

Write omega for a primitive cube root of1. Its inverse support consists
of x=omega and x=omega^2. Over p=1 the third sheet x=1 has tau=2 and
W_tau=9, hence is smooth. For each fixed q, the first two points have
the same actual graph image but are distinct on the source. The two
branch slopes d tau/dp=(1+2x)/(3x^2) differ by (omega^2-omega)/3, so
the singular curve is nodal, not a repeated component.

The conductor as an R-ideal is EXACTLY

    C_R={r in R: rR subset B}=I R,       I=x^2+x+1=tau+1.

For inclusion IR subset C_R, check all three A-module generators:

    I=tau+1 in B,
    I x=tau+p in B,
    I x^2=tau^2-p in B.

Hence IR subset B, and IR is an R-ideal, giving the conductor inclusion.
Conversely if rR subset B then both r and rx lie in B. Evaluate them at
the colliding points (x,q)=(omega,q0),(omega^2,q0), for every q0. Their
r-values must be equal, say a, and their rx-values must also be equal,
so omega*a=omega^2*a and a=0. Thus r vanishes on both whole lines.
In R=C[x,x^-1,q], the distinct factors x-omega,x-omega^2 divide r;
their product I divides r. This proves equality, without a duality or
abstract conductor theorem.

For D={x=omega}, F(D) is the entire closed line p=1, and
F^-1(F(D)) is all three lines x=1,omega,omega^2. Thus the individual
singular divisor is not saturated; even the union of the two singular
preimage lines misses the smooth third line. Images here are literal
set images, not only their closures.

## Failure of radial Euler descent

For E=(x partial_x+y partial_y)/2,

    E(tau)=(x+2x^2)/2=tau-x/2.

The element x is not in B because it takes different values at the two
colliding graph points. Therefore E(tau) is not in B, although tau is.
Equivalently its two values differ by (omega^2-omega)/2. So E(B) is
NOT contained in B despite radial canonicality, field primitivity and
finite unramified normalization. E certainly preserves the whole field
Frac B=C(x,y), which is a strictly weaker statement.

Similarly E(I)=E(tau) does not vanish on either root of I; hence
E(C_R) is NOT contained in C_R. Thus an unproved assertion that radial
Euler automatically preserves the conductor would fail on this control.
This does NOT refute that assertion after adding full-plane polynomiality;
such a global premise requires a separate argument.

## Positive control and stopping rule

Remove the matched terms (10/9)x^2 from q and -4x^5/9 from T. Then
q0=y/(3x^2)+(4/3)x, T0=xy/6-x^4/3 still satisfy J=1 and
dT0=alpha-p dq0. Now (pq0/2-T0)/p=x, so A0[T0]=R, where
A0=C[p,p^-1,q0]. The graph is smooth and embedded; its conductor is R,
preserved by E. The etale map to the punctured target still has degree3.
Hence failure is not automatic for every radial canonical potential.

Cheapest check: reconstruct J,dT, the cubic, all three conductor products
and E(tau), then evaluate the colliding points. This is a single exact
manual discriminator for the specific Euler-to-ring/conductor arrow, not
a generic auxiliary/gauge/parameter/degree/pole/jet farm. No claim of
full-plane saturation failure, BGV refutation, normality obstruction for
an actual source, new degree exclusion or JC2 resolution. No follow-on
control family or stronger-source theorem is selected by this report.

All mathematics manual; no CAS/scientific interpreter/helper/import/AST/
test, worker, agent or network was used for this derivation. Inert text/
hash/current clock and the existing administrative finalizer only. No
protected-tree inspection, shared-source edit, stage, commit or deletion.
Own full readback, protocol postpin and final marker precede publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6811`.
- Body SHA-256:
  `81dc61fd204f1b67fcec1a7065b4cdd2a0cd3968623edc068ba2bee2304c13ef`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
