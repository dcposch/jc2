# Hostile review: KELLER-PENCIL-GENUS — UNIT-SPEED, FORK-GENUS, θ_inf = κ, NEG-GENUS, PROFILE-WITNESS, the conditional ceiling

**Lane.** `KELLER-PENCIL-GENUS-REVIEW`. Date 2026-09-02. Reviewer grok-4.6.
**Charged producer.** Opus 5 flagship `keller-pencil-genus-opus5-20260902.md` (PROVED-HERE / UNREVIEWED).
**Method.** Independent adjunction / tree / RH, plus sympy 1.14.0 over `QQ` and Singular 4.4.1 `normal.lib`. No AWS, no `sat()`, no ledger edit, no `jc2-lean`. Default to refutation; every displayed genus, Jacobian, preimage count, and `κ` column was recomputed. No new exit price.

**Headline.** The mechanism claim survives: the 1-form on a fibre is Riemann–Hurwitz (a wash), the genus of the generic pencil member is the fork mass of the polar subtree, and `NOETHER-K` / `R_aff = 0` cannot bound that mass. Nothing here is an unconditional ceiling. The nine `N = 2W` kills, including live `N = 4` (B3), are legitimate **only** as `CH2` conditionals. No item is `REFUTED` as a theorem. Two advertising overclaims and one wording bug are `GAP` with one-line repairs; they do not carry load.

## Verdict table

| # | Item | Verdict |
|---|---|---|
| (a) | UNIT-SPEED: `ω_u\|C_t=dv`; zeros `μ−1` at `nS` places; poles `e+1` over `∞`; mate ⇔ exactness | **CONFIRMED** with wording repair `KPG:145`. Do not promote the algebraicity converse. |
| (b) | FORK-GENUS; `Z·K_X=2g_L−2−N`; checks `(x,y+x^k)`, `(x,xy^m)`, `N=4` (B3) | **CONFIRMED**. Promote `KPG:257-273` `Lambda`, not the executive truncation. |
| (c) | `θ_inf=κ` (three proofs; 15/15); SHARP-CHAU `D≥nS+κ` | **CONFIRMED** (Proof 1). **GAP** on “three independent proofs” of the general-dominant statement. |
| (d) | `Psi=0` ⇒ `n(W−S)≤2N−2`; `E_0` a leaf ⇒ `nW≤2N−2`; kill of `N=2W` cells | **CONFIRMED** as conditional. Kill is legitimate *as a conditional*. `E_0` a leaf is **false** on `(x,y+x^k)`. |
| (e) | NEG-GENUS; PROFILE-WITNESS (Jac, `N`, profile, `g→∞`) | **CONFIRMED**. PROFILE matches the listed numerical constraints and is non-Keller. |
| (f) | `NOETHER-K` alone cannot produce a ceiling | **CONFIRMED** as a theorem about the ramification pairing. **GAP** if read as “Keller has nowhere else to enter”. |
| — | GENUS-DEFECT; charge’s `Z·(K_X+2Z)` off by `N` | **CONFIRMED**. `I12:67-69` is the correct form. |
| — | ATYPICAL-LEDGER; vanishing cycles an identity | **CONFIRMED**. RH for `A_F`; no genus bound. |
| — | `OPEN[FORK-MASS]`, `OPEN[POLAR-CHAIN]`, `OPEN[SING-WITNESS]` | **CONFIRMED** well-posed. Bounded quantities in §9. |

No `REFUTED` theorem; no cell emptied; no Keller realisation.

---

## 0. Custody, ring map, scope

Frozen charged inputs, hashed on this host with `shasum -a 256` **before any reading**. All five match the charge exactly:

```text
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  [frozen]/keller-pencil-genus-opus5-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  [frozen]/n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  [frozen]/n-vs-mapdeg-review-gpt55-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  [frozen]/meridian-floor-sharpen-review-gpt55-20260902.md
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  [frozen]/integration12-coordinator-fable51-20260902.md
```

Line tags `KPG:L`, `NVM:L`, `NR:L`, `MFR:L`, `I12:L` refer to these frozen copies. `FALLACY-v2` in force. Producer `/tmp/kpg` drivers were listed, not used as premises.

**Ring map (FALLACY variable/ring).** Field `QQ`, ring `QQ[x,y]`, homogenisation `QQ[X,Y,Z]`. Pencils `(α,β,t)=(3,5,7)` and `(2,11,3)`. `F_{m,k}=ψ_k∘(x,xy^m)` by `Q=xy^m`, `P=x+Q^k`; image check: `{Q=V}` ⇒ `x=U−V^k` and `(U−V^k)y^m=V`. `G_k=ψ_k∘(x,xy^4−y^2)` likewise: `x=U−V^k` and `(U−V^k)y^4−y^2−V=0`. Matching names are not a map proof. Singular `genus` = `normal.lib` geometric genus of `{αP+βQ−t=0}`; controls `y^2−x^3−x` (1), `y^2−x^3` (0), `y^2−x^2−1` (0), `y^3−x^3−1` (1). No `sat()`. Unit ideal iff `dim=-1` and `reduce(1,I)=0`. No primed symbol is a derivative except `∂/∂x`, `∂/∂y`, `du`, `dv`, `Jac`.

