# R5-CHARGE — draft disproof-matrix charge sheet

**Lane.** Preparation (disproof side), 2026-08-31, grok-4.6.
**Sole legitimate target.** Declared finite-support cell of R5: the hypothetical exact \(\mathbb{Z}_{109}\) polynomial lift of \((x-x^{109},\,y)\).
**Charged inputs (frozen, read-only).**
- `xmodel/as109-d12-seed-provenance-reconciliation-grok46-20260831.md`
- `xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`
**Scope.** Desk-scale exact reasoning only. No CAS. No computation of uncertain duration. No edits to canonical ledgers, charged files, or `jc2-lean`.
**Delivery.** Either a complete draft charge sheet for coordinator review and different-model audit, or a typed STOP at the first preflight step that cannot be discharged.

## 0. Hash verification of frozen charged inputs

Frozen copies under `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.1pSBBA/inputs` were hashed with SHA-256 (`shasum -a 256`). Both match the charged values. Proceed. Workspace copies of the same filenames were not used as authority. Citations below to those two charged files refer to the frozen copies.

| expected | observed | file |
|---|---|---|
| `bb2a3d0753583ef08f78f989e2c9b6a1026652e423f1b2722533274d80ae9a6a` | match | `as109-d12-seed-provenance-reconciliation-grok46-20260831.md` |
| `126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286` | match | `block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md` |

The 11-step fail-closed preflight is the charged reconciliation §6 (frozen copy). The second charged file is a 2026-08-31 coordinator integration of Theorem N-A / residual \(D_1\) / ROW-SWEEP. It does not mention AS109, R5, Witt rings, or a support grammar. It is cited only as a firewall against identifying R5 with the char-0 residual class of that integration (reconciliation R8 / td6 Card C). It supplies no ring map and no freeze.

Desk method. Read-only. No CAS. No uncertain-duration computation. No inspection of `jc2-lean`. No edit of canonical ledgers or charged files. Primary literature may be fetched and hashed. UNSTATED is recorded rather than filled by family resemblance, cap, or analogy (FALLACY-v2; reconciliation §5–§6).

## 1. Preflight step 1 — name R5 explicitly

**Status.** Discharged.

**Registry id.** `R5`. Campaign name: `AS109-LIFT`.

**Object.** The hypothetical exact polynomial lift of the special fibre R4 over the 109-adic integers. Displayed in every cited exact-lift producer as

```text
P = x - x^{109} + 109 A,     Q = y + 109 B,
A, B ∈ Z_{109}[x,y],         det J(P,Q) = 1.
```

R4 is the special fibre `(x-x^{109}, y)` over `F_{109}` (support gate `86–97`). R5 is not R4: the coefficient ring is `Z_{109}`, fraction field `Q_{109}` (closed-support `6–7,32–38`; AS-TRI promotion `16–32,50–52`). The AS-TRI firewall is binding: the proof “would be false if `Z_{109}` were incorrectly read as `F_{109}`”.

**Named subshape.** Not chosen at this step. The charged reconciliation permits a named subshape of R5 (two-sided floor-twelve, or residual `n=6`) in place of the whole moduli set `L`. This draft names the ambient object `R5` here and attempts, at step 4, to freeze a finite-support cell inside it. Naming a subshape without exponent sets is not a freeze.

**Excluded ids (not the degree-12 frontier; do not charge).**

| id | why excluded |
|---|---|
| R1 `AS3-FIBRE`, R2 `AS3-W2` | documented finite-level `F_3` / `W_2(F_3)` lifts; no map to R5 (reconciliation §3) |
| R3 `TATE-p` | all-Witt cotangent control; support/degree grow by construction; `NO MAP CLAIMED` to R5 |
| R4 `AS109-FIBRE` | residue field of R5, not the lift |
| R6 `AS109-HENSEL` | theorem about R5 (109 sheets), not a search grammar |
| R7 `AS109-D12-CELL` | underspecified matrix card; missing data are this preflight, not a ninth seed |
| R8 `MAX12-CHAR0` | char-0 maximum-eleven theorem used as an *ingredient* of the R5 floor; not an AS109 seed |

Labels “AS109”, “F_109”, “degree 12”, “Witt”, “row 19” are not names (preflight §6.1).

