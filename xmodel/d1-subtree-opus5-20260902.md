# D1-SUBTREE — the Jacobian condition below the last major disc is an EQUALITY: the sub-tree is forced to be a star, `N` is PINNED by the skeleton (floor = ceiling, and only at the bottom), and the ceiling `D <= C(N)` still does not follow

Lane: `D1-SUBTREE` (successor `OPEN[D1-SUBTREE]` of N-ON-THE-TREE).
Date: 2026-09-02. Agent: Opus 5. Desk derivation + desk-scale CAS
(python3 3.14.7 / sympy 1.14.0, exact over `Q`; no Singular, no AWS, no web, no
fetching). Drivers in `box/d1sub-drivers-20260902/`; peak RSS < 1.2 GB, one core.

## 0. Custody, method, scope

The four charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all four match the charge (`44223b32…` n-on-the-tree, `863b05db…`
depth-ceiling, `4a171d91…` depth-ceiling review, `8116bc65…` integration15).

**N-ON-THE-TREE (NOTT) is a PROPOSAL and is treated as one.** CONTACT-DEFICIENCY and
FRONTIER-N are re-proved (§2.3) and re-controlled on genuine Keller pairs;
DETECTOR-NULL gets a **second, shorter proof from a different clause of Moh's
Prop 6.1** (§3.5); **RADIUS-ORDER is retracted as new — it is Moh's own Lemma 5.2**
(§7 C1); N-CEILING is re-derived and then shown to be **attained**, which is the
whole result.

Moh 1983 was read **firsthand from the page images** at every point that carries
weight; the OCR (`box/depth-drivers-20260902/moh.txt`, `b6a36914…`) is used only to
locate. Pages rendered with `pdftoppm` from
`refs/moh1983_jram340_configurations_of_roots.pdf` (`6c8847a8…`):

```text
  p.151 (PDF 12)  Lemma 2.1 with BOTH displays -- the Jacobian condition on the
                  eta-expansion (DC and NOTT quote only its corollary "M_i <= n-1").
  p.178 (PDF 39)  Lemma 5.2:  ((n-L)/d_r) lambda* = -1 + delta*.
  p.179 (PDF 40)  Definition 5.1(1)-(4) VERBATIM: DC's page-image recovery CONFIRMED.
  p.180 (PDF 41)  Proposition 5.3 VERBATIM, stated "for r >= 2".
  p.190-191 (PDF 51-52)  Prop 6.1: hypotheses (r >= 2, MINOR window
                  d_r/(n-M_r) >= V_r >= 1), clauses (1),(2), and the proof display
                  ord g(sigma*) = (n/(n-M_r))(-1+delta_r) + V_r(n/d_r)(delta*_{r-1}-delta_r).
  p.164-165 (PDF 25-26)  Prop 4.1, Def 4.1 (the operator D(a,b,p,q)), Prop 4.2.
```

Typing discipline as charged: DEPTH-CEILING's reviewed items at their scopes
(DEPTH-LOG, PLACE-LEDGER, CONTACT-DEFICIENCY monic GEN, NU-TWO, MOH-SHARP-2);
**no case (A)** (EMPTY at every N), **no A2**, **no `Z(G) = 1`**; H2 quoted only where
the campaign window `4 <= N <= 16` is used, and marked at every use. No canonical
ledger edited; `jc2-lean` not inspected; nothing fetched.
**No `charge_basis` line: this report asserts no new exit price.**

Deliverables, sealed (`box/d1sub-drivers-20260902/`):

```text
  574f2f44…  jacfibre.py    101 checks   27a30dd7…  treecheck.py   151 checks
  cf0780cc…  d1floor.py 232 384 controls e2b4d616…  runall.py   (filters)
  e7d7d2e6…  general.py  (knapsack)      cb6cebd1…  runall.log
  a01c2cc9…  general.log                 6c921bc6…  README.md
```

Six degree-like integers kept apart and never substituted: `D`; the geometric degree
`N`; `K = gcd(deg P, deg Q)`; **Moh's `n = deg_y g = deg g = D`** and **Moh's
`m = deg_y f`**; the campaign's `n = deg Abar_F` (source side, occurring nowhere
here); `nu = 2`. Moh's `d_i`, the exponent `d` of `l(P) = alpha H^d`, and `d_s` are
three-way distinguished; `delta` is never confused with `delta_aff`.

## 1. Verdict, up front

```text
(1) THE JACOBIAN CONDITION BELOW D_1 IS NOT A GAP -- IT IS AN EQUALITY.
    THEOREM JAC-FIBRE (§3.1): for a Keller pair in Moh's gauge and EVERY Puiseux
    branch tau of a generic fibre {g = c_2},
          ord_t f(tau)  +  ord_t g_y(tau)  =  -1                      (exactly),
    the general law being  ... = -1 + ord_t J(tau).  Since
    g_y(tau_i) = prod_{j != i}(tau_i - tau_j), this constrains the tree of the roots
    ALONE, at every depth, in particular below delta_1 where Moh's recursion stops.
    Consequence (§3.2), THEOREM FRONTIER-EXACT:
          N  =  sum over the roots rho of g of ( 1 - delta^0_rho )^+ ,
    delta^0 the g-frontier.  The deficiency is not "a bounded rational the sub-tree
    can drive to 0": it is 1 - delta^0, computed by the g-tree alone.
(2) THEOREM D1-PIN (§3.6).  The floor this gives at the bottom major disc,
    c_rho >= (1-delta_1) + lambda_g(delta_1), and the ceiling NOTT already had,
    c_rho <= -lambda_f(delta_1), are EQUAL -- and, in closed form,
          floor(r) - ceiling(r)  =  (1 - delta_r) (-M_r - m) / (n - M_r) ,
    which vanishes iff M_r = -m, i.e. AT r = 1 AND AT NO OTHER LEVEL.  So the value
    is pinned:  c_rho = m(1-delta_1)/(n+m)  for every g-root of a bottom major disc,
          N  =  sum over bottom major discs B of  a_1(B) (1-delta_1(B)) d/(d+e)
             =  sum_B V_2(B) q(B),   q := d e K prod_{j=2}^{s} P_j/Q_j = (1-delta_1)de/(d+e).
    N is DETERMINED by the skeleton, not merely bounded.  OPEN[D1-SUBTREE] CLOSED.
(3) THEOREM D1-STAR (§3.7).  Equality is therefore forced in every step: below
    delta_1 the slope of lambda_g is exactly 1 and lambda_f is exactly constant.  The
    sub-tree of D_1 is a STAR -- its a_1 = eV_2 roots of g separate pairwise at
    exactly delta_1, no root of f in D_1 follows any of them below delta_1, and Moh's
    p(pi) at the bottom has a_1 SIMPLE roots.  This is why his recursion stops: not
    a missing datum, but NOTHING BELOW.
(4) OPEN[UPPER-TO-FLOOR]: ANSWERED, AND THE ANSWER DOES NOT REACH THE CEILING.
    A floor on N from boundary data exists (first in the record) and EQUALS the
    ceiling.  But the pinned value is small for small V_2: measured, min over branch
    data of V_2 q is 3/64 at D <= 120 and 3/112 at D <= 200, with NO growth in D.  So
    no D <= C(N) follows -- THEOREM PIN-NOT-CEILING (§4).  The filter that IS new is
    INTEGRALITY, not size.
(5) MEASURED.  252 Puiseux-level controls (9 genuine Keller pairs to D = 8, exact;
    24 non-Keller negative rows) + 232 384 skeleton controls, 0 failures.  Integrality
    kills 98.98% of V-assignments and 60.0% of groups at D <= 120 under the
    branch-uniformity hypothesis (UNI), and 24.7% of groups WITHOUT (UNI) by exact
    knapsack.  NO degree is emptied; no (B2)/(B3) cell dies.
```

