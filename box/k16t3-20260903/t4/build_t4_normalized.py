#!/usr/bin/env python3
"""Emit and audit the normalized quadratic-field t=4 residual system.

Input is the independently verified, proof-equivalent constant-pivot residual
program.  This script checks its SHA-256, checks weighted homogeneity of every
residual row, identifies the base and c rows exactly, normalizes the forced
nonzero coordinate u=q5_1 to one, and emits the resulting ideal over
Q(v)/(486*v^2-270*v+35).  It does not run Singular.
"""

from __future__ import annotations

import hashlib
import json
import math
import pathlib
import re

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE.parent / "preprocessed" / "t4_triangular_Q_slimgb.sing"
OUTPUT = HERE / "t4_normalized_Qv_slimgb.sing"
AUDIT = HERE / "t4_normalized_audit.json"
EXPECTED_SOURCE_SHA256 = (
    "54abfe8f94f98d2d2baa3d46b8504e2fe793868c22eea6f1d7d894b96c34d045"
)


EXPECTED_WEIGHTS = {
    "b1": 1,
    "b2": 2,
    "b3": 3,
    "b4": 4,
    "a1_0": 4,
    "a2_0": 8,
    "a3_0": 12,
    "a5_0": 20,
    "a6_0": 24,
    "a7_0": 28,
    "a8_0": 32,
    "a9_0": 36,
    "a10_0": 40,
    "a11_0": 44,
    "a12_0": 48,
    "q2_0": 8,
    "q3_0": 12,
    "q4_0": 16,
    "q5_0": 20,
    "q5_1": 17,
    "q6_0": 24,
    "q6_1": 21,
    "q7_0": 28,
    "q7_1": 25,
    "q8_0": 32,
    "q8_1": 29,
    "q9_0": 33,
    "q9_1": 34,
    "c": 85,
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse_source():
    raw = SOURCE.read_bytes()
    digest = sha256_bytes(raw)
    if digest != EXPECTED_SOURCE_SHA256:
        raise AssertionError("source hash mismatch: " + digest)
    text = raw.decode("utf-8")
    match = re.search(r"ring R=0,\(([^\n]+)\),dp;", text)
    if match is None:
        raise AssertionError("main ring declaration not found")
    names = match.group(1).split(",")
    symbols = sp.symbols(" ".join(names))
    local = dict(zip(names, symbols))
    body = text.split("ideal I=", 1)[1].split(";\nideal G=", 1)[0]
    generator_text = body.split(",\n")
    if generator_text[-1] != "T*c-1":
        raise AssertionError("Rabinowitsch generator not in final position")
    expressions = [
        sp.expand(sp.sympify(item.replace("^", "**"), locals=local))
        for item in generator_text[:-1]
    ]
    if len(expressions) != 48 or len(names) != 30:
        raise AssertionError("unexpected residual shape")
    return digest, names, symbols, local, expressions


def check_homogeneity(expressions, variables):
    weights = [EXPECTED_WEIGHTS[str(variable)] for variable in variables]
    if min(weights) <= 0:
        raise AssertionError("grading is not positive")
    degrees = []
    constraint_rows = set()
    for row_index, expression in enumerate(expressions):
        polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
        monomials = polynomial.monoms()
        row_degrees = {
            sum(exponent * weight for exponent, weight in zip(monomial, weights))
            for monomial in monomials
        }
        if len(row_degrees) != 1:
            raise AssertionError("nonhomogeneous row %d: %s" % (row_index, row_degrees))
        degrees.append(next(iter(row_degrees)))
        first = monomials[0]
        for monomial in monomials[1:]:
            difference = tuple(a - b for a, b in zip(monomial, first))
            if any(difference):
                constraint_rows.add(difference)
    # A rank-28 relation matrix on 29 variables makes the displayed positive
    # grading unique up to scale; this is diagnostic, not an assumption.
    matrix = sp.Matrix(sorted(constraint_rows))
    if matrix.rank() != len(variables) - 1:
        raise AssertionError("grading constraint matrix does not have rank 28")
    vector = sp.Matrix(weights)
    if matrix * vector != sp.zeros(matrix.rows, 1):
        raise AssertionError("displayed weights do not span the grading kernel")
    return degrees, len(constraint_rows), matrix.rank()


def reduce_coefficient_mod_h(expression, variables, v, H):
    """Reduce coefficients modulo H(v), with variables kept polynomial."""
    polynomial = sp.Poly(sp.expand(expression), *variables)
    out = sp.Integer(0)
    for monomial, coefficient in polynomial.terms():
        coefficient_poly = sp.Poly(coefficient, v, domain=sp.QQ)
        remainder = coefficient_poly.rem(H).as_expr()
        term = remainder
        for variable, exponent in zip(variables, monomial):
            if exponent:
                term *= variable**exponent
        out += term
    return sp.expand(out)


def primitive_rational_row(expression, variables, v):
    """Return a canonical primitive ZZ[v,V] rational multiple."""
    polynomial = sp.Poly(expression, *variables, v, domain=sp.QQ)
    denominators = [int(sp.denom(coefficient)) for coefficient in polynomial.coeffs()]
    denominator_lcm = math.lcm(*denominators) if denominators else 1
    cleared = sp.Poly(
        sp.expand(expression * denominator_lcm), *variables, v, domain=sp.ZZ
    )
    content, primitive = cleared.primitive()
    multiplier = sp.Rational(denominator_lcm, int(content))
    if primitive.LC() < 0:
        primitive = -primitive
        multiplier = -multiplier
    return sp.expand(primitive.as_expr()), multiplier


def singular(expression):
    return str(sp.expand(expression)).replace("**", "^")


def emit_program(names, local, expressions):
    chart_names = names[:-1]  # omit T
    chart_variables = [local[name] for name in chart_names]
    degrees, constraint_count, grading_rank = check_homogeneity(
        expressions, chart_variables
    )

    u = local["q5_1"]
    q9 = local["q9_1"]
    c = local["c"]
    base_row = 35 * u**4 - 270 * u**2 * q9 + 486 * q9**2
    c_row = -2187 * c + 130 * u**3 * q9 - 1404 * u * q9**2
    base_matches = [i for i, row in enumerate(expressions) if sp.expand(row-base_row) == 0]
    c_matches = [i for i, row in enumerate(expressions) if sp.expand(row-c_row) == 0]
    if base_matches != [26] or c_matches != [2]:
        raise AssertionError(
            "base/c rows differ: base=%s c=%s" % (base_matches, c_matches)
        )

    v = sp.Symbol("v")
    H = sp.Poly(486 * v**2 - 270 * v + 35, v, domain=sp.QQ)
    if not H.is_irreducible or sp.discriminant(H.as_expr(), v) != 4860:
        raise AssertionError("quadratic field audit failed")
    c_image = sp.expand((130 * v - 1404 * v**2) / 2187)
    c_numerator = sp.Poly(130 * v - 1404 * v**2, v, domain=sp.QQ)
    if sp.gcd(H, c_numerator).degree() != 0:
        raise AssertionError("normalized c image is not a unit")
    if H.eval(0) == 0 or H.eval(sp.Rational(65, 702)) == 0:
        raise AssertionError("a forbidden c factor vanishes on the base field")

    remaining_names = [
        name for name in chart_names if name not in {"q5_1", "q9_1", "c"}
    ]
    remaining_variables = [local[name] for name in remaining_names]
    substitutions = {u: 1, q9: v, c: c_image}
    normalized_rows = []
    row_sources = []
    row_multipliers = []
    zero_rows = []
    duplicate_rows = []
    seen = {}
    for source_index, expression in enumerate(expressions):
        substituted = sp.expand(expression.subs(substitutions, simultaneous=True))
        reduced = reduce_coefficient_mod_h(substituted, remaining_variables, v, H)
        if reduced == 0:
            zero_rows.append(source_index)
            continue
        primitive, multiplier = primitive_rational_row(
            reduced, remaining_variables, v
        )
        # Verify the emitted row is a nonzero rational multiple in K[V].
        check = reduce_coefficient_mod_h(
            sp.expand(primitive - multiplier * substituted),
            remaining_variables,
            v,
            H,
        )
        if check != 0 or multiplier == 0:
            raise AssertionError("row normalization failed at %d" % source_index)
        key = str(primitive)
        if key in seen:
            duplicate_rows.append((source_index, seen[key]))
            continue
        seen[key] = source_index
        normalized_rows.append(primitive)
        row_sources.append(source_index)
        row_multipliers.append(str(multiplier))

    if 2 not in zero_rows or 26 not in zero_rows:
        raise AssertionError("base/c rows did not vanish after field substitution")
    if not normalized_rows:
        raise AssertionError("normalized ideal has no rows")

    lines = [
        "// mechanically generated by build_t4_normalized.py",
        "// source SHA256=" + EXPECTED_SOURCE_SHA256,
        "// t=4 residual: 48 rows/29 chart variables incl c before normalization",
        "// all residual rows verified homogeneous for the displayed positive grading",
        "// c!=0 forces u=q5_1!=0; over Qbar use lambda^17*u=1",
        "// v=q9_1/u^2 then satisfies H4=486*v^2-270*v+35",
        "// cbar=v*(130-1404*v)/2187 is a unit modulo irreducible H4",
        "ring RAC=(0,v),(gamma,pi),dp;",
        "minpoly=486*v^2-270*v+35;",
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); } else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        "ring RW=(0,v),(c,T),dp;",
        "minpoly=486*v^2-270*v+35;",
        "number cbar=(130*v-1404*v^2)/2187;",
        "number cbar_inverse=1/cbar;",
        'if (cbar!=0 && cbar*cbar_inverse==1) { print("CONTROL_CBAR_UNIT_PASS"); } else { print("CONTROL_CBAR_UNIT_FAIL"); }',
        'print("CONTROL_EMPTY_START");',
        "ideal CE=c,T*c-1;",
        "ideal GE=std(CE);",
        'if (typeof(GE)=="ideal" && nameof(basering)=="RW") { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=c-cbar,T*c-1;",
        "ideal GN=std(CN);",
        'if (typeof(GN)=="ideal" && nameof(basering)=="RW") { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); } else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        "ring R=(0,v),(%s),dp;" % ",".join(remaining_names),
        "minpoly=486*v^2-270*v+35;",
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); } else { print("CONTROL_RING_FAIL"); }',
        'print("MAIN_START t=4 normalized_field=Qv_H4 input_rows=48 normalized_rows=%d variables=%d");'
        % (len(normalized_rows), len(remaining_names)),
        "ideal I=" + ",\n".join(singular(row) for row in normalized_rows) + ";",
        "ideal G=slimgb(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_EXACT_NORMALIZED_EMPTY"); G; } else { print("MAIN_EXACT_NORMALIZED_NONTRIVIAL"); print("BASIS_OUTPUT_TRUNCATED_TO_20"); int basis_cap=size(G); if (basis_cap>20) { basis_cap=20; } for (int basis_i=1; basis_i<=basis_cap; basis_i++) { G[basis_i]; } }',
        "quit;",
    ]
    program = "\n".join(lines) + "\n"
    OUTPUT.write_text(program)

    normalized_vector = "\n".join(str(row) for row in normalized_rows) + "\n"
    audit = {
        "source": str(SOURCE),
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "source_residual_rows": len(expressions),
        "source_chart_variables_including_c": len(chart_names),
        "homogeneous_rows": len(degrees),
        "grading_constraint_count": constraint_count,
        "grading_rank": grading_rank,
        "grading_nullity": 1,
        "positive_primitive_weights": EXPECTED_WEIGHTS,
        "base_row_index_0based": 26,
        "base_row": str(base_row),
        "c_row_index_0based": 2,
        "c_row": str(c_row),
        "H4": str(H.as_expr()),
        "H4_discriminant": 4860,
        "H4_irreducible_over_Q": True,
        "c_image": str(c_image),
        "gcd_H4_c_numerator": "1",
        "normalization": {"q5_1": "1", "q9_1": "v", "c": str(c_image)},
        "remaining_variables": remaining_names,
        "zero_source_rows": zero_rows,
        "duplicate_source_rows": duplicate_rows,
        "normalized_row_sources": row_sources,
        "normalized_row_multipliers": row_multipliers,
        "normalized_rows": len(normalized_rows),
        "normalized_vector_sha256": sha256_bytes(normalized_vector.encode()),
        "output": str(OUTPUT),
        "output_bytes": len(program.encode()),
        "output_sha256": sha256_bytes(program.encode()),
    }
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    return audit


def main():
    _digest, names, _symbols, local, expressions = parse_source()
    audit = emit_program(names, local, expressions)
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
