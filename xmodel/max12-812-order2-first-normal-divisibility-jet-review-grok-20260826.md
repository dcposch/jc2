# Hostile review — first exact normal/divisibility jet of the `(8,12)` order-two one-parameter Rees family

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md` |
| Target SHA-256 | `827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews were opened only because they are named; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target and every charged local source; no Singular, Sage, msolve, Lean, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc`,
matching the required pin. Producer verdict language, the target's own
status line, and charged review tokens were not used as evidence. No file
other than this review was written.

---

## Verdict

The substitution `(1.1)` is the exact expansion of `K^2` in the depressed
monic octic chart, with four normal excesses scaled by `Lambda`. On
`D(Lambda)` it is an ambient-coordinate automorphism of the one-parameter
coefficient-load space: the inverse `(1.2)` is regular and the Jacobian
determinant is `8 Lambda^4`. Keeping `(p,c,r)` as full variables absorbs
every tangent displacement of the high coefficients `(C_6,C_5,C_4)` and
does not freeze a particular quartic. The zero section `n_0=n_1=n_2=n_3=0`
is higher normal contact in this chart and is not discarded from the full
strict-arc problem.

Pulling the seven exact rows back by `(1.1)` yields a polynomial identity
`Lambda^2 | Phi_ell` in the chart ring, not an order statement on reduced
points. Unloaded tails vanish identically on the polynomial image of
`(p,c,r) |-> K^2`; the coefficient Jacobian of the unloaded seven-tail map
vanishes in every `f`-direction at every such point, so the linear-in-
`Lambda` piece is the zero polynomial; affine linearity in the three lower
loads together with the displayed load and target exponents produces no
cross term of order less than two. Dividing by `Lambda^2` is an equality
of ideals on `D(Lambda)`. The unsaturated special fibre `Q1` is not the
Rees boundary: chart closure still requires
`((Theta_1,...,Theta_7):Lambda^infinity):J^infinity` before `Lambda=0`,
then irrelevant saturation by `(p,c,r)`.

Every `q_ell` is the Hessian of the unloaded tails in `(n_0,...,n_3)` plus
`k_{10}` times the exact `k_{10}` load derivative at `K^2`. Independence
of `k_6,k_2,mu_2,mu_4,mu_6,J` is absence of those variables from the
generators, hence a product with affine six-space, not a finite-quotient
elimination. Both saturations in `(3.2)` are the correct multi-generator
colons: `(p,c,r)` is the irrelevant ideal of the weighted cone on
`P(2,3,4)`, and `(n_0,n_1,n_2,n_3,k_{10})` isolates the nonzero first
normal/load stratum without declaring higher-contact arcs empty. Reduced
common-quartic support licenses leading points, not an identification of
scheme structure with the seven-tail fibre. No `(9,12)` formula, terminal
`U=4` map, Taylor condition, or order-two closure is used.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md` | `827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc` | target (matches required pin) |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | one-parameter family `(0.1)`, retained loads, `Lambda`/`J` saturations |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md` | `1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de` | named parent of the reduction; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-runit-delta-review-grok-20260826.md` | `0fa0dc4afb160ae4b9ed6bc195e1158e44b92cdc5bb5ea1619a146e9d52aac96` | named parent of the `R=1+tau` localization; opened only to obey the inspection clause |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` | reduced common-quartic support, triangular chart `(6.1)`–`(6.2)`, coefficient Jacobian `(7.1)`, affine loads, target exponents |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md` | `aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495` | replaces false load-direction vanishing `(7.2)`; keeps `(7.1)` |
| `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | exact seven ordinary tails as ten-tuples `(a0..a6,k10,k6,k2)` |

All seven hashes match the values printed in the target and in the review
prompt. The named reduction and `R`-unit reviews were not used as
algebraic evidence. The frozen tails are ordinary `(8,12)` ten-tuples:
every monomial has load exponents in
`{(k_{10},k_6,k_2)} = {(0,0,0),(1,0,0),(0,1,0),(0,0,1)}`, so the tails
are affine-linear in the three lower loads, with no load–load product and
no load degree greater than one. There is no `a_7`, no `k_8`, and no `F_9`.

---

## Strongest exact theorem that survives

Work over `Q` in the one-parameter ring

```text
A = Q[Lambda, C0,...,C6, k10, k6, k2, mu2, mu4, mu6, J]
```

of the charged family

```text
Phi_ell = r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
          - Lambda^(12+ell) delta_ell,
