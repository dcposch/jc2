# `(8,12)` order two: `p=0,D(k0)` support exhaustion and ramified closure design

Date: 2026-08-26

Status: **EXACT GRADE-TEN SUPPORT PARTITION AND PREREGISTERED THIRD-CHART /
TOTAL-REES DESIGN.  THE CUSP UNIT IS PRODUCER-LEVEL PENDING HOSTILE REVIEW;
THE `A`-CHART AND TOTAL-CHART GLUE ARE NOT YET SOURCE-CERTIFIED.**

## 0. Outcome first

The odd and cusp charts do **not** exhaust the raw `p=0,D(k0)` grade-ten
support.  They exhaust precisely the two regions where the leading linear
polynomial `R=cs*z+rs/4` is nonzero:

```text
D(rs)                         cusp,
V(rs) intersect D(cs)         odd face.
```

The missing region is

```text
V(rs,cs):                     R=0,
                              C=0 set-theoretically,
                              A=a1*z+a0 free.                 (0.1)
```

It is the exact-square zero-section direction of the half-weight chart.  On
the projectivized leading support it has two `A` opens.  A fixed-`p=0`
specialization of the reviewed high-contact receiver predicts a correction-
aware kill on both: the `D(a0)` chart has the pure pole
`-a0^3/(16*z^6)`, while `V(a0) intersect D(a1)` is triangular at grades
fourteen and fifteen and ends in `-a1^3/(16*z^3)`.

If that prediction is replayed from the complete source and the cusp, odd,
and `A` clients are proved to be a Cech cover of one total raw Kummer/Rees
chart, the empty-special-fibre lemma excludes every positive rational
valuation of the root-separation parameter at once.  Without the total-chart
and overlap certificate this implication is unavailable; isolated `p=0`
units must not be advertised as moving-`p` closure.

## 1. Exact raw support partition

After the reviewed sharp third-tail theorem has forced `M=0`, put

```text
p=0,                         L=z^2,
A=a1*z+a0,
C=(c1*z+c0)/2,
R=cs*z+rs/4,
k0 != 0.
```

The complete raw grade-ten rows are

```text
E1=(15/256)*k0*cs*rs^2 +(3/8)*(a1*c0+a0*c1),
E2=(5/1024)*k0*rs^3   +(3/8)*a0*c0+(3/32)*c1^2,
E3=(3/16)*c0*c1,
E4=(3/32)*c0^2.                                      (1.1)
```

No radical is used to derive the cusp localization.  On `D(rs*k0)`, `E4`
makes `c0` nilpotent, `E2` makes `c1` a unit modulo that nilpotent, and `E3`
then forces `c0=0` in the raw localized quotient.  One obtains

```text
c0=0,
5*k0*rs^3+96*c1^2=0,
15*k0*cs*rs^2+96*a0*c1=0.                           (1.2)
```

This is the cusp chart whose dual exact-Q grade-twelve producer replay gives

```text
E_(6,12)=-(21/1024)*rs^3*u^2,
u=c1/rs,
```

a unit on `D(rs*k0)`.  It remains provisional until its hostile review lands.

For the reduced support of (1.1), `c0=0` everywhere.  If `rs=0`, then `E2`
gives `c1=0`; the remaining two rows vanish.  Thus there is the exact locally
closed partition

```text
Supp(J10)_red intersect D(k0)
 = D(rs)
   disjoint union [V(rs) intersect D(cs)]
   disjoint union V(rs,cs).                         (1.3)
```

The middle term is the reviewed odd chart, killed by its exact grade-fourteen
unit.  On the last term the raw ideal still carries `C`-nilpotent thickness:

```text
(c0^2, c0*c1,
  (3/8)*a0*c0+(3/32)*c1^2,
  (3/8)*(a1*c0+a0*c1)).                             (1.4)
```

Every map to a DVR kills `c0,c1`, but a scheme-level or empty-fibre
certificate must retain (1.4) and eliminate it by raw identities.

## 2. The missing `A` Cech chart

Use the high-contact scaling in the complete ordinary source, but specialize
the square centre to `p=0` before any localization by `p`:

```text
Lambda=sigma^2,
R=sigma^2*(B0+sigma*B1+...),
C=sigma^4*(E0+sigma*E1+...),
A=A0+sigma*A1+...,
k10=k0+sigma*k1+...,

B0=b1*z+b0,                 E0=(e1*z+e0)/2,
A0=a1*z+a0,                 L=z^2.                 (2.1)
```

The already reviewed complete analytic receivers specialize to

```text
h14=[
   (3/4)*A0*E0/L
  -(3/8)*B0*A0^2/L^2
  +(5/32)*k0*A0^2/L
]_-,                                                (2.2)

h15=[
   (3/4)*(A0*E1+A1*E0)/L
  -(3/8)*(B1*A0^2+2*B0*A0*A1)/L^2
  +(5/32)*(k1*A0^2+2*k0*A0*A1)/L
  -(1/16)*A0^3/L^3
]_-.                                                (2.3)
```

