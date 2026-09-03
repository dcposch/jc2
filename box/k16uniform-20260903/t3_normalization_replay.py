#!/usr/bin/env python3
"""Exact replay of the charged t=3 normalization and affine reduction.

All source programs are the frozen lane inputs.  Generated files stay beside
this driver.  The script prepares, but does not launch, the final Singular
standard-basis computation.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
INPUTS = pathlib.Path("/tmp/jc2-lane.fjoTgL/inputs")
EXPECTED = {
    "t_order_system.py": "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
    "triangular_preprocess.py": "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
    "t3_normalized_slice.py": "9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7",
}


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    for name, expected in EXPECTED.items():
        actual = sha256(INPUTS / name)
        if actual != expected:
            raise RuntimeError(f"charged source mismatch: {name}: {actual}")

    generic = load(INPUTS / "t_order_system.py", "k16_uniform_t3_generic")
    # The charged normalized-slice module imports this exact module name.
    triangular = load(INPUTS / "triangular_preprocess.py", "triangular_preprocess")
    normalized = load(INPUTS / "t3_normalized_slice.py", "k16_uniform_t3_normalized")

    data = generic.build(t=3, gauged=True)
    reduction = triangular.reduce_chart(data, 256, 600.0, 5_000_000)
    if (len(data["tagged"]), len(data["params"]) + 1) != (51, 36):
        raise AssertionError("unexpected full chart dimensions")
    if (len(reduction.pivots), len(reduction.rows),
            len(reduction.remaining_variables) + 1) != (13, 37, 23):
        raise AssertionError("unexpected constant-pivot dimensions")

    by_name = {str(v): v for v in reduction.remaining_variables + [reduction.c]}
    x, y, c = by_name["q4_1"], by_name["q7_1"], reduction.c
    homogeneous_H = 11*x**4 - 84*x**2*y + 147*y**2
    H = sp.expand(homogeneous_H.subs(x, 1))
    c_image = 10*x*y*(2*x**2 - 21*y) / 343

    c_rows = [row for row in reduction.rows if c in row.expr.free_symbols]
    if len(c_rows) != 1:
        raise AssertionError("expected one c row")
    c_row = c_rows[0]
    if sp.expand(sp.solve(c_row.expr, c)[0] - c_image) != 0:
        raise AssertionError("c identity differs")
    base_rows = []
    all_variables = reduction.remaining_variables + [c]
    for row in reduction.rows:
        if row is c_row or not row.expr.free_symbols <= {x, y}:
            continue
        ratio = normalized.rational_associate(row.expr, homogeneous_H, all_variables)
        if ratio is not None:
            base_rows.append((row, ratio))
    if len(base_rows) != 1:
        raise AssertionError("expected one H row")

    auxiliary = [v for v in reduction.remaining_variables if v not in (x, y)]
    q_variables = auxiliary + [y]
    canonical: dict[str, normalized.SliceRow] = {}
    q_rows = []
    duplicate_sources = []
    for row in reduction.rows:
        if row is c_row:
            continue
        expr = sp.expand(row.expr.subs(
            {x: 1, c: c_image.subs(x, 1)}, simultaneous=True))
        primitive, _multiplier = normalized.primitive_expr(expr, q_variables)
        key = str(primitive)
        if key in canonical:
            duplicate_sources.append(row.source_index)
        else:
            sliced = normalized.SliceRow(
                row.source_index, row.h_power, row.monomial, primitive)
            canonical[key] = sliced
            q_rows.append(sliced)

    K = normalized.QuadraticField(y, auxiliary)
    if K.reduce(H) != 0:
        raise AssertionError("minimal polynomial does not vanish")
    k_input = []
    zero_mod_H = []
    for row in q_rows:
        expr = K.reduce(row.expr)
        if expr == 0:
            zero_mod_H.append(row.source_index)
        else:
            k_input.append(normalized.SliceRow(
                row.source_index, row.h_power, row.monomial, expr))

    rows, remaining, pivots, dropped, terminal_unit, elapsed = (
        normalized.eliminate_over_k(
            k_input, auxiliary, K, max_seconds=900.0,
            max_bytes=20_000_000))
    if terminal_unit is not None:
        raise AssertionError("unexpected coefficient-field constant")
    if (len(pivots), len(rows), [str(v) for v in remaining]) != (
            17, 6, ["b3", "b4", "a2_0"]):
        raise AssertionError("unexpected affine residual")

    generator_lines = [
        "source_index_0based\th_power\tgamma_power\tpi_power"
        "\ttotal_degree\tterm_count\tprimitive_generator"
    ]
    residual_summary = []
    polynomial_variables = [y] + remaining
    for row in rows:
        poly = sp.Poly(row.expr, *remaining, domain=sp.QQ.frac_field(y))
        primitive = normalized.singular_expr(row.expr, polynomial_variables)
        generator_lines.append(
            f"{row.source_index}\t{row.h_power}\t{row.monomial[0]}"
            f"\t{row.monomial[1]}\t{poly.total_degree()}"
            f"\t{len(poly.terms())}\t{primitive}"
        )
        residual_summary.append({
            "source_index_0based": row.source_index,
            "h_power": row.h_power,
            "monomial_gamma_pi": list(row.monomial),
            "total_degree_in_residual_unknowns": poly.total_degree(),
            "term_count_over_K": len(poly.terms()),
        })
    generator_path = HERE / "t3_residual_generators.tsv"
    generator_path.write_text("\n".join(generator_lines) + "\n", encoding="utf-8")

    singular_path = HERE / "t3_normalized_K_std.sing"
    singular_path.write_text(
        normalized.emit_k_system(rows, remaining, y, "std", terminal_unit),
        encoding="utf-8")

    audit = {
        "typing": "EXACT symbolic replay; Singular input prepared only",
        "charged_sources_sha256": {
            name: sha256(INPUTS / name) for name in EXPECTED
        },
        "full_chart": {"equations": 51, "unknowns_including_c": 36},
        "constant_pivot_reduction": {
            "pivots": len(reduction.pivots),
            "rows": len(reduction.rows),
            "unknowns_including_c": len(reduction.remaining_variables) + 1,
        },
        "grading": {
            "x": "q4_1", "weight_x": 13,
            "y": "q7_1", "weight_y": 26,
            "weight_c": 65,
        },
        "normalization": {
            "homogeneous_H": str(homogeneous_H),
            "H": str(H), "discriminant": int(sp.discriminant(H, y)),
            "c_image_before_slice": str(c_image),
            "c_image": str(c_image.subs(x, 1)),
            "H_at_y_0": str(H.subs(y, 0)),
            "H_at_c_second_factor_root": str(H.subs(y, sp.Rational(2, 21))),
        },
        "slice": {
            "q_rows_after_primitive_duplicate_removal": len(q_rows),
            "q_duplicate_sources": duplicate_sources,
            "K_input_rows_excluding_minpoly": len(k_input),
            "zero_mod_H_sources": zero_mod_H,
            "auxiliary_unknowns_before_affine_pass": len(auxiliary),
        },
        "affine_elimination": {
            "pivot_count": len(pivots),
            "pivot_sources": [p.source_index for p in pivots],
            "pivot_bands": [p.h_power for p in pivots],
            "pivot_variables": [str(p.variable) for p in pivots],
            "remaining_unknowns": [str(v) for v in remaining],
            "remaining_rows": residual_summary,
            "dropped": dropped,
            "elapsed_seconds": elapsed,
        },
        "artifacts": {
            generator_path.name: sha256(generator_path),
            singular_path.name: sha256(singular_path),
        },
    }
    audit_path = HERE / "t3_normalization_audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    print(json.dumps({
        "audit": audit_path.name,
        "audit_sha256": sha256(audit_path),
        "residual_rows": len(rows),
        "residual_bands": [row.h_power for row in rows],
        "residual_unknowns": [str(v) for v in remaining],
        "singular_input": singular_path.name,
        "singular_input_sha256": sha256(singular_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