**Second charged input.** The N-A / residual-`D_1` / ROW-SWEEP coordinator integration does not name R5 and supplies no map from the Nori residual class (one explicit three-node `(6,4)` curve, plus six AM-numerical types) to R5 or R8. It is not a registry id. Identifying that residual class with R5, or with char-0 shapes `(8,12)`/`(9,12)`, is the Card C silent-identification flag (reconciliation §4.7) and is not done here.

**Step 1 entry (charge sheet).** Target = R5 = `AS109-LIFT` = hypothetical exact `Z_{109}` polynomial lift of `(x-x^{109}, y)`.

## 2. Preflight step 2 — lift ring, matrix ring, reduction map

**Status.** Discharged (rings and map exhibited; no matrix is charged, because later preflight stops).

**Lift ring.** `R = Z_{109}[x,y]`, with `A,B ∈ R`. Packed identity, closed-support (1.1) at `32–44`, no digit choices and no base-109 carries in the identity itself:

```text
p = 109,     s = x^{108},
F_(A,B) = (x - x^p + p A,  y + p B),
L(A,B) = A_x + B_y,
N(A,B) = (A_x - s) B_y - A_y B_x,

det J(F_(A,B)) - 1 = p ( L(A,B) - s + p N(A,B) ).     (1.1)
```

Exact Keller condition in this chart: `E(A,B) := L(A,B) - s + 109 N(A,B) = 0` in `R`. Equivalent form used as the closed-support contraction residual (support gate `230–232`): `L(u)-s+109 N(u)=0`.

**Truncated alternative (not chosen).** Support-gate digits modulo `109^3` with carry-aware second residual (erratum `42–70`):

```text
P = x-x^p + p A_0 + p^2 A_1,     Q = y + p B_0 + p^2 B_1    (mod p^3),
C_1 = L(A_0,B_0)-s,     K = C_1/p  after C_1 ≡ 0 (mod p),
K + L(A_1,B_1) + N_0 ≡ 0 (mod p).
```

Uncarried `E1,E2` over `F_{109}` are quarantined as the exact condition modulo `109^3` (erratum `31–40,121–125`; five-slot countercontrol `92–125`). They are not the matrix.

**Matrix ring.** If a linearized rank certificate is later formed, its coefficient field is `F_{109}`. That field is a *digit field of R5*, not the lift ring (reconciliation R7; AS-TRI `50–52`). Matching the letter `x` across `Z_{109}[x,y]` and `F_{109}[x,y]` is not a map (FALLACY-v2 variable/ring map).

**Reduction map (exhibited).** Coefficient reduction

```text
ρ : Z_{109}[x,y] → F_{109}[x,y],
ρ(∑ a_{ij} x^i y^j) = ∑ (a_{ij} mod 109) x^i y^j,
```

extended componentwise to pairs. On the packed ansatz:

```text
ρ(F_(A,B)) = (x - x^{109}, y).
```

That is the seed-reduction check of preflight §6.8, written here because it is the image of the map, not an extra hypothesis. For the packed residual, `109 N` dies under `ρ`:

```text
ρ(E(A,B)) = L(ρA, ρB) - x^{108}  ∈ F_{109}[x,y].
```

So an `F_{109}`-linear matrix of first-order unknowns is the coefficient matrix of `L(Ā,B̄) = x^{108}`, which is a *necessary* reduction of (1.1), not a substitute for (1.1). The nonlinear term `109 N` is invisible over `F_{109}`. Consequently this matrix ring cannot, by itself, be a floor-twelve test: the two-slot family `A_0=y^m`, `B_0=x^{108} y` already solves the reduced equation for every `m≥1` (support gate `117–140`; review claim 3 CONFIRMED).

**Not claimed.** No map R7→R5 (reconciliation §3). No map R3@`p=109` → R5 as polynomial maps `A^2→A^2`. No identification of `Z_{109}` with `F_{109}`.

**Step 2 entry.** Lift ring `Z_{109}[x,y]` + packed (1.1). Matrix ring `F_{109}` only as `ρ` of that packed residual. Map `ρ` as displayed. Uncarried `E1,E2` not used.

## 3. Preflight step 3 — Witt level \(n\)

