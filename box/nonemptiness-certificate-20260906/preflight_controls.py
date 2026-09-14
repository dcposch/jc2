#!/usr/bin/env python3
"""Light exact controls and frozen-metadata preflight; no solver or CAS.

This is not a T2/T3 solution search and never emits a properness verdict for
the client. It checks necessary packet conditions and proves only syntactic
absence of coordinates, not independence of coordinates that occur.
"""
import argparse
import ast
import hashlib
import json
import math
from pathlib import Path
import re
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "box/t2t3-compressor-gate-20260906/support-counts.jsonl": "5c250e0bf8a9823e21133111cfc8ab5c4ee788353bbeb41153d4b477b53c50d6",
    "box/t2t3-direct-20260906/build_direct.py": "77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e",
    "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json": "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea",
    "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json": "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46",
    "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json": "1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_pinned(path):
    raw = (ROOT / path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PINS[path], "Source drift: " + path)
    return raw


# Tiny sparse exact polynomials in x,y,z for method controls only.
ZERO = (0, 0, 0)


def c(value):
    return {ZERO: Fraction(value)} if value else {}


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coeff in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coeff
    return {m: a for m, a in out.items() if a}


def mul(a, b):
    out = {}
    for m, u in a.items():
        for n, v in b.items():
            mn = tuple(i + j for i, j in zip(m, n))
            out[mn] = out.get(mn, Fraction(0)) + u * v
    return {m: a for m, a in out.items() if a}


def neg(a):
    return {m: -v for m, v in a.items()}


def ev(poly, point):
    return sum((a * math.prod(t**e for t, e in zip(point, m))
                for m, a in poly.items()), Fraction(0))


def d(poly, i):
    out = {}
    for m, a in poly.items():
        if m[i]:
            n = list(m)
            n[i] -= 1
            out[tuple(n)] = m[i] * a
    return out


def controls(mutate_local_containment=False):
    x, y, z = [{tuple(int(i == j) for i in range(3)): Fraction(1)}
               for j in range(3)]
    one = c(1)
    p = 5
    g1 = add(mul(x, x), neg(one))
    g2 = add(y, neg(x))
    g3 = add(mul(z, x), neg(one))
    f4 = add(x, neg(one))
    h = add(x, one)
    if mutate_local_containment:
        h = x
    point = (1, 1, 1)
    require(all(ev(f, point) == 0 for f in [g1, g2, g3, f4]), "Positive point")
    require(mul(h, f4) == g1 and ev(h, point) % p != 0, "Local containment")
    jac = [[ev(d(g, i), point) for i in range(3)] for g in [g1, g2, g3]]
    det = (jac[0][0] * (jac[1][1]*jac[2][2] - jac[1][2]*jac[2][1])
           - jac[0][1] * (jac[1][0]*jac[2][2] - jac[1][2]*jac[2][0])
           + jac[0][2] * (jac[1][0]*jac[2][1] - jac[1][1]*jac[2][0]))
    require(det % p != 0, "Positive smooth subsystem")

    # Primitive rows can hide vertical torsion until arbitrarily late.
    depths = [1, 2, 4, 8, 16]
    for depth in depths:
        f2 = add(x, c(p**depth))
        require(ev(x, ZERO) == 0 and ev(f2, ZERO) % p**depth == 0, "Finite survival")
        require(ev(f2, ZERO) % p**(depth + 1) != 0, "Next-digit obstruction")
        require(add(f2, neg(x)) == c(p**depth), "Characteristic-zero unit certificate")
        require(ev(d(f2, 0), ZERO) == 1, "Misleading maximal Jacobian rank")

    # An annihilating multiplier that vanishes at the mod-p point is forbidden.
    require(mul(x, c(p)) == mul(c(p), x), "Bad localizer identity")
    require(ev(x, ZERO) % p == 0, "Bad localizer must be rejected")

    # Monic witness algebra Q[x]/(x^2-2), with y=x: no irreducibility needed.
    a = add(mul(x, x), c(-2))
    b = add(y, neg(x))
    target = add(mul(y, y), c(-2))
    require(add(a, mul(add(y, x), b)) == target, "Witness containment")
    spoly = add(mul(y, a), neg(mul(mul(x, x), b)))
    require(spoly == add(mul(x, a), mul(c(-2), b)), "Exact S-polynomial reduction")

    # A one-parameter formal lift with growing x-support need not be polynomial.
    for depth in depths:
        series = add(*( {(i, 0, 0): Fraction(p**i)} for i in range(depth)))
        residual = add(mul(add(one, mul(c(-p), x)), series), neg(one))
        require(residual == {(depth, 0, 0): Fraction(-(p**depth))}, "Growing-support control")

    return {"local_smooth_positive": "PASS", "monic_witness_positive": "PASS",
            "vertical_primitive_rows_depths": depths,
            "vertical_rank_false_positive": "REJECTED",
            "vanishing_localizer_false_positive": "REJECTED",
            "growing_support_false_positive": "REJECTED",
            "ordinary_optimized_and_double_optimized_checks": "explicit exceptions, no assert"}


