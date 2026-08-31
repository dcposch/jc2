# Trivial-dicritical literature registry

**Lane.** Scout / literature-registry (not a proof).
**Question.** Can a Keller map `F:C^2 -> C^2` (Jacobian a nonzero constant, not invertible) have a *trivial dicritical*: a dicritical divisor `l` at infinity whose image closure is an affine curve (a component of the non-properness set `A_F`) and whose generic local degree is `mu_l = 1` — equivalently, by Lemma 4.2 of the charged day’s SHEET-GATE writeup, a divisorial valuation `v` at infinity with `v(dx∧dy)=0` that is dicritical for `F` with affine image?
**Charged input.** Frozen copy of `xmodel/ideation-20260831T1033Z-synthesis.md` (hash below).
**Date.** 2026-08-31.
**Author lane.** grok-4.6.

Three objects stay distinct throughout: (i) an Orevkov/Chau *map-dicritical* (irreducible compactification component on which the extended map is nonconstant with affine image); (ii) a *function-dicritical* of a single polynomial `f:C^2->C` (component on which `f` extends nonconstantly to `P^1`); (iii) a dicritical *series* in the Newton–Puiseux sense. The boxed question is (i). Campaign names `mu_l` (generic local degree of the surface map along `l`), `s_l` (degree of `l ->` image curve), and `v(dx∧dy)` are identified with literature only where a cited statement supplies the identification.

## 0. Hash verification and input freeze

Frozen charged input:

```text
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.7FYKQ5/inputs/ideation-20260831T1033Z-synthesis.md
```

Rehash matches. Stop condition not triggered.

## 1. The boxed question, as typed by the synthesis

The 20260831T1033Z synthesis parks the Euler–inertia identity (M) and the strong all-degree bound `2m <= N-1` behind a common missing lemma: a `mu`-bound on *trivial-inertia* owner dicriticals. Subsequent same-day seats (SHEET-GATE, BUDGET-N) reduce that lemma to one bit: whether a Keller map can carry a map-dicritical with generic local degree `1` and affine image. The synthesis itself does not answer it. SHEET-GATE’s Lemma 4.2 (campaign, not literature) converts `mu_l = 1` into `v(dx∧dy)=0` along the divisorial valuation of `l`. This registry asks whether the *primary literature* already forces `mu_l >= 2` on every such `l`.

## 2. Cached primary sources (local `refs/`)

### 2.1 Orevkov 1987 (`refs/jc86.pdf`)

| field | value |
|---|---|
| Citation | S. Yu. Orevkov, *On three-sheeted polynomial mappings of C^2*, Math. USSR-Izv. **29** (1987), 587–596 (transl. of Izv. Akad. Nauk SSSR Ser. Mat. **50** (1986), 1231–1240) |
| Local | `refs/jc86.pdf` (author-retyped English, 2011-01-12) |
| SHA-256 | `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db` |

Does not use the word “dicritical”. Defines `L_F` as the nonconstant finite-value part of the boundary. Lemma 3.1 (local normal form), Lemma 4.2 (budget), Corollary 4.3, the `N=2,3` covering argument, Lemma 5.3, and the remark after the theorem are the load-bearing statements.

### 2.2 Chau / Nguyễn Văn Châu papers in `refs/`

| paper | local | SHA-256 |
|---|---|---|
| *Non-zero constant Jacobian polynomial maps of C^2*, Ann. Polon. Math. **71** (1999), 287–310 | `refs/chau1999_apm71_full.pdf` | `ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7` |
| *Non-proper value set and the Jacobian condition*, arXiv:math/0305088v1 (2003); Ann. Polon. Math. **84** (2004), 203–210 | `refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf` | `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f` |

The 1999 scan is two-column; displayed formulae have OCR noise. Prose of Def. 3.4, Thm 3.6, Lemmas 4.2–4.3, Thm 4.4, Remark 4.9 is recoverable. The 2004 file is the arXiv note, not the journal typesetting.

### 2.3 Other cached files inspected

| file | SHA-256 | use |
|---|---|---|
| `refs/do.pdf` (Domrina–Orevkov, four-sheeted, one dicritical) | `6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3` | PARTIAL at `N=4`, unique map-dicritical |
| `refs/zoladek2008_official.pdf` (Żołądek, *Topology* **47** (2008), 431–469) | `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad` | typical ramification index; `mu_D=1` implies smooth immersion |

