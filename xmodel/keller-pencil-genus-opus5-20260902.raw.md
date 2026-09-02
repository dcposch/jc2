# KELLER-PENCIL-GENUS — the genus of the generic pencil member: the mechanism is the fork mass, and the obstruction is exact

Lane: `KELLER-PENCIL-GENUS`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + desk-scale CAS (Singular 4.4.1 `normal.lib`, python3; no AWS, no
fetching, no web). Drivers in `/tmp/kpg`, not installed in `box/`.

## 0. Custody, method, scope

The five charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all five match the charge exactly:

```text
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  meridian-floor-sharpen-opus5-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  meridian-floor-sharpen-review-gpt55-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  n-vs-mapdeg-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  deg-af-vs-n-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
```

Abbreviations: **MFS** = MERIDIAN-FLOOR-SHARPEN, **MR** = its gpt-5.5 hostile review,
**NVM** = N-VS-MAPDEG (the ceiling flagship), **DG** = DEG-AF-VS-N, **MI** =
MPRIME-ALLN-H2.

Typing discipline, as charged. MF-EXACT, LOC-MULT, MF-SHARP, SHARP-CHAU are consumed
at **MR's PROMOTE typing with its repairs** (MR items 1,3,4,6,7): MF-EXACT's floor is
the `S`-known one, `Phi` is a floor computed as a minimum over configurations and is
not a nonemptiness statement, and SHARP-CHAU carries its hypotheses.
**NVM is a PROPOSAL**: `(I1)`-`(I6)`, DEG-SPLIT, NOETHER-K, NO-CEILING, MOH-CROSS,
OPEN[ANTICANON-DEFECT] are consumed *only where re-derived here*, and every use is
flagged; its 41-map engine output is used as **data to be checked**, not as a premise
(and it checks out, Sec 5.2). DG is at its review's promoted typing with repairs; MI
is banked (`[P3]`, `(L)`, `(K)`, `(C1)`-`(C3)`, Lemma 4.1, 7.B', the generic meridian
cycle type, THEOREM PROFILE). Case (A) is EMPTY and is not priced; no `Z(G)=1`; no A2
cell. No canonical ledger edited; `jc2-lean` not inspected; nothing fetched
(`refs/` unchanged). **No `charge_basis` line: this report asserts no new exit price.**

## 1. Verdict, up front

```text
(1) THE SYMPLECTIC ROUTE IS A WASH, AND EXACTLY WHY.  On one fibre, "unit speed" is
    equivalent to "v|_{C_t} is etale of degree N": the 1-form omega_u = (dx^dy)/du
    restricted to C_t IS dv, its divisor is supported at infinity with ZEROS of order
    mu-1 at the nS non-proper places and POLES of order e+1 over infinity, and its
    degree identity is Riemann-Hurwitz, i.e. MF-EXACT.  The charge's paradox is
    resolved by the zeros (THEOREM UNIT-SPEED).  Existence of the mate v is
    EQUIVALENT to exactness of omega_u on every fibre -- that is the Keller
    hypothesis restated, not an extra inequality.
(2) THE MECHANISM IS ON THE BOUNDARY: THE BRANCHING OF THE POLAR TREE.
    Let T_+ = supp Z = Phi^{-1}(L_infty), a subtree of the boundary tree, with LEAF
    MASS Lambda = sum_{deg 1} m_C (= 2 m_C if T_+ is one vertex) and FORK MASS
    Psi = sum_{deg>=3} m_C(deg - 2).  For EVERY dominant polynomial F:
        (FORK-GENUS)      2 g_L - 2  =  N - kappa - Lambda + Psi ,
                          Z . K_X    =  Psi - Lambda - kappa ,      Lambda >= 2 .
    So the coordinator's desk note Z.K_X = 2 g_L - 2 - N is CONFIRMED (adjunction on
    the base-point-free net Phi^*|O(1)|), and OPEN[ANTICANON-DEFECT] is EXACTLY
    "bound the fork mass".  The charge's displayed Z.(K_X + 2Z) is off by N; the
    coordinator's form is the correct one.
(3) NEW IDENTITY:  theta_inf = kappa.  The escaping-place count of the pencil member
    IS the number of boundary components over L_infty counted with degree.  Three
    independent proofs; verified in closed form against every kappa NVM's engine
    reports (15/15).  Consequences: SHARP-CHAU sharpens to  D >= nS + kappa; and
    SHARP-CHAU is DEG-SPLIT plus T >= 0 -- two separately banked statements coincide,
    with defect exactly the satellite mass.
(4) CONDITIONAL CEILING, PRICED.  Psi = 0 (polar tree a chain)  ==>
    g_L <= (N-1)/2 and n (W-S) <= 2N - 2, hence delta_aff finite at every N -- the
    finiteness DG Sec 6.2 and CD Sec 3 want.  Adding "E_0 is a leaf of T_+" gives
    n W <= 2N - 2, which KILLS the 9 cells with N = 2W (including the live N = 4 (B3)
    cell) and refutes beta = 1 at W = 2.  Neither hypothesis is proved; both are
    now single, checkable statements about the SHAPE of the boundary tree.
(5) NEGATIVE ROUTE: EXECUTED, IN CLOSED FORM.  At every fixed N >= 2 the genus is
    UNBOUNDED in the dominant class:  psi_k o (x, x y^m) has N = m and
        2 g - 2 = (m-1)(k+1) - m - gcd(k-1,m)  ->  infinity   (THEOREM NEG-GENUS),
    machine-verified at 15 points.  Worse: at N = 4 the family psi_k o (x, xy^4 - y^2)
    matches [P3], (C1), 7.B', (K), the cycle type 1^2 . 2 and H2's irreducible
    one-place-at-infinity A_F, with g -> infinity (g = 0,3,4 at k = 1,2,3).
    NO profile datum can bound g_L.
(6) TYPED CORRECTION TO NVM (PROPOSAL).  Its OPEN[ANTICANON-DEFECT] scope note says
    "what makes them work is the affine ramification term Z.R_aff, which Keller
    kills".  In the witnessing family Z.R_aff = N - 1 EXACTLY, constant in k, while
    2g-2 grows linearly in k.  Deleting a bounded term cannot bound a divergent one:
    the Keller condition, entered through NOETHER-K alone, is quantitatively
    incapable of producing a ceiling.
(7) CONTROLS.  61 Singular genus computations, 0 mismatches; NVM's entire family-(A)
    and family-(B) engine output (kappa, Lambda, T, sum a_i, Z.K_X) reproduced in
    CLOSED FORM by a route that never resolves a base locus.  The Suzuki/Euler
    ledger closes exactly on MI's promoted N = 4 (B3) data (b_1 = 5 = 2.W + 1).
```

