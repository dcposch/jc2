# Fable 5 primary — td=8 equal-join Statement 3.9 coefficient transport

Lane: Fable 5, primary mathematics (not review). Date: 2026-08-29 UTC.
Status: **SOURCE_READY_FOR_DIFFERENT_MODEL_HOSTILE_REVIEW**.

## 0. Charge, sources, custody

Charged question: for the reviewed td=8 equal-join D2 route — two identical
poles `(Λ,a,b,ν)=(4,1,2,3)`, two rigid `(21,15)` cells, the affine equal
join (`ν_G=4+3t`), the rigid `(85,35)` trunk, the `(0,y)` terminal — derive
the actual cross-vertex coefficient system imposed by printed Statement 3.9
and decide `ROUTE_KILLED_BY_ST39` / `ST39_TRANSPORT_SURVIVES` / `PARTIAL`.

Sources read (SHA-256 recomputed this session):

```
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a  xmodel/m2-td8-equal-join-route-family-sol56-20260829.md (D2 route producer)
aeb7714e656b7c112ce2933b48b6da6c18fdec3136b2d2651c44e6d9874c5584  xmodel/m2-td8-equal-join-prop81iv-route-sol56-20260829.md (reviewed route certificate)
c2a112fa84e0c11085f285ddab79999caf6b00d8a8fe37a84390a13ee7cfc675  xmodel/m2-td8-equal-join-prop81iv-route-hostile-review-fable5-20260829.md
                                                                  (my passed local ODE review; body d6e743dd…)
```

Printed text consumed directly (printed page = pdf page, per promoted
DEPTH ground-truth note): Not 3.8–3.13, St 3.7–3.9 (+ printed proof of
3.9), St 3.11, St 3.16, Prop 3.2, St 3.17, St 3.18 (pp. 12–18); Prop 4.1,
Prop 4.2 (+ proof), Not 4.1, Prop 4.4, Prop 4.6 (pp. 18–23); Prop 5.3,
Prop 5.4, St 5.2, Prop 5.5 (pp. 25–27); Not 6.1, St 6.1–6.2, Prop 6.3,
6.4, Cor 6.1, Prop 6.7, 6.8 (pp. 29–34); Not 7.1, St 7.1–7.3, Prop 7.1,
7.3, 7.5 (pp. 34–38); Not 8.1, St 8.1, Prop 8.1 (+ proof), St 8.2, 8.3,
8.4, 8.5, Prop 8.2, 8.3 (pp. 39–44). Layout re-extraction of printed
p. 15 confirmed St 3.9 (i)–(iii) verbatim with no dropped glyph (the `⊖`
trap affects 8.1, not 3.9). Promoted ladder consulted: `ladder/SHEET6-DEPTH.md`
header/§0 (i-normalized frame dictionary `ρ = D/deg p_full`,
`w=(κ̄−ρ)/ν`); `ladder/TRANSPORT.md` header only (GGV normalization layer
— determined off-topic, not used). Not read: any Grok/Opus transport,
lambda, semilinear, or ideation output; the grok46 route-family review
was not needed and was not read this session.

No web, AWS, commit, push, canonical edit, heavy CAS, long/high-memory
process, global `git status`, workspace-wide search, or `jc2-lean` access
of any kind. Files written: this report and the packet
`cases/m2_td8_equal_join_st39_transport_fable5_20260829/` only; scratch in
`/tmp`.

---

## 1. Verdict

**`ST39_TRANSPORT_SURVIVES`** (sought outcome 2: an explicit compatible
formal coefficient system exists), **for every `t ≥ 0`, uniformly — no
finite exceptional set, no residue splitting, no root-of-unity or
exponent-parity kill.**

