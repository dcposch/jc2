#!/usr/bin/env python3
"""Build the graph-preserving D43 rung system at one certified D25 point.

INTERNAL / UNREVIEWED.  Unlike the 52 compatibility-only presentation,
this artifact retains all first-occurrence rung variables and all 89 rung
equations, so a witness lifts directly to the pristine D43 rows.
"""

import argparse
import hashlib
import json
import os
import pickle
import random
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_reduce as DR
import d25_eplus as DE
import d43_family2 as F
import d43_nf_certificate as NF
import eplus43 as X


def pivot_columns(matrix, p):
    work = [[x % p for x in row] for row in matrix]
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


def build(ckdir, witness_path, out_path, reconstructed=False):
    witness = json.load(open(witness_path))
    p = int(witness["prime"])
    cell_values = {name: int(value) % p
                   for name, value in witness["parked_point"].items()}
    reconstruction = None
    if reconstructed:
        env = DE.fiber_env(p, "a00pp")
        dval, d25diag = DE.reconstruct_point(p, cell_values, env)
        wit72, deep = DE.witness72_of(p, dval)
        _point_v2, _E, frontier = X.completed_point_v2(
            p, wit72, deep, env)
        extra = {}
        for label, value in frontier.items():
            family, level = label.rsplit("_", 1)
            extra[(family, int(level) - 32)] = value
        point = X.point43_from_v2(p, wit72, deep, env,
                                  extra_tails=extra)
        for family in X.FAMS:
            for r, value in point["tails"][family].items():
                semantic = "%s_%d" % (family, 32 + int(r))
                mapped = F.T2X.get(semantic, semantic)
                if mapped in cell_values:
                    assert cell_values[mapped] == int(value) % p, \
                        (mapped, cell_values[mapped], value)
                cell_values[mapped] = int(value) % p
        cell_values[F.T2X["uf24"]] = int(
            point["fixed"].get("uf24", 0)) % p
        reconstruction = {
            "method": "d25_eplus.reconstruct_point + completed_point_v2",
            "diag": d25diag,
            "frontier": frontier,
            "specialized_coordinates": sorted(
                set(cell_values) - set(witness["parked_point"])),
        }
    base_values = [cell_values[name] for name in DR.GBVARS]
    rows = []
    rung_sizes = []
    rung_unknowns = {}
    for k in range(26, 43, 2):
        path = os.path.join(ckdir,
                            "d43red_p%d_a00pp_band%d.pkl" % (p, k))
        with open(path, "rb") as fh:
            bank = pickle.load(fh)
        grouped = {h: groups for (h, _s), groups in bank["rows"].items()}
        _hs, ynames, grouped_rows, _C, _L, rank = NF.rung_kernel(
            grouped, k, p)
        evaluated = [NF.eval_group_row(row, base_values, cell_values, p,
                                       F.T2X, DR.unpack)
                     for row in grouped_rows]
        rows.extend(evaluated)
        rung_sizes.append(len(evaluated))
        mapped = [F.T2X.get(name, name) for name in ynames]
        if k == 42:
            mapped += ["Xf_alpha", "Xg_beta"]
        rung_unknowns[str(k)] = {"variables": mapped, "rank": rank}
    variables = sorted({name for row in rows for mono in row for name in mono})
    payload = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "cell": {name: cell_values[name] for name in sorted(cell_values)},
        "d25_reconstruction": reconstruction,
        "rows": rows,
        "variables": variables,
        "rung_sizes": rung_sizes,
        "rung_unknowns": rung_unknowns,
    }
    with open(out_path, "wb") as fh:
        pickle.dump(payload, fh, protocol=4)
    print("D43 RAW POINT SYSTEM p=%d: %d rows, %d vars, %d terms -> %s"
          % (p, len(rows), len(variables), sum(map(len, rows)), out_path))


def emit_slice(bank_path, out_prefix):
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    rows = bank["rows"]
    variables = bank["variables"]
    jacobian0 = [[row.get((name,), 0) for name in variables]
                 for row in rows]
    pivots = pivot_columns(jacobian0, p)
    assert len(pivots) == len(rows) == 89
    keep = [variables[j] for j in pivots]
    keep_set = set(keep)
    restricted = [{mono: coeff for mono, coeff in row.items()
                   if all(name in keep_set for name in mono)}
                  for row in rows]
    used = {name for row in restricted for mono in row for name in mono}
    assert used == keep_set
    degrees = [max(map(len, row), default=0) for row in restricted]
    assert max(degrees) <= 3
    ms_path = "%s_p%d.ms" % (out_prefix, p)
    NF.emit_external_ms(ms_path, keep, restricted, p)
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "meaning": "graph-preserving 89 pristine rung rows at one "
                   "certified D25 point; all 67 omitted coordinates = 0",
        "source_bank": bank_path,
        "source_bank_sha256": hashlib.sha256(
            open(bank_path, "rb").read()).hexdigest(),
        "full_point_system": {"rows": len(rows),
                              "variables": len(variables),
                              "terms": sum(map(len, rows))},
        "origin_jacobian_rank": NF.matrix_rank(jacobian0, p),
        "slice": {"rows": len(restricted), "variables": len(keep),
                  "terms": sum(map(len, restricted)),
                  "max_degree": max(degrees), "variables_kept": keep,
                  "msolve_input": ms_path},
        "gates": {"all_rung_graph_rows_retained": "89/89",
                  "origin_jacobian_full_row_rank": "89/89",
                  "literal_zero_specialization": "PASS"},
    }
    report_path = "%s_p%d.json" % (out_prefix, p)
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 RAW POINT SLICE p=%d: 89x156 -> 89x89, %d terms, "
          "degree <= %d -> %s" %
          (p, sum(map(len, restricted)), max(degrees), ms_path))


