# Source-typing lane: dicritical hypotheses (D1)--(D4)

**Lane.** Bounded source-audit of the untyped bridge between Chau's dicritical *series* and Orevkov's dicritical *lines*.
**Charged input.** `block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md`
**SHA-256 (verified).** `ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9`
**Date.** 2026-08-31
**Scope.** Primary-source typing of (D1)--(D4); companion-sheet floor `f(B_i) >= 1`. No CAS. No `jc2-lean`. No edits to canonical ledgers or charged files. No `charge_basis` line: this lane asserts no new exit price.

Throughout, a dicritical *series* is a Newton--Puiseux object `φ(x,ξ)`; a dicritical *line* (Orevkov component) is an irreducible compact curve in a regular compactification. These are not identified except where a cited source supplies a map between them.

---

## 0. Charge, hash, and constraints

The frozen copy

```text
/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kTgXaB/inputs/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

rehashes to `ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9`, matching the charge. Stop condition not triggered.

The reviewer's §5 isolates the untyped step in Lemma 2.2 of the reducible-tree ledger: Chau 2004 Lemma 1 produces a dicritical *series* `φ` and a nonconstant curve `f_φ(C)`; the next sentence replaces it by an Orevkov dicritical *line* `l ⊂ L_F` and replaces `deg f_φ > 0` by `μ_l ≥ 1`. The weakest repair named there is

```text
(D1) every Orevkov l in L_F has one irreducible nonconstant image alpha(l);
(D2) alpha: L_F -> Irr(A_F) is surjective;
(D3) mu_l is a positive integer for every such l;
(D4) N-1 = sum_l (mu_l + corr_l), with every corr_l >= 0.
```

Computation in this lane is reading, quotation, and desk-scale deduction only.

---

## 1. Primary sources obtained

### 1.1 Orevkov 1987 (degree-at-infinity identity; "Lemma 4.2")

**Obtained.** Author-hosted English PDF of the paper whose journal translation is the 1987 text.

| field | value |
|---|---|
| Russian original | S. Yu. Orevkov, *On three-sheeted polynomial mappings of C²*, Izv. Akad. Nauk SSSR Ser. Mat. **50** (1986), no. 6, 1231–1240 |
| English translation | *Math. USSR-Izvestiya* **29** (1987), 587–596 |
| DOI | `10.1070/IM1987v029n03ABEH000984` |
| Math-Net | `https://www.mathnet.ru/eng/im1571` |
| Author PDF | `https://www.math.univ-toulouse.fr/~orevkov/jc86.pdf` |
| Local copy | `refs/jc86.pdf` |
| SHA-256 | `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db` |

The PDF is the author-retyped AMS-TeX English text (creation date 2011-01-12). It contains Lemma 4.2, Corollary 4.3, the definitions of `L`, `L_∞`, `L_FC`, `L_C`, `L_F`, and the multiplicity used in (D3)--(D4). It does not use the word "dicritical".

### 1.2 Chau 1999 Remark 4.9 (secondary restatement)

**Obtained.**

| field | value |
|---|---|
| Citation | Nguyen Van Chau, *Non-zero constant Jacobian polynomial maps of C²*, Ann. Polon. Math. **71** (1999), 287–310 |
| DOI | `10.4064/ap-71-3-287-310` |
| Local copy | `refs/chau1999_apm71_full.pdf` |
| SHA-256 | `ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7` |

The scan is two-column; OCR of the displayed formulae is imperfect. Verbatim prose of Remark 4.9, Definition 3.4, Theorem 4.4, and the function-level correspondence on pp. 291–292 is recoverable. Formulae (4.9) and (4.10) are quoted below from the layout extraction, with uncertain glyphs flagged.

### 1.3 Le Van Thanh--Chau / Chau 2004 ("Lemma 1", "Corollary 2")

**Chau 2004 obtained. A joint "Le Van Thanh--Chau 2004" paper containing these two statements was not found.**

Searches for "Le Van Thanh" + Chau + dicritical / nonproper / Jacobian returned no 2004 paper. The nearest names in the same literature are Lê Dũng Tráng--Weber 1995 (cited by Chau as `[LW]`) and Ha--Lê 1984. The statements the charge names sit in Chau's sole-authored 2004 note, which the rank-four integration already pins at `5d7df7ce...:66-70`.

