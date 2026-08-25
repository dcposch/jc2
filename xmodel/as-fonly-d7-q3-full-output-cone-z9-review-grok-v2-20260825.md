# Hostile different-model review — AS F-only D7 complete `Z/9` output-cone survivor at three Q3 fibres

| Field | Value |
|---|---|
| Claim under review | Frozen producer: at each of the three pinned, reviewed Q3 affine fibres `0000`, `0270`, `0513`, the complete fixed-D7 output coefficient cone `F=F_*+27U+81V` (equivalently `T=U+3V in Z/9`, 72 variables) makes every one of the 91 coefficients of `det J(F)-1` in degrees 0 through 12 vanish modulo 243. Mod-3 rank/kernel `27/45` at every parent; exact Bockstein lift rank/kernel `36/81`, `43/74`, `43/74`; nonempty with `3^81`, `3^74`, `3^74` solutions |
| Overall verdict | **CONFIRMED** |
| Finite fibrewise `Z/9` cone theorem | **CONFIRMED** |
| Whole predecessor scheme / terminal mod 729 / order-243 digits | **REFUSED** (not claimed by the producer body; not licensed here) |
| Strongest licensed scope | three pinned reviewed Q3 fibres, all fixed-D7 output digits at orders 27 and 81, determinant modulo 243. One compiler at three inputs, not three implementations |
| Replay/custody | **CONFIRMED** of the frozen AWS r6d run recorded below (non-blocking `OUTPUT.sha256` self-hash / empty-launcher snapshot noise, identical in kind to the Q3 parent review; not used as mathematical evidence). `replay_all.sh` was not re-launched. This review used read/search only; no Bash, Python, CAS, solver, or local Jacobian replay |
| Smallest failing identity | none inside the displayed cone |
| Smallest missing hypothesis | none that breaks the numbered fibrewise claim. A constant matrix over the global predecessor scheme, terminal modulus 729, and order-243 digits are **missing by design** |
| Evidence tier | SHA-pinned exec of two-level prefix / Q3 / Q4 / Q4-restore / H6 V2; integer identity `P_x Q_y - P_y Q_x - 1`; exact `/27` then `% 9` on all 91 slots; `T=U+3V` identification from `27^2=729≡0 (mod 243)`; F3 RREF plus exact Bockstein; 72 doubled bases; 1296 P/Q pair remainders `% 729==0`; Q3-kernel differences literally `% 81==0` inside D7 and `72*kdim` mixed second differences `% 2187==0`; stored 72-digit particulars with `T=low+3*high`; rc 0 and stdout/JSON rank agreement; AS seed from the H6 V2 source patch plus parent `P4` supports |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Review constraint | read/search only; no Bash, Python, CAS, solver, web, or network; no producer/case/ledger/prompt edits; all substantive replay is the frozen AWS run. The interrupted earlier review client is unused |
| Review window (UTC) | 2026-08-25 |

Producer report, preregistration, portable case, compiler, remote runner, replay wrapper, freeze/manifest, SOURCE_CLOSURE inventory, all three AWS job directories (result, Q3 parent JSON, rc, stdout, stderr, INPUT/OUTPUT hashes), the CONFIRMED Q3 whole-kernel review, the CONFIRMED Q4 68-row review, the selected-family Gaussian and degree-one reviews (as negative controls on row 8, not as evidence for this cone), and the hash-pinned parent compilers through H6 V2 were reread in full before any verdict. No producer, case, prompt, parent, or ancestry file was edited.

---

## Required decisions

### Finite fibrewise `Z/9` cone theorem

