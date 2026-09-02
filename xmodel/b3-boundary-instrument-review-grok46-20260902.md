# Hostile review: B3-BOUNDARY-INSTRUMENT — nine bridges, two controls, the census, and GAP-CANDIDATE[BI-ATTACH]

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-02.
**Lane.** `B3-BOUNDARY-INSTRUMENT-REVIEW`.
**Charge.** Default to refutation. Desk-scale exact reasoning plus sympy 1.14.0 over `Q`. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis` line. No canonical-ledger edit; `jc2-lean` not opened. Item (0) is mandatory first and is the only item that may touch the checked `N=4` ledger.

**Headline.** `GAP-CANDIDATE[BI-ATTACH]` is **GAP-REPAIRED**: the assembly consumes constant-versus-fork of a Deg-2 *block*, not a vertex transpose `(μ_l,s_l)`. The `N=4` kill remains SET §§2–7; do not reopen `N=4-CHECKED-CLOSED`. Nine of ten bridges survive with stated hypotheses; `(H-∞)` is **not** verified at `N=4` (wrong tail). `Census(4)=35` reproduces. Control 2 on `Γ` passes as `REPRESENTATIVE`. No empty window at `N=5,6`; one missed charged type at `N=6` (cap `3`). Three-cusps cell is `j>=2`. Successor is well-posed as a census, not as a `v_0`-profile list.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (0) | `GAP-CANDIDATE[BI-ATTACH]` vs checked `N=4` chain | **GAP-REPAIRED**. Split *is* load-bearing for Cor. 5. Transpose is the Cor. 4-excluded Deg-2 fork, not the assembly's object. Kill remains SET §§2–7. Checked ledger **not** reopened. |
| (1) | BI-1: DO (9) at `g` is `[P3]` | **CONFIRMED**. `H2`, Keller, 7.B'. No `SCOPE[B3-QH]`. |
| (1) | BI-2: `n(v~_y)=e_y` | **CONFIRMED**. All `N`, `(R1)`,`(R2)`. No `(H-∞)`. |
| (1) | BI-3: fibre-at-`p` ledger | **CONFIRMED** as equality *under* `(H-∞)`. **GAP** on the claim that `(H-∞)` holds at `N=4`. |
| (1) | BI-4: E-CHARGE at the boundary | **CONFIRMED**. Contracted model (BR binding). `H2`. |
| (1) | BI-5: mark saturation / ramification profile | **CONFIRMED** for non-dicritical Deg `=a` over `v_0`. Saturation and `{n(v~)^{m(v~)}}` stay under `(H-∞)`. |
| (1) | BI-6: unit lifts transport determinants | **CONFIRMED** as the DF-4/DF-7 mechanism. |
| (1) | BI-7: disconnected reading never kills `j<=a` | **CONFIRMED**. Route closed negative. |
| (1) | BI-8: spine-depth cap `#forks <= N-s_l μ_l` | **CONFIRMED** as a cap. Tightness at `N=4` exhibited, not assumed. |
| (1) | BI-MERIDIAN: `1^a · prod (μ_l)^{s_l}` | **CONFIRMED**. `H2`, 7.B', MI Lemma 4.1. |
| (1) | EXTRACTION-1 | **CONFIRMED**. `H2` via MI Lemma A. |
| (2) | Census closed form; `Census(4)=35`; `(4,1)` sub-count 23 | **CONFIRMED**. Independent `Rows(m)` for `m<=12` match. |
| (3) | CONTROL 1 (`N=4`) | **CONFIRMED** for `(μ,corr)=(2,1)` and the SET §§2–7. Two-unit-lifts identification **conditional** on `(H-∞)` and B3-N4 (`SCOPE[B3-QH]`). |
| (3) | CONTROL 2 (`Γ`) | **CONFIRMED** as `REPRESENTATIVE`. Every requested item. |
| (4) | `N=5,6` runs: no empty window; `j>=2` at three-cusps | **CONFIRMED** no empty window and the `j>=2` constraint. **GAP**: charged-type count at `N=6` is 9, not 8 (one missed cell, cap `3`). |
| (5) | Successor `OPEN[BI-CENSUS-DEG5-DEG6]` | **CONFIRMED** well-posed as a Deg-`<=5,6` census with BI-1/8 spine data. `v_0` list `{(1,1,1),(1,2),(3)}` is **not** licensed. Settle BI-ATTACH first. |

---

## 0. Custody, method, scope

Frozen copies were hashed with `shasum -a 256` **before any was read**. All six match the charge:

```text
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  b3-boundary-instrument-opus5-20260902.md
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  do1-mu2-replay-sol56-20260901.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  b3-e-geometry-opus5-20260902.md
12dea79fc65d31dd5ac2dac9fa3faff638cd1d5a12b7c6f72a7f18658b09ba4a  b3-e-geometry-review-grok46-20260902.md
```