| field | value |
|---|---|
| arXiv | Nguyen Van Chau, *Non-proper value set and the Jacobian condition*, arXiv:math/0305088v1, 6 May 2003, `https://arxiv.org/pdf/math/0305088` |
| Journal | *Note on the Jacobian condition and the non-proper value set*, Ann. Polon. Math. **84** (2004), 203–210, DOI `10.4064/ap84-3-2` |
| Local copy | `refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf` |
| SHA-256 | `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f` |

The arXiv v1 PDF contains Lemma 1 (dicritical-series covering of `A_f`, cited as "Lemma 4, [C]" i.e. Chau 1999) and Corollary 2 (one set-theoretic point at infinity). The journal note is the published form of this arXiv; the integration treats them as the same statements.

### 1.4 Sources sought and unobtainable

- **Le Van Thanh--Chau 2004.** Unobtainable as a bibliographic object. The Lemma 1 / Corollary 2 pair is Chau 2004, §1.3.
- **Official Math. USSR-Izv. typeset PDF of Orevkov 1987.** Not downloaded from IOPScience; the author English PDF and Math-Net record identify the same Lemma 4.2. No statement below is reconstructed from memory of the journal typesetting.

**Auxiliary source used only to type lines, not series** (not named in the charge, obtained because the series-to-line gap is the attack):

| field | value |
|---|---|
| Citation | Nguyen Van Chau, *Pencil of irreducible rational curves and plane Jacobian conjecture*, arXiv:0905.3939v3; Ann. Polon. Math. **101** (2011), 47–53 |
| URL | `https://ar5iv.labs.arxiv.org/html/0905.3939v3` and `https://arxiv.org/pdf/0905.3939` |

This paper defines a dicritical *component* of a map `F` (an irreducible curve in the compactification) and writes `A_F` as the union of the affine images of those components. Hypotheses: polynomial map `C² → C²` with finite fibres. Keller maps satisfy that (Jacobian never zero, so affine fibres are finite).

---

## 2. Typed statements extracted (verbatim)

**Orevkov §2, definitions of the boundary curves.** After regularizing `f : C̃² → C²` by blowups at infinity, with `X̃` the resulting smooth compact surface:

> We also introduce the following notation: `L = X̃ − C̃²`, `L_∞ = f⁻¹(P¹ × P¹ − C²)`, and `L_FC = L − L_∞`. Since `f(C̃²) ⊂ C²`, we have the inclusion `L_∞ ⊂ L`. Finally we denote by `L_C` the union of those irreducible components of `L_FC` on which `f` is constant, and by `L_F` the curve `L_FC − L_C`.

**Orevkov Lemma 2.1(a),(c)** (hypotheses: the regularisation of §2; `K` a connected component of `L_FC`):

> a) `K` intersects `L_∞` at a unique point `p`, and `f(K − p) ⊂ C²`.
> c) `ℓ_k ⊂ L_F`, and `ℓ_i ⊂ L_C` for `1 ≤ i ≤ k−1`.

So each connected component of the finite-value boundary is a linear chain of rational curves whose unique nonconstant endpoint is in `L_F`.

**Orevkov multiplicity (opening of §4).**

> Let `φ : A → B` be a continuous mapping of topological spaces. By the multiplicity of `φ` at `x ∈ A` we mean the largest number `k = μ_x φ` such that in every neighbourhood of `x`, there are points `x_1, …, x_k` such that `φ(x_1) = ⋯ = φ(x_k)`.

If `φ(A) = B` and `∑_{a ∈ φ⁻¹(b)} μ_a φ = μ_φ < ∞` independently of `b`, then `φ` is of constant multiplicity `μ_φ`.

After contracting `L_∞` to a point `∞` and each connected component of `L_C` to a point, `f` induces a constant-multiplicity map `f* : X̃* → X*` of multiplicity `N`. For each irreducible curve `ℓ ⊂ X̃`, `μ_x f*` is generically constant on `π(ℓ)`; that constant is written `μ_ℓ f*`.

