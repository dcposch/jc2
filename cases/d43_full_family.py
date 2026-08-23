#!/usr/bin/env python3
"""Fully reconstructed residue-A D43 family, exact modulo p.

INTERNAL / UNREVIEWED.  This driver restores the 95 pristine graph rows
in bands 6..24 which are absent from the 34-row parked D25 quotient, and
joins them to the 89 pristine graph rows in bands 26..42.  The resulting
audit ideal is

    34 parked rows + 95 old graph rows + 89 late graph rows.

The 52 banked late compatibility rows are exact left-kernel combinations
of the late graph rows and are audit redundancies, not additional
generators.  No full expanded D43 file is passed to a solver here.

The reduced band checkpoints contain rows as

    sum_deep deep_monomial * NF_det23(base_coefficient).

This representation supports a small exact-slice route without emitting
the multi-gigabyte expanded family.  ``--point-slice`` fixes one certified
parked A^14 point, keeps every genuine graph coordinate, and emits all 184
graph rows after exact coefficient evaluation.  It is a witness-search
slice only: emptiness of that slice is not family emptiness.
"""

import argparse
import hashlib
import json
import os
import pickle
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_reduce as DR
import d43_family2 as F
import d43_nf_certificate as NF


PRIMES = (105337, 105673)
OLD_BANDS = tuple(range(6, 25, 2))
LATE_BANDS = tuple(range(26, 43, 2))
ALL_BANDS = OLD_BANDS + LATE_BANDS
OLD_SIZES = (9, 10, 9, 9, 10, 10, 9, 10, 10, 9)
LATE_SIZES = (10, 10, 9, 10, 10, 10, 10, 10, 10)
CELL_NAMES = set(NF.FREE + NF.DEP + NF.FIXED)


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def checkpoint_path(ckdir, p, band):
    return os.path.join(
        ckdir, "d43red_p%d_a00pp_band%d.pkl" % (p, band))


def load_rung(ckdir, p, band):
    path = checkpoint_path(ckdir, p, band)
    with open(path, "rb") as fh:
        bank = pickle.load(fh)
    assert int(bank["prime"]) == p
    assert int(bank["band"]) == band
    assert bank["fiber"] == "a00pp"
    assert tuple(bank["gbvars"]) == tuple(DR.GBVARS)
    grouped = {h: groups for (h, s), groups in bank["rows"].items()
               if int(s) == band}
    hs, ynames, rows, C, L, rank = NF.rung_kernel(grouped, band, p)
    return {
        "path": path, "sha256": sha256_path(path), "band": band,
        "etas": hs, "ynames": ynames, "rows": rows,
        "C": C, "left_kernel": L, "rank_C": rank,
    }


def mapped_deep(deep):
    if "uf30" in deep:
        return None
    return tuple(sorted(F.T2X.get(name, name) for name in deep))


def add_grouped(dst, src, scale, p):
    scale %= p
    if not scale:
        return
    for deep, base in src.items():
        target = dst.setdefault(deep, {})
        for packed, coeff in base.items():
            value = (target.get(packed, 0) + scale * coeff) % p
            if value:
                target[packed] = value
            else:
                target.pop(packed, None)
        if not target:
            dst.pop(deep, None)


def serialize_grouped(groups, p):
    """Canonical expanded text used by d43_graph_family.py."""
    mapped = {}
    for deep, base in groups.items():
        deep2 = mapped_deep(deep)
        if deep2 is None:
            continue
        for packed, coeff in base.items():
            key = packed, deep2
            value = (mapped.get(key, 0) + coeff) % p
            if value:
                mapped[key] = value
            else:
                mapped.pop(key, None)
    terms = []
    for (packed, deep), coeff in sorted(mapped.items()):
        term = str(coeff)
        for name, exponent in zip(DR.GBVARS, DR.unpack(packed)):
            if exponent:
                term += "*" + name
                if exponent > 1:
                    term += "^%d" % exponent
        for name in deep:
            term += "*" + name
        terms.append(term)
    return "+".join(terms) if terms else "0"


