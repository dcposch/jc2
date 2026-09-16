# Equal-degree factorization after scaling quotient is finite

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra same-model co-check.
Date: September 16, 2026. Basis: d748bf2636c58fdb551edbfaa5bdf8d13185c3e7.
Evidence: MANUAL, using the standard triviality of connected finite etale
covers of complex A2. Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending FIRST.
Claim: EQUAL-DEGREE-RESULTANT-QUOTIENT-1. JC2 remains unresolved.

## Statement

Work over C. Fix k>=1, and let V_k be the vector space of degree-k
homogeneous binary forms, including the zero form. On V_k x V_k use

    lambda.(L,Q)=(lambda L,lambda^-1 Q).

The resultant is invariant because the degrees are equal. Define the
affine quotient

    Y_k = {Res(L,Q)=1} // G_m,

and its product map rho:Y_k->V_(2k), [L,Q]->LQ. For ANY polynomial map
H:A2->V_(2k), let X_H=Y_k x_(V_(2k)) A2, with projection pi to A2.
Every reduced irreducible component Z of X_H which dominates A2 maps
ISOMORPHICALLY onto A2 under pi.

No affineness-in-coefficients, immersion, injectivity, degree or nonzero-value
hypothesis on H is required. There need not be a dominating component.
The assertion concerns the literal affine scaling quotient and literal
scheme base change, not an unspecified rational quotient or parameter chart.

Consequently this architecture cannot create a nontrivial plane Keller
map by recognizing a dominating component as the whole source plane.
If an arbitrary source parametrization into Z is allowed instead, pi|Z
is already an isomorphism: the entire Keller problem lies in that initial
parametrization, not in a new covering degree contributed by the quotient.
No conclusion about arbitrary Keller sources follows.

## Prior scope and purpose

The [unequal-degree affine-plane theorem](binary-form-affine-plane-obstruction-swarmHQ-root-20260916T053400Z.md)
and [its independent review](binary-form-affine-plane-review-swarmHQ-sol-20260916T053900Z.md)
explicitly exclude equal degrees and nonlinear product surfaces from their
scope. Their multiplication differential has a one-dimensional scaling
kernel, but the resultant changes along it when the factor degrees differ.
Here that kernel survives on Res=1, motivating a continuous quotient to
reduce dimension. The decisive distinction is that the quotient restores
global finiteness; no degree scan or repeated affine-slice test is involved.

The older theorem is history, not a mathematical premise. Its whole
producer was read, full SHA256
862d220b14eaff712e7c5e92a98d02231dd86ce013d4c1208a0df80666f216e6.
Targeted campaign and external discovery found no literal quotient result
being consumed here. This is not an exhaustive priority search or a claim
that the elementary Segre/invariant-theory mechanism is novel.

## 1. The exact quotient ring

Write L=sum_(i=0)^k l_i X^(k-i)Y^i and
Q=sum_(j=0)^k q_j X^(k-j)Y^j. In the polynomial coefficient ring S,
l_i has scaling weight1 and q_j weight-1. Every weight-zero monomial
is a product of l_i q_j. Therefore

    B=S^(G_m)=C[l_i q_j] = C[z_ij]/(all 2x2 minors),
    C_k=Spec B.

This is the rank-at-most-one matrix cone (the affine Segre cone).
Its nonzero complex points are exactly nonzero decomposable tensors L x Q,
and two pairs giving the same such tensor differ by opposite scaling.
The usual determinantal presentation can also be seen by localizing at
any nonzero z_ij and recovering all other entries from its row and column;
the image ring definition B=C[l_i q_j] is the ring used throughout.

The polynomial Res(L,Q) has bidegree(k,k), hence belongs to B; denote it
by r. Taking weight zero in S/(r-1) gives exactly B/(r-1): the ideal is
homogeneous for the scaling weights, and its weight-zero part is (r-1)B.
Thus Y_k=Spec(B/(r-1)). All its points have L,Q nonzero and coprime.
Here the quotient is geometric, not just a generic identification:
fixing a nonzero l_i gives a unique representative with l_i=1 locally.

## 2. Multiplication of the full cone is finite

Give each z_ij degree1 and put

    h_a=sum_(i+j=a) z_ij,       0<=a<=2k.

These are the product coefficients and define mu:C_k->V_(2k).
The common zero set of all h_a in C_k is just the vertex. Indeed a
nonzero rank-one tensor comes from nonzero forms L,Q, whose product
cannot be zero in the polynomial domain C[X,Y]. By the Nullstellensatz,
B/(h_0,...,h_(2k)) is finite-dimensional over C.

Choose finitely many homogeneous representatives of a vector-space basis
of that quotient. Induction on graded degree expresses every element of
B as a C[h_0,...,h_(2k)]-linear combination of these representatives:
after subtracting a representative, the remainder is a sum of h_a times
elements of one smaller degree. Hence B is FINITE over the product
coefficient ring. In particular mu is finite even at the cone vertex.
Every degree-2k complex binary form factors into degrees k,k, so mu is
surjective and the h_a are algebraically independent. Only finiteness is
needed in the sequel. Restricting to r=1 preserves finiteness of rho.

