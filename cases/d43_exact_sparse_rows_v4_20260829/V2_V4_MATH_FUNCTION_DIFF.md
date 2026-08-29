# V2 -> V3 -> V4 mathematical-function byte-diff closure

Generated deterministically by `math_function_diff_v4.py` (rerun it to reproduce this file byte-for-byte); adjudication date 2026-08-29.

Pinned inputs (whole-file SHA-256, verified before extraction):

* `selected_rows_v2.py`: `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2`
* `selected_rows_v3.py`: `3a29c8495b03026feda09b3b0629f95a7f69c41fbe9adf89fc6ad44e2945f9da`
* `selected_rows_v4.py`: `3b3519f86df300ce46109b18546fe1c84edf68a0c0606849bca1c5d4e47971c5`

## Verdict

**CLOSED - NO MATHEMATICAL DRIFT BEYOND THE REVIEWED CHANGES.**

* v3 -> v4: every top-level function is byte-identical; the only
  module-level assignment diffs are the two `.v3` -> `.v4` schema
  strings (`SCHEMA`, `MANIFEST_SCHEMA`).  The module docstring and
  the optimized-Python refusal message (module-level statements,
  not functions) are the only other file diffs.
* v2 -> v4: 39 shared functions are byte-identical, including the
  entire collapsed-arithmetic and jet/row core (every `cp_*`,
  `cv_add/scale/constant`, `cs_*`, `cj_*`, `collapse_vexpr`,
  `convert_a_orbit`, `collapsed_gm_jet2`, `collapsed_b_block`,
  `_selected_product`, `selected_source_rows`, `evaluate_*`, and
  every canonicalization/semantic-digest function).
* The 25 differing shared functions decompose exactly into the
  five repair classes charged by the v2 hostile review and
  confirmed by the v3/v4 reviews; no predicate was weakened and
  no numeric or algebraic expression changed anywhere.

Two version literals inside mathematical functions are retained
byte-for-byte from v3 to keep the v3->v4 math diff empty and are
disclosed rather than renamed: `cv_mul`'s cap message says
`exact v3 lane` and `build_collapsed_side` logs the progress tag
`D43-v3-<side>`.  Both are inert log/error strings.

## Classified differing functions (v2 -> v4)

* `_load_pickle_after_hash`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `assemble_pair`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES
* `assert_operational_registration`: ASSERT_TO_REQUIRE_SAME_PREDICATES + VERSION_LITERAL_STRING_ONLY
* `assert_raw_b_orbits`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `banked_pin_audit`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `build_collapsed_side`: VERSION_LITERAL_STRING_ONLY + EXPLICIT_V1_FACT_REVALIDATION_ADDED
* `build_side`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES
* `collapse_r1_ring_element`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `collapsed_d21_gate`: LITERAL_D21_GATE_REWRITE_CHARGED_ROOT_1
* `conditional_emit_all`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES
* `cv_mul`: VERSION_LITERAL_STRING_ONLY
* `expected_collapsed_d21_band20`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `load_manifest`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `load_pair`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES
* `load_shard_receipt`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES
* `load_side_receipt`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES + EXPLICIT_V1_FACT_REVALIDATION_ADDED
* `main`: LEASE_THREADING_AND_BINDING
* `print_registry`: EXPLICIT_V1_FACT_REVALIDATION_ADDED
* `registered_modular_replay`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `template_bridge_modular_gate`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `template_bridge_spec`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `validate_cover`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `validate_exact_inventory`: ASSERT_TO_REQUIRE_SAME_PREDICATES
* `validate_preflight_receipt`: LEASE_THREADING_AND_BINDING + ASSERT_TO_REQUIRE_SAME_PREDICATES
* `verify_operational_sources`: ASSERT_TO_REQUIRE_SAME_PREDICATES

Class key: `ASSERT_TO_REQUIRE_SAME_PREDICATES` converts bare asserts to fail-closed
`require`/`CustodyError` raises with unchanged predicates (checks
were only added, never removed); `LEASE_THREADING_AND_BINDING` threads the
exclusive run lease and its nonce through every payload and
loader; `LITERAL_D21_GATE_REWRITE_CHARGED_ROOT_1`
replaces the v2 digest-decided D21 gate with literal structural
equality plus literal mutation refusal (digests receipts-only);
`VERSION_LITERAL_STRING_ONLY` changes only version strings in messages or
log tags; `EXPLICIT_V1_FACT_REVALIDATION_ADDED` adds explicit re-validation of
frozen-v1 facts previously guarded only by v1's own asserts.

Removed in v3/v4: `atomic_text`, `finalize_run` (the v2 early-positive-authority publisher
and its helper).  Added in v3/v4: `CustodyError`, `finalize_candidate`, `lease_binding`, `load_run_lease`, `probe_lock_held`, `require`, `require_lease_binding`, `require_registry`, `require_sparse_free_support`.

## Full unified diffs of the differing shared functions

### `_load_pickle_after_hash`

```diff
--- v2:_load_pickle_after_hash
+++ v4:_load_pickle_after_hash
@@ -2,5 +2,5 @@
     if not expected_hash or len(expected_hash) != 64:
-        raise ValueError("missing explicit SHA-256")
+        raise CustodyError("missing explicit SHA-256")
     if sha256_path(path) != expected_hash:
-        raise ValueError("payload hash drift before unpickle")
+        raise CustodyError("payload hash drift before unpickle")
     with path.open("rb") as stream:
```

### `assemble_pair`

