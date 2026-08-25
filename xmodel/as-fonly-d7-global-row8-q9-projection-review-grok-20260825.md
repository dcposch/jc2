# Hostile different-model review — AS F-only D7 global Q9 projection of the row-8 scalar

| Field | Value |
|---|---|
| Claim under review | Frozen corrected producer: over all 79 compatible structural bases of the corrected current Q10 source, project every complete 32-variable Q9 affine fibre to `(q1,q2,q3,q4)=(c2_1,c2_2,d2_0,d2_1)` and census the source-oriented scalar `omega=carry(q1+2q3)+2h·carry(2q2+q4) mod 3`; the scalar is uniformly distributed on every nonempty fibre, hence is not an obstruction at Q9 alone |
| Overall verdict | **CONFIRMED** |
| Finite projection/census theorem | **CONFIRMED** |
| Downstream restoration / mod-243 / all-depth / JC2 | **REFUSED** (not claimed by the producer body; not licensed here) |
| Strongest licensed scope | `omega` is no obstruction at Q9 alone; each of the 11,881 current nonempty Q9 fibres has `omega=0` completions. Not Q8 through Q3 restoration; not a complete map modulo 243; not all-depth; not a counterexample; not JC2 |
| Replay/custody | **CONFIRMED** of the frozen Box02 V2/V3 runs recorded below (non-blocking `OUTPUT.sha256` self-hash / empty-launcher snapshot noise, identical in kind to prior Q9/Q3 reviews; not used as mathematical evidence). No AWS re-launch. This review used read/search only |
| Smallest failing identity | none inside the displayed Q9 projection |
| Smallest missing hypothesis | none for the Q9-only statement; Q8 through Q3 restoration is **missing by design** and is not a defect of this package |
| Evidence tier | SHA-pinned exec of the corrected Q10-to-Q9 compiler `54d05ebf…`; integer `E/3+M` reconstructed on every projected 4-tuple with monomial `(i,d-i)` and axis `0=x`; closed formula asserted before counting; exact F3 RREF/kernel, 4-coordinate image basis, multiplicity `3^(ker_dim-proj_rank)`; 27/27 rc-zero V2 and V3 shards; hand-summed q10/q9/completion/omega/class totals from frozen `runner.stdout`; V3 rank-pair/fibre-size controls matching the CONFIRMED Q9 parent census; V1 swapped-label source retained as a negative control |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Review constraint | read/search only; no Bash, Python, CAS, solver, web, or network; no producer/case/ledger/prompt edits; all substantive replay is the frozen AWS run |
| Review window (UTC) | 2026-08-25 |

Producer report, portable case, preregistration and erratum, corrected V2/V3 sources, V1 swapped source, runner, aggregate script, all 54 extracted shard payloads and rc/stdout/SOURCE files, both aggregates, both manifests, the consumed Q9 compiler, the CONFIRMED Q9 source-state review, and the 79-base inventory were reread before any verdict. No producer, case, prompt, parent, or ancestry file was edited.

---

## Required decisions

### Finite Q9 projection theorem

**Correct.** On the 33,225 corrected-Q10 source states, the complete 32-variable Q9 affine fibre is reconstructed from the SHA-pinned compiler, projected exactly onto `(c2_1,c2_2,d2_0,d2_1)`, and counted with constant multiplicity. The source-oriented scalar is

```text
omega = floor((q1+2*q3)/3) + 2*h*floor((2*q2+q4)/3)  (mod 3).
```

It is uniformly distributed on every one of the 11,881 nonempty fibres. Every such fibre has `omega=0` completions. Exact totals, hand-summed from the frozen 27+27 shard stdout records and cross-checked against the shard JSON, are

```text
Q10 source states                         33,225
nonempty Q9 predecessor states            11,881
Q9 completions                     8,096,356,425,843
omega=0,1,2 each                   2,698,785,475,281
compatible structural bases                   79
nonempty fibres classified zero-partial   11,881.
```

### Downstream restoration

**Not licensed.** The package imposes no Q8, Q7, Q6, Q5, Q4, or Q3 restoration. The `omega=0` slice of a current Q9 fibre is not shown to restore, and is not a complete finite-depth map.

### Strongest licensed scope after that decision