**Correct.** On each of the three pinned reviewed Q3 affine fibres, the complete order-27/order-81 D7 output-digit cube is a linear congruence module over `Z/9` for `det J ≡ 1 (mod 243)`, and that module is nonempty. The identification `T=U+3V` is an identity, not a truncation: fresh-fresh quadratic terms carry `27^2=729`, which vanishes modulo 243 (equivalently after exact `/27` they vanish modulo 9). The compiled 91-row inventory is the full coefficient list of a degree-at-most-12 determinant of two degree-at-most-seven maps. Mod-3 rank 27 with kernel 45 lifts by an exact Bockstein whose rank/kernel pairs are `36/81`, `43/74`, `43/74`. Each displayed particular is a 72-tuple in `{0,…,8}` reconstructing as `T = U + 3V`, and the SHA-pinned compiler asserts every 91-slot coefficient of the reconstructed integer determinant is divisible by 243 before writing JSON.

### Whole predecessor / terminal 729 / order-243 digits

**Not licensed.** Order-9 coordinates remain frozen inside `F_*`. Their mixed quotient with a fresh order-27 digit is `KU` on the global predecessor scheme and is correctly refused as a constant-matrix statement. No coefficient is imposed modulo 729, and no order-243 digit is a variable.

### Strongest licensed scope after that decision

Three **pinned reviewed Q3 fibres** (`0000`, `0270`, `0513`), each with its displayed Q3 particular and with the reviewed Q3 kernel absorbed as order-81 D7 output, for **all 72** polynomial output coefficients of total degree at most seven at orders 27 and 81, making `det J-1` vanish coefficientwise modulo 243 on the 91 slots of degrees 0 through 12. This is one implementation at three SAT-model inputs. It does not cover the rest of the Q5/global predecessor scheme, does not impose terminal modulus 729 or order-243 digits, and does not produce a `Z_3` point, a collision, a characteristic-zero counterexample, a no-lift theorem, or JC2.

### Source, arithmetic, coverage, or custody defects

- **None load-bearing.** The producer body's fibrewise hedge, mixed-term firewall for order-9 coordinates, and refusal list match the licensed object.
- **Non-blocking software:** several JSON flags (`literal_integer_replay_mod243_passed`, `linear_mod9_from_bilinearity_and_729_vanishing`, `q3_kernel_absorbed_by_order81_output_space`, `q3_fresh_mixed_terms_divisible_by_2187`, `constant_columns_identically_zero`) are written as the literal `True` after the corresponding asserts. The load-bearing objects are the asserts, the integer control counts `1296 / 1008 / 720 / 720`, the stored 72-digit particulars, and rc 0. Those flags were not used as evidence.
- **Non-blocking source-typing:** the z9 compiler asserts degree at most seven on Q3-kernel differences, not on `P0,Q0` or on the reconstructed particular. Degree completeness of the 91-slot inventory is inherited from the pinned Q4 parent (`max_total_degree_P4 = max_total_degree_Q4 = 7` at all three models), from Q3 adjoining only `81*(H5+H4)` of degrees 5 and 4, and from the D7 support of the 72 fresh digits. Derivatives of two degree-7 maps have degree at most 6, so the determinant has degree at most 12 and cannot grow a coefficient outside the 91 slots. An in-solver `sum(xy)<=7` assert on the base and reconstructed maps would close this hole locally; it is not a missing coefficient in the frozen run.
- **Non-blocking packaging:** dense `matrix9` / Bockstein matrices are not serialized, only SHA-256 plus ranks. Independent re-RREF from the payload is therefore impossible. Rank/kernel arithmetic `27+45=72`, `36+81=117`, `43+74=117`, injectivity of the Bockstein parametrization, and stdout/JSON agreement were checked. The AWS compiler is the Jacobian-level certificate.
- **Non-blocking custody:** each AWS `OUTPUT.sha256` records a self-hash taken while the file was being written, and snapshots `launcher.stdout` / `launcher.stderr` as empty (`e3b0c442…`); the later `MANIFEST.sha256` hashes the final files, and the `result.json` hashes inside `OUTPUT.sha256` match FREEZE/MANIFEST. Identical in kind to the Q3 parent review. Not used as mathematical evidence.
- **Not a defect:** `SOURCE_CLOSURE.sha256` inventories a superset of the runtime `exec` chain (sibling Gaussian/degree-one/state-complete sources are packaged, not executed). The live chain is the SHA-asserted prefix listed in Hostile check 1.
- **Not a defect:** the three jobs are one compiler at three inputs. Rank/kernel pairs `36/81` versus `43/74`/`43/74` are input-dependence of that compiler, not a second implementation.

