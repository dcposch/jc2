# DEPTH-CEILING — the Puiseux depth at infinity of a degree-minimal Jacobian pair: the count is log-bounded, the size is free, and N is a quadratic functional the recursion never forms

Lane: `DEPTH-CEILING`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + desk-scale CAS (python3 3.14.7 / sympy 1.14.0 over `Q`; Singular
4.4.1 `hnoether.lib` for Hamburger–Noether expansions at infinity; no AWS, no
fetching, no web). Drivers in `/tmp/dc/depth`, not installed in `box/`. Wall time
< 12 min total, peak RSS < 400 MB.

## 0. Custody, method, scope

The five charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all five match the charge exactly:

```text
7b0ffec769314ce91a0831f7b2a88f5d5c8c97c08bfa56bd1e9bb8dbfb5c23f0  minimal-keller-shape-opus5-20260902.md
0b55a2c8bf7a8ab64fadf458e8a51bc5390bcb4808bd3c97d58a8769a97cc4a7  integration13-coordinator-fable51-20260902.md
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  integration12-coordinator-fable51-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  sat-mass-opus5-20260902.md
eed289e8fe1abf77b91e19c0aceea6b55c0300944f6b2eb9f5c5d471c330433b  APPROACHES.md
```

Abbreviations: **INT12/INT13** = the coordinator bindings, **MKS** =
MINIMAL-KELLER-SHAPE, **SM** = SAT-MASS, **GGV** = Guccione–Guccione–Valqui,
*On the shape of possible counterexamples to the Jacobian conjecture*, J. Algebra
471 (2017) (arXiv:1401.1784v3), **Moh** = T. T. Moh, *On the Jacobian conjecture and
the configurations of roots*, J. reine angew. Math. **340** (1983) 140–212.

Typing discipline as charged. INT12's polar ledger and INT13's genus/polar-tree set
are consumed at their **reviewed** typing; MI/THEOREM PROFILE, MF-EXACT, `7.B'`,
`(K)`, `H2` at banked typing. **MKS is a PROPOSAL**: every MKS statement used below
is either re-derived here or replaced; two of its readings are corrected (§8). Case
(A) is EMPTY and is not priced; no `Z(G)=1`; no A2 cell; no quasi-homogeneity. No
canonical ledger edited; `jc2-lean` not inspected; nothing fetched.
**No `charge_basis` line: this report asserts no new exit price.**

Local PDFs read this session, hashed, with the extraction hashes:

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
b6a369146240dbd36107907ebfb63ab2fc602abb524151d6ab31d39e5bc10722  (pdftotext -layout of the Moh PDF; line numbers below refer to it)
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
449d8028da79c7f2ae9eff9161553fcc35f75a48989f169c5d9ef54edf88773f  (pdftotext -layout of the GGV PDF; line numbers below refer to it)
```

**Display-equation trap, handled.** The Moh scan is ABBYY OCR and **drops every
displayed formula**, so Definition 5.1 and Proposition 5.3 — the recursion this lane
is charged with — are absent from the text layer. They were recovered by rendering the
pages (`pdftoppm -f 40 -l 41 -r 130`, journal pp. 179–180) and reading the images, then
**verified by reproducing Moh's own published `delta` table from the recovered
formula** (§6.1). This is the campaign's `PDF stacked-fraction trap` in its harsher
form: not inverted, *absent*. `refs/` contains **no** Abhyankar–Moh, Nagata,
Appelgate–Onishi, Heitmann, van den Essen, Cassou-Noguès/Kaliman or Jung–van der Kulk
item (checked by `ls`): all **ABSENT**, none load-bearing.

## 1. Verdict, up front

```text
(1) THE CHARGE'S PREMISE IS HALF WRONG, AND THE HALF THAT IS WRONG IS DECIDABLE.
    "the depth is free" is FALSE for the DEPTH AS A COUNT, TRUE for it AS A SIZE.
    THEOREM DEPTH-LOG (proved here from two independent refs/-verified sources):
         3 <= s <= log_2 K   (characteristic pairs),   k+1 <= log_2 K   (GGV corners),
    with K := gcd(deg P, deg Q) >= 16.  There is never "always a next pair"; the
    bound is attained.  What IS free is the SIZE of each pair: the exponent M_r
    (order n) and the multiplicity V_r (order d_r).
(2) THIS IDENTIFIES MOH'S OWN UNEXPLAINED STEP.  Moh (OCR 3275-3277): "d_s >= 4.  A
    simple computation shows that s <= 5."  That computation is DEPTH-LOG at
    n <= 100:  n >= 4*2^{s-2}, and 4*2^4 = 64 <= 100 < 128.  s <= 5 is a CONSEQUENCE
    OF THE CUTOFF, not a theorem; at n <= 400 it reads s <= 7.  Measured: max s
    observed = max floor(log_2 K) at every n tested.
(3) T IS NOT A DEPTH.  In place form (THEOREM PLACE-LEDGER, re-derived and measured
    here by Hamburger-Noether at infinity, 16/16 rows):
       D = sum nu_gamma , N = sum m_gamma , T = sum (nu_gamma - 1) , r_inf = D - T
                                                                          = kappa + Sn,
    over the places at infinity of a generic member of the net, nu_gamma =
    I(gamma,L_inf), m_gamma = the pole order of P.  So T is the total DEGREE EXCESS of
    those places -- the total ramification of x over x = infinity in gauge deg = deg_y.
    The pair count at a place is <= log_2 nu_gamma.  T ~ D/2 (HALF-CAP) while the pair
    count is ~ log_2 D: "T = the Puiseux depth" is a size, not a depth.
(4) WHERE N IS, EXACTLY.  N is NOT absent from Moh's world -- it is a QUADRATIC
    functional of the very tree he computes (THEOREM CONTACT-DEFICIENCY, here):
       N  =  - sum_{i,j} ord_t( tau_i - phi_j )  =  2deuv - sum_{same-slope} ord_t ,
    tau_i the n roots of g - c_2, phi_j the m roots of f - c_1 in t = x^{-1},
    H = L_1^u L_2^v the primitive leading form.  BUT every constraint Moh derives
    (Lem 2.1; Prop 4.4/4.6; Def 5.1; Prop 5.3; Thm (4)-(7); search (1)-(13)) and every
    GGV corner condition (Prop 6.4-6.7, Thm 7.6, 7.11) is about RADII and COUNTS ALONG
    ONE MAJOR TOWER; none forms the pairing sum.  The recursion is not blind to N in
    principle, only in practice -- and the missing instrument is named and finite.
(5) UNCONDITIONAL GAIN: D_min >= 105, up from MKS's 102 (THEOREM MOH-SHARP-2:
    D_min = Ke, K >= 16, e >= 3, K neither p nor 2p -- GGV Cor 7.9's argument applied
    at K = a+b rather than at B, legitimate by GGV Prop 4.7's v_{1,1}-preservation).
    Admissible D in [101,120] = {105,108,112,117,120}; 30 of 100 survive in [101,200].
(6) OPEN[NU2-RIGIDITY] (MKS) CLOSED POSITIVE, GAUGE-FREE: Moh Prop 4.5 + Lem 5.3 +
    Prop 5.4 give, in ANY gauge with deg = deg_y, a leading form with EXACTLY TWO
    distinct linear factors of DIFFERENT multiplicities, and M_s = n-2.  So nu = 2 and
    E_0 is free without the subrectangular reduction: MKS's E0-FREE is gauge-free.