def cell_from_values(root, p, free_values):
    replay_path = os.path.join(root, "d25_certificate_replay.json")
    record = json.load(open(replay_path))["parked_fibers"][str(p)]["a00pp"]
    W1 = int(record["derived_witness"]["W1"])
    W2 = int(record["derived_witness"]["W2"])
    parked = os.path.join(root, "d25fam_p%d_a00pp.ms" % p)
    cell = NF.build_cell_map(parked, replay_path, W1, W2)
    free_values = tuple(int(x) % p for x in free_values)
    assert len(free_values) == len(NF.FREE)
    values = dict(zip(NF.FREE, free_values))
    values.update(cell["fixed"])
    for name, poly in cell["maps"].items():
        values[name] = NF.eval_free_poly(poly, free_values, p)
    assert set(DR.GBVARS) <= set(values)
    return cell, values


def evaluated_row(groups, base_values, cell_values, p):
    """Exact checkpoint row at one parked point, graph vars retained."""
    return NF.eval_group_row(groups, base_values, cell_values, p,
                             F.T2X, DR.unpack)


def eval_row(row, assignment, p):
    total = 0
    for mono, coeff in row.items():
        value = coeff
        for name in mono:
            value = value * assignment[name] % p
        total = (total + value) % p
    return total


def row_degree(row):
    return max((len(mono) for mono in row), default=0)


def pivot_columns(matrix, p):
    """Column indices of the canonical left-to-right row-echelon pivots."""
    work = [[int(x) % p for x in row] for row in matrix]
    nr = len(work)
    nc = len(work[0]) if nr else 0
    rank = 0
    pivots = []
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], p - 2, p)
        work[rank] = [x * inv % p for x in work[rank]]
        for i in range(nr):
            if i != rank and work[i][col]:
                scale = work[i][col]
                work[i] = [(x - scale * y) % p
                           for x, y in zip(work[i], work[rank])]
        pivots.append(col)
        rank += 1
        if rank == nr:
            break
    return pivots


def parse_linear_gb(path, p):
    """Parse a completely linear msolve -g 2 basis as one F_p point."""
    text = open(path).read()
    match = re.search(r"#variable order:\s*(.+)\n", text)
    assert match, "missing msolve variable order"
    order = [name.strip() for name in match.group(1).split(",")]
    match = re.search(r"\[([^\]]*)\]:\s*$", text, re.S)
    assert match, "missing printed Groebner basis"
    polynomials = [item.strip() for item in match.group(1).split(",")
                   if item.strip()]
    assert len(polynomials) == len(order), (len(polynomials), len(order))
    pattern = re.compile(r"1\*([A-Za-z0-9_]+)\^1(?:\+([0-9]+))?$")
    solved = {}
    for polynomial in polynomials:
        parsed = pattern.fullmatch(polynomial)
        assert parsed, ("nonlinear GB element", polynomial)
        name, constant = parsed.groups()
        assert name in order and name not in solved
        solved[name] = (-int(constant or 0)) % p
    assert set(solved) == set(order)
    return order, solved


def jacobian_at(rows, variables, assignment, p):
    matrix = []
    for row in rows:
        gradient = []
        for variable in variables:
            total = 0
            for mono, coeff in row.items():
                multiplicity = mono.count(variable)
                if not multiplicity:
                    continue
                value = coeff * multiplicity % p
                removed = False
                for name in mono:
                    if name == variable and not removed:
                        removed = True
                    else:
                        value = value * assignment[name] % p
                total = (total + value) % p
            gradient.append(total)
        matrix.append(gradient)
    return matrix


def exponent_jacobian_rank(rows, names, assignment, p):
    """Jacobian rank for parse_ms rows keyed by exponent tuples."""
    matrix = []
    for row in rows:
        gradient = []
        for index, variable in enumerate(names):
            total = 0
            for mono, coeff in row.items():
                exponent = mono[index]
                if not exponent:
                    continue
                value = coeff * exponent % p
                for j, power in enumerate(mono):
                    reduced = power - (1 if j == index else 0)
                    if reduced:
                        value = value * pow(assignment[names[j]], reduced,
                                            p) % p
                total = (total + value) % p
            gradient.append(total)
        matrix.append(gradient)
    return NF.matrix_rank(matrix, p)


def restrict_row(row, keep, assignment, p):
    """Set variables outside ``keep`` to the supplied exact scalars."""
    result = {}
    for mono, coeff in row.items():
        retained = []
        value = coeff
        for name in mono:
            if name in keep:
                retained.append(name)
            else:
                value = value * assignment[name] % p
        if not value:
            continue
        key = tuple(sorted(retained))
        value = (result.get(key, 0) + value) % p
        if value:
            result[key] = value
        else:
            result.pop(key, None)
    return result


