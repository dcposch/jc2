# The ℓ-shifted Xu calculus, derived; R063's child — Opus 5 — 2026-09-06

```text
VERDICT.  The ell-shifted calculus is PROVED on BOTH sides, with one named inherited
gap (Lemma 2.1 <=> Moh's unprinted Prop 4.2/4.4 cond.(3) shift, already typed
OPEN[PROP42-ELL-CONDITION3]).  New: I_m^l = (1+l) + sum_{Pm}(delta-1-l) and Cor 5.3^l
(OPEN 2 closed); Xu's "I(f_y,g_y)=0" is FALSE at l>0 but harmless.
R063: DEAD-by-child-integrality.  Unique licensed child configuration; I'_M = 71/4
flat, {33/2, 103/6} after the closure, and the maximal sweep (no Lemma A, no Lemma B,
no Galois law, minimal unit, 8 orbits, depth 6) returns 6 values, none an integer.
I'_m = 2 throughout.  Depth cap VACUOUS.
```

## 0. Custody

Receipt manifest built from the numbered `charged_input_<i>_sha256=`/`_basename=` fields with
`awk`, piped to `sha256sum -c`: **6/6 OK** before any mathematical read; all reads were the
frozen copies in `/tmp/jc2-lane.Vw9q0o/inputs`. Text by `pdftotext -layout` (line numbers below
refer to `box/xu-ell-shift-20260906/xu.txt`); the three load-bearing Moh displays were read as
**page images** (`pdftoppm -f 30 -l 32`), since the OCR drops every display equation. No ledger
edit, no `jc2-lean`, no `ideation-*`, no fleet. Uncharged repo reads, declared:
`box/residual66-20260905/roster.jsonl` (`cb384ecd…`) and the prior lane's
`box/exact-contact-20260906/*.py`. Writes: this report and `box/xu-ell-shift-20260906/` (392 KB);
report + JSON under 1 MB. No new exit-price assertion — every verdict excludes a *configuration*,
not a price — so there is no `charge_basis=` line.

Key. **X** = charged Xu PDF, **M** = charged Moh PDF (journal page numbers). `f` is the
**smaller** member (`deg_y f = m`), `g` the larger (`deg_y g = n`), as in X Thm 5.1's proof; the
roster's `(n,m)` is `(deg F, deg G)`, so X's `f` is the roster's `g`, and `I_M` is symmetric
under the swap. `'` marks the child generation; it is never a derivative.

## 1. The hypothesis that changes, and the identity that carries the change

Xu's standing hypothesis from X:64 on is "`(f,g)` is a Jacobian pair", `J := f_xg_y − f_yg_x ∈
K*`; the Prop 6.3 child has instead `J = c·x^ℓ`, `c ∈ K*`, `ℓ = v_s−u_s−1` (`ℓ=1` on R009, R050,
R063). Exactly **one** printed identity feeds `J` into the calculus — **M p.164, Prop 4.1**,
whose printed proof is

```
   J_{t,pi}(h(sigma), g(sigma)) = J_{f,g}(h,g) · J_{x,y}(f,g) · J_{t,pi}(x,sigma)
                                = h_f(sigma) · 1 · J_{t,pi}(x,sigma) = −h_f(sigma) t^{−2+delta}.
