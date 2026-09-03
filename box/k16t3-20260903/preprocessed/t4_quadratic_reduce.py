#!/usr/bin/env python3
"""Affine reduction of the normalized t=4 chart over its quadratic field.

The input is the independently emitted and audited q5_1=1 system over
K=Q(v)/(486*v^2-270*v+35).  This script performs only affine eliminations
whose leading coefficient is a checked nonzero element of K.  It prepares
exact Singular std/slimgb programs and never invokes Singular.
"""

from __future__ import annotations

import csv
import hashlib
import json
import pathlib
import re
import sys
import time

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
T4DIR = ROOT / "box/k16t3-20260903/t4"
SOURCE = T4DIR / "t4_normalized_Qv_slimgb.sing"
SOURCE_AUDIT = T4DIR / "t4_normalized_audit.json"
SOURCE_BUILDER = T4DIR / "build_t4_normalized.py"
ROW_META = HERE / "t4_emission_scalars.tsv"
CORE_DRIVER = HERE / "t3_normalized_slice.py"

# The first deterministic scan was interrupted only after these five pivots
# had been printed and locally checked.  Replaying the explicit sequence is
# much faster and is independently revalidated below.  The resulting system
# is deliberately typed PARTIAL_AFFINE_REDUCTION, not exhaustion.
FORCED_PIVOTS = [
    (41, "a1_0"),
    (20, "q6_1"),
    (36, "q2_0"),
    (14, "q7_1"),
    (31, "q8_1"),
]

EXPECTED = {
    SOURCE: "848c2c6aa4215b9e15d87a3dd9b8903a7d1b395e2960284f4232458bf1b84bd7",
    SOURCE_AUDIT: "00f114c02923570e4918cc55bfc54771d58c33d755c35afcf148180b558ac0ee",
    SOURCE_BUILDER: "e359327c0b7f96fe87657491b909899aa6848e17f6d38e8ef5364e313ba380d4",
    ROW_META: "b3c6eda9cf51e5bc37864c1f7bbbe2660df8656635a87b9f1839a2dd84ef772c",
    CORE_DRIVER: "9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7",
}

sys.path.insert(0, str(HERE))
import t3_normalized_slice as core  # noqa: E402


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class H4Field(core.QuadraticField):
    def __init__(self, v: sp.Symbol, auxiliary: list[sp.Symbol]):
        self.y = v
        self.auxiliary = list(auxiliary)
        self.H = 486*v**2 - 270*v + 35
        self.domain = sp.QQ[tuple(self.auxiliary)]
        self.hpoly = sp.Poly(self.H, v, domain=self.domain)


def split_affine(expr: sp.Expr, variable: sp.Symbol, v: sp.Symbol):
    coefficient_terms = []
    remainder_terms = []
    for term in sp.Add.make_args(expr):
        exponent = term.as_powers_dict().get(variable, 0)
        if exponent == 0:
            remainder_terms.append(term)
        elif exponent == 1:
            coefficient_terms.append(term / variable)
        else:
            raise AssertionError("forced pivot is nonlinear in %s" % variable)
    coefficient = sp.Add(*coefficient_terms)
    remainder = sp.Add(*remainder_terms)
    if coefficient == 0 or coefficient.free_symbols - {v}:
        raise AssertionError("forced coefficient is not in K*: %s" % coefficient)
    return coefficient, remainder


def exact_dedup(rows: list[core.SliceRow]):
    kept = []
    dropped = []
    representatives = {}
    for row in rows:
        if row.expr == 0:
            dropped.append({"source_index": row.source_index, "reason": "zero_mod_H4"})
        elif row.expr in representatives:
            dropped.append({
                "source_index": row.source_index,
                "reason": "literal_duplicate_mod_H4",
                "representative_source_index": representatives[row.expr].source_index,
            })
        else:
            representatives[row.expr] = row
            kept.append(row)
    return kept, dropped


