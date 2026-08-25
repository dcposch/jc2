# Hostile different-model review — common-cubic witness Jacobian/SNF

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-common-cubic-witness-jacobian-snf-producer-20260825.md` (SHA-256 `9c05e2cb31b4ba5a3cc2fe22f9fb76a568ade14f2214ef4b96707f6158f13a31`) |
| Frozen case | `cases/as_b9_9_12_common_cubic_witness_jacobian_snf_20260825/` |
| Compiler source | `jacobian_snf.py` (SHA-256 `f8d1a0008fc7ccaec0ca1e4fde893f42df6105069a02b2fab01583755c192911`) |
| Kernel source | `classify_kernel.py` (SHA-256 `c10e01d13c74ff1ae4bc2a769139abe44e442edf53ae9be8b8c27d1c63bc87fb`) |
| Pinned witness | SHA-256 `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` (the CONFIRMED `3^{11}` common-cubic point) |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen r6d python-flint 0.9.0 primary, the Box03 same-source replay, and the r6d kernel classification. Box03 is an independent-host custody replay of the same pinned compiler, not a second source |
| Wording / scope | **CONFIRMED**. Failure of the classical maximal-minor inequality is not read as failure of a Smith-coordinate/dilatation route, lifting, or nonexistence |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | source-independent reconstruction of the `299 x 149` integer Jacobian on AWS r6d (finite difference in the 146 map coefficients, bivariate product rule in `H`, polar cross-check of all 276 determinant rows); entrywise identity with the frozen matrix; exact gauge kernel membership; multi-prime rank; custom `F_3` rank; FLINT SNF on the independently built matrix, cross-checked against the 3-free Smith parts; residual-threshold table and selected minor; scaling image identified with the stored top-form residual. No local Bash/Python/CAS/solver replay |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer, this case, and the review prompt uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

At the one literal normalized `(9,12)` common-cubic witness modulo `3^{11}`, the displayed system is 276 determinant coefficient rows plus 10 rows of `P9 - P_{(0,9)} H^3` plus 13 rows of `Q12 - Q_{(0,12)} H^4`, in the 55 coefficients of `P`, the 91 coefficients of `Q`, and the three non-monic coefficients of `H = y^3 + h_1 x y^2 + h_2 x^2 y + h_3 x^3`. An independent AWS reconstruction of that `299 x 149` integer Jacobian matches the frozen matrix entrywise. Exact ranks are `146` over `Q` and `94` over `F_3`. The 3-adic Smith valuation histogram is

```text
v3 : count
 0 : 94
 1 : 29
 2 :  8
 3 :  1