```diff
--- v2:assemble_pair
+++ v4:assemble_pair
@@ -1,4 +1,4 @@
 def assemble_pair(manifest_path: Path, preflight_path: Path,
-                  f_receipt_path: Path, g_receipt_path: Path,
-                  output_path: Path):
+                  lease_path: Path, f_receipt_path: Path,
+                  g_receipt_path: Path, output_path: Path):
     manifest, manifest_hash = load_manifest(manifest_path)
@@ -6,4 +6,6 @@
     verify_operational_sources(manifest)
+    run_dir = Path(os.environ.get("JOB_ROOT", ""))
+    lease, lease_hash = load_run_lease(lease_path, run_dir)
     _preflight, preflight_hash = validate_preflight_receipt(
-        preflight_path, manifest, manifest_hash)
+        preflight_path, manifest, manifest_hash, lease, lease_hash)
     side_metadata = {}
@@ -12,4 +14,5 @@
         payload, receipt = load_side_receipt(path, manifest_hash,
-                                             preflight_hash)
-        assert payload["side"] == side
+                                             preflight_hash, lease,
+                                             lease_hash)
+        require(payload["side"] == side, "side receipt side drift")
         side_metadata[side] = {
@@ -18,3 +21,4 @@
                 "operational_source_list_sha256", "registry_sha256",
-                "support_sha256", "coefficient_algebra_sha256")}
+                "support_sha256", "coefficient_algebra_sha256",
+                "run_nonce", "lease_sha256")}
         del payload
@@ -23,11 +27,16 @@
                 "operational_source_list_sha256", "registry_sha256",
-                "support_sha256", "coefficient_algebra_sha256")
+                "support_sha256", "coefficient_algebra_sha256",
+                "run_nonce", "lease_sha256")
     for key in matching:
-        assert side_metadata["f"][key] == side_metadata["g"][key]
-    assert side_metadata["f"]["operational_source_list_sha256"] == \
-        manifest["operational_source_list_sha256"]
+        require(side_metadata["f"][key] == side_metadata["g"][key],
+                "side receipts disagree on %s" % key)
+    require(side_metadata["f"]["operational_source_list_sha256"] ==
+            manifest["operational_source_list_sha256"],
+            "side receipts bind a different source list")
     workers = {side: receipts[side]["worker"] for side in ("f", "g")}
-    assert workers["f"]["pid"] != workers["g"]["pid"]
-    assert workers["f"]["hostname"] == workers["g"]["hostname"] == \
-        manifest["aws"]["expected_hostname"]
+    require(workers["f"]["pid"] != workers["g"]["pid"],
+            "side builds share a PID")
+    require(workers["f"]["hostname"] == workers["g"]["hostname"] ==
+            manifest["aws"]["expected_hostname"],
+            "side builds are not on the registered host")
     overlap = (workers["f"]["started_epoch_ns"] <=
@@ -37,3 +46,3 @@
     if not overlap:
-        raise ValueError("f/g build intervals do not prove concurrency")
+        raise CustodyError("f/g build intervals do not prove concurrency")
     pair = {
@@ -60,3 +69,5 @@
     }
+    pair.update(lease_binding(lease, lease_hash))
     pair["pair_custody_sha256"] = sha256_bytes(canonical_json({
+        "run_nonce": pair["run_nonce"],
         "side_receipts": pair["side_receipts"],
```

### `assert_operational_registration`

```diff
--- v2:assert_operational_registration
+++ v4:assert_operational_registration
@@ -10,2 +10,2 @@
             aws.get("registration_status") != "REGISTERED_IMMUTABLE"):
-        raise ValueError("v2 manifest is review-only and AWS-unregistered")
+        raise CustodyError("v3 manifest is review-only and AWS-unregistered")
```

### `assert_raw_b_orbits`

```diff
--- v2:assert_raw_b_orbits
+++ v4:assert_raw_b_orbits
@@ -2,7 +2,11 @@
     expected = {12: R1.vC(R1.rmono(B=1))}
-    assert raw_orbits["B"]["series"] == expected
-    assert raw_orbits["GB42"]["series"] == expected
-    assert raw_orbits["GB21"]["series"] == expected
-    assert raw_orbits["B"]["size"] == raw_orbits["GB42"]["size"] == 42
-    assert raw_orbits["GB21"]["size"] == 21
+    require(raw_orbits["B"]["series"] == expected,
+            "raw B source series drift")
+    require(raw_orbits["GB42"]["series"] == expected,
+            "raw GB42 source series drift")
+    require(raw_orbits["GB21"]["series"] == expected,
+            "raw GB21 source series drift")
+    require(raw_orbits["B"]["size"] == raw_orbits["GB42"]["size"] == 42,
+            "raw B/GB42 orbit size drift")
+    require(raw_orbits["GB21"]["size"] == 21, "raw GB21 orbit size drift")
     try:
@@ -13,2 +17,2 @@
     else:
-        raise AssertionError("uncancelled EB was accepted")
+        raise CustodyError("uncancelled EB was accepted")
```

### `banked_pin_audit`

```diff
--- v2:banked_pin_audit
+++ v4:banked_pin_audit
@@ -6,6 +6,7 @@
         if sha256_path(path) != manifest["input_sha256"][relative]:
-            raise ValueError("banked certificate drift")
+            raise CustodyError("banked certificate drift")
         point = json.loads(path.read_text())["point"]
         graph = point["graph_156"]
-        assert graph["Xf_alpha"] == graph["Xg_beta"] == 0
+        require(graph["Xf_alpha"] == graph["Xg_beta"] == 0,
+                "banked alpha/beta drift")
         nonzero = set()
@@ -14,3 +15,3 @@
                 nonzero.add(BASE.GRAPH_TO_SOURCE.get(name, name))
-        assert nonzero == set(SUPPORT)
+        require(nonzero == set(SUPPORT), "banked support drift")
         result.append({"prime": prime, "support_exact": True,
```