## 2. Part (1): the fibre as a unit-speed etale cover

### 2.1 Set-up, and MF-EXACT re-derived as the control

`F = (P,Q)` Keller (normalise `Jac F = 1`), noninvertible, geometric degree `N`,
`H2`. Fix generic `(alpha,beta)`, put `u = alpha P + beta Q` and choose
`v = gamma P + delta Q` with `{u,v} := Jac(u,v) = alpha delta - beta gamma = 1`.
Since `dP ^ dQ = dx ^ dy` is nowhere zero, `dP, dQ` are everywhere independent, so
**every member of the pencil is a submersion**: `C_t := u^{-1}(t)` is smooth for all
`t`, and `X_u := (-u_y, u_x)` is a nowhere-vanishing polynomial vector field tangent
to every `C_t` with `X_u(v) = 1` (unit speed).

`v|_{C_t} : C_t -> A^1` is **etale of degree `N`**: `dv` is nowhere proportional to
`du`, so `dv|_{ker du} != 0`; and `#(v|_{C_t})^{-1}(s) = #F^{-1}(t,s) = N` off `A_F`.
Its non-properness set is the `n` points of `L_t cap A_F`, `L_t := {u = t}`.

Topologically: `C_t ∖ v^{-1}(B_t) -> C ∖ B_t` (`B_t = L_t cap A_F`, `#B_t = n`) is an
`N`-sheeted covering with monodromy `rho_t = rho o (pi_1(L_t ∖ A_F) ↠ G)`, transitive
(Zariski + LEMMA E-ETALE). Under `H2` each `rho_t(sigma_i)` has the generic cycle
type `1^a prod_l mu_l^{s_l}` (MI:694-695), so `c(sigma_i) = a + S` and
`N - c(sigma_i) = W - S`; over `infty` the fibre has `theta_inf` points. Only the
`a` fixed points of `sigma_i` are filled in (the `a` affine preimages); the `S`
cycles are the escaping ends. Riemann-Hurwitz on the compactified `pi : X_L -> P^1`:

```text
      2 g_L - 2 = -2N + n (W - S) + (N - theta_inf)   <=>   MF-EXACT.
```

That is the charged control, reproduced from the covering data alone. **Note what it
says: `g_L` is a FUNCTION of `(N, a, W, S, n, theta_inf)`.** It is not an independent
invariant, and MR's `N = 4` reading (`n = 4 ⟹ (g_L,theta_inf) = (0,2)`) is the
substitution.

### 2.2 The 1-form route: where the charge's paradox breaks

`dx ^ dy = du ^ dv`, so the Gelfand-Leray form `omega_u := (dx^dy)/du` restricts on
`C_t` to `dv|_{C_t}`, regular and **nowhere vanishing** (etaleness). The charge's
paradox — "`(omega) = -sum c_P P` with `c_P >= 1`, hence `2g-2 <= -theta_L`" — fails
at the first step: `div(omega)` is supported at infinity but is **not** a sum of
poles. Write `theta_L = nS + theta_inf` for the places at infinity of `C_t`. Then

```text
   at a NON-PROPER place P (v regular, v - v(P) = tau^{mu} . unit):  ord_P(dv) = mu - 1 >= 0   [a ZERO]
   at a place over infty     (v has a pole of order e):              ord_P(dv) = -(e+1)        [a POLE]
   deg div(dv) = sum_{nS places} (mu_l - 1) - sum_{theta_inf}(e_P + 1)
               = n(W - S) - N - theta_inf  =  2 g_L - 2   by MF-EXACT.
```

The `nS` escaping places carry **zeros**, not poles; that is exactly the datum the
naive count omitted. And the degree identity *is* Riemann-Hurwitz. Residues vanish
(`dv` exact), periods vanish (`v` single-valued) — both automatic, so neither is a
condition. **The 1-form route returns MF-EXACT and nothing else.**

### 2.3 THEOREM UNIT-SPEED — the symplectic datum on a fibre, exactly

> **THEOREM UNIT-SPEED.** Let `C` be a smooth connected affine curve. The following
> are equivalent: (i) `C` carries a nowhere-vanishing regular exact 1-form `omega`
> with `deg(pole part) = N`; (ii) `C` carries a nowhere-vanishing regular vector
> field `xi` and a regular function `v` with `dv(xi) = 1` and `deg v = N`;
> (iii) there is an etale morphism `v : C -> A^1` of degree `N`.
> Under any of them the genus is determined by the covering data by Riemann-Hurwitz
> and by nothing else. Consequently the pair `(X_u, v)` on a single fibre `C_t`
> carries **no information beyond** `(n, N, a, W, S, theta_inf)`.
>
> *Proof.* (ii)⇔(iii): `xi` trivialises `TC`, and `dv(xi) = 1` says `dv` never
> vanishes, i.e. `v` is etale; conversely `xi := (dv)^{-1}`. (i)⇔(iii): `omega`
> exact and nonvanishing means `omega = dv` with `v` regular and etale, and the pole
> degree of `dv` is `sum (e_P + 1) - theta_inf = N`. The last sentence is Sec 2.2. ∎

Two corollaries worth stating because they close charged sub-questions.

* **The "all periods vanish" clause is vacuous.** `omega_u|_{C_t} = dv` is exact, so
  every period over `H_1` (rank `2g_L + theta_L - 1`) vanishes automatically, as do
  the residues at the `theta_inf` poles (`res` of an exact form is `0`).
* **What the symplectic structure DOES say, globally, is the Keller hypothesis
  itself.** A mate `v` with `{u,v} = 1` exists iff `omega_u` is exact on every fibre
  of `u` (integrate `omega_u` from a section; algebraicity is the residual). So
  "consume the symplectic datum" and "consume `Jac F in C^*`" are the same
  instruction; the symplectic language adds no independent inequality. This is why
  Sec 3, not Sec 2, carries the mechanism.

**Negative control (charged item 1, and it bites).** Being a submersion is worthless
by itself: `f_b = x + x^2 y^b` has `(f_b)_x = 1 + 2xy^b`, `(f_b)_y = b x^2 y^{b-1}`
with no common zero, and its generic fibre `y^b = (c-x)/x^2` is a superelliptic curve
with `2g - 2 = b - 2 - gcd(2,b)`, so `g -> infinity`. Driver `genus3.sing`: `std` of
the critical ideal is the unit ideal for `b = 2..9`, and Singular's `genus` returns
`0,1,1,2,2,3,3,4` — the closed form at `8/8`.

## 3. Part (2): the boundary — the mechanism

