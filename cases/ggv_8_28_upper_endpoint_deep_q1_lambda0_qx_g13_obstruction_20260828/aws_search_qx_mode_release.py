#!/usr/bin/env python3
"""AWS-only bounded exact search for a scalar-mode repair of the Q=X q-tail."""

from __future__ import annotations

from fractions import Fraction as Q
import importlib.util
import itertools
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
Q15 = HERE / "verify_lambda0_q15.py"
EVEN = HERE / "verify_even_subbranch_reduction.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rref(matrix):
    rows = [list(row) for row in matrix]
    if not rows:
        return rows, []
    row = 0
    pivots = []
    for column in range(len(rows[0])):
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


def nullspace(matrix):
    reduced, pivots = rref(matrix)
    columns = len(matrix[0]) if matrix else 0
    free = [column for column in range(columns) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [Q(0)] * columns
        vector[free_column] = Q(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def main():
    assert platform.system() == "Linux"
    assert "Amazon" in Path("/sys/class/dmi/id/sys_vendor").read_text()
    run_tag = os.environ.get("AWS_RUN_TAG", "")
    assert run_tag == "ggv-lambda0-qx-mode-release-grid-20260828"
    qm = load("q15_frozen", Q15)
    up = load("even_frozen", EVEN)
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
    q_columns = []
    for name, degrees in specs:
        for degree in degrees:
            raw = {raw_name: [] for raw_name, _ in raw_specs}
            primitives = [[] for _ in primitive_specs]
            if name.startswith("d"):
                primitives[[item[0] for item in primitive_specs].index(name)] = qm.monomial(degree)
            else:
                raw[name] = qm.monomial(degree)
            gates = qm.h7_to_h15(A, q, [], [], **raw)
            q_columns.append(qm.concatenate([
                qm.add(gate, qm.scale(-1, qm.t5(A, primitive)))
                for gate, primitive in zip(gates, primitives)
            ]))
    q_matrix = [[column[row] for column in q_columns] for row in range(50)]
    q_basis = nullspace(q_matrix)
    assert len(q_basis) == 5
    raw_index = {name: index for index, name in enumerate(names)}

    def raw_poly(vector, name, degrees):
        out = []
        for degree in degrees:
            value = vector[raw_index[f"{name}_{degree}"]]
            if value:
                if len(out) <= degree:
                    out.extend([Q(0)] * (degree + 1 - len(out)))
                out[degree] = value
        return up.trim(out)

    def trajectory(vector, shift, a_power, exponent, maximum=19):
        normalized = [{} for _ in range(maximum + 1)]
        normalized[0] = up.la(A, [Q(1)])
        normalized[2] = up.la(A, up.scale(Q(-1, 8), q), -1)
        normalized[4] = up.la(A, up.scale(Q(1, 256), up.mul(q, q)), -2)
        normalized[7] = up.la(A, raw_poly(vector, "f", range(6)), -3)
        normalized[9] = up.la(A, raw_poly(vector, "f9", range(1, 8)), -4)
        normalized[11] = up.la(A, raw_poly(vector, "f11", range(1, 6)), -4)
        normalized[13] = up.la(A, raw_poly(vector, "f13", range(2, 4)), -4)
        out = [{} for _ in range(maximum + 1)]
        powered = up.la_series_power_one(A, normalized, exponent, maximum - shift)
        prefactor = up.la(A, [Q(1)], a_power)
        for degree, value in enumerate(powered):
            out[degree + shift] = up.la_mul(A, prefactor, value)
        return out

    # Complete odd characteristic is affine-linear in the scalar modes.
    specs_by_name = {
        "base": (0, 6, Q(3, 2)),
        "c2": (2, 5, Q(5, 4)),
        "c4": (4, 4, Q(1)),
        "c6": (6, 3, Q(3, 4)),
        "c8": (8, 2, Q(1, 2)),
        "c10": (10, 1, Q(1, 4)),
    }
    components = {
        name: [trajectory(vector, *spec) for vector in q_basis]
        for name, spec in specs_by_name.items()
    }

    def survivor(mode_values):
        characteristic = []
        for basis_index in range(5):
            series = [{} for _ in range(20)]
            for name, scalar in (("base", Q(1)), ("c2", Q(1)), *mode_values.items()):
                if not scalar:
                    continue
                for weight in range(20):
                    series[weight] = up.la_add(
                        A, series[weight],
                        up.la_scale(A, scalar, components[name][basis_index][weight]),
                    )
            characteristic.append(series)
        equations = []
        receiver_count = 0
        for weight in range(9, 20, 2):
            denominator_power = max(
                [0] + [-min(series[weight])
                       for series in characteristic if series[weight]]
            )
            numerators = []
            maximum_degree = 0
            for series in characteristic:
                numerator = []
                for a_exponent, coefficient in series[weight].items():
                    numerator = up.add(
                        numerator,
                        up.mul(up.power(A, a_exponent + denominator_power), coefficient),
                    )
                numerators.append(numerator)
                maximum_degree = max(maximum_degree, len(numerator) - 1)
            receivers = [
                up.scale(-1, up.mul(up.power(A, denominator_power), qm.monomial(degree)))
                for degree in up.g_window(weight)
            ]
            maximum_degree = max(
                [maximum_degree] + [len(poly) - 1 for poly in receivers]
            )
            for row in equations:
                row.extend([Q(0)] * len(receivers))
            for degree in range(maximum_degree + 1):
                equations.append(
                    [poly[degree] if degree < len(poly) else Q(0)
                     for poly in numerators]
                    + [Q(0)] * receiver_count
                    + [poly[degree] if degree < len(poly) else Q(0)
                       for poly in receivers]
                )
            receiver_count += len(receivers)
        complete_basis = nullspace(equations)
        raw_projections = [vector[:5] for vector in complete_basis if any(vector[:5])]
        raw_rank = len(rref(raw_projections)[1]) if raw_projections else 0
        return raw_rank, raw_projections

    values = tuple(range(-3, 4))
    counts = {}
    hits = []
    # c4 is omitted from the grid because t^4 F lands inside every relevant
    # shifted raw window; the checker separately confirms c4=0 and c4=1 give
    # the same survivor dimension at every recorded hit.
    for c6, c8, c10 in itertools.product(values, repeat=3):
        dimension, basis = survivor({
            "c4": Q(0), "c6": Q(c6), "c8": Q(c8), "c10": Q(c10),
        })
        counts[dimension] = counts.get(dimension, 0) + 1
        if dimension:
            comparison, _ = survivor({
                "c4": Q(1), "c6": Q(c6), "c8": Q(c8), "c10": Q(c10),
            })
            assert comparison == dimension
            hits.append({
                "c6": c6, "c8": c8, "c10": c10,
                "dimension": dimension,
                "basis": [[str(value) for value in vector] for vector in basis],
            })
    print(json.dumps({
        "run_tag": run_tag,
        "q_survivor_dimension": 5,
        "grid": list(values),
        "grid_variables": ["c6", "c8", "c10"],
        "dimension_counts": {str(key): value for key, value in sorted(counts.items())},
        "hits": hits,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