Sigray, Żołądek-adjacent, and 2026 claimed-proof PDFs in `refs/` were not mined for dicritical multiplicities.

## 3. Fetched primary literature (Abhyankar series, Cassou-Noguès, Lê–Weber, Gwoździewicz, Jelonek, …)

| source | URL | SHA-256 |
|---|---|---|
| Chau, *Pencil of irreducible rational curves and plane Jacobian conjecture*, arXiv:0905.3939v3; Ann. Polon. Math. **101** (2011), 47–53 | `https://arxiv.org/pdf/0905.3939` | `c7eee42dfb8cc18b07598748457763d5cf54fdbcb7b574bbf295d26fafed079c` |
| Lê Dũng Tráng, *Simple rational polynomials and the Jacobian conjecture*, Publ. RIMS **44** (2008), 641–659 | `https://www.kurims.kyoto-u.ac.jp/~prims/pdf/44-2/44-2-23.pdf` | `f2b525dee30e125f31c16d4ee18ac5245c9b2389bc4cccaa04ac2cf0b219c449` |
| Cossart–Matusinski, *Dicritical divisors after S.S. Abhyankar and I. Luengo*, arXiv:1103.0707v2; J. Algebra **342** (2011), 147–153 | `https://arxiv.org/pdf/1103.0707` | `abdd75c2d4cd99b58521998c952d8105067befa77addf985287dfe3e4ba8b5f5` |
| Abhyankar–Heinzer, *Existence of dicritical divisors revisited*, arXiv:1508.06015 | `https://arxiv.org/pdf/1508.06015` | `f74931ed0bcb88e9a4944e280f7c83353a1e8407346ab483e990d654cc2f0243` |
| Heinzer–Shannon, *Abhyankar’s work on dicritical divisors*, arXiv:1707.06733 | `https://arxiv.org/pdf/1707.06733` | `0d48ba8998d9a308883f6d7b49b775196038b7578ae61c4d83479a87756e8a26` |
| Artal Bartolo–Luengo–Melle-Hernández, *High-school algebra of the theory of dicritical divisors*, arXiv:1408.0743 | `https://arxiv.org/pdf/1408.0743` | `4f843da849629df91a25d62a9452e6303b9178b4aaa961926b2825bf99281863` |
| Jelonek, *The set of points at which a polynomial map is not proper*, Ann. Polon. Math. **58** (1993), 259–266 | `http://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf` | `30b497466c1c27923a918db1c7277e90485667647fb3f2d6505f3f2c26ef420e` |
| Jelonek–Lasoń, *Quantitative properties of the non-properness set*, arXiv:1411.5011v2 | `https://arxiv.org/pdf/1411.5011` | `da2c918f0aca141043333b05863a088abea6402c43fdd8e589aa074e81e9159a` |
| Cassou-Noguès, *Quotients jacobiens d’applications polynomiales*, Ann. Inst. Fourier **53** (2003), 399–443 | `http://www.numdam.org/article/AIF_2003__53_2_399_0.pdf` | `21b7c38131cafa3e69e640cdddb535d317642ea04915b8efe69ae4a1add8c308` |
| Borisov, *Unramified planar self-maps*, arXiv:1110.5118 | `https://arxiv.org/pdf/1110.5118` | `bd45d7fb5cabb9aa9eea07cdfd9fea4f11c663fd8a6a26ebca5ba6f520de15bd` |

**Sought, not pinned as PDF in this lane.** Lê–Weber, Kodai Math. J. **17** (1994), 374–381 (Project Euclid / J-STAGE returned HTML, not a PDF); Abhyankar–Luengo, *Algebraic theory of dicritical divisors*, Amer. J. Math. **133** (2011), 1713–1732 (no open PDF); Abhyankar, *Dicritical divisors and Jacobian problem*, Indian J. Pure Appl. Math. **41** (2010), 77–97 (no open PDF); Gwoździewicz, *On the singularities at infinity of plane algebraic curves*, Rocky Mountain J. Math. **32** (2002) (Euclid HTML); Cassou-Noguès–Daigle, *Rational polynomials of simple type*, Adv. Stud. Pure Math. **75** (2017), 7–28 (Euclid excerpt only). Content of Lê–Weber used below is taken from the journal first-page extract and from Lê 2008’s restatement of the bamboo theorem, and is flagged as such.