## 2. Part (1): the sub-tree of `D_1`, set up exactly

### 2.1 Gauge, tree, and the two functions

`(f,g)` is a Keller pair in Moh's gauge (GEN): `deg f = deg_y f = m`,
`deg g = deg_y g = n = D`, both monic in `y`, `m < n`, `[f,g] = c in C^*`. Put
`t = x^{-1}`, work in `C<t>`, `ord = ord_t`, `ord_t x = -1`; `rho_1..rho_n` are the
roots of `g`, `phi_1..phi_m` those of `f`. For a Puiseux series `sigma`,

```text
   lambda_h^sigma(delta) := ord_t h(sigma_delta) = sum_j min(delta, ord(sigma - h-root_j)),
```
`sigma_delta` Moh's general `pi`-root of radius `delta` on `sigma`'s path (Prop 1.2).
`lambda_h` is continuous, piecewise linear, nondecreasing, of slope `#{h`-roots in the
disc`}`, with `lambda_g(-1) = -n`, `lambda_f(-1) = -m`. **The frontier**
`delta^0_sigma` is the least `delta` with `lambda_g^sigma(delta) = 0`.

### 2.2 Moh's tower, verbatim, and what it fixes above `D_1`

Read firsthand (p.179): **Definition 5.1**, a tower `D_s ⊋ … ⊋ D_r` with integers
`{V_i : i = r+1..s+1}` such that

```text
 (1) in D_i the polynomial g(y) has precisely (n/d_{i+1}) V_{i+1} roots and T_j^psi(y)
     has precisely (-mu_j/d_{i+1}) V_{i+1} roots, j = 1..i ;
 (2) V_{i+1} d_i/d_{i+1} >= V_i > d_i/(n - M_i),  i = r+1..s,   V_{s+1} = d_{s+1} ;
 (3) delta_i = 1 - (n-M_i) prod_{j>i}[V_j(n-M_j)-d_j] / [(n-M_s-1) prod_{j>i}[V_j(n-M_{j-1})-d_j]] ;
 (4) at the general point sigma_i of D_i the conditions of Prop 4.6 hold with
     v = V_{i+1}(d_i/d_{i+1}).
```

`Prop 5.3` (p.180, **"for r >= 2"**) builds `D_{r-1}` from `D_r` given a factor
`pi - C_r` of Prop 4.6's `p(pi)` of multiplicity `V_r` in the window of (2). At
`r = 2` this delivers `D_1`; at `r = 1` there is no `M_0` and the recursion halts.
With `M_1 = -m`, `d_2 = K`, `n = Ke`, `m = Kd`:

```text
   a_1 := # g-roots in D_1 = (n/d_2) V_2 = e V_2 ,      b_1 := # f-roots = d V_2 ,
   b_1/a_1 = m/n   (Def 5.1(1) at i = 1, with -mu_1 = m) .
```

**Moh's Lemma 5.2 (p.178), verbatim:** `((n-L)/d_r) lambda* = -1 + delta*`. Read at
`L = M_r`, `delta* = delta_r`, and pushed to `g` by `ord g(sigma) = (n/d_r) lambda`,
this is exactly

```text
   (RO)   lambda_g(delta_r)  =  n (delta_r - 1)/(n - M_r) ,   in particular
          lambda_g(delta_1)  =  - n (1 - delta_1)/(n + m)  <  0 .
```

The same display reappears inside Moh's proof of Prop 6.1 (p.191, first line of the
computation). **`lambda_f(delta_r) = (m/n) lambda_g(delta_r)` is likewise Moh's own**:
the proof of Prop 6.1 records `ord g(sigma*) = n lambda*` and
`ord T_i^psi(sigma*) = (-mu_i) lambda*` as its displays (1) and (2), and `-mu_1 = m`.
(The distinction `T_1^psi` vs `f` costs nothing here: `T_1^psi = f + const` because
`deg_y T_1^psi = m < n = deg_y g`, and at every level where `lambda_f < 0` the trees
of `f` and `f + const` coincide; `lambda_f(delta_1) < 0` by (RO).)

### 2.3 `N` restricted to `D_1`, re-derived

> **CONTACT-DEFICIENCY (re-derivation).** Both coordinates monic in `y` with
> `deg = deg_y`, so `Res_y(f-c_1, g-c_2) = prod_{i,j}(phi_j - tau_i)` with no
> leading-coefficient factor, and for generic `(c_1,c_2)` the `N` common zeros are
> reduced with distinct `x`-coordinates; `deg_x = -ord_t`, so
> `N = - sum_{i,j} ord_t(tau_i - phi_j)`. The monic/`deg = deg_y` hypothesis is
> load-bearing (NOTT tested it by failure; the gauge is fixed by hypothesis here).

> **FRONTIER-N (re-derivation).** `sum_j ord_t(tau - phi_j) = ord_t(f(tau) - c_1)
> = min(0, ord_t f(tau))` for generic `c_1`, so
> ```text
>       N  =  sum over the n roots tau of g - c_2 of  ( - ord_t f(tau) )^+ .
> ```
> Each `tau` sits at contact `delta^0` with a nearest root `rho` of `g`
> (`delta^0_tau := max_j ord(tau - rho_j)`), and then
> `lambda_g^rho(delta^0) = sum_j ord(tau - rho_j) = ord_t g(tau) = 0`: `delta^0_tau`
> **is** the frontier of the matched `g`-root. Hence
> `N = sum_rho (-lambda_f^rho(delta^0_rho))^+`, and restricted to one bottom major
> disc,
> ```text
>     N|_{D_1}  =  sum_{rho in D_1} ( -lambda_f(delta^0_rho) )^+   in
>                  [ 0 , a_1 (-lambda_f(delta_1)) ]      -- NOTT's bounded quantity.
> ```

The **residual free datum** NOTT names is the joint tree of the `a_1 + b_1` points of
`D_1` strictly below `delta_1`. Part (2) computes it.

## 3. Part (2): imposing `[f,g] = 1` below `D_1`

### 3.1 THEOREM JAC-FIBRE — the Jacobian condition on one branch of one fibre

