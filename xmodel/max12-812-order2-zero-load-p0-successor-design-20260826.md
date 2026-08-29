# `(8,12)` order two: zero-`k10` and quadruple-square successor

Date: 2026-08-26

Status: **CORRECTION-AWARE SUCCESSOR DESIGN, WITH ONE SHARPENED HAND
LEMMA TO BE REPLAYED FROM THE COMPLETE SOURCE.  NO SQUARE-BRANCH OR
ORDER-TWO VERDICT.**

## 0. Scope and charged inputs

This note covers the square strata omitted by the reviewed calculations on
`D(p*k10)`:

1. `p != 0`, with boundary value `k10=0`, including the two
   square/discriminant root-allocation intersections and arcs on which
   `k10` first appears at positive order; and
2. `p=0`, where `L=z^2` and the two roots of the generic square chart collide
   at the quadruple quartic `K=z^4`.

It consumes only the reviewed first-normal support, the exact third-tail
formula, the reviewed nonsquare discriminant K3 theorem, the reviewed square
half-weight and high-contact theorems, and the moving-`p` covariance check.
The late global ideation report is strategy input, not a mathematical premise.

The source convention is

```text
L=z^2+p/2,
K=L^2+Lambda*R,
N=L*M+Lambda*S,
T=2*L*R+M,
B=R^2+S.
```

All polynomials `M,R,S` have degree at most one.  No reduced support below is
substituted before the complete raw source ideal at that grade has been
formed.

## 1. A sharper third-tail lemma

The complete third negative Laurent tail at zero `k10` is

```text
h3 = [ T*(12*B*L^2-T^2)/(16*L^3) ]_- .              (1.1)
```

The first seven vanished tails force

```text
L^3 | P,       P=T*(12*B*L^2-T^2).                  (1.2)
```

This condition kills `M` on **both** square charts.

On `p != 0`, reduction modulo the squarefree quadratic `L` gives

```text
P == -M^3  (mod L),
```

so `L|M^3`; since `deg(M)<=1`, this forces `M=0`.

On `p=0`, write

```text
L=z^2,
M=alpha*z+beta,
R=cs*z+rs/4,
S=(v1*z+v0)/2.
```

The constant coefficient of `P` is `-beta^3`, hence `beta=0`.  After that
specialization, `12*T*B*z^4` begins in degree five while `T^3` has degree-three
coefficient `alpha^3`.  Therefore

```text
[z^3]P=-alpha^3,
```

and (1.2) forces `alpha=0`.  The older third-tail theorem's conclusion
`beta=0` at `p=0` is correct but not sharp.

The same calculation permits an integral moving load

```text
k10=Lambda*kappa.
```

Its order-three contribution is a polynomial multiple of `L^5`; it has no
negative tail and cannot cancel (1.1).  Tangent motion
`p=p0+Lambda*p1` along the square center likewise differentiates only lower
polynomial grades.  The complete-source replay in Section 7 must verify both
statements rather than treating this hand observation as promoted.

### Consequence for the square/discriminant intersection

For `p=-2*a^2 != 0`, the two intersections have

```text
L=(z-a)(z+a),       M=lambda*(z+a)
```

or the deck-conjugate allocation `M=lambda*(z-a)`.  They have `M!=0` and
are killed by (1.2).  At `a=0`, their common limit is `M=lambda*z`, and the
new `z^3=-lambda^3` coefficient kills it as well.  Thus no nonzero
zero-load first-contact direction remains at either intersection.

This does **not** eliminate a ramified arc on which `k10` has a fractional
positive slope relative to `Lambda`: such a load can tie a lower normalized
ray before the integral `Lambda^3` coefficient.  Those slopes are routed by
the fan below.

## 2. Horizontal contact raising on `p != 0`

After `M=0`, use the reviewed half-weight normalization

```text
Lambda=sigma^2,
M=sigma^3*A,
S=sigma*C,
k10=sigma^q*k,       q>0,
```

and let

```text
a=ord_sigma(A),   r=ord_sigma(R),   c=ord_sigma(C).
```

After subtracting polynomial terms, the possible first negative monomials
through the cubic separator have the following weights relative to absolute
grade ten:

| term | relative weight | pole denominator |
|---|---:|---:|
| `A*C` | `a+c` | `L` |
| `C^2` | `2c` | `L^2` |
| `R*A^2` | `2+r+2a` | `L^2` |
| `R*A*C` | `2+r+a+c` | `L^3` |
| `R*C^2` | `2+r+2c` | `L^4` |
| `k*R^3` | `q+3r` | `L` |
| `k*R*C` | `1+q+r+c` | `L` |
| `k*R^2*A` | `3+q+2r+a` | `L^2` |
| `k*A^2` | `4+q+2a` | `L` |
| `k*A*C` | `4+q+a+c` | `L^2` |
| `A^3` | `5+3a` | `L^3` |

These are affine forms on the rational cone
`a,r,c>=0, q>0`.  Three entries are completeness sentinels rather than lower
face generators:

```text
wt(RAC)=wt(AC)+(2+r),
wt(RC^2)=wt(C^2)+(2+r),
wt(kAC)=wt(AC)+(4+q).
```