**Consumed typing.** `MF-EXACT` `MFR:143-149`; `SHARP-CHAU` `MFR:76-81`; `NOETHER-K`/`DEG-SPLIT` `NR:44-51,220-230` (Keller/H2). NVM engine columns are data, checked in §3. Coordinator adjunction `I12:67-69` is under test in §2.

**Naming collision.** `Lambda` here is leaf mass on `T_+=supp Z`. NVM’s `Lam=Σ s_l n_{c(l)}` is dicritical polar mass. Never substituted.

---

## 1. Item (a) — UNIT-SPEED versus Riemann–Hurwitz

**Verdict: CONFIRMED**, with a wording repair at `KPG:145` and a scope repair on the converse “exactness ⇒ polynomial mate”.

### 1.1 Local orders, re-derived

Let `C` be a smooth connected affine curve, `v ∈ 𝒪(C)` étale of degree `N` onto `A^1`, compactified to `π: X → P^1` of degree `N`. Write `τ` for a local parameter at a place `P` of `X`.

- If `v` is regular at `P` and `v−v(P) = τ^μ · u(τ)` with `u(0)≠0`, then `dv = (μ τ^{μ−1} u + τ^μ u') dτ`, so `ord_P(dv) = μ−1 ≥ 0`. These are the **non-proper / escaping** places: `v` stays finite, approaching a point of `L ∩ A_F`. Under the generic meridian cycle type `1^a ∏ μ_l^{s_l}` there are `S` such places per meridian, `n` meridians, and `Σ(μ−1) = n(W−S)`.
- If `v` has a pole of order `e` at `P`, `v = τ^{-e} · u(τ)`, then `ord_P(dv) = −(e+1)`. These are the places over `∞`. There are `θ_inf` of them, and `Σ e_P = N`, hence `Σ(e_P+1) = N + θ_inf`.

On the affine curve, étaleness says `dv` has neither zero nor pole. So `div(dv)` is supported at infinity, with **zeros** (not poles) at the `nS` escaping places and **poles** at the `θ_inf` places over `∞`. This is `KPG:130-135`, and it is the exact point the naive “`(ω) = −Σ c_P P` with `c_P≥1`” count missed.

Degree of a meromorphic 1-form: `deg div(dv) = n(W−S) − N − θ_inf`. Riemann–Hurwitz for `π` is independently

```text
2 g − 2  =  −2N + n(W−S) + (N − θ_inf)  =  n(W−S) − N − θ_inf
```

which is `MF-EXACT` (`MFR:143-149`). The degree identity **is** Riemann–Hurwitz. Residues of an exact form vanish; periods of `dv` vanish because `v` is single-valued. Neither is an extra condition.

**Wording repair, `KPG:145`.** Clause (i) writes “`deg(pole part) = N`”. The pole part of `dv` has degree `Σ(e_P+1) = N+θ_inf`, not `N`. The proof at `KPG:155` correctly uses `Σ(e_P+1) − θ_inf = N` (the degree of `v` as a map to `P^1`). Repair: replace “`deg(pole part)=N`” by “`Σ_P e_P = N`”, or by the proof’s own `Σ(e_P+1)−θ_inf = N`. Load-bearing equations are unaffected.

### 1.2 Concrete controls

- **Automorphism** `(x, y+x^k)`, `N=1`, `A_F=∅`, `n=0`. Fibre of `u=αx+β(y+x^k)` is a graph over `x`, hence `C_t ≅ A^1`, `g=0`, `θ_inf=1`. Here `v` has a single pole of order `e=1`, `dv` a pole of order `2`, no zeros: `deg div = −2 = 2g−2`. Homogenised leading form `5 X^k` (CAS, `k=2,3`): one point `[0:1:0]` on `L_∞`, matching `θ_L = θ_inf = 1`. Singular `genus(3x+5(y+x^k)−7) = 0` for `k=2..5`.
- **Keller-free submersion** `f_b = x + x^2 y^b` (`KPG:171-175`). Critical ideal of `(∂_x f, ∂_y f)` is the unit ideal for `b=2..5` (Singular `dim=-1`, `reduce(1,I)=0`). Fibre genus `0,1,1,2,2` at `b=2..6`, matching `2g−2 = b−2−gcd(2,b)` at 5/5. Submersion alone does not bound `g`. This negative control bites, as charged.

### 1.3 The wash, and the converse

On a Keller fibre `(X_u,v)` is an étale degree-`N` coordinate; its only numerical content is `(n,N,a,W,S,θ_inf)` through RH. That is the wash `KPG:40-47`. One direction of `KPG:163-167` is tautological (`Jac∈C^*` plus a linear change in the `(P,Q)`-span gives a polynomial mate, `dx∧dy=du∧dv`). The converse — fibrewise holomorphic exactness ⇒ a polynomial mate — has an algebraicity remainder that `KPG:165` names and does not close. Promote the wash, not the converse. Nothing downstream uses it.

---

## 2. Item (b) — FORK-GENUS, two derivations, three checks