(7) MEASURED.  Moh's published delta columns reproduced EXACTLY from the recovered
    Definition 5.1(3) (6 of 6 legible values; the illegible row predicted).  His
    "25 possible values for M_2" at (75,50) reproduced to the unit.  16/16
    place-ledger rows, 0 failures, 0 skips; SM's kappa, Lambda, T and nu_max columns
    all reproduced from an independent route (no blow-ups).
(8) CORRECTIONS TO CHARGED INPUTS.  MKS's cross-validation of MOH-SHARP rests on an
    OCR misreading: Moh's fourth surviving pair is (64,48) = 16*(4,3), not "(64,68)
    = 4*(16,17)"; ALL FOUR of Moh's survivors have K >= 16 and NONE is killed by GGV
    Cor 6.6.  The MOH-SHARP inequality itself is unaffected and is strengthened in (5).
```

## 2. Part (1): the object, stated — and the three depths kept apart

### 2.1 Set-up and gauge

`(P,Q)` is a Jacobian pair over `C`: `[P,Q] := P_xQ_y - P_yQ_x in C^*`. A
*counterexample* is a non-invertible such pair. `D := max(deg P, deg Q)`,
`K := gcd(deg P, deg Q)`. **Degree-minimal** means no `psi x chi in Aut x Aut` lowers
`D`; `D_min` is the minimum (INT12, PROMOTED).

Two degree-preserving gauges appear and must not be confused. **(GEN)**: a *generic
linear* change making `deg = deg_y` for both coordinates, both monic in `y`, and
(after a shear `y -> y + lambda x`) neither leading form divisible by `y`. This is
Moh's gauge (`moh.txt:527-529`, `3266`); being linear it preserves degree-minimality.
**(SUBRECT)**: the Makar-Limanov / van den Essen subrectangular gauge used by MKS —
non-linear, degree-preserving, and *different* (in (GEN) the leading form is monic in
`y`, in (SUBRECT) a monomial `x^u y^v`). Both give `nu = 2`; nothing below needs
(SUBRECT). Throughout `t := x^{-1}`, Puiseux series in `C<t>`, `ord` the `t`-adic
order.

### 2.2 The leading-form data, and the two points at infinity

`[l(P), l(Q)] = 0` for the top forms, so `l(P) = alpha H^d`, `l(Q) = beta H^e` with
`gcd(d,e) = 1`, `deg H = K`, `deg P = Kd`, `deg Q = Ke` (proved in MKS §2.1 and
re-proved here in one line; the statement is classical and is *not* carried from an
ABSENT source). Degree-minimality forces `d, e >= 2` and `d != e`, hence
`max(d,e) >= 3` and `D = K max(d,e) >= 3K` (GGV Rem 4.2, `gv.txt:718`).

> **THEOREM NU-TWO (VERIFIED in `refs/`, gauge-free).** In the gauge (GEN), for a
> degree-minimal counterexample,
> ```text
>     H = L_1^{u} L_2^{v} ,   L_1, L_2 distinct linear forms,  u + v = K,  u != v,
>     nu := #{distinct roots of H} = 2 ,     M_s = n - 2 .
> ```
> *Source, firsthand.* Moh **Prop 4.5** (`moh.txt:1594-1597`): the top forms of `g`
> and of the `T_i` "are powers of a common form which has **at most two distinct
> linear factors**. Moreover the multiplicities for the two factors are
> **different**" — the preceding remark (`1589-1591`) reads this as "at most two
> points at infinity for `f(x,y)=0`". **Lemma 5.3** (`2453-2457`): the smallest disc
> containing all roots of `g T_1` has logarithmic radius `-1` **iff** `M_s = n-2`
> **and** the top form of `g` has **two** roots. **Prop 5.4** (`2321-2330`): if that
> radius is `> -1` then either `k[x,y] = k[f,g]` (invertible) or an automorphism
> lowers `deg f` and `deg g` simultaneously (non-minimal). ∎

**This closes `OPEN[NU2-RIGIDITY]` (MKS §8) POSITIVE.** MKS proved `nu = 2` only in
(SUBRECT); Moh's Prop 4.5 gives it in (GEN), a *linear* gauge, so `nu = 2` is an
invariant of the pair, not of a reduction. MKS's `E0-FREE` and the withdrawal of KPG's
CH2 kills are therefore **gauge-free**, and `u != v` is banked.

### 2.3 The three depths — kept apart (FALLACY-v2: flag/place/series)

Three integers are all called "the depth at infinity" in the charge and in the record.
They are different objects with different bounds.

```text
 (d1) s   = # EFFECTIVE CHARACTERISTIC PAIRS OF THE PAIR (Moh sec.2): the tree data
            {M_i,d_i} of the roots of the defining equation of f over k[x][g], i.e.
            the characteristic sequence of the rational curve y |-> (f(0,y),g(0,y))
            at y = infinity (moh.txt:106-109, 541-573).  d_1 = n, d_2 = gcd(n,M_1) =
            gcd(m,n) = K, d_{i+1} = gcd(d_i,M_i).  TARGET-side.  3 <= s <= log_2 K.
 (d2) k+1 = # GGV REGULAR CORNERS (gv.txt:1039, 2115), a SOURCE Newton-polygon
            object.                                            k + 1 <= log_2 K.
 (d3)       CHARACTERISTIC PAIRS OF THE BRANCHES AT INFINITY of a generic member --
            the object the campaign's cluster resolves.  At a place: <= log_2 nu_gamma.
 (T)  T   = sum_C (nu_C - 1) c_C is NONE of these: a WEIGHTED SIZE of order D/2
            (HALF-CAP), while (d1)-(d3) are ~ log_2 D.
```

The campaign's `nu_C` (source polar multiplicity, SM) and this lane's `nu`
(`#` roots of the top form, MKS) are also distinct and are written out everywhere.

### 2.4 THEOREM PLACE-LEDGER — the whole boundary ledger as a sum over places

Let `C_gen` be a generic member of the net `<P^h z^{D-deg P}, Q^h z^{D-deg Q}, z^D>`
(affinely, `{aP + bQ + c = 0}` with `(a,b,c)` generic), and let `gamma` run over its
places at infinity. Put `nu_gamma := I(gamma, L_infty)` and
`m_gamma := -ord_gamma(P|_{C_gen})` (the pole order).

> **THEOREM PLACE-LEDGER (every dominant `F`; re-derivation of SAT-WEIGHT and
> DEG-SPLIT in place form).**
> ```text
>    D = sum_gamma nu_gamma ,        N = sum_gamma m_gamma ,
>    T = sum_gamma (nu_gamma - 1) ,  r_inf(C_gen) = #{gamma} = D - T ,
>    kappa = #{gamma : m_gamma > 0}  (the PROPER places) ,
>    S n   = #{gamma : m_gamma = 0}  (the NON-PROPER places) ,
>    hence  D = T + kappa + S n      [= DEG-SPLIT].
> ```
> *Proof.* After full resolution `C~_gen` is smooth, meets the boundary
> transversally, and lies in the class `Z = DH - sum a_i E_i`. Hence
> `C~_gen . C = Z.C = c_C` for every boundary component, so `C` carries `c_C` places
> and `#{gamma} = sum_C c_C = D - T` (SM §2.4). Each place inherits its component's
> invariants, `nu_gamma = nu_C`, `m_gamma = m_C`, so `sum nu_gamma = sum_C nu_C c_C = D`
> and `sum m_gamma = sum_C m_C c_C = N` (SAT-WEIGHT, re-derived); `m_C = 0` exactly on
> the dicriticals, whence the two counts. ∎

