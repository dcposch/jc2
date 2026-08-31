# LIT-TARGETED — three searches that could short-circuit the endgame

**Lane.** Targeted literature registry (REGISTRY, not proofs). Desk-scale exact
reasoning. Primary PDFs fetched and hashed; no CAS.

**Date.** 2026-08-31

**Agent.** grok-4.6 (xAI)

**Charged inputs (frozen copies; hashes verified below).**

- `xmodel/pi1s4-64-triple-cover-close-sol56-20260831.md`
- `xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`

**Questions.**

1. Unit representation of binary cubics over polynomial rings.
2. π₁ of complements of (2,q)-type polynomial curves / fold-unions.
3. Certified braid monodromy in practice (SIROCCO / Sage / alternatives).

---

## 0. Hash verification and charged-input extract

Frozen copies were rehashed before any content was used. Both match; stop condition not triggered.

```text
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  .../pi1s4-64-triple-cover-close-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  .../block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

(Full paths as charged; SHA-256 of the PDF/Markdown bytes on 2026-08-31.)

**Coordinator extract (fable5).** Theorem N-A and N-A-RES promoted; residual topological core is one target-isomorphism class, the explicit three-node `(6,4)` curve, with

```text
OPEN[PI1S4-(6,4)-FIXED-TUPLE]:
does an S4 transposition tuple with node-commutation constraints exist,
fixed by the (6,4)-cable braid at infinity?
```

Row table: `(6,4)` nodal OPEN, sole numerical type `Δ=(6,4,3)`, `β₁=15`, `(δ_∞,δ_aff,M_∞)=(7,3,16)`, attained by an explicit three-node curve. `(8,4)` nodal OPEN and recorded as target-equivalent to that survivor. `(8,6)`/`(9,6)` nodal OPEN on realization. This lane does not re-audit those promotions.

**Triple-cover-close extract (sol56).** Global monogenicity of the cubic resolvent over `R=C[x,y]` is equivalent to the Miranda index form `I(S,T)` representing a unit (`I(s,t)∈C^*`). Freeness of the trace-zero module does not imply a power basis. A weighted-degree counterexample

```text
I(S,T)=x S^3 - 3 S^2 T + 3 S T^2 + y^2 T^3
```

gives a connected normal locally-monogenic generic-`S_3` cubic algebra over `R` with irreducible reduced sextic branch and no unit value; it is not the row (two points at infinity). Conditional on a global power basis and the provisional row geometry, a cancellation lemma kills every Davenport band, hence **no monogenic resolvent can carry the row**. Residual:

```text
OPEN[PI1S4-(6,4)-TRIPLE-COVER-GLOBAL-MONOGENICITY-ROW]:
does every hypothetical charged S4 representation have a resolvent
index form representing a unit?
```

The exact unresolved class is `R_{F,S4}^{nm}` (charged display (7.1)): `S_4`-compatible normal domain with `disc(I)=-27 κ F` and `I(R^2)∩C^*=∅`.

**What a literature close would have to do.** (Q1) a criterion or sourced countermodel for unit representation of a binary cubic over `C[x,y]` with squarefree discriminant, in the row class. (Q2) a Tokunaga-type existence/nonexistence theorem for `S_3`/`S_4` covers branched at a simple-singularity sextic of type `3A_1+A_{14}` (or at a fold-union of two rational curves). (Q3) a certified computational path for the braid monodromy of that sextic at AWS scale.

All statements below are registry items: exact source, SHA-256 of fetched PDF bytes, verbatim scope, yield `CLOSES` / `PARTIAL` / `STRUCTURE` / `NOTHING` for the named question. No CAS. No `charge_basis` line. Campaign names (`(6,4)` row, `R_{F,S4}^{nm}`) identify the question, not a proof.

**PDF hash convention.** SHA-256 of the bytes streamed on 2026-08-31. Miranda’s CSU preprint rehashes to the same value already recorded in the charged triple-cover-close report. Files that downloaded as HTML or as the wrong arXiv paper are listed as SOURCE-OPEN, not hashed as content.

## 1. Question 1 — Unit representation of binary cubics over polynomial rings

**Question.** Let `I(S,T)` be a binary cubic over `R=C[x,y]` with squarefree discriminant. When is `I(s,t)=1` solvable in `s,t∈R`? Equivalently (Miranda / charged §1): when is the associated free cubic `R`-algebra globally monogenic?

### 1.1 Fetched sources

| tag | source | URL | SHA-256 | pp |
|---|---|---|---|---|
| M85 | Miranda, *Triple covers in algebraic geometry*, Amer. J. Math. **107** (1985), 1123–1158 | `https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf` | `0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875` | 37 |
| GGS02 | Gan–Gross–Savin, *Fourier coefficients of modular forms on G₂*, Duke Math. J. **115** (2002), 105–169 | `http://www.math.toronto.edu/~ila/GanGrossSavin.pdf` | `007efcf17a30ff33857dfd8cc2f58a7d203c8c5c6794703d4acb76c2225c99f8` | 65 |
| P08 | Poonen, *The moduli space of commutative algebras of finite rank*, arXiv:math/0608491v2; J. Eur. Math. Soc. **10** (2008), 817–836 | `https://arxiv.org/pdf/math/0608491` | `1261759bc63f0ce098f762819c72b407e9ca403fb4d36545f48cfe43fefb3b53` | 17 |
| W10 | Wood, *Rings and ideals parametrized by binary n-ic forms*, arXiv:1007.5508v1 | `https://arxiv.org/pdf/1007.5508` | `f56608a471d77c9ab5ba865a946b520155fc84210efcaffd7ebe494470feb6ff` | 30 |
| W10b | Wood, *Quartic rings associated to binary quartic forms*, arXiv:1007.5501v2 | `https://arxiv.org/pdf/1007.5501` | `043b681e2aabae78bc16e6e04e880514eb3ecabbec5f4e4a97739a981977bc2b` | 15 |
| W10c | Wood, *Parametrization of ideal classes in rings associated to binary forms*, arXiv:1008.4781v1 | `https://arxiv.org/pdf/1008.4781` | `69f7043f6ec715615117db4af9d2f8a12115aab62f9e3d84e70d75d1a4acff80` | 31 |
| B04 | Bhargava, *Higher composition laws II*, Ann. of Math. **159** (2004), 865–886 | `https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n2-p09.pdf` | `858e71743b8c6486d18ee40f0f22da74f25d880a397a0e0e6e8a1d0f84f49930` | 22 |
| O’D16 | O’Dorney, *Rings of small rank over a Dedekind domain and their ideals*, arXiv:1508.02777v4; Res. Math. Sci. **3** (2016) | `https://arxiv.org/pdf/1508.02777` | `632081d5262241ede5856921852da28b2a540f72e5938824ee39790c87c9e964` | 40 |
| CM25 | Ciliberto–Miranda, *Non-cyclic triple planes with branch curve of degree at most 10*, arXiv:2512.07965v1 | `https://arxiv.org/pdf/2512.07965` | `e935f9e7286f57ac50aa6e955854e9aa43fa7e26d35405f21dcac5ef95531c6b` | 41 |
| Sh12 | Shirane, *A note on normal triple covers over P² with branch divisors of degree 6*, arXiv:1211.2526v1 | `https://arxiv.org/pdf/1211.2526` | `b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153` | 9 |

