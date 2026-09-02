# MINIMAL-KELLER-SHAPE — what degree-minimality forces on the boundary tree: the first fork is decided, and it decides CH2

Lane: `MINIMAL-KELLER-SHAPE`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + desk-scale CAS (an independently written resolution-of-indeterminacy
engine in python3/sympy 1.14.0 over `Q`; Singular 4.4.1 `normal.lib` for genus; no AWS,
no fetching, no web). Drivers in `/tmp/mks`, not installed in `box/`. Wall time
< 3 min, peak RSS < 300 MB.

## 0. Custody, method, scope

The five charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all five match the charge exactly:

```text
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  integration12-coordinator-fable51-20260902.md
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  keller-pencil-genus-opus5-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  sat-mass-opus5-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  n-vs-mapdeg-review-gpt55-20260902.md
```

Abbreviations: **INT12** = coordinator binding, **KPG** = KELLER-PENCIL-GENUS,
**SM** = SAT-MASS, **NVM** = N-VS-MAPDEG, **NVM-R** = its gpt-5.5 review,
**GGV** = Guccione–Guccione–Valqui 2017 (in `refs/`).

Typing discipline, as charged. INT12's polar ledger (`(I1)`–`(I6)`, PROP DN,
DEG-SPLIT, NOETHER-K, CAP-STRICT, MERIDIAN-FLOOR+, MOH-CROSS, NO-CEILING at
LATTICE-LEDGER scope) at its **reviewed** typing; MI/THEOREM PROFILE, MF-EXACT,
`7.B'`, `(K)`, `H2` at banked typing. Case (A) is EMPTY and is not priced; no
`Z(G)=1`; no A2 cell; no quasi-homogeneity. **KPG and SM are PROPOSALS, consumed
only where re-derived here**: FORK-GENUS, GENUS-DEFECT, ESCAPE-KAPPA, POLAR-DEGREE,
CH1/CH2, DEG-SPLIT, SAT-WEIGHT and HALF-CAP are each re-derived below, every use
flagged; their measured tables are treated as **data to be checked** against a third
engine (Sec 6.5). No canonical ledger edited; `jc2-lean` not inspected; nothing
fetched. **No `charge_basis` line: this report asserts no new exit price.**

Local PDFs read this session with `pdftotext -layout`, hashed:

```text
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
b6a369146240dbd36107907ebfb63ab2fc602abb524151d6ab31d39e5bc10722  (extracted text of the Moh PDF)
```

`refs/` contains **no** Abhyankar–Moh, **no** Nagata, **no** Appelgate–Onishi, **no**
Heitmann, **no** Cassou-Noguès/Kaliman, **no** van den Essen and **no** Jung/van der
Kulk item (checked by `ls`). Those are marked **ABSENT** below and every use is
flagged LITERATURE-TYPED, never verified here.

## 1. Verdict, up front

```text
(1) THE FIRST FORK IS A NEWTON-POLYGON INVARIANT.  THEOREM FIRST-FORK (any
    dominant F, no Keller):  deg_{L~}(E_0) = nu := #{distinct roots of the top form
    of the max-degree coordinate} = #{points at infinity of the generic member};
    and nu >= 2 forces deg_{T_+}(E_0) = nu.  So E_0 is a LEAF of T_+ iff nu = 1
    (top form a power of a linear form), and a FORK iff nu >= 3, whence Psi >= D.
    Verified on 46 exactly resolved maps, 0 mismatches.
(2) CH2 IS DECIDED, NEGATIVE.  (b) NO: for every counterexample the
    Makar-Limanov / van den Essen SUBRECTANGULAR gauge -- which PRESERVES both
    degrees, hence degree-minimality -- makes l_{1,1}(P) a MONOMIAL, so
    H = c x^{u} y^{v} with u,v >= 1 and  nu = 2  EXACTLY:  E_0 is a FREE
    (valency-2) vertex of T_+, never a leaf, never a fork.  And "E_0 a leaf" is a
    NON-MINIMALITY signature: right-composing with any non-linear source
    automorphism forces nu = 1 (measured 3/3, with D and Psi both jumping).  KPG's
    9 conditional kills do NOT stand.  The conditional is also mispriced: THEOREM
    E0-LEAF-CAP (general, no Keller) gives  Psi = 0 and E_0 a leaf ==>
    D <= N + 1 - 2 g_L, so CH2 in ANY gauge plus MOH-FLOOR kills every N <= 99, not
    9 cells.  A hypothesis that strong is the theorem, not a lemma.
(3) CH1 IS DECIDED, NEGATIVE, IN THE CONTROL CLASS.  Psi = 0 FAILS for the simplest
    automorphisms: (x, y + x^k) has Psi = k = D, Lambda = k + 2, Lambda - Psi = 2
    (Noether) for every k.  By POLAR-DEGREE the controlled object is Psi - Lambda --
    the ceiling itself.  Under Keller + H2 + MERIDIAN-FLOOR+, Psi = 0 forces
    Lambda <= N: the two chain ends carry <= N while E_0, interior, carries D >= 102.
(4) T IS FREE, AND SAT-CROSS'S PRICE IS EXACTLY THE THEOREM.  With HALF-CAP
    (re-derived) and DEG-SPLIT, T <= tau is EQUIVALENT to D_min <= 2(tau + N):
    OPEN[SAT-MASS] is not half the ceiling, it IS the ceiling at W <= 3.  And SM's
    own floor T >= D_min/2 - kappa >= 51 - N sits exactly ONE unit above its target
    tau <= 50 - N.  Newton-polygon theory leaves T free: T = sum(nu_C - 1)c_C is the
    continuant data of the satellite chains = the Puiseux characteristic of the
    branches at infinity, and GGV's corner theory constrains only the FIRST corner
    (u >= 4, v <= u(u-1), u + v >= 16), never the depth.
(5) TWO UNCONDITIONAL GAINS.  (i) MOH-FLOOR sharpens: D_min = K*max(d,e) with
    K = gcd >= 16 (GGV Cor 6.6, VERIFIED in refs/) and max(d,e) >= 3, so
    D_min >= 102 and D_min has a divisor K with 16 <= K <= D_min/3 (which excludes
    101, 103, 106, 107, 109, 113, 118 in the range [101,120]).  Moh's own surviving list (64,68), (84,56), (75,50),
    (99,66) is exactly this shape -- three are K*(2,3), the fourth has gcd 4 and is
    killed again by GGV.  (ii) In the subrectangular gauge T = T_class: SM's
    DEFINITION REPAIR is VACUOUS at a degree-minimal counterexample (measured
    T = T_class on all 32 rows with nu != 1, T > T_class on all 14 with nu = 1).
(6) CONTROLS.  46 exact resolutions over Q with the full dual tree; all satisfy
    Z^2 = N, sum a_i^2 = D^2 - N, Z.K_X two ways, the proximity-excess cross-check,
    FORK-GENUS and the new Theta-form -- 0 failures.  6 Singular genus computations
    confirm 2 g_L - 2 = N + Z.K_X (incl. g = 3 for KPG's G_2).  12 rows reproduce
    SM's table from a third engine.
```

