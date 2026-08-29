#!/usr/bin/env python3
"""Exact support-specialized and checkpoint-sharded D43 source rows.

The primary path rebuilds the pure-y jets with every source coordinate
outside the registered 22-coordinate support pinned literally to zero.  The
checkpoint path can instead consume hash-pinned final cumulative full jets,
but fails closed unless both final hashes are present in the immutable
manifest.  Neither path imposes the deferred E5 equations for W1,W2.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pickle
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
ROOT = CASES.parent
sys.path.insert(0, str(CASES))

import directionb_strike as DIRECTION
import r1_experiment as R1


SCHEMA = "jc2.d43.exact-selected-source-rows.v1"
MANIFEST_SCHEMA = "jc2.d43.exact-selected-source-manifest.v1"
RECEIPT_SCHEMA = "jc2.d43.exact-sparse-checkpoints.v1"
SHARD_SCHEMA = "jc2.d43.exact-source-row-shard.v1"
MERGE_SCHEMA = "jc2.d43.exact-source-row-merge.v1"
D = 43
ABSOLUTE_DEPTH = 32 + D
EXPECTED_REGISTRY_SHA256 = \
    "b3fce1ef76e01c4698b97f7e4cc3562f4da3cd022b301ddde15b1ae086298ce6"

SUPPORT = (
    "tf1_47", "tf1_52", "tf1_57", "tf1_62", "tf1_67", "tf1_72",
    "tf2_47", "tf2_52", "tf2_57", "tf2_62", "tf2_67", "tf2_72",
    "tg1_47", "tg1_52", "tg1_57",
    "tg2_47", "tg2_52", "tg2_57",
    "tg01_52", "tg01_62", "tg02_52", "tg02_62",
)
LOW_SUPPORT = (
    "tf1_47", "tf1_52", "tf2_47", "tf2_52", "tg1_47",
    "tg1_52", "tg2_47", "tg2_52", "tg01_52", "tg02_52",
)
GRAPH_TO_SOURCE = {
    "x4": "tf1_47", "x7": "tf1_52",
    "x12": "tf2_47", "x15": "tf2_52",
    "x20": "tg1_47", "x23": "tg1_52",
    "x28": "tg2_47", "x31": "tg2_52",
    "x36": "tg01_52", "x41": "tg02_52",
}

# This is the source registry underlying eplus43.ROWS_CANON, written without
# importing its NumPy engine: eta 0..27 have starts 8,10,6 by residue class;
# the two appended source rows start at 16 and 36.
S30 = tuple(({0: 8, 1: 10, 2: 6}[eta % 3]
             if eta < 28 else (16 if eta == 28 else 36))
            for eta in range(30))
TARGETS = tuple((eta, slot)
                for eta, start in enumerate(S30)
                for slot in range(start, D, 6))
BANDS = tuple(range(6, D, 2))
BAND_TARGETS = {
    band: tuple(target for target in TARGETS if target[1] == band)
    for band in BANDS
}
assert len(TARGETS) == 184
assert tuple(len(BAND_TARGETS[band]) for band in BANDS) == (
    9, 10, 9, 9, 10, 10, 9, 10, 10, 9,
    10, 10, 9, 10, 10, 10, 10, 10, 10,
)


def canonical_json(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp.%d" % os.getpid())
    with temporary.open("wb") as stream:
        stream.write(json.dumps(value, indent=1, sort_keys=True).encode())
        stream.write(b"\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def atomic_pickle(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp.%d" % os.getpid())
    with temporary.open("wb") as stream:
        pickle.dump(value, stream, protocol=4)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def _fraction_pair(value):
    return [int(value.numerator), int(value.denominator)]


def canonical_ring(element):
    result = []
    for radical_key, coefficient in sorted(element.items()):
        assert len(radical_key) == 8
        result.append([
            list(map(int, radical_key)),
            [_fraction_pair(coefficient[0]),
             _fraction_pair(coefficient[1])],
        ])
    return result


def canonical_vexpr(expression, registry_names):
    result = []
    for monomial, coefficient in expression.items():
        assert tuple(monomial) == tuple(sorted(monomial))
        names = [registry_names[index] for index in monomial]
        result.append([names, canonical_ring(coefficient)])
    return sorted(result, key=lambda item: (item[0], item[1]))


def semantic_vexpr_digest(expression, registry_names) -> str:
    return sha256_bytes(canonical_json(
        canonical_vexpr(expression, registry_names)))


def canonical_rows(rows, registry_names):
    return [[list(target), canonical_vexpr(rows[target], registry_names)]
            for target in sorted(rows)]


def semantic_rows_digest(rows, registry_names) -> str:
    return sha256_bytes(canonical_json(canonical_rows(rows, registry_names)))


def support_sha256() -> str:
    return sha256_bytes(canonical_json(list(SUPPORT)))


def target_registry_sha256() -> str:
    return sha256_bytes(canonical_json([list(target) for target in TARGETS]))


def reconstruct_registry(pins=None):
    DIRECTION.fresh_registry()
    if pins is not None:
        R1.PINS = dict(pins)
    R1.VDEG_CAP = D
    orbits = R1.build_generators(ABSOLUTE_DEPTH)
    names = tuple(variable["name"] for variable in R1.VARS)
    registry_hash = sha256_bytes(repr(list(names)).encode())
    assert registry_hash == EXPECTED_REGISTRY_SHA256, (
        "registry drift", registry_hash, EXPECTED_REGISTRY_SHA256)
    assert set(SUPPORT) <= set(names)
    assert not any(name in ("Xf_alpha", "Xg_beta") for name in names)
    pin42 = tuple(sorted(name for name in names
                         if name.startswith(("tf", "tg"))
                         and name.rsplit("_", 1)[-1] == "74"))
    assert pin42 == (
        "tf1_74", "tf2_74", "tg01_74", "tg02_74", "tg1_74",
        "tg2_74",
    )
    return orbits, names, registry_hash, pin42


def sparse_registry():
    _orbits, dry_names, dry_hash, pin42 = reconstruct_registry()
    pins = {name: R1.RZERO for name in dry_names if name not in SUPPORT}
    orbits, names, registry_hash, pin42_again = reconstruct_registry(pins)
    assert names == dry_names and registry_hash == dry_hash
    assert pin42_again == pin42 and set(pin42) <= set(pins)
    free = tuple(name for name, state in zip(names, R1.VSTAT)
                 if state is None)
    assert free == SUPPORT, (free, SUPPORT)
    expected_B = {12: R1.vC(R1.rmono(B=1))}
    assert orbits["B"]["series"] == expected_B
    assert orbits["GB42"]["series"] == expected_B
    assert orbits["GB21"]["series"] == expected_B
    assert orbits["B"]["size"] == orbits["GB42"]["size"] == 42
    assert orbits["GB21"]["size"] == 21
    used_ids = {
        index
        for orbit in orbits.values()
        for expression in orbit["series"].values()
        for monomial in expression
        for index in monomial
    }
    assert {names[index] for index in used_ids} == set(SUPPORT)
    return orbits, names, registry_hash, pin42


def assert_no_sentinel(jet):
    for target, expression in jet.items():
        for monomial in expression:
            if monomial and monomial[-1] == R1.HIVAR:
                raise ValueError("high-degree sentinel at %r" % (target,))


def specialize_jet(jet, retained_ids):
    retained_ids = set(retained_ids)
    assert_no_sentinel(jet)
    result = {}
    for target, expression in jet.items():
        restricted = {
            monomial: coefficient
            for monomial, coefficient in expression.items()
            if all(index in retained_ids for index in monomial)
        }
        if restricted:
            result[target] = restricted
    assert_no_sentinel(result)
    return result


def _selected_product(left, right, target):
    target_eta, target_slot = target
    result = {}
    for (eta, slot), left_expression in left.items():
        complement = (target_eta - eta, target_slot - slot)
        right_expression = right.get(complement)
        if right_expression is None:
            continue
        product = R1.vmul(left_expression, right_expression)
        if product:
            result = R1.vadd(result, product)
    return result


def selected_source_rows(jf, jg, targets, add_target=True):
    """Compute only requested (eta,slot) components of the source J row."""
    targets = tuple(targets)
    assert len(targets) == len(set(targets))
    assert set(targets) <= set(TARGETS)
    assert_no_sentinel(jf)
    assert_no_sentinel(jg)
    jA = {(eta, slot): R1.vscal(value, R1.K3(slot - 12))
          for (eta, slot), value in jf.items() if slot != 12}
    jBg = {(eta, slot): R1.vscal(value, R1.K3(slot - 18))
           for (eta, slot), value in jg.items() if slot != 18}
    jfH = {(eta - 1, slot): R1.vscal(value, R1.K3(eta))
           for (eta, slot), value in jf.items() if eta}
    jgH = {(eta - 1, slot): R1.vscal(value, R1.K3(eta))
           for (eta, slot), value in jg.items() if eta}
    rows = {}
    for target in targets:
        positive = _selected_product(jA, jgH, target)
        negative = _selected_product(jfH, jBg, target)
        row = R1.vadd(positive, R1.vscal(negative, R1.K3(-1)))
        if add_target and target == (0, 20):
            row = R1.vadd(row, {(): R1.rC(R1.K3(42))})
        rows[target] = row
    assert_no_sentinel(rows)
    return rows


def load_manifest(path: Path):
    raw = path.read_bytes()
    manifest = json.loads(raw)
    assert manifest["schema"] == MANIFEST_SCHEMA
    assert manifest["D"] == D
    assert manifest["absolute_depth"] == ABSOLUTE_DEPTH
    assert manifest["expected_registry_sha256"] == \
        EXPECTED_REGISTRY_SHA256
    assert manifest["support"] == list(SUPPORT)
    assert manifest["support_sha256"] == support_sha256()
    assert manifest["target_registry_sha256"] == target_registry_sha256()
    assert manifest["scope"] == {
        "alpha": 0,
        "beta": 0,
        "e5_W_quartics": "DEFERRED_EXACT_SOURCE_RELATIONS_NOT_IMPOSED",
        "inhomogeneous_row20_plus42": True,
        "pin42": True,
        "pure_y": True,
    }
    assert manifest["shard_plan"] == [
        {"band": band, "id": "band%02d" % band,
         "targets": len(BAND_TARGETS[band])}
        for band in BANDS
    ]
    return manifest, sha256_bytes(raw)


def assert_operational_registration(manifest):
    aws = manifest["aws"]
    required = (aws["expected_hostname"], aws["expected_instance_id"],
                aws["expected_product"], aws["required_run_tag"])
    if (not all(required) or int(aws["expected_nproc"]) <= 0 or
            aws.get("registration_status") != "REGISTERED_IMMUTABLE"):
        raise ValueError("manifest is review-only and has no immutable AWS "
                         "registration")


def verify_source_inputs(manifest):
    verified = {}
    for relative, expected in sorted(manifest["source_sha256"].items()):
        path = ROOT / relative
        actual = sha256_path(path)
        if actual != expected:
            raise ValueError("source hash drift for %s: %s != %s" %
                             (relative, actual, expected))
        verified[relative] = actual
    return verified


def banked_pin_audit(manifest):
    reports = []
    for prime in (105337, 105673):
        relative = "cases/d43_full_certificate_p%d.json" % prime
        path = ROOT / relative
        expected_hash = manifest["source_sha256"][relative]
        assert sha256_path(path) == expected_hash
        point = json.loads(path.read_text())["point"]
        graph = point["graph_156"]
        assert graph["Xf_alpha"] == graph["Xg_beta"] == 0
        nonzero = set()
        for name, value in graph.items():
            if not value or name in ("Xf_alpha", "Xg_beta"):
                continue
            nonzero.add(GRAPH_TO_SOURCE.get(name, name))
        assert nonzero == set(SUPPORT), (prime, sorted(nonzero))
        parked = point["parked_28"]
        assert parked["W1"] and parked["W2"]
        assert all(not value for name, value in parked.items()
                   if name not in ("W1", "W2", "uW1", "uW2"))
        reports.append({
            "prime": prime,
            "certificate_sha256": expected_hash,
            "nonzero_source_support": sorted(nonzero),
            "complement_zero": True,
            "alpha_beta_zero": True,
        })
    return reports


def build_sparse_checkpoints(manifest_path: Path, output_dir: Path):
    manifest, manifest_hash = load_manifest(manifest_path)
    assert_operational_registration(manifest)
    assert manifest["authorization"]["build_sparse_checkpoints"]
    verified_sources = verify_source_inputs(manifest)
    pin_audit = banked_pin_audit(manifest)
    orbits, names, registry_hash, pin42 = sparse_registry()
    jf = R1.gm_jet2(R1.FORB, orbits, D, "D43sparse-f")
    jg = R1.gm_jet2(R1.GORB, orbits, D, "D43sparse-g")
    assert_no_sentinel(jf)
    assert_no_sentinel(jg)
    retained_ids = {index for index, name in enumerate(names)
                    if name in SUPPORT}
    assert jf == specialize_jet(jf, retained_ids)
    assert jg == specialize_jet(jg, retained_ids)

    output_dir.mkdir(parents=True, exist_ok=True)
    checkpoints = {}
    for side, jet in (("f", jf), ("g", jg)):
        path = output_dir / ("d43_sparse_%s.pkl" % side)
        payload = {
            "schema": SCHEMA,
            "kind": "support-specialized-exact-source-jet",
            "side": side,
            "D": D,
            "absolute_depth": ABSOLUTE_DEPTH,
            "registry_sha256": registry_hash,
            "registry_names": names,
            "support": SUPPORT,
            "support_sha256": support_sha256(),
            "pin42_names": pin42,
            "pure_y": True,
            "alpha_beta": (0, 0),
            "jet": jet,
            "jet_semantic_sha256": semantic_rows_digest(jet, names),
        }
        atomic_pickle(path, payload)
        checkpoints[side] = {
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "semantic_sha256": payload["jet_semantic_sha256"],
        }
    receipt = {
        "schema": RECEIPT_SCHEMA,
        "status": "EXACT_SPARSE_CHECKPOINTS_COMPLETE",
        "manifest_sha256": manifest_hash,
        "registry_sha256": registry_hash,
        "support_sha256": support_sha256(),
        "target_registry_sha256": target_registry_sha256(),
        "source_sha256": verified_sources,
        "banked_pin_audit": pin_audit,
        "pin42_names": list(pin42),
        "scope": manifest["scope"],
        "checkpoints": checkpoints,
    }
    atomic_json(output_dir / "SPARSE_CHECKPOINTS.json", receipt)
    return receipt


def _load_pickle_after_hash(path: Path, expected_hash: str):
    if not expected_hash or len(expected_hash) != 64:
        raise ValueError("missing explicit checkpoint SHA-256 for %s" % path)
    actual = sha256_path(path)
    if actual != expected_hash:
        raise ValueError("checkpoint hash drift for %s: %s != %s" %
                         (path, actual, expected_hash))
    with path.open("rb") as stream:
        return pickle.load(stream), actual


def load_sparse_checkpoint_pair(receipt_path: Path, manifest_hash: str):
    receipt = json.loads(receipt_path.read_text())
    assert receipt["schema"] == RECEIPT_SCHEMA
    assert receipt["manifest_sha256"] == manifest_hash
    assert receipt["registry_sha256"] == EXPECTED_REGISTRY_SHA256
    assert receipt["support_sha256"] == support_sha256()
    assert receipt["target_registry_sha256"] == target_registry_sha256()
    _orbits, expected_names, registry_hash, _pin42 = reconstruct_registry()
    del _orbits
    assert registry_hash == receipt["registry_sha256"]
    result = []
    for side in ("f", "g"):
        item = receipt["checkpoints"][side]
        path = receipt_path.parent / item["path"]
        payload, _actual = _load_pickle_after_hash(path, item["sha256"])
        assert payload["schema"] == SCHEMA
        assert payload["side"] == side
        assert payload["registry_sha256"] == EXPECTED_REGISTRY_SHA256
        assert tuple(payload["registry_names"]) == expected_names
        assert tuple(payload["support"]) == SUPPORT
        assert payload["support_sha256"] == support_sha256()
        assert payload["pure_y"] and tuple(payload["alpha_beta"]) == (0, 0)
        assert payload["jet_semantic_sha256"] == \
            semantic_rows_digest(payload["jet"], payload["registry_names"])
        assert payload["jet_semantic_sha256"] == item["semantic_sha256"]
        assert_no_sentinel(payload["jet"])
        result.append((payload["jet"], tuple(payload["registry_names"])))
    assert result[0][1] == result[1][1]
    return result[0][0], result[1][0], result[0][1], receipt


def input_custody_sha256(input_kind, input_receipt):
    return sha256_bytes(canonical_json({
        "input_kind": input_kind,
        "input_receipt": input_receipt,
    }))


def load_full_checkpoint_pair(manifest, checkpoint_root: Path):
    """Inert until the immutable manifest contains both final hashes."""
    specs = manifest["full_checkpoint_inputs"]
    if specs["status"] != "READY_FINAL_F_AND_G":
        raise ValueError("full checkpoint lane is preregistered but inert: "
                         + specs["status"])
    if specs["producer_consumer_code_status"] != \
            "READY_PINNED_PRODUCER_CODE_COMPATIBILITY_VERIFIED":
        raise ValueError("full checkpoint producer/consumer code is not "
                         "compatibility-certified")
    orbits, names, registry_hash, _pin42 = reconstruct_registry()
    del orbits
    retained_ids = {index for index, name in enumerate(names)
                    if name in SUPPORT}
    jets = []
    for side, expected_orbit in (("f", "B"), ("g", "GB21")):
        spec = specs[side]
        path = checkpoint_root / spec["basename"]
        payload, _actual = _load_pickle_after_hash(path, spec["sha256"])
        assert payload["reg_hash"] == registry_hash
        assert payload["orbit"] == expected_orbit
        jet = specialize_jet(payload["jp"], retained_ids)
        jets.append(jet)
    return jets[0], jets[1], names, {
        "schema": "full-checkpoint-inputs",
        "inputs": specs,
    }


def expected_d21_band20(manifest, registry_names):
    relative = "directionb_tails_D21.pkl"
    path = ROOT / relative
    payload, _actual = _load_pickle_after_hash(
        path, manifest["source_sha256"][relative])
    assert payload["D"] == 21
    name_to_id = {name: index for index, name in enumerate(registry_names)}
    rows = {}
    for eta in [target[0] for target in BAND_TARGETS[20]]:
        expression = payload["byk"][20][eta]
        row = {}
        for monomial, coefficient in expression.items():
            source_names = tuple(payload["vars"][index]
                                 for index in monomial)
            if all(name in LOW_SUPPORT for name in source_names):
                mapped = tuple(sorted(name_to_id[name]
                                      for name in source_names))
                row[mapped] = coefficient
        if eta == 0:
            row = R1.vadd(row, {(): R1.rC(R1.K3(42))})
        rows[(eta, 20)] = row
    return rows


def d21_band20_regression(rows, manifest, registry_names):
    assert set(rows) == set(BAND_TARGETS[20])
    expected = expected_d21_band20(manifest, registry_names)
    actual_digests = {
        str(eta): semantic_vexpr_digest(rows[(eta, 20)], registry_names)
        for eta, _slot in BAND_TARGETS[20]
    }
    expected_digests = {
        str(eta): semantic_vexpr_digest(expected[(eta, 20)], registry_names)
        for eta, _slot in BAND_TARGETS[20]
    }
    if actual_digests != expected_digests:
        raise ValueError("D21 exact band-20 regression failed")
    assert semantic_rows_digest(rows, registry_names) == \
        semantic_rows_digest(expected, registry_names)
    return {
        "status": "PASS_EXACT_D21_BAND20_EQUALITY",
        "row_digests": actual_digests,
        "band_semantic_sha256": semantic_rows_digest(rows, registry_names),
    }


def shard_targets(bands):
    bands = tuple(sorted(set(map(int, bands))))
    if not bands or not set(bands) <= set(BANDS):
        raise ValueError("invalid band set %r" % (bands,))
    return tuple(target for target in TARGETS if target[1] in bands)


def emit_shard(manifest_path: Path, output_path: Path, bands,
               sparse_receipt: Path | None = None,
               full_checkpoint_root: Path | None = None):
    manifest, manifest_hash = load_manifest(manifest_path)
    verify_source_inputs(manifest)
    bands = tuple(sorted(set(map(int, bands))))
    if bands != (20,) and not manifest["authorization"]["fanout_after_pilot"]:
        raise ValueError("fanout is not authorized by this immutable manifest")
    assert_operational_registration(manifest)
    if sparse_receipt is not None and full_checkpoint_root is not None:
        raise ValueError("choose exactly one checkpoint source")
    if sparse_receipt is not None:
        jf, jg, names, input_receipt = load_sparse_checkpoint_pair(
            sparse_receipt, manifest_hash)
        input_kind = "support-specialized-source-checkpoints"
    elif full_checkpoint_root is not None:
        jf, jg, names, input_receipt = load_full_checkpoint_pair(
            manifest, full_checkpoint_root)
        input_kind = "hash-pinned-final-full-checkpoints"
    else:
        raise ValueError("one checkpoint source is required")
    input_custody = input_custody_sha256(input_kind, input_receipt)
    targets = shard_targets(bands)
    rows = selected_source_rows(jf, jg, targets, add_target=True)
    used_names = {names[index]
                  for row in rows.values() for monomial in row
                  for index in monomial}
    assert used_names <= set(SUPPORT)
    assert not used_names.intersection({"tf1_74", "tf2_74", "tg1_74",
                                        "tg2_74", "tg01_74", "tg02_74"})
    regression = None
    if bands == (20,):
        regression = d21_band20_regression(rows, manifest, names)
    payload = {
        "schema": SHARD_SCHEMA,
        "status": "EXACT_SOURCE_ROW_SHARD_COMPLETE",
        "manifest_sha256": manifest_hash,
        "input_kind": input_kind,
        "input_receipt": input_receipt,
        "input_custody_sha256": input_custody,
        "D": D,
        "registry_sha256": EXPECTED_REGISTRY_SHA256,
        "registry_names": names,
        "support": SUPPORT,
        "support_sha256": support_sha256(),
        "target_registry_sha256": target_registry_sha256(),
        "bands": bands,
        "targets": targets,
        "rows": rows,
        "row_semantic_sha256": {
            "%d,%d" % target:
                semantic_vexpr_digest(rows[target], names)
            for target in sorted(rows)
        },
        "shard_semantic_sha256": semantic_rows_digest(rows, names),
        "d21_band20_regression": regression,
        "scope": manifest["scope"],
        "claim_boundary": manifest["claim_boundary"],
    }
    atomic_pickle(output_path, payload)
    receipt = {
        "schema": SHARD_SCHEMA + ".receipt",
        "status": payload["status"],
        "manifest_sha256": manifest_hash,
        "payload": output_path.name,
        "payload_bytes": output_path.stat().st_size,
        "payload_sha256": sha256_path(output_path),
        "bands": list(bands),
        "targets": [list(target) for target in targets],
        "shard_semantic_sha256": payload["shard_semantic_sha256"],
        "input_custody_sha256": input_custody,
        "d21_band20_regression": regression,
    }
    atomic_json(output_path.with_suffix(output_path.suffix + ".receipt.json"),
                receipt)
    return receipt


def load_shard_receipt(receipt_path: Path, manifest_hash: str):
    receipt = json.loads(receipt_path.read_text())
    assert receipt["schema"] == SHARD_SCHEMA + ".receipt"
    assert receipt["manifest_sha256"] == manifest_hash
    payload_path = receipt_path.parent / receipt["payload"]
    payload, _actual = _load_pickle_after_hash(
        payload_path, receipt["payload_sha256"])
    assert payload["schema"] == SHARD_SCHEMA
    assert payload["manifest_sha256"] == manifest_hash
    assert payload["input_custody_sha256"] == input_custody_sha256(
        payload["input_kind"], payload["input_receipt"])
    assert receipt["input_custody_sha256"] == \
        payload["input_custody_sha256"]
    assert payload["shard_semantic_sha256"] == \
        semantic_rows_digest(payload["rows"], payload["registry_names"])
    assert payload["shard_semantic_sha256"] == \
        receipt["shard_semantic_sha256"]
    expected_row_digests = {
        "%d,%d" % target:
            semantic_vexpr_digest(payload["rows"][target],
                                  payload["registry_names"])
        for target in sorted(payload["rows"])
    }
    assert payload["row_semantic_sha256"] == expected_row_digests
    return payload


def validate_common_custody(shards):
    custody = {shard["input_custody_sha256"] for shard in shards}
    if len(custody) != 1:
        raise ValueError("shards do not share identical input custody")
    return next(iter(custody))


def validate_cover(shards, expected_targets=TARGETS):
    expected_targets = set(expected_targets)
    seen = {}
    for shard_index, shard in enumerate(shards):
        for target, row in shard["rows"].items():
            if target in seen:
                raise ValueError("duplicate target %r in shards %d and %d" %
                                 (target, seen[target][0], shard_index))
            seen[target] = (shard_index, row)
    missing = expected_targets - set(seen)
    extra = set(seen) - expected_targets
    if missing or extra:
        raise ValueError("target cover mismatch: missing=%r extra=%r" %
                         (sorted(missing), sorted(extra)))
    return {target: seen[target][1] for target in sorted(seen)}


def merge_shards(manifest_path: Path, receipt_paths, output_path: Path):
    manifest, manifest_hash = load_manifest(manifest_path)
    if not manifest["authorization"]["fanout_after_pilot"]:
        raise ValueError("184-row merge requires a post-pilot manifest")
    assert_operational_registration(manifest)
    shards = [load_shard_receipt(Path(path), manifest_hash)
              for path in receipt_paths]
    assert len(shards) == 19
    assert all(shard["registry_sha256"] == EXPECTED_REGISTRY_SHA256
               for shard in shards)
    assert all(tuple(shard["registry_names"])
               == tuple(shards[0]["registry_names"]) for shard in shards)
    input_custody = validate_common_custody(shards)
    rows = validate_cover(shards)
    names = tuple(shards[0]["registry_names"])
    payload = {
        "schema": MERGE_SCHEMA,
        "status": "EXACT_184_SOURCE_ROWS_MERGED",
        "manifest_sha256": manifest_hash,
        "registry_sha256": EXPECTED_REGISTRY_SHA256,
        "registry_names": names,
        "support": SUPPORT,
        "support_sha256": support_sha256(),
        "target_registry_sha256": target_registry_sha256(),
        "targets": TARGETS,
        "rows": rows,
        "semantic_sha256": semantic_rows_digest(rows, names),
        "source_shard_semantic_sha256": [
            shard["shard_semantic_sha256"] for shard in shards],
        "input_custody_sha256": input_custody,
        "scope": manifest["scope"],
        "claim_boundary": manifest["claim_boundary"],
    }
    atomic_pickle(output_path, payload)
    receipt = {
        "schema": MERGE_SCHEMA + ".receipt",
        "status": payload["status"],
        "manifest_sha256": manifest_hash,
        "payload": output_path.name,
        "payload_bytes": output_path.stat().st_size,
        "payload_sha256": sha256_path(output_path),
        "semantic_sha256": payload["semantic_sha256"],
        "targets": len(rows),
    }
    atomic_json(output_path.with_suffix(output_path.suffix + ".receipt.json"),
                receipt)
    return receipt


def print_registry():
    _orbits, names, registry_hash, pin42 = reconstruct_registry()
    report = {
        "schema": SCHEMA,
        "registry_variables": len(names),
        "registry_sha256": registry_hash,
        "support": list(SUPPORT),
        "support_sha256": support_sha256(),
        "pin42_names": list(pin42),
        "targets": len(TARGETS),
        "target_registry_sha256": target_registry_sha256(),
        "band_counts": {str(band): len(BAND_TARGETS[band])
                        for band in BANDS},
    }
    print(json.dumps(report, indent=1, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("registry")

    build = subparsers.add_parser("build-sparse")
    build.add_argument("--manifest", type=Path, required=True)
    build.add_argument("--output-dir", type=Path, required=True)

    emit = subparsers.add_parser("emit-shard")
    emit.add_argument("--manifest", type=Path, required=True)
    emit.add_argument("--output", type=Path, required=True)
    emit.add_argument("--bands", type=int, nargs="+", required=True)
    source = emit.add_mutually_exclusive_group(required=True)
    source.add_argument("--sparse-receipt", type=Path)
    source.add_argument("--full-checkpoint-root", type=Path)

    merge = subparsers.add_parser("merge")
    merge.add_argument("--manifest", type=Path, required=True)
    merge.add_argument("--output", type=Path, required=True)
    merge.add_argument("--receipts", type=Path, nargs="+", required=True)

    args = parser.parse_args()
    if args.command == "registry":
        print_registry()
    elif args.command == "build-sparse":
        receipt = build_sparse_checkpoints(args.manifest, args.output_dir)
        print(json.dumps(receipt, sort_keys=True))
    elif args.command == "emit-shard":
        receipt = emit_shard(
            args.manifest, args.output, args.bands,
            sparse_receipt=args.sparse_receipt,
            full_checkpoint_root=args.full_checkpoint_root)
        print(json.dumps(receipt, sort_keys=True))
    elif args.command == "merge":
        receipt = merge_shards(
            args.manifest, args.receipts, args.output)
        print(json.dumps(receipt, sort_keys=True))
    else:
        raise AssertionError(args.command)


if __name__ == "__main__":
    main()
