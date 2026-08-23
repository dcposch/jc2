#!/usr/bin/env python3
"""Exact parked-cell normal forms of graph-preserving D43 prefixes.

INTERNAL / UNREVIEWED.  This is the certificate/solver route for the true
graph object: split the 34-row parked ideal into its sixteen certified A^14
components, substitute the ten triangular parked pivots exactly, and retain
the pristine rung graph equations.  No D43 completion coordinate is fixed.
"""

import argparse
import hashlib
import itertools
import json
import os
import pickle
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_reduce as DR
import d43_family2 as F
import d43_nf_certificate as NF


def add_external_scaled(dst, src, scale, p):
    scale %= p
    if not scale:
        return
    for mono, coeff in src.items():
        value = (dst.get(mono, 0) + scale * coeff) % p
        if value:
            dst[mono] = value
        else:
            dst.pop(mono, None)


def reduce_group_row(groups, reducer):
    """Substitute one grouped raw row into F_p[free_14, external]."""
    p = reducer.p
    cell_names = set(NF.FREE + NF.DEP)
    result = {}
    for deep, base in groups.items():
        if "uf30" in deep:
            continue
        mapped = tuple(F.T2X.get(name, name) for name in deep)
        internal = tuple(name for name in mapped if name in cell_names)
        external = tuple(sorted(name for name in mapped
                                if name not in cell_names))
        base_nf = reducer.base_polynomial(base)
        if not base_nf:
            continue
        if internal:
            base_nf = NF.poly_mul(base_nf, reducer.cell_pattern(internal),
                                  p)
        for exponents, coeff in base_nf.items():
            names = list(external)
            for name, exponent in zip(NF.FREE, exponents):
                names.extend([name] * exponent)
            mono = tuple(sorted(names))
            value = (result.get(mono, 0) + coeff) % p
            if value:
                result[mono] = value
            else:
                result.pop(mono, None)
    return result


def jacobian_rank(rows, variables, assignment, p):
    matrix = []
    for row in rows:
        gradient = []
        for variable in variables:
            value = 0
            for mono, coeff in row.items():
                multiplicity = mono.count(variable)
                if not multiplicity:
                    continue
                term = coeff * multiplicity % p
                removed = False
                for name in mono:
                    if name == variable and not removed:
                        removed = True
                    else:
                        term = term * assignment[name] % p
                value = (value + term) % p
            gradient.append(value)
        matrix.append(gradient)
    return NF.matrix_rank(matrix, p)


def emit_cell(root, ckdir, p, prefix, cell_index, out_prefix):
    replay_path = os.path.join(root, "d25_certificate_replay.json")
    replay = json.load(open(replay_path))["parked_fibers"][str(p)]["a00pp"]
    hint = replay["derived_witness"]
    roots1 = NF.fourth_roots(p, int(replay["W1^4"]), int(hint["W1"]))
    roots2 = NF.fourth_roots(p, int(replay["W2^4"]), int(hint["W2"]))
    cells = list(itertools.product(roots1, roots2))
    assert 0 <= cell_index < len(cells)
    W1, W2 = cells[cell_index]
    parked = os.path.join(root, "d25fam_p%d_a00pp.ms" % p)
    cell = NF.build_cell_map(parked, replay_path, W1, W2)
    reducer = NF.CellReducer(cell, DR.GBVARS, DR.unpack, p)

    rows = []
    rung_report = {}
    compat_count = 0
    negative_control = None
    for k in range(26, prefix + 1, 2):
        path = os.path.join(ckdir,
                            "d43red_p%d_a00pp_band%d.pkl" % (p, k))
        with open(path, "rb") as fh:
            bank = pickle.load(fh)
        grouped = {h: groups for (h, _s), groups in bank["rows"].items()}
        _hs, ynames, raw_groups, _C, L, rank = NF.rung_kernel(grouped, k, p)
        reduced = [reduce_group_row(row, reducer) for row in raw_groups]
        selected = {F.T2X.get(name, name) for name in ynames}
        if k == 42:
            selected.update(("Xf_alpha", "Xg_beta"))
        compat_terms = []
        for li, vector in enumerate(L):
            combination = {}
            for scale, row in zip(vector, reduced):
                add_external_scaled(combination, row, scale, p)
            assert not any(name in selected for mono in combination
                           for name in mono), (k, li)
            compat_terms.append(len(combination))
            compat_count += 1
            if negative_control is None:
                hit = next(i for i, value in enumerate(vector) if value)
                bad = [dict(row) for row in reduced]
                mono = next(iter(bad[hit]))
                bad[hit][mono] = (bad[hit][mono] + 1) % p
                bad_combination = {}
                for scale, row in zip(vector, bad):
                    add_external_scaled(bad_combination, row, scale, p)
                assert bad_combination != combination
                negative_control = {"rung": k, "compat_row": li,
                                    "raw_row": hit,
                                    "result": "PERTURBATION_DETECTED"}
        rows.extend(reduced)
        rung_report[str(k)] = {
            "rows": len(reduced), "rank_C": rank,
            "compat_rows_derived": len(L),
            "row_terms": [len(row) for row in reduced],
            "compat_terms": compat_terms,
        }

    variables = list(NF.FREE)
    variables += sorted({name for row in rows for mono in row for name in mono}
                        - set(variables))
    assignment0 = {name: 0 for name in variables}
    assignment1 = {name: i + 1 for i, name in enumerate(variables)}
    ms_path = "%s_p%d_cell%02d_upto%d.ms" % (out_prefix, p, cell_index,
                                               prefix)
    NF.emit_external_ms(ms_path, variables, rows, p)
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p, "fiber": "a00pp", "cell": cell_index,
        "W1": W1, "W2": W2, "prefix": prefix,
        "meaning": "parked-cell exact NF; all D43 graph variables retained",
        "parked_quotient": {"free": list(NF.FREE),
                            "reconstructed": list(NF.DEP),
                            "parked_identities": "34/34"},
        "rows": len(rows), "variables": len(variables),
        "terms": sum(map(len, rows)),
        "max_degree": max(max(map(len, row), default=0) for row in rows),
        "compat_rows_exactly_derived": compat_count,
        "jacobian_rank": {
            "origin": jacobian_rank(rows, variables, assignment0, p),
            "sequence": jacobian_rank(rows, variables, assignment1, p),
        },
        "negative_control": negative_control,
        "rungs": rung_report,
        "msolve_input": ms_path,
        "msolve_input_sha256": hashlib.sha256(open(ms_path, "rb").read()).hexdigest(),
    }
    report_path = "%s_p%d_cell%02d_upto%d.json" % (out_prefix, p,
                                                     cell_index, prefix)
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 GRAPH NF p=%d cell=%02d <=%d: %d rows, %d vars, %d terms -> %s"
          % (p, cell_index, prefix, len(rows), len(variables),
             sum(map(len, rows)), ms_path), flush=True)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=HERE)
    parser.add_argument("--ckdir", required=True)
    parser.add_argument("--prime", type=int, choices=NF.PRIMES, required=True)
    parser.add_argument("--prefix", type=int, choices=range(26, 43, 2),
                        required=True)
    parser.add_argument("--cell", type=int, choices=range(16), required=True)
    parser.add_argument("--out-prefix", required=True)
    args = parser.parse_args()
    emit_cell(args.root, args.ckdir, args.prime, args.prefix, args.cell,
              args.out_prefix)


if __name__ == "__main__":
    main()