**Verdict: CONFIRMED.** Executive-summary `Lambda` is truncated; the theorem statement at `KPG:257-273` is the one to promote.

### 2.1 Adjunction (GENUS-DEFECT)

`σ: X → P^2` resolves the base locus of the net `⟨P^h_D, Q^h_D, z^D⟩`. `Φ = F̄∘σ: X → P^2` is a morphism of geometric degree `N`. `Z := Φ^*(L_∞)`. Then `Z^2 = deg(Φ)·L_∞^2 = N`. The complete linear system `|Φ^* 𝒪(1)|` is base-point-free, so Bertini gives a smooth generic member `D_L = Φ^*(L)`. This `D_L` is the smooth model `X_L` of the generic pencil fibre (affine part `D_L ∩ A^2 = C_L`). Adjunction on the surface:

```text
2 g_L − 2  =  D_L · (D_L + K_X)  =  Z · (Z + K_X)  =  N + Z·K_X,
```

hence `Z·K_X = 2 g_L − 2 − N`. No Keller, no `H2`. This is `KPG:193-195` and the coordinator desk note `I12:67-69`.

**Charge correction.** The displayed `2g_L−2 = Z·(K_X+2Z) = Z·K_X+2N` is the relative canonical pairing for a *fibre* class (`Z^2=0`). On `X` one has `Z^2=N≠0`. Off by `N`, as `KPG:197-201` says. Confirmed.

### 2.2 Tree combinatorics: why `Psi − Lambda − κ` exactly

Boundary components are smooth rational, so `K_X·C=−2−C^2` and `Z·K_X=Σ_{T_+} m_C(−2−C^2)`. SNC: `Z·C=m_C C^2+Σ_{adj} m_{C'}=c_C`, hence `−m_C C^2=Σ_{adj} m_{C'}−c_C`. The double sum runs over neighbours in the full tree `L~`; neighbours with `m=0` (dicriticals, and anything not in `supp Z`) contribute nothing, so it equals `Σ_{C'∈T_+} m_{C'} deg_{T_+}(C')`. Each edge of `T_+` is charged to both ends once. `Σ_{T_+} c_C=κ` (`c_C=k_C` if `Φ(C)=L_∞`, else `0`). Thus `Z·K_X=Σ m_C(deg_{T_+}-2)−κ`.

With `deg` = valency inside `T_+`, set `Lambda=Σ_{deg=1} m_C + 2 Σ_{deg=0} m_C` (leaf mass) and `Psi=Σ_{deg≥3} m_C(deg−2)` (fork mass), so `Σ m(deg−2)=Psi−Lambda` (valency-2 vertices cancel). Then `Z·K_X=Psi−Lambda−κ` and `2g_L−2=N−κ−Lambda+Psi` (`KPG:263-273`). Valency-2 vertices are the chain-length / satellite-mass half `T`, disjoint from `Psi`.

`Lambda≥2`: nonempty `T_+` (`N>0`); one vertex ⇒ `Lambda=2m≥2`; else ≥2 leaves. The pairing never used connectedness (`T_+` is a forest if the generic `u`-fibre is reducible; Keller has irreducible generic member, `MFR:107-116`).

**Repair, `KPG:50` vs `KPG:257`.** The summary omits the isolated-vertex term that the theorem includes. Promote `KPG:257-259`. Controls `id` and `(x^2,y^2)` are that case (`Lambda=2` and `4`).

### 2.3 Three mandatory checks

**Automorphism** `(x, y+x^k)`. `N=1` forces `κ = Σ k_C = 1` (`N = Σ m_C k_C` is a sum of positive integers). `g_L=0` (graph; Singular 0 at `k=2..5`). FORK-GENUS: `−2 = 1 − 1 − Lambda + Psi`, so `Psi − Lambda = −2`. With `Psi≥0`, `Lambda≥2` this forces `Psi=0`, `Lambda=2`: `T_+` is a chain (or a point) of leaf mass 2. Then `Z·K_X = −3`, Noether, matching `NVM:421-422` and `KPG:399-401`.

Hostile addendum, used in §4: `m_{E_0}=D=k`. If `E_0` were a leaf of `T_+` then `Lambda ≥ k+1 ≥ 3` for `k≥2`, contradicting `Lambda=2`. So **`E_0` is not a leaf** on the only infinite Keller family in the record. `CH2` is a genuine extra hypothesis, not a default of Keller compactifications.

**(x, x y^m).** Geometric degree `N=m`: `x=U`, `U y^m=V`. Fibre `x(α + β y^m)=t` is rational (`x = t/(α+β y^m)`), `g_L=0`. Mate `v = x(γ+δ y^m)` has poles exactly where `α+β y^m=0`, i.e. `m` places, so `θ_inf=m`. ESCAPE-KAPPA then gives `κ=m=N`. FORK-GENUS: `−2 = m − m − Lambda + Psi`, again `Psi−Lambda=−2`. Singular `genus=0` at `m=1..5`. Homogenised leading form `5 X Y^m`: geometric points `[1:0:0]` (multiplicity `m`, the `θ_inf` places) and `[0:1:0]` (the single escaping place, `nS=1`). Closed-form family (A) with `c=1`: `2g−2 = N−1−gcd(1,N)−gcd(0,N) = N−1−1−N = −2`, `κ=gcd(0,N)=N`. Consistent.