**Status.** Discharged as a typed non-truncation.

**Declaration.** There is no finite `n` such that the charged object is “the system modulo `109^n`”. The charged system is the packed exact identity (1.1) in `Z_{109}[x,y]`: all 109-adic digits of the coefficients of `A` and `B` at once. Digit unknowns: every coefficient of the pair `(A,B)`, not a finite Witt tower `(A_0,…,A_{n-1})`.

**Why floor-twelve constrains this choice.** The promoted floor (producer `17–20`; review verdict CONFIRMED at line 7; no-cap firewall `20–22`) is:

```text
P = x - x^{109} + 109 A,   Q = y + 109 B  in Z_{109}[x,y],
det J(P,Q) = 1
    ⇒   max(deg_y A, deg_y B) ≥ 12.
```

The hypothesis is exact `det J = 1` in characteristic zero over `Q_{109}`, using the char-0 maximum-eleven automorphism theorem plus residue-ball Hensel. It is not a statement about a pair over `W_n(F_{109}) = Z/109^n`.

At every *finite* Witt level the Tate control R3 at `p=109` is the pair `F_n = (x-x^{109}, y S_n)` over `Z/109^n`, with `S_n = ∑_{j=0}^{n-1} 109^j x^{j·108}` and `det J = 1 - 109^n x^{n·108}`. That pair has `y`-degree 1 at every finite `n` (tate `42–83`; polar `10–21`; wild review `376–379`, sampled at `p=3,5` with the same closed form). A finite-`n` truncation with correction `y`-degree 1 is therefore compatible with known objects and is *not* a degree-12 cell of R5. Charging “the first unsolved Witt step” (R7 card) would be exactly that truncation, and would silently identify R3 with R5.

The σ_τ action on the moduli of lifts depends on `τ` modulo `109^2` and does not descend to `F_{109}` (opus5 `491–495`). That is a gauge signature, not a licence to truncate the lift at `n=2`.

Carry-aware digits modulo `109^3` (erratum) are a named truncation of the packed identity. They are not chosen: floor-twelve does not apply to them, and the uncarried `E2` is quarantined.

**Finite `n` that would have been wrong.**

- `n=1`: special fibre R4; no lift.
- `n=2`: first digit `L ≡ x^{108} (mod 109)`, solved by the unbounded `G_m` family; affine-`y` and `y`-degree 1 live here.
- `n=3`: erratum’s layer; still not a char-0 degree floor.
- Unrestricted further `n` of R3: preflight §6.11 forbids charging it.

**Step 3 entry.** `n = packed-exact` (no finite modulus `109^n`). Unknowns = coefficients of `(A,B)` in `Z_{109}[x,y]`. Justification: floor-twelve is a theorem only at this level; every finite `n` is occupied by `y`-degree-1 objects that are not the degree-12 frontier.

## 4. Preflight step 4 — freeze finite \(x\)- and \(y\)-support exponent sets

**Status.** `NO-FROZEN-GRAMMAR`. This is the first preflight step that cannot be discharged. STOP here. Steps 5–11 are not reached. The matrix route stays closed until the new input named at the end of this section exists.

Preflight §6.4 requires explicit finite exponent sets for `A` and `B` (or `P` and `Q`). A slot-count cap is not a grammar. “Maximum correction `y`-degree 12” is a floor, not a set. If no finite exhaustive gauge-normal grammar exists, the historical stop is `NO-FROZEN-GRAMMAR` and the cell is not chargeable.

### 4.1 Attempted `y`-bidegree (floors, not a freeze)

Banked two-sided exclusions, both corrections simultaneously, arbitrary finite `x`-degree: `≤2` (quadratic gate `14–19`), `≤3` (cubic `(3.2)` at cubic `316`), `≤4` (quartic `7–10,25–30`). Affine-`y` (both `deg_y ≤1`) is an independent no-go (closed-support Thm 3.1). Floor-twelve, promoted: `max(deg_y A, deg_y B) ≥ 12` (floor-twelve producer `17–20`; review CONFIRMED). One-sided: `deg_y Q = deg_y B ≥ 6` (prime/4 `(1.2)`), strengthening AS-TRI `deg_y B ≥ 2`. AS-TRI licensed compositions kill the two-sided shapes `(deg_y A, deg_y B) = (12,0)` and `(12,1)`.

