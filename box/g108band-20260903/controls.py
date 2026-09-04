#!/usr/bin/env python3
"""Exact-Q regression controls for the D=108 joint-band engine.

This driver is self-contained.  It mechanically re-instantiates the two
readings of Moh's Appendix-II (16,12) chart used by the frozen (99,66)
control, after first deriving (16,12) from its (64,48) parent.  The frozen
symbols ``kappa,T`` are renamed ``c,Zc`` so the control exercises the same
explicit Rabinowitsch convention as the D=108 branch.

For each Appendix-II reading Singular works over Q with dp ordering.  The
raw Jacobian-coefficient ideal has its c=0 origin; adjoining Zc*c-1 makes it
the unit ideal.  Empty- and point-wrapper controls, and an exact lift of 1,
are checked independently.  A tame affine two-point automorphism is checked
symbolically over Q as a positive plumbing control.

Only caller-selected output paths are written: two ``.sing`` replay files
and ``controls.json`` below ``--output-dir``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
from typing import Any

import sympy as sp


FROZEN_CONTROLS_SHA256 = (
    "cb616b8ee886097ace1f74a8f0c5307d1882f8a9ecd54742839577833f2f66a7"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_text(payload: str) -> str:
    return sha256_bytes(payload.encode("utf-8"))


def atomic_write(path: Path, payload: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def parent_reduction() -> dict[str, Any]:
    """Derive the p.208 control degrees from the frozen p.202 parent row."""
    n, m = 64, 48
    characteristic = (-m, 52, 62)
    divisors = [n]
    for value in characteristic:
        divisors.append(gcd(divisors[-1], value))
    require(divisors == [64, 16, 4, 2], "unexpected (64,48) divisor tower")

    s = 3
    values = {2: 3, 3: 3}
    # ``divisors`` is displayed as d_1,...,d_4, while Python is zero-based.
    d_s = divisors[s - 1]
    v_s = values[s]
    u_s = d_s - v_s
    require((d_s, v_s, u_s) == (4, 3, 1), "unexpected parent split data")
    require(n % d_s == 0 and m % d_s == 0, "nonintegral control descent")
    reduced = (n // d_s, m // d_s)
    require(reduced == (16, 12), "Appendix-II degree reduction mismatch")
    return {
        "parent_degrees": [n, m],
        "M_1_through_M_3": list(characteristic),
        "d_1_through_d_4": divisors,
        "V_2_V_3": [values[2], values[3]],
        "d_s": d_s,
        "v_s": v_s,
        "u_s": u_s,
        "descent_factor": d_s,
        "reduced_degrees": list(reduced),
        "bridge": "TRIVIAL[u_s=1]",
    }


def build_1612(repeated_c5: bool) -> dict[str, Any]:
    """Instantiate the frozen p.208 chart, with kappa,T renamed c,Zc."""
    x, y = sp.symbols("x y")
    b1, b2, b3, b4, a1 = sp.symbols("b1 b2 b3 b4 a1")
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols(
        "c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13"
    )
    c, Zc = sp.symbols("c Zc")

    h = y**3 * (y - x) + b1 * y**3 + b2 * y**2 + b3 * y + b4
    A = y**2 * (y - x) + b1 * y**2 + b2 * y + b3
    Bpoly = y * (y - x) + b1 * y + b2
    if repeated_c5:
        alpha3 = c5 * A + c5 * Bpoly + c7
        coefficient_generators = [
            b1, b2, b3, b4, a1,
            c1, c2, c3, c4, c5, c7, c8, c9, c10, c11, c12, c13,
        ]
        alpha1 = a1
        variant = "printed_repeated_c5"
    else:
        alpha3 = c5 * A + c6 * Bpoly + c7
        coefficient_generators = [
            b1, b2, b3, b4,
            c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13,
        ]
        alpha1 = sp.Integer(0)
        variant = "absorbed_alpha1_distinct_c6"

    alpha2 = c1 * A + c2
    beta2 = c3 * A + c4
    beta3 = c8 * A + c9 * Bpoly + c10
    alpha4 = c11 * A + c12 * Bpoly + c13 * (y - x)
    degree16 = sp.expand(h**4 + alpha1 * h**3 + alpha2 * h**2 + alpha3 * h + alpha4)
    degree12 = sp.expand(h**3 + beta2 * h + beta3)

    # Frozen control ordering is J(f_degree12,g_degree16)-kappa.  Thus this is
    # the negative of the main engine's J(F_degree16,G_degree12), immaterial
    # after localizing the otherwise free nonzero scalar c.
    jacobian_minus_c = sp.expand(
        sp.diff(degree12, x) * sp.diff(degree16, y)
        - sp.diff(degree12, y) * sp.diff(degree16, x)
        - c
    )
    ring_generators = coefficient_generators + [c, Zc]
    coefficient_poly = sp.Poly(
        jacobian_minus_c,
        x,
        y,
        domain=sp.QQ[tuple(ring_generators)],
    )
    raw_rows = [
        sp.Poly(coefficient, ring_generators).as_expr()
        for coefficient in coefficient_poly.coeffs()
    ]

    require(len(coefficient_generators) == 17, "p.208 coefficient count mismatch")
    require(len(raw_rows) == 77, "p.208 Jacobian-row count mismatch")
    require(sp.Poly(degree16, x, y).total_degree() == 16, "degree-16 form mismatch")
    require(sp.Poly(degree12, x, y).total_degree() == 12, "degree-12 form mismatch")
    origin = {generator: 0 for generator in coefficient_generators + [c]}
    require(
        all(sp.expand(row.subs(origin)) == 0 for row in raw_rows),
        "raw p.208 ideal lost its c=0 origin",
    )

    return {
        "variant": variant,
        "coefficient_generators": coefficient_generators,
        "ring_generators": ring_generators,
        "raw_rows": raw_rows,
        "wrapper": Zc * c - 1,
        "c": c,
        "Zc": Zc,
        "raw_origin_verified": True,
    }


def singular_expression(expression: sp.Expr) -> str:
    return str(sp.expand(expression)).replace("**", "^")


def build_singular_script(system: dict[str, Any]) -> str:
    variables = ",".join(map(str, system["ring_generators"]))
    rows = [singular_expression(row) for row in system["raw_rows"]]
    wrapper = singular_expression(system["wrapper"])
    raw = ",".join(rows)
    localized = ",".join(rows + [wrapper])
    return (
        f"ring R=0,({variables}),dp;\n"
        f"ideal Raw={raw};\n"
        f"ideal Localized={localized};\n"
        "ideal RawStd=std(Raw);\n"
        "ideal LocalizedStd=std(Localized);\n"
        'print("BEGIN_LOCALIZED_DIM"); print(dim(LocalizedStd)); print("END_LOCALIZED_DIM");\n'
        'print("BEGIN_LOCALIZED_GB"); print(LocalizedStd); print("END_LOCALIZED_GB");\n'
        'print("BEGIN_RAW_NF"); print(reduce(1,RawStd)); print("END_RAW_NF");\n'
        'print("BEGIN_LOCALIZED_NF"); print(reduce(1,LocalizedStd)); print("END_LOCALIZED_NF");\n'
        "ideal EmptyControl=c,Zc*c-1;\n"
        "ideal PointControl=c-1,Zc*c-1;\n"
        'print("BEGIN_EMPTY_NF"); print(reduce(1,std(EmptyControl))); print("END_EMPTY_NF");\n'
        'print("BEGIN_POINT_NF"); print(reduce(1,std(PointControl))); print("END_POINT_NF");\n'
        "matrix UnitLift=lift(Localized,ideal(1));\n"
        'print("BEGIN_LIFT_CHECK"); print(matrix(Localized)*UnitLift); print("END_LIFT_CHECK");\n'
        "quit;\n"
    )


def singular_section(output: str, name: str) -> str:
    matches = re.findall(
        rf"BEGIN_{re.escape(name)}\n(.*?)\nEND_{re.escape(name)}",
        output,
        re.DOTALL,
    )
    require(len(matches) == 1, f"expected one Singular section {name}, got {len(matches)}")
    return matches[0].strip()


def run_appendix_variant(
    repeated_c5: bool,
    output_dir: Path,
    singular: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    system = build_1612(repeated_c5)
    script = build_singular_script(system)
    script_name = f"appendixii-{system['variant']}-Q.sing"
    script_path = output_dir / script_name
    atomic_write(script_path, script)

    environment = os.environ.copy()
    for name in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
    ):
        environment[name] = "1"
    started = time.perf_counter()
    replay = subprocess.run(
        [singular, "-q"],
        input=script,
        text=True,
        capture_output=True,
        check=False,
        timeout=timeout_seconds,
        env=environment,
    )
    elapsed = time.perf_counter() - started
    require(replay.returncode == 0, f"Singular failed for {system['variant']}: {replay.stderr}")

    localized_dimension = int(singular_section(replay.stdout, "LOCALIZED_DIM"))
    localized_basis = singular_section(replay.stdout, "LOCALIZED_GB")
    raw_nf = singular_section(replay.stdout, "RAW_NF")
    localized_nf = singular_section(replay.stdout, "LOCALIZED_NF")
    empty_nf = singular_section(replay.stdout, "EMPTY_NF")
    point_nf = singular_section(replay.stdout, "POINT_NF")
    lift_check = singular_section(replay.stdout, "LIFT_CHECK")
    require(localized_dimension == -1, "localized p.208 ideal is not zero-dimensional empty")
    require(localized_basis == "1", "localized p.208 standard basis is not 1")
    require(raw_nf == "1", "raw p.208 ideal unexpectedly unit")
    require(localized_nf == "0", "localized p.208 ideal is not unit")
    require(empty_nf == "0", "empty localization control failed")
    require(point_nf == "1", "nonempty point localization control failed")
    require(lift_check == "1", "localized unit-ideal lift did not recompose to 1")

    raw_payload = "".join(
        f"{sp.srepr(sp.expand(row))}\n" for row in system["raw_rows"]
    )
    return {
        "variant": system["variant"],
        "field": "Q",
        "ordering": "dp",
        "generator_order": list(map(str, system["ring_generators"])),
        "n_coefficient_variables": len(system["coefficient_generators"]),
        "n_unknowns_before_wrapper": len(system["coefficient_generators"]) + 1,
        "n_J_coefficient_rows": len(system["raw_rows"]),
        "wrapper": "Zc*c-1",
        "raw_origin_c0_verified": system["raw_origin_verified"],
        "raw_rows_sha256": sha256_text(raw_payload),
        "singular_script": script_name,
        "singular_script_sha256": sha256_text(script),
        "singular_stdout_sha256": sha256_text(replay.stdout),
        "singular_stderr": replay.stderr,
        "elapsed_seconds": round(elapsed, 6),
        "localized_dimension": localized_dimension,
        "localized_basis": localized_basis,
        "controls": {
            "raw_reduce_1": raw_nf,
            "localized_reduce_1": localized_nf,
            "empty_c_and_wrapper_reduce_1": empty_nf,
            "point_c1_and_wrapper_reduce_1": point_nf,
            "localized_unit_lift_recomposition": lift_check,
        },
        "verdict": "SATURATED-EMPTY[P208-COMMON-POLYNOMIAL-ANSATZ/Q]",
    }


def tame_automorphism_control() -> dict[str, Any]:
    a, x, y, A, C = sp.symbols("a x y A C")
    F = a * x + y
    G = (a - 1) * x + y
    jacobian = sp.expand(
        sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x)
    )
    inverse_x = sp.expand(F - G)
    inverse_y = sp.expand(a * G - (a - 1) * F)

    # A tame factorization for a != 0: (x,y) -> (a*x+y,y), followed by
    # (u,v) -> (u,((a-1)*u+v)/a).
    first_u, first_v = a * x + y, y
    composed_G = sp.cancel(((a - 1) * first_u + first_v) / a)
    first_determinant = a
    second_determinant = sp.cancel(1 / a)

    Fansatz = A * x + y
    Gansatz = C * x + y
    shared_row = sp.expand(
        sp.diff(Fansatz, x) * sp.diff(Gansatz, y)
        - sp.diff(Fansatz, y) * sp.diff(Gansatz, x)
        - 1
    )
    witness_F = Fansatz.subs(A, 2)
    witness_G = Gansatz.subs(C, 1)
    witness_jacobian = sp.expand(
        sp.diff(witness_F, x) * sp.diff(witness_G, y)
        - sp.diff(witness_F, y) * sp.diff(witness_G, x)
    )
    infinity_difference = sp.expand((-a) - (1 - a))

    checks = {
        "jacobian_is_one": jacobian == 1,
        "inverse_x_is_x": inverse_x == x,
        "inverse_y_is_y": inverse_y == y,
        "tame_composition_F": sp.expand(first_u - F) == 0,
        "tame_composition_G_for_a_nonzero": sp.cancel(composed_G - G) == 0,
        "factor_determinants_multiply_to_one": sp.cancel(
            first_determinant * second_determinant
        ) == 1,
        "infinity_points_are_distinct": infinity_difference == -1,
        "shared_ansatz_row_is_A_minus_C_minus_1": sp.expand(
            shared_row - (A - C - 1)
        ) == 0,
        "slice_witness_jacobian_is_one": witness_jacobian == 1,
    }
    require(all(checks.values()), "tame automorphism control failed")
    return {
        "type": "EXACT-AUTOMORPHISM/SURVIVES[UNIVERSAL-GLOBAL-CHECKS]",
        "field": "Q(a)",
        "pair": {"F": str(F), "G": str(G), "J": str(jacobian)},
        "inverse": {"x": "F-G", "y": "a*G-(a-1)*F"},
        "tame_factorization_condition": "a != 0",
        "factor_determinants": [str(first_determinant), str(second_determinant)],
        "points_at_infinity": ["[1:-a:0]", "[1:1-a:0]"],
        "point_coordinate_difference": str(infinity_difference),
        "shared_ansatz_row": str(shared_row),
        "slice_A2_C1": {
            "F": str(witness_F),
            "G": str(witness_G),
            "J": str(witness_jacobian),
        },
        "checks": checks,
        "special_D108_tower": "NOT-APPLICABLE[degrees (1,1)]",
        "survives": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--singular", default="Singular")
    parser.add_argument("--singular-timeout", type=int, default=1200)
    args = parser.parse_args()
    require(args.singular_timeout > 0, "--singular-timeout must be positive")
    singular = shutil.which(args.singular)
    require(singular is not None, f"Singular executable not found: {args.singular}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    reduction = parent_reduction()
    variants = [
        run_appendix_variant(True, args.output_dir, singular, args.singular_timeout),
        run_appendix_variant(False, args.output_dir, singular, args.singular_timeout),
    ]
    require(all(item["localized_basis"] == "1" for item in variants), "control kill failed")
    automorphism = tame_automorphism_control()

    result = {
        "schema": "g108band-exact-Q-controls-v1",
        "type": "APPENDIX-II-KILL/EXACT-Q + TAME-AUTOMORPHISM-SURVIVAL",
        "frozen_reference": {
            "basename": "controls.py",
            "sha256": FROZEN_CONTROLS_SHA256,
            "mechanical_changes": [
                "derive (16,12) from the frozen (64,48) parent row",
                "rename kappa,T to c,Zc",
                "replace GF(32003) Groebner by exact Q Singular dp",
                "add raw/localized, empty/point, and lift controls",
            ],
        },
        "parent_reduction": reduction,
        "appendix_ii": {
            "convention": (
                "control degree16=main F and degree12=main G; the frozen ordered "
                "Jacobian is J(degree12,degree16)-c, harmless up to c -> -c"
            ),
            "c_role": "control-local nonzero Jacobian scalar",
            "variants": variants,
            "both_exact_Q_localizations_empty": True,
        },
        "tame_automorphism": automorphism,
        "controls_pass": True,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    atomic_write(args.output_dir / "controls.json", encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