def audit(ckdir, root, p):
    expected = dict(zip(OLD_BANDS, OLD_SIZES))
    expected.update(dict(zip(LATE_BANDS, LATE_SIZES)))
    old_hash = hashlib.sha256()
    late_hash = hashlib.sha256()
    late_compat_hash = hashlib.sha256()
    external = set()
    rungs = {}
    nold = nlate = ncompat = 0
    for band in ALL_BANDS:
        rung = load_rung(ckdir, p, band)
        assert len(rung["rows"]) == expected[band]
        assert len(rung["etas"]) == expected[band]
        row_terms = []
        for row in rung["rows"]:
            text = serialize_grouped(row, p)
            digest = old_hash if band <= 24 else late_hash
            digest.update(text.encode("ascii"))
            digest.update(b"\n")
            for deep in row:
                deep2 = mapped_deep(deep)
                if deep2 is not None:
                    external.update(name for name in deep2
                                    if name not in CELL_NAMES)
            row_terms.append(sum(len(base) for deep, base in row.items()
                                 if "uf30" not in deep))
        if band <= 24:
            nold += len(rung["rows"])
        else:
            nlate += len(rung["rows"])
            for vector in rung["left_kernel"]:
                combination = {}
                for scale, row in zip(vector, rung["rows"]):
                    add_grouped(combination, row, scale, p)
                text = serialize_grouped(combination, p)
                late_compat_hash.update(text.encode("ascii"))
                late_compat_hash.update(b"\n")
                ncompat += 1
        rungs[str(band)] = {
            "rows": len(rung["rows"]),
            "rank_C": rung["rank_C"],
            "left_kernel_rows": len(rung["left_kernel"]),
            "expanded_terms": row_terms,
            "checkpoint": rung["path"],
            "checkpoint_sha256": rung["sha256"],
        }
    assert (nold, nlate, ncompat) == (95, 89, 52)

    emission_path = os.path.join(root,
                                 "d43_graph_emission_p%d.json" % p)
    emission = json.load(open(emission_path))
    late_expected = emission["graph_rows_sha256"]
    compat_expected = emission["compatibility_rows_sha256"]
    assert late_hash.hexdigest() == late_expected
    assert late_compat_hash.hexdigest() == compat_expected

    parked = os.path.join(root, "d25fam_p%d_a00pp.ms" % p)
    parked_names, parked_prime, parked_rows = NF.parse_ms(parked)
    assert parked_prime == p and len(parked_rows) == 34
    assert set(parked_names) == CELL_NAMES
    parked_expected = emission["sources"]["parked_sha256"]
    assert sha256_path(parked) == parked_expected

    # Every external name plus the 28 parked names is the corrected
    # 184-coordinate union header from the previous graph audit.
    assert len(external) == 156, (len(external), sorted(external))
    assert len(external | CELL_NAMES) == 184
    report = {
        "status": "INTERNAL / UNREVIEWED / MOD-p",
        "prime": p, "fiber": "a00pp",
        "scope": "residue-A, B=84 frozen, no-log, PIN42, W1W2 != 0",
        "ideal": {
            "variables": 184,
            "rows": 218,
            "row_blocks": {"parked": 34, "old_graph_bands_6_24": 95,
                           "late_graph_bands_26_42": 89},
            "late_compatibility_audit_redundancies": 52,
            "rows_if_redundancies_retained": 270,
        },
        "gates": {
            "parked_rows": "34/34",
            "old_graph_rows": "95/95",
            "late_graph_rows": "89/89",
            "late_graph_byte_regression": "PASS",
            "late_compatibility_from_graph_byte_regression": "PASS",
            "union_variable_census": "184/184",
        },
        "hashes": {
            "parked_source_sha256": parked_expected,
            "old_graph_rows_sha256": old_hash.hexdigest(),
            "late_graph_rows_sha256": late_hash.hexdigest(),
            "late_compatibility_rows_sha256": late_compat_hash.hexdigest(),
        },
        "external_variables": sorted(external),
        "rungs": rungs,
    }
    return report