Two candidate “minimal” shapes, both already named by the registry as the only licensed subshapes of R5:

1. **Two-sided floor-twelve box.** `deg_y A ≤ 12`, `deg_y B ≤ 12`, and `max = 12`. Smallest rectangle compatible with the two-sided floor. FALLACY-v2 floor/attainment: a lower bound is not exact. Nothing in the cited producers proves that a lift, if it exists, attains 12 rather than some larger degree. Choosing 12 as a *declared cell* would be a cap, not a theorem-forced unique bidegree.
2. **Residual `n=6` corner** (prime/4 §5; n=6 face `30–38`). `n = deg_y Q = 6`, `m = deg_y P ≥ 12`, `3 | m`, `6 | deg_x(q_6)`, `d = gcd(m,6) ∈ {3,6}`, with common-core `p_m = α h^{m/d}`, `q_6 = β h^{6/d}` and `d=3 ⇒ 3|H`, `d=6 ⇒ 6|H`. Here `m` is unbounded above 12, and `H = deg_x h` is unbounded subject only to those divisibilities. Smallest currently honest *stratum*, not a finite set of exponents.

Neither (1) nor (2) is a unique cell. Sextic coprime `(5,6)` is a Pfaffian preflight, not an AS109 exclusion (sextic-frontier `19–35`). Residual `n=6` and two-sided `(12,*)` are different shapes (reconciliation R5 `y` support; R7).

### 4.2 `x`-exponents remain unbounded on every licensed shape

- Cap-eight literal-slot grammar: already at the first lift, `A_0 = y^m`, `B_0 = x^{108} y` is a two-slot collision-preserving `E1` solution for every integer `m ≥ 1` (support gate `117–140`; review claim 3 CONFIRMED). The exponent `m` is unbounded. A monomial-count cap is not a finite vertex set.
- Independent-slot closed-support + unit-`L`: any finite full slot module with those hypotheses is forced to contain `x^{108k}` for every `k ≥ 1` (closed-support Thm 2.2, induction on `q_k = (0, x^{108k} y)` and `r_k = (x^{108k+1}, 0)`). Finite free residual modules cannot contain all of those monomials. The theorem uses no degree bound, marked collision, or eight-slot cap.
- Floor theorems themselves are stated at arbitrary finite `x`-degree (quadratic `8–9`; prime/4 `26–28`; cubic `319–320`; quartic `8–10`; floor-twelve review `20–22`: “No target reduction, support cap, fixed-total-degree hypothesis, or source normalization is used”).
- Residual (5.1): `6 | deg_x(q_6)` includes every multiple, and the constant-leading case `deg_x(q_6)=0`. That is an arithmetic progression, not a finite set.

A coupled example `U_cpl = R·(x^{109}, (1-109)x^{108} y)` shows raw support on two slots need not be independent (closed-support `148–160`). Coupling is necessary, not a freeze: the same example still fails closure on `W = R·s`. No cited producer supplies a finite coupled `R`-module with proved `N`-closure and unit right inverse (closed-support §4, items 1–4).

### 4.3 No exhaustive gauge-normal grammar

Historical stop, dual-confirmed: `NO-FROZEN-GRAMMAR` (support gate verdict; review promotion `29–33`, claim 5). Literal enumeration is infinite. Omitting the `G_m` family requires a proved gauge normal form, not a larger loop limit (support gate `154–155`). A degree rectangle “would make the computation finite but is expressly forbidden and would be an unregistered sparse cap” (support gate `19–20`). Successor support is not a gauge invariant without explicit `mod 109^3` transport, and that transport is not a finite normal form (review `31`).

The triangular source family that generated the stop:

```text
G_m = (x + 109 y^m, y),     m ≥ 1,
```

is an exact integral triangular automorphism, determinant one, inverse `(x-109 y^m, y)`, fixing `(0,0)` and `(1,0)`. Precomposition produces the two-slot family modulo `109^2`. Exact transport through the successor adds three new slots with unbounded exponent `m` (support gate `170–184`; review claim 4 CONFIRMED). Erratum: this family has integral `C_1 = 0`, so the grammar obstruction is not an artifact of the quarantined carry (erratum `133–150`).

