# Canonical contact reformulation: the missing step is global

ROOT manual discriminator, September12,2026,14:35UTC.
MANUAL/UNREVIEWED, not FIRST, no normality or JC2 conclusion.
One actual-source interface calculation and one local scope check; no
conductor-shape/degree/control-family expansion or descendant.

## 1. Exact actual-source contact vector

Assume R=C[x,y], J(f,g)=1, alpha=(xdy-ydx)/2,
dH=alpha-fdg, and B=C[f,g,H] finite birational with normalization R.
Let P(U,V,W) be its irreducible relation and c=P_W(f,g,H).
Write E=(x partial_x+y partial_y)/2 and omega=dx wedge dy.
The ambient contact form theta=dW+U dV pulls back to alpha, and
theta wedge dtheta=dW wedge dU wedge dV is nowhere zero.

Using the source bracket J(a,b) defined by da wedge db=J(a,b)omega,

    J(f,H)=E(f)-f,       J(g,H)=E(g).

Taking the bracket of P(f,g,H)=0 with f and g therefore gives

    c E(f)=f c-P_V,      c E(g)=P_U,
    c E(H)=-f P_U.

All P-derivatives here are evaluated at (f,g,H). Equivalently the
polynomial ambient vector field

    D=(U P_W-P_V)partial_U+P_U partial_V-U P_U partial_W

annihilates P and theta(D), so induces the characteristic derivation on
B. Its lift to R is exactly cE. The calculation includes the signs and
does not assume c is a unit. In particular, the induced regular derivation
on the singular graph is cE, NOT E. Dividing by c is precisely the missing
ring-preservation assertion; extending a rational foliation is weaker than
extending its particular Euler generator as a regular derivation.

The global cE has the same generic radial leaves, but vanishes along the
conductor. The already-reviewed conductor identity I=cR does not permit
division inside B. In fact cR subset B by the definition of conductor,
so the bare statement cE(B) subset B alone imposes no new obstruction.
The three displayed coefficient identities retain the special source
structure, but no argument here extracts unitness or E(B) subset B from them.

This is a reformulation, not a newly solved source constraint. The
previous radial finite-graph theorem supplies its hypotheses in a suitable
frame; it does not supply graph normality or finiteness of F.

## 2. A local nodal model survives radial normalization

This is a LOCAL analytic/formal control, not a whole-plane polynomial
counterexample to the stronger global Gorenstein question.
In target coordinates U,V,W consider the two smooth branches

    H_1=V+U,       H_2=V,
    P=(W-V-U)(W-V).

Near U=0 their union is an ordinary double hypersurface, with finite
unramified normalization by the two smooth branch germs. The local
dualizing module is free. Restriction of theta=dW+U dV gives

    alpha_1=(1+U)dV+dU,     alpha_2=(1+U)dV,
    d alpha_i=dU wedge dV.

Both restrictions agree on the common curve U=0. Each admits explicit
RADIAL symplectic coordinates near U=0:

    x_1=sqrt(1+U),  y_1=2*x_1*(V+log(1+U)),
    x_2=-sqrt(1+U), y_2=2*x_2*V.

Choose the convergent square-root and logarithm germs with values1,0 at
U=0; the same formulas make sense formally. For x=plus/minus sqrt(1+U)
and y=2x Z,

    (xdy-ydx)/2=x^2 dZ,       dx wedge dy=dU wedge dZ.

Putting Z=V+log(1+U) or V verifies BOTH displayed alpha_i and the exact
volume equality dx_i wedge dy_i=dU wedge dV. Thus the normalization
branches have literal radial forms in these local charts, yet the target
is not normal. The two source points at U=V=0 are (1,0) and (-1,0), not
the Euler origin. This does not identify two neighborhoods by a global
polynomial coordinate transformation.

Here c_1=P_W|_1=U,c_2=P_W|_2=-U. The branch radial fields in base
coordinates are E_1=(1+U)partial_U-partial_V and
E_2=(1+U)partial_U. Consequently E(c) has opposite values1,-1 on the
double curve. This is fully compatible with the reviewed paired identity,
not an example refuting it. The square roots/logarithm are explicitly
local; this control supplies neither a globally polynomial full-A2 source
nor an actual Keller map. It demonstrates why a proof must use global
polynomiality, not only local branch/dualizing/radial normal-form data.

## 3. Primary-source applicability check

Jiang, Truong and Zung, "Normalization of Singular Contact Forms and
Primitive 1-forms", Acta Mathematica Vietnamica, DOI
10.1007/s40306-024-00545-5:
https://link.springer.com/article/10.1007/s40306-024-00545-5.
ROOT read the Theorem1.2/1.3 statements and adjacent discussion, including
the formal, analytic and smooth categories and extra analytic hypotheses;
not the entire paper or all proofs. HTML SHA256 at14:33UTC:
426eb4320e86753772627b3b715ce1dc1a2f3242c25519955e7b83faac2bf696.
Their normalizations are LOCAL in the stated categories. They do not
provide a global polynomial conjugacy or normality of a finite singular
graph. The explicit control above needs no invocation of those theorems.
Eight targeted queries yielded no source-attached closing theorem; this
is not an exhaustive novelty search, broad sweep or proof of absence.

## 4. Disposition

Question tested: does expressing the canonical graph as a contact surface,
or applying local normalization to its characteristic foliation, discharge
global Euler descent? Answer: NO CLOSING IMPLICATION from this calculation.
The natural global derivation is conductor-multiplied; the local normal
form category survives a nodal control. This blocks those specific shortcuts,
not a genuinely global contact-geometric argument. No claim that the whole
Gorenstein/radial assertion is true or false follows.

History checksum: current APPROACHES/AUDIT/PROGRESS/ladder REDUCTION and
named conductor/radial report names checked; old moving-section and
characteristic-p conductor clients have different objects. No direct prior
contact-vector/globality entry found in the canonical searches. This is
not exhaustive literature novelty. Native Gorenstein discriminator is
independent and LIVE; no peer output has been read or consumed.

Manual derivation and inert text/hash/document retrieval only. No
scientific interpreter/CAS/helper/import/AST/test, AWS or protected-tree
operation. Local report edits only via apply_patch in leased partial;
unchanged administrative finalizer. Own WHOLE checks precede marker LAST.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6213`.
- Body SHA-256:
  `7ea84a29a9deef2b51d37276093d5c25612c4e94e0917e3aca61a5eb1da1ee01`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
