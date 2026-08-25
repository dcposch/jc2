# Hostile different-model review — AS F-only D7 degree-one influence on three displayed Q3 fibres

| Field | Value |
|---|---|
| Claim under review | Frozen V2 producer: at each of three pinned Q5 predecessor points `base0000`, `base0270`, `base0513`, consume the entire reviewed Q3 affine fibre and the selected homogeneous degree-3/2 order-27 and order-81 digits, then add every homogeneous degree-one output digit `27(W1,Z1)+81(H1,J1)`; the literal integer Jacobian, after exact `/27` then `/81` on the fixed 91-slot inventory, yields a rank-6 ten-coordinate first carry with exactly 81 accepted assignments, a branchwise affine `/81` map on every inactive coordinate, and an inconsistent system on all 243 branches, with row 8 (`x^2 y`) identically zero in the remaining variables and residual constants `2,2,1` |
| Overall verdict | **CONFIRMED** |
| Finite displayed-family theorem (degree-3/2/1 blocks) | **CONFIRMED** |
| Completeness of all degree-at-most-three derivative effects | **FAILED** as a source-complete cone (higher-degree order-27 digits, source reparametrization, and other carry directions that can still move a `/27` or `/81` row are not in the compiler). The theorem stops at the explicitly displayed blocks |
| Affine-output lemma as global coverage | **FAILED** as a promotion (the lemma normalizes a genuine complete `Z_3` determinant-one map somewhere in a full normalized scheme; it does not identify these three incomplete pinned fibres with that scheme) |
| Strongest licensed scope | displayed homogeneous degree-3, degree-2, and degree-one order-27 and order-81 output digits, together with derivative-zero constants, over the entire displayed Q4/Q3 fibre of three fixed Q5 predecessor *points*; not complete Q3-fibre exclusion; not three structural bases; not 79→76; not global predecessor-scheme coverage |
| Replay/custody | **CONFIRMED** of the frozen Box02 V2 run recorded below (non-blocking `OUTPUT.sha256` self-hash / snapshot noise, identical in kind to the Q3 parent and Gaussian V2 reviews; not used as mathematical evidence). `replay_all_v2.sh` was not re-launched. This review hashed and parsed frozen artifacts with host Python; it did not re-execute the integer Jacobian compiler |
| Smallest failing identity | none inside the displayed degree-3/2/1 family |
| Smallest missing hypothesis | a source-complete derivative-effect theorem, or a chart-composition theorem identifying every relevant incomplete predecessor fibre with one of these three, would be required to promote beyond the displayed blocks. Both are **missing** |
| Evidence tier | source reconstruction of `P_x Q_y - P_y Q_x - 1` over `Z`; exact `/27` and `/81` before `% 3`; fixed 91-slot order with row 8 = `x^2 y`; whole Q3-kernel parametrization retained; 63 over-cap slots retained among the 91; ten-column first-carry cone, rank 6, `3^4` enumeration, 81 accepted; quadratic design `1+2n+C(n,2)` = 1326/1128 then 861/703 with both `2e_i` and `e_i+e_j`; frozen sparse degree-one support plus per-branch matrix/RHS SHA-256; rank lift `5→6` and `/81` lifts `6,7,7 → 7,9,9` as the unused-variable negative control |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` |
| Review constraint | no producer/case/ledger/prompt edits; no AWS re-launch; no local Jacobian replay. Frozen JSON, stdout, and source were hashed and parsed |
| Review window (UTC) | 2026-08-25 |

Producer report, V2 freeze, V2 JSON, V1 source (byte-identical freeze), Q3 parent producer, CONFIRMED Q3 parent review, CONFIRMED_WITH_REPAIRS Gaussian selected-family review, affine-output normalization lemma, and the hash-pinned compiler anchors were reread in full before any verdict. No producer, case, prompt, parent, or ancestry file was edited.

---

## Required decisions

### Finite displayed-family theorem (degree-3/2/1)

**Correct.** On the displayed homogeneous degree-3, degree-2, and degree-one order-27 and order-81 family, over the entire displayed Q3 affine fibre of each of the three pinned Q5 predecessor points, the compiled `/27` then `/81` tower is exhaustive for those coordinates, affine on each accepted branch, and inconsistent on all 81 branches per parent (`3 * 81 = 243`). The `/243` layer is never reached. Row 8 is a genuine remaining-variable obstruction with residual constants `2,2,1`. Added degree-one columns are source-present and mathematically active at both layers, and they never hit row 8.

### Completeness of the degree-at-most-three derivative-effect inventory

**Failed as a source-complete cone.** Inside the *displayed output-digit blocks* the inventory is the full homogeneous degree-≤3 package at orders 27 and 81, with constants omitted for an algebraic reason. That is not a proof that every source, reparametrization, nonhomogeneous-at-another-order, or degree-≥4 order-27 direction that can affect a `/27` or `/81` row is present. The theorem stops at the explicitly displayed blocks. The producer body already stops there; this review reimposes the stop rather than repairing a title.

### Affine-output lemma as global coverage

**Failed as a promotion.** The lemma licenses a normalized *complete-map* chart. It does not turn an incomplete pinned Q3 fibre into a normalized determinant-one map, and it does not identify an arbitrary incomplete predecessor fibre with one of these three points. The three points do not become the global predecessor scheme by composition with the lemma.

### Strongest licensed scope after those decisions

Three **fixed Q5 predecessor points** (`base0000`, `base0270`, `base0513`), each with its entire displayed Q4 affine fibre and entire displayed Q3 affine fibre, excluding every accepted first-carry branch of the **displayed** homogeneous degree-3, degree-2, and degree-one order-27 and order-81 output digits, including all 63 over-cap slots of degrees 7–12 among the 91 rows. Constants are excluded because their derivatives vanish identically. This does not exclude three whole structural bases, does not reduce the 79-base remainder to 76, does not cover the rest of the accepted global Q5/Q4/Q3 predecessor scheme, and does not exclude omitted source directions.

### Source, arithmetic, coverage, or custody defects

- **None load-bearing.** The producer body’s displayed-family hedge, lemma firewall, and refusal list match the licensed object.
- **Non-blocking custody:** each AWS `OUTPUT.sha256` records a self-hash taken while the file was being written, and snapshots `launcher.stdout` as empty; the later `MANIFEST_V2.sha256` hashes the final files. Identical in kind to the Q3 parent and Gaussian V2 reviews. Not used as mathematical evidence.
- **Non-blocking custody:** the Box02 V2 deployment staged V2 source bytes under the legacy filename `audit_degree1.py` and invoked the V1 runner. The staged source hash is exactly the V2 hash `219b1038…`. Local `audit_degree1.py` remains the V1 freeze `a225182d…`. The mathematical core of V1 and V2 is the same; V2 only adds slot asserts and sparse degree-one support metadata.
- **Non-blocking software:** the independent verifier checks frozen JSON structure, histograms, and stored sparse degree-one support. It does not rebuild the Jacobian and does not re-rank a stored dense matrix (dense `/27` and `/81` matrices are not serialized; only SHA-256 plus sparse added-column support). The AWS producer is the Jacobian-level certificate. This is weaker packaging than Gaussian V2’s stored dense matrices, not a false theorem.
- **Not a defect:** `kernel_dimension: 0` on every `/81` branch is `rref_solve` returning an empty kernel on a contradictory system, not a consistent full-rank kernel. `consistent_branch_count` is the survivor statistic.

### Independent replay

Not re-launched. Frozen Box02 command and hashes are recorded in the custody section below.

---

## Promotion

**Accept `AT EACH OF THREE PINNED Q5 PREDECESSOR POINTS, THE ENTIRE REVIEWED Q3 AFFINE FIBRE PLUS ALL DISPLAYED HOMOGENEOUS DEGREE-THREE, DEGREE-TWO, AND DEGREE-ONE ORDER-27 AND ORDER-81 OUTPUT DIGITS HAS AN EXACT RANK-6 TEN-COORDINATE /27 CARRY WITH 81 ACCEPTED ASSIGNMENTS; ON EVERY ACCEPTED BRANCH THE /81 MAP IS AFFINE ON THE REMAINING INACTIVE CUBE AND INCONSISTENT, WITH ROW 8 (x^2 y) IDENTICALLY ZERO IN THE REMAINING VARIABLES AND RESIDUAL CONSTANTS 2, 2, 1. ADDED DEGREE-ONE COLUMNS ARE SOURCE-PRESENT AND MATHEMATICALLY ACTIVE AT /27 AND /81, ALTER NON-ROW-8 EQUATIONS AND RANKS, AND NEVER HIT ROW 8.`**

**Refuse `COMPLETE Q3 FIBRE EXCLUSION`, `SOURCE-COMPLETE DEGREE-AT-MOST-THREE DERIVATIVE-EFFECT CONE`, `LEMMA-MEDIATED GLOBAL NORMALIZED-CHART COVERAGE`, `THREE STRUCTURAL BASES EXCLUDED`, and `79-BASE REMAINDER REDUCED TO 76`.**

On the aligned F-only `D=7` chart, after the CONFIRMED Q3 whole-kernel gate and the CONFIRMED selected-family Gaussian gate:

- Over `Z`, the compiled map is
  `P = P_Q3 + 27(W_3+W_2+W_1) + 81(H_3+H_2+H_1)`,
  `Q = Q_Q3 + 27(Z_3+Z_2+Z_1) + 81(J_3+J_2+J_1)`,
  with every subscript a homogeneous binary form of that total degree, and with `P_Q3,Q_Q3` running over the full Q3 affine fibre (`q3_particular + F_3`-span of `q3_kernel`), not a single particular. Constant output digits are omitted because their partial derivatives vanish identically.
- The Jacobian orientation is the parent integer determinant
  `P_x Q_y - P_y Q_x - 1`,
  obtained transitively from `replay_full_q4_restore.py` via `solve_full68.py` and `solve_q3.py`. Axis 0 is the `x`-exponent. Every coefficient is divided exactly by 27 or 81 *before* reduction modulo 3.
- The 91-slot order is
  `slots = [(i, d-i) for d in 0..12 for i in 0..d]`,
  i.e. `[x^i y^{d-i}]`. Length `1+2+…+13 = 91`. Degrees 7–12 contribute `8+9+10+11+12+13 = 63` over-cap rows, all retained at both `/27` and `/81`. Degree 3 occupies indices 6–9; **row 8 is `(2,1) = x^2 y`**.
- Fresh degree-one digits are 8 coordinates (two each for `W1,Z1,H1,J1`). Raw dimension is `q3_kdim + 28 + 8`, hence 50, 46, 46. The `/27` matrix has exactly ten nonzero columns: the selected-family eight
  `w3_1,w3_2,z3_1,z3_2,w2_1,w2_2,z2_0,z2_1`
  plus the two trace columns `W1_x` and `Z1_y`. Stored `active_raw_columns` are `[15,16,19,20,23,24,25,26,43,44]` at `base0000` and `[11,12,15,16,19,20,21,22,39,40]` at the other two. Rank 6, so `3^{10-6} = 81` accepted assignments. Branching on those 81 and retaining every inactive coordinate is exhaustive for this family.
- After the first carry is fixed in raw coordinates (not an RREF wrap of the `/27` kernel), mixed and pure quadratic remainders of remaining digits at `/81` have 3-adic valuation at least 6, so the restricted map is at most affine. The compiler proves affineness by origin, both nonzero multiples `2e_i`, and every pair sum `e_i+e_j`. Design counts are `1+2n+C(n,2)`: 1326 at `n=50`, 1128 at `n=46` for `/27`; 861 at `n=40`, 703 at `n=36` for `/81`.
- Every one of the 243 branch systems is inconsistent. Row 8 of every `/81` matrix is the zero vector, so the residual is independent of every remaining displayed coordinate. Frozen constants are `2,2,1`. Because row 8 is identically zero, no `/243` successor exists inside these displayed fibres.
- Negative control: the two `/27` trace columns occur in row 0 with coefficient 1 each, lift selected-family rank 5 to 6, and lift 27 accepted assignments to 81. At `/81`, every branch has nonzero added-degree-one columns (exactly 3 on `base0000`, 4 on each other parent) hitting `[1]`, `[xy]`, and on two parents `[x^3]`, never row 8. Correspondingly `/81` ranks lift from selected-family `6,7,7` to `7,9,9`. An implementation that merely appended unused variables would not change those ranks.

**Do not promote this to:** a source-complete Q3-fibre exclusion; a theorem that degree-≥4 order-27 digits, source reparametrizations, or other carry directions are absent; lemma-mediated coverage of the global normalized predecessor scheme; exclusion of three whole structural bases; a reduction of the 79-base remainder to 76; a complete map modulo 243; an all-depth lift; a counterexample; or JC2.

**Smallest honest successor.** Keep the displayed-family theorem. A promotion beyond these three fibres requires an additional chart-composition theorem, and a promotion to complete fibre exclusion on even one fibre requires a source-complete derivative-effect inventory (or a theorem killing the omitted directions without moving `[x^2 y](det J-1)/81`). Do not treat the affine-output lemma as that theorem.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as complete exclusion of a Q3 fibre, or as the complete normalized derivative-effect cone of degree at most three;
- this gate as a proof that source reparametrizations, degree-≥4 order-27 output digits, or other omitted carry directions cannot move a `/27` or `/81` row;
- the affine-output normalization lemma as identifying these three incomplete fibres with a full normalized complete-map chart, or as exhausting the global predecessor scheme;
- this gate as exclusion of three whole structural bases, or as reducing 79 remaining bases to 76;
- coincidence of the label `0513_0201000` with the later 79-base SAT survivor on structural digits `0201000` as an identification of model bytes (consumed model SHA-256 `9c319fe4…` is not the later survivor `e857efac…`);
- this gate as a complete determinant-one map modulo 243, an all-depth lift, a characteristic-zero point, a counterexample, or JC2;
- two-level V1 `solve_two_level.py` as an affine `/81` theorem (its canonical RREF wrap remains the negative control that `/81` is nonlinear in those coordinates, which is why this successor retains raw inactive digits);
- V1 `audit_degree1.py` JSON hashes as the V2 freeze (V1 is the same mathematics without support metadata; the portable freeze and verifier pin V2).

---

## Hostile checks

Tried hard, and failed, to flip the Jacobian orientation; to reduce modulo 3 before exact division by 27 or 81; to make the 91-slot order anything other than `[x^i y^{d-i}]` for `d=0..12`; to make row 8 be `x y^2` or `x^3`; to replace the whole Q3 kernel by a single particular; to drop the 63 over-cap rows from the 91-row `/27` or `/81` inventories; to overwrite or omit the degree-3/2 blocks when adjoining degree one; to omit a homogeneous degree-one monomial at order 27 or 81; to find a first-carry active set other than the old eight plus the two trace columns, a `/27` rank other than 6, or an accepted-assignment count other than 81; to make branching on the ten active coordinates while freezing inactive coordinates to zero miss an affine `/27` solution; to omit the pure `2e_i` tests or the mixed `e_i+e_j` tests, or to mismatch design counts 1326/1128 and 861/703; to make added degree-one columns identically zero, or to find them in row 8; to find a `/81` rank pair other than `7/8`, `9/10`, `9/10`, a row-8 constant other than `2,2,1`, or a survivor; to treat constants as a gauge rather than an algebraic vanishing of derivatives; to read the affine-output lemma as covering these three incomplete fibres; or to read three predecessor *points* as three structural bases, as the 79-base scheme, or as a 79→76 reduction.

### 1. Parent pin, orientation, indexing, three model files

Transitive compiler pins (V2 `SOURCE_MANIFEST_V2.sha256` / `MANIFEST_V2.sha256`, recomputed on the host):

| object | SHA-256 |
|---|---|
| V2 `audit_degree1_v2.py` | `219b1038e7e6779220795d2f9d4acab73d6d482d061c7a0fe01c05fdcebe8554` |
| V2 `verify_outputs_v2.py` | `3bc77959afd3eeefa94725cce01e27414f5f1da737131eb470bd05d01ed2681c` |
| V2 `run_remote_v2.sh` | `f762597271c963592ba9421d1204c3a94ac0a97c5e98e297440c7fd59a173a0a` |
| V2 `replay_all_v2.sh` | `890d6d69d0cb8a9a177d3d585fe3e94dc977dba65777120d0cc6ba6084b14b73` |
| V1 `audit_degree1.py` | `a225182dd8bd90af05b9c5fb2427191008e4de55ceea99c7a77284fa2abe4c0c` |
| V1 `run_remote.sh` | `65e8b7301d722ff371e59bff54d615f5130555ad68c2c2871c88c317dc4bda55` |
| two-level `solve_two_level.py` | `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd` |
| Q3 `solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| Q4 `solve_full68.py` | `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4` |
| Q4 restore `replay_full_q4_restore.py` | `9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c` |
| Q3 different-model review | `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` (`CONFIRMED`) |
| Gaussian different-model review | `47eaa4b7f850e8974a27f83cd1d2328d04e8a54dd359c7716611daea4b287e8e` (`CONFIRMED_WITH_REPAIRS`; selected family) |
| affine-output lemma | `cae83192932d09ad6fc43be2440cfbde09fc78f6e1cb3136cf1e80afdbcf4b9b` |
| V2 preregistration | `d42734629549332c2f01b3db7ff521def0cd00d5bcd005ae3dfd56640dd7aed2` |

