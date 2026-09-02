# TIME-FUNCTION ENDGAME — the interpolation conditions at the bottom disc are a one-variable Keller equation; the star is ABC-extremal, rigid at the selected `D = 105` skeleton, and the first two orders beyond Moh's leading order CONSTRAIN but do not KILL

**Lane.** `TIME-FUNCTION-ENDGAME` (flagship). **Producer.** Opus 5, 2026-09-02.
**Basis.** `8743131113dbea1a599766dc625992f4f77270da`. **Scope.** Keller, noninvertible,
degree-minimal, Moh's gauge (GEN, NU-TWO). No case (A), no A2, no `Z(G) = 1`, no
`jc2-lean`, no canonical-ledger edit. `FALLACY-v2` in force. No `charge_basis` (no new
exit-price assertion is made).

---

## 0. Custody, method, scope

Seven frozen inputs hashed **before any was opened**; all seven match the charge:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  d1-subtree-review-grok46-20260902.md
ad1bf4467319f98a29e50de16915ced5f5c4177f7ffe28657332aba00ad18245  ideation-20260902T1608Z-synthesis.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  moh_skeleton_N.py
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
574f2f4498be8aef0457d17bbe6da4e3d80719f0fcd0f87c470d5864e0406eea  jacfibre.py
```

Read firsthand in addition: `box/depth-drivers-20260902/moh.txt` (the `pdftotext -layout`
extraction of Moh, *J. reine angew. Math.* **340** (1983) 140–212), pages 176–192 —
Lemma 5.1, Lemma 5.2, **Definition 5.1**, Prop. 5.3, Lemma 5.3, **Prop. 5.5 and its
proof (p. 187–188)**, Prop. 5.6, Prop. 6.1. Journal page `P` is PDF page `P − 139`.

**Consumed as promoted** (integration #17 §A): JAC-FIBRE, FRONTIER-EXACT, D1-PIN,
D1-STAR, RADIUS-ORDER = Moh Lemma 5.2, the integrality filter, `N ≥ 6` from the
frontier line. **Not consumed:** PIN-NOT-CEILING's ceiling reading, (UNI) beyond one
orbit, PLACE-LEDGER identification.

**New drivers**, all in `box/tfe-drivers-20260902/` (python 3.14.7 / sympy 1.14.0 /
mpmath 1.3.0 over `Q`; every number below is exact unless marked *numerical*):

```text
69ff5bde bottomode.py   c698da00 control1.py   71219169 control2.py   5c04bec2 control3.py
f2ea1b38 control4.py    527cd7fc deltadenom.py ef18f0e6 devcensus.py  2edff6d2 localkeller.py
42f125a6 order2.py      43904846 orders.py     f2411498 pick105.py    a10ff4fc star.py
c5e79c93 starcheck.py   39e742b3 starexist.py  9b19d5cb starnum.py    8c900f84 timefun.py
```

Wall time for everything reported: **< 20 min**, peak memory well under 1 GB. Six
notations kept apart throughout: the campaign's geometric degree `N`; Moh's
`n = deg_y g = D`; `m = deg_y f`; `K = gcd(m,n)`; the exponents `d, e` of
`l(f) = α H^d`, `l(g) = β H^e`; Moh's gcd chain `d_i`.

---

## 1. Verdict, up front

The charge's programme goes through, and it lands on a **one-variable Keller equation**.

1. **THEOREM BOTTOM-ODE (PROVED-HERE).** Conditions (i)–(ii) of the charge, restricted
   to one bottom-major disc and read at Moh's leading order, are *exactly* the ordinary
   differential equation
   ```text
        d · p_f · p_g'  −  e · p_g · p_f'  =  κ  ∈  C^* ,     κ = c·d·e/q ,
   ```
   `deg p_g = a_1 = eV_2`, `deg p_f = b_1 = dV_2`, `c = [f,g]`, `q = (1−δ_1)de/(d+e)`.
   The order-matching that makes the right-hand side a *constant* is precisely D1-PIN
   (`λ_f(δ_1) + λ_g(δ_1) = δ_1 − 1`); D1-PIN is thus not an accident of Moh's numerics
   but the statement that the Jacobian survives to the bottom of the tower.
2. **Three corollaries, all uniform in the skeleton (PROVED-HERE).**
   *STAR-SIMPLE*: `p_f` and `p_g` are squarefree and coprime — a two-line proof of
   D1-STAR(d) **plus its `f`-analogue, which is new**: the `b_1` roots of `f` in `D_1`
   also separate pairwise at exactly `δ_1`.
   *STAR-RESIDUE*: `p_f(c_i)·p_g'(c_i) = κ/d`, the **same** nonzero constant at every one
   of the `a_1` star points.
   *STAR-SUM*: `Σ_i c_i^k / p_g'(c_i)^2 = 0` for `k = 0, …, (e−d)V_2 − 2`, and
   `= (d/κ)(lc p_f / lc p_g)` at `k = a_1 − b_1 − 1`. This **is** the "residue identity
   summing over the star that forces a sum of reciprocals to vanish" the charge
   conjectured — it exists, it is exact, and it is `(e−d)V_2 − 1` conditions.
3. **THEOREM STAR-ABC (PROVED-HERE).** BOTTOM-ODE is *equivalent* to
   `p_f^e − ρ·p_g^d` attaining the Mason–Stothers/ABC bound with equality:
   `deg(p_f^e − ρ p_g^d) = V_2(de − d − e) + 1` with all three factors squarefree.
   Equivalently `R = p_f^e/p_g^d : P^1 → P^1` is a degree-`deV_2` map branched over
   exactly three points with profiles `[e^{dV_2}]`, `[d^{eV_2}]`,
   `[(d+e)V_2 − 1, 1^{…}]`. **The bottom star of a Keller pair is a Davenport–Stothers
   extremal pair, i.e. a dessin d'enfant.**
4. **The uniform question, answered honestly: NO SKELETON KILL.** Decided by
   Gröbner/Nullstellensatz over `Q`, saturated at `κ ≠ 0`: every `(d,e,V_2)` tested is
   **REALISABLE**. The star conditions are exact, rigid, and *satisfiable*; they do not
   empty a single cell of the census. Candidate search condition (16) is therefore
   **not** an emptiness condition — it is a *rigidity* condition, which is what the next
   order needs.
5. **Part (2) verdict at the selected `D = 105` skeleton: (b), positive-dimensional,
   with the dimension computed.** Order 0 is *determined* (the star is rigid: a unique
   orbit, `p_g ∝ π(π²+b)`, star `{0, ±s}`). Orders 1 and 2 are governed by a linear
   operator `L_ε` whose rank drops **exactly** at `ε ∈ μZ_{>0}`, `μ = −λ_g/a_1 = 1/20`.
   At non-resonant orders: 7 unknowns, 5 conditions, **cokernel 0** — free. At each of
   the three resonant orders: kernel 3, **cokernel 1** — one scalar condition, which
   cuts the order-1 free plane from dimension 2 to a **union of two lines**. Non-empty:
   the skeleton survives orders 1 and 2. This is the first exact-form Appendix-II
   *constraint*; it is not a kill.