**Orevkov Lemma 4.2** (hypotheses: the regularised map of §2, the collapse to `f*` of constant multiplicity `N`; outer sum over irreducible components of `L_F`):

> `∑_{ℓ ⊂ L_F} [ μ_ℓ f* + ∑_{x ∈ π(ℓ)−{∞}} (μ_x f* − μ_ℓ f*) ] = N − 1`
>
> where the outer sum is takes over all irreducible components of `L_F`.

Immediately after the display:

> Although the inner sum in (4) is taken over all points of `π(ℓ)−{∞}`, it is clear that it can contain only finitely many nonzero summands. Moreover, from an obvious property of the semicontinuity of the multiplicity, it follows that each summand in the inner sum is nonnegative, and we get
>
> **Corollary 4.3.** `∑_{ℓ ⊂ L_F} μ_ℓ f* ≤ N − 1`
>
> where the equality is attained if and only if `μ_x f* = μ_ℓ f*` for each irreducible component `ℓ ⊂ L_F` and for all points `x ∈ π(ℓ)`, `x ≠ ∞`.

**Orevkov Lemma 5.2** (used only to see that `f*(ℓ*)` is a curve germ, not a point): if `x` lies on `ℓ* = π(ℓ)` for `ℓ ⊂ L_F` and `μ_x f* = μ_ℓ f*`, then a germ of `f*|ℓ*` at `x` "determines a nonsingular branch of the curve `f*(ℓ*)` at `f*(x)`".

**Chau 1999, Definition 3.4** (hypotheses: `f = (P,Q)` a polynomial map, `P,Q` monic in `y`; `π`-series as in §2):

> A `π`-series `φ` is a dicritical series of `f` if either `[φ] ∈ Π_P` and `b_φ ≤ 0` or `[φ] ∈ Π_Q` and `a_φ ≤ 0`.

**Chau 1999, function-level correspondence** (for a single polynomial `g`, not for the map `f`; pp. 291–292):

> There is a natural one-to-one correspondence `φ : [φ] ↦ ℓ` between `Π_g` and the collection of all dicritical (horizontal) components `ℓ` of the divisor curve `D` in a regular extension `g*` of `g`, `g* : M = C² ⊔ D → CP`, which can be obtained by resolution of singularities (cf. `[LW]` and `[O1]`). […] This observation is not used in this paper.

**Chau 1999, Theorem 4.4** (hypotheses: `f = (P,Q)` non-zero constant Jacobian, monic in `y`):

> `E_f = ⋃_{[φ] ∈ Π_f} C_{[φ]}`,
>
> where `C_{[φ]} = {(P_φ(ξ), Q_φ(ξ)) : ξ ∈ C}`, together with (E1) `deg P_φ / deg Q_φ = deg P / deg Q`; (E2) if `i_φ > 1` then `0 ∈ E_φ` and `(P_φ, Q_φ)(0)` is a singular point of the image germ; (E3) every curve `C_{[φ]}` has a singularity.

For Keller maps the critical-value set is empty, so `E_f = A_f`.

**Chau 1999, Remark 4.9** (reconstructed from layout; displayed sums have OCR noise; the prose and the citation of Orevkov Lemma 4.2 are stable):

> In `[O1]` Orevkov constructed a reduction `f*` of a regular extension of `f`, `f* : (C² ⊔ D ⊔ {∞}, D, ∞) → (C² ⊔ {∞}, E_f, ∞)`, where `D` is the union of a finite number of curves homeomorphic to `C`. From this Orevkov obtained a nice formula for the geometric degree of `f`:
>
> `deg_geo f − 1 = ∑_{ℓ ⊂ D} [ μ_ℓ + ∑_{u ∈ ℓ} (deg_u f* − μ_ℓ) ]`  (4.9)
>
> (Lemma 4.2 of `[O1]`), where `μ_ℓ` is the degree `deg_u f*` for generic `u ∈ ℓ`. […] It is possible to rewrite Orevkov's formula in terms of the data of `Π_f` and to obtain the following formula (4.10) [a sum over `[φ] ∈ Π_f` of local degrees of the chart maps `F_φ`]. […] This formula can also be obtained in the way used for Theorem 4.5 and the equalities (4.4) and (4.8) on Euler–Poincaré characteristics.

