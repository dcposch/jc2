# Singular normal source with one smooth ramification-support curve

2026-10-31. ROOT-MANUAL / UNREVIEWED candidate for a focused hostile check.
This tests the local smooth-source inference, not JC2 or actual Keller realization.

Let B=C[a,b,c]/(ac-b^2), X=Spec B, and E=V(b,c) in X. Set

    P=a^2+b,
    Q=3c+12ab+8a^3.

Claim: h=(P,Q):X -> A2 is finite flat of degree4, X is normal and singular at its origin, E is scheme-smooth A1, and the entire non-etale locus of h has reduced support E. Thus normality, finiteness over a smooth plane, and a single smooth reduced ramification-support curve do not force the source surface to be smooth.

## Direct algebra

Put A=C[P,Q] and introduce T. There is an exact presentation

    B = C[P,Q,T]/(f),
    f=T^4-6PT^2+QT-3P^2,
    a=T, b=P-T^2, c=(Q-12PT+4T^3)/3.

Indeed substitution gives 3(ac-b^2)=f, and the formulas for P,Q recover the original two functions. These mutually inverse presentations prove that the abstract polynomial ring C[P,Q] embeds in B. The monic quartic makes B free over it with basis1,T,T^2,T^3. In particular h is finite flat, dominant, and degree4.

The irreducible hypersurface ac-b^2 is a two-dimensional domain. Its gradient (c,-2b,a) vanishes only at the origin. A hypersurface is Cohen-Macaulay, and it is regular at every codimension-one point; Serre's criterion therefore makes B normal. At the origin its local embedding dimension is3 and its dimension is2, so X is singular there.

The relative differential module of the monogenic presentation is

    Omega_(B/A) = (B/(f_T)) dT,
    f_T=4a^3-12Pa+Q=3c.

Because h is finite flat, its etale locus is precisely D(c). Also

    sqrt((c))=(b,c),
    B/(b,c)=C[a].

Consequently its entire reduced non-etale support is the single smooth line E, including the singular origin. This checks the full support; no second ramification curve is suppressed. The non-etale scheme itself is V(c), not the reduced curve E.

At a generic point of E, a is invertible and c=b^2/a. Hence c has order2 along E. The transverse ramification index is3 in characteristic zero. Equivalently, using local coordinates (a,b), the ordinary Jacobian of (P,Q) is3b^2/a^2. This is consistent with a doubled ramification divisor and does not assert a reduced different.

The ideal of E at the origin is not principal: the classes of b and c are independent in (b,c)/m(b,c), so Nakayama's lemma requires two generators. Thus E is smooth as a curve but is not Cartier at the source singularity.

On E the image is (P,Q)=(a^2,8a^3), the cusp Q^2=64P^3. Its normalization parameter is a, so E maps isomorphically to the normalization of its reduced image. At the origin of the target the finite fibre has support only the source origin, since f specializes to T^4. The same construction therefore gives the proposed finite normal singular surface germ.

## Whole-source limitation and provenance

    B[c^(-1)] = C[b,c,c^(-1)], with a=b^2/c.

Thus X minus E is A1 times G_m, not A2: c is a nonconstant unit. This defeats only the proposed local smoothness lemma. It does not realize the WHOLE polynomial Keller source, rule out ambient singularities in the actual normalization, or imply a JC2 counterexample.

The construction comes from the already recorded finite rank-zero donor by a=u^2,b=uv,c=v^2. Its functions P=u^4+uv and Q=3v^2+12u^3v+8u^6 are invariant under (u,v)->(-u,-v). The direct algebra above proves the new candidate without requiring an unproved quotient assertion. The canonical parent is `/home/ubuntu/jc2/xmodel/rank-zero-ramification-counterexample-swarmHQ-root-sol56-20261030.md`, SHA256 c1e6940e4f1174ee943205057edc045e246cd377d7e2566e8f78b031ed089b83, basis e84ee01e12a7713a59b72679308ecc1d44264c1a; ROOT read all126LF after seal verification. Its earlier whole-source and donor-repair stops remain.

Named standard foundations: hypersurface Cohen-Macaulayness, the Jacobian and Serre normality criteria, relative differentials for a monogenic finite algebra, finite-flat plus unramified implies etale, and tame DVR ramification in characteristic zero. No fresh source audit is claimed.

One fixed falsifier only. No parameter family, computational search, source-repair project, public promotion or follow-on construction is requested. Historical priority and novelty remain unassessed; the broad frozen routing search was lexical only. A hostile review must specifically check the monic presentation, normality, full reduced support, non-Cartier point and failure of the whole-A2 condition.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4538`.
- Body SHA-256:
  `6c93a7cfbee6b03de92397b15e2162f96754d9c4fdb68ea1fca24d4b9edd6f9e`.
- Frozen basis: `68e87443925f50914a6cbb858d9d2f061dbda8b3`.