## 4. Statement registry (one entry per sourced claim)

**R1. Orevkov, multiplicity, §4, author PDF p. 6.** Hypotheses: continuous map of topological spaces. “By the multiplicity of `φ` at `x ∈ A` we mean the largest number `k = μ_x φ` such that in every neighbourhood of `x`, there are points `x_1,…,x_k` such that `φ(x_1)=⋯=φ(x_k)`.” **Yield: STRUCTURE.** Forces `μ_x ≥ 1` at every domain point of the collapsed map `f*`, hence `μ_l ≥ 1` on every component of `L_F`. Does not force `μ_l ≥ 2`.

**R2. Orevkov, Lemma 3.1, author PDF pp. 4–5.** Hypotheses: holomorphic `g=(u,v)` near `0` in `C^2`, finite fibres, `g(0)=0`, Jacobian nonzero for `y≠0`, `g({y=0}) ⊂ {v=0}`. In suitable coordinates, `u=x'`, `v=(y')^k`. **Yield: PARTIAL.** A *nontrivial* generic inertia along a smooth divisor forces `k≥2`. Does not constrain a divisor with generic inertia `k=1`.

**R3. Orevkov, Lemma 4.2, author PDF p. 7.** Hypotheses: regularised polynomial map, collapse to constant-multiplicity `f*` of multiplicity `N`; outer sum over irreducible components of `L_F`.

> `∑_{ℓ ⊂ L_F} [ μ_ℓ f* + ∑_{x ∈ π(ℓ)−{∞}} (μ_x f* − μ_ℓ f*) ] = N − 1`

Inner summands nonnegative by semicontinuity; **Corollary 4.3:** `∑ μ_ℓ f* ≤ N−1`, equality iff `μ_x f* = μ_ℓ f*` for all affine points of each `π(ℓ)`. **Yield: STRUCTURE.** Budget, not a per-component lower bound of `2`. Compatible with a term `μ_ℓ=1` (then that component costs at least `1`, and may cost more via corrections).

**R4. Orevkov, `N=2` and `N=3` covering argument, author PDF pp. 9–10.** Keller, geometric degree `N`. If `N=2`, Corollary 4.3 forces `μ=1` constantly on `L_F`, hence a two-fold unbranched covering of `C^2`, contradiction. If `N=3`, the two configurations with some `μ=1` constantly (two components both `μ=1`, or one component `μ=1` except one extra point) yield unbranched coverings of `C^2` or of `C^2` minus a point, both simply connected, contradiction. The remaining case is a unique component with `μ=2` constantly. **Yield: PARTIAL.** Closes *all-components-unramified* (and the `N=3` mixed-with-one-correction) configurations. Does not close a mixed profile that keeps a ramified owner (`μ≥2`) plus a separate `μ=1` dicritical, which first becomes numerically possible at `N≥4`.

**R5. Orevkov, Lemma 5.3 and the remark after Theorem 1.1, author PDF pp. 9–10.** If `N>2`, `L_F` irreducible, and `μ_l f* = N−1`, then `f` on `l minus L_∞` is a biregular isomorphism onto a nonsingular affine curve. Remark: “the curve `L_F` cannot contain an irreducible component `l` such that `μ_l f* = N−1`.” **Yield: PARTIAL.** Forbids a unique dicritical of multiplicity `N−1`. Does not forbid `μ=1`.

**R6. Chau 1999, Theorem 3.6(ii), scan pp. 296–297.** Hypotheses: Keller, `P,Q` monic in `y`. For a *dicritical series* `φ` of `f`: `a_φ=0`, `b_φ=0`, and `deg P_φ / deg Q_φ = deg P / deg Q`. **Yield: STRUCTURE.** Newton constraint on leading terms along a series. Not a statement about `μ_l`. (Lemma 3.1’s `Δ_φ ≥ 2` is *not* licensed for dicritical series: its hypothesis `a+b>0` fails when `a=b=0`.)

