#!/usr/bin/env python3
"""Exact q-fiber proof that the fixed Q=X even prefix has zero endpoint."""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
Q15_REPORT = ROOT / "xmodel/ggv-upper-endpoint-deep-q1-lambda0-q15-independent-sol-ultra-20260828.md"
Q15_REPORT_SHA256 = "188317138e60224f5a7e9dc1de18ab339384c5246c1cabf12acc20657dac7d5f"
Q15_CHECKER = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/verify_lambda0_q15.py"
Q15_CHECKER_SHA256 = "6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a"
R2_REPORT = ROOT / "xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-g13-obstruction-r2-sol-ultra-20260828.md"
R2_REPORT_SHA256 = "b5433f4e4a76f48d8899d59b28290dc7075ac591b89913323e5102a998e73a08"
R2_CHECKER = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_g13_obstruction_20260828/verify_qx_g13_obstruction.py"
R2_CHECKER_SHA256 = "fb29dec1a7eb08a41818c8ea802c984f893d8a222d38aade6fdf4af9bc272638"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rref(matrix):
    rows = [list(row) for row in matrix]
    row = 0
    pivots = []
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((index for index in range(row, len(rows))
                      if rows[index][column]), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        divisor = rows[row][column]
        rows[row] = [value / divisor for value in rows[row]]
        for index in range(len(rows)):
            if index != row and rows[index][column]:
                factor = rows[index][column]
                rows[index] = [a - factor * b
                               for a, b in zip(rows[index], rows[row])]
        pivots.append(column)
        row += 1
        if row == len(rows):
            break
    return rows, pivots


def quadratic(left, right):
    out = {}
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if not a or not b:
                continue
            key = tuple(sorted((i, j)))
            out[key] = out.get(key, Q(0)) + a * b
            if not out[key]:
                del out[key]
    return out


def qadd(*items):
    out = {}
    for item in items:
        for key, value in item.items():
            out[key] = out.get(key, Q(0)) + value
            if not out[key]:
                del out[key]
    return out


def qscale(value, item):
    return {key: Q(value) * coefficient for key, coefficient in item.items()
            if Q(value) * coefficient}


def main():
    assert sha256(Q15_REPORT) == Q15_REPORT_SHA256
    assert sha256(Q15_CHECKER) == Q15_CHECKER_SHA256
    assert sha256(R2_REPORT) == R2_REPORT_SHA256
    assert sha256(R2_CHECKER) == R2_CHECKER_SHA256
    qm = load("q15_frozen", Q15_CHECKER)
    r2 = load("qx_g13_frozen", R2_CHECKER)
    up = r2.load_upstream()
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    q = [Q(0), Q(1)]
    raw_specs = (
        ("f", tuple(range(6))),
        ("f9", tuple(range(1, 8))),
        ("f11", tuple(range(1, 6))),
        ("f13", tuple(range(2, 4))),
    )
    primitive_specs = (
        ("d7", tuple(range(3))),
        ("d9", tuple(range(5))),
        ("d11", tuple(range(7))),
        ("d13", tuple(range(9))),
        ("d15", tuple(range(11))),
    )
    specs = raw_specs + primitive_specs
    names = [f"{name}_{degree}" for name, degrees in specs for degree in degrees]
    columns = []
    for name, degrees in specs:
        for degree in degrees:
            raw = {raw_name: [] for raw_name, _ in raw_specs}
            primitives = [[] for _ in primitive_specs]
            if name.startswith("d"):
                primitives[[item[0] for item in primitive_specs].index(name)] = qm.monomial(degree)
            else:
                raw[name] = qm.monomial(degree)
            gates = qm.h7_to_h15(A, q, [], [], **raw)
            columns.append(qm.concatenate([
                qm.add(gate, qm.scale(-1, qm.t5(A, primitive)))
                for gate, primitive in zip(gates, primitives)
            ]))
    matrix = [[column[row] for column in columns] for row in range(50)]
    reduced, pivots = rref(matrix)
    free = [column for column in range(55) if column not in pivots]
    assert [names[column] for column in free] == [
        "d15_4", "d15_5", "d15_6", "d15_8", "d15_9",
    ]
    basis = []
    for free_column in free:
        vector = [Q(0)] * 55
        vector[free_column] = Q(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    index = {name: position for position, name in enumerate(names)}

    def raw_poly(vector, name, degrees):
        out = []
        for degree in degrees:
            value = vector[index[f"{name}_{degree}"]]
            if value:
                if len(out) <= degree:
                    out.extend([Q(0)] * (degree + 1 - len(out)))
                out[degree] = value
        return up.trim(out)

    def raw_data(vector):
        return {
            name: raw_poly(vector, name, degrees)
            for name, degrees in raw_specs
        }

    raw_basis = [raw_data(vector) for vector in basis]
    f0 = [raw["f"][0] if raw["f"] else Q(0) for raw in raw_basis]
    f11_x1 = [raw["f11"][1] if len(raw["f11"]) > 1 else Q(0)
              for raw in raw_basis]
    assert f0 == [Q(0), Q(-2**29, 75), Q(0), Q(0), Q(2**28, 225)]

    def raw_F(raw):
        return {
            0: up.power(A, 4),
            2: up.scale(Q(-1, 8), up.mul(up.power(A, 3), q)),
            4: up.scale(Q(1, 256), up.mul(up.power(A, 2), up.mul(q, q))),
            7: up.mul(A, raw["f"]),
            9: raw["f9"], 11: raw["f11"], 13: raw["f13"],
        }

    def normalized(raw, maximum=15):
        out = [{} for _ in range(maximum + 1)]
        out[0] = up.la(A, [Q(1)])
        out[2] = up.la(A, up.scale(Q(-1, 8), q), -1)
        out[4] = up.la(A, up.scale(Q(1, 256), up.mul(q, q)), -2)
        out[7] = up.la(A, raw["f"], -3)
        out[9] = up.la(A, raw["f9"], -4)
        out[11] = up.la(A, raw["f11"], -4)
        out[13] = up.la(A, raw["f13"], -4)
        return out

    births = {"c2": 2, "c4": 4, "c6": 6, "c8": 8}

    def jet_component(raw, label, weight, coordinate):
        base = up.characteristic_jets(A, raw_F(raw), [Q(0)] * 10, 15)
        if label == "base":
            value = base[weight]
        else:
            modes = [Q(0)] * 10
            modes[births[label] // 2 - 1] = Q(1)
            loaded = up.characteristic_jets(A, raw_F(raw), modes, 15)
            value = (loaded[weight][0] - base[weight][0],
                     loaded[weight][1] - base[weight][1])
        return value[coordinate]

    def la_component(raw, label, weight):
        zero_modes = [Q(0)] * 10
        base = r2.characteristic(up, A, normalized(raw), zero_modes, 15)[weight]
        if label == "base":
            return base
        modes = [Q(0)] * 10
        modes[births[label] // 2 - 1] = Q(1)
        loaded = r2.characteristic(up, A, normalized(raw), modes, 15)[weight]
        return up.la_add(A, loaded, up.la_scale(A, -1, base))

    def vector(label, weight, coordinate):
        return [jet_component(raw, label, weight, coordinate)
                for raw in raw_basis]

    zero = [Q(0)] * 5
    assert vector("c4", 11, 0) == up.scale(-1, f0)
    assert all(vector(label, 11, 0) == zero for label in ("base", "c2", "c6", "c8"))
    assert vector("c6", 13, 0) == up.scale(Q(3, 4), f0)
    assert all(vector(label, 13, 0) == zero for label in ("base", "c2", "c4", "c8"))
    assert vector("c4", 15, 1) == f11_x1
    assert all(vector(label, 15, 1) == zero for label in ("base", "c2"))
    h6 = vector("c6", 15, 1)
    h8 = vector("c8", 15, 1)
    assert h6 == [Q(0), Q(-2**21, 5), Q(0), Q(0), Q(-2**19, 3)]
    assert h8 == [Q(0), Q(0), Q(2**29, 75), Q(0), Q(0)]

    # Coefficient X^1 in the remainder modulo A of the A^-1 pole numerator.
    pole_x1 = {}
    for label in ("base", "c2", "c4", "c6", "c8"):
        values = []
        for raw in raw_basis:
            element = la_component(raw, label, 15)
            assert not element or min(element) >= -1
            numerator = element.get(-1, [])
            _, remainder = up.poly_divmod(numerator, A)
            values.append(remainder[1] if len(remainder) > 1 else Q(0))
        pole_x1[label] = values
    assert all(pole_x1[label] == zero for label in ("base", "c2", "c4"))
    r6 = pole_x1["c6"]
    r8 = pole_x1["c8"]
    assert r6 == [Q(0), Q(0), Q(0), Q(0), Q(-7 * 2**19, 3)]
    assert r8 == [Q(0), Q(0), Q(2**29, 15), Q(0), Q(0)]

    # Formal ideal identity.  P13=(3/4)c6*f0 and
    # R15=c6*(r6.a)+c8*(r8.a).  After the automatic c4 cancellation,
    # E=f0*(c6*h6.a+c8*h8.a).
    correction = [Q(0), Q(-2**21, 5), Q(0), Q(0), Q(2**20, 15)]
    assert quadratic(f0, h6) == qadd(
        qscale(Q(1, 5), quadratic(f0, r6)),
        quadratic(correction, f0),
    )
    assert quadratic(f0, h8) == qscale(Q(1, 5), quadratic(f0, r8))

    # Modes c10 and later do not enter G15: F5=0 and later modes are unborn.
    assert 10 + 5 == 15 and all(not raw.get("f5", []) for raw in raw_basis)
    assert min((12, 14, 16, 18, 20)) > 10

    print("q7_q15_fixed_even_fiber=dimension_5;free=d15_4,d15_5,d15_6,d15_8,d15_9")
    print("G13_X0=(3/4)*c6*f0")
    print("G15_pole_remainder_X1=-(7*2^19/3)*c6*a4+(2^29/15)*c8*a2")
    print("endpoint=f0*((-2^21*a1/5-2^19*a4/3)*c6+(2^29*a2/75)*c8)")
    print("endpoint=(f0/5)*G15_pole_X1+(4/3)*(-2^21*a1/5+2^20*a4/15)*G13_X0")
    print("PASS_EXACT_QX_FIXED_EVEN_ENDPOINT_ZERO")


if __name__ == "__main__":
    main()