(delta_1,...,delta_7) = (0, mu2, 0, mu4, 0, mu6, J/4).
```

Let `K=z^4+p z^2+c z+r` and let `(1.1)` be the polynomial chart displayed
in the target. Then:

1. On `D(Lambda)`, `(1.1)` is an automorphism of the ambient coefficient-
   load space, with inverse `(1.2)`. The three high coefficients are
   equivalent to `(p,c,r)` (Jacobian determinant `8`), and the four
   extras `n_i` are the unique complementary normal coordinates. The zero
   section `n_0=n_1=n_2=n_3=0` is the locus of higher normal contact in
   this chart.
2. In the chart ring
   `Q[Lambda,p,c,r,n0,n1,n2,n3,k10,k6,k2,mu2,mu4,mu6,J]`,
   `Lambda^2` divides every pulled-back `Phi_ell` as a polynomial identity.
   The divided rows `Theta_ell = Phi_ell/Lambda^2` are therefore
   polynomials, and `(Phi_1,...,Phi_7)=(Theta_1,...,Theta_7)` as ideals of
   the localization at `Lambda`. Chart closure of the interior still
   requires the principal saturations by `Lambda` and by `J` before
   imposing `Lambda=0`, then saturation by the coefficient-irrelevant
   ideal `(p,c,r)=(C0,...,C6)|_{Lambda=0}`.
3. Writing `q_ell = Theta_ell mod Lambda` and `Q1=(q_1,...,q_7)`, each
   `q_ell` is a quadratic form in `(n0,n1,n2,n3)` with coefficients in
   `Q[p,c,r]`, plus `k10` times the polynomial `k10`-derivative of the
   exact tails at `K^2`. No generator involves `k6,k2,mu2,mu4,mu6,J`, so
   `V(Q1)` is the product of that seven-row scheme with affine six-space
   in those variables.
4. The first nonzero-normal/load gate
   `Q1^* = (Q1:(p,c,r)^infinity):(n0,n1,n2,n3,k10)^infinity`
   is the scheme-theoretic closure of `V(Q1)` minus the weighted-
   projective origin minus the zero normal/load section. Any genuine
   strict arc whose first nonzero normal/load contact in this chart occurs
   at order one lands on `V(Q1^*)`. The identity `Q1^*=(1)` therefore
   forces higher contact; it does not exclude arcs of order at least two,
   and it is not the saturated divided-family boundary.

This is an exact first divisibility jet of the charged one-parameter
family. It does not prove that boundary empty or nonempty, exclude
`[6,2]`, test a terminal `U=4` map, impose either Taylor family, close
order two, close `(8,12)`, prove maximum twelve, or prove JC2.

---

## Attack 1 — coefficients of `(1.1)`, isomorphism on `D(Lambda)`, tangent motion, zero section

**CONFIRMED.** Every coefficient of `(1.1)` is the expansion of `K^2`.
The chart is an ambient automorphism on `D(Lambda)`. The variables
`(p,c,r)` absorb all reduced-support tangent motion. The zero normal
section is higher contact and is correctly retained for the full arc
problem.

Expand `K^2=(z^4+p z^2+c z+r)^2`:

```text
z^8,
2p z^6,
2c z^5,
(p^2+2r) z^4,
2pc z^3,
(c^2+2pr) z^2,
2cr z,
r^2.
```

There is no `z^7` term because `K` is depressed. In the monic depressed
octic coordinates this is exactly

```text
C6=2p,  C5=2c,  C4=p^2+2r,
C3=2pc, C2=c^2+2pr, C1=2cr, C0=r^2
```

at `Lambda=0`, matching the charged triangular parametrization `(6.1)`.
The four extras `Lambda n_i` in `(1.1)` are the charged normal coordinates
`(6.2)` scaled by `Lambda`. The inverse formulae `(1.2)` are identities:

```text
C6/2 = p,
C5/2 = c,
C4/2 - C6^2/8 = (p^2+2r)/2 - p^2/2 = r,
n_i = (C_i-[K^2]_i)/Lambda  on D(Lambda).
```

The forward map in coefficient space is polynomial of type
`A^8 -> A^8` in `(Lambda,p,c,r,n0,n1,n2,n3)` to
`(Lambda,C0,...,C6)`, extended by the identity on the seven loads. Its
Jacobian, ordered as `(p,c,r,n3,n2,n1,n0) |-> (C6,C5,C4,C3,C2,C1,C0)`,
is block triangular: the high `3 x 3` block is

```text
( 2  0  0 )
( 0  2  0 )
( 2p 0  2 ),
```

determinant `8`, and the low `4 x 4` block is `Lambda` times the identity,
determinant `Lambda^4`. Over `Q` the product `8 Lambda^4` is a unit on
`D(Lambda)`. Combined with the polynomial inverse `(1.2)`, this is an
isomorphism of ambient schemes on `D(Lambda)`, not a projection of a load
and not a truncation of a series. At `Lambda=0` the map is no longer
invertible: it realises the common-quartic cone, as a divisibility chart
must.

Tangent motion. The same `3 x 3` block shows that every first-order
displacement of `(C_6,C_5,C_4)` is uniquely a displacement of `(p,c,r)`.
Adding extra normals `n_4,n_5,n_6` would be a gauge redundancy. The four
low extras `n_0,...,n_3` are complementary to that tangent space inside
the seven-dimensional coefficient space of a depressed octic. Because
`(p,c,r)` remain coordinates of the ambient, they may depend on `Lambda`
along an arc; first-order motion along the common-quartic family is
reabsorbed into the leading point `(p(0),c(0),r(0))` rather than being
projected out. The first differential of the unloaded tails vanishes in
every coefficient direction (Attack 2), including the four normal ones:
that does not create a missing tangent coordinate, it is the reason the
first obstruction is quadratic in the `n_i`.

Zero section. Along a regular arc in this chart,
`C_i-[K^2]_i = Lambda n_i` for `i<=3`. Vanishing of `(n_0,...,n_3)` at
`Lambda=0` is precisely divisibility by `Lambda^2`, i.e. higher normal
contact. The identically common-quartic family is the zero section as a
subscheme. Target §1 is right not to discard it from the set of all
strict arcs. Target §3 then saturates it away only to isolate the
order-one stratum; that is a stratification, not a contradiction. The
zero *normal* section does not force `k_{10}=0`; load contact is a
separate coordinate, correctly grouped with the normals only in `mN`.

---

## Attack 2 — unloaded vanishing, coefficient Jacobian, polynomial `Lambda^2` divisibility, loads and targets

**CONFIRMED.** The divisibility `(2.1)` is a polynomial identity in the
chart ring. Affine linearity and the displayed exponents exclude a hidden
lower-order cross term. The false load-direction identity `(7.2)` is not
consumed; the erratum is.

Unloaded vanishing. The charged Mason identification of reduced
exceptional support says that the first seven ordinary unloaded tails
vanish on `f=K^2`, and in fact every Faber tail vanishes there. The
parametrization `(p,c,r) |-> K^2` is polynomial. Composition of the tail
polynomials with that parametrization is a polynomial map `A^3 -> A^7`
which vanishes at every `Q`-point, hence is the zero polynomial. This
uses reduced support plus characteristic zero; it does not require the
seven-tail ideal to be radical.

Coefficient Jacobian. Let `f=K^2+varepsilon E` with `E` an arbitrary
polynomial of degree at most six (any coefficient direction). Write
`w=(K^2+varepsilon E)^{1/8}` and let `z(w,varepsilon)` be the inverse.
At `varepsilon=0` one has `w=K^{1/4}` and `dw/dz=(1/4)K^{-3/4}K'`. The
first variation of the inverse is

