# Hostile review — TD6 V89H19R1 raw P13 coordinate-12 audit

| Field | Value |
|---|---|
| Target | Frozen H19R1 raw-P13 coordinate-12 producer in `cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/`; dual harvests `harvest_h19r1_{r6a,r6b}_20260826T234603Z`; upstream frozen H15/H12/H11 source and manifests; H15 vector-record-count erratum; confirmed H15+H18 review |
| Overall verdict | **CONFIRMED** |
| Smallest mathematical failure | none |
| Smallest wording that is stronger than the theorem | preregistration sentence that the client “identifies the exact support that FIRST elimination cancels.” The client identifies raw specialized coordinate-12 support, which is not the H18 unit. It does not track that support through FIRST. |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile source/custody/algebra review. Producer was Sol. `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; in-memory H15 archive member audit; static comparison of `raw_degree_contributions` with H15 `compile_current_degree` and generic `compile_x_current`; independent parse of both TSVs and both harvest result texts; exact `Q` arithmetic on the four active addends. No compiler replay, no Singular, Sage, Lean, or `jc2-lean` |
| Repo / HEAD | `/Users/dc/code/math/jc2` / `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

This is the first executed review of the frozen H19R1 package. The v1 report path was not written.

Controlling prompt SHA-256 `ea3b89334a6559c404f9c00e4e10fa80d2fdec5cd7a64ca75cbfef100a27faa6`. Output-path override prompt SHA-256 `3f76cae6cb77b262e42366282ac0735e4ef2f7c770cebaaa5c8d30894db508f7`. Independently recomputed SHA-256 of every required primary pin matches. No file other than this review was written. The frozen producer package, campaign ledgers, other xmodel files, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On the frozen exact-Q slice, the H19R1 client rebuilds literal CURRENT degree 13 from the same six compiler-loop families as frozen H15, asserts that the reconstructed sum equals H15 `compile_current_degree(bands, 13)`, and extracts E3 coordinate 12 before FIRST. Dual AWS replicas on distinct r6i.16xlarge hosts returned rc 0 with byte-identical mathematical outputs and stdout. Independently parsed, those outputs are:

```text
total = F0:
  (27,)  500000000/(27*U)
  (29,) -1562500000/(27*U)
```

with empty q-monomial in every record. This is not H18's normalized unit `(3500000000/9)*(U/V)`. Exact `F=0` does not change coordinate 12. Omitting the preregistered source addend `f1_times_dg2:i=13:j=1` before aggregation leaves `(27,)` unchanged and replaces the `(29,)` coefficient by `-1625000000/(27*U)`.

The original H19 package remains quarantined: it pinned only the H15 client file, and its negative control dropped `total_records[1:]` after serialization. H19R1 repairs both defects.

The confirmed statement is only that the direct raw-unit shortcut fails, so an explicit original-FIRST membership/cancellation bridge remains. This review does not prove original-FIRST membership, a total-`F` lift, a whole-TD6 theorem, or JC2.

**CONFIRMED**

---

## Verdict table

| Charge | Finding |
|---|---|
| 1. Freeze/evidence, per-host manifests, runtime, rc, byte agreement | **CONFIRMED.** Freeze 6/6, combined evidence 24/24, both harvest evidence 280/280. Math outputs and stdout byte-identical. stderr/meta/lanes/pyc differ and are not mathematics |
| 2. R1 repairs original H19's two defects | **CONFIRMED.** Transitive H15→H12→H11→compiler manifests and H15 archive are pinned and checked. Omission removes a labeled source addend before summation |
| 3. Six loop families vs H15 `compile_current_degree` | **CONFIRMED.** Indices, derivative multipliers, signs, `-45*g3`, and canonicalization match. `-45*g3` is inactive at degree 13. Reconstruction equality is asserted |
| 4. 2757 / 68 / 132 / 22 enforced, no omitted family | **CONFIRMED.** 2757, 132, and 22 q are asserted. 68 is `len(contributions)` after dropping zeros, with completeness from the six-loop identity plus `reconstructed == parent`. The four active addends sum to the displayed coordinate 12 |
| 5. Independent TSV parse, four-label census, omission | **CONFIRMED.** Exact four ordered labels; two total and two F=0 records; omission changes only `(29,)` as stated |
| 6. Raw records ≠ H18 unit; narrow conclusion only | **CONFIRMED** for the narrow conclusion. Stronger “FIRST-cancellation support” language in the preregistration is not a theorem |
| 7. Assertions, python-flint pin, no Singular qring, preflight | **CONFIRMED.** `python_optimize=0`; flint 0.9.0 with module hash `1f7ef1f5…`; no qring in this client; census labels are frozen before dual launch |
| 8. Confirmation is not FIRST membership / total-F / TD6 / JC2 | **CONFIRMED.** Stated in the producer result and required here |

