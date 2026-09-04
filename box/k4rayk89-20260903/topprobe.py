#!/usr/bin/env python3
"""Minimal formal-quotient top-band probe for the K=8 and K=9 rows.

This is an intentionally small necessary-condition chart.  Write

    h    = H + h_1 + h_2 + ...,
    beta = P + beta_1 + beta_2 + ...,

where ``H=y^(K-1)(y-x)``, ``P=mu*y^(K-3)(y-x)``, and the subscript is
the loss of total degree from the leading form.  If

    beta^3 = h^2 (C_0 + C_1 + ...),

then its loss-n band is

    R_n = T_n - sum_(i=1)^n S_i C_(n-i) - H^2 C_n,
    T_n = sum_(a+b+c=n) beta_a beta_b beta_c,
    S_n = sum_(a+b=n) h_a h_b.

Here ``C_0=mu^3*y^(K-7)(y-x)``.  The positive-degree quotient bands C_i
are arbitrary homogeneous forms of degree K-6-i.  Once that degree is
negative they are zero.  At n*=2K-12, the formal H^2*C_n term is replaced
by the charged terminal form Theta for Jacobian target coefficient c=1.

The driver emits durable per-band files using staged_band_emitter, submits
cumulative prefixes to guided_gb over good primes, and confirms over exact Q
only when a modular prefix is a unit.  Every Singular process is bounded and
gets exactly one core.  A modular unit is always reported as F_p-only unless
the exact-Q replay also reduces 1 to zero.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
ARTIFACTS = HERE / "topprobe-artifacts"
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
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


SUPPORTED_K = (8, 9)
GOOD_PRIMES = (32003, 32009, 32027)
MAX_CORES = 3


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def singular_expr(expr: sp.Expr) -> str:
    """Return a stable expanded expression accepted by Singular."""

    return sp.sstr(sp.expand(expr), order="lex").replace("**", "^")


def homogeneous_form(
    prefix: str,
    degree: int,
    x: sp.Symbol,
    y: sp.Symbol,
    *,
    omit_pure_y: bool = False,
) -> tuple[sp.Expr, list[sp.Symbol]]:
    """Create a full binary form, optionally omitting its pure-y coordinate."""

    if degree < 0:
        return sp.Integer(0), []
    symbols: list[sp.Symbol] = []
    terms: list[sp.Expr] = []
    for x_power in range(degree + 1):
        if omit_pure_y and x_power == 0:
            continue
        symbol = sp.Symbol(f"{prefix}_x{x_power}")
        symbols.append(symbol)
        terms.append(symbol * x**x_power * y ** (degree - x_power))
    return sp.Add(*terms), symbols


def clear_constant_denominator(expr: sp.Expr) -> tuple[sp.Expr, int]:
    """Clear the rational scalar denominator of a coefficient row."""

    together = sp.together(expr)
    numerator, denominator = sp.fraction(together)
    if not denominator.is_Integer:
        raise ValueError(f"nonconstant denominator in recurrence row: {denominator}")
    den = abs(int(denominator))
    numerator = sp.expand(numerator if int(denominator) > 0 else -numerator)
    if numerator == 0:
        return numerator, 1
    return numerator, den


def theta_form(K: int, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    if K == 8:
        core = (
            195 * x**4
            + 240 * x**3 * y
            + 320 * x**2 * y**2
            + 512 * x * y**3
            + 2048 * y**4
        )
        denominator = 6630
    elif K == 9:
        core = (
            35 * x**4
            + 42 * x**3 * y
            + 54 * x**2 * y**2
            + 81 * x * y**3
            + 243 * y**4
        )
        denominator = 1365
    else:
        raise ValueError(f"no charged terminal form registered for K={K}")
    return sp.expand(y**K * (y - x) ** 2 * core / sp.Integer(denominator))


def jacobian(left: sp.Expr, right: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.diff(left, x) * sp.diff(right, y) - sp.diff(left, y) * sp.diff(right, x))


@dataclass
class TopProbe:
    K: int
    variables: list[str]
    weights: list[int]
    rows: list[BandRow]
    stage_numbers: list[int]
    stage_descriptions: dict[int, str]
    denominator_multipliers: dict[str, int]
    audit: dict[str, Any]

    @property
    def global_generators(self) -> tuple[tuple[str, str], ...]:
        return (("mu_localizer", "mu*mu_inv-1"),)

    def rows_through(self, stage: int) -> list[BandRow]:
        return [row for row in self.rows if int(row.source["n"]) <= stage]


def build_probe(K: int) -> TopProbe:
    if K not in SUPPORTED_K:
        raise ValueError(f"K must be one of {SUPPORTED_K}")

    x, y = sp.symbols("x y")
    mu = sp.Symbol("mu")
    mu_inv = sp.Symbol("mu_inv")
    n_terminal = 2 * K - 12
    H = sp.expand(y ** (K - 1) * (y - x))
    P = sp.expand(mu * y ** (K - 3) * (y - x))
    C0 = sp.expand(mu**3 * y ** (K - 7) * (y - x))
    theta = theta_form(K, x, y)

    h: dict[int, sp.Expr] = {0: H}
    beta: dict[int, sp.Expr] = {0: P}
    C: dict[int, sp.Expr] = {0: C0}
    symbol_data: dict[str, tuple[int, str]] = {
        "mu": (K + 2, "mu"),
        "mu_inv": (1, "localizer"),
    }

    for n in range(1, n_terminal + 1):
        h[n], h_symbols = homogeneous_form(
            f"h{n}", K - n, x, y, omit_pure_y=(n == 1)
        )
        beta[n], beta_symbols = homogeneous_form(f"beta{n}", K - 2 - n, x, y)
        for symbol in h_symbols:
            symbol_data[str(symbol)] = (n, "h")
        for symbol in beta_symbols:
            # This is the positive chart grading used by the pinned chart:
            # w(beta coefficient at loss n) = K+2+n.
            symbol_data[str(symbol)] = (K + 2 + n, "beta")

    last_free_C = K - 6
    for n in range(1, last_free_C + 1):
        C[n], c_symbols = homogeneous_form(f"C{n}", K - 6 - n, x, y)
        for symbol in c_symbols:
            symbol_data[str(symbol)] = (3 * K + 6 + n, "C")
    for n in range(last_free_C + 1, n_terminal + 1):
        C[n] = sp.Integer(0)

    # A band-first ordering puts newly entering variables before older ones
    # inside the weighted-degree reverse-lex order.  All weights are positive.
    def variable_key(name: str) -> tuple[int, int, str]:
        weight, family = symbol_data[name]
        family_rank = {"C": 0, "beta": 1, "h": 2, "mu": 3, "localizer": 4}[family]
        return (-weight, family_rank, name)

    variable_symbols = sorted(
        {symbol for expr in [*h.values(), *beta.values(), *C.values()] for symbol in expr.free_symbols}
        - {x, y},
        key=lambda symbol: variable_key(str(symbol)),
    )
    # mu is already present in P/C0; mu_inv only occurs in the global row.
    variable_names = [str(symbol) for symbol in variable_symbols]
    if "mu" not in variable_names:
        variable_names.append("mu")
    variable_names.append("mu_inv")
    variable_names = sorted(set(variable_names), key=variable_key)
    weights = [symbol_data[name][0] for name in variable_names]

    rows: list[BandRow] = []
    denominator_multipliers: dict[str, int] = {}
    stage_descriptions: dict[int, str] = {}
    top_degree = 3 * K - 6

    for n in range(1, n_terminal + 1):
        Tn = sp.Add(
            *(
                beta[a] * beta[b] * beta[n - a - b]
                for a in range(n + 1)
                for b in range(n - a + 1)
            )
        )
        Sn: dict[int, sp.Expr] = {
            i: sp.Add(*(h[a] * h[i - a] for a in range(i + 1)))
            for i in range(1, n + 1)
        }
        quotient_tail = sp.Add(*(Sn[i] * C[n - i] for i in range(1, n + 1)))
        terminal_term = theta if n == n_terminal else H**2 * C[n]
        recurrence = sp.expand(Tn - quotient_tail - terminal_term)
        expected_degree = top_degree - n
        polynomial = sp.Poly(recurrence, x, y)
        degrees = {sum(monomial) for monomial, coefficient in polynomial.terms() if coefficient != 0}
        if degrees and degrees != {expected_degree}:
            raise AssertionError(f"K={K} n={n}: wrong x,y degrees {degrees}, expected {expected_degree}")

        if n <= last_free_C:
            stage_descriptions[n] = f"C{n} arbitrary of degree {K - 6 - n}"
        elif n < n_terminal:
            stage_descriptions[n] = f"C{n}=0 (negative quotient degree)"
        else:
            stage_descriptions[n] = f"C{n}=Theta (charged CST=1 terminal replacement)"

        coefficients = {monomial: coefficient for monomial, coefficient in polynomial.terms()}
        for x_power in range(expected_degree + 1):
            monomial = (x_power, expected_degree - x_power)
            coefficient = sp.expand(coefficients.get(monomial, 0))
            if coefficient == 0:
                continue
            cleared, multiplier = clear_constant_denominator(coefficient)
            label = f"K{K}_n{n}_x{x_power}_y{expected_degree - x_power}"
            denominator_multipliers[label] = multiplier
            rows.append(
                BandRow(
                    label=label,
                    band=f"n{n:02d}",
                    degree=n,
                    expr=singular_expr(cleared),
                    source={
                        "K": K,
                        "n": n,
                        "x_power": x_power,
                        "y_power": expected_degree - x_power,
                        "xy_total_degree": expected_degree,
                        "stage": stage_descriptions[n],
                        "cleared_denominator_multiplier": multiplier,
                    },
                )
            )

    R0 = sp.expand(P**3 - H**2 * C0)
    theta_jacobian_residual = sp.expand(jacobian(H, theta, x, y) - x**4 * H**2)
    audit = {
        "K": K,
        "n_terminal": n_terminal,
        "H": singular_expr(H),
        "P": singular_expr(P),
        "C0": singular_expr(C0),
        "Theta": singular_expr(theta),
        "R0_zero": R0 == 0,
        "theta_J_equals_x4_H2": theta_jacobian_residual == 0,
        "h1_pure_y_coordinate_absent": f"h1_x0" not in symbol_data,
        "free_C_last_index": last_free_C,
        "intermediate_zero_C": [
            n for n in range(last_free_C + 1, n_terminal) if C[n] == 0
        ],
        "stage_row_counts": {
            str(n): sum(int(row.source["n"]) == n for row in rows)
            for n in range(1, n_terminal + 1)
        },
        "row_count": len(rows),
        "variable_count": len(variable_names),
        "variables": variable_names,
        "weights": weights,
        "order": "wp (weighted degree reverse lexicographic in Singular)",
        "target_normalization": "CST=1 is built into Theta; no modular-to-Q lift is used",
        "localization": "mu*mu_inv-1",
    }
    if not all(
        (
            audit["R0_zero"],
            audit["theta_J_equals_x4_H2"],
            audit["h1_pure_y_coordinate_absent"],
        )
    ):
        raise AssertionError(f"formal-quotient construction audit failed: {audit}")

    return TopProbe(
        K=K,
        variables=variable_names,
        weights=weights,
        rows=rows,
        stage_numbers=list(range(1, n_terminal + 1)),
        stage_descriptions=stage_descriptions,
        denominator_multipliers=denominator_multipliers,
        audit=audit,
    )


def build_pin12_k8_probe() -> TopProbe:
    """K=8 pointwise PIN12/K8-H3 parametrization of the same top subsystem.

    This uses only divisions by powers of ``mu``.  We clear the remaining
    denominator from the terminal recurrence and retain ``mu*mu_inv-1``, so
    the emitted polynomial system is equivalent on the requested localized
    chart.  No division by y or y-x appears in the emitted equations.
    """

    K = 8
    x, y = sp.symbols("x y")
    mu = sp.Symbol("mu")
    mu_inv = sp.Symbol("mu_inv")
    L = y - x
    H = y**7 * L
    P = mu * y**5 * L
    q0 = mu**3 * y * L

    # tau=tau_y*y+tau_x*x.  The monic h normalization and phi=y*v give
    # v_y=2*tau_y, so v has only one additional coordinate.
    tau_y, tau_x, v_x, chi = sp.symbols("tau_y tau_x v_x chi")
    tau = tau_y * y + tau_x * x
    v = 2 * tau_y * y + v_x * x
    phi = y * v

    p2, p2_symbols = homogeneous_form("beta2", 4, x, y)
    p3, p3_symbols = homogeneous_form("beta3", 3, x, y)
    p4, p4_symbols = homogeneous_form("beta4", 2, x, y)
    h4, h4_symbols = homogeneous_form("h4", 4, x, y)

    p1 = sp.expand(y**2 * (3 * y**2 * tau - L * phi))
    h1 = sp.cancel((3 * y**6 * tau - sp.Rational(3, 2) * y**4 * L * phi) / mu)
    h2 = sp.cancel(
        sp.Rational(3, 2)
        * (mu * y**2 * p2 + sp.Rational(1, 4) * y * L * phi**2 - y**6 * chi)
        / mu**2
    )
    h3 = sp.cancel(
        (
            L * y * v**3
            + 36 * chi * v * y**4
            + 24 * mu**2 * p3 * y**2
            - 12 * mu * p2 * v
            - 18 * v**2 * tau * y**2
        )
        / (16 * mu**3)
    )
    q1 = 3 * mu**2 * tau
    q2 = 3 * mu * chi
    theta = theta_form(K, x, y)

    T4 = 3 * P**2 * p4 + 6 * P * p1 * p3 + 3 * P * p2**2 + 3 * p1**2 * p2
    S2 = 2 * H * h2 + h1**2
    S3 = 2 * H * h3 + 2 * h1 * h2
    S4 = 2 * H * h4 + 2 * h1 * h3 + h2**2
    # Every denominator in N4 is at most mu.  Multiplication by mu is an
    # equivalence because the global row localizes mu.
    terminal = sp.cancel(mu * (T4 - S2 * q2 - S3 * q1 - S4 * q0 - theta))
    numerator, denominator = sp.fraction(terminal)
    if denominator != 1:
        raise AssertionError(f"K8 PIN12 terminal denominator did not clear: {denominator}")
    terminal = sp.expand(numerator)

    polynomial = sp.Poly(terminal, x, y)
    expected_degree = 14
    degrees = {sum(monomial) for monomial, coefficient in polynomial.terms() if coefficient != 0}
    if degrees != {expected_degree}:
        raise AssertionError(f"K8 PIN12 terminal degrees {degrees}")
    coefficient_map = dict(polynomial.terms())
    rows: list[BandRow] = []
    denominator_multipliers: dict[str, int] = {}
    for x_power in range(expected_degree + 1):
        monomial = (x_power, expected_degree - x_power)
        coefficient = sp.expand(coefficient_map.get(monomial, 0))
        if coefficient == 0:
            continue
        cleared, multiplier = clear_constant_denominator(coefficient)
        label = f"K8_PIN12_n4_x{x_power}_y{expected_degree - x_power}"
        denominator_multipliers[label] = multiplier
        rows.append(
            BandRow(
                label=label,
                band="n04_pin12",
                degree=4,
                expr=singular_expr(cleared),
                source={
                    "K": 8,
                    "n": 4,
                    "x_power": x_power,
                    "y_power": expected_degree - x_power,
                    "xy_total_degree": expected_degree,
                    "stage": "PIN12 + K8-H3; terminal C4=Theta",
                    "cleared_denominator_multiplier": multiplier,
                },
            )
        )

    weight_by_name: dict[str, int] = {
        "mu": 10,
        "mu_inv": 1,
        "tau_y": 11,
        "tau_x": 11,
        "v_x": 11,
        "chi": 22,
    }
    weight_by_name.update({str(symbol): 12 for symbol in p2_symbols})
    weight_by_name.update({str(symbol): 13 for symbol in p3_symbols})
    weight_by_name.update({str(symbol): 14 for symbol in p4_symbols})
    weight_by_name.update({str(symbol): 4 for symbol in h4_symbols})
    variables = sorted(weight_by_name, key=lambda name: (-weight_by_name[name], name))
    weights = [weight_by_name[name] for name in variables]
    audit = {
        "K": 8,
        "variant": "PIN12_K8_H3",
        "scope": "pointwise-equivalent radical parametrization on mu!=0",
        "terminal_denominator_cleared_by": "mu",
        "no_y_or_y_minus_x_localization": True,
        "h1_pure_y_coordinate_absent": sp.Poly(h1, x, y).coeff_monomial(y**7) == 0,
        "theta_J_equals_x4_H2": sp.expand(jacobian(H, theta, x, y) - x**4 * H**2) == 0,
        "row_count": len(rows),
        "variable_count": len(variables),
        "variables": variables,
        "weights": weights,
        "order": "wp (weighted degree reverse lexicographic in Singular)",
        "localization": "mu*mu_inv-1",
        "target_normalization": "CST=1 built into Theta_8",
        "parametrization": {
            "tau": singular_expr(tau),
            "v": singular_expr(v),
            "phi": singular_expr(phi),
            "beta1": singular_expr(p1),
            "h1": singular_expr(h1),
            "h2": singular_expr(h2),
            "h3": singular_expr(h3),
            "q1": singular_expr(q1),
            "q2": singular_expr(q2),
        },
    }
    if not audit["h1_pure_y_coordinate_absent"] or not audit["theta_J_equals_x4_H2"]:
        raise AssertionError(f"K8 PIN12 audit failed: {audit}")
    return TopProbe(
        K=8,
        variables=variables,
        weights=weights,
        rows=rows,
        stage_numbers=[4],
        stage_descriptions={4: "PIN12 + K8-H3; terminal C4=Theta"},
        denominator_multipliers=denominator_multipliers,
        audit=audit,
    )


def ring_string(probe: TopProbe, characteristic: int) -> str:
    return (
        f"ring R={characteristic},({','.join(probe.variables)}),"
        f"wp({','.join(str(weight) for weight in probe.weights)});"
    )


def emit_probe(probe: TopProbe, output_root: Path = ARTIFACTS) -> dict[str, Any]:
    root = output_root / f"K{probe.K}"
    config = BandEmitConfig(
        output_dir=root / "bands",
        ring=ring_string(probe, 0),
        option_lines=("option(redSB);", "short=0;"),
        global_generators=probe.global_generators,
        manifest_name="topprobe-bands-manifest.json",
    )
    manifest = emit_staged_band_files(probe.rows, config)
    metadata = {
        "type": "K4RAY-FORMAL-QUOTIENT-TOP-PROBE",
        "audit": probe.audit,
        "stages": {str(n): probe.stage_descriptions[n] for n in probe.stage_numbers},
        "denominator_multipliers": probe.denominator_multipliers,
        "manifest": manifest,
        "generator_union_sha256": manifest["generator_union_checksum"],
    }
    metadata_path = root / "topprobe-meta.json"
    atomic_write(metadata_path, json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    return {**metadata, "metadata_path": str(metadata_path)}


def make_system(probe: TopProbe, characteristic: int, stage: int, name: str) -> SingularSystem:
    prefix_rows = probe.rows_through(stage)
    generators = tuple(row.expr for row in prefix_rows) + tuple(
        expression for _label, expression in probe.global_generators
    )
    prelude = "\n".join(
        (
            "option(redSB);",
            "short=0;",
            ring_string(probe, characteristic),
            f'print("TP__K {probe.K}");',
            f'print("TP__STAGE {stage}");',
            f'print("TP__PREFIX_ROWS {len(prefix_rows)}");',
            f'print("TP__VARIABLES {len(probe.variables)}");',
            'print("TP__ORDER wp");',
            'print("TP__LOCALIZER mu*mu_inv-1");',
            'print("TP__PRELUDE_DONE 1");',
        )
    )
    return SingularSystem(
        name=name,
        prelude=prelude,
        generators=generators,
        characteristic=characteristic,
        variables=tuple(probe.variables),
        homogeneous=False,
        positive_weights=(),
        metadata={
            "K": probe.K,
            "stage": stage,
            "stage_description": probe.stage_descriptions[stage],
            "formal_quotient_only": True,
            "target_CST": 1,
        },
    )


def modular_unit_runs(result: Any) -> list[Mapping[str, Any]]:
    return [
        run
        for run in result.certificate.get("runs", [])
        if run.get("characteristic", 0) > 1
        and not run.get("timed_out", False)
        and run.get("returncode") == 0
        and run.get("main", {}).get("accepted", False)
        and run.get("main", {}).get("unit", False)
    ]


def run_probe(
    probe: TopProbe,
    *,
    primes: Sequence[int],
    timeout: int,
    exact_timeout: int,
    output_root: Path = ARTIFACTS,
    exact_confirm: bool = True,
) -> dict[str, Any]:
    if not primes:
        raise ValueError("at least one modular prime is required")
    if len(primes) > MAX_CORES:
        raise ValueError(f"at most {MAX_CORES} primes may run concurrently")
    root = output_root / f"K{probe.K}"
    emit_metadata = emit_probe(probe, output_root)
    stage_results: list[dict[str, Any]] = []
    exact_result: dict[str, Any] | None = None

    for stage in probe.stage_numbers:
        systems = [
            make_system(probe, prime, stage, f"topprobe_K{probe.K}_n{stage}_p{prime}")
            for prime in primes
        ]
        stage_dir = root / "runs" / f"stage-n{stage}" / "modular"
        modular = guided_groebner(
            systems,
            policy=PromotionPolicy(
                note="inhomogeneous localization: modular unit remains F_p-only"
            ),
            config=RunConfig(
                output_dir=stage_dir,
                timeout_seconds=timeout,
                total_cores=len(systems),
                max_parallel_jobs=len(systems),
                run_perturbed_control=False,
            ),
        )
        unit_runs = modular_unit_runs(modular)
        record: dict[str, Any] = {
            "stage": stage,
            "description": probe.stage_descriptions[stage],
            "row_count": len(probe.rows_through(stage)),
            "modular_verdict": modular.verdict.value,
            "modular_units": [run["characteristic"] for run in unit_runs],
            "modular_result": modular.to_json(),
        }

        if unit_runs and exact_confirm:
            exact_system = make_system(probe, 0, stage, f"topprobe_K{probe.K}_n{stage}_Q")
            exact_dir = root / "runs" / f"stage-n{stage}" / "exact-Q"
            exact = guided_groebner(
                exact_system,
                policy=PromotionPolicy.exact_q(
                    note="literal exact-Q replay required after modular unit"
                ),
                config=RunConfig(
                    output_dir=exact_dir,
                    timeout_seconds=exact_timeout,
                    total_cores=1,
                    max_parallel_jobs=1,
                    run_perturbed_control=False,
                ),
            )
            exact_result = exact.to_json()
            record["exact_Q"] = exact_result
            if exact.verdict.value == "UNIT_IDEAL_CHAR0":
                record["terminal_decision"] = "UNIT_IDEAL_CHAR0"
                stage_results.append(record)
                break
            record["terminal_decision"] = exact.verdict.value

        stage_results.append(record)

    final = {
        "type": "K4RAY-FORMAL-QUOTIENT-TOP-PROBE-RUN",
        "K": probe.K,
        "scope": "necessary top recurrence only; not the full pinned chart",
        "fallacy_v2": (
            "modular unit is F_p-only until exact-Q replay; a positive-dimensional "
            "top recurrence is not a counterexample"
        ),
        "primes": list(primes),
        "per_process_cores": 1,
        "timeout_seconds": timeout,
        "exact_timeout_seconds": exact_timeout,
        "emission": emit_metadata,
        "stages": stage_results,
        "exact_result": exact_result,
    }
    if exact_result and exact_result.get("verdict") == "UNIT_IDEAL_CHAR0":
        final["verdict"] = "UNIT_IDEAL_CHAR0"
    elif stage_results and stage_results[-1]["modular_units"]:
        final["verdict"] = "MODULAR_UNIT_UNCONFIRMED"
    elif stage_results and all(
        not run.get("timed_out", False)
        and run.get("returncode") == 0
        and run.get("main", {}).get("accepted", False)
        and not run.get("main", {}).get("missing_markers", [])
        and run.get("main", {}).get("dimension") is not None
        for run in stage_results[-1]["modular_result"]["certificate"]["runs"]
    ):
        final["verdict"] = "TOP_RECURRENCE_SURVIVES_MODULARLY"
    else:
        final["verdict"] = "INCONCLUSIVE_TIMEOUT"
    summary_path = root / "topprobe-run-summary.json"
    atomic_write(summary_path, json.dumps(final, indent=2, sort_keys=True) + "\n")
    final["summary_path"] = str(summary_path)
    return final


def parse_primes(text: str) -> tuple[int, ...]:
    primes = tuple(int(piece) for piece in text.split(",") if piece.strip())
    if any(prime <= 2 for prime in primes):
        raise ValueError("good primes must exceed 2")
    return primes


def compact_result(result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "K": result["K"],
        "verdict": result["verdict"],
        "summary_path": result.get("summary_path"),
        "stages": [
            {
                "stage": stage["stage"],
                "description": stage["description"],
                "row_count": stage["row_count"],
                "modular_verdict": stage["modular_verdict"],
                "modular_units": stage["modular_units"],
                "exact_Q_verdict": stage.get("exact_Q", {}).get("verdict"),
            }
            for stage in result["stages"]
        ],
    }


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "run", "all"))
    parser.add_argument("--K", type=int, choices=SUPPORTED_K)
    parser.add_argument("--primes", default=",".join(str(p) for p in GOOD_PRIMES))
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--exact-timeout", type=int, default=300)
    parser.add_argument("--no-exact-confirm", action="store_true")
    parser.add_argument(
        "--optimized",
        action="store_true",
        help="use the pointwise PIN12/K8-H3 reduction (currently K=8 only)",
    )
    parser.add_argument("--output-root", type=Path, default=ARTIFACTS)
    args = parser.parse_args()

    if args.command in {"build", "run"} and args.K is None:
        parser.error(f"{args.command} requires --K")
    Ks = SUPPORTED_K if args.command == "all" else (args.K,)
    if args.optimized and (args.command == "all" or Ks != (8,)):
        parser.error("--optimized currently requires --K 8 and build/run")
    outputs: list[dict[str, Any]] = []
    for K in Ks:
        assert K is not None
        probe = build_pin12_k8_probe() if args.optimized else build_probe(K)
        output_root = args.output_root / "optimized-pin12" if args.optimized else args.output_root
        if args.command == "build":
            emitted = emit_probe(probe, output_root)
            outputs.append(
                {
                    "K": K,
                    "audit": probe.audit,
                    "metadata_path": emitted["metadata_path"],
                    "manifest_path": emitted["manifest"]["manifest_path"],
                }
            )
        else:
            result = run_probe(
                probe,
                primes=parse_primes(args.primes),
                timeout=args.timeout,
                exact_timeout=args.exact_timeout,
                output_root=output_root,
                exact_confirm=not args.no_exact_confirm,
            )
            outputs.append(compact_result(result))
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    cli()
