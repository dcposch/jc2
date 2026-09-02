# N-ON-THE-TREE — the geometric degree is a contact deficiency at the *last major disc*; Moh's tree bounds it ABOVE, never below, and the `N <= 16` filter is therefore satisfied, not violated

Lane: `N-ON-THE-TREE` (successor `OPEN[N-ON-THE-TREE]` of DEPTH-CEILING).
Date: 2026-09-02. Agent: Opus 5. Desk derivation + desk-scale CAS
(python3 3.14.7 / sympy 1.14.0 over `Q`; no Singular, no AWS, no web, no fetching).
Deliverable installed at `box/moh_skeleton_N.py`; driver directory
`box/nott-drivers-20260902/`. Full run (all controls + filter to `D <= 200`)
42.3 s wall, one core, peak RSS < 200 MB; the `D <= 400` filter 161 s.

## 0. Custody, method, scope

The four charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all four match the charge (`863b05db…` depth-ceiling, `7b0ffec7…` MKS,
`bf1d428c…` integration14, `489e9ba2…` cluster-census codegen).

**DEPTH-CEILING (DC) is a PROPOSAL and is treated as one.** Everything used from
it is re-derived or independently re-validated: CONTACT-DEFICIENCY is re-proved
and re-controlled from scratch (§2); Moh's Def 5.1(1)–(4) and Prop 5.3 — which DC
recovered from page images, the OCR having dropped every display — are
re-implemented independently and re-validated against Moh's published `delta`
columns (CONTROL 3) plus **two further published facts DC did not use** (§4.1),
pinning the recovered display three ways; DC's census is re-implemented and
re-calibrated (CONTROL 4). DC's `MOH-SHARP-2` degree list only chooses which
degrees to tabulate; nothing rests on it.

Sources read firsthand, with line numbers into the extraction shipped in
`box/depth-drivers-20260902/`:

```text
6c8847a8...  refs/moh1983_jram340_configurations_of_roots.pdf
b6a36914...  box/depth-drivers-20260902/moh.txt   (pdftotext -layout; line numbers below)
30220204...  box/moh_skeleton_N.py                (deliverable)
be641ba8...  box/nott-drivers-20260902/filter400.log
```

Typing discipline as charged: integrations #12–#14 at their scopes; H2 only where
the campaign ledger is quoted; **no case (A)** (EMPTY at every N), **no A2**, **no
`Z(G) = 1`**. No canonical ledger edited; `jc2-lean` not inspected; nothing
fetched. **No `charge_basis` line: this report asserts no new exit price.**

Six degree-like integers are kept apart and never substituted (§11): `D`, `N`,
`K = gcd(deg P, deg Q)`, **Moh's `n = deg_y g = deg g = D`** and **`m = deg_y f`**,
the campaign's `n = deg Abar_F` (source-side, occurring nowhere here), and `nu` =
# distinct roots of the top form.

## 1. Verdict, up front

```text
(1) THE INSTRUMENT EXISTS, RUNS, AND ANSWERS THE OPPOSITE QUESTION.  N is
    computable on Moh's tree (THEOREM FRONTIER-N, sec.3) and the skeleton
    determines an UPPER bound on it (THEOREM N-CEILING, sec.4.4)
        N  <=  U(skeleton)  =  u d (-lambda_g(delta_1))  =  u d e (1-delta_1)/(d+e),
    u = V_s K/d_s the multiplicity of the major linear factor of the top form
    (H = L_1^u L_2^v, u > v, u+v = K), deg P = Kd, deg Q = Ke = D.  There is NO
    lower bound: the unknown sub-tree of D_1 can only ADD contact, i.e. LOWER N.
    So the charged filter "N <= 16" is SATISFIED by every skeleton and rejects
    nothing (FILTER-INVERSION, sec.6.1); the operative test is U >= N_min.
(2) MEASURED, D <= 400 (161 s, one core, box/nott-drivers-20260902/filter400.log).
    3 874 261 branch-robust groups.  U < 2 (kills N >= 2): ZERO, with measured
    min U = 792/329 = 2.407 and derived asymptotic floor 2de/(d+e) >= 12/5 -- the
    unconditional filter provably CANNOT fire.  U < 4 (kills N >= 4 under H2):
    1147 groups, 0.030%.  NO degree D is emptied.  THE CEILING IS NOT PROVED ON
    ANY RANGE BY THIS INSTRUMENT, and the obstruction is structural, not cost.
(3) MOH'S SEC.6 IS NOT THE GAP; D_1 IS.  LEMMA DETECTOR-NULL (sec.4.3): by Moh
    Prop 6.1(2) / Theorem (5) every pi-root of a minor disc with ord g < 0 is a
    DISTRIBUTION DETECTOR, so lambda_f = (m/n)lambda_g there, so lambda_f = 0 at
    the g-frontier, so minor discs contribute EXACTLY ZERO to N.  The charge's
    premise ("what is missing is the minor-disc distribution") is INVERTED: what
    is missing is the sub-tree of the LAST MAJOR disc D_1, where Moh's own minor
    criterion degenerates (at r = 1 it reads #roots <= n/(n+m) < 1) and there is
    no M_0.  D_1 is where his recursion ends and N is born.
(4) TWO NEW IDENTITIES, both verified: FRONTIER-N writes N on the tree of the
    roots of f*g alone, no c-shift (exact on 7 explicit-root rows); RADIUS-ORDER
    (sec.4.2) shows Moh's logarithmic radius and the order of g are ONE datum,
    lambda_g(delta_i) = -n prod_{j>i} P_j/Q_j = -n(1-delta_i)/(n-M_i) (242 099
    V-skeletons, 0 failures).  UNCONDITIONAL COROLLARY: 1/N > 1/deg P + 1/deg Q,
    hence N < D/2; at the MOH-SHARP-2 admissible degrees, N <= 44.
(5) WHAT IS DELIVERED INSTEAD: a per-skeleton N-WINDOW.  At D in [101,200] the
    ceiling beats the H2 cap on 19 455 of 116 385 surviving groups (16.7%) and
    PINS N = 4 exactly on 418.  Moh's four n <= 100 survivors (list re-verified
    against sec.6 AND Appendix II; DC's (64,68) -> (64,48) CONFIRMED by an
    independent route) carry U = 9, 6, 10.5, 12, 8, 16 at his own published V:
    ALL FOUR sit inside N <= 16.  Two OCR displays in Moh 1983 are corrected
    (sec.4.1, sec.9), each forced and each an independent check on the recursion
    DC recovered from page images.
```

## 2. Part (1): CONTACT-DEFICIENCY, re-derived, with its hypotheses made explicit

### 2.1 The statement and the proof

