# Hostile different-model review — AS F-only D7 normalized Q2/Q1 Gaussian exclusion V2

| Field | Value |
|---|---|
| Claim under review | Frozen V2 producer: at each of three pinned Q5 predecessor points `base0000`, `base0270`, `base0513`, consume the entire reviewed Q3 affine fibre and adjoin homogeneous degree-3/2 order-27 and order-81 digits; the literal integer Jacobian, after exact `/27` then `/81` on the fixed 91-slot inventory, yields a rank-5 eight-coordinate first carry with exactly 27 accepted assignments, a branchwise affine `/81` map, and an inconsistent system on every branch, with singleton left-null support on row 8 (`x^2 y`) |
| Overall verdict | **CONFIRMED_WITH_REPAIRS** |
| Finite Gaussian/certificate theorem (displayed family) | **CONFIRMED** |
| Claimed source normalization | **FAILED** (not a proved source/symplectic affine theorem; omitted order-27 degree-1 digits are not licensed to be absent, and can in principle move the row-8 residual) |
| Strongest licensed scope | selected homogeneous degree-3/2 order-27 and order-81 digit family, over the entire displayed Q4/Q3 fibre of three fixed Q5 predecessor *points*; not complete Q3-fibre exclusion; not three structural bases; not 79→76 |
| Replay/custody | **CONFIRMED** of the frozen Box02 run recorded below (non-blocking `OUTPUT.sha256` self-hash / snapshot noise, identical in kind to the Q3 parent review; not used as mathematical evidence). `replay_all.sh` was not re-launched. This review used read/search/glob only |
| Smallest failing identity | none inside the selected family |
| Smallest missing hypothesis | a source/symplectic affine theorem killing order-27 (and order-81) degree-1 digits without changing `[x^2 y](det J-1)/81`; that hypothesis is **missing**, so complete Q3-fibre exclusion is **not** licensed |
| Evidence tier | source reconstruction of `P_x Q_y - P_y Q_x - 1` over `Z`; exact `/27` and `/81` before `% 3`; fixed 91-slot order with row 8 = `x^2 y`; whole Q3-kernel parametrization; 63 over-cap slots retained among the 91; eight-column first-carry cone, rank 5, `3^8` enumeration, 27 accepted; quadratic design `1+2n+C(n,2)` = 630/496 with both `2e_i` and `e_i+e_j`; 81 stored matrices/RHS and singleton row-8 left-nulls; V2 inclusion-minimal multirow omission with raw-digit `/27` and `/81` replay; V1 one-row control retained as a negative control |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Review constraint | read/search/glob only; no Bash, Python, CAS, solver, web, or network; no producer/case/ledger/prompt edits; all substantive replay is the frozen AWS run |
| Review window (UTC) | 2026-08-25 |

Producer report, V2 freeze, V2 certificates, Q3 parent producer, CONFIRMED Q3 parent review, and the three hash-pinned compiler anchors were reread in full before any verdict. No producer, case, prompt, parent, or ancestry file was edited.

---

## Required decisions

### Finite Gaussian/certificate theorem for the displayed family

**Correct.** On the selected homogeneous degree-3/2 order-27 and order-81 family, over the entire displayed Q3 affine fibre of each of the three pinned Q5 predecessor points, the compiled `/27` then `/81` tower is exhaustive, affine on each accepted branch, and inconsistent on all 27 branches. The `/243` layer is never reached. Row 8 is a genuine singleton obstruction in the report's residual convention `2,2,1`.

### Claimed source normalization

**Failed.** Arbitrary homogeneous degree-3/2 digits at orders 27 and 81 are a *selected* family, not a proved complete source-normalized derivative-effect cone. Constant digits cannot change `det J`. Degree-1 digits are not shown to be absent by a source/symplectic affine theorem in the consumed parent chain, and order-27 linear digits can in principle change the row-8 residual. Theorem wording must remain “selected normalized digit family,” not “complete Q3 fibre exclusion.”

### Strongest licensed scope after that decision