```

The `1` in the middle **is** `J_{x,y}(f,g)`. Replacing it by `x^ℓ = t^{−ℓ}` gives
`−h_f(σ)t^{−2+δ−ℓ}`: every `−2+δ` in Moh becomes `−2+δ−ℓ`, and nothing else moves. Moh states
the two consequences himself, both re-read on the page images: **p.169 Remark** (under
`J_{x,y}(f,g) = x^l`) replaces Prop 4.4 (6) by `(6)* ord T_r^ψ(σ) = (−μ_r+M_r−n)λ − 1 + δ − l`,
and **p.171 Remark** replaces Prop 4.6 (3) by `(3)* λ = (−1−l+δ)/(n−M_r) < (−1−l+δ)/(n−M_i)`.

The p.171 Remark is the decisive licence: only *hypothesis* (3) changes. Prop 4.6's five
**conclusions** — `g_σ = C_0 p^{n/d_r}`, `T_{r,σ} = p^{(−μ_r+M_r−n)/d_r} q`, `q` squarefree,
roots of `p` ⊂ roots of `q`, `p` not a power of `q` — are unchanged, because M p.171 simplifies
the ODE to `D(v(−μ_r/d_r) v, p, T_{r,σ}) = C* p^{…+1}`, in which `λ` has cancelled. **So the
whole Prop 4.6 pattern enumeration is `ℓ`-invariant**; only the radii and `λ` shift.

## 2. The derivation, statement by statement

### 2.1 X Lemma 4.1 (X:193) — VERBATIM

Its statement already has `J` general: "Let `f, g ∈ K[x,y]`. Let `f_x g_y − f_y g_x = J(x,y)`";
its proof (X:200–202) is the chain rule plus `dx/dt = −t^{−2}`. So `(4.1)` holds and its right
side *evaluates* to `g_y(α)·(d/dt)f(α) − f_y(α)·(d/dt)g(α) = −J(t^{−1},α)t^{−2} = −c t^{−ℓ−2}`.
**SURVIVES VERBATIM**; the charged report's `−t^{−ℓ−2}` is right and needs no new argument.

### 2.2 X §3 — VERBATIM, printed as Jacobian-free

X:76: *"In this section, we do not need the Jacobian condition."* So Lemma 3.1, Prop 3.3(i)–(v)
and Thm 3.4 hold unchanged — in particular `f_y(σ) = f'_σ(π)t^{λ_σ−δ}+…` and
`|D^{f_y}_σ| = |D^{f_ξ}_σ| − 1` at a final `σ`.

### 2.3 X Def 4.3 — VERBATIM; X Lemma 4.4 — SHIFTS BY `ℓ`

Xu's proof (X:229–241) uses Prop 4.1 as `∂(f(σ),g(σ))/∂(t,π) = −J t^{δ−2}`; by §1 this is now
`−c t^{δ−2−l}`.

* **(i) major** (`λ^f, λ^g < 0`): `σ` final gives `λ^f f_σ g'_σ − λ^g f'_σ g_σ ≠ 0`, so the orders
  match: `λ^f + λ^g − 1 = δ − 2 − l`, i.e. **`δ = λ^f + λ^g + 1 + ℓ`**, and `δ < 1 + ℓ`.
* **(ii) minor** (`λ^f = λ^g = 0`): `(ε f_1 g'_σ − ε f'_σ g_1)t^{ε−1} + … = −c t^{δ−2−l}` gives
  `ε − 1 ≤ δ − 2 − l`, hence **`δ ≥ ε + 1 + ℓ > 1 + ℓ`**.