**SOURCE-OPEN.** Deligne’s letter to Gan, Gross and Savin, 13 Nov 2000: unpublished; content recovered only as reconstructed in W10 pp. 2, 10, 21 and bibliography item [7]. Delone–Faddeev 1940 / AMS Transl. 10 (1964): no open PDF pinned. Casnati–Ekedahl, J. Algebraic Geom. **5** (1996), 439–460: no open PDF. Gross–Lucianovic *On cubic rings and quaternion rings*: arXiv number not pinned (math/0608376 is a different paper). Voight, *Rings of low rank with a standard involution*, IJM **55** (2011) fetched as arXiv:0809.1397 (`1d7d454a75074b202b616b4f795ad832492217a802e91a8160061d71f6aa319d`, 31 pp.) — quaternion/involution scope, not used below.

### 1.2 Registry

**R1. Miranda, Thm 2.7.1 / Rem. 2.8.1, Prop. 3.3, display (3.4), Thm 3.6 / Def. 3.7, Lem. 4.5 / Prop. 4.7.** Scope: a triple cover of a scheme is given by a rank-2 locally free Tschirnhausen sheaf `E` and a section of `Sym^3 E^∨ ⊗ det E` (binary cubic). With a trace-zero basis the index form is `I(S,T)`; `det(1,θ,θ²)=I(s,t)`; the branch polynomial is `disc(I)` up to `C^*`. **Yield: STRUCTURE.** This is the charged criterion (1.3), already consumed. No unit-representation theorem over `C[x,y]`.

**R2. GGS02, §4, Prop. 4.2 (pp. 113–117).** Scope: base ring `Z`. Twisted `GL_2(Z)`-orbits on integral binary cubics `↔` isomorphism classes of cubic rings (free rank-3 `Z`-algebras). Primitive forms `↔` Gorenstein cubic rings. **Yield: STRUCTURE** over `Z`. Not a statement over `C[x,y]`.

**R3. P08, Prop. 5.1 and Rem. 4.6 (pp. 5–6 of the arXiv file).** Scope: the moduli scheme `B_n` of based rank-`n` algebras over `Z` is smooth iff `n≤3`. For `n=3`, a “good” basis `1,α,β` with `αβ∈O_S` puts `B_3^{1,good} ≅ A^4`, and the four coordinates are the binary-cubic coefficients, paraphrasing Delone–Faddeev §15 and GGS02 §4. **Yield: STRUCTURE.** The moduli space is smooth affine 6-space; this does not decide which binary cubics represent units.