**Promoted `N=4` (B3) data** (`N=4`, `a=2`, `W=2`, `S=1`, `n=4` from `MF-EXACT` plus `MFR:176-182`). Then `2g_L+θ_inf=2`, so `(g_L,θ_inf)=(0,2)` and `κ=2`. FORK-GENUS: `−2 = 4 − 2 − Lambda + Psi`, i.e. `Lambda − Psi = 4`. POLAR-DEGREE (Keller+H2, §4): `n(W−S)=4 = 8 − Lambda + Psi`, same relation. If moreover `E_0` is a leaf then `Lambda ≥ D+1 ≥ nS+κ+1 = 7`, hence `Psi ≥ 3`: the polar tree forks **or** `E_0` is not a leaf. This is arithmetic, not a resolution. It is the first test case of `OPEN[POLAR-CHAIN]`.

### 2.4 POLAR-DEGREE needs Keller

FORK-GENUS holds for every dominant `F`. The ramification formula (NVM `NR:220-226`, re-derived from `K_X=−3Z+R`) is

```text
2g_L − 2  =  Z·R − 2N  =  Z·R_aff + n(W−S) − N − κ
```

under `H2`. Equating with FORK-GENUS: `n(W−S) = 2N − Lambda + Psi − Z·R_aff`. Keller is `R_aff=0`, and that is `POLAR-DEGREE` (`KPG:287`). Scope is correct in the producer; it is not a general-dominant identity.

---

## 3. Item (c) — `θ_inf = κ`, three proofs, 15/15, Chau

**Verdict: CONFIRMED** as a theorem for every dominant polynomial `F` (generic direction). **GAP** on the claim that all three proofs establish that general-dominant statement.

### 3.1 Proof 1 (base points) — this is the proof

`z_u = L ∩ L_∞`, generic on `L_∞`. The 0-cycle `Φ^*(z_u)` is supported on components `C` with `Φ(C)=L_∞`: contracted components of `T_+` map to finitely many points of `L_∞`, avoided by genericity; dicriticals map onto `A_F`-bar, which meets `L_∞` in a finite set (the places at infinity of `A_F`), likewise avoided. `H2` is **not** required for that last sentence — only that `A_F`-bar `∩ L_∞` is finite. For generic `z_u`, `Φ|_C: C → L_∞` is unramified of degree `k_C`, and distinct such `C` do not share points over `z_u`. So `# Φ^{-1}(z_u) = Σ k_C = κ` geometric points.

`D_L=Φ^*(L)` contains `Φ^{-1}(z_u)`. The target `P^1` of `v|_{C_t}` is the line `L`, and `∞∈L` is `z_u`, so the places of `X_L` over `∞` are exactly `Φ^{-1}(z_u)`. Hence `θ_inf=κ` (`KPG:211-217`), for every dominant `F` with generic direction.

### 3.2 Proofs 2 and 3 are Keller+H2 consistency

**Proof 2.** GENUS-DEFECT `2g−2 = N + Z·K_X` (always) plus `NOETHER-K` `Z·K_X = −2N − κ + n(W−S)` (Keller+H2, `NR:353-357`) give `2g−2 = −N −κ + n(W−S)`. `MF-EXACT` is the same with `θ_inf` in place of `κ`. So the three identities are compatible iff `θ_inf=κ`. This **uses** Keller. It is a genuine third derivation **inside** Keller+H2, not a proof of the general-dominant theorem.

**Proof 3.** `K_X=−3Z+R` and the `H2` split `Z·R=Z·R_aff+(N−κ)+n(W−S)` equate with `MF-EXACT` after `R_aff=0`. Same Keller+H2 scope as Proof 2.

**Repair, `KPG:58-59` and `KPG:209`.** Keep the theorem for every dominant `F`, citing Proof 1. Retitle Proofs 2–3 as “Keller+H2 corollaries / consistency with `NOETHER-K` and `MF-EXACT`”. Do not advertise three independent proofs of the general statement.

### 3.3 Closed form versus NVM’s printed engine (the 15/15)

Independent cyclic-cover RH, no resolution. Fibre of `F_{m,k}`: `y^m = α w / (t − β w − α w^k)`, a cyclic `m`-cover of `P^1_w` branched at `0` (index `e=1`), at the `k` simple poles of the denominator, and at `∞` (`e=k−1`). Number of places over `∞` is `gcd(k−1,m)`. On the fibre, `v` is affine-linear in `w` (`KPG:429-430`, re-expanded here: `P = t/α − (β/α)w` identically), so `v→∞` iff `w→∞`. Thus `θ_inf = gcd(k−1,m)`. Proof 1 then gives `κ = gcd(k−1,m)`.

Family (A) `(x, x^c y^N)`: `y^N = (t−αx)/(β x^c)`, places over `x=∞` number `gcd(c−1,N)`, and `v` is affine-linear in `x`, so `κ = gcd(c−1,N)`.