Three **fixed Q5 predecessor points** (`base0000`, `base0270`, `base0513`), each with its entire displayed Q4 affine fibre and entire displayed Q3 affine fibre, excluding every accepted first-carry branch of the **selected** homogeneous degree-3/2 order-27 and order-81 digits, including all 63 over-cap slots of degrees 7–12 among the 91 rows. This does not exclude three whole structural bases, does not reduce the 79-base remainder to 76, and does not exclude omitted source directions (in particular order-27 degree-1 digits).

### Source, arithmetic, coverage, or custody defects

- **Load-bearing (wording/scope repair, no AWS rerun):** title and any “displayed Q3 fibre exclusion” reading overclaim the licensed object. Keep the producer body's selected-family hedge; do not promote the provisional source-normalization audit to a complete fibre theorem.
- **Non-blocking custody:** each AWS `OUTPUT.sha256` records a self-hash taken while the file was being written, and snapshots `launcher.stdout` as empty; the later MANIFEST hashes the final files. Identical in kind to the Q3 parent review. Not used as mathematical evidence.
- **Non-blocking parent-markdown drift:** the CONFIRMED Q3 review consumed `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-producer-20260825.md` as `737b45f6…`; V2 `MANIFEST.sha256` pins the same path as `be7ea59a…`. The Q3 *compiler* pin `solve_q3.py` = `14d69e65…` is stable across parent review, two-level source, and V2 freeze. Mathematical parent is the code and the frozen `q3_parent.json` bytes, which match the Q3 output SHAs.
- **Not a defect:** the independent verifier checks stored matrices, not a second Jacobian. Raw-digit reconstruction of omission controls lives in the producer and ran on AWS. V3 `classify_branches.py` as a standalone script asserts `/81` consistency and is not a successful endpoint; V2 correctly `exec`s only the prefix before `branches = []`.

### Independent replay

Not re-launched. Frozen Box02 command and hashes are recorded in the custody section below.

---

## Promotion

**Accept `AT EACH OF THREE PINNED Q5 PREDECESSOR POINTS, THE ENTIRE REVIEWED Q3 AFFINE FIBRE PLUS THE SELECTED HOMOGENEOUS DEGREE-3/2 ORDER-27 AND ORDER-81 DIGITS HAS AN EXACT RANK-5 EIGHT-COORDINATE /27 CARRY WITH 27 ACCEPTED ASSIGNMENTS; ON EVERY ACCEPTED BRANCH THE /81 MAP IS AFFINE ON THE REMAINING CUBE AND INCONSISTENT, WITH SINGLETON LEFT-NULL SUPPORT ON THE x^2 y SLOT (ROW 8) AND RESIDUAL CONSTANTS 2, 2, 1.`**

**Refuse `COMPLETE Q3 FIBRE EXCLUSION`, `SOURCE-COMPLETE DERIVATIVE-EFFECT CONE`, `THREE STRUCTURAL BASES EXCLUDED`, and `79-BASE REMAINDER REDUCED TO 76`.**

On the aligned F-only `D=7` chart, after the CONFIRMED Q3 whole-kernel gate:

- Over `Z`, the compiled map is
  `P = P_Q3 + 27(W_3+W_2) + 81(H_3+H_2)`,
  `Q = Q_Q3 + 27(Z_3+Z_2) + 81(J_3+J_2)`,
  with every subscript a homogeneous binary form of that total degree, and with `P_Q3,Q_Q3` running over the full Q3 affine fibre (`q3_particular + F_3`-span of `q3_kernel`), not a single particular.
- The Jacobian orientation is the parent integer determinant
  `P_x Q_y - P_y Q_x - 1`,
  obtained transitively from `replay_full_q4_restore.py` via `solve_full68.py` and `solve_q3.py`. Axis 0 is the `x`-exponent. Every coefficient is divided exactly by 27 or 81 *before* reduction modulo 3.
- The 91-slot order is
  `slots = [(i, d-i) for d in 0..12 for i in 0..d]`,
  i.e. `[x^i y^{d-i}]`. Length `1+2+…+13 = 91`. Degrees 7–12 contribute `8+9+10+11+12+13 = 63` over-cap rows, all retained at both `/27` and `/81`. Degree 3 occupies indices 6–9; **row 8 is `(2,1) = x^2 y`**.