def point_slice(ckdir, root, p, free_values, out_prefix):
    cell, cell_values = cell_from_values(root, p, free_values)
    base_values = [cell_values[name] for name in DR.GBVARS]
    rows = []
    row_labels = []
    rung_reports = {}
    for band in ALL_BANDS:
        rung = load_rung(ckdir, p, band)
        evaluated = [evaluated_row(row, base_values, cell_values, p)
                     for row in rung["rows"]]
        rows.extend(evaluated)
        row_labels.extend([[band, eta] for eta in rung["etas"]])
        rung_reports[str(band)] = {
            "rows": len(evaluated), "rank_C": rung["rank_C"],
            "terms": [len(row) for row in evaluated],
            "degrees": [row_degree(row) for row in evaluated],
        }
    assert len(rows) == 184
    variables = sorted({name for row in rows for mono in row for name in mono})
    assert len(variables) == 156, (len(variables), variables)
    ms_path = out_prefix + "_p%d.ms" % p
    NF.emit_external_ms(ms_path, variables, rows, p)
    payload_path = out_prefix + "_p%d.pkl" % p
    with open(payload_path, "wb") as fh:
        pickle.dump({"status": "INTERNAL / UNREVIEWED / MOD-p",
                     "prime": p, "fiber": "a00pp",
                     "free_values": dict(zip(NF.FREE, free_values)),
                     "cell_values": cell_values, "variables": variables,
                     "row_labels": row_labels, "rows": rows},
                    fh, protocol=4)
    constants = [row.get((), 0) for row in rows]
    jacobian0 = [[row.get((name,), 0) for name in variables]
                 for row in rows]
    rank = NF.matrix_rank(jacobian0, p)
    rank_aug = NF.matrix_rank(
        [row + [constant] for row, constant in zip(jacobian0, constants)], p)
    pivots = pivot_columns(jacobian0, p)
    assert len(pivots) == rank
    pivot_variables = [variables[j] for j in pivots]
    pivot_set = set(pivot_variables)
    pivot_rows = [{mono: coeff for mono, coeff in row.items()
                   if all(name in pivot_set for name in mono)}
                  for row in rows]
    pivot_path = out_prefix + "_pivot_p%d.ms" % p
    NF.emit_external_ms(pivot_path, pivot_variables, pivot_rows, p)
    prefix_slices = {}
    for last_band in ALL_BANDS:
        count = sum(1 for band, _eta in row_labels if band <= last_band)
        current = rows[:count]
        current_variables = sorted({name for row in current
                                    for mono in row for name in mono})
        current_jacobian = [
            [row.get((name,), 0) for name in current_variables]
            for row in current]
        current_pivots = pivot_columns(current_jacobian, p)
        current_keep = [current_variables[j] for j in current_pivots]
        current_set = set(current_keep)
        restricted = [{mono: coeff for mono, coeff in row.items()
                       if all(name in current_set for name in mono)}
                      for row in current]
        current_path = out_prefix + "_upto%d_pivot_p%d.ms" % (last_band, p)
        NF.emit_external_ms(current_path, current_keep, restricted, p)
        prefix_slices[str(last_band)] = {
            "rows": len(restricted), "full_variables": len(current_variables),
            "variables": len(current_keep), "terms": sum(map(len, restricted)),
            "max_degree": max(map(row_degree, restricted)),
            "variables_retained": current_keep,
            "msolve_input": current_path,
            "msolve_input_sha256": sha256_path(current_path),
        }
    report = {
        "status": "INTERNAL / UNREVIEWED / MOD-p",
        "prime": p, "fiber": "a00pp",
        "meaning": "exact fixed-A14-point slice of all 184 pristine graph rows; slice emptiness is not family emptiness",
        "free_values": dict(zip(NF.FREE, free_values)),
        "W1": cell["W1"], "W2": cell["W2"],
        "rows": 184, "old_graph_rows": 95, "late_graph_rows": 89,
        "variables": len(variables), "terms": sum(map(len, rows)),
        "max_degree": max(map(row_degree, rows)),
        "origin_rank": rank, "origin_augmented_rank": rank_aug,
        "nonzero_constants": sum(bool(x) for x in constants),
        "msolve_input": ms_path, "msolve_input_sha256": sha256_path(ms_path),
        "origin_pivot_slice": {
            "meaning": "canonical origin-Jacobian pivot variables retained; all other graph coordinates set to zero; witness-search only",
            "rows": len(pivot_rows), "variables": len(pivot_variables),
            "terms": sum(map(len, pivot_rows)),
            "max_degree": max(map(row_degree, pivot_rows)),
            "variables_retained": pivot_variables,
            "msolve_input": pivot_path,
            "msolve_input_sha256": sha256_path(pivot_path),
        },
        "origin_pivot_prefix_slices": prefix_slices,
        "pickle": payload_path, "rungs": rung_reports,
    }
    report_path = out_prefix + "_p%d.json" % p
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    return report