Remark 4.9 therefore *claims* a rewrite of the outer sum over Orevkov's `D` (homeomorphic copies of `C`, i.e. the affine parts of `L_F` components) as a sum over dicritical-series classes. It does not prove a numbered bijection `Π_f ↔ L_F`. The function-level correspondence quoted above is explicitly unused in that paper.

**Chau 2004, definition of a dicritical series and Lemma 1** (hypotheses of the paper: `f = (P,Q)` polynomial, `J(P,Q) ≡ const ≠ 0`, degrees `deg P = Kd`, `deg Q = Ke`, `gcd(d,e) = 1`; the monic-in-`y` form (5) is assumed after a coordinate change that does not change `A_f`). A series `φ(x,ξ)` of the displayed Newton--Puiseux shape (7) is dicritical if

> `f(x, φ(x,ξ)) = f_φ(ξ) + lower terms in x, deg f_φ > 0`.

> **Lemma 1.** (Lemma 4, `[C]`)
> `A_f = ⋃_{φ is a dicritical series of f} f_φ(C)`.

The proof of Lemma 1 states both directions, and is the precise series-to-chart bridge:

> If `φ` is a dicritical series of `f` of the form (7), we can define the map `Φ(t,ξ) := (t^{−m}, φ(t^{−m}, ξ))`. Then, `Φ` sends `C* × C` to `C²` and the line `{0} × C` to the line at infinity of `CP²`. The polynomial map `F_φ(t,ξ) := f ∘ Φ(t,ξ)` sends the line `{0} × C` into `A_f ⊂ C²`. Therefore, `f_φ(C)` is an irreducible component of `A_f`, since `deg f_φ > 0`. Conversely, if `ℓ` is an irreducible component of `A_f`, […] we can construct a unique dicritical series `φ(x,ξ)` such that […] `f_φ(C) = ℓ`.

**Chau 2004, Corollary 2** (same hypotheses as Theorem 1; `A_f ≠ ∅`):

> If `A_f ≠ ∅`, then `A_f` is a curve with one point at infinity and the irreducible branches at infinity of `A_f` have Newton--Puiseux series of the form `u = c v^{d/e} + lower terms in v` with coefficients `c` to be `d`-radicals of `B^d / A^e`.

This is the one *set-theoretic* infinite point. It does not say that a reducible `A_f` has one analytic place.

**Chau 2011, dicritical *components*** (hypotheses: polynomial `F = (P,Q) : C² → C²` with finite fibres; `f = (p,q)` a regular extension to a compactification `X` of `C² \ B`):

> By a dicritical component of `F` we mean an irreducible component `ℓ ⊂ D_∞` such that `(p_ℓ, q_ℓ)` is a non-constant mapping. Obviously, by the definitions
>
> `A_F = ⋃_{ℓ dicritical components of F} (f(ℓ) ∩ C²)`.
>
> In particular, `F` is a proper map of `C²` if and only if `F` does not have dicritical components.

And, as a supporting identity in the same paragraph block: `A_F = f(D_∞) ∩ C²`.

Orevkov's `L_F` is exactly this class of objects: irreducible components of the compactification-at-infinity on which the regularised map is nonconstant. Chau 2011 does not quantify `μ_ℓ`.

---

## 3. Verdicts on (D1)--(D4)

Notation of the campaign form: `F` is a Keller map of geometric degree `N`, `A_F` its nonproper-value curve, `L_F` Orevkov's nonconstant finite-value boundary, `α(ℓ)` the Zariski closure in `C²` of `f(ℓ \ {p})` (equivalently `f*(π(ℓ) \ {∞}) ∩ C²`).

### 3.1 (D1)

**Verdict: SOURCED**, with a one-line derived irreducibility.

- Orevkov's definition of `L_F` plus Lemma 2.1(a) give: `f` is nonconstant on `ℓ`, and `f(ℓ \ {p}) ⊂ C²`. Lemma 5.2 gives that the generic germ of `f*|ℓ*` is a curve branch, not a point. Chau 2011's definition of a dicritical component is the same nonconstancy, and writes the affine image `f(ℓ) ∩ C²`.
- The image of an irreducible curve under a nonconstant holomorphic map is irreducible, so `α(ℓ)` is a single irreducible nonconstant affine curve. One irreducible source curve cannot have two distinct irreducible curves as its Zariski image.

