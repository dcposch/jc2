# Hostile different-model review — AS F-only D7 full chronological Q4 68-row gate

| Field | Value |
|---|---|
| Claim under review | Frozen producer: three exact Boolector models of the displayed 197-row Q5 formula, after nested-integer parent replay, each admit a consistent 68-by-12 F3 affine system in the homogeneous degree-five 81-digit `(H5,J5)`. Rank pairs are `4/4`, `8/8`, `8/8` at structural bases 0000, 0270, 0513, with particulars `011000\|000000`, `022000\|210000`, `001001\|120120` and kernels of dimensions 8, 4, 4. Each particular reconstructs an integer map whose degree-four Jacobian row vanishes modulo 243 and whose 63 terminal rows of degrees 7 through 12 vanish modulo 729. The J-only five-row section is a correct Q4 control and a mandatory negative control against omitting the terminal 63. Scope is pointwise at these three models |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks below; whole Q5 fibre, Q3 through Q0, a complete map modulo 243, all-depth lifting, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian expansion over `Z` at all twelve 81-digit basis vectors; independent 68-by-12 matrix, RHS, and RREF; exact division-by-81 and division-by-243 on the reconstructed determinant; 3-adic valuations of every total degree; frozen-producer byte replay of all three models; dedicated 197-row H6 V2 parent replay at base0270; two-row omission negative control at base0270 |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (unchanged; producer bytes remain uncommitted) |
| Review window (UTC) | 2026-08-25T12:15:05Z – 2026-08-25T12:23:39Z |
| Python | host CPython 3.14.6 |
| Host | `dc-mbp-m2.local`, Darwin arm64. SAT models copied from Box02 (`34.203.207.55`). Independent replay ran locally (~7 s/model). No AWS compute was launched |

Producer, freeze, case, parent replay, and transitive source-pinned ancestry were reread in full before any verdict. No producer, case, prompt, or ancestry file was edited.

---

## Promotion

**Accept `THREE EXACT Q5 SAT MODELS ADMIT POINTWISE CHRONOLOGICAL Q4 LIFTS: AFTER THE COMPLETE 197-ROW NESTED-INTEGER PARENT REPLAY, THE 68-BY-12 F3 SYSTEM IN HOMOGENEOUS DEGREE-FIVE 81-DIGIT (H5,J5) IS CONSISTENT OF RANK PAIR 4/4, 8/8, 8/8 AT BASES 0000, 0270, 0513, WITH AFFINE FIBRES OF SIZES 3^8, 3^4, 3^4. EACH DISPLAYED PARTICULAR MAKES THE DEGREE-FOUR JACOBIAN ROW 0 MODULO 243 AND THE 63 TERMINAL ROWS OF DEGREES 7 THROUGH 12 0 MODULO 729. THE FIVE-ROW J-ONLY SECTION IS A CORRECT Q4 CONTROL AND IS INSUFFICIENT AT BASE0270 AND BASE0513 BECAUSE IT BREAKS TERMINAL ROWS.`**

On the aligned F-only `D=7` chart `P = x - x^3 + 3U + 9C + 27W + 81(H7+H6)`, `Q = y + 3V + 9D + 27Z + 81(J7+J6)`, after a Q5 SAT model has been replayed:

- Over `Z`, adjoining `P4 = P5 + 81 H5`, `Q4 = Q5 + 81 J5` with `H5,J5` homogeneous of degree 5 expands as
  `det J(P4,Q4) - 1 = Δ0 + 81 L + 6561 [H5,J5]`,
  where `L = (H5)_x Q5_y + P5_x (J5)_y - (H5)_y Q5_x - P5_y (J5)_x`.
- Degree 4 of `L` is `(H5)_x + (J5)_y` plus a multiple of 3. Consequently the degree-four change is `81 · div(H5,J5)` modulo 243. The five Q4 rows are `div ≡ -g4 (mod 3)` with `g4 = [(Δ0)_4 / 81] mod 3` in the slot convention `[x^i y^{4-i}]`. The Cartier slot `g4[2] = [x^2 y^2]` vanishes on every consumed model, as required by the parent Q4 restore.
- Degrees 7 through 12 of `L` begin at the 3-coefficient
  `A (J5)_y + (H5)_x v_y - u_y (J5)_x - (H5)_y v_x`
  with `A = U_x - x^2`. That is exactly the producer's `fourth_digit_cross`. After dividing by 243 one has the 63 terminal F3 rows `cross ≡ 0`, because the Q5 parent already forces `(Δ0)_{7..12} ≡ 0 (mod 729)` and `81^2 = 6561 ≡ 0 (mod 729)`.