### `build_collapsed_side`

```diff
--- v2:build_collapsed_side
+++ v4:build_collapsed_side
@@ -4,2 +4,4 @@
     raw_orbits, names, registry_hash, pin42 = BASE.sparse_registry()
+    require_registry(names, registry_hash, pin42)
+    require_sparse_free_support()
     assert_raw_b_orbits(raw_orbits)
@@ -14,3 +16,3 @@
     a_jet = collapsed_gm_jet2(orbit_names, collapsed_orbits, depth,
-                              "D43-v2-%s" % side)
+                              "D43-v3-%s" % side)
     jet = cj_mul(a_jet, collapsed_b_block(b_power, depth), depth)
```

### `build_side`

```diff
--- v2:build_side
+++ v4:build_side
@@ -1,3 +1,3 @@
-def build_side(manifest_path: Path, preflight_path: Path, side: str,
-               output_path: Path):
+def build_side(manifest_path: Path, preflight_path: Path, lease_path: Path,
+               side: str, output_path: Path):
     manifest, manifest_hash = load_manifest(manifest_path)
@@ -5,6 +5,8 @@
     inventory = verify_operational_sources(manifest)
+    run_dir = Path(os.environ.get("JOB_ROOT", ""))
+    lease, lease_hash = load_run_lease(lease_path, run_dir)
     _preflight, preflight_hash = validate_preflight_receipt(
-        preflight_path, manifest, manifest_hash)
+        preflight_path, manifest, manifest_hash, lease, lease_hash)
     if not manifest["authorization"]["build_independent_sides"]:
-        raise ValueError("side builds are not authorized")
+        raise CustodyError("side builds are not authorized")
     started_ns = time.time_ns()
@@ -14,3 +16,3 @@
             for monomial in expression for index in monomial}
-    assert used <= set(SUPPORT)
+    require(used <= set(SUPPORT), "side jet escapes the registered support")
     payload = {
@@ -40,2 +42,3 @@
     }
+    payload.update(lease_binding(lease, lease_hash))
     atomic_pickle(output_path, payload)
@@ -45,3 +48,4 @@
         "registry_sha256", "support_sha256", "coefficient_algebra_sha256",
-        "jet_semantic_sha256", "worker")}
+        "jet_semantic_sha256", "worker",
+        "run_nonce", "lease_sha256", "terminal_authority")}
     receipt.update({"payload": output_path.name,
```

### `collapse_r1_ring_element`

```diff
--- v2:collapse_r1_ring_element
+++ v4:collapse_r1_ring_element
@@ -13,3 +13,4 @@
     collapsed = COMMON.collapse_r1_ring_element(signed)
-    assert all(len(key) == 2 and min(key) >= 0 for key in collapsed)
+    require(all(len(key) == 2 and min(key) >= 0 for key in collapsed),
+            "collapsed monomial escapes the two W coordinates")
     return collapsed
```

### `collapsed_d21_gate`

```diff
--- v2:collapsed_d21_gate
+++ v4:collapsed_d21_gate
@@ -1,5 +1,10 @@
 def collapsed_d21_gate(rows, manifest, registry_names):
+    """Literal structural band-20 equality with literal mutation refusal.
+
+    The decision rests on Python structural equality of the canonical
+    collapsed objects (registry-ordered variable monomials over exact
+    ``RadicalCoefficient`` values).  SHA-256 digests are computed only as
+    custody receipts and never decide the gate.
+    """
     expected = expected_collapsed_d21_band20(manifest, registry_names)
-    actual_digest = semantic_rows_sha256(rows, registry_names)
-    expected_digest = semantic_rows_sha256(expected, registry_names)
     mutation_rows = {
@@ -12,2 +17,16 @@
     }
+    for name, mutated in sorted(mutation_rows.items()):
+        if mutated == expected:
+            raise CustodyError(
+                "collapsed D21 mutation %s is not literally distinct "
+                "from the reference" % name)
+    if rows != expected:
+        raise CustodyError(
+            "exact collapsed D21 band20 literal equality failed")
+    for name, mutated in sorted(mutation_rows.items()):
+        if rows == mutated:
+            raise CustodyError(
+                "collapsed D21 band20 literally equals mutation %s" % name)
+    actual_digest = semantic_rows_sha256(rows, registry_names)
+    expected_digest = semantic_rows_sha256(expected, registry_names)
     mutation_digests = {
@@ -16,8 +35,10 @@
     }
-    if len({expected_digest, *mutation_digests.values()}) != 4:
-        raise ValueError("collapsed D21 mutation was not detected")
-    if actual_digest != expected_digest:
-        raise ValueError("exact collapsed D21 band20 equality failed")
+    require(actual_digest == expected_digest,
+            "receipt digests disagree after literal equality")
+    require(len({expected_digest, *mutation_digests.values()}) == 4,
+            "receipt digests fail to separate the mutations")
     return {
-        "status": "PASS_EXACT_COLLAPSED_D21_BAND20_EQUALITY",
+        "status": "PASS_EXACT_COLLAPSED_D21_BAND20_LITERAL_EQUALITY",
+        "decision_basis": "LITERAL_STRUCTURAL_EQUALITY",
+        "digests_are_receipts_only": True,
         "actual_semantic_sha256": actual_digest,
@@ -25,3 +46,3 @@
         "required_mutation_digests": mutation_digests,
-        "all_mutations_distinct": True,
+        "all_mutations_literally_refused": True,
     }
```

