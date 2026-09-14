#!/usr/bin/env python3
"""Independent verifier for the S5/S6 source-complete recertification lane.

This script deliberately does not import ``s56_emitter``.  It recomputes the
support formula, parses emitted setup polynomials, checks the old-to-new zero
specialization and partition-origin affine map, and validates every available
guided-GB run against its durable input/output files.
"""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
import re
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
EXPECTED = {
    "S5": {"n": 9, "m": 6, "M2": 2, "V2": 1, "K": 3, "ell": 8,
           "delta1": F(3, 2), "B": F(-3, 2), "delta_s": F(-3, 2)},
    "S6": {"n": 9, "m": 6, "M2": 5, "V2": 2, "K": 3, "ell": 8,
           "delta1": F(2, 3), "B": F(-5, 3), "delta_s": F(-3)},
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def inventory(data: dict[str, Any], deficit: int) -> tuple[set[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
    K = data["K"]
    D = {(b, a) for a in range(K) for b in range(math.floor(data["delta1"] * a - deficit * data["B"]) + 1)}
    d = -data["delta_s"]
    G = {(b, a) for a in range(K) for b in range(math.floor(d * (deficit * K - a)) + 1)}
    return D | G, D, G


def setup(text: str) -> dict[str, sp.Expr]:
    rows = dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*);$", text, re.M))
    return {key: sp.sympify(value.replace("^", "**")) for key, value in rows.items()}


def stem_row(stem: str) -> str:
    if stem.startswith("S5_"):
        return "S5"
    if stem.startswith("S6_"):
        return "S6"
    raise AssertionError(stem)


def expected_face(name: str, part: tuple[int, ...]) -> sp.Expr:
    x, y, s2 = sp.symbols("x y s2")
    if name == "S5" and part == (2,):
        return sp.expand(y * (y - x) ** 2)
    if name == "S5" and part == (1, 1):
        return sp.expand(y * (y - x) * (y - s2 * x))
    if name == "S6" and part == (1,):
        return sp.expand(y**2 * (y - x))
    raise AssertionError((name, part))


def expected_block(prefix: str, mons: set[tuple[int, int]]) -> sp.Expr:
    x, y = sp.symbols("x y")
    result = sp.Integer(0)
    for b, a in mons:
        result += sp.Symbol(f"{prefix}_{b}_{a}") * x**b * y**a
    return sp.expand(result)


def parse_resource(stderr: Path) -> dict[str, Any]:
    text = stderr.read_text(encoding="utf-8", errors="replace")
    out: dict[str, Any] = {}
    for key, pattern in {
        "maximum_rss_kb": r"Maximum resident set size \(kbytes\):\s*(\d+)",
        "elapsed_wall": r"Elapsed \(wall clock\) time.*:\s*(\S+)",
        "exit_status": r"Exit status:\s*(\d+)",
    }.items():
        match = re.search(pattern, text)
        if match:
            out[key] = int(match.group(1)) if key != "elapsed_wall" else match.group(1)
    return out


def verify_chart(meta_path: Path) -> dict[str, Any]:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    meta = payload["meta"]
    name = stem_row(meta_path.stem)
    data = EXPECTED[name]
    part = tuple(meta["partition"])
    assert payload["support_parameter"] == meta["chart"] == "source-complete"
    assert payload["source_correction"]["ell"] == meta["row"]["ell"] == data["ell"] == 8
    assert F(meta["closed_form"]["delta1"]) == data["delta1"]
    assert F(meta["closed_form"]["B"]) == data["B"]
    assert F(meta["delta_s"]) == data["delta_s"]
    assert meta["beta1"].startswith("structurally_zero")
    assert meta["gauges"] == ["Q -> Q - const(beta_2)", "P -> P - const(alpha_3)"]
    assert meta["scalar_shear_used"] is False

    expected = {i: inventory(data, i)[0] for i in (1, 2, 3)}
    actual_h = set(map(tuple, meta["h_inventory"]))
    actual_alpha = {int(i): set(map(tuple, mons)) for i, mons in meta["alpha_inventories"].items()}
    actual_beta = {int(i): set(map(tuple, mons)) for i, mons in meta["beta_inventories"].items()}
    assert actual_h == expected[1]
    assert actual_alpha[1] == expected[1]
    assert actual_alpha[2] == expected[2]
    assert actual_alpha[3] == expected[3] - {(0, 0)}
    assert actual_beta[2] == expected[2] - {(0, 0)}
    for i in (1, 2, 3):
        union, D, G = inventory(data, i)
        support = meta["source_support"]
        assert set(map(tuple, support["D"][str(i)])) == D
        assert set(map(tuple, support["G"][str(i)])) == G
        assert set(map(tuple, support["S"][str(i)])) == union

    expected_variables = {f"h_{b}_{a}" for b, a in actual_h}
    for i, mons in actual_alpha.items():
        expected_variables |= {f"A{i}_{b}_{a}" for b, a in mons}
    for i, mons in actual_beta.items():
        expected_variables |= {f"B{i}_{b}_{a}" for b, a in mons}
    if len(part) > 1:
        expected_variables.add("s2")
    expected_variables.add("c")
    assert set(payload["variables"]) == expected_variables
    assert len(payload["variables"]) == meta["params_without_T"]

    builder = ROOT / payload["builder"]
    assert sha256(builder) == payload["builder_sha256"]
    builder_text = builder.read_text(encoding="utf-8")
    polys = setup(builder_text)
    x, y = sp.symbols("x y")
    face = expected_face(name, part)
    assert sp.expand(polys["h"] - face - expected_block("h", actual_h)) == 0
    for i, mons in actual_alpha.items():
        assert sp.expand(polys[f"AA{i}"] - expected_block(f"A{i}", mons)) == 0
    for i, mons in actual_beta.items():
        assert sp.expand(polys[f"BB{i}"] - expected_block(f"B{i}", mons)) == 0
    ring = re.search(r"^ring R=\(0,(.*)\),\(y,x\),dp;$", builder_text, re.M)
    assert ring and ring.group(1).split(",") == payload["variables"]
    assert f"H0 = H0 - c*x^{data['ell']};" in builder_text

    legacy_meta = HERE / "legacy-capped" / "meta" / meta_path.name.replace("source_complete", "legacy")
    legacy_payload = json.loads(legacy_meta.read_text(encoding="utf-8"))
    legacy_polys = setup((ROOT / legacy_payload["builder"]).read_text(encoding="utf-8"))
    added = set(payload["variables"]) - set(legacy_payload["variables"])
    substitution = {sp.Symbol(var): 0 for var in added}
    for key in polys:
        assert sp.expand(polys[key].subs(substitution) - legacy_polys[key]) == 0, (meta_path.stem, key)

    # The fixed partition face is only an affine coordinate origin: every
    # nonmonic face monomial has a free h-coordinate in S_1.
    face_support = {
        (mon[0], mon[1])
        for mon, coeff in sp.Poly(face - y**data["K"], x, y).terms()
        if coeff != 0
    }
    assert face_support <= actual_h
    affine = meta["partition_to_canonical_map"]
    assert affine["triangular_affine_ring_isomorphism"] is True
    assert len(affine["forward_partition_to_canonical"]) == len(actual_h)
    assert len(affine["inverse_canonical_to_partition"]) == len(actual_h)

    build = payload.get("builder_run")
    assert build and build["returncode"] == 0 and not build["timed_out"]
    assert build["native_done"] and build["target_gate"] and build["rows_exists"]
    rows_path = ROOT / payload["rows_path"]
    assert sha256(rows_path) == build["rows_sha256"]
    with rows_path.open(encoding="utf-8") as source:
        assert source.readline().rstrip("\n") == "source_index|h_power|x_power|y_power|expr"
        row_count = sum(1 for line in source if line.strip())
    assert row_count == build["row_count"]
    stdout = ROOT / build["stdout"]
    stdout_text = stdout.read_text(encoding="utf-8", errors="replace")
    assert "? error occurred" not in stdout_text
    assert f"NATIVE_DONE equations={row_count}" in stdout_text
    assert "NATIVE_GATE target_xk_level0_nonzero=1" in stdout_text
    return {
        "stem": meta_path.stem,
        "status": "PASS",
        "row": name,
        "partition": list(part),
        "parameters_without_T": len(payload["variables"]),
        "rows": row_count,
        "rows_sha256": sha256(rows_path),
        "builder_sha256": sha256(builder),
        "legacy_zero_specialization": True,
        "partition_origin_affinely_canonical": True,
        "source_complete_support": True,
        "ell8_target_gate": True,
    }


def verify_solve(record_path: Path) -> dict[str, Any]:
    record = json.loads(record_path.read_text(encoding="utf-8"))
    assert record["meta_sha256"] == sha256(ROOT / record["meta"])
    assert record["rows_sha256"] == sha256(ROOT / record["rows"])
    run = record["guided_result"]["certificate"]["runs"][0]
    script, stdout, stderr = map(Path, (run["script"], run["stdout"], run["stderr"]))
    assert run["script_sha256"] == record["script_sha256_recomputed"] == sha256(script)
    assert run["stdout_sha256"] == record["stdout_sha256_recomputed"] == sha256(stdout)
    assert run["stderr_sha256"] == record["stderr_sha256_recomputed"] == sha256(stderr)
    script_text = script.read_text(encoding="utf-8", errors="replace")
    stdout_text = stdout.read_text(encoding="utf-8", errors="replace")
    assert record["ring_prelude"].strip() in script_text
    assert f"GG__GENERATOR_COUNT main {record['generator_count']}" in stdout_text or run["timed_out"]
    main = run["main"]
    completed = (
        run["returncode"] == 0
        and not run["timed_out"]
        and "GG__RUN main END" in stdout_text
        and "GG__SCRIPT_DONE main 1" in stdout_text
        and "? error occurred" not in stdout_text
        and main["accepted"]
        and main["nf_all_zero"]
        and not main["missing_markers"]
    )
    clean_unit = completed and main["unit"] and main["basis_size"] == 1 and main["dimension"] == -1 and main["lead_dim"] == -1
    resource = parse_resource(stderr)
    # The lane runner samples the whole process group into a JSON sidecar.
    # That is the authoritative RSS source when GNU time has not written a
    # trailer (for example, a deliberately stopped incomplete diagnostic).
    monitor = record.get("resource", {}).get("process_group_monitor", {})
    if monitor:
        assert monitor.get("schema") == "jc2.s56-recert.process-group-resource/v1"
        assert monitor.get("returncode") == run["returncode"]
        assert monitor.get("timed_out") == run["timed_out"]
        resource["process_group_monitor"] = monitor
        resource.setdefault("maximum_rss_kb", monitor.get("maximum_process_group_rss_kb", 0))
    assert resource.get("maximum_rss_kb", 0) > 0 or run["timed_out"]
    return {
        "record": str(record_path.relative_to(ROOT)),
        "status": "PASS",
        "characteristic": record["characteristic"],
        "branch": record["branch"],
        "completed_accepted": completed,
        "clean_unit": clean_unit,
        "exact_q_clean_unit": clean_unit and record["characteristic"] == 0,
        "dimension": main["dimension"],
        "basis_size": main["basis_size"],
        "returncode": run["returncode"],
        "timed_out": run["timed_out"],
        "elapsed_seconds": run["elapsed_seconds"],
        "resource": resource,
    }


def main() -> None:
    frozen = json.loads((HERE / "frozen-inputs-check.json").read_text(encoding="utf-8"))
    assert frozen["ok"] and all(item["ok"] for item in frozen["checks"])
    charts = [verify_chart(path) for path in sorted((HERE / "source-complete" / "meta").glob("*.json"))]
    assert len(charts) == 3
    solves = [verify_solve(path) for path in sorted((HERE / "solves").glob("**/solve-record.json"))]
    payload = {
        "schema": "jc2.s56-recert.independent-verification/v1",
        "status": "PASS",
        "frozen_inputs_ok": True,
        "charts": charts,
        "solves": solves,
        "clean_modular_units": sum(item["clean_unit"] and item["characteristic"] > 0 for item in solves),
        "clean_exact_q_units": sum(item["exact_q_clean_unit"] for item in solves),
        "script": str(Path(__file__).relative_to(ROOT)),
        "script_sha256": sha256(Path(__file__)),
    }
    output = HERE / "verification.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
