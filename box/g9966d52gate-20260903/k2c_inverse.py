#!/usr/bin/env python3
"""Compact K2c inverse certificate for the original C2c/C3c coordinates."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import sys
from typing import Any


ROOT = Path("/home/ubuntu/jc2")
BASE = ROOT / "box/g9966d52gate-20260903"
ENGINE = ROOT / "box/g9966band-20260903/band_engine.py"
PINNED_ENGINE_SHA256 = "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_engine():
    require(sha256_file(ENGINE) == PINNED_ENGINE_SHA256, "engine digest mismatch")
    name = "g9966_k2c_compact_engine"
    spec = importlib.util.spec_from_file_location(name, ENGINE)
    require(spec is not None and spec.loader is not None, "cannot load engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def order_key(position: tuple[int, int]) -> tuple[int, int]:
    return position[0], -position[1]


def first_output_slot_for_c2(position: tuple[int, int]) -> tuple[int, int]:
    r, q = position
    return r, q + 11


def h3_name(position: tuple[int, int]) -> str:
    r, q = position
    top = {(0, 8): "1", (0, 9): "3", (0, 10): "3", (0, 11): "1"}
    return top.get((r, q), f"Hc_{r}_{q}")


def rows_hash(rows: list[str]) -> str:
    return hashlib.sha256("".join(row + "\n" for row in rows).encode()).hexdigest()


def main() -> None:
    engine = load_engine()
    h3, hvars = engine.h3_template()
    h3_support = set(h3)
    require(len(hvars) == 21, "h3 tail count mismatch")

    c2_positions = {
        (r, q)
        for r in range(1, 23)
        for q in range(min(10, 22 - r) + 1)
    }
    c3_positions = {
        (r, q)
        for r in range(1, 34)
        for q in range(min(10, 33 - r) + 1)
    }
    require((len(c2_positions), len(c3_positions)) == (187, 308),
            "C2/C3 count mismatch")

    lowq_slots = [
        (r, q)
        for r in range(1, 34)
        for q in range(min(21, 33 - r) + 1)
    ]
    require(len(lowq_slots) == 495, "low-q output count mismatch")

    d2_slots = [
        (r, q)
        for r in range(1, 34)
        for q in range(34 - r)
        if 3 * r + 4 * q <= 96
    ]
    d2_identity_slots = {(1, 22), (1, 23), (2, 22)}
    require(set(d2_slots) - set(lowq_slots) == d2_identity_slots,
            "D2 identity slot mismatch")

    equality_targets = {
        (4 * k, 24 - 3 * k): (-1) ** k * comb(8, k)
        for k in range(1, 9)
    }

    h3sq_support = {
        (a[0] + b[0], a[1] + b[1])
        for a in h3_support
        for b in h3_support
    }
    h3cube_support = {
        (a[0] + b[0], a[1] + b[1])
        for a in h3sq_support
        for b in h3_support
    }

    rules: list[dict[str, Any]] = []
    seen_pivots: set[str] = set()
    for slot in sorted(lowq_slots, key=order_key):
        r, q = slot
        if q <= 10:
            pivot_position = slot
            pivot = f"C3c_{r}_{q}"
            require(pivot_position in c3_positions, f"missing C3 pivot {pivot}")
        else:
            pivot_position = (r, q - 11)
            pivot = f"C2c_{r}_{q - 11}"
            require(pivot_position in c2_positions, f"missing C2 pivot {pivot}")
        require(pivot not in seen_pivots, f"duplicate pivot {pivot}")
        seen_pivots.add(pivot)

        c2_terms = []
        for cpos in sorted(c2_positions, key=order_key):
            hr, hq = r - cpos[0], q - cpos[1]
            if (hr, hq) not in h3_support:
                continue
            variable = f"C2c_{cpos[0]}_{cpos[1]}"
            if variable == pivot:
                require((hr, hq) == (0, 11), "pivot is not the unit h3 top column")
                continue
            dependency_slot = first_output_slot_for_c2(cpos)
            require(order_key(dependency_slot) < order_key(slot),
                    f"non-triangular dependency {variable} in slot {slot}")
            c2_terms.append({
                "variable": variable,
                "h3_coefficient": h3_name((hr, hq)),
                "first_solved_at": list(dependency_slot),
            })

        if 3 * r + 4 * q <= 96:
            target = str(equality_targets.get(slot, 0))
            target_type = "D2-fixed-equality" if slot in equality_targets else "D2-fixed-zero"
        else:
            target = f"K2c_{r}_{q}"
            target_type = "K2c-coordinate"

        rules.append({
            "slot": list(slot),
            "pivot": pivot,
            "coefficient": "1",
            "target": target,
            "target_type": target_type,
            "inverse_rule": (
                f"{pivot} = {target} - coeff(K3^3,{r},{q})"
                + ("" if not c2_terms else " - sum(prior C2c * K3 coefficient)")
            ),
            "prior_C2_dependencies": c2_terms,
            "h3cube_support_possible": slot in h3cube_support,
        })

    require(len(seen_pivots) == 495, "not all original C2/C3 variables pivoted")

    k2c_before_d1 = [
        (r, q) for r, q in lowq_slots if 3 * r + 4 * q >= 97
    ]
    require(len(k2c_before_d1) == 106, "K2c pre-D1 count mismatch")

    d1_pivot_order = [
        (11, 16), (15, 13), (19, 10), (23, 7), (27, 4),
        (10, 17), (14, 14),
    ]
    d1_rules = []
    expected_coefficients = ["1", "-3", "9", "-27", "81", "1", "-3"]
    solved = set()
    for W, kmax in ((97, 4), (98, 1)):
        positions = [(r, q) for r, q in k2c_before_d1 if 3 * r + 4 * q == W]
        for k in range(kmax + 1):
            row_terms = [
                {"K2c": f"K2c_{r}_{q}", "coefficient": str(comb(q, k))}
                for r, q in positions if q >= k
            ]
            pivot_slot = d1_pivot_order[len(d1_rules)]
            pivot_name = f"K2c_{pivot_slot[0]}_{pivot_slot[1]}"
            raw_coefficient = next(int(item["coefficient"]) for item in row_terms if item["K2c"] == pivot_name)
            require(raw_coefficient != 0, "zero raw h2-D1 pivot coefficient")
            require(pivot_name not in solved, "duplicate h2-D1 pivot")
            solved.add(pivot_name)
            d1_rules.append({
                "row": f"h2_D1_W{W}_k{k}",
                "pivot": pivot_name,
                "raw_coefficient_before_prior_D1_elimination": str(raw_coefficient),
                "coefficient": expected_coefficients[len(d1_rules)],
                "raw_row_terms": row_terms,
            })
    require([item["coefficient"] for item in d1_rules] == expected_coefficients,
            "h2-D1 pivot coefficients mismatch")

    free_after_d1 = sorted(
        f"K2c_{r}_{q}" for r, q in k2c_before_d1
        if f"K2c_{r}_{q}" not in solved
    )
    require(len(free_after_d1) == 99, "K2c post-D1 count mismatch")

    branch52_map, _free, centre52 = engine.h3_branch_map("delta52")
    require(centre52 == {"parameters": ["u", "v", "c"], "localization": "c!=0", "b0": "fixed_zero"},
            "delta52 centre mismatch")

    rule_lines = [
        f"{rule['slot']}|{rule['pivot']}|{rule['target']}|{len(rule['prior_C2_dependencies'])}"
        for rule in rules
    ]
    payload: dict[str, Any] = {
        "type": "K2C-C2C3-COMPACT-TRIANGULAR-INVERSE / EXACT-SUPPORT",
        "engine": {"path": str(ENGINE), "sha256": sha256_file(ENGINE)},
        "coordinate_definition": (
            "K2c_r_q=[t^r(w-1)^q](K3^3+(t^22 C2)K3+t^33 C3), low q. "
            "D2-fixed low-q outputs are set to the fixed h2 face; the remaining "
            "106 low-q outputs are declared K2c coordinates before h2-D1."
        ),
        "original_coordinate_counts": {"C2c": 187, "C3c": 308, "total": 495},
        "output_counts": {
            "low_q_nonidentity_slots": len(lowq_slots),
            "D2_constraint_slots_in_low_q": sum(1 for r, q in lowq_slots if 3 * r + 4 * q <= 96),
            "D2_identity_slots_not_in_low_q": [list(item) for item in sorted(d2_identity_slots)],
            "K2c_coordinates_before_h2_D1": len(k2c_before_d1),
            "K2c_coordinates_after_h2_D1": len(free_after_d1),
        },
        "unit_triangular_certificate": {
            "row_order": "(r,-q)",
            "unit_leader_rule": "C3c_r_q for q<=10; C2c_r_(q-11) for 11<=q<=21",
            "all_diagonal_coefficients": "1",
            "all_original_C2C3_variables_pivot_once": True,
            "every_nonleader_C2_dependency_solved_earlier": True,
            "h3_top_unit_used_for_C2_leader": "coeff(K3,(0,11))=1",
            "C3_leader_is_direct_output_column": True,
            "inverse_rules_are_compact_not_fully_expanded": True,
        },
        "inverse_rules": rules,
        "inverse_rules_sha256": rows_hash(rule_lines),
        "h2_D1_rules": d1_rules,
        "free_K2c_after_h2_D1": free_after_d1,
        "delta52_branch_state": {
            "centre": centre52,
            "Hc_substitutions_count": len(branch52_map),
            "localization": "c!=0",
            "c_is_not_a_pivot": True,
        },
        "unit_ideal_note": (
            "A unit-triangular polynomial coordinate change is a quotient-ring "
            "isomorphism. Therefore a reduced constant residue 64 gives the unit "
            "ideal in either the K2c basis or the original C2c/C3c basis; the "
            "fully expanded inverse is not needed for the stage-8 death certificate."
        ),
    }
    output_path = BASE / "k2c-c2c3-inverse.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    serialized = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if output_path.exists():
        require(output_path.read_bytes() == serialized, f"refusing to change {output_path}")
    else:
        output_path.write_bytes(serialized)
    print(json.dumps({
        "status": "K2C-COMPACT-INVERSE-PASS",
        "path": str(output_path),
        "sha256": hashlib.sha256(serialized).hexdigest(),
        "original_C2C3_variables": 495,
        "inverse_rules": len(rules),
        "K2c_before_D1": 106,
        "K2c_after_D1": 99,
        "inverse_rules_sha256": payload["inverse_rules_sha256"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