### `conditional_emit_all`

```diff
--- v2:conditional_emit_all
+++ v4:conditional_emit_all
@@ -1,3 +1,4 @@
 def conditional_emit_all(manifest_path: Path, preflight_path: Path,
-                         pair_path: Path, output_dir: Path):
+                         lease_path: Path, pair_path: Path,
+                         output_dir: Path):
     manifest, manifest_hash = load_manifest(manifest_path)
@@ -5,5 +6,8 @@
     verify_operational_sources(manifest)
+    run_dir = Path(os.environ.get("JOB_ROOT", ""))
+    lease, lease_hash = load_run_lease(lease_path, run_dir)
     _preflight, preflight_hash = validate_preflight_receipt(
-        preflight_path, manifest, manifest_hash)
-    jf, jg, names, pair = load_pair(pair_path, manifest_hash, preflight_hash)
+        preflight_path, manifest, manifest_hash, lease, lease_hash)
+    jf, jg, names, pair = load_pair(pair_path, manifest_hash, preflight_hash,
+                                    lease, lease_hash)
     band20 = selected_source_rows(jf, jg, BAND_TARGETS[20])
@@ -18,2 +22,3 @@
     }
+    gate.update(lease_binding(lease, lease_hash))
     try:
@@ -49,2 +54,3 @@
         }
+        payload.update(lease_binding(lease, lease_hash))
         path = shard_dir / ("band%02d.pkl" % band)
@@ -54,3 +60,4 @@
             "preflight_receipt_sha256", "pair_custody_sha256",
-            "pilot_gate_sha256", "band", "semantic_sha256")}
+            "pilot_gate_sha256", "band", "semantic_sha256",
+            "run_nonce", "lease_sha256", "terminal_authority")}
         receipt.update({"payload": path.name,
@@ -63,5 +70,6 @@
         path, manifest_hash, preflight_hash, pair["pair_custody_sha256"],
-        gate_hash) for path in shard_receipt_paths]
+        gate_hash, lease, lease_hash) for path in shard_receipt_paths]
     rows = validate_cover(shards)
-    assert rows == {target: all_rows[target] for target in TARGETS}
+    require(rows == {target: all_rows[target] for target in TARGETS},
+            "reloaded shard cover is not literally the emitted rows")
     inventory = validate_exact_inventory(rows)
@@ -91,2 +99,3 @@
     }
+    merged.update(lease_binding(lease, lease_hash))
     merge_path = output_dir / "d43_a00pp_exact_184_raw_J_rows.pkl"
@@ -106,2 +115,3 @@
     }
+    receipt.update(lease_binding(lease, lease_hash))
     atomic_json(output_dir / "MERGE_RECEIPT.json", receipt)
```

### `cv_mul`

```diff
--- v2:cv_mul
+++ v4:cv_mul
@@ -6,3 +6,3 @@
             if len(monomial) > D:
-                raise ValueError("variable-degree cap exceeded in exact v2 lane")
+                raise ValueError("variable-degree cap exceeded in exact v3 lane")
             coefficient = cp_mul(ca, cb)
```

### `expected_collapsed_d21_band20`

```diff
--- v2:expected_collapsed_d21_band20
+++ v4:expected_collapsed_d21_band20
@@ -6,3 +6,3 @@
                                       manifest["input_sha256"][relative])
-    assert payload["D"] == 21
+    require(payload["D"] == 21, "D21 reference bank depth drift")
     name_to_id = {name: index for index, name in enumerate(registry_names)}
```

### `load_manifest`

```diff
--- v2:load_manifest
+++ v4:load_manifest
@@ -3,12 +3,19 @@
     manifest = json.loads(raw)
-    assert manifest["schema"] == MANIFEST_SCHEMA
-    assert manifest["D"] == D and manifest["absolute_depth"] == ABSOLUTE_DEPTH
-    assert manifest["expected_registry_sha256"] == EXPECTED_REGISTRY_SHA256
-    assert manifest["support"] == list(SUPPORT)
-    assert manifest["support_sha256"] == support_sha256()
-    assert manifest["target_registry_sha256"] == target_registry_sha256()
-    assert manifest["coefficient_algebra"] == COEFFICIENT_ALGEBRA
-    assert manifest["coefficient_algebra_sha256"] == \
-        coefficient_algebra_sha256()
-    assert manifest["authorization"] == {
+    require(manifest["schema"] == MANIFEST_SCHEMA, "manifest schema drift")
+    require(manifest["D"] == D and
+            manifest["absolute_depth"] == ABSOLUTE_DEPTH,
+            "manifest depth drift")
+    require(manifest["expected_registry_sha256"] == EXPECTED_REGISTRY_SHA256,
+            "manifest registry hash drift")
+    require(manifest["support"] == list(SUPPORT), "manifest support drift")
+    require(manifest["support_sha256"] == support_sha256(),
+            "manifest support hash drift")
+    require(manifest["target_registry_sha256"] == target_registry_sha256(),
+            "manifest target registry hash drift")
+    require(manifest["coefficient_algebra"] == COEFFICIENT_ALGEBRA,
+            "manifest coefficient algebra drift")
+    require(manifest["coefficient_algebra_sha256"] ==
+            coefficient_algebra_sha256(),
+            "manifest coefficient algebra hash drift")
+    require(manifest["authorization"] == {
         "build_independent_sides": True,
@@ -16,15 +23,7 @@
         "solve": False,
-    }
-    assert 0 < manifest["preflight_receipt_max_age_seconds"] <= 259200
-    assert manifest["resource_contract"] == {
-        "conditional_emitter_address_space_bytes": 549755813888,
-        "cpu_f": "2", "cpu_g": "3",
-        "file_size_bytes": 137438953472,
-        "kill_after_seconds": 60,
-        "minimum_disk_free_bytes": 107374182400,
-        "minimum_memory_available_kib": 838860800,
-        "side_address_space_bytes": 412316860416,
-        "timeout_seconds": 86400,
-        "zero_swap_required": True,
-    }
+    }, "manifest authorization drift")
+    require(0 < manifest["preflight_receipt_max_age_seconds"] <= 259200,
+            "manifest preflight age bound drift")
+    require(manifest["resource_contract"] == RESOURCE_CONTRACT,
+            "manifest resource contract drift")
     return manifest, sha256_bytes(raw)
```

