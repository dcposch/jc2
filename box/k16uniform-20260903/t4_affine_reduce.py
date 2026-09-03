#!/usr/bin/env python3
"""Exact affine reduction of the normalized t=4 quadratic-field system.

The arithmetic and pivot routine are imported verbatim from the frozen,
charged t3_normalized_slice.py.  That routine accepts a pivot only after its
coefficient is proved invertible modulo H and its substitution kills the
pivot row modulo H.  It also canonicalizes all remaining rows after every
step and removes only zero or literal-duplicate canonical representatives.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
INPUT = pathlib.Path("/tmp/jc2-lane.fjoTgL/inputs")
ROWS = HERE / "t4_normalized_rows.tsv"
OUT = HERE / "t4_affine_audit.json"
EXPECTED = {
    "t3_normalized_slice.py": "9e394dae1920e90413ff1aa6d0f5f8eb4dd9aa343a5826e0f4f8c586bd980ac7",
    "triangular_preprocess.py": "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
}
EXPECTED_ROWS_SHA256 = "eca6c7e0026703c7f17e22b750e7eb51cbd867a7d19b4b900c104db161202020"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class K4:
    """Adapter implementing the frozen pivot routine's quadratic-field API."""

    def __init__(self, y, auxiliary):
        self.y = y
        self.auxiliary = list(auxiliary)
        self.H = 486*y**2 - 270*y + 35
        self.domain = sp.QQ[tuple(self.auxiliary)]
        self.hpoly = sp.Poly(self.H, y, domain=self.domain)

    def reduce(self, expr):
        poly = sp.Poly(sp.expand(expr), self.y, domain=self.domain)
        return sp.expand(poly.rem(self.hpoly).as_expr())

    def inverse(self, coefficient):
        coefficient = self.reduce(coefficient)
        if coefficient.free_symbols - {self.y} or coefficient == 0:
            raise ZeroDivisionError("putative K coefficient is not a nonzero scalar")
        inverse = sp.invert(sp.Poly(coefficient, self.y, domain=sp.QQ),
                           sp.Poly(self.H, self.y, domain=sp.QQ)).as_expr()
        inverse = self.reduce(inverse)
        if self.reduce(coefficient*inverse - 1) != 0:
            raise AssertionError("inverse identity fails modulo H4")
        return inverse


def main():
    for name, expected in EXPECTED.items():
        if digest(INPUT/name) != expected:
            raise RuntimeError("frozen hash mismatch: " + name)
    if digest(ROWS) != EXPECTED_ROWS_SHA256:
        raise RuntimeError("normalized row artifact hash mismatch; rerun the exact normalizer")

    # The frozen t=3 helper imports this module by its literal name.
    tp = load(INPUT/"triangular_preprocess.py", "triangular_preprocess")
    helper = load(INPUT/"t3_normalized_slice.py", "t4_frozen_k_helper")
    norm = json.loads((HERE/"t4_normalization_audit.json").read_text())
    names = norm["normalized"]["remaining_variables"]
    symbols = {name: sp.Symbol(name) for name in names + ["q9_1"]}
    y = symbols["q9_1"]
    auxiliary = [symbols[name] for name in names]
    rows = []
    with ROWS.open(encoding="utf-8") as f:
        for item in csv.DictReader(f, delimiter="\t"):
            rows.append(helper.SliceRow(
                int(item["source_index"]), int(item["h_power"]),
                (int(item["gamma_power"]), int(item["pi_power"])),
                sp.sympify(item["expression"], locals=symbols)))
    if len(rows) != 38 or len(auxiliary) != 26:
        raise RuntimeError("unexpected normalized dimensions")

    K = K4(y, auxiliary)
    result = helper.eliminate_over_k(
        rows, auxiliary, K, max_seconds=1100.0, max_bytes=100_000_000)
    residual, remaining, pivots, dropped, unit, elapsed = result
    if len(pivots) != 22 or len(residual) != 8 or len(remaining) != 4:
        raise AssertionError("unexpected final affine dimensions")

    record = {
        "typing": "EXACT SEQUENTIAL QUOTIENT-RING ISOMORPHISMS OVER K4",
        "H4": str(K.H),
        "normalized_rows_sha256": digest(ROWS),
        "frozen_source_hashes": EXPECTED,
        "elapsed": elapsed,
        "inverse_identity_checked_mod_H_at_every_pivot": True,
        "pivot_substitution_checked_mod_H_at_every_pivot": True,
        "pivots": [{
            "step": p.step, "source": p.source_index, "band": p.h_power,
            "monomial": list(p.monomial), "variable": str(p.variable),
            "coefficient": str(p.coefficient), "inverse": str(p.inverse),
            "rhs": str(p.step_rhs), "rows_after": p.remaining_rows_after,
            "bytes_after": p.expression_bytes_after,
        } for p in pivots],
        "dropped": dropped,
        "unit": unit,
        "vars": list(map(str, remaining)),
        "residual": [{
            "source": r.source_index, "band": r.h_power,
            "monomial": list(r.monomial), "expr": str(r.expr),
            "degree": sp.Poly(r.expr, *remaining,
                              domain=sp.QQ.frac_field(y)).total_degree(),
        } for r in residual],
    }
    OUT.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                   encoding="utf-8")
    print(json.dumps({
        "audit": str(OUT), "audit_sha256": digest(OUT),
        "pivots": len(pivots), "rows": len(residual),
        "variables": list(map(str, remaining)),
        "bands": [r.h_power for r in residual],
        "degrees": [item["degree"] for item in record["residual"]],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