def name_set(expressions):
    answer = set()
    for expression in expressions:
        # These are frozen plain arithmetic expressions, never evaluated here.
        answer.update(re.findall(r"\b[A-Za-z_][A-Za-z_0-9]*\b", str(expression)))
    return answer - {"tt", "zz"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-local-containment", action="store_true")
    args = parser.parse_args()
    require(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),
            "Optimization firewall: assert node")
    meta = [json.loads(line) for line in load_pinned(next(iter(PINS))).splitlines()]
    load_pinned("box/t2t3-direct-20260906/build_direct.py")
    out = {"controls": controls(args.mutate_local_containment), "clients": []}
    paths = list(PINS)[2:]
    for row, path in zip(meta, paths):
        source = json.loads(load_pinned(path))
        case = row["case"]
        if case.startswith("99-"):
            expressions = [term[2] for key in ("h3", "C2", "C3", "B2", "A3")
                           for term in source["maps"][key]]
            expressions += [r[1] for r in source["residual_rows"]]
            recurrence = {"t3eq", "t3_fq"}
            sep, zsep = ("rho", "Zrho") if case == "99-delta2" else ("c", "Zc")
            lam, zlam = "leader55", "Z55"
            semantic = set(source["full_free_coordinates"]) | {zsep} | recurrence | {"lambda3", "Z3"}
        else:
            expressions = [source[k] for k in ("h_expr", "D_expr", "C_expr")]
            expressions += source["residual_strings"]
            recurrence = {"t3eq", "t3_fgq", "t3_fq2"}
            sep, zsep, lam, zlam = "c", "Zc", "leader63", "Z63"
            semantic = set(source["names"]) | {zsep} | recurrence | {"lambda3", "Z3"}
        direct = {"target_" + v for v in "abcd"} | recurrence | {sep, zsep, lam, zlam, "lambda3", "Z3"}
        used = name_set(expressions) | direct
        require(used <= semantic, "Unexpected expression coordinate")
        require(len(semantic) == row["semantic_variables"], "Semantic count mismatch")
        inactive = sorted(semantic - used)
        require(inactive == ["target_e"], "Unexpected inactive-coordinate finding")
        require(row["checked_nonzero_values"] == row["nonzero_generator_total"], "Wrong support witness type")
        require(row["zero_witness_values"] == 0, "Source witness unexpectedly changed")
        p = row["prime"]
        assignments = row["specialization_assignments"]
        inverse_residuals = [(assignments[u] * assignments[v] - 1) % p
                             for u, v in ((zsep, sep), (zlam, lam), ("Z3", "lambda3"))]
        require(all(inverse_residuals), "Expected non-solution must fail all inverse rows")
        out["clients"].append({
            "case": case, "variables": len(semantic), "rows": row["nonzero_generator_total"],
            "syntactically_inactive_coordinates": inactive,
            "jacobian_rank_upper_bound": len(semantic) - len(inactive),
            "minimum_left_cokernel_dimension": row["nonzero_generator_total"] - len(semantic) + len(inactive),
            "frozen_support_assignment_inverse_residuals": inverse_residuals,
            "full_mod_p_point_available_in_charged_metadata": False,
            "hensel_certificate_preflight": "NO: no solution, no full-row containment certificate",
            "ideal_properness": "UNDECIDED",
        })
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