### `load_pair`

```diff
--- v2:load_pair
+++ v4:load_pair
@@ -1,16 +1,27 @@
-def load_pair(pair_path: Path, manifest_hash: str, preflight_hash: str):
+def load_pair(pair_path: Path, manifest_hash: str, preflight_hash: str,
+              lease, lease_hash):
     pair = json.loads(pair_path.read_text())
-    assert pair["schema"] == PAIR_SCHEMA
-    assert pair["status"] == "MATCHED_INDEPENDENT_F_G_PAIR_COMPLETE"
-    assert pair["manifest_sha256"] == manifest_hash
-    assert pair["preflight_receipt_sha256"] == preflight_hash
-    assert pair["registry_sha256"] == EXPECTED_REGISTRY_SHA256
-    assert pair["support_sha256"] == support_sha256()
-    assert pair["coefficient_algebra_sha256"] == coefficient_algebra_sha256()
-    assert pair["pair_custody_sha256"] == sha256_bytes(canonical_json({
+    require(pair["schema"] == PAIR_SCHEMA, "pair schema drift")
+    require(pair["status"] == "MATCHED_INDEPENDENT_F_G_PAIR_COMPLETE",
+            "pair status drift")
+    require(pair["manifest_sha256"] == manifest_hash,
+            "pair manifest hash drift")
+    require(pair["preflight_receipt_sha256"] == preflight_hash,
+            "pair preflight hash drift")
+    require_lease_binding(pair, lease, lease_hash, "pair")
+    require(pair["registry_sha256"] == EXPECTED_REGISTRY_SHA256,
+            "pair registry hash drift")
+    require(pair["support_sha256"] == support_sha256(),
+            "pair support hash drift")
+    require(pair["coefficient_algebra_sha256"] ==
+            coefficient_algebra_sha256(),
+            "pair coefficient algebra hash drift")
+    require(pair["pair_custody_sha256"] == sha256_bytes(canonical_json({
+        "run_nonce": pair["run_nonce"],
         "side_receipts": pair["side_receipts"],
         "worker_concurrency": pair["worker_concurrency"],
-    }))
-    assert pair["worker_concurrency"]["status"] == \
-        "PASS_OVERLAPPING_DISTINCT_PIDS"
+    })), "pair custody digest drift")
+    require(pair["worker_concurrency"]["status"] ==
+            "PASS_OVERLAPPING_DISTINCT_PIDS",
+            "pair concurrency status drift")
     result = {}
@@ -20,12 +31,16 @@
         if pair_path.parent.resolve() not in receipt_path.parents:
-            raise ValueError("side receipt escapes pair directory")
+            raise CustodyError("side receipt escapes pair directory")
         if sha256_path(receipt_path) != item["sha256"]:
-            raise ValueError("side receipt hash drift")
+            raise CustodyError("side receipt hash drift")
         payload, receipt = load_side_receipt(receipt_path, manifest_hash,
-                                             preflight_hash)
-        assert receipt["payload_sha256"] == item["payload_sha256"]
-        assert payload["jet_semantic_sha256"] == item["jet_semantic_sha256"]
+                                             preflight_hash, lease,
+                                             lease_hash)
+        require(receipt["payload_sha256"] == item["payload_sha256"],
+                "pair payload hash drift")
+        require(payload["jet_semantic_sha256"] == item["jet_semantic_sha256"],
+                "pair semantic digest drift")
         result[side] = payload
-    assert tuple(result["f"]["registry_names"]) == \
-        tuple(result["g"]["registry_names"])
+    require(tuple(result["f"]["registry_names"]) ==
+            tuple(result["g"]["registry_names"]),
+            "pair registries disagree")
     return result["f"]["jet"], result["g"]["jet"], \
```

### `load_shard_receipt`

