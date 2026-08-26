# `(8,12)` loaded order-four source projection: weakest gate and prime-lift criterion

Date: 2026-08-26

Status: **EXACT HAND LEMMA CHAIN; AWS CERTIFICATE ENDPOINTS PENDING.**  This
note does not yet eliminate the source leaf.  It separates the weakest
sufficient source theorem from a stronger computable criterion intended to
prove it.

## 0. Charged inputs and immutable correction

Let `J` be the corrected normalized coefficient ideal

```text
J=((r1,r2,r3,r4-1,r5,r6):r7^infinity)
  subset Q[a0,...,a6],
```

from the source-confirmed V2 client.  Put `s=a5`, `t=a6` and, on `t!=0`,

```text
q=s^2/t^3,       y=t^2,       v=y^4=t^8.              (0.1)
```

The charged geometric theorem is

```text
xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md
SHA-256 cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756.
```

Its different-model review is **CONFIRMED** at SHA-256
`59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a`.
The review found one harmless
coordinate-normalization typo: with `Q=q+4/27`, the cusp tangent is
`w=(3/8)Q^3+...`; `1/52488` is its coefficient in the scaled coordinate
`l_B=27Q`.  The `(2,7)` branch, all valuations, the divisor, and genus one
are unchanged.  The frozen V1 theorem is not mutated.  The canonical
nonmutating correction is

```text
xmodel/max12-812-order4-residual-cusp-kummer-genus1-tangent-erratum-20260826.md
SHA-256 26a083fcfa805a52fdb295ceaaf94ae7497047d8545a2323a48a688ac39e2300.
```

The exact plane membership/irreducibility/four-node output has SHA-256
`9b0e08c2d826286364f07f6a6fba9560e23ca8ea4fcba15cbbcf373152badbe3`.
It proves containment in the candidate plane, not source dominance.

## 1. The weakest sufficient source theorem

Let `Z` be any irreducible coefficient-curve component over `C` that can
contain the nonconstant image of a genuine normalized loaded order-four
source.  Assume:

1. `t` is not identically zero on `Z`, so (0.1) is defined at its generic
   point;
2. `(q,y):Z --> Y` is nonconstant, where `Y` is the complete normalization
   of the exact curve `P(q,y^4)=0` from the charged geometric theorem.

Then no such source exists.

Indeed, the coefficient functions live on the order-four Kummer source curve
and transform with the reviewed deck characters.  Hence `q` and `y` are
deck-`mu4` invariant, so their rational map descends to the source quotient
`P1_x`.  Properness extends it across all poles.  The charged theorem and its
review give `g(Y)=1`, while every morphism `P1 --> Y` is constant.  This
contradicts assumption 2.

This is the **weakest gate used here**.  It requires neither birationality of
the coefficient curve, equality with a full finite quotient, primeness of
the invariant graph, nor any assertion about `rho=r7^4`.  Conversely,
nonconstancy of `rho` alone does not imply assumption 2.

## 2. Monic good-reduction lemma

Let `V=Z_(p)`, with fraction field `K=Q` and residue field `k=F_p`.  Let
`G` be a finite monic Groebner basis in `V[x_1,...,x_n]`.  Suppose its
coefficientwise reduction `Gbar` is a Groebner basis and

```text
k[x]/(Gbar)
```

is a domain.  Then

```text
K[x]/(G)
```

is a domain.

Proof: division by the monic basis gives unique normal forms, so the standard
monomials form a free `V`-basis of `A=V[x]/(G)`.  In particular `A` is
`p`-torsion-free.  For a nonzero normal form `a`, let `nu(a)` be the minimum
`p`-adic valuation of its finitely many coefficients.  If `ab=0`, remove
`p^(nu(a)+nu(b))` using torsion-freeness.  The remaining two factors both have
nonzero reductions, whose product would vanish in the domain `A/pA`, a
contradiction.  Thus `A`, and hence `A tensor_V K`, is a domain.  QED.

For the present client `p=32003`.  The AWS certificate must establish all of
the following, not merely a matching dimension:

- every coefficient of the reduced characteristic-zero basis is
  `32003`-integral (successful exact reduction is the denominator check);
- its monic leading terms survive reduction;
- its reduction and the native `r7`-saturated special fibre contain one
  another exactly;
- their initial ideals contain one another exactly;
- the native special fibre equals the unique prime returned by the exact
  minimal-prime computation.

Under these checks the lemma proves that `J` is prime over `Q`.  A modular
prime without the monic/base-change checks would not suffice.

## 3. Nonverticality from the same flat model

Continue with the free `V`-model `A` from Section 2 and let `s,t` denote the
images of `a5,a6`.  Suppose the exact special-fibre contraction

```text
J_k intersect k[s,t]
```

is a principal nonzero irreducible ideal.  Then its image has dimension one.
The generic `(s,t)` image also has dimension one.

For if both `s` and `t` were algebraic over `K` in `A_K`, they would satisfy
nonzero univariate relations over `K`.  Clear unit denominators and divide
out the minimum `p`-adic content.  Because `A` is `p`-torsion-free, these
relations lie in the `V`-model.  Their reductions cannot be nonzero constants
(the special fibre is nonzero), and so they give nonzero univariate relations
for both `s` and `t` in `A_k`.  That would make the special `(s,t)` image
zero-dimensional, contradiction.

Thus at least one of `s,t` is nonconstant.  If both `q` and `v` in (0.1) were
constant, then `t^8=v` and `s^2=q t^3` would make both `s,t` algebraic over
the constant field, again a contradiction.  Hence `(q,v)`, and likewise
`(q,y)`, is nonconstant.

## 4. Why this is componentwise after base change

The exact irreducible polynomial `P(q,v)` belongs to `J` after clearing the
allowed power of `t`.  Sections 2--3 therefore give an inclusion of function
fields

```text
Q(P(q,v)=0)  -->  Frac(Q[a0,...,a6]/J).                (4.1)
```

Both sides have transcendence degree one, so (4.1) is a finite algebraic
extension.  The target plane is geometrically integral (independently
confirmed in the genus review).  After extending constants to `C`, every
minimal factor of the finite generic algebra lies over its generic point.
Consequently every geometric component of the coefficient curve dominates
the same residual plane; none is a vertical `(q,v)` component.  This is the
componentwise step.  It follows from the finite function-field inclusion,
not from irreducibility of the quotient plane alone.

Separately, exact equality

```text
J:a6^infinity = J                                      (4.2)
```

is required.  It says multiplication by `a6` is injective on the source
coordinate ring; flat constant extension preserves that injection, so no
geometric component is contained in `a6=0`.  Isolated `a6=0` points are
allowed and are restored by completing the rational map.  Equation (4.2) is
an independent chart-completeness audit and is not inferred from Sections
2--3.

Finally, a genuine source gives a nonconstant coefficient map: otherwise
`r7`, being a fixed polynomial in the coefficients, would be constant,
contradicting the confirmed terminal equation `8 dr7/dx=j/u !=0`.  Its image
is therefore dense in one geometric coefficient component, and the preceding
componentwise dominance proves the weakest gate of Section 1.

## 5. Exact AWS gates and firewall

The frozen registration is

```text
cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/
  REGISTRATION_PROJECTION_CERT_V1.md
```

with freeze-manifest SHA-256
`25a12c4bd62ef11c86c6626adccef14a96d9956df63c1695319686807dcadca0`.
The registered live lanes are:

```text
max12_812_order4_mu4_nonzero_a6_complement_v1_20260826T020100Z_r6d
max12_812_order4_mu4_nonzero_projection_primelift_v1_20260826T020100Z_r6d.
```

Promotion requires all exact source-equivalence sentinels, the two-sided
ideal and initial-ideal comparisons, equality with the unique modular prime,
the one-dimensional special projection, the two-sided `a6` saturation, clean
return codes, frozen hashes, and hostile review of this lemma chain.  A
timeout, OOM, missing comparison, merely modular irreducibility, quotient
irreducibility without source dominance, or graph output that omits a source
component is **NO VERDICT**.
