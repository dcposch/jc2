# Opus 5 hostile review — Grok td=8 equal-join `(0,y)` initialization

Lane: Opus 5, different-model adversarial referee. Date: 2026-08-29 UTC.

Target: `xmodel/m2-td8-equal-join-zero-side-initialization-primary-grok46-20260829.md`.

**Lead verdict: `PASS_WITH_REPAIR_AND_NARROWING`** at the formal-treetop scope.

The existence claim (sought outcome 2) survives a hostile re-derivation from
the printed statements, for every integer `t >= 0`, after five repairs. Two
of the target's *negative* claims do not survive: §0's "sought outcome (1)
does not exist at the printed-statement tier" and §7's `i_tr`-transfer
("a negative answer at the reduced pattern kills every `t` at once"). §4.3's
layer count is refuted as stated and replaced by an exact shear identity that
is stronger in one respect and `t`-dependent in another.

---

## 0. Custody — every declared hash recomputed this session

```
741b7198dd06b86ae7a8366163db56b473cd2929964a93a661e626301c84218f  target (full)   MATCH
3d07291357a266225f6e269d876c62dc6a18c7271ac3a730999fede430c696f1  target (body)   MATCH
```

Target body hash reproduced at 25126 bytes = all bytes above its self-hash
line, `rstrip`ped plus one `\n`. Three other plausible split conventions were
tried and rejected; the target is self-consistent.

Declared custody table, all recomputed:

```
fef9de46d1ec1287ebf4e64883394ca851ffb9e799d3b7d588e1daf9e15ab020  prompt                       MATCH  1795
e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61  opus5 transport review       MATCH 26424
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  fable5 exact-lambda review   MATCH 26123
910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4  fable5 transport primary     MATCH 19670
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  opus5 exact-lambda primary   MATCH 32759
9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a  sol56 route family           MATCH  5623
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf         MATCH
```

Printed source re-extracted by me, not taken from the target: pp. 8–10
(Lemma 2.1, Not. 2.3–2.4, St. 2.1, St. 3.1, Def. 3.1–3.2), 11–18 (Not. 3.1–3.14,
Def. 3.3–3.4, Prop. 3.1–3.2, St. 3.4–3.18, Prop. 4.1), 28–33 (Prop. 6.1,
**Thm 6.1**, Not. 6.1, St. 6.1–6.2, Prop. 6.2), 39–44 (Not. 8.1, St. 8.1,
Prop. 8.1, St. 8.2–8.5, Prop. 8.2–8.4), 48–51 (Not. 9.1–9.3, St. 9.1–9.5,
Prop. 9.2, **Prop. 9.3(IV)**). Layout extraction; stacked-fraction hazard
respected by re-reading Prop. 9.3(b)–(m), Prop. 8.1(i)–(v) and St. 3.9(ii)
as displayed blocks.

Independent exact arithmetic: one desk script, `Fraction`/`int` only, 64
values of `t` (`0..59`, `97`, `313`, `1000`, `7919`), 0 failures after the one
correction noted in §2.6. No AWS, no web, no `jc2-lean`, no CAS, no canonical
edit, no commit or push. Only this file was written; scratch in `/tmp/zsi`.

---

## 1. Scorecard

| clause | verdict |
|---|---|
| Case-IV degree equations (i)–(m), all `t` | **CONFIRMED** — exact, and `ν = ν_G` reading independently forced |
| `D_tr = κ_tr d_tr = 17 i_tr` | **CONFIRMED** — and robust: `D_tr = X_tr i_tr` with `X = (dp/dq)·k̄`, `κ`-free |
| Type `(2,3)` numbers and all four Lemma 2.1 inequalities | **CONFIRMED** in `Z[t]` |
| `R = 5/3`, `ψ = 1`, both `t`-free | **CONFIRMED** |
| `p_{(0,y)} = C_R η^{k_f}` | **CONFIRMED** — and it is *printed* (Prop. 8.3(iii) shape) |
| Root-product identity, `μ_R k_f ∈ Z`, exponent integrality | **CONFIRMED** for all `t` — justification mis-cited |
| `(★_R)` coefficient identity, `l_f − k_f = −34 i_tr` | **CONFIRMED with repair** — `d_h` printed wrong (R3) |
| `M*_R = 1`, `i_R = k_f`, `δ_R = 3/5`, `R_R = −2/5` | **REFUTED** (R2) — `M*_R = 5`; `(★_R)` survives because `i_R R_R` is invariant |
| Forced pure-monomial q-side at `(0,y)` | **CONFIRMED and strengthened** — forced by Prop. 8.1(iv) alone, not by interior `β = 0` |
| `β = 0`; twin `(A₁/A₂)² = ω^{−15}`, `(L₁/L₂)`-exponent `−5` | **CONFIRMED as cited**, correctly used as derived rigidity |
| One global tower, one 7-tuple, both attachments; no cycle | **CONFIRMED** — St. 8.3 is edge-local, and edge-locality composes on a tree |
| `C_tr = C_R`, `t_{j,tr} = t_{j,R}`, `B_tr^{k_4} = s_4 C_tr^{l_4}`, six gauges | **CONFIRMED** up to a discrete `k_4`-th root |
| Ten-microstep drop `51 i_tr → i_tr` | **CONFIRMED** exactly (St. 3.17(ii)) |
| "`κ = κ_F = 17`" at `(0,y)`; nine silent `κ_F`-graded layers | **REFUTED** (R4) — `κ_{(0,y)} = 1` by the target's own §3.1 |
| Layer-10 uniqueness from the 7-tuple | **GAP** — true only after importing the reviewed trunk rigidity, which is not a `(0,y)` datum |
| Chart swap `k_f = d_{(0,x)} = deg(p_{(0,y)})` | **GAP, load-bearing** (R1) — printed both ways; the route lives or dies on it |
| §0 "sought outcome (1) does not exist at the printed tier" | **REFUTED** — under the Notation-3.10 reading it exists and is one line |
| §7 `i_tr`-transfer / reduced-pattern stop condition | **REFUTED** (R5) — `i_tr = 1` is not admissible and the condition count is `t`-linear |
| Formal ≠ polynomial-pair realization (§6, §8 firewall) | **CONFIRMED**, and extended |

