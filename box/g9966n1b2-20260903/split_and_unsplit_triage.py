#!/usr/bin/env python3
"""Exact split-face checks and corrected unsplit-system specifications."""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b2-20260903"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


driver = load("n1b2_lane_driver_for_triage", HERE / "lane_driver.py")
ob = driver.ob


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def qstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def detector_orders(u: int, v: int) -> list[F]:
    if u < 2:
        return []
    ceiling = F(v, u)
    result = set()
    for den in range(1, u + 1):
        for num in range(den + 1, 10 * v + 1):
            value = F(num, den)
            if value >= ceiling:
                break
            if gcd(num, den) == 1:
                result.add(value)
    return sorted(result)


def partitions(total: int, cap: int | None = None):
    if total == 0:
        yield ()
        return
    high = total if cap is None else min(total, cap)
    for first in range(high, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def mu_data(M: list[int], d: list[int]) -> list[F]:
    total = 0
    values = []
    for index in range(len(M)):
        increment = M[index] if index == 0 else M[index] - M[index - 1]
        total += increment * d[index]
        values.append(F(total, d[index]))
    return values


def ode_residual(u: int, v: int, W: int, delta: F, p, q, z):
    X = F(u) * delta - F(v)
    b = 9 * X
    a = W * X - 1 + delta
    return sp.factor(
        9 * sp.Rational(a.numerator, a.denominator) * q * sp.diff(p, z)
        - sp.Rational(b.numerator, b.denominator) * sp.diff(q, z) * p
        - 9 * (v - u) * p ** (W + 1)
    ), a, b


def face_charts():
    z, c, C, a0 = sp.symbols("z c C a")
    definitions = {
        "S1": [
            (F(4), [1, 1], z * (z - c), lambda p: p**28 * (C + 7 * sp.integrate(p**3, z)), 31, 2, 9, "localize c"),
        ],
        "S2": [
            (F(3, 2), [2, 2], (z**2 - c)**2, lambda p: (z**2 - c)**45 * (C + z**3 - 3*c*z), 23, 4, 7, "localize c"),
            (F(3, 2), [2, 1, 1], z**2 * (z**2 - c), lambda p: z**45 * (z**2-c)**24, 23, 4, 7, "localize c"),
            (F(5, 3), [1, 1, 1, 1], z * (z**3 - c), lambda p: p**21 * (C + z**9 - 3*c*z**6 + 3*c**2*z**3), 23, 4, 7, "localize c"),
        ],
        "S3": [],
        "S4": [
            (F(2), [2, 1], z**2 * (z + 3*a0), lambda p: z**45 * (z+3*a0)**24 * (z-2*a0), 23, 3, 8, "localize a"),
            (F(5, 2), [1, 1, 1], z * (z**2-c), lambda p: p**20 * (C + 10*sp.integrate(p**3, z)), 23, 3, 8, "localize c"),
        ],
        "S7": [
            (F(3, 2), [2, 2], (z**2-c)**2, lambda p: (z**2-c)**25 * (C+z**3-3*c*z), 13, 4, 7, "localize c"),
            (F(3, 2), [2, 1, 1], z**2*(z**2-c), lambda p: z**25*(z**2-c)**14, 13, 4, 7, "localize c"),
            (F(5, 3), [1, 1, 1, 1], z*(z**3-c), lambda p: p**11*(C+z**9-3*c*z**6+3*c**2*z**3), 13, 4, 7, "localize c"),
        ],
    }
    definitions["S3"] = definitions["S2"]
    output = {}
    for name, charts in definitions.items():
        records = []
        for delta, part, p, q_builder, W, u, v, localization in charts:
            q = sp.factor(q_builder(p))
            residual, aa, bb = ode_residual(u, v, W, delta, p, q, z)
            if residual != 0:
                raise AssertionError((name, delta, part, residual))
            free = sorted(str(symbol) for symbol in (p.free_symbols | q.free_symbols) - {z})
            records.append({
                "delta": qstr(delta),
                "partition": part,
                "p": str(sp.factor(p)),
                "q": str(q),
                "W": W,
                "degree_p": int(sp.degree(p, z)),
                "degree_q": int(sp.degree(q, z)),
                "a_order": qstr(aa),
                "b_order": qstr(bb),
                "ode_residual": "0",
                "free_face_parameters": free,
                "localization": localization,
                "solver_parameter_count_with_Rabinowitsch": len(free) + 1,
                "scope": "exact necessary split-face parametrization; not a joint two-point chart",
            })
        output[name] = records
    return output


def unsplit_specs(enumeration):
    row_by_id = {row["id"]: row for row in enumeration["rows"]}
    row_estimates = {"S1": 352, "S2": 1558, "S3": 1044, "S4": 981, "S7": 1055}
    records = {}
    for name in ("S1", "S2", "S3", "S4", "S7"):
        row = driver.ROWS[name]
        C = ob.closed_form(row)
        one = ob.build_full_spec(row, (C["u"],))["meta"]
        parts = list(partitions(C["u"]))
        counts = {
            "+".join(map(str, part)): one["params_without_T"] + len(part) - 1
            for part in parts
        }
        records[name] = {
            "licensed_scope": "complement after exhaustive exclusion of every strict-below split chart",
            "prop63_requirement": f"actual delta*_2 >= {row_by_id[name]['v_s']}/{row_by_id[name]['u_s']}",
            "datum": {
                "n": row.n, "m": row.m, "M2": row.M2, "V2": row.V2,
                "ell": row.k, "K": C["K"], "u_prime": C["u"],
            },
            "closed_form": ob.serial_closed_form(C),
            "h_inventory": one["h_inventory"],
            "alpha_inventories": one["alpha_inventories"],
            "beta_inventories": one["beta_inventories"],
            "partitions": [list(part) for part in parts],
            "parameter_counts_without_T": counts,
            "parameter_count_range_without_T": [min(counts.values()), max(counts.values())],
            "predicted_generic_coefficient_rows": row_estimates[name],
            "row_count_scope": "generic-support prediction; only actual emitted rows are certificate rows",
            "exact_system": {
                "top_face": "h_top=y^V2*(y-x)^lambda1*Product_(j>=2)(y-s_j*x)^lambda_j",
                "h_lower_rule": "s<K, r+s<K, 0<=r<=u_prime, -r+delta1*s>=B",
                "coefficient_rule": "s<K, r+s<=j*K, -r+delta1*s>=j*B",
                "equations": "every x,y coefficient of the full h-adic remainder of J(Q,P)-c*x^ell",
                "localizer": "T*c*omega-1, omega=Product s_j(s_j-1) Product_(i<j)(s_i-s_j)",
                "field": "Q",
            },
        }
    return records


def main() -> None:
    enumeration = json.loads((HERE / "enumeration.json").read_text(encoding="utf-8"))
    by_id = {row["id"]: row for row in enumeration["rows"]}
    faces = face_charts()
    windows = {}
    survivors = {
        "S1": {"4": [[1, 1]]},
        "S2": {"3/2": [[2, 2], [2, 1, 1]], "5/3": [[1, 1, 1, 1]]},
        "S3": {"3/2": [[2, 2], [2, 1, 1]], "5/3": [[1, 1, 1, 1]]},
        "S4": {"2": [[2, 1]], "5/2": [[1, 1, 1]]},
        "S7": {"3/2": [[2, 2], [2, 1, 1]], "5/3": [[1, 1, 1, 1]]},
    }
    for name in ("S1", "S2", "S3", "S4", "S7"):
        u, v = by_id[name]["u_s"], by_id[name]["v_s"]
        values = detector_orders(u, v)
        windows[name] = {
            "ceiling": qstr(F(v, u)),
            "strict_window": f"1<delta<{qstr(F(v,u))}",
            "denominator_bound": u,
            "candidate_orders": [qstr(value) for value in values],
            "surviving_face_types": survivors[name],
            "branch_semantics": "a skeleton is not intrinsically split; listed charts plus their no-split complement are exhaustive duties",
        }

    mu = {name: [qstr(-value) for value in mu_data(by_id[name]["M"], by_id[name]["d"])] for name in by_id}
    payload = {
        "schema": "jc2.g9966n1b2.split-unsplit-triage/v1",
        "split_windows": windows,
        "split_face_charts": faces,
        "unsplit_corrected_order_systems": unsplit_specs(enumeration),
        "minus_mu": mu,
        "joint_chart_status": {
            "S1": {"F_box": [54, 12], "G_box": [81, 18], "T2_box": [126, 28], "F_G_coefficients_after_two_corner_pins": 2271},
            "S2": {"F_box": [42, 24], "G_box": [63, 36], "T2_box": [70, 40], "F_G_coefficients_after_two_corner_pins": 3441},
            "S3": {"F_box": [42, 24], "G_box": [63, 36], "T2_box": [70, 40], "F_G_coefficients_after_two_corner_pins": 3441},
            "S4": {"F_box": [48, 18], "G_box": [72, 27], "T2_box": [80, 30], "F_G_coefficients_after_two_corner_pins": 2973},
            "S7": {"F_box": [42, 24], "G_box": [63, 36], "T2_box": [35, 20], "F_G_coefficients_after_two_corner_pins": 3441},
            "scope": "starting Prop.6.2 boxes only; complete major-incidence/effective-T2/T3/Jacobian coupling unbuilt, so every split branch is OPEN",
        },
        "fallacy_controls": {
            "strict_below_separated_from_at_ceiling": True,
            "descent_applied_only_to_no_split_complement": True,
            "face_chart_not_called_joint_chart": True,
            "no_exit_price_assertion": True,
        },
    }
    output = HERE / "split-unsplit-triage.json"
    atomic_write(output, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "output": str(output.relative_to(ROOT)),
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "windows": {key: value["candidate_orders"] for key, value in windows.items()},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