Against `NVM:430-431,551`, closed form matches 15/15: `(B)` `m=2` `κ=1,2,1,2,1` and `Z·K_X=−2,−2,0,0,+2`; `(B)` `m=3` `κ=1,1,3,1,1` and `Z·K_X=−1,+1,+1,+5,+7`; `(A)` `N=8` `c=1..5` `κ=8,1,2,1,4`. No resolution used. (NVM’s summary `D=6k` for `ψ_k∘(x,xy^2)` is a typo for `D=3k`; not load-bearing.)

### 3.4 SHARP-CHAU sharpens to `D ≥ nS+κ`

`MFR:389-391`: `θ_L = nS + θ_inf ≤ D_F` (a degree-`D` plane curve meets `L_∞` in a divisor of degree `D`, hence in at most `D` places). With `θ_inf=κ`, `D ≥ nS+κ`. This is strictly stronger than banked `D≥nS+1` (`κ≥1`, and `κ=1` is the old bound). Under `H2`, `DEG-SPLIT` (`NR:310-314`, review-CONFIRMED) reads `D = nS + κ + T` with `T≥0`, so SHARP-CHAU *is* DEG-SPLIT plus effectivity of satellite mass. Confirmed as an identification of two statements, one banked (Chau/places) and one NVM-PROPOSAL (DEG-SPLIT), now coinciding under `H2`.

The remaining infinity count in `MF-EXACT` is now a boundary invariant `κ∈[1,N]`.

---

## 4. Item (d) — conditional ceiling, translations, the `N=2W` kill

**Verdict: CONFIRMED as a pair of conditionals.** The translations are correct. The kill of the nine `N=2W` cells, including live `N=4` (B3), is legitimate **as a conditional statement**. Neither hypothesis is proved.

### 4.1 `Psi = 0` ⇒ `g_L ≤ (N−1)/2` and `n(W−S) ≤ 2N−2`

FORK-GENUS with `Psi=0` and `Lambda≥2`: `2g−2 = N−κ−Lambda ≤ N−κ−2`, so `g_L ≤ (N−κ)/2 ≤ (N−1)/2`. POLAR-DEGREE (Keller+H2+ESCAPE-KAPPA): `n(W−S) = 2N − Lambda + Psi ≤ 2N−2`. Both `KPG:289-292`. Correct.

`Lambda≥2` is an identity of a nonempty tree, not an estimate. Valency-2 vertices do not appear; `Psi=0` kills the only positive term.

### 4.2 `E_0` a leaf ⇒ `nW ≤ 2N−2`

`m_{E_0}=D` always (`NVM:54-55`, `(I1)`: the coefficient of the strict transform of `L_∞` is not changed by blowing up points on it). If `E_0` is a leaf of `T_+` then `Lambda ≥ D + 1` (the other leaf has `m≥1`; an isolated `E_0` is even larger, `Lambda=2D`). `CH2` also takes `Psi=0`. Then

```text
nW  =  n(W−S) + nS  =  2N − Lambda + nS  ≤  2N − (D+1) + nS.
```

SHARP-CHAU as sharpened: `D ≥ nS+κ`, so `−D+nS ≤ −κ ≤ −1`, hence `nW ≤ 2N−2`. This is `KPG:293-296`. Correct, and it uses the sharpened Chau bound (without `κ` one only gets `nW ≤ 2N−1`, off by one — the sharpening is load-bearing for the stated constant `2N−2`).

### 4.3 The nine `N=2W` cells, including live `N=4` (B3)

`N=2W` and `nW ≤ 2N−2` ⇒ `n ≤ 4 − 4/N < 4`, so `n ≤ 3`. Banked `MERIDIAN-FLOOR+` (`NR:56-57,289-292`; `I12:50-53`): `n ≥ ceil((N−1)/(W−S))+1`. The *weakest* floor in these cells is `S=1` (allowed by `7.B'`), `W−S = W−1 = N/2−1`, giving `n ≥ 4` at every `N=4,6,…,20`. Floor `4` versus ceiling `3`: empty. Independently of `beta`.

The nine pairs `(N,W) = (4,2),(6,3),…,(20,10)` are exactly the `N=2W` cells the producer lists (`KPG:559-561`). Live `N=4` (B3) has `n=4` forced (`MF-EXACT` + `(g,θ)=(0,2)`), and `nW=8 > 6=2N−2`. **Conditional kill, legitimate.**

At `W=2`, `beta=1`, `MF-SHARP` has `n≥N` (`MFR:370`) while `CH2` has `n≤N−1`, so `CH2` forces `beta≥2` (`KPG:563-564`).

`CH1` does not kill the live cell (`n(W−S)=4≤6`). Against `MERIDIAN-FLOOR+` the `CH1` ceiling is ~twice the floor, so it kills no counting-admissible cell on meridian-floor data alone. The “0 of 81” is this arithmetic; the translation asked for does not need the 81-row driver.

### 4.4 What is not proved

