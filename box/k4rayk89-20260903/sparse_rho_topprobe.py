#!/usr/bin/env python3
"""Sparse total-band alpha/rho extension of the K=9 terminal RREF chart.

The explicit PIN12/K9-H3 builder supplies exact x,y-coordinate bands after
RREF elimination of h4,h5,h6.  This driver never forms the monolithic
``beta^2 / h`` remainder.  Instead it solves the six alpha bands by exact
constant-Q RREF and emits the remaining coefficient conditions band by band:

    beta^2 - h*alpha = 0                 in degrees 14..4,
    beta^2 - h*alpha = q0/3,q1/3,q2/3   in degrees 3,2,1,

while leaving the scalar rho0 free.  No E, lambda, MASTER, or Jacobian rows
are built.  Thus this is a necessary subsystem; only an exact-Q unit can kill
a branch.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import time
from typing import Any, Mapping, Sequence

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
RUNS = HERE / "topprobe-artifacts" / "sparse-rho"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

from box.lib.staged_band_emitter import (  # noqa: E402
    BandEmitConfig,
    BandRow,
    emit_staged_band_files,
)
from explicit_bands import (  # noqa: E402
    ChartBuilder,
    CoordPoly,
    atomic_write,
    cp_add,
    cp_clean,
    cp_expr,
    cp_mul,
    cp_scale,
    cp_substitute,
    denominator_lcm,
    exact_rref_with_transform,
    singular_expr,
)


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def alpha_form(index: int, degree: int) -> tuple[CoordPoly, list[sp.Symbol]]:
    poly: CoordPoly = {}
    symbols: list[sp.Symbol] = []
    for i in range(degree + 1):
        j = degree - i
        symbol = sp.Symbol(f"alpha{index}_{i}_{j}")
        poly[(i, j)] = symbol
        symbols.append(symbol)
    return poly, symbols


def beta_square_band(index: int, pbands: Mapping[int, CoordPoly]) -> CoordPoly:
    return cp_add(
        *(
            cp_mul(pbands[a], pbands[index - a])
            for a in range(index + 1)
            if a in pbands and index - a in pbands
        )
    )


def h_alpha_band(
    index: int,
    hbands: Mapping[int, CoordPoly],
    alpha_bands: Mapping[int, CoordPoly],
) -> CoordPoly:
    return cp_add(
        *(
            cp_mul(hbands[a], alpha_bands[index - a])
            for a in range(index + 1)
            if a in hbands and index - a in alpha_bands
        )
    )


def cp_add_factored(*polys: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    """Add coordinate maps without distributing parameter products."""

    result: CoordPoly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] = result.get(monomial, sp.Integer(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient != 0}


def cp_mul_factored(
    left: Mapping[tuple[int, int], sp.Expr],
    right: Mapping[tuple[int, int], sp.Expr],
) -> CoordPoly:
    """Multiply coordinate maps while retaining a factored coefficient DAG."""

    result: CoordPoly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            result[monomial] = result.get(monomial, sp.Integer(0)) + a * b
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient != 0}


def cp_scale_factored(
    poly: Mapping[tuple[int, int], sp.Expr], scalar: sp.Expr
) -> CoordPoly:
    return {monomial: scalar * coefficient for monomial, coefficient in poly.items()}


def beta_square_band_factored(
    index: int, pbands: Mapping[int, CoordPoly]
) -> CoordPoly:
    return cp_add_factored(
        *(
            cp_mul_factored(pbands[a], pbands[index - a])
            for a in range(index + 1)
            if a in pbands and index - a in pbands
        )
    )


def h_alpha_band_factored(
    index: int,
    hbands: Mapping[int, CoordPoly],
    alpha_bands: Mapping[int, CoordPoly],
) -> CoordPoly:
    return cp_add_factored(
        *(
            cp_mul_factored(hbands[a], alpha_bands[index - a])
            for a in range(index + 1)
            if a in hbands and index - a in alpha_bands
        )
    )


def fraction_matrix_sha256(matrix: Sequence[Sequence[Fraction]]) -> str:
    payload = "\n".join(
        ",".join(f"{value.numerator}/{value.denominator}" for value in row)
        for row in matrix
    )
    return sha256_text(payload + "\n")


def solve_alpha_band(
    residual: Mapping[tuple[int, int], sp.Expr],
    alpha_band: CoordPoly,
    *,
    band_index: int,
    expected_rank: int,
) -> tuple[CoordPoly, list[sp.Expr], dict[str, Any]]:
    """Eliminate alpha_n through the exact constant matrix for -H*alpha_n."""

    alpha_degree = 5 - band_index
    total_degree = 14 - band_index
    symbols = [alpha_band[(i, alpha_degree - i)] for i in range(alpha_degree + 1)]
    monomials = [(i, total_degree - i) for i in range(total_degree + 1)]
    equations = [sp.expand(residual.get(monomial, 0)) for monomial in monomials]
    zero_symbols = {symbol: sp.Integer(0) for symbol in symbols}
    matrix: list[list[Fraction]] = []
    right: list[sp.Expr] = []
    for equation in equations:
        coefficients = [sp.expand(equation).coeff(symbol) for symbol in symbols]
        rest = sp.expand(equation.xreplace(zero_symbols))
        rebuilt = sp.expand(
            rest
            + sum(
                (coefficient * symbol for coefficient, symbol in zip(coefficients, symbols)),
                sp.Integer(0),
            )
        )
        if rebuilt != equation:
            raise AssertionError(f"alpha band {band_index} is nonlinear")
        row: list[Fraction] = []
        for coefficient in coefficients:
            if not coefficient.is_Rational:
                raise AssertionError(
                    f"alpha band {band_index} has nonconstant pivot coefficient {coefficient}"
                )
            rational = sp.Rational(coefficient)
            row.append(Fraction(int(rational.p), int(rational.q)))
        matrix.append(row)
        right.append(-rest)

    rref, transform, pivots = exact_rref_with_transform(matrix)
    free_columns = [column for column in range(len(symbols)) if column not in pivots]
    if len(pivots) != expected_rank or free_columns:
        raise AssertionError(
            f"alpha band {band_index}: rank {len(pivots)}, expected {expected_rank}; "
            f"free={free_columns}"
        )
    # For H=y^9-x*y^8 the equations in ascending x-power are
    #   rest_i - a_i + a_(i-1) = 0.
    # Therefore a_i=sum_(j<=i) rest_j, followed by the exact triangular
    # compatibility basis sum_(j<=d+1)rest_j=0 and rest_j=0 for j>d+1.
    # This is precisely the constant-matrix RREF, but avoids expanding every
    # entry of the full symbolic left-transform matrix.
    rest = [sp.expand(equation.xreplace(zero_symbols)) for equation in equations]
    partial: sp.Expr = sp.Integer(0)
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    for index, symbol in enumerate(symbols):
        partial = sp.expand(partial + rest[index])
        substitutions[symbol] = partial
    first_compatibility = sp.expand(partial + rest[len(symbols)])
    compatibility = [first_compatibility, *rest[len(symbols) + 1 :]]
    compatibility = [expression for expression in compatibility if expression != 0]
    resolved = cp_substitute(alpha_band, substitutions)
    audit = {
        "band_index": band_index,
        "total_degree": total_degree,
        "engine": "exact_Q_constant_matrix_RREF",
        "equation_count": len(equations),
        "alpha_candidate_count": len(symbols),
        "rank": len(pivots),
        "expected_rank": expected_rank,
        "pivot_variables": [str(symbols[column]) for column in pivots],
        "free_alpha_variables": [],
        "compatibility_count": len(compatibility),
        "matrix_sha256": fraction_matrix_sha256(matrix),
        "rref_sha256": fraction_matrix_sha256(rref),
        "transform_sha256": fraction_matrix_sha256(transform),
        "row_transform_exact": True,
        "span_equivalence": "closed triangular basis from invertible exact-Q left row operations",
    }
    return resolved, compatibility, audit


def clear_row(
    expression: sp.Expr,
    *,
    label: str,
    band: str,
    degree: int,
    source: Mapping[str, Any],
) -> tuple[BandRow, int]:
    combined = sp.together(expression)
    integral, denominator = sp.fraction(combined)
    if not denominator.is_Integer:
        raise AssertionError(f"non-numeric denominator in {label}: {denominator}")
    multiplier = abs(int(denominator))
    if int(denominator) < 0:
        integral = -integral
    encoded = sp.sstr(integral, order="lex").replace("**", "^")
    if re.search(r"/\s*[0-9]+", encoded):
        raise AssertionError(f"uncleared rational in {label}")
    return (
        BandRow(
            label=label,
            band=band,
            degree=degree,
            expr=encoded,
            source={**source, "cleared_rational_denominator": multiplier},
        ),
        multiplier,
    )


def rows_from_coefficients(
    coefficients: Sequence[sp.Expr],
    *,
    prefix: str,
    band: str,
    degree: int,
    source: Mapping[str, Any],
) -> tuple[list[BandRow], list[int]]:
    rows: list[BandRow] = []
    denominators: list[int] = []
    for index, expression in enumerate(coefficients):
        if expression == 0:
            continue
        row, denominator = clear_row(
            expression,
            label=f"{prefix}_{index}",
            band=band,
            degree=degree,
            source={**source, "row_in_band": index},
        )
        rows.append(row)
        denominators.append(denominator)
    return rows, denominators


def rows_from_coordinate_band(
    polynomial: Mapping[tuple[int, int], sp.Expr],
    *,
    prefix: str,
    band: str,
    degree: int,
    source: Mapping[str, Any],
) -> tuple[list[BandRow], list[int]]:
    rows: list[BandRow] = []
    denominators: list[int] = []
    for (i, j), expression in sorted(polynomial.items()):
        if expression == 0:
            continue
        if i + j != degree:
            raise AssertionError(
                f"{prefix}: monomial {(i, j)} lies outside expected total degree {degree}"
            )
        row, denominator = clear_row(
            expression,
            label=f"{prefix}_x{i}_y{j}",
            band=band,
            degree=degree,
            source={**source, "x_power": i, "y_power": j},
        )
        rows.append(row)
        denominators.append(denominator)
    return rows, denominators


def ordered_ring(
    variables: Sequence[sp.Symbol],
    weights: Mapping[sp.Symbol, int],
    characteristic: int = 0,
) -> tuple[str, list[str], list[int]]:
    pairs = [(symbol, weights[symbol]) for symbol in variables if str(symbol) != "mu_inv"]
    pairs.sort(key=lambda item: (-item[1], str(item[0])))
    pairs.extend((symbol, weights[symbol]) for symbol in variables if str(symbol) == "mu_inv")
    names = [str(symbol) for symbol, _weight in pairs]
    ordered_weights = [int(weight) for _symbol, weight in pairs]
    return (
        f"ring SS={characteristic},({','.join(names)}),wp({','.join(str(weight) for weight in ordered_weights)});",
        names,
        ordered_weights,
    )


def coordinate_encoding(poly: Mapping[tuple[int, int], sp.Expr]) -> dict[str, str]:
    return {
        f"x{i}_y{j}": singular_expr(expression)
        for (i, j), expression in sorted(poly.items())
        if sp.expand(expression) != 0
    }


def build(branch: str, tag: str) -> dict[str, Any]:
    started = time.monotonic()
    def trace(phase: str, **payload: Any) -> None:
        print(
            json.dumps(
                {
                    "trace": phase,
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                    **payload,
                },
                sort_keys=True,
            ),
            flush=True,
        )

    trace("terminal_build_begin", branch=branch)
    builder = ChartBuilder(
        9,
        branch,
        "terminal",
        terminal_rref=True,
        coordinate_state_only=True,
    )
    terminal_chart = builder.build()
    trace("terminal_build_end", variables=len(terminal_chart.variables))
    if builder.coordinate_state is None:
        raise AssertionError("explicit terminal builder did not expose coordinate state")
    state = builder.coordinate_state
    hbands: dict[int, CoordPoly] = {
        index: dict(poly) for index, poly in state["hbands"].items()
    }
    pbands: dict[int, CoordPoly] = {
        index: dict(poly) for index, poly in state["pbands"].items()
    }
    qbands: dict[int, CoordPoly] = {
        index: dict(poly) for index, poly in state["qbands"].items()
    }
    variables: list[sp.Symbol] = list(state["variables"])
    weights: dict[sp.Symbol, int] = dict(state["weights"])
    if len(set(variables)) != len(variables):
        raise AssertionError("duplicate solver variable after terminal RREF")
    if hbands[1].get((0, 8), 0) != 0:
        raise AssertionError("h1 pure-y^8 coefficient was not eliminated")
    if hbands[0].get((0, 9), 0) != 1 or any(
        j == 9 and i != 0 for i, j in hbands[0]
    ):
        raise AssertionError("H is not monic of y-degree 9")

    output = RUNS / tag / f"K9_{branch}" / "build"
    ring, solver_variables, solver_weights = ordered_ring(variables, weights)

    rows: list[BandRow] = [
        BandRow(
            label=row.label,
            band=f"t00_{row.band}",
            degree=row.degree,
            expr=row.expr,
            source={**row.source, "intended_stage": "terminal"},
        )
        for row in state["terminal_rows"]
    ]
    denominators: list[int] = []
    alpha_bands: dict[int, CoordPoly] = {}
    alpha_audits: list[dict[str, Any]] = []
    residual_audits: list[dict[str, Any]] = []

    def checkpoint(phase: str) -> None:
        checkpoint_dir = output / "checkpoints" / phase
        manifest = emit_staged_band_files(
            rows,
            BandEmitConfig(
                output_dir=checkpoint_dir / "emitted_Q",
                ring=ring,
                option_lines=("option(redSB);", "short=0;"),
                global_generators=(("mu_localizer", "mu*mu_inv-1"),),
                manifest_name="bands-manifest.json",
            ),
        )
        payload = {
            "type": "K9-SPARSE-RHO-DURABLE-PREFIX",
            "K": 9,
            "branch": branch,
            "phase": phase,
            "scope": "necessary-prefix",
            "variables": solver_variables,
            "weights": solver_weights,
            "row_count": len(rows),
            "rows": [
                {
                    "label": row.label,
                    "band": row.band,
                    "degree": row.degree,
                    "expr": row.expr,
                    "source": dict(row.source),
                }
                for row in rows
            ],
            "alpha_rref_audit": alpha_audits,
            "residual_band_audit": residual_audits,
            "manifest": manifest["manifest_path"],
            "band_union_checksum": manifest["generator_union_checksum"],
            "elapsed_seconds": round(time.monotonic() - started, 6),
        }
        atomic_write(checkpoint_dir / "prefix.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
        atomic_write(
            output / "checkpoint-latest.json",
            json.dumps(
                {
                    "phase": phase,
                    "row_count": len(rows),
                    "prefix": str(checkpoint_dir / "prefix.json"),
                    "band_union_checksum": manifest["generator_union_checksum"],
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
        )
    for n in range(6):
        trace("alpha_band_begin", n=n)
        entering, symbols = alpha_form(n, 5 - n)
        trial_alpha_bands = {**alpha_bands, n: entering}
        residual = cp_add(
            beta_square_band(n, pbands),
            cp_scale(h_alpha_band(n, hbands, trial_alpha_bands), -1),
        )
        trace("alpha_residual_built", n=n, coordinates=len(residual))
        resolved, compatibility, audit = solve_alpha_band(
            residual,
            entering,
            band_index=n,
            expected_rank=6 - n,
        )
        alpha_bands[n] = resolved
        if set(symbols) & set().union(*(value.free_symbols for value in resolved.values())):
            raise AssertionError(f"alpha band {n} retained an eliminated auxiliary")
        new_rows, new_denominators = rows_from_coefficients(
            compatibility,
            prefix=f"ALPHA_DIV_n{n}",
            band=f"t10_a{n:02d}_ALPHA_DIV",
            degree=14 - n,
            source={"kind": "ALPHA_DIVISIBILITY", "band_index": n},
        )
        rows.extend(new_rows)
        denominators.extend(new_denominators)
        audit["emitted_compatibility_count"] = len(new_rows)
        alpha_audits.append(audit)
        trace(
            "alpha_band_end",
            n=n,
            compatibility=len(new_rows),
            cumulative_rows=len(rows),
        )
        if n == 5:
            checkpoint("alpha_complete")
            trace("checkpoint_emitted", checkpoint_phase="alpha_complete", rows=len(rows))

    for n in range(6, 14):
        trace("rho_band_begin", n=n)
        residual = cp_add_factored(
            beta_square_band_factored(n, pbands),
            cp_scale_factored(h_alpha_band_factored(n, hbands, alpha_bands), -1),
        )
        degree = 14 - n
        if n <= 10:
            family = "RHO_HIGH_ZERO"
            target_index: int | None = None
        else:
            target_index = n - 11
            residual = cp_add_factored(
                residual,
                cp_scale_factored(qbands[target_index], -sp.Rational(1, 3)),
            )
            family = "RHO_POSITIVE_MATCH"
        new_rows, new_denominators = rows_from_coordinate_band(
            residual,
            prefix=f"{family}_n{n}",
            band=f"t20_r{n:02d}_{family}",
            degree=degree,
            source={
                "kind": family,
                "band_index": n,
                "rho_q_index": target_index,
            },
        )
        rows.extend(new_rows)
        denominators.extend(new_denominators)
        residual_audits.append(
            {
                "band_index": n,
                "total_degree": degree,
                "condition": "zero" if n <= 10 else f"q{target_index}/3",
                "coordinate_count": len(residual),
                "emitted_row_count": len(new_rows),
            }
        )
        trace("rho_band_end", n=n, emitted=len(new_rows), cumulative_rows=len(rows))
        checkpoint(f"rho_n{n}_complete")
        trace("checkpoint_emitted", checkpoint_phase=f"rho_n{n}_complete", rows=len(rows))

    # n=14 is the scalar rho_0 band and is intentionally unconstrained.
    declared_names = {str(symbol) for symbol in variables}
    for row in rows:
        identifiers = set(re.findall(r"\b[A-Za-z_]\w*\b", row.expr))
        unknown = identifiers - declared_names
        if unknown:
            raise AssertionError(
                f"row {row.label} uses undeclared symbols {sorted(unknown)}"
            )
    denominator_value = math.lcm(terminal_chart.denominator_lcm, *denominators)
    trace("row_checks_end", rows=len(rows), denominator_lcm=denominator_value)
    fingerprint_payload = json.dumps(
        {
            "K": 9,
            "branch": branch,
            "scope": "RREF_SPARSE_ALPHA_RHO_NECESSARY_SUBSYSTEM",
            "variables": solver_variables,
            "weights": solver_weights,
            "rows": [(row.label, row.band, row.degree, row.expr) for row in rows],
            "global": [("mu_localizer", "mu*mu_inv-1")],
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    chart_sha256 = sha256_text(fingerprint_payload)

    manifest = emit_staged_band_files(
        rows,
        BandEmitConfig(
            output_dir=output / "emitted_Q",
            ring=ring,
            option_lines=("option(redSB);", "short=0;"),
            global_generators=(("mu_localizer", "mu*mu_inv-1"),),
            manifest_name="bands-manifest.json",
        ),
    )
    trace("manifest_emitted", bands=manifest["band_count"])
    family_counts = Counter(row.source["kind"] for row in rows)
    metadata = {
        "type": "K4RAY-K9-RREF-SPARSE-ALPHA-RHO",
        "K": 9,
        "branch": branch,
        "scope": "RREF_SPARSE_ALPHA_RHO_NECESSARY_SUBSYSTEM",
        "normalization": {
            "CST": 1,
            "mu": "variable",
            "mu_localizer": "mu*mu_inv-1",
            "y_or_y_minus_x_localized": False,
        },
        "coverage": {
            "terminal": "N4=0, N5=0, N6=+Theta9 after exact h4/h5/h6 RREF",
            "alpha_solved_bands": list(range(6)),
            "rho_high_zero_band_indices": list(range(6, 11)),
            "rho_positive_matches": {"11": "q0/3=rho3", "12": "q1/3=rho2", "13": "q2/3=rho1"},
            "rho_scalar_band_14": "free (absorbed by lambda); no q3/3 equation",
            "E_MASTER_ID6_rows": 0,
        },
        "split_coverage": {
            "A": "y|v, parameterized as v=y*w",
            "B": "y|(y-x)v^2-12mu*p2, parameterized with y*zeta",
            "union": "exhaustive because y is prime; intersection retained in both",
            "this_chart": branch,
        },
        "variables": solver_variables,
        "weights": solver_weights,
        "variable_count": len(solver_variables),
        "row_count": len(rows),
        "global_generator_count": 1,
        "row_family_counts": dict(sorted(family_counts.items())),
        "intended_stage_order": [
            "t00_terminal",
            "t10_alpha_divisibility_n0_through_n5",
            "t20_rho_zero_and_positive_match_n6_through_n13",
        ],
        "manifest_order_note": "band prefixes encode the intended lexical incremental order",
        "terminal_rref_audit": state["formula_controls"].get("terminal_RREF"),
        "alpha_rref_audit": alpha_audits,
        "residual_band_audit": residual_audits,
        "formula_controls": {
            key: value
            for key, value in state["formula_controls"].items()
            if key != "terminal_RREF"
        },
        "denominator_lcm": denominator_value,
        "reconstruction": {
            "omitted_from_metadata_to_bound_symbolic_serialization": True,
            "replay": "rebuild ChartBuilder(9,branch,'terminal',terminal_rref=True).coordinate_state and sparse alpha bands",
            "rho_positive_target": "q0/3 at degree 3; q1/3 at degree 2; q2/3 at degree 1; rho0 free",
        },
        "solver_ring": ring,
        "band_manifest": manifest["manifest_path"],
        "band_union_checksum": manifest["generator_union_checksum"],
        "solver_rows": [
            {
                "label": row.label,
                "band": row.band,
                "degree": row.degree,
                "expr": row.expr,
                "source": dict(row.source),
            }
            for row in rows
        ],
        "chart_sha256": chart_sha256,
        "build_seconds": round(time.monotonic() - started, 6),
        "fallacy_v2": {
            "unit_mod_p": "F_p-only until exact-Q confirmation",
            "posdim": "necessary subsystem only; not a point or counterexample",
        },
    }
    metadata_path = output / "sparse-rho-chart.json"
    atomic_write(metadata_path, json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    trace("metadata_emitted", bytes=metadata_path.stat().st_size)
    result = {
        "K": 9,
        "branch": branch,
        "variables": len(solver_variables),
        "rows": len(rows),
        "row_family_counts": dict(sorted(family_counts.items())),
        "denominator_lcm": denominator_value,
        "chart_sha256": chart_sha256,
        "band_union_checksum": manifest["generator_union_checksum"],
        "build_seconds": metadata["build_seconds"],
        "metadata": str(metadata_path),
    }
    print(json.dumps(result, sort_keys=True))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag")
    parser.add_argument("--branch", choices=("A", "B"), required=True)
    args = parser.parse_args()
    build(args.branch, args.tag)


if __name__ == "__main__":
    main()