> **THEOREM CONTACT-DEFICIENCY (re-derivation).** Let `f, g in C[x,y]` be **monic
> in `y`** with `deg f = deg_y f = m`, `deg g = deg_y g = n`, and let `F = (f,g)`
> be dominant. Put `t = x^{-1}` and let `phi_1..phi_m`, `tau_1..tau_n` be the
> roots of `f - c_1`, `g - c_2` in the Puiseux field `C<t>`. Then for generic
> `(c_1,c_2) in C^2`,
> ```text
>     N  :=  deg F  =  deg_x Res_y(f - c_1, g - c_2)  =  - sum_{i,j} ord_t(tau_i - phi_j) .
> ```

*Proof.* Both are monic in `y`, so the resultant is the **bare product**
`prod_{i,j}(phi_j - tau_i)` with no leading-coefficient factor — this is where
monicity is load-bearing (negative control below) — and it lies in `C[x]`. Three
genericity clauses turn `deg_x` into `N`: the fibre is reduced (automatic for a
Keller pair, whose Jacobian is a unit; generic `c` otherwise); the `N` points have
distinct `x`-coordinates (generic linear change inside the gauge); and `deg_x Res`
does not drop, its coefficients being polynomials in `(c_1,c_2)` so that the
degree is maximal on a Zariski-open set of `c`. Finally `deg_x = -ord_t` on
`C[x]` and `ord_t` is additive on products. ∎

**Slope split.** If `l(f) = alpha H^d`, `l(g) = beta H^e`, `H = L_1^u L_2^v` and a
shear makes both slopes nonzero, the `tau`'s split `(ue,ve)` and the `phi`'s
`(ud,vd)`; the `ue*vd + ve*ud = 2deuv` cross-class pairs each have `ord_t = -1`, so
`N = 2deuv - sum_{same-slope} ord_t(tau_i - phi_j)`.

*Scope note (emphasis correction to DC §5.1).* Same-slope orders are `> -1` for
free but `>= 0` — what makes DC's budget form a statement about *positive* contact
— only under **Moh Lemma 6.1** (`delta_{s-1} >= 0`, `moh.txt:2905-2912`) and
**Prop 6.1** (`delta*_{s-1} >= 1`). Off that normalisation the same-slope sum is
negative and `N` exceeds the cross-class count on **all seven** control rows
(row 0: `N = 4 > 3`); five of the seven do not even have a common `H`, so `2deuv`
is undefined there (CONTROL 5a).

### 2.2 Controls (CONTROL 1 and CONTROL 2 in the deliverable)

Seven explicit non-Keller two-tower pairs, built as products of
`(y - a x)^p - b x^q` so that **every Puiseux root is in closed form**, hence
`ord_t(tau - phi)` is exact. Writing a factor as `(a,p,b,q)`:

```text
  f-spec                    g-spec                    m  n  N(res) N(pair) N(frontier)
  [(1,1,3,0),(2,1,5,0)]     [(1,2,7,1),(2,1,11,0)]    2  3    4       4        4
  [(1,2,3,1),(2,2,5,1)]     [(1,3,7,2),(2,1,11,0)]    4  4   13      13       13
  [(1,2,3,1),(2,2,3,1)]     [(1,3,3,1),(2,3,3,1)]     4  6   18      18       18
  ... 4 further rows (m,n) = (3,4),(3,4),(4,4),(4,6): N = 9, 9, 12, 18, all three
  columns equal on every row.
```

**Gauge controls, positive and NEGATIVE.**

```text
  map                          N (true)   deg_x Res_y   in gauge?
  automorphism (y, x + y^5)        1           1        yes  (monic, deg = deg_y)
  automorphism (y, x + y^7)        1           1        yes
  (x, x y^2) / (x, x y^5) / (x^3, y^2)   2/5/6 = 2/5/6  no  (accidentally agree)
  psi_2 o (x, x y^2)               2           6        no  -- IDENTITY FAILS
  psi_3 o (x, x y^3)               3          12        no  -- IDENTITY FAILS
```

The last two are the charged **negative control**: `f = x + x^2 y^4` is not monic
in `y` (leading coefficient `x^2`), the resultant acquires the factor
`lc(g)^{deg f} = x^4`, and `deg_x Res = 6 != 2 = N`. **The monic/`deg = deg_y`
hypothesis is load-bearing and was tested by failure.** The automorphism rows are
the charged `N = 1` control: the pairing computes `N = 1` correctly.

## 3. THEOREM FRONTIER-N — the pairing in the form the tree can eat

The pairing above is written on the roots of `f - c_1` and `g - c_2`; Moh's tree
is the tree of the roots of `f` and `g`. The two are related exactly, and the
relation is the whole mechanism.

For a Puiseux series `sigma` and `delta in Q`, write `sigma_delta` for Moh's
general `pi`-root of radius `delta` on `sigma`'s path (`moh.txt:361-374`), and
recall Moh's Prop 1.2: the multiplicity of `sigma_delta` as a `pi`-root of `h` is
the number of roots of `h` in the disc. Elementarily,

```text
    ord_t h(sigma_delta)  =  sum_{j} min( delta , ord_t(sigma - h-root_j) )  =:  lambda_h(delta) ,
```
a continuous, piecewise-linear, nondecreasing function of `delta` whose slope is
the number of roots of `h` still in the disc; `lambda_g(-1) = -n` and
`lambda_f(-1) = -m` in the gauge.

> **THEOREM FRONTIER-N (proved here; every dominant `F` with both coordinates
> monic in `y` of `y`-degree `=` degree).** For each root `rho_i` of `g` let
> `delta^0_i` be the unique level with `lambda_g^{(i)}(delta^0_i) = 0`. Then for
> generic `(c_1,c_2)`,
> ```text
>       N  =  sum_{i=1}^{n} max( 0 , - lambda_f^{(i)}(delta^0_i) ) .
> ```

*Proof.* Let `B` be the ball of radius `delta^0 := delta^0_i` around `rho_i`,
with `a(B)` `g`-roots. On `B`, `g(sigma) = g_sigma(pi)t^0 + ...` with
`deg_pi g_sigma = a(B)` (Prop 1.2), so `g_sigma(pi) = c_2` has `a(B)` roots, simple
for generic `c_2`. Hence the `a(B)` roots of `g - c_2` inside `B` follow the
`g`-tree down to `delta^0` and then separate, pairwise at `ord` exactly `delta^0`;
this is a bijection onto the `g`-roots of `B`, and `delta^0` is common to them
(`lambda_g` depends only on the ball above `delta^0`). So for the corresponding
root `tau` of `g - c_2`, `ord_t(tau - phi^0_j) = min(delta^0, ord_t(rho_i - phi^0_j))`
for every root `phi^0_j` of `f` (generic `c_2` keeps the separation coefficient off
the finitely many bad values), i.e. `ord_t f(tau) = lambda_f^{(i)}(delta^0)`.
Finally `ord_t(f(tau) - c_1) = min(0, ord_t f(tau))` for generic `c_1`, and
`Res_y(f-c_1,g-c_2) = prod_tau (f(tau) - c_1)` because `f - c_1` is monic. ∎