This is not Chau 2004 Lemma 1. Lemma 1 produces `f_φ(C)` from a *series*. (D1) is a statement about Orevkov *lines*. The sourced line-level statements are Orevkov §2 + Lemma 2.1 and Chau 2011's definition.

### 3.2 (D2)

**Verdict: SOURCED at line level by Chau 2011; SOURCED at series level by Chau 2004 Lemma 1; the series-to-line identification is DERIVED, not a numbered theorem in the 1987/1999/2004 trio.**

Surjectivity `Irr(A_F) ← {dicritical components}` is Chau 2011's displayed union, under finite fibres (true for Keller maps). Each irreducible component of `A_F` appears as the affine image of some dicritical component because the union *equals* `A_F` and each summand is irreducible (or has irreducible closure).

Surjectivity `Irr(A_F) ← {dicritical series}` is Chau 2004 Lemma 1, both directions, under the Jacobian condition.

The missing map in the ledger's Lemma 2.2 is series → line. What the sources actually give:

1. Chau 2004 Lemma 1 *proof*: the chart `Φ(t,ξ) = (t^{−m}, φ(t^{−m},ξ))` sends the line `{0} × C` to the line at infinity of `CP²`, and `F_φ` sends that line into `A_F`. That `{0} × C` is a local chart on a compactification component on which `f` is nonconstant, hence (after the remaining blowups of Orevkov §2) an irreducible component of `L_F`.
2. Orevkov Lemma 2.1: each connected component of `L_FC` is a linear chain with a unique `L_F` endpoint. This matches Chau 2004's associated sequence `{φ_i}` (intermediate series constant/polar, last series dicritical).
3. Chau 1999 Remark 4.9 *claims* that Orevkov's outer sum over `ℓ ⊂ D` rewrites as a sum over `[φ] ∈ Π_f`, and says the rewrite "can also be obtained" from Chau's own Euler formulae. It does not prove bijectivity.
4. Chau 1999's 1–1 correspondence `[φ] ↦ ℓ` is stated for a *function* `g`, and the paper says it is not used there.

Desk derivation of the campaign map `α`: send each Orevkov `ℓ ⊂ L_F` to `α(ℓ) :=` Zariski closure of `f(ℓ \ {p})`. Chau 2011 says the images cover `A_F`. Chau 2004 Lemma 1 plus the `Φ`-chart says every series-realised component is the image of the corresponding `t = 0` line, which is an `L_F` component. Distinct target components cannot share one irreducible source image, by (D1). This is the derived `α : L_F → Irr(A_F)` of the campaign, and it is surjective.

It is **not** sourced as a named bijection in Orevkov 1987, Chau 1999, or Chau 2004. The ledger's silent replacement "series `φ` ↝ line `ℓ ⊂ L_F`" is the gap the reviewer named. Chau 2011 closes the *covering* at line level without passing through series. The 1999 function-level correspondence does not, by itself, license the replacement.

### 3.3 (D3)

**Verdict: DERIVED from Orevkov's multiplicity, not from `deg f_φ > 0`. The ledger's deduction is a false identification.**

Orevkov defines `μ_ℓ f*` as the generic value of `μ_x f*` on `π(ℓ)`. The number `μ_x φ` is the largest `k` such that every neighbourhood of `x` contains points `x_1,…,x_k` with the same image. The point `x` itself lies in every neighbourhood of `x`, so `k = 1` always works at every point of the domain of `f*`. Hence `μ_x f* ≥ 1`, hence `μ_ℓ f* ≥ 1` for every `ℓ ⊂ L_F` (those components survive in `X̃*`: only `L_∞` and `L_C` are contracted).

Independently, Chau 1999 Lemma 4.3 takes `deg_{(0,d)} F_φ` to be "the same natural number `μ_φ` for almost all `d ∈ C`", and Lemma 4.3 plus the Jacobian identity `det DF_φ = −m_φ J t^{n_φ−2m_φ−1} ≢ 0` make `F_φ` a dominant polynomial map, so the generic local degree along `t = 0` is a positive integer. Remark 4.9 identifies that generic local degree with Orevkov's `μ_ℓ`.

