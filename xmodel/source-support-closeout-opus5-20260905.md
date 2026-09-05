# CLOSEOUT: the SOURCE-SUPPORT THEOREM, promoted with all hypotheses named

Lane `source-support-closeout-opus5-20260905`, basis `2307078a`. The three typed residuals of the
frozen gate §4 — `OPEN[Q-IS-T1]`, `OPEN[PROP51-ELL-EXTENSION]`, `OPEN[OLD-CAP-REGRESSION-αβ]` — are
closed below. No ledger edits; no `jc2-lean`; no ideation.

## 0. Custody

Five charged inputs verified mechanically: manifest rebuilt with `awk` from the
`charged_input_<i>_sha256=`/`_basename=` lines of the `.run.v2` receipt and checked with
`sha256sum -c` — **5/5 OK** (`box/source-support-closeout-20260905/inputs.check.log`).
Printed pages read as rendered images, PDF page = printed − 139. Recomputation is in
`box/source-support-closeout-20260905/`: `alpha_beta_regression`, `q_is_t1_witness`,
`prop51_ell_validate` (`.py|.json|.out`), renders `pg*.png`.

---

## 1. `OPEN[PROP51-ELL-EXTENSION]` — CLOSED, and the printed licence is wider than the gate saw

### 1.1 A second printed Remark, on p.169

The gate cited only the p.171 Remark (Prop 4.6, condition (3) → (3)\*). **There is a second one, on
printed p.169**, and it licenses the *other* tool Prop 5.1 uses. Verbatim, p.169:

> "*Remark. With a verbatim proof, for a slightly general Jacobian condition of the following form
> (cf. Appendix II) `J_{x,y}(f(x,y),g(x,y)) = x^l`, **Proposition 4.4** is still valid with the
> condition (6) replaced by the following* (6)\* `ord T_r^ψ(σ) = (−μ_r+M_r−n)λ − 1 + δ − l =
> (deg T^ψ_{r,σ}(π)+ε)(d_r/v)λ`."

These are the only two such Remarks in the paper (`grep "still valid"` over the full text: two hits).
And p.173 opens §5 with "*Propositions 4.4 and 4.6 are our main tools*" — so **both** tools of
Prop 5.1's proof are printed as `ℓ`-valid.

### 1.2 Lemma (ℓ-extended Prop 5.1), self-contained

*Let `k` be algebraically closed of characteristic 0, `g(x,y)` monic in `y` with
`deg_y g = n > 1`, and `J_{x,y}(f,g) = c·x^ℓ`, `c ∈ k*`, `ℓ ≥ 0`. Let `δ_h` be the least
`ord(τ_i − τ_j)` over roots of `g(y)∏_{i=1}^h T_i^ψ(y)`. Then, with `M_s` the last effective
characteristic pair (p.174 Definition–Remark),*

> `δ_s = −(ℓ+1)/(n − M_s − 1)`,  hence  `d := −δ_s = (ℓ+1)/(n−M_s−1) > 0`.

*Proof.* Moh's proof (pp.173–175) is two steps, and each is a one-line arithmetic identity once the
right condition is inserted.

**Step 2 (the equality) — printed, p.171.** Prop 5.1(2) verifies Prop 4.6 at `σ` the unique `π`-root
of the `δ*`-disc with `δ = δ* = λ`, `r = h`, `v = d_h`. Condition (3)\* reads
`λ = (−1−ℓ+δ)/(n−m_r)`; substituting `λ = δ`, `m_r = M_h`:

    δ(n − M_h) = −1 − ℓ + δ  ⟺  δ(n − M_h − 1) = −(ℓ+1)  ⟺  δ_h = −(ℓ+1)/(n − M_h − 1).