```text
z_1 = - (dw/dvarepsilon) / (dw/dz)
    = - (E/(8 K^{7/4})) / ((1/4) K^{-3/4} K')
    = - E / (2 K K').
```

The first variation of `g(z(w))` coming from the motion of `z` is

```text
3 K^2 K' z_1 = 3 K^2 K' (-E/(2 K K')) = -(3/2) K E,
```

a polynomial in `z`. Adding the first variation `g_1=(3/2)KE` of the
degree-twelve Faber polynomial cancels this identically as a series in
`w`. That choice of `g_1` is admissible (`deg((3/2)KE)<=10`) and is the
unique first-order deformation of `F_{12}` compatible with the defining
property `g(z(w))=w^{12}+O(w^{-1})`. Therefore every tail deforms as
`O(varepsilon^2)`. Equivalently, the binomial expansion `(7.1)` has
polynomial constant and linear terms in `E`, and those terms are absorbed
into `g` rather than into the negative `w`-series. The erratum leaves
`(7.1)` unchanged and restricts the false vanishing to the coefficient
directions.

Consequently, writing `U_ell(C)` for the unloaded tails and
`C=K^2+Lambda N` with `N=n_3 z^3+n_2 z^2+n_1 z+n_0`,

```text
U_ell(K^2+Lambda N) = a0 + a1 Lambda + a2 Lambda^2 + ...,
```

