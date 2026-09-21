# An actual additive quotient and a one-point scheme-neighborhood criterion

Producer: swarmHQ ROOT (gpt-6-astra; hosted identity not independently attested)
Date: 2026-09-21 UTC
Basis: ee7e771e975e0244ad33fb154da9fd793d97a0d6
Evidence tier: MANUAL with explicitly named classical imports
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model hostile FIRST

## Statement and scope

Work over C. Let F=(P,Q):A2_w -> A2_Y be polynomial with
det DF=c in C*, with no degree bound. On V=A5_(t,w1,w2,a1,a2), let
G=Ga2 act by

    Phi_b(t,w,a) = (t,w+t*b,a-(F(w+t*b)-F(w))/t).

The divided difference is polynomial, including at t=0. The following
claims concern this EXACT actual-source construction, not arbitrary free
unipotent actions or arbitrary affine-plane fibrations.

1. This is a scheme-theoretically free polynomial action. Its invariant
   ring is C[t,Y1,Y2], where Y=F(w)+ta.
2. The fppf quotient p:V->X exists as an algebraic space and G-torsor.
   X is a smooth irreducible finite-type three-dimensional C-space with
   affine diagonal. The invariant map factors as q=h p, with h:X->A3_(t,Y)
   etale and birational. Over t!=0, h is an isomorphism. The special fiber
   X0 of pi=t:X->A1 is A2_w, and h0=F. Every geometric fiber of pi is A2.
3. F is an automorphism if and only if SOME point of X0 has a ZARISKI-open
   scheme neighborhood in X. Equivalently in this family, X is a scheme,
   X is separated over C, X is affine, the action is proper, or the displayed
   action is polynomially conjugate over (t,Y) to translation on the last
   two coordinates of A3 x A2.

Consequently, under hypothetical noninvertibility, NO point of X0 has a
scheme neighborhood. This does not deny existence of an etale scheme
chart: we give one explicitly. The existence of a scheme neighborhood,
separatedness, or action properness is NOT proved. JC2 remains unresolved.

## Dependencies and prior work

The action and quotient calculations were recorded internally on September20
at17:25:44 and19:27:23; the21:01:06 whole-portfolio synthesis repaired the
local-neighborhood proof and separated p,h,q,pi. Those were INTERNAL MANUAL
calculations and strategy, not a hostile FIRST or accepted public theorem.
This report makes the existing reduction auditable; it does not claim a
new positive mechanism or literature priority. The explicit chart below
is a direct proof device for the same quotient, not a new source family.

Standard named imports are fppf torsor descent, the Jacobian criterion
for etaleness, source/target locality and base change for etale morphisms,
and Zariski's Main Theorem. Two precise source anchors, checked September21:

- [Stacks, Lemma80.11.7, tag06PH](https://stacks.math.columbia.edu/tag/06PH):
  a free action of a flat, locally finitely presented group gives an
  algebraic-space quotient and an fppf torsor. Here G=Ga2 over C.
- [Stacks, Lemma37.43.3, tag05K0](https://stacks.math.columbia.edu/tag/05K0):
  a quasi-finite separated morphism to a qcqs scheme factors through an
  open immersion followed by a finite morphism. We use it only on schemes
  mapping to affine space, not on an unproved separated X.

Both displayed statements and their page proofs were read; their cited
dependency proofs were not re-audited. The birational-definition page
[tag01RN](https://stacks.math.columbia.edu/tag/01RN) was also checked,
not used as a stronger open-immersion theorem. No other search-result
statement is imported. The birational Keller endpoint is derived in
Section5 below from the named ZMT and elementary polynomial-ring facts.

## 1. Action and invariant ring

Taylor expansion, or polynomial division by t, proves regularity of Phi.
The divided differences telescope under composition, so Phi_b Phi_d is
Phi_(b+d), and Phi_(-b) is the inverse. The generating derivations are

    D_i = t partial_wi - P_wi partial_a1 - Q_wi partial_a2,  i=1,2.

They commute and are locally nilpotent because they arise from the two
commuting polynomial additive actions.

For scheme-theoretic freeness, work over an arbitrary C-algebra with a
putative stabilizer b. Its equations include t*b=0. Every Taylor term of
degree at least two in b in (F(w+tb)-F(w))/t has a factor t*b_j; modulo
those equations the remaining stabilizer equation is DF(w)b=0. The
matrix has a polynomial inverse since its determinant is c. Thus b=0
as a scheme-theoretic equation, including over nonreduced test rings.

Both t and Y=F(w)+ta are invariant. Inverting t gives

    O(V)[1/t] = C[t,t^-1,Y1,Y2,w1,w2],

with D_i=t partial_wi. Its common kernel is C[t,t^-1,Y1,Y2]. If an
invariant in O(V) had a minimal denominator t^k, k>0, write it as
t^-k H(t,Y) with H(0,Y)!=0. Reduction of t^k times that polynomial
invariant modulo t would imply H(0,F(w))=0. This is impossible since F
is dominant (its Jacobian is invertible). Hence k=0. Algebraic
independence of t,Y follows already after inverting t.

## 2. Quotient and the four morphisms

The free-action theorem applies to V and G. It gives the algebraic space
X=V/G and the fppf torsor p. Formation of this sheaf quotient commutes
with invariant base change. The invariant functions define

    p:V->X,   h:X->A3_(t,Y),   q=h p,   pi=t:X->A1.

Over t!=0 the coordinates (t,Y,s=w/t) identify V with
(Gm x A2_Y) x Ga2_s, and the action is s->s+b. Thus h is an isomorphism
there. At t=0 the action is (w,a)->(w,a-DF(w)b). The polynomial change
r=-DF(w)^-1 a identifies it with translation in r. It follows that
X0=A2_w, and its map to {t=0} in A3 is exactly F, not an identity map.

The affine diagonal assertion can be checked by pulling back along the
fppf cover p x p:V x V->X x X. The resulting morphism is

    G x V -> V x V,   (b,v)->(v,Phi_b(v)),

a morphism between affine schemes, hence affine. Affineness descends
fpqc locally on the target. This does NOT assert that the diagonal is
closed or that X is separated.

The torsor is smooth of relative dimension2. Smoothness of X over C
descends from its smooth surjective cover V; local finite type descends
as well. Quasi-compactness follows from surjectivity of V->X, and the
affine diagonal gives quasi-separatedness. Dimension is3. Irreducibility
follows from the SURJECTIVE continuous map from irreducible V, not just
from smoothness of q. In particular the nonempty open t!=0 is dense.

## 3. An explicit etale chart, not a scheme neighborhood

Let S=A3_(t,u1,u2) and map it into V by a=0,w=u. Compose with p to
obtain g:S->X. Its base change along the torsor p identifies with

    Theta:S x Ga2_b -> V,
    (t,u,b) |-> (t,z=u+tb, a=(F(u)-F(u+tb))/t).

The determinant of this five-variable polynomial map is c. To check
this on t!=0, first pass from (u,b) to (z=u+tb,u), of determinant t^2,
then from (z,u) to (z,(F(u)-F(z))/t), of determinant c/t^2. With t kept
as the first coordinate the result is c, and polynomial equality
extends to t=0. Thus Theta is etale by the Jacobian criterion. Faithfully
flat descent gives that g is etale. This is not an injectivity claim.

The restriction g0:S0->X0 is the identity on u. Therefore g(S), together
with the known open U=X[t^-1]=Gm x A2_Y, covers X. Including U is
important: surjectivity of F has NOT been assumed. On S we have

    h g(t,u) = (t,F(u)),

an etale morphism. On U, h is an isomorphism. Since g(S) and U form an
etale cover, h is etale everywhere. Its isomorphism over the dense open
t!=0 makes it birational. Its point fibers over (0,Y) are F^-1(Y);
this does not make h or F finite.

These computations also show that pi has A2 geometric fibers over
EVERY geometric point of A1. In contrast, q has fiber F^-1(Y) x A2_a
at (0,Y). Under hypothetical generic degree N>1 that is generically N
disjoint affine planes along t=0. Do not substitute these q fibers for
the fibers of pi, or identify an etale chart g with an open immersion.

## 4. A scheme neighborhood at one special point forces birationality

Suppose x is ANY point of X0 with a Zariski-open scheme neighborhood.
Choose an affine open V0 of that neighborhood containing x. It is an
open subspace of X. The restricted map h|V0:V0->A3 is etale, quasi-finite
and separated: the latter follows because both V0 and the target are
affine schemes. No separatedness of the rest of X is used.

Since X is smooth irreducible, V0 is integral. Every nonempty open of
X meets the dense open t!=0, so h|V0 is birational. Apply ZMT to get
V0 as an open subscheme of a finite A3-scheme T. Replace T by the
scheme-theoretic closure of this integral open, an integral finite
A3-scheme with the same function field. Its coordinate ring is a finite
integral extension of C[t,Y] inside C(t,Y), hence is C[t,Y] by normality.
Thus h|V0 is an open immersion.

Base change to t=0 now makes the restriction

    F|_(V0 intersect X0): V0 intersect X0 -> A2_Y

an open immersion. Its source is a NONEMPTY open of the irreducible
plane X0=A2_w, hence dense; its image is nonempty open too. It induces
C(w1,w2)=C(P,Q). Therefore F is birational. This restriction step is
why even a single scheme neighborhood suffices.

## 5. From birationality to automorphy; converse and properness

For completeness, apply the same ZMT/normality argument to a birational
Keller F:A2->A2. It is an open immersion onto an affine open W isomorphic
to A2. If A2-W had a divisor, a defining irreducible polynomial f of
one such divisor would restrict to a nonconstant unit on W, contrary
to O(W)^*=C*. Therefore A2-W has codimension at least2. A rational
function regular on W has no pole at any irreducible polynomial divisor,
so unique factorization implies it is polynomial on A2. Thus
O(W)=C[Y1,Y2]. The induced map on coordinate rings is an isomorphism,
so F is an automorphism. This argument does not invoke surjectivity of
an arbitrary Keller map or an unproved properness criterion.

Conversely, if G0=F^-1 is polynomial, put

    s = (w-G0(Y))/t,   Y=F(w)+ta.

The numerator vanishes at t=0, so s is polynomial on V. The inverse
coordinate change is

    w=G0(Y)+ts,   a=(Y-F(G0(Y)+ts))/t,

again polynomial by divisibility by t. In (t,Y,s), the action is
s->s+b. Its quotient is A3_(t,Y); hence X is affine, separated and a
scheme, and every point has a scheme neighborhood. The translation
action morphism is a closed immersion onto equal-(t,Y) pairs, so it
is proper.

If instead distinct u,v satisfy F(u)=F(v), the two arcs
(t,u,0) and (t,v,0) in V over C[[t]] satisfy

    Phi_((v-u)/t)(t,u,0) = (t,v,0)

over C((t)), but their required group parameter does not extend to
C[[t]]. Uniqueness follows from freeness. The action morphism is thus
not proper by the valuative criterion. If F is not birational, its
finite-etale locus over a nonempty target open supplies distinct complex
points in a generic fiber; no global finiteness is asserted. Consequently
proper action implies birationality, and hence automorphy.

Finally the action morphism is the base change of the diagonal of X.
If X were separated it would be a closed immersion and thus proper.
This completes every implication in the stated equivalences. The same
reasoning does not prove any of these equivalent positive conditions.

## Replay and negative controls

Desk-only polynomial and scheme-theoretic argument; no CAS, finite search,
modular evidence, numerical sampling or cloud computation.

Positive check: F=identity gives Y=w+ta and s=-a, so the displayed
translation coordinates and quotient are literal polynomial coordinates.

Hypothesis check: for the NON-KELLER map F=(w1^2,w2), the same displayed
action has a nontrivial stabilizer b1 at t=0,w1=0. The quotient-torsor
argument cannot be imported after dropping the constant-unit Jacobian.
This is not a Keller counterexample. The principal scope check is
internal to the exact family: an etale chart of X exists unconditionally,
whereas the claimed equivalence requires a Zariski-open scheme neighborhood.

## Limitations and next test

No scheme neighborhood is constructed, no properness is established,
and no counterexample F is supplied. All implications are conditional
uniform reductions or structural facts about the actual quotient. No
ordinary resolution-property, fixed-generator, cohomology-vanishing,
affine-fibration or Luna theorem is invoked to supply the missing premise.
There is no automatic new quotient family, classification or source search.

Next bounded test is one different-model hostile FIRST of this frozen
report, emphasizing arbitrary-base freeness, quotient base change,
the chart determinant and coverage, local ZMT hypotheses, and the special-
fiber restriction. Only a surviving reviewed result may be promoted.

## OPENS RAISED

None. The global positive premise is the retained JC2 gap, not a newly
commissioned source, classification, cohomology or construction task.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author whole-body readback completed 2026-09-21 01:25:51 UTC; only this
collision output and completion footer were subsequently added.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13014`.
- Body SHA-256:
  `dd57fcc5f09e476fba7ccc45585b40302ff471c035be2e4847a37cff974ed7d5`.
- Frozen basis: `ee7e771e975e0244ad33fb154da9fd793d97a0d6`.
