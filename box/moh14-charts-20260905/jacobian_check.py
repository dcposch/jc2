#!/usr/bin/env python3
"""Re-evaluate J(P,Q) for a specialized descended pair.

Reads class meta (inventories + gauges) and a dict of parameter values,
builds P,Q in Q[x,y] or F_p[x,y] via sympy, and checks whether
J(P,Q) equals c * x^ell exactly.  A PASS is a genuine monomial-Jacobian
receiver point (not a Keller pair unless it lifts).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load_meta(class_id: str, stem: str) -> dict:
    return json.loads((HERE / "classes" / class_id / "meta" / (stem + ".json")).read_text())


def build_PQ(meta: dict, values: dict, p: int = 0):
    x, y = sp.symbols("x y")
    C = meta["meta"]["closed_form"]
    K, e, q = int(C["K"]), int(C["e"]), int(C["q"])
    ell = int(meta["meta"]["row"]["k"])

    def val(name, default=0):
        v = values.get(name, default)
        return sp.Integer(v)

    h = y ** K
    for a, b in meta["meta"]["h_inventory"]:
        h = h + val("h_%d_%d" % (a, b)) * x ** a * y ** b
    h = sp.expand(h)
    P = h ** e
    for i in range(1, e + 1):
        expr = 0
        for a, b in meta["meta"]["alpha_inventories"][str(i)]:
            expr = expr + val("A%d_%d_%d" % (i, a, b)) * x ** a * y ** b
        P = P + sp.expand(expr) * h ** (e - i)
    Q = h ** q
    for i in range(2, q + 1):
        expr = 0
        for a, b in meta["meta"]["beta_inventories"].get(str(i), []):
            expr = expr + val("B%d_%d_%d" % (i, a, b)) * x ** a * y ** b
        Q = Q + sp.expand(expr) * h ** (q - i)
    P, Q = sp.expand(P), sp.expand(Q)
    J = sp.expand(sp.diff(P, x) * sp.diff(Q, y) - sp.diff(P, y) * sp.diff(Q, x))
    c = val("c")
    target = sp.expand(c * x ** ell)
    residual = sp.expand(J - target)
    if p:
        residual = sp.Poly(residual, x, y, modulus=p).as_expr()
        J = sp.Poly(J, x, y, modulus=p).as_expr()
    return dict(
        K=K, e=e, q=q, ell=ell, c=str(c),
        J=str(J)[:300], target=str(target),
        residual_zero=(residual == 0),
        residual_head=str(residual)[:300],
        P_head=str(P)[:200], Q_head=str(Q)[:200],
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--class-id", required=True)
    ap.add_argument("--stem", required=True)
    ap.add_argument("--point-json", required=True)
    ap.add_argument("--char", type=int, default=0)
    a = ap.parse_args()
    meta = load_meta(a.class_id, a.stem)
    values = json.loads(Path(a.point_json).read_text())
    rec = build_PQ(meta, values, a.char)
    print(json.dumps(rec, indent=2))
    return 0 if rec["residual_zero"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