Translation gauge on the lift set `L` (opus5 §4.1, claimed EXACT): `σ_τ(x,y) = (x+τ, y)` for every `τ ∈ Z_{109}` maps `L` to `L`, freely. It acts on moduli of lifts, not as a deck `F ∘ σ_τ = F` (opus5 `502–505`). Slice `[x^{108} y^0]A = 0` is proved only under `deg_x A ≤ 108` (opus5 `515–524`). For `deg_x A > 108` solvability in `τ` is a Newton/Hensel question, not automatic. The same note states that this corollary “does not supply the section for the `(x + 109 y^m, y)` triangular family that generated the stop” (opus5 `526–531`). Using the slice as a freeze would additionally require a proof that every lift in the charged cell has `deg_x A ≤ 108`. No such theorem is cited. Independent-slot closed-support already forces arbitrarily high `x`-powers in the naive full module.

Completed-orbit `Φ_F` of R3 at a polynomial point of the same special fibre is restricted-analytic, `κ_n(F) → ∞` (polar `40–58`). Default: unbounded analytic gauge, not a polynomial bound (preflight §6.6). Polar gate performed no `p=109` enumeration (polar `71`). Instantiating the general-odd-`p` theorem at `p=109` is not a polynomial grammar for R5.

First-order triangular `G_m` used as a *control* on R4 (support gate `142–149`) is not a unique slice of R5 (reconciliation R4 gauge).

### 4.4 Why a self-chosen rectangle is not a discharge

Declaring, for example,

```text
supp(A), supp(B) ⊆ { x^i y^j : 0 ≤ i ≤ 108,  0 ≤ j ≤ 12 }
```

would be a degree rectangle. The support gate forbids it as an unregistered sparse cap. Closed-support Thm 2.2 already says the *independent-slot* matrix on any finite `S` cannot satisfy CLOSED-SUPPORT + UNIT-L; running that matrix would repeat a killed certificate design, not test a new coupled cell (preflight §6.10: inconsistency of a frozen cell kills that cell only; a rectangle is not exhaustive of R5). Floor-twelve does not imply `deg_x ≤ 108`. Residual `n=6` does not imply a bound on `H`. FALLACY-v2: never fill a gap by cap or analogy.

### 4.5 Typed STOP

```text
STOP[R5-CHARGE / NO-FROZEN-GRAMMAR]
step = 4
cell = not chargeable
```

No finite exhaustive gauge-normal grammar for a declared finite-support cell of R5 is present in the charged registry or the producers it cites. This permanently closes the matrix route until new theory, as the launch charge allowed.

**New input that would discharge step 4 (exactly).** One of the following, reviewed, with exponent sets written as finite lists of pairs `(i,j)`:

1. A theorem giving a finite exhaustive gauge-normal form for R5 or a named subshape, including a section of the triangular family `G_m` (the family that generated the stop), successor transport at least through the packed identity (1.1), and invariance of the chosen collision under that section; or
2. A finite coupled `R`-submodule `U' ⊂ R[x,y]^2` (not the full independent-slot module on its raw support) together with a finite free residual module `W` and an `R`-linear right inverse of `L`, with proofs of `s ∈ W`, `L(U') ⊆ W`, `N(U') ⊆ W` including polarizations, and `y`-degree at least two in the section (closed-support §4); the raw monomial supports of a basis of `U'` then become the frozen exponent sets; or
3. If the translation slice `[x^{108} y^0]A = 0` is used: a theorem that every lift in the named subshape satisfies `deg_x A ≤ 108` (or an `R`-integral solution of the higher-degree gauge polynomial for `τ`), *and* item 1 or 2 still, because that slice does not kill `G_m`.

Not sufficient: a larger slot cap; sampling exponents; a motif compiler written during a stopped run (support review `33`); a degree rectangle; “maximum `y`-degree 12”; identifying R3’s growing `x`-support `{0,108,…,(n-1)108}` with an R5 freeze; routing into R8 residual `(8,12)`/`(9,12)` or into the Nori residual class of the second charged file.

## 5. Preflight step 5 — generator order

**Status.** Not reached. STOP at step 4.