`audit_degree1_v2.py` SHA-pins `solve_two_level.py` at `cec50f9f…` and `exec`s the unique prefix before `stages = []`. That prefix SHA-pins and `exec`s `solve_q3.py` before building any Q2/Q1 row. The Q3 parent SHA-pins the Q4 68-row gate, which SHA-pins the Q4 restore that *defines*

```text
det J - 1 = P_x Q_y - P_y Q_x - 1
```

with `nderivative(·,0) = ∂/∂x` on monomials `(i,j) = x^i y^j`. Every `exec` asserts the child SHA before compile.

`homogeneous_numeric(d, c)` is `{(i, d-i): c_i}`, matching the slot convention. The three consumed SAT models are the same Boolector endpoints already confirmed by the Q3/Q4/Gaussian reviews:

| point | model SHA-256 | regenerated `q3_parent.json` SHA-256 | Q3 kernel dim |
|---|---|---|---:|
| `base0000` | `dbb405ac9ab12b9d4b01df6e934ac6979609dfd4eabbe2ccf65a65aaf8cdcb81` | `89c9b8bfb4c46b566e10e7f5716502b0a3b6f64af29a5f4e14234cc09b945187` | 14 |
| `base0270` | `05627048aa3e648b975acc1ed47e97a451241c3544e7fa5b58a7c42a1cd4be03` | `9016e7737c7f3a31107a80f4da91e1e8cec7be686569cd548e55e135fcec4dfb` | 10 |
| `base0513` | `9c319fe4d1a576569869cbccbcc7411fee5eb12dedaa4e6a820a395263820200` | `e2711128f358f5b65f215a2898ccf90fa10a7e1e6908ccdde7c9a4410290b4bb` | 10 |

