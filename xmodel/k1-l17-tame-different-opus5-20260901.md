# K1-L17a + K1-L17 — local monogenicity and the tame different equality

**Lane:** k1-l17-tame-different · **Model:** Opus 5 · **Date:** 2026-09-01
**Verdict:** **BOTH LANDED GREEN.** `BUILD_EXIT=0`, no `sorry`, axioms = `{propext,
Classical.choice, Quot.sound}` on all 11 declarations.
**Scope correction (read §5 before promoting):** the equality is proved under
**residue characteristic zero**, not under "characteristic zero" as the brief phrased it
(that phrasing is false for general Dedekind domains), and not under the *sharp* tameness
hypothesis `p ∤ e`. The sharp version is left typed `OPEN` with a named obstruction.

---

## 1. Deliverables and hashes

Written to `xmodel/k1-l17-files/` (see §6: the `jc2-lean` submodule working tree is
unreadable and unwritable from this session, so the files could not be placed under
`jc2-lean/keystone-graph/KeystoneGraph/`).

| file | lines | SHA-256 |
|---|---:|---|
| `KeystoneGraph/Monogenic.lean` | 265 | `91588126a50b810bc12fd1b81bb8ba07911db74f954f8a3c9c781a4dcc5efdc2` |
| `KeystoneGraph/TameDifferent.lean` | 139 | `6c1fddc89c91da05b09ffc239d63e03107fef95081862546a510fd9b499eb68b` |
| `KeystoneGraph.lean` (root, merged imports) | 3 | `2eecb5c283437c7416b420096ab8c2b1389e269ec9eeaaf8a2476785b5f82e4b` |

Reference skeleton used: submodule `jc2-lean` HEAD
`63634b9dfa0184baaa0893f268f30000d9960838` ("Open the Keystone 1 formalization project",
2026-09-01 14:27:04 -0700); Mathlib pinned at `20bc12820422504f9e52ee6caebf8182a9015336`,
toolchain `leanprover/lean4:v4.34.0-rc1`.
`Setup.lean` SHA-256 as committed: `02bc41ec57a0442624fd90e13e0508bc05bf84c83a9434c13e694afe7c19ff02`.

`grep -n "sorry\|axiom "` over both new files → **none**.

---

## 2. Statements proved (verbatim source)

### 2.1 `KeystoneGraph/Monogenic.lean` — K1-L17a

Ambient section variables:

```lean
variable {A B : Type*} [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
  [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
  [Algebra A B] [Module.Finite A B] [FaithfulSMul A B]
```

```lean
theorem span_eq_maximalIdeal_of_mem_of_notMem_sq {y : R}
    (h1 : y ∈ maximalIdeal R) (h2 : y ∉ maximalIdeal R ^ 2) :
    Ideal.span {y} = maximalIdeal R
```
(section variables `{R : Type*} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]`)

```lean
theorem residue_aeval (x : B) (q : A[X]) :
    residue B (aeval x q) = aeval (residue B x) (q.map (residue A))
```

```lean
theorem exists_aeval_sub_mem {x : B}
    (hx : Algebra.adjoin (ResidueField A) {residue B x} = ⊤) (u : B) :
    ∃ q : A[X], u - aeval x q ∈ maximalIdeal B
```

```lean
theorem adjoin_eq_top_of_residue_gen_of_span_eq {x : B}
    (hres : Algebra.adjoin (ResidueField A) {residue B x} = ⊤)
    {g : A[X]} (hg : Ideal.span {aeval x g} = maximalIdeal B) :
    Algebra.adjoin A {x} = ⊤
```

```lean
theorem exists_residue_gen_and_span_eq
    [Algebra.IsSeparable (ResidueField A) (ResidueField B)] :
    ∃ (x : B) (g : A[X]), Algebra.adjoin (ResidueField A) {residue B x} = ⊤ ∧
      g.Monic ∧ Ideal.span {aeval x g} = maximalIdeal B
```

```lean
theorem exists_adjoin_singleton_eq_top
    [Algebra.IsSeparable (ResidueField A) (ResidueField B)] :
    ∃ x : B, Algebra.adjoin A {x} = ⊤
```