**R7. Chau 1999, Lemmas 4.2–4.3, scan p. 304.** Hypotheses: Keller, `[φ]∈Π_f`. The chart map `F_φ(t,ξ)=f∘Φ` has `det DF_φ = −m_φ J t^{n_φ−2m_φ−1} ≢ 0`. Generic local degree `deg_{(0,d)} F_φ` equals a natural number `μ_φ`, jumping up on the finite singular set `E_φ` of `(P_φ,Q_φ)`. If `i_φ>1` then `0∈E_φ` and `deg_{(0,0)} F_φ > μ_φ`. **Yield: STRUCTURE.** Gives `μ_φ ≥ 1` (dominant polynomial chart). The jump is a correction, not a floor of `2`. Identifying `μ_φ` termwise with Orevkov’s `μ_ℓ` is claimed in Remark 4.9, not proved as a numbered bijection.

**R8. Chau 1999, Theorem 4.4 (E3), scan pp. 304–305.** Hypotheses: Keller, monic in `y`. `E_f = ⋃ C_{[φ]}` over dicritical series, and every curve `C_{[φ]}` has a singularity. Proof: Jung form `deg p=kd`, `deg q=ke`, `d>e>1`; if some `C` were smooth then `(p_φ,q_φ)` would be a regular embedding `C -> C^2`, so Abhyankar–Moh–Suzuki would force one degree to divide the other, contradicting (E1). **Yield: STRUCTURE / PARTIAL.** Forbids a *smooth embedded line* as a component of `A_F` under the Jung-form hypothesis `d>e>1`. Does not forbid a nodal (or otherwise singular) image, and does not mention `μ`.

**R9. Chau 1999, Remark 4.9, scan p. 308.** Restates Orevkov Lemma 4.2 as (4.9) and claims a rewrite (4.10) as a sum over `[φ]∈Π_f`. Conjectures that `E_f` “can never be an irreducible curve”. **Yield: STRUCTURE.** Secondary restatement of R3. The irreducibility conjecture is open in that paper and is not a `μ≥2` theorem.

**R10. Chau 2004, Lemma 1 (cited as Lemma 4 of [C]), arXiv pp. 3–4.** Hypotheses: Keller, after a coordinate change making `P,Q` monic. `A_f = ⋃ f_φ(C)` over dicritical series; both directions, via the chart `Φ(t,ξ)=(t^{−m}, φ(t^{−m},ξ))`. **Yield: STRUCTURE.** Covers `A_F` by series images. `deg f_φ>0` means the image is a curve, not `μ_l≥2`.

**R11. Chau 2011, definition of a dicritical component, arXiv p. 4.** Hypotheses: polynomial `F:C^2->C^2` with *finite fibres* (true for Keller). “By a dicritical component of `F` we mean an irreducible component `ℓ ⊂ D_∞` such that `(p_ℓ,q_ℓ)` is a non-constant mapping. Obviously… `A_F = ⋃ (f(ℓ) ∩ C^2)`. In particular, `F` is a proper map of `C^2` if and only if `F` does not have dicritical components.” Also `A_F = f(D_∞) ∩ C^2`. **Yield: STRUCTURE.** Line-level covering of `A_F`. No multiplicity.

**R12. Domrina–Orevkov, four-sheeted I, §2, `refs/do.pdf` pp. 6–7.** Hypotheses: Keller, topological degree `4`, *one* dicritical component. “It follows from [Orevkov 1987, lemma 4.2] that the ramification order of `F` along the dicritical component is `1`, `2`, or `3`. The ramification of order `3` is impossible, see [remark after 5.3]. If the ramification order is `1` then `F` is an unbranched covering over `C^2`. This is also impossible. So, the only possible order of ramification is `2`.” **Yield: PARTIAL.** Closes unique-dicritical degree four *if* their `μ=1 ⇒` unbranched-covering step is granted. That step is sourced in Orevkov only when corrections vanish (R4); a unique `μ=1` component at `N=4` would be forced by R3 to carry corrections totalling `2`, so the slogan is not a verbatim Orevkov theorem. Flag the last inference as **authors’**, not a numbered lemma.

