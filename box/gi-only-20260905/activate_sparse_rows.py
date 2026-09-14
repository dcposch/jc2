#!/usr/bin/env python3
"""Verify and atomically activate sparse-extracted G-only coefficient rows.

This is the production boundary for ``experiments/fast-extract``.  It refuses
to install a row file until all of the following pass:

* charged builder_fix hash and the canonical builder's y-first polynomial
  ring/orientation/complete G-coordinate inventory;
* candidate receipt, source-builder hash, row hash, row count, and syntax;
* two full exact-Z specializations of the emitted h-adic rows, independently
  recomposed and compared with the literal ``J(P,Q)-c*x^ell``;
* a negative perturbation and a reversed-orientation negative control;
* literal expanded-row dictionary equality for every completed native control
  class (70, 109, and 127 unknowns).

Only missing or header-only canonical row paths may be replaced.  Activation
is atomic and records a custody receipt plus a metadata pointer consumed by
the existing solve driver through its meta-prebuild custody.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EXPERIMENT = HERE / "experiments" / "fast-extract"
SPARSE_ROOT = EXPERIMENT / "sparse-hadic"
SPARSE_SCRIPT = EXPERIMENT / "sparse_hadic_extract.py"
FROZEN_BUILDER_FIX = Path("/tmp/jc2-lane.ymMTCq/inputs/builder_fix.py")
BUILDER_FIX_SHA256 = "d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b"
CUSTODY = HERE / "sparse-extraction-custody.json"
CONTROL_CLASSES = (
    "C_n24m16_Mm12_m2_5_ell1_s4",
    "C_n18m12_M2_9_ell2_s3",
    "C_n24m18_Mm15_14_ell1_s3",
)
HEADER = "source_index|h_power|x_power|y_power|expr"

# Numeric bivariate polynomial: (x degree,y degree) -> exact integer.
NBP = dict[tuple[int, int], int]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT))
    except ValueError:
        # Charged frozen inputs intentionally live in the lane's /tmp capsule.
        return str(resolved)


def artifact(path: Path) -> dict[str, Any]:
    return {"path": rel(path), "bytes": path.stat().st_size, "sha256": sha256(path)}


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(value, fh, indent=2, sort_keys=True)
            fh.write("\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def load_sparse_module():
    spec = importlib.util.spec_from_file_location("gi_sparse_hadic_exact", SPARSE_SCRIPT)
    if spec is None or spec.loader is None:
        raise ImportError(SPARSE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def nbp_addto(dst: NBP, src: NBP, scale: int = 1) -> None:
    for coord, coefficient in src.items():
        value = dst.get(coord, 0) + scale * coefficient
        if value:
            dst[coord] = value
        else:
            dst.pop(coord, None)


def nbp_mul(left: NBP, right: NBP) -> NBP:
    out: NBP = {}
    for (lx, ly), lc in left.items():
        for (rx, ry), rc in right.items():
            coord = (lx + rx, ly + ry)
            value = out.get(coord, 0) + lc * rc
            if value:
                out[coord] = value
            else:
                out.pop(coord, None)
    return out


def nbp_derivative(poly: NBP, axis: int) -> NBP:
    out: NBP = {}
    for (xpow, ypow), coefficient in poly.items():
        exponent = xpow if axis == 0 else ypow
        if exponent:
            coord = (xpow - 1, ypow) if axis == 0 else (xpow, ypow - 1)
            out[coord] = coefficient * exponent
    return out


def nbp_jac(left: NBP, right: NBP) -> NBP:
    out = nbp_mul(nbp_derivative(left, 0), nbp_derivative(right, 1))
    nbp_addto(out, nbp_mul(nbp_derivative(left, 1), nbp_derivative(right, 0)), -1)
    return out


def evaluate_bp(poly, values: list[int]) -> NBP:
    out: NBP = {}
    for coord, parameter_poly in poly.items():
        total = 0
        for monomial, coefficient in parameter_poly.items():
            term = coefficient
            for number in monomial:
                term *= values[number]
            total += term
        if total:
            out[coord] = total
    return out


def eval_row_expression(
    expression: str,
    variable_number: dict[str, int],
    points: list[list[int]],
) -> tuple[list[int], list[tuple[int, tuple[tuple[str, int], ...]]]]:
    """Evaluate one expanded row and return detailed occurrences of c."""
    totals = [0 for _ in points]
    c_terms: list[tuple[int, tuple[tuple[str, int], ...]]] = []
    for piece in re.findall(r"[+-]?[^+-]+", expression.strip()):
        sign = -1 if piece.startswith("-") else 1
        body = piece[1:] if piece[:1] in "+-" else piece
        coefficient = sign
        factors: list[tuple[str, int]] = []
        for raw in body.split("*"):
            if re.fullmatch(r"\d+", raw):
                coefficient *= int(raw)
                continue
            match = re.fullmatch(r"([A-Za-z_][A-Za-z_0-9]*)(?:\^(\d+))?", raw)
            if not match or match.group(1) not in variable_number:
                raise ValueError(f"unlicensed row factor {raw!r}")
            factors.append((match.group(1), int(match.group(2) or 1)))
        if any(name == "c" for name, _ in factors):
            c_terms.append((coefficient, tuple(factors)))
        for index, point in enumerate(points):
            value = coefficient
            for name, power in factors:
                value *= point[variable_number[name]] ** power
            totals[index] += value
    return totals, c_terms


def literal_numeric_target(E, base: dict, values: list[int], e: int, q: int, ell: int) -> tuple[NBP, NBP]:
    numeric = {name: evaluate_bp(poly, values) for name, poly in base.items()}
    h = numeric["h"]
    powers: list[NBP] = [{(0, 0): 1}]
    for _ in range(max(e, q)):
        powers.append(nbp_mul(powers[-1], h))
    P = dict(powers[e])
    for i in range(1, e + 1):
        nbp_addto(P, nbp_mul(numeric[f"AA{i}"], powers[e - i]))
    Q = dict(powers[q])
    for i in range(2, q + 1):
        nbp_addto(Q, nbp_mul(numeric[f"BB{i}"], powers[q - i]))
    literal = nbp_jac(P, Q)
    nbp_addto(literal, {(ell, 0): values[-1]}, -1)
    reversed_target = nbp_jac(Q, P)
    nbp_addto(reversed_target, {(ell, 0): values[-1]}, -1)
    return literal, reversed_target


def exact_native_controls(E) -> list[dict[str, Any]]:
    controls = []
    for class_id in CONTROL_CLASSES:
        class_dir = HERE / "classes" / class_id
        cls = json.loads((class_dir / "class.json").read_text(encoding="utf-8"))
        stem = cls["canonical_stem"]
        builder = class_dir / "builders" / f"{stem}_builder.sing"
        text = builder.read_text(encoding="utf-8")
        ring = re.search(r"^ring R=0,\((.*?)\),\(lp\(1\),dp\(\d+\)\);$", text, re.M)
        if not ring:
            raise AssertionError(f"bad fixed ring in {builder}")
        names = ring.group(1).split(",")[2:]
        numbers = {name: i for i, name in enumerate(names)}
        native = class_dir / "rows" / f"{stem}_rows.tsv"
        sparse = SPARSE_ROOT / class_id / f"{stem}_sparse_rows.tsv"
        if not native.is_file() or not sparse.is_file():
            raise FileNotFoundError(f"missing native-control rows for {class_id}")
        left = E.read_native_rows(native, numbers)
        right = E.read_native_rows(sparse, numbers)
        if left != right:
            raise AssertionError(f"literal sparse/native row mismatch for {class_id}")
        controls.append({
            "class_id": class_id,
            "unknowns_without_T": len(names),
            "rows": len(left),
            "literal_expanded_row_dictionary_equality": True,
            "native": artifact(native),
            "sparse": artifact(sparse),
            "status": "PASS",
        })
    return controls


def verify_candidate(E, class_id: str) -> dict[str, Any]:
    class_dir = HERE / "classes" / class_id
    cls_path = class_dir / "class.json"
    cls = json.loads(cls_path.read_text(encoding="utf-8"))
    stem = cls["canonical_stem"]
    builder = class_dir / "builders" / f"{stem}_builder.sing"
    builder_text = builder.read_text(encoding="utf-8")
    receipt_path = SPARSE_ROOT / class_id / f"{stem}_sparse_extraction.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    rows = ROOT / receipt["rows"]

    if receipt.get("status") != "PASS" or receipt.get("class_id") != class_id or receipt.get("stem") != stem:
        raise AssertionError(f"bad candidate receipt identity for {class_id}")
    if receipt.get("source_fixed_builder_sha256") != sha256(builder):
        raise AssertionError(f"source builder changed after extraction for {class_id}")
    if receipt.get("rows_sha256") != sha256(rows) or receipt.get("rows_bytes") != rows.stat().st_size:
        raise AssertionError(f"candidate row artifact mismatch for {class_id}")
    if receipt.get("unknowns_without_T") != cls["unknowns_without_T"]:
        raise AssertionError(f"candidate unknown count mismatch for {class_id}")
    if receipt.get("exactness", {}).get("coordinate_specializations") != 0:
        raise AssertionError(f"candidate specialized coordinates for {class_id}")
    if receipt.get("exactness", {}).get("auxiliary_variables") != 0:
        raise AssertionError(f"candidate introduced auxiliaries for {class_id}")

    ring_match = re.search(r"^ring R=0,\((.*?)\),\(lp\(1\),dp\((\d+)\)\);$", builder_text, re.M)
    if not ring_match or not builder_text.startswith("// G_i-ONLY chart"):
        raise AssertionError(f"builder is not canonical G-only builder_fix output: {builder}")
    ring_variables = ring_match.group(1).split(",")
    if ring_variables[:2] != ["y", "x"] or ring_variables[-1] != "c":
        raise AssertionError(f"bad y-first ring blocks for {class_id}")
    names = ring_variables[2:]
    numbers = {name: i for i, name in enumerate(names)}
    if len(names) != cls["unknowns_without_T"] or len(names) != len(set(names)):
        raise AssertionError(f"incomplete/nonunique G coordinate ring for {class_id}")
    if "literal coefficient ideal: J(P,Q)" not in builder_text or "BB1" in builder_text:
        raise AssertionError(f"orientation/beta_1 gate failed for {class_id}")

    setup = dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*);$", builder_text, re.M))
    base = {name: E.parse_base_polynomial(expr, numbers) for name, expr in setup.items()}
    e, q, ell = int(cls["e"]), int(cls["q"]), int(cls["ell"])
    seeds = (11, 29)
    points: list[list[int]] = []
    for seed in seeds:
        point = [((index + 3) * (seed + 5) + 2 * index * index) % 11 - 5 for index in range(len(names))]
        point[numbers["c"]] = 2 + seed % 5
        points.append(point)
    h_numeric = [evaluate_bp(base["h"], point) for point in points]
    h_powers: list[list[NBP]] = [[{(0, 0): 1}] for _ in points]
    recomposed: list[NBP] = [{} for _ in points]
    seen: set[tuple[int, int, int]] = set()
    c_occurrences: list[dict[str, Any]] = []
    row_count = 0
    with rows.open(encoding="utf-8") as fh:
        if fh.readline().rstrip("\n") != HEADER:
            raise AssertionError(f"bad candidate row header for {class_id}")
        for line_number, line in enumerate(fh, 2):
            if not line.strip():
                continue
            fields = line.rstrip("\n").split("|", 4)
            if len(fields) != 5 or int(fields[0]) != row_count:
                raise AssertionError(f"bad source index at {rows}:{line_number}")
            hpow, xpow, ypow = map(int, fields[1:4])
            key = (hpow, xpow, ypow)
            if min(key) < 0 or key in seen:
                raise AssertionError(f"bad/duplicate row coordinate {key} for {class_id}")
            seen.add(key)
            evaluations, c_terms = eval_row_expression(fields[4], numbers, points)
            for coefficient, factors in c_terms:
                c_occurrences.append({"row": key, "coefficient": coefficient, "factors": factors})
            for index, value in enumerate(evaluations):
                while len(h_powers[index]) <= hpow:
                    h_powers[index].append(nbp_mul(h_powers[index][-1], h_numeric[index]))
                if value:
                    nbp_addto(recomposed[index], {
                        coord: value * coefficient
                        for coord, coefficient in h_powers[index][hpow].items()
                        for coord in [(coord[0] + xpow, coord[1] + ypow)]
                    })
            row_count += 1
    if row_count != receipt["coefficient_generators"]:
        raise AssertionError(f"candidate row count mismatch for {class_id}")
    expected_c = [{"row": (0, ell, 0), "coefficient": -1, "factors": (("c", 1),)}]
    if c_occurrences != expected_c:
        raise AssertionError(f"target c occurrence mismatch for {class_id}: {c_occurrences[:3]}")

    controls = []
    for index, (seed, point) in enumerate(zip(seeds, points)):
        literal, reversed_target = literal_numeric_target(E, base, point, e, q, ell)
        equality = recomposed[index] == literal
        reversed_negative = recomposed[index] != reversed_target
        perturbed = dict(recomposed[index])
        perturbed[(0, 0)] = perturbed.get((0, 0), 0) + 1
        negative = perturbed != literal
        inverse = Fraction(1, point[numbers["c"]])
        inverse_zero = inverse * point[numbers["c"]] - 1 == 0
        if not (equality and reversed_negative and negative and inverse_zero):
            raise AssertionError(f"numeric control failed for {class_id}, seed {seed}")
        controls.append({
            "seed": seed,
            "coefficient_assignment": "deterministic exact integers",
            "c": point[numbers["c"]],
            "literal_J_PQ_minus_cxell_equality": equality,
            "reversed_J_QP_minus_cxell_negative": reversed_negative,
            "plus_one_negative": negative,
            "Tc_minus_1_at_T_equals_1_over_c": inverse_zero,
            "recomposed_xy_terms": len(recomposed[index]),
            "status": "PASS",
        })
    return {
        "class_id": class_id,
        "stem": stem,
        "status": "PASS",
        "candidate_receipt": artifact(receipt_path),
        "candidate_rows": artifact(rows),
        "canonical_builder": artifact(builder),
        "ring": ring_match.group(0),
        "unknowns_without_T": len(names),
        "coefficient_generators": row_count,
        "generators_including_Tc_minus_1": row_count + 1,
        "c_target_occurrence": c_occurrences,
        "exact_numeric_controls": controls,
        "all_G_coordinates_retained": True,
        "coordinate_specializations": 0,
        "auxiliary_variables": 0,
        "literal_orientation": "J(P,Q)-c*x^ell",
        "inverse_generator": "T*c-1",
    }


def verify_candidate_fresh(class_id: str) -> dict[str, Any]:
    """Process-pool entry point; each verifier gets an isolated module state."""
    return verify_candidate(load_sparse_module(), class_id)


def install_rows(verification: dict[str, Any]) -> dict[str, Any]:
    class_id, stem = verification["class_id"], verification["stem"]
    source = ROOT / verification["candidate_rows"]["path"]
    destination = HERE / "classes" / class_id / "rows" / f"{stem}_rows.tsv"
    destination.parent.mkdir(parents=True, exist_ok=True)
    previous = None
    if destination.exists():
        previous = artifact(destination)
        if destination.stat().st_size > len(HEADER) + 1:
            if sha256(destination) != sha256(source):
                raise RuntimeError(f"refusing to overwrite non-header canonical rows: {destination}")
            return {"action": "ALREADY_IDENTICAL", "previous": previous, "canonical_rows": artifact(destination)}
    temporary = destination.with_name("." + destination.name + f".activate.{os.getpid()}")
    try:
        with source.open("rb") as incoming, temporary.open("wb") as outgoing:
            shutil.copyfileobj(incoming, outgoing, length=8 << 20)
            outgoing.flush()
            os.fsync(outgoing.fileno())
        if sha256(temporary) != verification["candidate_rows"]["sha256"]:
            raise AssertionError(f"activation-copy hash mismatch for {class_id}")
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    return {"action": "ATOMIC_INSTALL", "previous": previous, "canonical_rows": artifact(destination)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--class-id", action="append", required=True)
    args = parser.parse_args()
    if sha256(FROZEN_BUILDER_FIX) != BUILDER_FIX_SHA256:
        raise SystemExit("charged builder_fix SHA-256 mismatch")
    E = load_sparse_module()
    native_controls = exact_native_controls(E)
    # Large rows are independent and verification is CPU-heavy.  Bound this
    # to the requested class count (three in the recovery run), and retain the
    # original command-line order in the returned list.
    with concurrent.futures.ProcessPoolExecutor(max_workers=min(3, len(args.class_id))) as pool:
        verifications = list(pool.map(verify_candidate_fresh, args.class_id))
    installations = [install_rows(item) for item in verifications]
    sparse_script = artifact(SPARSE_SCRIPT)
    receipt: dict[str, Any] = {
        "schema": "moh-gi-only-sparse-extraction-activation-custody-v1",
        "status": "PASS",
        "activated_utc": utc_now(),
        "scope": "exact full G_i production coefficient rows; no chart specialization",
        "sparse_extractor": sparse_script,
        "frozen_builder_fix": artifact(FROZEN_BUILDER_FIX),
        "native_exact_controls": native_controls,
        "all_native_exact_controls_passed": True,
        "classes": [dict(verification, activation=installation) for verification, installation in zip(verifications, installations)],
    }
    atomic_json(CUSTODY, receipt)
    custody_artifact = artifact(CUSTODY)

    # Make the custody discoverable by the existing solver.  solve_class.py
    # hashes meta_prebuild in solve-result.json, so this field is transitively
    # in every subsequent result without changing solver mathematics.
    for verification, installation in zip(verifications, installations):
        class_id, stem = verification["class_id"], verification["stem"]
        pointer = {
            "method": "exact_sparse_monic_y_division",
            "status": "PASS",
            "custody_receipt": custody_artifact,
            "sparse_extractor": sparse_script,
            "canonical_rows": installation["canonical_rows"],
            "canonical_builder_sha256": verification["canonical_builder"]["sha256"],
            "literal_J_PQ_controls_passed": True,
            "native_literal_row_controls_passed": True,
            "no_coordinate_specialization": True,
            "no_auxiliary_variables": True,
        }
        meta_path = HERE / "classes" / class_id / "meta" / f"{stem}.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["coefficient_rows_extraction_custody"] = pointer
        meta["jacobian_coefficient_generator_count"] = verification["coefficient_generators"]
        meta["generator_count_including_inverse"] = verification["generators_including_Tc_minus_1"]
        atomic_json(meta_path, meta)
        class_path = HERE / "classes" / class_id / "class.json"
        cls = json.loads(class_path.read_text(encoding="utf-8"))
        cls["coefficient_rows_extraction_custody"] = pointer
        cls["jacobian_coefficient_generator_count"] = verification["coefficient_generators"]
        cls["generator_count_including_inverse"] = verification["generators_including_Tc_minus_1"]
        atomic_json(class_path, cls)

    manifest_path = HERE / "classes_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    by_class = {item["class_id"]: item for item in verifications}
    for item in manifest:
        verification = by_class.get(item["class_id"])
        if verification:
            item["coefficient_rows_extraction_custody"] = rel(CUSTODY)
            item["jacobian_coefficient_generator_count"] = verification["coefficient_generators"]
            item["generator_count_including_inverse"] = verification["generators_including_Tc_minus_1"]
    atomic_json(manifest_path, manifest)
    print(json.dumps({
        "status": "PASS",
        "custody": custody_artifact,
        "activated": [{
            "class_id": item["class_id"],
            "rows": installation["canonical_rows"],
            "coefficient_generators": item["coefficient_generators"],
        } for item, installation in zip(verifications, installations)],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