- Fresh digits are 28 coordinates (no degree-1, no constants). Raw dimension is `q3_kdim + 28`, hence 42, 38, 38. The `/27` matrix has exactly eight nonzero columns
  `w3_1,w3_2,z3_1,z3_2,w2_1,w2_2,z2_0,z2_1`,
  stored as `active_raw_columns` `[15,16,19,20,23,24,25,26]` at `base0000` and `[11,12,15,16,19,20,21,22]` at the other two (those are `q3_kdim` plus the same relative fresh indices). Rank 5, so `3^{8-5} = 27` accepted assignments. Branching on those 27 and retaining every inactive coordinate (Q3 fibre, remaining W/Z slots, and all H/J) is exhaustive for this family.
- After the first carry is fixed in raw coordinates (not an RREF wrap of the `/27` kernel), mixed and pure quadratic remainders of remaining digits at `/81` have 3-adic valuation at least 1, so the restricted map is at most affine. The compiler proves affineness by origin, both nonzero multiples `2e_i`, and every pair sum `e_i+e_j`. Design counts are `1+2n+C(n,2)`: 630 at `n=34`, 496 at `n=30`.
- Every one of the 81 branch systems is inconsistent. Stored left-nulls are singletons on row 8: `[[8,1]]` on all 27 branches of `base0000` and `base0270`, `[[8,2]]` on all 27 branches of `base0513`. Pairing with the right side normalizes to 1, so the report's residual constants are `(-rhs[8]) mod 3 = 2,2,1`. Because row 8 of each `/81` matrix is the zero vector, the residual is independent of every remaining displayed coordinate.
- V2 omission controls are inclusion-minimal multirow sets of sizes 2–4, 3–6, 2–5. The producer reconstructs raw digits and literally checks every `/27` row and every retained `/81` row; at least one omitted `/81` row is nonzero. The V1 one-row control is a negative control: those sizes are all at least 2, and re-adding any omitted row restores inconsistency, so a single-row deletion never suffices. V1 source `certify_all.py` is SHA-pinned and still contains the false one-row assertion.

**Do not promote this to:** a source-complete Q3-fibre exclusion; a theorem that degree-1 or constant order-27/81 digits are gauged away; exclusion of three whole structural bases; a reduction of the 79-base remainder to 76; a complete map modulo 243; an all-depth lift; a counterexample; or JC2.

**Smallest honest successor.** Either (i) keep the selected-family theorem and, separately, compile order-27 degree-1 digits `(C_1,D_1)` as their own exact gate on the same three points, reconstructing the integer determinant and testing whether they move row 8; or (ii) prove a source/symplectic affine slice theorem that kills those digits without changing `[x^2 y](det J-1)/81`, then return for promotion. Do not silently treat V2's omitted-row weakening as a reason to drop the V1 one-row negative control.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as complete exclusion of a Q3 fibre, or as the complete normalized derivative-effect cone at orders 27 and 81;
- this gate as a proof that degree-1 (or constant) order-27/81 digits are absent by source/symplectic affine normalization;
- this gate as exclusion of three whole structural bases, or as reducing 79 remaining bases to 76;
- this gate as a complete determinant-one map modulo 243, an all-depth lift, a characteristic-zero point, a counterexample, or JC2;
- V3 `classify_branches.py` as a successful `/81`-consistent classifier (its branch loop asserts consistency; the Gaussian theorem is that those systems are inconsistent);
- V1 `certify_all.py` as a successful one-row omission package (it is the negative control showing redundant obstruction support);
- two-level V1 `solve_two_level.py` as an affine `/81` theorem (its canonical RREF wrap is a different negative control: `/81` is nonlinear in those coordinates, which is why V3/V2 retain raw inactive digits).

---

## Hostile checks