> **THEOREM JAC-FIBRE (proved here).** Let `f, g in C[x,y]` be monic in `y`, `F` dominant,
> `J := [f,g] = f_x g_y - f_y g_x`. Fix generic `c_2`, let `tau in C<t>` be any root of
> `g - c_2`, and let `a_0` be the `t^0`-coefficient of `f(tau)`. Then
> ```text
>       ord_t ( f(tau) - a_0 )  +  ord_t g_y(tau)  =  -1  +  ord_t J(tau) .      (JF)
> ```
> In particular, for a **Keller** pair `ord_t J(tau) = 0` on every branch and
> ```text
>       ord_t f(tau) + ord_t g_y(tau) = -1        at every PROPER branch (ord_t f(tau) < 0).
> ```

*Proof.* Put `F(t) = f(t^{-1}, tau(t))`, `G(t) = g(t^{-1}, tau(t)) = c_2`. From
`G' = 0`: `tau' = g_x t^{-2}/g_y` (`g_y(tau) != 0`, as `dg` never vanishes when
`J != 0`, and for generic `c_2` in any case). Substituting into
`F' = -f_x t^{-2} + f_y tau'` gives

```text
        F'(t) . g_y(t^{-1},tau(t))  =  - t^{-2} J(t^{-1},tau(t)) .          (star)
```

`(star)` is an identity of Puiseux series. Taking `ord_t` and using
`ord_t F' = ord_t(F - a_0) - 1` (char 0) yields (JF). `f(tau)` is nonconstant, since a
branch on which both `f` and `g` are constant would be a point. ∎

Two readings. **(i)** `(star)` is the Gelfand–Leray form `df = c dx/g_y` in Puiseux
coordinates: the Keller condition says the pole order of `f` and the vanishing order
of `g_y` on a branch add to `-1`, **with no room left**. **(ii)** `g - c_2` is monic
with roots `tau_1..tau_n`, so

```text
        g_y(tau_i) = prod_{j != i} (tau_i - tau_j) ,     so
        - ord_t f(tau_i)  =  1 + sum_{j != i} ord_t(tau_i - tau_j)          (Keller, proper)
```
— **an identity between the pole order of `f` and the contact orders of the fibre's
own branches, with `f` only on the left.** This is the instrument the charge asked
for: an identity in `t` constraining *every* level of the tree, including the levels
below `delta_1` where no characteristic exponent remains.

### 3.2 COROLLARY FRONTIER-EXACT — the deficiency IS `1 - delta^0`

> **COROLLARY FRONTIER-EXACT.** For a Keller pair in the gauge and generic `c_2`,
> every root `tau` of `g - c_2` satisfies
> ```text
>       - ord_t f(tau)  =  1 - delta^0_tau ,      hence
>       N  =  sum over the n roots rho of g of  ( 1 - delta^0_rho )^+ ,
> ```
> and, combined with FRONTIER-N, `lambda_f(delta^0_rho) = delta^0_rho - 1` **exactly**
> at every frontier with `delta^0 < 1`, while `delta^0 >= 1` is exactly the condition
> that the branch be non-proper.

*Proof.* Let `Lambda(delta) := ord_t (g-c_2)(sigma_delta) = sum_j min(delta, ord(tau-tau_j))`
along `tau`'s own path (the `j = i` term is `delta`). For `delta < delta^0` one has
`lambda_g^tau(delta) < 0`, hence `Lambda(delta) = ord_t(g(sigma_delta) - c_2) =
lambda_g^tau(delta)`; both sides are continuous, so `Lambda(delta^0) = 0`. By
FRONTIER-N's separation clause (the `a(B)` roots of `g - c_2` in the frontier ball
have distinct `pi`-coefficients, so they separate pairwise at exactly `delta^0`, and
every other root is farther out), `ord(tau_i - tau_j) <= delta^0` for all `j != i`,
so `Lambda(delta^0) = delta^0 + sum_{j != i} ord(tau_i - tau_j) = 0`. Insert into
(ii) of §3.1. ∎

**This inverts the charge's — and NOTT's — reading of the sub-tree.** More structure
below `delta_1` makes `lambda_g` rise faster, hence `delta^0` SMALLER, hence the
contribution `1 - delta^0` LARGER. Extra contact among the roots of `g` does not lower
`N`; and extra contact between `f`-roots and `g`-roots is not free, because
`lambda_f(delta^0) = delta^0 - 1` is forced.

### 3.3 The general-point form, and its exact relation to Moh's Prop 4.1

Moh's **Prop 4.1** (p.164) is `(star)` at a general `pi`-root: for `h in k[f,g]`,

```text
   J_{t,pi}(h(sigma), g(sigma)) = [lambda_h h_sigma(pi) g'_sigma(pi)
                                 - lambda_g g_sigma(pi) h'_sigma(pi)] t^{lambda_h+lambda_g-1} + ...
                                = - h_f(sigma) t^{-2} (d sigma/d pi) .
```
With `h = f` (`h_f = 1`) and `d sigma/d pi = t^delta` the right side has order exactly
`delta - 2 + ord_t J(sigma)`, while the left has order `>= lambda_f + lambda_g - 1`.
Hence

```text
   (JAC-ARC)   lambda_f(delta) + lambda_g(delta)  <=  delta - 1 + ord_t J(sigma_delta),
```
with equality **iff** Moh's operator `D(lambda_f, lambda_g, f_sigma, g_sigma) != 0`,
i.e. **iff `sigma_delta` is not a distribution detector** (Def 3.1's clauses (3)–(4)
are precisely `lambda_f g'_sigma/g_sigma = lambda_g f'_sigma/f_sigma`).

> **SCOPE CORRECTION, tested by failure against my own first draft.** (JAC-ARC) as an
> *inequality* is **not** a Keller criterion: for a non-Keller pair `ord_t J < 0`, so
> `lambda_f + lambda_g <= delta - 1` holds *a fortiori*, and CONTROL T5 exhibits four
> non-Keller pairs violating it nowhere. The Keller content is the **equality at the
> frontier** (§3.2). Any use of (JAC-ARC) must carry the `ord_t J` term.

### 3.4 What Moh's Lemma 2.1 does and does not give below `D_1`

The charge asks for "the Jacobian identity on the exponent tower". Read firsthand
(p.151), **Lemma 2.1** with both displays: with `g = eta^{-n}` and
`f = eta^{-m} + sum_{i > -m} f_i(x) eta^i`,

```text
   J_{x,y}(f,g) = c in k^*  <==>  ord_eta( sum f_i(x)eta^i - sum f_i(0)eta^i ) = n-1
                                  and  deg_x f_{n-1}(x) = 1 ,
   equivalently  f_i(x) in k for i < n-1  and  f_{n-1}(x) = ax + b, a != 0 .
```
Its proof is one line of chain rule, `J = (df/dx)|_g . (dg/dy)|_x`. **This is a
complete statement of the Keller condition — but on the `eta`-adic side**, and its
only consequence for the tree is Moh's own: `f_{n-1} != 0` and `gcd(n,n-1) = 1` force
`M_i <= n-1`. It says **nothing** about the `t`-adic sub-tree of `D_1`, because the
`M_i` are exponents of `eta = g^{-1/n}`; the `f_i(x)` for `i > n-1` are unconstrained
by it (they are fixed by `g` and `c` through `f_x = c/g_y`, which is `(star)` again).
**The instrument that reaches below `D_1` is `(star)` in `t`, not Lemma 2.1 in
`eta`** — the exact answer to the charge's "is the Jacobian identity at that depth an
identity in the wrong variable?": Lemma 2.1 is; `(star)` is not.

