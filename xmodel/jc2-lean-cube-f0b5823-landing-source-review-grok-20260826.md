# Hostile source-completeness review — cube landing `f0b5823`

| Field | Value |
|---|---|
| Claim under review | Nested Lean commit `f0b5823c2d008807fa6524401faf2e1413d7a5f8`, file `gcd3-69-cube/Solution.lean`: the new headline `GCD369CubeTrajectoryLandingEmpty` glues already-certified cube-core branch exclusions into emptiness of a finite landing type |
| Overall verdict | **FORMAL_GLUE_ONLY** |
| Strongest theorem licensed by the pinned source | `GCD369CubeTrajectoryLandingEmpty : GCD369CubeTrajectoryLanding K → False` over `[Field K] [CharZero K] [IsAlgClosed K]`.  This is emptiness of an explicitly enumerated coproduct of ten already-empty packages.  It is not a cube-core, `(6,9)`, maximum-eleven, or JC2 theorem |
| Smallest missing source-to-landing declaration | `GCD369CubeSourceToTrajectoryLanding` below.  Absent from every Lean, markdown, yaml, and json file of the pinned nested commit |
| Reviewer | Grok 4.6 (xAI).  Source-logic and theorem-scope audit only.  Lean was not executed |
| Nested repository | `/Users/dc/code/math/jc2/jc2-lean` |
| Pinned nested commit | `f0b5823c2d008807fa6524401faf2e1413d7a5f8` (`Assemble the finite cube trajectory landing theorem`) |
| Live nested `HEAD` at review (not used as source) | `c03b1662b0d518fca24c734a95da47a7679dc6ea` |
| Pinned file | `gcd3-69-cube/Solution.lean` (3092 lines at the pinned commit) |
| Required SHA-256 | `6407444078ad5ea0ce93ec55440b2629d10676abcff6614887ef47c97e8e0de2` |
| Recomputed SHA-256 (`git show` \| `shasum -a 256` and `openssl dgst -sha256`) | `6407444078ad5ea0ce93ec55440b2629d10676abcff6614887ef47c97e8e0de2` (match) |

Bytes were read with `git show f0b5823c2d008807fa6524401faf2e1413d7a5f8:gcd3-69-cube/Solution.lean`.  Working-tree bytes were not substituted.  The cube package at this commit contains only `Solution.lean`, `lakefile.toml`, `lake-manifest.json`, and `lean-toolchain`: no `Challenge.lean`, no `formalization.yaml`, no `sources/`.  Compilation was not treated as coverage.  Informal cube-trajectory reports outside the nested commit were used only to name the missing source-to-landing obligation, not as Lean evidence.

The docstring on `GCD369CubeTrajectoryLandingEmpty` calls it “the source-completeness gluing theorem for the already certified branches.”  The type is the opposite of source completeness: it assumes an inhabitant of the finite list and derives `False`.  That is formal glue.  Coverage would be a map *into* the list.

---

## 1. Headline type and constructor inventory

### 1.1 Exact headline

```lean
inductive GCD369CubeTrajectoryLanding (K : Type*) [Field K] : Prop

theorem GCD369CubeTrajectoryLandingEmpty {K : Type*}
    [Field K] [CharZero K] [IsAlgClosed K]
    (L : GCD369CubeTrajectoryLanding K) : False
```

Proof body: `cases L` on the ten constructors, then one already-proved branch exclusion per constructor.  No new algebraic identity is proved.  `IsAlgClosed` is inherited from the mixed-cusp and Davenport–Stothers branches; several other constructors do not use it.

This is not a substantive gluing of source trajectories.  It is the tautology that a finite coproduct of empty packages is empty: if each constructor’s payload already implies `False`, then the inductive does too.  Several payloads are already contradictory *by definition*, independently of the cube-core story.

### 1.2 Constructors of `GCD369CubeTrajectoryLanding`, consumed theorems, and independence