10 :  3
11 :  7
12 :  2
13 :  2
```

with determinantal-ideal valuation `205` and largest individual valuation `13`. The two numbers are not interchangeable. Every rank-146 row subset has common residual precision exactly `N=11`, so the classical inequality `N > 2 v_3(\det \mathrm{minor})` fails at this witness: even the optimal lower bound would require `N>410`. The rational right kernel is exactly the two constant translations and the degree-compatible target shear `Q \mapsto Q+tP`. Target scaling `(P,-Q)` is not an exact kernel direction; its 14 nonzero images lie in the common-core rows and equal `\pm` the stored top-form residual, hence are divisible by `3^{11}` but not by a higher uniform power.

This is a pointwise conditioning and kernel theorem at one displayed representative. It is not a Smith-coordinate Hensel theorem, not an all-depth lift or exclusion, not a full-family result, not a maximum-twelve theorem, not a counterexample, and not JC2.

## Strongest exact claim

Fix the displayed witness of SHA-256 `a39bc918…`, with

```text
H ≡ y^3 + 119880 x y^2 + 40581 x^2 y  (mod 177147).
```

The integer Jacobian `J` of the 299 displayed equations in the 149 raw coefficients has

```text
rank_Q J = 146,    dim ker_Q J = 3,    rank_{F_3} J = 94,    dim ker_{F_3} J = 55.
```

The 146 nonzero Smith invariant 3-valuations sum to `205` and have maximum `13`. Among row subsets whose residuals all have valuation at least a common `N`, the largest `N` retaining rational rank 146 is `N=11`. Every `146 \times 146` minor therefore has 3-valuation at least `205`, and no such minor can satisfy `N > 2 v_3(\det)`. After quotienting the two translations and the shear `Q \mapsto Q+tP`, there is no further rational right-kernel direction at this integer representative.

## Sharpest non-claim

A pointwise Jacobian/Smith/kernel diagnostic at **one** normalized common-cubic mod-`3^{11}` witness. Failure of the classical maximal-minor inequality is not failure of lifting and is not nonexistence. The valuation `13` is not a certified Hensel radius. The 55-dimensional mod-3 tangent kernel is not quotiented. There is no local row-ideal-generation theorem, no Smith-coordinate/right-inverse theorem, no 153 left-cokernel certification, no all-depth or `Z_3` point, no full-family result, no maximum-twelve theorem, no counterexample, and no JC2. Dual-host FLINT is one engine on one source, plus one independent construction of the same matrix.

---

## Evidence layers (do not collapse)

1. **Source-independent reconstruction (this review, AWS r6d).** Job `as_b9_cc_jacobian_independent_audit_grok_20260825T1816Z` on `ip-172-30-0-45`, python-flint 0.9.0 from the pinned exact-core venv, source SHA-256 `e35655aea0022123c895feb49c3b9f55029eef115faced8565cedf226c5fb390`. The 299-vector is evaluated from bivariate `jac(P,Q)-1` and the bivariate powers `H^3`, `H^4`. Map-coefficient columns are exact finite differences (the residual is affine in every `P` and `Q` coefficient). The three `H`-columns are the product rule. A polar formula `dP_x Q_y - dP_y Q_x` / `P_x dQ_y - P_y dQ_x` independently matches every determinant column. The reconstructed matrix and residual equal the frozen producer payload on every entry. Result SHA-256 `04e67b8e5e3a23e1c5f77289dc48c9522e305210394a98cd05c99f80b44f9b06`. Wall time `3:37.34`, maximum RSS `254528` KiB, `solver.rc=0`. This is a second construction of the matrix, not a second execution of `jacobian_snf.py`.

2. **Source-identical dual-host FLINT (producer custody, not a second solution).** r6d job `as_b9_common_cubic_jacobian_snf_20260825T173957Z`, elapsed `3:37.34`, maximum RSS `261384` KiB, `rc=0`. Box03 job `as_b9_common_cubic_jacobian_snf_20260825T175448Z_box03`, elapsed `3:36.10`, maximum RSS `261084` KiB, `rc=0`. Result bytes and matrix gzip bytes are identical (`d1c1ed60…` and `65eb73af…`). Distinct `/usr/bin/time -v` stderr hashes show two processes. This is custody that the audited compiler ran twice.

3. **Kernel classification on the pinned matrix.** r6d job, elapsed `0.09s`, maximum RSS `31988` KiB, result SHA-256 `92593c04…`. Single-host. It consumes the already-built matrix; it is not a second matrix construction.

No local python-flint, no local SNF, and no local execution of `jacobian_snf.py` or `classify_kernel.py`. A same-source replay is useful custody and is not an independent source construction.

---

## Charge 1 — Reconstruction and orientation of all 276 determinant rows and all 23 top-form rows in 149 variables

**CONFIRMED**

Combinatorics of the normalized box, independent of any compiler:

| Object | Count | Reason |
|---|---|---|
| `P` coefficients, total degree `<=9` | `10·11/2 = 55` | graded monomials |
| `Q` coefficients, total degree `<=12` | `13·14/2 = 91` | graded monomials |
| non-monic `H` coefficients | `3` | `h_1,h_2,h_3` |
| variables | `55+91+3 = 149` | |
| determinant ambient, total degree `<=22` | `23·24/2 = 276` | |
| `P9` coefficients | `10` | |
| `Q12` coefficients | `13` | |
| top-form rows | `10+13 = 23` | |
| equations | `276+23 = 299` | |

Variable order is `P` in graded degree `0..9`, then `Q` in graded degree `0..12`, then `h_1,h_2,h_3`. Determinant rows are the 276 slots in graded degree `0..22`. Top-form rows follow as `P9` with `i=0..9` then `Q12` with `i=0..12`. The Jacobian of a `(P<=9,Q<=12)` pair has total degree at most `8+11=19`, so the three highest determinant degree layers are structurally zero and are retained.

Orientation of the determinant is `P_x Q_y - P_y Q_x - 1`, matching the already CONFIRMED W5/`independent_witness_verify` Jacobian. The cubic is the bivariate form `H = y^3 + h_1 x y^2 + h_2 x^2 y + h_3 x^3`. Coefficient `i` of `H^n` is the coefficient of `x^i y^{3n-i}`; the independent auditor checked that this agrees with unary convolution of `[1,h_1,h_2,h_3]`. The `i=0` top-form rows are tautological (`P_{(0,9)}-P_{(0,9)}·1` and likewise for `Q`) and contribute zero Jacobian rows; they are still part of the displayed 23.

Independently recomputed SHA-256:

| Object | SHA-256 |
|---|---|
| `jacobian_snf.py` | `f8d1a0008fc7ccaec0ca1e4fde893f42df6105069a02b2fab01583755c192911` |
| `classify_kernel.py` | `c10e01d13c74ff1ae4bc2a769139abe44e442edf53ae9be8b8c27d1c63bc87fb` |
| `run_aws.sh` | `4fcf53a20b2b080d0b061037023c5ba467faa3dcc505d408c48e53bbfdc46963` |
| `PREREGISTRATION.md` | `1152646cae8d53bc9d41884e5b75c02b57a322dc104b176b671c1e2148c96b94` |
| `KERNEL_CLASSIFICATION.md` | `d6a32bc7c87f3220d876b98725b997ce875617d83b757b36bd74e18ca9c43dda` |
| `README.md` | `56887e9c96578b74d106f98bb11f3724ba9cf1b8f5719450a8a24493b4d53dc4` |
| witness `AWS_R6D` / `AWS_BOX03` | `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` |
| matrix gzip, both hosts | `65eb73affe9e8217607650e932f0c71ae243949aac26703474045da5a6adebaf` |
| matrix payload | `0202da0d68e4dd7cd6998751469f0d3d6ae6facc66bd18bc88d80fead8823f36` |
| `AWS_R6D/result.json` and `AWS_BOX03/result.json` | `d1c1ed60daf3a8f3c3c464c4e8b16c2de706623ba6184af791ebf0039716e381` |
| `AWS_R6D_KERNEL/result.json` | `92593c04c9fc1b439a7d3975a75b2e5840b170f9cc0289569bdcba9d1e18d90c` |
| producer report | `9c05e2cb31b4ba5a3cc2fe22f9fb76a568ade14f2214ef4b96707f6158f13a31` |
| this review’s prompt | `c3b7ff93c3c5b593cb208399e6f9223cc4c45200187580c11a45c5e9612202a7` |
| `MANIFEST.sha256` | `eabb80671e30d7f69ef88e059286aee6c290acefe009be50e976aa54f992d5f3` |
| independent auditor | `e35655aea0022123c895feb49c3b9f55029eef115faced8565cedf226c5fb390` |
| independent result | `04e67b8e5e3a23e1c5f77289dc48c9522e305210394a98cd05c99f80b44f9b06` |

Every FREEZE line (8 paths) and every MANIFEST line (34 paths) recomputes. The independent matrix equals the frozen `rows` and `residual` on all `299·149` and `299` entries, and the frozen `row_labels` match the orientation above.

## Charge 2 — Exact ranks `146` over `Q` and `94` over `F_3`

**CONFIRMED**

Against the independently reconstructed matrix, without taking `fmpz_mat.rank()` as the sole certificate:

- The three source-defined gauges (constant `P`, constant `Q`, and `Q \mapsto Q+tP`) multiply the matrix to the zero vector on every coordinate. They have rank `3` over `F_2`, `F_5`, and `F_{13}`. Hence `\mathrm{rank}_Q J \le 149-3 = 146`.
- Modular rank is `146` at `p \in \{13,17,19,23,29,31\}`. Hence `\mathrm{rank}_Q J \ge 146`.
- Therefore `\mathrm{rank}_Q J = 146` and `\dim\ker_Q J = 3`.
- A separate `F_3` Gaussian elimination, not the producer’s `rank_mod3`, returns rank `94`. Tangent dimension `149-94=55`.

FLINT `J.rank()` on the independent matrix agrees. Rank drops over `F_5`, `F_7`, and `F_{11}` (`139`, `142`, `144`) are the expected ones from the 3-free Smith parts `{1,2,4,20,280,3080}`: seven invariants divisible by `5`, four by `7`, two by `11`. They do not disturb the rational rank. The count of valuation-zero Smith invariants is `94`, matching `rank_{F_3}`.

The 55-dimensional mod-3 tangent space is the same numerical rank as the fresh kernel at the `3^{10}\to 3^{11}` gate of the CONFIRMED common-cubic family. That is consistency, not a quotient of this kernel.

## Charge 3 — Smith valuation histogram; determinantal-ideal `205` versus largest invariant `13`

**CONFIRMED**

The independent FLINT SNF of the reconstructed matrix has 146 nonzero diagonal entries whose 3-valuations histogram to

```text
0:94,  1:29,  2:8,  3:1,  10:3,  11:7,  12:2,  13:2.
```

Counts sum to `94+29+8+1+3+7+2+2 = 146`. The weighted sum is

```text
1·29 + 2·8 + 3·1 + 10·3 + 11·7 + 12·2 + 13·2
  = 29+16+3+30+77+24+26 = 205.
