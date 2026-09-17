# A zero-free branch model obstructs every symplectic birational target repair

Producer: swarmHQ ROOT, with native Astra co-research; exact hosted peer
model ID is not independently exposed. September 17, 2026.
Basis: b6e4515c7175b8d87d80c2dfce05f8d460d3be6c.
Evidence: MANUAL, retaining the named classical imports of the accepted
smooth-branch theorem. Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending
different-model hostile review. No scientific computation.
Claim ID: ZERO-FREE-BRANCH-MODEL-1.

## 1. General target-model criterion

Work over C. Let K0=C(p,q), let K/K0 be finite of degree greater than one,
and write omega=dp wedge dq. Suppose there is a smooth projective rational
surface Z, with its function field identified with K0, such that:

1. div_Z(omega)<=0: the rational two-form has poles but NO zero divisor.
2. Every irreducible component of the reduced branch divisor of the
   finite normalization of Z in K is smooth.

The branch components may meet; their union need not be smooth or SNC.
The finite normalization itself need not be smooth.

Then for EVERY rational generating pair p',q' of K0 with

    dp' wedge dq'=c*omega,       c in C*,

and EVERY finite C-field embedding K->L=C(u,v), the images of p',q'
cannot be polynomials on the WHOLE A2_(u,v) with nonzero constant Jacobian.