`Psi=0` is false in family (B). `E_0` a leaf is false on automorphisms with `k≥2` (§2.3). Neither is known for noninvertible Keller maps (`KPG:68-69,705-708`). Do not bank any `EMPTY`. `OPEN[POLAR-CHAIN]` at `N=4` (`Lambda−Psi=4`, and `Psi≥3` if `E_0` is a leaf) is well-posed.

---

## 5. Item (e) — NEG-GENUS and PROFILE-WITNESS, own CAS

**Verdict: CONFIRMED.** Rings as in §0. Three `(m,k)` and three `k` are the charged minimum; the tables run a larger desk set.

### 5.1 THEOREM NEG-GENUS

`F_{m,k} = ψ_k ∘ (x, x y^m) = (x + x^k y^{mk}, x y^m)`.

- **Jacobian.** `Jac F_{m,k} = m x y^{m-1}` (chain rule, `Jac ψ_k=1`). Not a unit for `m≥1`. Non-Keller.
- **Geometric degree.** On `{Q=V}`, `x=U−V^k` and `(U−V^k) y^m = V`. Generic `(U,V)=(3,5)`: squarefree of degree `m` in `y` (discriminant nonzero at the three charged pairs). `N=m`, independent of `k`.
- **`A_F`.** Escape `x = t^{-m} u`, `y=t` along `(x,xy^m)` yields `A_G={U=0}`; left action of `ψ_k` sends this to `{U=V^k}`, irreducible, rational, one place at infinity, `n=k`. Generic point of `A_F` has `a=0` affine preimages (`x=0` and `V≠0` is empty for `G`). `W=m`, `S=1`, `μ=m`.
- **Genus, independent RH.** Cyclic `m`-cover `y^m = −w/(w^k +(β/α)w − t/α)`: ramification `(m−1) + k(m−1) + (m−gcd(k−1,m))`, so `2g−2 = (m−1)k − 1 − gcd(k−1,m) = (m−1)(k+1) − m − gcd(k−1,m)`. `θ_inf=gcd(k−1,m)=κ` (§3.3). Affine ramification at `w=0` is `m−1`. The pairing identity of §2.4 then gives `Z·R_aff = m−1 = N−1`, **constant in `k`**.

Singular `genus(3P+5Q−7)`, and a second pencil `2P+11Q−3` on the charged triples. Fibres irreducible over `QQ`.

```text
(m,k)   N  n  κ=gcd(k-1,m)  2g−2 closed  g closed  g (3,5,7)  g (2,11,3)  Jac
(2,2)   2  2  1             0            1         1          1           2xy
(2,5)   2  5  2             2            2         2          2           2xy
(3,4)   3  4  3             4            3         3          3           3x y^2
```

The producer grid `m=1,2,3` × `k=2..6` was rerun (15/15; `m=1` gives `g=0`). Family (A) sample `2g−2=N−1−gcd(c,N)−gcd(c−1,N)`: `(N,c)=(2,1) g=0; (3,2) g=1; (8,2) g=3; (8,5) g=2; (5,2) g=2` (5/5). For `m≥2`, `g→∞` at fixed `N=m`. `Z·K_X=(m−1)(k+1)−2m−gcd(k−1,m)→+∞`, matching `NVM:637-639` as data.

Profile: family (B) has `a=0`, so it **violates** `(C1)` and is not a profile witness. That is the producer’s dichotomy (`KPG:468-469`), confirmed.

### 5.2 THEOREM PROFILE-WITNESS, including Jac

`G_k = ψ_k ∘ (x, x y^4 − y^2)`. `H = (x, Q)` with `Q = x y^4 − y^2`; `Jac G_k = Jac H = 2y(2x y^2−1)` for every `k` (chain rule). **Not a unit.** Non-Keller, as claimed.

**`N=4`.** Substitution `x=U−V^k`, `(U−V^k) y^4 − y^2 − V = 0`. At generic `(U,V) ∈ {(3,5),(7,11),(−2,3)}` this is squarefree of degree 4 in `y` (discriminant nonzero) for `k=1,2,3`. Geometric degree 4.

**Cycle type `1^2 · 2`.** On `H`: `s Y^2 − Y − w = 0` with `Y=y^2`. As `s→0`, `Y_− → −w` (two finite `y` if `w≠0`) and `Y_+ ∼ 1/s`, `y ∼ ± s^{−1/2}` (one 2-cycle). So `a=2`, `μ=2`, `S=1`, `W=2`, `N=a+W=4`. Left automorphism `ψ_k` does not change source cycle type. `[P3]`: `a+W=N`. `(C1)`: `2a=4≥4`. `7.B'`: `μ=2≥2`.

**`(K)`.** Lemma 4.1: `N − a_P = r_P W + K_P`. Generic point of `A_F`: `a_P=2`, `r_P=1`, `K_P=0`. Origin (`V=0`, `U=0`): the specialised equation is `−y^2=0`, one affine point `(0,0)`, so `a_P=1`; with `r_P=1` (smooth curve, next paragraph) `K_P = 4−1−2 = 1 = a−1`. Sum of covering defects is `a−1`. If `(K)` were summed only over *singular points of the curve* `A_F`, the sum would be `0 ≠ 1`. Producer `KPG:491-496` already scopes this: the match is numerical/combinatorial, and `A_F` is smooth, which MI Prop 6.1 forbids under Keller. Confirmed with that scope.