### Independent replay

Not re-launched. Frozen r6d command and hashes are recorded in the custody section below.

---

## Promotion

**Accept `AT EACH OF THE THREE PINNED REVIEWED Q3 AFFINE FIBRES 0000, 0270, AND 0513, THE COMPLETE FIXED-D7 OUTPUT-DIGIT CONE F = F_* + 27U + 81V, EQUIVALENTLY T = U+3V IN Z/9 WITH 72 COMBINED COEFFICIENTS, IS A LINEAR CONGRUENCE MODULE FOR det J(F) ≡ 1 (MOD 243) ON ALL 91 COEFFICIENTS OF DEGREES 0 THROUGH 12, AND THAT MODULE IS NONEMPTY. THE MOD-3 SYSTEM HAS RANK/KERNEL 27/45 AT EVERY PARENT; ITS EXACT BOCKSTEIN LIFT HAS RANK/KERNEL 36/81, 43/74, 43/74, HENCE 3^81, 3^74, 3^74 SOLUTIONS. EACH DISPLAYED PARTICULAR REPLAYS THE INTEGER DETERMINANT COEFFICIENTWISE DIVISIBLE BY 243. THE REVIEWED Q3 KERNEL IS ABSORBED AS AN ORDER-81 D7 OUTPUT DIRECTION, WITH EVERY MIXED SECOND DIFFERENCE AGAINST THE 72 FRESH BASES DIVISIBLE BY 2187. LIVE DEGREE-FOUR ROW-8 COLUMNS EXPLAIN WHY THE EARLIER DISPLAYED DEGREE-AT-MOST-THREE EXCLUSIONS DO NOT CLOSE THESE FULL CONES.`**

**Refuse `WHOLE Q5/GLOBAL PREDECESSOR SCHEME`, `TERMINAL MODULUS 729`, `ORDER-243 DIGITS`, `ALL-DEPTH COMPATIBLE TOWER`, `Z_3 SOLUTION`, `COLLISION`, `CHARACTERISTIC-ZERO COUNTEREXAMPLE`, `NO-LIFT`, and `JC2`.**

On the aligned F-only `D=7` chart, after the CONFIRMED Q3 whole-kernel gate:

- Over `Z`, write
  `P = P_* + 27 U + 81 V`,
  `Q = Q_* + 27 W + 81 Z`,
  with `U,V,W,Z` of total degree at most seven, and with `(P_*,Q_*)` one literal Q3 particular. Combining digits as `T = U+3V` (and likewise for the second output) gives 36+36=72 variables in `Z/9`. The Jacobian is bilinear, so
  `det J(P_*+27T_P, Q_*+27T_Q) - 1 = Δ_* + 27 L(T) + 729 [T,T]`.
  Since `729 = 3*243 ≡ 0 (mod 243)`, the condition `det J ≡ 1 (mod 243)` is exactly the linear system `(Δ_*/27 + L(T)) ≡ 0 (mod 9)`. The identification `T=U+3V` is therefore valid for this modulus; it is not a discarded order-243 remainder.
- Orientation is the parent integer determinant
  `P_x Q_y - P_y Q_x - 1`,
  with `nderivative(·,0)=∂/∂x`, obtained transitively from `replay_full_q4_restore.py` via `solve_full68.py`, `solve_q3.py`, and the two-level prefix. H6 V2 inserts the AS seed in source:
  `P = (x-x^3) + 3U + 9C + 27W + 81(H7+H6)`,
  `Q = y + 3V + 9D + 27Z + 81(J7+J6)`.
  Every subsequent order-81 or order-27 correction is `0 mod 3`, so every reconstructed map reduces to `(x-x^3, y) mod 3`.