Notation as in NVM Sec 2.3, re-derived here. Homogenise `P,Q` to `D := max(deg P,
deg Q)`; `sigma : X -> P^2` resolves the base locus of the net
`V := <P^h_D, Q^h_D, z^D>` (all base points on `L_infty`), `Phi = F-bar o sigma :
X -> P^2` a morphism of degree `N`, `L~ := X ∖ A^2` an SNC **tree of smooth rational
curves** (`X` is `P^2` blown up at points over `L_infty`), `Z := Phi^*(L_infty)
= sum_C m_C C`, `c_C := Z.C`, `T_+ := supp Z = Phi^{-1}(L_infty)`.

### 3.1 GENUS-DEFECT: the coordinator's note, confirmed, and the charge's slip

`Phi^*|O_{P^2}(1)|` is **base-point-free** (pullback of a bpf system under a
morphism), so by Bertini its generic member `D_L := Phi^*(L)` is smooth, and it is
irreducible (MFS Sec 2.3). `D_L cap A^2 = F^{-1}(L) = C_L`, so `D_L` **is** the
smooth model `X_L`, and adjunction on `X` gives

> **THEOREM GENUS-DEFECT.** `2 g_L - 2 = Z.(Z + K_X) = N + Z.K_X`, i.e.
> `Z.K_X = 2 g_L - 2 - N`. **The anticanonical defect of the base cluster is the
> genus of the generic pencil member.** (No Keller, no `H2`.)

**Typed correction to the charge.** The charge displays `2 g_L - 2 = Z.(K_X + 2Z)
= Z.K_X + 2N`. `K_X - pi^*K_{P^1} = K_X + 2Z` is the relative canonical class only on
the model where `Z` is a *fibre* class (`Z^2 = 0`), and there `Z.(K_X + 2Z) = Z.K_X`.
On `X` one has `Z^2 = N != 0` and the correct statement is adjunction, `Z.K_X + N`.
The coordinator's desk note is the correct form; nothing downstream changes.

### 3.2 THEOREM ESCAPE-KAPPA — the escaping-place count is a boundary invariant

Let `kappa := sum_{C : Phi(C) = L_infty} k_C`, `k_C := deg(Phi|_C)` (NVM `(I2)`,
re-derived below).

> **THEOREM ESCAPE-KAPPA.** For every dominant polynomial `F` and generic direction,
> `theta_inf = kappa`.
>
> *Proof 1 (base points).* Let `z_u = L cap L_infty`. For generic `z_u`,
> `Phi^{-1}(z_u)` consists of exactly `kappa` points: each `C` with `Phi(C) =
> L_infty` contributes `k_C` unramified points, contracted components map to points
> `!= z_u`, and dicriticals map onto `A_F-bar`, which meets `L_infty` only at the
> place of `A_F-bar` at infinity. Every such point lies on `D_L = Phi^*(L)` (its
> image `z_u` lies on `L`), `D_L` is smooth, and these are precisely the points of
> `D_L` over `infty in L ≅ P^1`. Hence `theta_inf = kappa`. ∎
>
> *Proof 2 (consistency).* GENUS-DEFECT plus NOETHER-K plus MF-EXACT are compatible
> **iff** `theta_inf = kappa`; two of the three are independently proved, so the
> third forces it.
>
> *Proof 3 (branch degree).* `K_X = -3Z + R` gives `2g_L - 2 = Z.R - 2N`, and
> `Z.R = Z.R_aff + (N - kappa) + n(W-S)`; equate with MF-EXACT.

**Consequences.** (`(a)`-`(d)` below are used in Sec 3.4, 5 and 6.)

```text
   (a)  1 <= theta_inf = kappa <= N (from N = sum m_C k_C, m_C >= 1): a boundary proof
        of the banked range, with equality iff every component over L_infty is reduced.
   (b)  SHARP-CHAU (MR item 7, CONFIRMED) becomes      D_F >= n S + kappa .
   (c)  DEG-SPLIT (NVM, PROPOSAL) reads D = nS + kappa + T under H2, so SHARP-CHAU IS
        DEG-SPLIT together with T >= 0: the slack in Chau's cap is EXACTLY the
        satellite mass, and two separately banked statements coincide.
   (d)  OPEN[MF-DEFECT] becomes: can kappa = 1 and g_L = 0 happen?  kappa = 1 means
        ONE boundary component dominates L_infty, with k_C = 1 and m_C = N.
```

### 3.3 THEOREM FORK-GENUS — the genus as a boundary-tree functional

Three elementary facts, each self-contained (they are NVM's `(I2)`-`(I4)`, but the
proofs below do not consume NVM):

```text
 (i)   Z.C = c_C  =  0 (C contracted) ,  k_C (Phi(C) = L_infty) ,  s_l n_{c(l)} (C
       dicritical, and then m_C = 0 since Phi(C) ⊄ L_infty).
 (ii)  Z.C = m_C C^2 + sum_{C' adj C} m_{C'}   (SNC: C'.C in {0,1}),
       hence  m_C(-C^2) = sum_{C' adj C} m_{C'} - c_C .
 (iii) T_+ is a SUBTREE.  Blowing up the theta_inf base points of the pencil makes it
       a morphism pi : X' -> P^1 with connected fibres (the generic member is
       irreducible); pi^{-1}(infty) is connected and its image in X is T_+.
```

Define, on the subtree `T_+` with `deg` = valency **inside `T_+`**,

```text
      Lambda  :=  sum_{deg C = 1} m_C  +  2 sum_{deg C = 0} m_C     (LEAF MASS, >= 2)
      Psi     :=  sum_{deg C >= 3} m_C (deg C - 2)                  (FORK MASS, >= 0)
```

so that `sum_{C in T_+} m_C (deg C - 2) = Psi - Lambda` (valency-2 vertices are free).

> **THEOREM FORK-GENUS.** For every dominant polynomial `F : A^2 -> A^2`,
> ```text
>        Z . K_X   =   Psi - Lambda - kappa ,
>        2 g_L - 2 =   N - kappa - Lambda + Psi .
> ```
> *Proof.* Boundary components are smooth rational, so `K_X.C = -2 - C^2` and
> `Z.K_X = sum_{C in T_+} m_C(-2 - C^2) = sum_{T_+}[ -2 m_C + sum_{C' adj C} m_{C'} -
> c_C ]` by (ii). The double sum is `sum_{C' in T_+} m_{C'} deg_{T_+}(C')` (neighbours
> with `m = 0` contribute nothing), and `sum_{T_+} c_C = kappa` by (i). Hence
> `Z.K_X = sum_{T_+} m_C(deg - 2) - kappa = Psi - Lambda - kappa`. Add
> GENUS-DEFECT. ∎