**BE** = B3-E-GEOMETRY, **BR** = its grok-4.6 review, **HF** = HORN-FLAGSHIP, **MI** = MPRIME-ALLN-H2, **DR** = the charged DO I `μ=2` replay, **BI** = the producer. After the sextet, the Russian publication and English preprint were read **only** to decide item (0) against Prop. 1, Lemma 6, Cor. 4–5, Lemmas 10–15. Numbering is published Russian; English in parentheses at first mention.

**Method.** Independent derivation of BI-1, the fibre identities, B3-E-GENUS arithmetic, BI-7, BI-8, BI-MERIDIAN, and the census generating function. sympy 1.14.0 over `Q` on `Γ`; exact integers for `Rows`, `Census`, charged types, caps; three blowups of `F=(x,xy^2)` at `[0:1:0]`. No Groebner, no AWS, no `jc2-lean`. No exit-price assertion.

**Consumed at BR / HR CONFIRMED, repairs binding:** E-ETALE; E-BMY-VACUITY (log-smooth); Prop 3.1 / LOC-1; Cor 3.2 with `g=p_a`; E-CHARGE (contracted model); B3-E-GENUS; B3-E-NOCROSS; BE §6's `(μ,corr)=(2,1)` as the `N=4` object; HF B3-DEGREE, B3-CAGE, B3-LOC, B3-PUSHOFF, B3-COMPONENT, Props 3.1/3.2, B3-N4, `SCOPE[B3-QH]`. **As MI states them:** Lemma A, Lemma 4.1, `(L)`,`(K)`,`(C1)`–`(C3)`, 7.B', N4-PIN, THEOREM PROFILE, `j<=a`, Orevkov 2.1/3.1. **From DR, repairs binding:** Def. 3, (9), (4.3), Prop. 3, Lemmas 1–9, (4.7), Prop. 4, Lemma 7, Corollaries 4–5, Lemmas 10–15.

**Not consumed:** `Z(G)=1`; case (A); `A2`; `E_0`; `deg E-bar` / `A_F-bar` / `κ-bar`; `(B2)`. Campaign `a` is sheet count; DO vertex is `v`; `l'=l ∩ Φ^{-1}(A^2)`, `p̃_l=l\l'`, `p=Φ(p̃_l)`, `v_0` the component of `L` through `p`.

---

## 1. Item (0) — BI-ATTACH versus the checked `N=4` chain

**Outcome: `GAP-REPAIRED`.** The `N=4` kill is still the SET §§2–7. The checked ledger is not reopened.

### 1.1 What the replay actually consumes — (a)

Russian Lemma 6 (p. 854; English 2.2): `m_{p̃}(g̃)=1`; if `(ã g̃)` is linear then `Deg(ã g̃)=2`. Proof: `n(g̃)=2`, `m(g̃)=1`, conditions A–B, Proposition 1 (English 1.15).

Proposition 1: if the splice diagram of `C` near `L` is of the form `←→` (either `L` is a double point of `C`, or a linear chain whose ends meet `c_1,c_2` transversally), then every connected component of the preimage is a **constant-degree** chain of the same form, and `Deg L̃_1 = m_{p̃_i}(c̃_i)\, n(c̃_i)`.

Definition 5: a vertex of `L̃_∞` is a *fork* iff `m>1`. Corollary 4 (p. 857; English 3.9): if `ã` is a fork then `Deg ã > 2`. Proof: Lemma 9(b) excludes the Deg-2 local types (Russian Figs. 3–5).

DR §6 assembly (the fill of published Corollary 5): *start at the maximal degree-two constant block incident to `g̃`*. If the far end were terminal, the other two sheets would form a separate component (nonfork vertices cannot merge maximal blocks). Connectedness forces a first merge; maximality makes it a fork; **Corollary 4 excludes a Deg-2 fork**; the first fork has Deg 3 or 4, and the six global graphs (Russian Figs. 20–25) follow.

That is load-bearing use of the *type* of the incident object (constant block, `m=1` on its non-constant vertices), not merely of its Deg. Lemmas 10–15 then run on those six graphs. Their displayed identities — (7.3) `-2d_2 = 18δ^2-2d_2-6yδ^2` vs `y>4`; (7.6) odd `=-1` vs even; (7.10) `-1=-B-αC <= -4` — consume Deg of tubes, `n(g̃)=2` in the transfer ratios of Lemma 5, and `n` of the forks in the figures. They do **not** consume an independent vertex split `(m,n)=(μ_l,s_l)` of a dicritical-incident *fork*.

A one-line Cor. 4 kill of a Deg-2 incident *fork* is already a step *inside* the SET §§2–7 (it is how the assembly discards Deg-2 as the first merge). It does not replace Lemmas 10–15.

### 1.2 The local model, recomputed — (b)

Charge: monomial `F` at a transverse crossing of `l` with a single `L̃_∞`-component `B_l`; `n(B_l)=ord_{B_l} F^*(v_0)`, `m(B_l)=deg(F|_{B_l})`.