- The 91-slot order is
  `slots = [(i, d-i) for d in 0..12 for i in 0..d]`,
  length `1+2+…+13 = 91`. Degree 3 occupies indices 6–9; **row 8 is `(2,1) = x^2 y`**. The D7 support is the same convention in degrees 0 through 7, length `36`, hence 72 combined variables. Parent `max_total_degree_P4/Q4 = 7` at all three models; Q3 adds only degree 4–5 at order 81; fresh digits are D7. The determinant of two degree-7 maps has degree at most 12, so the 91 slots are the complete coefficient inventory.
- The F3 RREF of the `/27 mod 3` matrix has rank 27 and kernel 45 (`27+45=72`) at all three parents, with `rank = augmented_rank` (consistent). The Bockstein is the standard lift: write `T = t0 + 3 t1` with `t0 = particular3 + K s`. Exact division by 3 of `base + matrix9·t0` and of `matrix9·K` produces a 91-by-117 system on `(s, t1)` over `F3` (`45+72=117`). Rank/kernel `36/81` and `43/74` satisfy `rank + ker = 117` and `rank = augmented_rank`. The map `(s,t1) ↦ K s + 3 t1` is injective on `F3` because `K` is in free-column echelon form, so solution counts are exactly `3^{ker}`. Frozen integers `443426488243037769948249630619149892803` and `202755595904452569706561330872953769` multiply by `2187 = 3^7` as required.
- Linearity controls that actually ran: both constant columns (indices 0, 36) identically zero; all 72 doubled bases affine modulo 9 after `/27`; all `36*36=1296` opposite-output pairs with bilinear remainder divisible by 729; Q3-kernel output differences divisible by 81 with degree at most 7; mixed second differences against all 72 fresh bases divisible by `81*27=2187`, counts `72*14=1008`, `72*10=720`, `72*10=720`. There is no hidden order-9 *variable*: the Q3 kernel is order 81, and order-9 digits of the H6 chart are frozen in `F_*`.
- Row 8 of the `Z/9` matrix has exactly four nonzero columns at every parent, with the same names and the same residues:
  `P_1_1` (degree 2, coeff 6), `P_3_1` (degree 4, coeff 3), `Q_0_2` (degree 2, coeff 3), `Q_2_2` (degree 4, coeff 2).
  In particular `P_3_1 ≡ 3 (mod 9)` is invisible modulo 3 and live in the Bockstein, and `Q_2_2` is a degree-four digit already visible modulo 3. Those degree-four columns are absent from the displayed homogeneous degree-at-most-three families that left a singleton row-8 obstruction. This cone is larger, and those families remain correctly excluded as selected families; they do not empty the full D7 cone.

**Do not promote this to:** coverage of the whole Q5/global predecessor scheme; a constant RREF over order-9 coordinates; terminal-mod-729 closure; an order-243 digit layer; an all-depth compatible tower; a `Z_3` point; a collision; a characteristic-zero counterexample; a no-lift theorem; or JC2. Do not read three SAT-model inputs as three structural bases or as a 79→76 reduction. Do not treat the selected-family Gaussian/degree-one exclusions as retracted; they exclude smaller families, and this review licenses only that those exclusions do not empty the *full* D7 cone.