No coefficient vector exists until exponent sets exist. Historical matrix orders in nearby AS109 files (`Q1`-first / `y`-major on the wild independent engine, wild review `127`; `s`-first / `y`-major on the polar hostile review, polar review `121`) are orders for R3 digit matrices at sampled odd primes, not a map to R5. Matching those names would not declare an R5 order (FALLACY-v2 variable/ring map). Discharge of step 4 still requires an explicit order of the resulting coefficient vector.

## 6. Preflight step 6 — gauge slice and \(\sigma_\tau\) restriction

**Status.** Not reached. STOP at step 4. Facts already used in §4.3 are recorded there, not as a discharged slice.

A later charge, after a grammar exists, would have to pick one section of: translation `σ_τ` with a named `τ` and the `deg_x A ≤ 108` restriction if that slice is used; a named triangular `G_m`; or a *polynomial* bound on `Φ_F` (default: unbounded analytic). It must record that `σ_τ` acts on lifts, not as a deck, and prove the cell is a section. Present producers do not supply the `G_m` section (opus5 `526–531`) and do not prove `deg_x A ≤ 108` on R5.

## 7. Preflight step 7 — collision as one typed condition

**Status.** Not reached. STOP at step 4. Not filled by mixing the two available conditions.

Available typed conditions on R5, distinct (support review `42,266`; reconciliation R4/R5 collision):

- Frozen marked sections: `A_i(1,0)-A_i(0,0)=0`, `B_i(1,0)-B_i(0,0)=0` for `i=0,1`. Stricter freeze; carry-aware form is erratum (2.3). Unnecessary for Hensel.
- Hensel residue-ball collision: each target ball `(0,b)+109 Z_{109}^2` has one preimage in every source ball `(a,b)+109 Z_{109}^2` (support gate `85–100`). A *consequence* of any exact lift, not a search grammar.

R1-style `(0,0),(1,0)→(0,0)` transported along `ρ` is a third recipe. A later charge must pick exactly one and push it through the map of step 2. Sol’s “collision pair” does not say which (reconciliation §4.8). No collision is declared here.

## 8. Preflight step 8 — image checks

**Status.** Not reached. STOP at step 4. The map `ρ` of step 2 already has seed reduction `ρ(F_(A,B))=(x-x^{109},y)` and packed `det J` (not a residue-unit substitute). Remaining checks, if a cell were frozen: chosen collision holds on the image; the elementary `(12,6)` automorphism `u=x+y`, `v=y+u^6`, `(P,Q)=(u+v^2,v)` is excluded (Jacobian 1, actual `y`-degrees `(12,6)`, `v_{109}(q_6)=0`, not congruent to the AS109 seed; n=6 face `332–351`; prime/4 hostile review claim 7 CONFIRMED). That control occupies the residual numerical type and is not AS109. It is not used here as a stand-in cell.

## 9. Preflight step 9 — do not wrap the cell in `sat()`

**Status.** Not reached. STOP at step 4.

No ideal is licensed by R7 as written (preflight §6.9). If an ideal appeared later: extract the component, assert its ring, run a positive and a negative control (FALLACY-v2 `sat()` wrapping). None is specified. No `sat()` wrapper is proposed.

## 10. Preflight step 10 — floor / attainment

**Status.** Not reached. STOP at step 4.

Binding even without a cell, and already used in §4.1: floor-twelve is a lower bound, not attainment of degree 12 (FALLACY-v2 floor/attainment; floor-twelve scope `40–44`: “supplies no lift, support bound, … routing into an exact degree-twelve cell”). Inconsistency of a future frozen cell would kill that cell only and might raise a bounded frontier only for that declared support. Consistency would not be a characteristic-zero polynomial counterexample and would not be R3’s restricted-analytic limit. Next-level monomials outside a freeze would be fixed-support failure, not a licence to widen the cap.

## 11. Preflight step 11 — computation shape (no execution)

**Status.** Not reached. STOP at step 4. No enumerator, AWS rank job, or desk matrix is charged.

Had steps 1–7 been discharged, this step would spec ring, variables, and expected dimensions without running anything, and would refuse the job if dimensions or fill-in were uncertain (preflight §6 lead-in). Present state: ring would have been `Z_{109}[x,y]` with packed (1.1), or `F_{109}` via `ρ`; variables and dimensions are UNSTATED because exponent sets are UNSTATED. Preflight §6.11 also stops without charging if any of 1–7 is UNSTATED (here: step 4), if a `NO MAP CLAIMED` pair is assumed (none is), or if the job is an unrestricted further Witt level of R3 (not proposed).