Each is one Q5 predecessor *point*. The Q3 JSON bytes regenerated on Box02 match the Q3 producer output hashes used by Gaussian V2. They are not whole structural bases.

### 2. Successor adds exactly the homogeneous degree-one blocks

Parent `raw_candidate` still builds

```text
P = P_Q3 + 27(W3+W2) + 81(H3+H2),
Q = Q_Q3 + 27(Z3+Z2) + 81(J3+J2)
```

from `values[:base_raw_n]`, with the Q3 fibre in the first `q3_kdim` coordinates and the 28 degree-3/2 digits after that. The successor does not rewrite that function. It calls it, then

```text
P += 27 W1 + 81 H1,   Q += 27 Z1 + 81 J1
```

with `W1,Z1,H1,J1 = homogeneous_numeric(1, extra[2k:2k+2])` for `k=0,1,2,3`. Degree one has exactly the monomials `y` and `x`, so those eight coordinates are all homogeneous linear forms at the two orders. `nadd` does not overwrite the degree-3/2 or Q3 blocks. Frozen JSON records `base_raw_variable_count` 42/38/38 and `extended_raw_variable_count` 50/46/46, and `added_degree1_raw_columns` exactly `range(base_raw, base_raw+8)`.

The `/27` active set is the selected-family eight columns plus the two new trace columns. The old eight are not dropped.

