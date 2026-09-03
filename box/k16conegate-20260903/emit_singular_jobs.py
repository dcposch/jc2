#!/usr/bin/env python3
"""Emit bounded Singular jobs for cone-gate fixed-t checks."""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction

import sympy as sp

INPUT = pathlib.Path("/tmp/jc2-lane.JyEMIr/inputs")
OUT = pathlib.Path("/home/ubuntu/jc2/box/k16conegate-20260903")


def load_record(t: int) -> dict[str, object]:
    return json.loads((INPUT / f"terminal_laurent_t{t}.json").read_text(encoding="utf-8"))


def ns_for_t(t: int, include_z: bool = False) -> dict[str, sp.Symbol]:
    names = ["b3", "b4", f"q{2*t+1}_1"] + [f"q{j}_0" for j in range(2, t)]
    if include_z:
        names.insert(0, "z")
    return {name: sp.Symbol(name) for name in names}


def clear_primitive(expr: sp.Expr, variables: list[sp.Symbol]) -> sp.Expr | None:
    expr = sp.expand(expr)
    if expr == 0:
        return None
    poly = sp.Poly(expr, *variables, domain="QQ")
    den = 1
    for coeff in poly.coeffs():
        den = sp.ilcm(den, Fraction(coeff).denominator)
    poly = sp.Poly(sp.expand(expr * den), *variables, domain="QQ")
    gcd = abs(sp.gcd(list(poly.coeffs())))
    return sp.expand(poly.as_expr() / gcd)


def singular_expr(expr: sp.Expr, y: sp.Symbol | None = None) -> str:
    text = str(sp.expand(expr)).replace("**", "^")
    if y is not None:
        text = text.replace(str(y), "Y")
    return text


def h_poly(t: int, y: sp.Symbol) -> sp.Expr:
    q = 2*t + 1
    return sp.expand(12*q*q*y*y - 12*q*(t + 1)*y + (t + 1)*(3*t + 2))


def split_roots(t: int) -> list[sp.Rational]:
    quotient, remainder = divmod(t + 1, 3)
    root = int(sp.sqrt(quotient))
    if remainder or root * root != quotient:
        raise ValueError(f"t={t} is not split over Q")
    q = 2*t + 1
    return sorted([sp.Rational(t + 1 - root, 2*q), sp.Rational(t + 1 + root, 2*q)])