```lean
theorem nonempty_powerBasis
    [Algebra.IsSeparable (ResidueField A) (ResidueField B)] :
    Nonempty (PowerBasis A B)
```

### 2.2 `KeystoneGraph/TameDifferent.lean` — K1-L17

Ambient section variables (`attribute [local instance] FractionRing.liftAlgebra
FractionRing.isScalarTower_liftAlgebra` is in force, as in Mathlib's `Different.lean`):

```lean
variable (A : Type*) {B : Type*} [CommRing A] [CommRing B]
  [IsDedekindDomain A] [IsDedekindDomain B] [Algebra A B]
  [Module.Finite A B] [Module.IsTorsionFree A B]
  [Algebra.IsSeparable (FractionRing A) (FractionRing B)]
```

```lean
theorem not_pow_dvd_differentIdeal_of_coprime
    {p : Ideal A} [p.IsMaximal] [CharZero (A ⧸ p)]
    {P Q : Ideal B} {e : ℕ} (he : e ≠ 0) (hPtop : P ≠ ⊤)
    (hQ : Ideal.map (algebraMap A B) p = P ^ e * Q) (hcop : IsCoprime P Q) :
    ¬ P ^ e ∣ differentIdeal A B
```

```lean
theorem not_pow_dvd_differentIdeal
    {p : Ideal A} [p.IsMaximal] [CharZero (A ⧸ p)]
    {P : Ideal B} [P.IsMaximal] {e : ℕ} (he : e ≠ 0)
    (hdvd : P ^ e ∣ Ideal.map (algebraMap A B) p)
    (hnot : ¬ P ^ (e + 1) ∣ Ideal.map (algebraMap A B) p) :
    ¬ P ^ e ∣ differentIdeal A B
```

```lean
theorem multiplicity_differentIdeal_eq
    {p : Ideal A} [p.IsMaximal] [CharZero (A ⧸ p)] (hp : p ≠ ⊥)
    {P : Ideal B} [P.IsMaximal] {e : ℕ} (he : e ≠ 0)
    (hdvd : P ^ e ∣ Ideal.map (algebraMap A B) p)
    (hnot : ¬ P ^ (e + 1) ∣ Ideal.map (algebraMap A B) p) :
    multiplicity P (differentIdeal A B) = e - 1
```

```lean
theorem multiplicity_differentIdeal_eq_ramificationIdx_sub_one
    {p : Ideal A} [p.IsMaximal] [CharZero (A ⧸ p)] (hp : p ≠ ⊥)
    {P : Ideal B} [P.IsMaximal] [P.LiesOver p] :
    multiplicity P (differentIdeal A B) = P.ramificationIdx A - 1
```

The last one is the **K1-L18 consumable**: explicit `A`, implicit `B`, `IsDedekindDomain`
hypotheses only, no Keystone setup, and `e` is Mathlib's `Ideal.ramificationIdx P A`
(the `Module.length` definition, `RingTheory/RamificationInertia/Ramification.lean:52`).
`multiplicity P I = n` for `I ≠ 0` in a Dedekind domain is exactly `v_P(I) = n`; the proof
goes through `multiplicity_eq_of_dvd_of_not_dvd`, i.e. it delivers both
`P^(e-1) ∣ 𝔇` and `¬ P^e ∣ 𝔇`.

---

## 3. Build tail and axioms

Final run (see §6 for why the destination directory differs from `scripts/box_build.sh`;
the remote block below is byte-identical to the script's):

```
✔ [8747/8749] Built KeystoneGraph.Setup (3.1s)
✔ [8748/8749] Built KeystoneGraph (2.8s)
Build completed successfully (8749 jobs).
BUILD_EXIT=0
```

Axiom probe (`lake env lean` on a file importing `KeystoneGraph`):

```
'KeystoneGraph.span_eq_maximalIdeal_of_mem_of_notMem_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.residue_aeval' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.exists_aeval_sub_mem' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.adjoin_eq_top_of_residue_gen_of_span_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.exists_residue_gen_and_span_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.exists_adjoin_singleton_eq_top' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.nonempty_powerBasis' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.not_pow_dvd_differentIdeal_of_coprime' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.not_pow_dvd_differentIdeal' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.multiplicity_differentIdeal_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'KeystoneGraph.multiplicity_differentIdeal_eq_ramificationIdx_sub_one' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
```

No new axioms; no `sorryAx`.

**Compatibility with concurrent lanes:** the same two modules also build green on top of the
box's *current* `Setup.lean` (updated by another lane, 1832 bytes) together with
`KellerUnramified.lean` — `BUILD_EXIT=0`, 8750 jobs. They were excluded from the final
quoted run only to keep it reproducible from the committed skeleton. See §6 for
`IntegralClosureFinite.lean`.

---

## 4. Proof routes (and where they diverge from the plan)

### 4.1 K1-L17a — as planned

The survey's re-check was redone at the pin: `exists_powerBasis`, `IsMonogenic` → **0 hits**;
`monogenic` → only `Mathlib/RingTheory/LocalRing/Etale.lean`, whose
`IsLocalRing.exists_adjoin_eq_top` assumes `Algebra.FormallyUnramified R S`, i.e.
`m_A B = m_B`. That is exactly the hypothesis that fails when `e > 1`, so it is **not**
reusable and the theorem was proved from scratch.

Proof as the plan describes: take a primitive element `β₀` of `l/k`
(`Field.exists_primitive_element`), lift it to `β ∈ B`, lift `minpoly k β₀` to a monic
`g ∈ A[X]` (`Polynomial.lifts_and_degree_eq_and_monic`), and replace `β` by `β + ϖ` when
`g(β) ∈ m_B²` — legitimate because separability makes `g'(β)` a unit, so
`Polynomial.binomExpansion` moves `g(β + ϖ)` out of `m_B²`. That yields `x` with
`v_B(g(x)) = 1`. Nakayama (`Submodule.le_of_le_smul_of_le_jacobson_bot`) then gives
`A[x] = B`, via a downward induction on the `m_B`-adic filtration: writing
`b = g(x)^n · u` and replacing `u` by a polynomial in `x` congruent to it mod `m_B`
pushes the remainder into `m_B^(n+1)`, and `m_B^e ⊆ m_A B` starts the induction.

`nonempty_powerBasis` is `IsAdjoinRootMonic.mkOfAdjoinEqTop'` + `.powerBasis`, using
`Module.free_of_finite_type_torsion_free'`.

### 4.2 K1-L17 — **different route from the plan**

The plan routed K1-L17 through K1-L17a: `conductor_mul_differentIdeal` (`Different.lean:637`)
plus `aeval_derivative_mem_differentIdeal` (:676), reducing to `v_𝔮(f'(x)) = e − 1`.
**That is not the route taken.** A shorter one exists using a Mathlib lemma the plan's
consumables list does not mention:

```lean
-- Mathlib/RingTheory/DedekindDomain/Different.lean:752
theorem not_dvd_differentIdeal_of_intTrace_not_mem
    [Algebra.IsSeparable (FractionRing A) (FractionRing B)]
    {p : Ideal A} (P Q : Ideal B) (hP : P * Q = Ideal.map (algebraMap A B) p)
    (x : B) (hxQ : x ∈ Q) (hx : Algebra.intTrace A B x ∉ p) :
    ¬ P ∣ differentIdeal A B
```

This is the trace criterion `𝔇^{-1} ⊆ 𝔮^{1-e} ⟺ Tr_{B/A}(B) ⊄ 𝔭` in ideal-theoretic form,
and it applies with `P := 𝔮^e` directly at the Dedekind level — **no localisation to the
DVR case is needed**, which is the expensive step the plan anticipated. The proof then is:

1. Factor `𝔭B = 𝔮^e · Q` with `IsCoprime 𝔮^e Q` (from `¬ 𝔮^{e+1} ∣ 𝔭B`, or from
   `Ideal.eq_prime_pow_mul_coprime`).
2. CRT: `B/𝔭B ≃ₐ[A/𝔭] (B/𝔮^e) × (B/Q)`; pick `y` mapping to `(1, 0)`.
3. `Algebra.trace_quotient_eq_of_isDedekindDomain` + `Algebra.trace_prod_apply` +
   `Algebra.trace_algebraMap` give `intTrace A B y ≡ dim_{A/𝔭}(B/𝔮^e)` mod `𝔭`.
4. Residue characteristic zero makes that nonzero, since `dim_{A/𝔭}(B/𝔮^e) ≥ 1`.

**Consequence for the plan:** K1-L17's 400–900-line / 35 %-coverage / HIGH-risk estimate was
pessimistic — the landed module is 139 lines. K1-L17a, delivered as instructed, turned out
**not to be a dependency** of K1-L17 as landed; it stands on its own (and is what a future
sharp-tameness or explicit-`f'(x)` route would consume).

### 4.3 FALLACY-v2 [Floor/attainment] — guard satisfied

`pow_sub_one_dvd_differentIdeal` is used **only** for the `≥` half inside
`multiplicity_differentIdeal_eq*`, where it is a genuine floor
(`P^(e-1) ∣ 𝔇`). The `≤` half `¬ P^e ∣ 𝔇` is a separate theorem with its own proof
(§4.2) and is nowhere derived from the floor. The equality is assembled by
`multiplicity_eq_of_dvd_of_not_dvd`, which consumes both halves.

---

## 5. Scope corrections — read before promoting

### 5.1 "Characteristic zero" in the brief is the wrong hypothesis

The brief says: *"for a finite extension of Dedekind domains `B/A` in characteristic zero
(so residue extensions of the relevant primes are separable and ramification is tame)"*.
**The parenthetical is false.** `A = ℤ`, `B = ℤ[i]` is a finite extension of Dedekind
domains of characteristic zero; at `p = (2)`, `P = (1+i)` one has `e = 2` but
`v_P(𝔇) = 2 ≠ e − 1 = 1`. Ring characteristic zero does not bound residue characteristic.

What *is* true, and what the modules assume, is `CharZero (A ⧸ p)` — **residue**
characteristic zero. In the K1 geometric setting `A`, `B` are algebras over a
characteristic-zero field `k` and every residue field of a maximal ideal contains `k`, so
this holds automatically; discharging it in K1-L18 is a one-liner from the `k`-algebra
structure, but it **must be discharged**, not assumed to follow from `CharZero A`.

### 5.2 The *sharp* tame hypothesis is `OPEN`

Classical tameness is: residue extension `l/k` separable **and** `p ∤ e`. That is strictly
weaker than `CharZero (A ⧸ p)`. It is not what is proved here.

The gap is localised and nameable. The proof (§4.2 step 3) evaluates the trace at `y ≡ 1`,
which gives `Tr = dim_k(B/𝔮^e) = e · f`. The sharp statement needs the graded computation
`Tr_{(B/𝔮^e)/k}(x) = e · Tr_{l/k}(x mod 𝔮)`, i.e. additivity of `LinearMap.trace` along
the `𝔮`-adic filtration of `B/𝔮^e`. **At the pin Mathlib has no sub-plus-quotient
additivity lemma for `LinearMap.trace`** (`git grep "trace_restrict\|trace_quotient_add\|
trace_eq_trace_add"` over `Mathlib/LinearAlgebra/**` and `Mathlib/RingTheory/**` → 0 hits),
so that lemma would have to be built first. Note also that `e · f` and `e` differ exactly
when `char k ∣ f`, so the two hypotheses genuinely differ.

Typed status: **`OPEN` — sharp tame hypothesis (`p ∤ e`, `l/k` separable) not proved.**
Successor lane, if wanted: `LinearMap.trace` additivity on a short exact sequence, then the
filtration induction. Not on the K1 critical path, since residue characteristic zero holds
in the geometric setting.

### 5.3 Hypotheses that are *not* needed

`not_pow_dvd_differentIdeal_of_coprime` needs neither `P.IsPrime` nor `P.IsMaximal`, only
`P ≠ ⊤` plus the coprime factorisation. This is a genuine (small) generalisation, not an
oversight.

### 5.4 Non-vacuity

Not machine-checked. Mathematically the hypothesis set is plainly satisfiable — e.g.
`A = ℚ[T]`, `B` the integral closure of `A` in a finite separable extension of `ℚ(T)`,
`p = (T)`, `A ⧸ p ≅ ℚ`. No Lean instantiation was built; treat "the theorem is non-vacuous"
as an unchecked (but routine) claim.

---

## 6. Execution gaps and disclosures

1. **`jc2-lean/` is unreadable and unwritable from this session (EPERM).** `ls`, `stat`,
   `find` and a write probe all fail with `Operation not permitted`, including with the
   sandbox explicitly disabled — the same obstruction the survey lane reported. The
   submodule's *git directory* (`.git/modules/jc2-lean`) **is** readable, so the skeleton was
   reconstructed byte-exactly from `git show HEAD:keystone-graph/…` into a scratch tree and
   all work was done there. **The two new modules therefore are not in the submodule
   working tree**; they are at `xmodel/k1-l17-files/KeystoneGraph/` and must be copied to
   `jc2-lean/keystone-graph/KeystoneGraph/`, with `KeystoneGraph.lean` gaining
   `import KeystoneGraph.Monogenic` and `import KeystoneGraph.TameDifferent`.
   No git branch or commit was created in the submodule.

2. **`scripts/box_build.sh` was not invoked verbatim.** Two reasons, both forced:
   (i) the script computes its source directory from its own location inside the
   unreachable working tree; (ii) its destination `/home/ubuntu/keystone-graph/` is a
   `rsync --delete` target that **another lane is actively using** — at the time of the final
   run it held `KellerUnramified.lean` (21:44 UTC-7) and `IntegralClosureFinite.lean`
   (22:00 UTC-7), neither of which is committed yet. Running the script would have deleted
   them. What was run instead is the script's **remote block byte-for-byte**
   (`lake exe cache get … ; lake build 2>&1 | tail -5 ; echo BUILD_EXIT=$rc`) over
   `rsync -a --delete --exclude='.lake'`, against an isolated box directory
   `/home/ubuntu/kg-k1l17` whose `.lake/packages` is a hardlink copy of the shared one, so
   the same pinned Mathlib build was used. Nothing in `/home/ubuntu/keystone-graph/` was
   modified by this lane.

3. **Another lane's module is currently red.** `IntegralClosureFinite.lean` on the box fails
   to build and several of its declarations report `sorryAx`
   (`isIntegrallyClosed_integralClosure`, `isFractionRing_integralClosure`,
   `keller_algebraMap_mem_integralClosure`, `keller_equivIntegralClosure`,
   `keller_isNoetherianRing`, `keller_isIntegrallyClosed`, `keller_isFractionRing`). That is
   their work in progress, reported here only because it is why a whole-project green build
   could not be quoted. It is not caused by, and does not affect, this lane's modules.

4. **`round1033-sheet-gate-opus5-20260831.md` was not consulted** (the survey flagged it as
   the place where the precise `v_j(dx∧dy)` reading lives). The statement shipped here is
   the ring-theoretic `v_P(𝔇) = e − 1`; whoever runs K1-L18 should check it against that
   file, since the recasting there may want a different indexing of `e`.

---

## 7. Successors

- **K1-L18** can start now: consume
  `multiplicity_differentIdeal_eq_ramificationIdx_sub_one`, discharging
  `CharZero (A ⧸ p)` from the `k`-algebra structure (§5.1) and `p ≠ ⊥` from
  `p` maximal in a Dedekind domain of dimension one.
- **Sharp tameness** (§5.2): needs `LinearMap.trace` additivity on short exact sequences.
  Optional.
- **K1-L17a has no consumer yet.** It is a complete, standalone result; if the sharp route
  or an explicit `f'(x)` computation is ever wanted, it is the entry point.
