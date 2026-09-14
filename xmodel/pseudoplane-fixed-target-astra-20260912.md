# Iterated scalar pairs: the exact fixed nonproper target

Author: Astra geometry. MANUAL / UNREVIEWED, not promotion.
First action 2026-09-12 02:21:47 UTC; original reserve02:41/HARD02:44
unchanged. Sole TASK SHA38d2a3c0528758d0060a5fcf2aabcb9777bdd0e68348c91619f415b197206937
matched before FRESH_WHOLE. No additional scientific input.

## The elementary covers and missing lines

Assume precisely the COMPLETE regular pair F=(h,g):S->A2 with
dh wedge dg=c Omega, c nonzero. The following conclusions are conditional
on that unconstructed pair. Over C put

    S: U²=A+A²Z,        T: t²-1=x²Z,
    q(x,t,Z)=(x²,xt,Z),
    j(A,U,Z)=(2U,1+2AZ,Z),
    i(x,y)=(x,1+x²y,2y+x²y²).

The displayed surface equations are smooth. The map q is the quotient
by (x,t,Z)->(-x,-t,Z): the invariant generators are x²,xt,Z since
t²=1+x²Z. The involution has no fixed point, so q is finite etale of
degree2. Finiteness also follows directly from the monic equations for
x and t over the target ring.

For j, the inverse has U=x/2 and
A=(t-1)/(2Z) where Z!=0, or A=x²/[2(t+1)] where t+1!=0.
These expressions agree on the overlap and show that its image is exactly
T minus M_-={Z=0,t=-1}. For i, the inverse is y=(t-1)/x² where x!=0,
or y=Z/(t+1) where t+1!=0. Thus its image is exactly T minus
D_-={x=0,t=-1}. These missing lines are distinct, meeting only once.

The form omega=dx wedge dt/x² extends across x=0 as
dx wedge dZ/(2t), and is invariant under the involution. It descends to
the nowhere-zero Omega on S. On A!=0, Omega=dA wedge dU/(2A²).
Substitution and the surface relation give j*omega=2Omega and
i*omega=dx wedge dy. Hence pi=q i and E=q j are etale, with
pi*Omega=dx wedge dy and E*Omega=2Omega.

Write D_+={x=0,t=1} and M_+={Z=0,t=1}.
The two inverse images under q of L={A=U=0} are D_+,D_-;
q maps each isomorphically onto L. The two inverse images of
C={Z=0,U²=A} are M_+,M_-, again mapping isomorphically to C.
Consequently pi retains one sheet over L and both sheets elsewhere;
E retains one over C and both elsewhere. Both maps are surjective and
generically degree2, including surjectivity at C intersect L.
Explicitly

    E(A,U,Z)=(4U²,2U(1+2AZ),Z).

It fixes L pointwise and restricts on C, parametrized by U, to U->2U.
In particular E(L)=L and E(C)=C as entire sets.

## Composition and the entire nonproper target

Use TASK's escaping-sequence definition of S_f. First, if q:Y->Z is
finite and U=Y minus D is a dense open subset, then

    S_(q|U)=q(D).                                        (1)

For an escaping sequence in U whose q-images converge, properness of the
finite map supplies a subsequence converging in Y; its limit must lie in
D, since a limit in U would contradict escape. Conversely, approximate
any point d of D by points of U. Such a sequence leaves every compact
subset of U and its q-images tend to q(d). Open-immersion identifications
preserve compactness. Applying (1) gives the exact equalities

    S_pi=L,                   S_E=C.

This proves nonfiniteness of both maps and includes every point of the
omitted lines, not merely their generic points.

Composition lemma. For continuous morphisms between these affine complex
varieties, with f:X->Y SURJECTIVE and g:Y->Z arbitrary,

    S_(g f)=S_g union g(S_f).                            (2)