SNC two-curve crossing, coordinates `(u,w)` with `l={w=0}`, `B={u=0}`, target `v_0={U=0}`, `g={W=0}`. Finite at `p̃` forces the diagonal monomial form: `F^*U=u^{a_1}·unit`, `F^*W=w^{b_2}·unit`. Off-diagonal `w` in `F^*U` would put `F(l)` in `v_0`; off-diagonal `u` in `F^*W` would put `F(B)` in `g`, hence at `p`, i.e. `B` contracted. So under `(H-∞)` (fibre finite, `B` non-constant) one has `a_1=s_l` (index of `F|_l` at `p̃`, (D2)) and local index of `F|_B` at `p̃` equal to `μ_l`. Then `n(B)=s_l` and `m(B) >= μ_l`. Equality `m=μ_l` is **not** forced: (1.12) only sums local indices to `m`. The lane's `(m,n)(B_l)=(μ_l,s_l)` is the equality case.

At `N=4`, `(s,μ)=(1,2)`: equality gives `(m,n)=(2,1)`, a Deg-2 fork, which Corollary 4 excludes. That is not a new kill and is not a contradiction with the length of DO I: it is Corollary 4 doing the job DR §6 already assigns it. The first *non-constant* `L̃_∞` vertex is then a fork of Deg 3 or 4, and the Deg-2 object is the **arm** (constant-degree block / edge) from that fork to `g̃`, with `Deg=m_{p̃}(g̃)\,n(g̃)=1·2=2` by Lemma 6.

The lane's transpose is therefore **not** the split of the object the assembly uses. The assembly's object is the Deg-2 constant block of Lemma 6. Non-constant vertices in a *linear* such block have `m=1` (a fork is nodal: source valence `(r-2)m+2 > r` for `m>1`), hence `(m,n)=(1,2)`. That coincides with `(s_l,μ_l)` at `N=4` because `s_l=1`.

Independent blowup of the local model `F=(x,xy^2)`, homogeneous `[X:Y:Z]↦[XZ^2:XY^2:Z^3]`, three blowups at `[0:1:0]`, chart after the third: `U'=x_3^2 z_3^2`, `V'=z_3`, exponent matrix `[[2,2],[0,1]]`, `det=2=sμ`. Dicritical `{x_3=0}` dominates `{U'=0}`; neighbour `{z_3=0}` maps to the point `p`. **MEASURED: the component `l` meets at `p̃` is contracted.** Preimage of `v_0 \ {p}` is empty in this chart. The naive identification "`B_l` = the `L̃_∞`-component that `l` meets" is unlicensed. Only `Deg` of the incident *block* `= s_l μ_l` is read off the local degree at `p̃`. This matches the producer on the contracted neighbour and on `Deg=2`; it does **not** license `(m,n)=(μ_l,s_l)` for a non-constant vertex.

With the split corrected to the assembly's (constant Deg-2 block, first fork Deg 3 or 4), the `N=4` kill is still Lemmas 8–9 → six graphs → Lemmas 10–15. **The SET §§2–7 survives.** No single lemma is replaced.

### 1.3 Contracted-component subtlety and determinants — (c)

Two different contracted objects are in play. FALLACY-v2, flag/place/series: they are not to be identified.

* Orevkov's `L_C` tail (MI's reading of Lemma 2.1): one per dicritical, attached at one point of `l`. At `N=4`, `K_{\mathrm{tot}}=1` sits at the affine `t` over the cusp (`μ_t=3>μ_l`). That tail maps to an affine point, hence lies in `A=L̃-L̃_∞-g̃`, **not** in `L̃_∞`.
* A contracted component of `L̃_∞` through `p̃`, mapping to `p∈L`. This is the neighbour in the resolved model. It is in `F^{-1}(L)`, F-constant, excluded from `a'` in formula (9). Minimality (2c) forbids only F-constant `(-1)`-curves, so self-intersection `<= -2` remains allowed.

The producer's verification of `(H-∞)` at `N=4` ("the unique contracted tail sits at the affine cusp, not at `p̃`") conflates these. It does **not** prove `(H-∞)`. That is OPEN even at `N=4`, as a bounded yes/no: whether a F-constant component of `L̃_∞` can map to `p` after minimality. Lemma 5 plus `det=1` for a one-contact Deg-2 block over a point *may* forbid a pure `(-2)`-chain (a `(-1)` is already forbidden), but that implication is not in DR and is not filled here.

Determinants DO uses: Lemma 5 gives the *ratio* `det Q / det(\text{target})` from `n`, `m_{p̃}`, and `Deg Q` of a constant-degree subgraph. Internal F-constant vertices, if present, are already subject to that ratio; they are not an extra free parameter in (7.3), (7.6), (7.10). Those identities are computed on the six assembled graphs, whose right arms are Deg-2 constant tubes. Inserting a contracted neighbour of local degree 2 does not change the transfer ratios those lemmas write. No displayed determinant in Lemmas 10–15 is altered by the subtlety.

### 1.4 What this does *not* do to the checked ledger