No CAS was run. No dimension is estimated. Uncertain dimensions are a reason not to start a cell, not a reason to guess.

## 12. Charge-sheet draft or typed STOP

This lane does **not** deliver a complete matrix charge sheet. It delivers a typed STOP at the first undischargeable preflight step.

```text
STOP[R5-CHARGE / NO-FROZEN-GRAMMAR]
registry_id = R5
name        = AS109-LIFT
step        = 4 of 11
reason      = no finite exhaustive gauge-normal grammar;
              x- and y-support cannot be written as finite exponent sets
next        = coordinator review + different-model audit of this STOP
matrix      = not charged
AWS/desk    = not charged
```

**Discharged (1–3).**

1. Target is R5, not R1–R4, R6–R8, and not a label.
2. Lift ring `Z_{109}[x,y]` with packed (1.1); matrix ring `F_{109}` only as coefficient reduction `ρ` of that packed residual; uncarried `E1,E2` quarantined.
3. Witt level = packed-exact; no finite `n` is compatible with using floor-twelve as a constraint.

**Stopped (4).** Attempted minimal `y`-shapes (two-sided box with `max=12`; residual `n=6`) are floors/strata, not exponent sets. `x`-support is unbounded on every licensed shape (`G_m` family; closed-support `x^{108k}` induction; floor theorems at arbitrary finite `x`-degree). Translation slice `[x^{108} y^0]A=0` is scoped to `deg_x A ≤ 108` and does not section `G_m`. A degree rectangle is an unregistered cap. Historical `NO-FROZEN-GRAMMAR` is dual-confirmed and is not overridden.

**Not reached (5–11).** Generator order, gauge slice as a charged section, one typed collision, remaining image checks, `sat()` ban, floor/attainment discipline for a cell, and computation shape.

**What would reopen the matrix route.** Exactly the new input of §4.5 (finite gauge-normal form with `G_m` section, or a finite coupled closed-support module, plus the translation-slice degree bound if that slice is used). Until that input exists, no enumerator, rank job, or linearized determinant-plus-collision matrix of an R5 cell is chargeable.

**Coordinator / different-model audit asks.** (i) Is packed-exact an admissible discharge of step 3, or does “write `n` in `mod 109^n`” force a STOP at step 3 instead? This draft treats a typed non-truncation as a declaration, not as UNSTATED. (ii) Is residual `n=6` closer to a freeze than the two-sided box? This draft says neither is a finite exponent set. (iii) Confirm that the second charged N-A/ROW-SWEEP file is not a hidden grammar.

No `charge_basis` line is included: this is not an exit-price assertion.

## 13. Sources fetched

No web fetch was required for the STOP. Primary literature used by cited producers is recorded from those producers and was not re-downloaded in this lane. Workspace producers below were hashed with `shasum -a 256` here; they are not the frozen charged inputs of §0.

**Charged frozen inputs (authority for this lane).**

| SHA-256 | file |
|---|---|
| `bb2a3d0753583ef08f78f989e2c9b6a1026652e423f1b2722533274d80ae9a6a` | `as109-d12-seed-provenance-reconciliation-grok46-20260831.md` |
| `126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286` | `block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md` |

**Workspace producers cited (read-only, hashed this lane).**

