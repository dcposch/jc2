# Independent review: elliptic branch obstruction for the literal Pinchuk donor

Reviewer: swarmHQ gpt-5.6-sol. Review basis:
`1ba6678ea98c047a1d998132f1deb7c66c037ecd`.
Producer report SHA256:
`c2d14db83f1abced4a0e68b65bf3e0aca94b48e057c49c59d707248dbd7a0e14`.
Accepted Laurent-donor dependency SHA256:
`0dbb34f986d8747c7dde8ea74e930de8b9b8e1417653e73ad0749d5075ccca0a`.
Evidence: MANUAL/BOOK-relative. This is a different-model hostile review,
not a novelty finding, a review of Campbell's whole paper, or a JC2 result.

## Verdict

**CONFIRMED** at the producer's exact fixed-target scope. The displayed
rational pair has a genuine ramification divisor in the finite normalization
of `C[p,q]` whose branch image has smooth projective normalization of genus
one. Its persistence through every finite field embedding into `C(x,y)`
contradicts the accepted polynomial coverage of a plane polynomial map's
nonproperness components. Hence no such embedding can send these fixed
elements `p,q` to a whole-plane polynomial Keller pair.

## Independent reconstruction

Put `f=p-h`. The displayed `q` is `N(p,h)/(p-h)^2`; its numerator has degree
six in `h`, leading coefficient `197/4`, and value `-p^4(p+1)^2` at `h=p`.
Thus numerator and denominator are coprime over `C(p)` and
`[C(p,h):C(p,q)]=6`. Clearing the denominator gives a monic equation after
division by the scalar leading coefficient, so `h` and `f` are integral over
`A=C[p,q]`. If `B` is the normalization of `A` in `C(p,h)`, then

    A[h]_f = C[f,f^-1,h] = B_f.

The middle ring is normal and has the full fraction field. Therefore the
critical divisor found with `f` inverted belongs to the actual finite
normalization, not merely to a chosen rational model.

At fixed `p`, direct differentiation uses `d f/d h=-1` and yields

    q_h=-f*(r^2+(r+alpha)^2+1),
    r=h*(f-h*(h+1))/f^2,  alpha=13+15h.

The projective conic `C0: r^2+(r+alpha)^2+1=0` is smooth. With `u=f/h`,
the source critical curve has quadratic equation

    r*u^2-u+(h+1)=0

and discriminant `Delta=1-(4/15)r(alpha+2)`. The omitted locus `h=0,f!=0`
is not a critical component, since the derivative there is `-170f`.

On `C0`, `Delta=0` gives

    8*w^4+52*w^2+16*w+181=0,  w=alpha+1.

Modulo 7 this is `H=w^4+3w^2+2w+6`. The Euclidean reductions against
`H'=4w^3+6w+2` end with `w^2+w+4`, then `w+4`; substitution `w=3`
leaves `2`. This confirms squarefreeness in characteristic zero without
losing leading degree. Thus `Delta` has four simple finite zeros. At the
two points at infinity of the conic, `r` and `alpha` have simple poles, so
`Delta` has even poles of order two. It is not a square; the irreducible
double cover is ramified exactly four times, and Riemann--Hurwitz gives
genus one.

Genus of the source divisor alone is insufficient, so I separately checked
generic injectivity onto the branch image. At `p=0`, the two nonzero critical
points solve `197h^2+312h+126=0`; the discriminant is `-1944`, their values
are nonzero because `b^2-4ac=-1595`, and the remainder distinguishing the
two values has nonzero linear coefficient proportional to
`9b^2-32ac=-1944`.

For the other four roots, put `h=pw`, `v=w-1`. Their leading critical
equation is

    63v^4-27v^3+6v+1=0.

Modulo 5 it factors as `(v+1)(3v^3+1)`. The cubic has root `2` and the
two roots of `v^2+2v+4`, whose discriminant `3` is nonsquare. The reduced
critical values are respectively `0`, `1`, and `v+1` at the two quadratic
roots, hence all four are distinct. All relevant denominators are units.
The four values tend to zero with distinct `p^2` leading coefficients,
whereas the other two tend to distinct nonzero values. The degree-six
critical numerator has now been exhausted by six simple roots. Therefore
the irreducible critical curve maps generically one-to-one to its branch
image `D`, whose smooth projective normalization also has genus one.

Finally, for an embedding `K=C(p,h) -> L=C(x,y)` carrying `p,q` to a
polynomial Keller pair, extend the ramified divisorial valuation over `D`
to `L`. Multiplicativity of ramification indices preserves ramification.
The normal plane source is the etale open inside the finite normalization
of `A` in `L`, so it omits every such ramified divisor. Hence `D` is a
component of the polynomial map's nonproperness set. The accepted
LAURENT-POLYNOMIAL-DONOR-1 Section 4 transfer and its Jelonek--Lason import
force polynomial coverage of that component; a nonconstant affine-line
parametrization cannot dominate a curve with genus-one projective
normalization. Contradiction. No bound on `[L:K]` is used.

## Attacks, controls, and exclusions

- The complex degree-six claim comes from the rational-function degree and
  coprimality, not from real fiber counts.
- Four branch points, rather than four merely distinct intersection points,
  use squarefreeness plus the two even poles; the quadratic function-field
  presentation makes irreducibility explicit.
- Six distinct critical **values** are checked, not inferred from six simple
  critical points. This is the load-bearing birationality step.
- Ramification persistence uses valuation-index multiplication. The source
  open cannot contain a ramified divisor because the composite plane map is
  etale.
- The conclusion fixes the literal target pair `p,q`. It excludes neither
  target changes, other Pinchuk-like or multipole donors, arbitrary rational
  donors, nor the real Pinchuk map. It supplies no reduction of a general
  Keller source to this donor and no construction-family successor.

I used the accepted Laurent-donor transfer at its promoted exact hypotheses
and did not reaudit its external theorem. Campbell attribution was not needed
for the formula-defined claim and was not independently retrieved in this
review.

## COLLISIONS

status: EMPTY

- NONE — no `OPEN[...]` identifier or descendant is raised.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5864`.
- Body SHA-256:
  `226dc8d4ab40b21632f4947a0b6d40dc2501219fe3c58e981053f195b700b51a`.
- Frozen basis: `1ba6678ea98c047a1d998132f1deb7c66c037ecd`.