They are globally dominated.  The essential fan is therefore exactly the
eight-form fan in the separate horizontal-contact design, with `+q` added to
its four loaded forms `kR^3,kRC,kR^2A,kA^2`.  This extension should reuse that
fan emitter and its opposite-root `AC/RC` charts; it must not duplicate the
already registered `q=0` clients.  Every further power of `R` raises weight
by `2+r>0`, so it cannot create an infinite descending family of new faces
before the cubic separator.  The compiler must still check these dominance
claims against the complete binomial support through the last required
grade.

The source clients should work over the etale root algebra

```text
E=Q[p,rho,1/(p*rho)]/(rho^2+p/2),
A_+=A(rho), A_-=A(-rho),
```

and similarly for `R,C`.  Evaluation is an isomorphism from linear
polynomials to the two root-value coordinates on `D(p)`.  Principal-part
vanishing therefore splits into two one-root obstruction modules, exchanged
by `rho -> -rho`.  This is the clean way to retain root-allocation faces:
no resultant saturation is allowed to delete a face supported at only one
root.  Descent is certified by the deck swap and by the overlap with the
ordinary `Q[p]` rows.

The zero-load boundary starts with only `a,r,c>=0,q>0`.  In particular the
bounds `a>=1,c>=3,r>=2` derived in the `k10`-unit horizontal design are **not**
available here: they consume the unit-load low-contact clients.  First form
the raw `C`-front ideal at `k10=0`, normalize all its faces, and derive any
stronger bounds source-side.  Only then may a surviving face enter the smaller
unit-load domain.

The normalized fan is grouped into four source modules, not one client for
every integer `q`:

1. **`C` front:** a face containing `A*C` or `C^2`.  Use the raw grade-ten
   ideal and its normalized blowup.  Its radical `C=0` is only a routing
   statement.
2. **mixed `R/A` front:** a face containing `R*A^2`, `R*A*C`, or `R*C^2`.
   Retain the two root allocations and the doubled directions.
3. **moving-load front:** a face containing one of the five `k` monomials,
   including every equality with an unloaded monomial.  `q` remains a
   symbolic ray weight; do not sample `q=1,2` and infer the rest.
4. **cubic cone:** after all earlier face equations, certify in the cokernel
   of those raw equations that the first non-`L`-divisible class is
   `-A_0^3`.  The reviewed V5 identity is the first connection check:
   first-order motion of `p` changes the grade-fifteen representative by a
   multiple of the preceding grade-fourteen class.

A cone is contact-raised only when its complete source obstruction forces the
leading coefficient of `A`, `R`, `C`, or `k10` to vanish while retaining the
corresponding zero section.  Reapply the same finite fan to the first nonzero
higher coefficient.  This is a Noetherian/contact-order induction, not a
claim that a radical unit excludes the tangent section.

## 3. The exact-square zero section and all loads

If the unloaded corrections vanish and

```text
f=Q^2,       Q=L^2+sigma^u*R+...,
```

then the first nonpolynomial terms of the three lower loads are

```text
(5/16) Lambda^2 k10 R^3/L,
(3/8)  Lambda^6 k6  R^2/L,
(1/2)  Lambda^10 k2 R/L.                             (3.1)
```

For `lambda=ord_sigma(Lambda)` their weights are

```text
2*lambda+ord(k10)+3*u,
6*lambda+ord(k6) +2*u,
10*lambda+ord(k2)+u.                                 (3.2)
```

At a tie, the common first numerator is

```text
R*((5/16)k10*R^2+(3/8)k6*R+(1/2)k2)  (mod L).       (3.3)
```

This quadratic load tie can have genuine root allocations, so no individual
load may be inverted or projected.  Add to (3.2) the exact target weights

```text
(12+ell)*lambda+ord(delta_ell),       1<=ell<=7,
```

with `delta=(0,mu2,0,mu4,0,mu6,J/4)`.  The resulting Newton fan is still
finite.  A target is a single ordinary row, not a Laurent polynomial that can
be merged into (3.3).  It must stay in its source row, and `J` must remain
subject to the registered interior saturation.

Only after this source fan leaves a component should the terminal `[6,2]`
receiver and both Taylor polynomiality families be pulled back to it.  The
known all-lower-load-zero divisor-19 obstruction is a prefilter; it does not
license deleting the target or Taylor variables in the fan.

## 4. The quadruple-root chart `p=0`

The root-value coordinates of Section 2 are singular at `rho=0`.  Replace
them by the value/derivative jets at the double root.  After Section 1 has
forced `M=0`, the exact half-weight grade at `k10=k0!=0` specializes to the
four nonzero source rows printed by the reviewed generic compiler.  Clearing
only rational units gives the raw ideal

```text
J0=(
 c0^2,
 c0*c1,
 5*k0*rs^3+96*c1^2+terms divisible by c0,
 5*k0*cs*rs^2+32*a0*c1+terms divisible by c0
).                                                   (4.1)
```

Here

```text
A=a1*z+a0,
C=(c1*z+c0)/2,
R=cs*z+rs/4.
```

