#!/usr/bin/env python3
"""Independent small-row reconstruction of Moh Theorem-1.2 order charts.

This file intentionally does not import the charged order_chart.py.  It builds
the sparse prefix ansatz from its mathematical description, obtains the
Jacobian directly, performs monic h-adic division, tags every coefficient,
and writes self-controlling Singular systems.  The optional ``envelope`` mode
adds the four h-coefficient directions suppressed by the sparse recurrence;
that mode is a diagnostic relaxation, not a claimed source theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sy


HERE = Path(__file__).resolve().parent
ART = HERE / "artifacts"


@dataclass(frozen=True)
class Datum:
    key: str
    n: int
    m: int
    M2: int
    V2: int
    k: int


DATA = {
    "k16_t1": Datum("k16_t1", 16, 12, 13, 3, 1),
    "k16_t2": Datum("k16_t2", 28, 20, 25, 3, 1),
    "banked_15_10": Datum("banked_15_10", 15, 10, 11, 3, 2),
    "open_25_15": Datum("open_25_15", 25, 15, 21, 2, 2),
}


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def singular_expr(expr: sy.Expr) -> str:
    expr = sy.cancel(sy.expand(expr))
    numerator, denominator = sy.fraction(expr)
    numerator = sy.expand(numerator)
    denominator = sy.expand(denominator)
    text = str(numerator) if denominator == 1 else f"({numerator})/({denominator})"
    return text.replace("**", "^")


def invariants(row: Datum) -> dict:
    K = math.gcd(row.n, row.m)
    e = row.n // K
    q = row.m // K
    u = K - row.V2
    R = row.n - row.M2 - 1
    pi_sum = e + q
    d2 = -Fraction(row.k + 1, R)
    d1 = Fraction((row.k + 1) * (pi_sum * u - R), R * (pi_sum * row.V2 - 1))
    B = row.V2 * d1 + u * d2
    if B >= 0:
        raise ValueError("this driver only handles nondegenerate negative-bound rows")
    return {"K": K, "e": e, "q": q, "u": u, "R": R, "Pi": pi_sum,
            "delta2": d2, "delta1": d1, "B": B}


def integer_partitions(total: int, cap: int | None = None) -> Iterable[tuple[int, ...]]:
    if total == 0:
        yield ()
        return
    high = total if cap is None else min(total, cap)
    for first in range(high, 0, -1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


def admissible_parts(row: Datum) -> list[tuple[int, ...]]:
    C = invariants(row)
    return [p for p in integer_partitions(C["u"]) if len(p) + 1 <= row.n - row.M2]


def face_data(row: Datum, part: Sequence[int], x: sy.Symbol, y: sy.Symbol) -> dict:
    C = invariants(row)
    if sum(part) != C["u"]:
        raise ValueError("partition sum mismatch")
    slopes = list(sy.symbols(f"s2:{len(part)+1}")) if len(part) > 1 else []
    factors: list[sy.Expr] = []
    names: list[str] = []
    for _ in range(part[0]):
        factors.append(y - x)
        names.append("y-x")
    for slope, multiplicity in zip(slopes, part[1:]):
        for _ in range(multiplicity):
            factors.append(y - slope * x)
            names.append(f"y-{slope}*x")
    for _ in range(row.V2):
        factors.append(y)
        names.append("y")
    top = sy.prod(factors)
    omega = sy.Integer(1)
    for slope in slopes:
        omega *= slope * (slope - 1)
    for i, left in enumerate(slopes):
        for right in slopes[i + 1:]:
            omega *= left - right
    return {"top": sy.expand(top), "factors": factors, "factor_names": names,
            "slopes": slopes, "omega": sy.expand(omega)}


def allowed_h_support(row: Datum, C: dict) -> list[tuple[int, int]]:
    support = []
    for ypow in range(C["K"], -1, -1):
        for xpow in range(C["u"] + 1):
            if xpow + ypow >= C["K"]:
                continue
            weight = -xpow + C["delta1"] * ypow
            if weight >= C["B"]:
                support.append((xpow, ypow))
    return support


def sparse_prefixes(row: Datum, part: Sequence[int], x: sy.Symbol, y: sy.Symbol) -> dict:
    C = invariants(row)
    face = face_data(row, part, x, y)
    if len(face["factors"]) != C["K"]:
        raise AssertionError("factor count is not K")
    b = list(sy.symbols(f"b1:{C['K']+1}"))
    prefix_product = sy.Integer(1)
    H: dict[int, sy.Expr] = {}
    weights: dict[int, Fraction] = {}
    outer = center = 0
    for degree, factor in enumerate(face["factors"], start=1):
        prefix_product = sy.expand(prefix_product * factor)
        if factor == y:
            center += 1
        else:
            outer += 1
        weights[degree] = outer * C["delta2"] + center * C["delta1"]
        if degree == 1:
            H[degree] = prefix_product
        elif degree == 2:
            H[degree] = sy.expand(factor * H[degree - 1] + b[0] * y + b[1])
        else:
            H[degree] = sy.expand(factor * H[degree - 1] + b[degree - 1])
    if weights[C["K"]] != C["B"]:
        raise AssertionError("top weight and common bound disagree")
    return {"face": face, "H": H, "weights": weights, "b": b}


def polynomial_support(expr: sy.Expr, x: sy.Symbol, y: sy.Symbol) -> list[tuple[int, int]]:
    return sorted((int(mon[0]), int(mon[1])) for mon, coefficient in sy.Poly(sy.expand(expr), x, y).terms()
                  if coefficient != 0)


def build_h(row: Datum, part: Sequence[int], mode: str, x: sy.Symbol, y: sy.Symbol) -> dict:
    C = invariants(row)
    tower = sparse_prefixes(row, part, x, y)
    h = tower["H"][C["K"]]
    extra: list[sy.Symbol] = []
    if mode == "envelope":
        # Sparse pivots are y^4,y^3,y^2,y,1.  These four directions free
        # xy^3, xy^2, x^2y^2, xy and span the complete nine-monomial envelope.
        candidates = [(1, 3), (1, 2), (2, 2), (1, 1)]
        allowed = set(allowed_h_support(row, C))
        if not set(candidates) <= allowed:
            raise ValueError("envelope relaxation is specialized to the open K=5 row")
        extra = list(sy.symbols("r13 r12 r22 r11"))
        for parameter, (xpow, ypow) in zip(extra, candidates):
            h += parameter * x**xpow * y**ypow
        h = sy.expand(h)
    elif mode != "sparse":
        raise ValueError(mode)
    lower = sy.expand(h - tower["face"]["top"])
    tower.update({"h": h, "extra_h_params": extra,
                  "h_support": polynomial_support(lower, x, y),
                  "allowed_h_support": allowed_h_support(row, C)})
    return tower


def same(a: sy.Expr, b: sy.Expr) -> bool:
    return sy.expand(a - b) == 0


def filtered_spaces(row: Datum, C: dict, tower: dict, x: sy.Symbol) -> dict:
    weighted: list[tuple[sy.Expr, Fraction, str]] = [(sy.Integer(1), Fraction(0), "1")]
    for degree in range(C["K"] - 1, 0, -1):
        weighted.append((tower["H"][degree], tower["weights"][degree], f"H{degree}"))
    weighted.append((x, C["delta2"], "x"))
    unique: list[tuple[sy.Expr, Fraction, str]] = []
    for item in weighted:
        if not any(same(item[0], prior[0]) for prior in unique):
            unique.append(item)
    weighted = sorted(unique, key=lambda item: (-item[1], item[2]))

    def space(deficit: int) -> list[sy.Expr]:
        cutoff = deficit * C["B"]
        return [expr for expr, weight, _ in weighted if weight >= cutoff]

    alpha = {i: space(i) for i in range(1, C["e"] + 1)}
    beta = {i: space(i) for i in range(2, C["q"] + 1)}
    alpha_pre = [len(alpha[i]) for i in range(1, C["e"] + 1)]
    beta_pre = [len(beta[i]) for i in range(2, C["q"] + 1)]
    gauges: list[str] = []
    notes: list[str] = []

    shear = C["e"] - C["q"]
    scalar = alpha.get(shear, []) == [sy.Integer(1)]
    embeds = scalar
    if embeds:
        for deficit, source in beta.items():
            target = alpha.get(deficit + shear, [])
            if any(not any(same(basis, candidate) for candidate in target) for basis in source):
                embeds = False
                break
    if embeds:
        alpha[shear] = []
        gauges.append(f"shear alpha_{shear}")
    else:
        notes.append(f"alpha_{shear} shear omitted")
    if sy.Integer(1) in beta.get(C["q"], []):
        beta[C["q"]] = [term for term in beta[C["q"]] if term != 1]
        gauges.append(f"translate beta_{C['q']}")
    if sy.Integer(1) in alpha.get(C["e"], []):
        alpha[C["e"]] = [term for term in alpha[C["e"]] if term != 1]
        gauges.append(f"translate alpha_{C['e']}")
    return {"weighted": weighted, "alpha": alpha, "beta": beta,
            "alpha_pre": alpha_pre, "beta_pre": beta_pre,
            "alpha_post": [len(alpha[i]) for i in range(1, C["e"] + 1)],
            "beta_post": [len(beta[i]) for i in range(2, C["q"] + 1)],
            "gauges": gauges, "gauge_notes": notes,
            "shear_scalar": scalar, "shear_embeddings": embeds}


def generic_coefficient(prefix: str, deficit: int, basis: Sequence[sy.Expr], parameters: list[sy.Symbol]) -> sy.Expr:
    value = sy.Integer(0)
    for index, term in enumerate(basis):
        symbol = sy.Symbol(f"{prefix}{deficit}_{index}")
        parameters.append(symbol)
        value += symbol * term
    return sy.expand(value)


def h_adic_digits(poly: sy.Expr, h: sy.Expr, y: sy.Symbol) -> dict[int, sy.Expr]:
    """Return the unique remainders in poly=sum rem_i*h^i, deg_y rem_i<deg_y h."""
    digits: dict[int, sy.Expr] = {}
    current = sy.expand(poly)
    hpoly = sy.Poly(h, y)
    level = 0
    while current != 0:
        quotient, remainder = sy.div(sy.Poly(current, y), hpoly, y)
        rem = sy.expand(remainder.as_expr())
        if rem != 0:
            digits[level] = rem
        current = sy.expand(quotient.as_expr())
        level += 1
        if level > 64:
            raise AssertionError("h-adic division failed to terminate")
    digits.setdefault(0, sy.Integer(0))
    return digits


def h_adic_jacobian_identity(low_terms: Sequence[tuple[sy.Expr, int]],
                             high_terms: Sequence[tuple[sy.Expr, int]],
                             h: sy.Expr, x: sy.Symbol, y: sy.Symbol) -> dict[int, sy.Expr]:
    """Bilinear expansion before the same ascending monic normalization."""
    levels: dict[int, sy.Expr] = {}
    J = lambda left, right: sy.diff(left, x) * sy.diff(right, y) - sy.diff(left, y) * sy.diff(right, x)
    for left, r in low_terms:
        for right, s in high_terms:
            same_level = J(left, right)
            if same_level != 0:
                levels[r + s] = levels.get(r + s, 0) + same_level
            next_down = s * right * J(left, h) + r * left * J(h, right)
            if next_down != 0:
                levels[r + s - 1] = levels.get(r + s - 1, 0) + next_down
    levels.setdefault(0, sy.Integer(0))
    hpoly = sy.Poly(h, y)
    level = 0
    maximum = max(levels)
    while level <= maximum:
        value = sy.expand(levels.get(level, 0))
        if value != 0:
            quotient, remainder = sy.div(sy.Poly(value, y), hpoly, y)
            levels[level] = sy.expand(remainder.as_expr())
            if quotient != 0:
                levels[level + 1] = levels.get(level + 1, 0) + sy.expand(quotient.as_expr())
                maximum = max(maximum, level + 1)
        level += 1
    return {level: sy.expand(value) for level, value in levels.items() if value != 0} | {
        0: sy.expand(levels.get(0, 0))
    }


def coefficient_rows(digits: dict[int, sy.Expr], c: sy.Symbol, k: int,
                     x: sy.Symbol, y: sy.Symbol) -> list[dict]:
    adjusted = dict(digits)
    adjusted[0] = sy.expand(adjusted.get(0, 0) - c * x**k)
    rows = []
    for level in sorted(adjusted):
        expression = sy.expand(adjusted[level])
        if expression == 0:
            continue
        for monomial, coefficient in sy.Poly(expression, x, y).terms():
            coefficient = sy.expand(coefficient)
            if coefficient != 0:
                rows.append({"h_power": level, "x_power": int(monomial[0]),
                             "y_power": int(monomial[1]), "expr": coefficient})
    return rows


def build_chart(row: Datum, part: Sequence[int], mode: str, jac_method: str) -> dict:
    C = invariants(row)
    x, y = sy.symbols("x y")
    c = sy.Symbol("c")
    tower = build_h(row, part, mode, x, y)
    spaces = filtered_spaces(row, C, tower, x)
    parameters = list(tower["b"]) + list(tower["extra_h_params"]) + list(tower["face"]["slopes"])
    alpha = {i: generic_coefficient("A", i, spaces["alpha"][i], parameters)
             for i in range(1, C["e"] + 1)}
    beta = {i: generic_coefficient("B", i, spaces["beta"][i], parameters)
            for i in range(2, C["q"] + 1)}
    h = tower["h"]
    high_terms = [(sy.Integer(1), C["e"])] + [(alpha[i], C["e"] - i) for i in alpha]
    low_terms = [(sy.Integer(1), C["q"])] + [(beta[i], C["q"] - i) for i in beta]
    if jac_method == "direct":
        P = sum(coefficient * h**power for coefficient, power in high_terms)
        Q = sum(coefficient * h**power for coefficient, power in low_terms)
        jacobian = sy.diff(Q, x) * sy.diff(P, y) - sy.diff(Q, y) * sy.diff(P, x)
        digits = h_adic_digits(jacobian, h, y)
    elif jac_method == "identity":
        digits = h_adic_jacobian_identity(low_terms, high_terms, h, x, y)
    else:
        raise ValueError(jac_method)
    rows = coefficient_rows(digits, c, row.k, x, y)
    parameters.append(c)
    target = [record for record in rows if record["h_power"] == 0 and
              record["x_power"] == row.k and record["y_power"] == 0]
    target_before = sy.expand(digits.get(0, 0)).coeff(x, row.k).coeff(y, 0)
    maximum_x = max((sy.Poly(value, x).degree() for value in digits.values() if value != 0), default=-1)
    sat = sy.expand(c * tower["face"]["omega"])
    metadata = {
        "row": asdict(row), "partition": list(part), "mode": mode, "jacobian_method": jac_method,
        "closed_form": {name: qstr(value) if isinstance(value, Fraction) else value for name, value in C.items()},
        "top_face": singular_expr(tower["face"]["top"]),
        "omega": singular_expr(tower["face"]["omega"]),
        "saturation_factor": singular_expr(sat),
        "factor_order": tower["face"]["factor_names"],
        "h": singular_expr(h),
        "h_parameters": [str(p) for p in tower["b"] + tower["extra_h_params"]],
        "h_parameter_count": len(tower["b"] + tower["extra_h_params"]),
        "h_support": [list(m) for m in tower["h_support"]],
        "h_support_count": len(tower["h_support"]),
        "allowed_h_support": [list(m) for m in tower["allowed_h_support"]],
        "allowed_h_support_count": len(tower["allowed_h_support"]),
        "basis": [{"name": name, "weight": qstr(weight)} for _, weight, name in spaces["weighted"]],
        "alpha_dims_pre": spaces["alpha_pre"], "beta_dims_pre": spaces["beta_pre"],
        "alpha_dims": spaces["alpha_post"], "beta_dims": spaces["beta_post"],
        "gauges": spaces["gauges"], "gauge_notes": spaces["gauge_notes"],
        "shear_scalar_check": spaces["shear_scalar"],
        "shear_embedding_check": spaces["shear_embeddings"],
        "unknowns_excluding_T": len(parameters), "equations": len(rows),
        "h_levels": sorted(digits), "max_x_degree_among_remainders": int(maximum_x),
        "target_coefficient_before_minus_c": singular_expr(target_before),
        "target_rows": [{**{k: v for k, v in record.items() if k != "expr"},
                         "expr": singular_expr(record["expr"])} for record in target],
    }
    return {"meta": metadata, "rows": rows, "parameters": parameters, "sat": sat}


def write_system(record: dict, stem: str, characteristic: int) -> Path:
    metadata = record["meta"]
    variables = [str(parameter) for parameter in record["parameters"]] + ["T"]
    sat = singular_expr(record["sat"])
    generators = [singular_expr(row["expr"]) for row in record["rows"]] + [f"T*({sat})-1"]
    field = "Q" if characteristic == 0 else f"p{characteristic}"
    path = ART / f"{stem}_{field}.sing"
    path.parent.mkdir(parents=True, exist_ok=True)
    text = [
        "// independent_order_gate.py: direct Jacobian plus monic h-adic division",
        f"// row={metadata['row']} partition={metadata['partition']} mode={metadata['mode']}",
        f"// target_before={metadata['target_coefficient_before_minus_c']}",
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
        f"ideal emptyControl=({sat}),T*({sat})-1;",
        "ideal emptyBasis=std(emptyControl);",
        'if (reduce(1,emptyBasis)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        f"ideal liveControl=({sat})-1,T*({sat})-1;",
        "ideal liveBasis=std(liveControl);",
        'if (reduce(1,liveBasis)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        f'print("MAIN_START equations={len(record["rows"])} unknowns={len(record["parameters"])} char={characteristic}");',
        "ideal I=" + ",\n".join(generators) + ";",
        "ideal G=std(I);",
        'print("MAIN_BASIS_SIZE");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_SURVIVES"); }',
        "quit;",
    ]
    path.write_text("\n".join(text) + "\n", encoding="utf-8")
    return path


def write_record(record: dict, stem: str, chars: Sequence[int]) -> dict:
    ART.mkdir(parents=True, exist_ok=True)
    metadata = record["meta"]
    metadata["systems"] = {}
    for characteristic in chars:
        path = write_system(record, stem, characteristic)
        metadata["systems"][str(characteristic)] = str(path.relative_to(HERE))
    metadata_path = ART / f"{stem}.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    metadata["metadata_sha256"] = hashlib.sha256(metadata_path.read_bytes()).hexdigest()
    return metadata


def write_tame_control(chars: Sequence[int]) -> list[str]:
    ART.mkdir(parents=True, exist_ok=True)
    outputs = []
    for characteristic in chars:
        field = "Q" if characteristic == 0 else f"p{characteristic}"
        path = ART / f"tame_automorphism_{field}.sing"
        path.write_text("\n".join([
            "// (Q,P)=(y,y^2-x), J(Q,P)=1; inverse y=Q, x=Q^2-P",
            f"ring A={characteristic},(x,y),dp;",
            "poly Q=y;",
            "poly P=y^2-x;",
            "poly D=diff(Q,x)*diff(P,y)-diff(Q,y)*diff(P,x);",
            'if (D-1==0) { print("TAME_J_PASS"); } else { print("TAME_J_FAIL"); }',
            f"ring R={characteristic},(c,T),dp;",
            "ideal I=c-1,T*c-1;",
            "ideal G=std(I);",
            'if (reduce(1,G)!=0) { print("TAME_SURVIVES"); } else { print("TAME_FALSE_EMPTY"); }',
            "quit;",
        ]) + "\n", encoding="utf-8")
        outputs.append(str(path.relative_to(HERE)))
    return outputs


def parse_partition(text: str) -> tuple[int, ...]:
    values = tuple(int(piece) for piece in re.split(r"[+,]", text) if piece)
    if not values:
        raise argparse.ArgumentTypeError("empty partition")
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", choices=sorted(DATA), default="open_25_15")
    parser.add_argument("--partition", type=parse_partition)
    parser.add_argument("--all-partitions", action="store_true")
    parser.add_argument("--mode", choices=["sparse", "envelope"], default="sparse")
    parser.add_argument("--jac-method", choices=["direct", "identity"], default="identity")
    parser.add_argument("--chars", default="0,32051,32057")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--tame-control", action="store_true")
    args = parser.parse_args()
    chars = [int(value) for value in args.chars.split(",") if value]
    if args.tame_control:
        print(json.dumps({"tame_systems": write_tame_control(chars)}, indent=2))
        return
    row = DATA[args.row]
    parts = admissible_parts(row) if args.all_partitions else [args.partition]
    if not parts or parts == [None]:
        raise SystemExit("use --partition or --all-partitions")
    summary = []
    for part in parts:
        if tuple(part) not in admissible_parts(row):
            raise SystemExit(f"inadmissible partition {part}")
        record = build_chart(row, part, args.mode, args.jac_method)
        stem = f"{row.key}_part_{'_'.join(map(str, part))}_{args.mode}"
        summary.append(write_record(record, stem, chars) if args.write else record["meta"])
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
