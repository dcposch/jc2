# EXACT-N — the dictionary is right, the squeeze closes, `D_1` **is** a star, and `OPEN[D1-SUBTREE]` is EMPTY; but `A_bot` is not a skeleton function, so `EXACT-N` is a two-sided window plus an integrality condition, not a closed form

Lane: `EXACT-N` (flagship, hostile; successor of `OPEN[D1-SUBTREE]` and
`OPEN[UPPER-TO-FLOOR]` of N-ON-THE-TREE). Date: 2026-09-02. Agent: Opus 5.
Desk derivation + desk-scale CAS (python3 3.14.7 / sympy 1.14.0 over `Q`;
no Singular, no AWS, no web, no fetching, no box01). Drivers in
`box/exactn-drivers-20260902/`.

## 0. Custody, method, scope

The five charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all five match the charge. Sources read firsthand:

```text
6c8847a8...  refs/moh1983_jram340_configurations_of_roots.pdf
b6a36914...  box/depth-drivers-20260902/moh.txt   (pdftotext -layout; MOH:line below)
30220204...  box/moh_skeleton_N.py                (reviewed instrument, consumed unedited)
8081141a...  box/exactn-drivers-20260902/dictionary.py    (STEP 1, three ways)
6ccfd788...  box/exactn-drivers-20260902/treestar.py      (D1-STAR on Keller pairs)
b0df9348...  box/exactn-drivers-20260902/noresidue.py     (the charge's "no log" question)
d1f3529f...  box/exactn-drivers-20260902/exactn.py        (Phi controls + the filter)
```

Consumed as **reviewed**: CONTACT-DEFICIENCY, FRONTIER-N, RADIUS-ORDER *in the
`M_s = n-2` scope*, DETECTOR-NULL, N-CEILING (upper), MOH-SHARP-2, NU-TWO —
all as promoted by the Grok hostile review and integration #16. `N_min = 6` is
integration #16 delta (a). Everything else in this report is
**PROVED-HERE / MEASURED-HERE, UNREVIEWED**. No canonical ledger edited;
`jc2-lean` not inspected; nothing fetched. **No `charge_basis` line: this report
asserts no new exit price.**

Six degree-like integers kept apart throughout (§12): Moh's `n = deg_y g = D`,
`m = deg_y f`; `K = gcd(m,n)`, `m = Kd`, `n = Ke`; the campaign's geometric
degree `N`; the campaign's source-side `n = deg Abar_F` (absent here); Moh's
`d_i`; the exponent `d` of `l(P) = alpha H^d`.

**Notation.** `t = x^{-1}`, `ord_t` the Puiseux valuation on `C<t>`,
`lambda_h^{(sigma)}(delta) = sum_j min(delta, ord_t(sigma - h_j))` over the roots
`h_j` of `h` (`= ord_t h(sigma_delta)` at Moh's general `pi`-root, Prop 1.2),
`a(delta), b(delta)` the numbers of `g`- and `f`-roots in the ball of radius
`delta`, `delta^0` the `g`-frontier (`lambda_g = 0`), `delta_i` the radius of the
major disc `D_i`, `M_1 = -m` (MOH:2527), `M_s = n-2`.

## 1. Verdict, up front

```text
(1) NO FLAW IN THE MATHEMATICS OF STEPS 1-4.  All four steps CONFIRM, with two
    corrections to the reasoning as written (C1, C2) and three to the conclusions
    (C3-C5).  The squeeze closes.  THEOREM D1-STAR (sec.5) and THEOREM EXACT-N
    (sec.7) are stated with exact hypotheses.
(2) THE RIGHT OBJECT IS ONE FUNCTION.  Put  Phi(delta) := delta - lambda_f(delta)
    - lambda_g(delta)  along a root of g.  Its slope is 1 - a - b <= 0, so Phi is
    NON-INCREASING; the Keller identity gives Phi(delta^0) >= 1 at every
    frontier (LEMMA DICT); RADIUS-ORDER at r = 1 with M_1 = -m gives
    Phi(delta_1) = 1 EXACTLY.  Hence Phi == 1 on [delta_1, delta^0], hence
    a + b == 1 there: D_1 IS A STAR.  All four charged steps are this one
    sandwich; STEP 2 is "Phi(delta^0) <= Phi(delta_1)" and STEP 3 is the same
    inequality read on lambda_f.
(3) THE r = 1 IDENTITY IS NOT A COINCIDENCE AND NOT AN ARTEFACT.  Grok sec.4.3's
    "banked algebraic coincidence" IS  Phi(delta_1) = 1, i.e. RADIUS-ORDER at r = 1
    composed with lambda_f = (m/n)lambda_g; its content is n - M_1 = n + m =
    #roots of f*g.  Moh does NOT define delta_1 by termination: Prop 5.3 defines
    delta_{r-1} GEOMETRICALLY (MOH:2163-2167) and PROVES the Def 5.1(3) formula,
    and the search computes "the radii delta_s,...,delta_1 ... from Definition 5.1"
    (MOH:3284-3286).  Independently, Phi(delta_1) = 1 is VERIFIED on four explicit
    Keller pairs straight from the joint f*g tree (sec.6(c)).  The star is new.
(4) OPEN[D1-SUBTREE] IS CLOSED, AND IT IS EMPTY.  Its bounded quantity
    N|_{D_1} in [0, a_1(-lambda_f(delta_1))] is pinned to its TOP: D_1 splits into
    a_1 + b_1 SINGLETONS at delta_1, so Moh's recursion stops there because nothing
    is left below.  FILTER-INVERSION's premise ("unknown structure can only lower
    N") is REFUTED at D_1.  COROLLARY MINOR-FRONTIER: every g-root of a minor disc
    has delta^0 > 1.
(5) BUT A_bot IS NOT A FUNCTION OF THE SKELETON, so STEP 4(iii)/(iv) and the
    charge's (c) are OVERSTATED.  What is exact is
        N = sum over bottom-major discs D_1^(k) of a_1^(k) d(1-delta_1^(k))/(d+e),
    with sum_k a_1^(k) =: A_bot <= a_{s-1} = ue.  The NUMBER of bottom-major discs
    is free, and that is realised, not feared: the Keller pair
    (x+y^5, y+(x+y^5)^3) has FIVE conjugate D_1's with a_1 c = 1/5 = N/5.  So
    EXACT-N delivers a FLOOR L = a_1 c (new; it INVERTS FILTER-INVERSION) with the
    reviewed ceiling U = ue c, plus an INTEGRALITY condition -- not a closed form.
(6) MEASURED, D <= 140 (18 064 groups, 345 s one core).  The floor never fires
    (max L = 3.32 to D <= 190); the INTEGRALITY does: U < 6 kills 697 (3.9%),
    EXACT-N MIXED (unconditional) 5 275 (29.2%), EXACT-N SINGLE 11 992 (66.4%);
    at D <= 190 SINGLE kills 49 623 of 76 282 (65.0%).  NO degree is emptied,
    the MOH-SHARP-2 degrees {105,108,112,117,120} included.
(7) COROLLARY NO-RESIDUE answers the charge's "automatic or a constraint": the
    x^{-1} coefficient of d/dx f(x,tau) vanishes for ANY Puiseux series, with no
    hypothesis; so on a Keller pair the x^{-1} coefficient of 1/g_y(x,tau)
    vanishes on every branch of every fibre -- a NECESSARY CONDITION ON g ALONE.
    Negative control: g = y^2 - x^2 - x has [x^{-1}] = +-1/2 and delta^0 = 1.
```

## 2. STEP 1 — the dictionary. **CONFIRMED**, with the integration step replaced

The charge asks: *"the dictionary's integration step (no log: the `x^{-1}`
coefficient of `1/g_y(tau_i)` must vanish — is that automatic or a constraint?)"*.
The question is well aimed but mis-directed: **do not integrate**. The identity
runs forward, and then no log can arise because nothing is integrated.