```

Maximum individual valuation is `13`. Dual-host producer SNF on the same matrix (byte-identical result JSON) records the same histogram, the same `maximal_rank_determinantal_ideal_v3 = 205`, and the same selected-minor valuation `350`.

These are different conditioning numbers. The product of the 146 invariant factors generates the 146-th determinantal ideal, so every rank-146 minor has valuation at least `205`. The largest single invariant `13` would be the relevant radius only after a Smith-coordinate / local row-ideal / left-cokernel theorem that this producer does not prove. No sentence in the producer silently replaces `13` by `205` as a Hensel radius.

The 3-free parts of the stored invariants lie in `{1,2,4,20,280,3080}`. Modular ranks at `5,7,11,13,\ldots,31` equal the number of invariants not divisible by that prime, which is an independent check of the SNF list rather than a second SNF engine.

## Charge 4 — Residual-threshold/rank argument; failure of every classical maximal-minor inequality

**CONFIRMED**

All 299 residuals are divisible by `3^{11}`. Exactly 143 are the integer zero; the finite valuations run from `11` to `23`. The nested threshold table on the independently built matrix is

```text
N   rank_Q  #rows
11   146     299
12   124     219
13    93     188
14    78     173
15    75     170
16    64     158
17    60     154
18    57     151
19    55     149
20    53     147
22    52     146
23    50     144
```

The unique maximal set of rows with residual valuation at least `12` has rational rank `124 < 146`. Any subset of those rows has rank at most `124`. Therefore every rank-146 row subset must include at least one residual of valuation exactly `11`, and the largest common precision retaining rank 146 is `N=11`.

The classical square-minor inequality is `N > 2 v_3(\det \mathrm{minor})`. Every rank-146 minor has `v_3 \ge 205`, so the inequality would require `N > 410`. Here `N=11 \le 410`. The explicitly selected replay minor (the producer’s RREF pivots, replayed as a determinant on the independent matrix) has valuation `350` and selected residual minimum `11`, and `11 > 2·350` is false. That selected minor is a direct negative control, not a generator of the determinantal ideal; the universal failure is already forced by `205` and `N=11`.

This is failure of that sufficient criterion at this witness. It is not a proof that no Hensel lift exists, and it is not a proof that a Smith-coordinate threshold near `2·13=26` is unavailable.

## Charge 5 — Exact rational-kernel classification: two translations plus `Q \mapsto Q+tP`

**CONFIRMED**

The three source-defined gauges are

1. `\delta P = 1` (the constant monomial), all other coordinates zero;
2. `\delta Q = 1` (the constant monomial), all other coordinates zero;
3. `\delta Q = P`, `\delta P = 0`, `\delta H = 0`, primitive.

They lie in the exact integer kernel of the independently reconstructed matrix. They are linearly independent over `Q`. Combined with `rank_Q = 146`, they exhaust the three-dimensional rational right kernel. No basis matching to the FLINT nullspace is required: two 3-dimensional subspaces of a 3-dimensional kernel coincide. FLINT’s nullspace on this representative happens to return exactly those three primitive vectors.

The shear is degree-compatible because `\deg P \le 9 < 12`, so it does not change the degree-12 part of `Q`. Identically, `det(P, Q+tP) = det(P,Q)`, the `P9` equation is untouched, and `Q12(Q+tP) = Q12(Q)`. Constant translations do not change derivatives, hence do not change the Jacobian determinant, and they do not meet the degree-9 or degree-12 top forms. After these gauges there is no further rational right-kernel direction at this integer representative. This does not quotient the 55-dimensional mod-3 tangent kernel.

## Charge 6 — Scaling negative control; nonzero over `Z`, zero modulo `3^{11}`

**CONFIRMED**

The target scaling `(\delta P, \delta Q) = (P, -Q)` is not in the exact rational kernel. Its image has 14 nonzero coordinates, all in the `P9`/`Q12` block, all divisible by `3^{11}`. Independently, that image equals the stored top-form residual on the ten `P9` rows and equals minus the stored residual on the thirteen `Q12` rows.

This is the first-order expansion, not an accident of FLINT. Determinant scaling is `det((1+t)P,(1-t)Q)=(1-t^2)det(P,Q)`, so the `t`-derivative at `0` vanishes on every determinant row. On the top forms,

```text
δ(P9 - P_{(0,9)} H^3) = P9 - P_{(0,9)} H^3,
δ(Q12 - Q_{(0,12)} H^4) = -(Q12 - Q_{(0,12)} H^4),
```

with `H` unmoved. The stored representative solves those 23 rows modulo `3^{11}`, not literally over `Z`, so the scaling image is exactly the congruential defect. The 14 nonzero rows are the non-tautological top-form residuals that fail to vanish over `Z`; the `i=0` rows remain the identity `0=0`.

## Charge 7 — No overread of maximal-minor failure as Smith-coordinate, lifting, or nonexistence

**CONFIRMED**

The producer’s firewall is load-bearing and is kept. In particular:

- “This is failure of that criterion at this witness, not failure of lifting.”
- “`13` is not silently replaced by `205` as a universal Hensel radius: a Smith-coordinate route might have a threshold near `2*13`, but its extra hypotheses are presently open.”
- “This producer proves no such sharper theorem.”
- The kernel classification “does **not** quotient the 55-dimensional mod-3 tangent kernel.”
- Exact scope: one displayed normalized common-cubic mod-`3^{11}` witness; no local row-ideal-generation theorem, Smith-coordinate Hensel theorem, all-depth lift or exclusion, full-family result, maximum-twelve theorem, counterexample, or JC2.

README and `KERNEL_CLASSIFICATION.md` repeat the same refusal. No sentence treats the failed classical inequality as emptiness, as a characteristic-zero point, or as a certified Smith-coordinate radius. The selected minor of valuation `350` is labelled a negative control, not the determinantal-ideal generator.

## Charge 8 — Source hashes, result hashes, timing/custody, one-witness scope

**CONFIRMED**

Freeze, manifest, both source closures, both result JSON files, both matrix gzips, both witnesses, the kernel result, the producer report, and the review prompt all recompute. r6d and Box03 solver stdout are byte-identical (`9b2d3bba…`); solver stderr hashes differ (`58fa89fc…` vs `af64bec8…`) as required for two processes. Both `solver.rc` files are the two-byte digest of `0\n`. Kernel classification is a separate r6d job with its own source closure (matrix gzip, witness, `classify_kernel.py`, `KERNEL_CLASSIFICATION.md`).

Timing:

| Job | Host | Wall | Max RSS | rc |
|---|---|---|---|---|
| `…T173957Z` compiler | r6d | `3:37.34` | `261384` KiB | 0 |
| `…T175448Z_box03` compiler | Box03 | `3:36.10` | `261084` KiB | 0 |
| kernel classification | r6d | `0.09s` | `31988` KiB | 0 |
| independent reconstruction | r6d | `3:37.34` | `254528` KiB | 0 |

Box03 installed python-flint 0.9.0 in a job-local venv; r6d reused the exact-core 0.9.0 venv. The independent auditor used that same r6d venv and the same FLINT version, on a different source.

Scope is exactly one displayed normalized common-cubic mod-`3^{11}` witness, namely the CONFIRMED point of SHA-256 `a39bc918…`. There is no family statement, no next-depth lift, and no JC2 conclusion.

---

## Non-blocking software / custody notes

These do not change the verdict.

1. **Box03 PID grouping.** The launcher’s PID metadata landed one directory above the job because of shell grouping. The case preserves the copied outer PID `89249` and the process snapshot; the solver cwd, source closure, output, timing, and `rc` are unaffected. The producer discloses this.

2. **Kernel classification is single-host.** Dual-host custody applies to the Jacobian/SNF matrix and result. The kernel job is one r6d execution of `classify_kernel.py` against that pinned matrix.

3. **Box03 is not a second source.** It is a second host executing `jacobian_snf.py` at SHA-256 `f8d1a000…`. The independent reconstruction above is the second source.

4. **Empty launcher stdout/stderr.** Both compiler hosts record the empty-file digest `e3b0c442…` for launcher stdout and stderr. Solver streams are the load-bearing logs.

5. **SNF engine.** The independent SNF is python-flint 0.9.0, the same library as the producer. Rational rank does not rest on that SNF: it is pinned by exact gauges plus modular rank at six primes of full rank. The histogram is additionally checked by matching modular ranks to the 3-free invariant list.

6. **Reviewer first launch.** Job `…T1814Z` aborted after the matrix had already matched, on an over-strict assertion that every tested prime has rank `146`. That was a reviewer script error (the 3-free parts introduce `5,7,11`), not a producer defect. Job `…T1816Z` is the completed independent audit.

## Defects

None. Mathematical, source, custody, and scope charges all hold. The notes above are non-blocking.

**CONFIRMED**