def emit_full(bank_path, out_prefix):
    """Emit an already point-specialized raw bank without elimination."""
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    rows = [row for row in bank["rows"] if row]
    variables = bank["variables"]
    used = {name for row in rows for mono in row for name in mono}
    variables = [name for name in variables if name in used]
    ms_path = "%s_p%d.ms" % (out_prefix, p)
    NF.emit_external_ms(ms_path, variables, rows, p)
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "meaning": "graph-preserving raw D43 rung system after exact "
                   "D25 coordinate reconstruction at one certified cell point",
        "source_bank": bank_path,
        "source_bank_sha256": hashlib.sha256(
            open(bank_path, "rb").read()).hexdigest(),
        "rows_before_zero_drop": len(bank["rows"]),
        "zero_rows_dropped": len(bank["rows"]) - len(rows),
        "rows": len(rows),
        "variables": len(variables),
        "terms": sum(map(len, rows)),
        "max_degree": max(max(map(len, row), default=0) for row in rows),
        "msolve_input": ms_path,
        "d25_reconstruction": bank["d25_reconstruction"],
    }
    report_path = "%s_p%d.json" % (out_prefix, p)
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 RECONSTRUCTED FULL p=%d: %d rows, %d vars, %d terms, "
          "degree <= %d -> %s" %
          (p, len(rows), len(variables), sum(map(len, rows)),
           report["max_degree"], ms_path))


def evaluate(row, assignment, p):
    total = 0
    for mono, coeff in row.items():
        value = coeff
        for name in mono:
            value = value * assignment[name] % p
        total = (total + value) % p
    return total


def numeric_gate(bank_path, out_path, trials=2):
    """Compare every raw specialized row to the independent jet engine."""
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    parked_names = set(NF.FREE + NF.DEP + NF.FIXED)
    cell = {name: int(value) % p for name, value in bank["cell"].items()
            if name in parked_names}
    env = DE.fiber_env(p, "a00pp")
    dval, _diag = DE.reconstruct_point(p, cell, env)
    wit72, deep = DE.witness72_of(p, dval)
    _point_v2, _E, frontier = X.completed_point_v2(p, wit72, deep, env)
    extra = {}
    for label, value in frontier.items():
        family, level = label.rsplit("_", 1)
        extra[(family, int(level) - 32)] = value
    base_point = X.point43_from_v2(p, wit72, deep, env,
                                   extra_tails=extra)
    rng = random.Random((p << 16) ^ 0xD43)
    records = []
    for trial in range(trials):
        assignment = {name: rng.randrange(p) for name in bank["variables"]}
        point = dict(base_point)
        point["fixed"] = dict(base_point["fixed"])
        point["tails"] = {family: dict(base_point["tails"][family])
                          for family in X.FAMS}
        alpha = assignment.get("Xf_alpha", 0)
        beta = assignment.get("Xg_beta", 0)
        for name, value in assignment.items():
            semantic = F.X2T.get(name, name)
            if semantic.startswith("X"):
                continue
            if semantic == "uf24":
                point["fixed"]["uf24"] = value
                continue
            family, level = semantic.rsplit("_", 1)
            point["tails"][family][int(level) - 32] = value
        E, _aux = X.build_operator(point, p, alpha, beta)
        want = []
        for k in range(26, 43, 2):
            want.extend(int(E.V[h][k]) % p for h in F.rung_rows_idx(k))
        got = [evaluate(row, assignment, p) for row in bank["rows"]]
        assert got == want, [(i, a, b) for i, (a, b) in
                             enumerate(zip(got, want)) if a != b][:5]
        records.append({"trial": trial, "rows_exact": len(got)})
    # Negative control: one coefficient perturbation must break replay at
    # the last deterministic assignment.
    bad_rows = [dict(row) for row in bank["rows"]]
    row_index = next(i for i, row in enumerate(bad_rows) if row)
    mono = next(iter(bad_rows[row_index]))
    bad_rows[row_index][mono] = (bad_rows[row_index][mono] + 1) % p
    bad = [evaluate(row, assignment, p) for row in bad_rows]
    assert bad[row_index] != want[row_index]
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "source_bank": bank_path,
        "trials": records,
        "total_exact_row_comparisons": trials * len(bank["rows"]),
        "negative_control": {"perturbed_row": row_index,
                             "result": "MISMATCH_DETECTED"},
        "result": "PASS",
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 RAW NUMERIC GATE p=%d: PASS %d/%d; "
          "negative control fired" %
          (p, trials * len(bank["rows"]), trials * len(bank["rows"])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckdir")
    parser.add_argument("--witness")
    parser.add_argument("--out")
    parser.add_argument("--slice-bank")
    parser.add_argument("--emit-full-bank")
    parser.add_argument("--numeric-gate-bank")
    parser.add_argument("--numeric-gate-out")
    parser.add_argument("--reconstructed", action="store_true")
    parser.add_argument("--slice-prefix",
                        default=os.path.join(HERE, "d43_raw_slice"))
    args = parser.parse_args()
    if args.numeric_gate_bank:
        if not args.numeric_gate_out:
            parser.error("--numeric-gate-bank requires --numeric-gate-out")
        numeric_gate(args.numeric_gate_bank, args.numeric_gate_out)
    elif args.emit_full_bank:
        emit_full(args.emit_full_bank, args.slice_prefix)
    elif args.slice_bank:
        emit_slice(args.slice_bank, args.slice_prefix)
    else:
        if not args.ckdir or not args.witness or not args.out:
            parser.error("build mode requires --ckdir, --witness, --out")
        build(args.ckdir, args.witness, args.out,
              reconstructed=args.reconstructed)


if __name__ == "__main__":
    main()