**Controls (hand-resolved clusters).** `F = id`: `T_+ = {L_infty}`, `m = 1`,
`Lambda = 2`, `Psi = 0`, `N = kappa = 1` → `2g-2 = -2` ✓. `F = (x,y^2)`: the cluster
is two free/satellite points, `T_+ = E_0(2) — E_2(2) — E_1(1)` a chain,
`Lambda = 3, Psi = 0, N = 2, kappa = 1` → `2g-2 = -2` ✓ (Singular: `g = 0`).
`F = (x^2,y^2)`: `Phi = [x^2:y^2:z^2]` is a morphism, `T_+ = {L_infty}` with `m = 2`,
`Lambda = 4, Psi = 0, N = 4, kappa = 2` → `2g - 2 = -2` ✓ (the fibres are smooth
conics).

### 3.4 What must be controlled, and the conditional ceiling

Substituting MF-EXACT (Keller + `H2`) into FORK-GENUS:

> **COROLLARY POLAR-DEGREE.** `n (W - S) = 2N - Lambda + Psi`.
>
> **COROLLARY CHAIN-CEILING.** If `T_+` is a **chain** (`Psi = 0`) then
> ```text
>        g_L <= (N - kappa)/2 <= (N-1)/2 ,        n (W - S) <= 2N - 2 .
> ```
> If moreover `E_0` (the strict transform of `L_infty`, which always has `m = D`) is
> a **leaf** of `T_+`, then `Lambda >= D + 1` and, with SHARP-CHAU `D >= nS + kappa`,
> ```text
>        n W  <=  2N - 2 .
> ```

This answers charged item (2) exactly. Writing `2 g_L - 2 = Z.R - 2N` with
`Z.R = Z.R_aff + (N - kappa) + n(W-S)`, the **positive** contributions to the genus
are: (α) the over-`L_infty` part `N - kappa in [0, N-1]` — bounded by `N`, harmless;
(β) the dicritical part `n(W-S)` — the unknown; (γ) the affine part `Z.R_aff` — which
Keller deletes. In the tree language of FORK-GENUS the same statement is sharper:
the only positive term is `Psi`, carried **exactly by the branch vertices of the
polar subtree**, and the only negative terms are `kappa` and the leaf mass. So:

```text
   OPEN[ANTICANON-DEFECT]  ==  bound  Psi - Lambda  ==  bound the BRANCHING of T_+ .
```

NVM Sec 3.1 already observed that the determinant package "cannot bound the number of
forks, the chain length, or the degree". FORK-GENUS upgrades that remark to an exact
identity: **the forks are not merely uncontrolled, they are the entire content of the
ceiling.** Symmetrically, NVM's free datum `T` (satellite mass) is the *chain-length*
half, and the two are disjoint: blowing up a satellite point changes no valency, while
a free blow-up on a component of valency `>= 2` creates a fork. Hence

```text
   OPEN[N-VS-MAPDEG] (upper half)  =  [ chain length: OPEN[SAT-MASS] ]
                                   AND [ branching:   OPEN[FORK-MASS] ] ,
   and only the second one controls the genus / delta_aff.
```

### 3.5 Where `Jac F in C^*` enters, and what it forbids

Exactly one place: `R = K_X + 3Z` is the ramification divisor of `Phi`, and Keller
says `R_aff = 0` — `Phi` is unramified over `A^2 ∖ A_F`, equivalently `v|_{C_t}` is
etale (Sec 2.1), equivalently the generic pencil member is smooth with no affine
critical point. Quantitatively it deletes `Z.R_aff` from `2g_L - 2 = Z.R - 2N`. It
forbids nothing else in this ledger: `N - kappa` and `n(W-S)` survive verbatim, and
`Psi` is untouched. Sec 5.5 shows that this deletion is **quantitatively too small**
to be the mechanism.

## 4. Part (3): the degeneration ledger, and what it is worth

### 4.1 Euler defects of the pencil, in closed form

For `c` a value of `u`, `chi(C_c) = N(1 - #B_c) + sum_{p in B_c} a_p` where
`B_c = L_c cap A_F` and `a_p = #F^{-1}(p) cap A^2`; `chi(C_gen) = N - nW`. Hence
`lambda_c := chi(C_c) - chi(C_gen) >= 0` (Ha-Le) is:

```text
   simple tangency of L_c with A_F at a smooth point :   lambda = W
   L_c through P in Sing A_F                         :   lambda_P = (mult_P - r_P) W - K_P
   L_c through an ordinary node/ordinary multiple pt  :   lambda = 0  (NOT atypical)
```

using Lemma 4.1's `N - a_P = r_P W + K_P`. Nonnegativity of `lambda_P` gives
`mult_P >= r_P + K_P/W` — a **second, independent, weaker proof of LOC-MULT**
(`W` in place of `W - S`), hence a positive control on MR item 3.

### 4.2 THEOREM ATYPICAL-LEDGER — Suzuki's ledger is Riemann-Hurwitz for `A_F`

Suzuki: `1 = chi(C_gen) + sum_c lambda_c`, so `sum_c lambda_c = nW - N + 1 =
b_1(C_gen)` (an affine curve is a wedge of `1 - chi` circles). Substituting Sec 4.1
and `sum_P K_P = a - 1` (`(K)`), with `tau` = number of simple tangent lines through
the pencil direction `z_u`:

> **THEOREM ATYPICAL-LEDGER.** `tau + sum_{P in Sing_aff A_F} (mult_P - r_P) = n - 1`.

This is precisely Riemann-Hurwitz for the degree-`n` projection
`P^1 ≅ norm(A_F-bar) -> P^1` from `z_u`: total ramification `2n - 2`, of which `n - 1`
sits at the unique place at infinity (`H2`: `(L_infty . A_F-bar) = n` at one place),
`mult_P - r_P` at each affine singular point, and `1` at each simple tangency. So the
coordinator's desk observation is confirmed: **the Euler-defect ledger of the pencil
reproduces the `(K)` ledger, and nothing more** — it is an identity, not an
inequality, and it is blind to `g_L` except through `n`.

*Aside (a floor, dominated).* `tau >= 0` with LOC-MULT gives
`n >= 1 + sum_P max(ceil(K_P/(W-S)), [P unibranch singular])`; over MFS's 81 cells
this never exceeds `Phi` (at `W=2, beta=1` it returns `N-1` or `N` where `Phi` gives
`N`; at large `W`, `3` against `4`). Recorded as a control, not a gain. `tau >= 1` is
**not** free — the tricuspidal quartic has `tau = 0`.

### 4.3 Vanishing cycles: also an identity. The `N = 4` control

