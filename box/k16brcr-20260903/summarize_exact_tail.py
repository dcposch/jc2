#!/usr/bin/env python3
"""Summarise the exact split-tail transcripts with SymPy.

The script performs no interpolation and no Groebner computation.  It parses
the exact A_t coefficients printed by Singular, checks weighted supports, writes
clean explicit-polynomial artifacts, and evaluates the t=3 q2-axis control in
the quadratic coefficient algebra.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def records(path: Path) -> dict[tuple[str, int], str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    marker_counts = {
        "RECURRENCE_PASS": sum(line.startswith("RECURRENCE_PASS ") for line in lines),
        "BRCR_DONE": lines.count("BRCR_DONE"),
        "DRIVER_DONE": lines.count("DRIVER_DONE"),
    }
    for marker, count in marker_counts.items():
        if count != 1:
            raise AssertionError((path, marker, count))
    bad = [
        line
        for line in lines
        if re.search(r"(?:^|\s)FAIL(?:\s|$)|error occurred|div\. by 0", line, re.I)
    ]
    if bad:
        raise AssertionError((path, bad))
    out: dict[tuple[str, int], str] = {}
    patterns = {
        "T": re.compile(r"^BRCR_ROW r=(\d+) k=(\d+)$"),
        "a": re.compile(r"^BRCR_A r=(\d+) size=\d+$"),
        "b": re.compile(r"^BRCR_b r=(\d+) size=\d+$"),
        "c": re.compile(r"^BRCR_c r=(\d+) size=\d+$"),
        "B": re.compile(r"^BRCR_B r=(\d+) size=\d+$"),
        "C": re.compile(r"^BRCR_C r=(\d+) size=\d+$"),
        "W": re.compile(r"^BRCR_W r=(\d+) size=\d+$"),
    }
    for index, line in enumerate(lines[:-1]):
        for kind, pattern in patterns.items():
            match = pattern.match(line)
            if match:
                out[(kind, int(match.group(1)))] = lines[index + 1].strip()
                break
    return out


def parse_expr(raw: str, symbols: dict[str, sp.Symbol]) -> sp.Expr:
    return sp.sympify(raw.replace("^", "**"), locals=symbols)


def pcount(weight: int, maxpart: int) -> int:
    counts = [0] * (weight + 1)
    counts[0] = 1
    for part in range(1, maxpart + 1):
        for degree in range(part, weight + 1):
            counts[degree] += counts[degree - part]
    return counts[weight]


def weighted_tuples(weight: int, maxpart: int) -> set[tuple[int, ...]]:
    """All exponent tuples for variables of weights 1,...,maxpart."""
    found: set[tuple[int, ...]] = set()

    def visit(part: int, remaining: int, prefix: tuple[int, ...]) -> None:
        if part > maxpart:
            if remaining == 0:
                found.add(prefix)
            return
        for exponent in range(remaining // part + 1):
            visit(part + 1, remaining - part * exponent, (*prefix, exponent))

    visit(1, weight, ())
    if len(found) != pcount(weight, maxpart):
        raise AssertionError((weight, maxpart, len(found), pcount(weight, maxpart)))
    return found


def coeff_to_d(value: sp.Expr, t: int, yy: sp.Symbol, d: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    return sp.cancel(value.subs(yy, (d + t + 1) / (2 * q)))


def quadratic_norm(value_d: sp.Expr, t: int, d: sp.Symbol) -> sp.Expr:
    poly = sp.Poly(sp.cancel(value_d), d)
    if poly.degree() < 0:
        return sp.Integer(0)
    if poly.degree() > 1:
        raise AssertionError((t, value_d, poly.degree()))
    aa = poly.nth(1)
    bb = poly.nth(0)
    return sp.factor(bb**2 - sp.Rational(t + 1, 3) * aa**2)


def compact_linear(value_d: sp.Expr, d: sp.Symbol) -> str:
    """Canonical ``(A*d+B)/D`` representation with coprime integers."""
    poly = sp.Poly(sp.cancel(value_d), d)
    aa = sp.Rational(poly.nth(1))
    bb = sp.Rational(poly.nth(0))
    den = sp.ilcm(int(aa.q), int(bb.q))
    aaa = int(aa * den)
    bbb = int(bb * den)
    common = math.gcd(math.gcd(abs(aaa), abs(bbb)), den)
    aaa //= common
    bbb //= common
    den //= common
    if den < 0:
        aaa, bbb, den = -aaa, -bbb, -den
    return f"({aaa}*d{bbb:+d})/{den}"


def reduce_y(value: sp.Expr, t: int, yy: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    hpoly = sp.Poly(
        12 * q * q * yy**2 - 12 * q * (t + 1) * yy + (t + 1) * (3 * t + 2),
        yy,
        domain=sp.QQ,
    )
    num, den = sp.fraction(sp.cancel(value))
    num_poly = sp.Poly(num, yy, domain=sp.QQ)
    den_poly = sp.Poly(den, yy, domain=sp.QQ)
    inv_den = sp.invert(den_poly, hpoly)
    return sp.rem(num_poly * inv_den, hpoly).as_expr()


def inv_y(value: sp.Expr, t: int, yy: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    hpoly = sp.Poly(
        12 * q * q * yy**2 - 12 * q * (t + 1) * yy + (t + 1) * (3 * t + 2), yy
    )
    inv = sp.invert(sp.Poly(value, yy), hpoly)
    return inv.as_expr()


def summarise(t: int, suffix: str) -> tuple[list[dict[str, object]], dict[tuple[str, int], str]]:
    path = HERE / f"brcr_t{t}_{suffix}.out"
    rec = records(path)
    expected_keys = {
        *((kind, r) for kind in ("T", "a", "b", "c") for r in range(t)),
        *((kind, r) for kind in ("B", "C", "W") for r in range(1, t)),
    }
    if set(rec) != expected_keys:
        raise AssertionError(
            (path, "record keys", sorted(expected_keys - set(rec)), sorted(set(rec) - expected_keys))
        )
    yy, d, b4, b3 = sp.symbols("yy d b4 b3")
    qvars = [sp.Symbol(f"q{j}_0") for j in range(2, t)]
    symbols = {str(v): v for v in [yy, d, b4, b3, *qvars]}
    base = [b4, *qvars]
    rows: list[dict[str, object]] = []
    for kind in ("a", "b", "c", "B", "C"):
        rs = range(t) if kind in ("a", "b", "c") else range(1, t)
        for r in rs:
            raw = rec[(kind, r)]
            expr = parse_expr(raw, symbols)
            if kind == "a":
                weight = r
            elif kind in ("b", "B"):
                weight = t + 1 + r
            else:
                weight = 2 * t + 2 + r
            poly = sp.Poly(expr, *base)
            actual_monomials = set(poly.monoms()) if expr != 0 else set()
            expected_monomials = weighted_tuples(weight, t - 1)
            actual = len(actual_monomials)
            expected = len(expected_monomials)
            axis = sp.expand(expr.subs({v: 0 for v in qvars}))
            leader = sp.cancel(axis.coeff(b4, weight))
            leader_d = coeff_to_d(leader, t, yy, d)
            norm = quadratic_norm(leader_d, t, d)
            rows.append(
                {
                    "t": t,
                    "branch": suffix,
                    "kind": kind,
                    "r": r,
                    "weight": weight,
                    "support": actual,
                    "expected_full_support": expected,
                    "full_support": actual_monomials == expected_monomials,
                    "leader_monomial": f"b4^{weight}",
                    "leader_coefficient_d": str(leader_d),
                    "leader_compact": compact_linear(leader_d, d),
                    "leader_norm": str(norm),
                    "leader_unit": norm != 0,
                }
            )
    explicit = [
        f"// Exact split tail for t={t}; coefficient relation H_t(yy)=0.",
        "// Singular syntax; generated from the verified frozen recurrence.",
    ]
    for r in range(t):
        k = 2 * t - 1 - r
        for kind in ("T", "a", "b", "c"):
            explicit.append(f"{kind}_{r if kind != 'T' else k} = {rec[(kind, r)]};")
    for r in range(1, t):
        explicit.append(f"B_{r} = {rec[('B', r)]};")
        explicit.append(f"C_{r} = {rec[('C', r)]};")
    (HERE / f"explicit_tail_t{t}_{suffix}.txt").write_text("\n".join(explicit) + "\n")
    return rows, rec


def t3_axis_control(rec: dict[tuple[str, int], str]) -> dict[str, str | bool]:
    t = 3
    yy, d, b4, b3, q2 = sp.symbols("yy d b4 b3 q2_0")
    symbols = {str(v): v for v in (yy, d, b4, b3, q2)}
    parsed = {key: parse_expr(raw, symbols) for key, raw in rec.items() if key[0] in {"a", "b", "c", "B", "C", "W", "T"}}
    sub_axis = {b4: 0, q2: 1}
    b2 = sp.cancel(parsed[("B", 2)].subs(sub_axis))
    c2 = sp.cancel(parsed[("C", 2)].subs(sub_axis))
    beta = reduce_y(-c2 * inv_y(b2, t, yy), t, yy)
    qtop = reduce_y(
        parsed[("a", 0)].subs(sub_axis) * beta**2
        + parsed[("b", 0)].subs(sub_axis) * beta
        + parsed[("c", 0)].subs(sub_axis),
        t,
        yy,
    )
    w1 = reduce_y(parsed[("W", 1)].subs(sub_axis), t, yy)
    w2 = reduce_y(parsed[("W", 2)].subs(sub_axis), t, yy)
    identity = reduce_y(w2 - b2**2 * qtop, t, yy)
    qtop_d = coeff_to_d(qtop, t, yy, d)
    row1_zero = all(
        reduce_y(parsed[(kind, 1)].subs(sub_axis), t, yy) == 0
        for kind in ("B", "C")
    )
    return {
        "point": "b4=0,q2_0=1",
        "row1_C_B": str((parsed[("C", 1)].subs(sub_axis), parsed[("B", 1)].subs(sub_axis))),
        "row2_B": str(b2),
        "row2_C": str(c2),
        "beta": str(beta),
        "Q": str(qtop),
        "Q_d": str(qtop_d),
        "Q_norm": str(quadratic_norm(qtop_d, t, d)),
        "W1": str(w1),
        "W2": str(w2),
        "W2_minus_B2sq_Q": str(identity),
        "rank_one": b2 != 0 or c2 != 0,
        "row1_zero": row1_zero,
        "W1_zero": w1 == 0,
        "W2_nonzero": w2 != 0,
        "Q_nonzero": qtop != 0,
        "identity_pass": identity == 0,
    }


def main() -> None:
    all_rows: list[dict[str, object]] = []
    rec_t3 = None
    for t in range(3, 7):
        rows, rec = summarise(t, "exact")
        all_rows.extend(rows)
        if t == 3:
            rec_t3 = rec
    for branch in (0, 1):
        rows, _ = summarise(2, f"split_b{branch}")
        all_rows.extend(rows)
    assert rec_t3 is not None
    failures = [
        row
        for row in all_rows
        if not row["full_support"]
        and not (
            row["t"] == 2
            and row["branch"] == "split_b0"
            and row["kind"] in {"a", "B", "C"}
        )
    ]
    if failures:
        raise AssertionError(failures)
    d = sp.Symbol("d")
    alpha_checks = []
    for t in range(3, 7):
        q = 2 * t + 1
        aa = 27 * t**3 - 30 * t**2 + t - 2
        bb = 6 * t**3 + 13 * t**2 - 3 * t + 2
        expected = -sp.Rational(t * (3 * t + 1), 12 * q**2 * (3 * t - 1) ** 2 * (3 * t + 2)) * (aa * d + bb)
        actual_raw = next(row["leader_coefficient_d"] for row in all_rows if row["t"] == t and row["kind"] == "a" and row["r"] == 0)
        actual = sp.sympify(actual_raw, locals={"d": d})
        difference = sp.cancel(actual - expected)
        alpha_checks.append({"t": t, "difference": str(difference), "pass": difference == 0})
    if not all(item["pass"] for item in alpha_checks):
        raise AssertionError(alpha_checks)
    (HERE / "support_leaders.json").write_text(json.dumps(all_rows, indent=2) + "\n")
    columns = ["t", "branch", "kind", "r", "weight", "support", "expected_full_support", "full_support", "leader_monomial", "leader_coefficient_d", "leader_norm", "leader_unit"]
    tsv = ["\t".join(columns)]
    for row in all_rows:
        tsv.append("\t".join(str(row[column]) for column in columns))
    (HERE / "support_leaders.tsv").write_text("\n".join(tsv) + "\n")
    compact_columns = ["t", "branch", "kind", "r", "weight", "support", "leader_monomial", "leader_compact", "leader_unit"]
    compact_tsv = ["\t".join(compact_columns)]
    for row in all_rows:
        compact_tsv.append("\t".join(str(row[column]) for column in compact_columns))
    (HERE / "support_leaders_compact.tsv").write_text("\n".join(compact_tsv) + "\n")
    control = t3_axis_control(rec_t3)
    if not all(
        (
            control["rank_one"],
            control["row1_zero"],
            control["W1_zero"],
            control["W2_nonzero"],
            control["Q_nonzero"],
            control["identity_pass"],
        )
    ):
        raise AssertionError(control)
    (HERE / "t3_q2_axis_control.json").write_text(json.dumps(control, indent=2) + "\n")
    (HERE / "alpha_formula_checks.json").write_text(json.dumps(alpha_checks, indent=2) + "\n")
    print(json.dumps({"rows": len(all_rows), "alpha_formula_checks": alpha_checks, "t3_axis_control": control}, indent=2))


if __name__ == "__main__":
    main()
