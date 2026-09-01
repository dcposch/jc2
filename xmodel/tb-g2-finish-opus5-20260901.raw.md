# TB-G2-FINISH: the mixed cover decides the (8,6) row at the infinity germ

Lane: `TB-G2-FINISH`. Date: 2026-09-01. Agent: Opus 5. Desk-scale exact
reasoning; no CAS.

## 0. Custody, method, scope

Charged frozen copies were hashed with `shasum -a 256` before they were read; all
three match the charge exactly:

```text
7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed  row-86-prebuild-opus5-20260901.md
abba04527ce7d0847bee3df9319e4e92d974218996e42745fee2c83590ed8e1a  shape-3-finish-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Below **PRE** = ROW-86-PREBUILD, **S3FR** = the SHAPE-3-FINISH hostile review,
**Coord** = the coordinator integration. **No other campaign document was opened this
lane**: every appeal to SK-2/SK-4/SK-5, to `(1.1)`/`(3.1)`, to Theorem A, to (M-INF-T),
to Shirane §1.1 or to Miranda is an appeal to the text quoted inside PRE or S3FR, and
is cited that way. No ledger or charged file was edited; `jc2-lean` was not inspected;
nothing was fetched.

**Method.** All algebra below is hand expansion in a polynomial ring with four to six
letters, done twice. As *confirmation only*, one plain-integer script (no CAS: no
Groebner basis, resultant, saturation or symbolic library) re-evaluated four identities
at 4000 random integer points each — `t = dD/da_0`, the Hessian
identity (3.2), the discriminant expansion (3.1), and `disc(Hess F) = -3 disc(F)` (used
only in a remark). Zero failures; each is also expanded by hand in the text.

**Scope.** Everything here is at the level of the `S_4` *representation*: a kill
removes a type from the `PI1-S4` residual and says nothing about whether a polynomial
curve with that `delta`-sequence exists; a survival says only that this lane's tools do
not kill.

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

`(8,6,3)`: `<3,8>` has gaps `1,2,4,5,7,10,13`, so `delta_aff = 7`, Frobenius
`13 = 2*7-1`, symmetric, `delta_inf = 14`, `beta_1 = 29` — independently of PRE, and
agreeing with it.

### 1.2 The mixed cover and the two TB integers

Promoted by S3FR §§5, 10 (ESTABLISHED, PROMOTE): on the non-constant stratum `Pi` is a
`3`-cycle (SK-5), the resolvent `psi . phi` surjects
`pi_1(P^2 - (Dbar + L_infty)) ->> S_3`, and normalising in the degree-3 subextension
gives a **normal triple cover** `pi : Z -> P^2` with

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
**(c)** `ord_y (df/dsigma)|_{sigma=0} = 4(g-1) = 4`. I checked them against the germ.
With `y = s^2` and `sigma(s) = sum_{k>=8} c_k s^k` (PRE §5), splitting `sigma(s)` into
even and odd parts gives `f = (sigma - A(y))^2 - y B(y)^2`, `ord_y A = 4`,
`ord_y B = delta_inf`; then `ord_y f(y,0) = min(8,beta_1) = 8`,
`ord_sigma f(0,sigma) = 2 = g`, `ord_y(-2A) = 4`. All three hold for all four types:
**the readings are `beta_1`-blind**, as PRE §6 says.

Reading (a) has a geometric content that §3 uses: it is the contact number,

```text
(1.1)    2m + 2 gamma  =  ord_y f(y,0)  =  (Dbar . L_infty)_{P_inf}  =  d  =  4g  =  8 ,
```

so `m + gamma = 2g = 4`, and TB's `m = 1 (mod 3)` is equivalent to `gamma = 0 (mod 3)`:

```text
(1.2)    (m, gamma)  in  { (4,0) , (1,3) } .
```

So the charge's parenthetical is right on both counts: `m = 1 (mod 3)` with
`0 <= m <= 2g = 4` leaves `m in {1,4}`, and Proposition TB-2 removes `m = 1`.
Re-derived (S3FR §4(H), ESTABLISHED): assume `m <= 3`, so `m = 1` and `gamma = 3` by
(a). Divide `disc(Phi) = U sigma^2 f` by `sigma^2` and use (3.1) below. Reading (c)
puts `ord_y = 4` on the left; the first right-hand term has `ord_y >= 2m + gamma = 5`;
no cancellation, so `ord_y(rho t_0) = 4` with `t_0 = t(eta')(y,0)`, hence
`ord t_0 = gamma = 3 >= 1` and `t(eta')(0,0) = 0`. But `gamma >= 1` forces
`alpha_3(0,0) = 0`, collapsing `t` to `-4 alpha_2(0,0)^3`, so `alpha_2(0,0) = 0`; every
monomial of `disc(eta')` contains `alpha_2` or `alpha_3`, so `disc(eta')(0,0) = 0`,
against reading (b). Hence

```text
(1.3)    m = 4 ,   gamma = 0 ,   alpha_3(0,0) != 0 ,   D(0,0) != 0 .
```

This is where PRE §6 stops, correctly. §§2–3 go one layer deeper — the layer PRE names,
"any deeper layer of TB must reach order `y^{beta_1/2}`" — and that layer does separate
the types.

## 2. The local datum at P_inf

In the chart `(y,sigma)` the place at `P_inf` is

```text
y = s^2 ,   sigma(s) = sum_{k >= 8} c_k s^k ,  c_8 != 0 ,  first ODD k equal to beta_1
```

(PRE §5, Route 2; normalising `y = s^2` costs only a reparametrisation). Split
`sigma(s)` into even part `A(y)` and odd part `s^{beta_1} w(s^2)`, `w` a unit. The germ
equation, the value semigroup of its local ring, and its analytic type are

```text
(2.1)  f = (sigma - A(y))^2 - y B(y)^2 ,  ord_y A = 4 ,  ord_y B = delta_inf = (beta_1-1)/2 ,
(2.2)  O_{Dbar,P_inf} = C{s^2} + s^{beta_1} C{s^2} ,   Gamma = <2, beta_1> ,
(2.3)  mult(f) = 2 ,  tangent cone sigma^2 ,  (f . L_infty) = 8 ,  type A_{beta_1 - 1} .
```

Two consequences. First, `f` is **irreducible** (one place at infinity, promoted) and
reduced. Second, (2.2) is the type's whole extra content: the branch order of *any*
function on the plane lies in `Gamma`, so no pullback has odd order below `beta_1`.
That is the only door through which `beta_1` — equivalently `c`, equivalently
`delta_aff` — enters at `P_inf`, and readings (a)–(c) do not reach it: they see `f` only
through `f(y,0)`, `f(0,sigma)` and `(df/dsigma)|_{sigma=0}`, all `min`-truncated below
`beta_1`.

The charge's question at the rep level, where there is no octic but only a numerical
type:

> **(Q)** For which `beta_1` is there a Miranda datum `(rho, eta')` over `C{y,sigma}`
> with `ord_y rho = m = 4`, `alpha_3(0,0) != 0`, and
> `disc(rho X^3 + sigma eta') = unit * sigma^2 * f`, `f` an `A_{beta_1-1}` germ
> satisfying (2.1)–(2.3)?

A NO kills that type at the representation level, since the mixed cover exists
whenever `phi` does (S3FR §5) and `m = 4` is then forced by (1.3). A YES is *not* an
existence statement for a cover over a global octic, and is not used as one.

## 3. THEOREM TB-GERM

### 3.1 Two identities

Write `Phi = a X^3 + b X^2 Y + c X Y^2 + d Y^3` with `a = rho + sigma alpha_0`,
`b = sigma alpha_1`, `c = sigma alpha_2`, `d = sigma alpha_3`, and
`D := disc(eta')`, `t := dD/dalpha_0 = -4 alpha_2^3 - 54 alpha_0 alpha_3^2 + 18 alpha_1 alpha_2 alpha_3`.
Since `disc` has degree exactly 2 in its first argument, its Taylor expansion in
`rho` terminates and gives S3FR (2.9):

```text
(3.1)   disc(Phi) = sigma^2 * [ -27 rho^2 alpha_3^2 + rho sigma t + sigma^2 D ]  =: sigma^2 * qt .
```

Hand-expanded here term by term from `18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2`,
and confirmed numerically. The new ingredient is an identity S3F/S3FR do not use:

```text
(3.2)   t^2 + 108 alpha_3^2 D  =  16 h^3 ,      h := alpha_2^2 - 3 alpha_1 alpha_3 .
```

*Proof.* Expand `t^2` (six terms) and `108 alpha_3^2 D` (five terms). The
`alpha_0^2 alpha_3^4` terms cancel (`2916 - 2916`), as do the `alpha_0 alpha_2^3 alpha_3^2`
terms (`432 - 432`) and the `alpha_0 alpha_1 alpha_2 alpha_3^3` terms (`-1944 + 1944`);
`alpha_0` disappears entirely. What is left is
`16 alpha_2^6 - 144 alpha_1 alpha_2^4 alpha_3 + 432 alpha_1^2 alpha_2^2 alpha_3^2 - 432 alpha_1^3 alpha_3^3
 = 16 (alpha_2^2 - 3 alpha_1 alpha_3)^3`. `[]`

For a binary cubic `F = AX^3+BX^2Y+CXY^2+DY^3` write `Hess F = (B^2-3AC)X^2 +
(BC-9AD)XY + (C^2-3BD)Y^2`. Then `h = (Hess eta')(0,1)`: the Hessian of `eta'` at the
triple-root direction of `Phi|_{sigma=0}`. Also `Hess Phi = sigma * H~` with
`H~(0,1) = sigma h`. So (3.2) is the classical syzygy
`Jac^2 = 4 (Hess F)^3 - 27 disc(F) F^2` read at that direction (`Jac` the Jacobian
covariant); I checked that route independently and it reproduces (3.2) exactly.

Completing the square in `rho` in (3.1) and substituting (3.2) gives the form the
rest of the section uses:

```text
(3.3)   27 alpha_3^2 * qt  =  4 sigma^2 h^3 - P^2 ,      P := 27 rho alpha_3^2 - sigma t / 2 .
```

Equivalently, with `qt = U f`: **`27 alpha_3^2 U * f = P^2 - 4 sigma^2 h^3` up to sign**;
under (1.3) the factor `27 alpha_3^2 U` is a unit of `C{y,sigma}`, so

```text
(3.4)   f  =  unit * ( P^2 - 4 sigma^2 h^3 ) .
```

### 3.2 Three lemmas

**L1 (`h(0,0) = 0`).** If `h(0,0) != 0` then `h^3` is a unit and has an analytic square
root `k`, so `P^2 - (2 sigma k)^2 = (P - 2 sigma k)(P + 2 sigma k)` with both factors in
the maximal ideal (`P(0,0) = 0` since `m = 4 >= 1`): `f` would be reducible or a square,
against (2.3). Hence `h(0,0) = 0`, and `h` is not a unit times a square.

**L2 (`t(0,0) != 0`; `S := {P=0}` smooth, tangent to `L_infty`).** Take degree-2 parts
in (3.4). On the right `4 sigma^2 h^3` has multiplicity `>= 5` by L1, leaving
`(lin P)^2`; on the left it is `unit(0) * sigma^2` by (2.3). So
`(lin P)^2 = const * sigma^2`, const `!= 0`. With `m = 4`, `rho` has no linear term, so
`lin P = -(t(0,0)/2) sigma` and `t(0,0) != 0`. Then `dP/dsigma(0,0) != 0`: `(y,P)` is a
coordinate system, `S` is smooth with tangent `{sigma = 0} = L_infty`, and on `S`
`sigma = 54 rho alpha_3^2 / t`, so

```text
(3.5)    ord_y ( sigma |_S )  =  m + 2 gamma  =  4 .
```

**L3 (`kappa := ord_y(h|_S)` is finite, `>= 1`).** Finite: if `h|_S = 0` then `P | h`,
so `P^3 | 4 sigma^2 h^3` and (3.4) reads `f = unit * P^2 * (1 - P * (...))`, i.e. a unit
times a square — contradicting reducedness. `>= 1` is L1.

### 3.3 The theorem

> **THEOREM TB-GERM (PROVED-HERE, UNREVIEWED).** *Let `D` be a residual branch
> curve of family-3 type at `g = 2`, i.e. `(d,n) = (8,6)`, with one place at
> infinity and germ `A_{beta_1 - 1}` at `P_inf`. Suppose `phi : pi_1(C^2 - D) ->> S_4`
> exists with meridians going to transpositions and non-constant block products, and
> let `pi : Z -> P^2` be the mixed cover of S3FR §5. Then, with `m = 4`, `gamma = 0`
> of (1.3),*
>
> ```text
> (3.6)     beta_1  =  4g + 3 kappa  =  8 + 3 kappa ,     kappa = ord_{P_inf}(h|_S) >= 1 ,
> ```
>
> *and `kappa` is odd. In particular*
>
> ```text
> (3.7)     beta_1 = 2  (mod 3)      is NECESSARY for phi to exist on the (8,6) row.
> ```

*Proof.* Work in the coordinates `(y,P)` of L2, set `W(y,P) := 4 sigma^2 h^3` expressed
in them, and put `G := P^2 - W`, so `f = unit * G` by (3.4). Since
`ord_P W(0,P) >= 2 + 3 = 5 > 2`, `G(0,P)` has `P`-order 2 and Weierstrass preparation
gives `G = u(y,P) * (P^2 + p(y) P + q(y))` with `u` a unit and `p,q` in `C{y}`; the
analytic type is then `A_{nu-1}` with `nu = ord_y(p^2 - 4q)`. Write
`W = w(y) + P V(y,P)`, `V(y,0) = W_1(y)`. Two evaluations pin `p` and `q`:

```text
at P = 0 :      -w  =  u(y,0) q            ==>   ord_y q  =  ord_y w ;
d/dP at P = 0 : -W_1 =  u_P(y,0) q + u(y,0) p  ==>  ord_y p >= min(ord_y W_1, ord_y q).
```

By (3.5) and L3, `ord_y w = 2 ord_y(sigma|_S) + 3 kappa = 8 + 3 kappa`. And
`W_1 = (8 sigma sigma_P h^3 + 12 sigma^2 h^2 h_P)|_{P=0}` gives
`ord_y W_1 >= min(4 + 3 kappa, 8 + 2 kappa)`, so

```text
ord_y (p^2)  >=  min(8 + 6 kappa, 16 + 4 kappa, 16 + 6 kappa)  >  8 + 3 kappa   for all kappa >= 1.
```

So `p^2` cannot cancel `4q`, and `nu = ord_y(4q) = 8 + 3 kappa`. Matching with the
type, `nu = beta_1`, gives (3.6); `beta_1` is odd (multiplicity-2 unibranch germ), so
`3 kappa` is odd and `kappa` is odd. `[]`

Two scope statements, declared rather than assumed. (i) The proof runs under
`(m,gamma) = (4,0)`; the other TB-admissible pair `(1,3)` of (1.2) is excluded by
Proposition TB-2 (promoted; re-derived in §1.3), and I do **not** claim the proof text
covers it — at `gamma >= 1` the factor `alpha_3^2` in (3.3) is not a unit and the germ
of `P^2 - 4 sigma^2 h^3` acquires the component `{alpha_3 = 0}`, which the Weierstrass
step does not separate. (Formally the same count at `(1,3)` gives `nu = 14 + 3 kappa`
and the same congruence; that is *not* claimed as proved and is not used.) (ii) TB-GERM
consumes SK-5 (through the mixed cover), TB and TB-2, all promoted with review; the new
content is (3.2)–(3.4), L1–L3 and the count.

**COROLLARY (rep-level kills).** `beta_1 = 8 + 3 kappa` has no solution for
`beta_1 = 21` (`kappa = 13/3`) or `beta_1 = 25` (`kappa = 17/3`). So **type A
`(8,6,11)` and `(8,6,7)` admit no such `phi`** and are dead at the representation
level. For `beta_1 = 23` (type B) `kappa = 5`, and for `beta_1 = 29` (`(8,6,3)`)
`kappa = 7`; both are odd positive integers, so both types pass this gate, and the
gate is exactly `3 | c` (since `beta_1 = 32 - c`).

## 4. Local admissibility: witnesses at A_22 and A_28

TB-GERM is a necessary condition. Its converse at the germ — that `m = 4` is
*admissible* at type B's `A_22` germ, i.e. that the kill does not extend to type B by
a finer local reading — needs a witness, not a silence. Here is one, for every odd
`kappa`.

> **PROPOSITION LOC (PROVED-HERE, UNREVIEWED).** *For every odd `kappa >= 1` the
> Miranda datum over `C{y,sigma}`*
>
> ```text
> (4.1)   Phi_kappa  =  ((y^4 + sigma)/27) X^3  -  (sigma y^kappa / 3) X^2 Y  +  sigma Y^3
> ```
>
> *(i.e. `rho = y^4/27`, `alpha_0 = 1/27`, `alpha_1 = -y^kappa/3`, `alpha_2 = 0`,
> `alpha_3 = 1`) has*
>
> ```text
> (4.2)   disc(Phi_kappa) = -(sigma^2/27) * [ (sigma + y^4)^2 - 4 sigma^2 y^{3 kappa} ] ,
> ```
>
> *whose second factor is an irreducible germ of type `A_{7 + 3 kappa}`, unibranch of
> multiplicity 2, tangent to `L_infty = {sigma = 0}` with contact `8`. The datum has
> `m = 4`, `gamma = 0`, `t(0,0) = -2 != 0`, `D(0,0) = -1/27 != 0`, `h = y^kappa`,
> `S = {sigma = -y^4}`, `ord_y(sigma|_S) = 4`, `ord_y(h|_S) = kappa`, and satisfies
> readings (a), (b), (c) and TB's congruence. At `kappa = 5` the germ is `A_22`, the
> type-B germ; at `kappa = 7` it is `A_28`, the `(8,6,3)` germ.*

*Proof.* With `c = 0` the discriminant collapses to `-4b^3d - 27a^2d^2`, i.e. to
`(4 sigma^4 y^{3kappa})/27 - sigma^2(y^4+sigma)^2/27`, which is (4.2). As a quadratic
in `sigma` the bracket is
`sigma^2 (1 - 4 y^{3 kappa}) + 2 sigma y^4 + y^8`, with leading coefficient a unit and
discriminant

```text
(4.3)    4 y^8 - 4 y^8 (1 - 4 y^{3 kappa})  =  16 y^{8 + 3 kappa} ,
```

so the germ is `A_{7+3kappa}`, unibranch exactly because `8 + 3 kappa` is odd, i.e.
`kappa` odd; its contact with `L_infty` is `ord_y y^8 = 8`. The invariants read off:
`h = y^kappa`, `t = -54 alpha_0 = -2`, `D = 4y^{3kappa}/27 - 1/27`, `P = y^4 + sigma`.
Reading (a): `ord_y(-27 rho^2 alpha_3^2) = 8 = 4g`; (b) `D(0,0) != 0`; (c) the
bracket's `sigma`-derivative at `sigma = 0` is `2y^4`, of order `4 = 4(g-1)`. `[]`

Two remarks on LOC's scope.

* It confirms (3.6) on an explicit witness: the general count of §3.3 and the direct
  computation (4.3) agree, which is the cheapest check that the count is neither
  vacuous nor uniformly false. (Family 2 at `g = 2` cannot serve as a positive control
  here: `Pi in V_4` there makes `T_pi = 0` and TB vacuous — S3FR §8.)
* The germ so produced is a **local** normal triple cover: Cohen–Macaulay (Shirane
  1.1.6, via S3FR §3) and regular in codimension one — smooth over the generic point of
  the simple branch, locally `z^3 = unit * sigma` over the generic point of `L_infty` —
  hence normal by Serre. It is not a global cover and is not offered as one;
  `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`.

**Verdict of the local layer.** `m = 4` is *inadmissible* at the `A_20` and `A_24`
germs and *admissible* at `A_22` and `A_28`. So the mixed-cover analysis, pushed past
the leading `sigma`-jets to the layer where `beta_1` enters, separates the four types
exactly — and separates them the same way as the inner braid. That is §5.

## 5. TB-GERM against TUBE-2: E = 3(2 - kappa)

PRE §4's THEOREM TUBE-2 (PROVED-HERE, UNREVIEWED there): on a family-3 `g = 2` row,
`rho_inf`-fixedness collapses to `T_1 = sigma^E . T_1` with
`E = e(iota) = 2 delta_aff - 29 = 14 - beta_1`, and the stabiliser of a non-constant
block subtuple in `B_2 = Z` is `3Z`, so `3 | E`, i.e. `beta_1 = 2 (mod 3)`. TB-GERM
gives `beta_1 = 8 + 3 kappa`, the same congruence. **The two gates are the same gate**,
and the two integers are the same integer:

```text
(5.1)    E  =  14 - beta_1  =  14 - (8 + 3 kappa)  =  3 (2 - kappa) ,      kappa = 2 - E/3 .
```

Checked against PRE's table without adjustment: `kappa = 5` gives `E = -9` (type B),
`kappa = 7` gives `E = -15` (`(8,6,3)`), and the two killed types have no integer
`kappa`, matching `E = -7, -11`. Divisibility of the inner-braid exponent by `3` *is*
the vanishing order of the Miranda cubic's Hessian along `{P=0}` at `P_inf`, up to
(5.1).

**What is shared.** Both consume SK-5 (`Pi` a `3`-cycle): TUBE-2 for `ord(Pi) = 3` and
`3`-cycle block products, TB-GERM through S3FR §5, where SK-5 is what makes `L_infty` a
*total* branch component. Beyond SK-5, nothing: TUBE-2 runs on cabling, the `A_4` word
equation and the `B_2` orbit; TB-GERM on Miranda's structure theory, the Tschirnhausen
filtration along `L_infty` (which supplies `k = 5`), TB-2 and (3.2)–(3.4). Neither uses
`delta_aff` except through `beta_1`.

This matters for routing. PRE flags TUBE-2 and the type-A kill as flagship-shaped,
`UNREVIEWED`, and asks for pairing. Those kills now have a second derivation whose only
shared input is a promoted, reviewed theorem. That is corroboration, not review — a
reviewer must still gate TUBE-2's conjugator `Pi Pi_{d'}^{-1}` and TB-GERM's L1–L3
separately — but a convention error in exactly one of the two would have to reproduce
(5.1) by coincidence.

## 6. The L_infty constraints

The charge asks for "the three/four `L_infty` crossing constraints". The phrase has
two readings on this row and I discharge both, declaring which is which rather than
identifying them (FALLACY-v2, flag/place).

**(i) Crossings of `L_infty` with the rest of `Delta-bar`: one, of contact 8.** `Dbar`
is irreducible of degree `4g = 8` with one place at `P_inf`, so `L_infty` meets the rest
of the weighted branch only at `P_inf`, with `(Dbar . L_infty)_{P_inf} = 8` — TB's
hypothesis, satisfied, and by (1.1) that contact number *is* reading (a). There are no
three or four crossings here; a row with several would leave TB's hypothesis.

**(ii) The three sheets over `L_infty`.** Over `T_0 = L_infty` the cover is totally
ramified with one point above each point, `Gamma = (pi^{-1}T_0)_red = T_0` (TB step
(A)), and `n = T|_{L_infty}` carries `0 -> N -> n -> Q -> 0` with multiplication
`Q^{(x)2} -> N` of cokernel length `m`. With `k_0 = 5`, `m = 4`:

```text
(6.1)   3 deg Q = -k_0 - m = -9 ,  deg Q = -3 ,  deg N = -2 ,  deg N - 2 deg Q = 4 = m .
```

Their integrality is TB's congruence and nothing more.

**(iii) The four-fold divisor of `rho`.** `rho`, the coefficient of `Phi|_{T_0} = rho X^3`,
is a section of `N (x) (Q^v)^{(x)2}` on `L_infty = P^1`, of degree `-2+6 = 4 = m`, and its
divisor is supported in `T_0 ∩ S_pi = {P_inf}` by TB step (C)'s completing note (a zero
at `p in T_0 - S_pi` would put all Miranda coefficients in `m_p`, forcing
`mult_p(disc) >= 4` against multiplicity 2 along `T_pi - S_pi`). Hence

```text
(6.2)   div(rho) = 4 * P_inf   on   L_infty = P^1 ,
```

i.e. a degree-4 form on `P^1` with one quadruple zero — the "four" constraint, and the
exact statement that `Z` is non-Gorenstein at precisely one point over `L_infty`, where
the fibre algebra is `C[z,w]/(z,w)^2` (TB step (F)). Consistent, and imposing nothing
further.

**Global structure recorded, not consumed.** (1) `Hess Phi` vanishes along `L_infty`, and
`H~ := (Hess Phi)/sigma`, a quadratic form on `T` valued in `O(-1)`, has discriminant
`-3Uf` by `disc(Hess F) = -3 disc(F)`: `Dbar` is its degeneracy divisor, with degrees
matching (`(det T^v)^2 (x) O(-2) = O(8)`). The double cover of `P^2` branched along
`Dbar` is the `sgn`-cover of the resolvent; it exists for any even-degree branch curve,
so it is no obstruction. (2) `Z` has an `A_1` point over each affine node: the two branch
meridians go to disjoint transpositions of `S_4`, whose image in `S_4/V_4 = S_3` is the
*same* transposition, so the local monodromy is `Z/2` on two of three sheets — `10` such
points for type B, `7` for `(8,6,3)`. Neither fact is used as a kill. The geography
route through `chi(O_Z) = 23 - c_2(T^v)` is *not* run: `c_2(T)` is not fixed by the
numerical type and the `Z/3`-cover class on the double plane is curve-dependent, so both
belong to the realization lane. (S3F recorded that Tokunaga class as automatically
divisible by `3`; S3FR §8 says not to re-run it. I did not.)

## 7. Verdicts

| type | `Delta` | `beta_1` | germ | `kappa = (beta_1-8)/3` | TB-GERM | TUBE-2 | **rep-level verdict** |
|---|---|---:|---|:--:|:--|:--|:--|
| A | `(8,6,11)` | 21 | `A_20` | `13/3` | **KILLED** | KILLED | **KILLED** (two independent chains) |
| **B** | `(8,6,9)` | 23 | `A_22` | `5` | passes | passes | **OPEN at named input**, residual pinned |
| — | `(8,6,7)` | 25 | `A_24` | `17/3` | **KILLED** | KILLED | **KILLED** (two independent chains) |
| — | `(8,6,3)` | 29 | `A_28` | `7` | passes | passes | **OPEN at named input**, residual pinned |

### 7.1 Type B — `Delta = (8,6,9)`

**Not killed.** The `m = 4` branch-at-infinity requirement is admissible at the `A_22`
germ: `kappa = 5` is a positive odd integer, and LOC exhibits a local Miranda datum
realising that germ with `m = 4`, `gamma = 0` and all three readings. So the charge's
question — does `m = 4` contradict this type's germ structure? — is answered **no**.
The local residual a successor inherits:

```text
k = k_0 = 5 ,  deg Delta-bar = 10 ,  S_pi = Dbar (deg 8) ,  T_pi = L_infty ;
m = 4 , gamma = 0 , kappa = 5 ;  deg Q = -3 , deg N = -2 , div(rho) = 4 P_inf ;
fibre over P_inf is C[z,w]/(z,w)^2 (non-Gorenstein, non-curvilinear) ;
10 further A_1 points of Z over the 10 affine double points ;
outer/inner braid datum exactly as pinned in PRE §8, with E = -9 = 3(2 - kappa) .
```

Named inputs that would close it, in decreasing value:

1. **The realization lane** (`I_23` plus the reduced `I_DP` of length 10): a
   NON-REALIZABLE verdict closes the type outright.
2. **`OPEN[S3-TB-G2]`, retyped.** No longer "kill `m = 4` at `g = 2`": `m = 4` is
   admissible at this germ, so that phrasing is unachievable by a local argument. What
   remains is global — does a normal non-cyclic triple plane exist with
   `deg Delta-bar = 10`, `(deg S_pi, deg T_pi) = (8,1)`, one non-Gorenstein point of
   the type above over the unique crossing, `10` `A_1` points, and `S_pi` rational with
   an `A_22` there? That is the slot Ciliberto–Miranda arXiv:2512.07965v1 classifies
   (weighted degree `<= 10`, completeness failing at one `p_g=0,q=1` slot). S3FR §10
   rules consuming it a new lane, not a repair; this lane supplies the local data such
   a lane needs, and does not consume it. Its missing input is `c_2(T)` = `chi(O_Z)`.
3. **Braid monodromy of a witness**, if REALIZED: `rho_inf`-fixedness is only the
   product relation; `7` vertical tangencies and `10` node squares give a 17-factor
   factorisation to test (PRE §8). `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` still does not
   reach type B (deficit 2, PRE §2).

### 7.2 `(8,6,3)` — the Moh backstop

Identical structure at `kappa = 7`: `beta_1 = 29 = 8 + 3*7`, germ `A_28`,
`delta_aff = 7`, `E = -15 = 3(2-7)`, LOC supplies the witness, TB-GERM does not fire.
**The TB route does not kill `(8,6,3)` at the representation level and cannot serve as
a backstop to the Moh route.** What it does supply is usable negative information: if
the Moh lane returns curve-level survival, the type must be attacked by the same global
triple-plane question as type B (`7` `A_1` points, germ `A_28`), and not by any further
local reading at `P_inf` — that layer is now exhausted in both directions (necessary
condition proved, witness exhibited).

### 7.3 Ledger increments

* `(8,6,11)` and `(8,6,7)` are killed a second time, by machinery disjoint from TUBE-2
  above SK-5. The row stands at two live types, `{(8,6,9),(8,6,3)}`, criterion `3 | c`,
  now with two proofs; and `c = 24 - 3 kappa`, so `3 | c` is integrality of the Hessian
  order `kappa` at `P_inf`.
* TB is **not** `beta_1`-blind. PRE §6 is right that the *leading-jet* layer is, and
  right that the separation must live at order `y^{beta_1/2}`; TB-GERM reaches that
  layer through (3.2)–(3.4) rather than through deeper jets, and finds exactly the
  inner-braid separation. `OPEN[S3-TB-G2]` should be retyped as the global existence
  question of 7.1(2), not as "kill `m = 4`".
* Family 3 at `g >= 3` is untouched: (3.2)–(3.4) are `g`-general, but (1.1)–(1.3) use
  `2g = 4` and TB-2 is a `g = 2` proposition. With `m` unpinned there (S3FR §8:
  `m in {2,5}` at `g=3`, `{0,3,6}` at `g=4`) the count returns a *family* of
  congruences, not one. Named successor, not a claim.

## 8. FALLACY-v2 audit

* **Flag/place/series.** Four objects at `P_inf` are kept apart: the contact
  `(Dbar . L_infty)_{P_inf} = 8` with the *specific* line `L_infty`; the analytic type
  `A_{beta_1-1}`; the numerator `beta_1`; and the defect `m = 4`. Reading (a) is
  *shown* to equal the contact number (1.1), not assumed to. Reduced branch (degree 9)
  and weighted branch (degree 10) are kept apart per S3FR §5, and the two readings of
  "three/four `L_infty` crossings" are separated in §6.
* **Floor/attainment.** `0 <= m <= 2g` is a bound; `m = 4` is TB-2's exact value. (3.6)
  is an *equality*, from a no-cancellation argument written out, not a floor promoted to
  a value. The corollary kills by non-integrality of `kappa` — an emptiness, not a
  failed bound.
* **Carrier/attainment.** LOC exhibits a *local* Miranda datum: not a cover over `P^2`,
  not a curve, not a witness for type B. The survival verdicts read "this lane's tools
  do not kill", never "the object exists".
* **Per-ray/exit-set charge.** No exit price is asserted; no `charge_basis` line, as
  the charge requires.
* **Pole/interior.** The only such steps are Weierstrass preparation in `P` (§3.3),
  whose hypothesis `ord_P W(0,P) > 2` is checked, and the analytic square root in L1,
  whose unit hypothesis is checked. `disc(Hess F) = -3 disc(F)` appears only in a
  remark (§6), never in a kill.
* **Prime label/derivative.** `dD/dalpha_0`, `dP/dsigma`, `df/dsigma`, `h_P`,
  `sigma_P` are genuine derivatives of named functions, and `t = dD/dalpha_0` is
  verified rather than assumed by notation. `eta'` is S3F's inherited label for the
  `sigma`-linear part of `Phi`, not a derivative; flagged here as such.