`H_1(A^2) = 0` forces the coinvariants of the pencil monodromy on `H_1(C_gen)` to
vanish, i.e. the vanishing cycles must span; and `sum_c lambda_c = b_1(C_gen)`
exactly. So the "rank needed vs. rank available" comparison the charge asks for is
**tight by construction** and yields no inequality: the atypical values are
`tau + #{P : lambda_P > 0} <= (n-1) + s`, which bounds the number of atypical values
by `n`, not `n` by anything.

**Control at MI's promoted `N = 4` (B3) data** (`N=4, a=2, W=2, S=1`, cusp with
`K=1`, fibre partition `(3,1)`, double points `(2,2)`, `beta = 1`), with the
MF-SHARP value `n = 4`:

```text
   MF-EXACT     n = 2 + 2 g_L + theta_inf  ->  g_L = 0 , theta_inf = kappa = 2.
   A_F          rational quartic, delta_aff = 3 = one cusp + two nodes.
   ATYPICAL     tau + (2 - 1) = 3   ->  tau = 2.
   SUZUKI       sum lambda = tau . W + [(2-1).2 - 1] = 4 + 1 = 5.
   b_1(C_L)     nW - N + 1 = 8 - 4 + 1 = 5.                     AGREE.
   FORK-GENUS   -2 = 4 - 2 - Lambda + Psi   ->  Lambda - Psi = 4;
                and if E_0 were a leaf of T_+ then Lambda >= D+1 >= nS+kappa+1 = 7,
                so Psi >= 3:  the N=4 polar tree must FORK, or E_0 is not a leaf.
```

**Control on automorphisms** (`N = 1`, `A_F = ∅`, `n = 0`): `b_1(C_L) = 0 - 1 + 1 = 0`
✓ (`C_L ≅ A^1`), no atypical values, `g_L = 0`, `theta_inf = kappa = 1`, and
FORK-GENUS returns `Psi - Lambda = -2`, i.e. `Z.K_X = -3`: **Noether's equation**.

## 5. Part (4): the negative route

### 5.1 The route is unavailable inside the class — and what to do instead

A family of *noninvertible Keller* pencils at fixed `N` with `g_L -> infinity` would
in particular exhibit a noninvertible Keller map, i.e. refute JC(2). So charged item
(4) cannot be executed literally; the honest execution is to relax one hypothesis at
a time and measure which relaxation admits divergence. All three relaxations below
do admit it, in closed form.

### 5.2 THEOREM NEG-GENUS — unbounded genus at fixed `N`, and NVM's engine reproduced

Let `psi_k(u,v) = (u + v^k, v)` and `F_{m,k} := psi_k o (x, x y^m)`, `m >= 1, k >= 1`.

> **THEOREM NEG-GENUS.** `F_{m,k}` is dominant with geometric degree `N = m`
> (independent of `k`), `A_F = {U = V^k}` irreducible rational with one place at
> infinity, `n = k`, `a = 0`, `W = m`, `S = 1`, `mu = m`, `D = (m+1)k`, and
> ```text
>     2 g_L - 2 = (m-1)(k+1) - m - gcd(k-1, m) ,      theta_inf = kappa = gcd(k-1, m) ,
>     Z.R_aff = m - 1 = N - 1 ,   T = (m-1+1)k - gcd(k-1,m) ... (see table) .
> ```
> Hence for every `m >= 2`, `g_L -> infinity` as `k -> infinity` at fixed `N = m`.
>
> *Proof.* On `{u = t}` put `w := Q = x y^m`; then `x = (t - beta w - alpha w^k)/alpha`
> and the fibre is the superelliptic curve `y^m = w/(t - beta w - alpha w^k)`, whose
> right side has divisor `(0) - sum_{k roots} + (k-1)(infty)` on `P^1_w`;
> Riemann-Hurwitz for the cyclic `m`-cover gives the genus. On the fibre
> `v = gamma t + (delta - gamma beta) w`, so `v -> infty` exactly over `w = infty`,
> where the cover has `gcd(k-1,m)` places. The affine ramification of `v|_{C_t}` is
> the single point `w = 0` with `ord(w) = m`, contributing `m-1`; independently
> `Jac = m x y^{m-1}`, `Phi` maps `{y=0}~` with degree 1 onto a line and contracts
> `{x=0}~`, so `Z.R_aff = m-1`. ∎

**Machine control (`genus2.sing`, Singular `normal.lib`).** `g` for `m = 1,2,3` and
`k = 2..6`: `0,0,0,0,0 | 1,1,2,2,3 | 2,3,3,5,6` — the closed form at **15/15**.

**NVM's engine, reproduced in closed form.** Family `(B)` = `F_{m,k}` and family
`(A)` = `(x, x^c y^N)` are the two families NVM's blow-up engine reports. Here they
are recomputed with no resolution of any base locus, from the superelliptic normal
form alone (for `(A)`: `y^N = (t - alpha x)/(beta x^c)`, `v = A x + B`):

```text
 family (A):  2 g_L - 2 = N - 1 - gcd(c,N) - gcd(c-1,N) ,  theta_inf = kappa = gcd(c-1,N),
              S n = Lambda_dicritical = gcd(c,N) ,  T = D - gcd(c,N) - gcd(c-1,N) ,
              Z.K_X = -1 - gcd(c,N) - gcd(c-1,N)  <= -3   (genus BOUNDED: g <= (N-3)/2)
 family (B):  as in NEG-GENUS ;  Z.K_X = (m-1)(k+1) - 2m - gcd(k-1,m) -> +infinity
              (genus UNBOUNDED)
```

Checked against NVM's printed engine columns: `kappa` 15/15 (both families, incl.
`(x,x^c y^8)`: `8,1,2,1,4`), `Lambda` 5/5, `T` 15/15, `sum a_i` 4/4, `Z.K_X` 10/10.
**0 mismatches.** Singular `genus` verifies family `(A)` at 28 further points
(`genus4.sing`, `N = 2..8`, `c = 1..4`) — again `28/28`. This is an independent
confirmation of the charged PROPOSAL's engine by a disjoint method.

### 5.3 The dichotomy the two families realise, and THEOREM PROFILE-WITNESS

```text
   family (A):  D -> infinity , n = 1 fixed , g bounded by (N-3)/2 ,  Psi - Lambda <= -2
                -> pure SATELLITE growth (T -> infinity), no branching.
   family (B):  D -> infinity , n = k -> infinity , g -> infinity ,
                Psi - Lambda = (m-1)(k+1) - 2m -> infinity
                -> pure FORK growth.
```

This is exactly the `T` / `Psi` split of Sec 3.4, realised. Family `(B)` has `a = 0`,
so it violates `(C1)`. The following family does not:

> **THEOREM PROFILE-WITNESS.** Let `G_k := psi_k o (x, x y^4 - y^2)`. Then for every
> `k >= 1`, `G_k` is a dominant polynomial map with
> ```text
>    N = 4 ,  a = 2 ,  W = 2 ,  S = 1 ,  mu = 2  (generic meridian cycle type 1^2 . 2),
>    a + W = N  [P3] ,  2a >= N  (C1) ,  mu >= 2  (7.B') ,  sum_P K_P = 1 = a - 1  (K),
>    A_F = {U = V^k} irreducible, rational, one place at infinity  (H2 shape), n = k,
> ```
> and the generic pencil member satisfies `g_L >= 2 ceil((k+1)/2) - 3 -> infinity`.
>
> *Proof.* Over `(s,w)`, `s y^4 - y^2 - w = 0`; with `Y = y^2`, `Y_- -> -w` gives two
> finite preimages (`a = 2`) and `Y_+ ~ 1/s` gives `y ~ ± s^{-1/2}`, one 2-cycle
> (`mu = 2, S = 1, W = 2`), so `N = 4`. At `w = 0` there is one preimage, so
> `K = 4 - 1 - 1.2 = 1 = a - 1`. On `{u = t}`, eliminating `x` gives
> `alpha(w + Y) = Y^2(t - beta w - alpha w^k)`, a conic in `Y` over `P^1_w` whose
> smooth model is the hyperelliptic curve `z^2 = alpha^2 + 4 alpha w(t - beta w -
> alpha w^k)` of degree `k+1`, genus `g_D = ceil((k+1)/2) - 1`; the fibre is a degree-2
> cover of it (`y = ± sqrt Y`), so `g_L >= 2 g_D - 1`. ∎
>
> **Machine control (`genus6.sing`):** `g = 0, 3, 4` at `k = 1,2,3` (degrees 5,10,15).

**Scope, stated exactly.** `G_k` violates `Jac in C^*`, and consequently its `A_F` is
*smooth*, which MI's Prop 6.1 forbids under Keller. So the witness matches every
*numerical/combinatorial* profile constraint in the banked ledger but not the
Keller-derived requirement that `A_F` be singular. That residue is not a constraint on
the genus: MFS Sec 3.3 already certified (machine-verified, with LOC-MULT added) that
`delta_aff` is **unbounded above in every cell**, so adding singularities is a free
degree of freedom in the ledger, not a bound. `OPEN[SING-WITNESS]` below asks for the
strengthening anyway, because a *failure* to build it would itself be a mechanism.

### 5.4 The instrument / counterexample table

```text
 hypothesis dropped                     witness              N fixed?  g -> inf?
 ---------------------------------------------------------------------------------
 nothing (noninvertible Keller)         NONE POSSIBLE        --        would refute JC(2)
 Jac in C^* only                        F_{m,k}   (5.2)      yes       YES, Z.R_aff = N-1
 Jac in C^*, keeping [P3],(C1),7.B',(K) G_k       (5.3)      yes (=4)  YES
 mate v (keep submersion only)          x + x^2 y^b (2.3)    n/a       YES
 ambient = A^2 (keep symplectic+etale)  C_0 x A^1 (below)    yes       YES
```

Last row: take `C_0 = {y^2 = f(x)}` minus its `2g+2` branch points with `v_0 = x`
(etale of degree `2`, `g` arbitrary), and on `S := C_0 x A^1_t` put `u := t`,
`v := v_0`, `omega := dv_0 ^ dt`. Then `S` is smooth affine with
`kappa-bar = -infinity` and trivial canonical bundle, `du ^ dv = -omega` is nowhere
zero, `F = (u,v)` is dominant of degree `2` and non-proper, and every fibre of `u`
has genus `g` (any `N` by taking `v_0` of degree `N`). (`A_F` is a union of parallel lines, so this witness is not
`H2`-shaped; its point is that `S ≅ A^2` — contractibility, `Pic = 0`, AMS — is
load-bearing and is **not** implied by "affine, `kappa-bar = -infinity`, trivial `K`".)

### 5.5 TYPED CORRECTION to NVM's `OPEN[ANTICANON-DEFECT]` scope note

NVM (PROPOSAL) writes: *"any proof of a Keller bound must use `Jac F in C^*`
essentially — these families are exactly the `n -> infinity` shape, and what makes
them work is the affine ramification term `Z.R_aff`, which Keller kills."* The first
clause is right; the second is quantitatively wrong, and this matters because it is
the report's stated reason for hope.

```text
   In family (B) -- NVM's own witness, psi_k o (x, x y^m) --
        Z . R_aff  =  m - 1  =  N - 1 ,      CONSTANT in k,
   while 2 g_L - 2 = (m-1)(k+1) - m - gcd(k-1,m) grows linearly in k.
   Two independent derivations (Sec 5.2): the RH bookkeeping on the fibre (the single
   affine point w = 0 with ord(w) = m) and the direct branch computation from
   Jac = m x y^{m-1}.
   Deleting a term bounded by N cannot bound a divergent one.  Therefore the Keller
   hypothesis, entered ONLY through NOETHER-K (i.e. through R_aff = 0), CANNOT produce
   a ceiling.  It must be used somewhere else -- and by Sec 3.4 the only place left in
   the ledger is the shape of the polar tree.
```

This does not weaken `OPEN[ANTICANON-DEFECT]`; it re-points it. Combined with
FORK-GENUS the open acquires a concrete bounded quantity for the first time.

## 6. Part (5): consequences, priced

### 6.1 What the conditional ceiling buys

Driver `price.py`, over MFS's 81 counting-admissible cells (`Phi` consumed at MR's
CONFIRMED strength, as a floor; profiles enumerated over all dicritical multisets with
`mu_l >= 2`, `sum s_l mu_l = W`):

```text
 CH1  (Psi = 0):                 n <= (2N-2)/(W-S) .  Kills 0 of 81 cells.
      It DOES make the (B3) enumeration finite at every N:  delta_aff <= p_a(n_max),
      e.g. N=4: n<=6, delta_aff<=10 ; N=8: n<=14, delta<=78 ; N=16: n<=30, delta<=406.
      It never reaches the (B2) death thresholds (3 for N<=10, 1 for N>=11): those
      need n <= 4, i.e. 2N - 2 <= 4(W-S), impossible since W-S <= W-1 <= N/2 - 1.
 CH2  (Psi = 0 AND E_0 a leaf of T_+):   n W <= 2N - 2.  Kills exactly the 9 cells
      with N = 2W:  (4,2), (6,3), (8,4), (10,5), (12,6), (14,7), (16,8), (18,9),
      (20,10)  -- including the campaign's live N = 4 (B3) cell.
      At W = 2 it gives n <= N-1, contradicting MF-SHARP's n >= N when beta = 1:
      so under CH2, beta >= 2 is FORCED at W = 2  (a conditional answer to
      OPEN[MULT-VS-BETA], in the negative direction).
```