> **LEMMA DICT (proved here).** Let `g in C[x,y]` be monic in `y` with
> `deg_y g = n >= 1`, let `J := [f,g] = f_x g_y - f_y g_x in C^*`, fix `c_2 in C`
> and let `tau in C<t>` be a root of `g - c_2` with `g_y(x,tau) != 0`. Put
> `lambda := ord_t f(x,tau(x))` and `delta^0 := -ord_t g_y(x,tau(x))`. Then
> ```text
>   (i)   lambda != 0   ==>   delta^0 = lambda + 1 ;
>   (ii)  lambda  = 0   ==>   f(x,tau) = c_0 + c_1 t^{e_1} + ... with 0 < e_1 < oo
>                             and delta^0 = e_1 + 1 > 1 .
> ```
> In both cases `max(0,-lambda) = (1 - delta^0)^+`, and **`delta^0 = 1` is
> impossible**.

*Proof.* `g(x,tau(x)) = c_2` identically, so `g_x + g_y tau' = 0`, so
`tau' = -g_x/g_y`, so
```text
      d/dx [ f(x,tau(x)) ]  =  f_x + f_y tau'  =  (f_x g_y - f_y g_x)/g_y  =  J/g_y(x,tau) ,
```
whose `ord_t` is `0 - ord_t g_y(tau) = delta^0`. On the other side
`h := f(x,tau(x)) in C<t>`, and `d/dx = -t^2 d/dt`, so for `h = sum_a c_a t^a`,
`d/dx h = -sum_a a c_a t^{a+1}`. If `lambda != 0` the leading term survives and
`ord_t(dh/dx) = lambda + 1`: that is (i). If `lambda = 0` then `h` is not constant
(a constant would give `dh/dx = 0 != J/g_y`), so `e_1 := ord_t(h - c_0) in (0,oo)`
and `ord_t(dh/dx) = e_1 + 1`: that is (ii). `delta^0 = 1` forces `lambda = 0` in
case (i) and `e_1 = 0` in case (ii); both contradictions. ∎

> **COROLLARY NO-RESIDUE.** For **any** Puiseux `h`, `d/dx h` has **zero**
> `t^1 = x^{-1}` coefficient (the `a = 0` term is annihilated). Hence on a Keller
> pair the `x^{-1}` coefficient of `1/g_y(x,tau)` vanishes for every simple
> branch of every fibre `g = c_2`. **Automatic on the `f` side; a genuine
> constraint on the `g` side** — a necessary condition for `g` to be a Keller
> coordinate, involving `g` only.

MEASURED (`noresidue.py`, `noresidue.log`): `[x^{-1}] 1/g_y(tau) = 0` for
`g = x + y^5` and `g = x + y^2 + y` (coordinates), and `= +-1/2 != 0` for the
non-coordinates `g = y^2 - x^2 - x` and `g = y^2 - x^2 - 5x + 2`, both of which
have `delta^0 = 1` exactly — the case LEMMA DICT forbids. A third row,
`g = y^2 - x^3 - x^2`, is reported **vacuous**: its exponent lattice is
`(1/2)Z`, so `x^{-1}` is not in it and the test cannot fire.

### 2.1 The tree step, and the shifted-tree contact formula

> **LEMMA SHIFT (proved here from reviewed FRONTIER-N).** For generic `c_2` and
> every root `rho_i` of `g` with frontier `delta^0_i`,
> ```text
>     ord_t g_y(x,tau_i)  =  sum_{j != i} ord_t(tau_i - tau_j)
>                         =  lambda_g^{(i)}(delta^0_i) - delta^0_i  =  -delta^0_i ,
> ```
> i.e. the `delta^0` of LEMMA DICT **is** the frontier of the *unshifted* `g`-tree.

*Proof.* `(g-c_2)_y = g_y` and `g - c_2 = prod_j(y - tau_j)` is monic, so
`g_y(x,tau_i) = prod_{j != i}(tau_i - tau_j)`. FRONTIER-N's proof (reviewed): the
`a(B)` roots of `g - c_2` in the frontier ball `B = B(rho_i, delta^0_i)` follow the
`g`-tree down to `delta^0_i` and separate there **pairwise at exactly `delta^0_i`**,
contributing `(a(B)-1)delta^0_i`. A root outside `B` has contact
`ord_t(rho_i - rho_{j'}) < delta^0_i` and — by the sub-lemma — also `< delta^0_{j'}`,
so both branches still track their `g`-roots there and the contact is unchanged by
the shift. Summing gives `lambda_g^{(i)}(delta^0_i) - delta^0_i = -delta^0_i`.
*Sub-lemma:* `ord_t(rho_i-rho_j) < delta^0_i` implies `< delta^0_j`. Otherwise
`delta^0_j <= ord_t(rho_i-rho_j)`, and at every radius `<= ord_t(rho_i-rho_j)` the
two roots share a ball, so `lambda_g^{(i)} = lambda_g^{(j)}` there; at `delta^0_j` this gives
`lambda_g^{(i)}(delta^0_j) = 0`, and the frontier is unique (slope `>= 1` where
`lambda <= 0`), so `delta^0_i = delta^0_j` — contradiction. ∎