**R13. Żołądek 2008, Proposition 6.5 and Corollary 6.6, official PDF pp. 457–458.** Hypotheses: Jacobian map, non-properness divisors in the resolved compactification. (a) Restates Orevkov’s budget. (b) `μ_z > μ_D` iff the image point is a singularity of the *immersed* curve `S`; “If `μ_D=1`, then `S` is smooth” (immersive; “an intersection of smooth local components is not treated as a singularity”). Cor. 6.6: `degtop=2,3` impossible; at `4` (resp. `5`) at most `2` (resp. `3`) non-properness divisors. **Yield: STRUCTURE / PARTIAL.** `μ=1` implies an immersive image. Combined with R8 this forbids `μ=1` *and* a smooth embedded image under Jung `d>e>1`; it does *not* forbid `μ=1` onto a nodal curve.

**R14. Żołądek 2008, Proposition 6.7, official PDF p. 458.** Hypotheses: non-properness divisor with Newton–Puiseux chart `x=a_1 y^{−γ_1}+⋯+u y^{−γ}`, `γ=l/k`, `gcd=1`. “The typical ramification index of `D` equals `μ_D = l−k`.” Proof: the alteration chart has `Jac θ̃ = v^{l−k−1}`; since `Jac P=1`, `P∘θ̃` is ramified along `v=0` with index `l−k`. **Yield: STRUCTURE.** This is the literature form of the campaign identity `e = 1+v(dx∧dy)` in an N–P chart: `mu_l=1` iff `l−k=1` iff `Jac θ̃` is a unit along `v=0`. No source in this paper forbids `l−k=1` for a Keller non-properness chart.

**R15. Lê 2008, Theorem 3.2 / Corollary 3.8, RIMS PDF pp. 650–659.** Hypotheses: Jacobian *pair* `(f,g)`; `f` a *simple rational polynomial* (generic fibre diffeomorphic to a punctured sphere, *and* every *function-dicritical* of `f` has degree `1`). “A simple rational polynomial which is not a locally trivial fibration over `C` cannot belong to a Jacobian pair.” Hence if `f` is simple rational in a Jacobian pair, `(f,g)` is an automorphism. **Yield: PARTIAL**, for a *different* degree: function-dicritical degree `1` for one component of `F`, plus rationality of fibres. Not a statement about map-dicritical `μ_l`.

**R16. Lê–Weber 1994, bamboo theorem (as restated in Lê 2008, Thm 1.4, and the Kodai first-page extract).** Hypotheses: polynomial function `f:C^2->C`, minimal compactification. Each connected component of `A \ A_∞` is a bamboo containing a unique function-dicritical, the unique component meeting `A_∞`. If `f` has no critical points, `f` fails to be a locally trivial fibration iff some bamboo has at least two components *or* some dicritical restriction has critical points. **Yield: STRUCTURE.** Function-side geometry. Lê–Weber’s Kodai PDF was not hashed in this lane.

**R17. Jelonek 1993, Theorem 15, APM **58**, pp. 259–260.** Hypotheses: dominant polynomial `f:C^n -> C^n` (not necessarily Keller). The non-properness set `S` is empty or a uniruled hypersurface, with an explicit degree bound in terms of `deg f_i` and `μ(f)`. Proposition 6: `f` is proper at `y` iff the fibre is finite and `∑ μ_{x_i}(f) = μ(f)`. **Yield: STRUCTURE.** For Keller maps in the plane, `S=A_F` is a uniruled curve (or empty). No ramification of dicriticals.

**R18. Jelonek–Lasoń 2014/2018, arXiv:1411.5011v2.** Hypotheses: generically finite polynomial map of algebraic degree `d`. `S_f` is covered by parametric curves of degree at most `d−1`. **Yield: STRUCTURE.** Quantitative shape of `A_F`, not `μ_l`.

**R19. Borisov, arXiv:1110.5118, Theorem 3.1, p. 9.** Hypotheses: counterexample to JC2, compactified unramified-on-`A^2` map `φ:Z->Y`. “Then `Z` contains a curve of type 3, where `φ` is ramified.” Type 3 = Orevkov map-dicritical. Proof: otherwise a generic line-pullback would force `φ` birational. **Yield: PARTIAL.** At least *one* map-dicritical is ramified (`μ≥2`). Explicitly weaker than “every dicritical is ramified”. Theorems 3.2 and 3.7 (big / ample log-ramification divisor `∑ r_i E_i` over type-3 curves) likewise require some `r_i>0` in the sum, not `r_i≥1` on every summand. Theorem 3.5 constrains the *curve-map* degree `f_i`, not `μ_l`.