## 2. Part (1): the classical package, typed

Throughout `(P,Q)` is a **Jacobian pair**: `P,Q in C[x,y]`, `[P,Q] := P_xQ_y - P_yQ_x
in C^*`. A **counterexample** is a Jacobian pair that is not an automorphism.
`deg` is total degree, `l(R) := l_{1,1}(R)` the top (degree) form, `D := max(deg P,
deg Q)`, `K := gcd(deg P, deg Q)`.

### 2.1 The leading-form theorem (Abhyankar / Nagata) — PROVED HERE, elementary

> **(LF).** For a counterexample `deg P + deg Q - 2 > 0` and `deg[P,Q] = 0`, so
> `[l(P), l(Q)] = 0`: the binary forms `l(P), l(Q)` are algebraically dependent and
> there are a binary form `H` and `alpha, beta in C^*` with
> ```text
>     l(P) = alpha H^d ,  l(Q) = beta H^e ,  gcd(d,e) = 1 ,  deg H = K ,
>     deg P = K d ,  deg Q = K e .
> ```
> *Proof.* `[l(P),l(Q)] = 0` for binary forms forces the same linear factors with
> proportional multiplicities; writing `deg P : deg Q = d : e` in lowest terms and
> `H := ` the primitive form gives the display. The "Newton polygons are similar"
> statement is the same fact read on the `(1,1)`-face. ∎

This is the statement the charge attributes to Abhyankar and Nagata (Nagata 1988/89,
**ABSENT** from `refs/`); proved above, so used PROVED-HERE, not carried.

> **(MIN).** At a **degree-minimal** representative (no elementary automorphism on
> either side lowers `max(deg P, deg Q)`): `d, e >= 2`, `d != e`, hence
> `max(d,e) >= 3` and `D = K max(d,e) >= 3K`.
> *Proof.* If `d = 1` then `l(Q) = beta(l(P)/alpha)^e`, so `(u,v) |-> (u, v - cu^e)`
> lowers `deg Q`, hence `D`; symmetrically for `e = 1`; `d = e` forces `d = e = 1`. ∎
> Equivalent form, **GGV Remark 4.2** (gv.txt:718): for a minimal pair neither
> `deg P` divides `deg Q` nor conversely.

### 2.2 Moh 1983 — VERIFIED in `refs/` this session

Read firsthand (`moh.txt`, lines of the extraction hashed above):

* search hypotheses (3257-3262): *"`deg f = m = -M_0 < deg g = n <= 100`"*,
  *"`J(f,g) = 1` and the degrees of `f` and `g` can not be reduced simultaneously"* —
  **both** coordinate degrees `<= 100` **and** degree-minimality, confirming NVM-R's
  repaired normalisation.
* outcome (3597-3599, 3839): *"the only possible counter-examples ... for
  polynomials of degrees less than 100 are of degrees `(64,68)`, `(84,56)`,
  `(75,50)` and `(99,66)`"*, all settled in Appendix II; *"There is no
  counter-example of polynomials of degrees less than or equal to 100"*.
* Moh's own `d_s = gcd{n, M_1,...,M_{r-1}} >= 4` (3275, with `3 <= s <= 5`) is on the
  **characteristic data**, **not** `gcd(deg P, deg Q)`; kept apart, as SM flags.

**MOH-FLOOR (consumed):** `D_min >= 101`.

### 2.3 Heitmann's `gcd >= 16` — VERIFIED in `refs/` via GGV

GGV (J. Algebra 471 (2017); arXiv:1401.1784v3) is in `refs/` and gives an
**elementary proof** of Heitmann 1990's bound. With `B := min{gcd(deg P, deg Q)}`
over counterexamples:

* **GGV Cor 6.6** (gv.txt:1761): `B >= 16`. Hence **every** counterexample has
  `K = gcd(deg P, deg Q) >= 16`. *(Heitmann 1990 itself is ABSENT from `refs/`.)*
* **GGV Prop 6.7** (gv.txt:1772): for the primitive corner `A_0 = (u,v)`,
  `u >= 4` and `v <= u(u-1)`; **Remark 6.8**: `gcd(deg_x P, deg_x Q) >= 4`.
* **GGV Thm 7.11** (gv.txt:2307): either `v_{1,1}(A_0) > 20`, or
  `A_0 = (4,12)`, `(rho,sigma) = (4,-1)`, `gamma = 3`; and `B != 2p` for `p` prime.
* **GGV Prop 6.4**: at the primitive corner direction `(rho,sigma)`,
  `l_{rho,sigma}(P) = lambda_P R^m` and `l_{rho,sigma}(Q) = lambda_Q R^n` with
  `en(R) = A_0 = (u,v)`, `st(R) = (r',s')`, `s' < r' < u < v`, `gcd(u,v) > 1`.

### 2.4 The subrectangular normal form — LITERATURE-TYPED via GGV

