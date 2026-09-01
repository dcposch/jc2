# KEYSTONE 1 — Mathlib coverage survey and formalization lane plan

**Lane:** k1-mathlib-survey-and-plan · **Model:** Opus 5 · **Date:** 2026-09-01
**Deliverable type:** LIBRARY SURVEY + LANE PLAN. No proofs, no promotions, no exit-price
assertions.

---

## 0. Sources of truth and how they were read

### Source (i) — pinned Mathlib, rev `20bc12820422504f9e52ee6caebf8182a9015336`

**Access note (disclosure).** The brief points at `~/code/math/jc2/jc2-lean/*/`. That path is a
**git submodule** (`.gitmodules`: `path = jc2-lean`, `url = https://github.com/dcposch/jc2-lean.git`,
gitlink `e84e32bce699b64ba1995d7bdb6dafb1e7bdf5a4`) whose **working tree is not readable from this
session**: `ls`, `stat` and `find` all return `Operation not permitted` (EPERM), including with the
sandbox explicitly disabled. So I could not grep that checkout.

**What I did instead.** The exact pinned commit is present in the object store of another local
Mathlib clone:

```
/Users/dc/code/math/palomar/albertson-berman-palomar/.lake/packages/mathlib
$ git cat-file -t 20bc12820422504f9e52ee6caebf8182a9015336   ->  commit
$ git log -1 --format='%H %ad %s' --date=iso 20bc1282...
  20bc12820422504f9e52ee6caebf8182a9015336 2026-08-19 19:09:03 +0000
  feat(NumberTheory/Height): bound the natural denominator by multiplicative height (#42891)
$ git describe --tags 20bc1282...  ->  master-2026-08-19-25-g20bc128204
$ git show 20bc1282...:lean-toolchain  ->  leanprover/lean4:v4.34.0-rc1
$ git ls-tree -r 20bc1282... --name-only -- Mathlib | grep -c '\.lean$'  ->  8350
```

Every "at the pin" claim below was produced by `git show <rev>:<path>` or
`git grep <pat> <rev> -- 'Mathlib/**/*.lean'` against that object store, i.e. against the byte-exact
pinned tree. **All file:line references below are line numbers in the pinned tree**, not in any
working copy.

Note also: `~/code/math/jc2/lean/` (a different, non-submodule project in this repo) pins Mathlib at
`905b95818eb32af7874a58b427f50c1711a5e96c` / `v4.32.2`. The campaign rev is newer.

### Source (ii) — current Mathlib master

`master = cf0e3d85122aa011a80a4329530261fe229de12b`, authored `2026-09-01T20:11:15Z` (today),
via `gh api repos/leanprover-community/mathlib4/commits/master`.

Cheap high-coverage delta check: I fetched `Mathlib.lean` from master (8472 module lines) and
diffed the module list against `git show <pin>:Mathlib.lean` (8350):

- **142 modules added** pin → master. Filtering to `RingTheory|AlgebraicGeometry|FieldTheory|
  NumberTheory`, the only additions are `NumberTheory.{CarmichaelNumber, FundamentalDiscriminant,
  ModularForms.RamanujanFormula, Padics.LocalField, Padics.Measure.AmiceTransform}` and
  **`RingTheory.Localization.Saturation`**. None is relevant to K1.
- **0 modules removed** in `RingTheory|AlgebraicGeometry`.

**Conclusion: for every item in this survey the pin and master agree**, up to declarations added
inside pre-existing files (which the diff would not catch — see the per-item GitHub code-search
probes below, which do catch those).

GitHub code-search probes on `repo:leanprover-community/mathlib4` (master), with a **positive
control** to prove search was live:

| query | `total_count` |
|---|---|
| `ZariskisMainProperty` (positive control) | **3** |
| `CohenMacaulay` | 0 |
| `AuslanderBuchsbaum` | 0 |
| `Module.depth` | 0 |
| `IsTamelyRamified` | 0 |
| `Jelonek` | 0 |
| `IsCohenMacaulay` | 0 |
| `purity` | 1 → `Mathlib/CategoryTheory/Presentable/CardinalPure.lean` (unrelated) |

Further probes (`Ideal.depth`, `isRegularLocalRing_of`, `ExcellentRing`, …) hit the GitHub search
rate limit (403) and are recorded below as **UNVERIFIED on master**; all of them were verified
ABSENT at the pin, and the module-list diff shows no new file that could plausibly host them.

---

## PART A — coverage survey

Legend: **EXISTS** / **PARTIAL** / **ABSENT**. "Src" = which source the verdict rests on.

---

### A.1 Zariski's Main Theorem and quasi-finite API — **EXISTS (both layers)**

Src: (i) direct read; (ii) module diff + positive control.

**Ring-theoretic ZMT** — `Mathlib/RingTheory/ZariskisMainTheorem.lean`:

| decl | line |
|---|---|
| `Algebra.ZariskisMainProperty (p : Ideal S) : Prop` | 75 |
| `Algebra.zariskisMainProperty_iff` (`∃ r ∉ p, IsIntegral R r ∧ ∀ x, ∃ m, IsIntegral R (r^m*x)`) | 79 |
| `Algebra.zariskisMainProperty_iff'`, `..._iff_exists_saturation_eq_top` | 88, 96 |
| `ZariskisMainProperty.of_isIntegral`, `.restrictScalars`, `.trans` | 131, 102, 109 |
| `ZariskisMainProperty.of_finiteType` `@[stacks 00Q9]` | 658 |
| `ZariskisMainProperty.of_finiteType_of_weaklyQuasiFiniteAt` `@[stacks 00Q9]` | 635 |
| `ZariskisMainProperty.exists_fg_and_exists_notMem_and_awayMap_bijective` | 664 |
| `Algebra.QuasiFiniteAt.exists_fg_and_exists_notMem_and_awayMap_bijective` | 701 |
| `ZariskisMainProperty.quasiFiniteAt`, `QuasiFiniteAt.of_*`, `quasiFiniteAt_iff_isOpen_singleton_fiber` | 708–752 |

The `..._awayMap_bijective` pair is the *ring-level open-immersion statement*: at a quasi-finite
prime there is `r ∉ p` with `A_r → S_r` bijective (localization away from an integral element).

**Scheme-level ZMT** — `Mathlib/AlgebraicGeometry/ZariskisMainTheorem.lean`:

| decl | line |
|---|---|
| `AlgebraicGeometry.exists_etale_isCompl_of_quasiFiniteAt` | 49 |
| `Scheme.Hom.exists_isIso_morphismRestrict_toNormalization` `@[stacks 03GW]` | 206 |
| `Scheme.Hom.quasiFiniteLocus` (as `X.Opens`), `mem_quasiFiniteLocus` | 316, 321 |
| `instance … : IsOpenImmersion (f.quasiFiniteLocus.ι ≫ f.toNormalization)` | 325 |
| `instance [LocallyQuasiFinite f] [LocallyOfFiniteType f] [IsSeparated f] [QuasiCompact f] : IsOpenImmersion f.toNormalization` | 359 |
| `IsFinite.of_isProper_of_locallyQuasiFinite` | 373 |

**Relative normalization** — `Mathlib/AlgebraicGeometry/Normalization.lean` (this is the object our
`Y = Spec B` *is*):

| decl | line |
|---|---|
| `Scheme.Hom.normalization` (for qcqs `f : X ⟶ Y`) | 126 |
| `Scheme.Hom.toNormalization : X ⟶ f.normalization` (our `j`) | 136 |
| `Scheme.Hom.fromNormalization : f.normalization ⟶ Y` (our `q`) | 173 |
| `instance : IsIntegralHom f.fromNormalization` | 199 |
| `normalizationObjIso` — sections = integral closure of `Γ(Y,U)` in `Γ(X, f⁻¹U)` | 219 |
| `instance : IsDominant f.toNormalization`, `ker_toNormalization = ⊥` | 340, 327 |
| `instance [IsAffineHom f] : IsAffineHom f.toNormalization` | 307 |
| universal property: `normalizationDesc`, `normalization.hom_ext` | 376, 440 |
| `instance [IsIntegral X] : IsIntegral f.normalization` | 357 |