Tried hard, and failed, to flip the Jacobian orientation; to reduce modulo 3 before exact division by 27 or 81; to make the 91-slot order anything other than `[x^i y^{d-i}]` for `d=0..12`; to make row 8 be `x y^2` or `x^3`; to replace the whole Q3 kernel by a single particular; to drop the 63 over-cap rows from the 91-row `/27` or `/81` inventories; to find a ninth active `/27` column, a first-carry rank other than 5, or an accepted-assignment count other than 27; to make branching on the eight active coordinates while freezing inactive coordinates to zero miss an affine `/27` solution; to omit the pure `2e_i` tests or the mixed `e_i+e_j` tests, or to mismatch design counts 630/496; to find a left-null support other than singleton row 8, or residual constants other than `2,2,1` in the report's convention; to make a V2 omission set of size 1, or to treat that as a silent weakening of V1; to license degree-1 digits as gauge without a parent theorem; or to read three predecessor *points* as three structural bases or as a 79→76 reduction.

### 1. Source formula, orientation, exact division, row 8

Transitive compiler pins (V2 `MANIFEST.sha256` / `SOURCE_MANIFEST.sha256`):

| object | SHA-256 |
|---|---|
| V2 `certify_all_v2.py` | `cb9d30f6d47ea65b317cbc93b68da4b4eec5e26a0c9b7d00aa68edfb73939a31` |
| V2 `verify_certificates_v2.py` | `68990434ef78a3709883e7443e45d258a1911f2741345403d3b9cdbb059b7e04` |
| V2 `run_remote.sh` | `6a13ce08c95eb25db04165863842864a4a7eb2d9ea874b835cf83b19916c41ff` |
| V1 `certify_all.py` | `9a34970455d0844b4a4894dca34389fd2cc43704466d9ddf13e3c09d88cddcda` |
| V3 `classify_branches.py` | `4f6b94ce223e60b9023b8e3fe91a1113b0978a4ff74e986aa1227e01217006b9` |
| two-level `solve_two_level.py` | `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd` |
| Q3 `solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| Q3 different-model review | `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` (`CONFIRMED`) |
| V2 preregistration | `15dd551af28019dc31cf9da3a752602c898235f2cada971f73e1b8cf6e86915e` |

`solve_two_level.py` SHA-pins and `exec`s the Q3 parent before building any Q2/Q1 row. The Q3 parent SHA-pins the Q4 68-row gate, which SHA-pins the Q4 restore that *defines*

```text
det J - 1 = P_x Q_y - P_y Q_x - 1
```

with `nderivative(·,0) = ∂/∂x`. V3 `exec`s the two-level prefix through `raw_rows` / `extract_affine` / `slots`. V1 Gaussian `exec`s the V3 prefix through `place` / `accepted`. V2 Gaussian `exec`s the V1 prefix through `tracked_contradiction` and replaces only the branch loop and the omission control. Every `exec` asserts the child SHA before compile.

`raw_rows` refuses any coefficient not divisible by the divisor, then reduces modulo 3. The 91-slot list is exactly the monomials of degrees 0 through 12 in the parent slot convention. Counting from 0:

- degree 0: index 0 = `(0,0)`
- degree 1: indices 1–2
- degree 2: indices 3–5
- degree 3: indices 6–9 = `(0,3),(1,2),(2,1),(3,0)`

so index 8 is `(2,1) = x^2 y`, matching `homogeneous_numeric(d, c)[i] = c_i x^i y^{d-i}`.

### 2. Entire Q3 fibre and 63 over-cap rows

`raw_candidate` starts from `q3_particular` and adds every `q3_kernel` vector. Frozen parent JSON consumed on AWS:

| base | `q3_parent.json` SHA-256 | kernel dim | raw vars |
|---|---|---:|---:|
| 0000 | `89c9b8bfb4c46b566e10e7f5716502b0a3b6f64af29a5f4e14234cc09b945187` | 14 | 42 |
| 0270 | `9016e7737c7f3a31107a80f4da91e1e8cec7be686569cd548e55e135fcec4dfb` | 10 | 38 |
| 0513 | `e2711128f358f5b65f215a2898ccf90fa10a7e1e6908ccdde7c9a4410290b4bb` | 10 | 38 |

Those three SHAs are exactly the Q3 producer output hashes. Certificates store `raw_variable_count` 42/38/38 and `row_count` 91. Both `/27` and `/81` call `raw_rows(..., slots)` with the full 91-list, so the 63 degree-7-through-12 rows are present at every reached stage. The planned `/243` layer on `high_slots` (those 63 alone) is never reached because every `/81` branch is inconsistent.

### 3. Eight active coordinates, rank 5, 27 assignments, exhaustive inactive retention

`classify_branches.py` builds the `/27` affine matrix on all `raw_n` coordinates, takes columns that are not identically zero, and enumerates `F_3^8` with inactive digits set to 0. Because inactive columns are zero, that is the full `/27` solution set. It asserts `len(accepted) == 3**(len(active1)-r1)`. Frozen certificates contain `"rank":5,"rhs":` in `stage1`, eight `active_raw_columns` as listed above, and 27 `accepted_assignments`. The independent verifier re-enumerates all 6561 active tuples against the stored 8-column matrix and reproduces those 27 assignments on each parent.

`place(fixed, x)` writes the accepted active 8-tuple and *every* inactive coordinate as a free `/81` variable. That is the full remaining cube of the displayed family: 34 coordinates at `base0000`, 30 at the others. No RREF representative of the `/27` kernel is substituted (that wrap is exactly why two-level V1's `/81` map failed affineness).

### 4. Quadratic design at `/81`

`extract_affine` in the two-level prefix:

- evaluates the origin and the `n` unit vectors to form columns;
- asserts `f(2e_i) = c + 2 M e_i` for every `i`;
- asserts `f(e_i+e_j) = c + M e_i + M e_j` for every pair;
- returns `design_count = 1 + 2n + C(n,2)`.

Certificates store `design_count` 630 (`n=34`) and 496 (`n=30`), and `input_dimension` 34/30. Producer stdout reports a single rank pair per parent, so the design ran on all 27 branches. After the order-27 first carry is fixed, remaining quadratic pieces are `27^2`, `27·81`, and `81^2`, all valuation `≥ 6`, hence `0 mod 3` after `/81`; the design is the exact F3 check of that valuation statement.

### 5. Eighty-one matrices, singleton row-8 left-nulls, residuals `2,2,1`

Producer stdout, certificates, and verifier stdout:

| parent | branches | `/81` rank / aug | design | left-null | residual constant |
|---|---:|---|---:|---|---:|
| `base0000` | 27 | 6 / 7 | 630 | `[[8,1]]` on every branch | 2 |
| `base0270` | 27 | 7 / 8 | 496 | `[[8,1]]` on every branch | 2 |
| `base0513` | 27 | 7 / 8 | 496 | `[[8,2]]` on every branch | 1 |

No certificate contains `left_null_sparse` supported on any row other than 8, and none mixes `[[8,1]]` with `[[8,2]]` on the same parent. Branch 0 matrices (visible at the head of each JSON) have row 8 identically zero; a singleton left-null on row 8 with `λ^T M = 0` and `λ ≠ 0` forces that for every branch. The verifier checks `λ^T M = 0` and `λ^T b = 1` on all 81 stored systems. Convention: `b = (-constant) mod 3` and `λ_8 * b_8 ≡ 1`, so `λ_8=1` implies `b_8=1` and constant `2`; `λ_8=2` implies `b_8=2` and constant `1`.

This review did not re-multiply all 81 matrices locally. The source that emits them, the stored sparse vectors, the visible zero row 8, and the AWS verifier together are the certificate.

### 6. V2 inclusion-minimal omission controls, and V1 as negative control

V2 greedily deletes a certificate-supported row until the kept subsystem is consistent, then re-adds every row whose re-insertion stays consistent, and asserts that re-inserting any remaining omitted row restores inconsistency. It then sets `raw = place(fixed, particular)`, demands `raw_rows(raw, 27, slots) = 0`, demands every kept `/81` slot vanish, and demands some omitted `/81` slot nonzero. That is literal raw-digit reconstruction from the integer determinant, not a check on the stored matrix alone.

Producer stdout omission sizes: `[2,3,4]`, `[3,4,5,6]`, `[2,3,4,5]`. All ≥ 2, matching the report. Certificates store `"kind":"inclusion-minimal-redundant-support"`. The independent verifier checks the kept/omitted partition of `{0,…,90}`, vanishing of stored-matrix residuals on kept rows, and a nonzero omitted residual; it does *not* re-run `raw_rows`. The Jacobian-level omission check is the producer, and it returned PASS on all three AWS lanes.

V1 `certify_all.py` still asserts a one-row omission control (`omission_control` returning a single `omitted_row`, and `stage81[i]==0` for all `i ≠ omitted`). V2 does not run that loop. Inclusion-minimality plus omitted size ≥ 2 is exactly the statement that no single-row deletion works, so V1 is a true negative control for redundant obstruction support, not a silent weakening of the rank/left-null theorem. V1 has no successful AWS endpoint, which is the expected fail-closed behaviour of that assertion.

### 7. Source-normalization charge (load-bearing)

The selected family is hardcoded in `raw_candidate`: blocks of homogeneous degree 3 and 2 only, 28 fresh coordinates. Two-level V1 preregistration already typed this as `(W3,Z3),(W2,Z2)` then `(H3,J3),(H2,J2)`, with degree 0 as a *control* that should branch to `(C1,D1)` if it becomes nonzero without a pivot — i.e. degree-1 digits were never claimed to be normalized away; they were deferred.

Constants: translations do not change derivatives, so they cannot move any Jacobian coefficient, including row 8.

Order-27 degree-1 digits `P += 27(ax+by+c)`, `Q += 27(dx+ey+f)` contribute
`27(a Q_y + e P_x - b Q_x - d P_y) + 729(ae-bd)`.
On the charged chart `Q = y + 3V + 9D + 27Z + 81J`, the degree-3 part of `Q_y` includes `3 V_y` from a degree-4 piece of `V`. After `/81` this is `a[V_y]_3`. For `V = ∑ v_i x^i y^{4-i}`, the slot `[x^2 y]` of `V_y` is `2 v_2`. That F3 coefficient is not shown to vanish by any consumed parent theorem, and it is not a multiple of 3. Therefore omitted order-27 linear digits **can in principle alter the row-8 obstruction**.

Order-81 linear digits contribute `a Q_y + …` already at `/81`; on this chart those degree-3 pieces carry extra factors of 3 and vanish modulo 3, so they are not the present threat. That is a chart-valuation observation, not a gauge theorem, and it does not license dropping the order-27 linear digits.

No parent review proves a symplectic-affine slice at this precision that sets those digits to zero while preserving `[x^2 y](det J-1)/81`. The Q3 parent successor sentence specifies order-27 degree-three/two pieces because those are the digits whose divergences hit the still-valuation-3 degrees 2 and 1 of `det J-1`; it does not prove that degree-1 *digits* are gauge. Degree 0 of `det J-1` is already exactly absent on the three displayed points, which is why constants and trace parts are constrained, not why the full linear block is absent.

Consequently the exact theorem stops at the selected family. The producer body's provisional hedge is the correct theorem shape. The title “exact Gaussian exclusion on three displayed Q3 fibres” is not licensed and is the wording repair.

### 8. Scope: three points, not three bases, not 79→76

Consumed SAT models are the same three Boolector endpoints already confirmed by the Q3/Q4 reviews (`dbb405ac…`, `05627048…`, `9c319fe4…`). Each is one Q5 predecessor *point*. Downstream Q4 and Q3 fibre coordinates are variables of the compiled map. Other Q5 solutions may exist under the same structural-base labels. The 79-structural-base predecessor scheme is untouched. The producer refusal list is accurate and is hereby reimposed, with the additional refusal of source-complete fibre language.

---

## Frozen AWS producer replay (not re-launched)

Host `ip-172-30-0-186` (Box02). Job `/home/ubuntu/jobs/as_q3_q2q1_gaussian_exclusion_v2_20260825T1340Z`. `JC2_ROOT` on the box was the staged closure `/home/ubuntu/jobs/as_q5_sat_q3_full_kernel_20260825T121434Z/source`. All three lanes have `start_utc` `2026-08-25T13:04:17Z`. Producer and verifier stderr files are empty (`e3b0c442…`). Launcher prints `PASS-AS-Q3-Q2Q1-GAUSSIAN-PRODUCER-AND-VERIFY-V2`.

| base | wall (start→end) | producer stdout SHA-256 | verifier stdout SHA-256 | certificates SHA-256 |
|---|---|---|---|---|
| 0000 | 13:04:17Z – 13:04:53Z | `31d0e4ca57a74bb26de0b858055c9017eb3b451a5ab29e84c040563fc4ebab81` | `27e03556613c87265f8f19c0f0bf9bfe9c94986bcd3017c2e16d4cfd26b77f12` | `8e563b395d4181d90967c75c35242abc557a8979b4c3f6d89757ce3d234b3f1b` |
| 0270 | 13:04:17Z – 13:04:49Z | `9900f7b67e68bf0d44f9e5a1aceebce0eeca81f8ec80e0ba32485a1ef18fb8fd` | `4a464e3d8a973d15c5110e5b8234d88dd807b35c099f553e341da0af4565fab2` | `5659a16810515290ede2dc78f404330971103f8cbc14fa3116901327f5dee2e9` |
| 0513 | 13:04:17Z – 13:04:48Z | `074f07c699b709bb264aacc19242b4f3957e87c615ab9c78e8e833f5a2dd04e7` | `e77de981385ec96c87c29284f83838ac1f69e6fc82c842f1edd10afcf680f33f` | `5ebacfe12f4492607f69e9518bb6a1ef6102179725f5033550d0b8397bae8015` |

Each producer stdout is `branches 27`, one rank pair, the omission-size set above, the certificates SHA, and `PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION-V2`. Each verifier stdout is `accepted_assignments 27 certificates 27` and `PASS-AS-Q3-Q2Q1-INDEPENDENT-CERTIFICATE-VERIFY-V2`.

Portable AWS replay from a staged repository closure (not executed by this review):

```bash
export JC2_ROOT=/path/to/jc2
export OUTPUT_ROOT=/path/to/fresh/output
bash "$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/replay_all.sh"
```

`replay_all.sh` re-runs `run_remote.sh` on the three frozen models and demands the three certificate SHAs above plus both PASS strings.

---

## Consumed hashes (as recorded in the freeze; not recomputed on the host)

| path | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-producer-20260825.md` | `44834700a9ca092b7c59b5ad8af1079115f5071ced6587f22cd612b75c96405d` |
| `xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-review-grok-20260825-prompt.md` | `7f3b82c3c170e202025289a2fe75b874b83ffa712de7a0ff30c3469723c883e0` |
| `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/PREREGISTRATION.md` | `15dd551af28019dc31cf9da3a752602c898235f2cada971f73e1b8cf6e86915e` |
| `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/certify_all_v2.py` | `cb9d30f6d47ea65b317cbc93b68da4b4eec5e26a0c9b7d00aa68edfb73939a31` |
| `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/verify_certificates_v2.py` | `68990434ef78a3709883e7443e45d258a1911f2741345403d3b9cdbb059b7e04` |
| `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/run_remote.sh` | `6a13ce08c95eb25db04165863842864a4a7eb2d9ea874b835cf83b19916c41ff` |
| `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/replay_all.sh` | `da621ad4469a7f076cf0d9f5970fc9be0c438000867a27de9a94ce1584180660` |
| `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_20260825/certify_all.py` | `9a34970455d0844b4a4894dca34389fd2cc43704466d9ddf13e3c09d88cddcda` |
| `cases/as_fonly_d7_q3_two_level_q2_q1_v3_branches_20260825/classify_branches.py` | `4f6b94ce223e60b9023b8e3fe91a1113b0978a4ff74e986aa1227e01217006b9` |
| `cases/as_fonly_d7_q3_two_level_q2_q1_20260825/solve_two_level.py` | `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-review-grok-20260825.md` | `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` |

---

## Verdict

Finite Gaussian/certificate theorem for the displayed family: **CONFIRMED**.

Source normalization / complete Q3-fibre reading: **FAILED**. Strongest licensed scope is the selected homogeneous degree-3/2 order-27 and order-81 digit family on three pinned Q5 predecessor points and their displayed Q4/Q3 fibres.

Replay/custody of the frozen Box02 run: **CONFIRMED** (non-blocking `OUTPUT.sha256` snapshot noise).

CONFIRMED_WITH_REPAIRS