### 3.5 DETECTOR-NULL, by the shorter route, with its scope pinned

Read firsthand (p.190–191), **Prop 6.1** is stated for **`r >= 2`** and for a factor
of `p(pi)` whose multiplicity satisfies the **minor** window
`d_r/(n - M_r) >= V_r >= 1`. Its clause **(1)** reads: *for any `pi`-root `sigma` of
`g(y) prod_{i<r} T_i^psi(y)` with `ord(sigma - tau) > delta_r`, the inequality
`delta < 1` implies `ord g(sigma) < 0`.*

> **LEMMA DETECTOR-NULL (second proof).** Prop 6.1(1) says `lambda_g(delta) < 0` for
> every `delta < 1` on a minor branch, i.e. `delta^0 >= 1` there. By
> FRONTIER-EXACT the contribution is `(1 - delta^0)^+ = 0`. ∎

This uses a different clause of the same proposition than NOTT's route
(Prop 6.1(2) + Def 3.1 + continuity), so the two cross-check each other. It also
**pins the scope**: Prop 6.1(2) holds under the printed `r >= 2` MINOR hypothesis.
Read without it — "any `sigma` with `ord g(sigma) < 0` is a detector" — it would give
`lambda_f(delta^0) = 0` at **every** frontier, hence `N = 0`, contradicting `N >= 2`.
NOTT's DETECTOR-NULL is correct as stated (minor discs only); the one-level-more-
general reading is refuted by FRONTIER-EXACT. That is the sharpest available check on
the import NOTT flagged in its DISCLOSURE (1).

### 3.6 THEOREM D1-PIN — floor meets ceiling, at the bottom and only there

> **THEOREM D1-PIN.** Let `rho` be a root of `g` in a bottom major disc `D_1`
> (radius `delta_1`, `a_1 = e V_2` roots of `g`, `b_1 = d V_2` roots of `f`), and let
> `c_rho := (-lambda_f(delta^0_rho))^+` be its contribution to `N`. Then
> ```text
>   FLOOR    c_rho = 1 - delta^0_rho  >=  (1 - delta_1) + lambda_g(delta_1)   [FRONTIER-EXACT
>            + lambda_g has slope >= 1 below delta_1, so delta^0 <= delta_1 - lambda_g(delta_1)]
>   CEILING  c_rho = -lambda_f(delta^0_rho) <= -lambda_f(delta_1)             [lambda_f nondecreasing]
> ```
> and, with (RO) and `lambda_f(delta_1) = (m/n)lambda_g(delta_1)`, **the two are equal**:
> ```text
>   FLOOR = (1-delta_1) - n(1-delta_1)/(n+m) = m(1-delta_1)/(n+m) = -(m/n)lambda_g(delta_1) = CEILING .
> ```
> More precisely, at any tower level `r`,
> ```text
>   floor(r) - ceiling(r)  =  (1 - delta_r) . (-M_r - m) / (n - M_r) ,
> ```
> which is `< 0` for `r >= 2` (`M_r > M_1 = -m`) and `= 0` **exactly at `r = 1`**.
> Hence, at every bottom major disc,
> ```text
>   c_rho  =  m(1-delta_1)/(n+m)  =  (1-delta_1) d/(d+e)     for EVERY rho in D_1,
>   N      =  sum over bottom major discs B of  a_1(B) . (1-delta_1(B)) . d/(d+e)
>          =  sum_B V_2(B) . q(B),    q := (1-delta_1) d e/(d+e) = d e K prod_{j=2}^{s} P_j/Q_j,
> ```
> with `sum_B a_1(B) <= a_{s-1} = u e` (the bottom discs are disjoint subsets of the
> unique major child `D_{s-1}` of the root ball, NU-TWO), i.e. `sum_B V_2(B) <= u`.
> In particular `N <= u q = U`: **NOTT's N-CEILING is ATTAINED when the bottom discs
> exhaust `D_{s-1}`, and is otherwise exact after the substitution `u -> sum_B V_2(B)`.**

*The coincidence is not an accident.* `-M_1 = m = deg_y f` is the leading exponent of
`f` in `eta`, and the level at which (RO) gives `lambda_g = -n(1-delta)/(n+m)` is the
unique level where "the `f`-mass still present" (ceiling) equals "the `g`-mass still
to be spent" (floor). So **`delta_1` can be DEFINED intrinsically as that crossing**,
with no Def 5.1(3) — and CONTROL T verifies the intrinsic definition reproduces the
right `delta_1` on 9 genuine Keller pairs.

### 3.7 THEOREM D1-STAR — the sub-tree of `D_1` is a star

> **THEOREM D1-STAR.** Under the hypotheses of D1-PIN, equality is forced in both
> chains, so along the path of every `g`-root `rho` of a bottom major disc,
> ```text
>   (a) lambda_g has slope EXACTLY 1 on [delta_1, delta^0] : no other root of g
>       accompanies rho below delta_1, i.e. the a_1 roots of g in D_1 separate
>       PAIRWISE at exactly delta_1 ;
>   (b) lambda_f is CONSTANT on [delta_1, delta^0] : no root of f in D_1 follows rho
>       below delta_1 ;
>   (c) delta^0_rho = delta_1 + n(1-delta_1)/(n+m) is the SAME for all rho in D_1 ;
>   (d) Moh's leading polynomial p(pi) at sigma_1 (Def 5.1(4) at i = 1) has
>       a_1 = e V_2 DISTINCT simple roots.
> ```
> The `b_1` roots of `f` may still cluster among themselves below `delta_1`; that is
> invisible to `N`, because `lambda_f` is measured along a `g`-root's path.

**This answers "why does Moh's recursion end at `D_1`".** NOTT located the gap
correctly but read it as *missing data*: "at `r = 1` the minor criterion reads
`#roots <= n/(n+m) < 1`, so every subdisc of `D_1` is major and would extend the tower
— but there is no `M_0`". D1-STAR says those subdiscs are **singletons**: formally
major, unable to extend the tower because Def 5.1(1) at `i = 0` would need `(m/n)V_1`
roots of `f`, not an integer for `V_1 = 1` unless `n | m`. **The recursion stops
because the tree stops.**

### 3.8 Controls (fail-closed; `box/d1sub-drivers-20260902/`)

Every claim of §3 is tested on **genuine Keller pairs** — polynomial automorphisms,
the only Keller pairs available — and on non-Keller negative rows. `jacfibre.py`
computes the multisets `{ord_t h(tau_i)}` **exactly**, by the Newton polygon of
`Res_y(g - c_2, z - h)` with respect to `ord_t`; `treecheck.py` computes
`lambda_f, lambda_g` **exactly on the tree**, using that for an automorphism both
`{f=0}` and `{g=0}` are lines with ONE place at infinity, so all `n` roots of `g` are
conjugate and the per-root contact multisets are `Res_y(g(x,y), g(x,y+z))` and
`Res_y(g(x,y), f(x,y+z))` divided by `n`.

