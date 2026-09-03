#!/usr/bin/env python3
"""Exact control replays for the Moh (99,66) branch-B lifting lane.

All mathematical builders are either reconstructed literally from Moh p.208 or
loaded from the frozen charged inputs.  New outputs are confined to this
directory.  The checks are controls only; in particular the t=1 K=16 order
chart is a necessary superset, not an identification with Moh's unprinted
eta-reduced ten-variable system.
"""
from __future__ import annotations

import contextlib
import dataclasses
import hashlib
import importlib.util
import io
import json
import math
import re
import shutil
import subprocess
import sys
import time
from functools import reduce
from pathlib import Path

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
OUT = ROOT / "box" / "moh9966lift-20260903" / "controls"
INPUTS = Path("/tmp/jc2-lane.kNGcqH/inputs")
RECEIPT = ROOT / "xmodel" / "moh9966-B-lift-sol56-20260903.run.v2"
PRIMES = (32003, 32009, 32027)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def receipt_check() -> dict:
    fields = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    rows = []
    for index in range(1, int(fields["charged_inputs"]) + 1):
        path = Path(fields["lane_inputs_dir"]) / fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        got = sha256(path) if path.is_file() else None
        rows.append({"index": index, "path": str(path), "expected": expected,
                     "got": got, "ok": expected == got})
    if not all(row["ok"] for row in rows):
        raise RuntimeError("charged-input content mismatch")
    return {"method": "receipt basename/hash fields parsed; digests recomputed",
            "ok": True, "rows": rows}


def run_singular(stem: str, text: str, timeout: int = 300) -> dict:
    script = OUT / f"{stem}.sing"
    log = OUT / f"{stem}.log"
    script.write_text(text, encoding="utf-8")
    started = time.perf_counter()
    try:
        proc = subprocess.run(
            ["Singular", "-q", "--no-rc", str(script)],
            capture_output=True, text=True, timeout=timeout, check=False,
        )
        output = (proc.stdout or "") + (proc.stderr or "")
        verdict = "SATURATED-EMPTY" if (
            "MAIN_SATURATED_EMPTY" in output
            or "MAIN_T1_EMPTY" in output
        ) else ("NONUNIT" if "MAIN_NONUNIT" in output else "ERROR")
        returncode = proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        output = stdout + stderr
        verdict = "TIMEOUT"
        returncode = None
    log.write_text(output, encoding="utf-8")
    fail_markers = sorted(set(re.findall(r"[A-Z0-9_]*FAIL[A-Z0-9_]*", output)))
    return {
        "verdict": verdict,
        "returncode": returncode,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "script": str(script.relative_to(ROOT)),
        "script_sha256": sha256(script),
        "log": str(log.relative_to(ROOT)),
        "log_sha256": sha256(log),
        "fail_markers": fail_markers,
        "pass_markers": sorted(set(re.findall(r"[A-Z0-9_]*PASS[A-Z0-9_]*", output))),
        "basis_one": "G[1]=1" in output or re.search(r"BASIS_BEGIN\s*1\s*BASIS_END", output) is not None,
        "stdout": output,
    }


def strengthen_frozen_script(text: str) -> str:
    """Add ring/type assertions without changing any mathematical generator."""
    text = text.replace(
        "option(redSB);\nprint(\"RING_BEGIN\")",
        "option(redSB);\n"
        "if (nameof(basering)==\"R\") { print(\"CONTROL_RING_PASS R\"); } "
        "else { print(\"CONTROL_RING_FAIL\"); }\n"
        "print(\"RING_BEGIN\")",
    )
    text = text.replace(
        "ideal G=std(I);\nprint(\"GENERATOR_COUNT\")",
        "ideal G=std(I);\n"
        "if (typeof(G)==\"ideal\" && nameof(basering)==\"R\") "
        "{ print(\"MAIN_IDEAL_RING_PASS\"); } "
        "else { print(\"MAIN_IDEAL_RING_FAIL\"); }\n"
        "print(\"GENERATOR_COUNT\")",
    )
    return text