**Smallest honest successor.** Keep the three survivors and, separately, either (i) impose the next terminal modulus / order-243 digit layer with Jacobian/Hensel data, or (ii) over the whole predecessor algebra retain an order-9 base direction and compute the mixed `K*U` section by Fitting strata rather than a constant RREF. Do not silently promote these three fibres to the global scheme.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as a statement about the whole Q5 fibre, the global predecessor scheme, or any Q5 model other than the three consumed Cartier-zero SAT endpoints;
- this gate as a constant linearized matrix in the presence of free order-9 coordinates (the mixed quotient `(9K)(27U)/243 = KU` is real on that larger scheme and is not controlled here);
- this gate as terminal-mod-729 closure, as order-243 digits, as an all-depth lift, as a `Z_3` solution, as a collision, as a characteristic-zero counterexample, as a no-lift theorem, or as JC2;
- this gate as a retraction of the selected homogeneous degree-3/2 or degree-3/2/1 exclusions (those families remain inconsistent at `/81` with row-8 residual `2,2,1`; they are proper subfamilies of this cone);
- three jobs as three independent implementations;
- stored JSON booleans as a substitute for the integer asserts, control counts, and particulars.

---

## Hostile checks

Tried hard, and failed, to replace the consumed Q3 parents by reset or unrelated maps; to flip the Jacobian orientation; to make `T=U+3V` drop a 243-relevant quadratic remainder; to shrink the 91-slot inventory or the 72 D7 variables; to leak a degree-8 output or a degree-13 determinant coefficient past the 91 slots; to skip exact division by 27 or by 3, or to reduce modulo 3 first; to break RREF signs, the inverse of 2 in `F3`, kernel-carry columns, or high-digit reconstruction; to make rank/kernel fail `n = rank + ker` or to make `3^{81}`/`3^{74}` disagree with the frozen integers; to skip a doubled basis, a P/Q pair, or a Q3-kernel/fresh mixed difference; to find a hidden order-9 *variable* inside the 72-cube or a Q3-kernel direction of order other than 81; to accept `literal_integer_replay_mod243_passed` without the assert site and stored particular; to make the reconstructed maps miss the AS seed `(x-x^3,y) mod 3`; to explain away live degree-four row-8 columns; to read the three jobs as independent implementations; or to promote the fibrewise cone to whole-predecessor, mod-729, order-243, `Z_3`, collision, counterexample, no-lift, or JC2 coverage.

### 1. Transitive source chain and consumed Q3 parents

Runtime `exec` pins, each asserted before compile, matching `SOURCE_CLOSURE.sha256` and `MANIFEST.sha256`:

| object | SHA-256 |
|---|---|
| z9 `solve_full_output_cone_z9.py` | `2d2e0f5fa03c663201157d109a961055ebe1b3daad552b34954f20a633de32f7` |
| two-level `solve_two_level.py` | `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd` |
| Q3 `solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| Q4 `solve_full68.py` | `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4` |
| Q4 restore `replay_full_q4_restore.py` | `9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c` |
| H6 V2 `replay_global_q5_h6_v2.py` | `41e0e74ec4d318bdd33242dcb9053ce53572470570ab5d54f1431184eb789ffa` |
| H6 V1 (bytes patched in memory) `replay_global_q5_h6.py` | `75e153c3ea2a0de9ce2bf26ba13893e44a4092cd8b1bdd1d45256f12ac023eea` |
| z9 runner `run_remote.sh` | `6941fe927b6cb69cd57d761e57e7f2b58fb52385133a6a62079e4757a40e3d1c` |
| z9 preregistration | `da5ccbb412c7556c50e80f65e3f2030a12e515b64658c0e0a0fc045595b1d96c` |
| source archive `SOURCE_CLOSURE.tar.gz` | `c3cb56df1c9ad751bd363a79300185245681ad5524ad5f347bf412e5499c702e` |

The z9 compiler `exec`s only the two-level *prefix* before `stages = []`, so the two-level Q2/Q1 stages and the Gaussian/degree-one siblings in the tarball are not live mathematics. That prefix fully `exec`s Q3, which fully `exec`s Q4, restore, and H6 V2. Nested `PARENT_OUTPUT_JSON` reuse writes Q4 then overwrites with Q3 on the same path; the frozen `q3_parent.json` bytes are the Q3 solver output.

Consumed SAT models and regenerated Q3 JSON match the CONFIRMED Q3 whole-kernel review on the nose, including kernel dimensions 14, 10, 10, matrix SHAs, and particulars:

| base | model SHA-256 | `q3_parent.json` SHA-256 | Q3 kdim | Q3 particular (prefix) |
|---|---|---|---:|---|
| 0000 | `dbb405ac9ab12b9d4b01df6e934ac6979609dfd4eabbe2ccf65a65aaf8cdcb81` | `89c9b8bfb4c46b566e10e7f5716502b0a3b6f64af29a5f4e14234cc09b945187` | 14 | `(H4,J4)=(0,2,0,0,2)\|(0,0,1,0,0)` |
| 0270 | `05627048aa3e648b975acc1ed47e97a451241c3544e7fa5b58a7c42a1cd4be03` | `9016e7737c7f3a31107a80f4da91e1e8cec7be686569cd548e55e135fcec4dfb` | 10 | `(H4,J4)=(0,0,0,0,2)\|(0,0,0,0,0)` |
| 0513 | `9c319fe4d1a576569869cbccbcc7411fee5eb12dedaa4e6a820a395263820200` | `e2711128f358f5b65f215a2898ccf90fa10a7e1e6908ccdde7c9a4410290b4bb` | 10 | `(H4,J4)=(0,0,0,0,0)\|(0,0,0,0,0)` |

Those three Q3 output hashes are exactly the Q3 producer hashes. `matrix_sha256` values `0ef37958…` / `976ed4dc…` / `976ed4dc…` are the Q3 review's independent matrices. The maps are the previously reviewed fibres, not resets.

### 2. Determinant orientation, `T=U+3V`, 91 slots, degree ≤ 7

`replay_full_q4_restore.py` defines

```text
det J - 1 = P_x Q_y - P_y Q_x - 1
```

with axis 0 the `x`-exponent. z9 obtains this function from the two-level prefix as `determinant_minus_one`. Slot 8 is asserted `(2,1)` and frozen `slot_order[8] = [2,1]`. Support length 36 and variable count 72 are asserted and stored.

Bilinearity gives remainder `729(U_x W_y - U_y W_x)` on a P/Q pair, identically divisible by 729, hence `0 mod 243` and `0 mod 9` after `/27`. Doubling a single output is affine in that output (the other held at the base), so the 72 doubles plus 1296 opposite-output pairs are the correct design; same-output mixed pairs are not required.

Degree bound: Q4 parent JSON records `max_total_degree_P4 = max_total_degree_Q4 = 7` at all three models; Q3 kernel differences are asserted `sum(xy)<=7` and `% 81 == 0`; fresh corrections are D7 by construction. Two degree-7 maps cannot produce a determinant monomial of degree > 12. The 91-slot scan is therefore complete for this cone: there is no silently omitted coefficient.

### 3. Mod-3 RREF and Bockstein

`rref_with_left` is Gaussian elimination over `F3` with tracked left operations. Pivot 2 is scaled by 2 (the inverse, since `2·2=1 mod 3`). Elimination is `value - scalar*pivot`. Kernel vectors put 1 on a free column and `(-work[row][free])%3` on pivots. Contradictions, if any, return a left-null with pairing 1; none occur.

Stage 1: `matrix3 = matrix9 % 3`, `rhs3 = (-base)%3`. Frozen `stage_mod3` is rank 27, augmented 27, kernel 45 at all three. stdout prints the same numbers.

Bockstein: `lift_base = (base + matrix9·particular3)/3 mod 3` with `numerator % 3 == 0` asserted; `kernel_carry = (matrix9·k)/3 mod 3` similarly. The stacked system is `[kernel_carry | matrix3] (s, t1)^T ≡ -lift_base`. Reconstruction

```text
T = (particular3 + K s + 3 t1) mod 9
```

is then asserted to satisfy `base + matrix9·T ≡ 0 (mod 9)` before the integer determinant replay. Python `//` and `%` on possibly negative integers are consistent with the least-nonnegative residue, so `(delta//27)%9` is the correct class in `{0,…,8}`.