```text
  jacfibre.py  101 checks, 0 failures, 4.1 s
    A 9 automorphisms in gauge, (m,n) up to (4,8): J in C^*, N = 1,
      {ord_t (f g_y)(tau_i)} = {-1} on EVERY branch, N = sum(1-delta^0)^+.
    B NEGATIVE, one-parameter: f = y, g = x^j + y^k, J = -j x^{j-1}.  On all 16 rows
      ord_t(f g_y)(tau) = -j = -1 + ord_t J(tau), and = -1 EXACTLY at j = 1.  The
      identity is tested by failure, and the failure is quantitative.
    C NEGATIVE, NOTT's two-tower rows (m,n) = (2,3),(4,4),(4,6),(3,4): the general
      law (JF) holds on all four, the Keller value -1 on none.
    D closed-form tree for (y, x+y^k), k = 2..8: floor = ceiling = 1/k, a_1 = k,
      pinned N = 1 -- the charged automorphism control.
  treecheck.py  151 checks, 0 failures, 27 s
    T on the TREE, 9 automorphisms: lambda_g(-1) = -n, lambda_f(-1) = -m; (JAC-ARC)
      at every breakpoint and midpoint; lambda_f(delta^0) = delta^0 - 1;
      N = n(1-delta^0)^+; Lemma 5.2 at r = 1 in its INTRINSIC form; floor = ceiling
      at delta_1; PROPORTIONALITY lambda_f(delta_1) = (m/n)lambda_g(delta_1) verified
      independently of Def 5.1(1); and D1-STAR (a) and (b).
    T5 NEGATIVE: N = sum(1-delta^0)^+ holds IFF Keller (4 rows); the general law
      c = 1 - delta^0 - ord_t J reproduces N = 2, 3, 5 where ord_t J is single-valued.
  d1floor.py  232 384 controls, 0 failures, on 40 001 V-skeletons with n <= 120
    1 Moh Lemma 5.2 vs an INDEPENDENT incremental integration of lambda_g (slope =
      root count): 0 mismatches.   2 floor(r) = ceiling(r) at r = 1 on all 40 001, at
    NO level r >= 2.   3 q = (1-delta_1)de/(d+e) = deK prod P_j/Q_j, U = u q: 0
    mismatches.   4 the automorphism control on the skeleton side, k = 2..9.
    5 Moh's six published rows, pinned (§5.2).   6 the closed-form window extremes vs
    brute force, 655 groups: 0 mismatches.
```

The D1-STAR verification deserves emphasis: the automorphisms of CONTROL T have
**nontrivial** `g`-trees (`n = 8` roots splitting `2+2+2+2` at `delta_1 = 5/8`), the
intrinsic `delta_1` is recovered by the floor/ceiling crossing alone, and below it the
slope of `lambda_g` is exactly 1 and `lambda_f` is exactly constant — on every row.

## 4. Part (3), honestly: the pinning is real and does NOT give the ceiling

The charge's part (3) is conditional on the sub-tree being able to drive
`N|_{D_1} -> 0`. It cannot (§3), so `THEOREM UPPER-ONLY` is **not** the statement to
make. The honest statement in the other direction is this one.

> **THEOREM PIN-NOT-CEILING (measured, with its hypotheses).** The boundary tree
> determines `N` exactly (D1-PIN), but the determined value does not grow with `D`:
> over the census of admissible skeletons, the minimum over branch data of a single
> bottom disc's contribution `V_2 q` is
> ```text
>     D <= 120 :  min L = 3/64   = 0.04688       (10 637 groups)
>     D <= 200 :  min L = 3/112 = 0.02679         (116 666 groups)
> ```
> and does not increase with `D`. Since `N >= L(skeleton)` is the only lower bound the
> boundary supplies, and `L` stays below 1, **no inequality of the form `D <= C(N)`
> follows from D1-PIN**, for any `C`. The obstruction is that `V_2 = 1` and
> `q = deK prod_{j} P_j/Q_j` can be small at every degree: `q` is a product of `s-1 <=
> 6` factors each `< 1`, and the windows of Def 5.1(2) allow the small end at every
> level.

**`OPEN[UPPER-TO-FLOOR]` is answered, split.** *Yes*: an instrument bounding `N`
**below** by boundary data exists — the first in the record — and it is an equality,
not a bound. *No*: it does not bound `D` at fixed `N`, the floor being `O(1)` and not
`Omega(D)`. The pinning delivers an **arithmetic** filter (§5), not a size filter.

**What the ceiling would now need.** `N = sum_B V_2(B) q(B)` shows the missing
ingredient is not a sharper boundary instrument but a **lower bound on the `V_j`, or
on the number of bottom discs, at large `D`** — that a degree-minimal counterexample
cannot have a thin tower. Nothing in Moh's Prop 4.4/4.6/5.3, his search list (1)–(13),
or GGV's corner recursion bounds `V_j` below beyond `V_j > d_j/(n-M_j)`. The charge's
candidates, repriced:

```text
  cofinal-invariant (0741Z round): still the only candidate that is not a boundary
      instrument; unaffected here, D1-PIN being boundary-local.
  Chevalley-Weil / affine ramification on the Galois closure: NOW BETTER POSED.
      D1-STAR makes the bottom discs stars, so the Galois action on the fibre's places
      is described entirely by (a_1(B), delta_1(B)) and the orbit structure of the
      bottom discs -- the exact datum such a count needs; the place-form is
      m_gamma = nu_gamma (1-delta_1)d/(d+e).
  source-side etale structure of E = F^{-1}(A_F): untouched; D1-PIN is TARGET-side and
      does not compose with it (the campaign's n = deg Abar_F is absent here).
```

## 5. Part (4): pricing the pinned filter on the charged census

### 5.1 The hypothesis-free floor, measured

`runall.py` re-implements the NOTT/DEPTH-CEILING census (`d_1 = n > d_2 = K > … >
d_s >= 4`; `s >= 3`; `M_1 = -m`, `M_s = n-2`; `m = Kd`, `n = Ke`, `gcd(d,e) = 1`,
`2 <= d < e`; `K >= 16`; Def 5.1(2); `V_s < d_s`) and computes, per **group**
`(n, m, M_2..M_s, V_s)`,

```text
   L := min over admissible lower-V data of  V_2 q     (a SOUND floor: N >= L,
        since at least one bottom major disc exists and each contributes V_2 q)
   U := u . max over admissible lower-V data of q      (= NOTT's branch-robust U_rob)
```
`q` is strictly increasing in every `V_j` (`d/dV(P/Q) = d_j(M_j-M_{j-1})/Q^2 > 0`), so
the extremes sit at the window ends — cross-checked against brute force (CONTROL 6).