---

## 2. What I re-derived, independently

### 2.1 `D_F` is `κ_F d_F`, and `D_tr = 17 i_tr` is robust

Notation 3.11 prints `D_{h,F} := κ_F d_{h,F}`, `D_F := D_{f,F}`; Statement 9.1's
proof confirms it (`d_F + d_{g,F} = 1 − u` therefore `D_F + D_{g,F} = κ_F(1−u)`).
So the target's `D_tr := κ_tr d_tr = 17 i_tr` is the printed meaning, and its
use inside Prop. 9.3(k) is correct.

I did not take `d_tr = i_tr` from the target. From St. 8.2's proof,
`deg(p)/deg(q) = δ/(1−u)`, so `δ_tr/(1−u_tr) = 85/35 = 17/7`; with the reviewed
`k̄_tr := κ_tr(1−π(tr)) = 7` this gives

```
X_tr = D_tr/i_tr = κ_tr δ_tr = (deg p / deg q) · k̄_tr = (17/7)·7 = 17
```

**independently of `κ_tr`**. So `D_tr = 17 i_tr` for every `t`, and it does not
depend on the case-IV(i) forcing `κ_tr = ν_tr = 17`. The target obtains the
right number by a route that appears to depend on `κ_tr`; the robust form
should be carried instead.

**Notation collision, flagged for consumers.** The hash-pinned Opus transport
review uses `D_F` to mean `deg(p_F)` (its §2.3 chain `3·i_tr = 336+252t = D_G`,
and its §2.6 `ψ = Q_F/D_F`). That is *not* the printed `D_F = κ_F d_F`. Both
reports are internally consistent; a consumer that mixes them will be off by a
factor of 5 at the trunk (`85 i_tr` vs `17 i_tr`) and will get `d_F = 55 i_tr`
instead of `51 i_tr` out of Prop. 9.3(k). The target reads the printed meaning
correctly and deserves credit for it, but never warns about the collision.

### 2.2 Case IV(i)–(m): confirmed, and the printed `ν` pinned

Printed Prop. 9.3(IV):
`(i) ν_G = κ_G`; `(j) (1−v)κ_G < ν_G`;
`(k) d_F = [D_G + (ν − (1−v)κ_G) deg(p_G)]/ν_G ∈ N`;
`(l) d_F < deg(p_G)`; `(m) d_F M_G/deg(p_G) ∈ N`.

The symbol `ν` in (k) was bound in case (III) as `ν := ν_F`. The target silently
reads `ν = ν_G`. That reading is **forced**, by two independent arguments the
target does not give:

* positivity — `ν_F = 1` by St. 9.2(ii), which gives
  `d_F = [17 i_tr + (1−7)·85 i_tr]/17 = −29 i_tr < 0`, contradicting `∈ N`;
* structure — case IV is case (I)/(II) with `u = 0`, so
  `n = κ_G v = κ_G − κ_G(1−v) = ν_G − (1−v)κ_G` by (i), and (k) becomes (c)
  verbatim with `D_F = d_F` (St. 9.2(i)). Here `n = 17 − 7 = 10`, so
  `π(trunk) = 10/17`.

Exact values (verified for all 64 `t`):

```
d_{(0,y)} = [17 i_tr + 10·85 i_tr]/17 = 867 i_tr/17 = 51 i_tr        (k)
(j)  7 < 17         (l)  51 i_tr < 85 i_tr        (m)  51·5/85 = 3 ∈ N
R = deg(p_G)/d_F = 85/51 = 5/3 = ν_G/(ρ + ν_G − k̄),  ρ = D_G/deg(p_G) = 1/5
ψ = ⌈R⌉ − 1 = 1,   ψ l_f < k_f
```

`R` and `ψ` are `t`-free, as claimed. Case IV(i) additionally forces
`e_{j−1} = κ`, i.e. `j = 1`: the trunk carries the **first** characteristic
exponent `α_1 = 10/17`. The target asserts this; it is genuinely forced, and it
is what kills any `V_{1,a}` point strictly between `(0,y)` and the trunk. The
absence of a `V_{2,a}` point there is *not* derived — it is a property of the
displayed tree. Disclose it as a hypothesis, not a consequence.

### 2.3 Type `(2,3)`: confirmed in `Z[t]`

With `k_f = deg(p_tr) = 85 i_tr` (St. 3.17(i), `p_{(0,y)}` single-rooted) and
`l_f = d_{(0,y)} = 51 i_tr`, `i_tr = 28(4+3t)`:

```
k_f = 2380(4+3t)   l_f = 1428(4+3t)   k_g = 3570(4+3t)   l_g = 2142(4+3t)
k_f/k_g = l_f/l_g = 2/3    k_g/k_f = 3/2 ∉ N*    gcd(k_f,k_g) = 1190(4+3t)
l_f < k_f, k_f < k_g, l_f < l_g, l_g ≤ k_g        α = 2 ≠ 1, β = 3 ≠ 1 (St. 2.1)
```

