#!/usr/bin/env python3
"""AWS-only exact fixed-quadratic-Q probe through the odd G15 receiver."""

from __future__ import annotations

from fractions import Fraction as QF
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


def nullspace(matrix):
    reduced, pivots = rref(matrix)
    columns = len(matrix[0]) if matrix else 0
    free = [column for column in range(columns) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [QF(0)] * columns
        vector[free_column] = QF(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def independent_span(vectors):
    if not vectors:
        return []
    reduced, _ = rref(vectors)
    return [row for row in reduced if any(row)]


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), QF(0))


def main():
    assert platform.system() == "Linux"
    assert "Amazon" in Path("/sys/class/dmi/id/sys_vendor").read_text()
    run_tag = os.environ.get("AWS_RUN_TAG", "")
    assert (
        run_tag == "ggv-lambda0-quadratic-q-g15-grid-r1-20260828"
        or run_tag == "ggv-lambda0-quadratic-q-g15-q1-fast-20260828"
        or run_tag.startswith("ggv-lambda0-quadratic-q-g15-fast-20260828-")
    )
    qm = load("q15_frozen", Q15)
    up = load("even_frozen", EVEN)
    A = [QF(-1), QF(0), QF(0), QF(0), QF(1)]
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
    raw_index = {name: index for index, name in enumerate(names)}

    def q_basis(q):
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
        basis = []
        for free_column in free:
            vector = [QF(0)] * 55
            vector[free_column] = QF(1)
            for row, pivot in enumerate(pivots):
                vector[pivot] = -reduced[row][free_column]
            basis.append(vector)
        return basis, [names[column] for column in free], len(pivots)

    def raw_poly(vector, name, degrees):
        out = []
        for degree in degrees:
            value = vector[raw_index[f"{name}_{degree}"]]
            if value:
                if len(out) <= degree:
                    out.extend([QF(0)] * (degree + 1 - len(out)))
                out[degree] = value
        return up.trim(out)

    def raw_data(vector):
        return {name: raw_poly(vector, name, degrees)
                for name, degrees in raw_specs}

    def trajectory(raw, q, shift, a_power, exponent, maximum=15):
        normalized = [{} for _ in range(maximum + 1)]
        normalized[0] = up.la(A, [QF(1)])
        normalized[2] = up.la(A, up.scale(QF(-1, 8), q), -1)
        normalized[4] = up.la(A, up.scale(QF(1, 256), up.mul(q, q)), -2)
        normalized[7] = up.la(A, raw["f"], -3)
        normalized[9] = up.la(A, raw["f9"], -4)
        normalized[11] = up.la(A, raw["f11"], -4)
        normalized[13] = up.la(A, raw["f13"], -4)
        out = [{} for _ in range(maximum + 1)]
        powered = up.la_series_power_one(A, normalized, exponent, maximum - shift)
        prefactor = up.la(A, [QF(1)], a_power)
        for degree, value in enumerate(powered):
            out[degree + shift] = up.la_mul(A, prefactor, value)
        return out

    trajectory_specs = {
        "base": (0, 6, QF(3, 2)),
        "c2": (2, 5, QF(5, 4)),
        "c4": (4, 4, QF(1)),
        "c6": (6, 3, QF(3, 4)),
        "c8": (8, 2, QF(1, 2)),
    }

    context_cache = {}

    def context(q):
        key = tuple(q)
        if key in context_cache:
            return context_cache[key]
        basis, free, rank = q_basis(q)
        assert rank + len(basis) == 55
        raws = [raw_data(vector) for vector in basis]
        components = {
            name: [trajectory(raw, q, *spec) for raw in raws]
            for name, spec in trajectory_specs.items()
        }
        value = basis, free, rank, raws, components
        context_cache[key] = value
        return value

    def analyze(q, modes):
        basis, free, rank, raws, components = context(q)
        characteristic = []
        fiber_dimension = len(basis)
        for basis_index in range(fiber_dimension):
            series = [{} for _ in range(16)]
            for name, scalar in (
                ("base", QF(1)), ("c2", QF(1)),
                ("c4", QF(modes[0])), ("c6", QF(modes[1])),
                ("c8", QF(modes[2])),
            ):
                if scalar:
                    for weight in range(16):
                        series[weight] = up.la_add(
                            A, series[weight],
                            up.la_scale(A, scalar, components[name][basis_index][weight]),
                        )
            characteristic.append(series)
        equations = []
        receiver_count = 0
        for weight in range(9, 16, 2):
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
                row.extend([QF(0)] * len(receivers))
            for degree in range(maximum_degree + 1):
                equations.append(
                    [poly[degree] if degree < len(poly) else QF(0)
                     for poly in numerators]
                    + [QF(0)] * receiver_count
                    + [poly[degree] if degree < len(poly) else QF(0)
                       for poly in receivers]
                )
            receiver_count += len(receivers)
        complete = nullspace(equations)
        survivor = independent_span([
            vector[:fiber_dimension] for vector in complete
            if any(vector[:fiber_dimension])
        ])

        # Exact origin linear forms on the five q-fiber coordinates.
        f7_x0 = []
        f11_x1 = []
        g11_x0 = []
        g15_x1 = []
        mode_vector = [QF(1), QF(modes[0]), QF(modes[1]), QF(modes[2])] + [QF(0)] * 6
        for raw in raws:
            raw_F = {
                0: up.power(A, 4),
                2: up.scale(QF(-1, 8), up.mul(up.power(A, 3), q)),
                4: up.scale(QF(1, 256), up.mul(up.power(A, 2), up.mul(q, q))),
                7: up.mul(A, raw["f"]), 9: raw["f9"],
                11: raw["f11"], 13: raw["f13"],
            }
            jets = up.characteristic_jets(A, raw_F, mode_vector, 15)
            f7_x0.append(raw_F[7][0] if raw_F[7] else QF(0))
            f11_x1.append(raw["f11"][1] if len(raw["f11"]) > 1 else QF(0))
            g11_x0.append(jets[11][0])
            g15_x1.append(jets[15][1])

        def endpoint(left, right):
            # Polarized bilinear form; diagonal is the actual endpoint.
            return QF(1, 2) * (
                dot(f11_x1, left) * dot(g11_x0, right)
                + dot(f11_x1, right) * dot(g11_x0, left)
                - dot(f7_x0, left) * dot(g15_x1, right)
                - dot(f7_x0, right) * dot(g15_x1, left)
            )

        witness = None
        for i, left in enumerate(survivor):
            for j, right in enumerate(survivor[i:], i):
                value = endpoint(left, right)
                if value:
                    candidate = left if i == j else [a + b for a, b in zip(left, right)]
                    diagonal = endpoint(candidate, candidate)
                    if not diagonal:
                        candidate = [a + 2 * b for a, b in zip(left, right)]
                        diagonal = endpoint(candidate, candidate)
                    assert diagonal
                    full_vector = [sum(candidate[k] * basis[k][column]
                                       for k in range(fiber_dimension))
                                   for column in range(55)]
                    witness = {
                        "fiber_coordinates": [str(value) for value in candidate],
                        "endpoint": str(diagonal),
                        "nonzero_full_coordinates": {
                            names[column]: str(value)
                            for column, value in enumerate(full_vector) if value
                        },
                    }
                    break
            if witness:
                break
        return {
            "q_rank": rank,
            "q_free": free,
            "receiver_survivor_dimension": len(survivor),
            "endpoint_nonzero_witness": witness,
        }

    q_fixtures = {
        "X": [QF(0), QF(1)],
        "1": [QF(1)],
        "1+X": [QF(1), QF(1)],
        "X2": [QF(0), QF(0), QF(1)],
        "1+X2": [QF(1), QF(0), QF(1)],
        "X+X2": [QF(0), QF(1), QF(1)],
        "1+X+X2": [QF(1), QF(1), QF(1)],
    }
    radius = int(os.environ.get("MODE_GRID_RADIUS", "2"))
    assert 0 <= radius <= 3
    mode_values = tuple(range(-radius, radius + 1))
    q_filter = os.environ.get("Q_FIXTURE_FILTER", "")
    if q_filter:
        assert q_filter in q_fixtures
        q_fixtures = {q_filter: q_fixtures[q_filter]}
    summary = {}
    first_witness = None
    for q_name, q in q_fixtures.items():
        dimension_counts = {}
        nonzero_count = 0
        for modes in itertools.product(mode_values, repeat=3):
            result = analyze(q, modes)
            dimension = result["receiver_survivor_dimension"]
            dimension_counts[dimension] = dimension_counts.get(dimension, 0) + 1
            if result["endpoint_nonzero_witness"]:
                nonzero_count += 1
                if first_witness is None:
                    first_witness = {
                        "Q": q_name,
                        "Q_coefficients": [str(value) for value in q],
                        "modes_c4_c6_c8": list(modes),
                        **result,
                    }
        summary[q_name] = {
            "dimension_counts": {str(k): v for k, v in sorted(dimension_counts.items())},
            "nonzero_endpoint_mode_count": nonzero_count,
        }
    print(json.dumps({
        "run_tag": run_tag,
        "mode_grid": list(mode_values),
        "mode_variables": ["c4", "c6", "c8"],
        "fixtures": summary,
        "first_nonzero_endpoint_witness": first_witness,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