**R20. Cassou-Noguès, AIF **53** (2003), Remarque 4.8, p. 433.** Hypotheses: polynomial map with Jacobian a nonzero constant. Deduced from “the principal lemma of [4]”: the only class of `Q_+` is `(deg f, deg g)`, and `Q_-`, `Q_{-0}` are empty. **Yield: STRUCTURE.** Newton-polygon constraint at infinity on the pair `(f,g)`, not a per-dicritical `μ`.

**R21. Artal–Luengo–Melle, arXiv:1408.0743, p. 3.** Records Żołądek that a Jacobian pair with two points at infinity has some *common* function-dicriticals, and a Cassou-Noguès private communication that *not all* function-dicriticals can be common (else the map-degree vanishes and the Jacobian is identically zero). **Yield: STRUCTURE.** Function-dicriticals of the two components; the “not all in common” sentence is private communication, not a hashed theorem.

**R22. Abhyankar–Luengo / Cossart–Matusinski / Abhyankar–Heinzer / Heinzer–Shannon.** Algebraic theory of dicritical *divisors of an element / special pencil* in a 2-dimensional regular local ring: residue of a dicritical is a polynomial in a uniformizer (AL main theorem, Cossart Thm 3.1 / Cor. 4.2 for `k[x,y]`). Existence: any finite set of prime divisors is realised as the dicritical set of some `z` (Abhyankar–Heinzer). **Yield: NOTHING** for the boxed question. These are function/pencil dicriticals. Existence theorems run the opposite direction (prescribing dicriticals, not forbidding `μ=1`). Abhyankar 2010 *Dicritical divisors and Jacobian problem* was not obtained as PDF; the Heinzer–Shannon survey describes it as motivation, not as a ramification theorem for map-dicriticals.

**R23. Cassou-Noguès–Daigle 2017 (Euclid excerpt, PDF not pinned).** A rational polynomial is of simple type if every function-dicritical has degree `1`; they classify Newton trees of those polynomials. **Yield: NOTHING / pointer.** Feeds R15; does not discuss Keller map-dicriticals.

## 5. Combination chains (if any close, or nearly close)

**Chain A (closes all-unramified, not the boxed mixed bit).** R3 + R4: if every map-dicritical has `μ=1` and affine corrections vanish, the collapsed map is an unbranched covering of a simply connected space. Impossible for `N≥2`. *Every link sourced in Orevkov.* Does not touch a ramified owner plus a separate `μ=1` dicritical.

**Chain B (closes unique dicritical of multiplicity `N−1`).** R3 + R5. Sourced. Irrelevant to `μ=1`.

**Chain C (unique dicritical, `N=4`).** R3 + R5 + R12. Domrina–Orevkov conclude only `μ=2` remains. The `μ=1` dismissal is their unbranched-covering slogan (R12), which matches R4 only if corrections vanish; R3 then forbids that at `N=4`. Treat as **PARTIAL with a flagged author-inference** on the `μ=1` step, not as a sourced general `μ≥2`.

**Chain D (smooth embedded image).** R13 (`μ=1 ⇒` immersive image) + R8 (every series-image is singular, via AMS + Jung `d>e>1`). Would close `μ=1` *and* `s_l=1` *and* reduced image smooth, under Jung form. **Two gaps, both flagged as inference:** (i) identifying Żołądek’s immersed `S` with Chau’s `C_{[φ]}` needs the series-to-line map, which Chau 1999 Remark 4.9 claims but does not number; Chau 2011 covers images by lines without identifying `μ`; (ii) R8’s proof uses `d>e>1`, not `deg P=deg Q`. Not a closing chain.

**Chain E (function-simple).** R15 (+ R16, R23). Closes Jacobian pairs in which one *component function* is a simple rational polynomial that is not a locally trivial fibration. Different degree (function-dicritical degree, not map `μ_l`).

**Chain F (at least one ramified).** R19, or independently the rank-four inertia input via R2. Already used by the campaign as `mu_owner ≥ 2` for nontrivial inertia. Does not lift to trivial-inertia owners.