```text
     D      groups      min L      max L      min U      max U   killed by L>16
   105         264     0.0652     2.2857     4.3373    33.5404          0
   108         824     0.0469     2.8125     4.8485    38.6272          0
   112        1163     0.0833     3.3158     6.2921    41.3702          0
   117          60     0.0556     1.2632     3.6346    39.8212          0
   120        4104     0.0469     2.8125     3.4595    44.8000          0
   150        3556     0.0375     2.7692     2.4186    58.0080          0
   180       17344     0.0268     4.8214     4.6512    71.3443          0
   200       15174     0.0500     4.8214     3.4475    80.2346          0
  -------------------------------------------------------------------------
   D <= 120 (complete)   10 637 groups   min L = 3/64  = 0.04688    0 kills
   D in [101,200]       116 666 groups   min L = 3/112 = 0.02679    0 kills
   CALIBRATION: at D <= 100 this census yields 3 975 groups -- NOTT's branch-robust
   group count TO THE UNIT, from an independently written enumerator.
```

**No group anywhere is killed by `L > 16`, none by `U < 2`.** The two-sided *size*
window `[L,U]` is therefore not a filter: `L` is small and `U` large.

### 5.2 The filter that IS new: integrality

`N` is an integer, and D1-PIN says `N = sum_B V_2(B) q(B)` with `sum_B V_2(B) <= u`.
Writing `q = p/r` in lowest terms, a **single-branch** skeleton must have `r | V_2`,
and more generally the denominators must cancel across branches. On Moh's own six
published rows (CONTROL 5) the achievable sets are small and all nonempty:

```text
  row                      u       q   r    p    U = u q    achievable N (uniform branches)
  (64,48)                 12     3/4   4    3          9    3, 6, 9
  (84,56) M2=64,V2=2      21     2/7   7    2          6    2, 4, 6
  (84,56) M2=72,V2=5      21     1/2   2    1       21/2    1, 2, …, 10
  (75,50) V2=3            20     3/5   5    3         12    3, 6, 9, 12
  (75,50) V2=2            20     2/5   5    2          8    2, 4, 6, 8
  (99,66)                 24     2/3   3    2         16    2, 4, 6, …, 16
```
All four of Moh's survivors carry an achievable `N` inside the campaign's window; the
`(84,56)` `M_2 = 64` row is pinned to `N in {4,6}` under H2, and `(64,48)` to
`N in {6,9}`. **The integrality condition is nontrivial and Moh's survivors pass it**
— as they must, since they were killed only by his Appendix II elimination.

Two runs differ in one hypothesis. **(UNI)**: all bottom major discs carry the same
lower-`V` datum — true within one Galois orbit (the Galois action of `C((t))` is an
isometry of the tree, so it permutes bottom discs preserving `(a_1, delta_1)`), a
HYPOTHESIS when there is more than one orbit; then `N = k V_2 q` with `k V_2 <= u`.
**General**: `N = sum_B V_2(B) q(B)`, `sum_B V_2(B) <= u`, by exact knapsack over
`Fraction`s pruned to sums `<= 16` with a 60 000-state cap; capped groups are counted
as SURVIVING, so the reported kill is a FLOOR on the true kill.

```text
  (UNI), D <= 120 complete            (wall 1441 s incl. all controls, one core)
     V-assignments 902 893 : no integer N >= 2 achievable  891 820  (98.77%)
                             no integer N in [4,16] (H2)   893 706  (98.98%)
     groups 10 637        : every assignment dead, uncond    5 864  (55.13%)
                                                      H2     6 386  (60.04%)
  (UNI), MOH-SHARP-2 admissible D in [101,120] = {105,108,112,117,120}
     V-assignments 655 892 : killed uncond 648 696 (98.90%), H2 650 126 (99.12%)
     groups 6 415          : killed uncond   3 494 (54.47%), H2   3 860 (60.17%)
     per degree (groups / H2-killed)   105: 264/209   108:  824/419   112: 1163/795
                                       117:  60/47    120: 4104/2390
  GENERAL (no (UNI)), exact knapsack over Fractions, D in [48,79]
     groups 725 : KILLED 179 (24.7%) ; capped/UNDECIDED 46, counted as SURVIVING
     per degree  48: 50/9   54: 40/18   60: 110/23  63: 30/15  64: 84/16
                 66: 25/12  72: 316/56  75: 40/15   78: 30/15
     cost: 1317 s at D = 72 alone -- the knapsack is the cost, not the census, which
     is why the general run stops at 79 and the (UNI) run reaches 120.
  NO degree D is emptied in any of the three runs.
```

### 5.3 What dies, stated exactly

```text
 * NO degree D is emptied, at any range run.  MOH-SHARP-2's D_min >= 105 is neither
   improved nor weakened.
 * NO (B2) or (B3) cell dies.  The filter conditions Moh SKELETONS at a fixed D; a
   campaign cell (N,D) dies only if EVERY skeleton at that D fails for that N, and
   none does.  Case (A) untouched (EMPTY at every N).
 * What dies is the V-assignment (the branch datum).  A surviving skeleton now carries
   not the interval [2,U] for N but an explicit FINITE SET of achievable integers,
   typically of size 1-4.
 * The unconditional kill is nearly as strong as the H2 kill (98.77% vs 98.98% of
   V-assignments at D <= 120): the filter is arithmetic, not window-driven, and does
   NOT depend on the H2 residual.
```

## 6. Consequences, priced

```text
 A. OPEN[D1-SUBTREE] CLOSED, opposite to the charge's default.  The Jacobian
    condition below D_1 is an EQUALITY (JAC-FIBRE), forces the sub-tree to be a star
    (D1-STAR), and pins N|_{D_1} = a_1(1-delta_1)d/(d+e).  The OPEN's bounded quantity
    is not merely bounded: it is determined.
 B. NOTT's N-CEILING is ATTAINED (with sum_B V_2(B) for u), so FILTER-INVERSION is
    HALF RETRACTED: the skeleton does bound N below -- it determines it.  What
    survives is the operative point: the determined value is small at every degree, so
    "N <= 16" still rejects nothing by SIZE.  It now rejects by ARITHMETIC.
 C. OPEN[UPPER-TO-FLOOR] ANSWERED, split (§4): a floor exists and equals the ceiling;
    it is O(1), not Omega(D); no D <= C(N) follows.  The record should say that the
    boundary tree cannot produce the ceiling, and the reason is now a THEOREM about
    what the boundary tree computes, not a failure to find an instrument.
 D. NEW SEARCH CONDITION FOR MOH'S PROGRAM, condition (15), free to evaluate:
       q := d e K prod_{j=2}^{s} [V_j(n-M_j)-d_j]/[V_j(n-M_{j-1})-d_j]
       must admit  sum_B V_2(B) q(B)  integral, >= 2, with sum_B V_2(B) <= u.
    Strictly stronger than NOTT's condition (14) (u q >= 2), which it contains.
 E. PLACE-LEDGER GETS ITS LOCAL LAW.  At every proper place gamma of the generic
    fibre  m_gamma = nu_gamma (1 - delta^0_gamma)  with  1-delta^0 = (1-delta_1)d/(d+e),
    so m_gamma/nu_gamma is CONSTANT over the proper places of one bottom disc and
    N = (sum_gamma nu_gamma)(1-delta_1)d/(d+e).  This supersedes NOTT's
    RAMIFICATION-FLOOR by an EQUALITY: nu_gamma = m_gamma (d+e)/((1-delta_1)d).
 F. DC's OPEN[NU-BOUND-AT-A-PLACE] RETYPED AGAIN: neither floor nor ceiling but an
    exact ratio, nu_gamma/m_gamma = (d+e)/((1-delta_1)d), fixed by the skeleton.  A
    bound on nu_gamma is now equivalent to a bound on m_gamma, i.e. on N -- so the
    hoped T <= sum h(m_gamma) route remains closed, for a sharper reason than in NOTT.
 G. NOT GAINED.  No bound on T, Psi, D or D_min; no cell emptied; no statement about
    realisability of any skeleton; nothing about case (A), A2, Z(G), the reducible
    branch, or the source side.  MOH-SHARP-2 unchanged.  HARMONIC-BOUND (NOTT) is
    unaffected and remains 1/N > 1/deg P + 1/deg Q.
```

