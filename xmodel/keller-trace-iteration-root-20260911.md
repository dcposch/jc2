# Iterated trace discriminator: closure under composition

ROOT/Astra, manual mathematics, PRODUCER-CHECKED / UNREVIEWED. Publication
first action2026-09-11 20:42:15UTC; original reserve20:53/HARD20:56UTC.
No scientific computation, AWS allocation or new external model used here.
No JC2 resolution or novelty claim. The only frozen mathematical report
input is keller-trace-image-root-20260911.md, SHA256
76fa7291c32150f8728b704116fdc92171ad40bf4c468bddfb1f01e0bf55c025,
read WHOLE after its original terminal publication and rehashed this turn.
Its theorem is accepted TRACE-IC-1 with the direct Theorem7.1 residue proof
of logarithmic-generator membership recorded in its FIRST review.
Neither currently live Astra report is an input.

## 1. Question and exact outcome

QUANTITY: whether applying the minimal trace-image condition to iterates
forces a new mixed-pole contradiction. CHEAPEST TEST: the following manual
composition calculation, completed within this publication window.

Let X and Y be polynomial planes over C, F:X->Y a Keller map, R=O(X),
A=O(Y), L=Frac R, K=Frac A. For any reduced curve E in X, define
B_E inside R[1/e] to be the inverse image of its sum of simple boundary IC
modules in R[1/e]/R, exactly as in the parent report. Put B_empty=R.
Write H2 for unshifted top algebraic de Rham cohomology.

Claim: if H2(B_E)=0, then

    Tr_(L/K)(B_E)=B_C,    C=S_F union closure(F(E)),           (I)

where C is reduced and S_F is the actual nonproperness divisor of F.
The target B_C is defined over A in the same way. No finite-degree/support
bound on E or its equation is assumed. This is a consequence of the
accepted minimal-boundary characterization, not a new properness theorem.

In particular, field-trace transitivity and (I) propagate the accepted
condition to every iterate. This calculation yields no extra mixed-pole
obstruction. It does NOT prove that all possible dynamical arguments are
redundant or that such a Keller map can exist.

## 2. Proof of the transfer identity

Denote the trace image by J. The lifted target partial derivatives are
polynomial R-linear combinations of partial_x,partial_y, and conversely
the source partials are polynomial combinations of the lifted ones. Thus
B_E is stable under the lifted derivatives. The two de Rham complexes
are identified by the polynomial inverse-Jacobian frame change; at top
degree the volume scalar is the nonzero constant det JF. Consequently
H2(B_E), computed as a target differential module, is still zero.
Trace commutes with the lifted derivatives, so J is a W_Y-module and
H2(J)=0 by right exactness. Also A is contained in J since R is contained
in B_E. Away from C the map F is finite etale and e is a unit at every
preimage, so traces are regular there. Hence J is contained in A[1/c],
where c is an equation for C; the lower-case polynomial c in this section
is unrelated to the Jacobian scalar.

The parent trace theorem gives generic fullness of Tr(R) at every
component of S_F. Since Tr(R) is contained in J, these components need no
new argument. Let eta be the generic point of a component of C outside
S_F. Put O=A_eta. Here R_eta is finite etale over the DVR O and is its
integral closure in L. At least one prime over eta lies on E.

The parent reducible curve-module result says R[1/e]/B_E is a finite sum
of point-supported differential modules. Localizing as an A-module at eta
kills this quotient: each of its finitely many supporting source points
maps to a closed target point, which can be avoided by some denominator
outside eta. Thus

    (B_E)_eta=R_eta[1/e].

This last ring is not finite over O, since 1/e has a pole at a retained
height-one prime of R_eta. If its traces had a lower valuation bound,
the finite trace-dual lattice of R_eta would contain a fixed uniformizer
multiple of the whole ring, forcing it finite over O. This is exactly
the parent's trace-dual argument, now in a finite-etale neighbourhood.
Therefore J_eta=K. Generic fullness holds on every component of C.

Finally H_C/L_C is a finite sum of point modules delta_z. The image of J
there is zero: any nonzero finite-length point module has a simple
quotient delta_z with H2=C, contradicting H2(J)=0 and right exactness.
Thus J/A is contained in L_C. Each simple summand of L_C maps to
H_C/(J/A); a nonzero map would be injective, impossible after localization
at its generic point, where that quotient is zero. Hence J/A=L_C and (I).

