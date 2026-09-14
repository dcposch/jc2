# Exact extending volume does not supply a marked source coordinate

ROOT, September13 2026. MANUAL / PRODUCER-CHECKED, UNPROMOTED pending
different-model FIRST. This is a countercontrol to a proposed geometric
implication, NOT a Keller counterexample or a new degree frontier.

## Statement and role

There is a smooth normal affine surface Y with an open immersion
j:A2->Y, an affine-base A1-fibration, and a finite full-field-normalization
map e:Y->A2, for which the source form du wedge dv extends to a GLOBALLY
EXACT regular two-form on Y. Nevertheless NO nonconstant element of O(Y)
pulls back to a polynomial coordinate of this marked source plane.
The two-form has simple zeros precisely on the two omitted affine lines.

Thus exactness cannot repair the previously tested open-chart/ruling
shortcut. The omitted hypothesis is still the actual Keller pair; the
control's finite map has a NONCONSTANT source Jacobian. No classification
of actual Keller normalizations or arbitrary integral-coordinate theorem
is asserted. No automatic surface-family or boundary-depth successor.

## The actual ring and its charts

In R=C[u,v] define

    z=uv, a=u^2*v, b=u*v^2, c=u^3*v-u, d=u*v^3-v,
    B=C[z,a,b,c,d] subset R,       Y=Spec B.

B means this ACTUAL image subring, not an ideal asserted without saturation
to be its whole presentation. The following identities suffice for every
localization below:

    ab=z^3,              zc=a(a-1),          zd=b(b-1),
    bc=(a-1)z^2,         ad=(b-1)z^2,
    cd=z(a-1)(b-1).

On D((a-1)(b-1)), the elements u=c/(a-1), v=d/(b-1) recover the source
coordinates, uv=z, uz=a, vz=b. Hence this localized B equals
C[u,v,((u^2*v-1)(u*v^2-1))^-1]. This is a genuine ring equality.

The first additional plane chart has coordinates (t,s) and generator values

    a=1+ts, z=t*a, b=t^3*a^2, c=s, d=t^2*a*(b-1).

On t!=0 it is the original plane via u=t^-1, v=t^2+t^3*s.
Its image is D(a) union D(c): inverse t=z/a on D(a), t=(a-1)/c
on D(c), and s=c. The identity zc=a(a-1) makes these inverses agree.
The other displayed identities recover b and d on both opens. Conversely
a=1+ts and c=s never vanish simultaneously, so the entire plane chart,
including t=0, is present. In particular

    B[c^-1]=C[t,c,c^-1].

Interchanging (u,a,c) and (v,b,d) gives a second whole plane chart (r,q):

    b=1+rq, z=r*b, a=r^3*b^2, d=q, c=r^2*b*(a-1),
    v=r^-1, u=r^2+r^3*q on r!=0.

Its image is D(b) union D(d). The three opens D((a-1)(b-1)), D(a),
D(b) cover Y, so these ring calculations prove Y is smooth. B is already
an integral ring with fraction field C(u,v), hence Y is normal.

At z=0, the identities imply (a,b)=(0,0),(1,0), or (0,1).
The latter two loci are exactly disjoint affine lines

    E1: z=0,a=1,b=0,d=0, c arbitrary;
    E2: z=0,a=0,b=1,c=0, d arbitrary.

The first locus lies in D((a-1)(b-1)). On z!=0, u=a/z and v=b/z
recover all points of the source. These inverses prove the polynomial
source map j is an ISOMORPHISM onto Y minus(E1 union E2), not merely
generically injective. No extra component is silently discarded.

Since B[c^-1]=C[t,c,c^-1], c:Y->A1 has an A1 fiber for every c!=0.
It is therefore an affine-base A1-fibration. Its restriction to the source
over c!=0 is G_m, parametrized by u!=0, v=(c+u)/u^3. The missing E1
point fills u=infinity. No assertion that every special fiber is reduced
or irreducible is used.

## Exact form, on all three charts

Take beta=-v du on the source, so d beta=du wedge dv. On the (t,s) chart
and the (r,q) chart respectively its rational expression becomes

    beta1=(1+ts)dt,
    beta2=-(2+3rq)dr-r^2 dq.

Both are regular on their ENTIRE planes. They agree with beta on the
dense overlaps, so they glue to a global regular Kahler one-form on Y.
Their derivatives are

    omega1=-t dt wedge ds,       omega2=r dr wedge dq.