6. **Controls (part 4): 78 checks, 0 failures.** `(y, x+y^k)` and the charged
   `(y+x², x+(y+x²)²)` satisfy (i)–(ii) exactly with `a_i = 0` and no log; the non-Keller
   family `(y, x^j+y^k)`, `j ≥ 2`, satisfies (i) but **fails (ii)**, with the obstruction
   identified in closed form (the time function becomes a genuine hypergeometric); all
   seven of NOTT's two-tower rows fail both the order-matching and BOTTOM-ODE.

One correction to the record and two new OPENs are in §6–§7. A measured arithmetic
anomaly in Def 5.1(3) (§7, `OPEN[DELTA-DENOM]`) is flagged and **not** used.

---

## 2. Part (1) — the smallest surviving `D = 105` skeleton, and the exact local set-up

### 2.1 The census at `D = 105` and the selection

`pick105.py` re-runs the charged census (`census` from `moh_skeleton_N.py`,
`windows_ok` = Def 5.1(2)) and applies D1-SUBTREE's (UNI) integrality filter
`N = k·V_2·q ∈ Z`, `k·V_2 ≤ u`, at the frontier floor `N ≥ 6`:

```text
D = 105 : 5037 admissible V-skeletons; 63 admit an integer N >= 6 under (UNI)
          of those, 49 admit N in [6,16]
```

**"Smallest" is declared, not inferred.** The order used is
`(s, min achievable N, e, m, M-vector lex, V-vector lex)`. All 63 survivors have the
minimum depth `s = 3` (Moh Prop. 5.5); the winner attains the minimum `N = 6`, and it
attains the absolute minima `a_1 = eV_2 = 3` and `b_1 = dV_2 = 2` of the two integers
that control the whole bottom computation (`e ≥ 3`, `d ≥ 2`, `V_2 ≥ 1`). Ten of the 63
share `(d,e,V_2) = (2,3,1)`; **§3–§4 apply verbatim to all ten**, because the bottom-disc
problem depends on the skeleton only through `(d,e,V_2)` and `δ_1`.

```text
== SELECTED SKELETON ==
  n = D = 105 ,  m = 70 ,  K = gcd(m,n) = 35 ,  (d,e) = (2,3) ,  s = 3
  M_1 = -m = -70 ;  M_2 = -63 ;  M_3 = n-2 = 103
  d_1..d_4 = 105, 35, 7, 1                      (d_{i+1} = gcd(n, M_1..M_i))
  V_2, V_3, V_4 = 1, 4, 1                       (Def 5.1(2) windows: 5/24 < 1 <= 20 ;
                                                                     7/2  < 4 <= 7)
  delta_1, delta_2, delta_3 = 3/4, 71/95, -1
  a_1, a_2, a_3 (g-roots in D_i) = 3, 60, 105
  b_1, b_2, b_3 (f-roots in D_i) = 2, 40,  70
  lambda_g(delta_i) = -3/20, -3/19, -105
  lambda_f(delta_i) = -1/10, -2/19,  -70
  u = V_3 K/d_3 = 20 ,  v = K - u = 15 ,  q = (1-delta_1)de/(d+e) = 3/10
  N = sum_B V_2(B) q(B) = 20 * 1 * 3/10 = 6     (k = 20 bottom-major discs, sum V_2 = u)
```

Sanity, all re-derived here, not imported: `b_i/a_i = m/n = 2/3`; `a_2 = u·e = 60`;
`λ_g(δ_r) = −n(1−δ_r)/(n−M_r)` (Lemma 5.2) at `r = 1` gives `−105·(1/4)/175 = −3/20`;
`λ_f = (m/n)λ_g`; and **`λ_f(δ_1) + λ_g(δ_1) = −1/4 = δ_1 − 1`** — the identity that §3
shows is the whole content of D1-PIN.

### 2.2 The Puiseux roots down the tower, with the tame coefficients named

Write `t = x^{-1}`, `ord = ord_t`, `ord x = −1`. Moh's Def 5.1(4) gives the general point
of `D_i` as `σ_i = Σ_j w_j t^{a_j} + π t^{δ_i}`. Along the distinguished path:

```text
  radius            what separates there (slope of λ_g)          free (tame) data
  -----------------------------------------------------------------------------------
  δ_3 = -1          the 45 = ve roots on the other linear factor  the two roots of l(g)
  (-1, 71/95)       nothing (slope a_2 = 60)                      the shared head w(t)
  δ_2 = 71/95       57 of the 60 leave; D_2 splits into 20 × 3    the t^{δ_2} coefficients
  (71/95, 3/4)      nothing (slope a_1 = 3)                       the shared head w(t)
  δ_1 = 3/4         the 3 g-roots AND the 2 f-roots of D_1        c_{i,0}, e_{j,0} = the STAR
                    separate PAIRWISE (D1-STAR + §3.3)
  below δ_1         each root goes its own way                    c_{i,ν}, e_{j,ν}, ν ≥ 1
```

So for one bottom-major disc `B` (there are `k = 20` of them, and
`Σ_B V_2(B) = 20 = u`) the data is

```text
   3 roots of g :  ρ_i(t) = w(t) + Σ_{ν≥0} c_{i,ν} t^{δ_1 + ν η},   i = 1,2,3
   2 roots of f :  φ_j(t) = w(t) + Σ_{ν≥0} e_{j,ν} t^{δ_1 + ν η},   j = 1,2
   57 roots of g outside D_1 but inside D_2 :  ord(σ_1 − ρ) = δ_2, contributing a
        unit factor (w−ρ) = t^{δ_2}·W_ρ(t), W_ρ(0) ≠ 0, whose π-linear term enters at
        t^{δ_1−δ_2} = t^{1/380} ;
   45 roots of g outside D_2 :  ord = −1, entering at t^{δ_1+1} = t^{7/4} ;
   38 roots of f outside D_1 but inside D_2, 30 outside D_2 : likewise
```

`η` is the step of the exponent lattice; the tame coefficients `c_{i,ν}, e_{j,ν}` for
`ν ≥ 1`, together with the tails of the `W_ρ`, are **exactly** the free data Moh's
recursion leaves untouched, and they are the unknowns of part (2).

The substitution `σ_1(π) = w(t) + π t^{δ_1}` gives, once and for all,

```text
   Γ(t,π) := t^{-λ_g} g(σ_1)  =  Π_{i≤a_1} (π − C_i(t)) · Π_{out} W_ρ(0)
                                 · Π_{out} (W_ρ(t)/W_ρ(0)) · Π_{out}(1 + π t^{δ_1−e_ρ}/W_ρ(t))
   Φ(t,π) := t^{-λ_f} f(σ_1)  =  the same with the f-roots,
```
`C_i(t) = c_{i,0} + c_{i,1}t^{η} + …`. Both are polynomials in `π` with coefficients in
`C[[t^{η}]]`, `Γ_0(π) = A_g Π_i(π − c_{i,0}) =: p_g`, `Φ_0(π) = A_f Π_j(π − e_{j,0}) =: p_f`,
`deg p_g = a_1 = 3`, `deg p_f = b_1 = 2`.

---

## 3. Part (2) — imposing (i)–(ii), order by order

### 3.1 LOCAL-KELLER: the exact form of the charge's conditions at one disc

