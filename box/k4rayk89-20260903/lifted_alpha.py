#!/usr/bin/env python3
"""Lifted-alpha fallback for the K=9 explicit lower-band charts.

The post-terminal-RREF coordinate state is supplied by ``explicit_bands``.
Instead of expanding the six solved alpha bands, this helper retains the 21
coefficients of an arbitrary polynomial alpha of total degree at most five and
imposes, band by band,

    beta^2 - h*alpha = 0                 in total degrees 14,...,4,
    beta^2 - h*alpha = q0/3,q1/3,q2/3   in total degrees 3,2,1.

The degree-zero difference is the free scalar rho_0.  Since h is monic of
y-degree nine, projection away from the alpha auxiliaries is exactly the
``quo_y(beta^2,h)``/actual-rho chart.  This file never fixes mu; it retains
``mu*mu_inv-1``.  It emits durable band files and can submit the cumulative
system through guided_gb, one characteristic and one core at a time.
"""

from __future__ import annotations

import argparse
from collections import Counter
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
RUNS = HERE / "explicit-runs" / "lifted-alpha"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

from box.lib.guided_gb import (  # noqa: E402
    GuidedGBResult,
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)
from box.lib.staged_band_emitter import (  # noqa: E402
    BandEmitConfig,
    BandRow,
    emit_staged_band_files,
)
from explicit_bands import (  # noqa: E402
    ChartBuilder,
    CoordPoly,
    atomic_write,
)


GOOD_PRIMES = (32003, 32009, 32027)
MAX_TIMEOUT = 600


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def alpha_form(index: int) -> tuple[CoordPoly, list[sp.Symbol]]:
    degree = 5 - index
    poly: CoordPoly = {}
    symbols: list[sp.Symbol] = []
    for i in range(degree + 1):
        j = degree - i
        symbol = sp.Symbol(f"alpha{index}_{i}_{j}")
        poly[(i, j)] = symbol
        symbols.append(symbol)
    return poly, symbols


def cp_add_factored(*polys: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    """Add coordinate maps without distributing their parameter products."""

    out: CoordPoly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, sp.Integer(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient != 0}


def cp_mul_factored(
    left: Mapping[tuple[int, int], sp.Expr],
    right: Mapping[tuple[int, int], sp.Expr],
) -> CoordPoly:
    """Multiply coordinate maps while retaining a factored coefficient DAG."""

    out: CoordPoly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            out[monomial] = out.get(monomial, sp.Integer(0)) + a * b
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient != 0}


def cp_scale_factored(
    poly: Mapping[tuple[int, int], sp.Expr], scalar: sp.Expr
) -> CoordPoly:
    return {
        monomial: scalar * coefficient
        for monomial, coefficient in poly.items()
        if coefficient != 0
    }


def beta_square_band(index: int, pbands: Mapping[int, CoordPoly]) -> CoordPoly:
    return cp_add_factored(
        *(
            cp_mul_factored(pbands[a], pbands[index - a])
            for a in range(index + 1)
            if a in pbands and index - a in pbands
        )
    )


