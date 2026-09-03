#!/usr/bin/env python3
"""Symbolic B3-axis derivation and frozen-record restriction checks."""
from __future__ import annotations

import json
import pathlib

import sympy as sp

INPUT = pathlib.Path("/tmp/jc2-lane.JyEMIr/inputs")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16conegate-20260903")


def red_d(expr: sp.Expr, t: sp.Symbol, d: sp.Symbol) -> sp.Expr:
    minpoly = 3*d**2 - (t + 1)
    expr = sp.together(sp.expand(expr))
    numer, denom = sp.fraction(expr)
    numer = sp.rem(sp.Poly(sp.expand(numer), d), sp.Poly(minpoly, d)).as_expr()
    denom = sp.rem(sp.Poly(sp.expand(denom), d), sp.Poly(minpoly, d)).as_expr()
    if sp.Poly(denom, d).degree() > 0:
        a0 = sp.Poly(denom, d).nth(0)
        a1 = sp.Poly(denom, d).nth(1)
        numer = sp.rem(sp.Poly(sp.expand(numer * (a0 - a1*d)), d),
                       sp.Poly(minpoly, d)).as_expr()
        denom = sp.expand(a0**2 - a1**2 * (t + 1) / 3)
    return sp.expand(sp.cancel(numer / denom))


def symbolic_axis() -> dict[str, object]:
    t, b3, lam, d = sp.symbols("t b3 lam d")
    q = 2*t + 1
    e = 3*t + 1
    red = lambda expr: red_d(expr, t, d)
    y = red((d + t + 1) / (2*q))
    g = red(e*t*(3*d + 2*(t + 1)) / (6*q**3))
    g1 = e / q
    g2 = red(g*(3*t + 2) / (2*t*y))
    c = red(-y*g)

    checks = {
        "H_t_to_3d2": red(12*q**2*y**2 - 12*q*(t + 1)*y + (t + 1)*(3*t + 2)),
        "(3t+2)g-2tyg2": red((3*t + 2)*g - 2*t*y*g2),
        "3qg+(t+1)g2-(4t+1)yg1": red(3*q*g + (t + 1)*g2 - (4*t + 1)*y*g1),
        "2qg2-tg1-2ey": red(2*q*g2 - t*g1 - 2*e*y),
    }

    w = lam*b3
    delta = red(g*(6*t*w + (5*t + 2)*b3) / (2*y*(2*t - 1)))
    eta = red(delta - g2*b3)
    Bc = red((eta + q*y*g1*b3 - 2*q*g*b3 + 2*t*g2*w) / (2*y))
    Cc = red(t*b3*(y*eta - 2*w*g) / (2*y))
    band_3t = red(Bc - y*b3*e - q*eta - t*w*g1)
    band_2tm1 = red(Cc - y*b3*Bc - t*w*eta)
    band_tm2 = red(-y*b3*Cc)

    sol = sp.solve(sp.Eq(sp.expand(band_3t / b3), 0), lam)
    if len(sol) != 1:
        raise RuntimeError(f"expected one lambda solution, got {sol}")
    lam_value = red(sol[0])
    alpha = sp.factor(sp.simplify(red(band_2tm1.subs(lam, lam_value)) / b3**2))
    phi = sp.factor(sp.simplify(red(band_tm2.subs(lam, lam_value)) / b3**3))
    band_3t_at_lam = sp.simplify(red(band_3t.subs(lam, lam_value)))

    norm_phi = sp.factor(sp.expand((-(t + 1))**2 - (6*t)**2*(t + 1)/3))
    lin_alpha = (27*t**3 - 30*t**2 + t - 2)*d + (6*t**3 + 13*t**2 - 3*t + 2)
    poly_alpha = sp.Poly(lin_alpha, d)
    norm_alpha = sp.factor(
        sp.expand(poly_alpha.nth(0)**2 - poly_alpha.nth(1)**2*(t + 1)/3)
    )

    return {
        "checks": {name: str(sp.simplify(value)) for name, value in checks.items()},
        "lambda": str(sp.factor(lam_value)),
        "band_3t_at_lambda": str(band_3t_at_lam),
        "alpha": str(alpha),
        "phi": str(phi),
        "norm_phi_linear": str(norm_phi),
        "norm_alpha_linear": str(norm_alpha),
        "norm_phi_integer_roots_ge_1": [
            str(r) for r in sp.solve(sp.Eq(sp.expand(norm_phi*3), 0), t)
            if r.is_integer and r >= 1
        ],
        "norm_alpha_integer_roots_ge_1": [
            str(r) for r in sp.solve(sp.Eq(sp.expand(norm_alpha*3), 0), t)
            if r.is_integer and r >= 1
        ],
        "phi_prefactor_integer_roots": [
            str(r) for r in sp.solve(sp.Eq(t*(t - 2)*(3*t + 1), 0), t)
            if r.is_integer
        ],
        "alpha_prefactor_integer_roots": [
            str(r) for r in sp.solve(sp.Eq(t*(3*t + 1), 0), t)
            if r.is_integer
        ],
    }