- Homogeneous degree 5 is the correct unknown for this digit: derivatives have degree 4, so they hit Q4 and the already-accepted high rows, and they do not hit Q3. The 68-row count is `5 + (8+9+10+11+12+13) = 68`. No generic localization is used.
- Independent integer Jacobian columns at all twelve basis vectors reproduce the frozen matrices, RHS signs, RREF ranks, particulars, and kernel dimensions at all three models. Frozen JSON bytes replay exactly.
- The J-only section `H5=0`, `J5 = g0 y^5 - g1 x y^4 + g3 x^3 y^2 - g4 x^4 y` solves the five Q4 rows whenever `g2=0`, because `5 ≡ -1 (mod 3)` on the extreme slots and the Cartier slot is untouched. At base0270 it fails terminal indices 3 and 4 (degree-7 slots `[x^3 y^4]`, `[x^4 y^3]`); at base0513 it fails 3, 4, 6, 7. At base0000 that section happens to kill the terminals too, and is correctly not used as a negative control.
- 3-adic valuations of `det J - 1` confirm chronology and the two moduli: the 68-row particular raises degree 4 from valuation 4 to 5 (modulo 243) and leaves degrees 7–12 at valuation ≥ 6 (modulo 729). Degrees 5 and 6 stay at valuation 5. Degrees 1–3 are not improved and remain below 243.

**Do not promote this to:** coverage of the whole Q5 fibre; a Q3–Q0 restoration; a complete determinant-one map modulo 243; an all-depth lift; a 3-adic ball around the displayed trit fibre; a counterexample to JC; or any JC2 inference. Do not drop the 63 terminal rows after taking a divergence preimage. Do not replace the displayed kernel by a single particular before a Q3 successor. Do not conflate these Cartier-zero models with the earlier one-row `[x^2 y^2]` obstruction at a different base-513 Q5 state.

**Smallest honest successor.** Retain the whole displayed `(H5,J5)` affine kernel and reimpose every lower-degree 81-digit row (Q3 through Q0) as a separate exact gate, then reconstruct the integer map and check the new rows by literal determinant. A five-row Q4 section is not a licensed predecessor of that successor.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as a statement about the entire Q5 fibre, or about any Q5 model with nonzero Cartier slot `g2`;
- this gate as Q3 through Q0, or as a complete map with `det J ≡ 1 (mod 243)` in every degree (degrees 1–3 remain at valuations 3 or 4);
- this gate as all-depth lifting, algebraization, a counterexample, or JC2;
- five-row J-only restoration as a chronological Q4 lift at base0270 or base0513;
- the 66-row system obtained by omitting the two failing degree-7 terminals at base0270;
- the draft fused Q3–Q0 case `cases/as_fonly_d7_q5_sat_fused_q3_q0_20260825/` as licensed by this review;
- the quarantined complete-mod-243 draft `cases/as_fonly_d7_q5_sat_complete_mod243_20260825/` as a successor.

---

## Hostile checks

Tried hard, and failed, to flip the Q4 RHS sign; to replace `div(H5,J5)` by the unreduced first-order Jacobian action `L` in degree 4 (the extra terms are `0 mod 3`, so `81 L ≡ 81 div (mod 243)`); to make `fourth_digit_cross` disagree with `(Δ - Δ0)_{7..12}/243` at any of the twelve basis vectors; to change the slot convention `[x^i y^{d-i}]`; to find an inexact division by 81 in degree 4 or by 243 in degrees 7–12; to make the quadratic `81^2[H5,J5]` contribute modulo 243 or 729 (`6561 = 3^8`); to produce a rank/augmented-rank mismatch or an empty kernel claim; to make the J-only section fail a Q4 row; to make the J-only section pass the 63 terminals at base0270 or base0513; to omit terminal indices 3 and 4 at base0270 and still have a chronological lift (the 66-row system becomes consistent of rank 6, the J-only vector solves it, and the dropped degree-7 coefficients `38151` and `134379` have 3-adic valuation 5, remainder `243` modulo `729`); to break degrees 5–6 or 0–3 by adjoining `(H5,J5)` at the claimed moduli; to skip the 197-row parent (`row_shapes 20 5 12 11 23 22 19 9 7 6 63` and `PASS-AS-GLOBAL-Q5-H6-DIRECT-REPLAY` occur, and the H6 JSON hash matches the pointer stored by the Q4 restore); or to promote the displayed F3 fibres to a whole-fibre, complete-map, all-depth, counterexample, or JC2 statement.

### 1. Orientation and constants