### 3. Ninety-one-slot inventory and exact division

V2 asserts `len(slots)==91` and

```text
slots == [(i, total-i) for total in range(13) for i in range(total+1)]
```

before any row is built, and `slots[8]==(2,1)`. Frozen JSON stores that list; slot 0 is `[0,0]`, slot 8 is `[2,1]`, slot 90 is `[12,0]`. Degree 0 is present. Degrees 7–12 contribute 63 slots. Both `/27` and `/81` iterate the full 91-list.

`rows` refuses any coefficient not divisible by the divisor, then reduces modulo 3. AWS return code 0 on all three lanes means no divisibility assertion fired. This review did not inspect the integer coefficients by a second Jacobian; the exact-division claim is source-plus-fail-closed-execution.

### 4. Chronology, exhaustive 81, inactive retention, affinity premise

Order of operations in source:

1. `extract_affine` of all `raw_n` coordinates at `/27` (design includes inactive columns);
2. `rref_solve` of the full `/27` system, consistent of rank 6;
3. restriction to nonzero columns (ten), re-solved at the same rank;
4. enumeration of the entire active kernel, `3^4 = 81` assignments, each replayed at `/27` with inactive digits set to 0;
5. for each assignment, `extract_affine` of *every* inactive raw coordinate at `/81`, then `rref_solve`.