**R4. W10, Thm 1.2 / Thm 4.7, Rem. 2.6, geometric construction of §2.3.** Scope: arbitrary base scheme `S`. `(-1)`-twisted binary `n`-ic forms over `S` `↔` “binary `n`-pairs” (an `O_S`-algebra `R` of rank `n` plus a specified module `I`), functorially in `S`. For `n=3` the extra module is redundant (`I ≅ R`). Rem. 2.6: if the leading coefficient is `±1` then `R_f = Z[θ]/f(θ)` is monogenic, and every monogenic ring arises this way. The `n=3` geometric construction (hypercohomology of `O(-3) → O` on `P^1_S`) “was originally given in a letter of Deligne [7] to Gan, Gross, and Savin.” Primitive form `↔` Gorenstein (Cor. 2.5, `n≠2`). **Yield: STRUCTURE.** Over `S=Spec C[x,y]` this is the Delone–Faddeev correspondence with free modules (Quillen–Suslin: every rank-2 is free, so every cubic algebra is given by a binary cubic up to `GL_2(R)`). Monogenicity is **defined** as the existence of a `GL_2(R)` representative with unit leading coefficient, i.e. as unit representation of `I`. No solvability criterion for `I(s,t)=1`.

**R5. W10b, Thm 2.1 / Thm 1.1.** Scope: `Z`. Binary cubics parametrize based cubic rings (citing GGS); binary quartics parametrize quartic rings with a *monogenic* cubic resolvent. **Yield: NOTHING** for Q1 (the monogenic-resolvent constraint is over `Z`, opposite direction).

**R6. B04, introduction and the cubic-ring remarks.** Scope: `Z`. Composition laws on `Z^2⊗Z^3⊗Z^3` recover class groups of cubic orders; the underlying Delone–Faddeev bijection is used, not proved. **Yield: NOTHING** for the unit equation over a polynomial ring.

**R7. O’D16, abstract and §1.** Scope: **Dedekind** base rings. Parametrizes quadratic, cubic, quartic algebras over an arbitrary Dedekind domain. **Yield: NOTHING.** `C[x,y]` is not Dedekind.

**R8. CM25, §5, Prop. 19–20.** Scope: normal non-cyclic triple covers of **`P^2`** with branch degree 6. Then either `q=1` (exceptional, or six lines in a pencil) or `X` is a normal cubic surface projected from an external point; if `X` is smooth the branch is an irreducible sextic with (in general) six ordinary cusps, or two smooth cubics meeting at three collinear points with contact 3. Tschirnhausen bundle `O(-1)⊕O(-2)`. **Yield: STRUCTURE / PARTIAL** for *projective* triple planes, not for algebras over `A^2`. The splitting type `O(-1)⊕O(-2)` is the projective analogue of a free affine Tschirnhausen module, which Quillen–Suslin already supplies over `A^2`.

**R9. Sh12, Thm 0.3 and Cor. 0.6.** Scope: normal triple covers of `P^2` with `deg Δ_π=6`. Then either the 9-cuspidal dual construction, or `X` is a cubic surface in `P^3`. Cor. 0.6: such a cover exists iff `Δ` is cut out by `G_2^3+G_3^2=0` (a `(2,3)`-torus sextic) with two local primitivity conditions. **Yield: PARTIAL** for the *projective* existence of a triple cover branched at a sextic. Affine monogenicity over `C[x,y]` is a different compactification question (the cover of `A^2` may ramify along the line at infinity).

### 1.3 Combination

The Delone–Faddeev–GGS–Wood–Deligne chain (R2+R4+R3) identifies cubic algebras over any base, including `C[x,y]`, with `GL_2`-orbits of binary cubics, and identifies global monogenicity with unit representation. That is the language of the charged residual, not a solution of `I(s,t)=1`. Simon’s class-group obstruction to Thue equations (cited in W10) is over number rings. Over `C[x,y]` there is no Picard obstruction of that form (`Pic R=0`). The charged counterexample (2.1) is compatible with the literature: locally monogenic Gorenstein cubic rings need not be globally monogenic once the leading coefficient is nonunit.

No fetched source gives a criterion that a binary cubic with squarefree discriminant over `C[x,y]` represents a unit, and none exhibits a countermodel in the row class `3A_1+A_{14}` / one place at infinity. R8–R9 constrain *projective* triple planes of degree 6 to torus type or to six-cuspidal / two-cubic branches, which is consumed in Q2.

**Q1 verdict. ABSENT as a close; STRUCTURE as a parametrization.** The unit-representation equation remains a new lemma.

## 2. Question 2 — π₁ of complements of (2,q)-type fold-unions

**Question.** Does the literature already decide existence of an `S_3` or `S_4` cover branched at the `(6,4)` row’s sextic (simple singularities `3A_1+A_{14}`), or at a fold-union of two rational curves exchanged by an involution (the `(8,4)` target-fold; two 3-nodal quartics with high contact)?

### 2.1 Fetched sources