def dim_job(t: int, tag: str, char: int, minpoly: sp.Expr | None,
            subs: dict[sp.Symbol, sp.Expr], algorithm: str = "std") -> pathlib.Path:
    rec = load_record(t)
    ns = ns_for_t(t)
    y = ns[f"q{2*t+1}_1"]
    variables = [ns["b4"]] + [ns[f"q{j}_0"] for j in range(2, t)] + [ns["b3"]]
    weights = [1] + list(range(2, t)) + [t + 1]
    gens = []
    allvars = variables + ([] if minpoly is None else [y])
    for item in rec["terminal"]:
        band = int(item["band"])
        if band == 0:
            continue
        expr = sp.sympify(item["expr"], locals=ns).subs(subs)
        gen = clear_primitive(expr, allvars)
        if gen is not None:
            gens.append(gen)
    if minpoly is None:
        header = f"ring R={char},({','.join(str(v) for v in variables)}),wp({','.join(map(str, weights))});"
    else:
        header = (
            f"ring R=({char},Y),({','.join(str(v) for v in variables)}),"
            f"wp({','.join(map(str, weights))});\n"
            f"minpoly={singular_expr(sp.Poly(minpoly, y).monic().as_expr(), y)};"
        )
    basis = "std(I)" if algorithm == "std" else "modStd(I,1)"
    lines = [header, "option(redSB);"]
    if algorithm == "modstd":
        lines.append('LIB "modstd.lib";')
    lines += [
        "ideal I=" + ",\n".join(singular_expr(g, y if minpoly is not None else None) for g in gens) + ";",
        f"ideal G={basis};",
        f'printf("DIMTEST t={t} {tag} char={char} algorithm={algorithm} DIM=%s SIZE=%s", dim(G), size(G));',
        'printf("LEAD=%s", lead(G));',
        "quit;",
    ]
    path = OUT / f"dimtest_t{t}_{tag}_{algorithm}.sing"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def t2_cone_job(branch: int, root: sp.Rational) -> pathlib.Path:
    t = 2
    rec = load_record(t)
    ns = ns_for_t(t, include_z=True)
    y = ns["q5_1"]
    z, b4, b3 = ns["z"], ns["b4"], ns["b3"]
    rows = {int(item["band"]): sp.expand(sp.sympify(item["expr"], locals=ns).subs(y, root))
            for item in rec["terminal"]}
    c = sp.expand(sp.sympify(rec["normalizer"]["c"], locals=ns).subs(y, root))
    tau = sp.expand(rows[0] - c)
    pos = [clear_primitive(rows[band], [b4, b3]) for band in range(1, 2*t)]
    pos = [p for p in pos if p is not None]
    tau_prim = clear_primitive(tau, [b4, b3])
    full = [clear_primitive(rows[band], [b4, b3]) for band in range(0, 2*t)]
    full = [p for p in full if p is not None]
    lines = [
        "ring R=0,(z,b4,b3),dp;",
        "ideal Ipos=" + ",".join(singular_expr(g) for g in pos) + ";",
        "ideal Rab=Ipos,1-z*(" + singular_expr(tau_prim) + ");",
        "ideal GR=std(Rab);",
        f'printf("T2_CONE branch={branch} y={root} RABINOWITSCH_tau_in_radical=%s", (size(GR)==1 && GR[1]==1));',
        "ideal Ifull=" + ",".join(singular_expr(g) for g in full) + ";",
        "ideal GF=std(Ifull);",
        f'printf("T2_CONE branch={branch} y={root} UNIT_IDEAL_8_1=%s", (size(GF)==1 && GF[1]==1));',
        "quit;",
    ]
    path = OUT / f"t2_cone_branch{branch}.sing"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_t2_tau_summary() -> None:
    t = 2
    rec = load_record(t)
    ns = ns_for_t(t)
    y, b4, b3 = ns["q5_1"], ns["b4"], ns["b3"]
    row0 = sp.sympify(rec["terminal"][0]["expr"], locals=ns)
    c = sp.sympify(rec["normalizer"]["c"], locals=ns)
    tau = sp.expand(row0 - c)
    alpha_band = sp.sympify(rec["terminal"][3]["expr"], locals=ns).subs(b4, 0)
    summary = {
        "tau": str(sp.factor(tau)),
        "tau_at_b4_0": str(sp.factor(tau.subs(b4, 0))),
        "band3_at_b4_0": str(sp.factor(alpha_band)),
        "band3_at_b4_0_y_1_5": str(sp.factor(alpha_band.subs(y, sp.Rational(1, 5)))),
        "band3_at_b4_0_y_2_5": str(sp.factor(alpha_band.subs(y, sp.Rational(2, 5)))),
    }
    (OUT / "t2_tau_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    jobs: list[dict[str, object]] = []
    write_t2_tau_summary()
    y2 = ns_for_t(2)["q5_1"]
    for branch, root in enumerate(split_roots(2)):
        jobs.append({"path": str(dim_job(2, f"branch{branch}", 0, None, {y2: root})),
                     "timeout_seconds": 120, "purpose": f"t=2 branch {branch} positive cone dim"})
        jobs.append({"path": str(t2_cone_job(branch, root)),
                     "timeout_seconds": 120, "purpose": f"t=2 branch {branch} tau and full unit"})
    for t in (3, 4, 5):
        ns = ns_for_t(t)
        y = ns[f"q{2*t+1}_1"]
        H = h_poly(t, y)
        timeout = 300 if t < 5 else 1200
        jobs.append({"path": str(dim_job(t, "field", 0, H, {}, "std")),
                     "timeout_seconds": timeout, "purpose": f"t={t} exact homogeneous dim std"})
    # Optional exact modular algorithm over characteristic zero for t=5.
    ns5 = ns_for_t(5)
    y5 = ns5["q11_1"]
    jobs.append({"path": str(dim_job(5, "field", 0, h_poly(5, y5), {}, "modstd")),
                 "timeout_seconds": 1200, "purpose": "t=5 exact homogeneous dim modStd"})
    # Modular control only; never a characteristic-zero promotion.
    jobs.append({"path": str(dim_job(5, "field_p1009", 1009, h_poly(5, y5), {}, "std")),
                 "timeout_seconds": 300, "purpose": "t=5 modular homogeneous dim control"})
    (OUT / "singular_jobs.json").write_text(
        json.dumps({"jobs": jobs}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for job in jobs:
        print(job["path"])


if __name__ == "__main__":
    main()
