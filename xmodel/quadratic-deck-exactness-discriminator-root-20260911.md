# Quadratic deck exactness: a bounded shortcut discriminator

ROOT, September11 2026. MANUAL / INTERNAL-UNREVIEWED strategy control.
This is not a new reduction, accepted theorem, or closure of an intermediate
quadratic extension. No source computation, worker or proof promotion.

## Question and disposition

Suppose a Keller map F=(f,g) admits an intermediate field K with
C(f,g) contained in K contained in C(x,y) and [C(x,y):K]=2. Its rational
deck involution sigma fixes f and g. Can finite-order symplectic geometry
force sigma to be polynomial, giving the familiar affine-fixed-point
contradiction? The linearization part is KNOWN. The proposed implication
from birational linearization or exactness to polynomiality is FALSE.
The live restriction remains the existence of an invariant polynomial
constant-Jacobian pair, not the abstract rational involution.

## Primary source and exact interface

Cerveau--Deserti, *Birational maps preserving the contact structure on P3*,
https://arxiv.org/pdf/1602.08866v2, defines eta=dx wedge dy. Its Proposition
3.35 already gives birational conjugacy of every eta-preserving involution
to central inversion; positive-genus fixed curves exclude the other Cremona
classes. Theorem3.32 characterizes exact/contact-liftable maps by zero
residues of sigma*(x dy)-x dy. The proof following Proposition3.35 gives
an area-preserving nonexact involution. These are prior results, not new
campaign lemmas. The journal version numbers the involution result3.4.4.

ROOT read the arXiv definitions and section3.4 through Proposition3.35/proof,
not the whole paper. The journal endpoint was blocked on direct opening;
its indexed excerpt is supplemental, not a whole journal-paper read.
Retained v2 PDF SHA3340f03bde79b17aa2d3b5c8aa8d9f5ab6623fdbf9203ffb439cab00396ab089
in box/quadratic-deck-exactness-discriminator-root-20260911/.

## Direct Keller consequence, stronger than closedness

Write J(f,g)=c in C*. Since sigma fixes f,g, it preserves df wedge dg and
hence dx wedge dy. Set lambda=x dy. The polynomial form

    lambda - c^(-1) f dg

is closed. The polynomial Poincare lemma (integrate polynomial coefficients)
gives H in C[x,y] with lambda-c^(-1)f dg=dH. Therefore

    sigma*lambda-lambda = d(H composed with sigma - H).             (1)

Thus every rational Keller deck transformation is exact, and the primitive
can be chosen as a coboundary of a POLYNOMIAL H. This argument does not
require order two. It supplies a necessary condition, not a constant-bracket
pair or a bound on poles. At any point where sigma is regular and fixes the
point, local invertibility of F makes sigma the identity germ, hence the
identity rational map. A nonidentity deck transformation has no such point.

## Decisive control in the already banked pseudo-plane

Take

    sigma(x,y)=(-x,-y-2/x^2).

It has order two and Jacobian1, is regular exactly on x!=0 as an affine
map, and has no affine fixed point there. The birational, area-preserving
change h(x,y)=(x,y+1/x^2) conjugates it to (-x,-y). Directly,

    sigma*lambda-lambda = -4 dx/x^2 = d(4/x),
    H=2xy,             H composed with sigma-H=4/x.

Even the polynomial-coboundary strengthening of(1) holds. The invariant
polynomials A=x^2, U=x+x^3y, Z=2y+x^2y^2 satisfy

    U^2=A+A^2 Z.

These are the existing pseudo-plane coordinates, not a Keller pair.
Their existence does NOT show that any two invariant polynomials have
constant nonzero bracket. It shows exactly why linearizability, exactness,
the polynomial-coboundary condition, and absence of affine fixed points
cannot alone force polynomiality of a rational deck candidate.

For contrast, replace the second component by -y+h(x), where

    h(x)=-2/x^2+1/(x^2-1).

Evenness of h again gives order two and Jacobian1. There are no affine
fixed points, because x must be0, a pole. But the defect is -x h'(x) dx,
which differs from h(x) dx by the exact differential -d(xh(x)). Its residues
at x=1 and x=-1 are respectively1/2 and -1/2. It cannot satisfy(1), so it
is not a Keller deck transformation. This control shows that exactness
can filter rational candidates even after the fixed-point test. It does
not eliminate the preceding pseudo-plane candidate.

## History checksum and next-action change

Scoped searches of AUDIT/APPROACHES/PROGRESS/REDUCTION and xmodel reports
found no exact Cerveau--Deserti citation, not a corpus novelty proof.
The August30 cyclic-birational-deck report already classifies the relevant
line-complement action and supplies the same pseudo-plane obstruction.
ROOT reread its lines1--290 only; current SHA
422bddb764966c9191703c16490d741d3f75d851277a706c6618ba78fdc4395d
was recorded AFTER that read, not a claimed prehash or fresh WHOLE intake.
The current strategy explicitly stops the rational-deck shortcut.

Disposition: KNOWN linearization, useful necessary residue test, DUPLICATE
surviving pseudo-plane gap. No new proof lane, generic Cremona enumeration,
or re-review of the old line-complement foundation is selected. A future
deck proposal with nonzero residues can be rejected cheaply; the present
zero-residue case still requires an invariant polynomial Keller pair or a
genuinely global obstruction to one. This does not close d1=2, non-Galois
target quotients, primitive maps or JC2. No canonical OPEN identifier is
raised. Cheapest selected discriminator was the displayed manual rational
calculation and primary/history comparison; no scientific code ran.

## COLLISIONS

status: EMPTY

- NONE — own-report collision tool found no explicitly raised OPEN entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5584`.
- Body SHA-256:
  `da88985e0c73116efccfe67dd860a25be38c5f64d4878cf84855eaeb379ff03c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