> **LEMMA LOCAL-KELLER (PROVED-HERE).** With `x = t^{-1}` and `y = w(t) + π t^{δ}`,
> ```text
>    ∂(x,y)/∂(t,π) = det [[ −t^{-2}, 0 ], [ w' + πδ t^{δ-1}, t^{δ} ]] = −t^{δ−2},
> ```
> so `[f,g]_{x,y} = c` transports to `F_t G_π − F_π G_t = −c·t^{δ−2}`, i.e. with
> `F = t^{λ_f}Φ`, `G = t^{λ_g}Γ` and `λ_f + λ_g − 1 = δ − 2`,
> ```text
>    (λ_f Φ + t Φ_t)·Γ_π  −  (λ_g Γ + t Γ_t)·Φ_π  =  −c .            (LOCAL-KELLER)
> ```

*Proof.* The determinant is immediate; the chain rule gives the transport; taking
`t`-degrees term by term gives the displayed form. ∎

The exponent identity `λ_f + λ_g = δ_1 − 1` is **forced** — it is not an extra
hypothesis. If it failed, the left side would have a leading `t`-order different from
`δ_1 − 2` and the equation would be unsatisfiable. **That identity is D1-PIN**
(`floor = ceiling` at `r = 1` is literally `(1−δ_1) + λ_g = −λ_f`). So:

> **READING.** D1-PIN says the Jacobian condition *reaches the bottom disc at all*; its
> failure at `r ≥ 2` (`floor − ceiling = (1−δ_r)(−M_r−m)/(n−M_r) < 0`) says the bracket is
> sub-leading there and imposes nothing. That is why the endgame lives at `D_1`.

Expanding `Φ = Σ_k Φ_k t^{ε_k}`, `Γ = Σ_k Γ_k t^{ε_k}` (`ε_0 = 0`, `ε_k` increasing in
the exponent lattice) gives the order-by-order system

```text
   order 0 :  λ_f Φ_0 Γ_0' − λ_g Γ_0 Φ_0'  =  −c                                  (ODE-0)
   order k :  L_{ε_k}(Φ_k, Γ_k)  =  − Σ_{i+j=k, i,j ≥ 1} [ (λ_f+ε_i) Φ_i Γ_j'
                                                          − (λ_g+ε_j) Γ_j Φ_i' ]  (ODE-k)
   L_ε(Φ,Γ) := (λ_f+ε) Φ Γ_0' − λ_g Γ_0 Φ' + λ_f Φ_0 Γ' − (λ_g+ε) Γ Φ_0' .
```

Condition (i) of the charge ("`y`-degree exactly `m`") is, locally, the degree bound
`deg_π Φ_k ≤ b_1 + #{f-roots outside D_1 activated by order ε_k}`; condition (ii)
("coefficients polynomial in `x`") is that `Φ, Γ` are honest elements of
`C[[t^{η}]][π]` — i.e. the no-log condition of JAC-FIBRE, at every order. (ODE-`k`) for
all `k` is the conjunction of both.

### 3.2 Order 0 = BOTTOM-ODE, and the constant is pinned

> **THEOREM BOTTOM-ODE (PROVED-HERE).** At every bottom-major disc of a Keller pair in
> Moh's gauge,
> ```text
>      d · p_f · p_g'  −  e · p_g · p_f'  =  κ ,      κ = −e c / λ_g(δ_1)
>                                                       = c (d+e)/(1−δ_1)  =  c d e / q ,
> ```
> with `deg p_g = a_1 = eV_2`, `deg p_f = b_1 = dV_2`, `q = (1−δ_1)de/(d+e)` the pinned
> per-`V_2`-unit contribution to `N` of D1-PIN. In particular `κ ≠ 0`.