Slot `i` of a degree-`d` row is `[x^i y^{d-i}]`. Homogeneous degree-five coefficients are `(c_0,...,c_5)` for `c_i [x^i y^{5-i}]`.

Let `Δ0 = det J(P5,Q5) - 1`. On each consumed model `g4 = row(Δ0_4 / 81, 4)` is
`[2,1,0,0,0]`, `[0,1,0,0,0]`, `[1,2,0,1,2]` at bases 0000, 0270, 0513, and the Cartier coordinate `g4[2]` is 0. The five Q4 equations are `div(H5,J5) = -g4` over F3. Independently, for every basis vector, `(det J(P5+81H, Q5+81J) - Δ0)_4 / 81 ≡ div (mod 3)` and the integer remainder after subtracting `81 · div` is `0 mod 243`.

The 63 terminal equations are `fourth_digit_cross(H5,J5) = 0` in degrees 7 through 12. Independently, those Jacobian columns divided by 243 agree with `fourth_digit_cross` at every basis vector. The closed form
`A J_y + H_x v_y - u_y J_x - H_y v_x`
is the 3-coefficient of the first-order action, with `A = U_x - x^2` from the charged source.

### 2. Matrix, RHS, RREF

Independent Jacobian columns, the producer `div`/`cross` columns, and the frozen `matrix_sha256` agree at all three models. RHS is `(-g4) + 63 zeros`. Independent RREF:

| base | rank | aug | pivots | particular `H5 \| J5` | ker dim | `#F3` | matrix SHA-256 |
|---|---:|---:|---|---|---:|---:|---|
| 0000 | 4 | 4 | 1,2,4,5 | `011000 \| 000000` | 8 | 6561 | `5153052fe31e7d78...` |
| 0270 | 8 | 8 | 1,2,4,5,6,7,9,10 | `022000 \| 210000` | 4 | 81 | `812646f1cdf47e77...` |
| 0513 | 8 | 8 | 1,2,4,5,6,7,9,10 | `001001 \| 120120` | 4 | 81 | `662f868ba1c57c22...` |

Particulars match the producer on the nose, not merely up to kernel. Producer kernel vectors are a basis of the independent nullspace. Frozen JSON bytes replay identically.

### 3. 197-row parent precedes consumption

`solve_full68.py` SHA-pins `replay_full_q4_restore.py` (`9fa64980...`) and `exec`s it before building the 68-row matrix. That parent SHA-pins H6 V2 (`41e0e74e...`), which SHA-pins and patches the nested replay down through Q6 high, global predecessor, and the Q9/Q10/Q11 shard compilers. Dedicated H6 V2 replay at base0270 prints

```text
row_shapes 20 5 12 11 23 22 19 9 7 6 63
PASS-AS-GLOBAL-Q5-H6-DIRECT-REPLAY
```

The displayed inventory sums to 197. Its JSON SHA-256 `6eaa4cb41b74b371fb165e714c0f58d37e74059954b3d06a2f3381b1417eac47` equals the `parent_output_sha256` stored by the frozen Q4 restore at that model. `ALLOW_OMITTED_Q5_GATE` was unset. If any of the 197 asserts failed, the 68-row solver could not have written a SAT JSON.

### 4. Exact divisions and moduli

`divide_exact` refuses any coefficient not divisible by the divisor. Independent reconstruction of each particular uses `/81` on degree 4 and `/243` on degrees 7–12, then the literal conditions `Δ_4 ≡ 0 (mod 243)` and `Δ_{7..12} ≡ 0 (mod 729)`. Minimum terminal valuation after the 68-row particular is 6 at every model. The Q4 valuation rises 4 → 5. These are the literal moduli named by the producer; they are not 81, 243 for terminals, or 2187.

J-only at base0270 restores Q4 (valuation 5) and drops degree 7 from valuation 6 to 5, which is why five-row restoration is not chronological.

### 5. Independent replay and two-row omission

SAT models were copied from Box02 path
`/home/ubuntu/jobs/as_q5_q4_cartier_79base_fanout_20260825T1145Z/base_*/solver.stdout`
and hashed before replay. Frozen `solve_full68.py` was exec'd locally against those bytes. All three JSON outputs matched the frozen AWS files bit-for-bit. Source, source-manifest, freeze-source, and MANIFEST hashes match the producer custody block.

At base0270 the J-only vector solves the five Q4 rows and fails terminal indices 3, 4. Omitting those two matrix rows (degree-7 slots `[x^3 y^4]`, `[x^4 y^3]`) yields a consistent 66-by-12 system of rank 6. J-only solves it. The dropped integer coefficients are `38151` and `134379`, each `243 mod 729`. The 68-row particular makes the same monomials `105705` and `56133`, both `0 mod 729`. This is the load-bearing omission control: dropping the two failing terminals falsely certifies a Q4 section that is not chronological.