the coefficients `a0,a1` are polynomials in `(p,c,r,n_i)` which vanish
for all values, hence are the zero polynomials. Viewing the pulled-back
unloaded rows as polynomials in `Lambda` with coefficients in
`Q[p,c,r,n_i]`, the first two coefficients vanish, so `Lambda^2` divides
them in the polynomial ring. This is the division algorithm, not an
analytic order along reduced points.

Loads and targets. Inspection of the charged ten-tuples shows every
monomial is affine in `(k_{10},k_6,k_2)`. The exact construction
`g=F_{12}+k_{10}F_{10}+k_6 F_6+k_2 F_2` already forces that. Thus

```text
r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
 = U_ell(C)
 + Lambda^2 k10 D10_ell(C)
 + Lambda^6 k6  D6_ell(C)
 + Lambda^{10} k2 D2_ell(C),
```

with each `D_{j,ell}` a polynomial in `C`. Substituting
`C=K^2+Lambda N`:

- `U_ell` is divisible by `Lambda^2` as just shown;
- the `k_{10}` summand is visibly divisible by `Lambda^2`, even though
  `D10_ell(K^2)` is generically nonzero (erratum: it vanishes if and only
  if `K` is a square, the proper closed sublocus `c=0`, `p^2=4r`);
- the `k_6` and `k_2` summands are divisible by `Lambda^6` and
  `Lambda^{10}`;
- every nonzero target has exponent `14`, `16`, `18`, or `19`.

No load–load product exists to create a new valuation. No derivative
`D_{j,ell}` has a pole in `C`. Evaluating `D10_ell` at
`K^2+Lambda N` cannot produce a negative power of `Lambda`. There is
therefore no cross term of order `0` or `1`. This is the role of the
affine-load hypothesis named in the target, and it is discharged by the
charged tails.

The original audit identity `(7.2)` claiming `F_{10}(K^2)=K^5` and its
companions is false (wrong root: `w=K^{1/4}`, not `K^{1/2}`) and is not
used. Using it would have incorrectly dropped `k_{10}` from the first
jet. The target keeps `k_{10}` at order `Lambda^2`, which is the erratum.

