#!/usr/bin/env python3
"""Reproducible checks for Moh's (99,66) radius-two B/C analysis.

This driver deliberately distinguishes three systems:

* A is the charged 14-unknown A/B predecessor control for Moh's transformed
  linear-power row.  It is rebuilt here without importing the earlier,
  uncharged helper.
* B is the necessary leading-coefficient ODE on the two-root cubic stratum.
* C is a necessary reduced consequence of the same ODE on the squarefree
  cubic stratum.

The B system is not Moh's omitted eleven-variable full coefficient system.
Its nonempty result must therefore not be read as a Keller-pair witness.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import shutil
import subprocess
import time
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "box" / "moh9966B-20260903"
SYSTEMS_DIR = OUT / "systems"
LOGS_DIR = OUT / "logs"
RESULT_PATH = OUT / "moh9966B_results.json"
RECEIPT = ROOT / "xmodel" / "moh9966-branchB-sol56-20260903.run.v2"
PRIMES = (32003, 32009, 32027)
CHARACTERISTICS = PRIMES + (0,)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def receipt_manifest_check() -> dict:
    """Read both filenames and hashes from the receipt; retype neither."""
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    input_dir = Path(fields["lane_inputs_dir"])
    count = int(fields["charged_inputs"])
    rows = []
    for index in range(1, count + 1):
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        path = input_dir / basename
        got = sha256_file(path) if path.is_file() else None
        rows.append(
            {
                "index": index,
                "basename": basename,
                "path": str(path),
                "expected": expected,
                "got": got,
                "ok": got == expected,
            }
        )
    manifest_path = OUT / "charged-inputs.sha256"
    manifest_path.write_text(
        "".join(f"{row['expected']}  {row['path']}\n" for row in rows)
    )
    return {
        "method": "receipt fields parsed mechanically; SHA-256 recomputed",
        "receipt": str(RECEIPT),
        "input_dir": str(input_dir),
        "ok": all(row["ok"] for row in rows),
        "rows": rows,
        "manifest": str(manifest_path.relative_to(ROOT)),
    }


def jacobian(first: sp.Expr, second: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(
        sp.diff(first, x) * sp.diff(second, y)
        - sp.diff(first, y) * sp.diff(second, x)
    )


def singular_expr(expr: sp.Expr) -> str:
    numerator, denominator = sp.fraction(sp.together(sp.expand(expr)))
    numerator = sp.expand(numerator)
    denominator = sp.expand(denominator)
    if denominator == 1:
        text = str(numerator)
    elif denominator == -1:
        text = str(-numerator)
    else:
        text = f"({numerator})/({denominator})"
    return text.replace("**", "^")


def coefficient_equations(poly: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> list[sp.Expr]:
    return [sp.expand(value) for value in sp.Poly(sp.expand(poly), x, y).coeffs() if value != 0]


def hadic_jacobian_equations(
    h: sp.Expr,
    low_terms: list[tuple[sp.Expr, int]],
    high_terms: list[tuple[sp.Expr, int]],
    c: sp.Symbol,
    x_power: int,
    x: sp.Symbol,
    y: sp.Symbol,
) -> tuple[list[sp.Expr], list[int]]:
    """Extract J(low,high) by powers of a monic polynomial h.

    A term is represented as (coefficient, h-exponent).  Euclidean division
    in Q(parameters,x)[y] carries every quotient to the next h-adic level.
    """
    by_power: dict[int, sp.Expr] = {}
    for aa, r_power in low_terms:
        for bb, s_power in high_terms:
            value = jacobian(aa, bb, x, y)
            if value != 0:
                by_power[r_power + s_power] = by_power.get(r_power + s_power, 0) + value
            value = (
                s_power * bb * jacobian(aa, h, x, y)
                + r_power * aa * jacobian(h, bb, x, y)
            )
            if value != 0:
                level = r_power + s_power - 1
                by_power[level] = by_power.get(level, 0) + value

    by_power.setdefault(0, sp.Integer(0))
    level = 0
    largest = max(by_power)
    while level <= largest:
        remainder = sp.expand(by_power.get(level, 0))
        if remainder != 0:
            quotient, residue = sp.div(sp.Poly(remainder, y), sp.Poly(h, y), y)
            by_power[level] = sp.expand(residue.as_expr())
            if quotient != 0:
                by_power[level + 1] = by_power.get(level + 1, 0) + sp.expand(quotient.as_expr())
                largest = max(largest, level + 1)
        level += 1

    by_power[0] = sp.expand(by_power[0] - c * x**x_power)
    equations: list[sp.Expr] = []
    nonzero_levels: list[int] = []
    for level in sorted(by_power):
        remainder = sp.expand(by_power[level])
        if remainder == 0:
            continue
        nonzero_levels.append(level)
        equations.extend(coefficient_equations(remainder, x, y))
    return equations, nonzero_levels


def branch_a_predecessor() -> dict:
    """Rebuild the charged 13-shape-variable plus c predecessor."""
    x, y = sp.symbols("x y")
    h_parameters = list(
        sp.symbols("h_0_8 h_0_7 h_0_6 h_0_5 h_0_4 h_0_3 h_0_2 h_0_1 h_0_0")
    )
    h = y**8 * (y - x)
    for parameter, y_power in zip(h_parameters, range(8, -1, -1)):
        h += parameter * y**y_power
    bp, bq, br, bs, c, T = sp.symbols("bp bq br bs c T")
    A = sp.cancel((h - h.subs(y, 0)) / y)
    beta = sp.expand(bp * A + bq * y + br * x + bs)
    quotient, _ = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
    alpha = sp.expand(quotient.as_expr())
    low_terms = [(sp.Integer(1), 2), (2 * beta, 0)]
    high_terms = [
        (sp.Integer(1), 3),
        (3 * beta, 1),
        (sp.Rational(3, 2) * alpha, 0),
    ]
    equations, levels = hadic_jacobian_equations(
        h, low_terms, high_terms, c, 4, x, y
    )
    raw_f = sp.expand(h**2 + 2 * beta)
    raw_g = sp.expand(h**3 + 3 * beta * h + sp.Rational(3, 2) * alpha)
    raw_equations = coefficient_equations(jacobian(raw_f, raw_g, x, y) - c * x**4, x, y)
    assert len(equations) == 29
    assert len(raw_equations) == 36
    assert equations[0] == -c
    parameters = h_parameters + [bp, bq, br, bs, c]
    return {
        "name": "A_CONTROL_PREDECESSOR",
        "parameters": parameters,
        "T": T,
        "factor": c,
        "equations": equations,
        "levels": levels,
        "raw_equation_count": len(raw_equations),
        "certificate": "1 = -(T*c-1) - T*(-c)",
        "certificate_terms": 2,
        "certificate_max_multiplier_degree": 1,
    }


def branch_b_ode() -> dict:
    z = sp.Symbol("z")
    a, k, q3, q2, q1, q0, T = sp.symbols("a k q3 q2 q1 q0 T")
    H = z**2 * (z + 3 * a)
    q = z**4 + q3 * z**3 + q2 * z**2 + q1 * z + q0
    ode = sp.expand(2 * H * sp.diff(q, z) - sp.diff(H, z) * q - k * H**2)
    raw = [sp.expand(ode.coeff(z, degree)) for degree in range(6, 0, -1)]
    assert raw[-1] == sp.expand(2 * a * raw[-2])
    equations = raw[:-1]

    witness = {a: 1, k: 5, q3: 4, q2: -3, q1: -18, q0: 0, T: sp.Rational(1, 5)}
    H_w = sp.expand(H.subs(witness))
    q_w = sp.expand(q.subs(witness))
    R_w = sp.expand(H_w**12 * q_w)
    full_ode = sp.expand(2 * H_w * sp.diff(R_w, z) - 25 * sp.diff(H_w, z) * R_w - 5 * H_w**14)
    assert full_ode == 0
    assert all(sp.expand(eq.subs(witness)) == 0 for eq in equations)

    x, y = sp.symbols("x y")
    zxy = x * y
    t3_face = y**25 * (zxy + 3) ** 14 * (zxy - 2)
    g_face = y**18 * (zxy + 3) ** 9
    face_jac = sp.factor(jacobian(t3_face, g_face, x, y))
    expected_face_jac = 45 * x * y**44 * (zxy + 3) ** 22
    assert sp.expand(face_jac - expected_face_jac) == 0

    return {
        "name": "B_TWO_ROOT_REDUCED_ODE",
        "logical_premise": (
            "p.209 x^15*y^40 is the radius-two T3 leader; explicit in the "
            "task, not proved by Moh's unspecified ellipsis"
        ),
        "parameters": [a, k, q3, q2, q1, q0],
        "T": T,
        "factor": a * k,
        "equations": equations,
        "raw_equations": raw,
        "dropped_redundant": str(sp.Eq(raw[-1], 2 * a * raw[-2])),
        "witness": {
            "a": 1,
            "k": 5,
            "q3": 4,
            "q2": -3,
            "q1": -18,
            "q0": 0,
            "T": "1/5",
            "H": str(H_w),
            "q": str(sp.factor(q_w)),
            "R": str(sp.factor(R_w)),
            "full_ode_remainder": str(full_ode),
            "bivariate_face_jacobian": str(face_jac),
            "bivariate_face_jacobian_expected": str(expected_face_jac),
            "type": "REPRESENTATIVE[PRINTED-LEADER-ODE-FACE], not a Keller pair",
        },
    }


def branch_c_consequence() -> dict:
    z = sp.Symbol("z")
    a, b, ell, k, T = sp.symbols("a b ell k T")
    H = z * (z - a) * (z - b)
    L = z + ell
    consequence = sp.expand(sp.diff(H, z) * L + 2 * H * sp.diff(L, z) - k * H)
    equations = [sp.expand(consequence.coeff(z, degree)) for degree in range(3, -1, -1)]

    symmetric_sum = a + b
    symmetric_product = a * b
    difference = a - b
    f1, f2, f3, f4 = equations
    f5 = T * symmetric_product * difference * k - 1
    multipliers = [
        T * difference * k * (symmetric_product / 2 - ell * symmetric_sum),
        -T * difference * k * ell,
        -T * difference * k / 2,
        3 * T**2 * difference**2 * k**2 * ell,
        -3 * T * difference * k * ell**2 - 1,
    ]
    certificate_remainder = sp.expand(
        multipliers[0] * f1
        + multipliers[1] * f2
        + multipliers[2] * f3
        + multipliers[3] * f4
        + multipliers[4] * f5
        - 1
    )
    assert certificate_remainder == 0
    degenerate = {a: 0, b: 0, ell: 0, k: 5}
    assert all(sp.expand(eq.subs(degenerate)) == 0 for eq in equations)
    return {
        "name": "C_THREE_SIMPLE_REDUCED_CONSEQUENCE",
        "logical_premise": (
            "p.209 x^15*y^40 is the radius-two T3 leader; explicit in the "
            "task, not proved by Moh's unspecified ellipsis"
        ),
        "parameters": [a, b, ell, k],
        "T": T,
        "factor": a * b * (a - b) * k,
        "equations": equations,
        "certificate": {
            "identity_remainder": str(certificate_remainder),
            "terms": 5,
            "max_multiplier_total_degree": max(
                sp.Poly(multiplier, a, b, ell, k, T).total_degree()
                for multiplier in multipliers
            ),
            "multipliers": [str(value) for value in multipliers],
        },
        "unsaturated_degenerate_point": {"a": 0, "b": 0, "ell": 0, "k": 5},
    }


def clean_name(symbol: sp.Symbol) -> str:
    name = re.sub(r"[^A-Za-z0-9_]+", "_", str(symbol)).strip("_")
    return name if name and not name[0].isdigit() else f"v{name}"


def singular_script(spec: dict, characteristic: int) -> tuple[str, dict[sp.Symbol, sp.Symbol]]:
    parameters = list(spec["parameters"])
    T = spec["T"]
    symbols = parameters + [T]
    names: list[str] = []
    rename: dict[sp.Symbol, sp.Symbol] = {}
    for symbol in symbols:
        base = clean_name(symbol)
        name = base
        suffix = 1
        while name in names:
            suffix += 1
            name = f"{base}_{suffix}"
        names.append(name)
        rename[symbol] = sp.Symbol(name)
    equations = [sp.expand(eq.subs(rename)) for eq in spec["equations"]]
    factor = sp.expand(spec["factor"].subs(rename))
    t_name = rename[T]

    # Explicit nonempty wrapper-control points; they test only the wrapper.
    if spec["name"].startswith("C_"):
        control_values = {"a": "1", "b": "2", "k": "1", "T": "-1/2"}
    else:
        first_name = clean_name(parameters[0])
        control_values = {first_name: "1", "T": "1"}
        if "k" in names:
            control_values["k"] = "1"
        if spec["name"].startswith("A_"):
            control_values = {"c": "1", "T": "1"}
    control_generators = [f"{name}-({value})" for name, value in control_values.items()]

    equation_text = ",\n  ".join(singular_expr(eq) for eq in equations)
    main_generators = equation_text + f",\n  {t_name}*({singular_expr(factor)})-1"
    text = f"""// {spec['name']}; characteristic {characteristic}