| Constructor | Payload (compressed) | Consumed theorem | Independent of source? |
|---|---|---|---|
| `constantPole` | `D : GCD369CubeConstantPoleDegreeLanding` | `GCD369CubeConstantPoleDegreeLandingEmpty D` | Yes.  Inner constructors require a non-integral rational to equal a `ℕ` |
| `earlyBoundary` | `D : GCD369CubeEarlyBoundaryData K` | `GCD369CubeEarlyBoundaryDataEmpty D` | No.  Structure packages Hahn-series order inequalities; emptiness uses the early-weight dichotomy |
| `rhoFour` | `Xn Yn Zn u v` and four displayed quadrics, last with constant `-52488` | `GCD369CubeRhoFourFirstLoadImpossible` | No.  Unit-ideal linear combination `1 = 0` from `h1,h2,h4` (`h3` unused) |
| `terminalOnly` | same first three quadrics, fourth without `-52488`, plus terminal quintic with `-17496` | `GCD369CubeTerminalOnlyQuadraticImpossible` | No.  Unit-ideal combination from `h1,h2,h5` (`h3,h4` unused) |
| `doubleNormal` | `S` and `3*S/4 = 0 ∧ 3*S/4 = 0 ∧ (-1/16 : K) = 0 ∧ -(4*S+3)/16 = 0` | `GCD369CubeDoubleRootNormalObstruction S` | Yes in characteristic zero: `(-1/16 : K) = 0` is already `False`.  Duplicate first conjunct |
| `zeroSheet` | `Kpoly Kdot eta` and Wronskian `≠ 0` for the common-power sheet | `GCD369CubeZeroSheetTerminalExclusion` | Yes.  `GCD369CubeZeroSheetBracket` proves that Wronskian is identically `0` |
| `mixedElliptic` | `μ ≠ 0`, coprime `M,N`, nonzero `Den`, Fermat–Catalan curve `72 M² − 3 N³ − 512μ Den⁶ = 0`, and `¬(degrees 0)` | `GCD369CubeMixedEllipticTerminalExclusion` | Yes as a pair: `GCD369CubeMixedEllipticConstancy` derives constancy from the curve, contradicting `hnonconstant` |
| `unmixedElliptic` | same pattern with `M² − 3 N³ − 4096μ Den⁶ = 0` | `GCD369CubeUnmixedEllipticTerminalExclusion` | Yes as a pair, via `GCD369CubeUnmixedEllipticConstancy` |
| `mixedCusp` | `ν ≠ 0`, `j ≠ 0`, reduced `LN/LB`, cusp Wronskian ODE | `GCD369CubeMixedCuspAllCoreTerminalExclusion` | No.  Payload is the ODE itself, not a theorem conjoined with its negation |
| `davenportStothers` | `j ≠ 0`, reduced `LN/LB`, seventh-power Wronskian ODE, **and** `hboundary` (common root of the normalized DS pair) | `GCD369CubeDSAllCoreTerminalExclusion` | Yes for inhabitation: `hboundary` is independently `False` by `GCD369CubeDSBoundaryExclusion`.  Positive-degree case of the consumed theorem then ignores the ODE and reapplies that Bezout |

Exact consumed types:

```lean
theorem GCD369CubeConstantPoleDegreeLandingEmpty
    (D : GCD369CubeConstantPoleDegreeLanding) : False

theorem GCD369CubeEarlyBoundaryDataEmpty
    {K : Type*} [Field K] [CharZero K]
    (D : GCD369CubeEarlyBoundaryData K) : False

theorem GCD369CubeRhoFourFirstLoadImpossible {K : Type*} [Field K] [CharZero K]
    (Xn Yn Zn u v : K)
    (h1 : 729 * u * Xn ^ 2 - 1458 * Xn * Zn - 729 * Yn ^ 2 = 0)
    (h2 : -2187 * v * Xn ^ 2 - 4374 * u * Xn * Yn + 4374 * Yn * Zn = 0)
    (_h3 : 2 * u ^ 2 * Xn ^ 2 - 6 * v * Xn * Yn - 4 * u * Xn * Zn
          - 2 * u * Yn ^ 2 + 3 * Zn ^ 2 = 0)
    (h4 : 19683 * u * v * Xn ^ 2 + 13122 * u ^ 2 * Xn * Yn
          - 26244 * v * Xn * Zn - 13122 * v * Yn ^ 2
          - 13122 * u * Yn * Zn - 52488 = 0) : False

theorem GCD369CubeTerminalOnlyQuadraticImpossible
    {K : Type*} [Field K] [CharZero K]
    (Xn Yn Zn u v : K)
    (h1 : 729 * u * Xn ^ 2 - 1458 * Xn * Zn - 729 * Yn ^ 2 = 0)
    (h2 : -2187 * v * Xn ^ 2 - 4374 * u * Xn * Yn + 4374 * Yn * Zn = 0)
    (_h3 : …) (_h4 : … without the constant -52488)
    (h5 : -729 * u ^ 3 * Xn ^ 2 + 2187 * v ^ 2 * Xn ^ 2
          + 4374 * u * v * Xn * Yn + 1458 * u ^ 2 * Xn * Zn
          + 729 * u ^ 2 * Yn ^ 2 - 4374 * v * Yn * Zn - 17496 = 0) : False

theorem GCD369CubeDoubleRootNormalObstruction {K : Type*} [Field K] [CharZero K]
    (S : K) :
    ¬ (3 * S / 4 = 0 ∧ 3 * S / 4 = 0 ∧ (-1 / 16 : K) = 0 ∧
       -(4 * S + 3) / 16 = 0)

theorem GCD369CubeZeroSheetTerminalExclusion
    {K : Type*} [Field K] [CharZero K]
    (Kpoly Kdot : K[X]) (eta : K)
    (hterminal : let f := Kpoly ^ 2 + C eta
                 let g := Kpoly ^ 3 + C (3 * eta / 2) * Kpoly
                 let fdot := C 2 * Kpoly * Kdot
                 let gdot := (C 3 * Kpoly ^ 2 + C (3 * eta / 2)) * Kdot
                 fdot * derivative g - derivative f * gdot ≠ 0) : False

theorem GCD369CubeMixedEllipticTerminalExclusion
    {K : Type*} [Field K] [CharZero K]
    (mu : K) (hmu : mu ≠ 0) (M N D : K[X])
    (hM : M ≠ 0) (hN : N ≠ 0) (hD : D ≠ 0) (hMN : IsCoprime M N)
    (hcurve : C 72 * M ^ 2 + C (-3) * N ^ 3 + C (-512 * mu) * D ^ 6 = 0)
    (hnonconstant : ¬ (M.natDegree = 0 ∧ N.natDegree = 0 ∧ D.natDegree = 0)) :
    False

theorem GCD369CubeUnmixedEllipticTerminalExclusion
    -- same shape with C 1 * M ^ 2 and C (-4096 * mu) * D ^ 6

theorem GCD369CubeMixedCuspAllCoreTerminalExclusion {K : Type*}
    [Field K] [CharZero K] [IsAlgClosed K]
    (nu j : K) (hnu : nu ≠ 0) (hj : j ≠ 0)
    (s LN LB : K[X]) (hs : s ≠ 0) (hLN : LN ≠ 0) (hLB : LB ≠ 0)
    (hlambdaReduced : ∀ x : K, eval x LN = 0 → eval x LB ≠ 0)
    (hODE : let P := C 19683 * LN ^ 13 - C (nu ^ 2) * LB ^ 13
            let Q := C 1458 * LN ^ 6 * LB ^ 7
            s * (derivative P * Q - P * derivative Q) = C j * Q ^ 2) : False

theorem GCD369CubeDSAllCoreTerminalExclusion {K : Type*}
    [Field K] [CharZero K] [IsAlgClosed K]
    (j : K) (hj : j ≠ 0) (s LN LB : K[X])
    (hs : s ≠ 0) (hLN : LN ≠ 0) (hLB : LB ≠ 0)
    (hlambdaReduced : ∀ x : K, eval x LN = 0 → eval x LB ≠ 0)
    (hODE : s * (derivative (LN ^ 7) * LB ^ 7 - LN ^ 7 * derivative (LB ^ 7))
            = C j * (LB ^ 7) ^ 2)
    (hboundary : ∃ r : K,
        eval r (X ^ 6 + C 4 * X ^ 4 + C 10 * X ^ 2 + C 6) = 0 ∧
        eval r (X ^ 9 + C 6 * X ^ 7 + C 21 * X ^ 5 + C 35 * X ^ 3
                + C (63 / 2) * X) = 0) : False
```