---

## Attack 3 — dividing by `Lambda^2` preserves the scheme on `D(Lambda)`; saturations still required

**CONFIRMED.** The ideals agree on `D(Lambda)`. Unsaturated `Q1` is not
the Rees boundary. The remaining saturations are exactly those named in
target §3.

After Attack 2, each `Theta_ell=Phi_ell/Lambda^2` is a polynomial. In the
localization at `Lambda`, the element `Lambda^2` is a unit, so

```text
(Phi_1,...,Phi_7) = (Theta_1,...,Theta_7)
```

as ideals, not merely as radicals. Nilpotents on `D(Lambda)` match.

In the unlocalized chart ring the inclusion is proper: `V(Phi)` may carry
extra structure supported on `Lambda=0`. The closure of the interior is
the kernel of the map to the localization, i.e. the principal saturation
`(Theta_1,...,Theta_7):Lambda^infinity`. The charged one-parameter client
further saturates by `J` because `j!=0`. Only after those two colons may
one impose `Lambda=0`. The coefficient-irrelevant colon is then by
`(C0,...,C6)`, which on the special fibre of `(1.1)` equals the ideal
`(p,c,r)` (over `Q` the generators `2p,2c,p^2+2r` already give
`(p,c,r)` as ideals, not just as radicals).

The unsaturated special fibre `Q1=(Theta mod Lambda)` can contain
components that die under `Lambda`-saturation, and it cannot see the
`J`-saturation at all (`J` has been scaled out of `q_ell`). Target §2's
sentence that a strict arc in this chart specializes to the boundary of
the divided family *after* the usual `Lambda` and `J` saturations is the
correct implication. Target §3 forbids identifying unsaturated `Q1` with
the full Rees boundary, and forbids treating an AWS computation of `Q1`
as that endpoint. No such inference is made.

---

## Attack 4 — shape of `q_ell`; product-factor independence

**CONFIRMED.** The displayed shape is the Taylor expansion of `Theta_ell`
in `Lambda`. Independence of the six forbidden variables is literal
absence from the generators.

Substitute the affine decomposition into `Theta_ell`:

```text
Theta_ell
 = U_ell(K^2+Lambda N)/Lambda^2
 + k10 D10_ell(K^2+Lambda N)
 + Lambda^4 k6 D6_ell(K^2+Lambda N)
 + Lambda^8 k2 D2_ell(K^2+Lambda N)
 - Lambda^{10+ell} delta_ell.
```

The unloaded Taylor series in `Lambda` begins at order two, with
quadratic term `(1/2) Hess U_ell(K^2)(N,N)` and cubic-and-higher terms
in `N` carrying extra positive powers of `Lambda`. Reducing modulo
`Lambda` therefore keeps only that Hessian, a quadratic form in
`(n0,n1,n2,n3)` with coefficients depending on `(p,c,r)`. The Hessian is
taken in the four normal directions only, because `C_4,C_5,C_6` are
tied to `(p,c,r)` and do not carry a `Lambda n` displacement; mixed
second derivatives into the high coefficients are not hit by `N`.

The `k_{10}` summand reduces to `k10 D10_ell(K^2)`, the exact load
derivative at the common quartic. On the square sublocus of the erratum
this derivative is zero and the `k_{10}` term drops out of `q_ell`;
generically it does not. The remaining summands are
`O(Lambda^4)`, `O(Lambda^8)`, and `O(Lambda^{11})` or higher, hence zero
modulo `Lambda`. In particular `q_ell` does not involve
`k6,k2,mu2,mu4,mu6,J`.

This is not an elimination. Those six variables never appear in the
generators of `Q1`, so in the full coefficient-load space

```text
V(Q1) = V(q_1,...,q_7) x A^6.
```

No row is solved for a target load, no denominator `Lambda^{14}` or
`Lambda^{19}` is inverted, and the toy projection
`I=(x-Lambda m)` of the charged reduction is not performed. The first
boundary of the divided family, before `Lambda`- and `J`-saturation, is
that product.