This is an affine, full-cone argument. Properness of a projectivization
alone has not been silently substituted for affine finiteness.

## 3. The ambient multiplication map is etale where r!=0

At a coprime pair the differential of multiplication is

    (dL,dQ) |-> Q dL+L dQ.

If it vanishes, coprimality forces dL=cL and dQ=-cQ, since both
factors and their variations have the same prescribed homogeneous degree.
Its kernel is exactly the scaling tangent. Quotienting removes this
one-dimensional kernel. The nonzero cone is smooth: it is the quotient
of the two nonzero coefficient vectors by free opposite scaling, with
the explicit local sections just described. Its dimension and that of
V_(2k) are both 2k+1. The descended differential is an isomorphism,
so mu is etale on D(r).

IMPORTANT: rho:Y_k->V_(2k) is finite and unramified, but is NOT etale
as a map to the full product space: imposing r=1 drops dimension by one.
The proof below uses etaleness of the AMBIENT mu, not that false statement.

## 4. Dominating components of an arbitrary base change

Let W=C_k x_(V_(2k)) A2. It is finite over A2, though it need not
be smooth or reduced everywhere. Its open V=D(r) is etale over A2,
so V is smooth of pure dimension2 and its irreducible components are
disjoint open-and-closed regular surfaces. The scheme X_H=V(r-1)
inside W is closed in W and lies wholly in V.

Take a reduced irreducible component Z of X_H dominating A2. Because
W is finite over A2, Z has dimension2. It is a closed irreducible
subset of the smooth pure-two-dimensional V, so it is an entire
irreducible component of V. On that component r-1 vanishes identically.
Thus its induced reduced scheme is this regular component, and Z->A2
is etale. It is also finite, being closed in W. Its image is nonempty,
closed and open in connected A2, so is all A2.

A connected finite etale cover of complex A2 is trivial (analytically
it is a finite covering of simply connected C2). Therefore pi|Z is an
isomorphism. This proves the claim even if other components of X_H are
lower-dimensional or nonreduced; none has been promoted into a source.
No immersion or transversality assumption on H was used.

## Controls and boundaries

- For k=1 take L=X+pY and Q=qX+(1+pq)Y. Their resultant is1 and
  H=qX^2+(1+2pq)XY+p(1+pq)Y^2 is a genuinely nonlinear coefficient
  family. It gives a section of X_H->A2 and a dominating component
  mapping identically to A2. Thus the conclusion is degree one, not
  nonexistence of all dominating components.
- For k=1, writing H=h_0 X^2+h_1 XY+h_2 Y^2 gives
  h_1^2-4h_0 h_2=r^2 on the cone. The r=1 quotient is a quadric
  surface, not an open subset of the three-dimensional product space.
  This directly checks the ambient-versus-slice etaleness distinction.
- Common-factor pairs have r=0; multiplication need not be etale there.
  Such points are excluded by the actual resultant-one equation, not
  discarded after selecting a convenient component.
- A whole base change need NOT be reduced or etale. For k=1 choose
  H(p,q)=(h_0,h_1,h_2)=(p^2,1,-1/4). Substituting r=1 into the cone
  equation gives p^2=0, so X_H=Spec C[p,q]/(p^2). This nonreduced
  nondominant example checks the necessity of the component/dominance
  qualification. It does not contradict etaleness of the ambient W
  along X_H, since X_H itself is cut out there by r-1.
- If H vanishes somewhere, its fiber in the cone is the vertex r=0.
  There can then be NO dominating Z: a finite etale Z would be surjective
  but the resultant-one fiber there is empty. No puncture is hidden.
- For unequal factor degrees j,k, the resultant changes by lambda^(k-j).
  Opposite scaling does not act on Res=1. This argument cannot replace
  the older unequal-degree theorem or its nonlinear-surface gap.

All calculations are manual. Standard inputs are the Nullstellensatz,
the etale differential criterion for smooth varieties, preservation of
finiteness/etaleness under base change, and the connected finite-cover
statement for complex A2. No scientific program, degree census, paid
execution, new exit-price assertion, general Keller-source reduction or
JC2 solution is claimed. QUANTITY: the generic degree of any dominating
component of this exact quotient construction; it must be1. CHEAPEST TEST:
the full-cone finiteness and regular-component argument above. No automatic
different quotient, larger-degree or nonlinear-source family follows.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9550`.
- Body SHA-256:
  `90030a3152c4089ec38184d1981b0f2ffe80bd118f07f709c3db8d05f676d269`.
- Frozen basis: `d748bf2636c58fdb551edbfaa5bdf8d13185c3e7`.