These formulae retain every first correction that can tie through grade
fifteen.  `k6`, `k2`, and the targets cannot enter these grades, but they must
remain in the source emitter and be rejected by exact grade sentinels rather
than deleted from the input.

### 2.1 The constant `A` open

On `D(a0)`, the coefficient of `z^-6` in (2.3) is exactly

```text
[z^-6]h15=-(1/16)*a0^3.                             (2.4)
```

Every other term in (2.3) has denominator at most `z^4`, so no correction or
load can cancel (2.4).  This predicts a literal raw Laurent unit after
localization by `a0`.

### 2.2 The tangent `A` open

On `V(a0) intersect D(a1)`, write `A0=a1*z`.  The only negative grade-
fourteen coefficients needed at the deepest two poles are

```text
[z^-2]h14=-(3/8)*a1^2*b0,
[z^-1]h14= (3/8)*a1*(e0-a1*b1).                    (2.5)
```

Thus the raw grade-fourteen rows, localized by `a1`, should force

```text
b0=0,                     e0=a1*b1.                (2.6)
```

After (2.6), no noncubic term in (2.3) reaches pole three, and

```text
[z^-3]h15=-(1/16)*a1^3.                             (2.7)
```

This is again a unit on the declared open.  Equation (2.7) must be checked
after forming all raw grade-fourteen and grade-fifteen source rows; replacing
their predecessor by its radical is forbidden.

The fixed-centre hypothesis is load-bearing.  If one instead inserts a
first `sigma`-tangent `p=2*sigma*ell+...`, the differentiated grade-fourteen
receiver can contribute at pole three before the full predecessor is used.
That is not a defect in (2.4)--(2.7): a total-family argument below is the
preferred way to treat all positive `p` valuations.  A naive claim that the
fixed-`p=0` cube itself handles moving `p` is false.

## 3. A finite collision Cech cover

Let the projectivized leading correction support use the six collision jets

```text
(rs,cs,c0,c1,a0,a1).                               (3.1)
```

The following ordered principal cover is finite and retains the raw ideal.

| open | source endpoint | current status |
|---|---|---|
| `D(rs)` | normalized cusp, grade-12 row-six unit | producer PASS; hostile review live |
| `V(rs) intersect D(cs)` | normalized odd sheet, grade-14 unit | hostile-review confirmed |
| `V(rs,cs) intersect D(c0)` | `E4=(3/32)c0^2` is already a unit | exact from (1.1) |
| `V(rs,cs,c0) intersect D(c1)` | `E2=(3/32)c1^2` is already a unit | exact from (1.1) |
| `V(rs,cs,c0,c1) intersect D(a0)` | pure grade-15 pole (2.4) | preregistered candidate |
| `V(rs,cs,c0,c1,a0) intersect D(a1)` | triangular (2.5), then unit (2.7) | preregistered candidate |

The complement of these six opens is the affine zero section where every
coordinate in (3.1) vanishes.  It is absent from the corresponding Proj only
after the normalized-Rees construction proves that (3.1) is the complete
leading ideal.  Otherwise it is an explicit higher-contact receiver and must
be sent to the exact-square all-load fan; it may not be discarded by saying
“projective.”

This table is the clean answer to the exhaustion question: odd plus cusp do
not exhaust; odd plus cusp plus the two trivial `C` opens and two `A` opens
are the candidate complete collision Cech cover.

## 4. Total Kummer/Rees family and all positive `p` valuations

Adjoin a root-separation coordinate

```text
p=-2*rho^2,                 L=(z-rho)*(z+rho).       (4.1)
```

Do not invert `rho`.  The Kummer deck action sends `rho` to `-rho` and swaps
the two root-value coordinates while leaving the ordinary polynomial
coefficients fixed:

```text
R_+- = rs/4 +- cs*rho,
C_+- = (c0 +- c1*rho)/2,
A_+- = a0 +- a1*rho.                               (4.2)
```

This deck is distinct from the source involution `z -> -z` used to describe
some collision sheets.

### Gate T: one total raw source algebra

Construct the normalized multigraded Rees algebra directly from the complete
ordinary source rows with `p=-2*rho^2`, the correction variable `sigma`, all
loads, and all targets.  Its compiler must retain the full bidegree of every
term in `(sigma,rho)` before choosing a valuation cone.  It is not enough to
collect sigma coefficients while treating `p` as weight zero and substitute
`p=sigma^m` later: such a substitution allows cross-grade cancellations that
the separated coefficient ideal would miss.