Inner types introduced in the same file (the first of them also in this commit):

```lean
inductive GCD369CubeConstantPoleDegreeLanding : Prop where
  | dsA4   (n : ℕ) (h : (2 : ℚ) / 14 = n)
  | dA4    (n : ℕ) (h : (2 : ℚ) / 13 = n)
  | c7A4   (n : ℕ) (h : (2 : ℚ) / 12 = n)
  | c7A3   (n : ℕ) (h : (3 : ℚ) / 12 = n)
  | c5A4   (n : ℕ) (h : (2 : ℚ) / 10 = n)
  | c4A3   (n : ℕ) (h : (3 : ℚ) / 9  = n)
  | c2A4   (n : ℕ) (h : (2 : ℚ) / 7  = n)
  | c1A4   (n : ℕ) (h : (2 : ℚ) / 6  = n)
  | c1A3   (n : ℕ) (h : (3 : ℚ) / 6  = n)
  | rho1A4 (n : ℕ) (h : (2 : ℚ) / 4  = n)
  | rho2X  (n : ℕ) (h : (-1 : ℚ) / 2 = n)
  | rho2Y  (n : ℕ) (h : (-1 : ℚ) / 6 = n)
  | rho2Z  (n : ℕ) (h : (1 : ℚ) / 6  = n)

structure GCD369CubeEarlyBoundaryData (K : Type*) [Field K] where
  k q a h Xn Yn Zn u v r EF EG
  hk : k ∈ ([1, 2, 4, 5, 7, 8, 10, 11] : List ℕ)
  ha : a ≠ 0
  hh : h ≠ 0
  hnocommon : ∀ z, z^3 + u*z + v = 0 → Xn*z^2 + Yn*z + Zn = 0 → False
  hKroot : r^3 + u*r + v = 0
  hEF : (↑(1:ℚ) : WithTop ℚ) < EF.orderTop
  hEG : (↑(3/2:ℚ) : WithTop ℚ) < EG.orderTop
  hfregular : (↑((12:ℚ)/k) : WithTop ℚ) ≤ (A^2 + H*B + EF).orderTop
  hgregular : (↑((18:ℚ)/k) : WithTop ℚ) ≤ (A^3 + C32*H*A*B + EG).orderTop
```

`GCD369CubeConstantPoleDegreeLandingEmpty` is itself glue of `GCD369CubeConstantPoleDegreeAudit`, a conjunction of thirteen `∀ n : ℕ, q ≠ n` facts for those rationals.  Naming the constructors `dsA4`, `c7A4`, … records an intended routing table in comments only.  No hypothesis of any constructor is a Keller pair, a Jacobian, a cube core `h = s^3`, a Faber–Laurent reduction, or original Taylor boundaries of a `(6,9)` pair.

---

## 2. Project-wide search for a source-to-landing map

Searched the entire pinned nested tree (`*.lean`, `*.md`, `*.yaml`, `*.json`) for `GCD369CubeTrajectoryLanding`, source-to-landing maps, exhaustive landing, and cube/Keller source types.

`GCD369CubeTrajectoryLanding` occurs four times, all in `gcd3-69-cube/Solution.lean`: the inductive, the Empty theorem signature, its type, and `#print axioms`.  No other package mentions it.

Closest declarations in the pinned project, none of which map cube/Keller/source data into `GCD369CubeTrajectoryLanding K`:

| Name | Type (compressed) | Why it is not the map |
|---|---|---|
| `GCD369CubeLowerRowTriangularity` | `[Field K] [CharZero K] →` displayed `A1…A5` linear combination `= C q ↔ u1=u2=u3=u4=0 ∧ 6*u5=q` | Algebraic triangularity of five lower-row polynomials.  Not consumed by Empty.  No landing constructor |
| `GCD369CubeDExceptionalNoCommonRoot`, `GCD369CubeC7NoCommonRoot`, `GCD369CubeC5NoCommonRoot`, `GCD369CubeC4NoCommonRoot`, `GCD369CubeC2NoCommonRoot`, `GCD369CubeC1NoCommonRoot`, `GCD369CubeRhoOneNoCommonRoot`, `GCD369CubeRhoTwoNoCommonRoot` | each: Kuranishi quadrics `→ ∀ r, cubic(r)=0 → normal(r)=0 → False` | Local non-intersection certificates.  Not constructors of the landing type.  Empty does not consume them |
| `GCD369CubeEarlyBoundaryDataEmpty` | `GCD369CubeEarlyBoundaryData K → False` | Emptiness of one already-packaged branch, not exhaustiveness of the list |
| `GCD369TopRowIdentity` (`gcd3-69-core`) | `8 D(s⁶)(s⁸ B) + 9 D(s⁵ A) s⁹ − 6 s⁶ D(s⁸ B) − 5 (s⁵ A) D(s⁹) = s¹⁴ (9 DA − 6 DB)` | First-gate `y¹³` cancellation.  No cube trajectory, no landing |
| `GCD369KummerAlignment` | nontrivial Kummer + top-row vanishing `→ 3A−2B=0` | Alignment on the *noncube* Kummer side |
| `GCD369SimultaneousDepression` | `3A−2B=0 →` coeff `5` of `p` and coeff `8` of `q` vanish | Depression identity |
| `GCD369CubeFactorNeutral` | `F⟮g·t⟯ = F⟮t⟯` for `g ≠ 0` | Generator-field neutrality, not a trajectory landing |
| `GCD369DavenportStothersCertificate` | order-three DS identities in parameter `mu` | Family identities, not a map of a Keller pair onto a landing constructor |
| `GCD369AlignedNoncubeExclusion` (`gcd3-69-noncube`) | displayed aligned noncube Keller/function-field data `→ False` | Opposite branch: `¬ ∃ u, H = u^3`.  Explicitly not the polynomial cube core |

There is no theorem of type

```text
(cube / Keller / Faber–Laurent / original-boundary source data) → GCD369CubeTrajectoryLanding K
```

and no theorem asserting that every such source inhabits one of the ten constructors.  That absence remains an open source-completeness obligation.

---

## 3. Constructor fidelity and already-contradictory premises

**Preserved relative to the consumed branch theorem, not relative to a Keller source.**  Each constructor’s fields are a re-packaging of the corresponding exclusion’s hypotheses.  There is no opaque `Admissible` predicate.  That is an honest formal interface at the *branch* grain.  It is not preservation of original cube-core hypotheses, because those hypotheses are not present.

**Already contradictory by definition (vacuous constructors).**

- `constantPole`: every inner constructor asks a rational in `{2/14, 2/13, 2/12, 3/12, 2/10, 3/9, 2/7, 2/6, 3/6, 2/4, -1/2, -1/6, 1/6}` to be a natural number.  `GCD369CubeConstantPoleDegreeAudit` already proves none is.
- `doubleNormal`: third conjunct is `(-1/16 : K) = 0`.  Under the Empty instance `[CharZero K]` this is `False` before `S` is used.  The two copies of `3 * S / 4 = 0` are not two independent rows.
- `zeroSheet`: `hterminal` is the negation of `GCD369CubeZeroSheetBracket`, which holds for every `Kpoly, Kdot, eta`.
- `mixedElliptic` / `unmixedElliptic`: `hcurve` plus `hnonconstant` is exactly “`P` and `¬P`” once constancy is applied.
- `davenportStothers`: `hboundary` is independently `False` for every `r` by `GCD369CubeDSBoundaryExclusion`.  Inhabiting the constructor already requires a false common root.  The seventh-power ODE is idle for emptiness of this summand.  Further, the positive-degree case of `GCD369CubeDSAllCoreTerminalExclusion` obtains `GCD369CubeDSMonomialExponent` and discards it, finishing solely from `hboundary`.