Current Q9 source fibres of the corrected Q10 state, over all 79 compatible structural bases, for the four-coordinate projection of the row-8 necessary scalar. The scalar cuts each nonempty fibre by exactly one-third and kills none of them. Anything downstream of Q9 remains open.

### Source, arithmetic, coverage, or custody defects

- **None load-bearing.** The frozen V1 swapped-label source is a negative control. Corrected V2 and V3 are separate executions of closely related source, not a second implementation.
- **Non-blocking custody:** each AWS `OUTPUT.sha256` records a self-hash of an empty file taken while that file was being written (`e3b0c442…`); `launcher.stdout` / `launcher.stderr` are empty; the later `MANIFEST_V3.sha256` hashes the final files, and the `result.json` hashes inside `OUTPUT.sha256` match the manifest. Identical in kind to the Q9 parent and Q3 reviews. Not used as mathematical evidence.
- **Non-blocking custody:** V1 shard payloads are not in the portable case. The swapped closed formula is visible in V1 source SHA-256 `9cca43b1…`. The producer’s “15 fail-closed / 12 coincidental pass” split is not independently counted from frozen V1 outputs here and is not used as evidence.
- **Non-blocking wording:** the code enumerates “at most 81” image points. The two `E_1` rows always constrain the four coordinates to a 9-point set, so the live image dimension is at most two. The 81-bound is valid and loose, not a multiplicity error.
- **Not a defect:** the aggregate script hard-codes `EXPECTED_Q10/Q9/COMPLETIONS`. This review summed the shard stdout/JSON and did not take those assertions as evidence.

### Independent replay

Not re-launched. Frozen Box02 commands and hashes are recorded in the custody section below.

---

## Promotion

**Accept `OVER ALL 79 COMPATIBLE STRUCTURAL BASES OF THE CORRECTED CURRENT Q10 SOURCE, THE ROW-8 NECESSARY SCALAR omega = carry(q1+2q3)+2h·carry(2q2+q4) (mod 3), WITH (q1,q2,q3,q4)=(c2_1,c2_2,d2_0,d2_1), IS UNIFORMLY DISTRIBUTED ON EVERY NONEMPTY Q9 AFFINE FIBRE. IT IS NOT AN OBSTRUCTION AT Q9 ALONE. EACH OF THE 11,881 NONEMPTY FIBRES HAS omega=0 COMPLETIONS.`**

**Refuse `Q8 THROUGH Q3 RESTORATION`, `COMPLETE MAP MODULO 243`, `ALL-DEPTH LIFT`, `COUNTEREXAMPLE`, and `JC2`.**

On the aligned F-only `D=7` chart, after the CONFIRMED Q9 source-state gate:

- The consumed compiler is `cases/as_fonly_d7_vertical_q9_state_gate_20260825/compile_shard.py` at SHA-256 `54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2`. Both corrected sources `exec` the prefix before the parent shard loop, assert that hash, and take the 32 names `C2,D2,C4,D4,W7,Z7` with `new_names[1:5]==("c2_1","c2_2","d2_0","d2_1")`. The old one-predecessor 13-trit canonical chart is not present in the executed prefix.
- Homogeneous orientation is `homogeneous_numeric(d,c)[i]=c_i x^i y^{d-i}`; `nderivative(·,0)=∂/∂x`. Direct expansion of degree two gives

  ```text
  C2 = c2_0 y^2 + c2_1 x y + c2_2 x^2,
  D2 = d2_0 y^2 + d2_1 x y + d2_2 x^2,
  C_x + D_y = (2 c2_2 + d2_1) x + (c2_1 + 2 d2_0) y.
  ```

  So the `x` coefficient is `2q2+q4` and the `y` coefficient is `q1+2q3`. Typed support puts `deg A, V_y, U_y, V_x ≥ 2` and `deg Cbase, Dbase ≥ 5`, so `degree_part(M,1)` is identically empty and `E_deg1` has no base contribution. Therefore

  ```text
  rx = floor((2q2+q4)/3) = [x](E/3+M),
  ry = floor((q1+2q3)/3) = [y](E/3+M),
  omega = ry - h·rx
        = floor((q1+2q3)/3) + 2h·floor((2q2+q4)/3)  (mod 3).
  ```

  The frozen preregistration SHA-256 `1a70dbaa…` swapped the displayed labels `rx` and `ry`. The nonmutating erratum SHA-256 `2b2fcef4…` is the correction. V1 source SHA-256 `9cca43b1…` implemented the swapped closed formula against the unswapped source read of `F1[(1,0)]` and `F1[(0,1)]`; it is a negative control, not evidence.