---

## 1. Charge 1 — freeze, evidence, runtime, byte agreement

Recomputed SHA-256 of the charged primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `P13_RAW_COORDINATE12_AUDIT_R1_RESULT.md` | `6573626441e58560935e6c4efac15f7a2cda873afc42f56e42ae5f4ca56837e8` | producer result |
| `P13_RAW_COORDINATE12_AUDIT_R1_EVIDENCE.sha256` | `f90f821879f1cc48b344db18aa1b63d113588025b2dc38b71cbe6e1cf30c55c1` | combined evidence |
| `P13_RAW_COORDINATE12_AUDIT_R1_FREEZE.sha256` | `35368feef910383f6199c9c95e91d4adb1ac0819cd6f1e3f930bd14b78c7d6a4` | freeze |
| `PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md` | `c578f6124f41fe69fa94be4b9cb02c56353b294f57d37a0c862d39405b1d836e` | preregistration |
| `replay_v89h19r1_raw_p13_coordinate12_audit.py` | `7919aa9d3a769e456abadd54eea12008b0a9121760b8382bbf8bdc72b3ec1784` | client |
| `run_v89h19r1_raw_p13_coordinate12_audit.sh` | `11d3c15d39e6a0155b74f46eb7e8abcfe9d4e4fc84bac6954e2206e34eb0e9f4` | runner |
| `SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256` | `a60d6fdb1e503caad7861cf1acd7ebc22a39eaac3ae53f1e1499514937f9c7d5` | source manifest |
| `P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md` | `27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418` | H15 count erratum |
| `replay_v89h15_allq_p13_full_normal_form.py` | `6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f` | H15 client |
| `source_p13_full_normal_form.tar.gz` | `2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81` | H15 archive |

Every path named in the following manifests rehashes at the case root:

| Manifest | Rows |
|---|---|
| `P13_RAW_COORDINATE12_AUDIT_R1_FREEZE.sha256` | 6/6 |
| `P13_RAW_COORDINATE12_AUDIT_R1_EVIDENCE.sha256` | 24/24 |
| `SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256` | 9/9 |
| `SOURCE_P13_FULL_NORMAL_FORM.sha256` | 7/7 |
| `SOURCE_P12_FULL_NORMAL_FORM.sha256` | 12/12 |
| `SOURCE_P12_FLAG.sha256` | 25/25 |
| `SOURCE_FLAG.sha256` | 18/18 |
| `PAYLOAD_CLOSURE.sha256` | 56/56 |
| `P13_FULL_NORMAL_FORM_FREEZE.sha256` | 11/11 |
| `P13_FULL_NORMAL_FORM_EVIDENCE.sha256` | 46/46 |
| `P12_FULL_NORMAL_FORM_FREEZE.sha256` | 16/16 |
| `P12_FULL_NORMAL_FORM_EVIDENCE.sha256` | 82/82 |
| `P12_FLAG_FREEZE.sha256` | 11/11 |
| `P12_FLAG_EVIDENCE.sha256` | 48/48 |
| `FLAG_FREEZE.sha256` | 11/11 |
| `FLAG_EVIDENCE.sha256` | 26/26 |
| `GRAPH_FREEZE.sha256` | 9/9 |
| `GRAPH_EVIDENCE.sha256` | 34/34 |
| `SOURCE_GRAPH.sha256` | 16/16 |