**Substantive as packaged algebra, still not source coverage.**

- `rhoFour` and `terminalOnly` are genuine unit-ideal certificates.  Unused `_h3` / `_h4` mean those displayed equations are not used; they are still required to inhabit the constructor, so the constructor is strictly stronger than the linear combination that kills it.
- `earlyBoundary` is a real Hahn-series obstruction for weights in `{1,2,4,5,7,8,10,11}`.  Weight `12` is excluded by design (comment: first equality case).  Weights `0,3,6,9` are not in the list.  Whether those omissions match a source routing table is a transcription obligation, not a Lean fact.
- `mixedCusp` matches `GCD369CubeMixedCuspAllCoreTerminalExclusion` field-for-field, including the constant/positive-degree split inside that theorem.  Original polynomial boundaries of `f` and `g` are not hypotheses.

**Direction.**  The landing type is `Prop`-valued and stores data (polynomials, Hahn series, equations).  Empty reads `Landing → False`.  Source completeness would read `Source → Landing` (or `Source → False` after composition).  Calling Empty a “source-completeness gluing theorem” is a type-level reversal in the comment, not in the type.  The type is correctly weaker.

**Hypothesis drop versus cube source.**  No constructor carries: a bivariate Keller pair; `det J ∈ Kˣ`; actual partial degrees `{6,9}`; a polynomial cube `h = s^3`; Faber–Laurent `g = [H(f^{1/6})]_+`; lower-row identities `r₁'=…=r₄'=0`, `6 r₅' = j/s`; or original Taylor jets `f(r) = P₀`, `g(r) = Q₀` except the *normalized DS pair* inside `hboundary`, which is already unsatisfiable.  `GCD369CubeLowerRowTriangularity` is the file’s own lower-row interface and is unused by the glue.

---

## 4. What AWS `lake build` plus no-`sorryAx` can and cannot establish

**Can establish (build/axiom hygiene only).**

- The pinned `Solution.lean` compiles against the pinned Mathlib rev `20bc12820422504f9e52ee6caebf8182a9015336`.
- `GCD369CubeTrajectoryLandingEmpty` and the ten consumed exclusions have no `sorryAx`.
- `#print axioms` on Empty reports some Mathlib kernel axioms (expected: at least `Classical.choice` from the two local `classical` blocks in `GCD369CubeRationalPrimitiveRootCount` and `GCD369CubeRationalPrimitiveOneRoot`, plus whatever those lemmas pull from `IsAlgClosed` root existence).
- Constructor indices of the inductive match the `cases` branches.

The AWS preregistration `cases/jc2_lean_cube_f0b5823_aws_verify_20260826/PREREGISTRATION.md` already records this limit.  A green build is not coverage.

**Cannot establish (independent mathematical transcription).**

- That every hypothetical polynomial-cube / Keller / Faber–Laurent trajectory produces some constructor.
- That the ten constructors are exhaustive even relative to this file’s own unused Kuranishi non-intersection family (`C7`, `C5`, `C4`, `C2`, `C1`, `rho1`, `rho2`, exceptional `d ≠ 0`).
- That constructor names `dsA4`, `c7A4`, … correctly transcribe source degree demands.
- That early weights `{1,2,4,5,7,8,10,11}` are the complete early-forced list.
- Any statement whose type mentions `(6,9)`, maximum eleven, maximum twelve, or JC2.

The cube file header comment says “polynomial-cube `(6,9)` trajectory certificates.”  That string is not a theorem.

---

## 5. Strongest licensed theorem and smallest missing declaration

**Licensed.**  Over a characteristic-zero algebraically closed field, there is no inhabitant of `GCD369CubeTrajectoryLanding K`.  Equivalently: each of the ten explicitly written packages is empty, so their disjoint union is empty.