| SHA-256 | file |
|---|---|
| `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` | `as109-closed-support-gate-20260824.md` |
| `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | `as109-support-gate-20260824.md` |
| `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | `as109-support-gate-20260824-erratum.md` |
| `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | `as109-support-review-grok-20260824.md` |
| `c76f26a6407a0e321da7d7001455819bd9ca92be6cc467afe5045aacc310c9be` | `as109-max11-floor12-composition-opus5-20260826.md` |
| `430ffa3cc25a3141a03062072db4fecab0a3b6250daab3323c7b74194bfb9e84` | `as109-max11-floor12-composition-review-sol-20260826.md` |
| `696152da19bf48091242064c8c506a06591ebba4e2b16b2314283bc6aeb54e2f` | `as109-one-sided-target-degree-tri-promotion-sol-20260827.md` |
| `3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36` | `as109-one-sided-prime4-composition-sol-20260827.md` |
| `bc13662108e6521ed2ea63a4840b13fd14e0e0b3a6e939caffefea6097958bea` | `as109-one-sided-prime4-composition-hostile-review-grok-20260827.md` |
| `7640715607c640beae845855feb261a0d207ea9409a1ccf8a915899f4461ec10` | `as109-n6-top-two-y-bands-face-isolation-grok-20260827.md` |
| `571c5e2bda00cf9221debcd43b26f635016a68622714bbf8bbb0e2a68f33525f` | `as109-n6-top-two-y-bands-face-isolation-hostile-review-sol-20260827.md` |
| `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | `as109-quadratic-coupling-gate-20260824.md` |
| `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | `as109-cubic-coupling-gate-20260824.md` |
| `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | `as109-quartic-discriminator-gate-20260824.md` |
| `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | `as109-sextic-frontier-preflight-20260824.md` |
| `60e198036854cce58a74e30a11db4df20d62e10e31b61f2a698c93a1594736b0` | `ideation-20260827T0145Z-opus5.md` |
| `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | `as109-bounded-polar-conductor-gate-20260824.md` |
| `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | `as109-bounded-polar-conductor-review-grok-20260824.md` |
| `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | `as109-wild-symplectic-conductor-gate-20260824.md` |
| `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | `as109-wild-symplectic-conductor-review-grok-20260824.md` |
| `c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2` | `witt-tate-control-20260824.md` |
| `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` | `FALLACY-v2.md` |

Support-gate SHA `b73aefd1…` and erratum SHA `ca8a549c…` match the hashes already recorded in the one-sided floor-six composition (`137–148`). Prime/4 composition SHA `3d6d09fd…` and its hostile-review SHA `bc136621…` match the n=6 face history table.

**Primary literature (cited by producers; not re-fetched this lane).** Vered Moskowicz, *A variation on Magnus' theorem and its generalizations*, arXiv:1810.08202v2 (2018), Theorem 2.7. Producer-recorded SHA-256 of `https://export.arxiv.org/e-print/1810.08202v2`: `ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419` (prime/4 composition `92–96`). Consumed only as the already-composed one-sided floor; this lane does not re-prove Theorem 2.7.

## 14. FALLACY-v2 compliance notes

- **Flag/place/series.** Not used. No exit-set, cv flag, or cover series is identified.
- **Per-ray/exit-set.** No exit claim.
- **Carrier/attainment.** `REPRESENTATIVE` is not treated as `FULL_ACTUAL_EXIT`. Floor-twelve is a floor.
- **Pole/interior.** Polar divisor `E_p=V(D)` is cited only as the polar-gate statement that `Φ_F` is unbounded analytic, not as an R5 polynomial identity.
- **Floor/attainment.** Applied at step 4: `≥12` and `deg_y Q ≥6` are lower bounds. Equality is not assumed. Residual `n=6` is a stratum, not attainment of a unique bidegree.
- **`sat()` wrapping.** No ideal. Step 9 not reached.
- **Raw remainder degree.** No normal-form remainder computed.
- **Variable/ring map.** Lift ring, matrix ring, and `ρ` are declared at step 2. Nearby `Q1`-first / `s`-first orders are refused as maps at step 5.
- **Prime label/derivative.** `p=109` is the prime. `A_x`, `B_y` are derivatives as defined in closed-support (1.1). Registry ids R1–R8 are labels of distinct objects, not derivatives.
- **Merge-free/M-descent.** Not used. The Nori/ROW-SWEEP residual class is not identified with R5.
- **Target/arrival index.** R5 is the target. Incoming N-A residual indices and R8 `(8,12)`/`(9,12)` are not arrival data for this cell.

No gap was filled by cap or analogy. The missing grammar is typed `NO-FROZEN-GRAMMAR`, not an invented rectangle. No `charge_basis` line: this report asserts no new exit price.

This is a preparation-lane STOP for coordinator review and different-model audit. It is not a promotion, not a nonexistence theorem for R5, and not a JC2 result.

<!-- BODY-END -->