---

## Attack 5 — both saturations in `(3.2)`, irrelevant locus, higher contact, nilpotents

**CONFIRMED.** Multi-generator saturation by `mK=(p,c,r)` then
`mN=(n0,n1,n2,n3,k10)` is the correct pair of colons. Neither colon
falsely excludes higher-contact arcs.

Irrelevant locus. The reduced common-quartic cone is the image of
`A^3_{(p,c,r)}` under `(6.1)`, a prime copy of `A^3`. The grading
`wt(p)=2`, `wt(c)=3`, `wt(r)=4` is the residual of `wt(C_i)=8-i`, and
the weighted `Proj` is `P(2,3,4)`. In the graded ring `Q[p,c,r]` the
irrelevant ideal is the unique graded maximal ideal of positive-degree
elements, namely `(p,c,r)`, not the principal product `pcr` and not a
proper subideal. Saturating by `pcr` would delete the coordinate faces
`p=0`, `c=0`, `r=0`, which the charged audit explicitly forbids.
Saturating by the ideal `(p,c,r)` deletes only the vertex, which is the
correct projective origin.

On the special fibre of `(1.1)` one has
`(C0,...,C6)=(2p,2c,p^2+2r,2pc,c^2+2pr,2cr,r^2)=(p,c,r)` as ideals over
`Q`, so the same colon is the coefficient-irrelevant colon of the
one-parameter client, transported to the chart.

Multi-generator semantics. For ideals `m,n`,

```text
(I:m^infinity):n^infinity
 = { f | m^j n^k f subset I for some j,k },
```

and geometrically

```text
V((I:m^infinity):n^infinity)
 = closure of V(I) \ (V(m) union V(n)).
```

This is not saturation by the sum `m+n`, which would remove only
`V(m) cap V(n)`, and it is not saturation by the product of generators.
Applied to `(3.2)`, sequential saturation removes components supported on
the origin in `(p,c,r)` and then components supported on the zero section
in `(n0,n1,n2,n3,k10)`, while keeping components that merely meet those
loci; their limit points on the zero section or at the origin are restored
by taking closure. The colon is an equality of ideals, so nilpotents and
embedded primes off `V(mK) union V(mN)` survive, and nilpotent thickening
supported on that union is discarded. That is the correct scheme-theoretic
complement.

Contact exactly one. A regular arc whose first nonzero normal/load
displacement in this chart is of order one has finite nonzero
`(n(0),k_{10}(0))` at a nonzero quartic, hence lands in
`V(Q1) \ (V(mK) union V(mN))` and therefore in `V(Q1^*)`. The implication
`Q1^*=(1) =>` every such order-one jet is absent, hence any remaining
strict arc has higher contact, is fail-closed in the stated direction. It
does not say there are no strict arcs. Higher-contact arcs live on the
zero normal section (and, if the `k_{10}` derivative also vanishes, on
the `k_{10}`-line of the square sublocus); they are removed from `Q1^*`
by design and are not declared empty.

On the square sublocus `c=0`, `p^2=4r` the polynomial `D10_ell(K^2)`
vanishes, so `q_ell` reduces to the Hessian in the `n_i`. Points with
`n=0` and `k_{10}` arbitrary then lie in `V(Q1)` and, for `(p,c,r)` not
the origin, survive in `Q1^*`. That is not a spurious first-order shadow:
if `K` is a square then `w^j=K^{j/4}` is polynomial for each
`j in {2,6,10}`, so all three load derivatives vanish identically at
`f=K^2`, and `k_{10}` is a genuine kernel direction of the tail map at
those points. It is a stratum for the next divided jet, which is what a
nonunit `Q1^*` is claimed to be. The slogan “contact exactly one” is
slightly loose on that kernel locus (normal contact is higher, the load
is unconstrained at this order), but no numbered identity fails, and the
fail-closed implication `Q1^*=(1) =>` higher contact remains valid.

