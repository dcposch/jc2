#!/usr/bin/env python3
"""Fail-closed scalar-row count for the T2 support-face lane.

The charged report defines the attainment equations as scalar coefficients
q_pq=[x^p y^q]Q. This driver declares the requested support-cut rings,
constructs the direct D2 face rows, enumerates those scalar T2 row tags, and
checks the cap before coefficient expansion or any Singular invocation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RECEIPT = ROOT / "xmodel/t2-face-cap80-sol56-20260906.run.v2"
INPUT_DIR = Path("/tmp/jc2-lane.x7VhB7/inputs")
CAP = 80


K2C = {
    "g9966_delta2": [
        "K2c_13_20", "K2c_16_17", "K2c_17_16", "K2c_18_11",
        "K2c_19_14", "K2c_20_13", "K2c_21_9", "K2c_22_8",
        "K2c_22_9", "K2c_23_9", "K2c_24_9", "K2c_25_7",
        "K2c_25_8", "K2c_26_5", "K2c_26_7", "K2c_27_6",
        "K2c_28_4", "K2c_28_5", "K2c_29_3", "K2c_29_4",
        "K2c_30_2", "K2c_30_3", "K2c_31_1", "K2c_31_2",
        "K2c_32_1", "K2c_33_0", "K2c_7_21",
    ],
    "g9966_delta52": [
        "K2c_25_8", "K2c_26_5", "K2c_29_4", "K2c_30_2",
        "K2c_31_1", "K2c_32_1", "K2c_33_0",
    ],
    "d108_repaired_free_mean_jet0_slice": [
        "K2c_21_15", "K2c_22_11", "K2c_25_9", "K2c_26_9",
        "K2c_27_7", "K2c_28_6", "K2c_29_7", "K2c_30_6",
        "K2c_31_5", "K2c_32_3", "K2c_33_2", "K2c_33_3",
        "K2c_34_2", "K2c_35_1", "K2c_36_0", "K2c_9_26",
    ],
}


CASES = {
    "g9966_delta2": {
        "k": 33,
        "attained_y_degree": 55,
        "minor_parameters": ["jet0", "u", "rho"],
        "source_inverse": "Zrho*rho-1",
        "leader": "lambda55",
        "leader_inverse_variable": "Z55",
        "P": {"step": 3, "power": 8},
        "FG_top_y_range": [45, 165],
        "minor_face_target": "zeta^2*(zeta+3*rho)",
        "inner_gate": {"raw_rows": 105, "nonzero_rows": 100,
                       "rational_pivots": 76, "dependent_zero": 29,
                       "residual": 0},
        "outer_omitted_constants": [
            "A2c_65_0", "A3c_98_0", "B1c_32_0", "B2c_65_0"
        ],
    },
    "g9966_delta52": {
        "k": 33,
        "attained_y_degree": 55,
        "minor_parameters": ["jet0", "u", "v", "c"],
        "source_inverse": "Zc*c-1",
        "leader": "lambda55",
        "leader_inverse_variable": "Z55",
        "P": {"step": 3, "power": 8},
        "FG_top_y_range": [45, 165],
        "minor_face_target": "zeta*(zeta^2-c)",
        "inner_gate": {"raw_rows": 130, "nonzero_rows": 120,
                       "rational_pivots": 94, "dependent_zero": 36,
                       "residual": 0},
        "outer_omitted_constants": [
            "A2c_65_0", "A3c_98_0", "B1c_32_0", "B2c_65_0"
        ],
    },
    "d108_repaired_free_mean_jet0_slice": {
        "k": 36,
        "attained_y_degree": 63,
        "minor_parameters": ["jet1", "jet2", "minor_mean", "c"],
        "source_inverse": "Zc*c-1",
        "leader": "lambda63",
        "leader_inverse_variable": "Z63",
        "P": {"step": 4, "power": 7},
        "FG_top_y_range": [40, 180],
        "minor_face_target": "((pi-minor_mean)^2-c)^4",
        "inner_gate": {"raw_rows": 129, "rational_pivots": 102,
                       "dependent_zero": 27, "residual": 0},
        "repaired_incidence": {
            "minor_n8_pi1": "old-2*minor_mean",
            "minor_n8_pi0": "old+minor_mean^2",
            "jet0_slice": 0,
        },
        "outer_omitted_constants": [
            "A2c_71_0", "A3c_107_0", "B1c_35_0", "B2c_71_0"
        ],
    },
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def mechanical_input_check() -> dict:
    """Build the receipt-derived manifest with awk and run sha256sum -c."""
    awk_program = r'''
BEGIN { FS="=" }
/^charged_input_[0-9]+_basename=/ {
  split($1,a,"_"); basename[a[3]]=$2; if (a[3]>count) count=a[3]
}
/^charged_input_[0-9]+_sha256=/ {
  split($1,a,"_"); digest[a[3]]=$2; if (a[3]>count) count=a[3]
}
END {
  for (i=1; i<=count; i++) print digest[i] "  " input_dir "/" basename[i]
}
'''
    with tempfile.TemporaryDirectory(prefix="t2-face-cap80-hashes-") as tmp:
        manifest_path = Path(tmp) / "charged.sha256"
        built = subprocess.run(
            ["awk", "-v", f"input_dir={INPUT_DIR}", awk_program, str(RECEIPT)],
            check=True, capture_output=True, text=True,
        )
        manifest_path.write_text(built.stdout, encoding="utf-8")
        checked = subprocess.run(
            ["sha256sum", "-c", str(manifest_path)],
            check=False, capture_output=True, text=True,
        )
    if checked.returncode != 0:
        raise RuntimeError("charged-input content mismatch:\n" + checked.stdout + checked.stderr)
    lines = [line for line in checked.stdout.splitlines() if line]
    if len(lines) != 6 or any(not line.endswith(": OK") for line in lines):
        raise RuntimeError("unexpected sha256sum transcript")
    return {
        "method": "receipt-derived awk manifest, then sha256sum -c",
        "receipt": str(RECEIPT),
        "receipt_sha256": sha256_file(RECEIPT),
        "input_dir": str(INPUT_DIR),
        "manifest_sha256": sha256_bytes(built.stdout.encode()),
        "transcript": lines,
        "all_match": True,
    }


def outer_tables(is99: bool) -> dict[str, list[tuple[int, int, str]]]:
    if is99:
        specs = {
            "A2": [(63 - 4*j, 3*j) for j in range(11)],
            "A3": [(95 - 4*j, 3*j) for j in range(11)],
            "B1": [(31 - 4*j, 3*j) for j in range(8)],
            "B2": [(63 - 4*j, 3*j) for j in range(11)],
        }
    else:
        specs = {
            "A2": [(69 - 5*j, 4*j) for j in range(9)],
            "A3": [(104 - 5*j, 4*j) for j in range(9)],
            "B1": [(34 - 5*j, 4*j) for j in range(7)],
            "B2": [(69 - 5*j, 4*j) for j in range(9)],
        }
    return {
        block: [(r, q, f"{block}c_{r}_{q}") for r, q in positions]
        for block, positions in specs.items()
    }


def polynomial_text(terms: list[tuple[int, str]]) -> str:
    combined: dict[str, int] = {}
    for coefficient, variable in terms:
        combined[variable] = combined.get(variable, 0) + coefficient
    pieces = []
    for variable in sorted(combined):
        coefficient = combined[variable]
        if coefficient:
            pieces.append(f"{coefficient}*{variable}")
    return "+".join(pieces).replace("+-", "-") or "0"


def face_rows(tables: dict[str, list[tuple[int, int, str]]], step: int,
              power: int) -> list[tuple[str, str]]:
    p_coeff = {
        step*j: math.comb(power, j) * (-1) ** (power-j)
        for j in range(power + 1)
    }
    rows: list[tuple[str, str]] = []
    for target, left, right in (("F", "A2", "A3"), ("G", "B1", "B2")):
        by_degree: dict[int, list[tuple[int, str]]] = {}
        for _r, q, variable in tables[left]:
            for pq, coefficient in p_coeff.items():
                by_degree.setdefault(q + pq, []).append((coefficient, variable))
        for _r, q, variable in tables[right]:
            by_degree.setdefault(q, []).append((1, variable))
        for q in sorted(by_degree):
            expression = polynomial_text(by_degree[q])
            if expression != "0":
                rows.append((f"D2_{target}_pi{q}_coefficient_minus_target", expression))
    return rows


def attainment_tags(k: int, target: int, leader: str) -> dict:
    ambient = 6*k
    tags = []
    for q in range(target + 1, ambient + 1):
        for p in range(ambient - q + 1):
            tags.append(f"q_{p}_{q}=0")
    upper_count = len(tags)
    for p in range(1, ambient - target + 1):
        tags.append(f"q_{p}_{target}=0")
    at_positive_x = len(tags) - upper_count
    tags.append(f"q_0_{target}-{leader}=0")
    canonical_tags = tags[:-1] + [f"q_0_{target}-lambda=0"]
    return {
        "ambient_total_degree_bound": ambient,
        "upper_y_scalar_rows": upper_count,
        "at_degree_positive_x_scalar_rows": at_positive_x,
        "leader_coefficient_minus_target_rows": 1,
        "scalar_tags_excluding_inverse": len(tags),
        "instantiated_tag_sha256_excluding_inverse":
            sha256_bytes(("\n".join(tags) + "\n").encode()),
        "canonical_tag_index_sha256_excluding_inverse":
            sha256_bytes(("\n".join(canonical_tags) + "\n").encode()),
        "first_tag": tags[0],
        "last_tag": tags[-1],
        "nothing_below_y_degree": target,
    }


def build_case(name: str, spec: dict) -> dict:
    is99 = name.startswith("g9966")
    tables = outer_tables(is99)
    outer_names = [item[2] for block in ("A2", "A3", "B1", "B2")
                   for item in tables[block]]
    rows = face_rows(tables, spec["P"]["step"], spec["P"]["power"])
    expected_face_count = 35 if is99 else 30
    if len(rows) != expected_face_count:
        raise RuntimeError(f"{name}: face-row count {len(rows)} != {expected_face_count}")
    t2 = attainment_tags(spec["k"], spec["attained_y_degree"], spec["leader"])
    target_names = ["target_a", "target_b", "target_c", "target_d", "target_e"]
    ring_names = (
        K2C[name] + spec["minor_parameters"] + outer_names + target_names
        + [spec["leader"], spec["leader_inverse_variable"],
           spec["source_inverse"].split("*")[0]]
    )
    if len(ring_names) != len(set(ring_names)):
        raise RuntimeError(f"{name}: duplicate ring indeterminate")
    raw_count = len(rows) + t2["scalar_tags_excluding_inverse"] + 2
    fg_low, fg_high = spec["FG_top_y_range"]
    nonzero_witness_count = fg_high - max(fg_low, spec["attained_y_degree"] + 1) + 1
    if nonzero_witness_count <= CAP:
        raise RuntimeError(f"{name}: nonzero cap witness is too small")
    if raw_count <= CAP:
        raise RuntimeError(f"{name}: unexpected cap pass; review required")
    result = {
        "case": name,
        "coefficient_field": "Q",
        "T2_family":
            "G^3-F^2+target_a*G^2+target_b*F*G+target_c*F+target_d*G+target_e",
        "degree_data": {"h2": spec["k"], "F": 3*spec["k"],
                        "G": 2*spec["k"], "T2": spec["attained_y_degree"]},
        "support_cut": {
            "K2c_survivors": K2C[name],
            "K2c_survivor_count": len(K2C[name]),
            "minor_parameters": spec["minor_parameters"],
            "outer_D2_equality_coordinates": outer_names,
            "outer_D2_equality_coordinate_count": len(outer_names),
            "outer_constants_and_all_deeper_coordinates_omitted":
                spec["outer_omitted_constants"],
            "Jacobian_rows": 0,
            "rows_below_attained_y_degree": 0,
        },
        "inner_face_gate_receipt": spec["inner_gate"],
        "minor_face_target": spec["minor_face_target"],
        "actual_D2_face": {
            "P": f"(pi^{spec['P']['step']}-1)^{spec['P']['power']}",
            "F_target": "P^3",
            "G_target": "P^2",
            "row_formula": ["coeff_pi(A2*P+A3)", "coeff_pi(B1*P+B2)"],
            "coefficient_minus_target_row_count": len(rows),
            "row_sha256": sha256_bytes(
                "".join(f"{label}\t{expr}\n" for label, expr in rows).encode()
            ),
            "labels": [label for label, _ in rows],
        },
        "attainment_scalar_rows": t2,
        "symbolic_nonzero_cap_witness": {
            "term": "target_b*F_top*G_top",
            "FG_top_y_range": spec["FG_top_y_range"],
            "rows_with_y_above_attained_degree": nonzero_witness_count,
            "reason": "each binomial coefficient is nonzero over Q and target_b occurs in no other family term",
        },
        "localizers": {
            "leader": f"{spec['leader_inverse_variable']}*{spec['leader']}-1",
            "source": spec["source_inverse"],
        },
        "ordered_ring_generators": ring_names,
        "ordered_ring_generator_count": len(ring_names),
        "ordered_ring_generator_sha256":
            sha256_bytes(("\n".join(ring_names) + "\n").encode()),
        "raw_listed_generator_count_after_support_cut": raw_count,
        "raw_listed_generator_count_breakdown": {
            "D2_face": len(rows),
            "T2_scalar_tags_excluding_inverse": t2["scalar_tags_excluding_inverse"],
            "leader_inverse": 1,
            "source_inverse": 1,
        },
        "cap": {"limit": CAP, "raw_listed_value": raw_count,
                "certified_nonzero_generator_lower_bound": nonzero_witness_count,
                "exceeded_even_after_zero_row_deletion": True,
                "checked_before_coefficient_expansion": True,
                "checked_before_Singular": True},
        "verdict": "CAP_OPEN",
        "singular": {"invoked": False,
                     "reason": f"fail-closed generator cap: {raw_count}>{CAP}"},
        "controls": {"run": False,
                     "reason": "controls are conditional on a solver decision"},
    }
    if "repaired_incidence" in spec:
        result["repaired_incidence"] = spec["repaired_incidence"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "result.json")
    args = parser.parse_args()
    started = time.time()
    custody = mechanical_input_check()
    cases = [build_case(name, spec) for name, spec in CASES.items()]
    result = {
        "schema": "t2-face-cap80-fail-closed-v2",
        "started_utc_epoch": started,
        "finished_utc_epoch": time.time(),
        "driver": str(Path(__file__).relative_to(ROOT)),
        "driver_sha256": sha256_file(Path(__file__)),
        "charged_inputs": custody,
        "cap_policy": {
            "limit": CAP,
            "counted_object": "literal scalar coefficient-row presentation q_pq plus face rows and explicit inverses",
            "fail_closed": True,
            "no_small_basis_substitution": True,
        },
        "cases": cases,
        "overall": "CAP_OPEN_ALL_THREE_NO_GROEBNER",
        "singular_processes_spawned_by_final_driver": 0,
        "rejected_compression": {
            "description": "formal H-block rows L5/L4 were not substituted for the charged scalar q_pq rows",
            "reason": "only compressed-block ideal => raw attained-row ideal was checked; reverse ideal inclusion was not proved",
        },
        "scope": "necessary support-face rings only; no unrestricted chart and no Keller pair is decided",
        "fallacy_v2": {
            "checked": True,
            "floor_not_used_as_attainment": True,
            "coefficient_minus_target_tags_declared": True,
            "ring_names_not_used_as_maps": True,
            "sat_wrapper_used": False,
            "new_exit_price_assertion": False,
            "charge_basis_line_required": False,
        },
        "disk_free_bytes_at_receipt_write": shutil.disk_usage("/").free,
    }
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if len(encoded) > 1024 * 1024:
        raise RuntimeError(f"result JSON exceeds 1 MiB: {len(encoded)}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(json.dumps({
        "output": str(args.output),
        "bytes": len(encoded),
        "sha256": sha256_bytes(encoded),
        "overall": result["overall"],
        "generator_counts": {
            case["case"]: case["raw_listed_generator_count_after_support_cut"]
            for case in cases
        },
        "singular_processes_spawned_by_final_driver": 0,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