The `ℓ = 0` instance is the printed `δ_h = −1/(n−M_h−1)`. The same substitution reproduces Moh's own
use of Prop 4.6 in Prop 4.5 (p.172: "*apply Proposition 4.6 with `r=r`, `λ = δ = −1`*", which via (3)
gives `n−m_r = 2`, i.e. Prop 4.5's hypothesis `M_r = n−2`) — an independent check on the reading.

**Step 1 (minimality) — needs one further, *named*, substitution.** Prop 5.1 assumes for contradiction
that `δ_h` is below the threshold, verifies Prop 4.4 (1)–(7) at `λ = δ = δ_h < 0`, `r = h`, `v = d_h`,
`ε = −1/δ_h`, and concludes `ord(τ_i−τ_j) > δ_h` for all root pairs — contradicting the definition of
`δ_h`. Under (6)\* the same computation gives `(1+ε)(d_r/v)λ = −1−ℓ+δ`, hence `ε = −(ℓ+1)/δ > 0 > −1`,
so condition (7) still holds. But Prop 4.4's condition (3), `λ < (−1+δ)/(n−M_i)`, is **not** among the
conditions the p.169 Remark replaces, and with `λ = δ` it reads `δ < −1/(n−M_i−1)`.

**The needed shift is (3) → (3)^ℓ: `λ < (−1−ℓ+δ)/(n−M_i)`.** It is unprinted, but it is the *same*
substitution, at the place it comes from and for the printed reason. Prop 4.4's (3) is inherited from
Prop 4.2, whose proof displays the equivalence verbatim (p.165):

> `λ < (−1+δ)/(n−M_{r+1})  ⟺  nλ + (−μ_{r+1})λ − 1 < −2 + δ + (−μ_{r+1}+M_{r+1})λ`
> "*Thus the left hand side of equation (1) of Proposition 4.1 with `h = T^ψ_{r+1}` has a smaller
> formal order.*"

So the `−1` in that numerator is the order of the Jacobian side of Prop 4.1's equation (1) — the same
`−1` that becomes `−1−ℓ` in (3)\* on p.171, where the p.170 proof shows the mirror-image equality
version of the identical display. Replacing `J = 1` by `J = x^ℓ` lowers that order by `ℓ` in the
inequality exactly as it does in the equality.

**The shift is forced by Moh's own printed table, not chosen.** With (3) unshifted, Step 1 would
yield `δ_s ≥ −1/(n−M_s−1)`; all four `u_3 = 1` descendants tabulated on printed p.207 violate it
(`−1 < −1/2`, `−1/2 < −1/4`, `−1 < −1/2`, `−1 < −1/3`). Appendix II is itself a refutation of the
"only (6) shifts" reading of the p.169 Remark. ∎

### 1.3 Numerical validation (`prop51_ell_validate.out`)

| source | rows | `−(ℓ+1)/(n−M_s−1)` | `ℓ=0` form `−1/(n−M_s−1)` |
|---|---|---|---|
| Moh Appendix II, printed p.207 | 4 | **4/4** | **0/4** |
| frozen campaign fibres | 12 | **12/12** | — |

The `ℓ=0` column is the new content: the table does not merely *agree* with the `ℓ`-form, it
*excludes* the `ℓ`-free one on every row, including the `ℓ=2` (`J = x²`) row `(15,10; M=11)`.

**Status.** Closed to: *two of the three inputs are printed verbatim (Props 4.4, 4.6 under `J = x^ℓ`);
the third — Prop 4.2/4.4 condition (3) → (3)^ℓ — is the same substitution at its printed source, and is
forced by Moh's own p.207 values.* No longer a bare "re-run claim". Generality is unchanged: `ℓ+1 ≥ 1`,
`n−M_s−1 ≥ 1` by p.174, and an effective terminal always exists since `M_1 = −m < 0 < n−1`, so
`δ_s ≤ −(ℓ+1)/(n−1) < 0` at every degree.

---

## 2. `OPEN[Q-IS-T1]` — CLOSED: descent does not need to commute with the root replacement

The gate asked whether `Q' = T_1'^{ψ'}(P')` for a licensed descendant. The printed answer makes the
question narrower than it looked.

**The descended pair is literally `(g, T_1^ψ)`, not `(f, g)`.** Printed p.198, proof of Prop 6.3
conclusion (3), verbatim:

> `J_{γ,π}(ḡ(σ), T̄_1^ψ(σ)) = J_{γ,π}(x,y)·J_{x,y}(g(x,y), T_1^ψ(f(x,y),g(x,y))) = J_{γ,π}(x,y) = −u_s/(b γ^{v_s−u_s−1})`.

So Prop 6.3 descends `(g, T_1^ψ)`; its second member `Q' = T̄_1^ψ(σ)` **is** the image of `T_1^ψ`
under the monomial descent, by construction. The exponent `v_s−u_s−1` is the campaign's `ℓ` (12/12).
Prop 6.3(2) also prints `deg_π ḡ(σ) = u_s n/d_s = n'`, `deg_π T̄_1^ψ(σ) = u_s(−μ_1)/d_s = m'`.

**What remains is not commutation but a gauge.** The descendant's own replacement `T_1'^{ψ'}(P')`
differs from `Q'` by a polynomial in `P'` (p.171: "*`T_1^ψ = f + polynomial in g`*"; p.200 is Moh's own
use of `f = T_1^ψ`). That change is Jacobian-free — `J(P',Q'+p(P')) = J(P',Q')` — and fixes `P'`, so it
is a group action on the pair, not a restriction of the family. The **only** thing it can spoil is the
row datum: if `deg_y T_1'^{ψ'} ≠ deg_y Q'` the normalised pair sits on a different census row.

**That is exactly what `M_1' = −m'` certifies.** Printed p.185: "*`deg T_1^ψ(f(x,y),g(x,y)) =
deg_y T_1^ψ = −M_1`*". So `M_1' = −m'` says the descendant's own `T_1'^{ψ'}` has `y`-degree `m'`,
i.e. **the normalisation is degree-neutral on that row** and the datum `(n',m',M',ℓ,s')` is unchanged.

**Witness (`q_is_t1_witness.out`), 12/12 on each of three checks:** `M_1' = −m'` (p.185 identity ⇒
normalisation degree-neutral); `ℓ = v_s−u_s−1` (Prop 6.3(3) exponent); `M_s' ≤ n'−2` (p.174
Definition–Remark ⇒ `d` well-defined).

**Status.** `Q = T_1^ψ(P)` is *not* an extra restrictive hypothesis on descendants: it is a
Jacobian-free normalisation available whenever `M_1 = −m` holds for the row, and it is what puts
`Q`'s roots inside `D_s` via printed p.179 ("*the minimal disc `D_s` which contains all roots of
`g(y)∏_{i=1}^h T_i^ψ(y)`*"). It must still be **named** in the theorem, since the containment is
consumed there; the residual generic obligation is the checkable side condition `M_1 = −m`, met on all
12 rows. FALLACY-v2 note: this is a claim about the *pair*, not an identification of `T̄_1^ψ(σ)` with
the descendant's `T_1'^{ψ'}(P')`; those agree only up to `+p(P')`, and no such identification is used.

---

## 3. `OPEN[OLD-CAP-REGRESSION-αβ]` — CLOSED: the definitive (fibre, block) table

`alpha_beta_regression.py` tests `G_i ⊆ I^old_i` on all **12 fibres × 72 blocks** (`h`; `α_i`, `i=1..e`;
`β_i`, `i=2..q`), with the `(0,0)` translation gauge removed from `α_e`, `β_q` exactly as
`verify_source_complete.py:62-63` does. Ground truth for `I^old` is the *emitting code*:

- `h` : `…/before/sprime3_compiler.py::h_inventory_necessary` —
  `{0≤b≤max(u,0), b+a≤K, (b,a)≠(0,K), −b+δ_1'a ≥ B_safe}`, `u = K−V_2`.
  (`orderbasis-20260903/order_basis_full.py::h_inventory` uses `b+a<K`, a subset — failures persist
  a fortiori.)
- `α_i`, `β_i` : `…::coeff_inventory_envelope(C,i)` — `{0≤a<K, b ≤ ⌊δ_1'a − i·B_safe⌋, b+a ≤ i·K}`.
  **No `u`-cut at `α/β`** in the emitted code; the `u`-cut question is `h`-only.

**Control.** `G_i \ (uncapped D1 floor)` reproduces the frozen `h_/alpha_/beta_added_beyond_raw` of
`support-completion.json` on **72/72 blocks** (`xcheck_all_agree=True`). The gate's §3.d `h`-block
test replicates exactly: same 4 fibres, escapee counts 11 / 11 / 20 / 3, and `V4_9`'s three escapees
are again `(3,0),(3,1),(4,0)`.

### 3.1 The definitive regression list — where the old inventories were **FALSE**

"FALSE" = a point of `G_i` satisfies the chart's **own** `D1` floor at the same threshold and is
nevertheless deleted by a cap. That isolates the cap as the false conjunct, with no appeal to a
coordinate change.

| fibre (class · V) | `K` | `d` | FALSE blocks | escapee counts (TOT / UCUT) |
|---|---|---|---|---|
| `n16m12_M6_13_ell3_s3_V1_1` | 4 | **2** | `h a1 a2 a3 a4 b2 b3` | h 10/9; a1..a4 10,26,42,58; b2,b3 26,42 (all TOT) |
| `n16m12_M6_13_ell3_s3_V1_3` | 4 | **2** | `h a1 a2 a3 a4 b2 b3` | identical to V1_1 |
| `n16m12_M6_13_ell3_s3_V4_3` | 4 | **2** | `h a1 a2 a3 a4 b2 b3` | h 10/**20**; α/β identical to V1_1 |
| `n24m18_M9_20_ell1_s3_V4_9` | 6 | 2/3 | `h` only | h 0/3 — `(3,0),(3,1),(4,0)` |
| the other **8** fibres | — | ≤ 1 | **none** | — |

**22 of 72 blocks; 4 of 12 fibres.** The `α/β` extension does **not** enlarge the fibre set — the
gate's `h`-block answer was already complete at fibre granularity — but it enlarges the block set
from 4 to 22, which is what matters, since a banked kill is regressed by *any* one false block.

The two caps fail for the two reasons the gate identified, now confirmed at every block:

- `b+a ≤ i·K` fails **iff `d > 1`**, i.e. `ℓ+1 > n'−M_s'−1` — only the `(16,12; 6,13; ℓ=3)` class
  (`d = 2`), and there in *every* block `h`…`β_3`, escapee count growing with `i` (10, 26, 42, 58).
- `b ≤ K−V_2` has no outer-disc derivation at all and fails additionally at `V4_3` and `V4_9`. Since
  the emitted `α/β` inventories carry no `u`-cut, that failure is **confined to the `h` block**, so
  `V4_9` is FALSE at `h` and clean at `α/β`.

### 3.2 What is *not* on that list, and why

Testing `G_i ⊆ I^{D1}` (the `17(nnnnn)`-repaired, uncapped state) fails on **11 of 12 fibres / 66 of
72 blocks** — every fibre but the `s'=4` control `n24m16_Mm12_m2_5_ell1_s4_V1_1_6`, clean in every
block against both `I^cap` and `I^{D1}`. That larger set is **not** in the regression list: those
exclusions come from the `D1` order floor itself, Moh's Theorem 1.2 read in the `D1`-centred
coordinate, whereas `G_i` lives in the `φ = (x, y+η)` coordinate. Calling them "false" would be the
FALLACY-v2 flag/place identification. They are a **normalisation gap** — the one Astra's union
`S_i = D_i ∪ G_i` repairs — already recorded block by block in the frozen `support-completion.json`.

**Regression set of `17(zzzzzz)`/`(aaaaaaa)` is final: 4 fibres, 22 blocks, listed above.**

---

## 4. THE SOURCE-SUPPORT THEOREM — citable statement

> **Theorem (source support).** Let `k` be algebraically closed of characteristic `0`. Let `(P,Q)` be
> polynomials in `k[x,y]`, monic in `y`, with `deg_y P = n' = eK`, `deg_y Q = m' = qK`,
> `K = gcd(n',m')`, `q ≥ 2`, and `J_{x,y}(P,Q) = c·x^ℓ`, `c ∈ k*`, `ℓ ≥ 0`. Assume:
>
> **(H1) Licensed descendant.** `(P,Q)` is a Prop 6.3 descendant of a minimal Jacobian source, with
> effective characteristic data in the sense of the p.174 Definition–Remark, so `M_s' ≤ n'−2`.
>
> **(H2) `Q` is the root replacement.** `Q = T_1^ψ(P)` — equivalently, by printed p.185, the row
> satisfies `M_1 = −m'`. This is a Jacobian-free normalisation, not a restriction (§2).
>
> **(H3) Terminal radius.** `d := −δ_{s'} = (ℓ+1)/(n' − M_s' − 1) > 0`, by the `ℓ`-extended Prop 5.1
> (§1.2). `d > 0` always holds under (H1).
>
> Let `η(x) = −[y^{N−1}]Q / N ∈ k[x]`, `N = deg_y Q`, `φ = (x, y+η(x))`, and
> `G_i = {(b,a) : 0 ≤ a < K, 0 ≤ b ≤ ⌊d·(iK − a)⌋}`. Then after `φ`, with `h` the `q`-th approximate
> root of `Q`, `P = h^e + Σ_{i=1}^{e} α_i h^{e−i}` and `Q = h^q + Σ_{i=2}^{q} β_i h^{q−i}`:
>
>   `supp(h − y^K) ⊆ G_1`,  `supp α_i ⊆ G_i` (`i=1..e`),  `supp β_i ⊆ G_i` (`i=2..q`),  **`β_1 = 0`**,
>
> and the constant terms of `α_e`, `β_q` may be gauged to `0` by translating `P`, `Q` by constants.

`(H1)`–`(H3)` are all the theorem needs; `k` infinite is used only to realise `deg = deg_y` for both
members at once. `φ` has determinant 1 and preserves polynomiality, `y`-monicity, both `y`-degrees,
`J = c x^ℓ` and all pairwise root contacts, so no root datum moves. The conclusion is a **necessary
over-approximation**: a chart containing `G_i` in every block receives every actual source pair, so
`UNIT` on it is a kill; `NONUNIT` proves nothing about any fibre. `D_i` is decorative — the proved
chart is `G_i`, smaller than `D_i` on five of the six classes. `d` and `|G_1|` depend only on
`(n', M_s', ℓ)`, so `G_i` is the same support for every `V`-label in a class — the coverage map behind
Astra's six-class consumption rule.

---

## 5. What may now be cited, and what is still open

- §4, with `(H1)`–`(H3)` named, may be cited as a general, all-degree necessary-support theorem for
  licensed descendants.
- `δ_s = −(ℓ+1)/(n−M_s−1)` may be cited with the p.169 **and** p.171 Remarks plus the single named
  (3) → (3)^ℓ substitution of §1.2, which Moh's p.207 table forces (`4/4` for, `0/4` against).
- The regression set is **4 fibres / 22 blocks** (§3.1); the `11 fibres / 66 blocks` of §3.2 are
  `NORMALISATION-GAP`, not refutations.
- Untouched and still typed: `OPEN[CENSUS-COVERAGE-ALL-DEGREE]`, `OPEN[SKELETON-DECORATION]`,
  `OPEN[SPLIT-WINDOW-CLASSIFICATION]`, `OPEN[SPLIT-TO-JOINT-MAP]`, `OPEN[U-NEGATIVE-CHART]`,
  `OPEN[DESCENT-STATE-S>2]`, `OPEN[K4-SHAPE-AND-UNIFORM-KILL]`.
- New, small, typed here: `OPEN[PROP42-ELL-CONDITION3]` — obtain a printed or fully written
  justification for `λ < (−1−ℓ+δ)/(n−M_{r+1})` in Prop 4.2 under `J = x^ℓ`. Everything downstream
  already treats it as true (p.207 requires it); this records that the paper states the `ℓ`-Remark
  only for Prop 4.4's condition (6).

No exit-price assertion is made here, so no `charge_basis` line is due: the source-support theorem
consumes no exit price and asserts none.

## References consumed

- T. T. Moh, *J. Reine Angew. Math.* **340** (1983) 140–212: printed pp. 165, 168–171, 173–175, 179,
  185, 197–198, 200, 207 (PDF page = printed − 139), read as rendered page images.
- `first-separation-gate-opus5-20260905.md` §§1–5; `moh-hsupport-gate-astra-20260905.md` §§4–5, 8;
  `first-separation-lemma-sol56-20260905.md` §§0–3; `FALLACY-v2.md` (flag/place, floor/attainment).
- Frozen artifacts: `box/moh14-charts-20260905/hsupport-gate-20260905/{classes_manifest.json,
  source-complete/support-completion.json, verify_source_complete.py, before/sprime3_compiler.py}`;
  `box/orderbasis-20260903/order_basis_full.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16386`.
- Body SHA-256:
  `a598beaf7f85ab9ab19805d052a6e124340fb85c2ec49fdd39f28b9438151ff1`.
- Frozen basis: `2307078a3141a760c911018f98bd26cf553576a1`.