Because inactive `/27` columns are identically zero and the `/27` map is affine, setting them to 0 while enumerating the active kernel is the full `/27` solution set. Retaining those coordinates as `/81` variables is the full remaining cube of the displayed family: 40 coordinates at `base0000`, 36 at the others. No RREF representative of the `/27` kernel is substituted.

Affinity premise, audited rather than assumed:

- `P` and `Q` are affine in every displayed coordinate (Q3 kernel coordinates enter affinely through `q3_candidate`; W/Z/H/J of degrees 3,2,1 are added linearly).
- `det J` is bilinear in `(P,Q)`, hence at most quadratic in the displayed coordinates.
- Over `F_3`, `extract_affine`’s tests of `2e_i` and `e_i+e_j` kill every quadratic monomial. Cubics in displayed coordinates cannot appear in a bilinear determinant of affine maps.
- Remaining-remaining products after the first carry have valuation at least 6 (`27^2`, `27·81`, `81^2`), hence vanish modulo 3 after `/81`. Mixed active-inactive products at two order-27 scales are `729/81=9 ≡ 0`, which is why all 81 branches of a parent share one `/81` matrix SHA-256 and differ only in RHS.

Frozen design counts match `1+2n+C(n,2)` exactly: 1326, 1128, 861, 703.

### 5. Rank pairs, 243 branches, row 8, constants, zero survivors