| tag | source | URL | SHA-256 | pp |
|---|---|---|---|---|
| T02 | Tokunaga, *Galois covers for S₄ and A₄ and their applications*, Osaka J. Math. **39** (2002), 621–645 | Euclid `ojm/1153492850` | `371a8098545cad966bb5fc70761a72d886a11e2a4ceb3100b5b75d0822745d54` | 25 |
| T00 | Tokunaga, *Dihedral coverings of algebraic surfaces and their application*, Trans. Amer. Math. Soc. **352** (2000), 4007–4017 | AMS `S0002-9947-00-02524-1` | `e51473979c0b67da50a55129302877c1f00e4bd5c34cf13a564d306f94e20adb` | 11 |
| T95 | Tokunaga, *On maximizing sextics whose complements have non-abelian fundamental groups*, MPIM preprint 1995-125 (journal: Math. Ann. **308** (1997), 633–648) | `https://archive.mpim-bonn.mpg.de/id/eprint/3110/1/preprint_1995_125.pdf` | `39547a66582ab24b51365095ad68d85a1d8a6059c4d1be3c23c37eaabfef4f09` | 23 |
| T91 | Tokunaga, *Triple coverings of algebraic surfaces according to the Cardano formula*, J. Math. Kyoto Univ. **31** (1991), 359–375 | Euclid `10.1215/kjm/1250519799` | `5e7989b8f4315940d9af91f11b5bb159447c77786d6a1c4f12ec0dba675da707` | 29 |
| T04 | Tokunaga, *Dihedral covers and an elementary arithmetic on elliptic surfaces*, J. Math. Kyoto Univ. **44** (2004), 255–270 | Euclid `10.1215/kjm/1250283554` | `bbf7f804d75be9ffc50b38b58e2d789923f439df29c7e0b8bc7db0b460f2c27f` | 16 |
| T96 | Tokunaga, *A remark on Artal’s paper*, Kodai Math. J. **19** (1996), 207–217 | Euclid `10.2996/kmj/1138043600` | `dff107ffb4db0ac2d526470e8e6701193fb03e6383c09bb3f09f2dd66626c78d` | 11 |
| IT09 | Ishida–Tokunaga, *Triple covers of algebraic surfaces and a generalization of Zariski’s example*, Adv. Stud. Pure Math. **56** (2009), 169–185 | Euclid `10.2969/aspm/05610169` | `60197300272399a30ec61654da6a26746cf516e7ba72297a61e4456fe8c129c5` | 17 |
| ACT08 | Artal–Cogolludo–Tokunaga, *Pencils and infinite dihedral covers of P²*, arXiv:math/0411506; Proc. Amer. Math. Soc. **136** (2008), 21–29 | `https://arxiv.org/pdf/math/0411506` | `272fdf54ea01380be540cd625c85dd9813d772884c796919e15c71a1ae4bad10` | 10 |
| AT04 | Artal–Tokunaga, *Zariski k-plets of rational curve arrangements and dihedral covers*, arXiv:math/0311280 | `https://arxiv.org/pdf/math/0311280` | `36abce4cc38a4339211b66c959f1398be1534187a1444351dfc8bb5de5798671` | 29 |
| TT18 | Tumenbayar–Tokunaga, *Elliptic surfaces and contact conics for a 3-nodal quartic*, Hokkaido Math. J. **47** (2018), 223–244 | Euclid `10.14492/hokmj/1520928068` | `2bfa93160eb4f0f779fc328e9ce32623cf53faa355edc7c14780468fff61af58` | 22 |
| Oka05 | Oka, *Zariski pairs on sextics I*, arXiv:math/0507051v1 | `https://arxiv.org/pdf/math/0507051` | `2a864cdd2530533c30f45d2cf9e9435e24f6a53b3788094df26a63e7208213e4` | 12 |
| T11 | Tokunaga, *Elliptic dihedral covers… Zariski pairs for line-conic arrangements*, arXiv:1111.5924 | `https://arxiv.org/pdf/1111.5924` | `3c915b4a766d791956db13ffbcd9f0af28c10b62f08157c8115198d72115a88b` | 26 |

Also Sh12, CM25 from §1. **SOURCE-OPEN.** Tokunaga, Canad. J. Math. **46** (1994), 1299–1317 (CJM 403 on the Cambridge PDF). Journal typesetting of Math. Ann. **308** (1997) (T95 is the MPIM preprint). Artal–Cogolludo–Tokunaga, *A survey on Zariski pairs*, Adv. Stud. Pure Math. **50** (2008), 1–100 (Euclid HTML/preview only).

### 2.2 Registry — projective triple covers of a simple-singularity sextic

**R10. IT09, Theorem 1.1 (pp. 170–171).** Verbatim scope: `B` a reduced sextic in `P^2` with at worst simple singularities. There exists a *generic* triple cover `π:X→P^2` with branch locus `B` if and only if `B` is given by `G_2^3 + G_3^2 = 0` with `G_i` homogeneous of degree `i`. (“Generic” = finitely many total branch points; such a cover is non-Galois.) **Yield: PARTIAL, the strongest close in this lane for projective `S_3`.** Converts existence of a non-Galois triple plane branched at `B` into the torus-type identity. Does **not** by itself decide whether the row sextic is torus type, and does **not** constrain a triple cover of `A^2` that ramifies along the line at infinity.

**R11. Sh12, Cor. 0.6 and Rem. 0.7(iv).** Same torus-type criterion for any normal triple cover of `P^2` with `deg Δ=6`, without the simple-singularity hypothesis. Rem. 0.7(iv) records that IT09 already forces torus type when the singularities are simple. **Yield: PARTIAL**, same projective compactification gap.

