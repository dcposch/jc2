#!/usr/bin/env python3
"""Independent hash/control replay and typed verdicts for batch 2."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b2-20260903"
PRIMES = (32003, 32009, 32027)
S5_P2 = "S5_n9_m6_M2_V1_k8_part_2_full"
S5_P11 = "S5_n9_m6_M2_V1_k8_part_1_1_full"
S6_P1 = "S6_n9_m6_M5_V2_k8_part_1_full"
Q2 = "s2^2-s2+1"
Q6 = "11*s2^6-33*s2^5+12*s2^4+31*s2^3+12*s2^2-33*s2+11"
MOD_FACTORS = {
    32003: ["s2+5315", "s2+6579", "s2+7929", "s2-7930", "s2-6580", "s2-5316"],
    32009: ["s2^2+7890*s2-7890", "s2^2-7892*s2+1", "s2^2-s2-10836"],
    32027: ["s2^2+8148*s2-8148", "s2^2-8150*s2+1", "s2^2-s2-15475"],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def branch_hash(material: str) -> str:
    return hashlib.sha256(material.encode()).hexdigest()[:10]


def guided_record(stem: str, characteristic: int, material: str | None = None) -> dict[str, Any]:
    directory = HERE / "guided" / stem / "coefficient-first"
    if material is not None:
        directory = directory.with_name(directory.name + "_branch_" + branch_hash(material))
    suffix = "Q" if characteristic == 0 else f"p{characteristic}"
    matches = list(directory.glob(f"*_{suffix}.guided.json"))
    if len(matches) != 1:
        raise AssertionError((stem, characteristic, material, matches))
    path = matches[0]
    record = json.loads(path.read_text(encoding="utf-8"))
    main = record["main"]
    clean = (
        record["returncode"] == 0
        and record["timed_out"] is False
        and main["accepted"] is True
        and main["nf_all_zero"] is True
        and main["unit"] is True
        and main["basis_size"] == 1
        and main["dimension"] == -1
        and main["missing_markers"] == []
    )
    for field, hash_field in (("script", "script_sha256"), ("stdout", "stdout_sha256"), ("stderr", "stderr_sha256")):
        artifact = Path(record[field])
        if sha256(artifact) != record[hash_field]:
            raise AssertionError(f"hash mismatch for {artifact}")
    if not clean:
        raise AssertionError(f"unclean unit record {path}")
    return {
        "certificate": str(path.relative_to(ROOT)),
        "certificate_sha256": sha256(path),
        "characteristic": characteristic,
        "material": material,
        "elapsed_seconds": record["elapsed_seconds"],
        "basis_size": main["basis_size"],
        "unit": main["unit"],
        "nf_all_zero": main["nf_all_zero"],
        "clean": clean,
        "script_sha256": record["script_sha256"],
        "stdout_sha256": record["stdout_sha256"],
    }


def verify_modular_factor_cover() -> dict[str, Any]:
    s = sp.symbols("s2")
    q6 = sp.sympify(Q6.replace("^", "**"))
    cover = {}
    for prime, factor_strings in MOD_FACTORS.items():
        factors = [sp.sympify(item.replace("^", "**")) for item in factor_strings]
        product = sp.Poly(sp.prod(factors), s, modulus=prime).monic()
        target = sp.Poly(q6, s, modulus=prime).monic()
        factorization_ok = product == target
        squarefree = sp.gcd(target, target.diff()).degree() == 0
        if not factorization_ok or not squarefree:
            raise AssertionError((prime, factorization_ok, squarefree))
        runs = [guided_record(S5_P11, prime, item) for item in factor_strings]
        cover[str(prime)] = {
            "factors": factor_strings,
            "factorization_equals_monic_Q6": factorization_ok,
            "squarefree": squarefree,
            "all_factor_charts_unit": all(run["clean"] for run in runs),
            "runs": runs,
        }
    return cover


def verify_rows_and_bands(stem: str) -> dict[str, Any]:
    meta_path = HERE / "meta" / f"{stem}.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / meta["rows_path"]
    builder = ROOT / meta["builder"]
    manifest_path = HERE / "bands" / stem / "Q" / "bands-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    staged_entries = list(manifest["band_files"])
    if manifest["global_file"] is not None:
        staged_entries.append(manifest["global_file"])
    staged_hashes_match = all(
        sha256(Path(entry["path"])) == entry["sha256"] for entry in staged_entries
    )
    canonical = []
    with rows_path.open(encoding="utf-8") as handle:
        header = handle.readline().rstrip("\n").split("|")
        if header != ["source_index", "h_power", "x_power", "y_power", "expr"]:
            raise AssertionError(f"bad row header {rows_path}")
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            source_index, _h, _x, _y, expr = line.split("|", 4)
            canonical.append(f"row_{source_index}\0{re.sub(r'\\s+', '', expr.strip())}")
    localizer = "T*(" + meta["sat"] + ")-1"
    canonical.append("localization\0" + re.sub(r"\s+", "", localizer))
    recomputed_union = hashlib.sha256(("\n".join(sorted(canonical)) + "\n").encode()).hexdigest()
    union_recomputation_matches = (
        recomputed_union == manifest["generator_union_checksum"]
        == manifest["monolithic_generator_checksum"]
    )
    checks = {
        "meta_sha256": sha256(meta_path),
        "builder_hash_matches": sha256(builder) == meta["builder_sha256"],
        "rows_hash_matches_builder_run": sha256(rows_path) == meta["builder_run"]["rows_sha256"],
        "builder_native_done": meta["builder_run"]["native_done"],
        "target_gate": meta["builder_run"]["target_gate"],
        "manifest_source_rows_matches": manifest["source_rows_sha256"] == sha256(rows_path),
        "staged_file_hashes_matches": staged_hashes_match,
        "union_recomputation_matches": union_recomputation_matches,
        "union_equals_monolithic": manifest["union_equals_monolithic"],
        "row_count": manifest["row_count"],
        "parameter_count_without_T": meta["meta"]["params_without_T"],
        "target": meta["source_correction"]["target"],
        "manifest": str(manifest_path.relative_to(ROOT)),
        "manifest_sha256": sha256(manifest_path),
    }
    if not all(value for key, value in checks.items() if key.endswith("matches") or key in {"builder_native_done", "target_gate", "union_equals_monolithic"}):
        raise AssertionError(checks)
    return checks


def timeout_record(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "timed_out": payload["timed_out"],
        "returncode": payload["returncode"],
        "elapsed_seconds": payload["elapsed_seconds"],
        "accepted": payload.get("main", {}).get("accepted"),
    }


def main() -> None:
    input_check_path = HERE / "charged-inputs-check.json"
    input_check = json.loads(input_check_path.read_text(encoding="utf-8"))
    input_checks_current = all(
        item["ok"]
        and item["expected"] == item["got"]
        and sha256(Path(item["path"])) == item["expected"]
        for item in input_check["checks"]
    )
    if not input_check["ok"] or len(input_check["checks"]) != 14 or not input_checks_current:
        raise AssertionError("frozen input custody failed")

    enumeration_path = HERE / "enumeration.json"
    enumeration = json.loads(enumeration_path.read_text(encoding="utf-8"))
    if enumeration["count"] != 8 or [row["id"] for row in enumeration["rows"]] != [f"S{i}" for i in range(1, 9)]:
        raise AssertionError("enumeration changed")

    top_pin_path = HERE / "top-pin-audit.json"
    top_pin = json.loads(top_pin_path.read_text(encoding="utf-8"))
    z = sp.symbols("z")
    h2 = sp.sympify(top_pin["partition_2"]["h"])
    theta2 = sp.sympify(top_pin["partition_2"]["theta"])
    top2_residual = sp.expand(3 * h2 * sp.diff(theta2, z) - 13 * sp.diff(h2, z) * theta2 - h2**2)
    expected_branches = {
        "s**2 - s + 1",
        "11*s**6 - 33*s**5 + 12*s**4 + 31*s**3 + 12*s**2 - 33*s + 11",
    }
    top_pin_checks = {
        "correct_identity": top_pin["identity"] == "3*h*d(theta)/dz-13*d(h)/dz*theta=h^2",
        "correct_descent_target": top_pin["source"]["descent_target"] == "J_(gamma,pi)(G,F)=c*gamma^8",
        "partition_2_residual_zero": top2_residual == 0 and top_pin["partition_2"]["identity_residual"] == "0",
        "partition_1_1_branch_cover": set(top_pin["partition_1_1"]["branches"]) == expected_branches,
        "branch_factors_not_inverted": top_pin["fallacy_controls"]["no_division_by_branch_factor"] is True,
        "only_root_separation_localized": top_pin["fallacy_controls"]["only_s_and_s_minus_1_are_localized"] is True,
    }
    if not all(top_pin_checks.values()):
        raise AssertionError(top_pin_checks)

    triage_path = HERE / "split-unsplit-triage.json"
    triage = json.loads(triage_path.read_text(encoding="utf-8"))
    split_residuals_zero = all(
        chart["ode_residual"] == "0"
        for charts in triage["split_face_charts"].values()
        for chart in charts
    )
    if not split_residuals_zero or not all(triage["fallacy_controls"].values()):
        raise AssertionError("split/unsplit exact triage failed")

    controls_path = HERE / "controls" / "controls-summary.json"
    controls = json.loads(controls_path.read_text(encoding="utf-8"))
    if controls["status"] != "PASS" or not all(controls["assertions"].values()):
        raise AssertionError("controls failed")
    genuine = controls["genuine_tame_automorphism"]
    genuine_run = genuine["guided_gb"]
    genuine_required = {
        "status": genuine["status"] == "PASS",
        "accepted": genuine_run["accepted"] is True,
        "nonunit": genuine_run["unit"] is False,
        "dimension_zero": genuine_run["dimension"] == 0,
        "vdim_one": genuine_run["vdim"] == 1,
        "nf_all_zero": genuine_run["nf_all_zero"] is True,
        "clean_exit": genuine_run["returncode"] == 0 and genuine_run["timed_out"] is False,
        "jacobian_one": genuine["construction"]["specialized_jacobian"] == "1",
        "polynomial_inverse": genuine["construction"]["polynomial_inverse"] == "(u,v)->(v,v^2-u)",
    }
    for field, hash_field in (
        ("script", "script_sha256"),
        ("stdout", "stdout_sha256"),
        ("stderr", "stderr_sha256"),
    ):
        genuine_required[f"{field}_hash"] = sha256(Path(genuine_run[field])) == genuine_run[hash_field]
    genuine_stdout = Path(genuine_run["stdout"]).read_text(encoding="utf-8")
    genuine_required["exact_map_markers"] = all(
        marker in genuine_stdout for marker in genuine["exact_map_markers"]
    )
    if not all(genuine_required.values()):
        raise AssertionError(genuine_required)
    tame_form = controls["tame_form"]
    tame_form_ok = (
        tame_form["verdict"] == "DIM0_CHAR0"
        and tame_form["runs"][0]["unit"] is False
        and tame_form["runs"][0]["dimension"] == 0
        and tame_form["runs"][0]["vdim"] == 2
        and tame_form["counts"]["markers"].get("PRE__CTRL_J") == "6*x*mu^2"
    )
    hint = controls["perturbed_hilbert"]
    perturb_ok = (
        hint["main_accepted"] is True
        and hint["perturbed_accepted"] is False
        and hint["main_lead_vdim"] == hint["predicted_length"] == 3640
    )
    if not tame_form_ok or not perturb_ok:
        raise AssertionError({"tame_form_ok": tame_form_ok, "perturb_ok": perturb_ok})
    control_bundle_sha = sha256(controls_path)

    s = sp.symbols("s2")
    q6_expr = sp.sympify(Q6.replace("^", "**"))
    if sp.factor(q6_expr) != q6_expr or sp.gcd(q6_expr, sp.diff(q6_expr, s)) != 1:
        raise AssertionError("Q6 is not irreducible squarefree over Q")

    s5_p2_runs = [guided_record(S5_P2, p) for p in PRIMES] + [guided_record(S5_P2, 0)]
    s5_q2_runs = [guided_record(S5_P11, p, Q2) for p in PRIMES] + [guided_record(S5_P11, 0, Q2)]
    s5_q6_exact = guided_record(S5_P11, 0, f"COEFF:s2:{Q6}")
    s5_q6_modular = verify_modular_factor_cover()
    s6_runs = [guided_record(S6_P1, p) for p in PRIMES] + [guided_record(S6_P1, 0)]

    # Verify that the exact sextic run really used Q[s2]/(Q6), not merely a label.
    q6_script = Path(json.loads((ROOT / s5_q6_exact["certificate"]).read_text(encoding="utf-8"))["script"])
    q6_text = q6_script.read_text(encoding="utf-8")
    q6_field_ok = "ring R=(0,s2)" in q6_text and f"minpoly={Q6};" in q6_text
    if not q6_field_ok:
        raise AssertionError("exact sextic coefficient-field map missing")

    s1_base = HERE / "guided" / "S1_n18_m12_Mm4_V1_k6_part_5_full"
    s1_timeouts = [timeout_record(path) for path in sorted(s1_base.rglob("*.guided.json"))]
    if not s1_timeouts or not all(item["timed_out"] for item in s1_timeouts):
        raise AssertionError("S1 timeout audit changed")
    s4_build = timeout_record(HERE / "build-runs" / "S4_n27_m18_M6_V1_k4_part_8_full.json")
    if not s4_build["timed_out"]:
        raise AssertionError("S4 formation was expected to time out")

    payload = {
        "schema": "jc2.g9966n1b2.results/v1",
        "audits": {
            "charged_inputs": {
                "path": str(input_check_path.relative_to(ROOT)),
                "sha256": sha256(input_check_path),
                "count": len(input_check["checks"]),
                "all_current_hashes_match": input_checks_current,
            },
            "enumeration": {
                "path": str(enumeration_path.relative_to(ROOT)),
                "sha256": sha256(enumeration_path),
                "count": enumeration["count"],
            },
            "top_pin": {
                "path": str(top_pin_path.relative_to(ROOT)),
                "sha256": sha256(top_pin_path),
                "checks": top_pin_checks,
            },
            "split_unsplit_triage": {
                "path": str(triage_path.relative_to(ROOT)),
                "sha256": sha256(triage_path),
                "all_face_ode_residuals_zero": split_residuals_zero,
                "fallacy_controls": triage["fallacy_controls"],
            },
        },
        "controls": {
            "path": str(controls_path.relative_to(ROOT)),
            "sha256": control_bundle_sha,
            "assertions": controls["assertions"],
            "independent_genuine_tame_checks": genuine_required,
            "tame_form_ok": tame_form_ok,
            "perturb_ok": perturb_ok,
            "attached_to_kills": ["S5", "S6"],
        },
        "S5": {
            "status": "DEAD[UNIT_IDEAL_CHAR0]",
            "corrected_datum": "(9,6;M2=2,V2=1;ell=8)",
            "partition_2_chart": verify_rows_and_bands(S5_P2),
            "partition_1_1_chart": verify_rows_and_bands(S5_P11),
            "partition_2": {"runs": s5_p2_runs, "three_primes_plus_Q": True},
            "partition_1_1_quadratic": {"branch": Q2, "runs": s5_q2_runs, "three_primes_plus_Q": True},
            "partition_1_1_sextic": {
                "branch": Q6,
                "irreducible_squarefree_Q": True,
                "exact_Q_algebraic_coefficient_field": s5_q6_exact,
                "exact_field_map_present": q6_field_ok,
                "modular_factor_covers": s5_q6_modular,
                "three_primes_plus_Q": True,
            },
            "branch_cover": "[2] union [1,1]; on [1,1], V(Q2*Q6)=V(Q2) union V(Q6)",
        },
        "S6": {
            "status": "DEAD[UNIT_IDEAL_CHAR0]",
            "corrected_datum": "(9,6;M2=5,V2=2;ell=8)",
            "full_chart": verify_rows_and_bands(S6_P1),
            "partition_1": {"runs": s6_runs, "three_primes_plus_Q": True},
            "note": "repaired computation; obsolete charged ell=2 certificate is not consumed",
        },
        "open": {
            "S1": {"status": "OPEN[FULL-BASIS-TIMEOUT+SPLIT-JOINT-UNBUILT]", "runs": s1_timeouts},
            "S2": {"status": "OPEN[EXACT-SYSTEM-SPECIFIED;JOINT-CHART-UNBUILT]"},
            "S3": {"status": "OPEN[EXACT-SYSTEM-SPECIFIED;JOINT-CHART-UNBUILT]"},
            "S4": {"status": "OPEN[FULL-BASIS-EMITTER-TIMEOUT+SPLIT-JOINT-UNBUILT]", "formation": s4_build},
            "S7": {"status": "OPEN[EXACT-SYSTEM-SPECIFIED;JOINT-CHART-UNBUILT]"},
        },
        "tally": {
            "lane_six_dead": 1,
            "lane_six_open": 5,
            "non_S8_dead_of_7": 2,
            "dead_non_S8": ["S5", "S6"],
            "banked_S8_dead": True,
            "overall": "PARTIAL",
            "N1_closed": False,
        },
        "promotion_guard": {
            "modular_units_are_screens_only": True,
            "every_promoted_death_has_exact_Q_unit": True,
            "inhomogeneous_localized_systems_not_promoted_by_properness": True,
            "no_exit_price_assertion": True,
        },
    }
    output = HERE / "results-summary.json"
    atomic_write(output, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "output": str(output.relative_to(ROOT)),
        "sha256": sha256(output),
        "S5": payload["S5"]["status"],
        "S6": payload["S6"]["status"],
        "tally": payload["tally"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