**`A_F`.** Escape for `H`: `y=t`, `x=t^{−2}+w t^{−4}` gives limit `(0,w)`, so `A_H={U=0}`; then `A_{G_k}={U=V^k}`. Gradient `(1, −k V^{k−1})` never vanishes. Smooth, irreducible, rational, one place at infinity, `n=k`. `H2` *shape*, not Keller.

**Genus.** The `(Y,w)` curve is the conic `α(w+Y)=Y^2(t−βw−α w^k)`, smooth model `z^2=Δ(w)` with `Δ=α^2+4α w(t−βw−α w^k)` of degree `k+1`, squarefree at `(α,β,t)=(3,5,7)` for `k=1..5` (`gcd(Δ,Δ')=0`). Hyperelliptic genus `g_D=⌊k/2⌋ = ceil((k+1)/2)−1`. The fibre is the degree-2 cover `y^2=Y`, so `g_L ≥ 2 g_D − 1 = 2 ceil((k+1)/2) − 3 → ∞`. This lower bound is **not sharp** (see the table); unboundedness does not need sharpness. Fibres irreducible over `QQ`. Two pencils agree.

```text
k   deg(3P+5Q−7)  g (3,5,7)  g (2,11,3)  2g_D−1   N  a  W  S  μ  Jac
1   5             0          0           −1       4  2  2  1  2  2y(2x y^2−1)
2   10            3          3            1       4  2  2  1  2  2y(2x y^2−1)
3   15            4          4            1       4  2  2  1  2  2y(2x y^2−1)
```

Matches `KPG:489`. No listed numerical profile datum bounds `g_L` in the dominant class. The Keller-derived requirement that `A_F` be singular is not a profile datum; it is `OPEN[SING-WITNESS]`.

---

## 6. Item (f) — `NOETHER-K` alone, and what “alone” means

**Verdict: CONFIRMED as a theorem about one identity.** **GAP** if promoted as “the only remaining Keller input is the polar tree”.

NVM’s scope note (`NVM:640-642`, replayed at `KPG:524-527`): the families that send `Z·K_X → +∞` at fixed `N` “work” because of the affine ramification term `Z·R_aff`, which Keller kills. That diagnosis is quantitatively false in NVM’s own family (B).

General ramification pairing (`NR:220`, `KPG:299-302`):

```text
2g_L − 2  =  Z·R_aff + n(W−S) − N − κ.
```

In family (B), two independent computations give `Z·R_aff = N−1` (fibre: one affine point `w=0` with `ord(w)=m`, contribution `m−1`; branch: `Jac = m x y^{m−1}`, `{y=0}` maps with degree 1 onto a line, `{x=0}` is contracted). The divergent piece is `n(W−S)=k(m−1)`, linear in `k`. Deleting a term bounded by `N` from a quantity that diverges linearly in `k` leaves a quantity that still diverges linearly in `k`. Equivalently, the hypothetical Keller substitution `R_aff=0` *keeping the same* `(n,W,S,κ)` still has `2g−2 = k(m−1)−m−gcd(k−1,m) → ∞`.

**What “alone” is.** The only use of `Jac F ∈ C^*` in NVM’s intersection ledger is `R_aff=0`, which converts the general pairing into `NOETHER-K` `Z·K_X = −2N −κ + n(W−S)`. That identity does not bound `n(W−S)` or `Psi`. Combined with FORK-GENUS, `n(W−S) = 2N − Lambda + Psi`, so `NOETHER-K` rewrites the ceiling as a bound on fork mass and does not supply one. This is a theorem about this ledger.

**What “alone” is not.** Keller also forces: étaleness on fibres (UNIT-SPEED, a wash); smoothness of `C_L`; singularity of `A_F` (the residue PROFILE-WITNESS does not match); and whatever constraints étaleness plus `Pic(A^2)=0` impose on the *shape* of `T_+`. The producer’s “only place left in the ledger is the polar tree” (`KPG:538-539,601-604`) is true **inside the NVM pairing ledger**. It is not a theorem that every other Keller consequence is useless. `OPEN[SING-WITNESS]` is exactly the other door, and a `NO` there would localise the ceiling in the singularity requirement rather than in `Psi`.

The correction kills “Keller minus `R_aff` is already a ceiling”. A successor that treats it as licence to ignore `A_F`-singularity is over-reading. Both doors stay open (§9).

---

## 7. ATYPICAL-LEDGER and the `N=4` control

`A_F`-bar is dominated by dicriticals `≅ P^1`, hence rational when irreducible. Projection from generic `z_u∈L_∞` is degree `n`; RH gives ramification `2n−2`, of which `n−1` sits at the unique place at infinity, leaving `τ + Σ(mult_P−r_P)=n−1` (`KPG:358-367`). Suzuki `Σ λ_c = nW−N+1` is the same identity. Vanishing cycles: `H_1(A^2)=0` plus `Σ λ_c=b_1(C_gen)` is tight; no inequality (`KPG:375-382`). At `N=4` (B3), `n=4` forces `(g,θ)=(0,2)`, `b_1=5`, `τ=2`, `Σλ=5`. Agrees with `KPG:384-396`.

