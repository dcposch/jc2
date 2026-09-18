# Same-quotient degree cancellation

Author: swarmHQ ROOT. Date: 2026-09-18. Status: UNPROMOTED / MANUAL,
pending different-model FIRST. No novelty or JC2-resolution claim.
Frozen public basis: cbf683543a193cf71003b7a9f435a0f240833da9.
Frozen HQ comparison basis: 22e1f70a4b376dd42bb8eeffcf6307018d53abeb.

## Exact changed test

The earlier [connected-quotient tower report](connected-quotient-tower-swarmHQ-root-20260916T155300Z.md)
allows different endpoint plane quotients but requires geometrically integral
generic fibers. Here there is ONE ambient self-map and the SAME quotient at
both ends. Relative constant-field degrees cancel, removing the generic-fiber
condition for this different construction. Selected history searches found no
exact statement; a broader degree-cancellation search clipped on unrelated
hits. This is not an exhaustive novelty determination. The proof below is a
classical field argument, not a claimed new field-theory theorem.

## Claim 1: field degree divisibility

Let E/C be a finitely generated field, M an intermediate field finitely
generated over C, and phi:E->E a C-field embedding. Suppose phi(M) is a
subfield of M, d=[E:phi(E)]<infinity, and e=[M:phi(M)]<infinity.
Then e divides d.

Proof. Let B be the relative algebraic closure of M in E. First r=[B:M]
is finite. Choose a transcendence basis t for E/M, so E is finite over
M(t), say of degree N. Every finite algebraic extension M'/M inside E
has [M'(t):M(t)]=[M':M], since t remains algebraically independent over
M'. Thus [M':M]<=N. Choose a finite subextension of maximal degree;
adjoining any further element of B cannot enlarge it, so it is B.

If b belongs to B, phi(b) is algebraic over phi(M), hence over M, and
lies in E. Therefore phi(B) is a subfield of B. The isomorphism phi
gives [phi(B):phi(M)]=r. The two towers above phi(M) give

    [B:phi(M)] = [B:M][M:phi(M)] = r e
                 = [B:phi(B)][phi(B):phi(M)] = [B:phi(B)] r.

Consequently [B:phi(B)]=e. Further, phi(B) is relatively algebraically
closed in phi(E): pull an algebraic element back by phi to an element
of E algebraic over B, hence algebraic over M, hence in B.

Put K=phi(B) and L=phi(E). An irreducible polynomial over K remains
irreducible over L. Indeed, inside an algebraic closure containing L,
coefficients of a monic factor are symmetric expressions in a subset
of its roots, so are algebraic over K. If these coefficients lie in L,
relative algebraic closedness forces them into K, contradicting
irreducibility for a proper factor. Since characteristic is zero, the
finite extension B/K has a primitive element. Its minimal polynomial
therefore has the same degree over L, yielding

    [B L:L] = [B:K] = e.

The fields L subset B L subset E then give

    d = [E:B phi(E)] e.

This proves the divisibility. In particular, this is NOT an assertion
that arbitrary compositum degrees divide the initial degree: relative
algebraic closedness of phi(B) in phi(E) is the needed hypothesis here.

## Claim 2: geometric specialization

Let X be an integral complex variety, Phi:X --> X a dominant rational
self-map of generic degree d, and rho:X --> A^2 a dominant rational
map. Let h:A^2 --> A^2 be dominant and generically finite, with

    rho composed with Phi = h composed with rho

as rational maps. Then deg(h) divides d, with NO geometric-integrality
or connectedness assumption on the generic fiber of rho.

Apply Claim 1 to E=C(X), M=rho* C(u,v), and phi=Phi*. Dominance embeds
the function fields; the identity identifies [M:phi(M)] with deg(h).
All finite-generation and finite-degree hypotheses are satisfied.

## Claim 3: conditional Keller consequence

If h is a polynomial Keller map of the plane and d belongs to {1,2,3},
then h is an automorphism, using the campaign's accepted whole-mapping-
degree 2 and 3 exclusions and birational Keller theorem. These are named
imports, not re-proved foundations. See the premise separation in
[the low-fiber transfer gate](low-fiber-tower-transfer-gate-sol-20260913.md).
No second-leg block exclusion is needed for this SINGLE-self-map result.

For d=1 the descended degree is 1. For d=2 or 3, divisibility gives
degree 1 or the same prime, and the accepted exclusions finish.

## Controls and exact limits

1. Disconnected quotient permitted: X=A^3, rho(x,y,z)=(x^2,y),
   Phi(x,y,z)=(x^3,y,z), h(u,v)=(u^3,v). The geometric generic fiber
   of rho has two components and d=e=3. This h is NOT Keller; its
   Jacobian is 3u^2. The field claim does not assume Keller.
2. Pure vertical degree permitted: with the same rho, take
   Phi(x,y,z)=(x,y,z^3) and h=id. Then d=3 and e=1.
3. SAME quotient matters. Take Phi=id, rho_s=(x,y), rho_t=(x^r,y),
   h(u,v)=(u^r,v), r>1. Then rho_t Phi=h rho_s but d=1 and e=r.
   Again h is non-Keller. Different quotient maps do not satisfy Claim 2.
4. If only Phi^k preserves rho, the argument gives deg(h) divides d^k,
   not deg(h)<=3, nor an intermediate polynomial target factorization.
   Arbitrary low-degree towers are NOT excluded by this statement.
5. No quotient rho or ambient Phi is constructed for an arbitrary Keller
   map. Arbitrary projections, embedded-plane restrictions, and two
   unrelated endpoint quotients do not meet the premise. There is no
   global JC2 reduction here.

## Exit and custody

Exit price: one self-contained conditional divisibility argument and
explicit scope controls, for independent FIRST review. No source search,
CAS, cloud job, reproof of accepted degree bounds, or automatic successor.
This report has no OPEN labels and imports no unreviewed historical claim.
## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The collision checker returned this result before sealing. It checks label
collisions, not mathematical validity or literature novelty.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5850`.
- Body SHA-256:
  `a5d7b06398856a6a92296b787d998b69d5d165487ad5c9ddbd913b06662d9f56`.
- Frozen basis: `cbf683543a193cf71003b7a9f435a0f240833da9`.
