# Hostile review — delayed-load source exclusion of the affine-Faber `A` cubic

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md` |
| Target SHA-256 | `9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695` |
| Charged cubic forms | `xmodel/max12-812-order2-affine-faber-exceptional-cubic-forms-source-ray-triage-20260826.md` |
| Charged cubic-forms SHA-256 | `40b6d15eb23fc85038182146d8f044dee3d37c7c7e6fc4880e0ac3d223297d5f` |
| Charged total-Rees audit | `xmodel/max12-812-order2-affine-faber-total-rees-gate-a-audit-20260826.md` |
| Charged total-Rees SHA-256 | `24592572b4a6469ca5cdf446d02a8acc71ca6ee540ad3b73b92e9f925b10edb6` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim of the target |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged artifacts were opened only because they are named; no producer status line, no printed residual, and no charged `PASS`/`CONFIRMED` string is evidence |
| Method | SHA-256 of the target, both charged parents, and every frozen pin named in target §0; independent reconstruction of the load graph, terminal valuation, first-normal divisibility, ordinary connection coefficient of `h2` in `R6`, and every displayed `A`-face substitution. No Singular, Sage, SymPy, msolve, Lean, or other CAS |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695`,
matching the required pin. Independently recomputed SHA-256 of both charged
parents match their required pins. Every frozen pin named in target §0
rehashes to the printed digest. Producer verdict language, the target's
own status line, AWS stdout residuals, and the total-Rees audit's typed
tokens `DELAYED_LOAD_P2` / `A_RAY_UNIT_BEFORE_P2` were not used as
algebraic evidence. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

The integral substitution `k10=Lambda^12 K10`, `k6=Lambda^8 K6`,
`k2=Lambda^4 K2` places every effective lower load of the one-parameter
source at `Lambda^14`. On an exact square the unloaded `F12` tail is
absent, so the grade-fourteen face is the ordinary affine-`mu2` system
with later targets at relative orders two, four, and five. The graph is a
polynomial domain, hence prime and `Lambda`-torsion-free, and is inverted
on `D(Lambda)` by the three displayed quotients. The specialization
`K10=1` is a chart of `D(K10)`, not a hidden weighted Kummer
normalization and not an exhaustive load-fan theorem.

A unit source `J` meeting a cubic normalized terminal five orders after
that face forces `3 v(t)=5 v(Lambda)`, primitively ramified as
`Lambda=sigma^3`, `t=sigma^5`. Under that ramification every leading
square-normal of the `A`-face weights occurs strictly before the loaded
face, so the unloaded quadratic `(3/8) N^2/Q0` must vanish in the first
seven ordinary rows. Those seven rows vanish if and only if `Q0` divides
`N^2`. On `D(r*D)` the centered quartic is squarefree and a degree-at-most-three
normal is zero. On `r=0` one has `Q0=z^2(z^2+p)` and the UFD divisor
`D_{Q0}=z(z^2+p)`, so the only surviving cubic normal is
`N=v z(z^2+p)` with `u=(p/2)v`.

