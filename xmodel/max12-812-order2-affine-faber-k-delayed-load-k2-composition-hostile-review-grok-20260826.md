# Hostile review — delayed-load affine-Faber `K` face to discriminant K2

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md` |
| Target SHA-256 | `6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989` |
| Overall verdict | **REPAIR** |
| Smallest failing identity | none |
| Smallest missing valuation face | kernel (and kernel-tied complementary) of order strictly less than `v(Lambda)/2`, on which the initial form is the quadratic Kuranishi map without the intrinsic `-m^3` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews were opened only because they are named; no producer status line and no charged `CONFIRMED`/`REPAIR`/`PASS` string is evidence |
| Method | source reading, SHA-256 of every named pin, and hand identities; no Singular, Sage, msolve, Lean, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989`,
matching the required pin. Independently recomputed SHA-256 of every
artifact pinned in target §0 and §5 match those pins. Producer verdict
language, the target's own status line, charged review tokens, and
finite-field lanes were not used as characteristic-zero algebra. No file
other than this review was written.

---

## Verdict

**REPAIR.**

The unloaded first-normal analysis of the delayed-load affine-Faber `K`
kernel on `D(D)` is correct, and the repeated-root point really does lie
in the `e`-unit K2 chart rather than on the routed square intersection
`b=e=0`. Exact-`Q` V3 lower-unitriangular row equality identifies the
complete frozen-source K2 ideal with the analytic ideal in every
localization used below. Delayed loads cannot enter the K2 grade, so
`kappa=0` is forced rather than inherited. On the balanced half-weight
ray, and on every later coordinate face, the repaired colons

```text
(I_K2 : kappa^infinity) = (1)                 in R_m,
((I_K2 + (kappa)) : e^infinity) = (1)         in R_m
```

together with the intrinsic `-m^3` term empty the chart.

The composition does **not** prove that every formal or Puiseux successor
is empty, because the normalized-blowup lemma weights only the transverse
deformation coordinates and then cites the charged K2 scheme as if it
were the initial form of every remaining DVR. The intrinsic `-m^3` lives
at absolute grade `3 v(Lambda)`, not at the weighted order of
`(x,y,complementary)`. There is therefore a Newton face

```text
mu := v(kernel) < v(Lambda)/2,
nu := v(complementary) >= 2 mu,
kappa = 0,
```

whose first tail after the first-normal is the quadratic map in the
half-weight kernel, **without** `-m^3`. That initial form is not a point
of the charged K2 scheme on `D(m)`: a K2 point with `kappa=0` must
satisfy `6 u_3 = m^3 != 0`, while the early face requires `u_3=0`.
Complementary linear pivots do not kill it, because the kernel is the
linearization kernel. Root-splitting of type `delta K = x A` at
fractional order is exactly this face.

No countermodel on `D(D)` was found. At the specific point
`(b,e)=(0,p)` the early quadratic is nondegenerate and forces
`(x,y)=(0,0)`, contradicting a leading form. That identity is not in the
producer. Filling this one face restores the stated emptiness. The
sigma-through-15 moving-double-root unit is corroboration of the
root-preserving balanced/late chart only; it does not cover the missing
face and is not used as exhaustiveness.