def h_alpha_band(
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


def clear_row(
    expression: sp.Expr,
    *,
    label: str,
    band: str,
    degree: int,
    source: Mapping[str, Any],
) -> tuple[BandRow, int]:
    # ``together`` clears only the numeric Q-denominator while preserving the
    # factored parameter-expression DAG.  Expanding these lifted rows is both
    # unnecessary and, after terminal RREF, disproportionately expensive.
    integral, denominator = sp.fraction(sp.together(expression))
    if not denominator.is_Integer:
        raise AssertionError(f"non-numeric denominator in {label}: {denominator}")
    multiplier = abs(int(denominator))
    if int(denominator) < 0:
        integral = -integral
    encoded = sp.sstr(integral, order="lex").replace("**", "^")
    if re.search(r"/\s*[0-9]+", encoded):
        raise AssertionError(f"uncleared numeric denominator in {label}")
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


def ordered_ring(
    variables: Sequence[sp.Symbol],
    weights: Mapping[sp.Symbol, int],
    characteristic: int,
) -> tuple[str, list[str], list[int]]:
    def key(symbol: sp.Symbol) -> tuple[int, int, str]:
        # Keep the Rabinowitsch inverse last.  Among equal correct grading
        # weights, lifted alpha auxiliaries lead the geometric coefficients.
        if str(symbol) == "mu_inv":
            return (10**9, 1, str(symbol))
        return (-int(weights[symbol]), 0 if str(symbol).startswith("alpha") else 1, str(symbol))

    ordered = sorted(variables, key=key)
    names = [str(symbol) for symbol in ordered]
    ordered_weights = [int(weights[symbol]) for symbol in ordered]
    ring = (
        f"ring SS={characteristic},({','.join(names)}),"
        f"wp({','.join(str(weight) for weight in ordered_weights)});"
    )
    return ring, names, ordered_weights


def build(branch: str, tag: str, characteristic: int = 0) -> dict[str, Any]:
    if branch not in ("A", "B"):
        raise ValueError("K=9 branch must be A or B")
    started = time.monotonic()
    builder = ChartBuilder(
        9,
        branch,
        "terminal",
        terminal_rref=True,
        coordinate_state_only=True,
    )
    terminal = builder.build()
    if builder.coordinate_state is None:
        raise AssertionError("missing terminal coordinate state")
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
    alpha_symbols: list[sp.Symbol] = []
    for index in range(6):
        band, symbols = alpha_form(index)
        alpha_bands[index] = band
        alpha_symbols.extend(symbols)
        # alpha monomial degree is 5-index; its coefficient grading is
        # 3K-degree = 27-(5-index) = 22+index.
        for symbol in symbols:
            weights[symbol] = 22 + index
    variables = [*alpha_symbols, *variables]

    band_audit: list[dict[str, Any]] = []
    for n in range(14):
        degree = 14 - n
        residual = cp_add_factored(
            beta_square_band(n, pbands),
            cp_scale_factored(h_alpha_band(n, hbands, alpha_bands), -1),
        )
        if n >= 11:
            q_index = n - 11
            residual = cp_add_factored(
                residual, cp_scale_factored(qbands[q_index], -sp.Rational(1, 3))
            )
            family = "RHO_POSITIVE_MATCH"
        elif n >= 6:
            q_index = None
            family = "RHO_HIGH_ZERO"
        else:
            q_index = None
            family = "ALPHA_LIFTED_DIV"
        emitted = 0
        for (i, j), expression in sorted(residual.items()):
            if i + j != degree:
                raise AssertionError(f"D_{n} coordinate {(i,j)} has wrong degree")
            if expression == 0:
                continue
            row, multiplier = clear_row(
                expression,
                label=f"D_n{n}_x{i}_y{j}",
                band=f"t{10 if n < 6 else 20:02d}_n{n:02d}_{family}",
                degree=degree,
                source={
                    "kind": family,
                    "band_index": n,
                    "x_power": i,
                    "y_power": j,
                    "rho_q_index": q_index,
                },
            )
            rows.append(row)
            denominators.append(multiplier)
            emitted += 1
        band_audit.append(
            {
                "band_index": n,
                "total_degree": degree,
                "condition": "zero" if n <= 10 else f"q{n-11}/3",
                "coordinate_count": len(residual),
                "emitted_row_count": emitted,
            }
        )

    if len(alpha_symbols) != 21:
        raise AssertionError("lifted alpha must have exactly 21 coefficients")
    if len(set(variables)) != len(variables):
        raise AssertionError("duplicate solver variable")
    declared = {str(symbol) for symbol in variables}
    for row in rows:
        unknown = set(re.findall(r"\b[A-Za-z_]\w*\b", row.expr)) - declared
        if unknown:
            raise AssertionError(f"{row.label} has undeclared names {sorted(unknown)}")
    denominator_value = math.lcm(terminal.denominator_lcm, *denominators)
    if characteristic and denominator_value % characteristic == 0:
        raise ValueError(f"bad characteristic {characteristic}")
    ring, solver_variables, solver_weights = ordered_ring(variables, weights, characteristic)
    fingerprint_payload = json.dumps(
        {
            "K": 9,
            "branch": branch,
            "scope": "TERMINAL_RREF_LIFTED_ALPHA_EXACT_RHO",
            "variables": solver_variables,
            "weights": solver_weights,
            "rows": [(row.label, row.band, row.degree, row.expr) for row in rows],
            "global": [("mu_localizer", "mu*mu_inv-1")],
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    chart_sha256 = sha256_text(fingerprint_payload)
    output = RUNS / tag / f"K9_{branch}" / f"emitted_p{characteristic}"
    manifest = emit_staged_band_files(
        rows,
        BandEmitConfig(
            output_dir=output,
            ring=ring,
            option_lines=("option(redSB);", "short=0;"),
            global_generators=(("mu_localizer", "mu*mu_inv-1"),),
            manifest_name="bands-manifest.json",
        ),
    )
    metadata = {
        "type": "K4RAY-K9-LIFTED-ALPHA-RHO",
        "K": 9,
        "branch": branch,
        "scope": "TERMINAL_RREF_LIFTED_ALPHA_EXACT_RHO",
        "projection_equivalence": (
            "h is monic of y-degree 9; D=beta^2-h*alpha has only a free scalar "
            "term, hence alpha=quo_y(beta^2,h) and D=rho0 plus the prescribed "
            "q0/3,q1/3,q2/3 bands"
        ),
        "normalization": {
            "CST": 1,
            "mu": "variable",
            "mu_localizer": "mu*mu_inv-1",
            "mu_set_to_one": False,
        },
        "coverage": {
            "terminal": "N4=0,N5=0,N6=+Theta9 after h4/h5/h6 RREF",
            "D_zero_degrees": list(range(14, 3, -1)),
            "rho_positive": {"3": "q0/3", "2": "q1/3", "1": "q2/3"},
            "rho0": "free",
            "q3_not_used_as_rho": True,
        },
        "variables": solver_variables,
        "weights": solver_weights,
        "variable_count": len(solver_variables),
        "lifted_alpha_variable_count": len(alpha_symbols),
        "row_count": len(rows),
        "row_family_counts": dict(sorted(Counter(row.source["kind"] for row in rows).items())),
        "terminal_rref_audit": state["formula_controls"].get("terminal_RREF"),
        "band_audit": band_audit,
        "denominator_lcm": denominator_value,
        "solver_ring": ring,
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
        "band_manifest": manifest["manifest_path"],
        "band_union_checksum": manifest["generator_union_checksum"],
        "chart_sha256": chart_sha256,
        "build_seconds": round(time.monotonic() - started, 6),
        "fallacy_v2": {
            "modular_unit": "F_p-only until exact-Q confirmation",
            "posdim": "not a counterexample and not a full-chart survivor",
        },
    }
    metadata_path = output.parent / "lifted-alpha-chart.json"
    atomic_write(metadata_path, json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    return {
        "chart": metadata,
        "rows": rows,
        "variables": variables,
        "weights_by_symbol": weights,
        "metadata_path": str(metadata_path),
        "manifest": manifest,
    }


def summarize(result: GuidedGBResult) -> dict[str, Any]:
    return {
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "runs": [
            {
                "characteristic": run["characteristic"],
                "returncode": run["returncode"],
                "timed_out": run["timed_out"],
                "elapsed_seconds": run["elapsed_seconds"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "basis_size": run["main"]["basis_size"],
                "nf_all_zero": run["main"]["nf_all_zero"],
                "missing_markers": run["main"]["missing_markers"],
                "script": run["script"],
                "stdout": run["stdout"],
            }
            for run in result.certificate["runs"]
        ],
    }


def run_system(
    built: Mapping[str, Any], characteristic: int, output_dir: Path, timeout: int
) -> GuidedGBResult:
    metadata = built["chart"]
    rows: Sequence[BandRow] = built["rows"]
    variables: Sequence[sp.Symbol] = built["variables"]
    weights: Mapping[sp.Symbol, int] = built["weights_by_symbol"]
    ring, names, _ordered_weights = ordered_ring(variables, weights, characteristic)
    system = SingularSystem(
        name=f"K9_{metadata['branch']}_lifted_alpha_p{characteristic}",
        prelude="\n".join(("option(redSB); short=0;", ring, 'print("LIFTED__PRELUDE 1");')),
        generators=tuple([row.expr for row in rows] + ["mu*mu_inv-1"]),
        characteristic=characteristic,
        variables=tuple(names),
        homogeneous=False,
        positive_weights=(),
        metadata={
            "scope": metadata["scope"],
            "chart_sha256": metadata["chart_sha256"],
            "inhomogeneous_localization": True,
        },
    )
    return guided_groebner(
        system,
        hint=None,
        policy=PromotionPolicy.exact_q(
            "lifted-alpha inhomogeneous chart; modular units are never promoted"
        ),
        config=RunConfig(
            output_dir=output_dir,
            timeout_seconds=timeout,
            total_cores=1,
            max_parallel_jobs=1,
            run_perturbed_control=False,
            no_rc=True,
        ),
    )


def command_build(args: argparse.Namespace) -> None:
    built = build(args.branch, args.tag, args.characteristic)
    metadata = built["chart"]
    print(
        json.dumps(
            {
                "K": 9,
                "branch": args.branch,
                "variables": metadata["variable_count"],
                "rows": metadata["row_count"],
                "chart_sha256": metadata["chart_sha256"],
                "build_seconds": metadata["build_seconds"],
                "metadata": built["metadata_path"],
            },
            sort_keys=True,
        )
    )


def command_run(args: argparse.Namespace) -> None:
    if not 1 <= args.timeout <= MAX_TIMEOUT:
        raise ValueError(f"timeout must lie in [1,{MAX_TIMEOUT}]")
    primes = tuple(int(piece) for piece in args.primes.split(",") if piece)
    built = build(args.branch, args.tag, 0)
    metadata = built["chart"]
    base = RUNS / args.tag / f"K9_{args.branch}" / "guided"
    prime_results: list[dict[str, Any]] = []
    for prime in primes:
        if metadata["denominator_lcm"] % prime == 0:
            raise ValueError(f"bad prime {prime}")
        prime_results.append(
            summarize(run_system(built, prime, base / f"p{prime}", args.timeout))
        )
    runs = [run for item in prime_results for run in item["runs"]]
    all_prime_unit = len(runs) == len(primes) and all(
        run["returncode"] == 0
        and not run["timed_out"]
        and run["unit"]
        and run["nf_all_zero"]
        and not run["missing_markers"]
        for run in runs
    )
    exact = None
    if all_prime_unit and args.exact_confirm:
        exact = summarize(run_system(built, 0, base / "exact_Q", args.timeout))
    verdict = exact["verdict"] if exact else ("MODULAR_ONLY" if all_prime_unit else "OPEN")
    summary = {
        "type": "K4RAY-K9-LIFTED-ALPHA-GUIDED",
        "K": 9,
        "branch": args.branch,
        "chart_sha256": metadata["chart_sha256"],
        "primes": list(primes),
        "per_call_timeout_seconds": args.timeout,
        "total_cores": 1,
        "prime_results": prime_results,
        "all_requested_primes_unit": all_prime_unit,
        "exact_result": exact,
        "verdict": verdict,
        "no_modular_promotion": True,
    }
    summary_path = base / "summary.json"
    atomic_write(summary_path, json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": verdict, "summary": str(summary_path)}, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("tag")
    build_parser.add_argument("--branch", choices=("A", "B"), required=True)
    build_parser.add_argument("--characteristic", type=int, default=0)
    build_parser.set_defaults(handler=command_build)
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("tag")
    run_parser.add_argument("--branch", choices=("A", "B"), required=True)
    run_parser.add_argument("--primes", default=",".join(str(value) for value in GOOD_PRIMES))
    run_parser.add_argument("--timeout", type=int, default=600)
    run_parser.add_argument("--exact-confirm", action="store_true")
    run_parser.set_defaults(handler=command_run)
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
