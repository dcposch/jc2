#!/usr/bin/env python3
"""Exact full-cell discriminator for the reviewed X27 -> X25 transition.

This script works on one promoted modular D25 A^14 cell: p=105337,
fiber a00pp, and the fixed (W1,W2) pair of the banked D25 witness.  It
pulls the six canonical band-26 cokernel equations back through the exact
triangular D25 certificate and differentiates that pullback exactly.

Only the reviewed one-band D1 source is used.  In particular this module
does not import or read a D43 object.  A rank certificate here is about the
band-26 compatibility map on this one modular cell; it says nothing about
band 28, an inverse limit, characteristic zero, or a germ.
"""

import argparse
import contextlib
import hashlib
import json
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.dirname(HERE)
ROOT = os.path.dirname(CASES)
sys.path.insert(0, CASES)
sys.path.insert(0, os.path.join(CASES, "round1_dtransition"))

import d25_eplus as DE
import transition_symbol as TS
import valuation_e as V
import valuation_e2 as V2


TOOL = "cases/round1_dtransition_fullcell/fullcell_compat.py"
P = 105337
FIBER = "a00pp"
FREE = tuple(DE.FREE_BASE + DE.FREE_LIFT)
DEP = tuple(DE.DEP)
FIXED_DIFF = ("uf18", "vf1_34", "vf1_36", "vf2_34", "vf2_36")
SOURCE_FILES = tuple(TS.SOURCE_FILES) + (
    "cases/round1_dtransition/transition_symbol.py",
    "cases/round1_dtransition/samples.json",
    "xmodel/round1-dtransition-20260824.md",
    "xmodel/review-dtransition-grok.md",
    "cases/round1_dtransition_fullcell/PREREG.md",
)