`k_g` and `l_g` are integral for every `t` (the `3/2` survives because `1428`
and `2380` are even). The target lists only three of Lemma 2.1(iii)'s four
inequalities; the omitted `l_g ≤ k_g` also holds. Notation 2.4 prints
`α/β = k_f/k_g`, which the target quotes correctly.

### 2.4 The `(0,y)` top form is printed, not just derived

The target derives `p_{(0,y)} = C_R η^{k_f}` from Prop. 3.1(**) plus the case-IV
hypothesis `F ∉ V_{1,a} ∪ V_{2,a}`. Sharper: **Proposition 8.3(iii) prints
exactly this shape** — "`p_G(η) = (η − c)^k` for some `k ∈ N*` if `G = (0,y)`",
with `c` unrestricted, so `c = 0` is admitted. And St. 3.18 prints "If `0` is a
root of `p_F`, then `F * 0` exists" with no deck `ε`, so the target's remark
that no `ε` is required is a quotation, not a repair.

Minor citation defect: the target writes `f^+_{(1,1)} = ⊖ x^{k_f} y^{l_f}`.
Lemma 2.1's proof prints `f^+_{(1,1)}(x,y) = x^{k_f} y^{l_f}` with **no** `⊖`
(the constant was already absorbed by the linear change `A`). Harmless — the
target only uses it for the sign-free statement `y → 0` as `x → ∞`.

### 2.5 `(★_R)` is right; three of its inputs are not

Prop. 8.1(iv) with `p = η^{M*_R}`, `u = 0`, and Prop. 4.2(iv) give the vertex
equation at `(0,y)`. Writing `P = C_R η^{k_f}`, `Q = B_R η^{s}` with
`s = k_f(μ_R − 1) + 1`:

```
l_f · P Q′ − d_h · P′ Q = C_R B_R [ l_f s − d_h k_f ] η^{k_f + s − 1}
```

With the **printed** `d_h = (1−u) + (μ_R − 1) d_F = (μ_R − 1) l_f + 1`:

```
l_f s − d_h k_f = l_f k_f(μ_R−1) + l_f − (μ_R−1) l_f k_f − k_f = l_f − k_f
k_f + s − 1 = μ_R k_f
```

so `(★_R): C_R B_R (l_f − k_f) = (∏_{j<m_R} k_j) c_0 T_R`, with
`l_f − k_f = −34 i_tr`. **CONFIRMED, exactly as the target states it.** The
right-hand exponent matches because `μ_R = Σ_{j<m}(k_j−1) l_j/k_j` (Prop. 4.2(iv)),
and `μ_R k_f ∈ Z` because each `k_f (k_j−1) l_j/k_j = (k_j−1) deg(p_{h_j,R})`
is an integer.

Three inputs on the way are wrong and must be repaired (R2, R3 below); the
errors in `i_R` and `R_R` cancel because only the product enters:

```
target:  i_R R_R = 85 i_tr · (−2/5) = −34 i_tr
correct: i_R R_R = 17 i_tr · (−2)   = −34 i_tr
```

`λ_R = δ_R/X_R = 1` under both, since `δ_R = X_R = d_R/i_R` at `κ_F = 1`.

The pure-monomial q-side does **not** need Opus's interior `β = 0`. Prop. 8.1(iv)
alone forces it: with `p = η^5`, `δ = 3`, `1−u = 1`, writing `q = Σ c_j η^j`,

```
3 η q′ − 5 q = R η   ⟹   (3j − 5) c_j = 0 for j ≠ 1,   −2 c_1 = R
```

and `3j = 5` has no integer solution, so `q = B_R η` **uniquely**. (The same
argument under the target's `p = η`, `δ = 3/5` gives `(3j/5 − 1)c_j = 0` and
`j = 5/3 ∉ Z`, so the conclusion is convention-independent.) This is a better
proof than the one given, because Opus's `β = 0` is a statement about *interior*
faces on an edge, not about a vertex, and the target applies it out of scope.

### 2.6 Three printed gates the target invokes out of scope — all harmless

**Statement 8.5.** The target writes "St. 8.5 applies (`trunk° = (0,y) ∉ V_{2,a}`):
`M_R | M_tr`, i.e. `1 | 5`". The conclusion is true, but the printed **proof** of
St. 8.5 opens with "from the assumption `G ∉ V_{2,a}` and from St. 3.18 one has
`p_G(η) = (η^ν − c^ν)^l` for some `c ∈ C*`" — a *nonzero* root. At `G = (0,y)`,
`ν = 1` and the root is `0`, so the proof does not cover this edge. The
conclusion `1 | 5` is vacuous anyway. Contrast the Opus review's gate G1: St. 8.5
is escaped at the interior edges because `Φ_H, Φ_G, Φ_tr` each have two root
orbits (so all three are in `V_{2,a}`); at the trunk edge it is *applicable in
statement* and simply satisfied.

**Proposition 8.4.** The target's escape — "corrected Prop. 8.4 is nonroot-only,
so root `M = 1` is legal" — is not the printed hypothesis. Printed Prop. 8.4
reads: "Assume `T_{a,pole} = {G}`. Then for any `F ∈ T_a^& ∩ V_a` one has
`M_F ≠ 1`." It is a **single-pole** statement, and `(0,y) ∈ T_a^& ∩ V_a` is
squarely inside its scope. The route has **two** poles, so Prop. 8.4 is
inapplicable for that reason, and `M_R = 1` is legal. The escape stands; the
stated reason does not, and I cannot verify the cited "correction" from any
hash-pinned artifact.