* **Variable/ring map.** Chart `(y,sigma) = (Y/X, Z/X)`, place orders `(2,8)`; the
  change to `(y,P)` is justified by `dP/dsigma(0,0) != 0` (L2) before use. Miranda's
  structure constants and the polarised cubic are distinguished: on `T_0` the polarised
  cubic is `(-b,3a,-3d,c) = (rho,0,0,0)`, so the `rho` of §3 is TB's `rho`, of order `m`
  — and is not PRE's braid `rho_inf`, nor S3F's resolvent, both of which are renamed
  here on first use.
* **`sat()` / raw remainder.** Not in play: no ideal, no normal form, no CAS.
* **Named risk.** One step would flip the verdict if mis-signed: the `108` in (3.2),
  which is what makes `Q` a perfect *cube* rather than a generic sextic. It is
  hand-expanded, checked at 4000 random integer points, and cross-derived from the
  syzygy `Jac^2 = 4(Hess F)^3 - 27 disc(F) F^2` at `[0:1]`. Second risk: (3.6)'s scope at
  `(m,gamma) = (1,3)`, declared open in §3.3 and removed by TB-2.
* **Not filled by cap or analogy.** Left OPEN at named tools: global existence for
  type B and `(8,6,3)`; `c_2(T)` / `chi(O_Z)`; Ciliberto–Miranda at weighted degree 10;
  `g >= 3`; the `(1,3)` branch of (1.2). None of these is filled by analogy with the
  cases that were computed.