Two readings that matter here.

* **In (GEN), `nu_gamma` is a ramification index.** `deg_y G = deg G = D` makes `y`
  integral over `C[x]` on `C_gen`, so every place at infinity lies over
  `x = infinity` and `nu_gamma = e_gamma`. Hence `T = sum(e_gamma - 1)` is **the total
  ramification of `x` on `C_gen` over `x = infinity`** — not a depth, a ramification
  number. `T = 0` iff every place is smooth and transverse to `L_infty` (SM's C1).
* **`N` lives only on the proper places.** `m_gamma = 0` at the `Sn` non-proper places,
  which still contribute `nu_gamma - 1 >= 0` to `T`. **Any bound `T <= f(N)` must bound
  `sum_{non-proper}(nu_gamma - 1)`, which `N` does not see at all** — the place-form of
  `OPEN[NU-BOUND]`.

**Keller cross-check (UNIT-SPEED in place form).** `dP|_{C_gen}` is nowhere zero on
the affine curve (Gelfand–Leray), so
`2g_L - 2 = -N - kappa + sum_{np}(mu_gamma - 1)`; with GENUS-DEFECT
`Z.K_X = 2g_L - 2 - N` and NOETHER-K `Z.K_X = -2N - kappa + n(W-S)` this gives
`sum_{np}(mu_gamma - 1) = n(W-S)`, `sum_{np} mu_gamma = nW`, and with DEG-SPLIT
```text
    (KL)     T  =  D + N + 2 g_L - 2 - n W .
```
Control: `(x, y+x^k)` has `D=k, N=1, g_L=0, W=0`, so `T = k-1` — SM's measured value.
`(KL)` is an identity equivalent to the reviewed ledger, recorded because it is the
form in which `T`, `N` and the genus sit on one line.

### 2.5 Characteristic sequence, satellite chains, `T`; and the approximate roots

At a place `gamma` the free chains of the Enriques tree are the integral parts of the
Puiseux exponents at infinity, the satellite chains the continued-fraction expansions
of the fractional parts, and `nu_C` on a chain is the continuant of that expansion,
with `nu_gamma = I(gamma, L_infty)` at the top. If the branch has Puiseux
characteristic `(p; q_1, ..., q_h)` in `t`, then `nu_gamma = p` and the number of
characteristic pairs is `h <= log_2 p`, because
`p = c_0 > c_1 = gcd(p,q_1) > ... > c_h = 1` is a strict divisor chain. **So the depth
at a place is logarithmic in its own degree, while `T = sum(nu_gamma - 1)` sums the
degrees, not the depths.**

Moh's `T_r(f,g)` are the `d_r`-th approximate roots of the defining equation of `f`
over `k[x][g]` (`moh.txt:652-654`), with `deg_y T_r = -mu_r` (Prop 2.2(1),
`moh.txt:680`); the search takes `f = T_1` without loss (`moh.txt:3262`). They are the
algebraic surrogate for the analytic characteristic data, specialised at `x = 0`
(Prop 2.1). **Controls, written out.**

```text
 F = (x, y + x^k):  the automorphism.  In (GEN) (here x -> x + a y) the leading form
      is a single linear form to the k-th power:  nu = 1, and by NU-TWO the pair
      is not degree-minimal -- which is correct, it IS invertible.  Place data:
      ONE place, nu_gamma = k, m_gamma = 1, mu-data empty; D = k, N = 1, T = k-1,
      kappa = 1, Sn = 0, r_inf = 1.  Measured (sec.6.2), 4 values of k.
 Jacobian-pair normal form (Moh, GEN):  f, g monic in y, deg = deg_y,
      m = Kd < n = Ke, l(f) = alpha H^d, l(g) = beta H^e, H = L_1^u L_2^v, u != v,
      M_1 = -m, M_s = n-2, and (Lemma 2.1, moh.txt:600-604) the characteristic
      exponents terminate at n-1:  gcd(d_i, n-1) = 1 for every d_i | n, d_i > 1.
```

## 3. Part (2): the recursion, written down exactly

### 3.1 Moh's tower recursion (recovered from the page images, then verified)

Fix `g` monic in `y` of `y`-degree `n > 1`, characteristic data `{M_i, d_i}`,
`d_{i+1} = gcd(d_i, M_i)`, `s` = index of the last effective pair.

> **DEFINITION 5.1 (Moh, p.179).** A tower of major discs
> `D_s ⊋ D_{s-1} ⊋ ... ⊋ D_r` satisfies, with integers `{V_i : i = r+1, ..., s+1}`:
> ```text
>  (1) D_i contains precisely  (n / d_{i+1}) V_{i+1}   roots of g(y),
>      and precisely  (-mu_j / d_{i+1}) V_{i+1}  roots of T_j(y), j = 1..i ;
>  (2) V_{i+1} d_i / d_{i+1}  >=  V_i  >  d_i / (n - M_i)   for i = r+1..s,
>      and  V_{s+1} = d_{s+1} ;
>  (3) D_i has logarithmic radius
>
>                    (n - M_i)      prod_{j=i+1}^{s} [ V_j (n - M_j)     - d_j ]
>      delta_i = 1 - ---------------------------------------------------------- ;
>                    (n - M_s - 1)  prod_{j=i+1}^{s} [ V_j (n - M_{j-1}) - d_j ]
>
>  (4) for sigma_i the unique general point of D_i, the conditions of Prop 4.6 hold
>      with sigma = sigma_i, delta = delta_i, v = V_{i+1} (d_i / d_{i+1}).
> ```

> **PROPOSITION 5.3 (Moh, p.180) — THE "NEXT PAIR" STEP.** Given the tower down to
> `D_r`, let `pi - C_r` be a factor of `p(pi)` (the leading polynomial of Prop 4.6)
> with multiplicity `V_r` satisfying
> ```text
>      deg p(pi) = V_{r+1} ( d_r / d_{r+1} )  >=  V_r  >  d_r / (n - M_r) .
> ```
> Then the next disc has
> ```text
>                     (n - M_{r-1})  prod_{j=r}^{s} [ V_j (n - M_j)     - d_j ]
>   delta_{r-1} = 1 - --------------------------------------------------------- ,
>                     (n - M_s - 1)  prod_{j=r}^{s} [ V_j (n - M_{j-1}) - d_j ]
> ```
> and `D_s ⊋ ... ⊋ D_r ⊋ D_{r-1}` is again a tower of major discs.

This *is* the recursion the charge asks for, in its exact published form. Read at
`i = s` (empty products) it gives `delta_s = -1/(n - M_s - 1)`, and with `M_s = n-2`
(NU-TWO) `delta_s = -1` — Moh's Lemma 5.3 normal form.

**The free datum at each step, exactly.** Passing from level `r` to `r-1` one chooses
the next characteristic exponent `M_{r-1} in (-m, M_r)` with
`gcd(d_{r-1}, M_{r-1}) = d_r` (`O((n+m)/d_r)` choices) and the multiplicity `V_r` in
`(d_r/(n-M_r), V_{r+1}d_r/d_{r+1}]` (`<= d_r <= K` choices) — and nothing else:
`delta_{r-1}` is then determined. At the last step (`M_s = n-2`,
`V_{s+1} = d_{s+1} = gcd(d_s,n-2) in {1,2}`) the window collapses to
`d_s/2 < V_s <= d_s`, i.e. `ceil(d_s/2)` choices — 2 for `d_s = 4`, 17 for `d_s = 33`.

**So "always a next pair" is a THEOREM with an exactly sized free parameter, not a
conjecture.** The Jacobian condition enters twice: through Lemma 2.1 (the exponents
terminate at `n-1`, `f_{n-1}` constant) and through Prop 4.4/4.6, whose numerical
criteria decide splitting vs. non-splitting and make `delta_{r-1}` a *formula* rather
than a free radius.

### 3.2 GGV's corner recursion, in the same terms

GGV's regular corners `(A_0,(rho_0,sigma_0)), ..., (A_k,(rho_k,sigma_k))`
(`gv.txt:1039, 2115`) are the source-side avatar, and Theorem 7.6 (`gv.txt:2115-2160`)
is the recursion: with `d_j` maximal such that `l_{rho_j,sigma_j}(P) = R_j^{m d_j}`
and `en_{rho_j,sigma_j}(F_j) = (p_j/q_j)(1/m) en_{rho_j,sigma_j}(P)`, one has
`q_i ∤ d_i` (i>0), `q_j | d_i` (i>j>0), `q_i ∤ q_j` (i>j>0),
`d_j | D_j := gcd(a_j,b_j,a_{j-1},b_{j-1})` with `Omega(D_j) >= Omega(d_j) >= j-1`,
and (type II) `q_0 | d_i`, `Omega(d_i) >= i`. The first corner is pinned by Prop 6.4
(`gv.txt:1596`: `s' < r' < u < v`, `2 <= f_1 < u`, `gcd(u,v) > 1`, `u f_2 = v f_1`,
`rho <= u`), Prop 6.5/6.7 (`v_{1,1}(A_0) >= 16`, `u >= 4`, `v <= u(u-1)`) and Thm 7.11
(`v_{1,1}(A_0) > 20`, or the single exception `A_0 = (4,12)`). **The free datum is the
pair `(A_j, (rho_j,sigma_j))` at each corner; the ladder `Omega(d_j) >= j-1` is the
corner-side twin of Moh's `d`-chain.**

## 4. THEOREM DEPTH-LOG — the count is bounded, twice

> **THEOREM DEPTH-LOG.** Let `(P,Q)` be a degree-minimal Jacobian counterexample,
> `K = gcd(deg P, deg Q)`.
> ```text
>  (a) [Moh side]   3 <= s <= log_2 K   for the effective characteristic pairs.
>  (b) [GGV side]   k + 1 <= log_2 K    for the regular corners.
>  (c) Both are attained by the numerical data (census, sec.6.3).
>  (d) At n <= 100 (a) reads s <= 5, and at n <= 400 it reads s <= 7.
> ```
> *Proof of (a).* `d_1 = n`, `d_2 = gcd(n, M_1) = gcd(n,m) = K` because `M_1 = -m`
> (Moh's search (1), `moh.txt:3258`; (5), `moh.txt:3273`). By definition of the
> characteristic data `d_{i+1} | d_i` and `d_{i+1} < d_i`, hence `d_{i+1} <= d_i / 2`.
> Moh's Corollary 6.1 gives `d_s >= 4` (`moh.txt:3275`). Therefore
> `K = d_2 >= 2^{s-2} d_s >= 4 * 2^{s-2} = 2^s`, i.e. `s <= log_2 K`. The lower bound
> `s >= 3` is Moh's Prop 5.5 (`moh.txt:2509-2513`: `s = 2` forces invertibility or a
> simultaneous degree reduction) together with Prop 5.4; both are recorded in his
> conclusion (6) (`moh.txt:3277`). ∎
> *Proof of (b).* By Thm 7.6(7), `Omega(d_k) >= k-1`, so `d_k >= 2^{k-1}`. By the
> proof of Cor 7.9 (`gv.txt:2270-2280`), `d_k | gcd(a,b)` where
> `(a,b) = (1/m) en_{1,0}(P)`, and `a < b` (Thm 2.6(4)) with `a + b = K` (Prop 4.7:
> `en_{1,0}(P) = st_{1,1}(P)`, and `v_{1,1}(st_{1,1}(P)) = deg P = mK`). Hence
> `2^{k-1} <= d_k <= gcd(a,b) <= a < K/2`, so `k < log_2 K`. ∎

**Consequence for the record.** APPROACHES row 1's stuck-point is quoted as
`No degree/td ceiling ("always a next pair", G)`. At the level of the *pair count*
that reading is refuted: there are at most `log_2 K` pairs, and Moh's own `s <= 5` is
that bound at his cutoff. The farm stalls not because pairs never stop but because at
each fixed depth the number of admissible *sizes* grows with the degree, and because
there is no uniform endgame for a surviving skeleton (§6.4).
**Cross-consistency:** `s >= 3` and `d_s >= 4` alone force `K >= 2d_s >= 8`;
Heitmann/GGV's `K >= 16` is a factor 2 stronger, and the agreement of two disjoint
`refs/` arguments is a check on both.

## 5. Part (3): the ceiling in depth form — where `N` enters, and where it does not

### 5.1 `N` is a contact deficiency: the exact expression in Moh's tree

> **THEOREM CONTACT-DEFICIENCY (proved here; every dominant `F` with both
> coordinates monic in `y` of `y`-degree = degree).** Let `phi_1..phi_m` be the roots
> of `f - c_1` and `tau_1..tau_n` the roots of `g - c_2` in `C<t>`, `t = x^{-1}`, for
> generic `(c_1,c_2)`. Then
> ```text
>     N  =  deg_x Res_y (f - c_1, g - c_2)  =  - sum_{i=1}^{n} sum_{j=1}^{m} ord_t(tau_i - phi_j) .
> ```
> If moreover `l(f) = alpha H^d`, `l(g) = beta H^e` with `H = L_1^u L_2^v` and both
> slopes nonzero (achieved by a shear inside (GEN)), then, splitting the pairs by
> slope,
> ```text
>     N  =  2 d e u v  -  sum_{same-slope pairs} ord_t(tau_i - phi_j) .
> ```
> *Proof.* Both are monic in `y`, so `Res_y = prod_{i,j}(phi_j - tau_i)` exactly, a
> polynomial in `x`; for generic `(c_1,c_2)` the common zeros are transverse and have
> distinct `x`-coordinates, so `deg_x Res = N`. `deg_x = -ord_t`. Roots with different
> leading coefficients have `ord_t(tau - phi) = -1` and there are
> `(eu)(dv) + (ev)(du) = 2deuv` such pairs; the rest have the same leading
> coefficient, so `ord_t > -1`. ∎

**Reading.** `N` is the *failure of contact at infinity* between the two generic
fibres, distributed over the `mn` root pairs: a **quadratic functional of exactly
Moh's tree data**, since Def 5.1(1) records how many roots of `g` and of each `T_j`
lie in each disc and `ord_t(tau_i - phi_j)` is the logarithmic radius of the smallest
disc containing both. With `f = T_1` (Moh's normalisation) the `phi_j` are literally
the roots he tracks.

**Budget form.** With `(MIN)` (`d >= 2, e >= 3`), NU-TWO (`u != v`, `u+v = K`) and
`K >= 16` one has `uv >= K-1 >= 15`, so
`sum_{same-slope} ord_t(tau_i - phi_j) = 2deuv - N >= 180 - N`. Sharper, uniformly in
the data: `2deuv >= 2 d (D/K)(K-1) >= 4D(K-1)/K >= (15/4) D`, so at the true floor
`D_min >= 105` (§7) the same-slope contact total is `>= 394 - N`. A counterexample
with `N <= 16` must therefore accumulate **at least 378 units of positive contact
order among its same-slope root pairs** — the exact quantitative form of "the branches
at infinity are extremely tangent". It is an identity, not an obstruction: the
individual `ord`'s are unbounded above.

### 5.2 Is `T` bounded by `N`? — the free datum, named and located

Combining PLACE-LEDGER with CONTACT-DEFICIENCY:

```text
     T  =  sum_{proper} (nu_gamma - 1)  +  sum_{non-proper} (nu_gamma - 1) ,
     N  =  sum_{proper} m_gamma ,     m_gamma = 0 on the non-proper places.
```

* **The non-proper half is invisible to `N`.** The `Sn` non-proper places contribute
  nothing to `N` and `nu_gamma - 1 >= 0` each to `T`.
* **The proper half is also free, already in the control class.** `(x, y+x^k)` has one
  proper place with `m_gamma = 1` and `nu_gamma = k`: the ratio `nu/m` is unbounded
  at a single proper place. Degree-minimality removes this witness (it is invertible)
  but nothing in the recursion replaces the bound.
* **The recursion never forms either sum.** Every Moh condition — Lemma 2.1; Prop 4.4
  (non-splitting) and 4.6 (splitting); Def 5.1(1)–(4); Prop 5.3; the Theorem's (4)–(7)
  (`moh.txt:3205-3225`); the search list (1)–(13) (`moh.txt:3256-3320`) — and every
  GGV condition — Prop 6.4(1)–(9), 6.5, 6.7, Thm 7.6(1)–(8), Prop 7.8, Cor 7.9,
  Thm 7.11 — constrains `(n,m,M_i,d_i,V_i,delta_i)` resp. `(A_j,rho_j,sigma_j,d_j,q_j,p_j)`:
  radii and counts along ONE major tower, or one corner chain. **The geometric degree
  `N`, the proper/non-proper split, and the pairing `sum_{i,j} ord(tau_i - phi_j)` do
  not occur anywhere.**

> **VERDICT (3), typed.** `T <= tau(N)` does **not** follow from the depth recursion,
> and the obstruction is not "the depth is free" — the depth (count) is `<= log_2 K`.
> The free datum is the pair `(M_r, V_r)` at each of the `<= log_2 K` steps, of sizes
> `O(n/d_r)` and `O(d_r)`; `T` is a *size*, assembled from them, and the recursion
> constrains sizes only through the `delta` formula, which is blind to the
> proper/non-proper split that defines `N`.

**Numerical artefact or realisable?** At the *numerical* level it is unobstructed:
fix `(N,W,S,kappa)` and a place list, raise `nu_gamma` at one place, and `D`, `T` grow
with every PLACE-LEDGER identity intact — SM's LEDGER-BLIND in place form, realised by
honest polynomials (`psi_k o (x, x y^m)`, non-Keller). At the *Jacobian* level the
census (§6.3) shows the skeleton space non-empty and growing at every degree reached,
but a skeleton is not a polynomial: Moh's four `n <= 100` survivors were all killed by
bespoke elimination. **The free datum is real at the level of the recursion and
unresolved at the level of realisability — the GGV farm's "modular only" status
(APPROACHES row 1) restated in Moh's variables.**

## 6. Part (4): Moh's method revisited — what limited it to 100

### 6.1 Positive control: the published `delta` table reproduced exactly

Moh's §6 table (`moh.txt:3325-3340`) lists, for the four surviving degree data, the
columns `V_3, V_2, delta_2, delta_1`. Recomputing them from the recovered Definition
5.1(3) (driver `mohrec.py`, `sha256 2b8e80e1...`):

```text
 n    m   M_2  M_s=n-2  d-chain          V=(V_2,V_3,V_4)  delta_3  delta_2   delta_1   published
 64  48    52     62    64,16,4,2        (3, 3, 2)          -1      1/4       9/16     1/4 , 9/16   MATCH
 84  56    64     82    84,28,4,2        (2, 3, 2)          -1      2/7      16/21     2/7 , 16/21  MATCH
 84  56    72     82    84,28,4,2        (5, 3, 2)          -1      1/4       7/12     [1/4],[7/12] MATCH
 99  66    77     97    99,33,11,1       (8, 8, 1)          -1      1/3       4/9      1/3 , 4/9    MATCH
 75  50    55     73    75,25,5,1        (3, 4, 1)          -1      1/5       1/2      OCR illegible
 75  50    55     73    75,25,5,1        (2, 4, 1)          -1      1/5       2/3      OCR illegible
```

**Six of six legible published values reproduced exactly**, and every `V_i` lies in
the Def 5.1(2) window (checked and printed by the driver). The two `n = 75` rows are
this lane's **prediction** for the entries the scan destroyed. Every one of the four
rows has `s = 3` effective pairs, `d_s in {4,4,5,11} >= 4`, `K in {16,28,25,33} >= 16`
and `(e,d) in {(4,3),(3,2),(3,2),(3,2)}`.

### 6.2 Positive control: the place ledger, measured independently

`places.py` (`sha256 8f02f149...`) computes the places at infinity of the generic
member `5P - 3Q + 7` by Hamburger–Noether expansion (Singular `hnoether.lib`) in the
two charts at each point of `L_infty` — **no blow-up, no cluster, no `Z`** — and
compares `D - r_inf` with the `T` published in SM §3 / MKS §6.5.

```text
 map                      D  r_inf  D-r_inf  T(pub)   nu list        kappa+Lam(pub)
 (x, y+x^2)               2     1       1       1     [2]                 1+0
 (x, y+x^3)               3     1       2       2     [3]                 1+0
 (x, y+x^4)               4     1       3       3     [4]                 1+0
 (x, y+x^6)               6     1       5       5     [6]                 1+0
 (x, xy)                  2     2       0       0     [1,1]               1+1
 (x, y^2)                 2     1       1       1     [2]                 1+0
 (x, xy^2)                3     3       0       0     [1,1,1]             2+1
 (x, x^2 y)               3     2       1       1     [1,2]               1+1
 (x, x^2 y^2)             4     3       1       1     [1,1,2]             1+2
 (x^2 y, y)               3     3       0       0     [1,1,1]             2+1
 psi_2 o (x,xy^2)         6     3       3       3     [1,1,4]             1+2
 psi_2 o (x,xy^3)         8     3       5       5     [1,1,6]             1+2
 psi_3 o (x,xy^3)        12     4       8       8     [1,1,1,9]           1+3
 psi_4 o (x,xy^2)        12     5       7       7     [1,1,1,1,8]         1+4
 (x^3, y^2)               3     1       2       2     [3]                 -
 (x^2, y^3)               3     1       2       2     [3]                 -
                                            16 rows, 0 failures, 0 skips
```

`r_inf = D - T` on every row; `sum nu_gamma = D` on every row; `r_inf = kappa + Lam`
on all 14 rows where SM publishes `kappa` and `Lam`; and `max nu_gamma` reproduces
SM's `nu_max` column entry for entry (`k`, `1`, `2`, `1`, `2`, `2`, `1`, `4`, `6`,
`9`, `8`). The last row was run separately with a 900 s Singular budget and its value
was **predicted before it was computed** (`r_inf = 5`, `nu = [1,1,1,1,8]`). The
resultant control (`res.py`, `sha256 b372c33c...`) confirms
`N = deg_x Res_y(P-c_1, Q-c_2)` on every row where **both coordinates are monic in
`y`** and shows it failing exactly where they are not — the hypothesis of
CONTACT-DEFICIENCY is load-bearing and was tested with a negative control.

### 6.3 The census: what the search space does

`census2.py` (`sha256 008e46fa...`) enumerates the *numerical characteristic
skeletons* `(n, m, [M_1 = -m, M_2, ..., M_s = n-2])` obeying only conditions read
firsthand: the divisor chain `d_1 = n > d_2 = K > ... > d_s >= 4` (Moh search (5),
Cor 6.1), `s >= 3` (Prop 5.5), `M_s = n - 2` (NU-TWO), `m = Kd`, `n = Ke`,
`gcd(d,e) = 1`, `2 <= d < e` ((MIN)), and `K >= 16` (GGV Cor 6.6 — which Moh did not
have).

**Calibration, to the unit.** At `(n,m) = (75,50)` Moh writes "there are 25 possible
values for `M_2`" (`moh.txt:3341-3344`). The multiples of `d_3 = 5` in `[-50,74)`
number **exactly 25**; adding `gcd(25,M_2) = 5` (i.e. `M_2` a genuine characteristic
exponent) removes the 5 multiples of 25 and leaves **20** — the census count. The two
enumerations differ by exactly those 5 degenerate values.

```text
    n   #skeletons   cumulative   max s   max floor(log_2 K)
   64          70          195      4          4
   75          20          426      3          4
   84          84          889      4          4
   96         872         2010      5          5
   99          10         2020      3          5
  128        1479         8408      5          5
  192       19026        63562      6          6
  384      547323      2154266      7          7

    cumulative:  n <= 100 : 2410 | n <= 200 : 74199 | n <= 300 : 562688 | n <= 400 : 2547496
```

Two readings.

* **`max s` observed `= max floor(log_2 K)` at every `n` tested** — DEPTH-LOG is
  sharp on the numerical data, and `s <= 5` is *exactly* Moh's cutoff artefact.
* **Growth is superpolynomial.** `#skeletons(96, 192, 384) = 872, 19026, 547323`:
  doubling `n` multiplies the count by `21.8` then `28.8`, an effective exponent
  rising from `4.45` to `4.85` — the `n^{Theta(log n)}` shape forced by `s ~ log_2 K`
  free exponents of range `O(n)` each.

### 6.4 What actually limited Moh to 100 — three candidates, one answer

```text
 (i)   the DEPTH.  NO.  s <= 5 at n <= 100 is a consequence of the cutoff (DEPTH-LOG);
       at n <= 400 the same argument gives s <= 7, recursion unchanged.
 (ii)  the SEARCH COST.  NO.  Moh's program "uses 147.148 sec of a CDC 6500 and costs
       only $2.41" (moh.txt:177-178); the skeleton space is ~2410 at n <= 100 and
       2.5x10^6 at n <= 400, which a modern desk enumerates in seconds.
 (iii) the ENDGAME.  YES.  "the number of coefficients of those possible counter-
       examples range from 3370 to 7328 ... beyond the capacity of a large Computer"
       (moh.txt:170-176).  Appendix II reduces each survivor to <= 12 coefficients BY
       HAND -- via Prop 6.3/6.4 to the reduced data (16,12), (21,14), (15,10) with
       Jacobian x, x, x^2 (moh.txt:3616-3626) -- then eliminates.  No uniform endgame:
       every survivor is a bespoke elimination.
```

**So the 100 is the endgame's wall, not the recursion's** — *the same* stuck-point
APPROACHES row 1 records for the GGV farm ("no general corner endgame"), reached from
the other side. Two literature programs, one wall: **enumerate cheaply, kill bespoke.**
Typed HEURISTIC, not a theorem: Moh's survival rate at `n <= 100` was `4/2410 ~ 0.17%`;
at a constant rate that is `~123` survivors at `n <= 200` and `~4200` at `n <= 400`,
each needing its own Appendix II.

**Does `N` enter Moh's argument?** Not as an input and not in any constraint (§5.2,
by exhaustive reading). But it is not invisible to his objects: by CONTACT-DEFICIENCY
it is the pairing `- sum_{i,j} ord_t(tau_i - phi_j)` on precisely the tree he builds.
So the decisive statement is **not** "the recursion is blind to `N`, so the boundary
program is dead"; it is:

> **THE MISSING INSTRUMENT, NAMED.** Moh's data pins the *major tower* — one chain of
> discs with its radii `delta_i` and counts `V_i`. The pairing
> `sum_{i,j} ord_t(tau_i - phi_j)` also runs over pairs separated inside the *minor*
> discs, which §6 (Prop 6.1) treats qualitatively and does not pin numerically.
> Evaluating `N` on a skeleton therefore needs the minor-disc counts as well. That is
> a finite, desk-scale addition to a search that already runs in seconds — and it
> converts "is `D` bounded in `N`?" into "does the filter `N <= 16` empty the skeleton
> census at each `D`?", a *computation*.

## 7. Part (5): consequences, priced

### 7.1 THEOREM MOH-SHARP-2 — `D_min >= 105`

> **THEOREM MOH-SHARP-2 (unconditional; sources all VERIFIED in `refs/`).** For every
> non-invertible Keller pair at its degree minimum, `D_min = K e` with
> ```text
>   (F1) e = max(d,e) >= 3, d >= 2, gcd(d,e) = 1        [(LF)+(MIN); GGV Rem 4.2]
>   (F2) K >= 16                                        [GGV Cor 6.6, gv.txt:1761]
>   (F3) K has a divisor c with 4 <= c < K              [Moh Cor 6.1 + Prop 5.5]
>   (F4) K is neither a prime p nor 2p                  [GGV Cor 7.9's argument at K]
>   (F5) D_min >= 101                                   [Moh, Appendix II]
> ```
> and therefore
> ```text
>   admissible D in [101,120] = { 105, 108, 112, 117, 120 }   =>   D_min >= 105 ,
>   admissible D in [101,200] : 30 of the 100 degrees.
> ```
> *On (F4).* GGV Cor 7.9 (`gv.txt:2266-2283`) proves `gcd(a,b) > 2` for **every**
> standard `(m,n)`-pair, where `(a,b) = (1/m) en_{1,0}(P)`; and its second half runs
> `gcd(a,b) | a+b`, `a < b`. GGV state the conclusion for the *minimiser* `B` because
> there `a+b = B`. For a general minimal counterexample GGV Prop 4.7 (`gv.txt:796`)
> supplies `phi` with `v_{1,1}` preserved and `en_{1,0}(P) = st_{1,1}(P)`, so
> `a + b = v_{1,1}(P)/m = K`; the identical argument then yields `K != p` and
> `K != 2p`. Nothing else is changed.
> *Positive control.* All four of Moh's `n <= 100` survivors satisfy (F1)–(F4)
> (`K = 16, 28, 25, 33`; `(e,d) = (4,3), (3,2), (3,2), (3,2)`) — as they must, since
> they were only killed by Appendix II's elimination, not by any shape condition.