**Narrowest maximum consequence.** For every integer `t ≥ 0` the displayed
td=8 equal-join tree admits an explicit coefficient system — top
coefficients, orbit gauges, tower constants, branch roots, deck choices —
satisfying simultaneously: Statement 3.9(i)–(iii) along every edge for the
f-side and every tower-side pattern; Proposition 8.1(i)–(v) with the local
rigid families (ratios `3/2`, opposite, `4/3`) at all four pattern
vertices; Proposition 5.3/5.4 with the forced pole family at both poles;
Proposition 4.2(iii)–(iv) with one global Abhyankar tower shared by both
branches; and the exact (Jacobian-pinned, not `⊖`-free) constants in
Proposition 4.6. Consequently **no vertex-local or cross-vertex
coefficient-transport discriminator at the printed-statement tier can
remove the D2 family**; the completeness program must proceed through
source landing (the `(0,y)`-side initialization, §9), exact lambda, or a
global argument. Transport survival is *not* source landing, realization
by a polynomial pair, exact-lambda, a degree ceiling, or any JC2
conclusion.

Two new rigidity laws fall out and are part of the deliverable: the
**twin-gauge law** `(A₁/A₂)² = ω^{−15}` (§7), and the **drop-stage law**
`l_m/k_m − (μ_W − 1) = dq_W / D_W` (§5), which pins previously unprinted
tower stages, e.g. `(k₂,l₂) = (7,6)` and `(k₃,l₃) = (112+84t, 635+476t)`.

---

## 2. The printed transport engine, assembled

All items below are printed statements, cited exactly; no ladder gloss is
load-bearing.

- **Elementary step.** `F∗c = I_P((n+1)/κ)`, `n = κπ(F)` (Not 3.8), with
  `η_{F∗c} = x^{1/κ}(η_F − c)` (proof of St 3.9, p. 15). For *any*
  polynomial `h`: `mult(p_{h,F},c) = deg(p_{h,F∗c})` (3.9(i)); writing
  `p_{h,F} = Σ_{j=l}^m a_j(η−c)^j`, `p_{h,F∗c} = Σ_{j≤l} b_jη^j`, `l =
  deg p_{h,F∗c}`: **`a_l = b_l`** (3.9(ii)); `d` drops by `mult/κ`
  (3.9(iii)).
- **Vertices and edges.** Vertices are exactly the faces whose f-pattern
  has more than one root (St 3.16); vertex-to-vertex, `F = G + c` gives
  `deg(p_F) = mult(p_G, c)` (St 3.17(i)). Continuations exist only at
  roots, and for a root `c ∈ C*` exactly one `ν_F`-th rotation `εc`
  continues (St 3.18) — the deck bookkeeping below.
- **One global tower.** `h₀ = g`, `h_{j+1} = h_j^{k_j} − s_j f^{l_j}`,
  `gcd(k_j,l_j)=1`, `s_j ∈ C*` **uniquely defined** (Prop 4.2), face-wise
  persistent (Prop 4.4), and *shared along every elementary step in*
  `T_a^&`: `h_{j,F} = h_{j,G}` for `j ≤ m_F` (St 8.3(i)). Enslavement at
  every face with `j < m_F`: `(h_{j,F}^+)^{k_j} = s_j (f_F^+)^{l_j}`
  (4.2(iii)) — the same `s_j` on both merge branches. Tower depth `m_F`
  is non-increasing child-ward (St 8.3, St 8.5 mechanism).
- **Exact constants.** From `h_{j+1} = h_j^{k_j} − s_j f^{l_j}`,
  `J(f,h_{j+1}) = k_j h_j^{k_j−1} J(f,h_j)`, so
  `J(f,h_m) = (∏_{j<m}k_j)·c₀·∏_{j<m}h_j^{k_j−1}` with `c₀ := J(f,g)` —
  an *exact* identity. Taking initial parts in the nondegenerate case
  (the definition of `m`) upgrades Prop 4.6(11) to the exact form: at
  every face,

  ```
  d_F·P·Q′ − d_{h,F}·P′·Q = (∏k_j)·c₀·∏_{j<m_F} p_{h_j,F}^{k_j−1}   (E)
  ```

  in η-polynomials, `P := p_{f,F}`, `Q := p_{h_m,F}`. The printed `⊖` of
  (11) and 8.1(iv) is *not free* once transport is imposed: it is this
  pinned product. (The rational factor `∏k_j` and the `κ_F`-normalizers
  are explicit nonzero rationals, identical on the two twin branches;
  they cancel in every closed cycle and rescale free gauges otherwise —
  packet P6 verifies invariance.)