def run_branch_a_c(legacy) -> dict:
    records = {}
    for label, builder in (
        ("branch_A_predecessor", legacy.branch_a_predecessor),
        ("branch_C_exclusion", legacy.branch_c_consequence),
    ):
        spec = builder()
        runs = []
        for characteristic in (*PRIMES, 0):
            script, ring_map = legacy.singular_script(spec, characteristic)
            script = strengthen_frozen_script(script)
            field = "Q" if characteristic == 0 else f"F_{characteristic}"
            run = run_singular(f"{label}_{field}", script, timeout=120)
            parsed = legacy.parse_singular_output(run["stdout"])
            run["parsed"] = parsed
            run["ring_variables"] = [
                str(ring_map[s]) for s in list(spec["parameters"]) + [spec["T"]]
            ]
            if run["returncode"] != 0 or run["fail_markers"] or parsed["verdict"] == "ERROR":
                raise AssertionError(f"{label}/{field} failed controls")
            runs.append(run)

        if label.startswith("branch_A"):
            T, c = spec["T"], spec["factor"]
            cert = sp.expand(-(T * c - 1) - T * spec["equations"][0] - 1)
            if spec["equations"][0] != -c or cert != 0:
                raise AssertionError("branch-A two-term certificate failed")
            certificate = {
                "identity": "1 = -(T*c-1) - T*(-c)",
                "identity_remainder": str(cert),
                "source_equation_index_0based": 0,
                "source_equation": str(spec["equations"][0]),
            }
        else:
            certificate = spec["certificate"]
            if certificate["identity_remainder"] != "0":
                raise AssertionError("branch-C certificate failed")
        records[label] = {
            "name": spec["name"],
            "parameters_excluding_T": [str(s) for s in spec["parameters"]],
            "factor_saturated": str(spec["factor"]),
            "equations": [str(e) for e in spec["equations"]],
            "equation_count": len(spec["equations"]),
            "certificate": certificate,
            "runs": runs,
        }
    return records


def jacobian(f, g, x, y):
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))


def singular_expr(expr: sp.Expr) -> str:
    numerator, denominator = sp.fraction(sp.together(sp.expand(expr)))
    if denominator == 1:
        ans = str(sp.expand(numerator))
    else:
        ans = f"({sp.expand(numerator)})/({sp.expand(denominator)})"
    return ans.replace("**", "^")


def build_moh_1612_literal() -> dict:
    """Moh p.208 equations (1)-(5), alpha_1 absorbed, J(f,g)=c*x."""
    x, y = sp.symbols("x y")
    b = list(sp.symbols("b1:5"))
    cc = list(sp.symbols("c1:14"))
    c, T = sp.symbols("c T")
    b1, b2, b3, b4 = b
    (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13) = cc
    h = sp.expand(y**3 * (y - x) + b1*y**3 + b2*y**2 + b3*y + b4)
    A = sp.cancel((h - b4) / y)
    B = sp.cancel((A - A.subs(y, 0)) / y)
    alpha2, beta2 = c1*A + c2, c3*A + c4
    alpha3, beta3 = c5*A + c6*B + c7, c8*A + c9*B + c10
    alpha4 = c11*A + c12*B + c13*(y - x)
    f = sp.expand(h**3 + beta2*h + beta3)
    g = sp.expand(h**4 + alpha2*h**2 + alpha3*h + alpha4)
    remainder = sp.Poly(jacobian(f, g, x, y) - c*x, x, y)
    equations = [sp.expand(value) for value in remainder.coeffs() if value != 0]
    unknowns = b + cc + [c]
    if len(unknowns) != 18 or len(equations) != 77:
        raise AssertionError("unexpected p.208 system size")
    origin = {v: 0 for v in unknowns}
    if any(sp.expand(eq.subs(origin)) != 0 for eq in equations):
        raise AssertionError("unsaturated origin is not a solution")
    return {"x": x, "y": y, "h": h, "A": A, "B": B, "f": f, "g": g,
            "c": c, "T": T, "unknowns": unknowns, "equations": equations}