Each 280-row per-host `EVIDENCE.sha256` verifies against that harvest. Local post-harvest `sha256sum -c` logs on both hosts report OK for the same mathematical rows.

Mathematical outputs, identical on r6a and r6b:

| Output | SHA-256 |
|---|---|
| `RAW_P13_COORDINATE12_R1.tsv` | `7ed98587b0c42de16ada758263707cd273f1c5356b4893e106c85f337abe7eae` |
| `RAW_P13_COORDINATE12_ACTIVE_ADDENDS_R1.tsv` | `40d186434a1aa73c2c770663accb200f3ae6215e0fc9f00d6495ac7b2a7ce0d4` |
| `RAW_P13_COORDINATE12_RESULT_R1.txt` | `f476675e3068e1f003bf5b990a757fc8e4db2ca792a9656886e68f174d1dd1cc` |
| stdout | `a98f99c1e93d95b635f285f59700322707c43a8082a362d3e392752ac344cfa8` |

The result text embeds those two TSV digests. Dual-host differences after filename normalization are exactly: `lanes.log`, `.meta`, `.stderr`, and 26 `__pycache__/*.pyc` files. Those are not algebraic output.

Runtime identity that is mathematical or custody-relevant, from both `.meta` files:

| Field | r6a | r6b |
|---|---|---|
| instance | `i-02cb2b4a379ffcc64` | `i-0f089e64c378f5da3` |
| tag | `…T234747Z_r6a` | `…T234747Z_r6b` |
| remote root | `/home/ubuntu/jobs/td6_coordinate12_h19_20260826T234603Z_r6a` | `…_r6b` |
| rc / `final_state` | 0 / `COMPLETE` | 0 / `COMPLETE` |
| Python | 3.12.3, `optimize=0` | 3.12.3, `optimize=0` |
| python-flint | 0.9.0 | 0.9.0 |
| flint module SHA-256 | `1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138` | same |
| packages | `python-flint==0.9.0` only | same |
| VM cap / timeout | 450,000,000 KiB / 43,200 s | same |
| threads | `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1` | same |
| wall / RSS / swaps | 6:38.39 / 297160 KiB / 0 | 6:31.81 / 297176 KiB / 0 |
| stderr exit status | 0 | 0 |

The Python interpreter binaries differ (`1643dacd…` vs `a92f0f95…`). That is expected across instances and is not a mathematical pin. The producer result does not claim binary identity of `/home/ubuntu/venvs/td6/bin/python`.

Both orchestrators pin the same H15 archive and the same H19 payload hashes before extract, refuse a reused job root, refuse non-Linux/non-matching instance identity, and `grep` the result for the source-omission lines and a legal PASS banner. `python_packages` contains no Sage or Singular.

Harvest payload copies of the H19 client, runner, preregistration, erratum, source manifest, and H15 archive are byte-identical to the case-root files. Harvest `source_root/source` copies of all `.py`/`.md`/`.sha256`/`.sh`/`.tsv` files agree with the case root and with each other (105 files checked).

---

## 2. Charge 2 — original H19 defects actually repaired

Original H19 (`replay_v89h19_raw_p13_coordinate12_audit.py`, SHA-256 `7303799cdcda8b67908b1565407b3339aebcff78c185ff0b1c131803bd83474f`) does two things that H19R1 claims to repair.

**Custody.** Original H19 asserts only `H15_SHA` of `replay_v89h15_allq_p13_full_normal_form.py`. H15's own header still pins the H12 client/result/freeze, so some H12 bytes were checked transitively at import, but the H15 archive, `SOURCE_P13`, `SOURCE_P12`, `SOURCE_P12_FLAG`, `PAYLOAD_CLOSURE`, and the vector-record erratum were not. H19R1 hash-pins those four manifests, recursively verifies every row, pins the erratum, and has the orchestrator:

1. hash-check the H15 archive `2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81` before extract;
2. `sha256sum -c` `SOURCE_P13`, `SOURCE_P12`, `SOURCE_P12_FLAG`, `PAYLOAD_CLOSURE`, and `SOURCE_RAW_P13` after extract.

Those source-check stdout files are nonempty OK logs; the corresponding stderr files are empty (SHA-256 `e3b0c442…`, the empty-file digest).

The H15 archive contains 225 regular members. Every unique path from `SOURCE_P13`, `SOURCE_P12`, `SOURCE_P12_FLAG`, `SOURCE_FLAG`, and `PAYLOAD_CLOSURE` (98 paths) is present as `source/<path>` with the working-tree digest. H12 pins H11 client/result/freeze in its header; H11 `ALL_Q` is the 22-tuple `2..14,16..24`. That is the claimed H15→H12→H11→compiler closure.

H19R1 does not itself `sha256sum -c SOURCE_FLAG` or `GRAPH_FREEZE` at runtime. Those files are nonetheless pinned as bytes by `SOURCE_P12_FLAG` / `FLAG_FREEZE` and were rehashed in this review. That is not a remaining original-H19 defect.

**Omission.** Original H19's negative control is:

```python
omitted = total_records[1:]
assert omitted != total_records
```

That deletes a serialized coordinate-12 output row. It never touches a compiler addend. H19R1 instead:

1. decomposes the degree-13 compiler into ordered labeled addends;
2. asserts the exact four-label specialized census;
3. removes `f1_times_dg2:i=13:j=1` from the addend tuple;
4. resums, recanonicalizes, and requires `omitted_parent != parent` and a changed specialized coordinate-12 record set.

The orchestrator additionally requires `source_omission_applied_before_aggregation=true` and the frozen omission label. That is a genuine source-addend omission, not an output-record deletion.

---

## 3. Charge 3 — six families versus H15 and the generic compiler

H15 `compile_current_degree` and H19R1 `raw_degree_contributions` implement the same six loops. The generic payload compiler `compile_x_current` in `payload/jc2/cases/td6_boundary_q2_deformation_20260824/replay.py` is the same formula, looped over degrees `0..39`, with an extra degree-0 constant `-1` that cannot appear at degree 13:

```text
f1*g2' + 2*f2*g1' + 3*f3*q' - 3*p'*g3
- 2*f1'*g2 - f2'*g1.
```

Index arithmetic is identical:

| Family | H19R1 label | `j` / multiplier | scale |
|---|---|---|---|
| `f1*g2'` | `f1_times_dg2:i={i}:j={j}` | `j = degree-i+1`, `scale_affine(g2[j], j)` | 1 |
| `2*f2*g1'` | `2f2_times_dg1:i={i}:j={j}` | `j = degree-i+1`, `scale_affine(g1[j], j)` | 2 |
| `3*f3*q'` | `3f3_times_qprime:i={i}:qdegree={degree-i}` | `Q_PRIME[degree-i]` | `3 * multiplier` |
| `-3*p'*g3` | `minus45_g3:degree={g_degree}` | `g_degree = degree-14` | `-45` |
| `-2*f1'*g2` | `minus2_df1_times_g2:i={i}:j={j}` | `j = degree-(i-1)`, `scale_affine(f1[i], i)` | `-2` |
| `-f2'*g1` | `minus_df2_times_g1:i={i}:j={j}` | `j = degree-(i-1)`, `scale_affine(f2[i], i)` | `-1` |

`scale_affine(form, k)` multiplies the affine form by the integer `k`. For a monomial `t^k` that is exactly `d/dt`. Derivative loops skip the degree-0 slot (`j >= 1` for `g'`, `i >= 1` for `f'`), matching the generic compiler.

The `-45` is `-3 * 15` from `p = t^{15}`, `p' = 15 t^{14}`. At degree 13, `g_degree = -1`, so the `-45*g3` family is correctly not emitted. It is still present in the source, so it is not an omitted family; it is empty at this degree.