For every Cech chart in Section 3, Gate T must print an explicit specialization
map from this one total algebra to the frozen `rho=0` client and an identity

```text
s = sum_i H_i*F_i + rho*H,                          (4.3)
```

where `s` is a product only of that chart's registered units and the `F_i`
are the complete total raw source rows.  All denominators of `H_i,H` must be
powers of registered units.  Cusp/odd/A equations from an analogous scaling
or a separately projected sheet do not satisfy Gate T.

If the six charts cover the normalized special fibre and (4.3) is certified
on every chart, then `rho` is a unit in each chart.  The empty-special-fibre
valuative lemma therefore excludes every formal arc in this total chart with
`ord(rho)>0`, including every positive rational order after finite
ramification.  Since `p=-2*rho^2`, this handles all positive `p` valuations
in the covered chart without one client per slope.

The conclusion is only as broad as the total Rees chart.  Any omitted Newton
cone, leading load, nilpotent direction, or zero section invalidates the
propagation.

### `D(rho)` overlap

On `D(rho)`, (4.2) is an invertible value map for linear polynomials.  The
total source rows must reproduce the reviewed generic-square root-value fan,
with both orientations and deck descent.  Cross-routing to the nonsquare K3
theorem is licensed only after an exact source-row transform produces its
coordinates `(kappa,e,U^2,F)` and proves its open `D(b*m)`; in the present
normalization the anticipated `b=4*rho` is a check, not an assumption.

## 5. Fallback finite joint fan

If Gate T does not yield a total-chart identity, do not enumerate many
integer `p` orders.  The initial Kummer fan is cut by only the three root-
cancellation walls

```text
ord(rs) = ord(cs)+ord(rho),
ord(c0) = ord(c1)+ord(rho),
ord(a0) = ord(a1)+ord(rho),                         (5.1)
```

together with the already frozen seven lower-hull functions for the
correction/load fan.  On an equality wall retain both oriented sums in
(4.2); a cancellation at one root is a new normalized face, not permission
to saturate by the other root value.  Higher cancellation order routes to an
infinity receiver under the contact-raising criterion.  Symbolic cones and
finite ramification classes are required; sampling `ord(rho)=1,2` is not a
coverage proof.

The boundary `k0=0` is not in this design.  Positive-order `k10` uses the
separate seven-generator lower hull

```text
AC, C2, RA2, A3, kR3, kRC, kA2,
```

with `kR2A` retained only as a source-completeness sentinel and never as a
primitive lower face.  The exact-square higher-contact receiver must also
retain `k6,k2` and target rows at their exact weights.

## 6. Minimal AWS sequence and stop conditions

1. **Fixed collision `A` client:** from the frozen complete source, specialize
   `p=0` before any `D(p)` saturation.  Emit all seven raw rows at grades
   fourteen and fifteen with (2.1), `k6,k2`, and all targets present.  On
   `D(a0)` certify (2.4); on `V(a0) intersect D(a1)` certify (2.5)--(2.7).
   Run exact Q plus one independent good-prime control on two AWS hosts.
2. **Raw Cech client:** retain (1.4), prove the six ordered opens cover the
   normalized projectivized support, print normalization/overlap maps, and
   route the all-zero complement explicitly.
3. **Gate T client:** emit the total `(sigma,rho)` source algebra and identities
   (4.3), with a negative control omitting the `A` charts.  The omitted-chart
   control must fail coverage.
4. **Overlap client:** on `D(rho)`, verify the deck-equivariant transform to
   both generic-square root charts and attempt the licensed nonsquare-K3 row
   transform only on `D(b*m)`.
5. **Fallback only if needed:** emit the exact fan (5.1) plus the frozen source
   lower hull; one symbolic initial module per face/orientation, not one job
   per integer slope.

Stop the collision lane when either:

- every Cech chart has a raw unit and Gate T supplies (4.3), in which case all
  positive `rho` valuations in that exact total chart are excluded; or
- a nonunit normalized component survives, in which case freeze it immediately
  and send it in parallel to terminal `[6,2]`, both Taylor families, and source
  reconstruction as a possible counterexample branch.

A modular-only unit, a reduced-support computation without raw identities, a
special fibre assembled from incompatible source scalings, an uncovered
zero section, or a finite list of sampled `rho` orders is `NO VERDICT`.

## 7. Explicit nonclaims

This note proves only the support partition (1.3) and the displayed fixed-
centre Laurent coefficient identities (2.4)--(2.7).  It does not yet prove
that those identities are the complete source rows at `p=0`, that the six
opens form the total normalized-Rees cover, that Gate T identities exist,
that any positive-valuation `p` arc is excluded, that the exact-square
all-load zero section is empty, or that a nonsquare K3 overlap exists.  It
does not close the square branch, order two, `(8,12)`, maximum twelve, or JC2.