Independent rank verification from a stored dense matrix is not possible (only SHA-256). Arithmetic `rank+ker=n`, `rank=augmented_rank`, injective parametrization, and stdout/JSON agreement hold. Frozen Bockstein matrix SHAs differ across the three inputs, as required of one compiler at three bases.

### 4. Linearity controls and hidden order-9

| control | frozen count | identity |
|---|---:|---|
| constant columns | 2 (`P_{0,0}`, `Q_{0,0}`) | identically zero (derivatives vanish) |
| doubled bases | 72 | affine after `/27` modulo 9 |
| P/Q pairs | 1296 | remainder `% 729==0` and affine after `/27` modulo 9 |
| Q3-kernel differences | 14 / 10 / 10 | output difference `% 81==0`, degree ≤ 7 |
| mixed Q3-kernel × fresh | 1008 / 720 / 720 | second difference `% 2187==0` |

An order-9 kernel direction would make the mixed term valuation 5 (`9*27=243`), failing `% 2187==0`. An order-27 kernel direction would give valuation 6 (`729`). Passage of the 2187-assert, together with `% 81==0` on the output difference, is a source-level proof that every reviewed Q3-kernel direction is an order-81 D7 increment, i.e. a `T`-step divisible by 3. Mixed vanishing at 2187 also makes the `Z/9` matrix constant on the Q3 fibre, so compiling at one particular plus absorption is the whole displayed fibre, not a point sample.

Order-9 *chart* digits `9C, 9D` exist in H6 V2 and are frozen in `F_*`. They contribute to the linear form `L(T)` and are not variables. Promoting this matrix to the global predecessor scheme would be exactly the `KU` overreach the producer refuses.

### 5. Literal particulars, modulo 243, AS seed

Each result stores a 72-vector `combined_z9_particular` in `{0,…,8}` together with `order27_digits = T%3` and `order81_digits = T//3`. Spot-checks (`T=3,4,6,8`) satisfy `T = low + 3 high`. The compiler then rebuilds `P_*+27T_P`, `Q_*+27T_Q` and asserts every 91-slot coefficient of `det J-1` is divisible by 243, then stores `determinant_sha256` of `repr(sorted(determinant.items()))`. rc 0 at all three jobs is the certificate that those asserts ran. The boolean flag was ignored.

AS seed is source, not a stored boolean. H6 V2 patches

```text
P = nadd({(1,0):1,(3,0):-1}, nscale(3,U), nscale(9,C), nscale(27,W), nscale(81,H7))
Q = nadd({(0,1):1}, nscale(3,V), nscale(9,D), nscale(27,Z), nscale(81,J7))
```

before adjoining `81(H6,J6)`. Frozen Q4-restore supports reduce to the same seed coefficientwise modulo 3 at all three models (`[x]=1`, `[x^3]≡-1`, `[y]=1`, every other displayed coefficient `≡0 (mod 3)`). Q3 and z9 corrections are multiples of 27 or 81, hence vanish modulo 3.

Q3 parent valuation tables already force every degree-0-through-12 coefficient of `Δ_*` to be divisible by 27 (degrees 1–2 at exact valuation 3; degree 3 at 5 after Q3; degrees 7–12 at ≥6). That is preregistration check 1, visible in the frozen Q3 JSON, not only in a z9 boolean.

### 6. Row 8 and the degree-at-most-three exclusions

Frozen `row8_nonzero_z9_columns` are identical at all three parents:

| column | name | degree | coeff mod 9 | visible mod 3? |
|---|---|---:|---:|---|
| 4 | `P_1_1` | 2 | 6 | no (`6≡0`) |
| 13 | `P_3_1` | 4 | 3 | no (`3≡0`) |
| 39 | `Q_0_2` | 2 | 3 | no |
| 48 | `Q_2_2` | 4 | 2 | yes |