Independent substitution of the charged `A`-face cubic forms then kills
both residual charts: on `D(r)`, after `e0=e2=u=v=0` and the `A1`-solution
for `g`, the row `A3` equals the unit `5 x^3 D/128`; on `r=0`, after the
divisor constraint, `A1` and `A3` solve `v=-x^3/(5 p^2)` and
`g=45 x^2 p/128 + 3 b p^2/8`, every `b` term cancels in `A5`, and the
residual is the unit `5 x^3 p^3/1024`. The two units cover `D(D x)`. The
specific rational normalized witness is additionally rejected at
`Lambda`-order ten by the ordinary rows `R2=3/3200`, `R6=3/6400`, with
the factor `1/2` in row six equal to `r/2` at `r=-1`. Tangential jets of
`p,D`, a moving center in the charged centered chart, ramification deck,
earlier normals, and nilpotents on a DVR do not cancel either unit
residual. The claim is only the primitive unit-`J` cubic `A` client on
this integral delayed-load ray.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md` | `9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695` | target (matches required pin) |
| `xmodel/max12-812-order2-affine-faber-exceptional-cubic-forms-source-ray-triage-20260826.md` | `40b6d15eb23fc85038182146d8f044dee3d37c7c7e6fc4880e0ac3d223297d5f` | charged `A`-face cubic forms (1.1) and `A1,A3,A5,J3`; substituted by hand, not trusted as printed residuals |
| `xmodel/max12-812-order2-affine-faber-total-rees-gate-a-audit-20260826.md` | `24592572b4a6469ca5cdf446d02a8acc71ca6ee540ad3b73b92e9f925b10edb6` | charged Gate-A audit; used only as named source of the one-parameter row, load graph, and ordinary connection, not as a total-Rees theorem |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | target §0 pin; literal source `(0.1)` |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md` | `1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de` | target §0 pin; opened because named |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | target §0 pin; `k10=0` criterion `K\|N^2` and UFD divisor; independently re-proved below on the delayed ray |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md` | `08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa` | target §0 pin; opened because named; not used as a calculation |

All seven hashes match the values printed in the target, the review prompt,
or the charged parents. Characteristic 65521 is a software control only
and is not used.

---

## Strongest exact theorem that survives

Work over a field of characteristic zero. In the one-parameter source

```text
Phi_l = r_l(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
        - Lambda^(12+l) delta_l,
(delta_1,...,delta_7)=(0, mu2, 0, mu4, 0, mu6, J/4),
```

impose the integral delayed-load graph

```text
k10=Lambda^12 K10,     k6=Lambda^8 K6,     k2=Lambda^4 K2
```

and restrict to the chart `K10=1` of `D(K10)`. Let `C` be near the centered
exact square `Q0^2` with `Q0=z^4+p z^2+r` and `D=(p^2-4r)/4 != 0`. On the
exceptional `A` face use the charged weights

```text
c=t x,
n2=t^2 e2,                 n0=t^2 e0,
n3=t^3 v,                  n1=t^3 (u+(p/2)v),
K6=15 D/8 + t^2 b,         K2=15 D^2/16 + t^2 g,
```

with `x D` a unit, and take the first normalized terminal to be the cubic
`J3 t^3` with `J3` a unit. After the primitive ramification
`Lambda=sigma^3`, `t=sigma^5` forced by a unit source `J`, there is no
formal arc solving the delayed-load source through the cubic grade.

Concretely: the leading square-normal must satisfy `Q0 | N^2`. On `D(r)`
this forces `e0=e2=u=v=0`; substitution of the charged forms then yields
the unit ordinary residual `A3=5 x^3 D/128`. On `r=0` one has `p` a unit,
`e0=e2=0`, and `u=(p/2)v`; substitution yields the unit residual
`A5=5 x^3 p^3/1024`. The two charts cover `D(D x)`. The same predecessor
rejects the specific normalized rational point
`(D,p,x,v)=(1,0,1,-1/20)` at `Lambda`-order ten, before the loaded face.

This is a characteristic-zero statement on the named integral ray, in the
centered ordinary-Faber chart, for a primitive unit-`J` cubic `A` client.
It is not a total-Rees overlap, an exhaustive load Newton-fan theorem, a
later-`J` theorem, a `K`-face theorem, a `D=0` or `K10=0` theorem, a
terminal/`[6,2]`/Taylor theorem, or an order-two, `(8,12)`, maximum-twelve,
or JC2 result.

---

## 1. Literal source substitution, face, and graph

The one-parameter source evaluates ordinary tails at the scaled loads
`Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2`. Substituting the charged
graph gives the three effective loads

```text
Lambda^2 * Lambda^12 K10 = Lambda^14 K10,
Lambda^6 * Lambda^8  K6  = Lambda^14 K6,
Lambda^10* Lambda^4  K2  = Lambda^14 K2.
```

Every finite lower load therefore first occurs at `Lambda^14`. The
ordinary tail map is affine-linear in `(k10,k6,k2)` because the generating
function is `g = F12 + k10 F10 + k6 F6 + k2 F2` and the inverse-root
coordinate `z(w)` depends only on the octic `C`. On an exact square
`C=Q^2` one has `F12^{3/2}=Q^3`, a polynomial, so the unloaded negative
tail vanishes identically. Dividing the source by `Lambda^14` therefore
yields the ordinary Faber rows of the loaded polynomial with loads
`(K10,K6,K2)`, equated to the targets that exist at this order.

Those targets are

| source datum | absolute power | relative to grade 14 |
|---|---:|---:|
| delayed loads `(K10,K6,K2)` | `Lambda^14` | `0` |
| `mu2` | `Lambda^14` | `0` |
| `mu4` | `Lambda^16` | `2` |
| `mu6` | `Lambda^18` | `4` |
| `J/4` | `Lambda^19` | `5` |

Odd targets are identically zero. Hence the grade-fourteen face is exactly
the displayed system

```text
R1=R3=R4=R5=R6=R7=0,           R2=mu2.
```

This is an equation at grade fourteen, not an identity for arbitrary
loads: `R4` and `R6` constrain `(K6,K2)` onto the affine-Faber graph, and
`mu2` absorbs `R2`. Row four's target begins at relative order two, row
six's at relative order four, and row seven's at relative order five, as
claimed.

The graph ideal

```text
(k10 - Lambda^12 K10,  k6 - Lambda^8 K6,  k2 - Lambda^4 K2)
```

is generated by a regular sequence of graph relations. The quotient is
the polynomial ring in `(Lambda, K10, K6, K2)`, a domain, hence prime and
`Lambda`-torsion-free. On `D(Lambda)` the inverse is the three displayed
divisibility quotients. This is a one-sided row map for the chosen
valuation ray. It does not commute with the registered coefficient-
irrelevant colon, and it does not prove fan coverage.

The target specializes `K10=1` and states that this is not a claim that
the specialization normalizes every point of `D(K10)`, and that no
exhaustiveness of load valuations is asserted. Both disclaimers are
necessary and are present. On `D(K10)` the two-sided unit change
`beta=K6/K10`, `gamma=K2/K10` does not require a square root. A full
weighted normalization of the ordinary source would instead impose
`q^2 K10=1` with deck `q |-> -q` and produce the ratios `K6/K10^3`,
`K2/K10^5`. No such Kummer claim is made. There is no hidden
normalization.

---

## 2. Primitive terminal tie

After division by `Lambda^14`, the remaining row-seven target is
`Lambda^5 (J/4)`. A normalized cubic terminal is `R7=(J3/4) t^3` plus
higher terms. Equating leading terms against a unit source `J` gives

```text
J3 t^3 = J Lambda^5.
```

With `J` and `J3` units this is `3 v(t)=5 v(Lambda)`. The positive
integer solutions are `v(Lambda)=3m`, `v(t)=5m`. The primitive solution
is `m=1`, realized by `Lambda=sigma^3`, `t=sigma^5`. Then
`t^3=sigma^{15}=Lambda^5`, so the cubic `J` meets grade nineteen.
For `m>1` the same cubic algebra still applies and is likewise
excluded; non-primitive ramification is not a loophole.

Under `(3.3)` the `A`-face normals of `(3.1)` occur at sigma-orders ten
(`n2,n0 ~ t^2`) and fifteen (`n3,n1 ~ t^3`). Their unloaded quadratics
occur at sigma-orders twenty and thirty. The loaded face is
`Lambda^14=sigma^{42}`. Both quadratics strictly precede the face, so
they must vanish as ordinary rows: there is no source target before
grade fourteen.

The identification of the first possible normalized terminal with a cubic
is the `A`-face content of the generic complete-local theorem (the odd
Jacobian has kernel the `c`-direction, and that kernel is `R7`-null). The
present target takes `J3 t^3` as a starting hypothesis, as the assignment
requires. It does not re-prove that no linear `J` exists on the `A` face,
and it does not treat a first normalized `J` of order `>3`.

---

## 3. Unloaded first-normal condition, independently

Near the exact square write `C=Q^2+E` with `deg(E)<=3`. The binomial
expansion

```text
(Q^2+E)^{3/2}
  = Q^3 + (3/2) Q E + (3/8) E^2/Q - (1/16) E^3/Q^3 + ...
```

has polynomial first two summands. The first possible unloaded negative
tail is therefore `[(3/8) E^2/Q]_-`. Tangential motion of `Q` is absorbed
into a moving quartic by square division, so the leading transverse jet
`N` may be taken of degree at most three. Before grade fourteen the
delayed `k10` has not entered, so the first-normal load term
`k10 K^{5/2}` is absent.

Let `Q0` be monic of degree four and `N` of degree at most three. Write
`N^2 = Q0 P + R` with `deg R < 4`. The negative series of `N^2/Q0` is the
proper fraction `R/Q0`. At infinity `Q0 ~ z^4`, so if `R != 0` then
`R/Q0` has valuation `4-deg(R) in {1,2,3,4}`. The first nonzero
`z`-Laurent coefficient therefore lies among `h1,...,h4`. Vanishing of
the first seven negative coefficients forces `R=0`, i.e. `Q0 | N^2`. The
converse is immediate. The change from the first seven negative
`z`-coefficients to the first seven ordinary Faber coefficients is
unitriangular, so the seven ordinary rows of `(3/8) N^2/Q0` vanish if and
only if `Q0 | N^2`. No radical is taken.

On the centered chart `Q0=z^4+p z^2+r`. The derivative is
`Q0'=2z(2z^2+p)`. The resultant computation

```text
prod Q0'(roots) = 2^4 (prod roots) prod(2 z_i^2+p)
                 = 16 r * 16 D^2
                 = 256 r D^2
```

gives `disc(Q0)=256 r D^2` in characteristic zero (the sign
`(-1)^{n(n-1)/2}` is `+1` for `n=4`). Thus `Q0` is squarefree precisely
on `D(r D)`. The target's phrase “on `D(r)`, discriminant a nonzero
scalar times `r D^2`” is read against the standing open `D != 0` of
`(2.1)`; the squarefree locus is `D(r D)`, and that is the locus used.

On `D(r D)`, squarefree plus `Q0 | N^2` yields `Q0 | N`. Then
`deg N < deg Q0` forces `N=0`. In particular `e0=e2=u=v=0`.

On `r=0` one has `D=p^2/4`, so `p` is a unit, and

```text
Q0=z^2 (z^2+p).
```

The two roots of `z^2+p` are simple and distinct from `0` because `p != 0`.
The UFD divisor is `D_{Q0}=prod (z-a)^{ceil(m_a/2)}=z(z^2+p)`, and
`Q0 | N^2` if and only if `D_{Q0} | N`. A normal of degree at most two
is then zero. A cubic normal must be a scalar multiple of the degree-three
polynomial `z(z^2+p)`, so

```text
N = v z(z^2+p) = v z^3 + p v z.
```

Comparing with `n3=t^3 v` and `n1=t^3(u+(p/2)v)` gives `u=(p/2)v`. This
normal satisfies the predecessor identically: `N^2/Q0=v^2(z^2+p)` is a
polynomial, so every negative coefficient vanishes. The cubic loaded
forms are then mandatory; they are not optional.

Higher unloaded terms `E^3/Q^3` occur at triple the normal order. For the
cubic normal this is `t^9=sigma^{45}`, strictly after the loaded face
`sigma^{42}`. They do not pollute the cubic grade.

---

## 4. Independent substitution of the charged `A`-face forms

The charged cubic forms are treated as algebraic input, not as printed
residuals. The `A`-face identity `beta=15 D/8` is independent of those
forms: with `s=5D-4 beta`, the divisor `5D+2s=0` is `15D-8 beta=0`, hence
`beta=15 D/8`. The affine-Faber even constraint
`15 Delta^2-64 beta Delta+256 gamma=0` with `Delta=4D` then forces
`gamma=15 D^2/16`. So `(3.1)` is the unique `A`-face point of the
grade-fourteen graph, plus `t^2` load jets.

### 4.1 Chart `D(r)`

Predecessor forces `e0=e2=u=v=0`. The charged `A1` collapses to

```text
A1 = -5/32 x^3 p - 3/4 b x D + 1/2 g x.
```

On `D(x)` this is `g=(5/16) x^2 p + (3/2) b D`, which is `(3.6)`. The
charged `A3` with the same vanishing normals is

```text
A3 = 5/128 x^3 p^2 + 5/128 x^3 D + 3/16 b x D p - 1/8 g x p.
```

Substitute `g`:

```text
-1/8 g x p
  = -1/8 x p ((5/16) x^2 p + (3/2) b D)
  = -5/128 x^3 p^2 - 3/16 b x D p.
```

The `p^2` terms cancel and the `b` terms cancel, leaving

```text
A3 = 5/128 x^3 D.
```

On `D(D x)` this is a unit. No primitive cubic solution exists on
`D(r D x)`. The first identity of §3 that could have failed is this
cancellation; it holds with the displayed constants.

### 4.2 Chart `r=0`

Now `D=p^2/4`, `e0=e2=0`, and `u=(p/2)v`. Then `D^2=p^4/16` and
`u D=p^3 v/8`. The charged `A1` becomes

```text
A1 = -5/32 x^3 p - 3/16 b x p^2 + 1/2 g x + 25/256 p^3 v.
```

Solving for `g`,

```text
g = 5/16 x^2 p + 3/8 b p^2 - (25/128) (p^3 v)/x.
```

The charged `A3` becomes

```text
A3 = 25/512 x^3 p^2 + 3/64 b x p^3 + 25/1024 v p^4 - 1/8 g x p.
```

Substitute `g`. The terms `±(3/64) b x p^3` cancel, and

```text
A3 = 5/512 x^3 p^2 + 25/512 v p^4.
```

On `D(p)` this forces `v=-x^3/(5 p^2)`, which is the first half of
`(3.9)`. Feeding `v` back into `g` produces

```text
g = 5/16 x^2 p + 3/8 b p^2 + 5/128 x^2 p
  = 45/128 x^2 p + 3/8 b p^2,
```

which is the second half of `(3.9)`.

Now `A5` with the same substitutions. The `g`-contribution collapses to
`-(3/64) g x p^2`. Inserting `g` gives the `b` terms

```text
3/512 + 3/256 - 9/512 = 3/512 + 6/512 - 9/512 = 0
```

in units of `b x p^4`. Every `b` term cancels, as claimed. The remaining
content is

```text
A5 = 45/8192 x^3 p^3 + 25/8192 v p^5.
```

The solved `v` contributes `-5/8192 x^3 p^3`, so

```text
A5 = 40/8192 x^3 p^3 = 5/1024 x^3 p^3.
```

On `r=0` with `D x != 0` one has `p` a unit, so this is a unit. The two
unit residuals cover `D(D x)`. There is no first wrong identity in
`(3.6)`, `(3.7)`, `(3.8)`, `(3.9)`, or `(3.10)`.

As a consistency check on the charged forms themselves, the rational
point `(D,p,x,v)=(1,0,1,-1/20)` with the other jets zero gives
`A1=0`, `A3=5/128+25/32*(-1/20)=0`, `A5=0`, and
`J3=-15/128 x^3 D^2 + 25/32 v D^3=-5/32`. This is a normalized ordinary-
Faber cubic, not a source solution; it is the input of §4, not a
counterexample to §3.

---

## 5. Direct rational-witness rejection

At `(D,p,x,v)=(1,0,1,-1/20)` with the other jets of `(4.1)` zero, the
leading normal is `N=-(t^3/20) z^3`. Also `r=-1` because
`D=(p^2-4r)/4=1` forces `r=-1`, so `Q0=z^4-1`. Then

```text
(3/8) N^2/Q0
  = (3/8)(1/400) t^6 z^6/(z^4-1)
  = (3/3200) t^6 z^6/(z^4-1).
```

Under `(3.3)`, `t^6=sigma^{30}=Lambda^{10}`. The Laurent expansion at
infinity is

```text
z^6/(z^4-1) = z^2 (1-z^{-4})^{-1} = z^2 + z^{-2} + z^{-6} + z^{-10}+...,
```

so the first seven negative coefficients satisfy `h2=h6=3/3200` and
`h1=h3=h4=h5=h7=0`. (The polynomial part `z^2` is not a tail.)

The ordinary connection, restricted to `h1=0`, includes

```text
R2=h2,
R4=h4+(p/2) h2,
R6=h6 + p h4 + (p^2/8 + r/2) h2.
```

The coefficient of `h2` in `R6` is independent of any producer print. From
`z(w)=w-(p/4)w^{-1}+(p^2/32-r/4)w^{-3}+O(w^{-5})` (at `c=0`), one has
`z^{-2}=w^{-2}(1+varepsilon)^{-2}` with
`varepsilon=-(p/4)w^{-2}+(p^2/32-r/4)w^{-4}+...`. Expanding
`(1+varepsilon)^{-2}=1-2varepsilon+3varepsilon^2` through `w^{-4}` yields
the coefficient `p^2/8+r/2` of `w^{-6}` in `z^{-2}`. At `p=0`, `r=-1`
this is `r/2=-1/2`. Therefore

```text
R2 = 3/3200,
R6 = 3/3200 + (-1/2)(3/3200) = 3/6400,
```

and `R4=0`. Both displayed ordinary rows are nonzero. There is no source
target at `Lambda`-order ten. The specific arc is rejected four orders
before the loaded face and nine orders before the proposed terminal. The
factor `1/2` in row six is `r/2`, not a universal conversion
`R6=h6/2`. The signs are those of `+(3/8)N^2/Q0` (both summands of the
first-normal principal part are positive) and of `r=-1`. Changing the
overall sign would leave both rows nonzero, so the exclusion is sign-stable.

This is a special-case kill of a witness that lives on `D(r)` with `N != 0`.
It does not replace §3: the general `D(r)` exclusion after the predecessor
has already set `N=0` is the unit `A3`.

---

## 6. Omissions

**Tangential jets of `p` and `D`.** The first variation `L` of the odd
rows in `c` vanishes identically on the `A`-face graph for every
`(p,D)`. A `t^2` jet of `p` or `D` that remains on the graph therefore
contributes nothing to the `t^3` odd rows. A `t^2` jet that leaves the
graph is already parameterized by the load jets `b,g`, which cancel in
both residuals. Mixed derivatives enter only at `t^5`. Neither unit
residual is affected.

**Moving center.** The charged forms and the central point `(2.1)` are
centered: `Q` has no `z^3` term. A translation coordinate is a further
odd direction, absent from the charged ordinary chart. It is a total-Rees
gauge obligation of a later overlap map, not a cancellation of
`5 x^3 D/128` or `5 x^3 p^3/1024` in the centered chart. It does not
invalidate the narrow claim.

**Deck and ramification.** The cubic ramification has deck
`sigma |-> zeta_3 sigma`. The residuals are independent of the sheet.
A common refinement with a square Kummer `Lambda=tau^2` is
`Lambda=q^6`, which only rescales the same primitive ratio `3:5`. Extra
positive `J`-valuation replaces `(3.2)` by `3 v(t)=5+j0` and is
firewalled.

**Earlier normals.** On `D(r)` the predecessor forces every leading
normal of degree at most three to vanish, so an earlier normal is
likewise zero. On `r=0` a leading cubic along `D_{Q0}` produces no
unloaded quadratic at all; placing it earlier still leaves the loaded
cubic residual a unit at the cubic grade. Even normals at odd orders
break the source involution `z |-> -z`; if retained, their squares occur
even earlier and are killed on `D(r)` by the same divisibility.

**Nilpotents.** The claim is about formal arcs, whose value rings are
domains. On a DVR one cannot have `N^2=0` with `N != 0`. On the
localized charts `D(x D)` and `D(x p)` the residuals are units, so even
a nonreduced coefficient ring cannot absorb them after localization.
Scheme-theoretic nonreduced structure of a `Lambda=0` special fibre is
outside the primitive-arc statement and is already firewalled by the
target's refusal to compute the full nonreduced total-Rees boundary.

**`K10=1` and `x=1`.** Both are unit charts of `D(K10)` and `D(x)`. The
target flags the former. Neither is a weighted normalization of the
complete ordinary source.

None of these omissions cancels a displayed unit or produces a primitive
unit-`J` cubic `A` solution on the named ray.

---

## 7. Firewall

The strongest exact theorem is the exclusion, in characteristic zero, of
a primitive unit-`J` cubic `A` client on the integral delayed-load ray
`(1.2)`, after the ramification `(3.3)`, in the centered ordinary-Faber
chart, on `D(D x)`.

The target does not prove, and this review does not promote, any of the
following:

- exhaustiveness of `(1.2)` among load Newton faces, including
  `K10=0` and every other valuation of `(k10,k6,k2)`;
- a first normalized `J` of order strictly larger than three;
- the `K` face `5D-2s=0`;
- the loci `D=0` or `x=0`;
- a two-sided total-Rees chart, overlap maps, `Lambda`/`J` torsion, or
  the registered coefficient-irrelevant open;
- terminal `[6,2]` beyond the cubic valuation, or either Taylor family;
- an ungauge moving-center coordinate;
- order two, `(8,12)`, maximum twelve, or JC2.

The charged total-Rees audit's `TOTAL_REES_GATE_A` remains fail-closed.
The present theorem is a source-row exclusion on one named ray, not a
Gate-A overlap.

---

## Scope and surviving theorem

Smallest failing identity: none.

Smallest missing hypothesis: none that breaks a numbered claim. The
cubic forms `A1,A3,A5` are charged input; they were independently
substituted, and the displayed cancellations and residuals are correct.
The cubic character of the first normalized terminal is an `A`-face
starting hypothesis, as scoped.

Strongest exact theorem that survives: the primitive unit-`J` cubic
`A` client on the integral delayed-load ray `(1.2)` after `(3.3)` has
no solution on `D(D x)`.

Precise scope firewall: as in target §5 and §7 above.

CONFIRMED
