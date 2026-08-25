# Hostile different-model review — exact B9 Kuranishi structural compression

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-common-cubic-kuranishi-structural-compression-producer-20260825.md` (SHA-256 `842f1a26c8e6d6edbe33dcdafafdc6d4e255afab8d1e6ca3458f7da952958ac5`) |
| Frozen case | `cases/as_b9_9_12_common_cubic_kuranishi_solver_20260825/` |
| Reviewed parent | `xmodel/as-b9-9-12-common-cubic-global-fresh-elimination-review-grok-20260825.md` (SHA-256 `6fc2210f9aa3d364c37d7e371a6653365dc58115dccc114bd3d93e8213b0be7a`), overall **CONFIRMED** |
| Map emitter | `emit_kuranishi_map.py` SHA-256 `1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf` |
| Span analyzer | `analyze_structural_span.py` SHA-256 `0cbfd304c5a214b2120b024ba322986543d42d4bd09192319b71329d924eb9c3` |
| Constants analyzer | `analyze_structural_span_constants.py` SHA-256 `4de5b5853484d2cdfa9cf549429d102ff718b4c0f3f8ad880d1e2338aab5dbf0` |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED**. On the already reviewed map `K : F_3^{95} -> F_3^{176}`, vanishing of all 176 coordinates is equivalent to vanishing of 110 original rows. Sixty-six coordinates are the zero function |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of dual-host Box02/Box03 byte-identical 111-row certificates and SMT, of the Box02 constant refinement, and of the Box02 dependency replay. The Box02 missing-PID defect is non-mathematical |
| Wording / scope | **CONFIRMED**. Zero-locus, lift, all-depth, counterexample, maximum-12, and JC2 readings are firewalled. Sampled rank 9 and solver failures are diagnostics |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | line-by-line source audit of the span/constants/dependency analyzers and the pinned emitter DAG; independent SHA-256 of freeze/manifest/sources/gzip/SMT/results; Box02/Box03 byte comparison; inspection of both gzip certificates (all 176 reconstruction identities, unit basis relations, group 215); hand evaluation of the 8-node SMT cone of `n33349`; independent syntactic support walk of the pinned 34,555-node formula. No local exec of producer analyzers, no residual/family replay, no Z3/Boolector/CaDiCaL launch, no AWS restaging |
| Git HEAD | `f96845eecaa073110d1526e0b08117205a4dcf30` (producer, this case, and the parent package uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

The reviewed parent licenses one exact map `K : F_3^{95} -> F_3^{176}` for the displayed one-parent `(9,12)` common-cubic chart at the `3^{11} -> 3^{12}` transition. This successor does not rebuild that map. It changes only the output presentation, by exact F3-linear algebra on the pinned modular DAG.

Among the 299 pre-quotient next-carry expressions there are 234 distinct recursive SHA-256 digests. Treating those digests as formal atoms, the 176 coordinates have rank 111. After evaluating the unique input-independent atom — group 215, which is the interned 20-bit zero `n3 = (_ bv0 20)` followed by the `3^{11}` digit and `fneg` — that atom is the F3 zero. The greedy basis row it supplied is coordinate 96 (`n33349`). The resulting rank is 110.

Consequently, on the complete displayed 95-parameter chart,

```text
K(x) = 0  iff  K_i(x) = 0 for the 110 certified original coordinate rows i.
```

This is an identity of the frozen circuit, not a sampled rank statement. The 447-point design, difference rank 9, and Z3 `table overflow` are diagnostics only.

## Strongest exact claim

Fix the reviewed parent map `K` of emitter SHA-256 `1d6dbd67…` and full-formula SHA-256 `108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c`, on the one frozen B9 mod-243 parent and the reviewed `17+78` predecessor chart. Write `K_0, …, K_{175}` for the 176 emitted coordinates, in order.

1. The 299 next-carry DAG nodes fall into 234 interned expressions. The 176 coordinates are F3-linear forms in those atoms of formal rank 111. Dual-host certificate gzip SHA-256 `45b40fd0540e060869a25683c0f5d852a0a24c39e4d04ff17d60af568453d578`, uncompressed `d363cc0c5adbf432d8f3d5287ca7fc068801535fc2b5f891511ecd5fd61c0785`. Every coordinate is the stored F3-linear combination of the 111 original rows; those 111 rows are independent in the formal-atom space.

2. Exactly one of the 234 atoms is input-independent. It is group 215, the 66 interned copies of next-carry indices `210..275`, and it evaluates to `0` in F3. Coordinates `96..161` are the same SMT node `n33349`, whose 8-node cone is

   ```text
   n3     = (_ bv0 20)
   n33078 = (0 / 177147) mod 3 = 0
   n33079 = 2 * 0 = 0
   n33348 = 1 * 0 = 0
   n33349 = 0 + 0 = 0
   ```

   with no chart inputs. Deleting the greedy basis row 96 drops the formal rank to 110. Constants certificate uncompressed SHA-256 `94574911f3a4b39117ddefdd5eab138d134a4a3ccae65a813e478d913c7b2228`. The 110 original rows are

   ```text
   {0,1,…,95} ∪ {162,163,…,175}.
   ```

   The other 66 coordinates are the zero function. Therefore `K(x)=0` if and only if those 110 coordinates vanish.

3. Ten of the 95 chart inputs are absent from the syntactic cone of every one of the 176 coordinates, hence from the 110-row basis:

   ```text
   a_0, a_1, s_0, s_1, s_2, s_3, s_4, s_6, s_14, s_29.
   ```

   The remaining 85 inputs form one syntactic incidence component. Used supports may overapproximate semantic dependence after cancellation; absence is exact.

## Sharpest non-claim

Exact linear compression of one already reviewed 176-coordinate circuit, for one parent, at one modulus. Not emptiness of the 110-coordinate zero locus, not a SAT lift, not survival past `3^{12}`, not an inverse-limit/`Z_3` point, not a characteristic-zero Keller map, not complete earlier-parent coverage, not a maximum-twelve theorem, not a counterexample, and not JC2. Formal rank 110 is an upper bound on functional rank among the remaining 233 distinct DAG atoms; further identities between those atoms are not excluded and are not needed for the spanning identity. Sampled difference rank 9 is not the source-DAG rank. Z3 4.16 `table overflow` is not a decision of `K`.

---

## Evidence layers (do not collapse)

1. **Parent map, already reviewed.** The parent different-model review CONFIRMED `K : F_3^{95} -> F_3^{176}` as the exact next-digit obstruction on this one chart. This review re-hashed that report to `6fc2210f…` and re-hashed the emitter, fresh-block gzip, and full formula; it does not re-execute the residual compiler or the 205×55 block.

2. **Pinned reconstruction of the same circuit.** `analyze_structural_span.py` `exec`s the same emitter at SHA-256 `1d6dbd67…` with `ROW_START=0`, `ROW_END=176`. Box02 and Box03 both emit SMT SHA-256 `108cfdaa…`, matching the parent full formula, and both write certificate gzip SHA-256 `45b40fd0…`.

3. **Certificate arithmetic, this review.** Decompressing the dual-host gzip and checking every stored relation reproduces all 176 reduced rows from the 111 original rows over F3. Every basis relation is a unit vector. The same check on the constants gzip reproduces all 176 refined rows from the 110 original rows.

4. **Constant-zero atom, this review.** Coordinates `96..161` are the identical assertion `(assert (= n33349 (_ bv0 2)))`. The SMT cone of `n33349` has eight nodes, no inputs, and evaluates to 0 by the same 2-bit/F3 and 20-bit/mod-531441 operations the constants analyzer implements.

5. **Unused inputs, this review.** An independent walk of all 34,555 `define-fun n*` bodies on the pinned SMT reproduces the AWS histogram, the ten unused names, and the 85+10 component sizes. The empty-support row is exactly coordinate 96.

6. **Solver layer unused.** `solve_kuranishi_z3.py` and the bit-blast negative exist. No SAT model, DRAT, or independently checked UNSAT certificate is consumed. None is this theorem.

---

## Charge 1 — parent licenses `K : F_3^{95} -> F_3^{176}` at one-parent scope

**CONFIRMED**

Independently recomputed SHA-256, matching the freeze and the parent review:

| Object | SHA-256 |
|---|---|
| Parent review | `6fc2210f9aa3d364c37d7e371a6653365dc58115dccc114bd3d93e8213b0be7a` |
| Parent producer | `524a56ddfc04a7990f009e8fe781c0b1df694771c747bb40f396490f8eaac94f` |
| `emit_kuranishi_map.py` (tree, Box02, Box03, constants copy) | `1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf` |
| `global_row22_v1.py` | `b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f` |
| `independent_common_core.py` | `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8` |
| `fresh_block.json.gz` | `f7f473c5781f610dd0f96112981e8f3b3c7757467d42b7c465a3dfde5c80e8af` |
| Full / span-parent SMT | `108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c` |

The parent review’s strongest claim is that vanishing of this compiled map is equivalent to existence of a `3^{12}` lift inside this one 149-digit chart, with predecessor coordinates `17+78=95` and left quotient 176. Its firewalls are one parent, finite `3^{12}` transition, no SAT/UNSAT, no all-depth, no JC2. This successor `exec`s that same emitter and re-emits the same formula bytes. It does not retarget the parent, the chart, or the modulus.

The span parent-emit metadata records `family_dimensions = [17, 78, 95]`, `fresh_block_shape_rank_kernel_quotient = [205, 55, 29, 26, 176]`, combined-support histogram `{1:154, 2:12, 3:5, 4:2, 5:2, 6:1}`, DAG node count 34,555, and all-coordinate structural hash `557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48`, all matching the parent freeze.

---

## Charge 2 — grouping, F3 rank, original rows, reconstruction from 111

**CONFIRMED**

`analyze_structural_span.py` groups `next_rhs` by `value.digest`. The emitter’s `Dag.node` hashes `sort|op|arg.digest…|body` and interns by `(sort, digest)`, so equal digests are byte-identical recursive expressions, not node-name coincidence. Distinct digests are treated as independent formal atoms; that is the declared upper-bound convention, not a hidden functional equality.

The reduced matrix is

```text
reduced[i][g] = sum_{j in group g} combined[i][j]  (mod 3),
```

i.e. the F3 coefficient of interned atom `g` in coordinate `i`. This is the correct linear form of `kappa[i] = sum_j combined[i][j] * next_rhs[j]`. Incremental RREF over F3 uses that 2 is its own inverse, selects a row when it first increases rank in original coordinate order `0..175`, and reorders the selected rows by pivot column. `solve_columns` then expresses every reduced row in that basis; the AWS job asserts the reconstruction.

Certificate inspection, this review, on the dual-host gzip:

| Check | Result |
|---|---|
| Uncompressed SHA-256 | `d363cc0c…` |
| `next_rhs_groups` | 234 groups, union `{0,…,298}`, 299 distinct indices |
| Digest list | 234 unique 64-hex strings, sorted |
| Group sizes | 233 singletons, one 66-member group |
| Reduced shape | 176 × 234 |
| Relations shape | 176 × 111 |
| Reconstruction `row i = sum_k rel[i][k] * basis[k]` | holds for all 176 rows |
| Basis relations | all 111 are unit vectors |
| Omitted relations | all 65 are `K_i = K_96` for `i = 97..161` |

The unit-plus-span check excludes a consistent transpose or swapped-index bug: a transposed storage would not be 176×234 with 176×111 unit relations, and would not reconstruct. Rank 111 is the rank of this formal-atom matrix. Original rows are the greedy coordinate indices, not a rewritten basis of mixed rows.

The 66-member group is group 215 = next-carry indices `210..275`. Those are the last 66 of the 276 determinant slots. Column 215 of the reduced matrix is 1 on coordinates `96..161` and 0 elsewhere. Row 96 is exactly `e_{215}`.

---

## Charge 3 — Box02/Box03 byte identity; missing PID is non-mathematical

**CONFIRMED**

`cmp` of Box02 vs Box03:

| Artifact | Identity |
|---|---|
| `structural_span_certificate.json.gz` | byte-identical, SHA-256 `45b40fd0…` |
| `span_parent.smt2` | byte-identical, SHA-256 `108cfdaa…` |
| `analyze_structural_span.py` | byte-identical to the tree, SHA-256 `0cbfd304…` |
| `emit_kuranishi_map.py` | byte-identical to the parent tree copy |
| `result.json` | equal after deleting `aws_job_tag` |

Box02 `launcher.rc` is `0`; `/usr/bin/time` reports exit status 0, wall 12.49 s, RSS 67048 KiB. Box03 `launcher.rc` is `0`, wall 12.43 s, RSS 67744 KiB, and `launcher.pid` is `95410`. Box02 has no `launcher.pid` in the job directory. The producer’s account — shell `&` precedence wrote the wrapper PID in the remote home directory — is a custody defect of the first launch only. The typed analyzer exited zero and the Box03 mirror carries PID/RC. No theorem depends on the missing Box02 PID file.

---

## Charge 4 — constant evaluation; group 215 is zero; deleting row 96 yields rank 110

**CONFIRMED**

`analyze_structural_span_constants.py` `exec`s the pinned parent analyzer (SHA-256 `0cbfd304…`), then evaluates every input-independent interned atom. The matched operations are exactly the emitter’s primitives, with the same moduli:

| DAG op | Evaluator | Emitter SMT |
|---|---|---|
| `(_ bv k 2)` / `(_ bv k 20)` | literal `(k, width)` | `c3` / `cm` |
| `fadd` / `fmul` | `(left ∘ right) mod 3` | 4-bit `bvurem` by 3 |
| `madd` / `mmul` | `(left ∘ right) mod 531441` | 40-bit `bvurem` by 531441, extract 20 |
| `mneg` | `(-v) mod 531441` | `ite` zero else `bvsub 531441` |
| `zero_extend 18` | keep value, width 20 | embed 2-bit into 20-bit |
| digit `extract 1 0` of `udiv / 3` | `(v // D) mod 3` | `bvudiv` then `bvurem` by 3 |

Unmatched constant bodies raise. The AWS job passed, so every constant node matched. Group 215 is the unique constant, value 0, recorded as `constant_group_values: {215: 0}`. Nonconstant groups number 233. The refined matrix is 176 × 234 (233 nonconstant columns plus a constant-coefficient column). The constant column is the zero vector. Refined rank is 110. The 110-row basis is the 111-row basis with index 96 deleted and no other change of order.

Independent SMT evaluation, this review, does not exec that analyzer. Coordinates `96..161` are 66 copies of `(assert (= n33349 (_ bv0 2)))`. The cone is

```text
n33349 = fadd(n0, n33348)
n0     = (_ bv0 2)
n33348 = fmul(n1, n33079)
n1     = (_ bv1 2)
n33079 = fmul(n2, n33078)
n2     = (_ bv2 2)
n33078 = digit_{177147}(n3)
n3     = (_ bv0 20)
```

with no `a_*` or `s_*`. Hand evaluation: `0 // 177147 = 0`, `2·0 = 0`, `1·0 = 0`, `0+0 = 0` in F3. This is the next-carry `fneg(divided_digit(final_row, 3^{11}))` of the interned 20-bit zero, then `fadd(0, fmul(1, ·))` as the coefficient-1 coordinate. Group 215 is exactly zero. It is not 1 or 2, so it is deleted rather than turned into an affine obstruction `K_i ≡ c ≠ 0`.

After substituting 0 for that atom, rows `96..161` are the zero row of the refined matrix. Row 96 was the unique greedy basis row for column 215; deleting it drops rank by 1 to 110. The constants gzip reconstruction holds for all 176 rows, with 110 unit basis relations and 66 empty omitted relations (the zero function). Result SHA-256 `0b079e314561e1a03139b3c40cd68b6fd459fc0f47ac62df3616792b144d4b27`.

The constant refinement is Box02-only. That is not a mathematical gap: the 8-node cone lives in the dual-host-identical SMT.

---

## Charge 5 — relation rows from the gzip; `K=0` iff basis110 `=0`

**CONFIRMED**

Indexing/transposition is excluded by the following simultaneous constraints, all read from the gzip certificates and the SMT, not from re-running RREF as a second algorithm:

- Reduced is 176 lists of length 234, not 234 lists of length 176.
- Relations are 176 lists of length 111 (resp. 110), not the transpose.
- Every basis relation is the corresponding unit vector in that 111-order (resp. 110-order).
- Every omitted 111-relation is exactly `K_i = 1 · K_96` for `i=97..161`.
- Coordinates `96..161` are one SMT node; a column/row swap would not land 66 consecutive equal assertions on the unique constant atom.
- Parent-emit `coordinate_hashes[96..161]` are 66 copies of `44374970b84de7d9b20ccecc258957b6be1fd773bb162dd25df6de3d7097d5d1`.

Because coordinates `96..161` are the zero function, vanishing of `K` is vanishing of the complementary 110 original coordinates

```text
{0,1,…,95} ∪ {162,…,175}.
```

Those are exactly the stored 110-row basis. The converse is the subset relation. Equivalence does not require the remaining 233 atoms to be functionally independent. Further identities among them could only lower the true functional rank; they cannot break these spanning relations.

The 111-row SMT SHA-256 `ed5e5629103c50e526ae268f0052140d49c66dff4dc21f71c3dd0e5a77a10db8` is the full formula with the terminal 176 assertions replaced by the 111 original-row assertions, including the tautology `n33349 = 0`. The producer’s description of that formula as logically equivalent with one extra identically-zero row is correct. It is not a SAT/UNSAT certificate.

---

## Charge 6 — exact unused inputs; used-support overapproximation firewall

**CONFIRMED**

`analyze_basis_dependencies.py` walks nullary `define-fun n*` bodies in emitter order, takes the union of already-computed child supports, and reads the 176 coordinate nodes from `lines[-178:-2]`. The pinned SMT ends with `(check-sat)` / `(get-model)` and has exactly 176 preceding `kappa` assertions, 95 `declare-fun` inputs `a_0..a_16`, `s_0..s_77`, and 34,555 `n*` definitions.

Independent walk of the same SMT, this review:

| Quantity | 111-row basis | 110-row basis | all 176 coordinates |
|---|---|---|---|
| Support-size histogram | `{0:1, 48:1, 49:1, 77:5, 80:10, 83:17, 84:9, 85:67}` | same without `{0:1}` | — |
| Used inputs | 85 | 85 | 85 |
| Unused inputs | the ten names below | the same ten | the same ten |
| Incidence components | ten unused singletons plus one 85-set | same | — |
| Empty-support row | coordinate 96 = `n33349` | none | the 66 copies of `n33349` |

Unused names, matching the AWS result and the producer (set equality; AWS lists them lexicographically):

```text
a_0, a_1, s_0, s_1, s_2, s_3, s_4, s_6, s_14, s_29.
```

Absence from every coordinate cone is exact functional independence of `K` from those ten inputs. Presence of the other 85 is syntactic and may overapproximate after cancellation. The AWS result’s `scope` string states that firewall, as does the producer. The 85 used inputs form one incidence component, so this analysis does not split the chart into independent blocks. Result SHA-256 `865f6e964af4b3b53eed5a8564bb11938d39be0d116a8046b027ffa86f6d839d`.

---

## Charge 7 — scope; diagnostics stay diagnostics

**CONFIRMED**

The producer’s theorem sentence is only the 110-row equivalence. Firewalls named and kept:

- one fixed B9 mod-243 parent, not all normalized or D12 maps;
- finite `3^{12}` transition, no next-depth or inverse-limit;
- no emptiness or survivor claim for the 110-coordinate zero locus;
- no maximum-12 or JC2 inference from this computation.

The 447-point control result is `kappa_zero_count = 0`, `origin_nonzero_count = 7`, `difference_affine_span_rank = 9`, `univariate_affine_failure_variable_count = 53`, with refusal scope that sample-constant functionals are navigation, not identities. Seven nonzero coordinates at the origin is compatible with 66 identically zero coordinates. Sampled rank 9 is not the source-DAG rank 110; the producer says so.

Z3 4.16 bit-blasting failed with `table overflow` at 7m35.51 s, RSS 59495164 KiB, exit 1. That is an engine negative. The producer places SAT/UNSAT outside the theorem.

The campaign routing citation of `xmodel/sol-fixed-total-d12-classical-closure-20260825.md` at freeze SHA-256 `71a8c83b…` is an independent degree-gcd note, labelled methodology/custody, not a claim of this circuit. The live tree currently hashes that file as `def1c2a1…`; the freeze is a snapshot. This is not a mathematical defect of the 110-row identity.

---

## Non-blocking notes (do not affect the verdict)

1. Box02 structural-span `launcher.pid` is missing. Disclosed. Box03 has PID/RC. Certificates are byte-identical.
2. Constant refinement and dependency replay are Box02-only. The load-bearing constant-zero identity was re-read from the dual-host SMT; the unused-input identity was re-walked from that SMT.
3. Producer RSS “about 68 MiB” / “roughly 59.5 GiB” are rounded (span RSS 65.5–66.2 MiB; bit-blast 59495164 KiB is ~56.7 GiB binary, ~59.5 GB decimal). Diagnostics only.
4. The 111-row basis SMT includes the tautology `n33349 = 0`. The producer says this. It is not a 110-row formula.

## Residual risk

The 110 spanning identity uses SHA-256 internment of DAG expressions as identity of formal atoms, plus exact evaluation of one closed 8-node cone. Residual risk is an undetected SHA-256 collision among the other 233 atoms, or an undetected algebraic identity among those atoms that would lower functional rank still further. Neither breaks `K=0` iff the 110 original rows vanish. The parent residual compiler is consumed from the already CONFIRMED parent review and was not re-executed here.