**Not licensed.**  Emptiness of the polynomial cube core; emptiness of actual partial degrees `(6,9)` with `3 ∣ H`; maximum-eleven automorphy; maximum-twelve frontier statements; JC2.  The sibling `GCD369AlignedNoncubeExclusion` is a different branch and is not composed here.

**Smallest missing declaration needed to close the cube branch** (not present in the pinned project; names of source data are descriptive, not claimed to exist as Lean types):

```lean
/-- Missing from commit f0b5823.  Smallest map that would turn
    `GCD369CubeTrajectoryLandingEmpty` into a cube-core exclusion. -/
theorem GCD369CubeSourceToTrajectoryLanding {K : Type*}
    [Field K] [CharZero K] [IsAlgClosed K]
    -- original hypothetical polynomial-cube source, including at least:
    -- a Keller / Jacobian row 6 r₅' = j/s with j ≠ 0,
    -- polynomial cube core h = s³,
    -- Faber–Laurent / lower-row triangularity data,
    -- and original polynomial boundary jets
    (source : GCD369CubeCoreSource K) :
    GCD369CubeTrajectoryLanding K
```

Closing the cube branch is then the composition

```text
GCD369CubeSourceToTrajectoryLanding ≫ GCD369CubeTrajectoryLandingEmpty
  : GCD369CubeCoreSource K → False
```

Defining `GCD369CubeCoreSource` and proving the map are the remaining source-transcription work.  Until that map exists, Empty cannot be applied to any genuine cube source.

A weaker but still missing exhaustive-or statement would also suffice:

```lean
theorem GCD369CubeTrajectoryExhaustive {K : Type*}
    [Field K] [CharZero K] [IsAlgClosed K]
    (source : GCD369CubeCoreSource K) :
    GCD369CubeTrajectoryLanding K
```

No such `Or`/`cases`-producing theorem exists either.

---

## 6. Axioms, sorry, classical, placeholders, vacuity

Pinned `gcd3-69-cube/Solution.lean`: no `axiom`, no `sorry`, no `admit`, no `sorryAx`.  `Challenge.lean` files in sibling packages contain `sorry` as statement stubs; the cube package has no Challenge file.

Local `classical` appears at:

- `GCD369CubeRationalPrimitiveRootCount` (line 2030), used to take `s.roots.toFinset` and unique-root bookkeeping over `[IsAlgClosed K]`;
- `GCD369CubeRationalPrimitiveOneRoot` (line 2199), which consumes that lemma.

This is ordinary Mathlib classical reasoning for algebraic closures, not a hidden extra axiom in the cube file.  It is inherited by mixed-cusp and DS exclusions, hence by Empty.  It is an intentionally scoped interface, not a defect.

No opaque placeholder predicate.  Vacuous implications are real and listed in §3: six of ten constructors (`constantPole`, `doubleNormal`, `zeroSheet`, `mixedElliptic`, `unmixedElliptic`, `davenportStothers`) are uninhabitable without the cube-core narrative.  That is a scoped-interface smell (glue of `False → False` summands), not a kernel hole.

Type-level direction reversal is confined to the docstring.  The type of Empty does not claim `Source → False`.

---

## Promotion boundary

Accept only: at nested commit `f0b5823c2d008807fa6524401faf2e1413d7a5f8`, SHA-256 `6407444078ad5ea0ce93ec55440b2629d10676abcff6614887ef47c97e8e0de2`, the declaration `GCD369CubeTrajectoryLandingEmpty` proves that the ten-constructor inductive `GCD369CubeTrajectoryLanding K` is empty over characteristic-zero algebraically closed fields, by dispatch to ten previously written branch exclusions.

Do not promote this to: a theorem that every polynomial-cube trajectory lands in that list; emptiness of the cube core; a `(6,9)` exclusion; composition with the aligned noncube theorem; maximum eleven or twelve; or JC2.

**Smallest honest successor.**  Introduce a Lean source type for the polynomial-cube hypotheses and prove `GCD369CubeSourceToTrajectoryLanding`.  Until then the cube branch is formally glued and mathematically unclosed.

FORMAL_GLUE_ONLY
