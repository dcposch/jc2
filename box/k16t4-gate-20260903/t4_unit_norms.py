#!/usr/bin/env python3
"""Record resultants/norms for the t=4 quadratic-algebra unit pivots."""

from __future__ import annotations

import hashlib
import json
import pathlib

import sympy as sp


OUT = pathlib.Path("/home/ubuntu/jc2/box/k16t4-gate-20260903")


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    y = sp.Symbol("q9_1")
    H = 486*y**2 - 270*y + 35
    hpoly = sp.Poly(H, y, domain=sp.QQ)
    leading = hpoly.LC()
    audit = json.loads((OUT / "t4_affine_audit.json").read_text(encoding="utf-8"))
    norm_audit = json.loads((OUT / "t4_normalization_audit.json").read_text(encoding="utf-8"))

    def reduce_mod(expr: sp.Expr) -> sp.Expr:
        return sp.expand(sp.Poly(sp.expand(expr), y, domain=sp.QQ).rem(hpoly).as_expr())

    def record(label: str, expr_text: str, inverse_text: str | None = None) -> dict:
        expr = sp.sympify(expr_text, locals={str(y): y})
        if expr.free_symbols - {y}:
            raise AssertionError((label, expr.free_symbols))
        degree = sp.Poly(expr, y, domain=sp.QQ).degree()
        resultant = sp.factor(sp.resultant(H, expr, y))
        determinant_norm = sp.factor(resultant / (leading ** degree))
        item = {
            "label": label,
            "element": str(expr),
            "degree_y": degree,
            "resultant_with_H4": str(resultant),
            "determinant_norm": str(determinant_norm),
            "nonzero": resultant != 0,
        }
        if inverse_text is not None:
            inverse = sp.sympify(inverse_text, locals={str(y): y})
            item["inverse"] = str(inverse)
            item["inverse_identity_mod_H4"] = reduce_mod(expr*inverse - 1) == 0
            if not item["inverse_identity_mod_H4"]:
                raise AssertionError(label)
        if resultant == 0:
            raise AssertionError(label)
        return item

    pivots = [
        record(f"pivot_{pivot['step']:02d}_{pivot['variable']}",
               pivot["coefficient"], pivot["inverse"])
        for pivot in audit["pivots"]
    ]
    cbar = norm_audit["c_row"]["slice_image"]
    c_units = [
        record("q9_1", "q9_1", norm_audit["unit_checks"]["v_inverse"]),
        record("130_minus_1404_q9_1", "130-1404*q9_1",
               norm_audit["unit_checks"]["130_minus_1404v_inverse"]),
        record("cbar", cbar, norm_audit["unit_checks"]["cbar_inverse"]),
    ]
    output = {
        "typing": "EXACT-RESULTANT-AND-INVERSE-UNIT-AUDIT",
        "H4": str(H),
        "H4_leading_coefficient": str(leading),
        "affine_audit_sha256": sha256(OUT / "t4_affine_audit.json"),
        "normalization_audit_sha256": sha256(OUT / "t4_normalization_audit.json"),
        "all_affine_pivot_resultants_nonzero": all(item["nonzero"] for item in pivots),
        "all_affine_inverse_identities_checked": all(
            item["inverse_identity_mod_H4"] for item in pivots
        ),
        "c_unit_resultants_nonzero": all(item["nonzero"] for item in c_units),
        "c_unit_inverse_identities_checked": all(
            item["inverse_identity_mod_H4"] for item in c_units
        ),
        "c_units": c_units,
        "affine_pivots": pivots,
    }
    path = OUT / "t4_unit_norms.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "audit": path.name,
        "sha256": sha256(path),
        "affine_pivots": len(pivots),
        "all_affine_resultants_nonzero": output["all_affine_pivot_resultants_nonzero"],
        "all_affine_inverses_checked": output["all_affine_inverse_identities_checked"],
        "c_units": len(c_units),
        "c_unit_resultants_nonzero": output["c_unit_resultants_nonzero"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