### 6. Chronological-lift and scope attack

"Chronological Q4 lift" here means: at one already-replayed Q5 SAT model, choose the 81-digit homogeneous degree-five pair so that the next un-restored degree (degree 4) becomes `0 mod 243` while every already-accepted higher-degree row stays at its parent modulus. The 68-row system is exactly that gate for these maps (Jacobian total degree ≤ 12). It is not:

- a whole-fibre statement (three Cartier-zero SAT endpoints only);
- a lower-row statement (valuations of degrees 1, 2, 3 stay 3, 3, and 4 or 5);
- a complete-map statement (`det J ≡ 1 (mod 243)` fails in degrees 1–3);
- an all-depth lift, a 3-adic ball, a counterexample, or JC2.

The displayed counts `3^8`, `3^4`, `3^4` are F3 affine points of `(H5,J5)` with trit coefficients in `{0,1,2}`, not p-adic neighbourhoods. A Q3 successor is licensed only if it retains that kernel and is constructed separately; this review does not confirm any such successor. The producer refusal list is accurate and is hereby reimposed.

Non-blocking custody noise, not used against the math: each AWS `OUTPUT.sha256` records a self-hash taken while the file was being written, which does not equal the file's final hash; every other listed job-dir file hashes as recorded. The AWS source closure lists empty-ish AppleDouble `._*` paths. The nested H6 JSON is overwritten in the job directory by the Q4-restore JSON; its hash is retained and was independently reproduced.

---

## Independent replay custody

Local workspace `/tmp/as_q4_full68_review/` (not a producer artifact):

| object | SHA-256 |
|---|---|
| independent review script | `47af07738b1c1bab82826d83d48fa5aec5d0e67cc1bfb2b4fc998696ed0cd336` |
| independent result JSON | `5b241a20b6452f70ddc10e4cc07ee44320777578c225286bebb899dfae47492c` |
| base0270 SAT model | `05627048aa3e648b975acc1ed47e97a451241c3544e7fa5b58a7c42a1cd4be03` |
| base0000 SAT model | `dbb405ac9ab12b9d4b01df6e934ac6979609dfd4eabbe2ccf65a65aaf8cdcb81` |
| base0513 SAT model | `9c319fe4d1a576569869cbccbcc7411fee5eb12dedaa4e6a820a395263820200` |
| live base0270 `full68.json` | `c801d191e472d5933a364f68bdce8d5604d3adead9ea6f836463dbf819c3eb05` |
| live base0270 H6 V2 JSON | `6eaa4cb41b74b371fb165e714c0f58d37e74059954b3d06a2f3381b1417eac47` |
| live base0270 H6 V2 stdout | `d1f6908d4b92ac771edb7f3700a262f375a472080915184c6f252bb8769d4b9c` |

AWS origin of the SAT models: Box02, job
`/home/ubuntu/jobs/as_q5_q4_cartier_79base_fanout_20260825T1145Z/`.
Producer AWS job: Box02 host `ip-172-30-0-186`,
`/home/ubuntu/jobs/as_q5_sat_q4_full68_20260825T120159Z`, run window
`2026-08-25T12:02:47Z` – `2026-08-25T12:03:06Z` at base0270.

---

## Consumed hashes