**R12. Oka05, pp. 1–3, inner-singularity calculus and Lemma 3.** Scope: irreducible *tame* `(2,3)`-torus sextics with simple singularities. Inner points of `C_2∩C_3` are `A_{3ι-1}` if `C_3` is smooth there (`ι=I(C_2,C_3;P)`), or `E_6` if `C_3` is singular and `ι=2`. Pho’s list of tame configurations is the eleven partitions of the intersection number 6; the `(5,1)` slot is `[A_{14},A_2]`, the `(6)` slot is `[A_{17}]`. No slot is `[A_{14},3A_1]`. `A_1=A_{3ι-1}` would force `ι=2/3`, so an ordinary node **cannot be inner**. Lemma 3 (“Tokunaga criterion”): `C` is torus type iff there is a conic `C_2` with `C_2∩C ⊂ Sing(C)` and `I(C,C_2;P)=2ρ(P,5)` at each such point. **Yield: PARTIAL.** The tame list excludes `[A_{14},3A_1]` as a *tame* torus configuration. Outer nodes on a non-tame torus sextic are not excluded by the displayed list. Lemma 3 is a checkable criterion once an explicit equation is in hand.

**R13. CM25, Prop. 19–20.** Projective non-cyclic triple planes of branch degree 6 are cubic-surface projections (or the `q=1` exceptions). Smooth `X` gives six cusps, or two cubics of contact 3. **Yield: STRUCTURE.** Compatible with R10–R11; does not name `3A_1+A_{14}`.

### 2.3 Registry — `S_4` and dihedral covers of `P^2`

**R14. T02, Theorems 0.6 and 0.7 (pp. 623–624).** Scope: reduced sextic `B` with at most simple singularities; `Z'` the double cover of `P^2` branched along `B`, `Z` its canonical resolution (a `K3`); `Γ(B)` the dual graph of the exceptional divisor of `Z→Z'`. If an `S_4`-cover of `P^2` is branched at `2B` (ramification index 2 along `B`) and factors through `Z'→P^2`, then `Γ(B)` contains a subgraph `A_2^{\oplus 9}` or `A_2^{\oplus 6}⊕A_1^{\oplus 4}`. Conversely, if `Γ(B)` contains `A_2^{\oplus 6}⊕A_1^{\oplus 4}` with the `A_1^{\oplus 4}` an **invariant block** under the covering involution, such an `S_4`-cover exists. **Yield: PARTIAL.** A transposition-type homomorphism `π_1(P^2\setminus B)→S_4` has odd meridians, hence factors through the double cover, and ramification index 2, so the hypotheses of 0.6 match a *projective* `S_4` cover branched only at `B`. For singularities `3A_1+A_{14}` the exceptional graph is `A_1^{\oplus 3}⊕A_{14}`. A path of 14 vertices contains six disjoint `A_2`’s, leaving two vertices plus the three nodes, so the ADE graph contains `A_2^{\oplus 6}⊕A_1^{\oplus 4}` as a subgraph; 0.6 does **not** forbid the cover. Sufficiency 0.7 additionally needs the leftover `A_1^{\oplus 4}` to be involution-invariant; that is a computation on the Horikawa involution of this `K3`, not supplied by T02 and not performed here. Affine `S_4` (meridians of `L_∞` allowed) is outside the statement.

**R15. T00, Theorems 0.3–0.4.** Scope: reduced curve `B` of even degree on a simply-connected surface, at most simple singularities, `NS(Z)` torsion-free. Existence of a `D_{2n}`-cover branched at `B` with ramification index 2, in terms of `n`-torsion in `NS(Z)/T` (0.3) or a numerical inequality in the total Milnor number and a count `l` of `a_{3k-1}` and `e_6` (0.4, `p=3`). Application: `B` of even degree `d` with `a` nodes and `b` cusps, `2a+6b > 2d^2-6d+6` implies `π_1(P^2\setminus B)` non-abelian. **Yield: NOTHING as a close of the row.** For `d=6`, `a=3`, `b=0` one has `2a+6b=6 ≯ 42`. The 0.4 inequality, evaluated on `Σ=P^2`, `L=O(3)`, `μ=3+14=17`, `l≥3` (each node is `a_1=a_{3\cdot1-1}`), does not fire (`l>4` fails at `l=3`). A `D_6≅S_3` cover is therefore not produced by this numerical test.

**R16. T95 / T02 Thm 0.2.** Maximizing-sextic and node-cusp numerical tests for non-abelian `π_1`. Same numerical gap as R15. T02 Remark 0.8: Oka’s conjecture that putting only nodes does not change `π_1` is false, via an `S_4`-cover that appears after adding a node. **Yield: STRUCTURE.** Nodes can create `S_4` covers; they do not by themselves kill them.

**R17. T91.** Cardano/Miranda local-to-global for triple covers; cyclic if totally ramified over a simply-connected base. **Yield: STRUCTURE**, already in the charged Miranda residual.

### 2.4 Registry — fold-unions / two rational curves