`N=4-CHECKED-CLOSED` is the unique-dicritical exclusion: `(μ,corr)=(2,1)` by DR §§2–7 with named fills, plus Prop. 4.1 for `(1,2)` and Cor. 3.8 for `(3,0)`. Item (0) does not touch Prop. 4.1, Cor. 3.8, or any identity in Lemmas 10–15. Corollary 4 remains REPLAYED-SOUND. Corollary 5's assembly remains the fill DR supplied. **Do not reopen.**

General-`N` residue, not a checked-ledger item: when `s_l>1`, Lemma 6's Deg of a linear incident chain is `s_l μ_l`, and linear non-constant vertices would have `(m,n)=(1,s_l μ_l)`, which is *not* `(s_l,μ_l)`. At every `(B3)` cell of `N=5,6` one still has `s_l=1`, so the two readings coincide. A Deg-2 *fork* is not excluded by the `N=4` Corollary 4 at `N=5` (that corollary used the four-sheet identity (9)). That is why the successor must settle BI-ATTACH before invoking a Cor. 4 analogue.

---

## 2. Item (1) — BI-1..BI-8, BI-MERIDIAN, EXTRACTION-1

### BI-1 — CONFIRMED

DF-2 / formula (9) is the generic-sheet identity `sum_{c̃ over C} Deg c̃ = N` for *every* irreducible target curve `C`, equality at every `N`. Apply it to `C=g=A_F-bar`. Components of `F^{-1}(g)` that dominate `g` split by `n`: `n>=2` are dicriticals (`n=μ_l>=2` by 7.B'; `Deg=s_l μ_l`); `n=1` are components of `Ē_X` (`E=F^*A_F` reduced by Keller, so multiplicity one). Sum of `m` over `Ē_X` is `a`. Contracted components do not dominate, hence are absent from `a'`. Thus `W+a=N`. This *is* MI `[P3]`, independently available from Lemma 4.1 at a smooth point.

**Hypotheses.** Keller; `H2` (one `g`; every dicritical has affine image `A_F`); 7.B'. No `(H-∞)`, no `SCOPE[B3-QH]`. Sanity: resolved `(1,2)` model has `W=2`, `a=0` (`E={x=0}` contracted), `W+a=N`.

### BI-2 — CONFIRMED

Local SNC coordinates at a mark `y` over `p`: `ṽ_y={u=0}`, `Ē_X={w=0}`; target `v_0={U=0}`, `g={W=0}`. A curve of source `A^2` cannot map into `L`, so `F^*U=u^{a_1}·unit` with `a_1=n(ṽ_y)`. Restrict to `Ē_X`: `F|_{Ē_X}` is `u↦U=u^{a_1}·unit`, local index `a_1`. Smoothness of `g` at `p` (`(R1)`) makes that the ramification index `e_y` of the normalised map. Sum over marks is `a` by BE Prop 3.1 (BR CONFIRMED).

**Hypotheses.** All `N`; `(R1)`, `(R2)`. Marks sit at smooth points of `L̃`, hence not at `p̃` (pairwise). No `(H-∞)`, no `SCOPE[B3-QH]`.

### BI-3 — CONFIRMED under `(H-∞)`; GAP on `(H-∞)` at `N=4`

Under `(H-∞)` the fibre `F^{-1}(p)` is finite and `sum_z deg_z F=N`. At `p̃_l`, monomial as in §1.2 with `d=0` gives local degree `s_l μ_l`. At a mark, `b_2=1` and `a_1=e_y` give `e_y`. The two families sum to `N` by BI-1, so there is no third. MEASURED: exponent det `=2=sμ` in the `(1,2)` model.

The claim "`(H-∞)` holds at `N=4`" is **not** proved by the N4-PIN tail argument (§1.3). OPEN even at `N=4`, bounded: one yes/no per dicritical, whether the unique `L̃_∞`-component through `p̃` is F-constant after minimality. If it is, BI-3 and BI-5 degrade from equalities to inequalities, as the producer already wrote for `N>=5`.

**Hypotheses of the equality.** `(H-∞)`, `(R1)`, `(R2)`, BI-1, BI-2, `H2`. No `SCOPE[B3-QH]`.

### BI-4 — CONFIRMED

BE Prop 3.1: each of the `r_p` punctures over `p` carries places of `E` at infinity of total degree `a-a_p=(r_p-1)W+K_p`. The `r_p` fibres are disjoint. In the contracted model (BR binding repair: `Φ` finite of degree `μ_t` at `t∈l'` only after contracting `L_C`) those places converge to points of `T_p` as branches `Γ` of `Ē_X` with `deg(Φ|_Γ)` the degree over `A_F-bar`. Same-branch bound `<=K_p` is E-CHARGE summed over `t∈T_p`; equality at unibranch `p`. At `K_p=0` every such branch is exchanged.

**Hypotheses.** `H2`; contracted Orevkov model; E-CHARGE as BR repaired it. No `(H-∞)`, no `SCOPE[B3-QH]`. Each `Γ` charged once, only when `Φ(Γ)=b(t)`.

### BI-5 — CONFIRMED for Deg; saturation under `(H-∞)`

DF-2 at `v_0`: `sum Deg=N`. Dicritical block contributes `W` (Lemma 6 / Prop. 1: `Deg=s_l μ_l`). Non-dicritical components carry `N-W=a`. This Deg identity does **not** use `(H-∞)` (F-constant components are already absent from `a'`).

Saturation: each `ṽ` has at most `m(ṽ)` points over `p`; writing `c_{ṽ}` for marks and using BI-2, `sum c_{ṽ} n(ṽ)=a` by BI-3 and `(H-∞)`. Then `c<=m` and `sum m n=a` force `c=m`. The ramification profile of `E~-bar→P^1` over `∞` is `{n(ṽ)^{m(ṽ)}}`, a partition of `a`. This half **does** use `(H-∞)`.

**Hypotheses.** Deg identity: BI-1, Lemma 6, DF-2, `H2`. Saturation: plus `(H-∞)`, `(R1)`, `(R2)`, BI-2, BI-3.

### BI-6 — CONFIRMED

A unit lift (`m=n=1`) has transfer factor `n/Deg=1` (DF-4), so source branch determinants equal the target ones. Two unit lifts merging over `det B>1` repeat a non-unit determinant, contradicting DF-7. With DF-6 (`det R_{v_0}=1`, `det D,L>1`) such merges are confined to the `R`-side. This is the mechanism DR uses (DR:379, 391, 448). "Coprimality kills are kills of the multiplicity of `E`'s sheets" is accurate for unit-lift merges; it does not claim every coprimality kill in Lemmas 8–9 is about `E`.

**Hypotheses.** DF-4, DF-6, DF-7. Existence of a Deg-1 component at `N=4` is Control 1(c), conditional on `(H-∞)` and Cor. 4. No `SCOPE[B3-QH]` for the mechanism.

### BI-7 — CONFIRMED. Route closed negative

B3-E-GENUS (BR CONFIRMED, `g=p_a(E~-bar)`):

```text
2 p_a  <=  1 - a + sum_p r_p max(0, (r_p-1)W + K_p - 1)  >=  1 - a.
```

Emptiness against `j<=a` (each component of `E°` covers `A_F°` of positive degree, total `a`) would need `1-p_a > a`, i.e. `2 p_a < 2-2a`. For every `a>=2`, `2-2a < 1-a`. In `(B3)`, `a>=ceil(N/2)>=2`. The covering cap never reaches the emptiness threshold. Independent check: `all((2-2*a)<(1-a) for a in range(2,20))` is true.

The `N=6`, `a=4`, three-cusps-plus-node cell has cap `-1`, hence `p_a<=-1`, hence `sum_i g_i - j + 1 <= -1`, hence `j>=2`. Constraint, not emptiness. `B3-COMPONENT` must return `j>=2` there.

**Hypotheses.** B3-E-GENUS; `j<=a` from the degree-`a` cover `E°→A_F°`; `(B3)` bound `a>=2`. No `(H-∞)`, no `SCOPE[B3-QH]`.

### BI-8 — CONFIRMED as a cap

Along a spine of constant blocks and forks outward from `l`, Deg is strictly increasing: a fork has `m>1`, the incoming arm from the dicritical has Deg `= n·e_{\mathrm{in}}` with `e_{\mathrm{in}}<m`, hence strictly smaller than the fork's `mn`. Deg is an integer, bounded above by `N` (DF-2). Starting Deg `=s_l μ_l` (Lemma 6). Number of forks `<= N - s_l μ_l`; one dicritical: `<=a`.

This is a cap, not an attainment (FALLACY-v2, floor/attainment). At `N=4`, `a=2`, DR's assembly uses exactly two forks (`A` of Deg 3 or 4, then `B` of Deg 4 when `A` has Deg 3). Tightness is exhibited against that assembly, not assumed.

**Hypotheses.** DF-2, DF-3 / Prop. 4, Lemma 6. All `N`. No `(H-∞)`, no `SCOPE[B3-QH]`.

### BI-MERIDIAN — CONFIRMED

MI Lemma 4.1 at a smooth point: fibre is `a` affine points plus, per dicritical and per each of its `s_l` points over `p`, a block of `μ_l` sheets cyclically permuted by the Lemma 3.1 normal form `u=x'`, `v={y'}^{μ_l}`. Cycle type `1^a · prod_l (μ_l)^{s_l}`. At `N=4`: `1^2·2=(2,1,1)`, reproducing N4-PIN. Sign `(-1)^{N-\#\mathrm{cycles}}=(-1)^{W-sum s_l}` is HF B3-DEGREE's `ε`.

**Hypotheses.** `H2`, 7.B', Lemma 4.1, Lemma 3.1 normal form. No `SCOPE[B3-QH]`.

### EXTRACTION-1 — CONFIRMED

DF-4/6/7/8 (Lemma 5, Prop. 3, Lemmas 2–4, edge formula) carry no `N=4` restriction beyond the *value* in DF-2. Prop. 3 needs `A_F-bar ∩ L` a single point; MI Lemma A supplies that at every `N` under `H2`. The `N`-dependence of DO is concentrated in DF-2.

**Hypotheses.** `H2` (Lemma A); Keller (étale, for DF-8's boundary support). No `SCOPE[B3-QH]`.

---

## 3. Item (2) — census closed form, recomputed

`P(m,r)` = number of integer partitions of `m` into exactly `r` parts. `f_m(z)=sum_{r>=1} P(m,r) z^r`. `Rows(m)=[z^{m+2}] f_m(z)^3` because (4.3) requires `r_L+r_R+r_D=m+2` and one partition per direction. `Census(N)=sum_{m>=2} floor(N/m)·Rows(m)`: for each `m>=2` the admissible `n` are `1,...,floor(N/m)`.

Independent exact integer computation (all partitions generated, `Poly` coefficient):

```text
 m<=6 Rows :  3, 6, 23, 51, 192
 Census    :  N=4:35   N=5:86   N=6:287
```

`Census(4)=3·2+6·1+23·1=35`. `(4,1)` sub-count `Rows(4)=23`. Brute triples of partitions of 4 with total length 6: 23. Length classes `(1,1,4)+(1,2,3)+(2,2,2)=3+12+8=23`, matching DR (5.1). `Rows(7..12)` and `Census(7..14)` match the producer (430, 1308, 3105, 8169, 18348, 46017 and 717, 2051, 5162, 13385, 31733, 77974, 177172, 405434). The affine ledger does not enter the generating function.

---

## 4. Item (3) — CONTROL 1 and CONTROL 2

### CONTROL 1 (`N=4`) — CONFIRMED for the kill-set; unit-lifts conditional

**(a) Entry.** `(C1)`+`(K)`+7.B': `2a>=N`, `a<=N-2` force `a=W=2`; `W=sum s_l μ_l` with `μ_l>=2` forces the single dicritical `(1,2)`. This is N4-PIN, independent of Orevkov Lemma 4.2. Two routes, one tuple `(m,n)(g̃)=(1,2)`. The affine data replaces DO's entry seam. **CONFIRMED.**

**(b) Which lemma fires.** Still DR §§5–7: local census Lemmas 8–9 → six graphs → Lemmas 10–15, terminating at (7.3), (7.6), (7.10). None of those three consumes an affine quantity. No single lemma fires. **CONFIRMED.** Item (0) does not change this.

**(c) `v_0`.** Deg over `v_0` is `2+2=4` (Lemma 6 + BI-5 Deg), no `(H-∞)`. B3-N4 (`SCOPE[B3-QH]` for puncture signs) gives `ε_∞=0`, two marks `e_y=1`, hence `n=1` by BI-2. Remaining Deg 2 with `n=1` is one Deg-2 fork or two unit lifts; Cor. 4 excludes the fork. **This Cor. 4 use is on the mark side, not on `B_l`.** Saturation needs `(H-∞)`, which is not verified at `N=4`. The identification of DR:534's "other two sheets" as the two places of `E` over `∞_{A_F}` is therefore **conditional**. The Deg identity `a=2` is not.

**(d) Census not shortened.** 35 raw rows enumerate fork neighbourhoods at an *arbitrary* target vertex. The affine ledger constrains the fibre over `g` and `Sing A_F`, and on the boundary only `v_0`. Six global graphs are first-fork type plus Figs. 13–16 — pure boundary data. Depth `<=a=2` reproduces DR's two merges. Index sets meet only at `v_0`. **CONFIRMED.**

### CONTROL 2 (`Γ: y^2=x^3(x-1)^2`) — CONFIRMED as `REPRESENTATIVE`

Parametrisation `(t^2, t^3(t^2-1))`. sympy 1.14.0 over `Q`: equation identity 0; `factor_list` one degree-5 factor `X^5-2X^4+X^3-Y^2`; `solve(f,f_X,f_Y)={(0,0),(1,0)}`. At `0`: orders `(2,3)`, ordinary cusp, `delta=1`. At `1`: `t=±1`, `dy/dx=±1`, transverse node, `t_1=1` odd, `delta=1`. Polynomials in `t`: no affine pole; `Z=0` gives `-X^5`, unique `[0:1:0]`. `p_a=6`, `delta_aff=2`, `delta_infty=4`, genus 0.

Instrument on `N=4`, `a=2`, dicritical `(1,2)`, points `(r,K)=(1,1)` [cusp], `(2,0)` [node]:

```text
 Deg over g           2+2=4=N                         BI-1
 fibre-at-p           2 at p̃ + marks summing to 2     BI-3 (under (H-∞))
 marks over p         2, e_y=1, n=1                   BI-2, B3-N4
 spine cap            <=2                             BI-8
 cusp                 a_p=1, load=1, all charged      BI-4, unibranch equality
 node                 a_p=0, load=4, all exchanged    BI-4, K=0
 chi_c                a(1-R)+sum a_p = 2(1-3)+1 = -3 = 1-4k
 n_infty              (R-1)a+2-2g-sum a_p r_p = 5
 g                    k_odd-1=0
 Ē_X-branches on l'   degrees (1; 2,2) at three t's   s_l=1 => #T_p=r_p
```

`Γ` is `REPRESENTATIVE`, never `A_F` for a Keller map. The run imports neither smoothness of `E` nor `χ(E)=1`: `E` is singular at the forced cusp preimage `y_0`, and `χ_c(E)=-3≠1`. The two index-1 marks and three `Ē_X`-branches of degrees `1;2,2` are licensed by BI-2/BI-4 at this type.

---

## 5. Item (4) — `N=5` and `N=6`

Admissible `(B3)` from THEOREM PROFILE + `(L)`,`(K)`,`(C1)`,`(C2)`, Lemmas 4.2/4.3, 7.B'. At both degrees `W=sum s_l μ_l` with `μ_l>=2` forces a single dicritical with `s_l=1`, hence `R=0`.

**`N=5`:** `a=3`, `W=2`, `D_{\mathrm{gap}}=1`, dicritical `(1,2)`, meridian `1^3·2`, `ε=-1`, `ρ(G)=S_5`. `sum K=2`. Charged types (partitions of 2 into `K>=1` at cusps and charged `r=2` points, at least one cusp and one multibranch):

```text
 {cusp K=2} + node           cap 1    cusp load 2 charged; node load 4, a_p=1
 {two cusps K=1,1} + node    cap 0    1+1 charged; node load 4, a_p=1
 {cusp K=1, mb K=1} + node   cap 4    1 charged; loads 6 and 4 at the two r=2 points
```

Three charged types, matching the producer. (At `N=5` a `K=0` node has `a_p=1`, not the `N=4` value 0. Loads still 4.)

**`N=6`, `a=3`:** `W=3`, `D_{\mathrm{gap}}=0`, dicritical `(1,3)`, meridian `1^3·3`, `ε=+1`, `ρ(G)⊆ A_6`. Charged types: `{cusp K=2}`, `{two cusps K=1,1}`. Caps 3 and 2. Two types.

**`N=6`, `a=4`:** `W=2`, `D_{\mathrm{gap}}=2`, dicritical `(1,2)`, meridian `1^4·2`, `ε=-1`, `ρ(G)=S_6`. `r=3` forces `K=0`, `a_p=0`. Partitions of `K_{\mathrm{tot}}=3`:

```text
 cusps (3,)           mb ()       cap  1
 cusps (1,2)          mb ()       cap  0
 cusps (1,1,1)        mb ()       cap -1     <-- three cusps; j>=2
 cusps (2,)           mb (1,)     cap  4
 cusps (1,)           mb (2,)     cap  5     <-- load 8 of which <=2 charged
 cusps (1,)           mb (1,1)    cap  7
 cusps (1,1)          mb (1,)     cap  3     <-- MISSED by the producer
```

Seven at `a=4` plus two at `a=3` is **nine** at `N=6`, not eight. The missed cell is two cusps `K=1,1` plus a charged multibranch `K=1` (Lemma 4.2 at `s_l=1`). It is `(B3)`, `sum K=a-1`, all `a_p>=0`, cap `3`, not empty. Prop. 6.2 bound `#{singular-branch}<=a-1=3` is saturated. Printed producer rows that exist match, including three-cusps cap `-1` and the load-8 row.

**No empty window.** Every enumerated cell has a consistent boundary ledger. The unique negative covering cap is `N=6`, `a=4`, three cusps + node, forced to `j>=2`, not to nothing. The missed cell does not empty anything. Bounded miss: one charged type, cap `3`.

---

## 6. Item (5) — successor well-posedness

`OPEN[BI-CENSUS-DEG5-DEG6]`: Lemmas 8–9 at `Deg<=5,6` (raw rows 86 and 287), DR §5.2–5.3 pruning redone, BI-1 / BI-5-Deg / BI-8 from the start. Bounded, combinatorial-plus-determinant. Well-posed.

Licensed spine data: start Deg `=s_l μ_l` (`2` or `3`); depth `<=a` (BI-8); non-dicritical Deg over `v_0` equals `a`.

What is **not** licensed:

* A Cor. 4 analogue ("no Deg-2 fork") at `N=5`. Cor. 4 used the four-sheet identity. At `N=5` a Deg-2 fork is a live local type. This is the residual of BI-ATTACH: settle whether the incident object is a constant Deg-2 block (Lemma 6 analogue, Deg `=sμ=2`) or can be a `(2,1)` fork. Prerequisite, as the producer said.
* The `v_0` profile list `{(1,1,1),(1,2),(3)}`. That is the list of partitions of `a=3` with **all `n=1`**. It assumes the fibre over `∞_{A_F}` is unramified, which is B3-N4's `ε_∞=0`, an `N=4` input under `SCOPE[B3-QH]`. At `N=5` the ramification profile over `∞` is exactly what BI-5-saturation would give, and that needs `(H-∞)`, which is OPEN. If some `e_y>1`, components with `n>1` appear.

`OPEN[BI-TAIL-AT-INFINITY]` remains, and extends to `N=4` (§2 BI-3). Bounded: one yes/no. If it fails, BI-3/BI-5 equalities become inequalities and every `v_0` pinning weakens.

---

## 7. FALLACY-v2 audit

Variable/ring map: DO vertex is `v`; campaign `a` is sheet count; `m`/`n`/`Deg` vs `s_l`/`μ_l` against Russian Def. 3, not a name match. Flag/place/series: `A_F`, punctures, `E`, places at infinity, marks, vertices, `l`/`l'`/`p̃` kept apart; affine `L_C` tail ≠ F-constant `L̃_∞` over `p` (§1.3); places over `∞_{A_F}` not identified with `l` at `p̃`. Carrier: `Γ` is `REPRESENTATIVE`. Floor/attainment: BI-8 is a cap; `Census(N)` is raw; Lemma 7 is a lower bound; E-CHARGE is an inequality except at unibranch points. Per-ray: each `Γ` charged once, only when `Φ(Γ)=b(t)`. Pole/interior: monomial form stated with the contracted alternative; `(H-∞)` not assumed at `N=4`. Prime labels: `l'`, `v'`, `U'`, `V'` are labels; derivatives are `f_X`, `f_Y`, `dy/dx` on `Γ`. Not filled by cap or analogy: `(H-∞)` at `N=4`, Deg-2 forks at `N=5`, the `N=5` `v_0` list, the missed `N=6` cell. No emptiness manufactured. No `charge_basis` line.

---

## 8. Typed verdict block

```text
LANE      B3-BOUNDARY-INSTRUMENT-REVIEW
SCOPE     Keller, noninvertible, H2, (B3). SCOPE[B3-QH] only for Control 1(c)
          via B3-N4. No Z(G)=1, case (A), A2, (B2), jc2-lean, ledger edit.

BI-ATTACH GAP-REPAIRED.  Split load-bearing for Cor. 5 (constant vs fork).
          Transpose is the Cor. 4-excluded Deg-2 fork, not the assembly
          object (Lemma 6 constant Deg-2 block). Kill remains SET §§2-7.
          Neighbour CONTRACTED (MEASURED det=2). Affine L_C ≠ L̃_∞ over p.
          No change to (7.3)/(7.6)/(7.10). N=4-CHECKED-CLOSED NOT REOPENED.

PROMOTE   BI-1 CONFIRMED (H2, Keller, 7.B')
          BI-2 CONFIRMED ((R1),(R2); all N)
          BI-3 CONFIRMED as equality under (H-∞); do not promote (H-∞) at N=4
          BI-4 CONFIRMED (contracted model, H2)
          BI-5 CONFIRMED for Deg=a; saturation under (H-∞)
          BI-6 CONFIRMED as DF-4/DF-7 mechanism
          BI-7 CONFIRMED; route closed negative
          BI-8 CONFIRMED as a cap; tight at N=4 exhibited
          BI-MERIDIAN CONFIRMED; reproduces (2,1,1)
          EXTRACTION-1 CONFIRMED (H2, Lemma A)
          CENSUS CONFIRMED; Census(4)=35, Rows(4)=23
          CONTROL 1: (μ,corr)=(2,1), SET §§2-7, census not shortened;
            two unit lifts conditional on (H-∞) and B3-N4
          CONTROL 2: REPRESENTATIVE PASS, every requested item
          N=5,6: NO EMPTY WINDOW; three-cusps j>=2
            GAP: N=6 charged types 9 not 8 (missed cell, cap 3)

NOT       any (B3) kill; EMPTY window; Γ as A_F; (H-∞) at any N;
CLAIMED   a general-N Cor. 4; deg A_F-bar / E-bar / κ-bar;
          the printed N=5 v_0 list {(1,1,1),(1,2),(3)}

OPENS     OPEN[BI-CENSUS-DEG5-DEG6] well-posed; 86 and 287 raw rows;
            settle BI-ATTACH first; do not use the n=1 v_0 list
          OPEN[BI-TAIL-AT-INFINITY] extends to N=4; one yes/no
          OPEN[DEG-AF-VS-N] still gates the boundary side

SUCCESSOR Well-posed as Deg<=5,6 census with BI-1/8 spine data.
          Not well-posed as a v_0 profile substitution.

MEASURED  Census(4)=35; (4,1) brute 23; Γ; attach det=2 contracted;
          charged types 3/9; three-cusps cap -1
COMPUTATION  python 3 + sympy 1.14.0 over Q; no Groebner, no AWS, no jc2-lean
DEVIATIONS   (H-∞) at N=4 opened; N=6 types 9 not 8; checked kill untouched
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30718`.
- Body SHA-256:
  `62a94bb553d010b87a976c2f72ae030e224ab340cc9cff0b2b12fcfe3d31e15b`.
- Frozen basis: `f42806e08e56732fb1d3825933eb52cb551e07c1`.