def ns_for_t(t: int) -> dict[str, sp.Symbol]:
    names = ["b3", "b4", f"q{2*t+1}_1"] + [f"q{j}_0" for j in range(2, t)]
    return {name: sp.Symbol(name) for name in names}


def mod_h(expr: sp.Expr, y: sp.Symbol, H: sp.Expr) -> sp.Expr:
    expr = sp.cancel(sp.together(sp.expand(expr)))
    numer, denom = sp.fraction(expr)
    rem = sp.rem(sp.Poly(sp.expand(numer), y), sp.Poly(H, y)).as_expr()
    return sp.expand(sp.cancel(rem / denom))


def forms_for_t(t: int) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Symbol, sp.Expr]:
    tt = sp.Integer(t)
    q = 2*tt + 1
    e = 3*tt + 1
    y = sp.Symbol(f"q{2*t+1}_1")
    d = 2*q*y - (tt + 1)
    H = sp.expand(12*q**2*y**2 - 12*q*(tt + 1)*y + (tt + 1)*(3*tt + 2))

    def red_y(expr: sp.Expr) -> sp.Expr:
        expr = sp.cancel(sp.together(sp.expand(expr)))
        numer, denom = sp.fraction(expr)
        rem = sp.rem(sp.Poly(sp.expand(numer), y), sp.Poly(H, y)).as_expr()
        return sp.expand(sp.cancel(rem / denom))

    alpha = red_y(
        tt*(3*tt + 1)*
        ((27*tt**3 - 30*tt**2 + tt - 2)*d + (6*tt**3 + 13*tt**2 - 3*tt + 2)) /
        (12*(2*tt + 1)**2*(3*tt - 1)**2*(3*tt + 2))
    )
    phi = red_y(
        -tt*(tt - 2)*(3*tt + 1)*(6*tt*d - (tt + 1)) /
        (72*(2*tt + 1)**3*(3*tt - 1))
    )
    g = red_y(e*tt*(3*d + 2*(tt + 1))/(6*q**3))
    c = red_y(-y*g)
    return alpha, phi, c, y, H


def restricted_rows(record_name: str) -> tuple[int, dict[int, sp.Expr], sp.Symbol, sp.Expr]:
    rec = json.loads((INPUT / record_name).read_text(encoding="utf-8"))
    t = int(rec["t"])
    ns = ns_for_t(t)
    y = ns[f"q{2*t+1}_1"]
    H = sp.sympify(rec["H"], locals=ns)
    subs = {sp.Symbol(f"q{j}_0"): 0 for j in range(2, t)}
    if "b4" in ns:
        subs[ns["b4"]] = 0
    rows = {}
    for item in rec["terminal"]:
        rows[int(item["band"])] = sp.expand(sp.sympify(item["expr"], locals=ns).subs(subs))
    return t, rows, y, H


def record_axis_checks() -> list[dict[str, object]]:
    records = [
        "terminal_laurent_t2.json",
        "terminal_laurent_t3.json",
        "terminal_laurent_t4.json",
        "terminal_laurent_t5.json",
        "chart_t3_b4_0.json",
        "chart_t5_b4_0.json",
        "chart_t6_b4_0.json",
    ]
    out = []
    b3 = sp.Symbol("b3")
    for record_name in records:
        t, rows, y, H = restricted_rows(record_name)
        alpha, phi, c, _y2, _H2 = forms_for_t(t)
        failures = []
        for band, got in sorted(rows.items()):
            want = c if band == 0 else sp.Integer(0)
            if band == 2*t - 1:
                want = alpha*b3**2
            if band == t - 2 and t >= 3:
                want = phi*b3**3
            if band == 0 and t == 2:
                want = c + phi*b3**3
            if mod_h(got - want, y, H) != 0:
                failures.append({"band": band, "residue": str(mod_h(got - want, y, H))})
        item = {
            "record": record_name,
            "t": t,
            "ok": not failures,
            "failures": failures,
            "nonzero_bands_expected": [0, t - 2, 2*t - 1] if t >= 3 else [0, 3],
        }
        out.append(item)
        print(f"{record_name}: B3-axis restriction {'MATCH' if item['ok'] else 'MISMATCH'}")
    return out


def main() -> None:
    symbolic = symbolic_axis()
    for name, value in symbolic["checks"].items():
        print(f"check {name} = {value}")
    print("lambda =", symbolic["lambda"])
    print("alpha =", symbolic["alpha"])
    print("phi =", symbolic["phi"])
    print("N_phi =", symbolic["norm_phi_linear"])
    print("N_alpha =", symbolic["norm_alpha_linear"])
    records = record_axis_checks()
    status = "PASS" if all(v == "0" for v in symbolic["checks"].values()) and all(r["ok"] for r in records) else "FAIL"
    print("B3_AXIS_REPLAY =", status)
    (OUT / "b3_axis_replay.json").write_text(
        json.dumps({"status": status, "symbolic": symbolic, "record_checks": records},
                   indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
