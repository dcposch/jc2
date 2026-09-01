# TB-G2-FINISH: the mixed cover decides the (8,6) row at the infinity germ

Lane: `TB-G2-FINISH`. Date: 2026-09-01. Agent: Opus 5.
Desk-scale exact reasoning; no CAS.

## 0. Custody, method, scope

Charged frozen copies were hashed with `shasum -a 256` before they were read; all
three match the charge exactly:

```text
7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed  row-86-prebuild-opus5-20260901.md
abba04527ce7d0847bee3df9319e4e92d974218996e42745fee2c83590ed8e1a  shape-3-finish-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Below **PRE** = the ROW-86-PREBUILD report, **S3FR** = the SHAPE-3-FINISH hostile
review, **Coord** = the coordinator integration. **No other campaign document was
opened this lane**: every appeal to SK-2 / SK-4 / SK-5, to `(1.1)`/`(3.1)`, to
Theorem A, to (M-INF-T), to Shirane §1.1 or to Miranda is an appeal to the text as
quoted inside PRE or S3FR, and is cited that way. No canonical ledger or charged
file was edited; `jc2-lean` was not inspected; no external source was fetched.

**Method.** All algebra below is hand expansion in a polynomial ring with four to
six letters, done twice. As *confirmation only*, one plain-integer script
(no CAS: no Groebner basis, no resultant, no saturation, no symbolic algebra
library) re-evaluated four identities at 4000 random integer points each — the
derivative identity `t = dD/da_0`, the Hessian identity (3.2), the cubic-family
discriminant expansion (3.1), and the classical `disc(H_f) = -3 disc(f)` used only
as a remark. Zero failures on all four. Every one of them is also expanded by hand
in the text.

**Scope of the verdicts.** Everything here is at the level of the `S_4`
*representation*: a kill removes a type from the `PI1-S4` residual and asserts
nothing about whether a polynomial curve with that `delta`-sequence exists. A
survival asserts only that the tools of this lane do not kill; no cover, and no
curve, is asserted to exist anywhere in this report.

## 1. The TB state at g = 2, re-derived

### 1.1 The row and the four types

`(d,n) = (8,6)`, `a = d-n = 2`, `g = gcd(d,n) = 2`, `p_a = 21`, `beta_1 = 32 - c`,
`2 delta_inf = beta_1 - 1`, `delta_aff = 21 - delta_inf`, germ `A_{beta_1-1}` at
`P_inf = [1:0:0]`, and `(Dbar . L_infty)_{P_inf} = d = 8` with `L_infty` the tangent
(PRE §1, re-derived there from the semigroup gaps; I re-list only what I use):

| type | `Delta` | `beta_1` | `delta_inf` | `delta_aff` | germ | `E = e(iota)` | TUBE-2 |
|---|---|---:|---:|---:|---|---:|:--|
| A | `(8,6,11)` | 21 | 10 | 11 | `A_20` | `-7` | KILLED |
| **B** | `(8,6,9)` | **23** | **11** | **10** | `A_22` | `-9` | passes |
| — | `(8,6,7)` | 25 | 12 | 9 | `A_24` | `-11` | KILLED |
| — | `(8,6,3)` | 29 | 14 | 7 | `A_28` | `-15` | passes |

`(8,6,3)`: `<8,6,3> = <3,8>` has gaps `1,2,4,5,7,10,13`, so `delta_aff = 7`,
Frobenius `13 = 2*7-1`, symmetric; `delta_inf = 14`, `beta_1 = 29`. Independent of
PRE's table, and agreeing with it.

### 1.2 The mixed cover and the two TB integers

Promoted by S3FR §§5, 10 (ESTABLISHED, PROMOTE): on the non-constant stratum
`Pi` is a `3`-cycle (SK-5), the resolvent `rho = psi . phi` is a surjection
`pi_1(P^2 - (Dbar + L_infty)) ->> S_3`, and normalising in the degree-3
subextension gives a **normal triple cover** `pi : Z -> P^2` with

```text
S_pi = Dbar (simple branch, disc order 1) ,  T_pi = L_infty (total branch, disc order 2) ,
Delta-bar = Dbar + 2 L_infty ,  deg Delta-bar = 4g+2 = 10 = 2k ,  k = -deg det T = 2g+1 = 5 .
```

THEOREM TB (S3FR §§3–4, ESTABLISHED): `k_0 + m = 0 (mod 3)`, where `k_0 = k = 5`
(restriction of `det T` to a line does not jump) and `m = ord_{P_inf}(Phi|_{L_infty})`;
`m = 0` iff the fibre over `P_inf` is curvilinear iff `Z` is Gorenstein there.
Hence `3 | (5+m)`, i.e. `m = 1 (mod 3)`.

### 1.3 The local readings, and the charge's `m in {1,4}`

In the chart `(y,sigma) = (Y/X, Z/X)` at `P_inf` the place has orders
`(ord v, ord u) = (g, 4g) = (2,8)`; write the germ of `Dbar` as `f`, and in the
adapted frame of TB step (D)

```text
Phi = rho(y) X^3 + sigma * eta' ,   eta' = sum_i alpha_i X^{3-i} Y^i ,
m = ord_y rho ,   gamma := ord_y alpha_3(y,0) ,   disc(Phi) = U * sigma^2 * f  (U a unit).
```

The three readings of S3FR §4(G) are: **(a)** `2m + 2 gamma = 4g = 8`; **(b)**
`ord_sigma disc(eta')(0,sigma) = g - 2 = 0`, i.e. `D(0,0) != 0`, valid when `m >= 1`;
**(c)** `ord_y (df/dsigma)|_{sigma=0} = 4(g-1) = 4`. I verified (a)–(c) against the
germ directly. With `sigma(s) = sum_{k>=8} c_k s^k` and `y = s^2` (PRE §5), split
`sigma(s)` into even and odd parts: `f = (sigma - A(y))^2 - y B(y)^2` with
`ord_y A = 4` and `ord_y B = delta_inf`. Then `ord_y f(y,0) = min(8, beta_1) = 8`,
`ord_sigma f(0,sigma) = 2 = g`, `ord_y (df/dsigma)|_{sigma=0} = ord_y(-2A) = 4`. All
three hold, for every one of the four types: **the readings are `beta_1`-blind**, as
PRE §6 says.

Reading (a) has a geometric content worth recording, because §3 uses it: it is
exactly the contact number,

```text
(1.1)    2m + 2 gamma  =  ord_y f(y,0)  =  (Dbar . L_infty)_{P_inf}  =  d  =  4g  =  8 ,
```

so `m + gamma = 2g = 4`, and TB's `m = 1 (mod 3)` is equivalent to `gamma = 0 (mod 3)`:

```text
(1.2)    (m, gamma)  in  { (4,0) , (1,3) } .
```

So the charge's parenthetical is right on both counts: `m = 1 (mod 3)` with
`0 <= m <= 2g = 4` leaves `m in {1,4}`, and Proposition TB-2 is what removes `m = 1`.
Re-derived here (S3FR §4(H), ESTABLISHED): assume `m <= 3`, so `m = 1` and, by (a),
`gamma = 3`. Divide `disc(Phi) = U sigma^2 f` by `sigma^2` and use the expansion
(3.1) of §3 below. Reading (c) says the left side has `ord_y = 4`; its first
right-hand term has `ord_y >= 2m + gamma = m + 4 = 5`; no cancellation, so
`ord_y(rho * t_0) = 4` with `t_0 = t(eta')(y,0)`, hence `ord t_0 = 4 - m = gamma = 3 >= 1`
and `t(eta')(0,0) = 0`. Since `gamma >= 1` gives `alpha_3(0,0) = 0`, `t` collapses to
`-4 alpha_2(0,0)^3`, so `alpha_2(0,0) = 0`; every monomial of `disc(eta')` contains
`alpha_2` or `alpha_3`, so `disc(eta')(0,0) = 0`, contradicting reading (b). Hence

```text
(1.3)    m = 4 ,   gamma = 0 ,   alpha_3(0,0) != 0 ,   D(0,0) != 0 .
```

This is where PRE §6 stops, correctly: `m = 4` is forced identically for all four
types, and combining it with `delta_aff` yields nothing, because the budgets never
enter. §§2–3 go one layer deeper, to the layer PRE names ("any deeper layer of TB
must reach order `y^{beta_1/2}`"), and that layer does separate the types.

## 2. The local datum at P_inf

Fix the type. In the chart `(y,sigma)` the place at `P_inf` is

```text
y = s^2 ,   sigma(s) = sum_{k >= 8} c_k s^k ,  c_8 != 0 ,  first ODD k equal to beta_1
```

(PRE §5, Route 2; the normalisation `y = s^2` costs only a reparametrisation). Split
`sigma(s)` into even and odd parts: `A(y)` even, `s^{beta_1} w(s^2)` odd with `w` a
unit. Then the germ equation, the value semigroup of its local ring, and its
analytic type are

```text
(2.1)  f = (sigma - A(y))^2 - y B(y)^2 ,  ord_y A = 4 ,  ord_y B = delta_inf = (beta_1-1)/2 ,
(2.2)  O_{Dbar,P_inf} = C{s^2} + s^{beta_1} C{s^2} ,   Gamma = <2, beta_1> ,
(2.3)  mult(f) = 2 ,  tangent cone sigma^2 ,  (f . L_infty) = 8 ,  type A_{beta_1 - 1} .
```

Two consequences used later. First, `f` is **irreducible** (one place at infinity,
promoted) and reduced. Second, (2.2) is the whole of the type's extra content: the
order along the branch of *any* function on the plane lies in `Gamma`, so no
pullback can have odd order below `beta_1`. That is the only place where `beta_1`,
i.e. `c`, i.e. `delta_aff`, can enter a local computation at `P_inf` — and reading
(a)/(b)/(c) never reach it, since they see `f` only through `f(y,0)`, `f(0,sigma)`
and `(df/dsigma)|_{sigma=0}`, all three of which are `min`-truncated below `beta_1`
by (2.1).

The question of the charge, made precise at the rep level (where there is no actual
octic, only the numerical type):

> **(Q)** For which `beta_1` does there exist a Miranda datum `(rho, eta')` over
> `C{y,sigma}` with `ord_y rho = m = 4`, `alpha_3(0,0) != 0`, and
> `disc(rho X^3 + sigma eta') = unit * sigma^2 * f` with `f` an `A_{beta_1-1}` germ
> satisfying (2.1)–(2.3)?

A NO for a given `beta_1` kills that type at the representation level, since the
mixed cover exists whenever `phi` does (S3FR §5) and `m = 4` is then forced (1.3).
A YES is *not* an existence statement for the cover over a global octic, and is not
used as one.

## 3. THEOREM TB-GERM

## 4. Local admissibility: witnesses at A_22 and A_28

## 5. TB-GERM against TUBE-2: E = 3(2 - kappa)

## 6. The L_infty constraints

## 7. Verdicts

## 8. FALLACY-v2 audit

## 9. Custody and sources
