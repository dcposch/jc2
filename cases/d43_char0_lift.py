#!/usr/bin/env python3
"""Exact first-order p-adic screen for the reconstructed D43 witness.

This deliberately separates two objects.

``source`` is the pristine 184-row Euler system, evaluated from the
regression-banked numeric jet constructor with its coefficient radicals
Hensel-lifted to Z/p^2.  It is a genuine characteristic-zero source model.

``assembled`` is the 218-row NF/parked presentation used by
``d43_full_family.py``.  Its prime-specific NF checkpoints and the integral
NF traces are not shipped in this repository.  Consequently this tool does
not pretend that a source-model p^2 lift is a lift of the 218-row assembled
presentation.  It records that boundary explicitly in its certificate.

The useful fail-closed implication is: an inconsistent correction system in
the enlarged 190-coordinate source model obstructs the reconstructed point.
Consistency is only a source-model screen; it is not a Hensel certificate.
"""

import argparse
import hashlib
import json
import os
import sys
import types


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d43_family2 as F
import d43_full_family as FULL
import d43_graph_witness as GW
import d43_nf_certificate as NF
import eplus43 as X
import r1_fullcore as FC


PRIME = 105337
FAMS = ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02")
FIXED_COORDS = ("W1", "W2", "uf18", "uf24", "vf1_34", "vf1_36",
                "vf2_34", "vf2_36")
