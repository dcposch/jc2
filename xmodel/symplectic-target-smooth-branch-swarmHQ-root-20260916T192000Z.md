# Smooth branch donors survive no constant-Jacobian birational target repair

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra co-research.
Date: September16,2026. Basis: 9aab38787eb24fffc86dacd5859f9c63d439959f.
Evidence: MANUAL / named classical imports. Lifecycle: PRODUCER-CHECKED,
UNPROMOTED pending different-model FIRST. Same-model corroboration is not FIRST.
Claim ID: SYMPLECTIC-TARGET-SMOOTH-BRANCH-1.

## 1. Statement and scope

Work over C. Let K0=C(p,q), let K/K0 be finite of degree greater than one,
and let X->P2_(p,q) be the normal finite projective normalization in K.
Assume EVERY irreducible component of its reduced projective branch locus
is a smooth projective curve. Components may intersect; their union is not
assumed smooth or a simple-normal-crossings divisor.

Let tau=(p',q') be a birational rational target coordinate change with

    C(p',q')=C(p,q),          J_(p,q)(p',q')=c in C*.

Then there is no C-field embedding K->L=C(x,y), of any finite degree,
such that the images of p',q' are polynomials in x,y with nonzero constant
Jacobian on the WHOLE source A2.

**Product-cover client.** In particular, take K=C(s,t), any rational
function R(s) of degree m>=2, and

    p=R(s),                 q=t/R'(s).

No constant-Jacobian birational rational target change, followed by ANY
finite-degree rational source substitution, makes this pair a whole-plane
polynomial Keller pair. The original rational pair has Jacobian one.
Polynomial R, including s-s^109, is a special case; no degree bound is used.

The decisive new scope is the target change, including exceptional branch
divisors created in its new affine chart. Arbitrary birational target changes
with NONCONSTANT Jacobian are not covered. Neither are arbitrary donors
with singular projective branch components. No reduction places every
hypothetical Keller source in this class; JC2 remains unresolved.

## 2. Zero-free area forms prohibit affine projective indeterminacy

Write omega=dp wedge dq on P2. Its divisor is -3L_infinity, with no zeros.
We claim that tau and tau^-1 are everywhere defined on their affine planes
AS MAPS TO P2. This does not assert they map those planes into A2.

Resolve tau by point blowups pi:Z->P2_old and a birational morphism
psi:Z->P2_new. Equality of rational forms gives

    psi^*(dp' wedge dq')=c*pi^*(dp wedge dq).

Fix a finite point a of the old plane. Every pi-exceptional divisor above
a has strictly positive order in pi^*omega. The first point blowup of a
nonvanishing regular two-form has order one on its exceptional curve.
Each later blowup over a has order one plus the multiplicity of the
existing effective zero divisor at its center, hence again positive.

If one such divisor E were not psi-exceptional, a proper birational
morphism of normal smooth surfaces is an isomorphism at the generic point
of its image curve. Equality of forms would then give a positive order
of dp' wedge dq' along a curve of P2_new. Its divisor is -3L'_infinity,
so this is impossible. All components of pi^-1(a) are therefore contracted
by psi. Their connected union has a single image point.

For clarity, this proves descent rather than merely claiming it: let Gamma
be the reduced closure of the graph of tau in P2_old x P2_new. The proper
birational projection Gamma->P2_old has a singleton fiber at a, by the
preceding connected-fiber argument on Z. It is quasi-finite over some open
neighborhood of a, hence finite there. A finite birational morphism onto
a normal variety is an isomorphism. Thus tau is defined at a. The inverse
has constant Jacobian c^-1, so the same reasoning applies to it.

Now resolve tau^-1 by pi':Z'->P2_new, with psi':Z'->P2_old a birational
morphism. Since tau^-1 is already defined on A2_new, all centers of pi'
may be chosen above L'_infinity. Consequently Z' contains the ENTIRE
A2_new unchanged. The morphism psi' factors as point blowups between
smooth surfaces. Therefore:

- the strict transform of any smooth projective old curve is smooth;
- every irreducible psi'-exceptional curve is smooth and rational.

Their intersections with the unchanged A2_new are smooth. In particular,
whenever the image of an old line is an affine curve, that affine curve
is smooth. If its normalization is A1, it is itself an embedded A1.