*Proof.* (ODE-0) is `λ_f p_f p_g' − λ_g p_g p_f' = −c`. Divide by `λ_g < 0` and multiply
by `e`, using `λ_f/λ_g = m/n = d/e` (Moh Def 5.1(1) at `i = 1`, equivalently
FRONTIER-EXACT's proportionality). The evaluation of `λ_g(δ_1)` is Lemma 5.2. ∎

The top coefficient cancels automatically — `(d)(b_1)(a_1)` against `(e)(a_1)(b_1)`
after `d a_1 = d e V_2 = e b_1` — which is the *first* nontrivial consistency check and
is exactly Def 5.1(1)'s proportionality again.

**Charged control, closed form.** `(f,g) = (y, x+y^k)`: `w = 0`, `δ_1 = −1/k`,
`σ_1 = πx^{1/k}`, `g(σ_1) = x(1+π^k)`, `f(σ_1) = πx^{1/k}`; so `p_g = 1+π^k`, `p_f = π`,
`(d,e) = (1,k)`, `q = 1`, `c = −1`, and
`1·π·kπ^{k-1} − k(1+π^k)·1 = −k = c d e/q` ✓.

**At the selected skeleton** `(d,e,V_2) = (2,3,1)`, so `deg p_g = 3`, `deg p_f = 2` and
`2 p_f p_g' − 3 p_g p_f' = κ`. Solving exactly (`bottomode.py`, sympy over `Q`, with
`p_g` monic and the `π²` coefficient translated away):

```text
  equations:  π^4 : 0 (identically)   π^3 : 3q_1        π^2 : −4p_1q_2 + 6q_0
              π^1 : −6p_0q_2 − p_1q_1  π^0 : κ = −3p_0q_1 + 2p_1q_0
  solutions:  p_0 = 0 ,  q_1 = 0 ,  q_0 = (2/3) p_1 q_2 ,  κ = (4/3) p_1² q_2  (≠ 0 iff p_1 ≠ 0)
```

> **The bottom star at every one of the twenty bottom discs is RIGID.** The solution
> variety has dimension 3 in the 6 coefficients, equal to the dimension of the group
> `π → απ+β`, `p_f → ν p_f`, so it is a **single orbit**:
> ```text
>      p_g = π(π² + b) ,   p_f ∝ π² + 2b/3 ,   b ≠ 0 ,
>      the star = { 0, +s, −s } with s² = −b, and the two f-points at ± sqrt(2/3)·s .
> ```
> Normalised (`b = −1`): `p_g = π³ − π`, `p_f = π² − 2/3`, `λ_fΦ_0Γ_0' − λ_gΓ_0Φ_0' = −1/15`,
> so `c = 1/15` and `κ = cde/q = (1/15)(6)/(3/10) = 4/3`, verified directly.

So **part (2)'s order 0 is case (c): determined**, and we go one order deeper.

### 3.3 Two corollaries that are new, and one that is not

> **COROLLARY STAR-SIMPLE (PROVED-HERE).** `p_g` and `p_f` are **both squarefree**, and
> `gcd(p_f, p_g) = 1`.

*Proof.* If `p_g(z) = p_g'(z) = 0` then `κ = d p_f(z)p_g'(z) − e p_g(z)p_f'(z) = 0`,
contradiction; symmetrically for `p_f`; and a common root of `p_f, p_g` also gives
`κ = 0`. ∎

`p_g` squarefree is D1-STAR(d) (promoted at #17 §A.4) — this is a two-line independent
proof of it. `p_f` squarefree is **new** and sharpens D1-STAR(b): the report's
"intra-`f` clustering below `δ_1` is free" is correct as stated (it is invisible to `N`),
but the Jacobian condition nevertheless forbids two `f`-roots of `D_1` from sharing
their `t^{δ_1}` coefficient. Recorded in §6 as a strengthening, not a correction.

> **COROLLARY STAR-RESIDUE (PROVED-HERE).** For every star point `c_i` (root of `p_g`),
> ```text
>      p_f(c_i) · p_g'(c_i)  =  κ/d  =  c e /(1−δ_1) ,  the SAME constant at all a_1 points.
> ```

*Proof.* Evaluate BOTTOM-ODE at `c_i`. ∎

### 3.4 Orders 1 and 2: the resonance structure, computed

`L_ε` is linear. Its top coefficient, for `deg Φ = β`, `deg Γ = α`, is
`[(λ_f+ε)a_1 − λ_g β]·lc(Φ)` when `β + a_1 > α + b_1` and
`[λ_f α − (λ_g+ε) b_1]·lc(Γ)` when `α + b_1 > β + a_1`. Since
`λ_g/a_1 = λ_f/b_1 = −μ` (this is again Def 5.1(1)'s proportionality), both vanish
exactly at

```text
      ε = μ (b_1 − β)      resp.     ε = μ (a_1 − α) ,      μ := −λ_g/a_1 = −λ_f/b_1 .
```

For the selected skeleton `μ = (3/20)/3 = 1/20`, and `μ = c_ρ/b_1` where
`c_ρ = m(1−δ_1)/(n+m) = 1/10` is D1-PIN's per-root contribution to `N`.

`orders.py` computes the rank of `L_ε` exactly, with `deg Φ_k ≤ b_1`, `deg Γ_k ≤ a_1`
(the "inner tame coefficients plus the outer scalar" bound of §2.2 — `a_1+1` and
`b_1+1` parameters respectively, which is the full space of those degrees):

```text
  gcd of the maximal minors of L_ε  =  ε (10ε − 1)(20ε − 3)(20ε − 1)/4000
  roots  ε ∈ { 0, 1/20, 1/10, 3/20 }  =  μ·{0, 1, 2, 3}  =  μ·{0, …, a_1}
  (4μ = 1/5 is NOT a root — the list stops at a_1, as the degree analysis predicts)

  ε generic      : unknowns 7, conditions 5, rank 5, kernel 2, COKERNEL 0
  ε ∈ μ{1,2,3}   : unknowns 7, conditions 5, rank 4, kernel 3, COKERNEL 1
```

The three resonances are the three *trivial* symmetries of the pair, appearing exactly
where they must: `ε = 2μ = −λ_f` is `f → f + const` (the charge's `a_i`), `ε = 3μ = −λ_g`
is `g → g + const`, and `ε = μ = λ_f − λ_g` is `g → g + const·f` (available because
`m < n`). Their appearance as the rank drops of `L_ε` is a check on the whole set-up.

A full grid over `(deg Φ_k, deg Γ_k) ∈ [0,4]²` at generic `ε` is in `orders.log`. The
only cokernels there occur at `deg Γ_k = 0`; as soon as `Γ_k` may have degree `≥ 1`,
`L_ε` is surjective. So the *degree* half of condition (i) does not obstruct.

**Order 1** (`order2.py`). The source is zero, so the order-1 data is `ker L_{ε_1}`.
Taking `ε_1 = δ_1 − δ_2 = 1/380` (the first exponent actually present in the lattice —
the `t^{δ_1−δ_2}` term of the 57 outer factors):

```text
   kernel dim 2 :  Φ_1 = (2/3)s_1 π² + (2/3)s_0 π + (76/675)s_1
                   Γ_1 = s_1 π³ + s_0 π² − (37/225)s_1 π − (1/3)s_0
```

**Order 2.** With that generic order-1 element, `order2.py` builds the quadratic source
and solves (ODE-2):

```text
   ε_2 generic (2/7)     : rank 5, kernel 2, cokernel 0     CONSISTENT, unobstructed
   ε_2 = μ   = 1/20      : rank 4, kernel 3, cokernel 1     ONE condition:  s_0 s_1 = 0
   ε_2 = 2μ  = 1/10      : rank 4, kernel 3, cokernel 1     ONE condition:  225 s_0² + 376 s_1² = 0
   ε_2 = 3μ  = 3/20      : rank 4, kernel 3, cokernel 1     ONE condition:  s_0 s_1 = 0
```

Both `μ` and `2μ` **are** in the exponent lattice (`1/20 = 19·(1/380)`,
`1/10 = 38·(1/380)`), so the resonant orders are genuinely reached.

> **VERDICT for part (2): case (b) — consistent, with a positive-dimensional solution
> set, and the dimension computed.**
> * Order 0 is *determined* (a single group orbit): §3.2.
> * Each non-resonant order contributes `(a_1+1)+(b_1+1) − (a_1+b_1) = 2` free parameters
>   and **no** condition.
> * Each resonant order `ε ∈ μ{1,2,3}` contributes 3 free parameters and **exactly one**
>   scalar condition on the accumulated lower-order data. At the first resonant order the
>   condition is a nonzero quadratic form on the order-1 plane: it cuts that plane from
>   dimension 2 to a **union of two lines** — non-empty.
> * **The skeleton does not die at orders 1 or 2.** The next order to impose is the next
>   resonant one, `ε ∈ μZ_{>0}` present in the lattice; on the present accounting there
>   are `19` non-resonant orders (`2` free parameters each) below `ε = μ` against `1`
>   condition at `ε = μ`, so no counting obstruction can appear at the bottom disc alone.

**Where a kill could still come from, stated precisely.** The `2` free parameters per
order are *local* to one disc: they are the inner tame coefficients `c_{i,ν}, e_{j,ν}`
of that disc **plus** the order-`ν` coefficients of the outer scalars
`Π_{out}W_ρ(t)/W_ρ(0)`. The outer scalars are **shared** by all `k = 20` bottom discs.
The local computation cannot see that coupling; a global count over the 20 discs is the
first place a counting obstruction can arise. That is `OPEN[DISC-COUPLING]` (§7).

---

## 4. Part (3) — the uniform question, and what it does and does not kill

### 4.1 The uniform conditions, in the form the charge asked for

Fix a bottom-major disc; `a_1 = eV_2`, `b_1 = dV_2`, `d < e`, `gcd(d,e) = 1`.
Because `deg p_f = b_1 < a_1 = deg p_g`, `p_f` **is** the Lagrange interpolant of its own
values at the star, and STAR-RESIDUE says those values are `(κ/d)/p_g'(c_i)`. Expanding
`p_f/p_g` at `π = ∞`,

```text
   p_f(π)/p_g(π)  =  Σ_{k ≥ 0} π^{−k−1} · (κ/d) · S_k ,     S_k := Σ_i c_i^k / p_g'(c_i)² ,
```
and `deg p_f = b_1` forces the first `a_1 − b_1 − 1` of these to vanish:

> **THEOREM STAR-SUM (PROVED-HERE).**
> ```text
>    Σ_i  c_i^k / p_g'(c_i)²  =  0        for k = 0, 1, …, (e−d)V_2 − 2 ,
>    Σ_i  c_i^{a_1−b_1−1} / p_g'(c_i)²  =  (d/κ)·( lc p_f / lc p_g )  ≠  0 .
> ```
> In particular, whenever `(e−d)V_2 ≥ 2`, **`Σ_i 1/p_g'(c_i)² = 0`**: the sum over the
> star of the squared reciprocals of the separations vanishes.

This is exactly the shape conjectured in the charge, and it is `(e−d)V_2 − 1` conditions,
so it **does** grow with `V_2`. Verified exactly on six stars (`starcheck.py`, symmetric
sums computed as traces in `Q[π]/(p_g)` — no radicals, no root isolation):

```text
(d,e,V)   a_1 b_1  κ      κ/d     #STAR-SUM  values          A(p_g),A(p_f)  k=a_1−b_1−1
(2,3,1)   3   2    3      3/2      0         []              2,2 case 1     2/3
(2,5,1)   5   2    15/4   15/8     2         [0, 0]          2,2 case 1     8/15
(2,7,1)   7   2    35/8   35/16    4         [0,0,0,0]       2,2 case 1     16/35
(3,4,1)   4   3   −8/9   −8/27     0         []              2,2 case 2    −27/8
(3,5,1)   5   3    35/27  35/81    1         [0]             1,1 case 1     81/35
(4,5,1)   5   4    5/32   5/128    0         []              2,2 case 1     128/5
                                                     73 checks, 0 failures
```

(The last column is `d/κ` exactly, as the theorem predicts with `lc p_f = lc p_g = 1`.)

### 4.2 STAR-ABC: what the star really is

> **THEOREM STAR-ABC (PROVED-HERE).** Let `P, Q` be nonconstant with `deg Q = b_1 = dV_2`,
> `deg P = a_1 = eV_2`, `ρ ≠ 0`. The following are equivalent:
> ```text
>   (1)  d Q P' − e P Q'  =  κ  ∈ C^* ;
>   (2)  deg( Q^e − ρ P^d )  =  V_2(de − d − e) + 1   for some ρ ≠ 0, with P, Q and
>        C := Q^e − ρP^d pairwise coprime and squarefree ;
>   (3)  R := Q^e/P^d : P^1 → P^1 has degree deV_2 and is branched over exactly three
>        points, with profiles  [e^{dV_2}] over 0,  [d^{eV_2}] over ∞, and
>        [(d+e)V_2 − 1, 1^{V_2(de−d−e)+1}] over R(∞).
> ```
> `V_2(de−d−e)+1` is the **Mason–Stothers/ABC bound**, so (2) says the bottom star is an
> **ABC-extremal (Davenport–Stothers) pair**, and (3) says it is a **dessin d'enfant**.

*Proof.* (1) ⇒ (2): with `C = Q^e − ρP^d`, differentiating `Q^e/P^d = ρ + C/P^d` gives
`C'P − dCP' = −Q^{e−1}·(dQP'−ePQ') = −κ Q^{e−1}`. Comparing degrees, the leading
coefficient of `C'P − dCP'` is `c_γ(γ − deV_2)` with `γ = deg C`, hence
`γ + a_1 − 1 = deg Q^{e−1} = b_1(e−1)` and `γ = V_2(de−d−e)+1`; a multiple root of `C`
would force `Q = 0` there, hence `P = 0`, contradicting `gcd(P,Q) = 1` (STAR-SIMPLE).
(2) ⇒ (1): Mason–Stothers applied to `A = Q^e`, `B = −ρP^d`, `C = A+B`. The standard
proof shows `(ABC)/rad(ABC) | W(A,B) = AB'−A'B`, and here
`W(A,B) = −ρ Q^{e−1}P^{d−1}(dQP'−ePQ')` while `(ABC)/rad(ABC) = ρ Q^{e−1}P^{d−1}`
(the three radicals being `Q`, `P`, `C`); equality of degrees in the ABC bound forces
`dQP' − ePQ'` to be a constant, nonzero because `A/B` is nonconstant.
(2) ⇔ (3): `R^{-1}(0)` is the `b_1` simple roots of `Q` each with multiplicity `e`,
`R^{-1}(∞)` the `a_1` simple roots of `P` each with multiplicity `d` (total `deV_2` each,
so `π = ∞` is neither a zero nor a pole), and `R' = −eκQ^{e−1}/P^{d+1}` vanishes nowhere
else; in the local coordinate `s = 1/π` at `π = ∞`, `dR/ds ∼ s^{(d+e)V_2−2}`, so the
ramification index there is `(d+e)V_2 − 1` and the Riemann–Hurwitz count
`2deV_2 − 2 = dV_2(e−1) + eV_2(d−1) + ((d+e)V_2 − 2)` closes exactly. ∎

Two immediate uses. First, an explicit construction which is also a decision procedure:
`Q^{e/d}` is a well-defined Laurent series at `π = ∞` for `Q` monic, and (2) holds iff
`P := [Q^{e/d}]_{≥0}` with the coefficients of `π^{-1}, …, π^{-(b_1−2)}` of `Q^{e/d}` all
zero — **`b_1 − 2` equations in the `b_1 − 2` essential parameters of `Q`** (monic, modulo
translation and scaling). Second, the whole problem is now indexed by `(d,e,V_2)` alone.

### 4.3 The census test — and the honest answer

`devcensus.py` enumerates the bottom-star data actually occurring:

```text
  D in [48,120] : 902 893 admissible V-skeletons
    distinct (d,e,V_2)  over all of them                            : 220
    distinct (d,e,V_2)  over those admitting an integer N ≥ 6 (UNI) : 96
    (d,e) occurring : (2,3) (2,5) (2,7) (3,4) (3,5) (3,7) (4,5) (4,7) (5,6) (5,7) (6,7)
    V_2 occurring   : 1 … 38  ((2,3));  1 … 22  ((2,5),(3,5),(4,5));  1 … 14  (e = 7)
```

`starexist.py` **decides** existence for a given `(d,e,V_2)` by the Nullstellensatz: build
the ideal generated by the `b_1 − 2` truncation equations together with `w·κ − 1` (the
saturation that removes the spurious component `Q = R^d`, `P = R^e`, on which `κ` vanishes
identically), and compute a Gröbner basis over `Q`; `1 ∈ I` iff the variety is empty
over `C` iff every skeleton with that `(d,e,V_2)` dies.

```text
STAR EXISTENCE by Nullstellensatz (grevlex over QQ, saturated at kappa != 0)
(d,e,V)     a_1   b_1   #TRUNC   #GB    verdict       secs
(2,3,1)     3     2     0        1      REALISABLE    0.0
(2,5,1)     5     2     0        1      REALISABLE    0.0
(2,7,1)     7     2     0        1      REALISABLE    0.0
(3,4,1)     4     3     1        3      REALISABLE    0.0
(3,5,1)     5     3     1        3      REALISABLE    0.0
(3,7,1)     7     3     1        4      REALISABLE    0.1
(2,3,2)     6     4     2        3      REALISABLE    0.0
(2,5,2)    10     4     2        5      REALISABLE    0.1
(2,7,2)    14     4     2       10      REALISABLE    0.2
(4,5,1)     5     4     2        9      REALISABLE    0.0
(4,7,1)     7     4     2       15      REALISABLE    0.1
(5,6,1)     6     5     3       29      REALISABLE    0.1
(5,7,1)     7     5     3       44      REALISABLE    0.2
(2,3,3)     9     6     4        8      REALISABLE    0.2
(2,5,3)    15     6     4       48      REALISABLE    8.4
```

Explicit witnesses for the `V_2 = 1` rows (exact, `star_run.log`; the `d = 2` family is
a truncated binomial series and exists for every `e`):

```text
 (2,3,1)  p_g = π(2π²+3)/2                       p_f = π²+1
 (2,5,1)  p_g = π(8π⁴+20π²+15)/8                 p_f = π²+1
 (2,7,1)  p_g = π(16π⁶+56π⁴+70π²+35)/16          p_f = π²+1
 (3,4,1)  p_g = (9π⁴+12π²+2)/9                   p_f = π(π²+1)
 (3,5,1)  p_g = (27π⁵+45π³−15π²+15π−10)/27       p_f = (3π³+3π−1)/3
 (4,5,1)  p_g = π(16π⁴+20π²+5)/16                p_f = (8π⁴+8π²+1)/8
```

> **ANSWER to part (3), stated plainly.** A uniform condition **exists**, in three
> equivalent exact forms (STAR-RESIDUE, STAR-SUM, STAR-ABC), it is stated for *every*
> skeleton, and its number of scalar constraints **does** grow with `V_2` — but so does
> the number of star points, and by STAR-ABC the constraints are the defining equations
> of a Davenport–Stothers dessin, whose existence is exactly the Riemann-existence
> question for a genus-0 three-point cover. **On every `(d,e,V_2)` decided here the
> answer is REALISABLE, so candidate search condition (16) kills nothing by skeleton.**
> Its value is the *rigidity* it supplies: at `(d,e,V_2) = (2,3,1)` the bottom star of a
> Keller pair is a single orbit `{0, ±s}`, and in general a finite set of dessins.

**Bounded quantity of the residual.** Decided here: `b_1 = dV_2 ≤ 6`. Not decided:
`b_1 ≥ 7`. The classical Davenport–Stothers literature (Stothers 1981; Zannier 1995,
*On Davenport's bound for the degree of `f³ − g²`*) asserts existence for all
`(d,e) = (2,3)` and all `V_2`, and the general Hurwitz-existence count for the profiles
of STAR-ABC(3) is a finite character-theoretic computation in `S_{deV_2}`. Typed as
`OPEN[STAR-ALLV]` in §7 — **not** asserted here.

### 4.4 Moh's own condition, recovered at every `s`

Moh proves Prop. 5.5 (`s = 2`) by exactly this route, and his argument generalises. Let
`H ⊆ Gal(C⟨t⟩/C((t)))` be the stabiliser of the disc (`w^ζ = w`), let `χ(ζ) = ζ^{A'δ_1}`
be the character by which it acts on `π`, and put `A := |χ(H)|`. Then `p_g` and `p_f` are
`χ`-eigenvectors, so each is `π^{j}·(`polynomial in `π^A)`, and `κ ≠ 0` at `π = 0` forces:

> **THEOREM STAR-EIGEN (PROVED-HERE; Moh's Prop. 5.5 argument, at every `s`).**
> ```text
>   either   a_1 ≡ 1  and  b_1 ≡ 0   (mod A)        [ π | p_g , π ∤ p_f ]
>   or       a_1 ≡ 0  and  b_1 ≡ 1   (mod A)        [ π ∤ p_g , π | p_f, simply ]
>   in both cases      A | (d+e)V_2 − 1 ,
> ```
> which is verbatim Moh's "`A | (n*+m*)V₂ − 1`" (p. 188, `n* = e`, `m* = d`).

Verified on all six exact stars (`starcheck.log`: the `A(p_g),A(p_f)` and `case`
columns; e.g. `(2,3,1)`: `A = 2`, `a_1 = 3 ≡ 1`, `b_1 = 2 ≡ 0`, `A | 4` ✓). It is also
verified on the charged automorphism control: `(y,x+y^k)` has `p_g = 1+π^k`, `p_f = π`,
`A = k = a_1`, `b_1 = 1`, case 2, `A | a_1 + b_1 − 1 = k` ✓.

**Consequence at the selected skeleton (conditional, hypothesis stated).** The unique
`(2,3,1)` star `p_g = π³+bπ` has symmetry order exactly `2`, so `A ∈ {1,2}`. If, as the
derivation above gives, `A = denom(L·δ_1)` with `L` the order in `Q/Z` of the group
generated by the exponents of the head `w`, then `δ_1 = 3/4` forces `2 | L`: **the head
of every bottom-major disc must carry an exponent of even denominator**. That is a real
structural constraint on the tame data above `δ_1`; it is *not* a skeleton kill, and it
is typed `UNREVIEWED` because the identification `A = denom(Lδ_1)` uses a Galois
bookkeeping that this lane derived but did not test against a worked tower.

---

## 5. Part (4) — controls

All four run fail-closed; `78` checks, `0` failures.

**CONTROL 1 — `(y, x+y^k)`, `k = 2..7` (`control1.py`, 24 checks).** `J = −1`; the
`n = k` roots are `τ_i = ζ^i(c_2−x)^{1/k}`; `g_y(τ_i) = kτ_i^{k−1}`; the exponent of
`J/g_y(τ_i)` is `(1−k)/k − j`, never `−1` for `k ≥ 2`, so **no log**;
`∫ J dx/g_y(τ_i) = τ_i` exactly, so `a_i = 0` and the time function reproduces
`f(x,τ_i)`; the Lagrange interpolant of the values `τ_i` at the nodes `τ_i` is `y`, of
`y`-degree `1 = m < n = k`, with polynomial coefficients. **(i) and (ii) hold exactly.**

**CONTROL 2 — the charged `(y+x², x+(y+x²)²)` (`control2.py`, 21 checks).** After the
shear gauge `x → x+y`:

```text
   f = x² + 2xy + y² + y                    m = deg_y f = deg f = 2, monic
   g = x⁴+4x³y+6x²y²+2x²y+4xy³+4xy²+x+y⁴+2y³+y²+y     n = 4, monic, J = [f,g] = −1
```

The inverse map gives the fibre `{g = c₂}` a polynomial parametrisation by `u = f`:
`x = X(u) = u⁴ − (13/3)u² − u + 40/9`, `y = Y(u) = −u⁴ + (10/3)u² + u − 25/9` at
`c₂ = 5/3`, `deg_u X = 4 = n`. The key identity is verified exactly:

```text
       g_y |fibre  =  −4u³ + (26/3)u + 1  =  J · dX/du            (this IS df/dx = J/g_y)
   ⇒   ∫ J dx / g_y  =  ∫ J X'(u) du / (J X'(u))  =  u  =  f ,    no log, a_i = 0, exactly.
```

Independently, as Puiseux series (`x = z^{-4}`, the four branches `z → i^k z`, expansions
carried to `z^6`): each branch lies on `{g = c₂}`; the residue (the `z^{-1}` coefficient)
of the 1-form `J dx/g_y` is **`0` on all four branches**; and term-by-term integration
returns `f(x,τ_k)` up to a constant on all four. Finally
`disc_y(g − c₂) = −(6912x³ − 27264x² − 31776x + 64901)/27 ≠ 0`, so the four nodes are
distinct and the interpolant of degree `< n` through the `n` values is unique: it is `f`,
of `y`-degree exactly `m = 2 < 4 = n`, with polynomial coefficients. **(i) and (ii) hold.**

**CONTROL 3 (NEGATIVE) — `f = y`, `g = x^j + y^k`, `j ≥ 2` (`control3.py`, 12 checks).**
`J = −j x^{j−1}`, Keller iff `j = 1`. Here the *interpolation* conditions separate the
Keller locus sharply. Since `1/g_y(τ_i) = ζ^i/(k(c₂−x^j)^{(k−1)/k})`, the interpolant is

```text
     L(y) = (H/T)·y ,     T = (c₂−x^j)^{1/k},   H = (c/k)∫ (c₂−x^j)^{(1−k)/k} dx ,
```
so **(i) always holds** (`y`-degree `1 = m < k = n`) and **(ii) holds iff `H/T` is a
polynomial**, iff there is a polynomial `p` with `p'(c₂−x^j) − (j/k)x^{j−1}p = 1`. The
degree of the left side is `deg p + j − 1`, so a solution exists **only for `j = 1`**.
Measured on all twelve rows `j = 1..3`, `k = 2..5`: (ii) holds exactly on the Keller
rows and fails on every non-Keller row, where `H/T` is a genuine `₂F₁` (printed in
`control3.log`). The obstruction is quantitative: it grows like `j − 1`.

**CONTROL 4 (NEGATIVE) — NOTT's seven two-tower rows (`control4.py`, 21 checks).** These
are the charged non-Keller rows; all roots are explicit, so the tree is exact. At the
deepest disc of the `g`-tree:

```text
 row  m  n  J const  δ_1     λ_f+λ_g   δ_1−1   (ORD)  a_1 b_1  deg W
  0   2  3  False    −1/2    −3        −3/2    FAIL    2   1     2
  1   3  4  False    −1/2    −9/2      −3/2    FAIL    2   2     3
  2   4  4  False    −2/3    −17/3     −5/3    FAIL    3   2     4
  3   3  4  False    −1/2    −5        −3/2    FAIL    2   1     2
  4   4  4  False    −1/3    −14/3     −4/3    FAIL    3   0     2
  5   4  6  False    −1/2    −13/2     −3/2    FAIL    4   2     5
  6   4  6  False    −1/3    −20/3     −4/3    FAIL    3   0     2
```

Both necessary conditions fail on every row: the order-matching
`λ_f(δ_1)+λ_g(δ_1) = δ_1−1` (so LOCAL-KELLER cannot even be *posed* with a constant right
side), and the bottom bracket `λ_f p_f p_g' − λ_g p_g p_f'`, which is a polynomial of
degree `2..5` in `π` rather than a nonzero constant. **Polynomiality fails, as charged.**

---

## 6. Corrections and strengthenings to the record

1. **STRENGTHENING of D1-STAR (b).** #17 §A.4 records "intra-`f` clustering below `δ_1` is
   free (it does not enter `N`)". That is correct *as a statement about `N`*, and this
   lane does not contradict it. But by STAR-SIMPLE the Jacobian condition forces `p_f` to
   be squarefree, i.e. the `b_1 = dV_2` roots of `f` in a bottom disc also separate
   **pairwise at exactly `δ_1`**. The correct statement is: intra-`f` clustering below
   `δ_1` is invisible to `N` but is *forbidden at the first order* by `[f,g] ∈ C^*`.
2. **D1-PIN, retyped upward (reading, not a correction).** `floor = ceiling` at `r = 1` is
   the order-matching of LOCAL-KELLER; it is *equivalent* to the bottom bracket having a
   constant, rather than vanishing, leading term. This gives D1-PIN a proof that does not
   pass through the FLOOR/CEILING inequality pair at all, and explains "only at `r = 1`"
   as "only there is the Jacobian leading".
3. **`κ` is pinned, not just nonzero.** `κ = c·d·e/q` with `q` the D1-PIN weight. So the
   single number `q` that computes `N` also computes the bottom-disc Wronskian constant.
   Checked in closed form on `(y,x+y^k)` and on the selected skeleton.
4. **Search condition (16), as a candidate, is a RIGIDITY condition and not an emptiness
   condition.** #17 §C lists `OPEN[STAR-REALISABILITY]` as "a skeleton whose bottom
   polynomial `p(π)` is forced to have a repeated root dies". This lane shows the repeated
   root never occurs (STAR-SIMPLE is automatic), and that the real content is STAR-ABC.
   `OPEN[STAR-REALISABILITY]` is therefore **answered NO as posed** for every
   `(d,e,V_2)` decided in §4.3.
5. The producer of D1-SUBTREE wrote that Moh's recursion stops at `D_1` because Def 5.1(1)
   at `i = 0` would need `(m/n)V_1` roots of `f`. That reading is untouched here; §3.1
   adds the analytic reason: below `δ_1` the Jacobian has already been *fully used*, and
   (ODE-`k`) for `k ≥ 1` is a linear, generically unobstructed, deformation problem.

---

## 7. Opens raised, each with its bounded quantity

* **`OPEN[STAR-ALLV]`** — does the Davenport–Stothers dessin of STAR-ABC(3) exist for
  every `(d,e,V_2)` in the census? *Bounded quantity:* the 220 triples `(d,e,V_2)` at
  `D ≤ 120` (96 among the `N ≥ 6` (UNI) survivors); 15 decided REALISABLE here
  (`b_1 = dV_2 ≤ 6`); 205 undecided, of which the largest is `b_1 = 76`. Route: the
  Hurwitz existence count for the profiles `([e^{dV}],[d^{eV}],[(d+e)V−1,1^*])` in
  `S_{deV}`, a finite character computation, or the Stothers/Zannier existence theorems.
* **`OPEN[DISC-COUPLING]`** — the local count of §3.4 gives `2` free parameters per
  non-resonant order at *one* bottom disc, but the outer-scalar half of those parameters
  is shared by all `k` bottom discs. *Bounded quantity:* at the selected skeleton
  `k = 20` discs, `2` local parameters per order of which `2` are outer scalars shared
  across all 20, against `1` condition per resonant order per disc, i.e. `20` conditions
  at each resonant order against `3·20 + 2` parameters — the first place a *counting*
  obstruction can appear. This is the natural successor computation.
* **`OPEN[DELTA-DENOM]` (measured anomaly; NOT used above).** By Moh Prop. 5.3, `δ_i` is
  a *minimum of `ord_t(τ−τ')` over roots of `g·ΠT_j`*, so its reduced denominator must
  divide the lcm of the ramification indices of the branches involved. Def 5.1(3) does not
  impose this. Measured (`deltadenom.py`, `D ∈ [48,120]`, 902 893 V-skeletons):
  ```text
     denom(δ_1) | n              : 6 719  (0.74%)
     denom(δ_1) | n  or | m      : 8 634  (0.96%)
     among the 9 553 (UNI)-N≥6 survivors, denom(δ_1) | n on 3 266 (34.19%)
     Moh's six published survivor rows: denom(δ_1) | n on 5/6, | n or m on 6/6
       (64,48) 9/16 | 64 ✓ ; (84,56) 16/21 | 84 ✓ ; (84,56) 7/12 | 84 ✓ ;
       (75,50) 1/2 ∤ 75 but 2 | 50 ✓ ; (75,50) 2/3 | 75 ✓ ; (99,66) 4/9 | 99 ✓
  ```
  The selected `D = 105` skeleton has `δ_1 = 3/4` with `4 ∤ 105`, `4 ∤ 70`, and
  `δ_2 = 71/95` with `95 ∤ 105`. *Bounded quantity:* the set of partitions of `n` (and of
  `−M_j`) into branch ramification indices whose lcm is divisible by `denom(δ_i)`; the
  provable weak form is only `denom(δ_i) ≤ n·max(n,m)`. **Nothing in §1–§5 depends on
  this**, and it is emphatically not asserted as a filter: the six-of-six against
  0.96% coincidence is a signal, not a theorem. It is the cheapest next arithmetic
  probe of Def 5.1(3).
* **`OPEN[EIGEN-A]`** — is `A = denom(L·δ_1)` with `L` the order of the head-exponent
  group? *Bounded quantity:* one worked tower with `s ≥ 3` and an explicitly computed
  head; the `s = 2` case is Moh's own (Prop. 5.5) and holds with `L = 1`. If confirmed,
  STAR-EIGEN becomes a genuine skeleton-plus-head condition; §4.4's consequence at
  `(2,3,1)` is conditional on it.

---

## 8. FALLACY-v2 audit

* **Flag/place/series.** `a_1 = eV_2` (roots of `g` in `D_1`), `b_1 = dV_2` (roots of
  `f`) and `deg C = V_2(de−d−e)+1` (the ABC residual) are kept distinct and never
  identified; the `π`-plane is never identified with the `t`-line or the `y`-line.
* **Per-ray/exit-set charge.** No exit price is asserted; no `charge_basis` line is
  emitted. `Σ_B V_2(B) = u = 20` is quoted from promoted D1-PIN, not re-derived.
* **Carrier/attainment.** §3.4's "positive-dimensional" is the dimension of the *local*
  solution set at two orders, never an attainment claim for a Keller pair. §4.3's
  REALISABLE is existence of the *bottom star* over `C`, explicitly not realisability of
  the skeleton. STAR-SUM's `S_k = 0` is an equality (Lagrange), not a bound.
* **Raw remainder degree.** `deg C` branches on the vanishing of the leading coefficient
  `c_γ(γ − deV_2)`; `C = 0` is excluded by `gcd(P,Q) = 1`.
* **Variable/ring map.** `(x,y) → (t,π)` is declared with its Jacobian `−t^{δ−2}`;
  `Φ, Γ ∈ C[[t^{η}]][π]`; `starcheck.py` declares `Q[π]/(p_g)` and inverts `p_g'` by
  extended gcd, which re-checks `gcd(p_g,p_g') = 1`.
* **Prime label/derivative.** `p_g'`, `Φ'`, `Γ'` are always `d/dπ`; `F_t` is `d/dt`;
  `X'(u) = dX/du` in control 2.
* **Fail-closed.** Every driver aborts on a failed check; every control table printed
  above is accompanied by its `checks, failures` line. The two numerical drivers
  (`starnum.py`) are **not** used for any claim: every existence verdict in §4.3 comes
  from the exact Gröbner decision, and the numerical run is reported only as the route
  that first exposed the spurious `Q = R^d` component.
* **Degenerate-branch trap, recorded.** The first numerical attempt converged to
  `Q = R^d`, `P = R^e` (where `κ ≡ 0`) and reported FAIL for `V_2 ≥ 2`; that is a
  *spurious* component of the truncation system, not a kill. It is removed by saturation.
  Anyone repeating §4.3 must saturate at `κ ≠ 0`.

---

## 9. Typed verdict block

```text
LANE         TIME-FUNCTION-ENDGAME (flagship, Opus 5), basis 8743131113db
PART (1)     D=105: 5037 admissible V-skeletons, 63 with an integer N>=6 under (UNI),
             49 with N in [6,16].  Smallest (declared order): n=105, m=70, K=35,
             (d,e)=(2,3), s=3, M=(-70,-63,103), V=(1,4,1), delta=(3/4,71/95,-1),
             a=(3,60,105), b=(2,40,70), q=3/10, u=20, N=20*1*3/10=6.
PROVED-HERE  LOCAL-KELLER (the transported Jacobian, exact at all orders);
             BOTTOM-ODE  d p_f p_g' - e p_g p_f' = kappa = c d e / q, kappa != 0;
             STAR-SIMPLE (p_f AND p_g squarefree, coprime);
             STAR-RESIDUE p_f(c_i) p_g'(c_i) = kappa/d at every star point;
             STAR-SUM sum_i c_i^k/p_g'(c_i)^2 = 0 for k <= (e-d)V_2-2, and
                      = (d/kappa)(lc p_f/lc p_g) at k = a_1-b_1-1;
             STAR-ABC (BOTTOM-ODE <=> Mason-Stothers equality <=> 3-point Belyi map
                      with profiles [e^{dV}],[d^{eV}],[(d+e)V-1,1^*]);
             STAR-EIGEN (Moh Prop 5.5's dichotomy, at every s: a_1=1,b_1=0 or
                      a_1=0,b_1=1 mod A; A | (d+e)V_2-1);
             the resonance set of L_eps is exactly mu*{0,...,a_1}, mu = -lam_g/a_1.
PART (2)     Order 0 DETERMINED: the (2,3,1) star is a single group orbit,
             p_g = pi(pi^2+b), p_f ~ pi^2+2b/3, star {0,+s,-s}.
             Orders 1,2: verdict (b) CONSISTENT, POSITIVE-DIMENSIONAL.  Non-resonant
             order: 7 unknowns, 5 conditions, cokernel 0 -> 2 free parameters.
             Resonant order (eps in mu{1,2,3}): kernel 3, cokernel 1 -> exactly one
             scalar condition; at eps_2 = mu it cuts the order-1 plane to two lines.
             NO KILL at orders 1 and 2.  Next order to impose: the next lattice point
             in mu*Z_{>0} (mu = 1/20 and 2mu are both reached, 1/20 = 19*(1/380)).
PART (3)     A uniform condition EXISTS in three equivalent exact forms and its
             constraint count grows like (e-d)V_2 - 1.  It does NOT kill by skeleton:
             15 of 15 decided (d,e,V_2) are REALISABLE by Nullstellensatz over Q,
             saturated at kappa != 0.  OPEN[STAR-REALISABILITY] answered NO as posed.
PART (4)     Controls 78 checks / 0 failures.  (y,x+y^k) and (y+x^2,x+(y+x^2)^2)
             satisfy (i)-(ii) exactly with a_i = 0 and no log; (y,x^j+y^k) with j>=2
             satisfies (i) and FAILS (ii) with the obstruction in closed form; all 7
             two-tower rows fail both the order-matching and BOTTOM-ODE.
STRENGTHENED D1-STAR(b): p_f squarefree too (f-roots of D_1 separate at delta_1).
NOT CLAIMED  any degree ceiling; realisability of any skeleton; emptiness of any degree
             or cell; (UNI) beyond one orbit; the delta-denominator filter; A = denom(L delta_1).
OPEN         STAR-ALLV (205 undecided triples, largest b_1 = 76);
             DISC-COUPLING (20 discs share the outer scalars: 20 conditions vs 62
             parameters at each resonant order -- the successor computation);
             DELTA-DENOM (measured: 0.96% of the census vs 6/6 of Moh's rows);
             EIGEN-A (one worked s>=3 tower with an explicit head).
READING      The bottom-disc interpolation conditions ARE a one-variable Keller
             equation, and its solutions are ABC-extremal pairs / dessins.  The
             endgame is therefore not "does the star exist" -- it always does -- but
             "do the twenty rigid stars of one skeleton fit together", which is
             DISC-COUPLING.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `46661`.
- Body SHA-256:
  `9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1`.
- Frozen basis: `8743131113dbea1a599766dc625992f4f77270da`.
- Drivers: `box/tfe-drivers-20260902/` (hashes in §0); logs `*.log` alongside.