## 7. Corrections to charged inputs and to the record

```text
 C1. NOTT §4.2 "THEOREM RADIUS-ORDER (new)" -- NOT NEW.  It is Moh's Lemma 5.2
     (p.178, display ((n-L)/d_r)lambda* = -1+delta*), used again in the proof of
     Prop 6.1 (p.191, first display).  NOTT's derivation is correct and its
     verification on 242 099 V-skeletons stands; the NOVELTY claim is withdrawn.
     This matters for custody, not for content: it upgrades (RO) from PROPOSAL to
     PUBLISHED, and D1-PIN rests on it.
 C2. NOTT §4.5 "N|_{D_1} in [0, a_1(-lambda_f(delta_1))], attaining the bottom when
     the counts stay proportional to lambda_g = 0" -- REFUTED.  FRONTIER-EXACT forces
     c_rho = 1 - delta^0 > 0 for every rho in D_1 and D1-PIN forces the TOP of that
     interval.  The sub-tree is not a free bounded rational; it is pinned.
 C3. NOTT §6.1 FILTER-INVERSION, "unknown structure can only INCREASE contact and
     DECREASE N" -- HALF REFUTED.  Extra contact among the roots of g RAISES N
     (it lowers delta^0).  Extra contact between f-roots and g-roots below delta_1
     is not free: lambda_f(delta^0) = delta^0 - 1 is forced.  The conclusion
     ("N <= 16 rejects nothing") survives, but for the reason of §4, not this one.
 C4. NOTT DISCLOSURE (1) worried that DETECTOR-NULL rests on an unre-proved import
     (Prop 6.1(2)).  §3.5 proves it independently from Prop 6.1(1) and shows the
     (2)-route is safe only under Moh's printed r >= 2 MINOR hypothesis.
 C5. DEPTH-CEILING §3.1's recovery of Def 5.1(1)-(4) is CONFIRMED VERBATIM against
     p.179 (all four clauses, both products in (3)); Prop 5.3 (p.180) likewise.  Both
     are stated "for r >= 2"; the tower reaching D_1 is the r = 2 instance of
     Prop 5.3, whose conclusion asserts D_s ⊋ … ⊋ D_1 is again a tower of major discs.
 C6. MY OWN FIRST DRAFT of (JAC-ARC) claimed the inequality
     lambda_f + lambda_g <= delta - 1 characterises the Keller locus.  REFUTED by
     CONTROL T5: it holds for non-Keller pairs too, because ord_t J(sigma) <= 0 makes
     the general bound STRONGER.  Recorded because the correction is what forced the
     exact form (JF), which is the result.
```

## 8. Opens raised, with bounded quantities

```text
OPEN[BRANCH-ORBITS]  (new; the exact residue of this lane).  D1-PIN gives
   N = sum_B V_2(B) q(B) over the bottom major discs B.  BOUNDED QUANTITY: the number
   of Galois orbits of bottom major discs, an integer in [1, u], and the partition of
   sum_B V_2(B) <= u among them.  (UNI) -- one orbit -- turns the integrality filter
   from a 24.7% group kill into a 60.0% group kill (§5.2).  Is a degree-minimal
   counterexample forced to have ONE orbit?  Moh's remark that "the tree data
   associated with the configuration of the roots ... are completely symmetric"
   (p.150) is about the eta-tree and does NOT settle this.
OPEN[V-FLOOR]  (new; the exact residue of PIN-NOT-CEILING).  The ceiling D <= C(N)
   now needs a LOWER bound on the tower multiplicities.  BOUNDED QUANTITY: the
   integers V_j in (d_j/(n-M_j), V_{j+1}d_j/d_{j+1}], j = 2..s, at a degree-minimal
   counterexample; equivalently q = deK prod P_j/Q_j in (0, de(K-1)/(d+e)).  Does any
   Jacobian condition force q = Omega(1) or V_2 = Omega(K)?  Nothing in Moh
   (4.4/4.6/5.3, search (1)-(13)) or GGV (Thm 7.6, Prop 6.4/6.5/6.7, Thm 7.11) does.
OPEN[STAR-REALISABILITY]  (new; cheap, and a genuine test of D1-STAR).  D1-STAR
   predicts Moh's p(pi) at sigma_1 has a_1 = eV_2 SIMPLE roots.  BOUNDED QUANTITY: per
   surviving skeleton, the multiplicity multiset of p(pi) at level 1 (a partition of
   eV_2).  A skeleton whose Prop 4.6 data force a repeated root there is KILLED
   outright.  Not implemented (it needs Prop 4.6's construction, not its numerics).
OPEN[MOH-14] (NOTT), OPEN[MOH-ENDGAME], OPEN[NONPROPER-DEGREE],
   OPEN[SUBRECT-ORBIT-BRIDGE], OPEN[ANTICANON-DEFECT], OPEN[SAT-MASS],
   OPEN[DELTA-AFF-VS-N]: carried unchanged.
CLOSED: OPEN[D1-SUBTREE] (§3).  ANSWERED-SPLIT: OPEN[UPPER-TO-FLOOR] (§4).
RETYPED: OPEN[NU-BOUND-AT-A-PLACE] -- an exact ratio, not a bound (§6 F).
```

## 9. FALLACY-v2 audit

* **Flag/place/series.** Six degree-like integers separated by name (§0); the
  campaign's `n = deg Abar_F` does not occur. Three trees kept apart, each with its
  own theorem: the **`eta`-adic** exponent tower (`{M_i,d_i}`, Lemma 2.1 — the
  Jacobian condition there is an identity in the *wrong variable* for this question,
  §3.4), the **`t`-adic major tower** (Def 5.1, Lemma 5.2), and the **sub-tree of
  `D_1`** (JAC-FIBRE). `T_1^psi = f + const` vs `f` is declared, and the level at
  which the distinction is harmless (`lambda_f < 0`) is proved, not assumed.