Classical inputs: resolution by point blowups away from the given domain
of definition, [Stacks Lemma54.4.3, 0C5H](https://stacks.math.columbia.edu/tag/0C5H),
and factorization of proper birational morphisms of regular surfaces,
[Lemma54.17.1, 0C5R](https://stacks.math.columbia.edu/tag/0C5R).
ROOT read both statements and displayed proofs. Connected blowup fibers,
proper quasi-finite finiteness, finite-birational normality, and the local
two-form blowup formula are standard additional inputs, used explicitly.

The zero-divisor observation is classical in spirit. Blanc's
[1012.0706v1](https://arxiv.org/pdf/1012.0706), December3,2010, Section1,
Lemma3.2 and Proposition3.3 motivated the scope check. His group-generation
theorem concerns dp/p wedge dq/q, NOT dp wedge dq. No generator theorem
for that logarithmic form is imported for the ordinary area form here.

## 3. Every new affine branch component is smooth

Normalize A2_new in K and call the resulting finite map Y'->A2_new.
Take any reduced irreducible branch component D in A2_new. Regard its
valuation on K0 through the birational identification of the two target
fields. On Z' above, D is literally a curve in the unchanged affine open.
There are two exhaustive possibilities for psi'(D):

1. It is a curve B in P2_old. A birational morphism to a normal surface
   identifies the generic DVRs, so ord_D=ord_B on K0. Ramification in K/K0
   then makes B an old branch component. By hypothesis B is smooth, and
   D is an open subset of its smooth strict transform.
2. It is a point. Then the closure of D in Z' is an irreducible exceptional
   curve of psi'. Factorization into point blowups makes it smooth rational,
   so D is smooth too. The point may be at old infinity; these divisors
   must NOT be discarded because the old visible branch lines disappeared.

A curve dominating an old nonbranch curve cannot become ramified merely
by changing rational coordinates. Thus every new affine branch component
is smooth, including the exceptional ones.

There is at least one such component: otherwise purity of the branch
locus makes the connected normal finite cover Y'->A2_new everywhere etale.
Complex A2 has no nontrivial connected finite etale cover, contradicting
[K:K0]>1. These are the accepted characteristic-zero purity/covering inputs,
not a new proof of them or a smoothness assumption about Y'.

## 4. Attachment to a hypothetical whole-plane Keller source

Suppose an embedding as in Section1 exists, and identify K0 subset K subset
L=C(x,y). Let F=(p',q') be the hypothetical polynomial Keller map.
For a branch component D above, choose a ramified valuation v of K over
ord_D. Any extension w to L satisfies

    e(w/ord_D)=e(w/v)*e(v/ord_D)>1.

If F were proper over a neighborhood of the generic point of D, its
quasi-finiteness and properness would make it finite there, and its Keller
condition would make that finite map etale. Its normal source ring is then
the full normalization in L. All valuations over ord_D would have index
one, a contradiction. Hence D is an irreducible component of the actual
nonproper-value set of F, not an unrelated marked curve.

We consume the classical polynomial-coverage and no-A1-component results:
every nonproperness component of a polynomial plane map is polynomially
parametrized, while a nonsingular polynomial plane map has no such component
isomorphic to A1. For the latter, see Nguyen Van Chau,
[0710.5212v1](https://arxiv.org/pdf/0710.5212), October27,2007, printed page3,
equation(1.4), its following paragraph and Theorem1.2. The introduction
also states the polynomial coverage input, credited there to Jelonek.
These are existing campaign imports; ROOT reread these selected primary
passages, not the whole proof dependency chain.

For completeness, polynomial parametrization makes the normalization A1:
the resulting nonconstant map A1->D lifts to the normalization and extends
to a finite map P1 onto its smooth projective completion. Riemann--Hurwitz
gives genus zero. Every point outside the affine normalization has its
nonempty preimage supported at the sole parameter infinity, so there is
exactly one such point. Since D is already smooth by Section3, D itself
is A1. This contradicts the no-A1-component theorem and proves Section1.

## 5. Product-cover attachment

For the displayed rational pair, R' is nonzero in characteristic zero and
t=qR'(s), so

    K=C(s,q),       K0=C(R(s),q),       [K:K0]=deg R=m.

The rational map R:P1_s->P1_p is a finite cover. Over finite p-values
outside its branch set, its product with the q-line is etale. Hence the
affine branch support of the normalization in K consists only of some
lines p=a, for finite branch values a of R. Passing from the affine target
to P2 can add only the line at infinity to the divisorial branch support.
All these projective lines are smooth, although they meet at infinity.
Thus the general theorem applies, without a Galois, small-degree, or
simple-critical-point hypothesis on R.

Direct differentiation gives J_(s,t)(R(s),t/R'(s))=1. The final exclusion
does not require the source substitution itself to be polynomial,
birational or constant-Jacobian: only the resulting whole-plane pair is
assumed polynomial Keller, and the field extension is finite.

## 6. Controls and historical comparison

Desk-only; no mathematical subprocess, CAS, numerical example or finite
word/degree search was used.

- The constant-Jacobian target restriction is essential to the smoothness
  argument. The birational map beta(u,t)=(t^2-u,t(t^2-u)) has inverse
  t=Q/P, u=(Q/P)^2-P, but J(beta)=u-t^2=-P. The old line u=0 maps to
  the singular cusp (P,Q)=(t^2,t^3). Thus arbitrary birational changes
  CAN singularize the affine image of a smooth line.
- tau(u,v)=(u+1/v,v) has Jacobian one and genuine affine poles. Its
  projective form [uv+1:v^2:v] is defined on every finite (u,v), and
  v=0 maps to [1:0:0]. No-affine-projective-indeterminacy is not a claim
  of polynomiality or an affine automorphism.
- For degree-one R the original pair is birational and may be the identity;
  nonempty affine branch is not forced. The theorem requires degree>1.
- A union of branch curves can have intersections even when every component
  is smooth. The proof needs componentwise smoothness only; it asserts
  nothing about the singularities of the whole branch union or of Y'.

Nearest history: September13 16:52 in notes.md excluded only the fixed
tau_c target repair for s-s^109, and today's12:31 operational selection
stopped the unsupported product-valuation attachment in arbitrary charts.
The present argument accounts for exceptional branch curves under a
constant-Jacobian target change; it does not recycle that false attachment.
The [positive-genus ramification filter](ramification-genus-birational-target-swarmHQ-root-20260915T152300Z.md)
allows arbitrary dominant rational target changes but needs positive source
residue genus. This theorem instead uses smooth projective BRANCH components
and constant-Jacobian birational targets; neither premise is replaced by
the other. The [fixed tripling filter](legendre-tripling-source-obstruction-swarmHQ-root-20260916T093800Z.md)
supplies the old nonproperness/no-line interface, not a claim that its entire
projective branch locus satisfies this theorem. No new attachment to that
elliptic donor is asserted. The rational-coefficient polynomial-in-fiber
donor theorem has a different fixed-target presentation.

## 7. Custody, limitations and next test

Native Astra was admitted19:15 with target19:24/HARD19:27. Actual startup
ACK19:15:14 supplied codex/node/apply_patch paths; exact hosted model ID
was not independently exposed. It was independently observed COMPLETED
before this report was written, before its target, after message-only
co-check of the graph descent, smooth strict transforms, exceptional branch
divisors and polynomial product-cover client. ROOT added the explicit
controls and states the equally direct rational-R product-cover client.
Same-model agreement does not promote any assertion.

ROOT read the whole positive-genus, rational-coefficient donor and fixed
tripling producer reports; history/frontier reads were selective. Source
and shared input hashes before writing:

    COORDINATION 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
    FALLACY-v2 e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
    APPROACHES ec2224e6edee202fa028ee2437af5c3cce9c7de545f1ae073dbbc6b48eca57f1
    AUDIT e12387bea2bfaea57ee6a099f984051f8351a6b88ed5b31ddce65e5e9fbf2988
    positive-genus a3a6793ba8f5c3ebccdd58e61ce8f1fa18ad4dd3d186950d2b961ac668a3a4b9
    fixed-tripling 26404af7ecee290db7d0ee68b1a5fed5d8cdd7f7c39f14f2255b007feea3ef1c
    rational-coefficient 5983d82682419aa836ebe9966f15a34eda927f2739365ad73fe6c72b17dbaa16

No sealed history, old artifact or protected project was modified. Source
queries were targeted, not a complete priority survey or broad-sweep round.
No proof of the stated result is claimed new to the literature.

Next test: one different-model hostile review of this frozen report,
especially affine graph descent, componentwise branch transport, the
exceptional case, and the rational-R client. No unreviewed descendant,
arbitrary nonconstant-J target search or new donor family is commissioned.
The general polynomial Keller construction problem and JC2 remain open.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13847`.
- Body SHA-256:
  `224c0536860ce8f4bf16786801f4a9bc95b288ac0bc51eba0bb08892dacd7143`.
- Frozen basis: `9aab38787eb24fffc86dacd5859f9c63d439959f`.