def continuation_slice(bank_path, center_gb, last_band, out_prefix):
    """Extend a verified linear exact-slice point to one deeper prefix.

    The center GB supplies values for its retained coordinates; all other
    graph coordinates are zero.  A canonical Jacobian-pivot slice at that
    center fixes nonpivot coordinates to their center values.  A solution
    of the emitted system is a point of the *unsliced* prefix because every
    pristine prefix row is retained and later replayed.
    """
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    assignment = {name: 0 for name in bank["variables"]}
    center_order, center = parse_linear_gb(center_gb, p)
    assert set(center_order) <= set(assignment)
    assignment.update(center)
    rows = [row for row, label in zip(bank["rows"], bank["row_labels"])
            if int(label[0]) <= last_band]
    labels = [label for label in bank["row_labels"]
              if int(label[0]) <= last_band]
    variables = sorted({name for row in rows for mono in row for name in mono})
    center_values = [eval_row(row, assignment, p) for row in rows]
    solved_through = None
    for band in ALL_BANDS:
        if band > last_band:
            break
        indices = [i for i, label in enumerate(labels) if label[0] <= band]
        if all(center_values[i] == 0 for i in indices):
            solved_through = band
        else:
            break
    jacobian = jacobian_at(rows, variables, assignment, p)
    pivots = pivot_columns(jacobian, p)
    keep = [variables[j] for j in pivots]
    keep_set = set(keep)
    restricted = [restrict_row(row, keep_set, assignment, p) for row in rows]
    ms_path = out_prefix + "_p%d.ms" % p
    NF.emit_external_ms(ms_path, keep, restricted, p)
    report = {
        "status": "INTERNAL / UNREVIEWED / MOD-p",
        "prime": p, "fiber": "a00pp", "last_band": last_band,
        "meaning": "exact continuation witness-search slice; all pristine prefix rows retained; slice emptiness is not family emptiness",
        "source_bank": bank_path, "source_bank_sha256": sha256_path(bank_path),
        "center_gb": center_gb, "center_gb_sha256": sha256_path(center_gb),
        "center_variables": len(center),
        "center_nonzero_coordinates": sum(bool(x) for x in center.values()),
        "center_solves_through_band": solved_through,
        "center_nonzero_rows_in_target_prefix": sum(bool(x) for x in center_values),
        "rows": len(rows), "full_variables": len(variables),
        "jacobian_rank_at_center": len(pivots),
        "variables": len(keep), "variables_retained": keep,
        "terms": sum(map(len, restricted)),
        "max_degree": max(map(row_degree, restricted)),
        "msolve_input": ms_path, "msolve_input_sha256": sha256_path(ms_path),
    }
    report_path = out_prefix + "_p%d.json" % p
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    return report