**R18. ACT08, Theorem 1 and Cor. 2.** Scope: `C=C_1∪C_2`, `deg C_1` even, `C_1` at most simple singularities, `C_2∩Sing(C_1)=∅`, even local intersection of each branch of `C_2` with `C_1`. If `D_{2n}`-covers branched at `2C_1+n C_2` exist for enough odd `n`, they exist for all `n`, and `F_2=G_1^2-G_2^2 F_1`; hence an epimorphism `π_1(P^2\setminus(C_1∪C_2))↠ Z/2 * Z/2`. **Yield: STRUCTURE** for two-component fold-unions. Directly the `(8,4)` rewriting as pullback of a two-component preimage, not a criterion for an irreducible `(6,4)` sextic.

**R19. TT18.** Scope: irreducible 3-nodal quartic `Q` plus a contact conic `C` (even intersection, missing the nodes). Constructs Zariski pairs `(C_1+Q, C_2+Q)` distinguished by Mordell–Weil sections of the rational elliptic surface of `(Q,z_o)`. **Yield: STRUCTURE.** The reducible sextic is quartic+conic, not the irreducible three-node sextic, and not two 3-nodal quartics (degree 8).

**R20. AT04 / T11.** Zariski `k`-plets of rational curve arrangements via dihedral covers; line-conic arrangements of degree 7. **Yield: STRUCTURE** for arrangements, not for the irreducible row.

### 2.5 Combination

**Projective generic triple cover of the row sextic.** R10+R11 reduce existence to torus type. R12 excludes the tame inner configuration `[A_{14},3A_1]`. Remaining loophole: a *non-tame* torus sextic with inner `A_{14}` (`ι=5`) and three *outer* nodes. That loophole is exactly the charged cancellation identity `A^3-B^2=F` with `deg A≤2`, `deg B≤3`, which the charged report already kills under row geometry — a campaign lemma, not a literature theorem. Literature alone: **PARTIAL**, one loophole, closed if a successor applies Oka/Tokunaga Lemma 3 to the explicit three-node equation.

**Projective `S_4` cover branched at `2B`.** R14 necessary condition is not violated at the ADE-subgraph level; the sufficient involution-invariance is uncomputed. **PARTIAL, not a kill.**

**Affine `S_4` transposition tuple (the actual residual `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`).** Every sourced criterion is for covers of `P^2` branched only at `B`. The affine complement is `P^2\setminus(\overline{B}∪L_∞)`. No fetched theorem decides a homomorphism that may send the meridian of `L_∞` nontrivially. **NOTHING as a close.**

**Fold-unions.** R18–R20 supply the language for the `(8,4)` two-component preimage, not a row-kill.

**Q2 verdict. SOURCED-PARTIAL.** The literature would close a *projective* generic triple plane branched at a simple-singularity sextic that is not torus type (R10). It does not close the affine `S_4` tuple, and it does not, by a hashed computation, certify that the explicit `(6,4)` curve fails torus type.

## 3. Question 3 — Certified braid monodromy in practice

**Question.** Version status and limitations of Sage/`sirocco` `braid_monodromy`; published computations at degree-6 simple-singularity scale; alternatives (Marco-Buzunáriz / libbraiding / Bertini); practical notes for a queued AWS job on the `(6,4)` three-node sextic. No CAS is run here.

### 3.1 Fetched sources

| tag | source | URL | SHA-256 | pp |
|---|---|---|---|---|
| MR16 | Marco-Buzunáriz–Rodríguez, *SIROCCO: A library for certified polynomial root continuation*, ICMS 2016, LNCS 9725, 191–197 | Zaragoza `zaguan.unizar.es/record/131386/files/texto_completo.pdf` | `e4e6063240a00dbdf3dfb116fc6ab14dcfec0cc02c9ed19731786a573414388e` | 7 |
| AA18 | Aktas–Akbas, *Computing the braid monodromy of completely reducible n-gonal curves*, arXiv:1611.00249 | `https://arxiv.org/pdf/1611.00249` | `fcf22b6e8d51bb30b15ba318b3f79a5bacad12279a142f9c357ced38f81d3666` | 13 |
| Cog11 | Cogolludo-Agustín, *Braid monodromy of algebraic curves*, Ann. Math. Blaise Pascal **18** (2011), 141–209 | `https://ambp.centre-mersenne.org/item/10.5802/ambp.293.pdf` | `a4c396b2ad06040efc55a82ccdaec4dc579d7b4dcb464a855178a6b9dc8d30ea` | 46 |

**Web documentation (not PDFs; no content-hash).** Sage reference `sage.schemes.curves.zariski_vankampen` (fetched 2026-08-31 from `doc.sagemath.org`); Sage PR #36768 (Artal, 2023-11-25); GitHub `miguelmarco/sirocco2`; `sagemath_sirocco` optional-package page listing `package-version.txt: 10.6`. AskSage 74927 (2023-12-17) on missing branch-point labels.

**SOURCE-OPEN.** Carmona, *Monodromía de trenzas de curvas algebraicas planas*, Ph.D. Zaragoza 2003 (cited as [3] in MR16; no PDF pinned). Bessis–Michel GAP package VKCURVE (described in AA18; no PDF). Bertini / Macaulay2 `NumericalAlgebraicGeometry` (compared in MR16; no package hash). libbraiding C++ library (Sage optional; Garside theory, not continuation).

