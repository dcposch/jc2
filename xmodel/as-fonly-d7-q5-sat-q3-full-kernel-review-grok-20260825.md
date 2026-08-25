# Hostile different-model review — AS F-only D7 Q3 whole-kernel producer

| Field | Value |
|---|---|
| Claim under review | Frozen producer: at each of three displayed Q5 predecessor states `base0000`, `base0270`, `base0513`, the entire reviewed chronological Q4 affine fibre plus all ten order-81 degree-four digits `(H4,J4)` admits a consistent affine Q3+terminal system of 4 degree-three `/81` rows and 63 degree-7-through-12 `/243` rows. Rank pairs are `4/4` with kernels of dimensions 14, 10, 10. Displayed particulars reconstruct integer maps whose inherited Q4 row, Q3 row, and 63 terminals vanish at the claimed moduli, and whose degrees 1 and 2 still begin at valuation 3. Scope is three pointwise Q4 fibres |
| Overall verdict | **CONFIRMED** |
| Source/compiler | **CONFIRMED** |
| Replay/custody | **CONFIRMED** of the frozen Box02 run (non-blocking `OUTPUT.sha256` self-hash noise, identical in kind to the Q4 parent review; not used as mathematical evidence). Producer `replay_all.sh` was not re-launched |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (whole Q5 fibre, Q2 through Q0, a complete map modulo 243, all-depth lifting, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian `P_x Q_y - P_y Q_x - 1` over `Z`; exact `/81` on degree 3 and `/243` on degrees 7–12 before any `% 3`; full quadratic design plus five extra mixed F3 probes; independent 67-row matrix, RHS, and RREF; reconstructed integer maps at all three particulars; coefficientwise 3-adic valuations in degrees 0–12; zero-`(H4,J4)` omission control; `81^2` remainder valuation; Q4-kernel columns identically zero |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (unchanged; producer and this review remain uncommitted) |
| Review window (UTC) | 2026-08-25T12:28:00Z – 2026-08-25T12:37:20Z |
| Python | host CPython 3.14.6 |
| Host | `dc-mbp-m2.local`, Darwin arm64. Independent reconstruction ran locally against frozen SAT models and frozen Q4 parent JSON. No AWS compute was launched |

Producer, freeze, case, Q4 parent, and the CONFIRMED Q4-parent review were reread in full before any verdict. No producer, case, prompt, parent, or ancestry file was edited.

---

## Promotion

**Accept `THREE DISPLAYED Q5 PREDECESSOR STATES, EACH WITH ITS COMPLETE REVIEWED Q4 AFFINE FIBRE, ADMIT EXACT Q3 LIFTS: AFTER CONSUMING THE PINNED 68-ROW Q4 GATE AND ADJOINING ALL TEN ORDER-81 DEGREE-FOUR DIGITS (H4,J4), THE 67-ROW SYSTEM OF FOUR DEGREE-THREE /81 ROWS PLUS 63 DEGREE-7-THROUGH-12 /243 TERMINAL ROWS IS AFFINE ON THE WHOLE FINITE CUBE AND CONSISTENT OF RANK PAIR 4/4, WITH KERNELS OF DIMENSIONS 14, 10, 10 AT BASES 0000, 0270, 0513. EACH DISPLAYED PARTICULAR REPLAYS THE INHERITED FIVE Q4 ROWS AND MAKES THE Q3 ROW 0 MODULO 243 AND THE 63 TERMINALS 0 MODULO 729. DEGREES ONE AND TWO REMAIN AT VALUATION 3, SO AN ORDER-81-ONLY Q2/Q1 CONTINUATION IS ILL-TYPED. THE ZERO-(H4,J4) SECTION FAILS Q3 ROWS AT BASE0000 AND BASE0270 AND HAPPENS TO PASS AT BASE0513.`**

On the aligned F-only `D=7` chart, after a reviewed chronological Q4 particular `(H5,J5)` and its affine kernel are consumed:

- Over `Z`, adjoining `P = P5 + 81(H5+H4)`, `Q = Q5 + 81(J5+J4)` with `H4,J4` homogeneous of degree 4 expands as
  `det J(P,Q) - 1 = Δ0 + 81 L + 6561 [H,J]`,
  where `L` is linear in `(H,J)` and `6561 = 3^8`. After exact division of degree 3 by 81, the quadratic remainder has valuation at least 4 and vanishes modulo 3. After exact division of degrees 7–12 by 243, it has valuation at least 3 and vanishes modulo 3. The reduced 67-row map is therefore at most affine. The producer quadratic design (origin, both nonzero multiples of every basis vector, every pair sum) independently confirms that every pure and mixed quadratic remainder is the zero F3-vector; five extra mixed probes (`e1+e2+e3`, `2e1+e2`, `2e1+2e2`, `e1+2e2+e3`, and a wrap-around triple) agree with the affine prediction.
- Degree 3 of `L` is `div(H4,J4) = (H4)_x + (J4)_y` plus a multiple of 3. Independently, at each displayed particular, `Δ3 - Δ3(H4=J4=0) - 81·div` has coefficientwise valuation at least 5, so the four Q3 rows are `div ≡ -g3 (mod 3)` with `g3 = [(Δ0)_3 / 81] mod 3` in the slot convention `[x^i y^{3-i}]`. Homogeneous degree 4 is the correct unknown for this digit: derivatives have degree 3, so they hit Q3 and the already-accepted high rows, and they do not hit degrees 1–2 at order 81.
- The 63 terminal rows are the same over-cap inventory as the Q4 parent, now recomputed after the new degree-four digits. Row count: `4 + (8+9+10+11+12+13) = 67`. Inherited Q4 is not a gate row of this system; it is replayed on the reconstructed integer map by exact `/81` of degree 4.
- Q4 kernel coordinates are variables and remain free. Independently, every Q4-kernel column of the 67-row matrix is the zero vector, and no RREF pivot lies in those columns. The Q3 fibre is the product of the full Q4 fibre with a 6-dimensional affine space in `(H4,J4)`. That is why the counts are `8+6=14` and `4+6=10`.
- The 10-column `(H4,J4)` operator is the same byte-for-byte matrix on all three models (SHA-256 `0206a926c348f7d8e161faba51f8ad1b4f0d26ad59757ed00691a3b14858efc8`). Only the RHS depends on the Q4 particular. Rank 4 with relative pivots on H4 slots 1, 2, 4 and J4 slot 2 is therefore a property of the degree-four divergence in characteristic 3, not a sampling accident.
- 3-adic valuations of `det J - 1` confirm chronology: the displayed particular raises degree 3 from valuation 4 to 5 at base0000 and base0270 (already 5 at base0513) and leaves degrees 7–12 at valuation ≥ 6. Degrees 1 and 2 stay at valuation 3. Degree 0 is exactly absent. These are the literal moduli; they are not a complete map modulo 243.

**Do not promote this to:** coverage of the whole Q5 fibre; a Q2/Q1/Q0 restoration; a complete determinant-one map modulo 243; an all-depth lift; a 3-adic ball around the displayed trit fibre; a counterexample to JC; or any JC2 inference. Do not drop `(H4,J4)` because they happen to vanish at base0513. Do not replace the displayed kernel by a single particular before a Q2 successor. Do not write an order-81-only Q2/Q1 gate: a valuation-3 coefficient is not in the image of multiplication by 81.

**Smallest honest successor.** Retain the whole displayed Q3 affine kernel (full Q4 fibre × 6-dimensional `(H4,J4)` kernel). Introduce order-27 degree-three and degree-two pieces first, recompute carries, and only then adjoin order-81 degree-three/two pieces as a separate exact gate. Reconstruct the integer map and check the new rows by literal determinant.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as a statement about the entire Q5 fibre, or about any Q5 model other than the three consumed Cartier-zero SAT endpoints;
- this gate as Q2 through Q0, or as a complete map with `det J ≡ 1 (mod 243)` in every degree (degrees 1–2 remain at valuation 3);
- this gate as all-depth lifting, algebraization, a counterexample, or JC2;
- zero-`(H4,J4)` as a licensed Q3 section (it fails at base0000 and base0270; passage at base0513 is a pointwise accident of an already-restored degree-three digit);
- any fused order-81-only Q2–Q0 case as licensed by this review;
- the quarantined complete-mod-243 draft `cases/as_fonly_d7_q5_sat_complete_mod243_20260825/` as a successor.

---

## Hostile checks

Tried hard, and failed, to flip the Jacobian orientation `P_x Q_y - P_y Q_x - 1`; to perform `% 3` before exact division; to change the slot convention `[x^i y^{d-i}]`; to make the degree-three inventory 5 rows or the terminal inventory anything other than 63; to leak `6561[H,J]` into the reduced rows (coefficientwise valuation 8 on the quadratic remainder); to find a quadratic or mixed-cubic F3 remainder on the design or on five extra probes; to produce a rank/augmented-rank mismatch; to move a pivot into the Q4 kernel coordinates; to make any Q4-kernel matrix column nonzero; to make the `(H4,J4)` 10-column operator depend on the Q4 particular; to disagree with a frozen matrix SHA, RHS SHA, particular, kernel basis, or JSON byte hash; to make zero-`(H4,J4)` pass Q3 at base0000 or base0270; to make it fail at base0513; to raise degrees 1–2 above valuation 3; to cancel a valuation-3 coefficient by an order-81 increment (`v3(81)=4`); to skip the pinned Q4 parent (its SHA is asserted before `exec`, and the regenerated parent JSON matches the frozen Q4 `full68.json` at all three models); or to promote the displayed F3 fibres to a whole-fibre, complete-map, all-depth, counterexample, or JC2 statement.

### 1. Provenance, orientation, exact division

Transitive pin:

| object | SHA-256 |
|---|---|
| Q3 `solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| Q4 parent `solve_full68.py` | `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4` |
| Q4 restore `replay_full_q4_restore.py` | `9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c` |
| H6 V2 `replay_global_q5_h6_v2.py` | `41e0e74ec4d318bdd33242dcb9053ce53572470570ab5d54f1431184eb789ffa` |
| Q4-parent review (CONFIRMED) | `6a77ff242a4d56461878a25dec7a3321e923f9c29a780ebad6e41d94f9fc6779` |
| remote runner `run_remote.sh` | `6006df0a49d5fcd27fcd2e1137449b7c795b1b75e31a8e7709cc793c7d7ef1e7` |

`solve_q3.py` SHA-pins and `exec`s the Q4 parent before building any Q3 row. The Q4 parent SHA-pins the restore, which SHA-pins H6 V2, and so on down the already-reviewed chain. Independent reconstruction uses a locally written Jacobian with the same orientation as the parent helper; the two determinants agreed as dictionaries at every evaluated point.

`divide_exact` refuses any coefficient not divisible by the divisor. Every design point, every extra probe, and all three particulars were exact at `/81` in degree 3 and `/243` in degrees 7–12. Reduction modulo 3 is applied only after that division, and only inside `row`.

Consumed SAT models are the same three Boolector endpoints already confirmed by the Q4 review:

| base | model SHA-256 | regenerated Q4 JSON SHA-256 |
|---|---|---|
| 0000 | `dbb405ac9ab12b9d4b01df6e934ac6979609dfd4eabbe2ccf65a65aaf8cdcb81` | `2641dc2946aad7e91bcf5fce94006903da4eb6dfc6df361da0cce32f6594f246` |
| 0270 | `05627048aa3e648b975acc1ed47e97a451241c3544e7fa5b58a7c42a1cd4be03` | `c801d191e472d5933a364f68bdce8d5604d3adead9ea6f836463dbf819c3eb05` |
| 0513 | `9c319fe4d1a576569869cbccbcc7411fee5eb12dedaa4e6a820a395263820200` | `96dcf7fa7b9dd2a0424ac2834d0135dc41df246d9eaeed3ec4242c6f001b1786` |

### 2. Row inventory and inherited Q4 replay

Degree 3 has four monomials. Degrees 7 through 12 have `8+9+10+11+12+13 = 63`. The producer asserts both lengths on every evaluation. Independent reconstruction asserts the same and replays, at each displayed particular, the inherited five Q4 rows by exact `/81` of degree 4: all three return `[0,0,0,0,0]`. Degree 4 remains divisible by 243; degrees 7–12 remain divisible by 729. Q4 is a replayed parent identity, not a sixth Q3 gate row.

### 3. Affine cube, matrix, RREF

Design counts are `1 + 2n + C(n,2)`: 190 at `n=18`, 120 at `n=14`. Independent columns, RHS `(-constant) mod 3`, and RREF:

| base | vars | design | rank | aug | pivots | particular `H4 \| J4` | ker | `#F3` | matrix SHA-256 |
|---|---:|---:|---:|---:|---|---|---:|---:|---|
| 0000 | 18 | 190 | 4 | 4 | 9,10,12,15 | `(0,2,0,0,2) \| (0,0,1,0,0)` | 14 | 4782969 | `0ef37958a09d4c0d...` |
| 0270 | 14 | 120 | 4 | 4 | 5,6,8,11 | `(0,0,0,0,2) \| (0,0,0,0,0)` | 10 | 59049 | `976ed4dcd353702b...` |
| 0513 | 14 | 120 | 4 | 4 | 5,6,8,11 | `(0,0,0,0,0) \| (0,0,0,0,0)` | 10 | 59049 | `976ed4dcd353702b...` |

Particulars match the producer on the nose, not merely up to kernel. Producer kernel vectors are a basis of the independent nullspace. Frozen JSON bytes replay identically. Relative to the `(H4,J4)` origin, all three systems pivot on the same four slots; the 0270 and 0513 matrices are the same bytes because the Q4-kernel columns are zero and the 10-column operator does not see the Q4 particular.

### 4. Integer maps and valuation tables

Each displayed particular was rebuilt as `P5 + 81(H5+H4)`, `Q5 + 81(J5+J4)` with `H5,J5` the Q4 particular (kernel coordinates of the particular are zero). Literal determinant checks:

- Q4 row `/81 ≡ 0 mod 3`, degree 4 divisible by 243;
- Q3 row `/81 ≡ 0 mod 3`, degree 3 divisible by 243 after the lift;
- 63 terminals `/243 ≡ 0 mod 3`, degrees 7–12 divisible by 729.

Independent minima of `v3(det J - 1)` match the producer tables:

| base | pre `0..12` | post `0..12` |
|---|---|---|
| 0000 | `∞,3,3,4,5,5,5,6,6,6,6,6,7` | `∞,3,3,5,5,5,5,6,6,6,6,6,7` |
| 0270 | `∞,3,3,4,5,5,5,6,6,6,6,6,6` | `∞,3,3,5,5,5,5,6,6,6,6,6,6` |
| 0513 | `∞,3,3,5,5,5,5,6,6,6,6,6,6` | `∞,3,3,5,5,5,5,6,6,6,6,6,6` |

Degree 0 is absent (no nonzero constant term) at all three points, before and after. Degrees 1 and 2 are not divisible by 81.

### 5. Zero-`(H4,J4)` omission control

`equations(0)` is the Q4 particular with `H4=J4=0`. Nonzero rows of that vector are Q3 slots, never terminals (the Q4 parent already killed degrees 7–12). Independently:

- base0000 fails slots `(0,2,3)` i.e. `[y^3]`, `[x^2 y]`, `[x^3]`;
- base0270 fails slot `3` i.e. `[x^3]`;
- base0513 fails nothing, because degree 3 already has valuation 5 at the Q4 particular, so `/81` is `0 mod 3`.

Passage at base0513 does not license omitting `(H4,J4)`. The 10-column operator still has rank 4; dropping those digits would discard a 6-dimensional fibre even at the point where the displayed particular happens to be the origin, and would be inconsistent at the other two points.

### 6. Typed consequence for Q2/Q1

After this gate, degrees 1 and 2 still have minimum valuation 3. An order-81 increment contributes `81 L` with `v3 ≥ 4`, so it cannot cancel a valuation-3 coefficient. Homogeneous degree 4 at order 81 has derivatives of degree 3 and does not hit degrees 1–2 at this modulus in any case. The source-honest next digit is therefore an order-27 degree-three/two piece, with carries recomputed, and only afterwards an order-81 degree-three/two piece. An order-81-only Q2/Q1 continuation is ill-typed at all three displayed points.

### 7. Scope

This is exactly three Cartier-zero Q5 SAT endpoints and their complete displayed Q4 affine fibres. The F3 counts `3^14` and `3^10` are trit points of the coefficient cube, not p-adic neighbourhoods. Degrees 1–2 remain below 243, so this is not a complete map modulo 243. The producer refusal list is accurate and is hereby reimposed.

Non-blocking custody noise, not used against the math: each AWS `OUTPUT.sha256` records a self-hash taken while the file was being written, which does not equal the file's final hash; every other listed job-dir file hashes as recorded. The AWS source closure lists empty-ish AppleDouble `._*` paths, as in the Q4 parent review. `aws_run/FREEZE.sha256` is present in the tree and consistent with its three listed objects, but is not itself a row of `MANIFEST.sha256`.

---

## Independent reconstruction custody

Local workspace `/tmp/as_q3_full_kernel_review_scratch/` (not a producer artifact). The reconstruction consumes the pinned Q4 parent for `P5,Q5` and the Q4 kernel, then rebuilds the Jacobian, design, matrix, RREF, integer maps, and valuations with independent helpers.

| object | SHA-256 |
|---|---|
| independent review script | `32db7bf8cd5c1c301235cd5c03be2f333b9ff39af4139f92d4b7f0ce9e713152` |
| independent result JSON | `0f5fa8f3fb17357bd702dbdf5719a713ba1575255a62140bb70e25905dad5aa7` |
| live base0000 `q3.json` | `89c9b8bfb4c46b566e10e7f5716502b0a3b6f64af29a5f4e14234cc09b945187` |
| live base0270 `q3.json` | `9016e7737c7f3a31107a80f4da91e1e8cec7be686569cd548e55e135fcec4dfb` |
| live base0513 `q3.json` | `e2711128f358f5b65f215a2898ccf90fa10a7e1e6908ccdde7c9a4410290b4bb` |
| `(H4,J4)` 10-column operator | `0206a926c348f7d8e161faba51f8ad1b4f0d26ad59757ed00691a3b14858efc8` |

---

## Frozen AWS producer replay (not re-launched)

Host `ip-172-30-0-186` (Box02). Job `/home/ubuntu/jobs/as_q5_sat_q3_full_kernel_20260825T121434Z`. All three lanes started `2026-08-25T12:15:22Z`. Stderr is only bounded `/usr/bin/time -v` custody. Exit status 0 on all three.

| base | command (timed) | stdout SHA-256 | stderr SHA-256 | wall | peak RSS | INPUT SHA-256 |
|---|---|---|---|---|---:|---|
| 0000 | `python3 .../solve_q3.py` with `MODEL_OUTPUT=.../base_0000_0000000/solver.stdout` | `ba542ad64ea7c47d24f308d72cce83b309411ccbbb559c80036869820cae0f03` | `b4f2598357d2d33078b03a6ba53b2206fa9a121156b85dd52b588a23b0681aa9` | 18.54 s | 21784 KiB | `b7c9312a32be744dc46f0f2b98f283f1f0fd7adc9f3b497ab0ad3ebd2d455931` |
| 0270 | same runner, `base_0270_0101000` | `06940d9b0be3258be69d2dc63904042f75d9bc3729fa71712a641bf7dd66e5d8` | `8c00e8595208d7c16bc30503f83427343dc8a0f36e002eaa6ad191498fbb4f54` | 18.90 s | 21736 KiB | `68185c3e0086df08d01396d16df5b1f5713c29fc5cfc094d764174534ea2a00b` |
| 0513 | same runner, `base_0513_0201000` | `12bb39e2c17ba15f9b2f135e839a36ebbee60ae1e1572384b08ee7f49412c9e7` | `61dad071c3ee28ff4630b8838c3780b6d57b649af86b25aa5c174364f478eb52` | 21.17 s | 21728 KiB | `e5c21a977ee02101bc877e6bb13a6f9d72ca05fd767cdbbdc54acef853e0bf79` |

Each `INPUT.sha256` pins `PREREGISTRATION.md`, `solve_q3.py`, `run_remote.sh`, the Q4 parent, and the SAT model. Source hashes match the live tree. `replay.rc` is `0` with SHA-256 `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` on all three lanes.

---

## Consumed hashes

| path | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-producer-20260825.md` | `737b45f6509c959fa45a55158cdd705462f5de804827cf0c00e24ca0ffca7a31` |
| `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-review-grok-20260825-prompt.md` | `07a408a2063040ca0c1e9883f8c1ff93549196643f1628ded441b4c3da517c04` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/PREREGISTRATION.md` | `c67711bc73b5fee9a2ed1619898741b31f2e112c961906dd4b0e55c02af56b91` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/run_remote.sh` | `6006df0a49d5fcd27fcd2e1137449b7c795b1b75e31a8e7709cc793c7d7ef1e7` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/replay_all.sh` | `c279212fd75f047d976235a69cb71c389b9b6f0c936f6cdc18f96042fa1a578b` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/SOURCE_MANIFEST.sha256` | `9fbaec99c4f8f9381d760230207eb5676af1f2dd4c2a6b5e2b1ef70f5a19b61f` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/FREEZE_SOURCE.txt` | `8a4e87b7257c24661d80dc283dda8670c387aa982a365274dccd4d227e7c9d43` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/MANIFEST.sha256` | `825637233981ffb4823b87a8a40e874186cc61058871db5bb722be1b284ec048` |
| `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/FREEZE.sha256` | `9be7bfc59564e368fa871707f52eff5ae2ee597169055e5004b4ba6335a85582` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/solve_full68.py` | `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4` |
| `xmodel/as-fonly-d7-q5-sat-q4-full68-review-grok-20260825.md` | `6a77ff242a4d56461878a25dec7a3321e923f9c29a780ebad6e41d94f9fc6779` |

Every SHA pin in the Q3 source manifest, freeze, and MANIFEST was checked against the live file. Every MANIFEST row hashed as recorded.

---

## Verdict

Source/compiler: **CONFIRMED**.

Replay/custody: **CONFIRMED** of the frozen Box02 run recorded above.

**CONFIRMED.**