- On the fibre, `E_1=0` forces `2q2+q4, q1+2q3 ∈ {0,3,6}`, so the integer carries equal the F3 values `q2` and `q3` after the linear change `q1=q3`, `q4=q2`. Thus on the image, `omega = q3 - h q2` is F3-affine-linear. A non-constant affine-linear form is uniform on every positive-dimensional flat of `F_3^2`. A zero-dimensional image would make `omega` constant, hence `zero-full` or `zero-empty`. No such class occurs among the 11,881 nonempty fibres, so every nonempty fibre is uniform and in particular has `omega=0` completions.
- Exact affine projection: RREF over `F_3` with pivots normalized, inconsistency read as a zero row with nonzero right-hand side, particular from reduced RHS with free variables 0, kernel one vector per free column. Projection to coordinates `1..4`, image basis by 4-column RREF, enumeration of at most `3^r ≤ 81` image points, multiplicity `3^(ker_dim-r)` applied uniformly. The sum of the histogram is asserted equal to `3^{ker_dim}`. Inconsistent systems return an empty histogram and, in V3, rank pair `(rank, rank+1)` with fibre size 0.

**Do not promote this to:** a proof that those `omega=0` completions restore Q8 through Q3; a complete determinant-one map modulo 243; an all-depth lift; a characteristic-zero point; a counterexample; or JC2.

**Smallest honest successor.** Compose `omega=0` with the actual Q8 (and then Q7 through Q3) restoration equations, retaining their affine particulars and carry state. Do not treat Q9 uniformity of `omega` as a downstream exclusion.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this census as Q8, Q7, Q6, Q5, Q4, or Q3 restoration of the `omega=0` slice;
- this census as a complete finite-depth map modulo 243, an all-depth lift, a characteristic-zero point, a counterexample, or JC2;
- the frozen preregistration SHA-256 `1a70dbaa…` closed formula without the erratum (it swaps `rx` and `ry`);
- V1 source SHA-256 `9cca43b1…` as a successful projection (it is the swapped-label negative control);
- V2 and V3 as independent implementations (they are separate executions of closely related source; V3 adds rank-pair and fibre-size controls);
- the hard-coded JSON flags `old_13_trit_canonical_chart_reused=false` and `source_omega_replayed_on_every_projected_point=true` as evidence in place of the `exec` of `compile_shard.py` and the per-tuple `assert` plus rc 0;
- the aggregate script’s hard-coded `EXPECTED_*` constants as the census.

---

## Hostile checks

Tried hard, and failed, to make `C_x+D_y` have `x` coefficient `q1+2q3`; to make `nderivative(·,0)` be `∂/∂y`; to make homogeneous index `i` be the `y`-exponent; to let `M` at degree 1 depend on `c2_0`, `d2_2`, `C4`, `D4`, `W7`, or `Z7`; to let `source_omega`’s zeroing of the other 28 Q9 coordinates change `[x]` or `[y]` of `E/3+M`; to substitute the 13-trit chart for the 32-variable compiler; to drop the exact `/3` before reduction modulo 3; to leak inconsistent Q9 systems into the nonempty count; to lose multiplicity by enumerating duplicate image points or using `3^{proj_rank}` instead of `3^{ker_dim-proj_rank}`; to find a nonempty fibre classified other than `zero-partial`; to make the global `omega` histogram other than exact thirds; to make V2 and V3 ordered streams disagree; to cover fewer than 79 bases or fewer than 33,225 Q10 states; or to read Q9 uniformity as Q8–Q3 restoration or JC2.

### 1. Consumed compiler, 79 bases, every Q10 state, no 13-trit chart

Corrected V2 source SHA-256 `8d1b070c724b7ef2b0869f7925b6bdffc38d4e8beee643192cb5fd3ac8bc1547` and V3 source SHA-256 `c0951aaf55df349a79e99a6aaae013bb5e9eb8d1fce9ea43995ec4550ccb4296` both:

```text
EXPECTED = "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2"
assert hashlib.sha256(payload).hexdigest() == EXPECTED
exec(compile(payload.split(marker, 1)[0] + b"\n", ...))
assert new_names[1:5] == ("c2_1", "c2_2", "d2_0", "d2_1")
```

Every V2 `SOURCE.sha256` records `8d1b070c…` for the staged `project_row8_shard.py`; every V3 file records `c0951aaf…`. Every shard JSON records `parent_sha256` equal to `54d05ebf…`. `SOURCE_MANIFEST_V3.sha256` pins the same compiler path. The executed prefix is the Q9 `source_rows` / `canonical_source` / 23-row, 32-variable system. A 13-trit chart object is not imported, not `exec`’d, and not enumerated; the boolean flag is ignored as evidence.

Coverage of structural space: `base_total = 3^7 = 2187`, shard `i` takes `[81i, 81(i+1))`. The 27 frozen ranges are contiguous, disjoint, and exhaust `[0,2187)`. Q10 admission is the parent’s `N12`/`Q11`/`Q10` tests on every affine solution of the structural/Frobenius/unknown system. Hand-sum of the 27 V3 (and identical V2) `q10_states` lines:

```text
30969
+ 537 + 537
+ 251 + 251
+ 89×4
+ 27×12
+ 0×6
= 33,225.
```

That is the CONFIRMED Q9 parent’s Q10 count, shard-for-shard (parent `shard_00.out` has `Q10_visible_states 30969`, `shard_03.out` 537, `shard_09.out` 251, and so on).

The 79 compatible bases are the parent inventory, pinned as `compatible_bases.tsv` SHA-256 `bc9d6c9e…` (79 `Q9_COMPATIBLE_BASE` lines). Nonempty projection `per_base` keys on all 21 nonempty shards match that list (shard 0 holds the 11 bases in `[0,80]`; shards 10,11,13,14,16,17,19,20,22,23,25,26 are the twelve singleton 27-state bases; shards 3 and 6 the two 13-base blocks; shards 9,12,15,18,21,24 the six 5-base blocks). Empty shards 1,2,4,5,7,8 have `per_base {}` and q10 count 0, matching parent.

### 2. Erratum: which carry is `x` and which is `y`

Independent expansion, from the compiler’s own `homogeneous_numeric` and `nderivative`, is the display in the Promotion section. The `x` carry is `floor((2q2+q4)/3)`; the `y` carry is `floor((q1+2q3)/3)`. The corrected closed formula in V2/V3 is

```text
first_carry  = (q1 + 2*q3) // 3     # y-carry = ry
second_carry = (2*q2 + q4) // 3     # x-carry = rx
return (first_carry + 2*h*second_carry) % 3
     ≡ (ry - h*rx)  (mod 3).
```

V1 closed formula used the swapped names and therefore computed `xcarry - h·ycarry`. That equals the source value iff `(1+h)(ycarry-xcarry)≡0 (mod 3)`, i.e. only where `h=2` or the two carries agree. V1 is classified as a negative control from those source bytes. It is not evidence.

### 3. Literal `E/3+M` on every projected tuple

`source_omega` builds `C=Cbase+C2`, `D=Dbase+D2` from the four projected coordinates, reconstructs

```text
E  = L1 + K + C_x + D_y,
E1 = degree_part(E,1) / 3,          # divide_exact, refuses non-multiples of 3
M  = A D_y + C_x V_y - U_y D_x - C_y V_x,
F1 = E1 + degree_part(M,1),
rx = F1[(1,0)] % 3,                  # [x]
ry = F1[(0,1)] % 3,                  # [y]
omega = (ry - h*rx) % 3,
```

and asserts equality with `closed_omega` **before** the histogram is incremented. Monomial keys are `(x-exp, y-exp)`. Degree-1 of `M` is identically `{}` on the typed support, so this is exactly `[x],[y]` of `E/3`. The call site zeros the other 28 Q9 coordinates; those coordinates do not enter `E_deg1` or `M_deg1`, so the zeroing is valid. All 54 corrected shards returned rc 0, so the assertion never fired. The JSON flag recording that fact is not used as evidence.

### 4. Affine projection and multiplicity

`q9_affine_system` is the parent’s finite-difference affine extraction: value at `0` and at each `e_i`, columns reduced modulo 3. The parent’s all-ones negative control for cross terms lives in `affine_rank_and_witness` and is a theorem of the typed support (CONFIRMED Q9 review §3: `{C2+C4,D2+D4}` cannot reach `N_9`; `E,M,T` are linear in the restored layers). The projection reuses the same linearization.