def emit_moh_1612_literal(data: dict) -> str:
    variables = data["unknowns"] + [data["T"]]
    c, T = data["c"], data["T"]
    equations = data["equations"]
    generators = ",\n  ".join(singular_expr(eq) for eq in equations)
    maximal = ",".join(str(v) for v in data["unknowns"])
    return f'''// Moh p.208 (1)-(5), alpha1 absorbed; exact Q replay
ring RAC=0,(gamma,pi),dp;
poly FAC=pi;
poly GAC=pi-(gamma^2)/2;
poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);
if (JAC==gamma) {{ print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }} else {{ print("CONTROL_ACTUAL_PAIR_FAIL"); }}
ring R=0,({','.join(map(str, variables))}),dp;
option(redSB);
if (nameof(basering)=="R") {{ print("CONTROL_RING_PASS R"); }} else {{ print("CONTROL_RING_FAIL"); }}
ideal CE={c},{T}*{c}-1;
ideal GCE=std(CE);
if (typeof(GCE)=="ideal" && nameof(basering)=="R") {{ print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }} else {{ print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }}
if (reduce(1,GCE)==0) {{ print("CONTROL_EMPTY_PASS"); }} else {{ print("CONTROL_EMPTY_FAIL"); }}
ideal CN={c}-1,{T}*{c}-1;
ideal GCN=std(CN);
if (typeof(GCN)=="ideal" && nameof(basering)=="R") {{ print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }} else {{ print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }}
if (reduce(1,GCN)!=0) {{ print("CONTROL_NONEMPTY_PASS"); }} else {{ print("CONTROL_NONEMPTY_FAIL"); }}
ideal E=
  {generators};
ideal M={maximal};
ideal GM=std(M);
int origin_ok=1;
for (int origin_i=1; origin_i<=size(E); origin_i++) {{ if (reduce(E[origin_i],GM)!=0) {{ origin_ok=0; }} }}
if (origin_ok==1) {{ print("CONTROL_UNSAT_ORIGIN_PASS"); }} else {{ print("CONTROL_UNSAT_ORIGIN_FAIL"); }}
ideal I=E,{T}*{c}-1;
ideal G=std(I);
if (typeof(G)=="ideal" && nameof(basering)=="R") {{ print("MAIN_IDEAL_RING_PASS"); }} else {{ print("MAIN_IDEAL_RING_FAIL"); }}
print("MAIN_START equations=77 unknowns_excluding_T=18");
print("MAIN_DONE basis_size="); size(G);
if (reduce(1,G)==0) {{ print("MAIN_SATURATED_EMPTY"); G; }} else {{ print("MAIN_NONUNIT"); }}
quit;
'''