Indeed an escaping sequence x_n with g(f(x_n))->z has either a subsequence
for which f(x_n) converges to a point y of Y, or no relatively compact
subsequence. In the first case y lies in S_f and z=g(y); in the second,
f(x_n) escapes Y and z lies in S_g. Conversely every point of g(S_f)
has its defining escaping sequence. For z in S_g, lift each point of a
defining escaping sequence y_n through surjective f. Any chosen lifts
escape X: the image of each compact subset of X is compact in Y.
Their g f-images converge to z. This proves BOTH inclusions. It needs
neither properness of f nor surjectivity or properness of g.

Set H_k=E^k pi. They are all surjective. By (2),
S_H0=L and S_H(k+1)=C union E(S_Hk). The invariance just checked yields

    S_Hk=C union L  for every k>=1.

Define F_k=F H_k. Applying (2) once more, now with g=F, proves:

    S_F0 = S_F union F(L),
    S_Fk = S_F union F(C union L)   for EVERY k>=1.        (3)

No closure or exceptional-point correction is omitted. Generally S_f
is closed: use a compact exhaustion of the source and diagonal choices
from defining escaping sequences for a convergent sequence of values in
S_f. Here F(C) and F(L) are also closed. Each restriction is a nonconstant
polynomial map from A1, since F is etale. One nonconstant coordinate is
a proper polynomial A1->A1, which forces every convergent image sequence
to have bounded parameters and hence a preimage limit. Thus all sets in
(3) are already closed; F need not be finite or surjective on S.

## Conditional degree consequence and its limit

The scalar-pair hypothesis makes F dominant etale and generically finite;
write d=deggeo(F)>=1. Pullback of its two-form gives

    J(F_k)=2^k c,          deggeo(F_k)=2^(k+1)d.

Thus (conditional on F) the polynomial-plane Keller maps F_k have
unbounded geometric degrees, with ONE nonproper target set for k>=1.
These degree computations use multiplicativity of function-field degrees,
not finiteness of the morphisms. No F is supplied by this argument.

DEGREE-BOUND GAP: (3) supplies no uniform bound on the degrees of plane
Keller maps with that target set. Such a bound would be an additional
theorem, not a consequence established here. Finite generation of a
fundamental group alone does not bound finite indices (already Z has
arbitrarily large finite indices); Noetherianity and a fixed number of
support components do not bound covering multiplicities. Finite-morphism
descending-chain assertions cannot be applied to the nonfinite E or pi.
An Euler calculation would still require the source and multiplicity data
that target-set equality has not fixed.

One precise uncontrolled datum is the divisorial ramification indices of
the normalization of the target in the function-field extension of F_k.
No bound on those indices is proved, and no growth of them is asserted.
The finite normalization covers have the displayed varying degrees;
they must not be confused with their common nonproper target support.
The maps and monodromies are not identified by (3). Their images happen
to equal F(S), but that follows separately from surjectivity of H_k,
not from equality of nonproper sets.

Control: E itself is a surjective nonfinite etale selfmap of S, not of
A2. Taking the identity on S in the composition lemma merely recovers
S_Hk; it does not satisfy or replace the stipulated pair S->A2.
This task proves neither existence of that pair, a degree bound, nor
any general JC2 conclusion. No novelty claim is made.

QUANTITY: exact equalities (3), including all points and closure.
CHEAPEST TEST: the finite-cover/open-immersion and escaping-sequence audit,
manual planned <=15 minutes; numerical/computational wall UNMEASURED.
No gap remains in the stated set formula, subject to independent review;
the separate degree-bound gap is explicit. No canonical OPEN, promotion,
resource request or descendant is created.

Own-only collision/scope check: report, manifest, PINS and custody were
initially absent. Only the leased report and own PINS/custody are authored;
TASK and all existing files are untouched. Final WHOLE readbacks, postpins,
marker-last transaction and exact expected verification are in custody.
No scientific execution, external input, peer, worker, protected tree or
shared edit was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7603`.
- Body SHA-256:
  `7332ac4a8a1cc1801a5099ff96e13b2f9674cf970d912d74824d8cb53b952982`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
