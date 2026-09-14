# D125: finite-arc obstructions constrain the closure boundary, not existence

2026-09-07. Root desk result, PROVISIONAL pending different-model review.
This is a theorem-interface composition of accepted14c/14f/14p/14q, not a
new global emptiness argument. It supplies explicit equations on the REDUCED
k=0 boundary of the k-saturated source, and an exact counter-control to
promoting those equations to the guarded source. No full source or CAS runs.

## 1. Literal rings and conclusion

Let S be the finite polynomial ring over Q in all coefficient coordinates
and k of the full normalized odd moving-face source14c. Let I contain every
unguarded source row. Do NOT include an inverse variable z or zk-1 here.
The optional whole B-shear gauge may be included; the formula below also
works without it. Put J=I:k^infinity, X=Spec(S/J), U=D_X(k).
Then X is the schematic closure of the k-nonzero part inside Spec(S/I).

Define actual coordinate polynomials

    H=A_(0,13)/3+3,
    y=A_(0,3), v=B_(0,15), w=B_(0,3),
    D=5y²+27(v+243)y−27w.

Claim at radical/set-theoretic scope only:

    H,D belong to sqrt(J+(k)).                       (C)

No exponent, explicit ideal-membership certificate, scheme reducedness, or
flatness is supplied. Neither H nor D is asserted to belong to sqrt(J).
In particular they must not be added to the k-nonzero solver input.
The pending tuned-center theorem is NOT a premise. If it is separately
accepted, the same argument would also give y,w in sqrt(J+(k)); that
conditional sentence is not promoted here.

## 2. Why an existing boundary point supplies a finite arc

Suppose q is a geometric point of X at k=0. The open U is dense by the
definition of saturation/schematic closure. Its inclusion is a finite-type
morphism because these schemes are Noetherian. The Noetherian valuative
image-closure lemma gives a discrete valuation ring A mapping to X, with
closed point q and generic point in U. Thus k maps to a nonzero element of
the maximal ideal. Source coordinates, unlike the omitted inverse z, are
all elements of A. This does not posit any q when the boundary is empty.

Primary source: [Stacks, Lemma32.15.1](https://stacks.math.columbia.edu/tag/0CM1),
statement and its complete short proof read September7 ~06:47UTC. Its
application is to U→X, not to a presumed proper map X→A1. No projective
compactification of X is assumed.

Complete A. Completion is injective for a DVR and remains a complete DVR
of equal characteristic zero. It is L[[s]] for a coefficient field L by
[Stacks, Lemma10.160.10](https://stacks.math.columbia.edu/tag/0C0S), whole
statement and proof read ~06:50UTC. The coefficient field contains Q;
no prescribed larger coefficient-field section is needed for these
rational source equations. This gives a genuine finite-coefficient source
arc with nonzero k(s) of finite positive order. Nilpotents in S/J do not
invalidate the argument: the map to a DVR kills them, which is why (C)
is a radical statement, not scheme equality.

The accepted generic theorem14p is stated with literal k=s^m. To apply it
here, write k=s^m u(s) with u0≠0. After a finite field extension adjoining
an mth root of u0, the recursive coefficient equation v(s)^m=u(s) has a
unique solution with the chosen nonzero constant: its next scalar pivot
is m*v0^(m−1), a unit in characteristic zero. The parameter tau=s*v(s)
has an invertible linear term, hence admits a formal compositional inverse.
Transporting the coefficient series gives k=tau^m and preserves all
rational source identities, their finite supports, and the center. This
is an explicitly stated field extension/parameter change, not same-field
normalization. Consequently14p excludes every such boundary q with
t0+3≠0. The already accepted14q handles arbitrary leading units directly
and excludes t0=-3 with delta0≠0.

## 3. Extract the boundary parameters from actual coefficients

By14f every field point at k=0 is

    A0=R_t³+alpha R_t,
    B0=R_t5+beta R_t³+gamma R_t,
    R_t=p5+g³p²+(t+3)gp²+t p³−(t+3)p.

The pure-p degree13 coefficient of R_t³ is3t (two p5 terms and
one t*p³). The alpha term has degree≤5, so H=t+3 at every boundary point.
Thus14p implies H=0 on the boundary of X. There t=-3,
R=p5+g³p²−3p³, and its origin order is3. The relevant coefficients are

    y=-3alpha,     w=-3gamma,     v=-243+beta.

For v, only five −3p³ terms contribute to [p15]R5 at t=-3;
[p15]R³=1, and gamma R is too small. These are scalar coefficient
projections, not full expansions of the actual powers. Substitution gives

    D=81(gamma−beta*alpha+5alpha²/9)=81delta0.

Hence14q implies D=0 on the same boundary. Vanishing on all geometric
points of this finite-type Q-scheme gives (C). Under the optional v=0
gauge, the expression becomes5y²+6561y−27w; its243 shift must not be lost.
The statement uses the full coefficient ring; a compressed presentation
may consume it only through its accepted coefficient maps.

## 4. Exact negative controls and decision consequence

The affine variety kw=1 is nonempty, k is nonconstant, and its k=0
fiber is empty. For example k=2,w=1/2. Every finite-coefficient arc
with k→0 is impossible, yet this variety is not empty. Thus even an
eventual exclusion of ALL finite boundary arcs would not decide U.
It would show only that k is a unit on its closure X (equivalently
J+(k)=S), not that J=S or I+(zk-1) is the unit ideal.

Nor is a boundary equation a global equation: on h=k, the boundary has
h=0, while k=h=2 is a point of the nonzero open. Combining h=k and kw=1
gives a nonempty component with no boundary at all. These are intentionally
toy affine varieties, not Keller pairs or points of the actual source.

The accompanying stdlib check.py verifies coefficient projections by at
most5-factor multinomial counts, the scalar discriminant substitution,
and these literal toy points. Omitted243, reversed gamma sign, and the
false global-h inference are actual changed-object controls; each must
fail normally and under−O. The proof of curve selection and the radical
inference is not replaced by finite tests.

This composition narrows the algebraic meaning of the existing arc
results. It does not license an extra source constraint or a repeated
jet search. Keep the pure-center question bounded and the direct whole
guarded-ideal decision live. An independent proof forcing a boundary
point, or controlling coefficient infinity/vertical-k components, is
still needed for a degeneration-based emptiness argument. This targeted
primary check does not reset the broad-sweep clock. STOP/IDLE after seal.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6623`.
- Body SHA-256:
  `141f39e8140418ac1b9c6d08846eec1e5bbab7d77db30941e8f21d2d22bcdd39`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
