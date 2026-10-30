# PROJECTIVEBASE2305 — a marked projective-base ruling of an affine plane extension

Status: INTERNAL / ROOT-MANUAL / UNREVIEWED. This is a general affine-extension lemma, not a Keller-specific exclusion or a novelty claim. It does not supply a regular affine coordinate on the extension. Standard finite-morphism/graph facts are named explicitly below; no new external source is adopted.

Let X=Spec B be a normal integral affine surface over C with a specified dense open immersion j:U=Spec R=A2 -> X, where R=C[x,y]. Identify B with its subring of R. Choose a nonconstant b in B. For a generic source linear coordinate ell, choose a complementary linear coordinate v so that the top homogeneous part of b is nonzero in the v-direction. After dividing by a nonzero constant, b is monic in v. Hence

    R is finite over C[b,ell], and therefore finite over B[ell].

Consider G=(j,ell):U -> X x A1. Its coordinate-ring map B[T] -> R sends T to ell, and the preceding finiteness makes G finite. Since j is an open immersion, G is the graph of a regular function on an open subscheme of X and is an immersion. A finite immersion is a closed immersion. In particular the ring map B[T] -> R is surjective, giving the additional equality

    R = B[ell].

Let Gamma be the reduced scheme-theoretic closure of G(U) in X x P1. Its projection p:Gamma -> X is projective and birational. Over U it is exactly the graph of ell. Since G(U) is already closed in X x A1,

    Gamma intersect (X x A1) = G(U).

The proper image p(Gamma) is closed and contains dense U, so it is X. If a point a lies in X minus U, every point of p^-1(a) lies over the sole point infinity of P1: otherwise it would belong to G(U). Thus every geometric fibre of p has one point as its support; over U the fibre is likewise one point. As p is of finite type, it is quasi-finite. A proper quasi-finite morphism is finite. Because Gamma is integral and p is finite birational onto normal X, p is an isomorphism.

The second projection therefore gives a morphism q:X -> P1 satisfying

    q|U = ell,              q^-1(A1) = U.

If E=X minus U is nonempty, q is surjective. Every fibre q^-1(c) for finite c is the actual reduced coordinate line {ell=c} in U, hence isomorphic to A1. The fibre q^-1(infinity) is an effective Cartier divisor with support exactly E. No connectedness, reducedness, smoothness or multiplicity bound for that fibre is asserted. Nor are individual components asserted Cartier.

For the actual finite normalization A=C[P,Q] subset B subset R of a hypothetical plane Keller map, the existing open-immersion package permits the lemma with b=P. Thus a generic source linear coordinate marks such a projective-base ruling of the actual X. The graph construction does not use the constant-Jacobian identity after that package is supplied, and applies more generally to any normal affine extension of a plane.

This is compatible with the retained non-Keller surface B=C[a,b,z]/(ab-z(z-1)(z-2)) and marked plane a=u(uv-1), b=v(uv-2), z=uv. For ell=u+v, the formulas u=a+b-ell*z+2*ell and v=ell*z-ell-a-b directly show R=B[ell]. The old report proves that B contains no source polynomial coordinate at all. There is no conflict: ell extends to P1, not to A1 on all X.

The remaining Keller implication is to exclude a nonempty infinity fibre using the actual constant-Jacobian finite map X->A2. Projective-base ruling, the effective Cartier combination of its components, and R=B[ell] do not provide that exclusion. In particular they do not make ell integral over A or regular on X; they do not imply N=1, surjectivity, properness of the original map, or JC2. Existing complete-base/degenerate-fibre stops remain binding; no classification farm follows.

Named standard foundations: a finite immersion is a closed immersion; closure commutes with restriction to an open subscheme; a proper morphism has closed image; finite-type morphisms with finite geometric fibres are quasi-finite; proper quasi-finite morphisms are finite; a finite birational morphism from an integral scheme to a normal integral scheme is an isomorphism. No surface classification or local-to-global regular-coordinate theorem is used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4210`.
- Body SHA-256:
  `0009790aec1450b97bd80e89515345f47c5ef0798983f75fab390faffbf2fc2f`.
- Frozen basis: `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