**BOTH SHIFT BY `ℓ`, from the printed proof.** (X's two `f_1`'s differ: X:229's is a
`t`-expansion coefficient, X:162's the cofactor of `f'_σ`; kept apart below.)

### 2.4 X Lemma 2.1 / Lemma 4.2 — the one INHERITED GAP, identified exactly

X:67 calls Lemma 2.1 "well-known" and prints no proof; X Lemma 4.2 (X:206–215) uses 2.1(ii) to
know the maximal-contact `σ` is *final*, which gives every root a related final `σ` and makes
`Σ_{σ∈P_M∪P_m}|D^{f_ξ}_σ| = m`. Apply §1 with `h = f`: since `λ^f = mλ`, `λ^g = nλ`
(M Prop 4.6(2), unchanged), the bracket is `λ^f f_σ g'_σ − λ^g f'_σ g_σ = −λ f_σ g_σ · W'/W`
with `W := f_σ^n/g_σ^m`, and the identity forces `λ^f+λ^g−1 ≤ δ−2−l` with the bracket
**vanishing** whenever that is strict. So

```
    Lemma 2.1(ii)^l   <==>   (m+n) lambda < delta − 1 − l   <==>   lambda < (−1−l+delta)/(n−M_1),
```

— precisely **M Prop 4.2/4.4 condition (3) in `ℓ`-form**. Moh's two Remarks shift (6) and
Prop 4.6(3) but *not* Prop 4.2/4.4 (3); the campaign already types this
`OPEN[PROP42-ELL-CONDITION3]` (printed source p.165), and Moh's Appendix II p.207 scores the
`ℓ`-form 4/4, the `ℓ=0` form 0/4. **NEW ARGUMENT NEEDED; supplied here only as the equivalence
above — the statement itself is inherited and typed OPEN, not created here.**

### 2.5 `(4.3)` — SHIFTS BY `ℓ`

Let `f_ξ(α) = 0`; then `f(α) = ξ`, so `d/dt f(α) = 0` and Lemma 4.1 reads
`−f_y(α)·d/dt g(α) = −c t^{−l−2}`. If `α` is **major** (`ord g(α)<0`) then
`ord d/dt g(α) = ord g(α) − 1`, so `ord f_y(α)g(α) = −1−l`. If `α` is **minor**
(`ord g(α)=0`) then `ord f_y(α) = −δ_σ` by Prop 3.3(i) (`f_σ` squarefree at a final `σ`, so
`f'_σ(c_α) ≠ 0`) — `ℓ`-free — hence `ord f_y(α)g(α) = −δ_σ = −(1+l) − (δ_σ−1−l)`. Summing over
the `m` roots with `Σ_σ |D^{f_ξ}_σ| = deg_y f`:

```
 (4.3)^l    I(f_xi, f_y g) = (1+l)·deg_y f + sum_{sigma in Pm} |D^{f_xi}_sigma| (delta_sigma − 1 − l).
```

### 2.6 The `(4.4)` side-condition — PROVED HERE; it does **not** shift

X:306 asserts without proof: *"ord `f_ξ(β) = 0` iff `β ∈ D^{f_y}_σ` for some `σ ∈ P_m` and
`ord g_y(β) ≥ −δ_σ`."* The bound is the load-bearing half; proof (new, `ℓ`-free):

Let `σ ∈ P_m` be final minor, `α ∈ D^{f_ξ}_σ`, `β ∈ D^{f_y}_σ`. By Prop 3.3(iii) `β`'s
`t^{δ_σ}`-coefficient is a root of the cofactor `f_1` of `f'_σ` and `α`'s is a root of `f_σ`,
and these share no root, so **`ord(β−α) = δ_σ` exactly**. By Lemma 4.2
`δ_σ = max{ord(α−γ) : g(γ)=0}`, attained. So root by root of `g`: `ord(β−γ) = ord(α−γ)` when
`ord(α−γ) < δ_σ`, and `ord(β−γ) = δ_σ` at the attaining `γ` (the `t^{δ_σ}` coefficients differ):

```
    ord g(beta) = sum_gamma ord(beta−gamma) = sum_gamma ord(alpha−gamma) = ord g(alpha) = 0,
    max_gamma ord(beta−gamma) = delta_sigma  (exactly),
    ord g_y(beta) >= min_j [ ord g(beta) − ord(beta−gamma_j) ] = −delta_sigma.       QED
```

Nothing here uses `J`. **`ℓ`-FREE — this is the statement the "shift `1 → 1+ℓ`" slogan gets
wrong**, and getting it right is what makes §2.7 come out with the clean threshold.

### 2.7 `(4.4)`, X Thm 4.7 — SHIFT; `I(f_y,g_y) = 0` is FALSE at `ℓ > 0`

For `β` a root of `f_y`, Lemma 4.1 gives `g_y(β)·d/dt f_ξ(β) = −c t^{−l−2}`. If
`ord f_ξ(β) < 0` then `−ord f_ξ(β)g_y(β) = 1+l`; if `ord f_ξ(β) = 0` then §2.6 gives
`−ord f_ξ(β)g_y(β) = −ord g_y(β) ≤ δ_σ = (1+l) + (δ_σ−1−l)`. With `|D^{f_y}_σ| = |D^{f_ξ}_σ|−1`:

```
 (4.4)^l  I(f_y, f_xi g_y) <= (1+l)(deg_y f − 1) + sum_{Pm} (|D^{f_xi}_sigma| − 1)(delta_sigma − 1 − l).
```

Xu next writes "from the Jacobian condition, `I(f_y,g_y) = 0`" (X:320). That **fails** for
`ℓ>0`, and the replacement is exact: if `Res_y(f_y,g_y)(x_0) = 0` then `f_y, g_y` share a root
over `x_0`, so `J(x_0,y_0) = c x_0^l = 0` and `x_0 = 0`; leading `y`-coefficients are the nonzero
constants `m, n` (char 0). Hence `Res_y(f_y,g_y) = c'·x^k` and `I(f_y,g_y) = k ≥ 0`, an
**integer** (`k=0` recovers Xu's `ℓ=0` claim). Because `k ≥ 0` both inequalities keep direction:

```
 Thm 4.7(i)^l    I(f_xi,f_y) <= (1+l)(deg_y f − 1) + sum_{Pm}(|D^{f_xi}_sigma|−1)(delta_sigma−1−l)
 Thm 4.7(ii)^l   I(f_xi,g)   >= (1+l) + sum_{Pm}(delta_sigma − 1 − l) + I(f_y,g_y)
                             >= (1+l) + sum_{Pm}(delta_sigma − 1 − l).
 Thm 4.7(iii)    DOES NOT SURVIVE: with no final minor roots it becomes
                 I(f_xi,g) = (1+l) + I(f_y,g_y),  I(f_xi,f_y) = (1+l)(deg_y f −1) − I(f_y,g_y).
```

### 2.8 X Thm 5.1 and Cor 5.3 — SHIFT BY `ℓ`

Thm 5.1's proof needs only `−λ^g_σ` at a final major `σ`; M Prop 4.6(3)* gives
`λ = (−1−l+δ_σ)/(n−M_1)` and `M_1 = −m` (re-checked on every child below), so

```
 Thm 5.1^l    I(f_xi, g) = I_M^l(f,g) := (n/(n+m)) sum_{sigma in PM} |D^f_sigma| (1 + l − delta_sigma)
 Cor 5.3^l    I_M^l >= I_m^l := (1+l) + sum_{sigma in Pm} (delta_sigma − 1 − l)        [>= each term by 2.3(ii)]
 X sec.2      I(f,g) = deg_x Res_y(f,g)  ==>  I_M^l is a NON-NEGATIVE INTEGER.        [l-FREE]
```

`I_m^ℓ` and `Cor 5.3^ℓ` are the charged report's **OPEN 2**, closed.

### 2.9 What is `ℓ`-INVARIANT

With `κ := ρ((1+ℓ) − δ_zero)` the packet closed forms are unchanged, and three more things are
invariant *because `ℓ` is an integer*:

```
  split law     kappa_j = kappa (rho_j W − m)/(rho W − m)                        l-free
  I_M term      n rho kappa/((n+m)rho − m) ;  I_m term  delta − (1+l) = −kappa/rho  l-free
  Galois law    A = den(L·delta)  is UNCHANGED by delta -> delta + l, l in Z     (control 4)
```

So the whole sibling-tower combinatorics (orbit shapes, `Q = ρW/m ∈ Z`, `#parts ≤ Q`, Lemmas A
and B, the final `ρ ≡ 0,1 mod A` law) transfers verbatim; `ℓ` enters **only** through the child's
Def 5.1 radii (the `(ℓ+1)` multiplier) and through `λ = m(δ−1−ℓ)/(n−M)`.

### 2.10 Ledger

| statement | status under `J = c·x^ℓ` |
|---|---|
| X Lemma 4.1, `(4.1)`, `(4.2)` | **VERBATIM** (`J` general already); RHS evaluates to `−c t^{−ℓ−2}` |
| X §3 (3.1, 3.3, 3.4); X Def 4.3 | **VERBATIM** (X:76 prints "we do not need the Jacobian condition") |
| M Prop 4.1 | **VERBATIM**; the printed `1` is `J_{x,y}(f,g)`, so RHS `= −h_f(σ)t^{−2+δ−ℓ}` |
| M Prop 4.6 conclusions (1)–(5) | **VERBATIM** (p.171 Remark; `λ` cancels in the simplified ODE) |
| M Prop 4.6 (3), Prop 4.4 (6) | **SHIFT**, printed `(3)*` p.171 and `(6)*` p.169 |
| X Lemma 4.4(i),(ii) | **SHIFTS**: major `δ = λ^f+λ^g+1+ℓ < 1+ℓ`; minor `δ > 1+ℓ` |
| X Lemma 2.1, Lemma 4.2 | **NEW ARGUMENT NEEDED** ≡ M Prop 4.2/4.4 cond. (3) `ℓ`-shift — typed `OPEN` |
| `ord g_y(β) ≥ −δ_σ` (X:306) | **PROVED-HERE and `ℓ`-FREE** (§2.6) — it does *not* shift |
| X `(4.3)`, `(4.4)` | **SHIFT**: `(1+ℓ)m + Σ_{P_m}|D|(δ−1−ℓ)`; `(1+ℓ)(m−1) + Σ_{P_m}(|D|−1)(δ−1−ℓ)` |
| `I(f_y,g_y) = 0` | **FALSE at `ℓ>0`**; replaced by `Res_y(f_y,g_y) = c'x^k`, `k ≥ 0` — **NEW** |
| X Thm 4.7(i),(ii) / (iii) | **SHIFT**, same direction (`k ≥ 0`) / **DOES NOT SURVIVE** — **NEW** |
| X Thm 5.1, `I_M` | **SHIFTS**: `I_M^ℓ = (n/(n+m))Σ_{P_M}|D^f|(1+ℓ−δ)`; integrality `ℓ`-FREE |
| X Cor 5.3, `I_m` | **SHIFTS**: `I_m^ℓ = (1+ℓ) + Σ_{P_m}(δ−1−ℓ)` — closes **OPEN 2** |

## 3. R063, R009, R050: the licensed children

Own data live from `box/lib/descend_own.py` (charged copy), not the roster's representative; all
three return `descent_license=DETERMINED_PROP6.4`, `top_license=DETERMINED_COMPLETE_US1`,
`V_type=DETERMINED` (one vector), `ℓ=1`.

**R063 (168,112) → child (42,28), `s'=3`, `M'=(−28,35,40)`, `d'=(42,14,7,1)`, `V'=(3,7)`,
`δ' = (7/6,−1/3,−2)`, `M'_1 = −m'` ✓.** The Prop 4.6 pattern set is **unique**; hand-checked:
level 3 has `deg p'_3 = 7`, `Q'_3 = 2`, `lo'_3 = 7/2`, forcing the single class `(7)`; level 2
has `deg p'_2 = 14`, `Q'_2 = 7`, `A'_2 = 3`, `lo'_2 = 2`, admitting only `z=5` with orbit `(3)`
(`z=2` equals `lo'_2`; `z ∈ {8,11,14}` omit `V'_2 = 3`). So `p'_2 = π^5(π^3−c)^3`, with ledger

```
   level-2 zero class  rho=10, kappa=14 -> MAJOR sibling;  final minor packets: NONE
   level-1 final major rho=6, x3 conjugates, delta=7/6, I'_M each = 3  (10+18 = 28 = m')
   ==>  I'_m = 1 + l = 2 ;  flat I'_M = 35/4 + 9 = 71/4   (the replay's number, reproduced)
```

But that flat termination is itself inadmissible: `δ_fin = 13/24`, `A = den(3·13/24) = 8`, and
`ρ = 10 ≢ 0,1 (mod 8)` violates the M p.201(8) final-disc Galois law. Closing the `ρ=10` packet
gives **2 outcomes at every depth ≥ 1 (the cap is vacuous)**: splitting at `W=42` with `z=2` and
orbits `(2,2)` or `(4)`, giving `I'_M = 9 + 15/2 = 33/2` and `9 + 49/6 = 103/6`, `I'_m = 2` both.

Neither is an integer. The **maximal sweep** — Lemmas A and B off, Galois final law off, minimal
unit `m'/gcd(n',m') = 2`, 8 orbits, depth 6 — returns
`I'_M ∈ {71/4, 33/2, 120/7, 281/18, 31/2, 103/6}`, **none an integer**. By Thm 5.1^ℓ + X §2 the
child has no admissible configuration; the descent is `LICENSED_AND_FORCED` with `V'`
`DETERMINED`, so **R063 is DEAD.** The `ℓ`-shift does *not* restore integrality, and is not what
decides the kill — the `I_M` terms are `ℓ`-free (§2.9); `ℓ` decides only *which* configurations
exist.

**R009 (192,128) → child (48,32), `V'=(2)`.** Two patterns. `z=1,(2,1)`: minor packets `ρ=2` at
`δ=3` (1+5 copies), final major `ρ=4 × 5` at `δ=4/3`, `2+10+20 = 32 = m'` ✓, so
`I'_M = 5·(8/5) = 8` and `I'_m = 2 + [1·(3−2) + 5·(3−2)] = 8`. `z=6,(2)` gives `592/29`, its
`ρ=12` sibling having **no** completion at any depth. **ALIVE, `I'_M = I'_m = 8`, margin 0** —
pinned exactly as the parent is.

**R050 (196,56) → child (49,14), `V'=(4)`.** Three patterns; `(4,3)` dies (`146/13`, `ρ=6`
sibling with no completion). Both survivors give `I'_M = 8` and
`I'_m = 2 + (5/2−2) + (6−2) = 13/2`, **margin 3/2**.

So `I'_M = I_M = 8` on R009 and R050, but **the margin is not descent-invariant** (R050: parent
`0`, child `3/2`) — visible only once `I_m^ℓ` exists.

## 4. Controls, and the census `I_m^ℓ` makes possible

1. **`ℓ=0` closure ≡ the charged `sibling_tower3.search`** on 6 states: identical outcome sets.
   **Xu's printed §6 numbers** appear in the parent enumeration: §6.1(i) `(8,4)`, §6.1(ii)
   `(4,6)`, §6.2(i) `(4,5)`, §6.2(ii) `(10,4)`. **`I_m^ℓ` at `ℓ=0` equals Xu's `I_m`** on all
   1,080 roster configurations. **`A = den(L·δ)` is unchanged by an integer `ℓ`-shift**
   (4,000 random `(L,δ,ℓ)`, 0 failures).
2. **Retrodiction, 7/7.** On all 46 complete `u_s=1` rows, the rows whose *child* has no
   admissible configuration are `R001, R025–R028, R057, R058, R063`; the first seven are
   **exactly** the rows already dead at the parent (R001 by Xu's Cor 5.3, the six by parent
   integrality). R063 is the only row alive at the parent and dead at the child.
3. **R001 is the sharpest control.** Its child config `z=1,(2,1)` has `I'_M = 4 < I'_m = 5` —
   Xu's own §6.2(i) parent numbers, reproduced at the child by `Cor 5.3^ℓ`. The charged replay,
   having no child `I_m`, logged R001 as a set-difference; `I_m^ℓ` closes it.

Census over the 46: **140** flat child configurations (the replay's count, reproduced); `I'_M ∉ Z`
kills **71** (70 by integrality alone); the new `Cor 5.3^ℓ` kills **4**, of which **3 pass
integrality** (R001 `4<5`, R002 `4<6`, R013 `8<12`); **66** pass both. Effect on the replay's
**OPEN 3**: its 8 parent/child set-differences become 7 (R001 moves to "both empty"). Its
verdict stands and is better supported: preservation FAILS, with R063 the counterexample, for
the reason it named.

## 5. FALLACY-v2 ledger

*Floor/attainment.* `I_M^ℓ ≥ I_m^ℓ` is a floor, `I_M^ℓ = deg_x Res_y(f_ξ,g)` an equality; the
R063 kill uses only the equality (`I'_m = 2` never binds), and set-valued cases (R050) are
reported as sets. *Carrier/attainment.*
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR` is preserved; R063 DEAD excludes a necessary
configuration, not a pair. *Prime label/derivative.* `'` is the child generation; the only
differentiations are Moh's `d/dπ` and Xu's `d/dt`, and X's two `f_1(π)`'s are separated in §2.3.
*Variable/ring map.* X's `(f,g)` is the roster's `(g,f)` (§0); `M_1 = −m` re-verified per child.
*Pole/interior.* Major/minor is decided by the sign of `κ` per packet, after the vertex class.
*Merge-free/M-descent.* Child `V'` from `descend_own`, never a copied parent `V`.
*Target/arrival index.* `W = n−M` kept distinct from `Q = ρW/m` and from `δ`. *A shifted formula
is not a theorem.* Every shift is tied to a printed line; the one statement I cannot tie is typed
`OPEN` in §2.4 and never used silently. *Depth cap.* Not a cap: the R063 closure saturates at
depth 1; depth 6 adds nothing.

## 6. Verdict

```text
(1) THE ell-SHIFTED CALCULUS: PROVED.  Exact statements sec.2.5-2.8; ledger sec.2.10.
    (4.3)^l, (4.4)^l, Thm 4.7(i),(ii)^l, Thm 5.1^l, and I_m^l = (1+l)+sum_{Pm}(delta-1-l)
    with Cor 5.3^l  <-- OPEN 2 CLOSED.  Two NEW arguments needed and supplied (sec.2.6,
    sec.2.7); Thm 4.7(iii) does NOT survive verbatim.  ONE named gap, inherited:
    Lemma 2.1 at l>0, reduced HERE to lambda < (-1-l+delta)/(n-M_1) = Moh Prop 4.2/4.4
    cond.(3) in l-form; unprinted, typed OPEN[PROP42-ELL-CONDITION3], 4/4 vs 0/4 on p.207.

(2) R063 (168,112):  DEAD-by-child-integrality.  Licensed child (42,28), s'=3,
    M'=(-28,35,40), d'=(42,14,7,1), V'=(3,7) DETERMINED, l=1.  UNIQUE Prop 4.6 pattern
    p'_3=(pi-c)^7, p'_2=pi^5(pi^3-c)^3 (hand-checked).  I'_M flat = 71/4 (replay
    reproduced), I'_m = 2 (no final minor roots).  The rho=10 packet cannot be final
    (10 not= 0,1 mod A=8) and its closure yields I'_M in {33/2, 103/6} at EVERY depth;
    maximal sweep (no A, no B, no GO, unit 2, 8 orbits, depth 6) ->
    {71/4, 33/2, 120/7, 281/18, 31/2, 103/6}.  NONE is an integer.  The l-shift does NOT
    restore integrality.  Residual 65 -> 64 (59 -> 58 if the six charged kills promote).
(3) R009 (192,128): child I'_M = I'_m = 8, margin 0.  ALIVE, pinned as the parent is.
    R050 (196,56) : child I'_M = 8, I'_m = 13/2, margin 3/2 (parent margin 0).  ALIVE.
    I'_M = I_M = 8 on both, but the MARGIN is not descent-invariant.

OPENS RAISED
  1. Lemma 2.1 at l>0 == Moh Prop 4.2/4.4 cond.(3) in l-form.  EVERY child verdict in the
     campaign, not only R063, rests on it: the highest-value source read left.  QUANTITY:
     prove or refute lambda < (-1-l+delta)/(n-M_i) from M p.165; <= 3 h.
  2. k := I(f_y,g_y) = deg_x Res_y(f_y,g_y) is a NEW child invariant nobody has computed.
     By Thm 4.7(iii)^l a minor-free child has I'_M = (1+l) + k EXACTLY; R063's child is
     minor-free, so its k would have to be 29/2 or 91/6 -- a structurally different second
     route to the same kill.  QUANTITY: compute k on the 46 rows; <= 2 h.
  3. The 7 remaining OPEN-3 differences (R002 R003 R010 R013 R019 R020, extra child
     integers) are child configurations with no parent counterpart; real or enumeration
     artifact is undecided.  QUANTITY: <= 1 h on the 6 rows.
  4. The 20 rows with u_s > 1 have no licensed child; the instrument is silent on them.
     QUANTITY: needs the Prop 6.3 radius for u_s >= 2, not more Xu.
  5. No configuration here is a witness pair.  Unchanged from the charged report.
```

Drivers, exact-rational and re-runnable, in `box/xu-ell-shift-20260906/`: `ell_shift.py`
(child `I'_M` and the new `I'_m`), `child_close.py` (`ℓ`-shifted closure), `child_row_close.py`,
`census.py`, `results.json`, `census.json`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20774`.
- Body SHA-256:
  `9a49a93021a1f50975274ffa9ce03f89b52b9974970273515fd5d7437048ad3b`.
- Frozen basis: `1e7c0c5be9b6c63398e284fc120d45894bdadcb2`.