Two readings, both used below. **(i)** `N` is a sum over the `g`-tree alone: the
`c`-shift is absorbed, the only new object being the *frontier* `{lambda_g = 0}`,
Moh's "blur at `2^0 = 1`" (`moh.txt:2884-2896`). **(ii)** `N` is a **deficiency**:
if the root counts are *proportional* (`b(delta)/a(delta) = m/n`) along `rho_i`'s
path wherever `lambda_g < 0`, then `lambda_f = (m/n)lambda_g` there, so
`lambda_f(delta^0_i) = 0` by continuity and `rho_i` contributes **nothing**. `N`
measures exactly the failure of proportionality — by Moh's Def 3.1, the failure of
the *distribution-detector* property.

**Verified**: `N(frontier) = N(resultant)` on all seven control rows (CONTROL 1),
including the deliberate near-proportional row 6, where `N = 18` because
proportionality breaks at the last level — the mechanism §4.4 quantifies.

## 4. Part (2): `N` on a Moh skeleton

### 4.1 What Moh's tree is, and how the two towers share their structure

Moh's characteristic data `{M_i, d_i}` is the tree datum of the roots of `f` over
`k[x]((g^{-1/n}))` (`moh.txt:527-573`); from §4 on he studies the **`t`-adic** tree
of the roots of `g(y) prod_i T_i^psi(y)` in `k<t>` (`moh.txt:1251-1266`), with
logarithmic radius `delta = ord_t` (`moh.txt:347-352`) and `T_1 = f`
(`moh.txt:3262`). Def 5.1(3) is what makes the first control the second.

> **HOW THE TWO TOWERS SHARE — exactly.** Def 5.1(1): the major disc `D_i`
> contains **precisely** `(n/d_{i+1})V_{i+1}` roots of `g` **and precisely**
> `(-mu_j/d_{i+1})V_{i+1}` roots of `T_j`, `j = 1..i`. With `-mu_1 = m`,
> ```text
>       b_i / a_i  =  m / n     for every i   ( a_i = # g-roots, b_i = # f-roots in D_i ) ,
> ```
> i.e. **the two towers are one tower with proportional counts** — Moh's Def 3.1
> (distribution detector, `moh.txt:1153-1167`) along the major chain, a
> consequence of the Jacobian condition through Props 4.4/4.6, whose numerical
> criteria decide splitting versus non-splitting and make `delta_{r-1}` a formula
> rather than a free radius. Verified on all six Moh rows (CONTROL 3).

**Two OCR corrections to Moh's own text, each forced, each an independent check
on the recovered Definition 5.1.**

* *(§6 leading form, `moh.txt:2884-2890`.)* The top form of `g` is printed
  `[(y-ax)^{V_s}(y-bx)^{u_s}]^{d_s}` with `u_s = d_s - V_s`; that has degree
  `d_s^2`, not `n`. The exponent is a **stacked fraction the OCR flattened** and
  must read `]^{n/d_s}`. Then the slope classes carry `(n/d_s)V_s` and
  `(n/d_s)(d_s-V_s)` roots — **exactly Def 5.1(1) at `i = s-1`** — so the top form
  is `L_1^{ue}L_2^{ve}` with `u = V_s K/d_s`, `v = (d_s-V_s)K/d_s`, `u+v = K`.
  Verified: `a_{s-1} = ue` on all six Moh rows.
* *(Theorem (5), `moh.txt:3243-3246`.)* "the number of roots of `g(y)` in `E_i` is
  `<= d_r/(n-M_r)`" is the bound on the **multiplicity** `V`; in root counts it
  reads `#roots <= n/(n-M_r)`, since `#roots = (n/d_r)V`. At `r = s` the corrected
  form makes the minor slope class minor iff `ve <= n/2` iff `v <= u` — **exactly
  NU-TWO**; the printed form would make it major.

**A third check, free.** Def 5.1(2) at `i = s` reads `V_s > d_s/2`, i.e. `u > v`:
**Moh's top-level window IS NU-TWO's `u != v`** (DC §2.2, from Prop 4.5 +
Lem 5.3 + Prop 5.4). And `V_s < d_s` (`v >= 1`) is forced by `delta_s = -1`
("more than one point at infinity", Cor 6.1(3), `moh.txt:3200`); the census
carries it.

### 4.2 THEOREM RADIUS-ORDER

Write `P_j := V_j(n - M_j) - d_j > 0` (positivity is Def 5.1(2)) and
`Q_j := V_j(n - M_{j-1}) - d_j > P_j`.

> **THEOREM RADIUS-ORDER (new).** Along the major tower,
> ```text
>     lambda_g(delta_r)  =  - n * prod_{j=r+1}^{s} P_j / Q_j
>                        =  - n (1 - delta_r)(n - M_s - 1)/(n - M_r) ,
> ```
> and with `M_s = n-2`, `lambda_g(delta_r) = -n(1-delta_r)/(n-M_r)`. Also
> `lambda_f(delta_r) = (m/n) lambda_g(delta_r)`.

*Proof.* Downward induction. At `r = s`: empty product,
`lambda_g(delta_s) = -n`. Step: Def 5.1(3) is
`1-delta_i = ((n-M_i)/(n-M_s-1))R_i` with `R_i = prod_{j>i}P_j/Q_j`, whence
`delta_i - delta_{i+1} = R_{i+1}d_{i+1}(M_{i+1}-M_i)/Q_{i+1}`; with
`a_i = nV_{i+1}/d_{i+1}` and
`lambda_g(delta_i) = lambda_g(delta_{i+1}) + a_i(delta_i-delta_{i+1})`,
`lambda_g(delta_i) = -nR_{i+1}[1 - V_{i+1}(M_{i+1}-M_i)/Q_{i+1}]
= -nR_{i+1}P_{i+1}/Q_{i+1} = -nR_i`.
The second display is Def 5.1(3) solved for `R_i`. ∎

**Verified** on 242 099 V-skeletons (`n <= 100`): both forms agree with the
incremental `lambda_g` on every row, 0 failures (CONTROL 6). At Moh's six rows,
`lambda_g(delta_1) = -1/4, -1/7, -1/4, -3/10, -1/5, -1/3` — negative on every row,
and on all 242 099, as it must be, since `lambda_g(delta_1) >= 0` forces `N = 0`
(§4.4). The `delta` values themselves appear in §5 as `1 - delta_1`.

### 4.3 LEMMA DETECTOR-NULL — Moh §6 supplies the minor discs, in full