### 3.2 Registry

**R21. MR16, abstract and §§1–4.** Scope: certified continuation of roots of a bivariate polynomial `f(x,y)` along a real segment in the `x`-line. Interval Newton / Krawczyk; output a piecewise-linear path with a disjoint tubular neighbourhood containing the true root path, hence the induced braid equals the geometric braid. Sage interface advertised as an out-of-the-box fundamental-group computation. Timing (2016, i5-4570): random polynomials of degree 4 through 14; SIROCCO consistently faster than Macaulay2 NAG and fails less often (M2 records multiple “fail” marks from degree 5 up; SIROCCO’s plot is drawn through degree 14). Arithmetic Zariski pairs are cited as the reason a purely algebraic braid computation cannot suffice. **Yield: STRUCTURE.** Degree 6 is inside the published certified range. The test suite is *random* polynomials, not a 3-nodal-plus-`A_{14}` sextic; reducibility, vertical tangents, and high-order discriminant roots are not stress-tested in the paper.

**R22. Sage `zariski_vankampen.braid_monodromy` (docs, 2026-08-31).** Scope: `f` a bivariate polynomial over a number field with an embedding into `QQbar`. Returns a list of braids, a strand-to-component dictionary, and the number of strands. Optional `arrangement=` for a factorization of `f`; optional `vertical=True` to mark vertical-line components and omit them from continuation when they have no vertical asymptotes. If the projection to the `x`-axis has vertical asymptotes, a linear change of variables is performed, except when `vertical=True` and the only vertical asymptotes are lines. `NotImplementedError` if the base field has no embedding into `QQbar`. Optional package `sirocco` required (in Sage since version 8). PR #36768 adds meridians of each component as words and a vertical-line exclusion. **Yield: STRUCTURE.** Matches the AWS need (irreducible sextic: `arrangement` unused; a preparatory shear to kill vertical tangents is the documented path). Known documentation defect: AskSage 74927, the returned object does not label which braid sits over which discriminant point — the list is ordered by the geometric basis of the discriminant complement, not by algebraic `x`-coordinates.

**R23. AA18.** Scope: *completely reducible* `n`-gonal curves. Their RBD algorithm in Sage; VKCURVE (GAP) fails to finish degree `>7` trigonal examples in a day and is tied to an old GAP. A method in [1] of that paper is stated to stop at degree 6. **Yield: NOTHING** for an irreducible sextic. The degree-6 ceiling quoted there is for a different algorithm.

**R24. Cog11.** Survey of Zariski–van Kampen, braid monodromy, and the Zaragoza computational school (Artal, Carmona, Cogolludo, Marco). Records that braid monodromy of plane sextics with simple singularities has been used to distinguish Zariski pairs whose Alexander polynomials agree. **Yield: STRUCTURE.** Published degree-6 computations exist; they are not a computation of the row curve.

**R25. libbraiding / “Bettini-Marco”.** The prompt’s “Bettini-Marco” is Marco-Buzunáriz (SIROCCO). libbraiding is a separate C++ Garside-theory library used by Sage for conjugacy, gcd, and centralizers in braid groups (`# optional - libbraiding`). It does not compute monodromy from a polynomial. Bertini / M2 NAG is uncertified path-tracking for polynomial systems, compared and found less robust for this task in R21. **Yield: STRUCTURE** as a naming clarification; **NOTHING** as a replacement for SIROCCO on this job.

### 3.3 Practical notes for the queued AWS job (not a computation)

1. **Install.** Sage with optional `sirocco` (and `libbraiding` only if braid-word simplification/conjugacy is wanted after the fact). Current Sage optional-package pin in the fetched docs: `sagemath-sirocco` 10.6; SIROCCO itself is the C library of R21, vendored.

2. **Coordinates.** Work over `Q` if the explicit three-node equation is rational; otherwise a number field with a specified embedding into `QQbar`. Apply a generic linear change so that: no vertical asymptote, no vertical tangent at a node, the unique infinite place `A_{14}` is not a vertical fibre, and the discriminant of `f(x,y)` in `y` is squarefree except at the known singularities. R22 will itself shear if it detects vertical asymptotes; a pre-shear keeps the geometric basis aligned with a chosen line at infinity.

3. **Scale.** Six strands. Discriminant degree for a degree-6 plane curve is on the order of `30`. R21’s random tests at degree 6–10 succeeded in seconds to tens of seconds on 2014-era hardware; the `A_{14}` fibre is a high-order discriminant point and may force small interval steps. Budget hours, not milliseconds; certification may increase precision automatically (sirocco2 README: fallback to higher MPFR precision on failure).

4. **Irreducibility.** Do not pass `arrangement=`. Node meridians are recovered after the fact from the local braid (a full twist of two strands, commuting if the node is an ordinary double point of two smooth branches).

5. **What certification buys.** The braid list is the geometric monodromy. The subsequent finitely-presented group and the search for a homomorphism to `S_4` sending meridians to transpositions with node-commutation, and with the infinity cable equal to the `(6,4)` braid, are exact algebra in the braid group / `S_4`. That algebra is not SIROCCO’s responsibility and is the actual residual `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`. A certified braid that admits no such homomorphism would close the row; a certified braid that admits one would close the “existence” half and leave only the algebra/resolvent questions of Q1.

