# Hostile review V2 — repaired delayed-load affine-Faber `K` composition

| Field | Value |
|---|---|
| Producer | `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md` |
| Producer SHA-256 | `6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989` |
| Controlling repair | `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-v2-20260826.md` |
| Repair SHA-256 | `7c731df0fdf699119973c2d9c80a7096adab40bec7fb95d70f10cf9b1009ff64` |
| Superseded addendum (not controlling) | SHA `8b17b8c116d1e3a9c5858713b91837d10216f540fe30d2f72a2c6482d01a874a`; opened only to confirm it is the document V2 corrects; its homogenization sentence is not used |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing valuation face | none: the early kernel/source-zero face omitted by the producer is empty on this repeated point after the V2 strict transform |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation of the composite (immutable producer + controlling V2 addendum). Different model family from the producer. No producer status line, no charged `CONFIRMED`/`REPAIR`/`PASS` string, and no audit token is evidence |
| Method | source reading, SHA-256 of every named pin actually consumed, and hand identities in characteristic zero; no Singular, Sage, msolve, Lean, CAS, or substantive exact Python. Frozen exact-`Q` row identities are algebraic evidence; finite-field lanes are software controls only |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the producer is
`6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989`
and of the controlling V2 addendum is
`7c731df0fdf699119973c2d9c80a7096adab40bec7fb95d70f10cf9b1009ff64`,
both matching the required pins. Independently recomputed SHA-256 of every
artifact pinned in producer §0 and §5, and of every further file actually
consumed below, match those pins. Producer verdict language, both
documents' status lines, charged review tokens, and finite-field lanes
were not used as characteristic-zero algebra. No file other than this
review was written.

---

## Verdict

**CONFIRMED.**

The immutable producer still omits the early kernel/source-zero Newton
face: its weighted-blowup paragraph treats every remaining DVR as a point
of the charged half-weight K2 scheme, whose intrinsic `-m^3` lives at
absolute grade `3 v(Lambda)` and is absent from the initial form whenever
`v(kernel) < v(Lambda)/2`. That omission is a real gap in the producer
alone.

The controlling V2 addendum closes it. Substituting `Lambda = rho^2 L`
into the charged expansion

```text
(3/8) Lambda^2 N^2/K - (1/16) Lambda^3 N^3/K^3
```

gives, at total `rho` degree six, the undivided high row
`L^2 (6 u_3 - L m^3)` (up to the same nonzero rational scalar as the
charged K2 formula). Saturation for the closure of `D(Lambda)` removes
the total-transform factor `L^2` and leaves the strict-transform row
`6 u_3 - L m^3`, not `6 u_3 - L^3 m^3`. On `L=0` the intrinsic cubic is
absent, as required for the omitted face.

On that face, at the repeated point `b=0`, `e=p`, `m=p x_0` with `e m`
a unit, the homogeneous kernel rows are `u_3 = -2 y h` and
`u_4 = h^2 - e y^2`. These force `y=h=0`, hence `x=0` from `h=m x/2`.
The two source-accessible complementary pivots then kill the remaining
weight-two coordinates. Unequal kernel valuations and root-splitting of
type `delta K = x A` land on this same face and are likewise empty.
On `L != 0`, ramification licenses a unit leading source coefficient
(normalizable to `L=1`); delayed loads keep `kappa=0` at this
predecessor; the reviewed `e`-open colon in `R_m` together with the
exact V3 lower-unitriangular bridge empties the chart before any `b`
localization.