What the sources do **not** give: `μ_ℓ ≥ 1` *because* `deg f_φ > 0`. The quantity `deg f_φ` is the degree of the polynomial parametrization `C → α(ℓ)` of the *target* curve. Orevkov's `μ_ℓ` is the generic local multiplicity of the *surface* map `f*` at points of the source line. These are different integers. Chau 2004 uses `deg f_φ > 0` only to know that `f_φ(C)` is a curve, not a point. The ledger's Lemma 2.2 proof concatenates them.

Semicontinuity (the sentence after Lemma 4.2) gives `μ_x − μ_ℓ ≥ 0`, not `μ_ℓ ≥ 1`. Corollary 4.3 is compatible with a hypothetical `μ_ℓ = 0` term, which would simply drop out of the sum. Positivity is from the definition of multiplicity on the domain, not from the inequality.

### 3.4 (D4)

**Verdict: SOURCED.**

Orevkov Lemma 4.2 is the identity `N − 1 = ∑_{ℓ ⊂ L_F} (μ_ℓ f* + ∑_{x ∈ π(ℓ)\{∞}} (μ_x f* − μ_ℓ f*))`. The inner summands are nonnegative by the semicontinuity sentence in the same paragraph. The outer sum runs over irreducible components of `L_F`, which are exactly the dicritical lines of (D1)--(D3). Polar/constant components are not in the sum: they were contracted in the construction of `f*`, and `μ_∞ f* = N` is peeled off as the `−1` on the right-hand side.

Chau 1999 (4.9) restates the same identity with `D` in place of `L_F` and `deg_u f*` in place of `μ_x f*`. That is a secondary restatement, not an independent proof. Formula (4.10), the series rewrite, is not needed for (D4) and is not used below.

Set `corr_ℓ := ∑_{x ∈ π(ℓ)\{∞}} (μ_x f* − μ_ℓ f*) ≥ 0`. Then (D4) is Lemma 4.2.

---

## 4. The reviewer's `μ_ℓ = 0` attack

**A realizing line with `μ_ℓ = 0` is excluded by Orevkov's definition of multiplicity, not by `deg f_φ > 0`.**

A realizing line, in the reviewer's sense, is an irreducible component `ℓ ⊂ L_F` whose image `α(ℓ)` is a whole irreducible component of `A_F`. Such an `ℓ` is a point-set of the domain of `f*` (Orevkov contracts only `L_∞` and `L_C`). At every such point `μ_x f* ≥ 1` by the `k = 1` clause of the definition in §4, so the generic value `μ_ℓ f*` cannot vanish.

Two failure modes that do *not* occur, and one that the ledger wrote down incorrectly:

1. **Not in `L_F`.** A compactification component on which `f` is constant is in `L_C`, is contracted to a point, and is absent from Orevkov's outer sum. It cannot realise a positive-dimensional image in `C²`. Chau 2011 likewise requires `(p_ℓ, q_ℓ)` nonconstant.
2. **Collision multiplicity versus parametrization degree.** A line can have `deg(f|ℓ) ≥ 1` as a map of curves while, in a different formalism, a local mapping degree toward *generic off-curve* values vanishes. Orevkov's `μ_x` is not that off-curve local degree: it is a collision count in neighbourhoods of `x`. Chau's `μ_φ = deg_{(0,d)} F_φ` *is* a local mapping degree of the chart, and for Keller maps `det DF_φ ≢ 0` makes it positive at generic `d`. Either reading gives `μ_ℓ ≥ 1`. Neither reading is "because `deg f_φ > 0`".
3. **The ledger's written deduction is still wrong.** Replacing `deg f_φ > 0` by `μ_ℓ ≥ 1` remains an untyped identification of two degrees. The conclusion happens to be true by a different argument. Promotion of Lemma 2.2 cannot cite Chau 2004 Lemma 1 as the reason `μ_ℓ ≥ 1`.