No sourced chain closes the unrestricted boxed question.

## 6. Verdict

**ABSENT.**

Primary sources force `μ_l ≥ 1` on every map-dicritical (R1, R3, R7, R11), force *some* map-dicritical to be ramified in a counterexample (R4, R19), and close several named special configurations (all-unramified; unique component of multiplicity `N−1`; unique component at `N=4` modulo the flagged slogan in R12; simple rational *functions* in a Jacobian pair). They do not contain a theorem that every affine-image map-dicritical of a Keller map has generic local degree `≥2`, and they do not forbid a mixed profile with a ramified owner and a separate `μ=1` dicritical mapping to an affine curve. The campaign identity `μ_l = 1 + v(dx∧dy)` is matched by Żołądek Prop. 6.7 in N–P charts (R14), where the open bit becomes `l−k=1`; no fetched source excludes that equality under the Jacobian condition.

## 7. Attack routes (if ABSENT / SOURCED-PARTIAL)

1. **Chart-Jacobian / N–P route (Żołądek 6.7 + Chau chart).** In a resolved non-properness chart, `μ_l = l−k` and `Jac θ̃ = v^{l−k−1}`. Show that a Keller map cannot have a dicritical chart with `l−k=1` (i.e. `θ̃` étale along `v=0` while `P∘θ̃` stays finite-valued and nonconstant). Chau’s `det DF_φ = −m J t^{n−2m−1}` is the unresolved-chart analogue; the missing lemma is the transformation of that order under the remaining blowups that produce a smooth map-dicritical. Desk-scale, one valuation.

2. **Image-singularity / covering route (R8+R13+R4, repairing Chain D).** Make the series-to-line identification a numbered lemma (Chau 2011 covering + Φ-chart from Chau 2004 Lemma 1 proof). Then split `μ=1` by `s_l`: `s_l=1` plus immersive image plus Jung `d>e>1` is the AMS obstruction; `s_l≥2` is a polynomial parametrization of degree `≥2` whose reduced image is singular, and the collapsed map is an unramified cover of `C^2 \ A_F` along that component — a π1 computation on the complement of a singular uniruled curve (Jelonek), not a simply-connected slogan.

3. **Unique-versus-mixed split at general `N`.** R12 almost kills unique `μ=1` at `N=4`; rewrite that step with corrections visible (R3), then decide the mixed remainder `(μ=2)+(μ=1)` which is the SHEET-GATE transposition-class bit and the BUDGET-N `m_triv` coefficient. Borisov’s ample ramification divisor (R19) is a possible global obstruction to a numerically trivial summand, but only after checking that an unramified type-3 curve is still in the support.

## 8. Acquisition list for a successor proof lane

Pin as PDFs, with hashes, before any promotion:

1. Official Math. USSR-Izv. typesetting of Orevkov 1987 (IOP / Math-Net), to confirm Lemma numbers against `refs/jc86.pdf`.
2. Lê Dũng Tráng–C. Weber, Kodai Math. J. **17** (1994), 374–381 (journal PDF).
3. Abhyankar–Luengo, Amer. J. Math. **133** (2011), 1713–1732.
4. Abhyankar, Indian J. Pure Appl. Math. **41** (2010), 77–97.
5. Journal form of Chau 2004, Ann. Polon. Math. **84** (2004), 203–210 (vs arXiv:math/0305088v1).
6. Gwoździewicz, Rocky Mountain J. Math. **32** (2002), 99–126 (or the published version of the Euclid record).
7. Cassou-Noguès–Daigle, Adv. Stud. Pure Math. **75** (2017), 7–28 (full text).
8. Domrina, *Four-sheeted polynomial mappings of C^2. The general case*, Izv. Math. **64** (2000), 1–33 (two-dicritical companion of R12).
9. Fourrier, Ann. Inst. Fourier **46** (1996), 645–687 (topology at infinity; cited by Cossart).
10. The “principal lemma of [4]” backing Cassou Remarque 4.8 (identify and pin that reference).

Not needed to start a proof lane, but useful: Neumann–Norbury classification of simple rational polynomials; Campbell, *Partial properness and the Jacobian conjecture*.

<!-- BODY-END -->
