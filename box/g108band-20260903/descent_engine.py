#!/usr/bin/env python3
"""Conditional exact-Q compiler for the D=108 Proposition-6.3 descent.

The no-split alternative ``delta* >= v_3/u_3 = 7/2`` licenses Moh's
Proposition 6.3 directly.  It produces the two-point monomial-Jacobian datum

    (n',m') = (24,16), M' = (-16,18), d' = (24,8,2), V' = (7,2),
    J(F,G) = c*x^4, c != 0.

This program runs the charged d'=2, e'=3 A/B order compiler over Q.  That
compiler is deliberately an *enlarged conditional diagnostic*: Proposition
6.3 proves polynomiality and pi-degrees, but the frozen source does not prove
the ordinary total-degree support/ring map used by the compiler.  Consequently
even a Singular unit-ideal result is never promoted past
``OPEN[DESCENT-SUPPORT/VARIABLE-MAP]``.

The denominator-shed source jet is audited exactly as

    a0 + a1*Y^2 + a2*Y^4 + a3*Y^6 + Pi*Y^7.

Its even strict-below support is recorded but is not imposed as an additional
restriction on the enlarged A/B diagnostic.

Only the caller-selected ``--output-dir`` is written.  The artifacts are:

* ``descent-system.txt``: declared ring, maps, and all exact equations;
* ``descent-replay.sing``: standalone Singular replay with controls and lift;
* ``descent-singular.log``: exact stdout/stderr and timing;
* ``descent.json``: machine-readable result and guarded status.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
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


PROMOTED_STATUS = "OPEN[DESCENT-SUPPORT/VARIABLE-MAP]"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def atomic_write(path: Path, payload: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


@dataclass(frozen=True)
class DescentDatum:
    n: int
    m: int
    M: tuple[int, int]
    d: tuple[int, int, int]
    V: tuple[int, int]
    s_prime: int
    u_prime: int
    v_prime: int
    k: int
    height_defect: int
    jet_height: int
    approximate_root_profile: tuple[int, int, int]


def derive_datum() -> tuple[DescentDatum, dict[str, Any]]:
    """Derive, rather than merely transcribe, the Proposition-6.3 datum."""
    parent_n, parent_m = 108, 72
    parent_M = (-72, 81, 106)
    parent_d = (108, 36, 9, 1)
    parent_V = (7, 7)
    parent_s = 3
    d_s, u_s, v_s = parent_d[parent_s - 1], 2, 7
    require((d_s, u_s, v_s) == (9, 2, 7), "unexpected D=108 top data")

    scale = Fraction(u_s, d_s)
    scaled = lambda value: scale * value
    values = [scaled(parent_n), scaled(parent_m), *(scaled(v) for v in parent_M[:-1])]
    require(all(value.denominator == 1 for value in values), "nonintegral descent datum")

    n_prime = int(scaled(parent_n))
    m_prime = int(scaled(parent_m))
    M_prime = tuple(int(scaled(value)) for value in parent_M[:-1])
    d_prime = (
        n_prime,
        gcd(n_prime, M_prime[0]),
        gcd(gcd(n_prime, M_prime[0]), M_prime[1]),
    )
    V_prime = (parent_V[0], d_prime[-1])
    s_prime = len(M_prime)
    v_prime = V_prime[0]
    u_prime = d_prime[s_prime - 1] - v_prime
    k = v_s - u_s - 1
    height_defect = n_prime - M_prime[-1]
    jet_height = v_s

    # Moh's semigroup recipe verifies the transformed T_2 pi-degree.
    q1 = M_prime[0]
    q2 = M_prime[1] - M_prime[0]
    lambda1 = q1 * d_prime[0]
    lambda2 = lambda1 + q2 * d_prime[1]
    require(lambda1 % d_prime[0] == 0, "nonintegral transformed mu_1")
    require(lambda2 % d_prime[1] == 0, "nonintegral transformed mu_2")
    neg_mu1 = -(lambda1 // d_prime[0])
    neg_mu2 = -(lambda2 // d_prime[1])

    datum = DescentDatum(
        n=n_prime,
        m=m_prime,
        M=M_prime,
        d=d_prime,
        V=V_prime,
        s_prime=s_prime,
        u_prime=u_prime,
        v_prime=v_prime,
        k=k,
        height_defect=height_defect,
        jet_height=jet_height,
        approximate_root_profile=(n_prime, m_prime, neg_mu2),
    )
    require(
        datum
        == DescentDatum(
            n=24,
            m=16,
            M=(-16, 18),
            d=(24, 8, 2),
            V=(7, 2),
            s_prime=2,
            u_prime=1,
            v_prime=7,
            k=4,
            height_defect=6,
            jet_height=7,
            approximate_root_profile=(24, 16, 14),
        ),
        f"descent derivation mismatch: {datum}",
    )
    require(height_defect == k + 2, "terminal defect is not k+2")
    return datum, {
        "parent": {
            "n": parent_n,
            "m": parent_m,
            "M": list(parent_M),
            "d": list(parent_d),
            "V_2_V_3": list(parent_V),
            "s": parent_s,
            "d_s": d_s,
            "u_s": u_s,
            "v_s": v_s,
        },
        "scale": "2/9",
        "semigroup_check": {
            "q_prime": [q1, q2],
            "lambda_prime": [lambda1, lambda2],
            "negative_mu_prime": [neg_mu1, neg_mu2],
        },
        "proposition_6_3_hypothesis": {
            "branch": "NO-SPLIT-ALTERNATIVE",
            "delta_star_lower_bound": "7/2",
            "v_s_over_u_s": "7/2",
            "licensed_directly_by": "Moh Proposition 6.3",
            "not_by": "Proposition 6.4 (its u_s=1 hypothesis is false here)",
        },
    }


def quotient_in_y(numerator: sp.Expr, denominator: sp.Expr, y: sp.Symbol) -> tuple[sp.Expr, sp.Expr]:
    quotient, remainder = sp.div(sp.Poly(numerator, y), sp.Poly(denominator, y))
    return sp.expand(quotient.as_expr()), sp.expand(remainder.as_expr())


def jacobian_xy(left: sp.Expr, right: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(
        sp.diff(left, x) * sp.diff(right, y)
        - sp.diff(left, y) * sp.diff(right, x)
    )


def hadic_jacobian_coefficients(
    h: sp.Expr,
    low_terms: tuple[tuple[sp.Expr, int], ...],
    high_terms: tuple[tuple[sp.Expr, int], ...],
    x: sp.Symbol,
    y: sp.Symbol,
) -> list[sp.Expr]:
    """Return the monic-y normal form of J(low,high) in powers of h.

    The charged compiler uses

        J(a h^r,b h^s) = h^(r+s) J(a,b)
          + h^(r+s-1) (s b J(a,h) + r a J(h,b)).

    Each coefficient is divided by monic ``h`` in ``y``.  Its quotient is
    carried to the next h-power; its remainder stays at the current level.
    """
    largest_initial_level = max(
        r + s for _a, r in low_terms for _b, s in high_terms
    )
    coefficients = [sp.Integer(0) for _ in range(largest_initial_level + 2)]
    for a, r in low_terms:
        for b, s in high_terms:
            coefficients[r + s] = sp.expand(
                coefficients[r + s] + jacobian_xy(a, b, x, y)
            )
            lower_level = r + s - 1
            if lower_level >= 0 and (r != 0 or s != 0):
                lower = (
                    s * b * jacobian_xy(a, h, x, y)
                    + r * a * jacobian_xy(h, b, x, y)
                )
                coefficients[lower_level] = sp.expand(
                    coefficients[lower_level] + lower
                )

    for level in range(len(coefficients) - 1):
        if coefficients[level] == 0:
            continue
        quotient, remainder = quotient_in_y(coefficients[level], h, y)
        coefficients[level] = remainder
        coefficients[level + 1] = sp.expand(coefficients[level + 1] + quotient)
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def build_charged_system() -> dict[str, Any]:
    """Build the charged d'=2,e'=3 A/B generator and 26 h-adic rows."""
    x, y = sp.symbols("x y")
    h_symbols = sp.symbols("h0:8")
    bp, bq, br, bs, c, T = sp.symbols("bp bq br bs c T")

    h = sp.expand(y**7 * (y - x) + sum(h_symbols[j] * y**j for j in range(8)))

    # The charged A/B chart uses the first nested quotient h=A*y+h_0.
    # Exact y-division declares and checks that map; matching coefficient
    # names alone would not do so.
    h_constant = h_symbols[0]
    A, A_remainder = quotient_in_y(h - h_constant, y, y)
    expected_A = y**6 * (y - x) + sum(
        h_symbols[j] * y ** (j - 1) for j in range(1, 8)
    )
    require(sp.expand(A - expected_A) == 0, "charged A quotient mismatch")
    require(A_remainder == 0, "h-h_0 is not exactly divisible by y")

    beta = sp.expand(bp * A + bq * y + br * x + bs)
    alpha, alpha_remainder = quotient_in_y(beta**2, h, y)
    require(sp.expand(beta**2 - alpha * h - alpha_remainder) == 0, "alpha division failed")

    low_terms = ((sp.Integer(1), 2), (2 * beta, 0))
    high_terms = ((sp.Integer(1), 3), (3 * beta, 1), (sp.Rational(3, 2) * alpha, 0))
    low = sp.expand(sum(coefficient * h**power for coefficient, power in low_terms))
    high = sp.expand(sum(coefficient * h**power for coefficient, power in high_terms))
    jacobian = jacobian_xy(low, high, x, y)
    target_residual = sp.expand(jacobian - c * x**4)

    hadic_coefficients = hadic_jacobian_coefficients(h, low_terms, high_terms, x, y)
    require(hadic_coefficients, "empty h-adic Jacobian expansion")
    hadic_coefficients[0] = sp.expand(hadic_coefficients[0] - c * x**4)
    require(
        sp.expand(
            sum(value * h**level for level, value in enumerate(hadic_coefficients))
            - target_residual
        )
        == 0,
        "h-adic Jacobian recomposition failed",
    )

    rows = []
    for level, coefficient in enumerate(hadic_coefficients):
        for monomial, value in sp.Poly(coefficient, x, y).terms():
            rows.append(
                {
                    "label": f"H{level}_x{monomial[0]}_y{monomial[1]}",
                    "h_power": level,
                    "x_degree": monomial[0],
                    "y_degree": monomial[1],
                    "expression": sp.expand(value),
                }
            )
    coefficient_unknowns = [*h_symbols, bp, bq, br, bs, c]
    ring_generators = [*coefficient_unknowns, T]
    wrapper = T * c - 1

    require(len(coefficient_unknowns) == 13, "charged compiler must have 13 unknowns")
    require(len(rows) == 26, f"expected 26 charged h-adic rows, got {len(rows)}")
    require(len(rows) + 1 == 27, "wrapper must make 27 localized equations")
    require(
        [len(sp.Poly(value, x, y).terms()) for value in hadic_coefficients] == [18, 8],
        "expected charged h-adic row split 18+8",
    )
    require(sp.Poly(h, y).degree() == 8, "h is not monic of y-degree 8")
    require(sp.Poly(A, y).degree() == 7, "A has wrong y-degree")
    require(sp.Poly(beta, y).degree() == 7, "beta has wrong y-degree")
    require(sp.Poly(alpha, y).degree() == 6, "alpha quotient has wrong y-degree")
    require(sp.Poly(low, y).degree() == 16, "low polynomial has wrong y-degree")
    require(sp.Poly(high, y).degree() == 24, "high polynomial has wrong y-degree")
    require(
        any(sp.expand(row["expression"] + c) == 0 for row in rows),
        "the charged h^0 x^4 row is not -c",
    )

    origin = {variable: 0 for variable in coefficient_unknowns}
    require(
        all(sp.expand(row["expression"].subs(origin)) == 0 for row in rows),
        "raw system lost its c=0 origin",
    )
    return {
        "x": x,
        "y": y,
        "h": h,
        "A": A,
        "A_remainder": A_remainder,
        "beta": beta,
        "alpha": alpha,
        "alpha_remainder": alpha_remainder,
        "low": low,
        "high": high,
        "jacobian": jacobian,
        "target_residual": target_residual,
        "hadic_coefficients": hadic_coefficients,
        "rows": rows,
        "coefficient_unknowns": coefficient_unknowns,
        "ring_generators": ring_generators,
        "c": c,
        "T": T,
        "wrapper": wrapper,
        "raw_origin_verified": True,
    }


def singular_expression(expression: sp.Expr) -> str:
    return str(sp.expand(expression)).replace("**", "^")


def build_singular_script(system: dict[str, Any]) -> str:
    generators = ",".join(map(str, system["ring_generators"]))
    row_expressions = [singular_expression(row["expression"]) for row in system["rows"]]
    wrapper = singular_expression(system["wrapper"])
    raw = ",".join(row_expressions)
    localized = ",".join([*row_expressions, wrapper])
    return (
        "// Conditional enlarged D=108 Proposition-6.3 descent diagnostic.\n"
        "// Exact field Q; dp order; c is localized only by T*c-1.\n"
        f"ring R=0,({generators}),dp;\n"
        f"ideal Raw={raw};\n"
        f"ideal Localized={localized};\n"
        "ideal RawStd=std(Raw);\n"
        "ideal LocalizedStd=std(Localized);\n"
        'print("BEGIN_RAW_DIM"); print(dim(RawStd)); print("END_RAW_DIM");\n'
        'print("BEGIN_LOCALIZED_DIM"); print(dim(LocalizedStd)); print("END_LOCALIZED_DIM");\n'
        'print("BEGIN_LOCALIZED_GB"); print(LocalizedStd); print("END_LOCALIZED_GB");\n'
        'print("BEGIN_RAW_NF"); print(reduce(1,RawStd)); print("END_RAW_NF");\n'
        'print("BEGIN_LOCALIZED_NF"); print(reduce(1,LocalizedStd)); print("END_LOCALIZED_NF");\n'
        "ideal EmptyControl=c,T*c-1;\n"
        "ideal PointControl=c-1,T*c-1;\n"
        'print("BEGIN_EMPTY_NF"); print(reduce(1,std(EmptyControl))); print("END_EMPTY_NF");\n'
        'print("BEGIN_POINT_NF"); print(reduce(1,std(PointControl))); print("END_POINT_NF");\n'
        "matrix UnitLift=lift(Localized,ideal(1));\n"
        'print("BEGIN_UNIT_LIFT"); print(UnitLift); print("END_UNIT_LIFT");\n'
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


def run_singular(
    script: str,
    singular: str | None,
    timeout_seconds: int,
) -> tuple[dict[str, Any], str]:
    if singular is None:
        result = {
            "ran": False,
            "returncode": None,
            "elapsed_seconds": 0.0,
            "outcome": "NOT-RUN[SINGULAR-NOT-FOUND]",
            "unit_ideal": None,
        }
        return result, "Singular executable not found; replay file was emitted.\n"

    environment = os.environ.copy()
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        environment[name] = "1"
    started = time.perf_counter()
    try:
        replay = subprocess.run(
            [singular, "-q"],
            input=script,
            text=True,
            capture_output=True,
            check=False,
            timeout=timeout_seconds,
            env=environment,
        )
    except subprocess.TimeoutExpired as exc:
        elapsed = time.perf_counter() - started
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        return (
            {
                "ran": True,
                "returncode": None,
                "elapsed_seconds": round(elapsed, 6),
                "timeout_seconds": timeout_seconds,
                "outcome": "BUDGET[SINGULAR-TIMEOUT]",
                "unit_ideal": None,
                "stdout_sha256": sha256_text(stdout),
                "stderr_sha256": sha256_text(stderr),
            },
            f"COMMAND: {singular} -q\nTIMEOUT: {timeout_seconds}\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}",
        )

    elapsed = time.perf_counter() - started
    log = (
        f"COMMAND: {singular} -q\nRETURN_CODE: {replay.returncode}\n"
        f"ELAPSED_SECONDS: {elapsed:.6f}\nSTDOUT:\n{replay.stdout}\nSTDERR:\n{replay.stderr}"
    )
    if replay.returncode != 0:
        return (
            {
                "ran": True,
                "returncode": replay.returncode,
                "elapsed_seconds": round(elapsed, 6),
                "timeout_seconds": timeout_seconds,
                "outcome": "ERROR[SINGULAR-NONZERO-EXIT]",
                "unit_ideal": None,
                "stdout_sha256": sha256_text(replay.stdout),
                "stderr_sha256": sha256_text(replay.stderr),
            },
            log,
        )

    raw_dimension = int(singular_section(replay.stdout, "RAW_DIM"))
    localized_dimension = int(singular_section(replay.stdout, "LOCALIZED_DIM"))
    localized_basis = singular_section(replay.stdout, "LOCALIZED_GB")
    raw_nf = singular_section(replay.stdout, "RAW_NF")
    localized_nf = singular_section(replay.stdout, "LOCALIZED_NF")
    empty_nf = singular_section(replay.stdout, "EMPTY_NF")
    point_nf = singular_section(replay.stdout, "POINT_NF")
    unit_lift = singular_section(replay.stdout, "UNIT_LIFT")
    lift_check = singular_section(replay.stdout, "LIFT_CHECK")
    unit_ideal = localized_basis == "1" and localized_nf == "0"
    controls = {
        "raw_reduce_1": raw_nf,
        "localized_reduce_1": localized_nf,
        "empty_c_and_wrapper_reduce_1": empty_nf,
        "point_c1_and_wrapper_reduce_1": point_nf,
        "localized_unit_lift_recomposition": lift_check,
    }
    require(raw_nf == "1", "raw ideal unexpectedly contains 1")
    require(empty_nf == "0", "empty localization control failed")
    require(point_nf == "1", "point localization control failed")
    if unit_ideal:
        require(localized_dimension == -1, "unit ideal has unexpected dimension")
        require(lift_check == "1", "unit lift failed to recompose 1")
    result = {
        "ran": True,
        "returncode": replay.returncode,
        "elapsed_seconds": round(elapsed, 6),
        "timeout_seconds": timeout_seconds,
        "outcome": (
            "UNIT[CONDITIONAL-ENLARGED-CHARGED-COMPILER]"
            if unit_ideal
            else "NONUNIT[CONDITIONAL-ENLARGED-CHARGED-COMPILER]"
        ),
        "unit_ideal": unit_ideal,
        "raw_dimension": raw_dimension,
        "localized_dimension": localized_dimension,
        "localized_basis": localized_basis,
        "unit_lift": unit_lift,
        "controls": controls,
        "stdout_sha256": sha256_text(replay.stdout),
        "stderr_sha256": sha256_text(replay.stderr),
    }
    return result, log


def system_text(system: dict[str, Any], datum: DescentDatum) -> str:
    lines = [
        "D=108 Proposition-6.3 no-split descent: conditional enlarged system",
        "field=Q",
        "generator_order=" + ",".join(map(str, system["ring_generators"])),
        "ordering=dp",
        f"datum={asdict(datum)}",
        "source_strict_below_jet=a0+a1*Y^2+a2*Y^4+a3*Y^6",
        "source_at_level_parting=Pi*Y^7",
        "source_jet_restricts_enlarged_diagnostic=false",
        "",
        "Declared maps:",
        "h=" + str(system["h"]),
        "A=quotient_y(h-h0,y)=" + str(system["A"]),
        "A_remainder=" + str(system["A_remainder"]),
        "beta=" + str(system["beta"]),
        "alpha=quotient_y(beta^2,h)=" + str(system["alpha"]),
        "alpha_remainder=" + str(system["alpha_remainder"]),
        "low=h^2+2*beta=" + str(system["low"]),
        "high=h^3+3*beta*h+(3/2)*alpha=" + str(system["high"]),
        "target=J_x_y(low,high)-c*x^4",
        "jacobian_coefficient_mode=h-adic-monic-y-normal-form",
        "h_adic_row_split=18+8",
        "wrapper=T*c-1",
        "",
        "Raw h-adic Jacobian coefficient rows:",
    ]
    for row in system["rows"]:
        lines.append(f"{row['label']}={row['expression']}")
    lines.extend(
        [
            "",
            f"raw_equations={len(system['rows'])}",
            f"localized_equations_including_wrapper={len(system['rows']) + 1}",
            f"promoted_status={PROMOTED_STATUS}",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--singular", default="Singular")
    parser.add_argument("--singular-timeout", type=int, default=3000)
    args = parser.parse_args()
    require(args.singular_timeout > 0, "--singular-timeout must be positive")

    datum, derivation = derive_datum()
    system = build_charged_system()
    singular_script = build_singular_script(system)
    readable_system = system_text(system, datum)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write(args.output_dir / "descent-system.txt", readable_system)
    atomic_write(args.output_dir / "descent-replay.sing", singular_script)

    singular_path = shutil.which(args.singular)
    singular_result, singular_log = run_singular(
        singular_script,
        singular_path,
        args.singular_timeout,
    )
    atomic_write(args.output_dir / "descent-singular.log", singular_log)

    rows_payload = "".join(
        f"{row['label']}={sp.srepr(row['expression'])}\n" for row in system["rows"]
    )
    diagnostic_status = {
        True: "DEAD[CONDITIONAL-ENLARGED-CHARGED-COMPILER]",
        False: "OPEN[CONDITIONAL-COMPILER-NONUNIT]",
        None: singular_result["outcome"],
    }[singular_result["unit_ideal"]]
    result = {
        "schema": "g108-prop63-descent-v1",
        "type": "CONDITIONAL-PROP-6.3-DESCENT/EXACT-Q",
        "conditional_only": True,
        "datum": {
            **asdict(datum),
            "M": list(datum.M),
            "d": list(datum.d),
            "V": list(datum.V),
            "approximate_root_profile": list(datum.approximate_root_profile),
        },
        "derivation": derivation,
        "source_support_audit": {
            "denominator_shedding": 2,
            "strict_below_exponents": [0, 2, 4, 6],
            "at_level_exponent": 7,
            "strict_below_series": "a0+a1*Y^2+a2*Y^4+a3*Y^6",
            "at_level_parting": "Pi*Y^7",
            "odd_strict_below_terms_introduced": False,
            "restricts_enlarged_diagnostic": False,
            "reason": (
                "Prop. 6.3 source support is audited exactly; the charged A/B "
                "compiler is intentionally an enlarged conditional diagnostic."
            ),
        },
        "compiler": {
            "name": "charged-dprime2-eprime3-A/B",
            "field": "Q",
            "ordering": "dp",
            "generator_order": list(map(str, system["ring_generators"])),
            "coefficient_unknowns": list(map(str, system["coefficient_unknowns"])),
            "n_coefficient_unknowns": len(system["coefficient_unknowns"]),
            "n_ring_generators": len(system["ring_generators"]),
            "n_raw_J_rows": len(system["rows"]),
            "n_charged_equations": len(system["rows"]),
            "n_localized_equations_including_wrapper": len(system["rows"]) + 1,
            "h_adic_row_split": [18, 8],
            "jacobian_coefficient_mode": "h-adic-monic-y-normal-form",
            "h": str(system["h"]),
            "A": str(system["A"]),
            "beta": str(system["beta"]),
            "alpha_quotient": str(system["alpha"]),
            "low_h_adic_terms": [["1", 2], ["2*beta", 0]],
            "high_h_adic_terms": [["1", 3], ["3*beta", 1], ["3/2*alpha", 0]],
            "jacobian_target": "c*x^4",
            "localization_wrapper": "T*c-1",
            "raw_origin_c0_verified": system["raw_origin_verified"],
            "raw_rows_sha256": sha256_text(rows_payload),
        },
        "artifacts": {
            "system": "descent-system.txt",
            "system_sha256": sha256_text(readable_system),
            "singular_replay": "descent-replay.sing",
            "singular_replay_sha256": sha256_text(singular_script),
            "singular_log": "descent-singular.log",
            "singular_log_sha256": sha256_text(singular_log),
        },
        "singular": singular_result,
        "diagnostic_status": diagnostic_status,
        "promoted_status": PROMOTED_STATUS,
        "promotion_blocker": (
            "Moh Proposition 6.3 does not prove the ordinary total-degree "
            "support and variable map used by the enlarged charged compiler."
        ),
    }
    require(result["promoted_status"] == PROMOTED_STATUS, "promotion guard changed")
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    atomic_write(args.output_dir / "descent.json", encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