**Quasi-finite API** — files `Mathlib/RingTheory/QuasiFinite/{Basic,Polynomial,Weakly}.lean`,
`Mathlib/RingTheory/RingHom/QuasiFinite.lean`, `Mathlib/RingTheory/Etale/QuasiFinite.lean`,
`Mathlib/AlgebraicGeometry/Morphisms/QuasiFinite.lean`. Key: `Algebra.QuasiFinite` class
(`QuasiFinite/Basic.lean:67`), `Algebra.QuasiFiniteAt` (:357),
`instance (priority := low) [Module.Finite R S] : QuasiFinite R S` (:107),
`Algebra.QuasiFinite.finite_primesOver` (:84), `RingHom.QuasiFinite.of_finite`
(`RingHom/QuasiFinite.lean:51`).

**Assessment for K1(1).** This is a near-instantiation, not a project. Residual work is two small
identifications, not ZMT itself:
1. `f.normalization ≅ Spec B` for `f = Spec(A → C[x,y])` — available from `normalizationObjIso` +
   `IsAffineHom f.toNormalization`.
2. `integralClosure A C[x,y] = integralClosure A C(x,y)` (i.e. `B ⊆ C[x,y]` is automatic), from
   `IsIntegrallyClosed C[x,y]` + transitivity of integrality. Small.

---

### A.2 Zariski–Nagata purity + supporting depth theory — **ABSENT (the hard gap)**

| sub-item | verdict | evidence |
|---|---|---|
| Purity of the branch locus (any form) | **ABSENT** | `git grep -i "purity\|zariski.?nagata\|branch locus\|branchLocus"` at pin → **0 hits**. Master: `purity` → 1 hit, `CategoryTheory/Presentable/CardinalPure.lean`, unrelated. |
| Auslander–Buchsbaum formula | **ABSENT** | `git grep -rn -i auslander` at pin → **0 hits**; master search `AuslanderBuchsbaum` → 0. |
| Cohen–Macaulay rings/modules | **ABSENT** | `git grep -l -i cohenmacaulay` at pin → **0 files**; master `CohenMacaulay` → 0, `IsCohenMacaulay` → 0. |
| Serre's criteria `R_k`/`S_k` | **ABSENT** | only `CategoryTheory.ObjectProperty.IsSerreClass` (a Serre *class* of objects, `CategoryTheory/Abelian/SerreClass/Basic.lean:47`) — different notion. |
| depth (the invariant) | **ABSENT as a definition; PARTIAL as machinery** | no `Module.depth` / `Ideal.depth` at pin (`git grep "def depth"` → only `WType.depth`, `Data/W/Basic.lean:113`); master `Module.depth` → 0. **But** `Mathlib/RingTheory/Depth/Rees.lean` proves Rees's theorem `ModuleCat.exists_isRegular_tfae` (Ext-vanishing ⟺ ∃ regular sequence of length `n` in `I`), and `Mathlib/RingTheory/Regular/{RegularSequence,Category,Flat,Free,IsSMulRegular,LinearMap,ProjectiveDimension}.lean` give `RingTheory.Sequence.IsWeaklyRegular` / `IsRegular`. So depth is *definable in one lane* on top of what exists. |
| Miracle flatness | **ABSENT** | `git grep -i "miracle\|flat_of_.*regular"` → only `AlgebraicGeometry/EffectiveEpi.lean:23` (regular *epimorphism*, unrelated). |
| projective dimension | **EXISTS** | `Mathlib/RingTheory/Regular/ProjectiveDimension.lean`, `Mathlib/RingTheory/LocalProperties/ProjectiveDimension.lean`, `Mathlib/Algebra/Category/ModuleCat/ProjectiveDimension.lean`, `Mathlib/CategoryTheory/Abelian/Projective/Dimension.lean`. |
| regular local / regular rings | **PARTIAL** | `IsRegularLocalRing` (`RingTheory/RegularLocalRing/Defs.lean:51`), `IsRegularRing` (:92). Only two files in that dir (`Defs.lean`, `Polynomial.lean`). No "regular ⟹ normal", no "regular ⟹ UFD", no AB. |
| Krull's height theorem | **EXISTS** | `Mathlib/RingTheory/Ideal/KrullsHeightTheorem.lean`: `Ideal.height_le_one_of_isPrincipal_of_mem_minimalPrimes` (:108) and the local version (:60). |
| reflexive modules (comm-alg sense) | **PARTIAL / mismatched** | `Module.IsReflexive` exists (`LinearAlgebra/Dual/Defs.lean:213`) but is the *bidual-isomorphism* linear-algebra class used by root systems, **not** reflexive-hull / `S_2` theory over a Noetherian domain. |

**Assessment.** Purity is a genuine multi-lane library project, from the ground up. There is no
shortcut in the library: the AB → CM → miracle-flatness → purity chain has **zero** of its four
links. This is the one place where K1 is far from Mathlib.

---

### A.3 Finiteness of integral closure; Krull/DVR API — **EXISTS in exactly the form K1 needs**

`Mathlib/RingTheory/DedekindDomain/IntegralClosure.lean` (AKLB setting: `A` domain, `K = Frac A`,
`L/K` finite, `C` with `[IsIntegralClosure C A L]`, plus `[Algebra.IsSeparable K L]` from line 139):

| decl | line | hypotheses |
|---|---|---|
| `IsIntegralClosure.isNoetherian : IsNoetherian A C` | 152 | `[IsIntegrallyClosed A] [IsNoetherianRing A]` |
| `IsIntegralClosure.isNoetherianRing : IsNoetherianRing C` | 168 | same |
| **`IsIntegralClosure.finite : Module.Finite A C`** | 175 | same |
| `IsIntegralClosure.module_free : Module.Free A C` | 183 | `[IsTorsionFree A L] [IsPrincipalIdealRing A]` |
| `IsIntegralClosure.rank : finrank A C = finrank K L` | 192 | `[IsPrincipalIdealRing A] [IsTorsionFree A L]` |
| `IsIntegralClosure.isDedekindDomain : IsDedekindDomain C` | 220 | `[IsDedekindDomain A] [IsDomain C]` |

This is precisely the trace-form argument, and `A = C[P,Q]`, `K = C(P,Q)`, `L = C(x,y)` satisfy every
hypothesis (char 0 ⟹ separable).

Supporting:

- `A` normal: `UniqueFactorizationMonoid (MvPolynomial σ D)` at
  `Mathlib/RingTheory/Polynomial/UniqueFactorization.lean:119, 131`; and
  `UniqueFactorizationMonoid.instIsIntegrallyClosed` (used at `DedekindDomain/Basic.lean:174`,
  `Polynomial/IsIntegral.lean:179`). **EXISTS.**
- **Krull-domain API: ABSENT.** `git grep -l IsKrullDomain` → 0 files; no `Mathlib/RingTheory/Krull*`
  directory. Not needed for K1 (Noetherian normal suffices).
- **height-1 localization of a normal Noetherian domain is a DVR: PARTIAL but assembled from
  existing parts.** No single named lemma, but all three ingredients exist:
  - `isIntegrallyClosed_of_isLocalization` (`RingTheory/IntegralClosure/IntegrallyClosed.lean:380`);
  - `IsLocalization.AtPrime.ringKrullDim_eq_height` (`RingTheory/Ideal/Height.lean:418`);
  - `IsDiscreteValuationRing.TFAE` (`RingTheory/DiscreteValuationRing/TFAE.lean:210`), whose item 3
    is exactly `IsIntegrallyClosed R ∧ ∃! P : Ideal R, P ≠ ⊥ ∧ P.IsPrime`, and
    `tfae_of_isNoetherianRing_of_isLocalRing_of_isDomain` (:168) for the `≤ 1` version.
  - Dedekind special case already packaged: `DedekindDomain/Dvr.lean:114`
    (`[IsLocalization.AtPrime Aₘ P] → IsDiscreteValuationRing Aₘ`).
  - For a **UFD** base (our `A`) there is a shorter route: `Ideal.eq_span_singleton_of_height_eq_one`
    (`RingTheory/Ideal/Height.lean:564`) ⟹ height-1 primes are principal ⟹ `A_𝔭` is a local PID.