**Delta against MKS.** MKS's MOH-SHARP gives `D_min >= 102` and excludes
`101,103,106,107,109,113,118` in `[101,120]`. (F3) additionally excludes
`111, 115, 116, 119` (their only `K` in range is prime); (F4) additionally excludes
`102, 104, 110, 114`. The floor moves `102 -> 105`.

### 7.2 Pricing against MOH-CROSS, SAT-CROSS and the cells

```text
 A. CELLS KILLED BY THIS LANE: none.  No (B2)/(B3) cell is emptied.
 B. MOH-CROSS (INT12) UNCHANGED IN FORM, SHARPENED IN VALUE: any proved
    D_min <= C(N) with C(N) <= 104 now kills geometric degree N (was 100).  (B2) at
    5<=N<=16 and (B3) at 4<=N<=8 still need [ANTICANON-DEFECT] + [SAT-MASS], now
    against 105.
 C. SAT-CROSS REPRICED DOWNWARD.  MKS's T-IS-THE-CEILING gives T <= tau <=>
    D_min <= 2(tau+kappa); with D_min >= 105 the floor is T >= 53 - N (was 51 - N)
    against SM's target tau <= 50 - N.  The gap widens from ONE unit to THREE.  It
    remains equivalent to the ceiling, not cheaper.
 D. DEPTH IS NOT THE GAP.  The pair count is <= log_2 K ~ 5 at the floor: a "depth
    ceiling" in the COUNT sense already exists and is useless, since it does not bound
    T, a size.  Any future "depth" lane must be charged with the SIZES (M_r, V_r);
    the exact windows are in sec.3.1.
 E. (B3) AT N = 4, in place form: kappa = 2 proper places with m_1 + m_2 = 4 (or one
    with k=2,m=2), Sn = 4 non-proper places, so r_inf = 6 and T = D - 6 >= 99 -- the
    generic pencil member has exactly SIX places at infinity carrying total degree
    D >= 105, all but two of them non-proper, distributed over the two towers of
    NU-TWO.
 F. NOT GAINED.  No bound on T, nu_gamma, Psi, n or D beyond (F1)-(F5); no cell
    emptied; nothing about case (A), A2, Z(G) or the reducible branch; no claim
    that a Jacobian skeleton is or is not realisable.
```