> **LEMMA DETECTOR-NULL.** Let `E` be a minor disc (any level `r >= 2`). Then
> every `g`-root in `E` contributes **0** to `N`.

*Proof.* Moh Prop 6.1(2) (`moh.txt:2757-2759`): "the inequality `ord g(sigma) < 0`
implies that `sigma` is a distribution detector for `g(y), T_1^psi(y), ...,
T_{r-1}^psi(y)`"; Theorem (5) (`moh.txt:3243-3246`) extends this to every minor
subdisc; and Def 3.1 says a detector has `ord T_j(sigma) = lambda * deg_y T_j` with
a common `lambda`, i.e. `lambda_f(sigma) = (m/n)lambda_g(sigma)` (`T_1 = f`). So
`lambda_f = (m/n)lambda_g` on `{lambda_g < 0} ∩ E`, hence `lambda_f(delta^0) = 0`
by continuity at every `g`-frontier level inside `E`, and FRONTIER-N gives
`max(0, -lambda_f(delta^0)) = 0`. ∎

This is Moh's own reading of his §6: "the roots of `g, T_1, ..., T_{r-1}` in it are
**all distributed proportionally according to the `y`-degrees up to the uncertainty
of `2^0 = 1`**" (`moh.txt:2874-2884`) — the "uncertainty at `2^0`" being exactly
the frontier. **Consequence:** the `Sn` non-proper places of PLACE-LEDGER are
exactly the frontier balls inside minor discs; the `kappa` proper places are
exactly those under bottom-major discs.

### 4.4 THEOREM N-CEILING

By NU-TWO the root ball `D_s` has **exactly two** children: the major slope class
`D_{s-1}` (`ue` roots of `g`, `ud` of `f`) and the minor class `D*_{s-1}`
(`ve`, `vd`). At each further level DETECTOR-NULL kills the minor children and the
major ones continue the tower; the tower stops at `D_1`, because at `r = 1` the
minor criterion reads `#roots <= n/(n-M_1) = n/(n+m) < 1` — no nonempty disc is
minor — and there is no `M_0`.

> **THEOREM N-CEILING.** For a degree-minimal Jacobian counterexample in Moh's
> gauge with tower data `(n, m, M_*, d_*, V_*)`,
> ```text
>     N  <=  U(skeleton)  :=  u * d * (-lambda_g(delta_1))^+
>                          =  u * d * e * (1 - delta_1) / (d + e) ,
>            u = V_s K / d_s ,  deg P = m = Kd ,  deg Q = n = Ke = D .
> ```
> In particular `lambda_g(delta_1) >= 0` (equivalently `delta_1 >= 1`) is
> **impossible**: it would force `N = 0`.

*Proof.* By FRONTIER-N, `N = sum_i(-lambda_f^{(i)}(delta^0_i))^+`, and
`lambda_f` is nondecreasing, so for `rho_i` in a disc `B` with
`delta(B) <= delta^0_i` the term is `<= (-lambda_f(delta(B)))^+`. Cover the
`g`-roots by the maximal minor discs together with the bottom-major discs. The
minor part contributes `0` (DETECTOR-NULL). The bottom-major discs are disjoint
subsets of `D_{s-1}` (the unique major child of the root ball), so their `g`-root
counts total `<= a_{s-1} = ue`; on each,
`-lambda_f(delta_1) = (d/e)(-lambda_g(delta_1))` (§4.1). Hence
`N <= ue(d/e)(-lambda_g(delta_1)) = ud(-lambda_g(delta_1))`; the closed form is
RADIUS-ORDER at `r = 1` with `M_1 = -m`, `n+m = K(d+e)`, `n = Ke`. If
`lambda_g(delta_1) >= 0` the same covering gives `N = 0`; but `N = 1` is the
invertible case (Keller ⟹ étale; degree 1 ⟹ birational ⟹ injective ⟹ surjective
by Ax–Grothendieck ⟹ automorphism), so a counterexample has `N >= 2`. ∎

> **COROLLARY HARMONIC-BOUND (unconditional in the stated scope).** Moh Lemma 6.1
> gives `delta_{s-1} >= 0`, and radii increase downward, so `delta_1 >= 0` and
> `1 - delta_1 <= 1`; `v >= 1` gives `u <= K - 1`. Hence
> ```text
>     N  <  K d e/(d+e)  =  m n/(m + n) ,     i.e.     1/N  >  1/deg P + 1/deg Q ,
> ```
> and since `d < e`, `N < D * d/(d+e) < D/2`.

Sanity: for `(x, y + x^k)` the corollary would read `N < k/(k+1) < 1`, false —
correctly so, since there `nu = 1`, `delta_s > -1`, and neither NU-TWO nor
Lemma 6.1 applies. Measured: `delta_{s-1} >= 0` and `delta_1 >= 0` on **all
1 260 149** V-skeletons with `n <= 130` and on **all 3 874 261** branch-robust
groups with `D <= 400`, 0 exceptions; `U < mn/(m+n)` on all 3 874 261, 0
exceptions.

> **COROLLARY RAMIFICATION-FLOOR.** At a **proper** place `gamma`,
> `m_gamma = nu_gamma(-lambda_f(delta^0)) <= nu_gamma(-lambda_f(delta_1))`, so
> `nu_gamma >= m_gamma/(-lambda_f(delta_1)) = m_gamma u e/U`; for (64,48) with
> Moh's `V`, `nu_gamma >= 16 m_gamma/3 >= 6` at every proper place. This answers
> DC's `OPEN[NU-BOUND-AT-A-PLACE]` in the **direction opposite** to the one it
> wants: the tree gives a FLOOR on the ramification, never a ceiling, so
> `T <= sum h(m_gamma)` is not reachable this way (§8 F).

### 4.5 The residual free datum, named and sized

> **What the pairing needs beyond the major tower, exactly.** For each bottom
> major disc `D_1` (radius `delta_1`, `a_1 = eV_2` roots of `g`, `b_1 = dV_2` of
> `f`): the joint ultrametric tree of those `a_1 + b_1` points **below**
> `delta_1`. Its entire effect on `N` is one rational,
> `N|_{D_1} = sum_{rho in D_1}(-lambda_f(delta^0_rho))^+ in [0, a_1(-lambda_f(delta_1))]`,
> attaining the top when the `b_1` `f`-roots separate from every `g`-root at
> `ord = delta_1` (combinatorially realisable) and the bottom when the counts stay
> proportional to `lambda_g = 0`. Summed over the bottom discs: `N in [0,U]`, cut
> only by the global `N >= 2`.
>
> **Does Moh §6 supply it? NO — and not because §6 is weak.** §6 supplies the
> *minor* discs in the strongest possible form (contribution 0). What is missing
> is the *major* bottom, structurally: at `r = 1` the minor criterion reads
> `#roots <= n/(n+m) < 1`, so every subdisc of `D_1` is "major" and would extend
> the tower — but there is no `M_0`. **`D_1` is where Moh's recursion ends and `N`
> is born.** It is not a datum to be *enumerated*: it is a bounded rational whose
> range the skeleton already computes.