- **Vertex structure.** `f_F^+ = ⊖(ξ^δ p)^i`, `i = deg(p_F)/M*_F`;
  `h_F^+ = ⊖ξ^{1−u}(ξ^δ p)^k q`, `k = i(μ_F−1) ∈ Z` (Prop 8.1(i)(ii)).
  Poles: `m = 0`, `μ = 0`, all pattern roots simple, `k_f·p·q′ − k_g·p′·q
  = ⊖` with `(k_f,k_g) = (2,3)` for type `(α,β) = (2,3)` (Prop 5.3,
  St 5.2, Prop 5.4).

**Full-pattern dictionary** (the St 3.17(i) chain; this independently
reproduces the parametric lane's `i = 14` pin):

| vertex | reduced `(dp,dq)` | `i_V` | full `D_V = deg p_{f,V}` | q-side full `Q_V` |
|---|---|---|---|---|
| pole `P_e` | `(4,6)`, all simple | — (`m=0`) | 4 | 6 |
| `H_e` `(ν=7)` | `(21,15)`, mult `(2,1)` | **2** | 42 | 36 |
| merge `G` `(ν=4+3t)` | `(24+18t, 9+6t)`, mult `(3,3)` | **14** | `336+252t` | `1905+1428t` |
| trunk `(ν=17)` | `(85,35)`, mult `(3,2)` | **112+84t** | `85(112+84t)` | `85k_tr+35` |

Chain checks: `i_H·2 = 4` (pole), `i_G·3 = 42 = i_H·21`, `i_tr·3 =
14(24+18t)`; `(l₀/k₀)·4 = (3/2)·4 = 6` closes the pole q-side. `M*` gcd
lists reproduce `i_G = 14`, `i_tr = 112+84t` exactly (packet P3).

---

## 3. Interior-face binomial lemma (q-side transport is pinned)

At an edge-interior face, `P = C(η−c)^A` (single root, St 3.16). Writing
`Q = Σ q_s (η−c)^s`, the exact (E) reads
`C[d_F(η−c)Q′ − d_{h,F}·A·Q] = Π·(η−c)^{s₀}`, `Π := (∏k_j)c₀∏t_j^{k_j−1}`,
`s₀ := A(μ−1)+1`, so `(d_F s − d_{h,F}A)q_s = 0` except at `s₀`. Hence

```
Q = β(η−c)^{s*} + γ(η−c)^{s₀},   s* := (d_{h,F}/d_F)A,
γ = Π / (C·(d_F − (1−u)A))  (pinned; d_F −(1−u)A < 0 in T_a^&),
β free (resonant),  and  s* > s₀  ⟺  F ∈ T_a^&.
```

Consequences. (a) Along an edge, 3.9(ii) gives `top(next) = lc_c(current)
= γ` at every interior step; the arriving top is absorbed by the next
face's free `β`; therefore **the q-side top coefficient arriving at any
child vertex is pinned by the f-side data and the global constants — no
jet freedom enters the chain**. Composing to the child vertex `W`
telescopes to `d_{f,W} − (1−u_W)·D_W` evaluated *at W*. (b) The f-side is
even simpler: interior f-patterns are perfect powers `C(η−c)^A`, so
`C` transports verbatim; across a whole edge, `C_W = lc_c(p_{f,V})` —
exactly the composed Statement 3.9(ii) demanded by the charge. (c) The
satellite roots of the binomial (the `(s*−s₀)`-th roots around `c`) feed
only the escape branches; they are inert for the chain system.

---

## 4. Drop-vertex lemma

Let `W` be a route vertex with reduced q-degree `dq_W`. Prop 8.1(ii)
gives `Q_W = D_W(μ_W−1) + dq_W`. If the tower depth were constant along
the top of the feeding edge, §3 plus 3.9(i) would force
`Q_W = D_W(μ_W−1) + 1`. Hence:

> **Every Prop 8.1 pattern vertex with `dq_W > 1` is a tower-drop vertex**
> (`m` strictly decreases at `W`), its q-side arrives as the *previously
> enslaved* element `h_{m_W}`, and the dropping stage satisfies the
> **drop-stage law**
> `l_{m_W}/k_{m_W} = Q_W/D_W`, equivalently
> `l_m/k_m − (μ_W − 1) = dq_W/D_W`.

All three route vertices have `dq > 1`, so all three drop. In the minimal
tower (stage 1 a pure shift, `k₁ = 1`, forced if the recorded `k = 1`
label at the `(21,15)` cell is Prop 8.1(ii)'s `k`; alternatives in §9):

| stage `j` | `(k_j, l_j)` | pinned by | remark |
|---|---|---|---|
| 0 | `(2,3)` | type `(α,β)=(2,3)` | `t₀² = s₀C³`; exponent `3i_V/2 ∈ Z` since every `i_V` is even |
| 1 | `(1, l₁)` | shift; `μ` unaffected | `l₁` not pinned by displayed data |
| 2 | **`(7,6)`** | `Q_H/D_H = 36/42` | drops at each `H_e`; `μ_H = 3/2`, `k_H = 1` |
| 3 | **`(112+84t, 635+476t)`** | `Q_G/D_G = (1905+1428t)/(336+252t)` | drops at `G`; coprime for all `t`: Euclid `635+476t → 75+56t → 37+28t → 1` |
| 4 | `(17·i_tr/g, (17k_tr+7)/g)` | `Q_tr/D_tr` | drops at trunk; fed by the free global `s₄` |

with `μ_G = 3/2 + 36/7 = 93/14`, `k_G = i_G(μ_G−1) = 79 ∈ Z`, and
`k_tr = 39984t² + 106650t + 71117 ∈ Z` for all `t` (packet P2). Note
`i_tr·l₃/k₃ = 635+476t ∈ Z` exactly (`k₃ = i_tr`), and `i_G·l₂/k₂ = 12`,
`i_G·l₀/k₀ = 21`, `i_H·l₀/k₀ = 3`: **every transport exponent is an
integer for every `t` — the sought exponent-parity obstruction is
absent** (packet P2 sweeps `t ≤ 400` plus the symbolic identities).

---

## 5. The cross-vertex coefficient system

Write `p_{f,V} = C_V Φ_V^{i_V}` (`Φ_V` monic reduced), q-side top `B_V`,
enslaved tops `t_{j,V}` (`t_{j,V}^{k_j} = s_j C_V^{l_j}`), and per edge
`L_c := lc_c(Φ_V)`. The complete system is:

- **Transport (3.9(ii) composed):** `C_W = C_V·L_c^{i_V}`;
  `t_{j,W} = t_{j,V}·L_c^{i_V l_j/k_j}` (automatically consistent with
  enslavement at `W` — the consistency `t_{j,W}^{k_j} = s_j C_W^{l_j}`
  telescopes identically, so enslavement adds *no* equations along
  edges, only the §4 divisibilities);
- **Drop feed:** `B_W = t_{m_W,V-side}·L_c^{i_V l_{m_W}/k_{m_W}}`
  (all route vertices; §4). Pole feed: `B_P = t₀`-transport,
  `B_P² = s₀C_P³`;
- **Vertex equation (★), the reduced exact (E):** with the local monic
  families and `R_V` their forced ODE constants,

  ```
  i_V · C_V · B_V · R_V = (rational frame factor) · c₀ · T_V,
  T_V := ∏_{j<m_V, k_j≥2} t_{j,V}^{k_j−1},
  R_H = (21/2)A_e²,  R_G = −(16+12t)a²,  R_tr = (68/3)A_F²,
  ```

  and at the poles `(d_P/2)·C_P·B_P·(9/8)r³ = c₀`, with the pole family
  forced to `σ = (3/2)r`, `π = (3/8)r²` under `2pq′−3p′q = ⊖`
  ((k_f,k_g) = (2,3); the `(1,2)` frame is dead — packet P1);
- **Leading-coefficient factors (exact, packet P4):** merge orbits
  `L_e = 8ν³a⁶/c_e³` at *both* orbits (`c₁^ν = a`, `c₂ = ωc₁`,
  `ω^ν = −1`), `Ψ_G′ = 2νa²` at both, H chain root
  `K_e = −(49/2)c_{P_e}^{19}`.

**Solvability (top-down, triangular).** The treetop data `C_tr, B_tr`
(via free `s₄`), `t_{j,tr}` (via free `s₀,s₂,s₃`) and `c₀` are free
initialization; then (★_tr) pins `A_F²`; the edge pins `C_G, t_{j,G},
τ_G`; (★_G) pins the merge gauge `a²`; the two merge edges pin
`C_{H_e}, t₀, τ`; (★_{H_e}) pins `A_e²`; the pole edges pin `C_{P_e},
B_{P_e}`; (★_{P_e}) pins `r_e³`. Every pinned quantity is a product of
nonzero factors, hence nonzero, for every `t ≥ 0`. All remaining freedom
is discrete (deck/branch roots of unity, St 3.18-coherent). The only
closed cycles in the tree are the twin pairs, §7.

---

## 6. Probe 1 — orbit attachment at the merge

Both merge orbits have reduced multiplicity 3 and are searrow
(`3(9+6t) > 24+18t`), and `mult = 3 | M_G = 3` (St 8.4); each feeds one
`(21,15)` cell whose full degree 42 equals the full multiplicity
`3·i_G = 42` (St 3.17(i)) — the attachment is *arithmetically forced* to
the two multiplicity-3 orbits and *symmetric*: swapping `H₁ ↔ H₂` is
equivalent to replacing `ω` by another admissible root of `ω^ν = −1` and
re-solving the twin law, which is always possible. No printed invariant
distinguishes the two attachments; both are compatible. The merge's own
q-side data (`Ψ_G`, `L′ = 2νa²`) is **inert below `G`**: the `H`-cells
are fed by the enslaved `h₂`, not by `h₃`'s pattern.

## 7. Probe 2 + the twin laws

**The two incoming gauges.** Taking the ratio of (★_{H₁}) to (★_{H₂})
— identical frames, identical rational factors, shared `s₂`, shared
parent — every continuous gauge cancels:

```
(A₁/A₂)² = (L₁/L₂)^{i_G(μ_H − 1 − l₂/k₂)} = (L₁/L₂)^{−i_G·dq_H/D_H}
         = (ω³)^{−14·(15/42)} = ω^{−15},    ω^{ν_G} = −1.
```

By the drop-stage law the exponent is `−i_G·dq_H/D_H = −15`
**independently of every un-pinned tower choice** — the twin law is
tower-invariant. It is solvable in `C*` for every `t` and every
admissible `ω` (packet P5 closes the cycle exactly over `Q(i)` at `t=1`,
`ω = −1`, where it forces `A₁/A₂ = ±i`; exponent mutations break it).
So Statement 3.9 does **not** kill the route here; instead it
*rigidifies* it: the two incoming `(21,15)` gauges are locked to each
other up to an explicit root of unity. The analogous pole-twin cycle is
absorbed by the free `r_e³` — no constraint.

**Does the trunk ratio consume the merge scale?** No. Each drop vertex
consumes its *own* fresh global: the H-pair consumes the shared `s₂`
(hence the twin law — the only place sharing bites), the merge consumes
`s₃`, the trunk consumes `s₄`. The trunk step introduces a genuinely new
gauge (`s₄`, equivalently the treetop `B_tr`); the merge scale
`(a², c₁, ω)` survives to the H-tier and is consumed there.

## 8. Sweep for the sought exact incompatibility — absent

- **Root-of-unity kill:** the deck enters only through `L₁/L₂ = ω³` and
  the twin exponent `−15`; `x² = ω^{−15}` is solvable in `C*` always.
  The `ε`-uniqueness of St 3.18 pins representatives but the deck acts
  coherently on the whole tree — checked to cancel in every cycle.
- **Exponent parity:** every transport exponent `i_V l_j/k_j ∈ Z`
  (`3i_V/2` integral since all `i_V` even; `i_G·6/7 = 12`;
  `i_tr·l₃/k₃ = l₃`); every enslaved pattern is a polynomial (orbit
  multiplicities times exponents integral). Packet P2.
- **Residue/finite-`t` failure:** all pins are nonzero and all gcd/
  integrality identities hold for all `t` (symbolic Euclid chains ending
  at remainder 1; `k_G = 79`, `k_tr(t) ∈ N`). No exceptional `t`.
- **Sign/branch incoherence of `t₀ = ±√(s₀C³)`:** transported as honest
  leading-coefficient arithmetic from one initialization — single-valued;
  squaring (★) never loses a solution because the branch is itself a
  gauge.

## 9. What the printed data does not determine (and why it cannot flip the verdict)

The displayed-route data does not pin: the stage-1 branch (`k₁ = 1` shift
vs `k₁ ≥ 2` alternatives — if the recorded `k=1` cell label is 8.1(ii)'s
`k`, the shift is forced), `l₁`, the stage-4-and-above tail, the numeric
`s_j`, `κ_F`-normalizers, or the `(0,y)`-side chain. All of these move
individual exponents but (i) the twin exponent is invariant
(`−i_G·dq_H/D_H`), (ii) the system stays triangular-monomial with one
fresh global per drop vertex, and (iii) all divisibilities were checked
against the worst case. So the verdict is uniform across the ambiguity;
no missing source coefficient is needed for it. The smallest data that
would pin the remaining tower shape is the single integer
`deg(p_{h₁,H})` (= `42l₁` iff the shift branch, `21l₁` iff `k₁ = 2`) —
a typed, finite discriminator for a future source-side packet.

**Exact next lemma** (the honest next gate): *(0,y)-side closure* — extend
this coefficient system up the un-displayed terminal chain with
`p_{(0,y)}` single-rooted (Prop 8.3(iii)) and the td=8/type-(2,3) degree
equations, i.e. decide whether the free initialization
`(C_tr, B_tr, s₀, s₂, s₃, s₄, c₀)` can be realized by an actual top form
of a degree-ratio-(2:3) pair. That is source landing at the treetop tier,
strictly outside Statement 3.9's scope.

## 10. Packet and replay

`cases/m2_td8_equal_join_st39_transport_fable5_20260829/`:

```
d2e1003465d0938d1056f6a47ca213d41c249fc458124cc0509f982e5f6270b3  st39_transport_check.py
832b9ed6fb6926bf143fcccede01da3ec1ed74baf831521252c04c60acfb9844  test_st39_transport_check.py
f4259b15ca02ab1b31b5451398f74d7f72f56746d7906ea6d48d684f1accecaf  README.md
```

Replay (all from the packet directory; runtimes ≈ 0.1 s each):

```
python3 st39_transport_check.py        →  ST39_TRANSPORT_CHECK_PASS checks=24987
python3 -O st39_transport_check.py     →  ST39_TRANSPORT_CHECK_PASS checks=24987
python3 test_st39_transport_check.py   →  ST39_TRANSPORT_TEST_PASS checks=24987 mutations=2
```

Layers: P1 exact local ODE constants + forced pole family (+ mutation
kills); P2 drop-vertex arithmetic, pinned stages, symbolic Euclid,
integrality (t ≤ 400 sweep + t ≤ 2000 Euclid); P3 `M*` gcd lists; P4
exact Q(i) leading-coefficient factors; P5 exact twin-cycle closure and
mutation kills; P6 end-to-end log-polar instantiation at `t = 0,1,2,10`
with prefactor-invariance reruns. The finite scans are regression
evidence; §§3–8 are the all-`t` proofs.

## 11. Scope firewall

Proved here: the formal Statement-3.9 coefficient-transport tier for the
displayed tree, as itemized in §1, promoting the D2 family from
independent local survival to transport survival, plus the twin-gauge and
drop-stage laws. Not proved and not claimed: source landing, geometric
realizability, realization by a single polynomial pair, exact lambda (all
recorded lambda values remain lower bounds), completeness of the td=8
book, any degree ceiling, any Keller map, any JC2 conclusion. The
`(0,y)`-side tail and the un-pinned tower branches are constructed
formally, not derived from a source. No canonical consumer may cite this
report before different-model hostile review. No AWS was used or is
authorized.

---
Report-body SHA-256 (bytes through the separator line above): 3b7851eaaee3f35c23de8d201eb22ad664ab2dba1614d6d4fc04cba562461171