```diff
--- v2:load_shard_receipt
+++ v4:load_shard_receipt
@@ -2,9 +2,14 @@
                        preflight_hash: str, pair_custody: str,
-                       gate_hash: str):
+                       gate_hash: str, lease, lease_hash):
     receipt = json.loads(receipt_path.read_text())
-    assert receipt["schema"] == SHARD_SCHEMA
-    assert receipt["manifest_sha256"] == manifest_hash
-    assert receipt["preflight_receipt_sha256"] == preflight_hash
-    assert receipt["pair_custody_sha256"] == pair_custody
-    assert receipt["pilot_gate_sha256"] == gate_hash
+    require(receipt["schema"] == SHARD_SCHEMA, "shard receipt schema drift")
+    require(receipt["manifest_sha256"] == manifest_hash,
+            "shard receipt manifest hash drift")
+    require(receipt["preflight_receipt_sha256"] == preflight_hash,
+            "shard receipt preflight hash drift")
+    require(receipt["pair_custody_sha256"] == pair_custody,
+            "shard receipt pair custody drift")
+    require(receipt["pilot_gate_sha256"] == gate_hash,
+            "shard receipt gate hash drift")
+    require_lease_binding(receipt, lease, lease_hash, "shard receipt")
     payload_path = receipt_path.parent / receipt["payload"]
@@ -12,11 +17,19 @@
                                       receipt["payload_sha256"])
-    assert payload["schema"] == SHARD_SCHEMA
-    assert payload["manifest_sha256"] == manifest_hash
-    assert payload["preflight_receipt_sha256"] == preflight_hash
-    assert payload["pair_custody_sha256"] == pair_custody
-    assert payload["pilot_gate_sha256"] == gate_hash
-    assert payload["semantic_sha256"] == semantic_rows_sha256(
-        payload["rows"], payload["registry_names"])
-    assert payload["semantic_sha256"] == receipt["semantic_sha256"]
-    assert tuple(payload["targets"]) == tuple(payload["rows"])
+    require(payload["schema"] == SHARD_SCHEMA, "shard payload schema drift")
+    require(payload["manifest_sha256"] == manifest_hash,
+            "shard payload manifest hash drift")
+    require(payload["preflight_receipt_sha256"] == preflight_hash,
+            "shard payload preflight hash drift")
+    require(payload["pair_custody_sha256"] == pair_custody,
+            "shard payload pair custody drift")
+    require(payload["pilot_gate_sha256"] == gate_hash,
+            "shard payload gate hash drift")
+    require_lease_binding(payload, lease, lease_hash, "shard payload")
+    require(payload["semantic_sha256"] == semantic_rows_sha256(
+        payload["rows"], payload["registry_names"]),
+        "shard payload semantic digest drift")
+    require(payload["semantic_sha256"] == receipt["semantic_sha256"],
+            "shard payload/receipt semantic digest mismatch")
+    require(tuple(payload["targets"]) == tuple(payload["rows"]),
+            "shard payload target census drift")
     return payload
```

### `load_side_receipt`

```diff
--- v2:load_side_receipt
+++ v4:load_side_receipt
@@ -1,20 +1,31 @@
 def load_side_receipt(receipt_path: Path, manifest_hash: str,
-                      preflight_hash: str):
+                      preflight_hash: str, lease, lease_hash):
     receipt = json.loads(receipt_path.read_text())
-    assert receipt["schema"] == SIDE_SCHEMA
-    assert receipt["manifest_sha256"] == manifest_hash
-    assert receipt["preflight_receipt_sha256"] == preflight_hash
+    require(receipt["schema"] == SIDE_SCHEMA, "side receipt schema drift")
+    require(receipt["manifest_sha256"] == manifest_hash,
+            "side receipt manifest hash drift")
+    require(receipt["preflight_receipt_sha256"] == preflight_hash,
+            "side receipt preflight hash drift")
+    require_lease_binding(receipt, lease, lease_hash, "side receipt")
     payload_path = receipt_path.parent / receipt["payload"]
     payload = _load_pickle_after_hash(payload_path, receipt["payload_sha256"])
-    assert payload["schema"] == SIDE_SCHEMA
-    assert payload["manifest_sha256"] == manifest_hash
-    assert payload["preflight_receipt_sha256"] == preflight_hash
-    assert payload["jet_semantic_sha256"] == semantic_rows_sha256(
-        payload["jet"], payload["registry_names"])
-    assert payload["jet_semantic_sha256"] == receipt["jet_semantic_sha256"]
-    assert payload["worker"] == receipt["worker"]
-    assert (payload["worker"]["pid"] > 1 and
+    require(payload["schema"] == SIDE_SCHEMA, "side payload schema drift")
+    require(payload["manifest_sha256"] == manifest_hash,
+            "side payload manifest hash drift")
+    require(payload["preflight_receipt_sha256"] == preflight_hash,
+            "side payload preflight hash drift")
+    require_lease_binding(payload, lease, lease_hash, "side payload")
+    require(payload["jet_semantic_sha256"] == semantic_rows_sha256(
+        payload["jet"], payload["registry_names"]),
+        "side payload semantic digest drift")
+    require(payload["jet_semantic_sha256"] == receipt["jet_semantic_sha256"],
+            "side payload/receipt semantic digest mismatch")
+    require(payload["worker"] == receipt["worker"],
+            "side payload/receipt worker mismatch")
+    require(payload["worker"]["pid"] > 1 and
             payload["worker"]["completed_epoch_ns"] >=
-            payload["worker"]["started_epoch_ns"])
-    assert payload["coefficient_algebra"] == COEFFICIENT_ALGEBRA
+            payload["worker"]["started_epoch_ns"],
+            "side worker interval malformed")
+    require(payload["coefficient_algebra"] == COEFFICIENT_ALGEBRA,
+            "side payload coefficient algebra drift")
     _orbits, expected_names, registry_hash, expected_pin42 = \
@@ -22,7 +33,11 @@
     del _orbits
-    assert registry_hash == EXPECTED_REGISTRY_SHA256
-    assert tuple(payload["registry_names"]) == expected_names
-    assert tuple(payload["support"]) == SUPPORT
-    assert tuple(payload["pin42_names"]) == expected_pin42
-    assert payload["pure_y"] and tuple(payload["alpha_beta"]) == (0, 0)
+    require_registry(expected_names, registry_hash, expected_pin42)
+    require(tuple(payload["registry_names"]) == expected_names,
+            "side payload registry names drift")
+    require(tuple(payload["support"]) == SUPPORT,
+            "side payload support drift")
+    require(tuple(payload["pin42_names"]) == expected_pin42,
+            "side payload pin42 drift")
+    require(payload["pure_y"] and tuple(payload["alpha_beta"]) == (0, 0),
+            "side payload scope drift")
     return payload, receipt
```