ring R={characteristic},({','.join(names)}),dp;
option(redSB);
print(\"RING_BEGIN\"); R; print(\"RING_END\");
ideal CE={singular_expr(factor)},{t_name}*({singular_expr(factor)})-1;
ideal GCE=std(CE);
if (reduce(1,GCE)==0) {{ print(\"CONTROL_EMPTY_PASS\"); }} else {{ print(\"CONTROL_EMPTY_FAIL\"); }}
ideal CN={','.join(control_generators)};
ideal GCN=std(CN);
if (reduce(1,GCN)!=0) {{ print(\"CONTROL_NONEMPTY_PASS\"); }} else {{ print(\"CONTROL_NONEMPTY_FAIL\"); }}
ideal E=
  {equation_text};
ideal GU=std(E);
if (reduce(1,GU)!=0) {{ print(\"UNSATURATED_NONUNIT_PASS\"); }} else {{ print(\"UNSATURATED_NONUNIT_FAIL\"); }}
ideal I=
  {main_generators};
ideal G=std(I);
print(\"GENERATOR_COUNT\"); size(E);
print(\"EXTENDED_GENERATOR_COUNT\"); size(I);
print(\"BASIS_SIZE\"); size(G);
print(\"BASIS_BEGIN\"); G; print(\"BASIS_END\");
if (reduce(1,G)==0) {{ print(\"MAIN_SATURATED_EMPTY\"); }} else {{ print(\"MAIN_NONUNIT\"); }}
quit;
"""
    return text, rename


def parse_singular_output(output: str) -> dict:
    lines = [line.strip() for line in output.splitlines()]

    def after(label: str) -> str | None:
        try:
            return lines[lines.index(label) + 1]
        except (ValueError, IndexError):
            return None

    try:
        begin = lines.index("BASIS_BEGIN") + 1
        end = lines.index("BASIS_END")
        basis = lines[begin:end]
    except ValueError:
        basis = []
    if "MAIN_SATURATED_EMPTY" in lines:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONUNIT" in lines:
        verdict = "NONUNIT"
    else:
        verdict = "ERROR"
    controls = {
        "empty_wrapper": "CONTROL_EMPTY_PASS" in lines,
        "nonempty_wrapper": "CONTROL_NONEMPTY_PASS" in lines,
        "unsaturated_nonunit": "UNSATURATED_NONUNIT_PASS" in lines,
    }
    if not all(controls.values()):
        verdict = "CONTROL-FAIL"
    return {
        "verdict": verdict,
        "controls": controls,
        "generator_count": after("GENERATOR_COUNT"),
        "extended_generator_count": after("EXTENDED_GENERATOR_COUNT"),
        "basis_size": after("BASIS_SIZE"),
        "basis": basis,
    }


def run_system(spec: dict, characteristic: int, timeout_seconds: int = 120) -> dict:
    label = "Q" if characteristic == 0 else str(characteristic)
    stem = spec["name"].lower()
    script_path = SYSTEMS_DIR / f"{stem}_{label}.sing"
    log_path = LOGS_DIR / f"{stem}_{label}.log"
    text, rename = singular_script(spec, characteristic)
    script_path.write_text(text)
    started = time.perf_counter()
    try:
        process = subprocess.run(
            ["Singular", "-q", "--no-rc", str(script_path)],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        elapsed = time.perf_counter() - started
        output = (process.stdout or "") + (process.stderr or "")
        log_path.write_text(output)
        record = parse_singular_output(output)
        record.update({"returncode": process.returncode})
        if process.returncode != 0:
            record["verdict"] = "ERROR"
    except subprocess.TimeoutExpired as error:
        elapsed = time.perf_counter() - started
        stdout = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else (error.stdout or "")
        stderr = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else (error.stderr or "")
        output = stdout + stderr
        log_path.write_text(output)
        record = {"verdict": "TIMEOUT", "controls": {}, "basis": []}
    record.update(
        {
            "characteristic": characteristic,
            "elapsed_seconds": round(elapsed, 6),
            "timeout_seconds": timeout_seconds,
            "script": str(script_path.relative_to(ROOT)),
            "log": str(log_path.relative_to(ROOT)),
            "script_sha256": sha256_file(script_path),
            "ring_variables": [str(rename[symbol]) for symbol in list(spec["parameters"]) + [spec["T"]]],
        }
    )
    return record


def ceil_fraction(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def two_arc_dimension(D: int, minor_order: int, major_s_order: int, omega_polynomial: bool, strict: bool) -> int:
    total = 0
    bump = 1 if strict else 0
    for x_degree in range(D + 1):
        minor_vanish = max(0, ceil_fraction(minor_order + bump - x_degree, 3))
        if omega_polynomial:
            minor_vanish = max(
                minor_vanish,
                0,
                ceil_fraction(D + bump - x_degree, 4),
            )
        major_vanish = max(0, ceil_fraction(major_s_order + bump - 3 * x_degree, 4))
        cap = D - x_degree
        total += max(0, cap - minor_vanish - major_vanish + 1)
    return total


def envelope_site_count(D: int, local_order: int, x_floor: int | None) -> int:
    count = 0
    for y_degree in range(D + 1):
        lower = max(y_degree + local_order, 4 * y_degree - D)
        if x_floor is not None:
            lower = max(x_floor, lower)
        upper = 2 * D + y_degree
        count += max(0, upper - lower + 1)
    return count


def shape_counts() -> dict:
    h_rows = []
    for x_degree in range(12):
        cap = 11 - x_degree
        minor_vanish = max(0, ceil_fraction(9 - x_degree, 3))
        major_vanish = max(0, ceil_fraction(32 - 3 * x_degree, 4))
        dimension = max(0, cap - minor_vanish - major_vanish + 1)
        if dimension:
            h_rows.append(
                {
                    "x_degree": x_degree,
                    "w_degree_cap": cap,
                    "w_zero_vanishing": minor_vanish,
                    "w_one_vanishing": major_vanish,
                    "dimension": dimension,
                    "basis": f"x^{x_degree}*w^{minor_vanish}*(w-1)^{major_vanish}",
                }
            )
    assert len(h_rows) == 9
    raw_original = {
        "f_monic_free": (67 * 68) // 2 - 1,
        "g_monic_free": (100 * 101) // 2 - 1,
    }
    raw_original["total"] = raw_original["f_monic_free"] + raw_original["g_monic_free"]
    result = {
        "straightened_two_arc_h": {
            "linear_dimension": sum(row["dimension"] for row in h_rows),
            "affine_free_after_monic": sum(row["dimension"] for row in h_rows) - 1,
            "rows": h_rows,
            "branch_B_after_double_root_and_Omega_polynomiality_free": 5,
            "branch_B_open_condition": "c3 != 0",
            "surviving_indices": [3, 4, 7, 8, 11],
            "type": "GAUGE-SLICE; literal a0,a1,a2 straightening is not proved by p.209",
        },
        "individual_P_spaces_in_zero_jet_slice": {
            "without_Omega_polynomiality": {
                "f": two_arc_dimension(66, 54, 192, False, False),
                "g": two_arc_dimension(99, 81, 288, False, False),
            },
            "with_Omega_polynomiality": {
                "f": two_arc_dimension(66, 54, 192, True, False),
                "g": two_arc_dimension(99, 81, 288, True, False),
            },
            "strict_interior_preserving_all_faces": {
                "f": two_arc_dimension(66, 54, 192, True, True),
                "g": two_arc_dimension(99, 81, 288, True, True),
            },
            "type": "COUNTING-BOUND on separate f,g shapes, before approximate-root/Jacobian equations",
        },
        "maximal_envelope_support_sites": {
            "raw_Laurent_from_forward_polynomiality_and_two_faces": {
                "f": envelope_site_count(66, -12, None),
                "g": envelope_site_count(99, -18, None),
                "T2": envelope_site_count(55, -10, None),
                "T3": envelope_site_count(145, -25, None),
            },
            "Omega_polynomial_slice": {
                "f": envelope_site_count(66, -12, 0),
                "g": envelope_site_count(99, -18, 0),
                "T2": envelope_site_count(55, -10, 0),
                "T3": envelope_site_count(145, -25, 0),
            },
            "branch_C_forced_face_minimum_x_only": {"f": -6, "g": -9, "T2": -5},
            "type": (
                "support-site counts, not independent coefficient counts; "
                "forced-face minima are not full-support lower bounds"
            ),
        },
        "raw_original_coefficient_count": raw_original,
    }
    assert result["individual_P_spaces_in_zero_jet_slice"]["with_Omega_polynomiality"] == {"f": 103, "g": 217}
    assert result["individual_P_spaces_in_zero_jet_slice"]["strict_interior_preserving_all_faces"] == {"f": 68, "g": 165}
    assert result["maximal_envelope_support_sites"]["raw_Laurent_from_forward_polynomiality_and_two_faces"] == {"f": 6187, "g": 13816, "T2": 4316, "T3": 29441}
    assert result["maximal_envelope_support_sites"]["Omega_polynomial_slice"] == {"f": 6109, "g": 13645, "T2": 4261, "T3": 29116}
    return result


def orientation_controls() -> dict:
    x, y, a0, a1, a2 = sp.symbols("x y a0 a1 a2")
    old_x = x**-1
    old_y = a0 + a1 * x + a2 * x**2 + x**3 * y
    determinant = jacobian(old_x, old_y, x, y)
    j_x = jacobian(x**2 / 2, y, x, y)
    j_x4 = jacobian(x**5 / 5, y, x, y)
    assert determinant == -x
    assert j_x == x and j_x4 == x**4
    return {
        "det_DPhi": str(determinant),
        "if_original_J_is_c": "J(Omega(f),Omega(g))=-c*x",
        "Moh_J_equals_x_requires": "c=-1 (or an equivalent sign normalization)",
        "positive_control_J_x": str(j_x),
        "positive_control_J_x4": str(j_x4),
    }


def serializable_spec(spec: dict) -> dict:
    result = {}
    for key, value in spec.items():
        if key in {"parameters"}:
            result[key] = [str(item) for item in value]
        elif key in {"T", "factor"}:
            result[key] = str(value)
        elif key in {"equations", "raw_equations"}:
            result[key] = [str(item) for item in value]
        else:
            result[key] = value
    return result


def write_artifact_hashes() -> None:
    paths = sorted(
        path for path in OUT.rglob("*")
        if path.is_file()
        and path.name != "artifacts.sha256"
        and "__pycache__" not in path.parts
    )
    (OUT / "artifacts.sha256").write_text(
        "".join(f"{sha256_file(path)}  {path.relative_to(ROOT)}\n" for path in paths)
    )


def main() -> None:
    if shutil.which("Singular") is None:
        raise SystemExit("Singular is required")
    OUT.mkdir(parents=True, exist_ok=True)
    SYSTEMS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    manifest = receipt_manifest_check()
    if not manifest["ok"]:
        raise SystemExit("charged-input SHA-256 mismatch")

    specs = [branch_a_predecessor(), branch_b_ode(), branch_c_consequence()]
    records = []
    for spec in specs:
        runs = [run_system(spec, characteristic) for characteristic in CHARACTERISTICS]
        records.append({"system": serializable_spec(spec), "runs": runs})

    result = {
        "manifest_check": manifest,
        "software": {
            "python": subprocess.run(
                ["python3", "--version"], capture_output=True, text=True, check=False
            ).stdout.strip(),
            "sympy": sp.__version__,
            "singular": subprocess.run(
                ["Singular", "--version"], capture_output=True, text=True, check=False
            ).stdout.splitlines()[0],
        },
        "cores_used_by_driver": 1,
        "execution": "serial",
        "per_run_timeout_seconds": 120,
        "primes": list(PRIMES),
        "orientation_controls": orientation_controls(),
        "shape_counts": shape_counts(),
        "systems": records,
    }
    RESULT_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    write_artifact_hashes()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