6. **Do not treat Sage’s `fundamental_group(...).simplified()` as a uniqueness theorem.** Tietze simplification is one-sided: a trivial simplified presentation proves `π_1` is the printed group; a complicated presentation proves nothing about non-existence of an `S_4` quotient. Test homomorphisms to `S_4` directly on the unsimplified van Kampen presentation.

**Q3 verdict. STRUCTURE, not a literature close.** SIROCCO/Sage is the right certified tool at this scale; there is no published braid of the row curve. The AWS job is well-posed. No alternative in the fetched sources dominates it for an irreducible sextic.

## 4. Verdicts

| Q | literature verdict | what it would have short-circuited | residual |
|---|---|---|---|
| 1. Unit representation of binary cubics over `C[x,y]` | **ABSENT** as a close; **STRUCTURE** as Delone–Faddeev–Wood–Deligne parametrization | emptiness of `R_{F,S4}^{nm}` / global monogenicity | `I(s,t)=1` over `C[x,y]` is still a new lemma |
| 2. `π_1` / Tokunaga `S_3`/`S_4` at the `(6,4)` sextic or fold-unions | **SOURCED-PARTIAL** | projective generic triple plane; possibly projective `S_4` | affine transposition tuple `OPEN[PI1S4-(6,4)-FIXED-TUPLE]` untouched; torus-type of the explicit curve uncomputed in literature |
| 3. Certified braid monodromy | **STRUCTURE** | a computed braid that admits / forbids the `S_4` tuple | no published braid of this curve; AWS job is the computation |

No combination of hashed theorems closes the running residual. The nearest literature kill is IT09 Theorem 1.1 plus a torus-type exclusion of the explicit three-node sextic (Oka/Tokunaga Lemma 3, or the charged cancellation lemma applied to homogeneous `G_2,G_3`). That kill would be of a *projective* generic triple cover of `P^2`, strictly smaller than the affine `S_4` residual.

## 5. Acquisition list

Pin as PDFs, with hashes, before any promotion that consumes them.

1. P. Deligne, letter to W. T. Gan, B. Gross and G. Savin, 13 November 2000 (unpublished; W10 [7]). Reconstructing from W10 is flagged as secondary.
2. B. N. Delone and D. K. Faddeev, *The theory of irrationalities of the third degree*, AMS Transl. Math. Monogr. 10 (1964) (or the 1940 Steklov original).
3. G. Casnati and T. Ekedahl, *Covers of algebraic varieties I*, J. Algebraic Geom. **5** (1996), 439–460.
4. H. Tokunaga, *On dihedral Galois coverings*, Canad. J. Math. **46** (1994), 1299–1317 (CJM 403 here).
5. Journal typesetting of Tokunaga, Math. Ann. **308** (1997), 633–648 (T95 is the MPIM preprint).
6. E. Artal Bartolo, J. I. Cogolludo and H. Tokunaga, *A survey on Zariski pairs*, Adv. Stud. Pure Math. **50** (2008), 1–100 (full PDF).
7. J. Carmona, *Monodromía de trenzas de curvas algebraicas planas*, Ph.D. thesis, Universidad de Zaragoza, 2003.
8. D. T. Pho’s list of tame torus-sextic configurations (cited as [12] in Oka05); journal form of Oka, *Zariski pairs on sextics I*.
9. The explicit equation of the three-node `(6,4)` curve from the row-sweep producer (not a literature item; needed to run Oka/Tokunaga Lemma 3 and the AWS braid job).
10. Gross–Lucianovic, *On cubic rings and quaternion rings* (standard citation; arXiv number not pinned in this lane).
11. Wood, *Gauss composition over an arbitrary base*, Adv. Math. **226** (2011), 1756–1771 (quadratic, not cubic; optional).

Not needed to start a proof lane, but adjacent: Tan, *Triple covers on smooth algebraic varieties*; Ishida, thesis `tokyo-metro-u.repo.nii.ac.jp/record/2106`; Catanese–Perroni, *Dihedral Galois covers of algebraic varieties and the simple cases*, J. Geom. Phys. **118** (2017).

## 6. Scope and non-claims

This is a literature registry. It does not prove or refute the `(6,4)` row, does not identify a cv flag with a physical place or a cover series, and does not assert an exit price. Yields `CLOSES` / `PARTIAL` / `STRUCTURE` / `NOTHING` are relative to the three named questions, not promotions into the coordinator ledger. The charged cancellation lemma and the weighted-degree counterexample (2.1) are campaign items, cited only to locate the residual; they are not re-proved. Row geometry remains provisional as in the coordinator input.

Two arXiv fetches were the wrong papers (`math/0608376`, `0907.3719`) and are not used. Tokunaga Osaka was obtained from Euclid `pdf_1/euclid.ojm/1153492850` after the journal URL returned HTML. Miranda’s CSU preprint rehashed identically to the charged triple-cover-close receipt.

<!-- BODY-END -->