`Q_PRIME` is `{0: 1, 24: 25}` plus `e * q_e` at degree `e-1` for each of the 22 retained exponents. The `3*f3*q'` family therefore can fire at degree 13 (for example `i=0` uses `Q_PRIME[13] = 14 q_{14}`). Those addends are in the reconstructed parent. They do not appear in the specialized coordinate-12 census, so they do not contribute to the displayed records.

Canonicalization is `v87.clean` of `QPoly.coerce` values, the same as H15's return. H19R1 asserts `reconstructed == parent` with `parent = h15.compile_current_degree(bands, 13)`. Dual AWS runs with assertions enabled both passed that equality. This review did not re-execute the compiler.

There is no seventh family in `compile_x_current`.

---

## 4. Charge 4 — counts enforced, no omitted source family

**2,757 parameter terms.** `assert events == 2 and len(parent) == 2757`. Frozen H15 already reports 2,757 literal P13 parameter terms from the same compiler. Enforced, not printed.

**22 q.** `ALL_Q = (2..14, 16..24)`, length 22, 15 absent. `v87.propagate_all_q` requires each seen count to be 1. H19R1 asserts `set(seen) == set(h15.ALL_Q)` and `seen[e] == 1` for every `e`. Enforced.

**132 transport variables.** `v87.build_bands` computes the complementary free section of the two transport events and `assert len(free) == 132`. H19R1 calls that function with assertions on. The result line `all_132_transport_variables_retained=true` is a literal string, but the count is asserted in the frozen compiler, not merely advertised. The 132 coordinates are the affine parameters of the bands; H19R1 does not compile FIRST and does not need to, because the diagnostic is the uneliminated current.

**68 nonzero source addends.** This is `len(contributions)` after dropping addends that canonicalize to zero. It is not a separate `assert count == 68`. Completeness of the *families* is the six-loop identity plus `reconstructed == parent`. Candidate slots at degree 13 are 14+14+14+0+14+14 = 70; 68 nonzero addends means two slots vanished, which is consistent and not independently re-counted here. Dual hosts both printed 68. Treating 68 as a frozen integer pin would be stronger than the client; treating it as the measured nonzero-addend count of the frozen loops is correct.

**Could an omitted family change coordinate 12?** The four specialized active addends already sum, in `Q`, to the two displayed F=0 records (Charge 5). Any other addend has specialized coordinate 12 equal to zero, so it cannot change the displayed specialized coordinate 12. Families present in generic `compile_x_current` and missing from H19R1 would also be missing from H15, and then `reconstructed == parent` would not detect them. Direct comparison with `compile_x_current` finds no such family. The degree-0 constant is irrelevant at degree 13.

Specialization is the frozen chart `C = (V^2-U^3)/U` via `h6.specialize_polynomial` → `v85.specialize_e3`. Total records equal F=0 records, so this coordinate is already F-independent before FIRST.

---

## 5. Charge 5 — TSV census and omission arithmetic

Independently parsed `RAW_P13_COORDINATE12_R1.tsv` (both hosts, SHA-256 `7ed98587…`):

| stage | parameter | q | numerator | denominator |
|---|---|---|---|---|
| total | `(27,)` | `()` | `500000000/27` | `U` |
| total | `(29,)` | `()` | `-1562500000/27` | `U` |
| F0 | `(27,)` | `()` | `500000000/27` | `U` |
| F0 | `(29,)` | `()` | `-1562500000/27` | `U` |
| F0_OMIT_SOURCE_ADDEND | `(27,)` | `()` | `500000000/27` | `U` |
| F0_OMIT_SOURCE_ADDEND | `(29,)` | `()` | `-1625000000/27` | `U` |

Independently parsed `RAW_P13_COORDINATE12_ACTIVE_ADDENDS_R1.tsv` (SHA-256 `40d18643…`), in file order:

| label | parameter | q | numerator | denominator |
|---|---|---|---|---|
| `f1_times_dg2:i=13:j=1` | `(29,)` | `()` | `62500000/27` | `U` |
| `2f2_times_dg1:i=12:j=2` | `(27,)` | `()` | `-250000000/27` | `U` |
| `minus2_df1_times_g2:i=13:j=1` | `(29,)` | `()` | `-1625000000/27` | `U` |
| `minus_df2_times_g1:i=12:j=2` | `(27,)` | `()` | `250000000/9` | `U` |

The labels are exactly the preregistered ordered 4-tuple. The index arithmetic matches Charge 3 at degree 13: `j=13-13+1=1` and `j=13-12+1=2` for the `g'` families; `j=13-(13-1)=1` and `j=13-(12-1)=2` for the `f'` families.

Exact sum of the four specialized addends:

```text
(27,): -250000000/27 + 250000000/9 = -250000000/27 + 750000000/27 = 500000000/27
(29,):  62500000/27 + (-1625000000/27) = -1562500000/27
```

This equals both the `total` and `F0` records. Dropping `f1_times_dg2:i=13:j=1` leaves `(27,)` unchanged and sends `(29,)` to `-1625000000/27`, which equals `F0_OMIT_SOURCE_ADDEND`. The producer claim that the source-term omission is real and detected is correct.

The client asserts `tuple(label for label,_ in active) == EXPECTED_ACTIVE_LABELS` and `sum(label == EXPECTED_OMISSION_LABEL ...) == 1`, so a permuted or duplicated census fails closed.

---

## 6. Charge 6 — not the H18 unit; attack stronger inferences

Frozen H18 coordinate-12 TSV (SHA-256 `c5d136d942177882424a75a47c631fbd386d7fff6dbb09187effd32f1be4687f`, matching the confirmed H15+H18 review):

```text
12  ()  ()  3500000000/9*U  V
```

that is `(3500000000/9)*(U/V)`.

Raw specialized coordinate 12 differs in every load-bearing slot:

- parameter support `(27,)` and `(29,)`, not `()`;
- denominator `U`, not `V`;
- two records, not one;
- coefficients `500000000/27` and `-1562500000/27`, not `3500000000/9`.

The client compares against exactly the H18 record

```python
expected = (((), (), "3500000000/9*U", "V"),)
direct_unit = specialized_records == expected
```

and both hosts printed `F0_coordinate12_direct_raw_unit=false` and `FIRST_membership_certificate_needed=true`. Exact `F=0` does not produce the unit either: `total == F0`.

Narrow conclusion, confirmed: the direct raw-unit shortcut fails. An explicit FIRST membership/cancellation bridge remains. H18 is not invalidated. The H18 unit is a fact about the *normalized* P13/FIRST quotient, not about the uneliminated current.

**Attack on stronger language.** The preregistration says that if the raw coordinate is not the unit, “the client identifies the exact support that FIRST elimination cancels.” That is not established.

The raw polynomial is E3-valued in 132 affine parameters. FIRST substitution multiplies E3 coefficients by E3[q] images of those parameters. E3 is an 18-coordinate algebra (`scalar_coordinates` concatenates the k-value coordinates). Coordinate 12 of a product is not the product of coordinate-12 parts. Quadratic monomials and other E3 coordinates of the 2,757-term parent can feed H18 coordinate 12 even when their raw coordinate 12 is zero. The four addends and two records are the raw specialized coordinate-12 support. They are not a proven FIRST preimage of `(3500000000/9)*(U/V)`.

The producer *result* does not make that stronger claim. It says the raw specialized coordinate is not the unit, and that a FIRST-membership/cancellation certificate remains necessary. That is the theorem.

Do not read this package as: “FIRST merely cancels `(27,)` and `(29,)` into the H18 unit.” That is a successor computation, not this diagnostic.

---

## 7. Charge 7 — assertions, flint, Singular, preflight

Both metas record `python_optimize=0`. The orchestrator `unset PYTHONOPTIMIZE` and aborts if `sys.flags.optimize != 0`. Assertions were enabled. The reconstruction equality, census, 2757, 22 q, 132 free section, and omission inequalities therefore executed.