If (D3) were dropped and `μ_ℓ = 0` allowed in the sum, Corollary 4.3 would bound only `∑ μ_ℓ`, not `#L_F` or `#Irr(A_F)`. A zero-multiplicity realizing line would cover a component of `A_F` at zero Orevkov cost and the bound `m ≤ N−1` would fail. That is why (D3) is load-bearing. It is also why it cannot be left as an informal gloss on `deg f_φ`.

---

## 5. Resulting theorem on `#Irr(A_F)` and the open remainder

**Theorem (sourced/derived subset of (D1)--(D4)).** Let `F : C² → C²` be a Keller map of geometric degree `N`. Let `L_F` be Orevkov's nonconstant finite-value boundary, and let `A_F` be the nonproper-value curve. Then

```text
m_B  ≤  #Irr(A_F)  ≤  #L_F  ≤  ∑_{ℓ ⊂ L_F} μ_ℓ f*  ≤  N − 1,
```

where `m_B` is the number of irreducible components of any reduced subcurve `B ⊂ A_F` (in particular, of the reduced branch of an actual proper block). At geometric degree `N = 4` this is `m ≤ 3`.

*Proof.* (D1), sourced: `α(ℓ)` is a single irreducible nonconstant curve, so a function `α : L_F → Irr(A_F)` is well-defined and distinct target components require distinct source lines. (D2), sourced at line level by Chau 2011, derived from Chau 2004 Lemma 1 plus the `Φ`-chart: `α` is surjective, so `#Irr(A_F) ≤ #L_F`. (D3), derived from Orevkov's multiplicity: `μ_ℓ f* ≥ 1` on every component of `L_F`, so `#L_F ≤ ∑ μ_ℓ f*`. (D4), sourced as Lemma 4.2 with nonnegative inner sums: `∑ μ_ℓ f* ≤ N−1`. A branch subcurve `B` has `#Irr(B) ≤ #Irr(A_F)`. Extra components of `A_F` not in `B` only tighten the inequality. QED.

**What remains OPEN.**

- The missing-multiplicity identity (2.3) of the ledger's Lemma 2.3 is not addressed here and stays OPEN. The bound `m ≤ N−1` does not use it.
- A numbered bijection `Π_f ↔ L_F` is not a theorem of Orevkov 1987, Chau 1999, or Chau 2004. Chau 2011 supplies covering by *components* without that bijection. Any later argument that needs to move *correction terms* from lines to series (or to identify `μ_ℓ` with `μ_φ` termwise, including the `i_φ` factor visible in the OCR of (4.10)) still owes that identification.
- The R2/R3 "unibranch critical value consumes leftover" premise of the hostile review §5.1 is untouched.
- Corollary 2 of Chau 2004 (one set-theoretic infinite point of `A_F`) is sourced and is the statement the rank-four integration already uses. It does not bound `m`.

Conditional on (D1)--(D4) as typed here, the four unlabelled source-forest shapes of the ledger are the complete list for an actual rank-four proper block. The 16-row bookkeeping remains the separate Euler error named by the review; this lane does not reopen it.

---

## 6. Companion-sheet floor `f(B_i) ≥ 1`

**The reviewer is right: the floor is load-bearing in Lemma 2.3 and is not listed in the ledger's §0.** It is not a dicritical fact and is not in Orevkov/Chau. It is a consumed rank-four fibre-census fact.

**Promoted source (not listed in the ledger §0, present in the packets the review was allowed to read).**

- Producer `xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md` (`768cf08f...`), (0.1) and §2: the fixed-sheet theorem leaves four partitions of four, of which the generic partitions of a branch component are only `T211: (2,1,1), u=2` and `T31: (3,1), u=1`; `S22` and `S4` are finite. Here `u(z) = #(π^{-1}(z) ∩ U)`.
- The same producer, quartic acyclic obstruction: "Assume every irreducible branch component has a generically unramified sheet."
- Coordinator integration `xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md` (`5d7df7ce...`), §6: "Their generic numbers of unramified sheets are `u_j = 2` or `1`." Bound in current `AUDIT.md` (rank-four branch-cycle theorem, 2026-08-30 21:57Z).
- Cubic/degree-three promotion in `AUDIT.md` (2026-08-30 21:57Z) names "generic companion sheets" for the canonical normalisation; that is the same floor in rank three, not a rank-four citation.