## 8. Corrections to charged inputs

```text
 C1. MKS sec.5.3 (MOH-SHARP cross-validation) -- WRONG LIST, from OCR.  MKS reads
     Moh's surviving degrees as "(64,68), (84,56), (75,50), (99,66) -- i.e. 4*(16,17),
     28*(3,2), 25*(3,2), 33*(3,2) ... the fourth has K = 4 < 16 and is killed a second
     time by GGV Cor 6.6."  Moh's Appendix II text (moh.txt:3596-3597) does print
     "(64, 68)", but his sec.6 table (moh.txt:3325-3332) gives  n = 64, m = -M_1 = 48,
     and Appendix II's own reduced row for that case is (n,m) = (16,12) = (64,48)/4.
     The pair is (64,48) = 16*(4,3).  Consequences: ALL FOUR survivors have K >= 16,
     NONE is killed by GGV Cor 6.6, and Heitmann's bound is ATTAINED (K = 16) by
     Moh's hardest case.  The MOH-SHARP inequality itself is unaffected.
 C2. MKS sec.5.3 ("Newton-polygon theory leaves T free ... never the depth") --
     TRUE FOR T, FALSE FOR THE DEPTH.  The depth (pair count) is bounded by
     log_2 K, twice over (DEPTH-LOG).  MKS's sentence conflates the size T with the
     count; the conclusion "T is free" survives, the reason given does not.
 C3. MKS OPEN[NU2-RIGIDITY] -- CLOSED POSITIVE (sec.2.2), by Moh Prop 4.5 + Lemma 5.3
     + Prop 5.4, gauge-free, with the extra datum u != v.
 C4. The charge's framing "T is exactly the continuant data ... i.e. the PUISEUX
     CHARACTERISTIC of the branches at infinity" -- REFINED.  T = sum(nu_gamma - 1)
     is the total DEGREE EXCESS of the places at infinity (equivalently the total
     ramification of x over x = infinity in gauge (GEN)), and r_inf = D - T.  It is a
     function of the Puiseux characteristics, but it is their SIZE, not their DEPTH.
 C5. SM's DEFINITION REPAIR and MKS's NO-Linf-TAIL are consistent with the place
     ledger and are untouched; note only that r_inf = kappa + Sn holds in BOTH the
     extended and classical readings, since it counts places, not points.
```

