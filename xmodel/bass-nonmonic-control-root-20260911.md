# Nonmonic first-order control: why Euler localization changes the theorem

ROOT manual derivation, INTERNAL / UNREVIEWED. Opened September11
22:07UTC; original publication reserve22:15/HARD22:18. No computation,
source execution or external theorem import. Basis
0d39df3c9fd69c939a8420c54d03228b9077777d. This is a discriminator for the
missing annihilator-normalization step, not another proposed family theorem.

## Exact algebraic-formal control

Let h=q(p+q) and let f=(1-h)^(1/2) be the formal branch with constant term1.
It is an algebraic element of C[[p,q]], and it is not polynomial:
specializing p=0 would give a polynomial square root of1-q^2, which has
simple roots. Put ep=p partial_p, eq=q partial_q, delta=p partial_q.
The linear vector field

    T=(p+2q) partial_p-q partial_q

kills h: T(h)=(p+2q)q-q(p+2q)=0. Differentiating f^2=1-h shows Tf=0,
since2f is a unit of the formal ring. Multiplication on the LEFT by delta
gives a first-delta-order operator lying in U:

    Phi=delta T=2 ep(eq+1)+delta(ep-eq),  Phi f=0.          (1)

Indeed the ordinary Weyl expansion is
p partial_q T=2p partial_p+p(p+2q)partial_p partial_q
-p partial_q-pq partial_q^2. The terms2p partial_p+2pq partial_p partial_q
are2ep(eq+1); the rest are delta ep-delta eq. This fixes every composition
order without assuming T itself lies in U: its2q partial_p term does not.

Thus first-delta-order alone does NOT imply polynomiality for algebraic
germs. Equation(1) has the extra diagonal factor2(eq+1), outside the
ep-r+delta G(ep,eq) family. Its homogeneous kernel contains h^n at every
even degree, and the binomial expansion of f uses infinitely many of them.

In the Ore localization by nonzero Euler polynomials, division of(1) on
the LEFT by2(eq+1) yields

    ep+delta[(ep-eq)/(2eq)].                              (2)

The shift is essential: (eq+1)delta=delta eq. Thus even this normalization
produces a RATIONAL coefficient with a denominator, not a polynomial G.
Multiplying to clear that denominator returns a nonmonic diagonal. No
assertion about other possible annihilators follows from(2) alone.

## The control cannot be an actual polynomial Keller-source element

Suppose p,q are any polynomial Keller pair in R=C[x,y] and an f in R
satisfies f^2=1-q(p+q). Lifted partial_p and partial_q preserve R, because
the Jacobian is a nonzero constant. Differentiation gives

    2f partial_p f=-q,   2f partial_q f=-(p+2q).

Hence q and p both belong to the principal ideal fR. Consequently
1=f^2+q(p+q) belongs to f^2R, so f is a unit, therefore constant in R.
Then q(p+q) would be constant, contradicting algebraic independence of p,q.
No such f exists. This is a direct source-specific divisibility obstruction,
not a characteristic-zero counterexample, and it uses neither Bass nor
an assumed generic first-order reduction.

## Consequence for strategy and limitations

The generic Euler localization must retain the difference between
polynomial and rational angular coefficients. Proving existence of some
first-order relation over its fraction field would not by itself supply the
tested monic/polynomial family. Conversely the direct source argument above
illustrates what extra information can reject a formal control; it does not
reject every possible higher-rank annihilator or establish such a relation.
This is compatible with BASS-DELTA1-1, not a refutation of it. No novelty,
properness theorem, general U-injectivity or JC2 conclusion is claimed.

History/scope check: exact strings q(p+q), sqrt(1-q),2ep(eq+1) and
first-delta-order searched in the current Bass reports and canonical
AUDIT/APPROACHES/PROGRESS/REDUCTION. Only the current first-order family
appeared. This is a bounded collision check, not an exhaustive novelty search.
No new named OPEN, scientific runtime or follow-on authority. Own full
readback and marker check precede transactional completion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3905`.
- Body SHA-256:
  `4b621f7780b3664142157f15db52f4cfbe3a8b6a95cb656ce10f49a2ee5565bf`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