### `main`

```diff
--- v2:main
+++ v4:main
@@ -7,2 +7,3 @@
     build.add_argument("--preflight-receipt", type=Path, required=True)
+    build.add_argument("--lease", type=Path, required=True)
     build.add_argument("--side", choices=("f", "g"), required=True)
@@ -12,2 +13,3 @@
     pair.add_argument("--preflight-receipt", type=Path, required=True)
+    pair.add_argument("--lease", type=Path, required=True)
     pair.add_argument("--f-receipt", type=Path, required=True)
@@ -18,7 +20,9 @@
     emit.add_argument("--preflight-receipt", type=Path, required=True)
+    emit.add_argument("--lease", type=Path, required=True)
     emit.add_argument("--pair", type=Path, required=True)
     emit.add_argument("--output-dir", type=Path, required=True)
-    final = commands.add_parser("finalize")
+    final = commands.add_parser("finalize-candidate")
     final.add_argument("--manifest", type=Path, required=True)
     final.add_argument("--preflight-receipt", type=Path, required=True)
+    final.add_argument("--lease", type=Path, required=True)
     final.add_argument("--output-dir", type=Path, required=True)
@@ -29,16 +33,17 @@
         print(json.dumps(build_side(args.manifest, args.preflight_receipt,
-                                    args.side, args.output), sort_keys=True))
+                                    args.lease, args.side, args.output),
+                         sort_keys=True))
     elif args.command == "assemble-pair":
         print(json.dumps(assemble_pair(
-            args.manifest, args.preflight_receipt, args.f_receipt,
-            args.g_receipt, args.output), sort_keys=True))
+            args.manifest, args.preflight_receipt, args.lease,
+            args.f_receipt, args.g_receipt, args.output), sort_keys=True))
     elif args.command == "conditional-emit-all":
         print(json.dumps(conditional_emit_all(
-            args.manifest, args.preflight_receipt, args.pair,
+            args.manifest, args.preflight_receipt, args.lease, args.pair,
             args.output_dir), sort_keys=True))
-    elif args.command == "finalize":
-        print(json.dumps(finalize_run(args.manifest,
-                                      args.preflight_receipt,
-                                      args.output_dir), sort_keys=True))
+    elif args.command == "finalize-candidate":
+        print(json.dumps(finalize_candidate(
+            args.manifest, args.preflight_receipt, args.lease,
+            args.output_dir), sort_keys=True))
     else:
-        raise AssertionError(args.command)
+        raise CustodyError("unknown command %r" % (args.command,))
```

### `print_registry`

```diff
--- v2:print_registry
+++ v4:print_registry
@@ -2,2 +2,3 @@
     _orbits, names, registry_hash, pin42 = BASE.reconstruct_registry()
+    require_registry(names, registry_hash, pin42)
     print(json.dumps({
```

### `registered_modular_replay`

```diff
--- v2:registered_modular_replay
+++ v4:registered_modular_replay
@@ -6,3 +6,3 @@
         if sha256_path(path) != manifest["input_sha256"][relative]:
-            raise ValueError("registered certificate hash drift")
+            raise CustodyError("registered certificate hash drift")
         point = json.loads(path.read_text())["point"]
@@ -27,4 +27,4 @@
         if nonzero:
-            raise ValueError("registered modular all-row replay failed at "
-                             "p=%d" % prime)
+            raise CustodyError("registered modular all-row replay failed at "
+                               "p=%d" % prime)
         unit = pow(W1 * W2 % prime, -1, prime)
```

### `template_bridge_modular_gate`

```diff
--- v2:template_bridge_modular_gate
+++ v4:template_bridge_modular_gate
@@ -33,3 +33,3 @@
     if any(values.values()) or not hm or not s1f:
-        raise ValueError("literal E/E5/E6/unit reconstruction gate failed")
+        raise CustodyError("literal E/E5/E6/unit reconstruction gate failed")
     return {"status": "PASS_LITERAL_E5_E6_ONE_UNIT_RECONSTRUCTION",
```

### `template_bridge_spec`

```diff
--- v2:template_bridge_spec
+++ v4:template_bridge_spec
@@ -21,4 +21,6 @@
     e5_2_factor = C * r * (r + one)
-    assert not E5_1
-    assert E5_2 == cp_mul(cp_rc(e5_2_factor), E)
+    require(not E5_1,
+            "literal E5_1 does not vanish after HM reconstruction")
+    require(E5_2 == cp_mul(cp_rc(e5_2_factor), E),
+            "literal E5_2 is not the displayed unit multiple of E")
     s1F = cp_mul(cp_k3(Fraction(2 ** 8, 7 ** 16)), HM)
@@ -26,3 +28,4 @@
                 cp_mul(cp_k3(-(7 ** 48)), cp_pow(s1F, 3)))
-    assert not E6
+    require(not E6,
+            "literal E6 cube row does not vanish after s1F reconstruction")
     return {
```

### `validate_cover`

```diff
--- v2:validate_cover
+++ v4:validate_cover
@@ -5,3 +5,3 @@
             if target in seen:
-                raise ValueError("duplicate target %r" % (target,))
+                raise CustodyError("duplicate target %r" % (target,))
             seen[target] = (shard_index, row)
@@ -10,3 +10,3 @@
     if missing or extra:
-        raise ValueError("184-cover mismatch")
+        raise CustodyError("184-cover mismatch")
     return {target: seen[target][1] for target in TARGETS}
```