## 9. Opens raised, with bounded quantities

```text
OPEN[N-ON-THE-TREE]  (new; the successor this lane most wants run).  Express N on a
   Moh skeleton.  BOUNDED QUANTITY: the integer
   N = - sum_{i=1..n} sum_{j=1..m} ord_t(tau_i - phi_j) in [1, mn], evaluated from
   the tree data of g * prod T_i.  The major tower (Def 5.1(1),(3)) supplies the
   radii and the root counts along one chain; what is missing is the minor-disc
   distribution (Moh sec.6, Prop 6.1).  DELIVERABLE: a function N(n, m, M_*, d_*, V_*,
   + minor data) and its evaluation on the four n <= 100 survivors, then the filter
   "N <= 16" run over the census of sec.6.3.  If the filter empties the census at
   every D, the ceiling is PROVED in that range; if it does not, the surviving
   skeletons are the exact objects a realisability lane must attack.  Desk-scale.
OPEN[NU-BOUND-AT-A-PLACE]  (new sharpening of SM's OPEN[NU-BOUND]).  Bound
   nu_gamma = I(gamma,L_infty) at a PROPER place in terms of m_gamma.  BOUNDED
   QUANTITY: nu_gamma in Z_{>=1} at the kappa <= N proper places of C_gen.  The
   automorphism (x,y+x^k) has nu/m = k unbounded at a proper place, so any bound must
   use non-invertibility.  With nu_gamma <= h(m_gamma) there,
   T <= sum h(m_gamma) + sum_{np}(nu-1) and only the non-proper half remains.
OPEN[NONPROPER-DEGREE]  (new; the other half).  Bound sum_{non-proper}(nu_gamma - 1).
   BOUNDED QUANTITY: the nonnegative integer T - sum_{proper}(nu_gamma - 1), supported
   on the S n places over the dicriticals -- the part of T that N cannot see.
OPEN[MOH-ENDGAME]  (new; the wall itself).  Is there a uniform elimination killing a
   surviving Moh skeleton, replacing Appendix II's four bespoke arguments?  BOUNDED
   QUANTITY: the number of free coefficients after the Prop 6.3/6.4 reduction (Moh:
   3370-7348 raw, <= 12 reduced, for his four).  Worth more than any extension of the
   search; the shared stuck-point of APPROACHES row 1.
```

Carried unchanged: `OPEN[DELTA-AFF-VS-N]`, `OPEN[ANTICANON-DEFECT]`,
`OPEN[SAT-MASS]`, `OPEN[FORK-DEPTH]`, `OPEN[FORK-MULT]`, `OPEN[TWO-DICRITICAL]`.
**Closed:** `OPEN[NU2-RIGIDITY]` (MKS) — POSITIVE, gauge-free.

## 10. FALLACY-v2 audit