def replay_forced(rows: list[core.SliceRow], variables: list[sp.Symbol],
                  K: H4Field):
    started = time.monotonic()
    rows, dropped = exact_dedup(rows)
    remaining = list(variables)
    pivots = []
    for source_index, variable_name in FORCED_PIVOTS:
        variable = next(v for v in remaining if str(v) == variable_name)
        matches = [(i, row) for i, row in enumerate(rows)
                   if row.source_index == source_index]
        if len(matches) != 1:
            raise AssertionError("forced source row multiplicity: %s" % (matches,))
        row_index, pivot_row = matches[0]
        coefficient, remainder = split_affine(pivot_row.expr, variable, K.y)
        inverse = K.inverse(coefficient)
        rhs = K.reduce(-inverse * remainder)
        if K.reduce(pivot_row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("forced pivot substitution does not kill row")
        del rows[row_index]
        remaining.remove(variable)
        next_rows = []
        for row in rows:
            expr = row.expr
            if variable in expr.free_symbols:
                expr = K.reduce(expr.subs(variable, rhs))
            next_rows.append(core.dataclasses.replace(row, expr=expr))
        rows, new_dropped = exact_dedup(next_rows)
        dropped.extend(new_dropped)
        expression_bytes = sum(len(str(row.expr)) for row in rows)
        pivots.append(core.KPivot(
            step=len(pivots)+1,
            source_index=pivot_row.source_index,
            h_power=pivot_row.h_power,
            monomial=pivot_row.monomial,
            variable=variable,
            coefficient=coefficient,
            inverse=inverse,
            step_rhs=rhs,
            remaining_rows_after=len(rows),
            expression_bytes_after=expression_bytes,
        ))
        print("K_PIVOT step=%d source=%d variable=%s rows=%d vars=%d bytes=%d" % (
            len(pivots), source_index, variable, len(rows), len(remaining),
            expression_bytes), flush=True)
    terminal_unit = None
    for row in rows:
        if not (row.expr.free_symbols - {K.y}) and row.expr != 0:
            inverse = K.inverse(row.expr)
            terminal_unit = {
                "source_index": row.source_index,
                "constant": str(row.expr),
                "inverse": str(inverse),
                "identity_verified_mod_H4": K.reduce(row.expr*inverse-1) == 0,
            }
            break
    return (rows, remaining, pivots, dropped, terminal_unit,
            time.monotonic()-started)


def parse_normalized():
    for path, expected in EXPECTED.items():
        actual = sha256_file(path)
        if actual != expected:
            raise RuntimeError("pinned input mismatch for %s: %s" % (path, actual))
    audit = json.loads(SOURCE_AUDIT.read_text(encoding="utf-8"))
    text = SOURCE.read_text(encoding="utf-8")
    match = re.search(r"ring R=\(0,v\),\(([^\n]+)\),dp;", text)
    if match is None:
        raise AssertionError("normalized main ring not found")
    names = match.group(1).split(",")
    v = sp.Symbol("v")
    variables = list(sp.symbols(" ".join(names)))
    local = {"v": v, **dict(zip(names, variables))}
    body = text.split("ideal I=", 1)[1].split(";\nideal G=", 1)[0]
    generator_text = body.split(",\n")
    expressions = [
        sp.expand(sp.sympify(item.replace("^", "**"), locals=local))
        for item in generator_text
    ]
    if len(expressions) != 38 or len(variables) != 26:
        raise AssertionError("unexpected normalized t=4 dimensions")
    if names != audit["remaining_variables"]:
        raise AssertionError("normalized variable order differs from audit")
    if len(audit["normalized_row_sources"]) != len(expressions):
        raise AssertionError("normalized source map length differs")

    with ROW_META.open(newline="", encoding="utf-8") as handle:
        metadata = list(csv.DictReader(handle, delimiter="\t"))
    if len(metadata) != 48:
        raise AssertionError("residual metadata does not have 48 rows")
    rows = []
    row_map = []
    for expression, residual_position in zip(
            expressions, audit["normalized_row_sources"]):
        meta = metadata[residual_position]
        source_index = int(meta["source_index_0based"])
        h_power = int(meta["h_power"])
        monomial = (int(meta["gamma_power"]), int(meta["pi_power"]))
        rows.append(core.SliceRow(source_index, h_power, monomial, expression))
        row_map.append({
            "normalized_row_position": len(rows) - 1,
            "triangular_residual_position": residual_position,
            "original_source_index": source_index,
            "h_power": h_power,
            "monomial": list(monomial),
            "source_normalization_multiplier": audit["normalized_row_multipliers"][len(rows)-1],
        })
    return v, variables, rows, row_map, audit


def emit_program(rows: list[core.SliceRow], remaining: list[sp.Symbol],
                 v: sp.Symbol, method: str, terminal_unit: dict | None) -> str:
    if method not in ("std", "slimgb"):
        raise ValueError(method)
    polynomial_variables = [v] + remaining
    generators = [core.singular_expr(row.expr, polynomial_variables) for row in rows]
    if terminal_unit is not None:
        generators.append("1")
    if not generators:
        generators.append("0")
    lines = [
        "// exact affine-reduced t=4 normalized system",
        "// generated by t4_quadratic_reduce.py from pinned normalized source",
        "// coefficient field K=Q(v)/(486*v^2-270*v+35)",
        "ring RAC=(0,v),(gamma,pi),dp;",
        "minpoly=486*v^2-270*v+35;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        "ring RC=(0,v),(u,W),dp;",
        "minpoly=486*v^2-270*v+35;",
        "number cbar=(130*v-1404*v^2)/2187;",
        "number cbar_inverse=1/cbar;",
        'if (cbar!=0 && cbar*cbar_inverse==1)'
        ' { print("CONTROL_CBAR_UNIT_PASS"); }'
        ' else { print("CONTROL_CBAR_UNIT_FAIL"); }',
        "ideal CE=u,W*u-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="RC")'
        ' { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
        ' else { print("CONTROL_EMPTY_FAIL"); }',
        "ideal CN=u-1,W*u-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="RC")'
        ' { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_NONEMPTY_FAIL"); }',
        "ring RK=(0,v),(%s),dp;" % ",".join(map(str, remaining)),
        "minpoly=486*v^2-270*v+35;",
        "option(redSB);",
        'if (nameof(basering)=="RK") { print("CONTROL_RING_PASS RK"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        'print("MAIN_START t=4 normalized_q5_1=1 coefficient_field=quadratic '
        'residual_equations=%d residual_unknowns=%d");'
        % (len(generators), len(remaining)),
        "ideal I=%s;" % ",\n".join(generators),
        "ideal G=%s(I);" % method,
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_QUADRATIC_FIELD_EMPTY"); G; }'
        ' else { print("MAIN_QUADRATIC_FIELD_NONTRIVIAL");'
        ' print("BASIS_OUTPUT_TRUNCATED_TO_20");'
        ' int basis_cap=size(G); if (basis_cap>20) { basis_cap=20; }'
        ' for (int basis_i=1; basis_i<=basis_cap; basis_i++)'
        ' { G[basis_i]; } }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    if HERE != ROOT / "box/k16t3-20260903/preprocessed":
        raise RuntimeError("output directory invariant failed")
    v, variables, input_rows, source_row_map, source_audit = parse_normalized()
    K = H4Field(v, variables)
    if sp.Poly(K.H, v, domain=sp.QQ).discriminant() != 4860:
        raise AssertionError("H4 discriminant mismatch")
    if not sp.Poly(K.H, v, domain=sp.QQ).is_irreducible:
        raise AssertionError("H4 is reducible")
    v_inverse = K.inverse(v)
    factor_inverse = K.inverse(130 - 1404*v)
    cbar = (130*v - 1404*v**2) / 2187
    cbar_inverse = K.inverse(cbar)
    if K.reduce(cbar*cbar_inverse - 1) != 0:
        raise AssertionError("cbar inverse failed")
    for row in input_rows:
        if K.reduce(row.expr - K.reduce(row.expr)) != 0:
            raise AssertionError("input row is not valid modulo H4")

    (rows, remaining, pivots, dropped, terminal_unit,
     elapsed) = replay_forced(input_rows, variables, K)

    pivot_lines = [
        "step\toriginal_source_index_0based\th_power\tgamma_power\tpi_power"
        "\tpivot_variable\tcoefficient_in_K\tinverse_mod_H4\tstep_rhs"
        "\tremaining_rows_after\texpression_bytes_after"
    ]
    for pivot in pivots:
        pivot_lines.append(
            "%d\t%d\t%d\t%d\t%d\t%s\t%s\t%s\t%s\t%d\t%d" % (
                pivot.step, pivot.source_index, pivot.h_power,
                pivot.monomial[0], pivot.monomial[1], pivot.variable,
                pivot.coefficient, pivot.inverse, pivot.step_rhs,
                pivot.remaining_rows_after, pivot.expression_bytes_after,
            )
        )
    pivot_path = HERE / "t4_kreduce_K_pivots.tsv"
    pivot_path.write_text("\n".join(pivot_lines) + "\n", encoding="utf-8")

    output_paths = []
    for method in ("std", "slimgb"):
        path = HERE / ("t4_kreduce_K_%s.sing" % method)
        path.write_text(
            emit_program(rows, remaining, v, method, terminal_unit),
            encoding="utf-8",
        )
        output_paths.append(path)

    audit = {
        "typing": "EXACT-SYMBOLIC-PREPROCESSING; no Singular result claimed",
        "pinned_inputs": {
            str(path.relative_to(ROOT)): digest for path, digest in EXPECTED.items()
        },
        "source_normalized_rows": len(input_rows),
        "source_normalized_unknowns": len(variables),
        "source_row_map": source_row_map,
        "normalization_proof_imported_and_hash_pinned": {
            "homogeneous_rows": source_audit["homogeneous_rows"],
            "grading_rank": source_audit["grading_rank"],
            "grading_nullity": source_audit["grading_nullity"],
            "positive_primitive_weights": source_audit["positive_primitive_weights"],
            "c_row_index_0based": source_audit["c_row_index_0based"],
            "base_row_index_0based": source_audit["base_row_index_0based"],
            "H4": source_audit["H4"],
            "H4_irreducible_over_Q": source_audit["H4_irreducible_over_Q"],
            "c_image": source_audit["c_image"],
        },
        "base_units": {
            "v_inverse_mod_H4": str(v_inverse),
            "130_minus_1404v_inverse_mod_H4": str(factor_inverse),
            "cbar_inverse_mod_H4": str(cbar_inverse),
            "all_inverse_identities_verified_mod_H4": True,
        },
        "K_elimination": {
            "typing": "PARTIAL_AFFINE_REDUCTION",
            "affine_exhaustion_claimed": False,
            "forced_checked_sequence": [list(item) for item in FORCED_PIVOTS],
            "input_rows": len(input_rows),
            "input_unknowns": len(variables),
            "pivot_count": len(pivots),
            "pivot_source_indices": [pivot.source_index for pivot in pivots],
            "pivot_variables": [str(pivot.variable) for pivot in pivots],
            "remaining_rows": len(rows),
            "remaining_unknowns": [str(variable) for variable in remaining],
            "remaining_row_sources": [
                {
                    "original_source_index": row.source_index,
                    "h_power": row.h_power,
                    "monomial": list(row.monomial),
                }
                for row in rows
            ],
            "dropped_rows": dropped,
            "terminal_unit": terminal_unit,
            "elapsed_seconds": round(elapsed, 6),
            "every_pivot_coefficient_inverse_checked_mod_H4": True,
            "every_pivot_substitution_checked_mod_H4": True,
            "proof_preservation": (
                "Each step K[V]/(a*v+b,rest) -> K[V\\{v}]/(rest[v=-b/a]) "
                "is an isomorphism because a has a checked inverse in K."
            ),
        },
        "outputs": {
            path.name: {"sha256": sha256_file(path), "bytes": path.stat().st_size}
            for path in output_paths
        },
        "singular_launched_by_this_driver": False,
    }
    audit_path = HERE / "t4_kreduce_audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")

    generated = output_paths + [pivot_path, audit_path,
                                HERE / "t4_quadratic_reduce.py"]
    manifest_path = HERE / "SHA256SUMS.t4-kreduce"
    manifest_path.write_text(
        "\n".join("%s  %s" % (sha256_file(path), path.name)
                  for path in sorted(generated, key=lambda item: item.name)) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "input_rows": len(input_rows),
        "input_unknowns": len(variables),
        "pivots": len(pivots),
        "remaining_rows": len(rows),
        "remaining_unknowns": [str(variable) for variable in remaining],
        "terminal_unit": terminal_unit,
        "manifest": str(manifest_path),
        "manifest_sha256": sha256_file(manifest_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