**Statement 8.2.** The target's §5 bullet is confused: it writes
`mult(p,0) = k_f` alongside `deg p = 1`, mixing the reduced Prop. 8.1 `p` with
`p_F`. More importantly St. 8.2's proof opens "From statement 3.16, we have that
`p` has more than one root", which fails at `(0,y)`. St. 8.2 simply does not
apply there. No kill either way.

**Statement 8.4 (the other one) corroborates R2.** Printed St. 8.4:
`F, G ∈ V_a ∩ T_a^&`, `G = F + c` ⟹ `mult(p,c) | M_G`, with `p` the *reduced*
polynomial at `F`. At `F = (0,y)`, `c = 0`, `G = trunk`: with my `M*_R = 5` this
reads `5 | M_tr = 5`, **exactly saturated**; with the target's `M*_R = 1` it
degenerates to the vacuous `1 | 5`. Independent evidence that `M*_R = 5`.

### 2.7 The shear identity — what the ten microsteps actually do

The target's §4.3 layer picture is wrong as indexed (R4), but the underlying
object is computable in closed form and is *better* than claimed in one respect.

All ten continuation roots are `0` (forced: any nonzero Puiseux coefficient at
`k/17`, `1 ≤ k ≤ 9`, would give `β_1 ≤ kκ/17 < 10κ/17`, contradicting
`α_1 = 10/17`). So `η_{F_k} = x^{k/17} η_{(0,y)}`, and substituting into
`f^{(0,y)} = Σ_j x^{j} p_j(η)` (integer `j`, since `κ_{(0,y)} = 1`):

```
[η^i] p_{F_k}  =  [η^i] p_{ d_{F_k} + k i /17 }   if 17 | i,     0 otherwise
d_{F_k} = 51 i_tr − 5 i_tr k,   gcd(k,17) = 1 for 1 ≤ k ≤ 9
```

Two consequences, both new relative to the target and to both pinned reviews:

1. **At `k = 10`,** `[η^i] p_tr = [η^i] p_{i_tr + 10 i/17}` for `17 | i`, and `0`
   otherwise. So `p_tr ∈ C[η^{17}]` is **automatic** from the `(0,y)` side — a
   free structural corroboration of `ν_tr = 17` and of the reviewed
   `Φ_tr = (η^{17}−A)^3(η^{17}−B)^2` shape. The corner is exactly saturated:
   `i = k_f = 85 i_tr` gives `j = 51 i_tr = l_f`, the Newton corner `(k_f,l_f)`.
2. **`p_tr` is a diagonal, not a layer.** It reads `5 i_tr + 1 = 140(4+3t) + 1`
   *distinct* layers of `f^{(0,y)}`, along the Newton line `17 j − 10 i = 17 i_tr`.
   The "silent stretch" imposes at most `9 · 5 i_tr = 45 i_tr = 1260(4+3t)`
   scalar vanishing conditions, not nine. Both counts are `t`-linear.

I verified the target's assignment is nonetheless **consistent**: setting all
`(0,y)` layers to zero except the top layer and the trunk diagonal reproduces
`p_{F_k} = C_R η^{k_f}` for `k = 1..9` exactly, because the only index that
could contribute at level `k < 10` would require `i < 0`. So §4.3 exhibits a
legal assignment; it just is not a nine-layer one.

### 2.8 One tower, one 7-tuple, both attachments — confirmed

Printed St. 8.3(i): for `F ∈ T_a^& ∩ (V_a \ {(0,y)})` with `F = G * c`,
`h_{j,F} = h_{j,G}` for `0 ≤ j ≤ m_F`. This is an **edge-local** statement about
honest polynomials `h_j ∈ C[x,y]`, not a branch-local one, and edge-locality
composes along a connected tree. Depths are `m_R = 5 ≥ m_tr = 4 ≥ m_G = 3 ≥
m_H = 2 ≥ m_P = 0`, so `(0,y)` carries the deepest tower and every other vertex's
tower is a truncation of it. Hence one global `(k_j, l_j, s_j)` really does feed
both merge branches. St. 8.3 applies to the trunk edge (`G = (0,y)` is the
*parent*, and only `F = (0,y)` is excluded).

No hidden independent gauge and no cyclic coefficient equation:

* the tree is a tree, so no cycle exists to close;
* `(0,y)` contributes exactly one new equation `(★_R)` and one new gauge `B_R`,
  and `B_R` is genuinely fresh — `m_R = 5` means `h_4` *is* enslaved at `(0,y)`,
  so the tops cancel in `h_5 = h_4^{k_4} − s_4 f^{l_4}` and `B_R` is a
  sub-leading remainder, not a function of `(t_{4,R}, s_4, C_R)`;
* `(★_R)` pins `B_R` downstream-only and never feeds back into
  `(C_R, s_0, s_2, s_3, s_4, c_0)`;
* the genuinely branch-local objects are `A_e`, `c_e`, `r_e`, `ω`, `ε` — exactly
  the ones the reviewed twin law `(A₁/A₂)² = ω^{−15}` governs, and the target
  uses that law correctly as *derived rigidity*, not as a closure condition.