Support indexing matches the names: degree 2 occupies indices 3–5 so `(1,1)` is 4; degree 4 occupies 10–14 so `(3,1)` is 13; Q-block offset 36 puts `Q_0_2` at 39 and `Q_2_2` at 48.

At the AS seed the first-order action is divergence `U_x+W_y`. `[x^2 y](U_x)` is hit by `P_3_1` with integer factor 3, hence `0 mod 3` and `3 mod 9`; `[x^2 y](W_y)` is hit by `Q_2_2` with factor 2. The degree-2 columns `P_1_1` and `Q_0_2` hit row 8 only through higher terms of the particular, and those contributions are themselves multiples of 3. The displayed degree-at-most-three families included degree 2 but omitted every degree-4 (and 5–7) digit, in particular `Q_2_2` and the Bockstein column `P_3_1`. Their `/81` row-8 obstruction is a theorem about that smaller family. It is not an emptiness theorem for the full D7 cone, which is consistent of the ranks above.

Nonzero-column degree histograms confirm degree 4 is live as a block (9 of 10 possible columns at `0000`, all 10 at the other two), not a single accidental entry.

### 7. Custody: one implementation, three inputs

Immutable AWS job `/home/ubuntu/jobs/as_q3_full_output_cone_z9_20260825T145301Z` on hostname `ip-172-30-0-45`. `replay_all.sh` loops the same `run_remote.sh` over three `MODEL_OUTPUT` files. Compiler SHA `2d2e0f5f…` is identical in PINNED_INPUTS, every `INPUT.sha256`, MANIFEST, and SOURCE_CLOSURE. Result SHAs differ because the SAT models differ.

| parent | rc | wall | peak RSS | result SHA-256 |
|---|---:|---|---:|---|
| 0000 | 0 | 11.80 s | 22972 KiB | `3e6a559c5b4906b489b9c43350b95259a191c1fbe529656f32b52fdc40bd4f0a` |
| 0270 | 0 | 11.80 s | 22972 KiB | `eb6936b975de974f26e0f571a3e1839ee118d6ed96ea12bf769ecd2f6015d97e` |
| 0513 | 0 | 11.74 s | 22960 KiB | `c8716a9828b42f3b97f89a41e646b5fa8b8744fe5945ebfe1b24a42141b9fd1e` |

stdout `output_sha256` lines match those result SHAs. FREEZE pins the same three plus producer `9ac1edbb…` and archive `c3cb56df…`. JC2_ROOT on the host is the staged closure, not a live checkout of unrelated maps.

`OUTPUT.sha256` self-hash / empty launcher files are snapshot noise, as in the Q3 parent. MANIFEST hashes of the final `result.json` files match FREEZE.

### 8. Strongest licensed theorem

Three pinned reviewed Q3 fibres, complete fixed-D7 output digits at orders 27 and 81, determinant modulo 243, nonempty `Z/9` affine cones of F3-ranks 36 / 43 / 43. Nothing else.

---

## Frozen AWS replay record (not re-launched)

- Host: r6d, `ip-172-30-0-45`
- Job: `/home/ubuntu/jobs/as_q3_full_output_cone_z9_20260825T145301Z`
- Start/end UTC: `2026-08-25T14:53:57Z` – `2026-08-25T14:54:09Z`
- Command (each parent): `python3 …/solve_full_output_cone_z9.py` under `timeout`/`ulimit` from `run_remote.sh`, with `JC2_ROOT` the staged source tree and `MODEL_OUTPUT` the pinned SAT model
- Source archive SHA-256: `c3cb56df1c9ad751bd363a79300185245681ad5524ad5f347bf412e5499c702e`
- Immediate compiler SHA-256: `2d2e0f5fa03c663201157d109a961055ebe1b3daad552b34954f20a633de32f7`

This review did not re-execute that command.