Reproduced from frozen JSON and producer stdout (not from a second RREF of dense matrices):

| parent | vars before/after | `/27` rank/aug | active | accepted | `/81` rank/aug | design `/27`,`/81` | row-8 constant | survivors |
|---|---:|---|---:|---:|---|---|---:|---:|
| `base0000` | 42 / 50 | 6 / 6 | 10 | 81 | 7 / 8 | 1326, 861 | 2 | 0 |
| `base0270` | 38 / 46 | 6 / 6 | 10 | 81 | 9 / 10 | 1128, 703 | 2 | 0 |
| `base0513` | 38 / 46 | 6 / 6 | 10 | 81 | 9 / 10 | 1128, 703 | 1 | 0 |

`3 * 81 = 243` branches. Every branch has `row8_nonzero_raw_columns == []` and `consistent == false`. Slot 8 is `[2,1] = x^2 y`. The `/81` matrix SHA-256 is unique per parent (the linear map on inactive coordinates does not depend on the accepted active assignment); row-8 constants are invariant on each parent’s 81 branches, while other RHS rows vary (54 distinct RHS SHA-256 values at `base0000`, 81 at each other parent). That is the invariant singleton obstruction.

### 6. Negative control: added columns are used, and they miss row 8

Not an unused-variable append.

At `/27`, the only added nonzero columns are the trace pair (`43,44` or `39,40`). Each is supported solely on row 0 with coefficient 1. Those two columns are equal as vectors, so they add exactly one rank: selected-family rank 5 becomes 6, and `27 * 3 = 81` accepted assignments. Order-81 linear digits are correctly invisible at `/27` (`81/27 = 3 ≡ 0`).

At `/81`, frozen sparse support of inactive added columns, identical on all 81 branches of a parent:

| parent | columns (raw) | names | rows hit |
|---|---|---|---|
| `base0000` | 42, 47, 48 | `W1_y`, `H1_x`, `J1_y` | 4 `[xy]`; 0 `[1]`; 0 `[1]` |
| `base0270` | 38, 41, 43, 44 | `W1_y`, `Z1_x`, `H1_x`, `J1_y` | 4 `[xy]`; 9 `[x^3]` coeff 2; 0 `[1]`; 0 `[1]` |
| `base0513` | 38, 41, 43, 44 | `W1_y`, `Z1_x`, `H1_x`, `J1_y` | 4 `[xy]`; 9 `[x^3]` coeff 1; 0 `[1]`; 0 `[1]` |

No stored degree-one support entry has `row_index == 8`. `/81` ranks lift from selected-family `6,7,7` to `7,9,9`. Trace columns `W1_x,Z1_y` are already fixed by `/27` and are therefore not `/81` variables; the remaining shears and the order-81 trace hit `[xy]`, `[x^3]`, and `[1]`, not `[x^2 y]`. The Gaussian selected-family “in principle” threat that order-27 linear digits can move row 8 is empirically false *on these three fibres*, as a displayed-family fact, not as a gauge theorem.

The sparse support is extracted from the compiled matrices by the producer and frozen; dense matrices are not stored. Rank change plus nonzero stored entries is enough to fail the unused-variable test.

### 7. Constants are algebraically absent

`det J = P_x Q_y - P_y Q_x`. A constant added to `P` or to `Q` does not change any derivative, at any modulus, including `/27` and `/81`. Exclusion from the variable list is that identity, not a normalization assumption, and not an application of the affine-output lemma.

### 8. Completeness of the degree-at-most-three derivative-effect inventory

Inside the displayed *output* blocks the package is complete for homogeneous degree ≤ 3 at orders 27 and 81:

- degree 3 and 2: parent 28 coordinates, all monomials of those degrees;
- degree 1: successor 8 coordinates, all monomials of that degree;
- degree 0: omitted, and licensed by §7;
- nonhomogeneous degree ≤ 3 is the sum of those homogeneous pieces.