class FullCellError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise FullCellError(message)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def json_hash(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def manifest():
    out = {}
    for rel in SOURCE_FILES:
        path = os.path.join(ROOT, rel)
        require(os.path.isfile(path), "missing provenance input: %s" % rel)
        out[rel] = {"bytes": os.path.getsize(path),
                    "sha256": sha256_file(path)}
    return out


def row_partial(row, variable, values, p=P):
    """Formal partial of a parsed sparse row, evaluated exactly mod p."""
    total = 0
    for coefficient, monomial in row:
        for chosen, (name, exponent) in enumerate(monomial):
            if name != variable:
                continue
            term = coefficient * exponent
            for j, (other, other_exponent) in enumerate(monomial):
                e = other_exponent - (1 if j == chosen else 0)
                if e:
                    term = term * pow(int(values[other]), e, p) % p
            total = (total + term) % p
    return total


def solve_unique(A, b, p=P):
    require(TS.rank(A, p) == len(A[0]),
            "linearized triangular system lost full column rank")
    x = TS.solve(A, b, p)
    require(x is not None, "linearized triangular system is inconsistent")
    return x


def fixed_cell_data(p=P):
    env = DE.fiber_env(p, FIBER)
    require(env["is_radical_frame"], "a00pp radical frame drifted")
    header, rows = DE.parse_fiber_ms(p, FIBER)
    origin = DE.witness_cellval(p, FIBER)
    require(all(int(origin[name]) % p == 0 for name in FREE + DEP),
            "banked witness is not the registered A14 origin")
    W = (int(origin["W1"]) % p, int(origin["W2"]) % p)
    cells = DE.cells_of_fiber(p, FIBER)
    require(W in cells, "witness W-pair is not a promoted cell")
    return env, header, rows, origin, W, cells.index(W)


def reconstruct_free(free_values, p=P):
    """Exact A14 certificate -> pre-frontier and completed source points."""
    env, header, rows, _origin, W, cell_index = fixed_cell_data(p)
    fv = {name: int(free_values.get(name, 0)) % p for name in FREE}
    cell = DE.solve_cell_point(p, header, rows, fv, *W)
    require(not any(DE.eval_row(row, cell, p) for row in rows),
            "34-row D25 cell certificate failed")
    dval, reconstruction = DE.reconstruct_point(p, cell, env)
    checks = DE.verify_full_point(p, dval, env, a00pp_frozen=True)
    require(all(checks.values()), "D25 reconstruction gate failed: %r" % checks)
    wit72, deep = DE.witness72_of(p, dval)
    point = DE.build_point_f(p, wit72, deep, env)
    radical, _r3, _h = V.radical_env(p)
    Z = [pow(radical["z"], m, p) for m in range(42)]
    E = TS.build_E(point, p, Z)
    frontier = {"applied": False, "values": {}}
    if E.V.astype(np.int64)[:30, 24].any():
        y, diag = DE.frontier_solve(E, p)
        require(y is not None, "band-24 triangular completion failed")
        for key, value in y.items():
            if value:
                point["tails"][key[0]][key[1]] = int(value) % p
        E = TS.build_E(point, p, Z)
        frontier = {
            "applied": True,
            "diag": diag,
            "values": {"%s_%d" % (f, 32 + r): int(v)
                       for (f, r), v in y.items()},
        }
    require(not E.V.astype(np.int64)[:, :25].any(),
            "completed point has a residual through band 24")
    return {
        "env": env,
        "header": header,
        "rows": rows,
        "cell": cell,
        "dval": dval,
        "point": point,
        "E": E,
        "Z": Z,
        "free_values": fv,
        "cell_index": cell_index,
        "W": list(W),
        "reconstruction": reconstruction,
        "checks": checks,
        "frontier": frontier,
    }


def relative_block(E, p=P):
    values = E.V.astype(np.int64) % p
    gradients = E.G.astype(np.int64) % p
    columns = [V2.GIDX[key] for key in TS.NEW_COORDS]
    A = [[int(gradients[a, 26, c]) for c in columns]
         for a in TS.NEW_ROWS]
    rhs = [(-int(values[a, 26])) % p for a in TS.NEW_ROWS]
    left, _pivots, _free = TS.kernel_basis(TS.transpose(A), p)
    require(TS.rank(A, p) == 4 and len(left) == 6,
            "source band-26 block is not rank 4 with cokernel 6")
    functions = [sum(lam[i] * rhs[i] for i in range(10)) % p
                 for lam in left]
    compatible = TS.solve(A, rhs, p) is not None
    require(compatible == (not any(functions)),
            "six-function vanishing does not characterize solvability")
    return A, rhs, left, functions, compatible


def cell_tangent(data, p=P):
    """Derivative of the certified 28-coordinate cell map at one point."""
    rows, cell = data["rows"], data["cell"]
    Jdep = [[row_partial(row, name, cell, p) for name in DEP]
            for row in rows]
    require(TS.rank(Jdep, p) == len(DEP),
            "dependent-coordinate Jacobian lost rank 10")
    tangent = {name: [int(i == j) for j in range(len(FREE))]
               for i, name in enumerate(FREE)}
    for name in DEP:
        tangent[name] = [0] * len(FREE)
    for j, name in enumerate(FREE):
        rhs = [(-row_partial(row, name, cell, p)) % p for row in rows]
        solution = solve_unique(Jdep, rhs, p)
        for dependent, value in zip(DEP, solution):
            tangent[dependent][j] = value
    for row in rows:
        for j in range(len(FREE)):
            derivative = sum(row_partial(row, name, cell, p) *
                             tangent[name][j] for name in FREE + DEP) % p
            require(derivative == 0, "cell tangent does not kill all 34 rows")
    return tangent, Jdep


def reconstruction_tangent(data, cell_derivative, p=P):
    """Differentiate the exact pivot/tg/deep zero-completion certificate."""
    env, dval = data["env"], data["dval"]
    Adeep, _bdeep = DE.band22_system(p, dval, env)
    _R, deep_pivots, _rows = TS.rref(Adeep, p)
    require(len(deep_pivots) == 4, "deep zero-completion rank is not four")
    deep_names = [V.DEEPMAP[x] for x in V.DEEPX]
    pivot_deep_names = [deep_names[i] for i in deep_pivots]
    pivot_names = [name for name, _label in V.PIV22_SEQ()]
    unknowns = pivot_names + list(DE.TG_PAIR) + pivot_deep_names
    require(len(unknowns) == 28 and len(set(unknowns)) == 28,
            "reconstruction tangent registry overlaps")

    rows21, variables = V.raw_rows21()
    _point, r3, _h = V.radical_env(p)
    equation_partials = []
    # Use every pristine D21 equation, not merely the 22 square-solve
    # pivots.  The latter determine the numeric reconstruction, but the
    # remaining equations carry the cell-compatibility syzygies needed for
    # a faithful tangent pullback away from the origin.
    for label, row in rows21:
        value, partials = DE.vexpr_vp_f(
            row, variables, dval, p, r3, env)
        require(value == 0, "pristine D21 equation nonzero at base point")
        equation_partials.append(partials)
    for _label, row in V.row22_rows(p):
        value, partials = DE.msrow_vp_f(row, dval, p, env)
        require(value == 0, "Row_22 equation nonzero at base point")
        equation_partials.append(partials)
    U = [[partials.get(name, 0) for name in unknowns]
         for partials in equation_partials]
    require(TS.rank(U, p) == len(unknowns),
            "combined pivot/tg/deep tangent rank is not 28")

    x2tf = DE.x2tf_cached()
    derivative = {x2tf[name]: vector[:]
                  for name, vector in cell_derivative.items()}
    for name in unknowns:
        derivative[name] = [0] * len(FREE)
    for j in range(len(FREE)):
        rhs = []
        for partials in equation_partials:
            known = sum(coefficient * derivative[name][j]
                        for name, coefficient in partials.items()
                        if name not in unknowns and name in derivative) % p
            rhs.append((-known) % p)
        solution = solve_unique(U, rhs, p)
        for name, value in zip(unknowns, solution):
            derivative[name][j] = value
    for partials in equation_partials:
        for j in range(len(FREE)):
            value = sum(coefficient * derivative.get(
                name, [0] * len(FREE))[j]
                        for name, coefficient in partials.items()) % p
            require(value == 0, "reconstruction tangent replay failed")
    return derivative, {
        "deep_pivot_indices": deep_pivots,
        "deep_pivot_names": pivot_deep_names,
        "combined_equations": len(U),
        "combined_unknowns": len(unknowns),
        "combined_rank": TS.rank(U, p),
    }


@contextlib.contextmanager
def extended_source_gradients():
    """Temporarily add the five varying prefix coefficients to V2.G."""
    old_index = dict(V2.GIDX)
    old_dimension = V2.GD
    old_orbit_levels = V2.orbit_levels
    old_other_block = V2.other_block
    old_b_block = V2.b_block
    for name in FIXED_DIFF:
        V2.GIDX[("__fixed__", name)] = len(V2.GIDX)
    V2.GD = len(V2.GIDX)

    def fixed_index(name):
        return V2.GIDX.get(("__fixed__", name))

    def orbit_levels(point, family, p):
        fixed = point["fixed"]
        side = "1" if family.endswith("1") else "2"
        levels = {
            12: (1, None),
            18: (fixed["uf18"], fixed_index("uf18")),
            24: (fixed["uf24"], fixed_index("uf24")),
            30: (fixed["uf30"], fixed_index("uf30")),
            32: (fixed["A" + side], fixed_index("A" + side)),
            34: (fixed["vf%s_34" % side],
                 fixed_index("vf%s_34" % side)),
            36: (fixed["vf%s_36" % side],
                 fixed_index("vf%s_36" % side)),
        }
        if family in ("tf1", "tf2"):
            levels[37] = (fixed["W" + side], fixed_index("W" + side))
        elif family in ("tg1", "tg2"):
            levels[37] = (fixed["HW" + side], fixed_index("HW" + side))
        values = point["tails"][family]
        for r in V2.allowed_r(family):
            levels[32 + r] = (values.get(r, 0), V2.GIDX[(family, r)])
        return levels

    def b_block(point, power, p):
        fixed = point["fixed"]
        R = V2.Jet(2, True)
        R.V[0][0] = 1
        for slot, name in ((6, "uf18"), (12, "uf24"), (18, "uf30")):
            R.V[0][slot] = fixed[name]
            index = fixed_index(name)
            if index is not None:
                R.G[0][slot][index] = 1
        R.V[1][20] = 1
        R2 = V2.jmul(R, R, p)
        R4 = V2.jmul(R2, R2, p)
        Q = V2.jmul(V2.jmul(R4, R2, p), R, p)
        Q.V[0][0] = (Q.V[0][0] - 3 * pow(2, p - 2, p)) % p
        result = None
        for _ in range(power):
            result = Q if result is None else V2.jmul(result, Q, p)
        return result

    def other_block(Y, k, n7, p, Z):
        """V2.other_block with exact prefix-variable differentials.

        In Delta=P-C_kY the slots 12,18,24,30 occur in both P and Y.
        The original production gradient does not track fixed prefix
        variables, so extending only orbit_levels would incorrectly record
        -C_k instead of 1-C_k for uf18/uf24/uf30.
        """
        dv = np.zeros(V2._S)
        dg = np.zeros((V2._S, V2.GD))
        for level, (value, gradient_column) in Y.items():
            slot = level - 12
            if slot >= V2._S:
                continue
            twist = Z[(k * level) % 42]
            contribution = (-twist * value) % p
            gradient_coefficient = (-twist) % p
            if level in (12, 18, 24, 30):
                prefix_value = {12: 1, 18: Y[18][0],
                                24: Y[24][0], 30: Y[30][0]}[level]
                contribution = (prefix_value - twist * value) % p
                gradient_coefficient = (1 - twist) % p
            dv[slot] = contribution
            if gradient_column is not None:
                dg[slot][gradient_column] = gradient_coefficient
        D = (dv, dg)
        powers = {1: D}
        for r in range(2, n7 + 1):
            powers[r] = V2.smul(powers[r - 1], D, p)
        mask = (np.arange(V2._S) % 6 == 0).astype(np.float64)
        q = {}
        for r in range(1, n7 + 1):
            value, gradient = powers[r]
            q[r] = (np.mod(value * mask * n7, p),
                    np.mod(gradient * mask[:, None] * n7, p))
        elementary = [(np.zeros(V2._S),
                       np.zeros((V2._S, V2.GD)))]
        elementary[0][0][0] = 1
        for j in range(1, n7 + 1):
            accumulator = (np.zeros(V2._S),
                           np.zeros((V2._S, V2.GD)))
            for r in range(1, j + 1):
                term = V2.smul(elementary[j - r], q[r], p)
                accumulator = V2.sadd(
                    accumulator,
                    V2.sscal(term, (-1) ** (r - 1) % p, p), p)
            elementary.append(V2.sscal(
                accumulator, pow(j, p - 2, p), p))
        block = V2.Jet(n7 + 1, True)
        for i in range(n7 + 1):
            if 20 * i >= V2._S and i > 0:
                break
            value, gradient = elementary[n7 - i]
            block.V[i][20 * i:] = value[:V2._S - 20 * i]
            block.G[i][20 * i:] = gradient[:V2._S - 20 * i]
        return block

    V2.orbit_levels = orbit_levels
    V2.other_block = other_block
    V2.b_block = b_block
    try:
        yield
    finally:
        V2.GIDX.clear()
        V2.GIDX.update(old_index)
        V2.GD = old_dimension
        V2.orbit_levels = old_orbit_levels
        V2.other_block = old_other_block
        V2.b_block = old_b_block


def point_coordinate_tangent(dval_derivative, p=P):
    """Map reconstructed dval names into valuation_e2 source columns."""
    deep_names = {V.DEEPMAP[x] for x in V.DEEPX}
    tangent = np.zeros((V2.GD, len(FREE)), dtype=np.int64)
    for name, vector in dval_derivative.items():
        source_name = V2.DEEP_RELABEL.get(name, name) \
            if name in deep_names else name
        if source_name in FIXED_DIFF:
            index = V2.GIDX[("__fixed__", source_name)]
        elif "_" in source_name:
            family, level = source_name.rsplit("_", 1)
            key = (family, int(level) - 32)
            if key not in V2.GIDX:
                continue
            index = V2.GIDX[key]
        else:
            continue
        tangent[index, :] = (tangent[index, :] +
                             np.array(vector, dtype=np.int64)) % p
    return tangent


def compatibility_jacobian(data, left_basis, p=P):
    """Exact 6 x 14 differential through cell, reconstruction, frontier."""
    cell_derivative, cell_J = cell_tangent(data, p)
    dval_derivative, rec_diag = reconstruction_tangent(
        data, cell_derivative, p)
    with extended_source_gradients():
        jf, jg = V2.build_jets(data["point"], p, data["Z"])
        E = V2.euler_rows(jf, jg, p)
        gradient = E.G.astype(np.int64) % p
        tangent = point_coordinate_tangent(dval_derivative, p)

        frontier_columns = [V2.GIDX[key] for key in DE.FRONTIER10]
        A24 = [[int(gradient[a, 24, c]) for c in frontier_columns]
               for a in DE.ROWS24]
        require(TS.rank(A24, p) == 4, "frontier tangent rank is not four")
        frontier_derivatives = [[0] * len(FREE) for _ in DE.FRONTIER10]
        for j in range(len(FREE)):
            residual_derivative = [
                int(np.dot(gradient[a, 24, :], tangent[:, j]) % p)
                for a in DE.ROWS24]
            solution = TS.solve(
                A24, [(-value) % p for value in residual_derivative], p)
            require(solution is not None,
                    "frontier derivative is outside the rank-four image")
            for i, (index, value) in enumerate(zip(
                    frontier_columns, solution)):
                tangent[index, j] = (tangent[index, j] + value) % p
                frontier_derivatives[i][j] = value
            replay = [
                (residual_derivative[i] + sum(
                    A24[i][k] * solution[k]
                    for k in range(len(DE.FRONTIER10)))) % p
                for i in range(len(DE.ROWS24))]
            require(not any(replay), "frontier tangent replay failed")

        jacobian = []
        for lam in left_basis:
            row = []
            for j in range(len(FREE)):
                residual_derivative = [
                    int(np.dot(gradient[a, 26, :], tangent[:, j]) % p)
                    for a in TS.NEW_ROWS]
                row.append((-sum(lam[i] * residual_derivative[i]
                                 for i in range(10))) % p)
            jacobian.append(row)
    rank = TS.rank(jacobian, p)
    _R, pivot_columns, pivot_rows = TS.rref(jacobian, p)
    rank_matrix = [[jacobian[i][j] for j in pivot_columns]
                   for i in pivot_rows]
    rank_minor = {
        "row_indices": pivot_rows,
        "column_indices": pivot_columns,
        "column_names": [FREE[j] for j in pivot_columns],
        "matrix": rank_matrix,
        "determinant_mod_p": TS.determinant(rank_matrix, p),
    }
    require(rank_minor["determinant_mod_p"] != 0,
            "canonical Jacobian rank witness is zero")
    function_dependencies, _dp, _df = TS.kernel_basis(
        TS.transpose(jacobian), p)
    minor = None
    if rank == 6:
        matrix = [[jacobian[i][j] for j in pivot_columns]
                  for i in range(6)]
        minor = {
            "column_indices": pivot_columns,
            "column_names": [FREE[j] for j in pivot_columns],
            "matrix": matrix,
            "determinant_mod_p": TS.determinant(matrix, p),
        }
        require(minor["determinant_mod_p"] != 0,
                "declared rank-six minor is zero")
    return jacobian, rank, minor, {
        "cell_dependent_jacobian_rank": TS.rank(cell_J, p),
        "reconstruction": rec_diag,
        "frontier_rank": TS.rank(A24, p),
        "frontier_derivatives": frontier_derivatives,
        "jacobian_rank_minor": rank_minor,
        "left_dependencies_among_function_differentials":
            function_dependencies,
    }


def point_record(free_values, tag, p=P):
    data = reconstruct_free(free_values, p)
    A, rhs, left, functions, compatible = relative_block(data["E"], p)
    jacobian, jacobian_rank, minor, tangent_diag = compatibility_jacobian(
        data, left, p)
    return {
        "tag": tag,
        "prime": p,
        "fiber": FIBER,
        "cell_index": data["cell_index"],
        "W": data["W"],
        "free_values": data["free_values"],
        "cell_point_sha256": json_hash(sorted(
            (name, int(value)) for name, value in data["cell"].items())),
        "completed_point_sha256": json_hash({
            "fixed": sorted((name, int(value))
                            for name, value in data["point"]["fixed"].items()),
            "tails": {family: sorted((int(r), int(value)) for r, value in
                                      data["point"]["tails"][family].items())
                      for family in V2.FAMS},
        }),
        "frontier": data["frontier"],
        "A26": A,
        "rhs26": rhs,
        "A26_rank": TS.rank(A, p),
        "left_cokernel_basis": left,
        "compatibility_functions": functions,
        "compatible": compatible,
        "compatibility_jacobian": jacobian,
        "compatibility_jacobian_rank": jacobian_rank,
        "rank_six_minor": minor,
        "tangent_diagnostics": tangent_diag,
    }


def decide(records):
    zeros = [record for record in records if record["compatible"]]
    rank_six = [record for record in records
                if record["compatibility_jacobian_rank"] == 6]
    smooth_zeros = [record for record in zeros
                    if record["compatibility_jacobian_rank"] == 6]
    if smooth_zeros:
        return "SMOOTH-CODIM6-STRATUM"
    if zeros and rank_six:
        return "NONEMPTY-ZERO-LOCUS;GENERIC-RANK6;ORIGIN-SINGULAR"
    if zeros:
        return "NONEMPTY-SINGULAR-OR-LOWER-RANK"
    return "INCONCLUSIVE"


def run(out_path):
    provenance = manifest()
    origin = point_record({}, "cell-origin")
    # A deterministic non-origin point on the same fixed-W A14 cell.  It is
    # a generic-rank discriminator, not a Monte Carlo assertion.
    sequence = {name: i + 1 for i, name in enumerate(FREE)}
    generic = point_record(sequence, "same-cell-sequence-1-to-14")
    require(origin["A26"] == generic["A26"],
            "band-26 coefficient matrix changed across the cell test")
    require(origin["left_cokernel_basis"] == generic["left_cokernel_basis"],
            "canonical cokernel basis changed across the cell test")
    origin_dependencies = origin["tangent_diagnostics"][
        "left_dependencies_among_function_differentials"]
    generic_dependencies = generic["tangent_diagnostics"][
        "left_dependencies_among_function_differentials"]
    shared_dependency = (origin_dependencies[0]
                         if len(origin_dependencies) == 1 and
                         origin_dependencies == generic_dependencies
                         else None)
    if shared_dependency is not None:
        require(all(sum(a * b for a, b in zip(
            shared_dependency, record["compatibility_functions"])) % P == 0
                    for record in (origin, generic)),
                "shared differential dependency does not annihilate values")
    verdict = decide([origin, generic])
    out = {
        "tool": TOOL,
        "status": "INTERNAL / PRODUCER-CHECKED / MOD-p FULL-CELL GATE",
        "verdict": verdict,
        "scope": (
            "one promoted p=105337 a00pp D25 A14 cell; source-defined "
            "X27->X25 through band 26 only"),
        "perimeter": (
            "No band-28 persistence, inverse limit, formal germ, "
            "characteristic-zero, algebraization, polynomial-map, or "
            "counterexample inference."),
        "free_coordinate_order": list(FREE),
        "compatibility_definition": {
            "source_rows": ["Row_26[eta^%d]" % a for a in TS.NEW_ROWS],
            "new_coordinates": ["%s_%d" % (f, 32 + r)
                                for f, r in TS.NEW_COORDS],
            "formula": "C_i(s)=lambda_i dot (-E_26(s)); i=1..6",
            "lambda_basis": origin["left_cokernel_basis"],
            "coefficient_matrix_rank": origin["A26_rank"],
            "straight_line_evaluator": TOOL + ":reconstruct_free+relative_block",
        },
        "two_point_shared_dependency": {
            "coefficient_vector": shared_dependency,
            "annihilates_function_values_at_both_registered_points":
                shared_dependency is not None,
            "scope_warning": (
                "This repeated exact relation is not by itself a polynomial-"
                "identity certificate on all of A14."),
        },
        "records": [origin, generic],
        "source_manifest": provenance,
        "source_manifest_sha256": json_hash(provenance),
    }
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)
        f.write("\n")
    print("origin compatible/rank:", origin["compatible"],
          origin["compatibility_jacobian_rank"])
    print("sequence compatible/rank:", generic["compatible"],
          generic["compatibility_jacobian_rank"])
    print("VERDICT:", verdict)
    print("WROTE:", out_path)
    return out


def selftest():
    require(len(FREE) == 14 and len(DEP) == 10,
            "D25 triangular registry is not 14 free + 10 dependent")
    require(len(TS.NEW_ROWS) == len(TS.NEW_COORDS) == 10,
            "reviewed transition registry changed")
    require(not any("d43" in name.lower() for name in SOURCE_FILES),
            "D43 provenance entered the full-cell tool")
    A = [[1, 2], [2, 4], [1, 0]]
    require(TS.rank(A, 101) == 2 and
            solve_unique(A, [3, 6, 1], 101) == [1, 1],
            "overdetermined exact solve selftest failed")
    print("PASS selftest: registries, D43 exclusion, exact derivatives/solve")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--out", default=os.path.join(HERE, "results.json"))
    args = parser.parse_args()
    if args.selftest:
        selftest()
    if args.run:
        run(args.out)
    if not args.selftest and not args.run:
        parser.print_help()


if __name__ == "__main__":
    main()