* **Flag/place/series.** Three "depths" are separated by name and bound (§2.3) and
  never substituted. Six degree-like integers are kept apart: `D`, `D_min`, `N`,
  `K = gcd(deg P, deg Q)`, `n = deg Abar_F`, `nu = #roots of the top form`. Moh's
  `n = deg g` is used **only inside his normalisation**, where it equals `D`, is
  flagged at first use, and is never paired with the campaign's `n = deg Abar_F` in one
  expression. Moh's `d_s = gcd{n,M_1..M_{s-1}}` is **not** `K` (SM's warning), but
  `d_2` **is** `K`, proved from `M_1 = -m`, not assumed. GGV's `(u,v) = A_0` (a corner)
  is **not** this lane's `(u,v)` (multiplicities of the roots of `H`): GGV Prop 6.7's
  `u >= 4` is about `A_0` and is never used on the leading-form multiplicity.
* **Per-ray/exit-set charge.** No exit price, no `charge_basis` line. In
  CONTACT-DEFICIENCY each of the `mn` root pairs is charged once — the slope split is
  a partition, `2deuv + de(u^2+v^2) = mn`, checked arithmetically. In PLACE-LEDGER each
  place belongs to exactly one boundary component and each `c_C` counts its own places.
* **Carrier/attainment; floor/attainment.** DEPTH-LOG is an upper bound used only as
  such; attainment is asserted for the *numerical* skeletons (measured), never for
  polynomials. `D_min >= 105` is a floor used as a floor. `sum_{same-slope} ord >=
  180 - N` is an identity plus floors, explicitly not an obstruction. The survivor
  extrapolations are typed HEURISTIC in place.
* **Pole/interior; variable/ring map.** `m_gamma`, `nu_gamma = I(gamma,L_infty)` are
  computed in the two standard charts at each point of `L_infty`, gauge hypothesis
  stated at every use. The resultant identity was tested with a **negative control**
  and fails exactly on the non-monic rows (§6.2). The Singular driver declares
  `ring R = 0,(a,b),ds` with `b` the `L_infty` coordinate in every chart, reads `ord`
  of the second parametrisation component only, and handles the field-extension return
  of `hnexpansion` (`typeof(L[1])=="ring"`) by descending into the returned ring — the
  first run silently skipped 7 rows there and the skip was **repaired**, not tolerated.
* **Prime label; `sat()`; raw remainder.** Moh's `T_r` vs `T_r^psi` (the `x -> 0`
  specialisation), and `d_i` (Moh's gcd chain) vs `d` (exponent in `l(P) = alpha H^d`)
  vs GGV's `d_j` (Thm 7.6), are three-way distinguished; no prime marks denote
  differentiation. No saturation, Groebner basis or quotient normal form: integer
  enumeration, exact rationals, resultants over `Q`, Hamburger–Noether expansions.
* **OCR discipline.** Every quoted statement carries an extraction line number. The
  two statements whose displays the OCR destroyed were recovered from page images and
  **independently validated by reproducing six published numerical values**; where the
  scan is illegible (`n = 75` deltas) the values are marked as prediction, not
  quotation. MKS's `(64,68)` is corrected against the same paper's own table.
* **Not filled by cap or analogy.** Abhyankar–Moh, Nagata, Appelgate–Onishi, Heitmann,
  van den Essen, Jung–van der Kulk, Cassou-Noguès/Kaliman are ABSENT and none is
  load-bearing; `(LF)`, `(MIN)`, DEPTH-LOG, PLACE-LEDGER, CONTACT-DEFICIENCY and
  MOH-SHARP-2 are proved here from VERIFIED sources or from scratch.

## 11. Typed verdict block

```text
LANE       DEPTH-CEILING
SCOPE      Keller, noninvertible, degree-minimal; H2 only where the campaign ledger is
           quoted.  Case (A) EMPTY and untouched; A2 untouched; no Z(G)=1.
           PLACE-LEDGER and CONTACT-DEFICIENCY hold for every dominant F (the latter
           in the stated gauge).

PROVED HERE  (all PROVED-HERE, UNREVIEWED)
 NU-TWO       2.2.  Degree-minimal counterexample in ANY gauge with deg = deg_y: the
              leading form has EXACTLY two distinct linear factors, of DIFFERENT
              multiplicities, and M_s = n-2.  Closes MKS OPEN[NU2-RIGIDITY]; makes
              E0-FREE gauge-free.  [Moh Prop 4.5 + Lem 5.3 + Prop 5.4, VERIFIED.]
 DEPTH-LOG    4.  3 <= s <= log_2 K (Moh side); k+1 <= log_2 K (GGV side).  Identifies
              Moh's unexplained "s <= 5" as the n <= 100 instance.  Sharp numerically.
 PLACE-LEDGER 2.4.  D = sum nu_gamma, N = sum m_gamma, T = sum(nu_gamma - 1),
              r_inf = D - T = kappa + Sn over the places at infinity of a generic
              member.  Re-derives SAT-WEIGHT/DEG-SPLIT; MEASURED on 16 rows, 0 fails.
              In gauge (GEN), T = total ramification of x over x = infinity.
 (KL)         2.4.  Keller: T = D + N + 2 g_L - 2 - nW.  Identity; control (x,y+x^k).
 CONTACT-     5.1.  N = deg_x Res_y = - sum_{i,j} ord_t(tau_i - phi_j)
 DEFICIENCY        = 2deuv - sum_{same-slope} ord_t.  Locates N inside Moh's tree.
 MOH-SHARP-2  7.1.  D_min = Ke with (F1)-(F5); admissible D in [101,120] =
              {105,108,112,117,120};  D_min >= 105.
 RECURSION    3.1.  Moh Def 5.1(1)-(4) and Prop 5.3 recovered from the page images and
 RECOVERED    VALIDATED by reproducing 6/6 legible published delta values; free datum
              per step = (M_{r-1}, V_r) with exact windows.

MEASURED     6.  mohrec.py: 6/6 published deltas MATCH, 2 predictions recorded.
             places.py: 16 rows, 0 failures, 0 skips.  census2.py: calibrated to Moh's
             own "25 values" to the unit; max s = max floor(log_2 K) at every n tested;
             growth n^{Theta(log n)}.  dmin.py, res.py as above (res.py includes a
             negative control).  < 12 min, < 400 MB, no AWS, no web.

CORRECTED    MKS's reading of Moh's surviving degree list ((64,68) -> (64,48); all four
             have K >= 16 and none is killed by GGV); MKS's "the depth is free" (the
             COUNT is log-bounded, the SIZE is free); the charge's identification of T
             with a Puiseux depth (it is a degree excess); SAT-CROSS's gap to its own
             floor (one unit -> three, via D_min >= 105).

CHARGE       (1) sec.2.  (2) sec.3: recursion written exactly, both sides, free datum
ANSWERED         sized per step; "always a next pair" is a THEOREM with boundedly many
                 steps.  (3) sec.5: T NOT bounded by N through the recursion; the free
                 datum is the SIZE (M_r,V_r), and the part of T that N cannot see is
                 sum_{non-proper}(nu_gamma - 1); the family is exhibited in place form,
                 realisable only in the non-Keller class.  (4) sec.6: the wall at 100
                 is the per-survivor ENDGAME, not the depth and not the search; N
                 occurs in no constraint but IS a quadratic functional of Moh's tree,
                 so the boundary program is not refuted, it is reduced to
                 OPEN[N-ON-THE-TREE].  (5) sec.7: D_min >= 105; MOH-CROSS threshold
                 104; SAT-CROSS three units below its floor.

NOT CLAIMED  No cell emptied.  No bound on T, nu_gamma or D beyond MOH-SHARP-2.  No
             statement about realisability of any skeleton.  No new exit price.
```

<!-- BODY-END -->