That is not a source-complete inventory of every effect that can move a `/27` or `/81` row. Directions that remain uncompiled include at least:

- homogeneous degree ≥ 4 at *order 27* (derivatives have degree ≥ 3 and hit the same `/27` degree-3 rows that contain row 8; the Q3 parent already contains order-81 degree 4 as `(H4,J4)`, which is not the same digit);
- source reparametrizations `x ↦ x + 27 L + …`, whose first-order output image is only partly inside the displayed output cone;
- other 3-adic orders and carry directions not in the displayed Q3 fibre plus these 36 fresh coordinates.

Cross-order *products of displayed digits* are in the bilinear determinant and are controlled by the quadratic design plus valuation. Completeness beyond the displayed blocks is not source-licensed. The theorem stops there.

### 9. Affine-output lemma versus the global normalized predecessor chart

The lemma is correct for a genuine complete map `F` with `det JF = 1` over `Z_3` or `Z/3^n Z`: `G = A^{-1}(F-c)` has `G(0)=0`, `JG(0)=I`, the same AS special fibre, and the same determinant equation, and postcomposition preserves a common total-degree cap. The F-only `D=7` gate meets that support condition.

The three displayed states are incomplete: degrees 1 and 2 of `det J-1` still begin at valuation 3 on the Q3 parent, and this successor only excludes a displayed digit family at `/27` and `/81`. The lemma’s hypothesis `det JF = 1` is not met, so the lemma does not produce a normalized complete representative of these fibres. Even the weaker 0-jet operation `F ↦ A^{-1}(F-c)`, which uses only `(det JF)(0)=1`, does not identify an arbitrary incomplete predecessor fibre with `base0000`, `base0270`, or `base0513`, and does not exhaust the 79-structural-base global chart.

Label collision is not identification: the later global-predecessor SAT survivor on structural digits `0201000` has model SHA-256 `e857efac…`; the consumed Q5 point `base0513` has `9c319fe4…`.

### 10. Scope

Maximum promotable claim without an additional chart-composition theorem: exclusion of the displayed homogeneous degree-3, degree-2, and degree-one order-27 and order-81 output-digit families, with derivative-zero constants, over the three pinned predecessor fibres named above.

Refused: whole structural-base exclusion; global predecessor-scheme coverage; `79 → 76`; all-depth lifting; a complete map modulo 243; a counterexample; JC2.

The producer refusal list already says this. It is hereby reimposed.

---

## Frozen AWS producer replay (not re-launched)

Host `ip-172-30-0-186` (Box02). Job `/home/ubuntu/jobs/as_q3_q2q1_degree1_influence_20260825T1343Z_v2`. `JC2_ROOT` on the box was the staged closure `…/source`. All three lanes have `start_utc` `2026-08-25T13:41:58Z` (`DEPLOY_START_UTC` `2026-08-25T13:41:55Z`). VM cap `ulimit -v 33554432` KiB (32 GiB); observed max RSS 21732 / 21720 / 21748 KiB. Producer stderr is GNU `time -v` resource custody, exit status 0. Verifier stderr is the same kind of resource custody.

The staged command invoked `audit_degree1.py` (legacy filename) with V2 bytes `219b1038…` under runner `65e8b730…`.

| base | wall (start→end) | user s | max RSS KiB | producer stdout SHA-256 | JSON SHA-256 |
|---|---|---:|---:|---|---|
| 0000 | 13:41:58Z – 13:43:03Z | 64.93 | 21732 | `4e3caed7369809c67755add4ee0ea4386aa1097bb21b824f0c831da05c4f0d33` | `9afa22f0c886bab3d5a2f4dbeb0f81c0e309b0cf0065fb360abe49c0ae2acf0f` |
| 0270 | 13:41:58Z – 13:42:51Z | 53.28 | 21720 | `fe4d027e2601d4bd35e9fd45953a896e40280a8b6e3fea41bf5c8313621d0d9b` | `d9a96fb1962e0505d2eab2acd53ac7c9f072725a3201c7ad89016aff4236f12d` |
| 0513 | 13:41:58Z – 13:42:53Z | 54.89 | 21748 | `5ace63a7cadd2f73be4b730c0cf461bb0170c28cbc0deed2ad21a65c70311293` | `6ad3142aff123e5fbc01aa77c56295119a5d3f16d2eb6c5c71785d826d6baa27` |