* **Per-ray/exit-set charge.** No exit price, no `charge_basis` line. Each root of
  `g - c_2` is charged once at its own frontier; the bottom major discs are disjoint
  subsets of `D_{s-1}` and each `g`-root is counted once; the covering "minor discs +
  bottom major discs" is exhaustive because every subdisc of a tower disc is major
  (continues the tower) or minor (Prop 6.1), and a tower halting above level 1 leaves
  its roots in minor discs, contributing 0.
* **Carrier/attainment; floor/attainment.** The result IS an attainment claim, so it
  is proved twice from opposite sides and the closed form of the gap
  `(1-delta_r)(-M_r-m)/(n-M_r)` is exhibited and verified on 40 001 skeletons. `L` and
  `U` are used only as bounds, never as values; `min L = 3/112` is MEASURED over an
  enumerated finite set with no claim beyond the range run; the knapsack's capped
  groups are counted as SURVIVING, so its kill is a floor.
* **Pole/interior.** `(star)` is used only where `g_y(tau) != 0` and `f(tau)` is
  nonconstant (both argued). `ord F' = ord(F-a_0)-1` is the char-0 branch and the
  `a_0` subtraction is carried explicitly — it is exactly the proper/non-proper split.
* **Prime label/derivative; variable/ring map.** `g_y` is a genuine partial derivative
  (Moh's notation); `T_r` vs `T_r^psi`, `p(pi)` vs `p'(pi)`, and Moh's `delta*_{r-1}`
  (minor) vs `delta_{r-1}` (major) are distinguished. All CAS is exact over `Q` with
  symbolic `c_1,c_2`; Puiseux orders are `Fraction`s from Newton polygons w.r.t.
  `ord_t` (`ord_t x = -1`) — a convention that was **wrong by a sign in the first run
  and caught by the controls** (every predicted `-1` came out `+1`); the fix is
  recorded in the driver docstring. No saturation, Groebner basis or normal form.
* **OCR discipline; no cap or analogy.** Every load-bearing statement of Moh is read
  from the **page image** with its PDF page number (§0); the OCR is used only to
  locate. NOTT's two OCR corrections are not used and are neither confirmed nor
  disputed. Where the branch structure is unknown the hypothesis (UNI) is named, the
  filter is run with and without it, and the hypothesis-free number is the operative
  one.

## 10. Typed verdict block

```text
LANE       D1-SUBTREE  (successor OPEN[D1-SUBTREE] of N-ON-THE-TREE)
SCOPE      Keller, noninvertible, degree-minimal, Moh's gauge (GEN, NU-TWO).
           JAC-FIBRE (general ord_t J form) and FRONTIER-EXACT hold for every
           dominant F in that gauge; D1-PIN and D1-STAR additionally use Moh
           Def 5.1(1), Lemma 5.2, Prop 6.1(1), all read firsthand from the page
           images.  Case (A) EMPTY and untouched; A2 untouched; no Z(G)=1.  H2 only
           where the campaign window is quoted, marked at every use.

PROVED HERE  (all PROVED-HERE, UNREVIEWED)
 JAC-FIBRE [3.1]  ord_t(f(tau)-a_0) + ord_t g_y(tau) = -1 + ord_t J(tau) on every
     branch of every generic fibre; = -1 for a Keller pair.  Exact identity (star).
 FRONTIER-EXACT [3.2]  N = sum_rho (1-delta^0_rho)^+ ; equivalently
     lambda_f(delta^0) = delta^0 - 1 exactly, and delta^0 >= 1 iff non-proper.
 DETECTOR-NULL [3.5]  second proof, from Prop 6.1(1); the scope of Prop 6.1(2)
     pinned by the N = 0 contradiction.
 D1-PIN [3.6]  floor(r) - ceiling(r) = (1-delta_r)(-M_r-m)/(n-M_r), zero iff r = 1;
     c_rho = m(1-delta_1)/(n+m) and N = sum_B V_2(B) q(B), q = (1-delta_1)de/(d+e).
 D1-STAR [3.7]  the sub-tree of D_1 is a star; p(pi) at level 1 has a_1 simple roots.
 PIN-NOT-CEILING [4]  the pinned value is O(1), not Omega(D); no D <= C(N) follows.
 PLACE LAW [6 E]  m_gamma = nu_gamma (1-delta_1)d/(d+e) at every proper place.

MEASURED   jacfibre.py 101 + treecheck.py 151 checks (9 genuine Keller pairs to
           D = 8; 24 non-Keller negative rows) + d1floor.py 232 384 controls; 0
           failures anywhere.  Census calibrated to NOTT to the unit (3 975 groups at
           D <= 100).  Filter: no degree emptied; integrality kills 60.0% of groups
           under (UNI) at D <= 120 and 24.7% without it at D <= 79; the floor
           min L = 3/112 at D <= 200 does not grow with D.
DECISION   THE JACOBIAN CONDITION BELOW D_1 IS AN EQUALITY AND IT PINS N.  The one
           place the record had never imposed it is now the one place where the
           boundary tree is EXACT.  OPEN[D1-SUBTREE] CLOSED; OPEN[UPPER-TO-FLOOR]
           ANSWERED-SPLIT (floor yes, ceiling no); successors OPEN[BRANCH-ORBITS],
           OPEN[V-FLOOR], OPEN[STAR-REALISABILITY].
CORRECTED  NOTT's RADIUS-ORDER novelty claim (it is Moh Lemma 5.2); NOTT's
           "N|_{D_1} can reach 0" (refuted); half of FILTER-INVERSION's mechanism;
           my own first (JAC-ARC) claim, refuted by its own negative control.
CONFIRMED  DC's page-image recovery of Def 5.1(1)-(4) and Prop 5.3, VERBATIM.  NOTT's
           DETECTOR-NULL, by an independent route.  NOTT's N-CEILING, now ATTAINED.

DISCLOSURE (1) The controls are on POLYNOMIAL AUTOMORPHISMS -- no noninvertible
               Keller pair exists to test on.  They have s = 1, M_s = n-1, so they sit
               outside Def 5.1(3); they test JAC-FIBRE, FRONTIER-EXACT, the intrinsic
               delta_1, the floor/ceiling coincidence and D1-STAR -- all but the
               numerical form of delta_1, tested separately in CONTROL 1.
           (2) D1-PIN's CEILING half imports Moh Def 5.1(1) at level 1 (verified
               independently on the automorphisms, CONTROL T).  If it failed, the
               FLOOR half (JAC-FIBRE + slope >= 1) would survive unchanged and
               D1-STAR would be lost.
           (3) sum_B V_2(B) <= u uses NU-TWO and disjointness; Moh's search (8)-(11)
               would sharpen it and was NOT implemented.  Sharpening lowers
               sum_B V_2(B), so the reported kills are a floor.
           (4) (UNI) is a HYPOTHESIS, named; the hypothesis-free knapsack is the
               operative number.  No box01 job; the run is desk-scale.
           (5) SIZE: body 45.3 KB against the charged 25-40 KB band.  The overrun is
               the verbatim source quotation (§0 page list, §2.2 Def 5.1/Lemma 5.2),
               the three proofs of §3, and the three measured filter tables of §5,
               kept complete rather than compressed.
```

<!-- BODY-END -->