`solve_affine` RREF is the parent RREF: search down a column, swap, normalize a `2` to `1` by multiplying by `2`, eliminate, pivots recorded in column order. Inconsistency is a zero left row with nonzero right. V3 returns `(rank, rank+1, None, [])` then; V2 returns `(rank, None, [])`. Particular sets free variables to 0; kernel has one vector per free column with pivot entries `(-work[row][free])%3`. Augmented matrix is `[A | -b]` for `A x + b = 0`. This is the parent convention, which asserts `source_rows(witness)==0`.

`span_basis` row-reduces the projected 4-tuples. Combinations of an RREF basis of a subspace of `F_3^4` are unique, so image points are not duplicated. `fibre_factor = 3**(len(kernel)-len(basis))` is constant on the affine image. `sum(histogram)==3**len(kernel)` is asserted per nonempty system. Inconsistent systems contribute `[0,0,0]` and are skipped from nonempty counts; V3 still records them under fibre size 0. No inconsistent-system leakage into the 11,881.

Rank keys: V3 stores `str((rank, augmented_rank))`, i.e. `"(13, 13)"` with spaces, matching the aggregate. V2 stores rank only, and only for nonempty fibres, which is why V3 exists as the control-complete run.

### 5. Independent aggregate of 54 shard payloads

All 27 V2 `runner.rc` files and all 27 V3 `runner.rc` files contain `0`. `Exit status: 0` on representative `runner.stderr`. V2 and V3 `runner.stdout` streams are byte-identical in the printed census and in `stream_sha256` for every shard index. Structural ranges are the 27 adjacent 81-blocks of `[0,2187)`.

Hand-sum, V3 (V2 identical):

| shard class | #shards | q10 | nonempty | completions | class |
|---|---:|---:|---:|---:|---|
| 0 | 1 | 30,969 | 10,989 | 8,057,958,750,711 | `zero-partial` 10,989 |
| 3 and 6 | 2 | 537 | 233 | 10,029,885,993 | `zero-partial` 233 |
| 9 and 18 | 2 | 251 | 29 | 1,248,354,909 | `zero-partial` 29 |
| 12,15,21,24 | 4 | 89 | 11 | 473,513,931 | `zero-partial` 11 |
| twelve singletons | 12 | 27 | 27 | 1,162,261,467 | `zero-partial` 27 |
| 1,2,4,5,7,8 | 6 | 0 | 0 | 0 | empty |

Sums: q10 `33,225`; nonempty `11,881`; completions `8,096,356,425,843`; every nonempty class line is `zero-partial` only. No `zero-empty` or `zero-full` string occurs in any shard JSON. Every nonempty shard’s `omega` triple is equal thirds, and `8,096,356,425,843 / 3 = 2,698,785,475,281`.

Per-shard `stream_sha256` values agree between V2 and V3, so the ordered digest `SHA256( ‖_i  (i as uint16 LE) ‖ stream_i )` agrees. The displayed hex `b3fe039b359754bede4230fdcda9dfc0d3fbd260b719d99870d1c8315639f82b` was not recomputed (no hasher in this session); equality of the two runs is the load-bearing fact.

### 6. V3 rank-pair / fibre-size controls, and every fibre `zero-partial`

Visible V3 JSON rank pairs on the twelve singleton shards are `{(16,16):27}` with fibre `3^16`. Parent Q9 `shard_00.out` records

```text
((13,13),6615), ((13,14),4320), ((15,15),2106),
((16,16),2268), ((16,17),3996), ((17,18),11664)
```

with fibre histogram `(0,19980), (3^16,2268), (3^17,2106), (3^19,6615)` and completions `8,057,958,750,711`, matching this package’s shard 0 q10/q9/completion. Adding the parent’s remaining shards reproduces

```text
(13,13)  6,615     (13,14)  4,320
(15,15)  2,106     (16,16)  3,160
(16,17)  5,288     (17,18) 11,736
```