### 4.6 The instrument

`box/moh_skeleton_N.py` (standard library + sympy; **fail-closed**: 100 controls
run before any filter number is printed, and any failure aborts with exit 1 and no
output). Sections: exact Puiseux-root arithmetic and the ultrametric order;
CONTACT-DEFICIENCY and FRONTIER-N with the seven two-tower rows and the gauge
negative control; `Skel` (Def 5.1(1)–(3), `delta_i`, `a_i`, `b_i`, `lambda_g`
three ways, `u, v`, `N_upper`); the census with its V-assignments; the filter.
Measured: **100 controls, 0 failures**, 42.3 s for the whole run to `D <= 200`.

## 5. Part (3): Moh's four `n <= 100` survivors

**List re-verified against `refs/`, twice.** Moh's §6 table (`moh.txt:3325-3340`)
gives `(n, m = -M_1) = (64,48), (84,56), (75,50), (99,66)` with
`M_2 = 52 / 64[72] / 55 / 77`, `M_3 = n-2`, and an extra `M_4 = n-1` in the two
cases where the `d`-chain has not yet reached 1 (Lemma 2.1: the exponents
terminate at `n-1`). Appendix II (`moh.txt:3596-3597`) prints "(64, 68)" — but its
**own** reduced table gives `(n,m) = (16,12) = (64,48)/4` (`moh.txt:3616-3626`),
and `68/4 = 17 != 12`. So `(64,48)` is right and "(64,68)" is a misprint carried
into MKS: **DC's correction C1 is CONFIRMED independently.** Bracketed
alternatives make six skeleton rows; all six are produced by the re-implemented
census with their published `V`'s (CONTROL 4).

```text
  row                  K  (d,e)  (u,v)   1-delta_1  U_tower   U_rob    N in (H2)   (u-v)de/(d+e)
  (64,48)             16  (3,4) (12,4)      7/16      9.000   13.880     [4,13]        13.714
  (84,56) M2=64,V2=2  28  (2,3) (21,7)      5/21      6.000   16.962     [4,16]        16.800
  (84,56) M2=72,V2=5  28  (2,3) (21,7)      5/12     10.500   16.962     [4,16]        16.800
  (75,50) V2=3        25  (2,3) (20,5)       1/2     12.000   18.182     [4,16]        18.000
  (75,50) V2=2        25  (2,3) (20,5)       1/3      8.000   18.182     [4,16]        18.000
  (99,66)             33  (2,3) (24,9)       5/9     16.000   18.151     [4,16]        18.000
```

`U_tower` uses Moh's **published** `V` row (his conditions (7)–(13) pin `V_2` as
well as `V_3`: the table "determines only one possible value for `M_2` and one for
`V_3`"). `U_rob` is the **branch-robust** bound: only `V_s` is a global datum of
the pair (it is the split `u:v` of the top form), while `V_{s-1},...,V_2` may
differ between inequivalent major branches; since the bottom discs of all branches
together carry at most `a_{s-1} = ue` roots of `g`,
`U_rob = u d * max over the lower V's of (-lambda_g(delta_1))`, and that maximum
is attained at the top of every Def 5.1(2) window (MEASURED, CONTROL 7: 3975
groups, 0 mismatches against brute force).

**Answer to the charge's question.** Each survivor carries a *range*, not a value,
because the sub-tree of `D_1` is free: `N in [2,U]`, and `N in [4, min(U,16)]`
under H2. With Moh's own `V` row, `U = 9, 6, 10.5, 12, 8, 16`: **all four of Moh's
surviving skeletons carry `N <= 16`**, i.e. sit inside the campaign's live window,
and the `(84,56)` `M_2 = 64` row is pinned to `N in [4,6]`.

## 6. Part (4): the filter, and why it inverts

### 6.1 The direction theorem