`m_R ≥ m_tr + 1 = 5` is correctly obtained by applying Cor. 6.1's drop at the
**trunk** (`dq_tr = 35 > 1`), which is legal because Cor. 6.1 excludes only
`(0,y)` itself. `B_tr = t_{4,R}` and `B_tr^{k_4} = s_4 C_tr^{l_4}` follow from
St. 3.9(i)(ii) (`a_l = b_l`: the lowest Taylor coefficient at `c` becomes the
child's leading coefficient) applied ten times through pure monomials. So the
7-tuple carries **six** `C*` degrees of freedom, up to a discrete `k_4`-th root.
Confirmed.

### 2.9 Exponent integrality — conclusion right, justification wrong

The `(0,y)` tower exponents are `k_f · l_j/k_j`, and the target justifies them
by quoting the *transport* exponents `i_V · l_j/k_j` from the Opus review
(`i_G·6/7 = 12`, `i_tr·l_3/k_3 = l_3`). Those are different quantities. The
correct values, all integral for every `t >= 0` (verified, 64 values):

```
j=0:  k_f·3/2      = 3570(4+3t)          j=1:  l_1 k_f  (pure shift, any l_1)
j=2:  k_f·6/7      = 2040(4+3t)          j=3:  k_f·l_3/k_3 = 85(635+476t)
j=4:  k_f·l_4/k_4  = Q_tr = 85 k_tr + 35,   k_tr = 39984t² + 106650t + 71117
```

I reproduced `k_tr(t)` coefficient-by-coefficient from
`k_tr = i_tr·79/14 + (k_3−1) l_3`, and the Bezout identity
`3 l_3 − 17 k_3 = 1` in `Z[t]` (equivalently `17 k_3 = 476 ν`, so the Opus
review's two forms `3l_3 − 17k_3` and `3l_3 − 476ν` are the same identity).

---

## 3. Defects — what must be repaired

**R1 (GAP, load-bearing; the biggest thing in this review). The chart swap is
a *reading*, and the source prints it both ways.**

The target's §3.1 asserts as equalities in `Z`:
`k_f = d_{(0,x)} = deg(p_{(0,y)})`, `l_f = deg(p_{(0,x)}) = d_{(0,y)}`.

*For the target:* the printed proof of **Theorem 6.1** says verbatim
"Moreover, `k_f = d_{(0,x)}` and `l_f = deg(p_{(0,x)})`". The printed proof of
**St. 9.4** says "Since `(0,x) ∈ T_a^↗`", which under Not. 6.1
(`T_a^↗ = {d_F > (1−π) deg p_F}`) needs `k_f > l_f` — true only under this
reading. And **Prop. 9.3(IV)** places `(0,y) ∈ T_a^&`, needing `l_f < k_f`, again
only under this reading. Three independent printed anchors.

*Against the target:* Notation 3.2 puts `(0,y)` in `T_{a,y}`; Notation 3.9 gives
`η_{(0,y)} = y`; St. 3.7 expands `h^F(x,η) = Σ x^{j/κ} p_j(η)`; Notation 3.10
sets `d_{h,F} := j/κ` for the top `j`. Since `N_f` sits in the rectangle with
vertex `(k_f, l_f)`, the top `x`-power of `f` is `k_f` with coefficient a
`y`-polynomial of degree `l_f`. That gives `d_{(0,y)} = k_f`,
`deg(p_{(0,y)}) = l_f` — the **opposite**. And it is this reading, not the
target's, that makes the printed St. 3.12 (`d_{h,(0,y)} ≥ deg(p_{h,(0,x)})` and
`d_{h,(0,x)} ≥ deg(p_{h,(0,y)})`) come out as equalities; under the target's
reading St. 3.12 forces `l_f ≥ k_f`, which with Lemma 2.1(iii) gives
`l_f = k_f`, contradicting Theorem 6.1 itself.

**Why this is load-bearing.** Under the Notation-3.10 reading, Prop. 9.3(k)
gives `k_f = d_{(0,y)} = 51 i_tr`, while St. 3.17(i) gives
`l_f = deg(p_{(0,y)}) = deg(p_tr) = 85 i_tr`, so `l_f > k_f` in violation of
Lemma 2.1(iii), **for every integer `t >= 0`, in one line, with no exceptional
residue**. That is precisely a sought-outcome-(1) source-level incompatibility.

**Repair.** The target must (a) label §3.1 as a *reading* of a source that is
internally inconsistent at this point, (b) record that the whole §6–§9 machinery
it uses is written in that reading, and (c) **withdraw §0's claim that "an exact
source-level incompatibility valid for every `t >= 0` does not exist at the
printed-statement / formal-treetop tier."** It exists under the other printed
reading. What the target may claim is the conditional: *given* the Theorem-6.1
convention, no such incompatibility was found. My own judgement is that the
Theorem-6.1 convention is the authoritative one (three anchors versus one, and
it is the only one under which Prop. 9.3(IV) is non-vacuous), so the route is
not dead — but that is a judgement about which printed line carries the erratum,
not a theorem, and it must be flagged to every consumer.

**R2 (false, §3.5). `M*_R = 1` and `i_R = k_f` are wrong; `M*_R = 5`.**
Notation 8.1 prints
`M*_F := gcd(deg p_F, deg p_{h_0,F}, …, deg p_{h_{m−1},F})` — it **excludes**
`deg p_{h_m,F}`, which belongs to `M_F`. The target's
"`M*_R = gcd(k_f, …, k_f(μ_R−1)+1) = gcd(k_f,1) = 1`" includes the excluded
term; what it actually computed is `M_R`. Exactly, for every `t >= 0` and every
pure-shift `l_1 ∈ {1,2,3,5,11,97}` (verified, 64 `t`-values):

```
M*_R = gcd( 2380(4+3t), 3570(4+3t), l_1·2380(4+3t), 2040(4+3t),
            85(635+476t), 85 k_tr + 35 )  =  5
```

so `i_R = deg(p_R)/M*_R = 17 i_tr`, the reduced `p = η^5`, `δ_R = d_R/i_R = 3`,
`R_R = −2`, `deg q = 1`. `M_R = gcd(deg p, deg q) = gcd(5,1) = 1` — the target's
`M_R` value is right, its `M*_R` value is not. **Impact contained:** `(★_R)`
depends on `i_R R_R = −34 i_tr`, invariant under the rescaling. Corroborated by
printed St. 8.4 saturating at `5 | M_tr = 5` (§2.6).

**R3 (false numeral, §3.5). `d_h = μ_R l_f + 1` is wrong.**
Printed Prop. 4.2(iv), quoted inside both Prop. 6.1's and Prop. 8.1's proofs, is
`d_{h,F} = (1−u) + (μ_F − 1) d_F`, i.e. `d_h = (μ_R − 1) l_f + 1`. With the
target's numeral the displayed coefficient would be `l_f − k_f − l_f k_f`, not
`l_f − k_f`. **Repair:** replace the numeral; the displayed conclusion and
`(★_R)` are then correct as printed.

**R4 (false, §4.3). "`here already κ = κ_F = 17`" contradicts the target's own §3.1.**
St. 9.2(iii) plus `π((0,y)) = 0` gives `κ_{(0,y)} = 1`, which §3.1 states. Under
the cited Fable R1 indexing `P_{k'} := p_{n − (κ/κ_F)k'}`, the `κ_F`-graded
spacing at `(0,y)` is therefore `1` in `d`, not `1/17`. The silent stretch is
`50 i_tr − 1` layers deep and imposes at most `45 i_tr` scalar conditions;
`P_10` is a diagonal across `5 i_tr + 1` layers, not one layer (§2.7). **Repair:**
replace "`P_1 = ⋯ = P_9 = 0`, `P_10 = C_tr Φ_tr^{i_tr}`" by the exact shear
identity of §2.7, which is stronger (it *derives* `p_tr ∈ C[η^{17}]`) and honest
about the `t`-dependence. The assignment itself survives.

**R5 (false, §7). The `i_tr`-transfer does not hold as stated.**
The target writes: "The `i_tr`-power on the trunk pattern is a global
multiplicity and factors off; a negative answer at the reduced pattern kills
every `t` at once." Two failures:

* The reduced instance `i_tr = 1` is **not admissible**: it needs
  `k_g = (3/2)·85 = 127.5 ∉ N`, violating Lemma 2.1. The smallest admissible
  reduction is `i = 2` (`k_f, l_f, k_g, l_g` = `170, 102, 255, 153`), which is
  not a member of the D2 family (`i_tr = 28(4+3t) ≥ 112`), so it is a *different*
  germ problem, not a specialization.
* The free-parameter count grows with `t`: `5 i_tr + 1 = 140(4+3t)+1` diagonal
  coefficients against `≤ 45 i_tr = 1260(4+3t)` silent conditions (§2.7). A
  dimension count at small `i` transfers upward only with a lemma nobody has.

**Repair:** withdraw the "kills every `t` at once" clause, or supply the
transfer lemma first. The stop condition is otherwise well posed.

**R6 (imprecision, §3.5).** "the Opus pinning of the printed `⊖` of Prop. 4.1's
proof is unused here: the exponent is literally `0`." An unpinned `⊖` constant
would survive at exponent `0` as a factor `c ≠ 1`. Either cite the Opus `-bbox`
pinning (chart normalizer exactly `1`), or absorb `c` into `c_0` explicitly. No
numeric impact.

**R7 (symbol collision, §3.5/§4.1).** `s_0` is used simultaneously for the
stage-0 tower constant in `C*` (the 7-tuple, `(B_R^{(g)})² = s_0 C_R³`) and for
the integer exponent `k_f(μ_R − 1) + 1` (inherited from the Opus review's R1).
Both occur in the same paragraph. Rename the exponent.

**R8 (mis-citation, §4.2).** The exponent-integrality justification quotes the
transport exponents `i_V l_j/k_j` where the `(0,y)` exponents `k_f l_j/k_j` are
required (§2.9). The conclusion is correct for every `t`; the evidence given is
for a different set of numbers.

**R9 (scope, §3.5/§5).** Three printed gates are invoked outside their printed
hypotheses — St. 8.5 (proof needs a nonzero root), Prop. 8.4 (needs a single
pole; the route has two, which is the actual escape), St. 8.2 (needs `p` with
more than one root). All three conclusions survive; all three reasons must be
replaced. See §2.6.

---

## 4. Attacks that found nothing

* **Cyclic coefficient equation / hidden tower gauge.** None. Tree, edge-local
  St. 8.3 composing globally, one fresh gauge per vertex, `(0,y)` downstream-only.
* **Branch asymmetry in the tower.** None. `s_2, s_3, s_4` live at single
  vertices above the merge; only `s_0, s_1` are in the shared range `j ≤ m_H = 2`,
  and St. 8.3(i) pins them to the same polynomials on both branches.
* **Exceptional `t`.** None. Every gcd, Bezout, integrality and inequality
  above is an identity in `Z[t]` or a `t`-free rational; 64 values checked
  including `t = 7919`.
* **Parity / root-of-unity obstruction at `(0,y)`.** None. `k_g = (3/2)k_f` and
  `l_g = (3/2)l_f` are integral because `i_tr` is even for every `t`;
  `(B_R^{(g)})² = s_0 C_R³` and `t_{4,R}^{k_4} = s_4 C_R^{l_4}` are always
  solvable in `C*`.
* **`p_tr` support obstruction.** I looked for one and found the opposite: the
  `17 | i` support of `p_tr` is *forced* by the shear (§2.7), so it is a
  consistency win for the route, not a kill.
* **Newton-rectangle corner overflow.** The trunk diagonal
  `17j − 10i = 17 i_tr` runs from `(0, i_tr)` to exactly the corner
  `(k_f, l_f)`; it stays inside the Lemma 2.1(i) rectangle for every `t`.
* **`ψ` budget via St. 9.4.** `ψ = 1` gives `Σ λ_{F_i} ≤ td − 2 = 6`, which does
  not bind here. No kill.

---

## 5. Formal treetop vs. everything downstream

I confirm the target's §6/§8 firewall and extend it. What §4 produces is an
assignment of Sigray top polynomials, tower constants and graded layers in
`C[η]` together with a free multiplicative group. It is **not**:

* a **Newton-rectangle germ** — the `45 i_tr` silent conditions and the
  `5 i_tr + 1` diagonal matches of §2.7 are posited, not solved;
* a **polynomial pair** `(f,g) ∈ C[x,y]²` — no `f`, no `g`, and the
  Lemma 2.1(i) support condition is untested;
* a **constant Jacobian** — only the top product law (E) at `m = m_F`;
  `J(f,g) = c_0` as an element of `C[x,y]` is not claimed and not implied;
* a **landing** — nothing places a source, and the reviewed interior transport
  from the trunk to the poles is equally formal;
* an **exact `λ`** — `λ_R = 1` here is the ODE-ray scale `δ/X`, an entirely
  different object from the `λ_F = Σ κ_H(π(H)−1)` of Notation 9.3; the target
  uses both symbols and does not warn;
* a **degree bound, a panel exclusion, td=8 book completeness, or JC2**.

Additional exclusion the target does not state: because of R1, even the *formal*
tier is conditional on which of two printed conventions is authoritative.

On sought outcome (3): the target claims it fails, i.e. that the printed data
determine the `(0,y)` tops and the jet uniquely up to discrete roots. **Narrowed
to GAP.** Layer 10 is determined only after importing the reviewed Prop. 8.1(iv)
trunk rigidity (`Φ_tr = (η^{17}−A)³(η^{17}−(4/3)A)²`, one scalar `A`) plus
`(★_tr)` pinning `A_F²`. That rigidity is a *trunk* datum, not a `(0,y)` datum:
from `(0,y)` alone, `p_tr` has `5 i_tr + 1` coefficients drawn from `5 i_tr + 1`
independent layers, none of which the 7-tuple touches. So outcome (3) is not
refuted at the `(0,y)` tier — it is relocated to the trunk, where it was already
answered. Conditional on the reviewed rigidity, the uniqueness claim is
CONFIRMED, and `P_10(0) = C_R(−(16/9)A_F^5)^{i_tr} ≠ 0` correctly gives the
trunk no `0`-root.

---

## 6. Maximum safe theorem

> Fix the Theorem-6.1 chart convention (`k_f = d_{(0,x)}`, `l_f = deg(p_{(0,x)})`)
> and take as given the hash-pinned reviewed transport data: the trunk tuple
> `(dp,dq,ν,M,k̄,X) = (85,35,17,5,7,17)`, the Prop. 8.1(iv) rigid families at
> `H, G, tr`, the exact product law (E) with `∏ k_j` and `c_0 := J(f,g)`, forced
> `β = 0`, the drop-stage law, and `(A₁/A₂)² = ω^{−15}` with `(L₁/L₂)`-exponent
> `−5`.
>
> Then for **every integer `t >= 0`**, with `i_tr = 28(4+3t)`, the displayed
> td=8 equal-join tree admits an explicit assignment of `(0,y)` top polynomials,
> tower constants, one Jacobian constant and elementary-step maps — namely
> `p_{f,(0,y)} = C_R η^{85 i_tr}`, `p_{g,(0,y)} = B_R^{(g)} η^{(3/2)·85 i_tr}`
> with `(B_R^{(g)})² = s_0 C_R³`, reduced `(p,q) = (η^5, B_R η)` with
> `M*_R = 5`, `M_R = 1`, `i_R = 17 i_tr`, `δ_R = 3`, `R_R = −2`, `λ_R = 1`,
> `m_R = 5`, and the shear of §2.7 — such that: the pair is of Notation 2.4 type
> `(2,3)` with all four Lemma 2.1 inequalities holding in `Z[t]`; `(0,y)` is a
> Prop. 9.3 case-(IV) terminal of the displayed trunk with (i)–(m) exact and
> `d_{(0,y)} = 51 i_tr`, `R = 5/3`, `ψ = 1` both `t`-free; St. 3.9(i)(ii)(iii),
> St. 3.17(i)(ii), St. 3.18, Prop. 8.3(iii), the exact product law (E) in the
> form `(★_R): C_R B_R(l_f − k_f) = (∏_{j<5} k_j) c_0 T_R` with
> `l_f − k_f = −34 i_tr`, Prop. 4.2 with one global tower shared by both merge
> branches, and both merge-branch attachments all hold **as formal data** in
> `C[η]` and in the free multiplicative group generated by
> `(C_R, s_0, s_2, s_3, s_4, c_0)` and roots of unity; the 7-tuple carries six
> `C*` degrees of freedom (`B_tr` is enslaved: `B_tr^{k_4} = s_4 C_tr^{l_4}`);
> the system is triangular with no cycle and no over-determination; and the
> reviewed triangular transport from the trunk toward the poles is untouched.
>
> Additionally, and not previously recorded: the `(0,y)`-side shear **forces**
> `p_tr ∈ C[η^{17}]`.

This proves no polynomial realization, no Newton-rectangle germ, no constant
Jacobian in `C[x,y]`, no landing, no exact `λ`, no degree bound, no td=8 book
completeness, and no JC2 result. It does not kill and does not promote the D2
family at the polynomial-germ gate.

---

## 7. Cheapest exact next source-realization discriminator

The target's §7 test is well posed at fixed `i_tr` but its transfer clause is
refuted (R5). Ordered by cost:

**D1 — settle the chart convention.** Desk, minutes, `-bbox` only. Adjudicate
St. 3.12's displayed consequence and Notation 3.10 against the proofs of
Theorem 6.1 and St. 9.4. Strictly cheaper than every other test, and it gates
all of them.
*Outcomes.* (a) Notation 3.10 authoritative ⟹ `l_f = 85 i_tr > k_f = 51 i_tr`
violates Lemma 2.1(iii) for every `t >= 0`; **the D2 family dies at the printed
tier, uniformly, in one line**, and sought outcome (1) is achieved.
(b) Theorem 6.1's proof authoritative (so St. 3.12 / Not. 3.10 carry an erratum)
⟹ the target's §3 stands as repaired and one proceeds to D2. (c) Genuinely
undecidable from the source ⟹ every td=8 `(0,y)` result must be published as a
conditional, and the erratum becomes the smallest datum in the program.

**D2 — the `i_tr`-transfer lemma.** Desk, exact, `t`-uniform by construction.
Using the shear `[η^i]p_tr = [η^i]p_{i_tr + 10i/17}` (`17 | i`), decide whether
unrealizability of the *reduced* pattern (`Φ_tr`, one copy) implies
unrealizability of `Φ_tr^{i_tr}`. The map from `f`-layers to the trunk diagonal
is linear and injective on that diagonal, so this is a finite-dimensional
question whose parameter count is `t`-linear — which is exactly why the transfer
cannot be assumed.
*Outcomes.* Transfer true ⟹ run D3 once at the smallest admissible reduction
and conclude for every `t`. Transfer false ⟹ §7's stop condition is withdrawn
and the only honest test is at fixed `t`, which is not desk-scale
(`k_f ≥ 266560` at `t = 0`); the program should then move to the Prop. 7.1
integrality ladder instead.

**D3 — the reduced pattern test, at `i = 2` not `i = 1`.** Only after D1(b) and
D2. Does there exist `f` in the Newton rectangle `[0,170]×[0,102]` of type
`(2,3)` with `p_{(0,y)} = C η^{170}`, the silent stretch vanishing, and trunk
diagonal proportional to `((η^{17}−A)³(η^{17}−(4/3)A)²)²` for some `A ∈ C*`?
*Outcomes.* Empty ⟹ with D2 the family is dead at polynomial-germ scope for
every `t`. Nonempty ⟹ the 7-tuple is realized at source-germ scope, and the
next gates are, in order, actual constancy of `J(f,g)` in `C[x,y]`, then the
Prop. 7.1 integrality ladder at `deg(p_H) = 2`. Nonempty with a free coefficient
beyond `A_F` ⟹ that coefficient is the new smallest datum and the target's
layer-10 uniqueness claim must be repaired again.

The Prop. 7.1 ladder remains the cheapest discriminator on the exact-`λ` side
and is independent of all three of the above; the target is right that the
present formal survival does not supersede it.

---

## 8. Explicit exclusions

No AWS. No web. No `jc2-lean` access of any kind — not entered, listed,
searched, read, built, statused, or controlled. No CAS (no Singular, msolve,
Sage, PARI); arithmetic was `int`/`Fraction` on 64 values of `t`. No canonical
ledger, code, test, prompt or shared artifact was edited. Nothing committed or
pushed. No packet written. Only
`xmodel/m2-td8-equal-join-zero-side-initialization-hostile-review-opus5-20260829.md`
was created.

I did not re-solve any vertex-local ODE at `H`, `G`, the trunk or the poles, and
I did not re-derive the twin-gauge identity; both are consumed as reviewed
transport, as the lane requires. The `(0,y)` monomial identity of §2.5 is not
one of those four families and was re-derived from the printed Prop. 8.1(iv).

This review does not license any consumer to cite the target's §3.5 `M*_R`,
`i_R`, `δ_R`, `R_R` or `d_h`, its §4.3 `κ_F` and layer count, its §5 St. 8.2 /
Prop. 8.4 bullets, its §0 sought-outcome-(1) claim, or its §7 transfer clause,
as written. After R1–R9 the existence result of §6 above is citable at formal
treetop scope, conditional on D1.

---

*Report body ends. Self-hash below covers all bytes above this line.*

report_body_sha256 = 0dee73677e476253dd57abd4d007dbd6912c40d668352878bdf7fc7c08ca42a3