`k_6` and `k_2` are correctly omitted from `mN`: they do not appear in
`Q1`, so forcing them to zero would not isolate a first-order condition.

---

## Attack 6 — source scope; no `(9,12)`, no terminal `U=4`, no Taylor, no order-two closure

**CONFIRMED.** Reduced support is used only for leading points and for
the polynomial vanishing of unloaded tails on the image of `(6.1)`. The
theorem does not identify the seven-tail scheme with the common-quartic
cone; the normals `n_i` exist precisely to probe thickening. The Hessian
in Attack 4 is that first thickening, not a claim that
`(r_1,...,r_7)` equals the ideal of the cone.

No `(9,12)` formula is imported. The cube chart `K=z^3+pz+c`,
`f=K^3`, and the false identity `F_6(K^3)=K^2` copied into the original
`(7.2)` are absent. The expansion `(1.1)` is the square of a depressed
quartic. The erratum's replacement — `w=K^{1/4}`, load derivatives vanish
iff `K` is a square — is the `(8,12)` statement.

The jet is independent of the terminal value of `U` because it is a
statement about the one-parameter family in `Lambda`, whose shape is the
Rees scaling of the ordinary tails. The charged source of that family is
the order-two `U=2,[6,2]` reduction; the algebra of `(1.1)`–`(3.2)` does
not evaluate a terminal `U=4` map, a Taylor polynomiality condition, or
an order-two closure. Target §4's AWS contract computes `Q1^*` as a
labelled first gate and forbids identifying it with the saturated
divided-family boundary. Target §5 states that the jet does not prove
the one-parameter boundary empty or nonempty, exclude `[6,2]`, close
order two, close `(8,12)`, prove maximum twelve, or prove JC2.

---

## Attacks that failed to break the claim

Treating Jacobian vanishing on the common quartic as only a statement
along reduced points, so that `Lambda^2 | Phi_ell` might fail as a
polynomial (the composed Jacobian is a polynomial on `A^3` vanishing
everywhere, hence zero; the `Lambda`-Taylor coefficients `a0,a1` are the
zero polynomials). Treating `(7.1)` as a `z`-Laurent remainder rather
than a cancellation in the `w`-series after moving `z(w)` and `g` (the
first variation of `z(w)` is exactly `-(3/2)KE` after multiplication by
`3K^2 K'`, cancelled by `g_1`). Importing the false load identity
`(7.2)` and dropping `k_{10}` from `q_ell` (the target does the
opposite). Adding redundant normals in `(C_4,C_5,C_6)` (the high
`3 x 3` is invertible). Saturating by the product `pcr` instead of the
ideal `(p,c,r)` (the target uses the ideal). Saturating by the sum
`mK+mN` instead of sequential colons (the target uses sequential colons,
which remove `V(mK) union V(mN)`). Reading `Q1^*=(1)` as emptiness of
the Rees boundary (the target says it forces higher contact only).
Eliminating `mu_2,mu_4,mu_6,J` from the first fibre because the even
rows solve for them on `D(Lambda)` (those variables are absent from
`q_ell` without being solved; the finite-quotient projection is not
taken). Identifying reduced common-quartic support with the seven-tail
scheme (the chart is an ambient automorphism on `D(Lambda)`, and the
Hessian probes thickening). Importing a `(9,12)` cube, a terminal `U=4`
map, a Taylor condition, or order-two closure (none is used).

---

## Scope that remains open

Whether `Q1^*` is the unit ideal or a nonempty list of strata is not
decided. The saturated divided-family boundary
`((Theta_1,...,Theta_7):Lambda^infinity):J^infinity` at `Lambda=0`,
after irrelevant saturation, is not computed. Higher-contact jets,
including the square-locus load kernel, remain. Neither Taylor family
is imposed. The jet does not exclude `[6,2]`, close order two, close
`(8,12)`, prove maximum twelve, or prove JC2.

CONFIRMED