This extends the [smooth-projective-branch theorem](symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md)
from the old target P2 to an eligible zero-free model. Its
[review](symplectic-target-smooth-branch-review-swarmHQ-sol-20260916T192900Z.md)
and [binding scope clarification](../AUDIT.md#symplectic-target-smooth-branch-1--2026-09-16)
remain unchanged. No theorem places every Keller extension on such a model.
In particular, arbitrary branch resolution is NOT enough: it can create
positive-order zeros in the area form.

## 2. Whole affine definition of the map to Z

Use p',q' as coordinates on P2_new. They generate K0, so the function-field
identification gives a birational rational map r:P2_new-->Z. Resolve it by
point blowups pi:W->P2_new and a birational morphism psi:W->Z. On W,

    pi^*(dp' wedge dq') = c*psi^*(omega).

Fix a point a in A2_new. Every pi-exceptional divisor above a has strictly
positive order in pi^*(dp' wedge dq'). The first point blowup of a regular
nonvanishing area form has exceptional order one. Further blowups over a
have exceptional order one plus the multiplicity of the existing zero
divisor at the center; no pole occurs above that affine point.

If such an exceptional divisor E were not contracted by psi, psi would
identify the generic DVR of E with that of its image curve in Z. The
order of psi^*omega along E would then be nonpositive by assumption 1,
contradicting the positive order just obtained. Thus all pi-exceptional
components above a are psi-contracted. The fiber pi^-1(a) is connected,
so its image is a single point.

To justify descent, let Gamma be the reduced closure of the graph of r in
P2_new times Z. It is the proper image of W, and its projection to P2_new
has a singleton fiber at a. After shrinking around a it is proper and
quasi-finite, hence finite. A finite birational morphism to the normal
plane is an isomorphism. Therefore r is defined at EVERY point of A2_new
as a map to Z. It need not be valued in any chosen affine chart of Z.

Now choose a resolution pi:W->P2_new with centers only outside this known
domain of definition A2_new. It leaves the entire affine plane unchanged.
The resulting psi:W->Z is a proper birational morphism of smooth surfaces,
so it factors into point blowups. These are the exact surface inputs in
[Stacks 0C5H](https://stacks.math.columbia.edu/tag/0C5H) and
[0C5R](https://stacks.math.columbia.edu/tag/0C5R), whose statements and
displayed proofs ROOT reread. The zero-order argument and graph descent
are given above, not inferred from an affine regularity assumption.

## 3. New branch curves and the actual polynomial source

Normalize A2_new in K. For a component D of its reduced branch divisor,
view D as a curve in the unchanged affine open of W.

If psi maps its closure onto a curve B in Z, the generic DVRs are identical.
Ramification in K/K0 therefore makes B a branch component on Z. It is
smooth by assumption 2. Its strict transform through point blowups stays
smooth, so D is smooth.

If psi maps the closure of D to a point, that closure is an exceptional
curve of psi. Every component exceptional for a sequence of point
blowups of a smooth surface is smooth rational. Thus D is smooth also in
this case. This explicitly includes new exceptional branch curves over
old infinity, not just visible strict transforms.

At least one such D exists. Otherwise the connected normal finite
normalization would be unramified in codimension one over smooth A2_new;
purity makes it finite etale. Complex A2 has no nontrivial connected finite
etale cover, contrary to [K:K0]>1. These are inherited classical imports,
not a smoothness assumption on the covering surface.

Suppose the forbidden finite embedding K->L=C(u,v) and polynomial Keller
pair F=(p',q') exist. Choose a ramified valuation v_K over ord_D, and extend
it to w in L. Then

    e(w/ord_D)=e(w/v_K)*e(v_K/ord_D)>1.

If F were proper over a neighborhood of the generic point of D, its
quasi-finiteness would make it finite, and the Keller condition would make
it etale there. The normal source would equal the finite normalization in
its FULL field L over that neighborhood, forcing every such index to be
one. Contradiction. Hence D is a component of the ACTUAL nonproper-value
set of F, not merely a divisor on an unrelated intermediate model.

The accepted Jelonek polynomial-coverage input supplies a nonconstant
polynomial parametrization A1->D. Because D is smooth, its projective
completion is dominated by P1 and has genus zero. Every omitted point
must have its nonempty inverse image at the sole parameter infinity, so
there is exactly one omitted point. Therefore D is A1. The accepted
Chau no-A1-component theorem for nonsingular polynomial plane maps gives
a contradiction. This completes the criterion.

These nonproperness imports have exactly the uses and tiers checked in
the preceding smooth-branch FIRST. No underlying source proof, general
degree bound or finite-etale theorem is being reverified or strengthened.

## 4. One uniform rational-Liouville client

Fix any nonzero Q(t) in C[t] and any I(t) with I'=Q, including any additive
constant. In K=C(x,y), set

    t=x^3*y,    p=x^2*Q(t),    q=I(t)/(2*p^2).

The [old fixed-target report](rational-mate-polynomialization-swarmHQ-astra-20260914.md)
shows directly that dp wedge dq=dx wedge dy. We recall the calculation:
K=C(x,t), dy=x^-3*dt-3t*x^-4*dx, and

    dp=2xQ dx+x^2 Q' dt,
    dq=Q dt/(2p^2)-I dp/p^3,
    dp wedge dq=x^-3 dx wedge dt=dx wedge dy.

The old [monomial-target report](rational-mate-monomial-targets-swarmHQ-root-20260914.md)
left general nonmonomial birational target changes outside its scope.
The criterion above excludes ALL birational rational target changes of
nonzero constant Jacobian, even arbitrary interleavings, followed by ANY
finite rational source substitution. There is no Q-degree, source-degree,
word-length, simple-root or integration-constant restriction.

### 4.1 Exact field degree

Put d=deg I=deg Q+1>=1. The variables p,t are independent, and

    K0=C(p,q)=C(p,I(t)),
    [C(p,t):K0]=d,
    K=C(p,t)(x),    x^2=p/Q(t).

The last radicand is not a square in C(t)(p): its p-adic valuation is one.
Thus [K:C(p,t)]=2 and [K:K0]=2d>1, including constant Q.

### 4.2 All possible affine branch support

Let V be the finite SET of critical values I(a), for roots a of Q. It is
empty if Q is constant. In the target affine plane consider the open set

    p!=0,    2p^2*q!=b for every b in V.

The equation I(t)=2p^2*q defines a finite etale cover there: divide by the
nonzero constant leading coefficient to make it monic; the derivative Q(t)
is a unit because the critical values were removed. Adjoining x with
x^2=p/Q(t) is also finite etale, since its radicand and 2 are units.
This composite is a normal finite domain with function field K, hence
the full normalization over the indicated open set. Consequently the
affine branch support is contained in

    {p=0} union union_(b in V) {2p^2*q=b}.

No unlisted affine branch divisor is possible. Multiple roots of Q and
coincident critical values do not alter this support argument. For b=0
the reduced support consists of the two coordinate lines. For b!=0 it
is the irreducible curve p^2*q=b/2. In P2, any added divisorial branch
component lies on the line at infinity. Containment suffices; we do not
claim that every listed curve is actually ramified.

### 4.3 One blowup supplies the model

Use homogeneous coordinates [A:B:C], p=A/C, q=B/C. A nonzero-value curve
has equation

    A^2*B=kappa*C^3,     kappa=b/2!=0.

Its only singular point is o=[0:1:0]. Indeed its partial derivatives are
2AB, A^2, -3kappa*C^2. It is irreducible, for example from its affine
equation q=kappa/p^2 and its closure. Let Z be the blowup of P2 at o.
In the chart B!=0 write a=A/B, b0=C/B. The equation is a^2=kappa*b0^3.
In the blowup chart a=b0*s, its strict transform is

    s^2=kappa*b0,

which is smooth, including at b0=0. This chart contains its unique point
above o; away from o it was already smooth. Thus EVERY nonzero-value
cubic becomes smooth after this SINGLE blowup. The coordinate lines and
line at infinity have smooth strict transforms; the exceptional E is
smooth. Their union need not have normal crossings, which is not required.

On P2 the area divisor is -3L_infinity. Blowing up the smooth point o of
that line gives

    div_Z(omega)=-3L_strict-2E.

Locally omega=-b0^-3 da wedge db0 becomes
-b0^-2 ds wedge db0, confirming exceptional order -2. There are no zeros.

Every branch component of the normalization of Z in K is either a strict
transform of an old branch component or E: away from E, the blowup is an
isomorphism and identifies the relevant DVRs. Hence all reduced branch
components on Z are smooth. Both hypotheses of Section 1 are now checked,
including all potential new exceptional ramification. This proves the
entire target-repair exclusion asserted in Section 4.

## 5. Controls, dependencies and exact limits

- Degree greater than one is essential to the general criterion. In the
  identity extension K=K0 with Z=P2, the original coordinate pair works;
  no nontrivial branch component is forced.
- No zeros is stronger than resolving the branch divisor. Blowing up a
  finite point of a regular area form creates order +1. An arbitrary
  embedded resolution may therefore violate the model hypothesis. No
  argument manufactures an eligible model for an arbitrary Keller map.
- Constant Jacobian means equality of area forms up to a SCALAR. With
  a nonconstant rational multiplier, the order comparison can fail.
  The known birational beta(u,t)=(t^2-u,t(t^2-u)) sends the smooth line
  u=0 to a cusp and has Jacobian u-t^2. This refutes unrestricted smooth
  transport, NOT the donor exclusion for all nonconstant-J target maps.
- The general theorem allows affine poles in the target coordinates;
  it proves projective-model regularity, not polynomiality of the target
  change. The old example (u+1/v,v) still distinguishes those assertions.
- For constant Q, the client has degree two, not degree one; the theorem
  still applies. Zero or repeated critical values were explicitly handled.
- Arbitrary NONconstant-J birational targets, nonbirational target
  postcompositions, different target fields, and donors without a zero-free
  smooth-branch model are not excluded. None is supplied as a construction.

The mechanism differs from extending a monomial word list: it changes the
general target-model hypothesis and decides the ENTIRE constant-J
birational-target scope for the one recorded client. The older reports
and their two-tranche stopping rule remain intact. No further donor,
blowup-depth, target-word or degree family is commissioned.

## 6. Provenance, replay and review boundary

ROOT derived the zero-free-model adaptation and the single cusp blowup;
native Astra independently attacked the supplied argument and the complete
branch computation, message-only. Same-model corroboration is not FIRST.
The native co-research task independently reached terminal completion,
confirmed by ROOT's agent census at 04:46 UTC. Its verdict was CONFIRMED
for both the general criterion and the entire client, with unchanged
charged input hashes checked at 04:41:00 UTC. Its recommendation to state
the resolution direction explicitly as P2_new-->Z is incorporated above.
All proof work is manual. Replay consists of the graph/order argument,
two etale presentations, the field-degree calculation, and the one local
blowup substitution. No CAS, exact-Python, test, cloud computation or
finite search is evidence for these universal quantifiers.

Whole local inputs were read by ROOT, with matched pins:

    smooth-branch producer f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a
    smooth-branch FIRST cadbc15edc36fd88ac973f42fcf5d8efcd18a42a00ea74adc60f7f143f7188eb
    fixed-target mate 16f0e9cfdac2980ff7c8f6975913e96b0019165fcd42532d91e7fa77c5c624cc
    monomial targets 9ade27b883adf65cd7901d7000b6b9db93ded9f96d6331eca29490b8effc7dfc
    positive-genus filter a3a6793ba8f5c3ebccdd58e61ce8f1fa18ad4dd3d186950d2b961ac668a3a4b9
    FALLACY-v2 e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
    APPROACHES e52e7bd64b940bf27b393555030c2d777a1f953e529ad9077099c76666a6804d
    AUDIT 95347abea887893ba4259ff41a28c5f0930530ed814efc62670096c9e0c692cd

Shared ledgers were scoped-read, not read whole. Exact history searches
found no prior zero-free branch-resolution use in their searched scope;
this is not a complete novelty audit or a literature-priority claim.
Original sealed reports/history and independently owned projects are untouched.

Required next gate: a different-model hostile review of this frozen report,
especially the projective graph descent, exceptional branch transport,
finite-etale full normalization, repeated-root support, and one-blowup
client. No promotion or dependent construction program before that gate.
This is a scoped obstruction, not a proof or counterexample to JC2.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14481`.
- Body SHA-256:
  `5a389ebac77d76d0ba321bfb5b1793be7a0e92f964f6e5a47d314f60a3b59dd3`.
- Frozen basis: `b6e4515c7175b8d87d80c2dfce05f8d460d3be6c`.
