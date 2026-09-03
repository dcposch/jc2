#!/usr/bin/env python3
"""Constant-pivot preprocessing for the gauged K=16 order charts.

This program performs only quotient-ring isomorphisms of the following form.
If a current equation is

    f = a*x + b,        a in Q^*,        x not in b,

then it deletes ``f`` and ``x`` and substitutes ``x = -b/a`` in every other
equation.  No polynomial, parameter, or chart-dependent leading coefficient
is inverted.  Rows are visited from the largest h-adic power down, with the
original coefficient-variable order breaking ties.  The rule is therefore
deterministic.

The emitted Singular programs retain the empty/nonempty wrapper controls, an
independent actual-pair Jacobian control, and the Rabinowitsch equation
``T*c-1``.  This script PREPARES those programs; it never invokes Singular.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import importlib.util
import json
import math
import pathlib
import sys
import time
from typing import Iterable

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GENERIC_DRIVER = ROOT / "box/k16t3-20260903/t3/t_order_system.py"
DEDICATED_T4_DRIVER = ROOT / "box/k16t3-20260903/t4/t4_order_system.py"
FROZEN_T2_DRIVER = pathlib.Path(
    "/tmp/jc2-lane.NKyBDU/inputs/t2_order_system.py"
)
FROZEN_T2_CERTIFICATE = pathlib.Path(
    "/tmp/jc2-lane.NKyBDU/inputs/t2_sat_certificate.txt"
)

PRIMES = {
    2: (),
    3: (32003, 32009, 32027),
    4: (32003, 65521, 1000003),
}


@dataclasses.dataclass
class Row:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


@dataclasses.dataclass
class Pivot:
    step: int
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    variable: sp.Symbol
    coefficient: sp.Rational
    step_rhs: sp.Expr
    final_rhs: sp.Expr | None = None


@dataclasses.dataclass
class Reduction:
    t: int
    original_variables: list[sp.Symbol]
    c: sp.Symbol
    original_rows: list[Row]
    remaining_variables: list[sp.Symbol]
    rows: list[Row]
    pivots: list[Pivot]
    zero_source_indices: list[int]
    elapsed_seconds: float


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_module(path: pathlib.Path, name: str):
    if not path.is_file():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import %s" % path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expression_vector_hash(expressions: Iterable[sp.Expr]) -> str:
    return sha256_text("\n".join(str(sp.expand(expr)) for expr in expressions) + "\n")


def assert_same_chart(left: dict, right: dict, label: str) -> dict:
    """Mechanically compare two builders, including ordered tagged rows."""
    left_names = [str(v) for v in left["params"]] + [str(left["c"])]
    right_names = [str(v) for v in right["params"]] + [str(right["c"])]
    if left_names != right_names:
        raise AssertionError("%s: parameter order differs" % label)
    for key in ("h", "A", "B", "z", "P", "Q"):
        if sp.expand(left[key] - right[key]) != 0:
            raise AssertionError("%s: %s differs" % (label, key))
    if len(left["tagged"]) != len(right["tagged"]):
        raise AssertionError("%s: tagged row count differs" % label)
    for index, (lrow, rrow) in enumerate(zip(left["tagged"], right["tagged"])):
        if lrow[:2] != rrow[:2] or sp.expand(lrow[2] - rrow[2]) != 0:
            raise AssertionError("%s: tagged row %d differs" % (label, index))
    return {
        "label": label,
        "parameter_order_equal": True,
        "h_A_B_z_P_Q_equal": True,
        "ordered_tagged_equations_equal": True,
        "equation_count": len(left["tagged"]),
        "equation_vector_sha256": expression_vector_hash(
            row[2] for row in left["tagged"]
        ),
    }


def constant_coefficient(expr: sp.Expr, variable: sp.Symbol):
    """Return a in Q^* when expr=a*variable+b with variable absent from b."""
    if variable not in expr.free_symbols:
        return None
    coefficient = sp.expand(sp.diff(expr, variable))
    if not coefficient.is_Rational or coefficient == 0:
        return None
    remainder = sp.expand(expr - coefficient * variable)
    if variable in remainder.free_symbols:
        return None
    if sp.expand(expr - (coefficient * variable + remainder)) != 0:
        raise AssertionError("failed affine decomposition")
    return sp.Rational(coefficient), remainder


def row_order(item: tuple[int, Row]):
    index, row = item
    return (-row.h_power, row.monomial[0], row.monomial[1], index)


def reduce_chart(
    data: dict,
    max_pivots: int,
    max_seconds: float,
    max_expression_bytes: int,
) -> Reduction:
    started = time.monotonic()
    original_variables = list(data["params"])
    remaining_variables = list(original_variables)
    original_rows = [
        Row(index, h_power, tuple(monomial), sp.expand(expr))
        for index, (h_power, monomial, expr) in enumerate(data["tagged"])
    ]
    rows = [dataclasses.replace(row) for row in original_rows]
    pivots: list[Pivot] = []
    zero_sources: set[int] = set()

    while True:
        if len(pivots) >= max_pivots:
            raise RuntimeError("constant-pivot bound reached before exhaustion")
        if time.monotonic() - started > max_seconds:
            raise RuntimeError("preprocessing time bound exceeded")

        choice = None
        for row_index, row in sorted(enumerate(rows), key=row_order):
            for variable_index, variable in enumerate(remaining_variables):
                affine = constant_coefficient(row.expr, variable)
                if affine is not None:
                    coefficient, remainder = affine
                    choice = (
                        row_index,
                        variable_index,
                        row,
                        variable,
                        coefficient,
                        remainder,
                    )
                    break
            if choice is not None:
                break
        if choice is None:
            break

        (
            row_index,
            variable_index,
            pivot_row,
            variable,
            coefficient,
            remainder,
        ) = choice
        rhs = sp.expand(-remainder / coefficient)
        if variable in rhs.free_symbols:
            raise AssertionError("pivot right side contains pivot variable")
        if sp.expand(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("pivot substitution does not kill pivot row")

        pivots.append(
            Pivot(
                step=len(pivots) + 1,
                source_index=pivot_row.source_index,
                h_power=pivot_row.h_power,
                monomial=pivot_row.monomial,
                variable=variable,
                coefficient=coefficient,
                step_rhs=rhs,
            )
        )
        zero_sources.add(pivot_row.source_index)
        del rows[row_index]
        del remaining_variables[variable_index]

        next_rows = []
        for row in rows:
            expr = row.expr
            if variable in expr.free_symbols:
                expr = sp.expand(expr.subs(variable, rhs))
            if expr == 0:
                zero_sources.add(row.source_index)
            else:
                next_rows.append(dataclasses.replace(row, expr=expr))
        rows = next_rows

        expression_bytes = sum(len(str(row.expr)) for row in rows)
        if expression_bytes > max_expression_bytes:
            raise RuntimeError(
                "expanded residual exceeds byte bound: %d" % expression_bytes
            )

    # Resolve the triangular right sides into the final polynomial ring.
    resolved: dict[sp.Symbol, sp.Expr] = {}
    for pivot in reversed(pivots):
        rhs = sp.expand(pivot.step_rhs.subs(resolved, simultaneous=True))
        if rhs.free_symbols.intersection({p.variable for p in pivots}):
            raise AssertionError("unresolved pivot in final ring map")
        pivot.final_rhs = rhs
        resolved[pivot.variable] = rhs

    # Verify the complete map on every original row, not merely on pivots.
    surviving = {row.source_index: row for row in rows}
    for original in original_rows:
        image = sp.expand(original.expr.subs(resolved, simultaneous=True))
        if original.source_index in surviving:
            if sp.expand(image - surviving[original.source_index].expr) != 0:
                raise AssertionError(
                    "ring-map image differs at source row %d"
                    % original.source_index
                )
        elif image != 0:
            raise AssertionError(
                "deleted source row %d has nonzero ring-map image"
                % original.source_index
            )

    pivot_set = {pivot.variable for pivot in pivots}
    if pivot_set.intersection(remaining_variables):
        raise AssertionError("pivot variable remains in output ring")
    for row in rows:
        if row.expr.free_symbols.intersection(pivot_set):
            raise AssertionError("pivot variable remains in residual equation")
    for pivot in pivots:
        if pivot.final_rhs is None or pivot.final_rhs.free_symbols.intersection(pivot_set):
            raise AssertionError("ring map does not land in reduced ring")

    return Reduction(
        t=int(data["t"]),
        original_variables=original_variables,
        c=data["c"],
        original_rows=original_rows,
        remaining_variables=remaining_variables,
        rows=rows,
        pivots=pivots,
        zero_source_indices=sorted(zero_sources),
        elapsed_seconds=time.monotonic() - started,
    )


def primitive_integer_polynomial(
    expr: sp.Expr, variables: list[sp.Symbol]
) -> tuple[sp.Poly, sp.Rational, int, int]:
    """Return primitive g in ZZ[V] and lambda in Q* with g=lambda*expr."""
    polynomial = sp.Poly(expr, *variables, domain=sp.QQ)
    denominator_lcm, cleared = polynomial.clear_denoms(convert=True)
    content, primitive = cleared.primitive()
    multiplier = sp.Rational(denominator_lcm, content)
    if primitive.LC() < 0:
        primitive = -primitive
        multiplier = -multiplier
    if sp.expand(primitive.as_expr() - multiplier * expr) != 0:
        raise AssertionError("primitive integer normalization identity failed")
    return primitive, multiplier, int(denominator_lcm), abs(int(content))


def singular_polynomial(expr: sp.Expr, variables: list[sp.Symbol]) -> str:
    """Render the proof-equivalent primitive integer multiple of a Q-row."""
    polynomial, _multiplier, _denominator_lcm, _content = (
        primitive_integer_polynomial(expr, variables)
    )
    rendered: list[str] = []
    for monomial, coefficient in polynomial.terms():
        coefficient = sp.Integer(coefficient)
        if coefficient == 0:
            continue
        factors = []
        for variable, exponent in zip(variables, monomial):
            if exponent == 1:
                factors.append(str(variable))
            elif exponent > 1:
                factors.append("%s^%d" % (variable, exponent))
        monomial_text = "*".join(factors)
        magnitude = abs(coefficient)
        if monomial_text and magnitude == 1:
            body = monomial_text
        else:
            scalar = str(magnitude)
            body = scalar if not monomial_text else scalar + "*" + monomial_text
        if not rendered:
            rendered.append(("-" if coefficient < 0 else "") + body)
        else:
            rendered.append((" - " if coefficient < 0 else " + ") + body)
    return "".join(rendered) if rendered else "0"


def coefficient_bad_primes(reduction: Reduction) -> list[int]:
    """Primes at which a Q-precomputed pivot is not a valid field pivot."""
    bad = {2}  # the independent actual-pair control uses 1/2
    for pivot in reduction.pivots:
        for integer in pivot.coefficient.as_numer_denom():
            integer = abs(int(integer))
            if integer > 1:
                bad.update(int(p) for p in sp.factorint(integer))
    # Denominators in every emitted coefficient must also remain units.
    variables = reduction.remaining_variables + [reduction.c]
    expressions = [row.expr for row in reduction.rows]
    expressions.extend(
        pivot.final_rhs for pivot in reduction.pivots if pivot.final_rhs is not None
    )
    for expr in expressions:
        for coefficient in sp.Poly(expr, *variables, domain=sp.QQ).coeffs():
            denominator = abs(int(sp.denom(coefficient)))
            if denominator > 1:
                bad.update(int(p) for p in sp.factorint(denominator))
    # Emission replaces each rational row f by a primitive integral row
    # g=lambda*f.  Both numerator and denominator of lambda must remain units
    # for the same emitted file to represent the reduced ideal over GF(p).
    for row in reduction.rows:
        _primitive, multiplier, _denominator_lcm, _content = (
            primitive_integer_polynomial(row.expr, variables)
        )
        for integer in multiplier.as_numer_denom():
            integer = abs(int(integer))
            if integer > 1:
                bad.update(int(p) for p in sp.factorint(integer))
    return sorted(bad)


def emit_singular(reduction: Reduction, characteristic: int) -> str:
    if characteristic < 0:
        raise ValueError("characteristic must be zero or a positive prime")
    bad_primes = coefficient_bad_primes(reduction)
    if characteristic and characteristic in bad_primes:
        raise ValueError(
            "characteristic %d is bad for pivots/denominators" % characteristic
        )
    variables = reduction.remaining_variables + [reduction.c, sp.Symbol("T")]
    field = str(characteristic)
    lines = [
        "// generated by triangular_preprocess.py; DO NOT infer uniform t",
        "// t=%d; constant Q* pivots=%d; original equations=%d; residual equations=%d"
        % (
            reduction.t,
            len(reduction.pivots),
            len(reduction.original_rows),
            len(reduction.rows),
        ),
        "// necessary order-chart superset; safe target gauges ON",
        "// good-characteristic assertion: p=%d not in {%s}"
        % (characteristic, ",".join(map(str, bad_primes))),
        "ring RAC=%s,(gamma,pi),dp;" % field,
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        "ring R=%s,(%s),dp;" % (field, ",".join(map(str, variables))),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        'print("CONTROL_EMPTY_START");',
        "ideal CE=c,T*c-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="R")'
        ' { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
        ' else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=c-1,T*c-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="R")'
        ' { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MAIN_START t=%d original_equations=%d residual_equations=%d '
        'original_chart_unknowns=%d residual_chart_unknowns=%d plus_T=1 characteristic=%d");'
        % (
            reduction.t,
            len(reduction.original_rows),
            len(reduction.rows),
            len(reduction.original_variables) + 1,
            len(reduction.remaining_variables) + 1,
            characteristic,
        ),
    ]
    polynomial_variables = reduction.remaining_variables + [reduction.c]
    generators = [
        singular_polynomial(row.expr, polynomial_variables) for row in reduction.rows
    ] + ["T*c-1"]
    lines.extend(
        [
            "ideal I=%s;" % ",\n".join(generators),
            "ideal G=std(I);",
            'print("MAIN_DONE basis_size=");',
            "size(G);",
            'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); G; }'
            ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY");'
            ' print("BASIS_OUTPUT_TRUNCATED_TO_20");'
            ' int basis_cap=size(G); if (basis_cap>20) { basis_cap=20; }'
            ' for (int basis_i=1; basis_i<=basis_cap; basis_i++)'
            ' { G[basis_i]; } }',
            "quit;",
        ]
    )
    return "\n".join(lines) + "\n"


def write_ring_map(path: pathlib.Path, reduction: Reduction) -> None:
    lines = [
        "step\tsource_index_0based\th_power\tgamma_power\tpi_power"
        "\tpivot_variable\tpivot_coefficient\tstep_rhs\tfinal_rhs"
    ]
    for pivot in reduction.pivots:
        lines.append(
            "%d\t%d\t%d\t%d\t%d\t%s\t%s\t%s\t%s"
            % (
                pivot.step,
                pivot.source_index,
                pivot.h_power,
                pivot.monomial[0],
                pivot.monomial[1],
                pivot.variable,
                pivot.coefficient,
                pivot.step_rhs,
                pivot.final_rhs,
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_emission_scalars(path: pathlib.Path, reduction: Reduction) -> None:
    variables = reduction.remaining_variables + [reduction.c]
    lines = [
        "source_index_0based\th_power\tgamma_power\tpi_power"
        "\tinteger_row_equals_multiplier_times_rational_row"
        "\tdenominator_lcm\tcleared_integer_content"
    ]
    for row in reduction.rows:
        _primitive, multiplier, denominator_lcm, content = (
            primitive_integer_polynomial(row.expr, variables)
        )
        lines.append(
            "%d\t%d\t%d\t%d\t%s\t%d\t%d"
            % (
                row.source_index,
                row.h_power,
                row.monomial[0],
                row.monomial[1],
                multiplier,
                denominator_lcm,
                content,
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def audit_record(reduction: Reduction) -> dict:
    pivot_coefficients = [str(pivot.coefficient) for pivot in reduction.pivots]
    pivot_bands: dict[str, int] = {}
    for pivot in reduction.pivots:
        key = str(pivot.h_power)
        pivot_bands[key] = pivot_bands.get(key, 0) + 1
    variables = reduction.remaining_variables + [reduction.c]
    integer_rows = [
        primitive_integer_polynomial(row.expr, variables)[0].as_expr()
        for row in reduction.rows
    ]
    return {
        "t": reduction.t,
        "tuple": [12 * reduction.t + 4, 8 * reduction.t + 4, 12 * reduction.t + 1, 3],
        "gauges": [
            "alpha_t=0",
            "const(beta_(2t+1))=0",
            "const(alpha_(3t+1))=0",
        ],
        "original_chart_unknowns_including_c": len(reduction.original_variables) + 1,
        "residual_chart_unknowns_including_c": len(reduction.remaining_variables) + 1,
        "original_equations": len(reduction.original_rows),
        "residual_equations": len(reduction.rows),
        "pivot_count": len(reduction.pivots),
        "zero_image_rows_including_pivot_rows": len(reduction.zero_source_indices),
        "pivot_variables": [str(pivot.variable) for pivot in reduction.pivots],
        "pivot_coefficients": pivot_coefficients,
        "pivot_band_histogram": pivot_bands,
        "highest_pivot_band": max(pivot.h_power for pivot in reduction.pivots),
        "lowest_pivot_band": min(pivot.h_power for pivot in reduction.pivots),
        "remaining_variables": [str(v) for v in reduction.remaining_variables]
        + [str(reduction.c)],
        "bad_characteristics_for_precomputed_map": coefficient_bad_primes(reduction),
        "original_equation_vector_sha256": expression_vector_hash(
            row.expr for row in reduction.original_rows
        ),
        "residual_equation_vector_sha256": expression_vector_hash(
            row.expr for row in reduction.rows
        ),
        "emitted_primitive_integer_equation_vector_sha256": expression_vector_hash(
            integer_rows
        ),
        "every_emitted_integer_row_verified_as_Qstar_multiple": True,
        "ring_map_verified_on_every_original_generator": True,
        "all_pivots_are_nonzero_Q_constants": True,
        "c_fixed_by_ring_map": True,
        "preprocess_elapsed_seconds": round(reduction.elapsed_seconds, 6),
        "residual_equation_text_bytes": sum(len(str(row.expr)) for row in reduction.rows),
    }


def parse_frozen_certificate() -> dict:
    text = FROZEN_T2_CERTIFICATE.read_text(encoding="utf-8")
    required = [
        "exact coefficient field Q",
        "37 Jacobian coefficient generators plus T*c-1",
        "MAIN_DONE basis_size=",
        "MAIN_SATURATED_EMPTY",
        "G[1]=1",
    ]
    missing = [needle for needle in required if needle not in text]
    if missing:
        raise AssertionError("frozen t=2 certificate missing markers: %s" % missing)
    return {
        "certificate_sha256": sha256_file(FROZEN_T2_CERTIFICATE),
        "markers_checked": required,
        "reported_reduced_basis": ["1"],
        "reported_result": "SATURATED-EMPTY",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-pivots", type=int, default=256)
    parser.add_argument("--max-seconds-per-t", type=float, default=600.0)
    parser.add_argument("--max-expression-bytes", type=int, default=5_000_000)
    args = parser.parse_args()
    if args.max_pivots <= 0 or args.max_seconds_per_t <= 0:
        parser.error("bounds must be positive")

    # Output is intentionally confined to this directory.
    if HERE != ROOT / "box/k16t3-20260903/preprocessed":
        raise RuntimeError("driver is outside the designated preprocessing directory")

    generic = load_module(GENERIC_DRIVER, "k16_generic_order_driver")
    frozen_t2 = load_module(FROZEN_T2_DRIVER, "k16_frozen_t2_order_driver")
    dedicated_t4 = load_module(DEDICATED_T4_DRIVER, "k16_dedicated_t4_order_driver")

    data_by_t = {t: generic.build(t=t, gauged=True) for t in (2, 3, 4)}
    validations = {
        "generic_t2_vs_frozen_t2": assert_same_chart(
            data_by_t[2], frozen_t2.build(gauged=True), "generic t=2 vs frozen t=2"
        ),
        "generic_t4_vs_dedicated_t4": assert_same_chart(
            data_by_t[4], dedicated_t4.build(gauged=True), "generic t=4 vs dedicated t=4"
        ),
        "frozen_t2_certificate": parse_frozen_certificate(),
    }

    reductions = {}
    for t in (2, 3, 4):
        reductions[t] = reduce_chart(
            data_by_t[t],
            max_pivots=args.max_pivots,
            max_seconds=args.max_seconds_per_t,
            max_expression_bytes=args.max_expression_bytes,
        )

    generated: list[pathlib.Path] = []
    audit = {
        "method": "successive affine elimination with a nonzero Q-constant pivot",
        "row_order": "descending h_power, ascending (gamma_power,pi_power), original row",
        "variable_tiebreak": "original gauged chart parameter order",
        "generic_driver": {
            "path": str(GENERIC_DRIVER.relative_to(ROOT)),
            "sha256": sha256_file(GENERIC_DRIVER),
        },
        "frozen_t2_driver": {
            "path": str(FROZEN_T2_DRIVER),
            "sha256": sha256_file(FROZEN_T2_DRIVER),
        },
        "dedicated_t4_driver": {
            "path": str(DEDICATED_T4_DRIVER.relative_to(ROOT)),
            "sha256": sha256_file(DEDICATED_T4_DRIVER),
        },
        "validations": validations,
        "reductions": {str(t): audit_record(reductions[t]) for t in (2, 3, 4)},
        "singular_launched_by_this_driver": False,
    }

    for t, reduction in reductions.items():
        map_path = HERE / ("t%d_ring_map.tsv" % t)
        write_ring_map(map_path, reduction)
        generated.append(map_path)
        scalar_path = HERE / ("t%d_emission_scalars.tsv" % t)
        write_emission_scalars(scalar_path, reduction)
        generated.append(scalar_path)
        characteristics = (0,) + PRIMES[t]
        for characteristic in characteristics:
            suffix = "Q" if characteristic == 0 else "p%d" % characteristic
            singular_path = HERE / ("t%d_triangular_%s.sing" % (t, suffix))
            singular_path.write_text(
                emit_singular(reduction, characteristic), encoding="utf-8"
            )
            generated.append(singular_path)

    audit_path = HERE / "reduction_audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    generated.append(audit_path)

    command_lines = [
        "# Prepared only. Run one command only when the coordinator confirms a Singular slot.",
        "# Exact t=2 validates the transformed certificate computationally.",
    ]
    for t in (2, 3, 4):
        for characteristic in (0,) + PRIMES[t]:
            suffix = "Q" if characteristic == 0 else "p%d" % characteristic
            name = "t%d_triangular_%s" % (t, suffix)
            command_lines.append(
                "/usr/bin/time -v Singular -q box/k16t3-20260903/preprocessed/%s.sing"
                " > box/k16t3-20260903/preprocessed/%s.out"
                " 2> box/k16t3-20260903/preprocessed/%s.err" % (name, name, name)
            )
    command_path = HERE / "RUN_COMMANDS.txt"
    command_path.write_text("\n".join(command_lines) + "\n", encoding="utf-8")
    generated.append(command_path)

    manifest_entries = [HERE / "triangular_preprocess.py"] + generated
    proof_path = HERE / "PREPROCESSING_PROOF.md"
    if proof_path.is_file():
        manifest_entries.append(proof_path)
    manifest = "".join(
        "%s  %s\n" % (sha256_file(path), path.name) for path in manifest_entries
    )
    manifest_path = HERE / "SHA256SUMS.prepared"
    manifest_path.write_text(manifest, encoding="utf-8")

    print(json.dumps(audit, indent=2, sort_keys=True))
    print("PREPARED_FILES=%d" % (len(generated) + 1))
    print("SINGULAR_LAUNCHED=NO")


if __name__ == "__main__":
    main()