The exact unscaled rows, which the client must use, are

```text
(15/256)k0*cs*rs^2+(3/8)(a1*c0+a0*c1),
(5/1024)k0*rs^3+(3/8)a0*c0+(3/32)c1^2,
(3/16)c0*c1,
(3/32)c0^2.                                          (4.2)
```

Thus the reduced special fibre has two visibly different regions:

- on `D(rs)`, a `(2,3)` cusp
  `5*k0*rs^3+96*c1^2=0`, with `cs` tied to `a0`; its normalization must be
  computed from the **raw** ideal (4.2), retaining conductor and nilpotent
  data;
- on `V(rs)`, one has `c1=0`, while the odd direction `R=cs*z` survives this
  grade because `R^3/L=cs^3*z` is polynomial.  The next binomial term has a
  genuine pole and must be included before calling this a component.

The special-fibre fan has two compatible charts.

1. **Root-separation/Kummer chart:** adjoin `rho` with
   `p=-2*rho^2`, retain the deck action `rho -> -rho`, and apply the generic
   root-value fan on `D(rho)`.  Positive-order `p` is not treated as a unit
   at the boundary; all `rho` weights and connection terms remain in the
   source substitution.
2. **Collision chart:** set `rho=0` and use the `z`-adic value/derivative
   filtration beginning with (4.2).  Normalize its cusp and odd face, then
   compile the next divided source grade with moving `p`, every correction,
   and all loads at their exact weights.

The overlap is checked after passing to the invariant quotient of the Kummer
chart; byte-identical chart presentations are neither expected nor required.

## 5. Licensed cross-routing to the nonsquare theorem

The reviewed nonsquare K3 theorem applies only after its exact K2 source rows
have produced

```text
(kappa,e,U^2,F)
```

on `D(b*m)`, followed by the normalized ray
`wt(U,e,kappa,F)=(1,2,2,2)`.  Here `b=4*a` is the separation between the
double root and the other factor, and `m` is the nonzero first-contact
coordinate.

Therefore a square special-fibre chart may be cross-routed only if an exact
row transform identifies its normalized source ideal with that K2 ideal and
the chart proves `b*m != 0`.  Merely having `p` or `rho` nonzero at the
generic point is insufficient.  The generic square/discriminant
root-allocation points are already killed earlier by Section 1.  The
quadruple point has `b=0` and cannot be imported into the reviewed K3 theorem.

The useful test is nevertheless small: on each normalized cusp/odd chart,
reconstruct the discriminant coordinates `(b,e,U,F,kappa,m)` and ask whether
the source rows give the reviewed lower-unitriangular K2 transform.  A PASS on
`D(b*m)` terminates that chart by the existing K3 theorem; failure keeps it in
the square collision atlas and makes no mathematical claim.

## 6. Minimal AWS client sequence and stop rules

1. **Sharp third tail (launch first):** exact `Q` plus independent
   `F_65521`; reconstruct all seven frozen source rows in the full square
   matched chart, retain `R,S`, use `k10=Lambda*kappa`, and replay both fixed
   `p` and `p=Lambda*p1`.  Verify the unitriangular source/Laurent identity,
   `P==-M^3 mod L`, and the special sentinels
   `[z^0]P=-beta^3`, `[z^3]P|_(beta=0)=-alpha^3`.
2. **Generic positive-load fan emitter:** enumerate the primitive cones of
   the eleven affine forms in Section 2, append the three load forms and seven
   target forms, and emit only distinct initial source modules.  Acceptance
   requires faces, overlaps, deck descent, and reproduction of the reviewed
   `k0`-unit rays.
3. **Quadruple grade ten:** exact `Q`/good-prime source replay of (4.2), raw
   normalization of its cusp and odd face, conductor/overlap output, and no
   saturation by `(c0,c1,rs,cs)`.
4. **Quadruple next grade:** one client per normalized cusp/odd chart,
   retaining moving `p`, all correction coefficients, `k10,k6,k2`, every
   target, and the raw predecessor ideal.  Attempt the licensed K2 row
   transform before any new elimination.
5. **Terminal/Taylor pullback:** only for a source component surviving Steps
   1--4; pull back the terminal row and both finite Taylor receivers without
   projecting their loads.

Stop fan expansion when every primitive cone and face has one of four exact
endpoints: unit away from its zero section, contact-raised to the same finite
fan, cross-routed on a proved `D(b*m)` overlap, or represented by one explicit
source component already sent to terminal/Taylor reconstruction.  A timeout,
modular-only unit, radical computation without the raw ideal, or missing
overlap is no verdict.

## 7. Explicit nonclaims

Only the elementary coefficient argument in Section 1 is asserted by hand,
and it remains producer-level until the complete-source dual-AWS replay and
hostile review.  The finite fan is a design, not an exhaustiveness theorem.
Nothing here proves the p-zero grade-ten cusp or odd face lifts, proves a
horizontal induction, excludes the square component, constructs a strict
arc, satisfies the terminal passport or either Taylor family, closes order
two or `(8,12)`, proves maximum twelve, or proves JC2.