## 9. Custody and sources

Charged inputs: hashes in §0, all matching, all read in full. No other campaign
artifact was opened; SK-2/SK-4/SK-5, `(1.1)`, `(3.1)`, Theorem A, (M-INF-T), and
Shirane §§1.1.1–1.1.7 / Remark 0.2 are used exactly as quoted and adjudicated in PRE
§§1–8 and S3FR §§3–8, and are cited to those sections, not to the originals. Consumed
as promoted-with-review: the mixed cover and its branch typing (S3FR §5, §10), THEOREM
TB (§§3–4), `m = g+2 (mod 3)`, `0 <= m <= 2g` (§4(G)), Proposition TB-2 (§4(H)), SK-5
(§2, §3.2). Consumed as PROVED-HERE-elsewhere and UNREVIEWED, for comparison in §5
only and never as a premise of §3: THEOREM TUBE-2 and `E = 14 - beta_1` (PRE §§4–5).

New this lane, all `PROVED-HERE, UNREVIEWED`: (3.2)–(3.4); L1–L3; THEOREM TB-GERM
(3.6)–(3.7) and its corollary; Proposition LOC; the correspondence (5.1). Routing:
TB-GERM is flagship-shaped and should be paired. Cheapest verification target is
(3.2) plus L1 — re-expanding `t^2 + 108 alpha_3^2 D` by hand and re-deriving
`h(0,0) = 0` from irreducibility checks the two steps that carry the congruence;
cheapest hostile target is the no-cancellation inequality of §3.3 and the
`(m,gamma) = (1,3)` scope statement.

No external literature was fetched, no new primary source is claimed, and no ledger,
charged file or `jc2-lean` path was touched.

No `charge_basis` line: this report asserts no new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30959`.
- Body SHA-256:
  `4f464f9c7321501cf0adaacc6ad573212911d41e4589ccf47e834be709b59d6c`.