MISSING_RECONSTRUCTED_TAILS = tuple(
    (family, r) for family in ("tf1", "tf2", "tg1", "tg2")
    for r in (39, 41))


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_json(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def hensel_root_mod_p2(a, p, polynomial, derivative):
    """Unique simple-root lift of a mod p to Z/p^2."""
    modulus = p * p
    value = polynomial(a)
    assert value % p == 0
    slope = derivative(a) % p
    assert slope
    correction = (-(value // p) * pow(slope, -1, p)) % p
    lifted = (a + p * correction) % modulus
    assert polynomial(lifted) % modulus == 0
    return lifted


def coefficient_lifts(p, env):
    """Hensel lifts of the a00pp coefficient-radical embedding."""
    modulus = p * p
    point = FC.radical_point(p)
    r3 = hensel_root_mod_p2(
        point["r3"], p, lambda value: value * value - 3,
        lambda value: 2 * value)
    zeta = hensel_root_mod_p2(
        point["z"], p, lambda value: pow(value, 42) - 1,
        lambda value: 42 * pow(value, 41))
    A1 = hensel_root_mod_p2(
        env["A1"], p, lambda value: pow(value, 3) - (3 + r3),
        lambda value: 3 * value * value)
    A2 = hensel_root_mod_p2(
        env["A2"], p, lambda value: pow(value, 3) - (3 - r3),
        lambda value: 3 * value * value)
    assert env["h1"] == env["h2"], "a00pp must be the +,+ h branch"
    h32 = hensel_root_mod_p2(
        env["h1"], p, lambda value: 2 * value * value - 3,
        lambda value: 4 * value)
    checks = {
        "r3^2-3": (r3 * r3 - 3) % modulus,
        "zeta^42-1": (pow(zeta, 42, modulus) - 1) % modulus,
        "A1^3-(3+r3)": (pow(A1, 3, modulus) - 3 - r3) % modulus,
        "A2^3-(3-r3)": (pow(A2, 3, modulus) - 3 + r3) % modulus,
        "2*h32^2-3": (2 * h32 * h32 - 3) % modulus,
    }
    assert not any(checks.values())
    return {
        "r3": r3, "zeta42": zeta, "A1": A1, "A2": A2,
        "h32": h32, "defining_equation_residues_mod_p2": checks,
    }


def _add(target, key, value, modulus):
    value = (target.get(key, 0) + value) % modulus
    if value:
        target[key] = value
    else:
        target.pop(key, None)


def _jet_mul(left, right, modulus, slots=43, hcap=34):
    result = {}
    for (ha, sa), ca in left.items():
        for (hb, sb), cb in right.items():
            h = ha + hb
            slot = sa + sb
            if h < hcap and slot < slots:
                _add(result, (h, slot), ca * cb, modulus)
    return result


def _series_mul(left, right, modulus, slots=43):
    result = {}
    for sa, ca in left.items():
        for sb, cb in right.items():
            if sa + sb < slots:
                _add(result, sa + sb, ca * cb, modulus)
    return result


def _orbit_levels(point, family):
    fixed = point["fixed"]
    side = "1" if family.endswith("1") else "2"
    levels = {
        12: 1, 18: fixed["uf18"], 24: fixed["uf24"],
        30: fixed["uf30"], 32: fixed["A" + side],
        34: fixed["vf%s_34" % side], 36: fixed["vf%s_36" % side],
    }
    if family in ("tf1", "tf2"):
        levels[37] = fixed["W" + side]
    elif family in ("tg1", "tg2"):
        levels[37] = fixed["HW" + side]
    for r, value in point["tails"][family].items():
        levels[32 + int(r)] = int(value)
    return levels


def _through_block(levels, n7, zeta, modulus):
    result = None
    for j in range(n7):
        factor = {(1, 0): 1}
        for level, value in levels.items():
            slot = level - 32
            if level >= 32 and slot < 43:
                twist = pow(zeta, (7 * j * level) % 42, modulus)
                _add(factor, (0, slot), -twist * value, modulus)
        result = factor if result is None else _jet_mul(
            result, factor, modulus)
    return result


def _other_block(levels, k, n7, zeta, modulus):
    delta = {}
    for level, value in levels.items():
        slot = level - 12
        if slot >= 43:
            continue
        twist = pow(zeta, (k * level) % 42, modulus)
        contribution = -twist * value
        if level in (12, 18, 24, 30):
            contribution += value
        contribution %= modulus
        if contribution:
            delta[slot] = contribution
    powers = {1: delta}
    for exponent in range(2, n7 + 1):
        powers[exponent] = _series_mul(
            powers[exponent - 1], delta, modulus)
    q = {
        exponent: {slot: n7 * value % modulus
                   for slot, value in powers[exponent].items()
                   if slot % 6 == 0}
        for exponent in range(1, n7 + 1)
    }
    elementary = [{0: 1}]
    for j in range(1, n7 + 1):
        accumulator = {}
        for exponent in range(1, j + 1):
            sign = 1 if (exponent - 1) % 2 == 0 else -1
            for slot, value in _series_mul(
                    elementary[j - exponent], q[exponent], modulus).items():
                _add(accumulator, slot, sign * value, modulus)
        inverse = pow(j, -1, modulus)
        elementary.append({slot: value * inverse % modulus
                           for slot, value in accumulator.items() if value})
    result = {}
    for eta_power in range(n7 + 1):
        shift = 20 * eta_power
        if eta_power and shift >= 43:
            break
        for slot, value in elementary[n7 - eta_power].items():
            if slot + shift < 43:
                _add(result, (eta_power, slot + shift), value, modulus)
    return result


def _aside_orbit(point, family, zeta, modulus):
    n7 = 3 if family.startswith("tg0") else 6
    levels = _orbit_levels(point, family)
    result = _through_block(levels, n7, zeta, modulus)
    for k in range(1, 7):
        result = _jet_mul(
            result, _other_block(levels, k, n7, zeta, modulus), modulus)
    return result


def _b_block(point, power, modulus):
    fixed = point["fixed"]
    seed = {
        (0, 0): 1, (0, 6): fixed["uf18"],
        (0, 12): fixed["uf24"], (0, 18): fixed["uf30"],
        (1, 20): 1,
    }
    square = _jet_mul(seed, seed, modulus)
    fourth = _jet_mul(square, square, modulus)
    q = _jet_mul(_jet_mul(fourth, square, modulus), seed, modulus)
    _add(q, (0, 0), -3 * pow(2, -1, modulus), modulus)
    result = None
    for _ in range(power):
        result = q if result is None else _jet_mul(result, q, modulus)
    return result


def source_rows(point, zeta, modulus):
    """The 184 canonical D43 row values over Z/modulus."""
    phi = _jet_mul(
        _jet_mul(_aside_orbit(point, "tf1", zeta, modulus),
                 _aside_orbit(point, "tf2", zeta, modulus), modulus),
        _b_block(point, 6, modulus), modulus)
    gamma = _jet_mul(
        _jet_mul(_aside_orbit(point, "tg1", zeta, modulus),
                 _aside_orbit(point, "tg2", zeta, modulus), modulus),
        _jet_mul(
            _jet_mul(_aside_orbit(point, "tg01", zeta, modulus),
                     _aside_orbit(point, "tg02", zeta, modulus), modulus),
            _b_block(point, 9, modulus), modulus), modulus)
    theta_phi = {(h, slot): (slot - 12) * value % modulus
                 for (h, slot), value in phi.items()}
    theta_gamma = {(h, slot): (slot - 18) * value % modulus
                   for (h, slot), value in gamma.items()}
    phi_eta = {(h - 1, slot): h * value % modulus
               for (h, slot), value in phi.items() if h}
    gamma_eta = {(h - 1, slot): h * value % modulus
                 for (h, slot), value in gamma.items() if h}
    euler = _jet_mul(theta_phi, gamma_eta, modulus)
    negative = _jet_mul(phi_eta, theta_gamma, modulus)
    for key, value in negative.items():
        _add(euler, key, -value, modulus)
    _add(euler, (0, 20), 42, modulus)
    return [euler.get((a, X.S30[a] + 6 * j), 0) % modulus
            for a, j in X.ROWS_CANON]


def _load_fixed_gradient_engine():
    """Configured float64 dual engine, extended by eight fixed columns.

    At p=105337 its accumulation bound is below 2^53.  This is used only
    for J mod p; p^2 values use the integer sparse engine above.
    """
    source_path = os.path.join(HERE, "valuation_e2.py")
    source = open(source_path).read()
    patches = [
        ("DBUILD = 42            # slots 0..41; pure-y exact below t^42",
         "DBUILD = 43            # D43 p-adic screen"),
        ("RMAX = 40              # tangent coords r <= 40 can reach bands <= 41",
         "RMAX = 42              # D43 p-adic screen"),
        ("GD = len(GIDX)                                                 # 170",
         "FIXCOLS = " + repr(FIXED_COORDS) + "\n"
         "for _nm in FIXCOLS:\n"
         "    GIDX[(\"FIX\", _nm)] = len(GIDX)\n"
         "GD = len(GIDX)"),
        ('lv = {12: (1, None), 18: (fx["uf18"], None), 24: (fx["uf24"], None),\n'
         '          30: (fx["uf30"], None), 32: (fx["A" + side], None),\n'
         '          34: (fx["vf%s_34" % side], None), 36: (fx["vf%s_36" % side], None)}',
         'lv = {12: (1, None),\n'
         '          18: (fx["uf18"], GIDX[("FIX", "uf18")]),\n'
         '          24: (fx["uf24"], GIDX[("FIX", "uf24")]),\n'
         '          30: (fx["uf30"], None), 32: (fx["A" + side], None),\n'
         '          34: (fx["vf%s_34" % side], GIDX[("FIX", "vf%s_34" % side)]),\n'
         '          36: (fx["vf%s_36" % side], GIDX[("FIX", "vf%s_36" % side)])}'),
        ('if fam in ("tf1", "tf2"):\n'
         '        lv[37] = (fx["W" + side], None)\n'
         '    elif fam in ("tg1", "tg2"):\n'
         '        lv[37] = (fx["HW" + side], None)',
         'if fam in ("tf1", "tf2"):\n'
         '        lv[37] = (fx["W" + side], GIDX[("FIX", "W" + side)])\n'
         '    elif fam in ("tg1", "tg2"):\n'
         '        lv[37] = (fx["HW" + side],\n'
         '                  (GIDX[("FIX", "W" + side)], fx["h32"]))'),
        ('if gc is not None:\n'
         '                fac.G[0][s][gc] = (-tw) % p',
         'if gc is not None:\n'
         '                if isinstance(gc, tuple):\n'
         '                    fac.G[0][s][gc[0]] = (-tw * gc[1]) % p\n'
         '                else:\n'
         '                    fac.G[0][s][gc] = (-tw) % p'),
        ('if gc is not None:\n'
         '            dg[s][gc] = (-tw) % p',
         'if gc is not None:\n'
         '            if isinstance(gc, tuple):\n'
         '                dg[s][gc[0]] = (-tw * gc[1]) % p\n'
         '            else:\n'
         '                # At levels 18/24 the shared P term varies with\n'
         '                # the same fixed coordinate as Y.\n'
         '                dg[s][gc] = ((1 if lvl in (18, 24) else 0) - tw) % p'),
        ('R = Jet(2, False)\n'
         '    R.V[0][0] = 1\n'
         '    R.V[0][6] = fx["uf18"]\n'
         '    R.V[0][12] = fx["uf24"]\n'
         '    R.V[0][18] = fx["uf30"]\n'
         '    R.V[1][20] = 1',
         'R = Jet(2, True)\n'
         '    R.V[0][0] = 1\n'
         '    R.V[0][6] = fx["uf18"]\n'
         '    R.G[0][6][GIDX[("FIX", "uf18")]] = 1\n'
         '    R.V[0][12] = fx["uf24"]\n'
         '    R.G[0][12][GIDX[("FIX", "uf24")]] = 1\n'
         '    R.V[0][18] = fx["uf30"]\n'
         '    R.V[1][20] = 1'),
    ]
    for old, new in patches:
        assert source.count(old) == 1, ("patch anchor drift", old[:80])
        source = source.replace(old, new)
    module = types.ModuleType("valuation_e43_fixed_gradient")
    module.__file__ = source_path
    sys.modules[module.__name__] = module
    exec(compile(source, module.__name__, "exec"), module.__dict__)
    assert module.DBUILD == 43 and module.RMAX == 42
    assert module.GD == 188
    return module, sha256_path(source_path)


def source_jacobian(point, p):
    """184 x 190 Jacobian and its ordered source-coordinate labels."""
    engine, source_hash = _load_fixed_gradient_engine()
    root_point = FC.radical_point(p)
    zeta_powers = [pow(root_point["z"], exponent, p)
                   for exponent in range(42)]
    phi, gamma = engine.build_jets(point, p, zeta_powers)
    euler = engine.euler_rows(phi, gamma, p)
    labels = [label for label, _index in sorted(
        engine.GIDX.items(), key=lambda item: item[1])]
    matrix = []
    for a, j in X.ROWS_CANON:
        band = X.S30[a] + 6 * j
        matrix.append([int(value) % p for value in euler.G[a][band]])
    # Alpha and beta are independent x-side directions and are zero at the
    # point, so they do not alter the preceding y/fixed derivatives.
    full_euler, _aux = X.build_operator(point, p, 0, 0, Z=zeta_powers)
    tail_columns_checked = 0
    for label, index in engine.GIDX.items():
        if label[0] not in FAMS:
            continue
        certified_index = X.V43.GIDX[label]
        for row_index, (a, j) in enumerate(X.ROWS_CANON):
            band = X.S30[a] + 6 * j
            assert matrix[row_index][index] == \
                int(full_euler.G[a][band][certified_index]) % p
        tail_columns_checked += 1
    assert tail_columns_checked == 180
    for row, (a, j) in zip(matrix, X.ROWS_CANON):
        band = X.S30[a] + 6 * j
        row.extend([int(full_euler.G[a][band][X.XCOL_A]) % p,
                    int(full_euler.G[a][band][X.XCOL_B]) % p])
    labels.extend([("X", "alpha"), ("X", "beta")])
    assert len(matrix) == 184 and len(matrix[0]) == len(labels) == 190
    return matrix, labels, source_hash


def solve_rectangular(matrix, rhs, p):
    """RREF solve with all free correction coordinates set to zero."""
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    work = [[int(value) % p for value in row] + [int(value) % p]
            for row, value in zip(matrix, rhs)]
    rank = 0
    pivots = []
    for column in range(columns):
        pivot = next((index for index in range(rank, rows)
                      if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [value * inverse % p for value in work[rank]]
        for index in range(rows):
            if index != rank and work[index][column]:
                scale = work[index][column]
                work[index] = [(left - scale * right) % p
                               for left, right in zip(work[index],
                                                      work[rank])]
        pivots.append(column)
        rank += 1
        if rank == rows:
            break
    inconsistent = any(not any(row[:columns]) and row[columns]
                       for row in work)
    if inconsistent:
        return None, rank, pivots
    solution = [0] * columns
    for index, column in enumerate(pivots):
        solution[column] = work[index][columns]
    return solution, rank, pivots


def apply_correction(point, labels, correction, p, coefficient_data):
    modulus = p * p
    lifted = {
        "tails": {family: {int(r): int(value)
                            for r, value in point["tails"][family].items()}
                  for family in FAMS},
        "fixed": {name: int(value) for name, value in point["fixed"].items()},
    }
    alpha = beta = 0
    for label, delta in zip(labels, correction):
        if not delta:
            continue
        if label[0] in FAMS:
            family, r = label
            value = (lifted["tails"][family].get(r, 0) + p * delta) % modulus
            if value:
                lifted["tails"][family][r] = value
            else:
                lifted["tails"][family].pop(r, None)
        elif label[0] == "FIX":
            name = label[1]
            lifted["fixed"][name] = (
                lifted["fixed"][name] + p * delta) % modulus
        elif label == ("X", "alpha"):
            alpha = p * delta % modulus
        elif label == ("X", "beta"):
            beta = p * delta % modulus
        else:
            raise AssertionError(label)
    fixed = lifted["fixed"]
    fixed.update({
        "A1": coefficient_data["A1"], "A2": coefficient_data["A2"],
        "r3": coefficient_data["r3"], "h32": coefficient_data["h32"],
        "HW1": coefficient_data["h32"] * fixed["W1"] % modulus,
        "HW2": coefficient_data["h32"] * fixed["W2"] % modulus,
    })
    # The present witness has alpha=beta=0.  Nonzero corrections would need
    # the value-side x multiplier; retain them in the certificate and fail
    # closed rather than silently dropping them.
    assert alpha == beta == 0, ("nonzero x-side correction unsupported",
                                alpha, beta)
    return lifted


def available_reduction_audit(p, bank_path, certificate):
    """Replay all reduction data that are actually shipped."""
    import pickle
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    external = {name: int(value) % p
                for name, value in certificate["point"]["graph_156"].items()}
    values = [FULL.eval_row(row, external, p) for row in bank["rows"]]
    term_counts = [len(row) for row in bank["rows"]]
    row_payload = [sorted((list(monomial), int(value))
                          for monomial, value in row.items())
                   for row in bank["rows"]]
    return {
        "pointbank_sha256": sha256_path(bank_path),
        "rows": len(bank["rows"]),
        "variables": len(bank["variables"]),
        "terms": sum(term_counts),
        "max_degree": max(FULL.row_degree(row) for row in bank["rows"]),
        "rows_zero_at_banked_point": sum(value == 0 for value in values),
        "canonical_pointbank_rows_sha256": sha256_json(row_payload),
        "banked_certificate_all_218_rows_zero":
            bool(certificate["replay"]["all_218_rows_zero"]),
    }


def assembled_special_fiber_rank(p, certificate, source_matrix,
                                 source_labels):
    """Exact rank of parked rows plus pristine rows in 184 coordinates.

    The checkpoint NF identity has the form raw = NF + Q*parked.  At a
    parked point this makes the combined Jacobian row spaces identical,
    even though the prime-specific Q traces are not shipped.  Thus the
    pristine source Jacobian supplies the otherwise-lost parked-coordinate
    columns without changing the combined mod-p rank.
    """
    full_point = {name: int(value) % p
                  for name, value in certificate["point"]["full_184"].items()}
    graph_point = certificate["point"]["graph_156"]
    parked_point = certificate["point"]["parked_28"]
    variables = sorted(full_point)
    source_index = {label: index for index, label in enumerate(source_labels)}

    def source_label(name):
        if name == "Xf_alpha":
            return ("X", "alpha")
        if name == "Xg_beta":
            return ("X", "beta")
        if name in ("uW1", "uW2"):
            return None
        semantic = F.X2T.get(name, name)
        if semantic in FIXED_COORDS:
            return ("FIX", semantic)
        family, level = semantic.rsplit("_", 1)
        return family, int(level) - 32

    coordinate_labels = [source_label(name) for name in variables]
    assert len({label for label in coordinate_labels if label is not None}) \
        == 182
    assert all(label is None or label in source_index
               for label in coordinate_labels)
    graph_matrix = [
        [0 if label is None else row[source_index[label]]
         for label in coordinate_labels]
        for row in source_matrix
    ]

    parked_names, parked_prime, parked_rows = NF.parse_ms(
        os.path.join(HERE, "d25fam_p%d_a00pp.ms" % p))
    assert parked_prime == p and len(parked_rows) == 34
    parked_position = {name: index for index, name in enumerate(parked_names)}
    parked_matrix = []
    for row in parked_rows:
        gradient = []
        for variable in variables:
            if variable not in parked_position:
                gradient.append(0)
                continue
            index = parked_position[variable]
            total = 0
            for monomial, coefficient in row.items():
                exponent = monomial[index]
                if not exponent:
                    continue
                value = coefficient * exponent % p
                for j, power in enumerate(monomial):
                    reduced = power - (1 if j == index else 0)
                    if reduced:
                        value = value * pow(
                            full_point[parked_names[j]], reduced, p) % p
                total = (total + value) % p
            gradient.append(total)
        parked_matrix.append(gradient)

    graph_indices = [index for index, name in enumerate(variables)
                     if name in graph_point]
    parked_indices = [index for index, name in enumerate(variables)
                      if name in parked_point]
    parked_rank = NF.matrix_rank(parked_matrix, p)
    graph_external_rank = NF.matrix_rank(
        [[row[index] for index in graph_indices] for row in graph_matrix], p)
    source_rank = NF.matrix_rank(graph_matrix, p)
    combined_rank = NF.matrix_rank(parked_matrix + graph_matrix, p)
    assert parked_rank == 14
    assert graph_external_rank == 111
    assert combined_rank >= parked_rank + graph_external_rank
    combined = parked_matrix + graph_matrix
    row_names = (["parked:%d" % index for index in range(34)] +
                 ["source:band%d:eta%d" % (X.S30[a] + 6 * j, a)
                  for a, j in X.ROWS_CANON])
    work = [[value % p for value in row] for row in combined]
    row_ids = list(range(len(work)))
    pivot_rows = []
    pivot_columns = []
    rank_cursor = 0
    for column in range(len(variables)):
        pivot = next((index for index in range(rank_cursor, len(work))
                      if work[index][column]), None)
        if pivot is None:
            continue
        work[rank_cursor], work[pivot] = work[pivot], work[rank_cursor]
        row_ids[rank_cursor], row_ids[pivot] = row_ids[pivot], row_ids[rank_cursor]
        inverse = pow(work[rank_cursor][column], -1, p)
        work[rank_cursor] = [value * inverse % p
                             for value in work[rank_cursor]]
        for index in range(rank_cursor + 1, len(work)):
            if work[index][column]:
                scale = work[index][column]
                work[index] = [(left - scale * right) % p
                               for left, right in zip(work[index],
                                                      work[rank_cursor])]
        pivot_rows.append(row_ids[rank_cursor])
        pivot_columns.append(column)
        rank_cursor += 1
    assert rank_cursor == combined_rank
    minor = [[combined[row][column] % p for column in pivot_columns]
             for row in pivot_rows]
    determinant = 1
    for column in range(combined_rank):
        pivot = next(index for index in range(column, combined_rank)
                     if minor[index][column])
        if pivot != column:
            minor[column], minor[pivot] = minor[pivot], minor[column]
            determinant = -determinant
        pivot_value = minor[column][column] % p
        determinant = determinant * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for index in range(column + 1, combined_rank):
            if minor[index][column]:
                scale = minor[index][column] * inverse % p
                minor[index] = [(left - scale * right) % p
                                for left, right in zip(minor[index],
                                                       minor[column])]
    determinant %= p
    assert determinant
    return {
        "rows": 218,
        "variables": 184,
        "parked_rank": parked_rank,
        "graph_external_rank": graph_external_rank,
        "block_lower_bound": parked_rank + graph_external_rank,
        "pristine_rows_rank_in_184_coordinates": source_rank,
        "full_combined_rank": combined_rank,
        "zariski_tangent_dimension": 184 - combined_rank,
        "parked_coordinate_columns": len(parked_indices),
        "graph_coordinate_columns": len(graph_indices),
        "justification": ("raw = NF + Q*parked over F_p, so adjoining the "
                          "parked Jacobian makes the raw and banked-NF "
                          "combined row spaces equal at the point"),
        "unit_minor": {
            "size": combined_rank,
            "determinant_mod_p": determinant,
            "equations": [row_names[index] for index in pivot_rows],
            "variables": [variables[index] for index in pivot_columns],
            "matrix_sha256": sha256_json(combined),
            "status": "NONZERO JACOBIAN MINOR ONLY; localized generation and flatness not certified",
        },
    }


def run(p, certificate_path, bank_path, out_path):
    assert p == PRIME, "the bounded lane is fixed at p=105337"
    certificate = json.load(open(certificate_path))
    assert int(certificate["prime"]) == p
    parked = certificate["point"]["parked_28"]
    external = certificate["point"]["graph_156"]
    point, env, alpha, beta, _provenance, _diag = GW.build_operator_point(
        p, parked, external)
    assert alpha == beta == 0
    coefficient_data = coefficient_lifts(p, env)
    modulus = p * p
    integral_point = {
        "tails": {family: {int(r): int(value)
                            for r, value in point["tails"][family].items()}
                  for family in FAMS},
        "fixed": {name: int(value) for name, value in point["fixed"].items()},
    }
    integral_point["fixed"].update({
        "A1": coefficient_data["A1"], "A2": coefficient_data["A2"],
        "r3": coefficient_data["r3"], "h32": coefficient_data["h32"],
        "HW1": coefficient_data["h32"] * point["fixed"]["W1"] % modulus,
        "HW2": coefficient_data["h32"] * point["fixed"]["W2"] % modulus,
    })
    values_p2 = source_rows(
        integral_point, coefficient_data["zeta42"], modulus)
    assert all(value % p == 0 for value in values_p2)
    rhs = [(-value // p) % p for value in values_p2]
    root_point = FC.radical_point(p)
    source_values_p = source_rows(point, root_point["z"], p)
    certified_euler, _certified_aux = X.build_operator(
        point, p, 0, 0,
        Z=[pow(root_point["z"], exponent, p) for exponent in range(42)])
    certified_values_p = [
        int(certified_euler.V[a][X.S30[a] + 6 * j]) % p
        for a, j in X.ROWS_CANON]
    assert source_values_p == certified_values_p == [0] * 184
    negative_point = {
        "tails": {family: dict(point["tails"][family]) for family in FAMS},
        "fixed": dict(point["fixed"]),
    }
    negative_point["tails"]["tf1"][25] = (
        negative_point["tails"]["tf1"].get(25, 0) + 1) % p
    negative_source = source_rows(negative_point, root_point["z"], p)
    negative_euler, _negative_aux = X.build_operator(
        negative_point, p, 0, 0,
        Z=[pow(root_point["z"], exponent, p) for exponent in range(42)])
    negative_certified = [
        int(negative_euler.V[a][X.S30[a] + 6 * j]) % p
        for a, j in X.ROWS_CANON]
    assert negative_source == negative_certified
    assert any(negative_source)
    jacobian, labels, engine_hash = source_jacobian(point, p)
    jacobian_label_index = {label: index for index, label in enumerate(labels)}
    fixed_difference_columns = {}
    for name in FIXED_COORDS:
        shifted = {
            "tails": {family: dict(integral_point["tails"][family])
                      for family in FAMS},
            "fixed": dict(integral_point["fixed"]),
        }
        shifted["fixed"][name] = (shifted["fixed"][name] + p) % modulus
        if name in ("W1", "W2"):
            shifted["fixed"]["HW" + name[-1]] = (
                coefficient_data["h32"] * shifted["fixed"][name]) % modulus
        shifted_values = source_rows(
            shifted, coefficient_data["zeta42"], modulus)
        finite_difference = [((left - right) % modulus) // p % p
                             for left, right in zip(shifted_values, values_p2)]
        column = jacobian_label_index[("FIX", name)]
        assert finite_difference == [row[column] for row in jacobian]
        fixed_difference_columns[name] = sha256_json(finite_difference)
    solution, rank, pivots = solve_rectangular(jacobian, rhs, p)
    augmented_rank = NF.matrix_rank(
        [row + [value] for row, value in zip(jacobian, rhs)], p)
    assert rank == NF.matrix_rank(jacobian, p)
    solvable = solution is not None
    replay = None
    if solvable:
        lifted_point = apply_correction(
            point, labels, solution, p, coefficient_data)
        replay_values = source_rows(
            lifted_point, coefficient_data["zeta42"], modulus)
        assert not any(replay_values)
        replay = {
            "all_184_source_rows_zero_mod_p2": True,
            "nonzero_correction_coordinates": sum(bool(x) for x in solution),
            "correction_sha256": sha256_json(solution),
        }

    label_index = {label: index for index, label in enumerate(labels)}
    restricted_labels = [
        label for label in labels if label not in MISSING_RECONSTRUCTED_TAILS]
    restricted_columns = [label_index[label] for label in restricted_labels]
    restricted_matrix = [[row[index] for index in restricted_columns]
                         for row in jacobian]
    restricted_solution, restricted_rank, _restricted_pivots = \
        solve_rectangular(restricted_matrix, rhs, p)
    restricted_augmented_rank = NF.matrix_rank(
        [row + [value] for row, value in zip(restricted_matrix, rhs)], p)
    restricted_replay = None
    if restricted_solution is not None:
        lifted_point = apply_correction(
            point, restricted_labels, restricted_solution, p,
            coefficient_data)
        replay_values = source_rows(
            lifted_point, coefficient_data["zeta42"], modulus)
        assert not any(replay_values)
        restricted_replay = {
            "all_184_source_rows_zero_mod_p2": True,
            "nonzero_correction_coordinates":
                sum(bool(value) for value in restricted_solution),
            "correction_sha256": sha256_json(restricted_solution),
        }

    tail_x_labels = [label for label in labels
                     if label[0] in FAMS or label[0] == "X"]
    tail_x_columns = [label_index[label] for label in tail_x_labels]
    tail_x_matrix = [[row[index] for index in tail_x_columns]
                     for row in jacobian]
    tail_x_rank = NF.matrix_rank(tail_x_matrix, p)
    full_rank = assembled_special_fiber_rank(
        p, certificate, jacobian, labels)

    missing_checkpoints = []
    audit_report = json.load(open(certificate["certificate"]["audit_report"]))
    for rung in audit_report["rungs"].values():
        path = rung["checkpoint"]
        if not os.path.exists(path):
            missing_checkpoints.append(path)
    missing_checkpoints = sorted(set(missing_checkpoints))

    report = {
        "status": "EXACT SOURCE-MODEL p^2 SCREEN; ASSEMBLED LIFT OPEN",
        "prime": p,
        "modulus": modulus,
        "fiber": "a00pp",
        "scope": "residue-A, B=84, D43, banked full witness",
        "coefficient_ring": {
            "kind": "the Hensel-selected Z_p embedding of the integral radical algebra",
            "roots_mod_p2": coefficient_data,
            "note": "coefficient radicals are simple-root Hensel lifts, not integer representatives of modular roots",
        },
        "source_model": {
            "equations": 184,
            "coordinates": 190,
            "coordinate_blocks": {
                "tail_coordinates": 180,
                "fixed_source_coordinates": list(FIXED_COORDS),
                "x_side_coordinates": ["alpha", "beta"],
            },
            "valuation_e2_sha256": engine_hash,
            "values_mod_p2_nonzero_quotients": sum(bool(value) for value in rhs),
            "minus_F_over_p_sha256": sha256_json(rhs),
            "jacobian_rank": rank,
            "augmented_rank": augmented_rank,
            "correction_solvable": solvable,
            "pivot_columns": [str(labels[index]) for index in pivots],
            "p2_replay": replay,
        },
        "rank_slices": {
            "canonical_182_tail_plus_x_columns_rank": tail_x_rank,
            "all_190_source_columns_rank": rank,
            "represented_182_columns_after_dropping_8_reconstructed_tails": {
                "dropped": [str(label) for label in MISSING_RECONSTRUCTED_TAILS],
                "rank": restricted_rank,
                "augmented_rank": restricted_augmented_rank,
                "correction_solvable": restricted_solution is not None,
                "p2_replay": restricted_replay,
            },
        },
        "assembled_special_fiber_jacobian": full_rank,
        "local_dimension": {
            "status": "NOT CERTIFIED",
            "zariski_tangent_dimension":
                full_rank["zariski_tangent_dimension"],
            "warning": "Tangent dimension is only an upper bound for local Krull dimension. The fixed-parked point has nine identically zero band-10 graph rows, and no localized standard basis / height certificate completed.",
        },
        "available_reduction_audit": available_reduction_audit(
            p, bank_path, certificate),
        "source_evaluator_regression": {
            "banked_point_rows_exact": "184/184",
            "all_180_tail_jacobian_columns_exact": True,
            "all_8_fixed_jacobian_columns_p2_finite_difference_exact": True,
            "fixed_column_hashes": fixed_difference_columns,
            "negative_control": {
                "coordinate": "tf1_57",
                "nonzero_rows": sum(bool(value) for value in negative_source),
                "values_sha256": sha256_json(negative_source),
                "matches_configured_banked_engine": True,
            },
        },
        "assembled_218_model_gate": {
            "status": "NOT CERTIFIED",
            "reason": "The shipped 184-row point bank has already evaluated all parked coordinates. The 19 prime-specific NF checkpoints named by the audit, their integral source-to-NF traces, and a common integral 34-row parked emission are absent. Hence F(x1)/p, the full parked-coordinate Jacobian columns, integral syzygies, local dimension, localized generation, and p-flatness of the 218-row presentation cannot be reconstructed from the shipped artifacts.",
            "missing_prime_specific_nf_checkpoints": missing_checkpoints,
            "forbidden_shortcut": "lifting reduced coefficients or W-root residues as arbitrary integers would define a different Z_p scheme",
        },
        "conclusion": {
            "source_point_reaches_p2": bool(solvable),
            "assembled_218_point_reaches_p2": None,
            "characteristic_zero_D43_point": None,
            "stage_2_cleared": False,
        },
        "inputs": {
            "certificate": certificate_path,
            "certificate_sha256": sha256_path(certificate_path),
            "pointbank": bank_path,
            "pointbank_sha256": sha256_path(bank_path),
        },
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 p-adic source screen p=%d: rank %d/%d, correction %s; "
          "assembled-218 certification OPEN -> %s" %
          (p, rank, augmented_rank, "SOLVABLE" if solvable else "OBSTRUCTED",
           out_path), flush=True)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=PRIME)
    parser.add_argument("--certificate",
                        default=os.path.join(HERE,
                                             "d43_full_certificate_p105337.json"))
    parser.add_argument("--bank",
                        default=os.path.join(HERE,
                                             "d43_full_pointbank_p105337.pkl"))
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    run(args.prime, args.certificate, args.bank, args.out)


if __name__ == "__main__":
    main()