def verify_linear_witness(bank_path, gb_path, last_band, out_path):
    """Replay a completely linear slice GB against every pristine row."""
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    order, solved = parse_linear_gb(gb_path, p)
    assignment = {name: 0 for name in bank["variables"]}
    assignment.update(solved)
    indices = [i for i, label in enumerate(bank["row_labels"])
               if int(label[0]) <= last_band]
    values = [eval_row(bank["rows"][i], assignment, p) for i in indices]
    report = {
        "status": "INTERNAL / UNREVIEWED / MOD-p",
        "prime": p, "fiber": "a00pp", "last_band": last_band,
        "source_bank": bank_path, "source_bank_sha256": sha256_path(bank_path),
        "linear_gb": gb_path, "linear_gb_sha256": sha256_path(gb_path),
        "variables_in_gb": len(order),
        "nonzero_coordinates": sum(bool(x) for x in solved.values()),
        "rows_replayed": len(values),
        "rows_zero": sum(value == 0 for value in values),
        "nonzero_rows": [{"index": indices[j],
                          "label": bank["row_labels"][indices[j]],
                          "value": value}
                         for j, value in enumerate(values) if value],
        "result": "PASS" if not any(values) else "FAIL",
        "point": {name: assignment[name] for name in sorted(assignment)},
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    assert not any(values), report["nonzero_rows"][:5]
    return report


def final_certificate(bank_path, gb_path, parked_path, audit_path,
                      out_path, floor_path):
    """Decode and replay a NONEMPTY certificate through the full gate."""
    import d43_graph_witness as GW

    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    order, solved = parse_linear_gb(gb_path, p)
    external = {name: 0 for name in bank["variables"]}
    external.update(solved)
    assert set(order) <= set(external)
    assert len(external) == 156
    graph_values = [eval_row(row, external, p) for row in bank["rows"]]
    assert len(graph_values) == 184 and not any(graph_values)
    rows_zero_by_band = {
        str(band): sum(value == 0 for value, label in
                       zip(graph_values, bank["row_labels"])
                       if int(label[0]) == band)
        for band in ALL_BANDS
    }

    parked_point = {name: int(value) % p
                    for name, value in bank["cell_values"].items()}
    parked_names, parked_prime, parked_rows = NF.parse_ms(parked_path)
    assert parked_prime == p and len(parked_rows) == 34
    parked_values = [NF.eval_named_poly(row, parked_names, parked_point, p)
                     for row in parked_rows]
    assert not any(parked_values)
    assert not (set(parked_point) & set(external))
    full_point = dict(parked_point)
    full_point.update(external)
    assert len(full_point) == 184

    graph_rank = GW.jacobian_rank(bank["rows"], bank["variables"],
                                  external, p)
    parked_rank = exponent_jacobian_rank(parked_rows, parked_names,
                                         parked_point, p)
    control_name = next(name for name in order if external[name])
    changed = dict(external)
    changed[control_name] = (changed[control_name] + 1) % p
    broken = sum(eval_row(row, changed, p) != 0 for row in bank["rows"])
    assert broken > 0

    floor = GW.floor_gate(p, parked_point, external)
    assert floor["checks_all_pass"]
    assert floor["selected_residual_nonzero_count"] == 0
    assert floor["nu_window"] is None
    with open(floor_path, "w") as fh:
        json.dump(floor, fh, indent=1, sort_keys=True)
        fh.write("\n")

    audit = json.load(open(audit_path)) if audit_path else None
    if audit is not None:
        assert int(audit["prime"]) == p
        assert audit["ideal"]["rows"] == 218
        assert audit["ideal"]["variables"] == 184
    slice_stem = os.path.splitext(gb_path)[0]
    slice_input = slice_stem + ".ms"
    slice_report = slice_stem + ".json"
    report = {
        "status": "INTERNAL / UNREVIEWED / MOD-p",
        "verdict": "NONEMPTY",
        "prime": p, "fiber": "a00pp",
        "scope": "residue-A, B=84 frozen, no-log, PIN42, W1W2 != 0",
        "ideal": {"variables": 184, "rows": 218,
                  "row_blocks": {"parked": 34,
                                 "old_graph_bands_6_24": 95,
                                 "late_graph_bands_26_42": 89}},
        "certificate": {
            "kind": "exact-slice linear-GB witness plus full unsliced replay",
            "slice_input": slice_input if os.path.exists(slice_input) else None,
            "slice_input_sha256":
                sha256_path(slice_input) if os.path.exists(slice_input) else None,
            "slice_report":
                slice_report if os.path.exists(slice_report) else None,
            "slice_gb": gb_path, "slice_gb_sha256": sha256_path(gb_path),
            "linear_gb_elements": len(order),
            "linear_gb_nonzero_coordinates":
                sum(bool(value) for value in solved.values()),
            "source_bank": bank_path,
            "source_bank_sha256": sha256_path(bank_path),
            "audit_report": audit_path,
        },
        "replay": {
            "parked_rows_zero": sum(value == 0 for value in parked_values),
            "old_graph_rows_zero":
                sum(value == 0 for value in graph_values[:95]),
            "late_graph_rows_zero":
                sum(value == 0 for value in graph_values[95:]),
            "graph_rows_zero_by_band": rows_zero_by_band,
            "all_218_rows_zero": bool(not any(parked_values + graph_values)),
            "fixed_parked_point_jacobian_rank": parked_rank,
            "graph_fiber_jacobian_rank": graph_rank,
            "negative_control": {
                "perturbed_coordinate": control_name,
                "nonzero_graph_rows": broken,
            },
        },
        "survivor_gate": {
            "floor_report": floor_path,
            "checks_all_pass": floor["checks_all_pass"],
            "failed_checks": floor["failed_checks"],
            "selected_residual_nonzero_count":
                floor["selected_residual_nonzero_count"],
            "nu_window": floor["nu_window"],
            "floor_eligible": floor["floor_eligible"],
            "ell_lower_bound": floor["ell_lb_certified"],
            "e_plus": floor["e_plus"],
        },
        "point": {"parked_28": parked_point, "graph_156": external,
                  "full_184": full_point},
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    return report


def parse_free(spec):
    if spec == "zero":
        return [0] * len(NF.FREE)
    if spec == "sequence":
        return list(range(1, len(NF.FREE) + 1))
    values = [int(x) for x in spec.split(",") if x]
    if len(values) != len(NF.FREE):
        raise ValueError("--free requires zero, sequence, or 14 integers")
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckdir")
    parser.add_argument("--root", default=HERE)
    parser.add_argument("--prime", type=int, choices=PRIMES)
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--point-slice", action="store_true")
    parser.add_argument("--continuation-slice", action="store_true")
    parser.add_argument("--verify-linear-witness", action="store_true")
    parser.add_argument("--final-certificate", action="store_true")
    parser.add_argument("--bank")
    parser.add_argument("--center-gb")
    parser.add_argument("--last-band", type=int)
    parser.add_argument("--parked")
    parser.add_argument("--audit-report")
    parser.add_argument("--floor-out")
    parser.add_argument("--free", default="zero")
    parser.add_argument("--out", required=True,
                        help="audit JSON path, or point-slice prefix")
    args = parser.parse_args()
    modes = (args.audit, args.point_slice, args.continuation_slice,
             args.verify_linear_witness, args.final_certificate)
    if sum(bool(x) for x in modes) != 1:
        parser.error("select exactly one execution mode")
    if args.audit:
        if not args.ckdir or not args.prime:
            parser.error("audit requires --ckdir and --prime")
        report = audit(args.ckdir, args.root, args.prime)
        with open(args.out, "w") as fh:
            json.dump(report, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print("D43 FULL AUDIT p=%d: PASS 34+95+89=218 -> %s" %
              (args.prime, args.out), flush=True)
    elif args.point_slice:
        if not args.ckdir or not args.prime:
            parser.error("point slice requires --ckdir and --prime")
        report = point_slice(args.ckdir, args.root, args.prime,
                             parse_free(args.free), args.out)
        print("D43 FULL POINT SLICE p=%d: 184x156, %d terms, degree <= %d" %
              (args.prime, report["terms"], report["max_degree"]),
              flush=True)
    elif args.continuation_slice:
        if not args.bank or not args.center_gb or args.last_band is None:
            parser.error("continuation requires --bank --center-gb --last-band")
        report = continuation_slice(args.bank, args.center_gb,
                                    args.last_band, args.out)
        print("D43 FULL CONTINUATION p=%d through %d: %d rows x %d pivots" %
              (report["prime"], args.last_band, report["rows"],
               report["variables"]), flush=True)
    elif args.verify_linear_witness:
        if not args.bank or not args.center_gb or args.last_band is None:
            parser.error("verification requires --bank --center-gb --last-band")
        report = verify_linear_witness(args.bank, args.center_gb,
                                       args.last_band, args.out)
        print("D43 FULL LINEAR WITNESS p=%d: PASS %d/%d through band %d" %
              (report["prime"], report["rows_zero"], report["rows_replayed"],
               args.last_band), flush=True)
    else:
        if not all((args.bank, args.center_gb, args.parked, args.floor_out)):
            parser.error("final certificate requires --bank --center-gb --parked --floor-out")
        report = final_certificate(args.bank, args.center_gb, args.parked,
                                   args.audit_report, args.out,
                                   args.floor_out)
        print("D43 FULL p=%d: NONEMPTY; PASS 34+95+89 and survivor gate; ell+ >= %d" %
              (report["prime"], report["survivor_gate"]["ell_lower_bound"]),
              flush=True)


if __name__ == "__main__":
    main()