| path | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-q5-sat-q4-full68-producer-20260825.md` | `8407cabc700df48ccde9ca894d5e6a8944434cc7de65403ff217ceddc4251b1a` |
| `xmodel/as-fonly-d7-q5-sat-q4-full68-review-grok-20260825-prompt.md` | `6b45e8620b833d8e12589a7b1a54d86bbe49ca7cc39541e79b8cb070a65af554` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/solve_full68.py` | `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/PREREGISTRATION.md` | `feb9474569b1017ce01c9b146d59b9ee66e555254831cca1f4bb5d3c554d22e0` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/run_remote.sh` | `bae19168d1264194ce45b7095dd66a5e4c7d8e21cc5b48d17d3908255f92eb01` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/SOURCE_MANIFEST.sha256` | `e8f7e1c0921d83415379f59307087edda9e3c9c9edf5103fec09411ab3de9a50` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/FREEZE_SOURCE.txt` | `c4413e46ee76e8ebe6c023ddca419a6b7106f64ee67ff159f87446fdb4886ceb` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/FREEZE.txt` | `43290ee63e173fb54d16db5b31528a4347a4dcb1051180c03cca9031f04f0e46` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/MANIFEST.sha256` | `ff53c21d6aca58dbe17f8394231d51f80066ec87c4057d2a389e83d55d6d11bb` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/aws_run/FREEZE.sha256` | `49e805ae9331981c6f8888acdc08f4feff41984283f074a647daa8e07696d3a2` |
| `cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825/aws_run/full_source_closure.sha256` | `18728cc3f0186228267bb36569d9cae2788b4b3778d8234ce6e526dbb2c78dfa` |
| `aws_run/base_0000_0000000/full68.json` | `2641dc2946aad7e91bcf5fce94006903da4eb6dfc6df361da0cce32f6594f246` |
| `aws_run/base_0270_0101000/full68.json` | `c801d191e472d5933a364f68bdce8d5604d3adead9ea6f836463dbf819c3eb05` |
| `aws_run/base_0513_0201000/full68.json` | `96dcf7fa7b9dd2a0424ac2834d0135dc41df246d9eaeed3ec4242c6f001b1786` |
| `aws_run/base_0000_0000000/q4_only_parent.json` | `f1404cd7905350010e90a5e05028efe30f78e1d73d67cac817cd23b7bce35d67` |
| `aws_run/base_0270_0101000/q4_only_parent.json` | `eba39aa80a75b30982d82ed4f9010ee3af2fa85ae46237d339c939c01eecfaa6` |
| `aws_run/base_0513_0201000/q4_only_parent.json` | `1b25f7d142f04a09228fc085b3750ad2790ec39ebe9561a998a4e9b65204ccaa` |
| `aws_run/base_0000_0000000/OUTPUT.sha256` | `6ab964a6901c3b5fd6793fcb2ae1b362f786125d6bc5420ccdee61512e44b6f3` |
| `aws_run/base_0270_0101000/OUTPUT.sha256` | `48b06f5c66eedcb3af2fa328a57f603a0ee21a2a565b29a8c3c3ea075d91c751` |
| `aws_run/base_0513_0201000/OUTPUT.sha256` | `0ef9b9bcf14ca1f977d96db43d0b35b5c51ec2c3f90b91b41aa05b1ad14f6e31` |
| `cases/as_fonly_d7_q5_sat_full_q4_restore_20260825/replay_full_q4_restore.py` | `9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c` |
| `cases/as_fonly_d7_q5_sat_full_q4_restore_20260825/SOURCE_MANIFEST.sha256` | `d52e6d6dbb1823d7d8c646d5f465e6a2b9cdfb5b700907b3fc7639bd76d0c8db` |
| `cases/as_fonly_d7_q5_sat_full_q4_restore_20260825/PREREGISTRATION.md` | `eb667c3ff3f6f20821ac740b36f43b43870fb74d4875dceabcd79396fb7f580e` |
| `cases/as_fonly_d7_global_q5_h6_replay_erratum_20260825/replay_global_q5_h6_v2.py` | `41e0e74ec4d318bdd33242dcb9053ce53572470570ab5d54f1431184eb789ffa` |
| `cases/as_fonly_d7_global_q5_h6_20260825/replay_global_q5_h6.py` | `75e153c3ea2a0de9ce2bf26ba13893e44a4092cd8b1bdd1d45256f12ac023eea` |
| `cases/as_fonly_d7_global_q6_high_20260825/replay_global_q6_high.py` | `e8361c81609afe6365d5eba8d4fda9bdf4b3dd4a44869fbcba330c614847c77c` |
| `cases/as_fonly_d7_global_predecessor_rawq7_20260825/replay_model.py` | `b4acf93af94774e124502f3b6cd20be40b10197a808eb7b8ad0d7c92395b99d4` |
| `cases/as_fonly_d7_vertical_q9_state_gate_20260825/compile_shard.py` | `54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2` |
| `cases/as_fonly_d7_vertical_next_top10_corrected_shards_20260825/compile_shard.py` | `3837508e6f0ffabbcdecfdc19a9ade1e4068bbece6aba80cfdc6b9937e25a686` |
| `cases/as_fonly_d7_vertical_next_top_corrected_shards_20260825/compile_shard.py` | `349ea50953ba6e92d2023ff60965e484eb06e85962bded09d3bfa9b1307dcc30` |
| `cases/as_fonly_d7_vertical_next_top_shards_20260825/compile_shard.py` | `64bbd0e15d0e10296ca81867a390338e41814ca575729e98bf2bd315a33bf893` |

Every SHA pin in that ancestry chain was checked against the live file. Every MANIFEST and SOURCE_MANIFEST row was checked against the live file.

---

## Verdict

**CONFIRMED.**