> **THEOREM DICT-N.** For a dominant Keller pair with `f, g` monic in `y` and
> `deg_x Res_y(f-c_1,g-c_2) = N` (Moh's gauge suffices), and generic `(c_1,c_2)`,
> ```text
>       N  =  sum_{i=1}^{n} ( 1 - delta^0_i )^+ ,
> ```
> a function of the **unshifted `g`-tree alone**.

*Proof.* FRONTIER-N (reviewed): `N = sum_i max(0, -lambda_f^{(i)}(delta^0_i))`.
LEMMA SHIFT identifies its `delta^0_i` with LEMMA DICT's; LEMMA DICT converts each
term. ∎

### 2.2 Controls on STEP 1 (`dictionary.py`, `dictionary.log`; 64 checks, 0 failures)

The multisets `{ord_t f(tau_i)}`, `{ord_t g_y(tau_i)}`, `{ord_t J(tau_i)}` are read
**root-free** off the Newton polygons of `Res_y(z-h, g-c_2)` for `h = f, g_y, J`
(exact rational slopes; the upper hull of `(k, deg_x c_{n-k})`).

```text
 CONTROL A (8 IN-GAUGE Keller pairs, J in C^*, up to (m,n) = (6,12)):
   lambda_i + 1 = delta^0_i on every branch, and DICT-N = FRONTIER-N = N(res) = 1
   on every row, including the depth-3 composite
   (y+(x+y^3)^2, (x+y^3)+(y+(x+y^3)^2)^2).
 CHARGED CONTROL (y+x^2, x+(y+x^2)^2), Jacobian -1, OUT of the gauge
   (deg f = 2 > deg_y f = 1, deg g = 4 > deg_y g = 2):  delta^0 = 1/2 on both
   branches -- so delta^0 != 1 as the charge asks -- and DICT-N = 1 = N.  The
   gauge is SUFFICIENT, not necessary, for DICT-N; LEMMA DICT uses only "g monic
   in y".
 CONTROL B (NEGATIVE, load-bearing):  the seven non-Keller two-tower rows of
   N-ON-THE-TREE CONTROL 1.  DICT-N = 0 on ALL SEVEN while N(res) = 4, 9, 13, 9,
   12, 18, 18.  The dictionary fails off the Jacobian condition by the whole of N.
 CONTROL B2 (the exact deficit):  sum_i ord_t f(tau_i) + n = -sum_i ord_t g_y(tau_i)
   + sum_i ord_t J(tau_i) on all 16 rows, 0 failures.  This is LEMMA DICT summed
   with the J-term restored -- exactly Grok's Res_y(J,g) check, and it is what
   fails on the non-Keller rows.
 CONTROL C:  LEMMA SHIFT against closed-form Puiseux roots on all seven two-tower
   rows: the unshifted-tree frontier equals -ord_t g_y(tau).  0 failures.
 CONTROL C2 (discriminating):  g = h^2, h = (y-x)^2 - 7x -- g-roots are h's two
   roots each DOUBLED, so the frontier ball has a(B) = 2 and splitting radius
   +oo > delta^0 = 1/2.  Generic c_2 gives -ord_t g_y(tau_i) = 1/2 on all four
   branches; at c_2 = 0 it degenerates.  The c_2-shift is LOAD-BEARING and LEMMA
   SHIFT is not an artefact of singleton frontier balls.
 CONTROL D:  {delta^0_i} is the same for three generic c_2 on six Keller rows.
```

**Correction to STEP 1 as written (C1).** "integrating in `x` (no log term can
occur because `f(x,tau_i(x))` is a Puiseux series)" inverts the logic and misplaces
the reason. Run it forward. The real dichotomy is `lambda != 0` versus
`lambda = 0`; the proposal's clause "`f` has a finite limit when `delta^0_i > 1`"
is then not an alternative *conclusion* but the second *case*, in which
`delta^0 = e_1 + 1` and the relation `delta^0 = lambda + 1` FAILS. The stated
conclusions — the pole is `1 - delta^0`, `delta^0 > 1` is non-proper,
`delta^0 = 1` is impossible — are all correct.

## 3. STEP 2 — the frontier bound. **CONFIRMED** (and it is one half of `Phi`)

`lambda_g^{(i)}` is nondecreasing with slope `a^{(i)}(s) >= 1` (the root `rho_i`
counts itself), so for `rho_i` in a bottom-major disc `D_1`,
`0 = lambda_g^{(i)}(delta^0_i) >= lambda_g(delta_1) + (delta^0_i - delta_1)`, i.e.
```text
      delta^0_i  <=  delta^0_star := delta_1 - lambda_g(delta_1) ,
```
with equality **iff** `a^{(i)}(s) = 1` for every `s in (delta_1, delta^0_i]`, i.e.
iff `rho_i` is alone in every ball of radius `> delta_1`. Exactly as charged.
(`delta^0_i > delta_1` because `lambda_g(delta_1) < 0`; RADIUS-ORDER makes that
equivalent to `delta_1 < 1`, MEASURED on all 242 099 `V`-skeletons at `n <= 100`.)

## 4. STEP 3 — the N-CEILING density. **CONFIRMED** (reviewed input, in scope)