**REPAIR**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md` | `6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989` | target (matches required pin) |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | `k10=0` criterion `K\|N^2` and UFD split into square, discriminant, and zero-normal |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md` | `08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md` | `2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5` | named in target §0; the delayed-load first-normal is the `k10=0` slice, so the nonzero-`k10` lemma is not consumed |
| `xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md` | `73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md` | `20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341` | analytic five-row K2 ideal, recurrences, intrinsic `-m^3`, square-intersection routing |
| `xmodel/max12-812-order2-discriminant-halfweight-k2-support-review-terra-20260826.md` | `f93ecb4320fadff500638fc6fa7bdfca904ed5556b7a13add4cddb9b40a76b70` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md` | `f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b` | controlling localization: both unit colons live in `R_m`, not in a hidden `b`-inverted ring |
| `cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/FREEZE.sha256` | `6e00100d10f5d05b5351d2ca7fd8535a9b0df49671860d51862b73d64e6319c9` | V3 freeze manifest |
| `cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULT.md` | `d0327db2e2214bc897be85d4373bf35e063c2a540254b2b33986f88755eca0e8` | exact-`Q` lower-unitriangular statement |
| `cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULTS.sha256` | `6eb104a3288bf663aced9b8aa6f0bdac3a91c9cb6bd26d44e4b4989a5efe7c36` | V3 result manifest |
| `cases/max12_812_order2_affine_faber_k_moving_discriminant_sigma15_20260826/RESULT.md` | `2ce2cb39f671fbfb545a5e9f44b6a0a75927b3624f0a6b87eecf80685f28dfe1` | finite moving-double-root unit; corroboration only |
| `cases/max12_812_order2_affine_faber_k_moving_discriminant_sigma15_20260826/EVIDENCE.sha256` | `7f94b11f3527927e34b94a53d3b1bdb6c236a9c18d42f80a52dafe7bb7fd2133` | sigma-15 evidence manifest |

Exact-`Q` V3 stdout SHA-256
`0763ca918737335ea7f77e08941cf568692d9fc67fbb6d85ab64ea35f1b7fe56`
is the corresponding `RESULTS.sha256` row. Exact-`Q` K2-support stdout
SHA-256
`7de0a587270481736b0b85b76cffce761567d7778d014cc0ddd4cd557ed0cb26`
matches the charged support theorem. Characteristic-32003 and
characteristic-65521 lanes are software controls and are not used as
characteristic-zero evidence.

Charged algebraic input actually consumed: the `k10=0` identity `q1=...=q7=0`
iff `K` divides `N^2`, with `D_K | N` after algebraic closure; the
discriminant family covering `[2,1,1]` and `[3,1]`; squarefree `K` forcing
`N=0`; the analytic K2 rows

```text
6 u_3 - m^3 + 16 kappa c_13 = 0,
6 u_n + 16 kappa c_(10+n) = 0,     n=4,5,6,7,
```

with recurrences `u_n + b u_(n-1) + e u_(n-2)=0` (`n>=5`) and
`(n+1) c_(n+1) = b (5/2-n) c_n + e (6-n) c_(n-1)`; the two colons in
`R_m=Q[b,e,h,y,kappa,m][m^(-1)]`; routing of `b=e=0` to the square; and
the exact identity `16 S_l = sum_(j<=l) T_(l,j)(b,e) H_j` with `T`
lower unitriangular of unit diagonal, obtained from
`q^4 + b v q^3 + e v^2 q^2 = 1`.

---

## Strongest exact theorem that survives

Work over a field of characteristic zero, on the integral delayed-load
ray `k10=Lambda^12 K10`, `k6=Lambda^8 K6`, `k2=Lambda^4 K2`, and on
`D(D)` with `D=(p^2-4 r)/4`. Let the exceptional affine-Faber `K`
kernel be the projective pair `(x,y)!=(0,0)` with leading square-normal

```text
Q0 = z^4 + p z^2 + r,
N1 = y z^3 + (2 D x + (p/2) y) z.
```

Let `lambda = v(Lambda)>0` on a ramified DVR, let `mu` be the valuation
of the transverse half-weight kernel in moving `A`-coordinates after
tangent absorption into `(a,d,m)`, and let `nu` be the valuation of the
three complementary directions including the first load.

1. On `D(r)` the quartic `Q0` is squarefree and `Q0 | N1^2` forces
   `N1=0`, hence `x=y=0`, contradicting projectivity. This open is empty
   at the unloaded first-normal gate.
2. On `r=0` one has `D=p^2/4` with `p` a unit, `Q0=z^2(z^2+p)`, and
   `Q0 | N1^2` iff `y=p x` with `p x != 0`. In discriminant coordinates
   this is exactly `(a,b,e,m)=(0,0,p,p x)`, with `e` and `m` units. It
   is not the routed square intersection `b=e=0`.
3. Delayed loads contribute first at source grade `Lambda^14`. The
   intrinsic K2 grade is `Lambda^3`. Thus `kappa=0` at every grade
   relevant below. A complementary load tying the balanced K2 face
   (`nu=lambda`) is not a delayed-load phenomenon; the first colon in
   `R_m` would empty it anyway.
4. If `nu < 2 mu`, a complementary linear pivot of the first-normal
   Jacobian is nonzero and the arc already fails an earlier initial
   row. At the point (2) the three complementary columns still have
   rank three, even though the displayed `A^{-3}` minor with `c_13`
   vanishes: the `kappa` column is a unit multiple of `c_14 e^7` on
   `A^{-4}`.
5. If `mu >= lambda/2` and `nu >= lambda`, the first new tail after
   the first-normal is the charged complete-source K2 map, including
   `-m^3`. The V3 identity makes this the analytic ideal. The second
   colon in `R_m` then empties `D(e)`, and the successor remains in
   `D(e)` because `e(0)=p` is a DVR unit. Coordinate faces with
   vanishing kernel or complementary leading coefficients are included;
   the all-zero face is killed by `-m^3`.
6. The remaining face `mu < lambda/2`, `nu >= 2 mu`, `kappa=0` is **not**
   a charged K2 point. At `(b,e)=(0,p)` its quadratic initial form still
   forces leading `(x,y)=(0,0)`, so the face is empty, but that
   computation is an addendum.

This is only the exceptional delayed-load `K` kernel on `D(D)`. It does
not treat the exceptional `A` face, the divisor `D=0`, the exact-square
load-ratio divisor `5 D - 2 s = 0`, other source/load slopes, order two,
`(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — UFD split of `Q0` and `N1`; identification `(1.5)`; licensed units

The charged `k10=0` criterion is that the first seven ordinary rows of
`(3/8) N^2/K` vanish if and only if `K` divides `N^2`. After base change
to an algebraic closure, writing `K = prod (z-a)^{m_a}` and
`D_K = prod (z-a)^{ceil(m_a/2)}`, this is equivalent to `D_K | N`.
Squarefree `K` therefore forces `K | N`; if also `deg N < deg K`, then
`N=0`.

The discriminant of `Q0=z^4+p z^2+r` is `16 r (p^2-4 r)^2 = 256 r D^2`.
On `D(D) intersect D(r)` this is a unit, so `Q0` is squarefree. Then
`Q0 | N1` and `deg N1 <= 3` force `N1=0`. Expanding

```text
N1 = z ( y z^2 + 2 D x + (p/2) y )
```

gives `y=0` and `2 D x=0`, hence `x=0` on `D(D)`, contradicting
`(x,y)!=(0,0)`. The `r!=0` open is empty. No higher-jet argument is
required.

On `r=0` one has `D=p^2/4`. The hypothesis `D!=0` makes `p` a unit, and
`Q0=z^2(z^2+p)` with roots `0` of multiplicity two and `±sqrt(-p)` of
multiplicity one. Thus `D_{Q0}=z(z^2+p)`, and `D_{Q0} | N1` if and only
if `z^2+p` divides `y z^2 + 2 D x + (p/2) y`. The remainder is
`2 D x - (p/2) y`. Substituting `D=p^2/4` yields `y=p x`. Then

```text
N1 = p x z^3 + (2 (p^2/4) x + (p/2) p x) z
   = p x z^3 + p^2 x z
   = p x z (z^2+p),
```

and `p x != 0` because `p` is a unit and `(x, p x)!=(0,0)`. This is
target `(1.3)`.

In discriminant coordinates `A=z-a`, `Q=A^2+b A+e`, `K0=A^2 Q`,
`N0=m A Q`, with `b=4 a` and `e=d+3 a^2`. The unique double root of
`z^2(z^2+p)` is at `0`, so `a=0`, `A=z`, `b=0`, `e=p`, and
`m=p x`. This is target `(1.5)`. In particular `e=p` and `m=p x` are
units. The routed square intersection is `b=e=0`, equivalently
`a=d=0` and `K0=A^4`. Here `e=p!=0`, so the point lies in the `e`-unit
chart.

The first-order affine-Faber `K` kernel also carries a coeval odd
quartic coefficient `c=x` from the `v_c` direction. That term does not
disturb the leading unloaded condition: `N1^2/Q0` is quadratic in the
kernel radius, while `c` enters `1/K` only at the next order. Leading
UFD is correctly computed on the even special fibre `Q0`.

The parametrization `(a,d,m) |-> (p,c,r,n0,n1,n2,n3,k10)` is immersive
at `(1.5)`: the eight-by-three Jacobian has rank three, and the
three-by-three minor in `(p,n2,n3)` has determinant `-m`. Tangent
absorption of root-preserving jets into series `a(s),d(s),m(s)` is
therefore unique order by order on `D(m)`.

---

## Attack 2 — V3 bridge, repaired K2 colons, and the `e`-unit chart

The frozen V3 identity is polynomial and coefficientwise zero in exact
characteristic zero: for each of the seven rows,
`16 S_l = sum_(j<=l) T_(l,j)(b,e) H_j`. The matrix `T` is the change
from negative `A`-coefficients to negative `w`-coefficients coming from
`q=A/w`, `v=1/w`, and `q^4+b v q^3+e v^2 q^2=1`. Because `w ~ A` at
leading order, `T` is lower unitriangular with ones on the diagonal, hence
invertible over `Q[b,e]`. The seven complete frozen-source K2 rows and
the seven analytic rows therefore generate the same ideal in
`R_m = Q[b,e,h,y,kappa,m][m^{-1}]`, which is every localization used
below. Inverting `e` or `b` is not required for the identification.

The controlling V2 support statements, rederived from the exact-`Q`
standard basis rather than from a review token, are precisely the two
colons in `R_m`. The client saturates the five remaining rows by `m`,
then by `kappa`, and separately saturates `G+(kappa)` by `m` then `e`;
neither colon inverts `b`. The printed exact-`Q` sentinels are
`K_NONZERO_UNIT=1` and `K0_E_NONZERO_UNIT=1`. The `b`-inverted raw
scheme on `D(b m)` is a different chart, used only to route
`b=e=0`.

Hand check of the second colon at the actual point `(1.5)`, which has
`b=0` and `kappa=0`. The generating function
`t^2 (y-h t)^2/(1+e t^2)` has `u_3=-2 y h` and `u_4=h^2-e y^2`. The
recurrence at `b=0` is `u_n + e u_(n-2)=0` for `n>=5`, so
`u_5=-e u_3`. The remaining K2 rows with `kappa=0` include
`6 u_3=m^3` and `6 u_5=0`. Thus `e m^3=0`. On `D(m)` this forces `e=0`,
so saturating by `e` yields the unit ideal. Independently of Groebner
machinery, the repeated-root point lies on an empty `e`-unit chart.

A successor arc of `(1.5)` has `e(s)=p+O(s)`. Because `e(0)=p!=0`, `e`
is a unit in the DVR. No successor can specialize onto the triple-root
support `e=0`. The square intersection `b=e=0` is not in the closure of
this point along any arc through `(1.5)`.

---

## Attack 3 — normalized-blowup lemma; missing early-kernel face

Write `lambda=v(Lambda)`. After absorbing tangent motion into
`(a,d,m)`, the remaining first-normal coordinates are five-dimensional.
The linearization of `(3/8) N^2/K + k K^{5/2}` at `(K0,N0,0)` has
negative part supported in `A^{-1},A^{-2}` from the complementary
`(C0,S0)` directions, nothing from `S1`, and the `k` column equal to
`H=A^5 Q^{5/2}`. The kernel is two-dimensional:

```text
delta K = x A,
delta N = y A + (m x)/2,
delta k = 0,
```

which is target `(3.1)`. Complementary rank is at most three everywhere.
At a generic discriminant point the minor in rows `A^{-1},A^{-2},A^{-3}`
and columns `(S0,C0,k)` is a nonzero multiple of `m^3 c_13`. At `(1.5)`
one has `b=0`, so `(1+e t^2)^{5/2}` has only even powers and `c_13=0`.
That particular minor vanishes, but rank does not drop:
`c_14=binom(5/2,7) e^7` is a unit times `e^7`, so the `kappa` column is
independent on `A^{-4}`. The three complementary pivots remain
`(S0, C0, kappa)`, of which the first two are unit multiples of `m` and
`m^2` on `A^{-1}` and `A^{-2}`.

The next tails after the first-normal, as functions of a DVR parameter,
have three competing grades:

```text
linear complementary :  2 lambda + nu,
quadratic kernel     :  2 lambda + 2 mu,
intrinsic -m^3       :  3 lambda.
```

The last comes from `-(1/16) Lambda^3 N0^3/K0^3` with `N0/K0=m/A`,
hence `-m^3/(16 A^3)` at `Lambda^3`, and is independent of all
transverse coordinates. The half-weight chart `Lambda=rho^2`,
`wt(kernel)=1`, `wt(complementary)=2` is exactly the locus
`mu=lambda/2`, `nu=lambda` on which all three grades coincide at
`rho^6`. The charged K2 scheme is the vanishing of that balanced
initial form.

The producer's lemma assigns weights only to `(kernel, complementary)`
and then asserts that, after dividing by the least weighted power, the
leading coefficients are a point of this K2 chart, with vanishing kernel
coordinates merely a coordinate face, and with `-m^3` preventing an
all-zero escape. That last clause correctly kills the **late** face
`mu>lambda/2` and `nu>lambda`, on which the first new tail is exactly
`-m^3 != 0`. Coordinate faces of the balanced chart (`mu=lambda/2` with
vanishing complementary, or `nu=lambda` with vanishing kernel) are
likewise K2 points on `D(e m)` and are empty by Attack 2.

It does not kill, and does not even name, the **early** face
`mu<lambda/2`, `nu>=2 mu`. On that face the first new tail has grade
`2 lambda + 2 mu < 3 lambda`. After dividing by that leading power, the
intrinsic `-m^3` is of strictly positive remaining valuation and is
absent from the initial form. The resulting equations are the quadratic
map in `(x,y)`, plus complementary linear terms if `nu=2 mu`, with
`kappa=0`. These are not the charged K2 equations: those require
`6 u_3 - m^3 = 0` on `kappa=0`, hence `u_3 != 0` on `D(m)`, while the
early face requires `u_3=0`. One cannot manufacture `-m^3=0` by a
coordinate face while remaining on `D(m)`, because `m(s)=p x + O(s)` is
a DVR unit. The early face is a genuine extra Newton face of the joint
map in `(Lambda, kernel, complementary)`, not a coordinate face of the
half-weight chart.

Linear complementary pivots do not apply: by construction the kernel is
the kernel of the first-normal Jacobian. Root-splitting with one root
held at the moving centre is the kernel direction `C1=x A` and, at
fractional order `mu<lambda/2`, lands on this face. Opposite splitting
`± s^alpha`, after absorbing the even `e`-motion into `(a,d)`, leaves a
complementary `C0` of valuation `2 alpha`; if `2 alpha < 2 mu` it is
already killed by the `A^{-2}` pivot, and if `2 alpha >= 2 mu` with
`mu<lambda/2` it is the tied early face, still without `-m^3`.

No countermodel. Restrict the early quadratic to `(b,e)=(0,p)`, which is
the leading value of every successor of `(1.5)` because `b=4a` vanishes
at the point and tangent `a`-jets are absorbed. Then

```text
u_2 = y^2,     u_3 = -2 y h,     u_4 = h^2 - e y^2,
u_5 = - e u_3,  h = m x / 2.
```

- If complementary is strictly later (`nu>2 mu`), the uncancelled
  `A^{-2}` row forces `u_2=0`, hence `y=0`, then `u_4=h^2=0`, hence
  `x=0`.
- If complementary is tied (`nu=2 mu`), it may cancel `u_1,u_2`, and
  the remaining conditions `u_3=u_4=0` with `e` a unit still force
  `y=0` and `h=0`, hence `x=0`.

Either subface has vanishing leading kernel coefficients, contradicting
the choice of least order. The early face is empty at this point. The
producer never writes `u_3=u_4=0 => (x,y)=(0,0)` on `b=0`, `e` a unit,
without `-m^3`. Until that identity is recorded as part of the
normalized-blowup lemma, the lemma does not exhaust relative valuations,
and the composition does not prove emptiness of every formal or Puiseux
successor.

The claim that a fractional intermediate sigma order cannot bypass
`(2.1)` is therefore false as written: `(2.1)` is a statement about the
balanced K2 ideal, and the early face is precisely a fractional (or
integer) order that never meets that ideal.

---

## Attack 4 — source scaling, load timing, and `kappa=0`

The one-parameter source is affine-linear in the three lower loads, with
effective substitutions `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^{10} k2`.
On the delayed graph these are all `Lambda^{14}` times a regular capital
coordinate. The K2 extraction is the coefficient of `rho^6` after
`Lambda=rho^2`, i.e. source grade `Lambda^3`. Delayed `k10` is
`rho^{24} K10`, and likewise `k6`, `k2` first appear at `rho^{28}`.
Affine-linearity forbids downward mixing. Independently of the support
theorem, delayed loads do not contribute at the K2 initial grade, so
the K2 load coordinate is `kappa=0`.

Ramification cannot restore a delayed load at this grade: the graph
`k10=Lambda^{12} K10` is homogeneous in the source parameter, and `K10`
is regular on the ray. A load Newton face with `v(k10)<12 lambda` is a
different source slope, excluded by the target's firewall.

A complementary `kappa` tying the **balanced** K2 face would mean
`v(k10)=lambda`, i.e. `k10` comparable to `Lambda`, which delayed loads
are not. The first colon `(I_K2:kappa^infinity)=(1)` in `R_m` would empty
that hypothetical tie, but it is not a delayed-load phenomenon and is
not a substitute for Attack 3. In particular the first colon does not
speak to the early face, on which `kappa=0` already and `-m^3` is not
present.

---

## Attack 5 — sigma-through-15 is corroboration; K2 composition does not yet supply root-splitting exhaustiveness

The charged sigma-15 package works on the exact moving-double-root chart

```text
Q = (z-a)^2 ((z-a)^2 + 4 a (z-a) + e),
N = s^5 lam z (z^2+p) + sum_{j=6}^{10} s^j (degree <= 3),
```

with `a(s)` and `e(s)` through order five, and with loads set to zero
because delayed loads first reach the absolute face after this
predecessor. Its exact-`Q` standard basis after saturation by `p lam` is
`(1)`. This is a finite root-**preserving** jet computation: the double
root is retained, and the leading normal is exactly `(1.3)` at order
five. It does not see a root-splitting transverse, a fractional order
outside the compiled window, or the early-kernel face of Attack 3.

The producer correctly declines to treat this as exhaustiveness. The
abstract K2 composition would supply the missing root-splitting coverage
if and only if every relative valuation, including `C1`-splitting at
order `mu<lambda/2`, reduced to a charged K2 point on `D(e m)`. Attack 3
shows that reduction is not proved. The addendum `u_3=u_4=0 => x=y=0`
at `(b,e)=(0,p)` does close that splitting face, but it is not in the
target. Until it is, the composition does not supply the claimed
exhaustiveness.

---

## Omissions that do not break the surviving theorem

- The nonzero-`k10` Padé lemma is charged and unused. On this ray the
  first-normal is the `k10=0` slice. A load-tied first-normal at
  `2 v(N_octic)=14 lambda` would be a different face; Padé would send
  it to the square locus `D=0`, off the present open. The target does
  not claim that face, and the present repair does not need it.
- Finite-field V3 and support lanes reproduce the exact-`Q` sentinels
  and are controls only.
- Later `[6,2]` rows, Taylor boundaries, and the exact-square/Pell
  receiver are correctly firewalled. The load-ratio divisor
  `5 D - 2 s = 0` with vanishing leading normal is that receiver, not
  the kernel `(1.1)`.

---

## Firewall

This review is only the exceptional delayed-load affine-Faber `K` kernel
on `D(D)`. It does not exclude the exceptional `A` face, the divisor
`D=0`, other source or load slopes, the remaining exact-square/Pell
receiver, the total order-two fan, order two, `(8,12)`, maximum twelve,
or JC2.

REPAIR