**Explicit consumed hypothesis (H_comp).** For an actual rank-four proper block `A² —g1→ Y —π→ A²` of degree `4`, and for every irreducible component `B_i` of the reduced branch `B = π(R)_red`, a generic closed point `z ∈ B_i` satisfies

```text
f(B_i)  :=  u(z)  :=  #(π^{-1}(z) ∩ U)  ≥  1.
```

Equivalently: the generic fibre partition of `B_i` is `T211` or `T31`, never `S22` or `S4`. For the canonical block (`d1 = 1`) this `u(z)` is the number of finite Keller preimages of `z`.

This is a *floor*, not an attainment. On `T211` the census gives `u = 2`; on `T31`, `u = 1`. Lemma 2.3 of the ledger uses only `≥ 1`, together with the upper bound `u_i ≤ 2` on `T211` and `u_i ≤ 1` on `T31` from the same census, to get `N − f(B_i) ≥ 2` and then `3 ≥ 2m` once (2.3) and (D1)--(D4) are granted. Without (H_comp), a hypothetical generic fibre with `u = 0` on some `B_i` would drop `N − f(B_i)` to `4` on that component and the summation would not force `m = 1`.

(H_comp) should be written in any restatement of Lemma 2.3 as a consumed promoted hypothesis, not hidden behind the phrase "the companion-sheet theorem".

---

## 7. Summary table and campaign impact

| claim | verdict | exact source or gap |
|---|---|---|
| (D1) one irreducible nonconstant image `α(ℓ)` | **SOURCED** | Orevkov `L_F` + Lemma 2.1(a) + Lemma 5.2; Chau 2011 definition of a dicritical component. Irreducibility of the image is desk-scale. |
| (D2) `α : L_F → Irr(A_F)` surjective | **SOURCED** (lines, Chau 2011) / **DERIVED** (from series via the `Φ`-chart) | Chau 2004 Lemma 1 covers `A_F` by series images. Chau 2011 covers `A_F` by component images. No numbered bijection `Π_f ↔ L_F` in 1987/1999/2004. |
| (D3) `μ_ℓ ≥ 1` | **DERIVED** | Orevkov §4 multiplicity at points of the domain of `f*`. **Not** `deg f_φ > 0`. |
| (D4) `N−1 = ∑ (μ_ℓ + corr_ℓ)`, `corr_ℓ ≥ 0`, sum over `L_F` | **SOURCED** | Orevkov Lemma 4.2 + the semicontinuity sentence; Corollary 4.3. Chau 1999 (4.9) is a restatement. |
| realizing line with `μ_ℓ = 0` | **excluded** | domain-multiplicity; not excluded by Chau Lemma 1. |
| `#Irr(A_F) ≤ N−1`, hence `m ≤ 3` at `N = 4` | **DERIVED** from the typed subset | the ledger's Lemma 2.2 conclusion, with the series/line step now typed. |
| identity (2.3) | **OPEN** | not this lane. |
| Chau 2004 Corollary 2 (one set-theoretic infinite point) | **SOURCED**, non-load-bearing for `m` | as already bound in `5d7df7ce...`. |
| `f(B_i) ≥ 1` | **consumed promoted hypothesis (H_comp)** | fibre census `768cf08f...` (0.1) / `5d7df7ce...` §6; unlisted in ledger §0. |

**Campaign impact.** The untyped bridge the reviewer named is real in the ledger's *written proof* (series ↝ line, and `deg f_φ` ↝ `μ_ℓ`). The *conclusion* `m ≤ 3` at geometric degree four is nonetheless a theorem of the sourced/derived subset of (D1)--(D4), with (D2) taken from Chau 2011's component covering or derived from Chau 2004 Lemma 1 plus the `Φ`-chart, and with (D3) taken from Orevkov's multiplicity rather than from `deg f_φ`. A replacement of Lemma 2.2 should cite those, not the false identification. Lemma 2.3 remains conditional on (2.3), on the typed (D1)--(D4), and on the explicit floor (H_comp). No new exit price is asserted.

<!-- BODY-END -->