For `rho_i in D_1`, `lambda_f^{(i)}` is nondecreasing and `delta^0_i >= delta_1`, so
```text
      -lambda_f^{(i)}(delta^0_i)  <=  -lambda_f(delta_1)  =  (d/e)(-lambda_g(delta_1))
                                  =  d(1-delta_1)/(d+e) ,
```
using (i) Def 5.1(1)'s `j = 1` clause `b_i/a_i = m/n` **at every level of the major
chain** (`T_1^psi = f`, Moh's own nonrestrictive normalisation, MOH:3257), which gives `lambda_f(delta) = (m/n)lambda_g(delta)` for all
`delta <= delta_1` because the counts are constant on `(delta_{i+1}, delta_i]`
(Moh's `delta_i` is the *splitting* radius of `D_i`: Prop 5.3 defines `D_{r-1}` as
"the minimal disc containing all roots ... with `ord(tau - tau_i) > delta_r`",
MOH:2163-2167, and Def 1.1's logarithmic radius of a minimal disc is
`min_{i,j} ord_t(tau_i - tau_j)`), and (ii) RADIUS-ORDER at `r = 1`,
`lambda_g(delta_1) = -n(1-delta_1)/(n - M_1) = -e(1-delta_1)/(d+e)` with
`M_1 = -m` (MOH:2527: "`M_1 = mu_1 = - deg_y T_1^psi`"), `n+m = K(d+e)`, `n = Ke`.
This is precisely the reviewed N-CEILING computation.

**Scope, as charged.** RADIUS-ORDER is reviewed only for `M_s = n-2`
(`n - M_s - 1 = 1`): the NU-TWO scope, and exactly where Moh's own analysis lives
(MOH:3253-3255). `M_1 = -m` is Moh's own. **Outside contributions are included**,
not neglected: `lambda_h(delta) = -deg h + int_{-1}^{delta}(count) ds` integrates
from `delta = -1`, where the ball is everything, so the two slope classes at level
`s` (carrying `(ue,ud)` and `(ve,vd)`) enter with their proportional counts; the
proportion is `m/n` at every level *including* the top, because
`l(f) = alpha H^d`, `l(g) = beta H^e` share `H` ((LF)).

## 5. STEP 4 — the squeeze. **CONFIRMED**, and it is one monotone function

Combining §3 (`1 - delta^0_i >= (1-delta_1) + lambda_g(delta_1)`), §4
(`-lambda_f^{(i)}(delta^0_i) <= d(1-delta_1)/(d+e)`), §2 (`-lambda_f^{(i)}(delta^0_i)
= 1 - delta^0_i` when `lambda != 0`), and the arithmetic identity
`(1-delta_1) + lambda_g(delta_1) = d(1-delta_1)/(d+e)`, all four inequalities
collapse. The clean way to see it — and the way that shows STEPS 2 and 3 are the
*same* inequality — is:

> **DEFINITION.** Along the path of a root `rho` of `g` (or of `f`), put
> ```text
>       Phi(delta)  :=  delta  -  lambda_f(delta)  -  lambda_g(delta) .
> ```
> `Phi` is continuous, piecewise linear, and depends only on the ball of radius
> `delta` containing `rho`. Its slope is `1 - a(delta) - b(delta) <= 0` because
> `a >= 1` and `b >= 0`: **`Phi` is non-increasing along every path**.

> **LEMMA Phi-DICT (Keller).** `Phi(delta^0) >= 1` at every `g`-frontier, with
> equality iff `lambda_f(delta^0) != 0`.
> *Proof.* `lambda_g(delta^0) = 0`, so `Phi(delta^0) = delta^0 - lambda_f(delta^0)`.
> If `lambda := lambda_f(delta^0) != 0`, LEMMA DICT(i) gives `delta^0 = lambda+1`,
> so `Phi(delta^0) = 1`. If `lambda = 0`, LEMMA DICT(ii) gives
> `Phi(delta^0) = delta^0 = e_1 + 1 > 1`. ∎

> **LEMMA Phi-TOWER.** On Moh's major tower,
> `Phi(delta_r) = delta_r + (n+m)(1 - delta_r)/(n - M_r)`. Hence
> ```text
>       Phi(delta_1) = 1  EXACTLY   (M_1 = -m, so n - M_1 = n + m),
>       Phi(delta_r) > 1  strictly for r >= 2   (M_r > -m).
> ```
> *Proof.* RADIUS-ORDER plus `lambda_f = (m/n)lambda_g` (§4). ∎

**MEASURED (`exactn.py`, CONTROL P1/P2):** `Phi(delta_1) = 1` on Moh's six
published rows and on **all 242 099 `V`-skeletons with `n <= 100`**, 0 failures;
`Phi(delta_r) > 1` for `r >= 2` and `Phi` non-increasing down the tower on all of
them, 0 failures; the incremental and closed forms of `Phi` agree everywhere.

> **THEOREM D1-STAR (proved here; UNREVIEWED).**
> *Hypotheses.* Moh's gauge; `[f,g] in C^*`; characteristic data with `M_1 = -m`,
> `M_s = n-2` (NU-TWO) and a tower `D_s ⊋ ... ⊋ D_1` satisfying Def 5.1(1)–(3);
> `lambda_g(delta_1) < 0` (equivalently `delta_1 < 1`).
> *Conclusion.* `D_1` is a **STAR**: its `a_1 = (n/d_2)V_2` `g`-roots and
> `b_1 = (m/d_2)V_2` `f`-roots are pairwise at contact **exactly** `delta_1`, and no
> proper sub-ball of `D_1` contains two of them. Consequently every `g`-root of
> `D_1` has
> ```text
>      delta^0 = delta_1 - lambda_g(delta_1) < 1 ,
>      contribution to N  =  -lambda_f(delta_1)  =  d(1-delta_1)/(d+e)  =: c  >  0 .
> ```
>
> *Proof.* Let `rho` be a `g`-root of `D_1`. `Phi(delta_1) = 1` (Phi-TOWER),
> `Phi(delta^0_rho) >= 1` (Phi-DICT), `delta^0_rho > delta_1` (§3), `Phi`
> non-increasing. Hence `Phi == 1` on `[delta_1, delta^0_rho]`, so its slope
> `1 - a - b` vanishes there: `a == 1`, `b == 0`, i.e. `rho` separates from every
> other root of `f*g` at radius exactly `delta_1`. Then
> `lambda_g^{(rho)}(delta) = lambda_g(delta_1) + (delta - delta_1)` gives
> `delta^0_rho = delta_1 - lambda_g(delta_1)`; and `b == 0` on the interval gives
> `lambda_f(delta^0) = lambda_f(delta_1)`, so `Phi(delta^0) = 1` reads
> `1 - delta^0 = -lambda_f(delta_1) > 0`. For an `f`-root of `D_1` use the mirror
> dictionary `d/dx g(x,phi) = -J/f_y(x,phi)` (`f` monic in `y`) at the `f`-frontier,
> which exceeds `delta_1` because `lambda_f(delta_1) = (m/n)lambda_g(delta_1) < 0`;
> the same `Phi` gives `a == 0`, `b == 1` above `delta_1`. ∎

**What each hypothesis buys.** The dictionary alone gives `Phi(delta_1) >= 1`;
Moh's Def 5.1(3) supplies only the *reverse* inequality `Phi(delta_1) <= 1`. So
half of RADIUS-ORDER at `r = 1` is forced by the Jacobian condition independently
of Moh's recursion — a cross-check on the recovered Def 5.1(3) the record did not
have.

> **COROLLARY D1-SUBTREE-EMPTY.** `OPEN[D1-SUBTREE]` is CLOSED. Its bounded
> quantity `N|_{D_1} in [0, a_1(-lambda_f(delta_1))]` is pinned to the TOP of the
> interval, `N|_{D_1} = a_1 c`. There is no free datum below `delta_1` at all.
> Moh's recursion terminates at `D_1` because `D_1` has no sub-tree, not merely
> because his minor criterion degenerates there.

> **COROLLARY MINOR-FRONTIER.** Every `g`-root of a minor disc has `delta^0 > 1`.
> *Proof.* DETECTOR-NULL (reviewed) gives `lambda_f(delta^0) = 0`; LEMMA DICT(ii)
> then gives `delta^0 = e_1 + 1 > 1`. ∎
> *Consistency (MINOR-GAP).* No ball `B` inside a minor disc can have `Phi(B) = 1`
> with `lambda_g(B) < 0`: it would be a star and its `g`-roots would contribute
> `-(m/n)lambda_g(B) > 0`, contradicting DETECTOR-NULL. This is **forced, not
> assumed**: Moh's Prop 6.1 gives `delta*_{r-1} >= 1` for *every* minor disc
> (MOH:2844), whence `Phi(B) = delta(B) + (n+m)(-lambda_g(B))/n > 1` there. Closed
> form at the top minor class: `Phi(delta*_{s-1}) = delta* + (d+e)(u - delta* v)`,
> which exceeds `u/v > 1` on the whole range `delta* < u/v` where
> `lambda_g(delta*) < 0`; at `delta* >= u/v` the frontier is `delta^0 = u/v > 1`
> with `lambda_f(delta^0) = 0` — DETECTOR-NULL reproved by hand at level `s`.

## 6. Is `Phi(delta_1) = 1` an artefact of how Def 5.1(3) *defines* `delta_1`? **No.**

**(a) Moh does not define `delta_1` by termination.** Prop 5.3 defines it
geometrically — "`delta_{r-1}` = the logarithmic radius of `D_{r-1}` which is the
minimal disc containing all roots `tau_i` of `g(y)prod T_i^psi(y)` with
`ord(tau - tau_i) > delta_r`" (MOH:2163-2167) — and then *proves* the Def 5.1(3)
formula for it (MOH:2179 ff.). The search uses it at `i = 1`: "the radii
`delta_s, ..., delta_1` of `D_s, ..., D_1` can be computed from Definition 5.1"
(MOH:3284-3286). So `delta_1` is a geometric radius and Def 5.1(3) is a theorem
about it, derived through Props 4.4/4.6 from the Jacobian condition.

**(b) Moh nowhere asserts the star.** His Theorem (4)–(7) (MOH:3234-3252) covers
`D_r` for `r >= 2` only, and his own summary of what is missing is the *blur*:
"we only get an estimate `delta*_1 >= 1` ... all roots in the disc `D*_{r-1}` ...
are indeed proportional to the `y`-degrees ... up to the uncertainty of `2^0 = 1`"
(MOH:2874-2884). The structure of `D_1` is not among his conclusions.
**THEOREM D1-STAR is new.**

**(c) Independent verification on real Keller pairs, with no recursion used.**
`treestar.py` computes the **whole joint `f*g` tree root-free**: the `w`-roots of
`Res_y(g(x,y), h(x,y+w))` are exactly the differences `{h_j - g_i}`, so the Newton
polygon in `w` yields the full multiset of ultrametric distances. On the four
Keller pairs below every root of `g` is Galois-conjugate to every other (one place
at infinity), so the aggregate profile divided by `n` is the per-root profile and
the tree is determined. 28 checks, 0 failures (`treestar.log`):

```text
  pair                    m   n   per-g-root contacts   per-g-root f-contacts
  (y, x+y^5)              1   5   (-1/5)^4              (-1/5)
  (x+y^3, y+(x+y^3)^2)    3   6   (-1/3)^4, (1/2)       (-1/3)^2, (1/2)
  (x+(y^2+1)^3, y+f^2)    6  12   (-1/6)^10, (3/4)      (-1/6)^5, (3/4)
  (x+y^5, y+(x+y^5)^3)    5  15   (-1/5)^12, (11/15)^2  (-1/5)^4, (11/15)

  pair                    delta_1   a_1  b_1  Phi(delta_1)  delta^0   N   #D_1's
  (y, x+y^5)                -1/5     5    1        1          4/5     1     1
  (x+y^3, y+(x+y^3)^2)       1/2     2    1        1          5/6     1     3
  (x+(y^2+1)^3, y+f^2)       3/4     2    1        1         11/12    1     6
  (x+y^5, y+(x+y^5)^3)     11/15     3    1        1         14/15    1     5
```

On every row: `Phi(delta_1) = 1` computed **from the tree**, `b_1/a_1 = m/n`
(Def 5.1(1) reproduced on a real pair), `D_1` is a star (nothing between `delta_1`
and `delta^0`), `-lambda_f(delta^0) = 1 - delta^0` (LEMMA DICT), and FRONTIER-N
reproduces `N = 1`. The last column is `#D_1's = n/a_1`, forced by conjugacy, and
it is the direct witness that `A_bot` is not `a_1` (§7). These pairs have `nu = 1`,
hence lie outside NU-TWO scope, but they show `Phi(delta_1) = 1` is a **geometric
identity of Keller pairs**, not a normalisation inside Moh's recursion.

**(d) The identity's content.** `Phi(delta_1) = 1` is
`delta_1 - lambda_f(delta_1) - lambda_g(delta_1) = 1`, i.e. `n - M_1 = n + m` = the
number of roots of `f*g`. Grok sec.4.3's "banked algebraic coincidence"
`(1-delta_1) + lambda_g(delta_1) = -lambda_f(delta_1)` is exactly this, rearranged;
it is **not independent content**, and its failure at `r = 2` (Grok's `-13/4` vs `3`
on `(64,48)`) is exactly `M_2 > -m`. Grok's `OPEN[N-CEILING-ATTAINMENT]` is
**CLOSED, per disc**: the density is attained on every bottom-major disc.
It is **not** closed globally: `N = U` iff `A_bot = ue` (see §7).

## 7. THEOREM EXACT-N, and why `A_bot` is not a skeleton function

> **THEOREM EXACT-N (proved here; UNREVIEWED).** Under the hypotheses of D1-STAR
> plus DETECTOR-NULL,
> ```text
>       N  =  sum over bottom-major discs D_1^(k) of  a_1^(k) * c^(k) ,
>       c^(k) = d(1 - delta_1^(k))/(d+e) ,     A_bot := sum_k a_1^(k)  <=  a_{s-1} = ue .
> ```
> Every other `g`-root lies in a minor disc and contributes `0`
> (DETECTOR-NULL; MINOR-FRONTIER). If all major branches carry the same lower-`V`
> profile then `N = A_bot c` with `A_bot in a_1 Z ∩ [a_1, ue]`.

*Proof.* DICT-N sums `(1-delta^0_i)^+` over the `n` roots of `g`; minor-disc roots
give `0` (DETECTOR-NULL + MINOR-FRONTIER); every other root lies in a bottom-major
disc (Moh's Theorem (4)–(7): the `E_i` partition `D_r` and at least one is major,
so each major chain descends to level 1), where D1-STAR evaluates the term as
`c^(k)`. The bottom-major discs are disjoint subsets of `D_{s-1}` (Def 1.1(2)). ∎

**Two-sided window, closed form.** With `1 - delta_1 = (n+m)prod_{j=2}^s P_j/Q_j`
(Def 5.1(3), `n-M_s-1 = 1`), `c = K d prod_{j=2}^{s}P_j/Q_j`, and
```text
      L := a_1 c = e V_2 d(1-delta_1)/(d+e)   <=   N   <=   u d e(1-delta_1)/(d+e) =: U ,
      L / U  =  V_2 / u .
```
`U` is the reviewed N-CEILING. **`L` is new and it INVERTS FILTER-INVERSION**: the
skeleton plus the Jacobian condition now bound `N` from **below**. MEASURED
(CONTROL P2/P3): `0 < L <= U` and `U a_1 = L u e` on all 242 099 `V`-skeletons at
`n <= 100`, 0 failures.

**Why `A_bot` is NOT computable from the skeleton, as the charge's (c) asks.**
The number of bottom-major discs is free, and that is exhibited, not feared: the
Keller pair `(x+y^5, y+(x+y^5)^3)` has `n = 15`, `a_1 = 3` and **five** conjugate
`D_1`'s, so `A_bot = 15 = ue` while `a_1 c = 1/5 = N/5` (§6(c) row 4). *(That
witness has `nu = 1`, hence lies outside NU-TWO; see DISCLOSURE (1). It refutes
"`A_bot` is a skeleton function" as a general principle and shows the multiplicity
is real, not that NU-TWO pairs must have five branches.)* What Galois symmetry
*does* give — the action of `Gal(C<t>/C((t)))` preserves `ord_t`, hence maps balls
to balls with the same root counts — is that conjugate copies of `D_1` are all
major with the same `V`, so `A_bot` is a **sum of `a_1`-values over branch
classes**, not an arbitrary integer; and only `V_s` is a global datum of the pair,
so distinct classes may carry distinct `(V_2..V_{s-1})`, hence distinct `c`. Hence:

```text
  EXACT-N-MIXED   (unconditional given the theorem):   exists a multiset of
     admissible lower-V profiles with  sum_k a_1^(k) <= ue  and
     sum_k a_1^(k) c^(k)  an INTEGER in [N_min, N_max].
  EXACT-N-SINGLE  (conditional on CONJ: all major branches share one profile,
     e.g. all conjugate):   exists an admissible V and j >= 1 with
     j a_1 <= ue  and  j a_1 c  an integer in [N_min, N_max].
```
`EXACT-N-SINGLE` is the charge's STEP 4(iv) verbatim; it is a **strictly stronger
filter** and needs the extra hypothesis. `OPEN[BRANCH-PROFILE]` below.

## 8. Moh's six survivor rows under EXACT-N

`c = d(1-delta_1)/(d+e)`; `A c` must be an integer in the live window. **Row**
means Moh's published `V` (one profile); **group** means all admissible
`(V_2..V_{s-1})` at his `V_s`, which is what a branch-robust reading must use.

```text
  row                    (d,e)  (u,v)  a_1   ue      c      L      U   row: N attainable   group: N attainable
                                                                        (single profile)    (single profile)
  (64,48)                 3,4   12,4   12   48   3/16   9/4      9        {9}   (A=48)          {9}
  (84,56) M2=64, V2=2     2,3   21,7    6   63   2/21   4/7      6      DEAD (only N=4)       DEAD (only N=4)
  (84,56) M2=72, V2=5     2,3   21,7   15   63    1/6   5/2   21/2       {10}  (A=60)         {10}
  (75,50) V2=3            2,3   20,5    9   60    1/5   9/5     12        {9}   (A=45)      {8, 9, 15}
  (75,50) V2=2            2,3   20,5    6   60   2/15   4/5      8        {8}   (A=60)      {8, 9, 15}
  (99,66)                 2,3   24,9   24   72    2/9  16/3     16       {16}  (A=72)         {9, 16}
```