def grading(rows, variables: list[sp.Symbol]) -> tuple[dict, dict[sp.Symbol, int]]:
    constraints = []
    for row in rows:
        monomials = [m for m, _ in sp.Poly(row.expr, *variables, domain=sp.QQ).terms()]
        if len(monomials) > 1:
            base = monomials[0]
            constraints.extend([[m[i] - base[i] for i in range(len(variables))]
                                for m in monomials[1:]])
    matrix = sp.Matrix(constraints)
    null = matrix.nullspace()
    if len(null) != 1:
        raise AssertionError("t=1 grading is not one-dimensional")
    vector = null[0]
    multiple = sp.ilcm(*[int(sp.denom(value)) for value in vector])
    integers = [int(value * multiple) for value in vector]
    divisor = reduce(math.gcd, [abs(value) for value in integers if value])
    integers = [value // divisor for value in integers]
    if all(value < 0 for value in integers):
        integers = [-value for value in integers]
    if not all(value > 0 for value in integers):
        raise AssertionError("t=1 grading is not positive")
    weights = dict(zip(variables, integers))
    return ({"constraint_count": len(constraints), "rank": matrix.rank(),
             "nullity": 1, "weights": {str(v): weights[v] for v in variables}}, weights)


@dataclasses.dataclass
class SliceRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    expr: sp.Expr


class NumberField:
    def __init__(self, y: sp.Symbol, H: sp.Expr, auxiliaries: list[sp.Symbol]):
        self.y, self.H = y, sp.expand(H)
        self.domain = sp.QQ[tuple(auxiliaries)]
        self.hpoly = sp.Poly(self.H, y, domain=self.domain)

    def reduce(self, expr: sp.Expr) -> sp.Expr:
        return sp.expand(sp.Poly(sp.expand(expr), self.y, domain=self.domain).rem(self.hpoly).as_expr())

    def inverse(self, coefficient: sp.Expr) -> sp.Expr:
        coefficient = self.reduce(coefficient)
        if coefficient.free_symbols - {self.y}:
            raise AssertionError("pivot coefficient is not in K")
        ans = sp.invert(sp.Poly(coefficient, self.y, domain=sp.QQ),
                        sp.Poly(self.H, self.y, domain=sp.QQ)).as_expr()
        ans = self.reduce(ans)
        if self.reduce(coefficient * ans - 1) != 0:
            raise AssertionError("inverse did not check")
        return ans


def primitive_row(pre, expr: sp.Expr, variables: list[sp.Symbol]):
    poly, multiplier, _denom, _content = pre.primitive_integer_polynomial(expr, variables)
    return poly.as_expr(), multiplier


def dedup(rows: list[SliceRow], field: NumberField):
    kept, dropped, seen = [], [], {}
    for row in rows:
        expr = field.reduce(row.expr)
        if expr == 0:
            dropped.append({"source_index": row.source_index, "reason": "zero_mod_H"})
        elif expr in seen:
            dropped.append({"source_index": row.source_index, "reason": "duplicate_mod_H",
                            "representative": seen[expr].source_index})
        else:
            current = dataclasses.replace(row, expr=expr)
            seen[expr] = current
            kept.append(current)
    return kept, dropped


def affine_candidates(rows, remaining, field: NumberField):
    occurrences = {v: sum(v in row.expr.free_symbols for row in rows) for v in remaining}
    ans = []
    for row_index, row in enumerate(rows):
        terms = sp.Add.make_args(row.expr)
        for variable_index, variable in enumerate(remaining):
            if variable not in row.expr.free_symbols:
                continue
            coeff_terms, rem_terms, nonlinear = [], [], False
            for term in terms:
                exponent = term.as_powers_dict().get(variable, 0)
                if exponent == 0:
                    rem_terms.append(term)
                elif exponent == 1:
                    coeff_terms.append(term / variable)
                else:
                    nonlinear = True
                    break
            if nonlinear:
                continue
            coefficient, remainder = sp.Add(*coeff_terms), sp.Add(*rem_terms)
            if coefficient == 0 or coefficient.free_symbols - {field.y}:
                continue
            if field.reduce(row.expr - coefficient*variable - remainder) != 0:
                raise AssertionError("affine decomposition failed")
            score = (len(str(remainder))*occurrences[variable], len(str(remainder)),
                     occurrences[variable], len(str(row.expr)), row.source_index, variable_index)
            ans.append((score, row_index, variable_index, coefficient, remainder))
    return ans


def eliminate_over_field(rows, auxiliaries, field: NumberField):
    remaining = list(auxiliaries)
    rows, dropped = dedup(rows, field)
    pivots, terminal = [], None
    while True:
        constants = [row for row in rows if not (row.expr.free_symbols - {field.y})]
        if constants:
            row = min(constants, key=lambda item: (len(str(item.expr)), item.source_index))
            inverse = field.inverse(row.expr)
            terminal = {"source_index": row.source_index, "h_power": row.h_power,
                        "monomial": list(row.monomial), "constant": str(row.expr),
                        "inverse": str(inverse)}
            break
        candidates = affine_candidates(rows, remaining, field)
        if not candidates:
            break
        _, row_index, variable_index, coefficient, remainder = min(candidates, key=lambda item: item[0])
        pivot = rows[row_index]
        variable = remaining[variable_index]
        inverse = field.inverse(coefficient)
        rhs = field.reduce(-inverse * remainder)
        if field.reduce(pivot.expr.subs(variable, rhs)) != 0:
            raise AssertionError("field-pivot substitution failed")
        del rows[row_index]
        del remaining[variable_index]
        next_rows = [dataclasses.replace(row, expr=field.reduce(row.expr.subs(variable, rhs)))
                     for row in rows]
        rows, newly_dropped = dedup(next_rows, field)
        dropped.extend(newly_dropped)
        pivots.append({"step": len(pivots)+1, "source_index": pivot.source_index,
                       "h_power": pivot.h_power, "monomial": list(pivot.monomial),
                       "variable": str(variable), "coefficient": str(coefficient),
                       "inverse": str(inverse), "rhs": str(rhs),
                       "rows_after": len(rows), "variables_after": len(remaining)})
    return rows, remaining, pivots, dropped, terminal


def normalize_t1(pre, reduction) -> dict:
    variables = reduction.remaining_variables + [reduction.c]
    grade, weights = grading(reduction.rows, variables)
    by_name = {str(v): v for v in variables}
    x, y, c = by_name["q2_1"], by_name["q3_1"], reduction.c
    c_rows = [row for row in reduction.rows if c in row.expr.free_symbols]
    base_rows = [row for row in reduction.rows if row.expr.free_symbols <= {x, y} and row.expr != 0]
    if len(c_rows) != 1 or not base_rows:
        raise AssertionError("distinguished t=1 rows not unique")
    c_row = c_rows[0]
    c_coefficient = sp.diff(c_row.expr, c)
    c_image = sp.factor(-(c_row.expr - c_coefficient*c) / c_coefficient)
    candidates = []
    for row in base_rows:
        primitive, multiplier = primitive_row(pre, row.expr, [x, y])
        candidates.append((len(str(primitive)), row, primitive, multiplier))
    _, base_row, Hhom, associate = min(candidates, key=lambda item: item[0])
    for _, row, candidate, _ in candidates:
        if sp.div(candidate, Hhom, x, y)[1] != 0:
            raise AssertionError(f"independent base row {row.source_index}")
    H = sp.expand(Hhom.subs(x, 1))
    c_slice = sp.factor(c_image.subs(x, 1))
    auxiliaries = [v for v in reduction.remaining_variables if v not in (x, y)]
    sliced = []
    for row in reduction.rows:
        if row is c_row:
            continue
        expr = sp.expand(row.expr.subs({x: 1, c: c_slice}, simultaneous=True))
        sliced.append(SliceRow(row.source_index, row.h_power, row.monomial, expr))
    q_variables = auxiliaries + [y]
    q_rows, q_map, seen = [], [], {}
    for row in sliced:
        expr, multiplier = primitive_row(pre, row.expr, q_variables)
        key = str(expr)
        if key in seen:
            q_map.append({"source_index": row.source_index, "status": "duplicate_Q",
                          "representative": seen[key].source_index, "multiplier": str(multiplier)})
        else:
            current = dataclasses.replace(row, expr=expr)
            seen[key] = current
            q_rows.append(current)
            q_map.append({"source_index": row.source_index, "status": "kept",
                          "multiplier": str(multiplier)})
    field = NumberField(y, H, auxiliaries)
    c_inverse = field.inverse(c_slice)
    rows, remaining, pivots, dropped, terminal = eliminate_over_field(q_rows, auxiliaries, field)
    if terminal is None:
        raise AssertionError("t=1 terminal unit missing")
    if (len(pivots), [p["variable"] for p in pivots]) != (4, ["q3_0", "b4", "b2", "a3_0"]):
        raise AssertionError("unexpected t=1 field pivots")
    if field.reduce(sp.sympify(terminal["constant"]) * sp.sympify(terminal["inverse"]) - 1) != 0:
        raise AssertionError("terminal certificate failed")
    certificate_quotient = sp.div(
        sp.expand(sp.sympify(terminal["constant"]) * sp.sympify(terminal["inverse"]) - 1),
        H, y,
    )
    return {
        "grading": grade,
        "x": str(x), "y": str(y), "weights_xyc": [weights[x], weights[y], weights[c]],
        "c_row": {"source_index": c_row.source_index, "h_power": c_row.h_power,
                  "monomial": list(c_row.monomial), "coefficient": str(c_coefficient),
                  "c_image": str(c_image)},
        "base_row": {"source_index": base_row.source_index, "h_power": base_row.h_power,
                     "monomial": list(base_row.monomial), "Hhom": str(Hhom),
                     "associate_multiplier": str(associate)},
        "weighted_slice_justification": "c!=0 and c_image has factor x, so x!=0; positive grading permits x=1 over algebraic closure",
        "H": str(H), "H_discriminant": str(sp.discriminant(H, y)),
        "H_irreducible_Q": bool(sp.Poly(H, y, domain=sp.QQ).is_irreducible),
        "c_slice": str(c_slice), "c_inverse": str(c_inverse),
        "c_inverse_remainder_mod_H": str(field.reduce(c_slice*c_inverse - 1)),
        "q_rows_after_c": len(sliced), "q_rows_after_duplicate_removal": len(q_rows),
        "q_row_map": q_map,
        "field_pivots": pivots, "dropped": dropped,
        "remaining_variables_before_terminal": [str(v) for v in remaining],
        "remaining_rows_before_terminal": len(rows),
        "remaining_bands": [row.h_power for row in rows],
        "terminal_unit": terminal,
        "terminal_bezout": {
            "identity": f"1 = ({terminal['constant']})*({terminal['inverse']}) - ({certificate_quotient[0]})*H",
            "quotient_of_product_minus_one_by_H": str(certificate_quotient[0]),
            "remainder": str(certificate_quotient[1]),
        },
    }


def emit_t1_normalized(normal: dict) -> str:
    H = normal["H"].replace("**", "^")
    cbar = normal["c_slice"].replace("**", "^")
    cinv = normal["c_inverse"].replace("**", "^")
    unit = normal["terminal_unit"]["constant"].replace("**", "^")
    inverse = normal["terminal_unit"]["inverse"].replace("**", "^")
    return f'''// Exact normalized t=1 certificate derived from frozen drivers
ring RAC=0,(gamma,pi),dp;
poly FAC=pi;
poly GAC=pi-(gamma^2)/2;
poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);
if (JAC==gamma) {{ print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }} else {{ print("CONTROL_ACTUAL_PAIR_FAIL"); }}
ring RC=(0,q3_1),(u,T),dp;
minpoly={H};
if (nameof(basering)=="RC") {{ print("CONTROL_COEFF_RING_PASS RC"); }} else {{ print("CONTROL_COEFF_RING_FAIL"); }}
number cbar={cbar}; number cbar_inverse={cinv};
if (cbar*cbar_inverse==1) {{ print("CONTROL_C_UNIT_PASS"); }} else {{ print("CONTROL_C_UNIT_FAIL"); }}
number terminal={unit}; number terminal_inverse={inverse};
if (terminal*terminal_inverse==1) {{ print("CONTROL_TERMINAL_UNIT_PASS"); }} else {{ print("CONTROL_TERMINAL_UNIT_FAIL"); }}
ideal CE=u,T*u-1; ideal GE=std(CE);
if (typeof(GE)=="ideal" && nameof(basering)=="RC") {{ print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }} else {{ print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }}
if (reduce(1,GE)==0) {{ print("CONTROL_EMPTY_PASS"); }} else {{ print("CONTROL_EMPTY_FAIL"); }}
ideal CN=u-1,T*u-1; ideal GN=std(CN);
if (typeof(GN)=="ideal" && nameof(basering)=="RC") {{ print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }} else {{ print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }}
if (reduce(1,GN)!=0) {{ print("CONTROL_NONEMPTY_PASS"); }} else {{ print("CONTROL_NONEMPTY_FAIL"); }}
ring RK=(0,q3_1),(b1,b3,a2_0,q2_0,u,T),dp;
minpoly={H}; option(redSB);
if (nameof(basering)=="RK") {{ print("CONTROL_RING_PASS RK"); }} else {{ print("CONTROL_RING_FAIL"); }}
ideal CE=u,T*u-1; ideal GE=std(CE);
if (typeof(GE)=="ideal" && nameof(basering)=="RK" && reduce(1,GE)==0) {{ print("CONTROL_MAIN_RING_EMPTY_PASS"); }} else {{ print("CONTROL_MAIN_RING_EMPTY_FAIL"); }}
ideal CN=u-1,T*u-1; ideal GN=std(CN);
if (typeof(GN)=="ideal" && nameof(basering)=="RK" && reduce(1,GN)!=0) {{ print("CONTROL_MAIN_RING_NONEMPTY_PASS"); }} else {{ print("CONTROL_MAIN_RING_NONEMPTY_FAIL"); }}
print("MAIN_START t=1 terminal_coefficient_field_unit");
ideal I=1; ideal G=std(I);
if (typeof(G)=="ideal" && nameof(basering)=="RK") {{ print("MAIN_IDEAL_RING_PASS"); }} else {{ print("MAIN_IDEAL_RING_FAIL"); }}
print("MAIN_DONE basis_size="); size(G);
if (reduce(1,G)==0) {{ print("MAIN_T1_EMPTY"); G; }} else {{ print("MAIN_NONUNIT"); }}
quit;
'''


def run_1612_controls(order_driver, pre) -> dict:
    literal = build_moh_1612_literal()
    literal_run = run_singular("moh1612_literal_p208_Q", emit_moh_1612_literal(literal), timeout=300)
    if literal_run["returncode"] != 0 or literal_run["fail_markers"] or literal_run["verdict"] != "SATURATED-EMPTY":
        raise AssertionError("literal Moh (16,12) replay failed")

    data = order_driver.build(t=1, gauged=True)
    if (len(data["equations"]), len(data["params"]) + 1) != (23, 18):
        raise AssertionError("unexpected t=1 full chart")
    reduction = pre.reduce_chart(data, 256, 120.0, 5_000_000)
    if (len(reduction.pivots), len(reduction.rows), len(reduction.remaining_variables) + 1) != (7, 15, 11):
        raise AssertionError("unexpected constant-pivot reduction")
    pre.write_ring_map(OUT / "moh1612_t1_Qstar_pivots.tsv", reduction)
    pre.write_emission_scalars(OUT / "moh1612_t1_emission_scalars.tsv", reduction)
    triangular_audit = pre.audit_record(reduction)

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        order_driver.emit_singular(data, characteristic=0)
    full_run = run_singular("moh1612_t1_full_gauged_Q", buffer.getvalue(), timeout=300)
    residual_run = run_singular("moh1612_t1_Qstar_residual_Q", pre.emit_singular(reduction, 0), timeout=300)
    for run in (full_run, residual_run):
        if run["returncode"] != 0 or run["fail_markers"] or run["verdict"] != "SATURATED-EMPTY":
            raise AssertionError("t=1 order-chart replay failed")

    normal = normalize_t1(pre, reduction)
    normalized_run = run_singular("moh1612_t1_normalized_unit_Q", emit_t1_normalized(normal), timeout=120)
    if normalized_run["returncode"] != 0 or normalized_run["fail_markers"] or normalized_run["verdict"] != "SATURATED-EMPTY":
        raise AssertionError("normalized t=1 certificate failed")
    return {
        "literal_p208_AB": {
            "typing": "p.208 equations (1)-(5), alpha1 absorbed; not Moh's unprinted eta-reduced ten-variable display",
            "ring": "Q[b1..b4,c1..c13,c,T], dp",
            "unknowns_excluding_T": 18,
            "equations": len(literal["equations"]),
            "h": str(literal["h"]), "A": str(literal["A"]), "B": str(literal["B"]),
            "unsaturated_witness": "all b_i,c_i,c=0",
            "run": literal_run,
        },
        "t1_order_spine": {
            "typing": "K=16 t=1 order-filtered necessary superset; exact calibration of band/pivot machinery",
            "full_shape": {"equations": len(data["equations"]),
                           "unknowns_including_c": len(data["params"]) + 1,
                           "h_level_histogram": {
                               str(level): sum(1 for hpow, _, _ in data["tagged"] if hpow == level)
                               for level in sorted({hpow for hpow, _, _ in data["tagged"]})
                           }},
            "triangular_audit": triangular_audit,
            "normalization": normal,
            "full_run": full_run,
            "Qstar_residual_run": residual_run,
            "normalized_run": normalized_run,
        },
    }


def strip_stdout(value):
    if isinstance(value, dict):
        return {k: strip_stdout(v) for k, v in value.items() if k != "stdout"}
    if isinstance(value, list):
        return [strip_stdout(v) for v in value]
    return value


def write_hash_manifest() -> None:
    paths = sorted(path for path in OUT.iterdir() if path.is_file()
                   and path.name not in {
                       "artifacts.sha256",
                       # Shell capture files are still open when this routine runs.
                       "controls_replay.stdout",
                       "controls_replay.stderr",
                   })
    (OUT / "artifacts.sha256").write_text(
        "".join(f"{sha256(path)}  {path.relative_to(ROOT)}\n" for path in paths),
        encoding="utf-8",
    )


def main() -> None:
    if shutil.which("Singular") is None:
        raise SystemExit("Singular is required")
    OUT.mkdir(parents=True, exist_ok=True)
    custody = receipt_check()
    legacy = load_module(INPUTS / "moh9966B_driver.py", "frozen_moh9966B_driver")
    order_driver = load_module(INPUTS / "t_order_system.py", "frozen_t_order_system")
    pre = load_module(INPUTS / "triangular_preprocess.py", "frozen_triangular_preprocess")
    result = {
        "custody": custody,
        "software": {
            "python": subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip(),
            "sympy": sp.__version__,
            "singular": subprocess.run(["Singular", "--version"], capture_output=True, text=True).stdout.splitlines()[0],
        },
        "branch_controls": run_branch_a_c(legacy),
        "moh_1612": run_1612_controls(order_driver, pre),
    }
    clean = strip_stdout(result)
    result_path = OUT / "controls_results.json"
    result_path.write_text(json.dumps(clean, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_hash_manifest()
    print(json.dumps(clean, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