> **THE FILTER INVERTS (this lane's decision).** A Moh skeleton determines an
> **upper** bound on `N` and no lower bound. Every ball of the tree contributes a
> nonnegative term `Delta(B)a(B)b(B)` to the contact total
> `N = mn - sum_{B != root} Delta(B)a(B)b(B)`, so unknown structure can only
> *increase* contact and *decrease* `N`; the only lower bound available is the
> global `N >= 2`. Hence **"N <= 16" is satisfied by every skeleton with `U <= 16`
> and is never contradicted: it rejects nothing.** The operative test is the
> reverse, `U(skeleton) >= N_min`.

This is the exact sense in which the charge's instrument is finite and decidable
but does not point at the ceiling: it is a ceiling **on `N`**, and the campaign
needs a ceiling **on `D` at fixed `N`**, i.e. a *floor* on `N`.

### 6.2 The run

Census conditions, all read firsthand: `d_1 = n > d_2 = K > ... > d_s >= 4`
(Moh search (5) + Cor 6.1); `s >= 3` (Prop 5.5); `M_1 = -m`, `M_s = n-2`
(search (1),(2) + Prop 5.4 / Lem 5.3); `m = Kd`, `n = Ke`, `gcd(d,e) = 1`,
`2 <= d < e` ((LF)+(MIN)); `K >= 16` (GGV Cor 6.6); Def 5.1(2) windows;
`V_s < d_s`. Calibrated to the unit against Moh's "25 possible values for `M_2`"
at `(75,50)` and DC's 2410 at `n <= 100` (CONTROL 4).

```text
   D     branch-robust groups     kill U<2   kill U<4 (H2)   min U      max U
   105          264                   0            0        4.337      33.54
   108          824                   0            0        4.848      38.63
   112         1163                   0            0        6.292      41.37
   117           60                   0           10        3.635      39.82
   120         4104                   0            7        3.459      44.80
  ---------------------------------------------------------------------------
   D <= 100     3 975                 0           79        2.430      35.78
   D <= 200   120 641                 0          360        2.414      80.24
   D <= 400 3 874 261                 0         1147        2.407     171.97

   U <= 0 (would force N = 0):  0 at every D <= 400.   U < 2 (kills N >= 2):  0.
   U < 4 (kills N >= 4 under H2):  1147 groups (0.030%).
   Degrees D <= 400 with EVERY group killed:  NONE.
```

Wall 161 s on one core for `D <= 400`; a box01 job spec is **not** needed and the
cluster was left alone.

### 6.3 Why the unconditional filter can never fire, and what the H2 filter kills

Letting the lower `V_j -> infinity` in the closed form, `P_j/Q_j -> (n-M_j)/(n-M_{j-1})`,
the product telescopes and
`sup U = (u-v)(de/(d+e)) * V_s(n-M_{s-1})/(V_s(n-M_{s-1}) - d_s) > (u-v)de/(d+e)`.
Minimising over the data (`2V_s - d_s = 1`, so `u-v = K/d_s`; `d_s <= K/2`;
`(d,e) = (2,3)`) gives the asymptotic floor `2de/(d+e) = 12/5 = 2.4`; the measured
global minimum over 3 874 261 groups is `792/329 = 2.4073`. **`U > 2` always, so
`N <= U` never contradicts `N >= 2`.**

The `U < 4` kills are therefore confined to `(u-v)de/(d+e) < 4`, i.e.
`u - v < 4(d+e)/(de) <= 10/3`: **the H2 filter kills exactly (a subset of) the
skeletons whose top form is nearly balanced.** Measured over `D <= 200`:
`U_rob > (u-v)de/(d+e)` on all 120 641 groups (min ratio `342/341`), and every
killed group has `u - v in {2,3}` — e.g. `n = 90, m = 60, K = 30, d_s = 15,
V_s = 8, (u,v) = (16,14)`, `U = 192/79 = 2.430`.

### 6.4 What the filter delivers instead: a per-skeleton `N`-window

Over the **surviving** groups, the top of the forced window `min(U_rob,16)`:
at `D in [48,100]`, 3 896 groups, of which 2 197 have top `= 16` and 104 have
`N = 4` forced; at `D in [101,200]`, 116 385 groups, of which 96 930 have top
`= 16`, **19 455 (16.7%) get a window strictly inside `[4,16]`**, and **418 are
pinned to `N = 4`**. The tightest survivors at the MOH-SHARP-2 admissible degrees,
with full data — **these are the objects a realisability/endgame lane must
attack**, and they arrive with `N` already pinned:

```text
  D    m   K  (d,e)  M_2..M_s      V_s  (u,v)     1-delta_1  U_rob   N forced
 105  42  21  (2,5)  (-35, 103)     4  (12, 9)      21/83    4.337     4
 108  72  36  (2,3)  (-63, 106)     5  (20,16)      20/99    4.848     4
 112  32  16  (2,7)  (-24, 110)     5  (10, 6)      36/89    6.292     [4,6]
 117  78  39  (2,3)  (-65, 115)     8  (24,15)     45/119   10.891     [4,10]
 120  80  40  (2,3)  (-60, 118)    11  (22,18)     20/109    4.844     4
   (at D = 105 the same U_rob = 4.337 occurs for M_2 = -35, -28, -14, ...)
```

### 6.5 The theorem that is NOT available, stated exactly

The charge asked: *if none survive at every `D <= 200` for `N <= 16`, state the
theorem*. **Some survive at every `D <= 400`**, so there is no such theorem. For
the record, what is NOT proved: "every degree-minimal Jacobian counterexample with
`4 <= N <= 16` has `D <= 200`". The surviving count grows superpolynomially
(3 975 at `D <= 100`, 3 873 114 at `D <= 400`), and the obstruction is structural,
not computational: the skeleton bounds `N` above; a ceiling needs `N` bounded
**below**; and the free sub-tree of `D_1` can drive the contribution to `0`.

## 7. Part (5): controls on the filter

**(a) `N = 1` skeletons — accepted by the pairing, rejected by non-invertibility.**
`(y, x + y^k)` has `N = 1` and the pairing computes it exactly (CONTROL 2). On the
skeleton side `m = 1`, so `d_2 = gcd(n,1) = 1`: the chain dies at once, `s = 1 < 3`
(Prop 5.5), `d_s = 1 < 4` (Cor 6.1), `K = 1 < 16` (GGV Cor 6.6) — three
independent rejections, and the automorphism never enters the census.
Geometrically the same fact is `nu = 1`, i.e. `delta_s > -1`, which Prop 5.4 turns
into a degree reduction.

**(b) Non-Keller families — rejected at the Jacobian steps.** For each of the
seven two-tower rows the deliverable computes the bracket of the **top forms**,
`[l(f),l(g)]`, whose vanishing is the first consequence of the Jacobian condition
((LF)). Five of the seven have `[l(f),l(g)] != 0` and are rejected **there**; the
two with `l(f) = H^2`, `l(g) = H^3` pass (LF) with `(d,e) = (2,3)` and are rejected
at `K = gcd(m,n) in {2,4} < 16` (GGV Cor 6.6, itself a Jacobian theorem). All
seven have non-constant Jacobian (checked), so it is visible *which* step rejects
each.

**(c) Positive control on the recursion, and census-wide consistency.** Moh's
published `delta` columns reproduced exactly from an independent implementation of
Def 5.1(3): the four legible pairs `(1/4,9/16)`, `(2/7,16/21)`, `(1/4,7/12)`,
`(1/3,4/9)` all MATCH, and the two illegible `n = 75` rows are predicted
`(1/5,1/2)`, `(1/5,2/3)`, agreeing with DC's independent prediction; all Def 5.1(2)
windows hold and `delta_s = -1`, `u+v = K`, `u > v`, `a_{s-1} = ue`,
`b_i/a_i = m/n` on every row. RADIUS-ORDER, the product form of `lambda_g` and the
closed `N-CEILING` agree with the incremental computation on all 242 099
V-skeletons at `n <= 100` (0 failures); `delta_1 >= delta_{s-1} >= 0` and radii
strictly increasing downward on all 1 260 149 V-skeletons at `n <= 130`
(0 exceptions, consistent with Lemma 6.1) and on all 3 874 261 branch-robust
groups with `D <= 400`; the top-of-window `V` realises the branch-robust maximum
on all 3975 groups at `D <= 100` (0 mismatches against brute force).

## 8. Consequences, priced

```text
 A. CELLS KILLED: none.  No (B2)/(B3) cell emptied; case (A) untouched (EMPTY).
 B. MOH-CROSS (INT12/#14) UNCHANGED.  No bound D_min <= C(N) is produced; the
    OPPOSITE inequality N <= U(D-data) is, and it kills nothing there.
 C. NEW UNCONDITIONAL INEQUALITY: 1/N > 1/deg P + 1/deg Q, hence N < D/2, at a
    degree-minimal counterexample in Moh's gauge; at the MOH-SHARP-2 admissible
    degrees {105,108,112,117,120} the measured maxima give N <= 44.  First bound
    in the record constraining N by boundary data alone; it does not reach 16.
 D. NEW SEARCH CONDITION FOR MOH'S PROGRAM, condition (14):
        u d e (1 - delta_1)/(d + e)  >=  2   (unconditional),   >= 4 under H2.
    Free to evaluate; kills 1147 of 3 874 261 groups at D <= 400; Moh's four
    survivors pass it comfortably (4.3 .. 18.2).
 E. THE PROFILE LEDGER DOES NOT COMPOSE -- a typing fact, not a gap.  The charged
    items (W = N - a with the counting window, 2S <= W, mu_l >= 2, kappa <= N, the
    meridian floor n >= ceil((N-1)/(W-S)) + 1) live on the SOURCE side, and the
    meridian floor's n is deg Abar_F, NOT Moh's n = D.  Their only interaction
    with a skeleton is the interval they leave for N, which under H2 is
    4 <= N <= 16 -- precisely what the filter of sec.6 consumes.  kappa <= N
    follows from RAMIFICATION-FLOOR plus sum nu_gamma = D and adds nothing.
 F. OPEN[NU-BOUND-AT-A-PLACE] (DC) GETS ITS SIGN: the tree yields a FLOOR on
    nu_gamma, so the hoped ceiling nu_gamma <= h(m_gamma) is not obtainable from
    the boundary tree.  REFUTED DIRECTION, not a kill.
 G. NOT GAINED.  No bound on T, Psi, D or D_min; no cell emptied; no statement
    about realisability of any skeleton; nothing about case (A), A2, Z(G) or the
    reducible branch.
```

## 9. Corrections to charged inputs and to the source

```text
 C1. DC sec.9, OPEN[N-ON-THE-TREE] ("what is missing is the minor-disc
     distribution (Moh sec.6, Prop 6.1)") -- INVERTED.  Prop 6.1 is exactly what
     makes the minor discs contribute ZERO (DETECTOR-NULL); sec.6 supplies them
     completely.  What is missing is the sub-tree of the LAST MAJOR disc D_1,
     where Moh's minor criterion degenerates (n/(n+m) < 1) and there is no M_0.
     The charge's "enumerate the minor data as a further free datum with its exact
     size" is therefore not the task: the free datum is one bounded rational per
     bottom-major disc, ranging over [0, a_1(-lambda_f(delta_1))].
 C2. DC sec.9, same OPEN ("If the filter empties the census at every D, the
     ceiling is PROVED in that range") -- the filter CANNOT empty the census, for
     a reason internal to the instrument (sec.6.1).  Measured: U > 2 at every one
     of 3 874 261 groups with D <= 400, asymptotic floor 12/5.  The conditional
     was never satisfiable.
 C3. DC sec.5.1, the budget form of CONTACT-DEFICIENCY -- SCOPE, not error.  The
     positivity of the same-slope contact orders is Moh Lem 6.1 (delta_{s-1} >= 0)
     plus Prop 6.1 (delta*_{s-1} >= 1), not a consequence of "same leading
     coefficient": off that normalisation N > 2deuv occurs (5 of 7 control rows).
 C4. MKS sec.5.3 / Moh Appendix II "(64, 68)" -- CONFIRMED as (64,48) by an
     independent route: Appendix II's own reduced row is (16,12), and 68/4 != 12.
 C5. MOH sec.6 leading-form display (moh.txt:2884-2890) -- the OCR drops a stacked
     fraction; the exponent is n/d_s, not d_s.  Forced by deg = n, confirmed by
     a_{s-1} = ue on six rows.
 C6. MOH Theorem (5) (moh.txt:3243-3246) -- "the number of roots of g(y) in E_i is
     <= d_r/(n-M_r)" is the bound on the MULTIPLICITY V; in root counts,
     #roots <= n/(n-M_r).  Forced at r = s, where the printed form would make the
     minor slope class major and the corrected form is exactly NU-TWO's v <= u.
```

## 10. Opens raised, with bounded quantities

```text
OPEN[D1-SUBTREE]  (new; the exact residue of OPEN[N-ON-THE-TREE], which this lane
   otherwise CLOSES).  Below D_1 the Jacobian condition is unused.  BOUNDED
   QUANTITY: N|_{D_1} = sum_{rho in D_1}(-lambda_f(delta^0_rho))^+ in
   [0, a_1(-lambda_f(delta_1))], over a_1 = eV_2 roots of g and b_1 = dV_2 roots of
   f below radius delta_1.  A LOWER bound there -- any Jacobian-forced minimum of
   the deficiency at the bottom of the tower -- would be the first floor on N from
   boundary data and would make the filter of sec.6 two-sided.  This is the one
   place a "next pair" argument has never been run, because Moh's own criterion
   degenerates there.
OPEN[MOH-14]  (new; cheap).  Is search condition (14), u d e (1-delta_1)/(d+e) >= 2,
   implied by Moh's (7)-(13) or independent?  BOUNDED QUANTITY: the 1147 groups
   with D <= 400 that (14) kills; check each against (9)-(13) (the Lambda_{r-1}
   root-of-unity restrictions), not implemented here.
OPEN[UPPER-TO-FLOOR]  (new; the direction problem).  Every boundary-tree instrument
   in this campaign that touches N -- CONTACT-DEFICIENCY, FRONTIER-N, N-CEILING --
   yields N <= (something).  BOUNDED QUANTITY: the integer N in [2,16] at a
   degree-minimal counterexample.  Name one instrument that bounds N BELOW by a
   function of D.  Absent that, the ceiling D <= C(N) cannot be reached from the
   boundary at all, and the record should say so.
```

Carried unchanged: `OPEN[MOH-ENDGAME]`, `OPEN[NONPROPER-DEGREE]`,
`OPEN[SUBRECT-ORBIT-BRIDGE]`, `OPEN[ANTICANON-DEFECT]`, `OPEN[SAT-MASS]`,
`OPEN[DELTA-AFF-VS-N]`. **Retyped:** `OPEN[NU-BOUND-AT-A-PLACE]` — a floor, not a
ceiling (§8 F).

## 11. FALLACY-v2 audit

* **Flag/place/series.** Six degree-like integers separated by name at every use
  (§0); Moh's `n = D` and the campaign's `n = deg Abar_F` never appear in one
  expression, and the meridian floor is declared **non-composing** for exactly
  that reason (§8 E). Moh's `d_i`, the exponent `d` of `l(P) = alpha H^d` and
  GGV's `d_j` are three-way distinguished; `nu` (= 2) is never used as `nu_C` or
  `nu_gamma`. The three levels of the tree — major tower, minor discs, sub-tree of
  `D_1` — carry different theorems (Def 5.1(1); Prop 6.1; nothing).
* **Per-ray/exit-set charge.** No exit price, no `charge_basis` line. In
  FRONTIER-N each `g`-root is charged once at its own frontier; in N-CEILING the
  bottom-major discs are **disjoint** subsets of `D_{s-1}` (Moh Def 1.1(2)) and
  counted once. The slope split is a partition, checked arithmetically
  (`2deuv + de(u^2+v^2) = deK^2 = mn`) on all six Moh rows.
* **Carrier/attainment; floor/attainment.** `U` is used **only** as an upper
  bound; `N = U` is never asserted and `[2,U]` is reported as an interval;
  attainability of the top is stated **combinatorially** and explicitly **not** at
  the Jacobian level. `min U = 2.407` is MEASURED over an enumerated finite set,
  the accompanying `12/5` a derived asymptotic floor; `U > 2` beyond `D = 400` is
  **not** claimed.
* **Pole/interior; variable/ring map; prime label.** `lambda_h(delta) = ord_t
  h(sigma_delta)` is used only where `sigma_delta` is a genuine `pi`-root of `h`
  (Moh Prop 1.2); the `max(0,·)` is exactly the branch on `ord >= 0`, tested by the
  near-proportional row. Controls are over `Q` in `x, y`; Puiseux roots carry
  exponents as `Fraction` and coefficients as sympy radicals, compared by
  `simplify`. The resultant identity was tested with a **negative control** and
  fails exactly off the gauge. No prime is read as a derivative (`T_r` vs
  `T_r^psi`). No saturation, Groebner basis or quotient normal form anywhere.
* **OCR discipline; no cap or analogy.** Every quotation carries an extraction
  line number; the two destroyed displays are corrected by internal consistency and
  validated numerically (C5, C6); the recovered Def 5.1 is validated three ways;
  the illegible `n = 75` deltas are marked prediction. Abhyankar–Moh, Heitmann,
  van den Essen, Nagata are ABSENT from `refs/` and none is load-bearing
  (`K >= 16` comes from GGV Cor 6.6, present). FRONTIER-N, RADIUS-ORDER,
  DETECTOR-NULL, N-CEILING, HARMONIC-BOUND are proved here; the one statement
  imported without re-proof is Moh Prop 6.1(2) / Theorem (5), quoted with line
  numbers and flagged as the load-bearing reading.

## 12. Typed verdict block

```text
LANE       N-ON-THE-TREE  (successor OPEN[N-ON-THE-TREE] of DEPTH-CEILING)
SCOPE      Keller, noninvertible, degree-minimal, Moh's gauge (deg = deg_y, monic
           in y, two points at infinity).  CONTACT-DEFICIENCY and FRONTIER-N hold
           for every dominant F in that gauge.  Case (A) EMPTY and untouched; A2
           untouched; no Z(G)=1.  H2 only where the campaign N-window is quoted.

PROVED HERE  (all PROVED-HERE, UNREVIEWED; section numbers in brackets)
 CONTACT-DEFICIENCY [2]  N = deg_x Res_y(f-c1,g-c2) = -sum ord_t(tau-phi), gauge
     and generic-c hypotheses explicit; 7-row positive control + NEGATIVE control.
 FRONTIER-N [3]     N = sum_i (-lambda_f^{(i)}(delta^0_i))^+ on the tree of the
     roots of f*g alone.  VERIFIED exactly on 7 explicit-root rows.
 RADIUS-ORDER [4.2] lambda_g(delta_i) = -n prod_{j>i}P_j/Q_j = -n(1-delta_i)/(n-M_i)
     -- Moh's radius and the order of g are one datum.  242099 rows, 0 failures.
 DETECTOR-NULL [4.3]  Minor discs contribute EXACTLY ZERO to N (Moh Prop 6.1(2) /
     Theorem (5) + Def 3.1).  Inverts the charge's premise.
 N-CEILING [4.4]    N <= U = u d (-lambda_g(delta_1)) = u d e (1-delta_1)/(d+e);
     lambda_g(delta_1) >= 0 is impossible.
 HARMONIC-BOUND [4.4]  1/N > 1/deg P + 1/deg Q ; N < D/2.
 RAMIFICATION-FLOOR [4.4]  nu_gamma >= m_gamma/(-lambda_f(delta_1)) at proper
     places; retypes DC's OPEN[NU-BOUND-AT-A-PLACE] as a floor.
 FILTER-INVERSION [6.1]  The skeleton bounds N above and never below; "N <= 16"
     rejects nothing.  Operative test U >= N_min.

MEASURED     box/moh_skeleton_N.py: 100 controls, 0 failures, 42.3 s to D <= 200;
             filter to D <= 400 in 161 s (box/nott-drivers-20260902/filter400.log).
             Census re-calibrated (2410 at n <= 100; Moh's "25 values" to the unit).
             D <= 400: 3 874 261 branch-robust groups; U<2 kills 0; U<4 kills 1147;
             NO degree emptied; min U = 792/329 = 2.407, max U = 171.97.
             D in [101,200]: 19 455 of 116 385 survivors get a window strictly
             inside [4,16]; 418 are pinned to N = 4.
DECISION     THE CEILING IS NOT PROVED ON ANY RANGE BY THIS INSTRUMENT, and the
             reason is structural (FILTER-INVERSION), not computational.  The
             finite instrument the record wanted exists, runs, and answers the
             opposite question.  OPEN[N-ON-THE-TREE] is CLOSED; its residue is
             OPEN[D1-SUBTREE], and the campaign-level question is
             OPEN[UPPER-TO-FLOOR].
CORRECTED    DC's location of the missing data (minor discs -> the sub-tree of
             D_1); DC's satisfiability of its own filter conditional; the scope of
             CONTACT-DEFICIENCY's budget form; two OCR displays in Moh 1983.
CONFIRMED    DC's (64,68) -> (64,48) correction, by an independent route.

DISCLOSURE   (1) The one statement imported without re-proof is Moh Prop 6.1(2) /
                 Theorem (5) (minor discs are distribution detectors): quoted with
                 line numbers, displays intact in the OCR.  If it fails,
                 DETECTOR-NULL fails and N-CEILING loses its covering argument;
                 FRONTIER-N and RADIUS-ORDER are unaffected.
             (2) Def 5.1(1)-(4) and Prop 5.3 come from DC, a PROPOSAL; they are
                 re-implemented independently and validated three ways.  A
                 different reading would change every number in secs.4-6 but not
                 the shape of the verdict.
             (3) The branch count of the bottom-major discs is bounded crudely by
                 a_{s-1} = ue; Moh's search (8)-(11) would sharpen it and were NOT
                 implemented.  Sharpening lowers U and can only STRENGTHEN the
                 kills, so the reported kill counts are a floor.
             (4) "N >= 2" uses Ax-Grothendieck; "N >= 4" uses the campaign's H2
                 residual (INT#14 sec.C) and is typed as such at every use.
             (5) No box01 job was submitted; D <= 400 runs in 161 s on one core.
             (6) SIZE: body 44.6 KB against the charged 25-40 KB band.  The
                 overrun is the evidence: the control tables of secs.2.2, 5, 6.2
                 and 6.4 and the two OCR corrections of sec.4.1, kept complete
                 rather than compressed.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `44633`.
- Body SHA-256:
  `44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967`.