python-flint is pinned at 0.9.0 with extension SHA-256 `1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138` before any extract. `pip freeze` on both hosts is exactly that package. This client does not factor denominators; the pin is custody of the shared exact stack used by the imported H15/V87 arithmetic, not a second P13 computation.

No `singular` or `qring` symbol appears in the H19R1 client or the H15 client. Arithmetic is `Rat3` / `E3` / `QPoly`.

The source-census preflight is the dead branch

```python
if not EXPECTED_OMISSION_LABEL:
    print("H19R1_PREFLIGHT_ACTIVE_LABELS=" + ...)
    return
```

In the frozen producer `EXPECTED_OMISSION_LABEL` is the nonempty first preregistered label, so that branch cannot run. The four labels are hardcoded in the client, listed in the preregistration, and asserted on both AWS replicas. A wrong census fails closed; it cannot be rediscovered at dual-launch time. No unfrozen choice leaks into the frozen producer. A separate preflight harvest is not in the freeze; it is not needed once the labels are pins.

---

## 8. Charge 8 — firewall

A confirmation of H19R1 does **not** prove:

- original-FIRST membership multipliers, or any identity
  `s = a * P13_12 + sum b_i FIRST_i + F h`;
- that raw coordinate 12 becomes the H18 unit by cancelling only the two displayed records;
- a lift that retains independent total `F` as a base variable;
- q15 as an independent source coordinate;
- omitted TD6 moduli (orbit, pole, correction, centering, boundary, or other);
- a whole-TD6 theorem, a two-sided Rees/source cover, or JC2.

The producer result already prints

```text
independent_total_F_unit_claim=false
whole_TD6_killed=false
JC2_resolved=false
```

H18 remains the confirmed no-common-zero theorem on the normalized P13/FIRST quotient. The cheapest honest successor is still an explicit FIRST-membership/cancellation certificate for coordinate 12, not a replay of this raw audit and not a P12 recombination.

---

## Upstream H15 / H18 pins used as context, not as this theorem

Independently rehashed and used only as the parent normal-form/unit statements that H19R1 compares against:

| Artifact | SHA-256 |
|---|---|
| `P13_FULL_NORMAL_FORM_RESULT.md` | `29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c` |
| `P13_FULL_NORMAL_FORM_EVIDENCE.sha256` | `7c77bf767eea783d8d25a4c99c9201d039ed24d3a9037a1d2034accba569aa67` |
| `P13_FULL_NORMAL_FORM_FREEZE.sha256` | `4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18` |
| `P13_COORDINATE12_UNIT_RESULT.md` | `0f152a88ba6422b04a3b4274ad5a0e71996c1c65395c7518b6e725321ab32d7f` |
| `P13_COORDINATE12_UNIT_EVIDENCE.sha256` | `bc9590017fb0f6942c9b7d396ba2b95e56fd1cbad2fc8c2b84e2b753bf79932d` |
| `P13_COORDINATE12_UNIT_FREEZE.sha256` | `0d3a9a6aad58635e9f02f160a3012b28dc351ecdbbafd97e59b7c1c2cda44974` |
| H15+H18 combined review | `cb4a85e298aacbbe5e1dc68c23d3f3819b7aa880d705da683d20fb61a06c1fc8` |

The H15 count erratum (238 vector records / 535 scalar entries, one of which is the H18 unit) is hash-pinned by H19R1 and does not alter this raw audit.

---

## Cleanest correction

No mathematical correction is required.

The one sentence in `PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md` that overstates the client should be read as: the client emits the raw specialized coordinate-12 support, which is not the H18 unit. A later FIRST-membership client must track coordinate 12 through the affine solve. That wording is not in the producer result and does not change the verdict.

---

## Commands used

```text
python3  # hashlib of every charged pin and every manifest row;
         # tarfile member audit of source_p13_full_normal_form.tar.gz;
         # independent TSV parse and Fraction arithmetic on the four addends
git rev-parse HEAD
```

No `compile_current_degree` replay, no AWS wrapper replay, no Singular.

**CONFIRMED**