This proof requires no IC/de Rham comparison on normalizations, no
semisimplicity of a nonproper direct image, and no multiplicative closure
of a trace image. The parent standard point-quotient input is retained.

Negative control: for the identity map and E={xy=0}, replacing B_E by
the full localization R[1/(xy)] changes the trace image to that same full
localization, strictly larger than B_E=R[1/x]+R[1/y]. Its H2 is C, not
zero. Thus the proof does not license replacing the minimal module by
an arbitrary ring with the same codimension-one localizations.

## 3. Actual composition and iterates

For Keller F,G, the elementary nonproper-set identity is

    S_(F composed G)=S_F union F(S_G).                       (II)

For completeness, the image of G omits at most finitely many points:
it is open because G is etale; an omitted divisor would pull back to an
everywhere nonzero polynomial, hence a constant, contradicting dominance.
For b in S_F choose y_n tending to infinity with F(y_n)->b, avoiding the
finite omitted set of G. Choose x_n with G(x_n)=y_n; x_n tends to
infinity, so b belongs to S_(F composed G). The inclusion F(S_G) is
obtained by composing the defining asymptotic sequences. Conversely,
if x_n tends to infinity while F(G(x_n))->b, then either G(x_n) has a
bounded subsequence converging to a point of S_G, or it has a subsequence
tending to infinity, yielding b in S_F. This proves (II) and in particular
shows the union is closed. No surjectivity of either Keller map is assumed.

Let tau be the rational trace transfer of F, with source and target
polynomial planes identified in the usual way, and M_n=tau^n(R).
Field-trace transitivity gives M_n=Tr_(F^n)(R). The initial parent result
is M_1=B_(S_F), with H2(M_1)=0. Suppose M_n=B_(S_(F^n)) and H2(M_n)=0.
Applying (I) and (II) yields

    M_(n+1)=tau(M_n)=B_(S_(F^(n+1))),
    S_(F^n)=union_(j=0)^(n-1) F^j(S_F).

The trace map from M_n, in the lifted frame, again gives H2(M_(n+1))=0.
Thus this module-image calculation is already closed under iteration.
Any further dynamical proof must add a genuinely incompatible source or
orbit property; repeated application alone has not supplied one.

## 4. A separate elementary curve restriction, and its limitation

For a nonconstant polynomial parametrization gamma(t), put
r(gamma)=1+deg gcd(gamma_1',gamma_2'). Its derivative vector transforms
under F by the unimodular matrix JF(gamma(t)), so its gcd is unchanged up
to a nonzero scalar. Suppose gamma is a normalization parametrization of
an irreducible curve with normalization A1, and write

    F composed gamma=eta composed h,

where eta is a normalization parametrization of the image and h is a
nonconstant polynomial. Such a factorization is through the finite A1
normalization; equivalently it follows from polynomial parametrization
and the intermediate one-variable function field. If g_eta=gcd(eta_1',eta_2'),
the remaining two derivative factors are coprime; they stay coprime after
substitution by h, by their polynomial Bezout identity. Hence

    gcd(gamma_1',gamma_2') = unit * h' * g_eta(h),
    r(gamma)=deg(h) * r(eta).                               (III)

Along forward images of one such curve, generic restriction degrees
therefore have product bounded by r(gamma). Only finitely many can exceed
one, at most floor(log_2 r(gamma)); after that every restriction is
birational. An immersive normalization has r=1 from the start.

This does NOT imply injectivity or absence of nodes. The polynomial
immersion eta(t)=(t^2,t^3-t) is birational, has derivative gcd1, and
identifies t=1 and t=-1. It is a curve-level control, not a constructed
Keller image of a line. Even eventual birationality along boundary orbits
does not bound new self-identifications, intersection counts, or orbit
lengths. No termination invariant or global contradiction follows here.
No novelty or exhaustive history claim is made for (III).

## 5. Disposition

NO_CLOSING_DISCRIMINATOR from iterating the trace-image identity. Formula
(I) explains its automatic propagation without replacing additive modules
by rings. Formula (III) gives a bounded generic-cover multiplicity, not a
bound on node formation. The surviving JC2 obligation is a new source
incompatibility, not a repeated trace-module equality or an immersive-curve
injectivity assumption. No new OPEN ID, compute run, worker, echo gate or
downstream mathematical promotion is authorized by this manual report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8905`.
- Body SHA-256:
  `c3dac8c66d64f619d1d9531edd879dc764bcc3e6c9c02382a2bd401869de413c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