---

### A.4 Dedekind ramification: Σe·f, different, tameness — **EXISTS, except tameness**

**Σ e·f = n, in a form strictly better than Dedekind.**
`Mathlib/RingTheory/RamificationInertia/Basic.lean` (file docstring: *"Typically this is only stated
for extensions of Dedekind domains, but we prove it for any finite flat extension of an integral
domain."*):

```lean
-- RingTheory/RamificationInertia/Basic.lean:44
theorem Ideal.sum_ramification_inertia_eq_finrank_fiber
    [Algebra.QuasiFinite R S] [Fintype (p.primesOver S)] :
    ∑ q : p.primesOver S, q.1.ramificationIdx R * q.1.inertiaDeg R
      = finrank p.ResidueField (p.Fiber S)

-- RingTheory/RamificationInertia/Basic.lean:72   <-- the Stage-1 workhorse
theorem Ideal.sum_ramification_inertia_eq_finrank
    [IsDomain R] [Module.Finite R S] [Module.Flat R S] [Fintype (p.primesOver S)] :
    ∑ q : p.primesOver S, q.1.ramificationIdx R * q.1.inertiaDeg R = Module.finrank R S

-- RingTheory/RamificationInertia/Basic.lean:81  (Galois form)
theorem Ideal.sum_ramification_inertia_eq_card … = Nat.card G
```

Definitions: `Ideal.ramificationIdx q R` = `(Module.length Sq (Sq ⧸ (q.under R).map …)).toNat`
(`RingTheory/RamificationInertia/Ramification.lean:52`); `Ideal.inertiaDeg q R` =
`finrank (q.under R).ResidueField q.ResidueField` (`RingTheory/RamificationInertia/Inertia.lean:44`).
Classical Dedekind version also present: `Ideal.sum_ramification_inertia`
(`NumberTheory/RamificationInertia/Basic.lean:615`), plus the local/DVR corollary at :669 and the
Galois file `NumberTheory/RamificationInertia/Galois.lean`.

Unramified ⟹ `e = 1`: `Ideal.ramificationIdx_eq_one_of_isUnramifiedAt`
(`NumberTheory/RamificationInertia/Unramified.lean:35`), hypotheses `[IsUnramifiedAt R p]
[EssFiniteType R S]`. Also `IsUnramifiedIn.ramificationIdx_eq_one` (:152) and
`isUnramifiedIn_iff_forall_ramificationIdx_eq_one` (:161).

`Fintype (p.primesOver S)`: from `Algebra.QuasiFinite.finite_primesOver`
(`RingTheory/QuasiFinite/Basic.lean:84`), or the Dedekind instance at
`RingTheory/DedekindDomain/Ideal/Lemmas.lean:1240`.

**Different ideal — `Mathlib/RingTheory/DedekindDomain/Different.lean`:**

| decl | line |
|---|---|
| `Submodule.traceDual`, `FractionalIdeal.dual` | 57, 229 |
| `differentIdeal : Ideal B` | 480 |
| `differentIdeal_ne_bot` | 542 |
| `differentIdeal_eq_differentIdeal_mul_differentIdeal` (transitivity) | 571 |
| `conductor_mul_differentIdeal` (`𝔣 * 𝔇 = (f'(x))` when `L = K[x]`) | 637 |
| `aeval_derivative_mem_differentIdeal` | 676 |
| **`pow_sub_one_dvd_differentIdeal` : `P^e ∣ pB → P^(e−1) ∣ 𝔇`** | 742 |
| `not_dvd_differentIdeal_iff : ¬P ∣ 𝔇 ↔ Algebra.IsUnramifiedAt A P` | 912 |
| `dvd_differentIdeal_iff : P ∣ 𝔇 ↔ ¬ IsUnramifiedAt A P` | 958 |

**Tame ramification — ABSENT.** `git grep -i "tamelyramified\|IsTamelyRamified\|tame"` over
`Mathlib/RingTheory/**` and `Mathlib/NumberTheory/**` at the pin → **0 hits**; master search
`IsTamelyRamified` → 0.

> **FALLACY-v2 [Floor/attainment].** What Mathlib supplies is `P^(e−1) ∣ 𝔇`, i.e. a **floor**
> `v_P(𝔇) ≥ e − 1`, plus the qualitative `P ∣ 𝔇 ↔ ramified`. The char-0 **equality**
> `v_P(𝔇) = e − 1` is *not* in the library and must not be quoted from
> `pow_sub_one_dvd_differentIdeal`. It is the load-bearing missing step for K1(4) and gets its own
> lane (K1-L17) with its own proof obligation.

**Semilocal reduction — smooth to set up.** Localizing `A` at a height-1 prime gives a DVR (A.3);
`Localization.AtPrime`, `Localization.AtPrime.algebraOfLiesOver`, `Ideal.primesOver`,
`Ideal.under`, `Ideal.LiesOver` are all present and are exactly the interface
`sum_ramification_inertia_eq_finrank` and `differentIdeal` already speak.

---

### A.5 Jacobian criterion for étale/unramified/smooth — **PARTIAL, but K1 needs only the Ω-route, which EXISTS**

Standard-smooth machinery (present):

| decl | file:line |
|---|---|
| `Algebra.PreSubmersivePresentation` | `RingTheory/Extension/Presentation/Submersive.lean:67` |
| `Algebra.SubmersivePresentation` | same:495 |
| `PreSubmersivePresentation.jacobian` | same:118 |
| `jacobian_eq_jacobiMatrix_det`, `jacobian_eq_det_aevalDifferential` | same:134, 154 |
| `isUnit_jacobian_iff_aevalDifferential_bijective` | same:160 |
| `Algebra.IsStandardSmooth`, `IsStandardSmoothOfRelativeDimension` | `RingTheory/Smooth/StandardSmooth.lean:62, 88` |
| `RingHom.etale_iff_isStandardSmoothOfRelativeDimension_zero` | `RingTheory/RingHom/LocallyStandardSmooth.lean:52` |
| `Algebra.Etale.iff_isStandardSmoothOfRelativeDimension_zero` | same:55 |
| `Mathlib/RingTheory/Etale/StandardEtale.lean`, `.../Etale/{Kaehler,Field,Locus,Finite}.lean` | — |

What is **missing** is a packaged "invertible Jacobian ⟹ étale" for an extension like
`C[P,Q] ⊆ C[x,y]` that is not handed to Mathlib as a presentation.

**But the four-box étale-box needs only *unramified*, and that is definitional:**

```lean
-- RingTheory/Unramified/Basic.lean:58–61
@[mk_iff, stacks 00UM]
class Algebra.FormallyUnramified : Prop where
  subsingleton_kaehlerDifferential : Subsingleton Ω[A⁄R]
```

so `formallyUnramified_iff` reduces the box to `Subsingleton Ω[C[x,y] ⁄ C[P,Q]]`, which the Keller
hypothesis gives by surjectivity of `KaehlerDifferential.mapBaseChange` (A.6). Then
`Algebra.IsUnramifiedAt` (`RingTheory/Unramified/Locus.lean:45`) at every prime, then
`Ideal.ramificationIdx_eq_one_of_isUnramifiedAt`. Also available for the codim/openness side:
`Algebra.unramifiedLocus`, `Algebra.isOpen_unramifiedLocus`,
`Algebra.basicOpen_subset_unramifiedLocus_iff`, `Algebra.unramifiedLocus_eq_univ_iff`
(`RingTheory/Unramified/Locus.lean` docstring).

---

### A.6 Kähler differentials, Ω², and the 2-form valuation — **Ω¹ EXISTS; Ω² ABSENT; the valuation bridge ABSENT**

**Ω¹ — EXISTS, with everything we need.** `Mathlib/RingTheory/Kaehler/{Basic,Polynomial,
TensorProduct,JacobiZariski}.lean`:

| decl | file:line |
|---|---|
| `KaehlerDifferential.mapBaseChange : B ⊗[A] Ω[A⁄R] →ₗ[B] Ω[B⁄R]` | `Kaehler/Basic.lean:719` |
| `KaehlerDifferential.range_mapBaseChange` | same:729 |
| **`KaehlerDifferential.exact_mapBaseChange_map`** (2nd fundamental exact sequence) | same:756 |
| `KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange` (conormal) | same:839 |
| `KaehlerDifferential.mapBaseChange_surjective` | same:844 |
| `KaehlerDifferential.mvPolynomialBasis (σ)` (free basis `dXᵢ`) | `Kaehler/Polynomial.lean:60` |
| `instance : Module.Free (MvPolynomial σ R) Ω[MvPolynomial σ R⁄R]` | same:98 |
| `KaehlerDifferential.isLocalizedModule_of_isLocalizedModule` (Ω localizes) | `Kaehler/TensorProduct.lean:17` |

**Ω² / exterior powers — the module theory EXISTS, the differential-forms instance does NOT.**
`Mathlib/LinearAlgebra/ExteriorPower/{Basic,Basis,Pairing}.lean` and
`Mathlib/LinearAlgebra/ExteriorAlgebra/{Basic,Basis,Grading,OfAlternating}.lean` exist, so
`⋀²(Ω[R⁄C])` is *constructible*. But:

- `git grep "exteriorPower.*KaehlerDifferential\|KaehlerDifferential.*exteriorPower"` → **0 hits**.
- No `Ω²` abbreviation, no de Rham complex over a general base, no `Ω^n` API.

**Valuation of a 2-form along a divisorial valuation — ABSENT.**

- No `differentIdeal` ↔ `KaehlerDifferential` bridge anywhere: `differentIdeal` occurs in exactly 4
  files (`RingTheory/DedekindDomain/{Different,LinearDisjoint}.lean`,
  `NumberTheory/NumberField/{Cyclotomic/Basic, Discriminant/Different}.lean`), none mentioning
  Kähler differentials.
- **Fitting ideals of modules: ABSENT.** `git grep -l "fittingIdeal\|Fitting"` returns only
  `Algebra/Lie/*` and `RingTheory/Artinian/Module.lean` — that is the *Fitting decomposition* of a
  Lie module, a different notion. So the natural "`𝔇 = Fitt₀ Ω_{B/A}`" bridge cannot be stated
  off-the-shelf.
- No Weil-divisor / divisor-class-group theory for schemes (`ls Mathlib/AlgebraicGeometry | grep -i
  divisor` → only `EllipticCurve/NormalForms.lean`).

**What DOES exist for valuations of *scalars*:**

| decl | file:line |
|---|---|
| `Ring.ord (x : R) : ℕ∞ := Module.length R (R ⧸ Ideal.span {x})` | `RingTheory/OrderOfVanishing/Basic.lean:36` |
| `Ring.ordFrac : K →*₀ ℤᵐ⁰` | same:324 |
| `Ring.ordFrac_of_isUnit` | `RingTheory/OrderOfVanishing/Noetherian.lean:154` |
| `AlgebraicGeometry.Scheme.ordHom (z) (hz : coheight z = 1)` | `AlgebraicGeometry/OrderOfVanishing.lean:31` |
| `AlgebraicGeometry.Scheme.ord (f : X.functionField) (z : X) : ℤ` | same:52 |

(scheme versions need `[IsIntegral X] [IsLocallyNoetherian X]`.)

**Consequence for K1(4).** The clean recasting is: replace `v_j(dx∧dy)` by `v_j(𝔇_{B/A})` (order of
the different at the boundary prime), which *is* expressible today; then K1(4) becomes
`e_j = 1 + v_j(𝔇)`, i.e. exactly the missing tameness equality of A.4. The genuine 2-form statement
(`dP∧dQ = Jac·dx∧dy` in `⋀²Ω¹`, and `div(q*ω) = R`) is a separate, optional, longer lane.

---

### A.7 Is anything forced out of pure commutative algebra? — **No, except the literal words "open immersion"**

Item-by-item recasting assessment:

| K1 claim | ring-theoretic recasting | statement-strength lost |
|---|---|---|
| (1) `A ⊆ B ⊆ C[x,y]`, `q ∘ j = F` | inclusions of subalgebras of `C[x,y]`; `B := integralClosure A C[x,y]`; composite is the identity inclusion | **none** |
| (1) `j : C² → Y` open immersion | for each prime `𝔮` of `B` in the image, `∃ r ∈ B ∖ 𝔮` with `B_r → C[x,y]_r` bijective (`ZariskisMainProperty.exists_fg_and_exists_notMem_and_awayMap_bijective`) | the **global gluing** — that the union of those `D(r)` is an open subscheme on which `j` is *one* isomorphism. Pointwise-local-iso ⟹ open immersion needs the scheme layer (or an ad-hoc gluing lemma). For K1(2)–(4), which are all statements at individual primes, the pointwise form is sufficient. |
| (2) `Y ∖ U` nonempty, pure codim 1 | `{𝔮 : Ideal B // 𝔮.IsPrime ∧ ¬ ZariskisMainProperty …}` is nonempty and every member has `height = 1` | none (Mathlib has `Ideal.height`) |
| (2) `A_F = q(Y∖U)` | **taken as the definition** (see A.9) | the Jelonek comparison becomes an uncited external remark |
| (3) Σ e = d, four boxes | `Ideal.sum_ramification_inertia_eq_finrank` over `Localization.AtPrime 𝔭` | none |
| (4) `e_j = 1 + v_j(dx∧dy)` | `e_𝔮 = 1 + v_𝔮(differentIdeal)` | the 2-form reading; recovering it needs the `⋀²Ω¹` + ramification-divisor bridge (A.6) |

**Recommendation.** State Stages 1–2 **entirely ring-theoretically**; import
`Mathlib.AlgebraicGeometry` only in the Stage-3 wrapper for (1). Rationale: (a) the scheme layer's
ZMT is already done, so nothing is *gained* by delaying; (b) the ring layer keeps elaboration times
and instance search cheap, which matters for lanes running beside the Max-11 campaign; (c) every
Stage-1 statement is a height-1/local statement, where the scheme layer would only add plumbing.

---

### A.8 Algebraic independence of `P,Q` from `Jac(P,Q) ≠ 0`; the degree-`d` API — **PARTIAL**

Present:

| decl | file:line |
|---|---|
| `AlgebraicIndependent` and API | `RingTheory/AlgebraicIndependent/{Defs,Basic,Adjoin,Transcendental,TranscendenceBasis,RankAndCardinality,AlgebraicClosure}.lean` |
| `Algebra.trdeg` | `RingTheory/AlgebraicIndependent/TranscendenceBasis.lean` |
| `Algebra.trdeg_add_eq` `@[stacks 030H]` | same:546 |
| `Algebra.trdeg_eq_zero_iff : trdeg R A = 0 ↔ Algebra.IsAlgebraic R A` | `.../Transcendental.lean:89` |
| `FinTrdeg`, `finTrdeg_iff_trdeg`, `FinTrdeg.trans` | `FieldTheory/FinTrdeg.lean:26, 39, 61` |
| `Algebra.FormallyUnramified.iff_isSeparable` (fields, `[EssFiniteType K L]`) | `RingTheory/Unramified/Field.lean:217` |
| `Algebra.FormallyEtale.iff_isSeparable` | `RingTheory/Etale/Field.lean:158` |
| `Algebra.IsIntegral.finite` (integral + finite type ⟹ module-finite) | `RingTheory/IntegralClosure/IsIntegralClosure/Basic.lean:96` |
| `Module.rankAtStalk`, `Module.freeLocus`, `Module.isLocallyConstant_rankAtStalk` | `RingTheory/Spectrum/Prime/FreeLocus.lean` |

**ABSENT:** the implication itself. `git grep -i "algebraicIndependent.*jacobi\|jacobi.*
algebraicIndependent\|algebraicIndependent_iff_.*det"` → **0 hits**.

**Proposed route (all consumables present, no circularity):**
1. `Ω[C[x,y]⁄C]` is free of rank 2 on `dx, dy` (`mvPolynomialBasis`).
2. `dP, dQ` span it, because the change-of-basis matrix is the Jacobian, a unit.
3. Hence `KaehlerDifferential.mapBaseChange C (adjoin C {P,Q}) C[x,y]` is **surjective**
   (`range_mapBaseChange`) — note this direction needs only that `dP,dQ` are in the range, **not**
   that `Ω` of the subalgebra is free, so it does **not** presuppose `P,Q` independent.
4. `exact_mapBaseChange_map` ⟹ `Subsingleton Ω[C[x,y] ⁄ adjoin C {P,Q}]` ⟹
   `Algebra.FormallyUnramified`.
5. Pass to fraction fields; `FormallyUnramified.iff_isSeparable` ⟹ `C(x,y)/C(P,Q)` separable
   algebraic.
6. `trdeg_add_eq` + `trdeg_eq_zero_iff`: `trdeg_C C(P,Q) = trdeg_C C(x,y) = 2` ⟹ `P,Q`
   algebraically independent ⟹ `adjoin C {P,Q} ≃ₐ MvPolynomial (Fin 2) C`.
7. `d := finrank C(P,Q) C(x,y)` finite: algebraic + finitely generated ⟹ `Algebra.IsIntegral.finite`.

> **FALLACY-v2 [Variable/ring map].** Step 3 must declare the algebra map
> `adjoin C {P,Q} → C[x,y]` explicitly and check images of the two generators; matching the names
> `P`,`Q` proves nothing. Step 6 must keep `trdeg` over `C` distinct from `finrank` over `C(P,Q)`.

---

### A.9 Jelonek non-properness set — **ABSENT (as expected)**

`git grep -rn -i "jelonek\|non-properness\|nonproper"` at pin → **0 hits**; master `Jelonek` → 0.
(Also: `git grep -i "jacobian conjecture\|Keller"` → 1 hit, `LinearAlgebra/QuadraticForm/
Signature.lean:30`, which is a contributor's surname.)

**Recommended minimal internal definition** — adopt K1(2) as the *definition*, exactly as the brief
suggests:

```lean
/-- The boundary (non-ZMT) primes of `B` over `A`. -/
def boundaryPrimes : Set (PrimeSpectrum B) :=
  { 𝔮 | ¬ Algebra.ZariskisMainProperty A 𝔮.asIdeal }

/-- The non-properness locus of `F`, DEFINED as the image of the boundary primes.
Agreement with Jelonek's `S_F` is an external citation, not a theorem here. -/
def nonPropernessLocus : Set (PrimeSpectrum A) :=
  PrimeSpectrum.comap (algebraMap A B) '' boundaryPrimes A B
```

and record in the module docstring: *"`nonPropernessLocus` is defined here as `q(Y ∖ U)`. That this
coincides with Jelonek's set of points at which `F` is not proper is Jelonek's theorem and is
**assumed as a citation, not proved**."* This converts the only genuinely-analytic input of K1 into
a definition + a clearly-marked external remark, and keeps the Lean development self-contained.

---

### A — summary table

| item | verdict | headline consumable / gap |
|---|---|---|
| 1 ZMT + quasi-finite | **EXISTS** (ring + scheme) | `ZariskisMainProperty.of_finiteType`; `IsOpenImmersion f.toNormalization` |
| 2 purity + depth/AB/CM/Serre/miracle-flatness | **ABSENT** (all five) | nothing to build on except `Depth/Rees.lean` and `ProjectiveDimension` |
| 3 finiteness of integral closure | **EXISTS** | `IsIntegralClosure.finite` |
| 3′ height-1 ⟹ DVR | **PARTIAL (assemblable)** | `IsDiscreteValuationRing.TFAE` item 3 + `isIntegrallyClosed_of_isLocalization` |
| 4 Σe·f = n | **EXISTS, better than needed** | `Ideal.sum_ramification_inertia_eq_finrank` (finite **flat**, no Dedekind) |
| 4′ different ideal | **EXISTS** | `differentIdeal`, `pow_sub_one_dvd_differentIdeal`, `dvd_differentIdeal_iff` |
| 4″ tameness `v(𝔇) = e−1` | **ABSENT** | floor only — must be proved (K1-L17) |
| 5 Jacobian criterion | **PARTIAL**; Ω-route **EXISTS** | `formallyUnramified_iff` is definitional |
| 6 Ω¹ | **EXISTS** | `mvPolynomialBasis`, `exact_mapBaseChange_map` |
| 6′ Ω² / 2-form valuation | **ABSENT** | `exteriorPower` exists but is never applied to `Ω`; no Fitting ideals; no Weil divisors |
| 7 scheme layer forced? | **No** | only the words "open immersion" |
| 8 alg. independence from Jac | **ABSENT (route exists)** | 7-step Ω+trdeg route above |
| 9 Jelonek | **ABSENT** | define as `q(Y∖U)`; comparison = citation |

---

## PART B — ordered lane plan

Format per lane: **ID · name** — goal; `consumables`; assumptions IN / discharged; est. Mathlib
coverage; risk; parallel-safety.

"Coverage %" = my estimate of the fraction of the lane's proof burden discharged by named existing
declarations, as opposed to bespoke Lean. These are **estimates**, not measurements.

"Box-safe" = the lane is pure Lean elaboration (no Singular, no CAS, no long char-0 Gröbner) and
therefore does **not** contend with the Max-11 campaign for the compute box. The **only** shared
resource is disk + a one-time Mathlib cache download.

> **Global setup note (applies to every lane).** Toolchain must be
> `leanprover/lean4:v4.34.0-rc1` and Mathlib rev `20bc12820422504f9e52ee6caebf8182a9015336`, i.e.
> the campaign pin. Do **not** `lake build` Mathlib from source on the campaign box — use
> `lake exe cache get` (≈15–25 GB of `.olean`s). Budget one cache fetch, once, in Stage 0.

---

### STAGE 0 — project skeleton

**K1-L00 · SKELETON** — create `keystone-graph/` beside `lean/`, single package.

- Files: `lakefile.toml` (name `KeystoneGraph`, `defaultTargets = ["KeystoneGraph"]`, one
  `[[require]] name = "mathlib"` pinned by `rev = "20bc12820422504f9e52ee6caebf8182a9015336"`),
  `lean-toolchain` = `leanprover/lean4:v4.34.0-rc1`, `KeystoneGraph.lean`,
  `KeystoneGraph/Setup.lean`, `.gitignore` containing `/.lake`.
- Palomar sandbox rules: exactly one package; **all** build artifacts under
  `keystone-graph/.lake`; no writes outside the package dir.
- Consumable produced: **`KeystoneGraph.Setup`** — a `structure` (or `variable` block) bundling
  `[Field k] [CharZero k] [IsAlgClosed k]`, `R := MvPolynomial (Fin 2) k`, `P Q : R`,
  `hJac : IsUnit (jacobianDet P Q)`, `A := Algebra.adjoin k {P, Q}`,
  `B := integralClosure A R`, `K := FractionRing A`, `L := FractionRing R`.
- Verification gate: `lake build` green; a `#print axioms` smoke target.
- Coverage: n/a. **Risk: LOW.** **Box-safe: yes** (after cache fetch).
- Est. 1 lane, hours.

---

### STAGE 1 — the fast win: Σe, the étale box, and the valuation formula (ring-theoretic)

Stage 1 lives **entirely at a fixed height-1 prime `𝔭` of `A`** — the generic point of a branch.
That is what makes it cheap: over `A_𝔭` (a DVR) **flatness is free**, so the global miracle-flatness
gap (Stage 2) never appears. This is the single most important scoping decision in the plan.

**K1-L10 · KELLER-UNRAMIFIED** — `Subsingleton Ω[R ⁄ A]`.
- `consumables`: `KaehlerDifferential.mvPolynomialBasis`, `KaehlerDifferential.range_mapBaseChange`,
  `KaehlerDifferential.exact_mapBaseChange_map`, `Algebra.formallyUnramified_iff`,
  `Matrix.isUnit_iff_isUnit_det`.
- IN: `hJac`. Discharged: nothing else.
- Coverage ≈ **85%** (bespoke: the 2×2 change-of-basis/surjectivity step, ~150–300 lines).
- **Risk: LOW-MED.** **Box-safe: yes.**

**K1-L11 · ALGIND** — `AlgebraicIndependent k ![P,Q]`; `A ≃ₐ[k] MvPolynomial (Fin 2) k`;
`FiniteDimensional K L`; `d := finrank K L`; `2 ≤ d` from noninvertibility (imported as hypothesis).
- `consumables`: K1-L10, `Algebra.FormallyUnramified.iff_isSeparable`
  (`Unramified/Field.lean:217`), `Algebra.trdeg_add_eq`, `Algebra.trdeg_eq_zero_iff`,
  `FinTrdeg`, `Algebra.IsIntegral.finite`, `MvPolynomial.algebraicIndependent_X`.
- IN: `hJac`, char 0. **Discharged: algebraic independence** (it becomes a theorem, not an axiom).
- Coverage ≈ **60%** (bespoke: `EssFiniteType` instance plumbing and the `trdeg` bookkeeping).
- **Risk: MED** — the `EssFiniteType K L` instance for `iff_isSeparable` and the localization
  instances are the likely friction. **Box-safe: yes.**

**K1-L12 · B-FINITE-NORMAL** — `Module.Finite A B`, `IsNoetherianRing B`, `IsIntegrallyClosed B`,
`IsFractionRing B L`, and `integralClosure A R = integralClosure A L` (i.e. `B ⊆ C[x,y]` is free).
- `consumables`: `IsIntegralClosure.finite`, `IsIntegralClosure.isNoetherian`,
  `IsIntegralClosure.isNoetherianRing`, `UniqueFactorizationMonoid.instIsIntegrallyClosed`,
  `MvPolynomial … UniqueFactorizationMonoid` (`Polynomial/UniqueFactorization.lean:119`),
  `IsIntegralClosure.isFractionRing_of_finite_extension`.
- IN: K1-L11 (so that `A` is a polynomial ring, hence normal Noetherian). Discharged: **K1(1)'s ring
  inclusions `A ⊆ B ⊆ C[x,y]`** and finiteness of `B` over `A`.
- Coverage ≈ **90%.** **Risk: LOW.** **Box-safe: yes.**

**K1-L13 · HEIGHT1-DVR** — for `𝔭 : Ideal A` prime of height 1: `IsDiscreteValuationRing A_𝔭`;
and `B_𝔭 := Localization (A_𝔭-algebra) B` is module-**free** of rank `d` over `A_𝔭`, Noetherian,
integrally closed, `IsDedekindDomain`.
- `consumables`: `Ideal.eq_span_singleton_of_height_eq_one` (`Ideal/Height.lean:564`) **or**
  `IsDiscreteValuationRing.TFAE` item 3 + `isIntegrallyClosed_of_isLocalization`
  (`IntegrallyClosed.lean:380`) + `IsLocalization.AtPrime.ringKrullDim_eq_height`
  (`Ideal/Height.lean:418`); `Module.free_of_finite_type_torsion_free'`
  (`LinearAlgebra/FreeModule/PID.lean:386`); `IsIntegralClosure.module_free` (:183),
  `IsIntegralClosure.rank` (:192); `IsIntegralClosure.isDedekindDomain`.
- IN: K1-L12. **Discharged: flatness of `q` over the branch generic point** — no CM, no AB.
- Coverage ≈ **70%** (bespoke: the two localization towers and their `IsScalarTower` instances).
- **Risk: MED** — instance plumbing across `A → A_𝔭 → B_𝔭 → L` is the classic time sink.
  **Box-safe: yes.**

**K1-L14 · SUM-EF** *(the fast win)* — `∑ 𝔮 ∈ 𝔭.primesOver B_𝔭, e_𝔮 · f_𝔮 = d`.
- `consumables`: **`Ideal.sum_ramification_inertia_eq_finrank`**
  (`RingTheory/RamificationInertia/Basic.lean:72`), `Algebra.QuasiFinite.finite_primesOver`
  (`QuasiFinite/Basic.lean:84`), `instance [Module.Finite R S] : QuasiFinite R S` (:107),
  K1-L13 for `Module.Flat` and `finrank = d`.
- IN: K1-L11 (`d`), K1-L12, K1-L13. Discharged: **K1(3) sum law.**
- Coverage ≈ **95%.** **Risk: LOW.** **Box-safe: yes.**
- This lane should be scheduled **first among the mathematical lanes** as the pipeline validator:
  it exercises the whole instance tower and yields a citable theorem in a single lane.

**K1-L15 · ETALE-BOX** — every `𝔮` in the ZMT (open) locus has `e_𝔮 = 1`; i.e. box `(U, e>1)` is
empty.
- `consumables`: K1-L10; `Algebra.IsUnramifiedAt` (`Unramified/Locus.lean:45`),
  `Algebra.FormallyUnramified.of_isLocalization` / `.of_restrictScalars`
  (`Unramified/Basic.lean:321,326`), `Ideal.ramificationIdx_eq_one_of_isUnramifiedAt`
  (`NumberTheory/RamificationInertia/Unramified.lean:35`).
- IN: K1-L10, K1-L12; `EssFiniteType A B`. Discharged: **box 1 of the four-box sort.**
- Coverage ≈ **90%.** **Risk: LOW.** **Box-safe: yes.**

**K1-L16 · FOURBOX-ARITHMETIC** *(conditional)* — from K1-L14 + K1-L15 + a **hypothesis**
`hram : ∃ 𝔮 ∉ U over 𝔭, 2 ≤ e_𝔮`, derive `1 ≤ a ≤ d − 2` and `3 ≤ d`, where `a = #(U-box)`.
- `consumables`: `Finset.sum_le_sum`, `Finset.card`, K1-L14, K1-L15.
- IN: **`hram` is imported as an explicit hypothesis, NOT proved** — it is the purity-dependent box
  `(Y∖U, e>1)`, which lands only in Stage 3 (K1-L31). Also imported: `1 ≤ a` (at least one point of
  the branch's fibre lies in `U`), which follows from `U` dense + `q` finite; prove it here if
  cheap, otherwise import.
- Coverage ≈ **80%** (arithmetic is easy; the bookkeeping of `a` as a `Finset.card` is the work).
- **Risk: LOW.** **Box-safe: yes.**
- > **FALLACY-v2 [Floor/attainment] and [Carrier/attainment].** `a ≤ d − 2` is derived from
  > `d = Σ e·f ≥ a·1 + 2`. This uses only `f ≥ 1`, so it does **not** require residue fields at the
  > branch generic point to be `k`. Do not silently upgrade `f = 1`; and do not present `hram` as
  > discharged when it is imported.

**K1-L17 · TAME-DIFFERENT** *(the real Stage-1 gap)* — for `B_𝔭/A_𝔭` a finite extension of Dedekind
domains in char 0 with `𝔮` over 𝔭: `v_𝔮(differentIdeal A_𝔭 B_𝔭) = e_𝔮 − 1`.
- `consumables`: `pow_sub_one_dvd_differentIdeal` (`Different.lean:742`) gives **≥** only;
  `dvd_differentIdeal_iff` (:958), `conductor_mul_differentIdeal` (:637),
  `aeval_derivative_mem_differentIdeal` (:676), `differentIdeal_eq_differentIdeal_mul_differentIdeal`
  (:571), `IsDiscreteValuationRing` API, `Ideal.ramificationIdx`.
- Bespoke proof obligation (the ≤ direction): localize at `𝔮` so that `B_𝔮` is a DVR over the DVR
  `A_𝔭`; residue extension is separable (char 0) so `B_𝔮 = A_𝔭[x]` is monogenic; the minimal
  polynomial is Eisenstein-like of degree `e·f`; `conductor_mul_differentIdeal` reduces the claim to
  `v_𝔮(f'(x)) = e − 1`, which is where `e ∈ k*` (tameness) enters.
- **A prerequisite may be missing:** the *local monogenicity* step ("a finite extension of DVRs with
  separable residue extension is monogenic") — `git grep "exists_powerBasis\|Algebra.IsMonogenic"`
  → **0 hits** at the pin. Treat this as a sub-lane **K1-L17a**.
- IN: char 0, K1-L13. Discharged: **the equality half of K1(4).**
- Coverage ≈ **35%.** **Risk: HIGH.** **Box-safe: yes.**
- Effort estimate: **K1-L17a ≈ 300–600 lines; K1-L17 ≈ 400–900 lines**; 2–4 bounded lanes total.
- > **FALLACY-v2 [Floor/attainment].** `pow_sub_one_dvd_differentIdeal` supplies a floor and
  > nothing else. Any lane report that cites it for the equality is REFUTED on sight.

**K1-L18 · VALUATION-FORMULA (recast)** — `e_𝔮 = 1 + v_𝔮(𝔇_{B_𝔭/A_𝔭})` for every boundary prime
`𝔮` with affine image.
- `consumables`: K1-L17 (equality), `Ring.ordFrac` / `Ideal.ramificationIdx`.
- IN: K1-L13, K1-L17. Discharged: **K1(4) in the ring-theoretic recasting.**
- Coverage ≈ **90%** *given* K1-L17. **Risk: LOW given L17.** **Box-safe: yes.**

**K1-L19 · TWO-FORM BRIDGE** *(optional, deferrable; restores the literal `v_j(dx∧dy)` reading)*
- Build `Ω²[R⁄k] := ⋀²(Ω[R⁄k])` via `exteriorPower`; prove `dP ∧ dQ = Jac(P,Q) • (dx ∧ dy)`
  (`ExteriorPower.Basis`, `mvPolynomialBasis`). Then relate `v_𝔮(dx∧dy)` to `v_𝔮(𝔇)` — this second
  half needs a ramification-divisor statement that Mathlib does not have.
- `consumables`: `Mathlib/LinearAlgebra/ExteriorPower/{Basic,Basis}.lean`,
  `KaehlerDifferential.mvPolynomialBasis`.
- Coverage ≈ **40%** for the first half, ≈ **0%** for the second.
- **Risk: HIGH.** Estimate 1 lane for `dP∧dQ = Jac·dx∧dy`; the divisor half is a Stage-3-class
  project. **Recommend: do the first half only, and record the second as an external remark.**

**Stage 1 verdict:** K1-L10, L12, L13, L14, L15 form a **clean, high-coverage, low-risk chain
delivering the sum law + the étale box** — genuinely a fast win, plausibly 5–8 lanes. K1-L16 lands
the four-box arithmetic *conditionally*. K1-L17 is the one hard lane, and it is hard for a specific,
nameable reason (tameness is absent), not for a diffuse one.

**Hypotheses entering Stage 1 as assumptions vs discharged:**

| hypothesis | status after Stage 1 |
|---|---|
| algebraic independence of `P,Q` | **DISCHARGED** (K1-L11) |
| `Module.Finite A B` | **DISCHARGED** (K1-L12) |
| normality of `B` | **DISCHARGED** (K1-L12, from `IsIntegralClosure`) |
| flatness of `B` over the base | **DISCHARGED at height-1 primes only** (K1-L13); **ASSUMED/absent globally** |
| `d ≥ 2` (noninvertibility) | **ASSUMED** (it is the K1 hypothesis) |
| `∃ 𝔮 ∈ Y∖U over the branch with e ≥ 2` | **ASSUMED** — purity-dependent, Stage 3 |
| Jelonek `A_F = q(Y∖U)` | **DEFINITION** (A.9), comparison is a citation |
| char 0 / `k` alg. closed | **ASSUMED** (standing) |

---

### STAGE 2 — finiteness/flatness of `q`, and the codim-1 structure of `Y ∖ U`

**K1-L20 · Q-FINITE** — `q : Spec B → Spec A` is finite: `Module.Finite A B` (already K1-L12) +
`Algebra.QuasiFinite A B` + `Algebra.IsIntegral A B`.
- `consumables`: K1-L12, `instance [Module.Finite R S] : QuasiFinite R S`,
  `IsIntegralClosure.isIntegral_algebra`.
- Coverage ≈ **95%.** **Risk: LOW.** **Box-safe: yes.**

**K1-L21 · Q-FLAT-GLOBAL** — `Module.Flat A B` over the **2-dimensional regular** base.
- This is the miracle-flatness gap. **Nothing in Mathlib applies.** Three options:
  - **(a) Full library route:** `Module.depth` (on `Depth/Rees.lean`) → Auslander–Buchsbaum →
    Cohen–Macaulay → miracle flatness. Estimate **3000–6000 lines, 8–15 bounded lanes**.
  - **(b) dim-2 shortcut:** `B` normal ⟹ `S₂`; finite `S₂` module over a 2-dim regular local ring
    ⟹ `depth = 2` ⟹ (AB) `pd = 0` ⟹ free. **Still needs depth and AB**; it only avoids CM *rings*
    and general miracle flatness. Estimate **1500–3000 lines, 4–8 lanes**.
  - **(c) AVOID (recommended for the critical path):** never state global flatness. All of K1(3)
    and K1(4) as charged live at generic points of branches, where K1-L13 gives freeness for free.
    Global flatness is needed only if one additionally wants `Σ_{y ∈ q⁻¹(p)} e_y = d` at **closed**
    points `p ∈ C²` — which the K1 statement's four-box clause does not use.
- **Recommendation: (c) on the critical path; (b) scheduled as an independent long lane** that can
  run for months without blocking anything.
- Coverage ≈ **5%.** **Risk: HIGH.** **Box-safe: yes** (pure Lean, but long).
- > **FALLACY-v2 [Target/arrival index].** Keep "`Σ e = d` at a **height-1** `𝔭`" (Stage 1, proved)
  > strictly distinct from "`Σ e = d` at a **closed** point `p`" (needs K1-L21). They are different
  > theorems with different hypotheses; conflating them is the predictable failure mode here.

**K1-L22 · U-OPEN** — the ZMT locus `U ⊆ Spec B` is open, and `Y ∖ U` is closed.
- `consumables`: `Algebra.QuasiFiniteAt.exists_fg_and_exists_notMem_and_awayMap_bijective`
  (`ZariskisMainTheorem.lean:701`), `Algebra.quasiFiniteAt_iff_isOpen_singleton_fiber` (:752);
  or at the scheme layer `Scheme.Hom.isOpen_quasiFiniteAt` / `Scheme.Hom.quasiFiniteLocus`.
- Coverage ≈ **80%.** **Risk: LOW-MED.** **Box-safe: yes.**

**K1-L23 · YU-NONEMPTY** — `Y ∖ U ≠ ∅` when `d ≥ 2`.
- Mathematically: if `U = Y` then `j` is an isomorphism, so `F` is finite, so (`C²` normal, `F`
  finite birational-onto-image + `d ≥ 2`) contradiction. Needs a small argument.
- `consumables`: `IsFinite.of_isProper_of_locallyQuasiFinite` (scheme layer) or
  `ZariskisMainProperty.of_isIntegral`; K1-L11 for `d ≥ 2`.
- Coverage ≈ **50%.** **Risk: MED.** **Box-safe: yes.**

**K1-L24 · YU-CODIM-1 (purity-gated)** — every `𝔮 ∈ Y ∖ U` has `Ideal.height 𝔮 = 1`.
- **BLOCKED on purity.** No Mathlib path. Deferred to Stage 3; until then, **import as a
  hypothesis**.
- Coverage ≈ **0%.** **Risk: HIGH.** **Box-safe: yes** (once unblocked).

**Stage 2 verdict:** L20/L22/L23 are ordinary lanes. L21 and L24 are the two library projects, and
**both are avoidable on the critical path** if Stage 1's height-1 scoping is kept and purity is
imported as an explicit hypothesis.

---

### STAGE 3 — the two pillars

**K1-L30 · ZMT PILLAR — Mathlib-shaped, do it.**
- Path: instantiate `f := Spec.map (algebraMap A R)`; supply `[LocallyOfFiniteType f]`
  (`MvPolynomial` is finite type over `A` by K1-L11), `[IsSeparated f]` and `[QuasiCompact f]`
  (affine), `[LocallyQuasiFinite f]` (fibres are finite because `P,Q` are algebraically independent
  — K1-L11 + `Algebra.QuasiFinite`). Then `instance … : IsOpenImmersion f.toNormalization`
  (`AlgebraicGeometry/ZariskisMainTheorem.lean:359`) **fires by `inferInstance`**.
- Remaining work is the identification `f.normalization ≅ Spec B`: `normalizationObjIso`
  (`Normalization.lean:219`), `instance [IsAffineHom f] : IsAffineHom f.toNormalization` (:307),
  `fromNormalization_app` (:258), plus K1-L12's `integralClosure A R = integralClosure A L`.
- `consumables`: the whole of `AlgebraicGeometry/{Normalization, ZariskisMainTheorem}.lean`.
- Coverage ≈ **80%.** **Risk: MED** (categorical plumbing, not mathematics).
- Effort estimate: **300–600 lines, 1–3 lanes.**
- Discharged: **K1(1) in full, including the literal "open immersion".**
- **Box-safe: yes**, but importing `Mathlib.AlgebraicGeometry` roughly doubles elaboration time —
  keep this lane in a separate module so Stage 1/2 files stay light.

**K1-L31 · PURITY PILLAR — declare it a long-lane library project.**
- Nothing exists (A.2). The dim-2 shortcut the brief asks about
  (Auslander–Buchsbaum + reflexive modules, van der Waerden style) is **not** available: `Module.
  IsReflexive` in Mathlib is the bidual class, not the comm-alg reflexive hull, and AB is absent.
- Sub-projects, in dependency order:
  1. **DEPTH** — define `Module.depth I M` on top of `ModuleCat.exists_isRegular_tfae`
     (`Depth/Rees.lean`); basic API (depth ≤ dim, depth and short exact sequences, depth under
     localization/completion). Est. **600–1200 lines.**
  2. **AB** — Auslander–Buchsbaum `pd + depth = depth R` over Noetherian local, using
     `RingTheory/Regular/ProjectiveDimension.lean` and minimal free resolutions. Est.
     **800–1600 lines.**
  3. **CM (light)** — only what purity needs: finite modules of maximal depth over a regular local
     ring are free (miracle flatness in the special case). Est. **400–800 lines.**
  4. **S₂/normality bridge** — normal Noetherian ⟹ `S₂` (this is half of Serre's criterion and is
     itself absent). Est. **400–900 lines.**
  5. **PURITY (dim 2 only)** — Zariski–Nagata for a finite extension of a 2-dimensional regular
     local ring. Est. **600–1200 lines.**
- **Total estimate: ≈ 2800–5700 lines; 8–15 bounded lanes; at the campaign's cadence, 3–6 months of
  lane time.** Full generality (all dimensions, general Zariski–Nagata) is materially larger and is
  **not** recommended.
- **Recommendation: do NOT put this on the K1 critical path.** Instead:
  - state K1(2) and the `(Y∖U, e>1)` box as **explicit hypotheses** of the K1 theorem;
  - ship K1 as a **conditional theorem** with those two hypotheses named and documented;
  - open K1-L31 as an independent, indefinitely-running track. It is also of general Mathlib
    interest, so it is a good candidate for upstreaming and for non-campaign help.
- Coverage ≈ **5%** (only `KrullsHeightTheorem` and `ProjectiveDimension` are reusable).
- **Risk: HIGH.** **Box-safe: yes.**

---

### B — schedule, coverage and parallelism summary

| stage | lanes | est. Mathlib coverage | risk | on critical path? | contends with Max-11 box? |
|---|---|---|---|---|---|
| 0 skeleton | K1-L00 | n/a | LOW | yes | no (one cache fetch) |
| 1 sum + étale box | L10, L12, L13, **L14**, L15 | **≈ 85%** | LOW-MED | yes | no |
| 1 four-box arithmetic | L16 (conditional) | ≈ 80% | LOW | yes | no |
| 1 valuation formula | **L17** (+L17a), L18 | **≈ 40%** | **HIGH** | yes | no |
| 1 alg. independence | L11 | ≈ 60% | MED | yes | no |
| 1 two-form (optional) | L19 | ≈ 25% | HIGH | **no** | no |
| 2 finite/open/nonempty | L20, L22, L23 | ≈ 75% | LOW-MED | yes | no |
| 2 global flatness | L21 | ≈ 5% | HIGH | **no** (avoid via height-1 scoping) | no |
| 2 codim-1 of Y∖U | L24 | 0% | HIGH | **no** (import as hypothesis) | no |
| 3 ZMT pillar | L30 | ≈ 80% | MED | yes | no |
| 3 purity pillar | L31 (8–15 sub-lanes) | ≈ 5% | HIGH | **no** (conditional theorem) | no |

**Recommended execution order:** L00 → **L14-dry-run scaffolding** → L10 → L11 → L12 → L13 → **L14**
→ L15 → L16 → L20 → L22 → L23 → L30 → L17a → L17 → L18 → (L19, L21, L24, L31 as independent
tracks).

**Everything in this plan is box-safe.** No lane needs Singular, Gröbner bases, or char-0 CAS work;
the resource profile is CPU-light, memory-moderate Lean elaboration plus a one-time ~15–25 GB
Mathlib cache. The Max-11 campaign and the K1 formalization can run fully in parallel.

---

## Open items / honest gaps in this survey

1. **`~/code/math/jc2/jc2-lean/` was unreadable** (EPERM, sandbox). Source (i) was read from the
   byte-identical pinned commit in another local clone's object store. Anything specific to that
   submodule — in particular the **max11 lane style file and the box-verify contract text** — I
   could **not** read. `grep -rn -i "box.verify\|max11" ` over the accessible parts of the repo
   returned nothing. **The lane format above is my reconstruction from the brief, and its conformance
   to the campaign's box-verify contract is UNVERIFIED.** First action for whoever picks this up:
   re-run the survey's Part B formatting against the real contract.
2. **Rate-limited master probes.** `Ideal.depth`, `isRegularLocalRing_of`, `ExcellentRing`,
   `normalization_isIntegrallyClosed` and `IsIntegrallyClosed of_serre` hit GitHub search's 403
   rate limit and are **UNVERIFIED on master**. All were verified ABSENT at the pin, and the pin→
   master module diff adds no file that could host them; but a declaration added inside an existing
   file would not be caught. Low residual risk.
3. **Coverage percentages are estimates**, not measurements. They should be re-scored after K1-L14
   lands, which is the first lane that exercises the real instance tower.
4. **`round1033-sheet-gate-opus5-20260831.md` was not consulted.** The brief points at it for the
   intended mathematical content; I worked from the K1 statement in the brief itself, since the
   deliverable is a survey and a plan rather than a proof. Anyone executing K1-L16/L17 should read
   that file first, because the precise form of the `(Y∖U, e>1)` box and of `v_j(dx∧dy)` there may
   narrow or widen K1-L18's recasting.
5. **K1-L17a (local monogenicity of a DVR extension with separable residue extension) may or may not
   be reducible to existing API** — I found no `exists_powerBasis` / `Algebra.IsMonogenic` at the
   pin, but I did not exhaustively search for an equivalent statement phrased via `PowerBasis` or
   `Algebra.adjoin`. Labelled **PARTIAL/UNVERIFIED**; treat the 300–600-line estimate as soft.