---

## 8. FALLACY-v2

Flag/place/series: `n`, `D`, `N`, `θ_inf`, `θ_L`, `κ`, `g_L`, leaf-mass `Lambda`, NVM-`Lam`, `Psi`, `T` never identified; `θ_inf=κ` is Proof 1. No exit price, no `charge_basis`. Tree double sum charges each `T_+` edge once to each end. `CH1`/`CH2` carry hypotheses; Sec 5 maps are declared non-Keller; no `FULL_ACTUAL_EXIT`. Identities versus floors are labelled; PROFILE’s `2g_D−1` is a floor, not attained at `k=2,3`. `div(dv)` is split by vertex class before any pole identity. Ring map §0; image check `x=U−V^k`; two pencils. `sat()` unused; unit-ideal test `reduce(1,I)=0` for the submersion critical ideal, expected in advance. No ceiling filled by cap or by the automorphism case (`Z·K_X=−3` is Noether).

---

## 9. Typed verdict block

```text
LANE     KELLER-PENCIL-GENUS-REVIEW
SCOPE    Hostile gate of KPG. Keller+H2 where claimed; Sec 5 witnesses
         are non-Keller. Case (A) EMPTY, A2, Z(G) untouched. No exit price.

CONFIRMED  UNIT-SPEED (div/RH/wash; repair KPG:145); GENUS-DEFECT;
  FORK-GENUS with Lambda as KPG:257-259 (auto Psi-Lambda=-2; (x,xy^m)
  same; N=4 (B3) Lambda-Psi=4); ESCAPE-KAPPA Proof 1; SHARP-CHAU
  D>=nS+kappa; POLAR-DEGREE (Keller+H2); CH1/CH2 translations;
  N=2W kill as CONDITIONAL (n>=4 vs n<=3); ATYPICAL-LEDGER;
  NEG-GENUS (CAS (2,2),(2,5),(3,4) and 15-grid); PROFILE-WITNESS
  (N=4, 1^2.2, Jac=2y(2xy^2-1), g=0,3,4 at k=1,2,3, non-Keller);
  NOETHER-K alone cannot bound Psi.

GAP      KPG:145 "deg(pole part)=N" -> sum e_P=N; algebraicity converse
         of UNIT-SPEED not proved; Proofs 2-3 of ESCAPE-KAPPA are
         Keller+H2 corollaries (KPG:218-224); "alone" does not close
         OPEN[SING-WITNESS].

REFUTED  no theorem of KPG. NVM scope note "what makes them work is
         Z.R_aff" is quantitatively false in family (B): Z.R_aff=N-1
         constant, 2g-2 diverges. (Producer's correction, confirmed.)

MEASURED Singular genus, pencils (3,5,7) and (2,11,3): NEG-GENUS 15/15
         +5 alt; family (A) 5/5; auto k=2..5; (x,xy^m) m=1..5;
         PROFILE k=1,2,3 both pencils; submersion b=2..6; four
         genus() controls. 0 mismatches. sympy: Jac, N, A_F smooth,
         CH1/CH2 on nine N=2W pairs, NVM kappa/Z.K_X 15/15.
         Submersion critical ideal unit, b=2..5 (dim=-1, NF(1)=0).

OPENS    OPEN[FORK-MASS]: integer Psi-Lambda=Z.K_X+kappa=2g_L-2-N+kappa
         (Lambda>=2, 1<=kappa<=N, Psi>=0). Bound => n(W-S)<=2N+f(N).
         FALSE for general dominant maps (family (B)).
         OPEN[POLAR-CHAIN]: # of valency>=3 vertices of T_+, in
         [0,#L~-2]. YES=>CH1. At N=4 (B3): Lambda-Psi=4, Psi>=3 if
         E_0 a leaf.
         OPEN[SING-WITNESS]: pair (n, delta_aff) of a fixed-N family
         with g_L->infty and A_F SINGULAR. Second door, not hygiene.

PROMOTION  Promote GENUS-DEFECT, FORK-GENUS (KPG:257-273 Lambda),
         ESCAPE-KAPPA on Proof 1, D>=nS+kappa, POLAR-DEGREE,
         CH1/CH2 as conditionals, ATYPICAL-LEDGER, NEG-GENUS,
         PROFILE-WITNESS with the smooth-A_F gap, the NVM ANTICANON
         correction. Do not promote an unconditional ceiling, any
         cell EMPTY, the UNIT-SPEED converse, "three independent
         proofs" of general-dominant ESCAPE-KAPPA, or "polar tree
         is the only remaining Keller input". Successor: run
         OPEN[POLAR-CHAIN] at N=4 and OPEN[SING-WITNESS] in parallel.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30809`.
- Body SHA-256:
  `b69033c3973febf0cd4e96217ee26a4fc3848a7ab90f1d494b47e9383d15bee1`.
- Frozen basis: `bb536b3ec38e3fbdc722bba4c23fdbc2b956a60f`.