Consequently omega=d beta is globally exact, j^*omega=du wedge dv, and
div(omega)=E1+E2 with multiplicity one. This is actual exactness, not just
extension, vanishing of one selected period, or a Jacobian-module identity.
Affineness makes the glued form a member of the algebraic module Omega_B^1;
no assertion that it has the special form f dg is made.

## No extending coordinate, without a degree bound

Let H in B be nonconstant of source total degree D. Along E1 the source
substitution is u=t^-1, v=t^2(1+ts). Thus a monomial u^i v^j has
valuation -i+2j at the generic point of E1. A pure u^D term would have
valuation -D, strictly below EVERY other monomial with i+j<=D. It could
not cancel, contradicting regularity of H on Y. Its coefficient is zero.
The symmetric E2 argument excludes a pure v^D term.

Therefore H's highest homogeneous form is divisible by uv. For every
constant h0, the projective closure of H=h0 contains the two DISTINCT
infinity points [1:0:0] and [0:1:0]. If H were a polynomial coordinate,
the inverse plane automorphism would polynomially parametrize H=h0 by A1.
That parametrization extends to P1->P2; its entire infinity set is the
image of the single parameter infinity. This contradiction excludes every
polynomial source coordinate from B. It uses no finite support envelope
or unproved classification of coordinate degrees.

## Literal finite normalization and the failed Keller hypothesis

The elements c,d are algebraically independent: after localizing at c,

    d=t^2*(1+tc)*(t^3*(1+tc)^2-1)

is a degree-eight polynomial in t over C(c), with leading coefficient c^3.
The identity

    z^8-z^5-2cd*z^4-(c+d)*z^3-cd*z+c^2*d^2=0

is MONIC in z. It follows by putting S=a+b in
zS=z^4+z-cd and S^2-S-2z^3=(c+d)z, then multiplying by z^2;
the resulting identity is polynomial also at z=0. Since a^2-a=cz and
b^2-b=dz, B is finite over C[c,d]. Normality and Frac(B)=C(u,v)
identify Y with the full-field normalization of that target plane.
The actual generic degree is eight by the displayed polynomial in t.

But on the original source

    J(c,d)=(3a-1)(3b-1)-u^3*v^3
          =1-3a-3b+8z^3,

which is NOT constant. For instance on u=1 it equals 1-3v-3v^2+8v^3.
Thus there is no Keller counterexample, despite exact volume, a finite
normalization, the whole plane chart and the affine-base ruling. This
degree-four-output map is a method control for the named GLOBAL implication,
not a classically open low-degree source or a reason to recheck any bound.

## Checks, priority and scope

ROOT's inexpensive first test applied volume extension to the previous
control ab=z(z-1)(z-2): its natural da wedge dz/a also pulls back to
du wedge dv, but exactness was not supplied. The construction above instead
glues two opposite zero-residue Wright-type charts and proves exactness
directly. It is not an enlargement of the parked S/T scalar or finite-r
calculation, and it supplies no pair on this surface.

WHOLE local inputs: full-normalization-ruling-astra-20260913.md,
SHA5585d8b34b45552330a95950fd01c4907f70527ea5d5f9c3b10b016ae5e160ce,
and source-volume-residue-integration-root-20260911.md,
SHA91ce3ee72fcdf88091806a9c7990f0c0be48006c45b42930272f5bc1a34f5eb8.
Canonical/source-title and selected exact-expression searches found no
prior instance of the combined five-generator control. A wider exact-text
hit in sol-wtc1-round2.md is a one-sided expression, not charged mathematics.
This is bounded history discovery, not an exhaustive literature-novelty claim.
The explicit proof above imports neither a Wright classification nor a
source-ruling theorem. Primary-host web discovery returned no consumed
closing theorem; snippets/citation lists are not mathematical evidence.

QUANTITY: does exact volume extension force a marked source coordinate
under the stated affine/ruling/normalization hypotheses?
CHEAPEST TEST: the two-chart valuation/primitive calculation above, completed
manually in this tranche. Outcome REFUTED for those combined hypotheses;
the actual everywhere constant-Jacobian condition remains essential and
unresolved. No global source exclusion, JC2 result or automatic successor.

No scientific interpreter, CAS, worker or verification computation ran.
This report uses apply_patch and the unchanged administrative finalizer.
The producer checked each inverse, all generator substitutions, both form
derivatives, the unique-extremal-monomial argument, the monic eliminant and
the explicit nonconstant Jacobian. Different-model FIRST is still required
before mathematical promotion. Whole draft/postpin readback precedes the
completion marker and immutable publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8481`.
- Body SHA-256:
  `766b0006603da80ab6dab06dee571dfdb54d0c4d05313b4ec978d13c04f9dc2a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