> **(SUBRECT)** [van den Essen, *Polynomial automorphisms and the Jacobian
> conjecture*, Cor. 10.2.21, argument credited to Makar-Limanov; quoted and used in
> **GGV Prop 4.7** (gv.txt:796, 816) and **Cor 5.21** (gv.txt:1454). van den Essen is
> **ABSENT** from `refs/`; GGV's use of it is VERIFIED.]
> For every counterexample `(P,Q)` there are `phi in Aut(C[x,y])` and integers
> `1 <= a < b` with
> ```text
>     (a,b) in Supp(phi P)  and  Supp(phi P) subset { (i,j) : 0 <= i <= a, 0 <= j <= b } ,
>     v_{1,1}(phi P) = v_{1,1}(P) ,   v_{1,1}(phi Q) = v_{1,1}(Q) .
> ```
> `a < b` is GGV Thm 2.6(4) (`st_{1,1}(P) !~ (1,1)`), and `1 <= a` is GGV Prop 4.1
> (`v_{1,0}(P) > 0`).

**The gauge is degree-preserving**, so applying it to a degree-minimal
representative yields a degree-minimal representative. This is the only place a
gauge choice is made, and it is made once.

### 2.5 Abhyankar–Moh one-place / semigroup — LITERATURE-TYPED, ABSENT, framing only

`(AM-JAC)` [Abhyankar, Tata Lect. Notes 57 (1977); cf. Razar 1979; carried at the
campaign's banked typing, `ladder/AM-CHECK.md` sec 0]: if `f` has one **place** at
infinity and `J(f,g) in C^*` then `(f,g)` is an automorphism pair.
`(AM-SG)` [Abhyankar–Moh, Crelle 260/261 (1973), 276 (1975)]: for one place at
infinity the delta-sequence obeys `d_{i+1}|d_i`, `d_{i+1} < d_i`,
`n_i delta_i > delta_{i+1}`, `n_i delta_i in <delta_0,...,delta_{i-1}>`. Neither is
load-bearing; `(AM-JAC)` is quoted once, as the reason `nu = 1` is the
*automorphism* signature. Appelgate–Onishi 1985, Nagata 1988/89 and
Cassou-Noguès/Kaliman are **ABSENT** and are not used.

## 3. Part (2): the translation

### 3.1 Set-up (re-derived, not quoted)

Homogenise to the common degree `D`; the net is `V = <G_1,G_2,G_3>`,
`G_1 = z^{D-deg P}P^h`, `G_2 = z^{D-deg Q}Q^h`, `G_3 = z^D`, all base points on
`L_infty`. `sigma : X -> P^2` resolves the base cluster `{p_1,...,p_r}`;
`Phi = Fbar o sigma`; `L~ := X \ A^2` is the SNC **tree** of the boundary;
`Z := Phi^*(L_infty^{tgt}) = D H - sum a_i E_i`, `Z^2 = N`; `m_C := ord_C Z`,
`nu_C := ord_C(sigma^*L_infty)`, `c_C := Z.C`, `T_+ := supp Z`. Leaf mass
`Lambda = sum_{deg_{T_+}=1}m_C + 2 sum_{deg_{T_+}=0}m_C`; fork mass
`Psi = sum_{deg_{T_+}>=3} m_C(deg_{T_+}C - 2)`.

Three identities are re-derived here and machine-verified on 46 maps (Sec 6):

```text
 (FG)     Z.K_X = Psi - Lambda - kappa            [KPG's FORK-GENUS, re-derived]
 (TH)     Z.K_X = Theta - kappa - S n ,   Theta := sum_{C in L~} m_C (deg_{L~}C - 2)
 (GD)     2 g_L - 2 = N + Z.K_X                   [adjunction; = KPG's GENUS-DEFECT]
```

`(TH)` is new and is the form the Newton polygon reads: it runs over the **whole**
boundary tree, so dicriticals (`m_C = 0`) drop out of the mass and reappear only
through `sum_{dicritical} Z.C = S n`; `(FG)` follows because deleting a dicritical
`l` lowers `sum m_C deg C` by `sum_{C adj l} m_C = Z.C_l - m_{C_l}C_l^2 = s_l n`.
`theta_inf = kappa` (ESCAPE-KAPPA) is re-derived in one line: for generic
`z_u = L cap L_infty`, `Phi^{-1}(z_u)` is `k_C` unramified points on each `C` over
`L_infty` (contracted components map elsewhere; dicriticals meet `L_infty^{tgt}`
only over the finitely many points of `Abar_F cap L_infty`), all on the smooth
member `D_L = Phi^*(L)`. With MF-EXACT this gives **POLAR-DEGREE**
`n(W-S) = 2N - Lambda + Psi` (Keller, H2).

### 3.2 THEOREM FIRST-FORK — the valency of `E_0` is a Newton-polygon invariant

Let `nu` be the number of distinct base points of the net on `L_infty`. The generic
member restricts on `L_infty` to `lambda f_1 + mu f_2` (`f_i = G_i|_{z=0}`), so `nu`
is the number of distinct roots of `l(R)`, `R` the max-degree coordinate (of
`gcd(l(P), l(Q))` if the degrees are equal). For a counterexample `deg P != deg Q`
(MIN) and `l(R) = const * H^{max(d,e)}`, so
`nu = #{distinct roots of H} = #{points at infinity of the generic pencil member}`.

> **THEOREM FIRST-FORK.** For every dominant `F` with at least two blow-ups,
> `deg_{L~}(E_0) = nu`. If `nu >= 2` then every neighbour `C` of `E_0` has
> `m_C > 0`, so `deg_{T_+}(E_0) = nu` as well. Consequently
> ```text
>   nu = 1  <=>  E_0 is a LEAF of L~  (and of T_+, if its neighbour has m > 0) ;
>   nu = 2  <=>  E_0 is FREE in T_+   (contributes to neither Lambda nor Psi) ;
>   nu >= 3 <=>  E_0 is a FORK of T_+ ,  and then  Psi >= m_{E_0}(nu-2) = D(nu-2) .
> ```
> *Proof.* Over one base point `p` the cluster points on the successive strict
> transforms of `L_infty` form a chain `q_1,...,q_h` (`q_{j+1} in E_{q_j} cap E_0`);
> blowing up `q_{j+1}` separates `E_{q_j}` from `E_0`, so exactly one component of
> that chain, `E_{q_h}`, meets `E_0` in `X`, and distinct base points give distinct
> branches: `deg_{L~}(E_0) = nu`. For the multiplicities, `nu_{q_j} = j` and
> `m_{E_{q_j}} = jD - sum_{k<=j}a_{q_k} >= j(D - a_{q_1})` since the proximity
> inequalities give `a_{q_1} >= a_{q_2} >= ...`; and `a_p <= I_p(C_gen, L_infty)`
> with `sum_p I_p = D` (Bezout, `nu` terms each `>= 1`), so `nu >= 2` forces
> `a_p <= D-1` and `m_{E_{q_h}} > 0`. ∎

**Measured: `deg_{L~}(E_0) = nu`, and `deg_{T_+}(E_0) = nu` whenever `nu >= 2`, on
46/46 resolutions** (the tree's `E_0` valency against an independent top-form
routine `nu_topform`).

### 3.3 The two towers of a subrectangular pair, explicitly

Apply (SUBRECT). Then `Supp(P) subset [0,a] x [0,b]` with `(a,b) in Supp(P)` and
`a + b = deg P`, so **the entire `(1,1)`-face of `Newton(P)` is the single vertex
`(a,b)`**: `l(P) = c x^a y^b` is a MONOMIAL. By (LF) `H` is then a monomial, so

```text
      H = c' x^{u_1} y^{v_1} ,   (a,b) = d (u_1,v_1) ,   en_{1,0}(Q) = e (u_1,v_1) ,
      K = u_1 + v_1 >= 16 ,      u_1 = gcd(deg_x P, deg_x Q) >= 4  [GGV Rem 6.8],
      1 <= u_1 < v_1 ,           D = e (u_1 + v_1) = e K ,  e := max(d,e) >= 3 .
```

so **`nu = 2` exactly**, with the two points at infinity

```text
     p_y = [0:1:0]  (root x = 0 of H, multiplicity u_1) ,
     p_x = [1:0:0]  (root y = 0 of H, multiplicity v_1) ,
```

and level-one multiplicities `a_p = D - max(deg_{y_p}P, deg_{y_p}Q)` (the min of the
three generators' multiplicities in the chart at `p`) obeying
`a_{p_y} <= e u_1`, `a_{p_x} <= e v_1`, `a_{p_y} + a_{p_x} <= D`, with equality iff
both coordinates are subrectangular — and then `sum_{i -> p_0} a_i = D` is
**already exhausted at level 1**:

> **COROLLARY NO-L∞-TAIL.** In the two-sided subrectangular gauge the extended
> cluster has **no** point above level 1 on `L_infty`; equivalently no branch of the
> general member is tangent to `L_infty`, `w = nu = 2`, `E_0^2 = -1`, and
> ```text
>          T = T_class .
> ```
> SM's DEFINITION REPAIR (`T - T_class = D - sum_{level 1}a_i`) is therefore
> **VACUOUS at a degree-minimal counterexample**. Measured: `T = T_class` on all 27
> `nu = 2` rows, `T > T_class` on all 9 `nu = 1` rows — the discrepancy SM exhibits
> is exactly the `nu = 1` signature.

**Deeper levels, in Newton/Puiseux terms.** In the chart `(X,Z) = (x/y,1/y)` at
`p_y` the germ of the net member attached to `R` is
`sum_{(i,j) in Supp R} c_{ij}X^i Z^{D-i-j}` — the shear image of `Newton(R)`. Its
tangent cone is the homogenisation of the **top-`y` coefficient polynomial**
`q_{b'}(x)` of the max-degree coordinate, of degree exactly `e u_1`, with
`Z nmid` it. Hence the level-2 points over `p_y` are the distinct roots of
`q_{b'}` (none in the `L_infty` direction — no tangency, consistent with `w = 2`)
and `deg_{L~}(E_{p_y}) = 1 + #{distinct roots of q_{b'}}`. Recursively, the tower
over `p_y` is the Enriques tree of the branches at infinity there: free chains are
the integral parts of the Puiseux exponents, satellite chains the continued-fraction
expansions of their fractional parts. So:

```text
   nu_C  = continuant of the satellite chain below C = -min(ord_C x, ord_C y) ,
   m_C   = -ord_C(generic pencil member) ,   c_C = a_C - sum_{q -> C} a_q ,
   kappa = sum_{m_C > 0} c_C = theta_inf ;  S n = sum_{m_C = 0} c_C ;
   T     = sum_C (nu_C - 1) c_C ,
   forks of L~  <->  characteristic (Newton) pairs of the branches at infinity
                     + separation vertices  (+ E_0 itself when nu >= 3) .
```

`Lambda`, `Psi` are the `m`-weighted leaf and fork counts of that tree, and `(TH)`
says the anticanonical defect is its `m`-weighted Euler characteristic.

## 4. Part (2), control: the automorphism case, written out

For `F in Aut(C^2)` non-linear: `A_F = emptyset` so `ell = 0`, `S = 0`, `n` is not
defined; `N = 1`, `kappa = theta_inf = 1`. By the Jung–van der Kulk reduction
(**ABSENT** from `refs/`, LITERATURE-TYPED) the leading forms are powers of a common
form and, by induction down the elementary word, that form is a power of a **linear**
form; hence `nu = 1` and, by FIRST-FORK, **`E_0` is a leaf**.

Measured (engine, exact):

```text
  F = (x, y + x^k) :  D = k, N = 1, nu = 1, E_0 a LEAF, kappa = 1, S n = 0,
        T = k - 1 = D - 1 (the JvdK word length, = SM's C3), T_class = k - 2,
        nu_max = k, sum a_i = 3k - 3 (Noether), Z.K_X = -3, Lambda = k + 2,
        Psi = k, so Lambda - Psi = 2 for every k.
  k = 3 tree:   E_0(m=3) - E_2(m=3) - E_3(m=3) - E_4(m=2) - E_5(m=1, k_C = 1)
                                        |
                                      E_1(m=1)          [one fork, at E_3]
  F = (x + y^2, y) : same row with k = 2.
  F = (x + (y+x^2)^3, y + x^2) : D = 6, nu = 1, E_0 a leaf, T = 5, Lambda = 11,
        Psi = 9, Lambda - Psi = 2, two forks.
```

**Three readings.** (i) `Lambda - Psi = 2` is Noether's `Z.K_X = -3` in tree form,
the `N = 1` instance of `(FG)`; both `Lambda` and `Psi` grow like `D` and only the
difference is rigid, so **`Psi = 0` is false already here**. (ii) `nu = 1` and
`T > T_class`: the `L_infty`-tail (the branch tangent to `L_infty`) is exactly the
tail an elementary reduction removes — what SM's `T != T_class` repair sees.
(iii) `T = D - 1`: for an automorphism the whole degree sits in the satellite
continuant, `S n = 0`, `kappa = 1`.

## 5. Part (3): the three decisions

### 5.1 (b) Is `E_0` a leaf of `T_+`? — **DECIDED: NO**

> **THEOREM E0-FREE.** Let `(P,Q)` be a counterexample and `phi` the (SUBRECT)
> gauge, which preserves both degrees. Then for `(phi P, phi Q)`
> ```text
>       nu = 2 ,      deg_{T_+}(E_0) = 2 ,
> ```
> so `E_0` is a **free** vertex of the polar tree, contributing to neither `Lambda`
> nor `Psi`. KPG's CH2 hypothesis "`E_0` a leaf of `T_+`" is FALSE in this gauge and
> its 9 conditional kills — the cells with `N = 2W`, including the live `N = 4`
> `(B3)` cell — do **not** stand.
> *Proof.* Sec 3.3 (`l(P)` a monomial, `u_1, v_1 >= 1`) plus FIRST-FORK. ∎

Two strengthenings, both needed because CH2 could be invoked in some *other* gauge
(its conclusion `nW <= 2N-2` is gauge-invariant):

> **THEOREM LEAF-IS-NONMINIMAL.** For any dominant `F` and any **non-linear** source
> automorphism `chi`, the top form of `F o chi` is a power of a linear form, so
> `nu(F o chi) = 1` and `E_0` is a leaf. *Proof.* The leading forms of `chi` are
> powers of one linear form `L` (JvdK); each monomial `x^iy^j` of `P` contributes
> `c_1^ic_2^j L^{d_1i + d_2j}`, so the top form of `P o chi` is a constant times a
> power of `L` unless the face sum cancels — and then the degree drops and one
> recurses. ∎
> Measured 3/3: `(x,xy)`, `(x,x^2y^2)`, `(x,x^2y^3)` have `nu = 2`, `E_0` free,
> `Psi = 0`; composing each with `chi = (x, y+x^2)` gives `nu = 1`, `E_0` a **leaf**,
> `Psi = 3, 6, 8 > 0`, and `D` raised from `2,4,5` to `3,6,8`. **So "`E_0` a leaf" is
> manufactured by degree-raising composition and destroyed by the degree-preserving
> subrectangular reduction: a NON-MINIMALITY signature.**

> **THEOREM E0-LEAF-CAP (general; no Keller, no `H2`).** If `Psi = 0` and `E_0` is a
> leaf (or an isolated vertex) of `T_+`, then, from `(FG)` and `(GD)`,
> ```text
>       Z.K_X = -Lambda - kappa <= -D - 1  ==>  D <= N + 1 - 2 g_L <= N + 1 .
> ```
> *Consequence, priced.* With MOH-FLOOR (`D >= D_min >= 101` in every gauge), CH2
> holding in **any** gauge gives `N >= 100`: **CH2 kills every `N <= 99`, not 9
> cells.** KPG's Sec 6.1 pricing is an under-reading by an order of magnitude.
> *Positive control:* the battery maps satisfying CH2 are exactly the **proper**
> ones — `(x,y^2)` `(2,2)`, `(x,y^3)` `(3,3)`, `(x^3,y^2)` `(3,6)`, `(x^2,y^3)`
> `(3,6)` — and each satisfies `D <= N + 1 - 2g_L`.

### 5.2 (a) Is the polar tree a chain (`Psi = 0`)? — **DECIDED NEGATIVE as a target**

* `Psi = 0` **fails in the control class**: `Psi = k = D` for `(x, y+x^k)` (Sec 4).
  The triangular automorphism already forks.
* The rigid object is `Psi - Lambda`: by `(FG)` + `(GD)` + MF-EXACT +
  `theta_inf = kappa`, **`Psi - Lambda = -2N + n(W-S)`** (POLAR-DEGREE). So
  `OPEN[FORK-MASS]` is not a sub-problem of the ceiling — it **is** the ceiling on a
  tree, and nothing in the Newton-polygon package bounds it.
* Unconditional gain from the gauge: `E_0` free means **the first fork of `T_+` is
  at level `>= 2`**, carried by the tangent cone of the branches at infinity
  (Sec 3.3), never by `L_infty`. So `Psi` counts characteristic pairs of the
  branches at infinity, weighted by their polar multiplicities.
* If nevertheless `Psi = 0`, then POLAR-DEGREE with MERIDIAN-FLOOR+
  (`n(W-S) >= N-1+(W-S) >= N`, using `W - S >= S >= 1` from `7.B'`) gives
  `Lambda = 2N - n(W-S) <= N`: `T_+` is a chain whose two endpoints carry total
  polar multiplicity `<= N <= 16` while `E_0`, **interior**, carries `D >= 102`. The
  chain must climb from `<= N` to `>= 102` and back, and along contracted stretches
  `m_{i-1} + m_{i+1} = m_i(-C_i^2)` — so the climb is paid for entirely by very
  negative self-intersections. That is a finite obstruction to test at a named cell,
  and the first place the `Psi = 0` branch can be attacked.

### 5.3 (c) Is `T` bounded by `50 - N`, or does Newton-polygon theory leave it free? — **FREE**

Re-derivation of the two inputs (both PROPOSALS, re-derived here):

* **DEG-SPLIT.** `sum_C Z.C = kappa + S n`, and `Ltil_red = H - sum_{prox=2}E_j` in
  `Pic X` gives `Z.Ltil_red = D - T`; hence `D = S n + kappa + T`. (The engine
  computes `T := D - Sn - kappa` and, separately, the extended-cluster satellite
  mass; they agree 46/46.)
* **HALF-CAP.** With one dicritical (forced by `7.B'` when `W <= 3`) and `D > N`
  (supplied by MOH-FLOOR): either
  `nu_l >= 2`, so `T >= (nu_l - 1)c_l >= S n`; or `nu_l = 1`, and then the unique
  free chain from `l` to `L_infty` has `sum a = D` with increasing multiplicities and
  length `>= 2`, so `2 S n <= D`. Either way `D <= 2(T + kappa)`. Sharpness at
  `(x,xy)`, `(x,x^2y^2)`; failure at `ell >= 2` (`(xy^2,xy)`, `(x^2y,xy)`,
  `(x,x(x-1)(x-2)y^2)`) reproduced on the engine.

> **THEOREM T-IS-THE-CEILING.** At `W <= 3` (so `ell = 1`), for a degree-minimal
> representative,
> ```text
>       T <= tau   <==>   D_min <= 2(tau + kappa) <= 2(tau + N) ,
>       T >= D_min/2 - kappa >= 51 - N .
> ```
> So `OPEN[SAT-MASS]` is **equivalent** to the ceiling `OPEN[N-VS-MAPDEG]` there,
> not a half of it; and SM's target `tau <= 50 - N` is exactly **one unit below its
> own proven floor** `T >= 51 - N`. A proof of `T <= 50 - N` is a proof of the
> theorem by contradiction with HALF-CAP: SAT-CROSS is correctly stated but is
> **not a cheaper price**.

**What the Newton polygon says about `T`, exactly.** `T = sum_C(nu_C - 1)c_C` with
`nu_C` the continuant of the satellite chain below `C` — the denominator data of the
Puiseux/characteristic pairs of the branches at infinity (Sec 3.3). The classical
package constrains only the **first** corner (`u >= 4`, `v <= u(u-1)`,
`u + v >= 16`, `gcd(u,v) > 1`, `2 <= f_1 < u`; GGV Prop 6.4/6.5/6.7, plus `B = 16`
or `B > 20`, Thm 7.11). **None of these bounds the number of characteristic pairs or
the depth of the cluster**, and GGV Thm 7.6's chain of regular corners is a
divisibility criterion along the corners, not a length bound. Measured: on
`psi_k o (x, x y^3)`, `k = 1,2,3`, the profile `(N, kappa, S, W) = (3,·,1,3)` is
fixed while `T = 0, 5, 8` and `nu_max = 1, 6, 9` grow.

**Unconditional gain instead.** From (MIN) + GGV Cor 6.6 + MOH-FLOOR:

> **THEOREM MOH-SHARP.** `D_min = K * max(d,e)` with `K = gcd >= 16` and
> `max(d,e) >= 3`; combined with `D_min >= 101`,
> ```text
>      D_min >= 102 ;   D_min always has a divisor K with 16 <= K <= D_min/3,
>      which excludes 101, 103, 106, 107, 109, 113, 118 in [101,120] ;
>      min(deg P, deg Q) >= 32  at the minimum.
> ```
> *Cross-validation, independent:* Moh's own surviving list before Appendix II is
> `(64,68), (84,56), (75,50), (99,66)` — i.e. `4*(16,17)`, `28*(3,2)`, `25*(3,2)`,
> `33*(3,2)`. Three of the four are exactly `K*(2,3)` with `K >= 16`; the fourth has
> `K = 4 < 16` and is killed a second time by GGV Cor 6.6. The classical
> `Ke`-structure is visible in the only published census.

## 6. Part (4): tests on the charged witnesses

**6.1 Automorphism controls** — Sec 4: `nu = 1`, `E_0` a leaf, `Lambda - Psi = 2`,
`T = D - 1`.

### 6.2 PROFILE-WITNESS `G_k = psi_k o (x, x y^4 - y^2)` — which Keller step it fails

```text
  k = 1 : D=5  N=4 nu=2 E_0 free kappa=4 Sn=1 T=0 Lambda=2 Psi=0 Z.K_X=-6 (g_L=0)
  k = 2 : D=10 N=4 nu=2 E_0 free kappa=1 Sn=2 T=7 Lambda=7 Psi=8 Z.K_X= 0 (g_L=3;
          Singular: genus = 3)
```

`G_k` has `nu = 2` and `E_0` free — the *same* first-fork shape as a counterexample,
so it does **not** fail FIRST-FORK, E0-FREE or NO-L∞-TAIL (`T = T_class` on both
rows). **The Keller-specific steps it fails are (MIN) and GGV:** `l(P) = (xy^4)^k`,
`l(Q) = xy^4` give `H = xy^4`, `K = 5 < 16` and `(d,e) = (1,k)` — so `G_k` is
target-side degree-reducible (`P - Q^k = x` drops the degree from `5k` to `1`), its
`K = 5` violates GGV Cor 6.6, and its corner `(u_1,v_1) = (1,4)` has `u_1 = 1 < 4`,
violating GGV Prop 6.7/Rem 6.8. The witness is admissible for every *numerical
profile* datum (as KPG says) and inadmissible for exactly the Newton-polygon data
this lane adds. **This is the first constraint in the campaign that the
PROFILE-WITNESS fails for a reason other than "`A_F` is smooth".**

### 6.3 HALF-CAP's two-dicritical witnesses

```text
  (x y^2, x y)  : D=3 N=1 nu=2 E_0 free ell=2 kappa=1 Sn=2 T=0 Lambda=2 Psi=0 Z.K=-3
  (x^2 y, x y)  : D=3 N=1 nu=2 E_0 free ell=2 kappa=1 Sn=2 T=0 Lambda=2 Psi=0 Z.K=-3
  (x, x(x-1)(x-2) y^2) : D=5 N=2 nu=2 E_0 free ell=3 kappa=2 Sn=3 T=0 Lambda=4
                          Psi=4 Z.K=-2  (two forks: the three dicriticals split off
                          the same vertex)
```

All three have `nu = 2` and `E_0` free, so HALF-CAP's failure is **not** a
first-fork phenomenon: it is the `ell >= 2` splitting deeper in the tree, where SM
locates it. The third row has `Psi = 4 > 0` with `T = 0` — fork mass and satellite
mass are genuinely independent, confirming KPG Sec 3.4's split.

### 6.4 The promoted `N = 4` `(B3)` data

`N = 4`, `a = 2`, `W = 2`, `S = 1` (so `ell = 1`), cusp with `K_P = 1`, `beta = 1`,
`n = 4` (MF-SHARP), hence `g_L = 0` and `theta_inf = kappa = 2` (MF-EXACT). Then:

```text
  (FG)     -2 = 4 - 2 - Lambda + Psi   ==>   Lambda - Psi = 4 .
  E0-FREE  E_0 contributes to NEITHER side: m_{E_0} = D >= 102 is absent from the
           ledger.  [KPG's "if E_0 were a leaf then Lambda >= 7, Psi >= 3": RETIRED.]
  kappa=2  one component over L_infty with k = 2, m = 2, or two with k = 1 and
           m_1 + m_2 = 4  (from N = sum m_C k_C = 4).
  T        T = D - n - kappa = D - 6, so D >= 102 gives T in {96, 98, 99, 102, ...}.
```

So the `N = 4` `(B3)` boundary tree has `E_0` interior with `m = D >= 102`, exactly
two towers, at most `kappa + ell = 3` non-contracted components, one dicritical with
`c = 4`, and `Lambda - Psi = 4`. A sharply constrained finite question for the
`B3-BOUNDARY-INSTRUMENT` lane — and **not** decided by "E_0 is a leaf".

### 6.5 Machine record

```text
ENGINE   /tmp/mks/tree.py (sha256 4b2017b1...) — two-chart blow-ups on exponent
         dictionaries over Q; returns the full dual tree of L~ with per-component
         (nu_C, m_C, c_C, C^2, adjacency), the cluster with its proximity structure,
         and the trichotomy.  Written for this lane; no code reused.
BATTERY  51 distinct maps attempted, 46 resolved exactly (D <= 48, N <= 25, r <= 25),
         each checked
         for:  Z^2 = sum m_C c_C = N ;  sum a_i^2 = D^2 - N ;  Z.K_X two ways
         (sum a_i - 3D  and  sum m_C(-2 - C^2)) ;  c_C from the tree = the proximity
         excess a_i - sum_{j->i}a_j ;  (FG) ;  (TH) ;  deg_{L~}(E_0) = nu against an
         independent top-form routine ;  deg_{T_+}(E_0) = nu when nu >= 2 ;
         (T = T_class) <=> (no L_infty tail).  **9 checks, 0 failures, 46/46**
         (driver final.py, sha256 8987bfdf...).
SKIPS    5 of the 51 skipped and reported: cluster not rational over Q (factors
         T^2+1, T^2-T+1, T^4+1).  The engine asserts and refuses.
GENUS    Singular normal.lib, 6 genus computations of {3P + 5Q - 7 = 0}, all
         matching 2 g_L - 2 = N + Z.K_X: mock(1,2;2,3) g=5 ; psi_2o(x,xy^3) g=2 ;
         psi_3o(x,xy^3) g=3 ; (x,x^3y^2) g=0 ; mock(1,3;2,3) g=3 ; G_2 g=3.  The
         last reproduces KPG's own Singular value for PROFILE-WITNESS at k = 2.
CROSS    12 rows overlap SM's sec 3 table; all columns (D, N, kappa, Lam, T,
         T_class, sum a_i, Z.K_X, nu_max) agree entry for entry from a third engine
         — including psi_4 o (x,xy^2): (12,2,1,4,7,7,36,0,8).  0 disagreements.
```

## 7. Part (5): consequences, priced

```text
 A. CELLS KILLED BY THIS LANE: none.  The lane RETRACTS conditional kills.  KPG's
    CH2 kills of the 9 cells with N = 2W (including the live N = 4 (B3)) are
    WITHDRAWN, together with CH2's negative answer to OPEN[MULT-VS-BETA]
    ("beta >= 2 forced at W = 2"), which rested on the same hypothesis.
 B. CH2 REPRICED (upward).  Proved in ANY gauge it gives D <= N + 1 - 2 g_L, hence
    with MOH-FLOOR it empties every N <= 99 -- the campaign range at once.  Not a
    lemma to aim at.
 C. CH1 REPRICED.  Psi = 0 is false for triangular automorphisms; under Keller + H2
    it forces Lambda <= N with E_0 interior carrying D >= 102.  By POLAR-DEGREE,
    Psi - Lambda IS the ceiling: OPEN[POLAR-CHAIN] and OPEN[FORK-MASS] are retyped
    as restatements of OPEN[DELTA-AFF-VS-N], not sub-problems.
 D. SAT-CROSS REPRICED.  T <= tau <=> D_min <= 2(tau + kappa) at W <= 3, so
    OPEN[SAT-MASS] = OPEN[N-VS-MAPDEG] there; and tau <= 50 - N is one unit below
    HALF-CAP's own floor T >= 51 - N.  Not a cheaper price.
 E. GAINED, UNCONDITIONAL:  D_min >= 102 with D_min = K e, 16 <= K <= D_min/3
    (MOH-SHARP; excludes 101,103,106,107,109,113,118), min(deg P,deg Q) >= 32;  T = T_class at a degree-minimal
    counterexample (NO-Linf-TAIL), so SM's definition repair is vacuous there;
    the first fork of T_+ is at level >= 2 and E_0 is free (E0-FREE).
 F. GAINED FOR (B3):  at N = 4, Lambda - Psi = 4 with E_0 free and m_{E_0} = D
    absent from the ledger; <= kappa + ell = 3 non-contracted components; exactly
    two towers with a_{p_y} <= e u_1, a_{p_x} <= e v_1, u_1 >= 4, u_1 + v_1 >= 16.
 G. NOT GAINED:  no bound on Psi, Lambda, T, n or D_min beyond E; no cell emptied;
    nothing about case (A), A2, Z(G) or the reducible branch.
```

## 8. Opens raised, with bounded quantities

```text
OPEN[FORK-DEPTH]  (new; the sharp form of OPEN[FORK-MASS] after E0-FREE).  Is the
   unweighted fork count of L~ bounded in N?  BOUNDED QUANTITY: the integer
   F := #{characteristic (Newton) pairs of the branches at infinity of the generic
   pencil member} + #{separation vertices}, in [0, r-1].  If YES and if in addition
   m_C <= N at every fork (automatic at every NON-contracted fork, since
   m_C c_C <= N), then Psi <= N F, so n(W-S) <= 2N - 2 + N F and the ceiling
   follows.  SCOPE: the second clause fails at CONTRACTED forks (E_0 has m = D,
   c = 0; family (B)'s single fork has m ~ D - 2).  Residual:
OPEN[FORK-MULT]  (new; the one integer left).  Bound m_C at the CONTRACTED forks of
   L~ for a degree-minimal Keller pair.  BOUNDED QUANTITY: m_C = -ord_C(generic
   pencil member) in Z_{>0} at the forks with Z.C = 0.  A bound m_C <= g(N), with
   OPEN[FORK-DEPTH], closes the ceiling.  Measured, NOT proved: m_C <= D = m_{E_0}
   on 44 of the 46 rows; the two exceptions, (x^3,y^2) and (x^2,y^3), both have
   D = 3 < N = 6 -- outside Lemma L4's D > N regime and outside the D_min >= 102 > N
   range that matters here.
OPEN[NU2-RIGIDITY]  (new, hygiene).  Is nu = 2 forced in EVERY degree-minimal gauge,
   or only in the subrectangular one?  BOUNDED QUANTITY: nu >= 1 at a degree-minimal
   representative.  YES makes E0-FREE gauge-free and closes CH2 outright; NO locates
   the residual freedom.  First test: does l_{1,1}(P) = alpha L^{deg P} contradict
   GGV Prop 4.1 + Thm 2.6(4) without the subrectangular reduction?
```

Carried unchanged: `OPEN[DELTA-AFF-VS-N]`, `OPEN[ANTICANON-DEFECT]`,
`OPEN[NU-BOUND]`, `OPEN[TWO-DICRITICAL]`, `OPEN[MIN-EMBED-DEGREE]`. **Retyped:**
`OPEN[SAT-MASS]` = `OPEN[N-VS-MAPDEG]` at `W <= 3` (5.3);
`OPEN[POLAR-CHAIN]`/`OPEN[FORK-MASS]` = `OPEN[DELTA-AFF-VS-N]` (5.2). **Closed:**
KPG's sub-question "is `E_0` a leaf of `T_+` at `N = 4`" — NO (5.1).

## 9. FALLACY-v2 audit

* **Flag/place/series.** Six degree-like integers kept apart and never substituted:
  `D`, `D_min`, `N`, `K = gcd(deg P, deg Q)`, `n = deg Abar_F`, `nu = #roots of the
  top form`. The collision between this lane's `nu` and SM's `nu_C` (source polar
  multiplicity) is flagged and both are written out. Moh's `d_s` is **not** `K`
  (Sec 2.2). `Lambda` (leaf mass, KPG) is not `Lam = S n` (dicritical mass, NVM).
  `theta_inf = kappa` is re-derived, not assumed.
* **Per-ray/exit-set charge.** No exit price; no `charge_basis` line. In `(TH)` each
  edge of `L~` is charged to its two endpoints once (`sum deg = 2(V-1)`) and each
  `c_C` once; the passage `(TH) -> (FG)` is charged once per dicritical and the
  `m = 0` neighbours shown to contribute zero — where a double count would hide. The
  two forms are machine-verified against each other on 46 rows.
* **Carrier/attainment; floor/attainment.** (SUBRECT) is quoted with its hypotheses
  and its degree-preservation clause; E0-FREE is stated **for that gauge**, the gauge
  dependence is attacked separately (LEAF-IS-NONMINIMAL), and the residue is typed
  `OPEN[NU2-RIGIDITY]`. `(FG)`, `(TH)`, `(GD)`, DEG-SPLIT, POLAR-DEGREE and
  FIRST-FORK are **identities**; the inequalities used are `Lambda >= 2`, `Psi >= 0`,
  `kappa in [1,N]`, `T >= 0`, `a_p <= I_p`, MERIDIAN-FLOOR+, HALF-CAP, MOH-FLOOR and
  GGV's corner bounds, cited where used. MOH-SHARP is a floor used only as a floor;
  E0-LEAF-CAP bounds `D` **under a hypothesis this lane argues is false** and is
  never banked as a kill. No cell is claimed empty and every battery map is typed
  NON-KELLER (or KELLER/INVERTIBLE/NON-MINIMAL for the automorphisms).
* **Pole/interior.** The chart at infinity enters through `(y/x, z/x)` and
  `(x/y, z/y)`; `a_p = D - max(deg_{y_p}P, deg_{y_p}Q)` is derived in the chart and
  checked against `sum_p a_p <= D` and the engine's blow-up count on every row.
  `rho_0 = 0` is used only where `D > N`.
* **Variable/ring map.** The engine declares its ring (`Q`, local coordinates
  `(s,t)`, exceptional coordinate per chart), divides by the exact order of vanishing
  with an assertion, and works in the basis `(H, E_1..E_r)`; genericity is realised
  by `(3,5,-7)`. Negative controls: the engine **refuses** on non-rational clusters
  (5 of 51 skipped, reported); the `nu` check never touches the resolution; and a
  leaf-count bound `#leaves(L~) <= kappa + ell` conjectured mid-lane was **REFUTED**
  by the engine at `(x, y+x^2)` (a contracted leaf `E_1`, `c = 0`) and is **deleted,
  not patched**.
* **Prime label / derivative; `sat()` / raw remainder.** `E_i^{strict}` vs `E_i` by
  superscript, never a prime; `q_{b'}` is a coefficient polynomial, `b'` an index;
  the only derivatives are inside `[P,Q]`. No saturation, no Groebner basis, no
  quotient normal form — polynomial `gcd` and `factor_list` over `Q` only, with a
  degree-1 assertion on every factor and an explicit `Skip` otherwise.
* **Not filled by cap or analogy.** Abhyankar–Moh, Nagata, Appelgate–Onishi,
  Heitmann, van den Essen, Jung–van der Kulk and Cassou-Noguès/Kaliman are ABSENT;
  the only literature verified here is GGV 2017 and Moh 1983, quoted with extraction
  line numbers. (LF) and (MIN) are proved, not cited.

## 10. Typed verdict block

```text
LANE       MINIMAL-KELLER-SHAPE
SCOPE      Keller, noninvertible, H2 where marked; case (B).  Case (A) EMPTY and
           untouched; A2 untouched; no Z(G)=1; no quasi-homogeneity.  Secs 3.1-3.2
           and E0-LEAF-CAP hold for EVERY dominant map.

PROVED HERE  (all PROVED-HERE, UNREVIEWED; statements and proofs in the body)
 (LF),(MIN)   Sec 2.1.  l(P)=alpha H^d, l(Q)=beta H^e, deg H = gcd; minimality <=>
              d,e >= 2 and deg P != deg Q, hence max(d,e) >= 3.
 FIRST-FORK   Sec 3.2.  deg_{L~}(E_0) = nu = #distinct roots of the top form;
              nu >= 2 => deg_{T_+}(E_0) = nu.  E_0 leaf <=> nu = 1; fork <=> nu >= 3
              (then Psi >= D).  Verified 46/46.
 E0-FREE      Sec 5.1.  In the degree-preserving subrectangular gauge a
              counterexample has nu = 2 exactly: E_0 is FREE in T_+.  CH2's
              hypothesis is FALSE there; its 9 conditional kills are WITHDRAWN.
 LEAF-IS-     Sec 5.1.  nu(F o chi) = 1 for every non-linear source automorphism:
 NONMINIMAL   "E_0 a leaf" is manufactured by degree-raising composition.  3/3.
 E0-LEAF-CAP  Sec 5.1, general.  Psi = 0 and E_0 a leaf => D <= N + 1 - 2 g_L; with
              MOH-FLOOR, CH2 in any gauge kills every N <= 99 -- it is the theorem.
 NO-Linf-TAIL Sec 3.3.  Two-sided subrectangular => sum_{level 1}a_i = D, w = nu = 2,
              no branch tangent to L_infty, T = T_class.  Measured 32/32 vs 14/14.
 (TH)         Sec 3.1.  Z.K_X = Theta - kappa - S n, Theta = sum_{L~}m_C(deg C - 2):
              the whole-boundary form of FORK-GENUS.  Verified 46/46.
 T-IS-THE-    Sec 5.3.  T <= tau <=> D_min <= 2(tau + kappa) at W <= 3;  and
 CEILING      tau <= 50 - N is one unit below the floor T >= 51 - N.
 MOH-SHARP    Sec 5.3.  D_min >= 102, with a divisor K in [16, D_min/3] (excluding
              101,103,106,107,109,113,118 in [101,120]); min(deg P,deg Q) >= 32.
 DICTIONARY   Sec 3.3.  T_+, Lambda, Psi, (s_l,mu_l), kappa, T on the Enriques tree
              of the branches at infinity; nu_C = continuant = -min(ord_C x,ord_C y),
              m_C = -ord_C(pencil member), forks = characteristic pairs +
              separations (+ E_0 if nu >= 3).

RE-DERIVED   FORK-GENUS, GENUS-DEFECT, ESCAPE-KAPPA, POLAR-DEGREE (KPG); DEG-SPLIT,
             HALF-CAP, SAT-WEIGHT's T-formula (SM).  All reproduce.

MEASURED     Sec 6.5: 51 maps attempted, 46 resolved exactly, 9 checks each, 0
             failures; 5 skips reported; 6 Singular genera; 12 rows reproduce SM's
             table from a third engine; 3 gauge-change pairs.  < 3 min, < 300 MB.

CORRECTED    KPG's CH2 (hypothesis false, kills withdrawn, conditional repriced to
             N <= 99), KPG's CH1 (Psi = 0 false in the control class), KPG's N=4
             "Psi >= 3 if E_0 a leaf" (retired), SM's extended/classical T repair
             (vacuous at a degree-minimal counterexample) and SAT-CROSS's price
             (one unit below its own floor), and MOH-FLOOR (-> D_min >= 102 with
             D_min = K e, 16 <= K <= D_min/3).  Details in Sec 7.

NOT CLAIMED  any bound on Psi, Lambda, T, n, delta_aff or D_min beyond MOH-SHARP;
             any cell EMPTY; any kill at any N; that nu = 2 holds in EVERY
             degree-minimal gauge (OPEN[NU2-RIGIDITY]); that any exhibited map
             approximates a counterexample; anything about case (A), A2, Z(G), the
             reducible branch, or the ABSENT literature.

OPENS RAISED OPEN[FORK-DEPTH], OPEN[FORK-MULT], OPEN[NU2-RIGIDITY]  (Sec 8).

SUCCESSOR    (1) OPEN[NU2-RIGIDITY]: a finite Newton-polygon question on GGV's own
                 machinery (does l_{1,1}(P) = alpha L^{deg P} survive Prop 4.1 +
                 Thm 2.6(4) without the subrectangular reduction?).  YES makes
                 E0-FREE gauge-free and closes CH2 outright.
             (2) OPEN[FORK-MULT] at N = 4 (B3): with kappa = 2, ell = 1,
                 Lambda - Psi = 4 and E_0 free with m = D >= 102, enumerate the
                 admissible T_+ shapes.  Finite; B3-BOUNDARY-INSTRUMENT owns it.
             (3) The single classical statement that would decide OPEN[FORK-DEPTH]:
                 a bound, for a degree-minimal Jacobian pair, on the NUMBER of
                 characteristic pairs of the branches at infinity of a generic
                 pencil member -- equivalently on the length k of GGV's
                 regular-corner chain (A_0,...,A_k) of Thm 7.6.  GGV bound the first
                 corner and give a divisibility criterion along the chain, but no
                 bound on k.  The cheapest remaining classical target.

DEVIATIONS   (1) Item (3)(a): the polar tree is NOT a chain in the control class and
                 the question is a restatement of the ceiling; reported as found.
             (2) Item (3)(c): the target T <= 50 - N coincides with the negation of
                 a proved floor; T retyped as the whole ceiling at W <= 3.
             (3) A leaf-count bound conjectured mid-lane was REFUTED by the engine
                 at (x, y+x^2); deleted, not patched, recorded in the audit.
             (4) 5 of 51 maps skipped for non-rational clusters.  Drivers in
                 /tmp/mks (tree.py 4b2017b1..., final.py 8987bfdf...,
                 g.sing 1d8b5938...), not installed in box/.
             (6) A regularity recorded mid-lane ("m_C <= D always") was REFUTED by
                 the consolidated battery at (x^3,y^2) and (x^2,y^3); Sec 8's OPEN
                 carries the corrected, scoped form.
             (5) SIZE: body 43.3 KB against the charged 25-40 KB band.  The overrun
                 is Sec 2 (the charged literature assembly, with exact statements
                 and line-numbered quotations) and Sec 3 (the translation with its
                 proofs); those were kept complete rather than compressed.
```

<!-- BODY-END -->