Read the other way — and this is the useful reading — the promoted floors *force*
structure on the polar tree of any surviving cell:

```text
   Psi  =   Lambda - 2N + n (W - S)                     [POLAR-DEGREE, exact]
        >=  Lambda - N - 1 + (W - S)      [MERIDIAN-FLOOR+ (NVM, PROPOSAL):
                                           n(W-S) >= (N-1) + (W-S)]
   at N = 4 (B3) with n = 4:  Lambda - Psi = 4 exactly; if E_0 is a leaf, Psi >= 3.
```

### 6.2 MOH-CROSS, `(B2)`, `(B3)`

* **MOH-CROSS is not reached.** It needs `D_min <= 100`; `D = nS + kappa + T` and `T`
  is untouched by anything here (it is the *chain* half, Sec 3.4). CH1 bounds `n` and
  `kappa` but not `T`. So the crossing still needs `OPEN[SAT-MASS]`, exactly as NVM
  says. Nothing in this lane closes an `N`.
* **`(B2)` at `5 <= N <= 16`:** unchanged. The death route needs an *upper* bound
  `delta_aff <= 3` (resp. `<= 1`); CH1 gives `delta_aff <= p_a((2N-2)/(W-S))`, three
  orders of magnitude too weak, and MFS's forced `dB2 >= 6` is a lower bound pointing
  the other way. Priced, not killed.
* **`(B3)` at `4 <= N <= 8`:** CH1 is exactly the missing finiteness input (DG Sec
  6.2, CD Sec 5): the `(B3)` list terminates at every `N`, with `k <= delta_aff -
  delta_c <= p_a(n_max) - delta_c`. This is the deliverable the charge names, and it
  is delivered **conditionally on `Psi = 0`**.

### 6.3 What a proof must look like

```text
   NOT intersection-theoretic on the resolution (NO-CEILING: every constraint there is
       Z.(effective) >= 0, and Psi is a free non-negative integer in that system);
   NOT the unit-speed datum on a fibre (UNIT-SPEED);
   NOT the profile (N,a,W,S,mu_l,s_l,K_P) alone (PROFILE-WITNESS at N = 4);
   NOT Keller via NOETHER-K / R_aff = 0 alone (Sec 5.5);
   NOT any property shared by C_0 x A^1 (Sec 5.4).
   LEFT, and it is one statement: the polar subtree T_+ of a noninvertible Keller map
   does not branch (much) -- a question about the boundary cluster at infinity, the
   object B3-BOUNDARY-INSTRUMENT already reads with Domrina-Orevkov.
```

## 7. Opens raised, with bounded quantities

```text
OPEN[FORK-MASS]  (new; replaces the bounded quantity of OPEN[ANTICANON-DEFECT]).
   For a noninvertible Keller map under H2, is the fork excess  Psi - Lambda  bounded
   above by a function of N?  BOUNDED QUANTITY: the integer Psi - Lambda = Z.K_X +
   kappa = 2 g_L - 2 - N + kappa, with Lambda >= 2, 1 <= kappa <= N, Psi >= 0.
   Any bound Psi - Lambda <= f(N) gives n(W-S) <= 2N + f(N) and delta_aff finite at
   every N.  SCOPE: FALSE for general dominant maps (family (B), Sec 5.2, reaches
   Psi - Lambda = (m-1)(k+1) - 2m -> infinity at fixed N).
OPEN[POLAR-CHAIN]  (new, the sharp form).  Is T_+ = Phi^{-1}(L_infty) a CHAIN for a
   noninvertible Keller map?  BOUNDED QUANTITY: the number of vertices of T_+ of
   valency >= 3, an integer in [0, #L~ - 2].  YES ⟹ CH1 (Sec 6.1).  First test case:
   MI's N = 4 (B3) data forces Lambda - Psi = 4, and forces Psi >= 3 if E_0 is a leaf
   of T_+; so at N = 4 the question is decidable from the boundary cluster alone.
OPEN[SING-WITNESS]  (new, hygiene).  Is there a fixed-N family with g_L -> infinity
   whose A_F is SINGULAR (i.e. matching (B2)/(B3), not only Sec 5.3's smooth A_F)?
   BOUNDED QUANTITY: the pair (n, delta_aff) of the witness at each k.
   A NO would be the first sign that the singularity requirement carries the ceiling.
```

Carried, with their bounded quantities unchanged: `OPEN[DELTA-AFF-VS-N]`,
`OPEN[SAT-MASS]`, `OPEN[MIN-EMBED-DEGREE]`, `OPEN[MULT-VS-BETA]` (conditionally
answered "beta >= 2" under CH2, Sec 6.1). `OPEN[MF-DEFECT]` is **restated, not
answered**: by ESCAPE-KAPPA it is exactly "`kappa = 1 ⟹ g_L >= 1`", equivalently
"`Lambda - Psi = N + 1` with a single degree-1 dominating component is impossible".

## 8. FALLACY-v2 audit

* **Flag/place/series.** Seven degree-like integers are kept apart and never
  substituted: `n`, `n_min`, `D`, `D_min`, `N`, `theta_inf`/`theta_L`, `kappa`;
  `theta_inf = kappa` is *proved* (three ways), not assumed. `g_L` is never identified
  with `g(E)` or with a witness genus; `Lambda` (leaf mass) is never confused with
  NVM's `Lam = sum s_l n_{c(l)}` — the collision is flagged in Sec 5.2.
* **Per-ray/exit-set charge.** No exit price asserted; no `charge_basis` line. In
  FORK-GENUS each edge of `T_+` is charged to its two endpoints exactly once
  (`sum_C deg C = 2(v-1)`) and each `c_C` once; the double sum is expanded with the
  `m_{C'} = 0` neighbours contributing zero, which is where an over-count would hide.
* **Carrier/attainment.** `Phi` is consumed as a floor and as a minimum over
  configurations; CH1/CH2 carry their hypotheses in the statement. No cell is claimed
  nonempty, no Keller realisation is claimed, and the Sec 5 witnesses are explicitly
  **not** Keller with their scope gaps itemised.
* **Floor/attainment.** MF-EXACT, GENUS-DEFECT, ESCAPE-KAPPA, FORK-GENUS,
  POLAR-DEGREE and ATYPICAL-LEDGER are **identities**; the only inequalities used are
  `Lambda >= 2`, `Psi >= 0`, `kappa in [1,N]`, `T >= 0`, Ha-Le `lambda_c >= 0`, and
  SHARP-CHAU. Each is cited where used.
* **Pole/interior.** The chart at infinity enters only through `div(dv)` (Sec 2.2),
  where the vertex class is checked branch by branch: zeros at the non-proper places,
  poles over `infty`. That check is exactly what catches the charge's sign error.