The cones `L=0`, `L != 0`, and an earlier complementary linear pivot
exhaust all fractional relative valuations of `(kernel, complementary,
source)`. There is no third face and no delayed-load timing mismatch.
The squarefree UFD branch, the repeated-point coordinate map, and the
narrow `K`-face firewall are unchanged. The moving sigma-through-15
unit is corroboration of a root-preserving integral chart only.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md` | `6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989` | immutable producer (matches required pin) |
| `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-v2-20260826.md` | `7c731df0fdf699119973c2d9c80a7096adab40bec7fb95d70f10cf9b1009ff64` | controlling nonmutating repair (matches required pin) |
| `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-20260826.md` | `8b17b8c116d1e3a9c5858713b91837d10216f540fe30d2f72a2c6482d01a874a` | superseded addendum; not used as controlling mathematics |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | `k10=0` criterion `K\|N^2` and UFD split |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md` | `08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md` | `2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5` | named in producer §0; nonzero-`k10` lemma not consumed |
| `xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md` | `73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-discriminant-rank-halfweight-kuranishi-20260826.md` | `ddbc758039621f70eae586b5482be3bfdd92754e990cdb015fa4c6d2e0eac0b1` | charged expansion (4.3)--(4.5), complementary linearization, kernel (4.2) |
| `xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md` | `20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341` | analytic five-row K2 ideal, recurrences, intrinsic `-m^3` |
| `xmodel/max12-812-order2-discriminant-halfweight-k2-support-review-terra-20260826.md` | `f93ecb4320fadff500638fc6fa7bdfca904ed5556b7a13add4cddb9b40a76b70` | named parent; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md` | `f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b` | both unit colons live in `R_m`, not in a hidden `b`-inverted ring |
| `cases/max12_812_order2_disc_halfweight_support_v2_20260826/RESULT.md` | `31faaba6a21250c218a37673d4d3c8b07883432223d70716bf7b50384ba607c4` | exact-`Q` colon statements and standard basis on `D(b m)` |
| `cases/max12_812_order2_disc_halfweight_support_v2_20260826/FREEZE.sha256` | `3576b8ca6692ed1d1d47319436ae6b85e981cabf8b90e4155c794b75797c9722` | support freeze |
| `cases/max12_812_order2_disc_halfweight_support_v2_20260826/RESULTS.sha256` | `570d149b58a2b5583cb86820e281b30911f21bd124959409a01c304d07cf7279` | support result manifest |
| `cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/FREEZE.sha256` | `6e00100d10f5d05b5351d2ca7fd8535a9b0df49671860d51862b73d64e6319c9` | V3 freeze manifest |
| `cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULT.md` | `d0327db2e2214bc897be85d4373bf35e063c2a540254b2b33986f88755eca0e8` | exact-`Q` lower-unitriangular statement |
| `cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULTS.sha256` | `6eb104a3288bf663aced9b8aa6f0bdac3a91c9cb6bd26d44e4b4989a5efe7c36` | V3 result manifest |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | affine-linearity of the one-parameter source in the three lower loads |
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

Charged algebraic input actually consumed: the `k10=0` identity
`q_1=...=q_7=0` iff `K` divides `N^2`, with `D_K | N` after algebraic
closure; squarefree `K` forcing `N=0` when `deg N < deg K`; the
discriminant family covering `[2,1,1]` and `[3,1]`; the analytic
expansion and rows

```text
(3/8) Lambda^2 N^2/K - (1/16) Lambda^3 N^3/K^3 + O(Lambda^4),

6 u_3 - m^3 + 16 kappa c_13 = 0,
6 u_n + 16 kappa c_(10+n) = 0,     n=4,5,6,7,