and fibre sizes `0^21344, (3^19)^6615, (3^17)^2106, (3^16)^3160`. Consistent pairs sum to 11,881; inconsistent plus consistent sum to 33,225. Completions `6615·3^19 + 2106·3^17 + 3160·3^16 = 8,096,356,425,843` were recomputed by hand in this review. V3 `solve_affine` is the same RREF; V3 aggregate JSON stores exactly those six rank-pair keys; small-shard V3 JSON matches the corresponding parent `.out` rank pairs. Rank 13/15/16 as keys for nonempty fibres are therefore the parent ranks, not a second invented census.

`zero-partial` is assigned per Q10 state, not from the global histogram: `hist[0]!=0` and not `(hist[1]==hist[2]==0)`. The 11,881 counter equals the nonempty-state counter on every shard. Combined with the F3-linear form of `omega` on the 9-point `E_1=0` set (Hostile check / Promotion), every nonempty fibre is uniform, not merely globally balanced.

### 7. Licensed conclusion

`omega` is no obstruction at Q9 alone. Each current nonempty Q9 fibre has `omega=0` completions. That is the strongest statement this package licenses. It does not say those completions satisfy Q8 through Q3, give a complete mod-243 map, lift all-depth, yield a counterexample, or affect JC2. The producer body already refuses those readings; this review refuses them again.

### 8. Custody: separate executions, not a second implementation

V2 job `/home/ubuntu/jobs/as_global_row8_projection_20260825T1417Z_v2` on host `ip-172-30-0-186` (Box02), source `8d1b070c…`, shard 0 window `2026-08-25T14:06:59Z`–`14:11:59Z`. V3 job `/home/ubuntu/jobs/as_global_row8_projection_20260825T1422Z_v3`, source `c0951aaf…`, shard 0 window `14:08:52Z`–`14:16:29Z`, peak RSS 21,784 KiB, elapsed 7:37, exit 0. Aggregate job `/home/ubuntu/jobs/as_global_row8_projection_aggregate_20260825T1420Z_v2` ran both

```text
python3 aggregate_projection.py SHARD_ROOT OUTPUT_JSON
python3 aggregate_projection.py --require-v3-controls SHARD_ROOT OUTPUT_JSON
```

with V3 elapsed 0.05s, RSS 16,648 KiB, exit 0. Archive SHA-256 values `6b2a4a12…` (V2) and `33094de6…` (V3) are recorded in `SHARD_ARCHIVES.sha256`. Aggregate JSON SHA-256 values `1de7a660…` (V2) and `e24c8791…` (V3) are recorded in `FREEZE_V3.sha256` and `MANIFEST_V3.sha256`. V3 `result.json` SHA-256 `6caad5c7…` is identical in shard 0 `OUTPUT.sha256` and the manifest.

V3 differs from V2 by returning `(rank, augmented_rank)` and recording fibre sizes, not by a second RREF, a second `source_omega`, or a second compiler pin. Identical per-shard stream hashes confirm they counted the same states and the same histograms. They are not an independent implementation.

`OUTPUT.sha256` self-hash of the empty file, empty launcher stdout/stderr (`e3b0c442…`), and the aggregate directory’s `T1420Z_v2` name covering both aggregates are snapshot/naming noise. Incomplete-transfer bytes were not found: 27+27 extracted shard trees, both `tar.gz` files, both aggregates, and both source-history snapshots are present.

SHA-256 values quoted above are textual cross-consistency across `SOURCE_MANIFEST_V3.sha256`, `MANIFEST_V3.sha256`, `FREEZE_V3.sha256`, per-shard `SOURCE.sha256`, and the source `EXPECTED` constants. They were not recomputed.

---

## Issues classified

| class | issue | load-bearing? |
|---|---|---|
| mathematical | none | — |
| source-typing | none: monomial `(i,d-i)`, axis `0=x`, `E/3+M` read as `[x],[y]`, erratum orientation independently derived | — |
| software | none in the projection/multiplicity; hard-coded JSON flags and aggregate `EXPECTED_*` are not evidence | no |
| custody | `OUTPUT.sha256` self-hash of empty file; empty launcher stdout; SHA-256 not recomputed; V1 shard payloads absent so the 15/12 split is unverified; V2/V3 are not independent implementations | no |
| wording/scope | “at most 81 image points” is a valid loose bound (live image ≤ 9); producer refusal of Q8–Q3 / mod-243 / all-depth / JC2 is already correct and is restated | no |

**Verdict: CONFIRMED.**