* **Variable/ring map.** Every CAS call declares its ring (`0,(x,y),dp`) and its
  substitution (`w = Q`, `Y = y^2`, `z^2 = Delta(w)`); genericity of `(alpha,beta,t)`
  is realised by `(3,5,7)`, and every closed form is checked at several independent
  points — the negative control on a bad specialisation. No primed symbol is a
  derivative; the only derivatives are `du, dv, dx^dy, Jac`.
* **`sat()` / raw remainder.** Not in play: no saturation, no quotient normal form,
  no resultant elimination whose leader could vanish. `std` is used once, to certify
  a critical ideal is the **unit ideal**, with the expected answer stated in advance.
* **Not filled by cap or analogy.** The ceiling is NOT asserted: CH1/CH2 are typed
  conditional, `OPEN[FORK-MASS]`/`OPEN[POLAR-CHAIN]` are typed OPEN with bounded
  quantities, and Sec 5.5's correction is derived twice rather than argued by
  analogy with the automorphism case (which Sec 4.3 shows is degenerate: `Z.K_X =
  -3` is forced there by Noether and is not evidence for `N >= 2`).

## 9. Typed verdict block

```text
LANE              KELLER-PENCIL-GENUS
SCOPE             Keller, noninvertible, H2, case (B).  Case (A) EMPTY, untouched;
                  A2 untouched; no Z(G)=1; no quasi-homogeneity anywhere.

PROVED HERE       (all PROVED-HERE, UNREVIEWED)
 UNIT-SPEED       unit speed on a fibre <=> "v|_{C_t} etale of degree N"; the 1-form
                  route returns MF-EXACT; div(dv) has ZEROS at the nS escaping places.
 GENUS-DEFECT     Z.K_X = 2 g_L - 2 - N   (coordinator's note CONFIRMED; the charge's
                  Z.(K_X+2Z) form is off by N).
 ESCAPE-KAPPA     theta_inf = kappa.  Hence D_F >= nS + kappa, and SHARP-CHAU is
                  DEG-SPLIT together with T >= 0.
 FORK-GENUS       2 g_L - 2 = N - kappa - Lambda + Psi ; Z.K_X = Psi - Lambda - kappa
                  (no Keller, no H2 needed).  POLAR-DEGREE: n(W-S) = 2N - Lambda + Psi.
 CHAIN-CEILING    Psi = 0 ==> g_L <= (N-1)/2, n(W-S) <= 2N-2 ; +E_0 a leaf ==> nW <= 2N-2.
 ATYPICAL-LEDGER  tau + sum (mult_P - r_P) = n - 1 ; lambda_P = (mult_P-r_P)W - K_P ;
                  Suzuki's ledger = RH for A_F (reproduces (K); weaker LOC-MULT).
 NEG-GENUS        closed-form family, N fixed, g -> infinity, Z.R_aff = N-1.
 PROFILE-WITNESS  N=4 family matching [P3],(C1),7.B',(K), cycle type 1^2.2 and the H2
                  shape of A_F, with g -> infinity.

MEASURED          61 Singular genus computations (normal.lib), 0 mismatches:
                  10 NVM-table maps vs adjunction; 15 family-(B); 28 family-(A);
                  8 submersion.  NVM's engine columns reproduced in closed form:
                  kappa 15/15, Lam 5/5, T 15/15, sum a_i 4/4, Z.K_X 10/10.
                  81-cell pricing of CH1/CH2.  Runtime < 15 min, < 1 GB.

CORRECTED         * the charge's 2g-2 = Z.(K_X+2Z) -> adjunction Z.K_X + N;
                  * NVM (PROPOSAL): "what makes them work is Z.R_aff" is
                    quantitatively refuted -- Z.R_aff = N-1 is CONSTANT in the
                    witnessing family while 2g-2 diverges;
                  * NVM Sec 3.1's qualitative "forks are not bounded" is upgraded to
                    "the forks ARE the ceiling" (FORK-GENUS).

NOT CLAIMED       any unconditional ceiling on g_L, n, delta_aff or D; any kill at any
                  N; any cell EMPTY (CH2's 9 kills are conditional on Psi = 0 and E_0
                  a leaf, neither proved); any Keller realisation; that Psi = 0 holds;
                  anything about case (A), A2, Z(G), MOH-CROSS or the reducible branch.

OPENS RAISED      OPEN[FORK-MASS], OPEN[POLAR-CHAIN], OPEN[SING-WITNESS] (Sec 7).

SUCCESSOR         (1) OPEN[POLAR-CHAIN] at N = 4 is decidable from the boundary
                      cluster already in the B3-BOUNDARY-INSTRUMENT lane's hands:
                      Lambda - Psi = 4, and Psi >= 3 if E_0 is a leaf of T_+.
                      That is a finite, checkable question on a single tree.
                  (2) OPEN[SING-WITNESS]: build (or fail to build) a divergent
                      fixed-N family with singular A_F.  A failure localises the
                      mechanism in the singularity requirement.
                  (3) The gate is unchanged in name (OPEN[DELTA-AFF-VS-N]) but its
                      bounded quantity is now an integer attached to a TREE, not to
                      a linear system: Psi - Lambda.

DEVIATIONS        (1) Charged item (4) cannot be executed with Keller maps (it would
                      refute JC(2)); it is executed as a relaxation ladder, Sec 5.4.
                  (2) Charged item (3)'s inequality does not exist: the vanishing
                      cycle count is an identity (Sec 4.3).  Reported as found.
                  (3) The mechanism found is NOT the symplectic datum the charge
                      pointed at; it is the boundary route of item (2).  Item (1) is
                      reported as the wash the charge suspected, with the exact
                      reason (UNIT-SPEED).
                  (4) Drivers in /tmp/kpg, not installed in box/.  genus5.sing (an
                      a>0, mu=1 probe) hit the 10-min cap; genus6.sing supersedes it.
                  (5) SIZE: the body is ~42.7KB against the charged 25-40KB band.
                      The overrun is in Sec 3 (the FORK-GENUS derivation) and Sec 5
                      (the two closed-form witness families with their proofs); I
                      kept those complete rather than compress the proofs.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `43178`.
- Body SHA-256:
  `5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1`.
- Frozen basis: `c513bcef9863771057803c0e45f9f42e4154f3ef`.
- Drivers (`/tmp/kpg`, not installed in `box/`):
  `1216727e…genus.sing`, `f2732dbe…genus2.sing`, `3b6c05c6…genus3.sing`,
  `f02742e8…genus4.sing`, `2a463ab7…genus5.sing`, `3ca38689…genus6.sing`,
  `0f32d232…price.py`.