sum u_n t^n = t^2 (y - h t)^2 / (1 + b t + e t^2),
h = m x / 2,
u_n + b u_(n-1) + e u_(n-2) = 0     (n >= 5);
```

the complementary linearization on `A^{-1},A^{-2}`; the two colons in
`R_m = Q[b,e,h,y,kappa,m][m^{-1}]`; routing of `b=e=0` to the square;
the exact identity `16 S_l = sum_(j<=l) T_(l,j)(b,e) H_j` with `T`
lower unitriangular of unit diagonal, from `q^4 + b v q^3 + e v^2 q^2 = 1`;
and the delayed substitutions `k10=Lambda^{12} K10`, `k6=Lambda^8 K6`,
`k2=Lambda^4 K2` with effective one-parameter loads all at `Lambda^{14}`.

---

## Strongest exact theorem that survives

Work over a field of characteristic zero, on the integral delayed-load
ray `k10=Lambda^{12} K10`, `k6=Lambda^8 K6`, `k2=Lambda^4 K2`, and on
`D(D)` with `D=(p^2-4 r)/4`. Let the exceptional affine-Faber `K`
kernel be the projective pair `(x,y) != (0,0)` with leading square-normal

```text
Q0 = z^4 + p z^2 + r,
N1 = y z^3 + (2 D x + (p/2) y) z.
```

Let `lambda = v(Lambda) > 0` on a ramified DVR. After absorbing
root-preserving tangent motion into the smooth discriminant parameters
`(a,d,m)`, let `mu` be the valuation of the two-dimensional half-weight
kernel in moving `A`-coordinates, `nu` the valuation of the three
complementary directions including the first load, and `L` the leading
coefficient of `Lambda` in the weighted chart `Lambda = rho^2 L` with
`wt(kernel)=1`, `wt(complementary)=wt(L)=2`.

1. On `D(r)` the quartic `Q0` is squarefree and `Q0 | N1^2` forces
   `N1=0`, hence `x=y=0`, contradicting projectivity. This open is empty
   at the unloaded first-normal gate.
2. On `r=0` one has `D=p^2/4` with `p` a unit, `Q0=z^2(z^2+p)`, and
   `Q0 | N1^2` iff `y=p x` with `p x != 0`. In discriminant coordinates
   this is exactly `(a,b,e,m)=(0,0,p,p x)`, with `e` and `m` units. It
   is not the routed square intersection `b=e=0`.
3. Delayed loads contribute first at source grade `Lambda^{14}`. The
   intrinsic K2 grade is `Lambda^3`, and the early-kernel grade is
   strictly less than `Lambda^3`. Thus `kappa=0` at every grade used
   below.
4. If `nu < min(2 mu, lambda)`, a complementary linear pivot of the
   first-normal Jacobian is nonzero and the arc already fails an earlier
   initial row. The two source-accessible pivots are unit multiples of
   `m` and `m^2` on `A^{-1}` and `A^{-2}`, independent of `b` and of
   `c_{13}`.
5. If `2 mu < min(nu, lambda)`, equivalently `L=0` after the weighted
   scale, the strict-transform high rows are `u_3=u_4=...=u_7=0`. At
   the point (2), `u_3=-2 y h` and `u_4=h^2-e y^2` with `e` a unit
   force `y=h=0`, hence `x=0`. Complementary pivots then kill the
   remaining weight-two coordinates. This includes unequal kernel
   valuations and root-splitting of type `delta K = x A`.
6. If `lambda <= min(2 mu, nu)`, equivalently `L` a unit after
   ramification, the strict-transform rows are the charged complete-source
   K2 map, including `-L m^3`. The V3 identity identifies this with the
   analytic ideal in `R_m` before any `b` localization. The colon
   `((I_{K2}+(kappa)):e^infinity)=(1)` in `R_m` empties `D(e)`, and the
   successor remains in `D(e)` because `e(0)=p` is a DVR unit. Coordinate
   faces with vanishing kernel or complementary leading coefficients are
   included; the all-zero face is not a projective point, and on `L` a
   unit is killed by `-L m^3 != 0`.

This is only the exceptional delayed-load `K` kernel on `D(D)`. It does
not treat the exceptional `A` face, the divisor `D=0`, the exact-square
load-ratio divisor, other source/load slopes, order two, `(8,12)`,
maximum twelve, or JC2.

---

## Attack 1 — homogenization and the strict-transform factor `L^2 (6 u_3 - L m^3)`

The charged tail expansion, after the first-normal polynomial has been
removed, is

```text
(3/8) Lambda^2 N^2/K - (1/16) Lambda^3 N^3/K^3 + O(Lambda^4),
```

together with the first-load term `k_{10} K^{5/2}`. Write
`Lambda = rho^2 L` and

```text
K = K0 + rho K1 + rho^2 K2,     N = N0 + rho N1 + rho^2 N2,
K1 = x A,                       N1 = y A + m x / 2,
```

with `(K1,N1)` the two-dimensional kernel and `(K2,N2)` of weight two.
The `rho^2` coefficient of `N^2/K` along the kernel is
`(N1 - (m/A) K1)^2 / K0 = (y A - h)^2 / (A^2 Q)`, independent of `L`.
Times `Lambda^2 = rho^4 L^2` this is `rho^6 L^2` times that quadratic.
The intrinsic cubic is `Lambda^3 (N0/K0)^3 = rho^6 L^3 m^3 / A^3`.

The generating function identity

```text
(y A - h)^2 / (A^2 Q) = t^2 (y - h t)^2 / (1 + b t + e t^2) = sum u_n t^n
```

(with `t=1/A`) converts the quadratic into the sequence `u_n`.
Multiplying the `A^{-3}` row by sixteen, using `16*(3/8)=6` and
`16*(-1/16)=-1`, yields the undivided high row

```text
L^2 * 6 u_3 - L^3 m^3 = L^2 (6 u_3 - L m^3),
```

up to the charged nonzero scalar convention. The remaining high rows
`n=4,5,6,7` are `L^2 * 6 u_n` (no cubic). Complementary linear terms
likewise carry `Lambda^2`, hence `L^2`. Delayed `kappa` is zero at this
grade (Attack 3), so it contributes no competing `L`-power.

The campaign studies the closure of `D(Lambda)`. Every row of the
undivided ideal is divisible by `L^2` and not, as a polynomial in the
kernel coordinates, by `L^3` (the coefficient `6 u_3` is not identically
zero). Saturating by `L` therefore removes exactly `L^2` and leaves

```text
6 u_3 - L m^3,     6 u_4,     ...,     6 u_7
```

as the strict-transform high rows. The superseded addendum's
`-L^3 m^3` after strict transform is the wrong homogenization: it
would keep an extra `L^2` on the cubic. V2's (1.1)--(1.2) are the
correct identities. On `L=1` they recover the charged row `6 u_3-m^3`.
On `L=0` they recover `u_3=0` followed by `u_4=0`, i.e. the early face
without `-m^3`.

If the kernel already vanishes, the undivided cubic is `L^3 (-m^3)` and
dividing only by `L^2` leaves `-L m^3`, which is `0=0` on `L=0`. That
does not create a point: kernel and complementary then vanish as well,
which is the origin of the weighted projective space, excluded by
projectivity. On `L` a unit the same situation is the late face killed
by `-L m^3 != 0` on `D(m)`.

---

## Attack 2 — `L=0` at the repeated point; unequal valuations; root splitting; complementary pivots

The generating function at `b=0` is

```text
(y^2 t^2 - 2 y h t^3 + h^2 t^4) / (1 + e t^2).
```

The geometric series `1/(1+e t^2) = sum_{k>=0} (-e)^k t^{2k}` gives

```text
u_2 = y^2,
u_3 = -2 y h,
u_4 = h^2 - e y^2,
u_5 = 2 e y h,
u_6 = e^2 y^2 - e h^2,
u_7 = -2 e^2 y h,
```

and the recurrence `u_n + e u_{n-2}=0` for `n>=5`. V2's displayed
`u_3=-2 y h`, `u_4=h^2-e y^2` match. On `L=0` the strict-transform
high rows are `u_3=u_4=0`. With `e` a unit,

```text
y h = 0,     h^2 = e y^2.
```

If `y=0` then `h^2=0`; if `h=0` then `e y^2=0`, hence `y=0`. Thus
`y=h=0`. Since `m` is a unit and `h=m x/2`, also `x=0`. Every leading
kernel coordinate vanishes.

Unequal kernel valuations, tested explicitly as leading forms of a DVR:

- If `v(y) < v(h)`, the leading pair is `(Y, H=0)` with `Y != 0`. Then
  `u_4` leads by `-e Y^2 != 0`.
- If `v(h) < v(y)`, the leading pair is `(Y=0, H)` with `H != 0`. Then
  `u_4` leads by `H^2 != 0`.
- If `v(y)=v(h)`, both lead and `u_3=u_4=0` force both residues to
  vanish, as above.

In all three subcases the leading kernel is zero, contradicting the
choice of least kernel order on this face.

Complementary subcases of the same face:

- If complementary is strictly later (`nu > 2 mu`), the `A^{-2}` row
  has no complementary cancellation. Its initial form is `6 u_2=6 y^2`,
  so `Y=0`, and then `u_4=H^2=0`. Stronger than `u_3=u_4=0` alone.
- If complementary is tied (`nu=2 mu`), the `A^{-1}` and `A^{-2}` rows
  may cancel `u_1` (already zero) and `u_2`. The remaining conditions
  are still `u_3=u_4=0`, which kill `(x,y)` as above. Substituting
  `y=0` back into `A^{-2}` then forces the complementary `C_0`
  residue to vanish as well.

The two source-accessible complementary pivots do not use `c_{13}` and
do not invert `b`. The first-normal linearization

```text
(3/4) m (delta N)/A - (3/8) m^2 (delta K)/A^2
```

has negative part

```text
A^{-1}:  (3/8) m (2 S_0 - m C_1),
A^{-2}:  -(3/8) m^2 C_0.
```

After times sixteen these are `6 m (2 S_0 - m C_1)` and `-6 m^2 C_0`.
Both coefficients are units on `D(m)`. The combination `2 S_0 - m C_1`
is precisely the complementary coordinate vanishing on the kernel
`(C_0, 2 S_0 - m C_1, kappa) = (0,0,0)`. At `b=0` one has `c_{13}=0`
because `(1+e t^2)^{5/2}` is even, so the particular `A^{-3}` minor
with the `kappa` column vanishes; that is irrelevant here: delayed
`kappa=0` already, and the two source-accessible pivots live on
`A^{-1},A^{-2}`. After `(x,y)=0`, those pivots remove the remaining
weight-two complementary coordinates. Delayed `kappa` is already zero.
The weighted projective point on `L=0` is therefore the origin, which
is not a point.

Root splitting. A motion that splits the double root while holding one
root at the moving centre is the kernel direction `delta K = x A`,
`delta N = y A + m x/2`. At fractional (or integral) order
`mu < lambda/2` this is exactly the `L=0` face just emptied. Opposite
splitting `± s^alpha` of the two simple roots, after the even `e`-motion
is absorbed into `(a,d)`, leaves a complementary `C_0` of valuation
`2 alpha`. If `2 alpha < 2 mu` it is the earlier complementary pivot
(Attack 4). If `2 alpha >= 2 mu` with `2 mu < lambda` it is the tied
or later complementary subcase of `L=0`, still without `-m^3`, and
still empty. Positive-valuation motion of `(b,e,m)` does not change
the initial form: residues remain `(0,p,p x)` with `e m` a unit, and
every term containing the positive-valuation `b` is strictly later.

No countermodel on this face.

---

## Attack 3 — `L != 0`: ramification, delayed `kappa=0`, `e`-open unit, V3 before any `b` localization

If the weighted minimum is attained by the source coordinate, the
leading coefficient `L` is a residue-field unit. After a finite
ramification one may take `L=1`; this is a DVR leading-coefficient
normalization, not a hidden Kummer chart of the source ray. Even
without setting `L=1`, the strict-transform cubic is `-L m^3` with `L`
a unit, so the same colon argument applies with `m^3` replaced by
`L m^3`.

Delayed load timing is read from the one-parameter source, which is
affine-linear in the three lower loads:

```text
Lambda^2 k10,     Lambda^6 k6,     Lambda^{10} k2.
```

On the delayed graph these are all `Lambda^{14}` times a regular
capital coordinate. The K2 extraction is the coefficient of `rho^6`
after `Lambda=rho^2 L`, i.e. source grade `Lambda^3`. Delayed `k10`
is `rho^{24} L^{12} K10`; `k6` and `k2` first appear at still higher
`rho` order. Affine-linearity forbids downward mixing. Independently,
the frozen V3 source polynomials in the balanced chart are independent
of `k6` and `k2` after extracting `rho^6`. Thus `kappa=0` at this
predecessor, on both `L=0` and `L != 0`. A load Newton face with
`v(k10) < 12 lambda` is a different source slope, excluded by the
firewall.

The exact V3 identity is polynomial and coefficientwise zero in
characteristic zero: for each of the seven rows,
`16 S_l = sum_(j<=l) T_(l,j)(b,e) H_j`. The matrix `T` is the change
from negative `A`-coefficients to negative `w`-coefficients coming from
`q=A/w`, `v=1/w`, and `q^4+b v q^3+e v^2 q^2=1`. It is lower
unitriangular with ones on the diagonal, hence invertible over
`Q[b,e]`. Inverting `e` or `b` is not required. The seven
complete frozen-source K2 rows and the seven analytic rows generate the
same ideal in `R_m`, which is every localization used below.

The controlling support statements in `R_m` are

```text
(I_{K2} : kappa^infinity) = (1),
((I_{K2} + (kappa)) : e^infinity) = (1).
```

Neither colon inverts `b`. The `R_{bm}` scheme description is a
different chart, used only to route `b=e=0`. The present point has
`b=0` and `e=p != 0`, so only the second colon is needed.

Hand check of that colon at `(b,kappa)=(0,0)`, independent of Groebner
machinery. The rows with `kappa=0` include `6 u_3 = L m^3` and
`6 u_5=0`. At `b=0` one has `u_5 = -e u_3`, so
`6 u_5 = -e * 6 u_3 = -e L m^3`. Thus `e L m^3=0`. On `D(m)` with `L`
a unit this forces `e=0`, and saturating by `e` yields the unit ideal.
A successor arc of the repeated point has `e(s)=p+O(s)`, so `e` is a
DVR unit and cannot specialize onto `e=0`. The square intersection
`b=e=0` is not in the closure of this point along any arc through it.

The first colon would empty a hypothetical tied nonzero load on the
balanced chart; delayed timing does not produce that chart, and the
colon is not a substitute for Attack 2.

---

## Attack 4 — exhaustiveness; no third face; no load-timing mismatch

After tangent absorption, the three competing grades of the first tail
beyond the first-normal are linear in `(lambda, mu, nu)`:

```text
linear complementary :  2 lambda + nu,
quadratic kernel     :  2 lambda + 2 mu,
intrinsic -m^3       :  3 lambda.
```

(The last is independent of all transverse coordinates.) Delayed load
terms sit at `>= 12 lambda` and do not compete. The Newton fan in the
positive octant therefore has exactly three cones and their walls:

1. `nu < min(2 mu, lambda)`: complementary leads. Unit linear pivot;
   earlier initial-row failure. This cone is already in the producer
   and is not retracted by V2.
2. `2 mu < min(nu, lambda)`: kernel leads before source. After the
   weighted scale this is `L=0`. Emptied by Attack 2.
3. `lambda <= min(2 mu, nu)`: source/intrinsic present. After the
   weighted scale this is `L` a unit. Emptied by Attack 3, including
   the late coordinate face on which kernel and complementary lead
   later than `Lambda` and the first new tail is exactly `-L m^3 != 0`.

Ties are coordinate faces of these cones (`nu=2 mu < lambda` is tied
`L=0`; `2 mu = lambda <= nu` is `L != 0` with vanishing complementary;
all three equal is the balanced K2 point). There is no fourth cone.
In particular a kernel/root-splitting correction at any fractional
ratio `mu/lambda < 1/2` is cone 2, not a missing ordinary chart, and
a later-than-half-weight correction is a coordinate face of cone 3.

Load timing does not manufacture a third face. On cone 2 the first
tail has grade `2 lambda + 2 mu < 3 lambda`, while delayed `k10` has
valuation `>= 12 lambda`. On cone 3 the K2 grade is `3 lambda`, still
strictly before `Lambda^{14}`. Treating `kappa` as a weight-two
complementary coordinate would require `v(k10)` comparable to `nu` or
`lambda`; delayed loads are not. Affine-linearity of the source in
the three lower loads forbids a product of delayed loads from dropping
into this grade.

The producer sentence that vanishing kernel coordinates are “a
coordinate face of the same K2 chart” is correct for cone 3 and false
as a description of cone 2; V2 supplies cone 2 rather than relabelling
it as a K2 point. The producer sentence that `-m^3` prevents an
all-zero escape is correct on cone 3 and unused on cone 2, where
emptiness is projectivity after the quadratic kernel rows.

---

## Attack 5 — squarefree UFD, repeated-point map, and sigma-through-15 remain as in the producer

The charged `k10=0` criterion is that the first seven ordinary rows of
`(3/8) N^2/K` vanish if and only if `K` divides `N^2`. After base
change to an algebraic closure this is `D_K | N`. Squarefree `K`
therefore forces `K | N`; if also `deg N < deg K`, then `N=0`.

The discriminant of `Q0=z^4+p z^2+r` is `16 r (p^2-4 r)^2 = 256 r D^2`.
On `D(D) intersect D(r)` this is a unit, so `Q0` is squarefree. Then
`Q0 | N1` and `deg N1 <= 3` force `N1=0`. Expanding
`N1 = z ( y z^2 + 2 D x + (p/2) y )` gives `y=0` and `2 D x=0`, hence
`x=0` on `D(D)`, contradicting `(x,y)!=(0,0)`. The `r != 0` open is
empty. V2 does not touch this branch.

On `r=0` one has `D=p^2/4`. The hypothesis `D != 0` makes `p` a unit,
and `Q0=z^2(z^2+p)` with `D_{Q0}=z(z^2+p)`. Then `D_{Q0} | N1` iff
`z^2+p` divides `y z^2 + 2 D x + (p/2) y`. The remainder is
`2 D x - (p/2) y`. Substituting `D=p^2/4` yields `y=p x`. Then
`N1 = p x z (z^2+p)` with `p x != 0`. In discriminant coordinates
`A=z-a`, `Q=A^2+b A+e`, `K0=A^2 Q`, `N0=m A Q`, with `b=4 a` and
`e=d+3 a^2`, the unique double root of `z^2(z^2+p)` is at `0`, so
`a=0`, `b=0`, `e=p`, `m=p x`. This is producer (1.5). In particular
`e` and `m` are units, and the point is not `b=e=0`. V2 uses this
same point and does not alter the map.

The map `(a,d,m) |-> (p,n2,n3)` has Jacobian determinant `-m`. Tangent
absorption of root-preserving jets into series `a(s),d(s),m(s)` is
unique order by order on `D(m)`.

The charged sigma-15 package works on the exact moving-double-root
chart with `a(s),e(s)` through order five, leading normal of type
(1.3) at order five, later normals through order ten, and loads set to
zero. Its exact-`Q` standard basis after saturation by `p lam` is
`(1)`. That is a finite root-preserving jet computation. It does not
see a root-splitting transverse, a half-integral correction at the
exact half-weight tie, or the early-kernel face of Attack 2. The
producer correctly declines to treat it as exhaustiveness. Attacks
1--4 supply exactly those missing cases from the weighted blowup, not
from the finite recursion. V2 does not promote the computation.

The coeval odd quartic coefficient `c=x` from the affine-Faber `K`
`v_c` direction does not disturb the leading unloaded UFD: `N1^2/Q0`
is quadratic in the kernel radius, while `c` enters `1/K` only at the
next order. Leading UFD is correctly computed on the even special
fibre `Q0`.

---

## Omissions that do not break the composite theorem

- The V2 addendum is short. It does not rewrite the three-cone
  fan or spell out unequal valuations. The identities it does write
  (`L^2(6 u_3-L m^3)`, `u_3=-2 y h`, `u_4=h^2-e y^2`, complementary
  unit pivots) are the ones that close the omitted face; the fan and
  the unequal-valuation cases are read from the charged grades and
  from those identities, not from a status line.
- The nonzero-`k10` Padé lemma is charged by the producer and unused.
  On this ray the first-normal is the `k10=0` slice. A load-tied
  first-normal at `2 v(N_{octic})=14 lambda` would be a different
  face; Padé would send it to the square locus `D=0`, off the present
  open.
- Finite-field V3 and support lanes reproduce the exact-`Q` sentinels
  and are controls only.
- Later `[6,2]` rows, Taylor boundaries, and the exact-square/Pell
  receiver are correctly firewalled.
- The superseded addendum's set-theoretic `L=0` emptiness calculation
  happens to agree with V2 (both give `u_3=u_4=0` on `L=0`), but that
  agreement was not used: the controlling derivation is V2's
  homogenization together with the charged generating function.

---

## Firewall

This review is only the exceptional delayed-load affine-Faber `K`
kernel on `D(D)`, for the composite of the immutable producer with the
controlling V2 source-coordinate addendum. It does not exclude the
exceptional `A` face, the divisor `D=0`, other source or load slopes,
the remaining exact-square/Pell receiver, the total order-two fan,
order two, `(8,12)`, maximum twelve, or JC2.

CONFIRMED