Read at `N in [6,16]` (`N_min = 6`, integration #16 delta (a)).
**EXACT-N pins `N` to a single value on five of the six published rows and kills
the sixth.** Under H2's older `[4,16]` nothing is killed and `(84,56) M_2 = 64`
carries `N = 4`. `EXACT-N-MIXED` (unconditional) leaves all six groups alive.

Three things the table settles. **(i)** The charge's prediction is CONFIRMED:
`63 * (1/6) = 21/2 not in Z`, so on the `U_tower = 10.5` row `A_bot = ue` is
**impossible** — N-CEILING's crude cover is provably not exact there — and the row
survives only with `A_bot = 60 < 63`, `N = 10`. **(ii)** `N = U` *does* occur:
on Moh's published `(64,48)` (`N = 9`) and `(99,66)` (`N = 16`) rows the only
admissible `A_bot` is `ue`.
**(iii)** `(64,48)` — the smallest Moh survivor, and MKS's row — is **pinned to
`N = 9`** at group level, i.e. for every admissible lower-`V`, under CONJ.

## 9. The filter over the census

`box/exactn-drivers-20260902/exactn.py`, standard library + the reviewed
`box/moh_skeleton_N.py` (consumed unedited). **FAIL-CLOSED**: the `Phi` controls
run first and any failure aborts with exit 1 and no filter output. Kills are per
branch-robust group `(m, M_2..M_s, V_s)`. Four filters:

```text
  FLOOR    L_min > N_max     L_min = min over admissible lower-V of a_1 c   (NEW)
  CEILING  U_max < N_min     U_max = max over admissible lower-V of u e c   (reviewed)
  SINGLE   no j >= 1 with j a_1 <= ue and j a_1 c integral in [N_min,N_max]  (needs CONJ)
  MIXED    no multiset of profiles with sum a_1 <= ue and sum a_1 c integral in
           [N_min,N_max]     (UNCONDITIONAL given THEOREM EXACT-N)
```
MIXED is a bounded knapsack (exact integer arithmetic after clearing one common
denominator per group) with early exit and a 20 000-state cap; cap hits are counted
**UNDECIDED, never killed**, so every MIXED number is a lower bound. Caps 20 000
and 200 000 give the identical count at `D <= 70` (131).

### 9.1 Measured

```text
  D    #groups   kill U<6   kill SINGLE   kill MIXED    min L    max L
 ---------------------------------------------------------------------------
  48        50          5            28            11     3/16      9/7
  60       110         40            75            52     3/32      9/7
  64        84          0            45            17      1/4      9/5
  72       316         12           148            61     3/25      9/5
  84       207         54           134            80     1/16     16/9
  90       577         29           402           195     3/50    30/13
  96      1113          5           533           128     3/32    45/16
 100       732         70           562           289     5/48    30/13
 105       264         30           222           159*    3/46     16/7      MOH-SHARP-2
 108       824         65           439           194     3/64    45/16      MOH-SHARP-2
 112      1163          0           821           385     1/12    63/19      MOH-SHARP-2
 117        60         10            47            26     1/18    24/19      MOH-SHARP-2
 120      4104         19          2463           549     3/64    45/16      MOH-SHARP-2
 126      1081         47           765           478     3/70    63/19
 128      1725          0          1023           447      1/8    42/11
 140      3072         70          2427          1070     5/72    63/19
 ---------------------------------------------------------------------------
 TOTAL D <= 140  (full run, 345 s one core, box/exactn-drivers-20260902/exactn140.log)
     branch-robust groups                18 064
     killed by the FLOOR  L > 16              0     (max L over the whole range 63/19 = 3.32)
     killed by the CEILING U < 6            697     ( 3.9 %)   [reviewed N-CEILING]
     killed by EXACT-N-MIXED  (uncond.)   5 275     (29.2 %)   cap hits 4 750, UNDECIDED
     killed by EXACT-N-SINGLE (needs CONJ) 11 992   (66.4 %)
     degrees EMPTIED                       NONE    (by any of the four filters)

 TOTAL D <= 190  (SINGLE only, 726 s; box/exactn-drivers-20260902/exactn-single200.log)
     branch-robust groups                76 282
     killed by the CEILING U < 6          1 288     ( 1.7 %)
     killed by EXACT-N-SINGLE            49 623     (65.0 %)
     degrees EMPTIED                       NONE

 * D = 105 has ZERO cap hits, so its MIXED count 159 is EXACT.  Cap sensitivity at
   D = 120: of the 1 528 capped groups a random sample of 60 rerun at cap 300 000
   decided 18 -- 3 INFEASIBLE, 15 feasible -- so the capped groups are mostly alive
   and the MIXED counts are close, not badly understated.  Cross-check: the two
   independent runs agree exactly on every column at every D <= 140.
```

### 9.2 Why no degree empties, and what the arithmetic says beyond the run

The kills are **arithmetic**, not metric: writing `c = p/q` in lowest terms, one
profile needs `q | A_bot` with `N_min <= A_bot p/q <= N_max`, i.e. `q <= ue` and a
multiple `A` of `lcm(q, a_1)` in `[N_min q/p, min(ue, N_max q/p)]`. Two facts keep
the census from emptying. **First, `ue` grows like `D` while the live window
`[6,16]` does not**, so admissible `A_bot` become *more* plentiful as `D` grows —
the opposite of what a `D`-ceiling needs. Second, each group carries many
admissible `(V_2..V_{s-1})`, each with its own `q`, and MIXED lets them combine.
**A uniform elimination is therefore NOT in reach from EXACT-N alone.** What would
change that is a bound on the number of major branches: if `A_bot = ue` were
forced, `N = U(skeleton)` would be a closed form and the filter would read "`U` is
an integer in `[6,16]`", which almost every skeleton violates. `A_bot = ue` is
**false in general** (§7, §8), so that is not available.

## 10. Consequences, priced

```text
 A. OPEN[D1-SUBTREE] CLOSED, AND EMPTY.  The residue N-ON-THE-TREE left -- a
    bounded rational per bottom-major disc -- is pinned to the TOP of its range.
    Moh's degeneracy at r = 1 (his minor criterion reads #roots <= n/(n+m) < 1, so
    every subdisc of D_1 would be "major") is EXPLAINED: those subdiscs are
    SINGLETONS, so the extension is vacuous and no M_0 is needed.
 B. OPEN[UPPER-TO-FLOOR] ANSWERED, PARTIALLY.  The first floor on N from boundary
    data is L = a_1 c -- and it is MEASURED far too weak (max L = 3.32 to D <= 190
    against a window topping at 16).  What kills is the ARITHMETIC, not the metric.
 C. FILTER-INVERSION SCOPED, NOT REFUTED.  Its mechanism is REFUTED at D_1 (no
    unknown structure; the f-tree is slaved by LEMMA DICT); its conclusion survives
    weaker, the free datum having moved from the SHAPE of the sub-tree to the
    NUMBER of bottom-major discs.
 D. N-CEILING ATTAINED PER DISC, NOT GLOBALLY.  Grok's OPEN[N-CEILING-ATTAINMENT]
    closes per bottom-major disc, stays open globally: N = U iff A_bot = ue, which
    happens at (64,48) and (99,66) and provably fails at (84,56) M2=72, V2=5.
 E. NEW NECESSARY CONDITION ON g ALONE: COROLLARY NO-RESIDUE; its exact content is
    the exclusion of delta^0 = 1.
 F. NEW SEARCH CONDITION FOR MOH'S PROGRAM, condition (15) beside N-ON-THE-TREE's
    (14):  some integer A_bot with a_1 <= A_bot <= ue must make
    A_bot * K d prod_{j=2}^{s} P_j/Q_j an integer in [6,16].
 G. NOT GAINED.  No bound on D, D_min, T, Psi; no (B2)/(B3) cell emptied; case (A)
    untouched (EMPTY at every N); A2 untouched; no realisability statement; nothing
    on the source side.  HARMONIC-BOUND, MOH-CROSS, PLACE-LEDGER unchanged.
```

## 11. Corrections and opens

```text
 C1. STEP 1 as written ("integrating in x; no log term can occur because
     f(x,tau_i) is a Puiseux series") -- DIRECTION.  Differentiate, do not
     integrate.  The x^{-1}-coefficient condition is AUTOMATIC on the f side
     (COROLLARY NO-RESIDUE) and a CONSTRAINT on g.  The genuine second case is
     lambda = 0, where delta^0 = e_1 + 1 and delta^0 = lambda + 1 FAILS; every
     conclusion of the proposal is nevertheless correct.
 C2. Grok ideation sec.4.3 -- RETYPED.  The r=1 "banked algebraic coincidence" is
     Phi(delta_1) = 1, i.e. RADIUS-ORDER at r=1 composed with lambda_f =
     (m/n)lambda_g; its content is n - M_1 = n + m.  Half of it (Phi >= 1) is
     FORCED by the Jacobian independently of Moh's recursion.
 C3. STEP 4(iii) -- CORRECT as stated but NOT a closed form: the parenthetical
     "sum per disc if different major branches carry different delta_1" is the
     whole difficulty.
 C4. STEP 4(iv) "a multiple of a_1" -- CONDITIONAL: it presupposes one lower-V
     profile across all major branches.  Unconditionally the condition is the
     MIXED knapsack of sec.9, which is strictly weaker.  Both are measured.
 C5. Charge (c) "compute A_bot from the skeleton so that N is a closed-form
     function of (n,m,M_*,V_*,u,v)" -- NOT ACHIEVABLE; the obstruction is
     exhibited, not conjectured (sec.7).
 C6. N-ON-THE-TREE sec.4.5, "N|_{D_1} ... the bottom when the counts stay
     proportional" -- the BOTTOM IS UNREACHABLE.  The Jacobian forces the top.
```

```text
OPEN[BRANCH-PROFILE]  (new; the exact residue of EXACT-N).  Do all major branches
   of one pair carry the same (V_2..V_{s-1}) -- equivalently, is the set of
   bottom-major discs one Galois orbit?  BOUNDED QUANTITY: one partition of
   A_bot <= ue into branch classes.  If YES the unconditional filter is
   EXACT-N-SINGLE, which measures 2-3x the kills.  Moh's Prop 4.6 assigns V_r as
   the multiplicity of a factor of ONE polynomial p(pi) of degree d_r/d_{r+1}; if
   the multiplicities used by distinct branches must sum inside Def 5.1(2)'s
   window, the branch mix is bounded.  NOT implemented: the p(pi) displays are
   OCR-destroyed and were not recovered.
OPEN[A-BOT-FLOOR]  (new; where a D-ceiling could still come from).  Is A_bot
   bounded below by more than a_1 -- e.g. by the number of Galois conjugates of
   D_1?  BOUNDED QUANTITY: the integer A_bot/a_1 in [1, u/V_2].
OPEN[EXACT-N-BEYOND-200]  (cost, not structure).  BOUNDED QUANTITY: the MIXED kill
   counts at 141 <= D <= 400 and the SINGLE counts at 191 <= D <= 400.
OPEN[MIXED-CAP]  (cost).  BOUNDED QUANTITY: the 4750 cap-hit groups at D <= 140,
   each undecided rather than killed; a full decision can only RAISE the MIXED
   kill count.
```

Carried unchanged: `OPEN[MOH-ENDGAME]`, `OPEN[NONPROPER-DEGREE]`,
`OPEN[DELTA75-BRACKET]`, `OPEN[U-GT-2-ALL-D]`, `OPEN[MOH-14]`,
`OPEN[SUBRECT-ORBIT-BRIDGE]`, `OPEN[ANTICANON-DEFECT]`, `OPEN[SAT-MASS]`,
`OPEN[DELTA-AFF-VS-N]`. **Retyped:** `OPEN[D1-SUBTREE]` CLOSED (empty);
`OPEN[UPPER-TO-FLOOR]` answered by a real but weak floor;
`OPEN[N-CEILING-ATTAINMENT]` (Grok) closed per disc.

## 12. FALLACY-v2 audit

* **Flag/place/series.** Moh's `n = D` and the campaign's `n = deg Abar_F` never
  occur together (the latter is absent); Moh's `d_i`, the exponent `d` of
  `l(P) = alpha H^d` and GGV's `d_j` are kept apart; `V_i` is never read as `nu`.
  The three levels of the tree carry three different theorems: major tower
  (Def 5.1(1) + RADIUS-ORDER), minor discs (Prop 6.1 / DETECTOR-NULL +
  MINOR-FRONTIER), sub-tree of `D_1` (**D1-STAR: trivial**). The two `delta^0`'s —
  analytic `-ord_t g_y(tau)` and the tree frontier — are **proved** equal
  (LEMMA SHIFT), not identified.
* **Per-ray/exit-set charge.** No exit price, no `charge_basis` line. Each `g`-root
  is charged once at its own frontier; bottom-major discs are disjoint subsets of
  `D_{s-1}` (Def 1.1(2)); the star's points are counted once each.
* **Carrier/attainment; floor/attainment.** `N = U` is **not** asserted: it holds
  iff `A_bot = ue`, exhibited on two rows and **refuted** on a third. `L` is used
  only as a floor, `U` only as a ceiling. MIXED cap hits are typed UNDECIDED and
  never counted as kills, so every MIXED count is a floor. The `nu = 1` Keller
  controls are positive controls for the dictionary and the star, **not** for
  NU-TWO scope (DISCLOSURE (1)).
* **Pole/interior; prime label.** `lambda_h(delta) = ord_t h(sigma_delta)` only at
  a genuine `pi`-root (Prop 1.2); the identity `pole = 1 - delta^0` is used only
  after the `lambda != 0` branch is established and the `lambda = 0` branch is
  carried everywhere. `T_r` versus `T_r^psi` never conflated; `g_y`, `f_y`, `tau'`
  are genuine derivatives with their source stated.
* **`sat()` / raw remainder / variable-ring map.** No Groebner basis, no
  saturation, no quotient normal form. Newton-polygon slopes are exact
  `Fraction`s from integer `deg_x`; resultants are `sympy.resultant` over `Q` with
  the eliminated variable declared at each call; the knapsack is exact integer
  arithmetic after clearing one common denominator per group.
* **No cap or analogy; OCR discipline.** `OPEN[BRANCH-PROFILE]`,
  `OPEN[A-BOT-FLOOR]`, `OPEN[MIXED-CAP]`, `OPEN[EXACT-N-BEYOND-200]` are left open
  rather than filled; the MIXED/SINGLE distinction is carried through every number.
  Every Moh quotation carries an `MOH:` line number; the one display this lane
  would need and cannot read (Prop 4.6's `p(pi)`) is named in
  `OPEN[BRANCH-PROFILE]` and nothing rests on it.

## 13. Typed verdict block

```text
LANE       EXACT-N (flagship, hostile).  Successor of OPEN[D1-SUBTREE] and
           OPEN[UPPER-TO-FLOOR] (N-ON-THE-TREE, reviewed).
SCOPE      Keller, noninvertible, degree-minimal, Moh's gauge (deg = deg_y, monic
           in y, two points at infinity, NU-TWO, M_s = n-2, M_1 = -m).  LEMMA
           DICT, COROLLARY NO-RESIDUE and THEOREM DICT-N hold for ANY pair with g
           monic in y and [f,g] in C^*.  Case (A) EMPTY and untouched; A2
           untouched; no Z(G)=1; H2 only where the campaign N-window is quoted.

PER-STEP VERDICT (against the charged proposal)
 STEP 1  DICT-N .......... CONFIRMED, with C1 (direction) and the lambda = 0 branch
         made explicit.  N = sum_i (1-delta^0_i)^+ on the unshifted g-tree alone;
         delta^0 = 1 IMPOSSIBLE.  The "no log" question ANSWERED: automatic on the
         f side, a constraint on g (NO-RESIDUE), with a negative control.
 STEP 2  frontier bound .. CONFIRMED (it is Phi(delta^0) <= Phi(delta_1)).
 STEP 3  N-CEILING density CONFIRMED (reviewed; scope re-checked: M_s = n-2 for
         RADIUS-ORDER, M_1 = -m from MOH:2527, outside contributions included).
 STEP 4  the squeeze ..... CONFIRMED.  (i) D1-STAR and (ii) the per-root density
         PROVED.  (iii) CORRECT but not a closed form (C3).  (iv) CONDITIONAL on
         one branch profile (C4).  The 10.5 prediction is CONFIRMED.
 (a) the r=1 identity  ... NOT a coincidence (it is Phi(delta_1)=1) and NOT an
         artefact of Def 5.1(3) (MOH:2163-2167, MOH:3284-3286).  The STAR is NOT
         Moh's statement.  Half the identity is forced by the Jacobian alone.

PROVED HERE  (all PROVED-HERE, UNREVIEWED)
 LEMMA DICT [2]        lambda != 0 => delta^0 = lambda+1 ; lambda = 0 =>
                       delta^0 = e_1+1 > 1 ; delta^0 = 1 impossible.
 COROLLARY NO-RESIDUE [2]  [x^{-1}] 1/g_y(x,tau) = 0 on a Keller pair -- a
                       condition on g alone.  Negative control g = y^2-x^2-x.
 LEMMA SHIFT [2.1]     -ord_t g_y(tau_i) = delta^0_i (unshifted-tree frontier).
 THEOREM DICT-N [2.1]  N = sum_i (1 - delta^0_i)^+ .
 Phi / Phi-DICT / Phi-TOWER [5]   Phi non-increasing; Phi(delta^0) >= 1;
                       Phi(delta_1) = 1 exactly, Phi(delta_r) > 1 for r >= 2.
 THEOREM D1-STAR [5]   D_1 is a star; delta^0 = delta_1 - lambda_g(delta_1) < 1;
                       per-root contribution exactly c = d(1-delta_1)/(d+e).
 COROLLARY D1-SUBTREE-EMPTY / MINOR-FRONTIER [5]   OPEN[D1-SUBTREE] closed and
                       EMPTY; minor-disc g-roots have delta^0 > 1.
 THEOREM EXACT-N [7]   N = sum_k a_1^(k) c^(k), A_bot = sum_k a_1^(k) <= ue;
                       FLOOR L = a_1 c <= N <= U = ue c (U reviewed, L new).

MEASURED   119 controls, 0 failures (dictionary 64, treestar 28, noresidue 4,
           exactn P1-P4 23).  Phi(delta_1) = 1 and Phi(delta_r) > 1 (r >= 2) on
           ALL 242 099 V-skeletons at n <= 100.  D <= 140: 18 064
           branch-robust groups; FLOOR kills 0; CEILING U<6 kills 697; EXACT-N
           MIXED kills 5 275 (cap hits 4 750 UNDECIDED); EXACT-N SINGLE kills
           11 992; NO degree emptied.  D <= 190 (SINGLE): 49 623 of 76 282; NO
           degree emptied.  MOH-SHARP-2 {105,108,112,117,120}: none emptied.
           Moh's six rows: five pinned to one N, one killed at N_min = 6.
DECISION   THE SQUEEZE CLOSES AND D_1 IS A STAR; OPEN[D1-SUBTREE] IS CLOSED AND
           EMPTY; the filter becomes TWO-SIDED and, for the first time, ARITHMETIC.
           It kills 29-66% of every degree and empties none.  The residual free
           datum is the NUMBER of bottom-major discs, not their shape.
REFUTED    "A_bot is a function of the skeleton" (charge (c)) -- REFUTED by the
           Keller witness (x+y^5, y+(x+y^5)^3) with five conjugate D_1's.
           "N|_{D_1} can be driven to 0 by proportional counts" (N-ON-THE-TREE
           sec.4.5) -- REFUTED: the Jacobian forces the top of the interval.
           "A_bot = ue always" -- REFUTED at (84,56) M_2=72, V_2=5 (U = 21/2).
GAP        OPEN[BRANCH-PROFILE]: SINGLE vs MIXED, i.e. whether all major branches
           share (V_2..V_{s-1}).  This is the ONLY gap between the strong filter
           (2-3x the kills) and the unconditional one.  Prop 4.6's p(pi) display
           is OCR-destroyed and was not recovered.
           OPEN[EXACT-N-BEYOND-200]: MIXED beyond D = 140 and SINGLE beyond
           D = 190 are a COST gap, not a structural one.

DISCLOSURE (1) NO POSITIVE CONTROL IN NU-TWO SCOPE EXISTS, and cannot: a Keller
               pair in the gauge with nu = 2 IS a counterexample.  The four
               Keller controls of sec.6(c) have nu = 1 (one place at infinity, by
               Abhyankar-Moh), so they verify LEMMA DICT, DICT-N, Phi(delta_1)=1,
               b_1/a_1 = m/n and the STAR on real Jacobian pairs, but not inside
               NU-TWO.  The NU-TWO input (RADIUS-ORDER, DETECTOR-NULL) is
               consumed as reviewed.
           (2) Def 5.1(1)-(4) and Prop 5.3 reach this lane through DEPTH-CEILING
               (a PROPOSAL) and N-ON-THE-TREE (reviewed).  Def 5.1(4) is NOT used
               and was NOT re-read (OCR-destroyed).  If Def 5.1(3) at i = 1 were
               wrong, the dictionary would still give Phi(delta_1) >= 1, hence
               delta^0 <= delta_1 - lambda_g(delta_1); D1-STAR would weaken to that
               one-sided statement and EXACT-N to N <= U.
           (3) The MIXED knapsack is capped at 20 000 states per group; cap hits
               are UNDECIDED, never kills, so every MIXED count is a floor.  At
               D <= 70 caps 20 000 and 200 000 give the identical count (131).
           (4) "N >= 2" uses Ax-Grothendieck; "N in [6,16]" uses integration #16
               delta (a) and is typed as such at every use.
           (5) No box01 job; no AWS; total wall for every driver in this report is
               under 25 minutes on one core.  SINGLE beyond D = 190 and MIXED
               beyond D = 140 were NOT run: the census enumeration alone stalls at
               D = 192 on this box.  OPEN[EXACT-N-BEYOND-200].
           (6) SIZE: body 48 KB against the charged 25-40 KB band.  The overrun is
               the four evidence tables (sec.6(c) joint trees, sec.8 survivor rows,
               sec.9.1 filter, sec.2.2 controls) and the two full proofs, kept
               complete rather than compressed.
```