Each producer stdout is `stage1_rank 6`, the ten-column active list above, `accepted 81`, one `/81` rank pair, `row8_constants` a singleton, `row8_nonzero_columns [(0, 81)]`, `consistent_branches 0`, the JSON SHA, and `PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-AUDIT`. All three `audit.rc` values are `0`.

Independent output verifier on the same box: `verify_v2.rc` `0`, stdout SHA-256 `77b52eeaef50210b4260ca194d891de10a90b8a4b42cbb8ebfccba78f047389b` (`PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-OUTPUT-VERIFY-V2`), stderr SHA-256 `684d674b5c2337a157e50c762944a692cb9d57c629a9784983658f70fc740ee1`.

Portable AWS replay from a staged repository closure (not executed by this review):

```bash
export JC2_ROOT=/path/to/jc2
export OUTPUT_ROOT=/path/to/fresh/output
bash "$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/replay_all_v2.sh"
```

`replay_all_v2.sh` re-runs `run_remote_v2.sh` on the three frozen Gaussian-exclusion models and then `verify_outputs_v2.py`, which demands the three JSON SHAs above plus the PASS string.

---

## Consumed hashes (recomputed on the host for source and freeze; AWS output hashes from frozen files)

| path | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-q3-q2q1-degree1-influence-producer-20260825.md` | `36e3d5e141ca48a1a23e07a7f179666456ad91b1bd69efdc6f473bc0a5fc5a16` |
| `xmodel/as-fonly-d7-q3-q2q1-degree1-influence-review-grok-20260825-prompt.md` | `9c88e99be306846b0f52962c5a8b2e8146670049097629bb51216654002630d5` |
| `xmodel/as-fonly-linear-normalization-lemma-20260825.md` | `cae83192932d09ad6fc43be2440cfbde09fc78f6e1cb3136cf1e80afdbcf4b9b` |
| `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/PREREGISTRATION.md` | `d42734629549332c2f01b3db7ff521def0cd00d5bcd005ae3dfd56640dd7aed2` |
| `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/audit_degree1_v2.py` | `219b1038e7e6779220795d2f9d4acab73d6d482d061c7a0fe01c05fdcebe8554` |
| `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/verify_outputs_v2.py` | `3bc77959afd3eeefa94725cce01e27414f5f1da737131eb470bd05d01ed2681c` |
| `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/run_remote_v2.sh` | `f762597271c963592ba9421d1204c3a94ac0a97c5e98e297440c7fd59a173a0a` |
| `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/replay_all_v2.sh` | `890d6d69d0cb8a9a177d3d585fe3e94dc977dba65777120d0cc6ba6084b14b73` |
| `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/audit_degree1.py` | `a225182dd8bd90af05b9c5fb2427191008e4de55ceea99c7a77284fa2abe4c0c` |
| `cases/as_fonly_d7_q3_two_level_q2_q1_20260825/solve_two_level.py` | `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-review-grok-20260825.md` | `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` |
| `xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-review-grok-20260825.md` | `47eaa4b7f850e8974a27f83cd1d2328d04e8a54dd359c7716611daea4b287e8e` |

---

## Classified issues

| class | load-bearing? | issue |
|---|---|---|
| mathematical | no | none inside the displayed degree-3/2/1 family |
| source-typing | no | parent `exec` prefix, orientation, slot convention, and homogeneous degree-one width all match the consumed Q3/Q4 chain |
| software | no | independent verifier is structural; dense matrices are not stored. AWS producer remains the Jacobian-level certificate |
| software | no | `kernel_dimension: 0` on inconsistent `/81` branches is the contradiction return of `rref_solve` |
| custody | no | `OUTPUT.sha256` self-hash / empty `launcher.stdout`, identical in kind to parent reviews |
| custody | no | Box02 staged V2 bytes under the V1 filename; hashes match V2 |
| wording/scope | no | completeness of all degree-≤3 derivative effects, and lemma-mediated global coverage, are not licensed; the producer already stops at the displayed blocks and three points. Reimposed, not repaired |

---

## Verdict

Finite displayed-family theorem for homogeneous degree-3/2/1 order-27 and order-81 digits on the three pinned Q3 fibres: **CONFIRMED**.

Source-complete degree-at-most-three derivative-effect reading: **FAILED**. Affine-output lemma as global predecessor-scheme coverage: **FAILED**. Strongest licensed scope is the displayed digit family on three pinned Q5 predecessor points and their displayed Q4/Q3 fibres.

Replay/custody of the frozen Box02 V2 run: **CONFIRMED** (non-blocking `OUTPUT.sha256` snapshot noise).

CONFIRMED