### `validate_exact_inventory`

```diff
--- v2:validate_exact_inventory
+++ v4:validate_exact_inventory
@@ -9,7 +9,7 @@
     if len(live) != 29 or len(zero) != 155:
-        raise ValueError("exact live/zero inventory differs from 29/155")
+        raise CustodyError("exact live/zero inventory differs from 29/155")
     if bands != {20: 10, 30: 9, 40: 10}:
-        raise ValueError("exact live-band inventory drift")
+        raise CustodyError("exact live-band inventory drift")
     if max(degrees, default=0) > 2:
-        raise ValueError("exact tail degree exceeds two")
+        raise CustodyError("exact tail degree exceeds two")
     return {"live_rows": len(live), "exact_zero_rows": len(zero),
```

### `validate_preflight_receipt`

```diff
--- v2:validate_preflight_receipt
+++ v4:validate_preflight_receipt
@@ -1,9 +1,15 @@
-def validate_preflight_receipt(path: Path, manifest, manifest_hash):
+def validate_preflight_receipt(path: Path, manifest, manifest_hash,
+                               lease, lease_hash):
     receipt = json.loads(path.read_text())
-    assert receipt["schema"] == PREFLIGHT_SCHEMA
-    assert receipt["pass"] is True
-    assert receipt["manifest_sha256"] == manifest_hash
-    assert receipt["operational_source_list_sha256"] == \
-        manifest["operational_source_list_sha256"]
-    assert receipt["live_identity"] == {
+    require(receipt["schema"] == PREFLIGHT_SCHEMA,
+            "preflight receipt schema drift")
+    require(receipt["pass"] is True, "preflight receipt did not pass")
+    require(receipt["terminal_authority"] is False,
+            "preflight receipt claims terminal authority")
+    require(receipt["manifest_sha256"] == manifest_hash,
+            "preflight receipt manifest hash drift")
+    require(receipt["operational_source_list_sha256"] ==
+            manifest["operational_source_list_sha256"],
+            "preflight receipt source list hash drift")
+    require(receipt["live_identity"] == {
         key: manifest["aws"]["expected_" + key]
@@ -11,15 +17,32 @@
                     "instance_type", "region")
-    }
-    assert receipt["live_tag"] == {
+    }, "preflight live identity drift")
+    require(receipt["live_tag"] == {
         "key": manifest["aws"]["required_tag_key"],
         "value": manifest["aws"]["required_tag_value"],
-    }
-    assert sys.platform.startswith("linux")
-    assert os.uname().nodename == manifest["aws"]["expected_hostname"]
-    assert os.environ.get("AWS_RUN_TAG") == \
-        manifest["aws"]["required_tag_value"]
-    assert os.environ.get("AWS_EXPECTED_HOSTNAME") == \
-        manifest["aws"]["expected_hostname"]
+    }, "preflight live tag drift")
+    require(receipt["run_lease"]["nonce"] == lease["run_nonce"],
+            "preflight receipt lease nonce drift")
+    require(receipt["run_lease"]["lease_sha256"] == lease_hash,
+            "preflight receipt lease digest drift")
+    require(receipt["run_lease"]["lock_held_probe"] is True,
+            "preflight receipt did not observe a held lease")
+    require(sys.platform.startswith("linux"),
+            "compute entry points require Linux")
+    require(os.uname().nodename == manifest["aws"]["expected_hostname"],
+            "hostname drift")
+    require(os.environ.get("AWS_RUN_TAG") ==
+            manifest["aws"]["required_tag_value"],
+            "AWS_RUN_TAG environment drift")
+    require(os.environ.get("JOB_TAG") ==
+            manifest["aws"]["required_tag_value"],
+            "JOB_TAG environment drift")
+    require(os.environ.get("AWS_EXPECTED_HOSTNAME") ==
+            manifest["aws"]["expected_hostname"],
+            "AWS_EXPECTED_HOSTNAME environment drift")
     expected_path = Path(receipt["run_dir"]) / "records" / "PREFLIGHT.json"
-    assert path.resolve() == expected_path.resolve()
+    require(path.resolve() == expected_path.resolve(),
+            "preflight receipt path drift")
+    require(Path(receipt["run_dir"]).resolve() ==
+            Path(lease["job_root"]).resolve(),
+            "preflight run_dir does not match the lease")
     issued = calendar.timegm(time.strptime(
@@ -27,3 +50,4 @@
     age = time.time() - issued
-    assert -300 <= age <= manifest["preflight_receipt_max_age_seconds"]
+    require(-300 <= age <= manifest["preflight_receipt_max_age_seconds"],
+            "preflight receipt age out of bounds")
     return receipt, sha256_path(path)
```

### `verify_operational_sources`

```diff
--- v2:verify_operational_sources
+++ v4:verify_operational_sources
@@ -3,3 +3,3 @@
     if sha256_path(list_path) != manifest["operational_source_list_sha256"]:
-        raise ValueError("operational source-list hash drift")
+        raise CustodyError("operational source-list hash drift")
     inventory = _parse_source_list(list_path)
@@ -7,3 +7,3 @@
     if set(inventory) != required:
-        raise ValueError("operational source inventory path-set drift")
+        raise CustodyError("operational source inventory path-set drift")
     for relative, expected in sorted(inventory.items()):
@@ -11,3 +11,3 @@
         if actual != expected:
-            raise ValueError("operational source drift for %s" % relative)
+            raise CustodyError("operational source drift for %s" % relative)
     return inventory
```

