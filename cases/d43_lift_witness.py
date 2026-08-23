#!/usr/bin/env python3
"""Lift a compressed D43 compatibility witness through the rung graphs.

INTERNAL / UNREVIEWED.  The 52 compatibility rows eliminate the ten
first-occurrence columns separately at each rung.  This gate checks the
load-bearing reverse direction: after back-solving a rung and substituting
those reconstructed values into every later rung, does the witness remain
compatible?  Only a point passing through rung 42 is a D43 survivor input.
"""

import argparse
import json
import os
import pickle
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_reduce as DR
import d43_family2 as F
import d43_nf_certificate as NF


def solve_rectangular(A, rhs, p):
    """RREF solve A*x=rhs with nonpivot coordinates fixed to zero."""
    nr = len(A)
    nc = len(A[0]) if nr else 0
    work = [[x % p for x in row] + [value % p]
            for row, value in zip(A, rhs)]
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
    inconsistent = any(not any(row[:nc]) and row[nc] for row in work)
    if inconsistent:
        return None, rank, pivots
    solution = [0] * nc
    for i, col in enumerate(pivots):
        solution[col] = work[i][nc]
    return solution, rank, pivots


def evaluate(poly, assignment, p):
    value = 0
    for mono, coeff in poly.items():
        term = coeff
        for name in mono:
            term = term * assignment.get(name, 0) % p
        value = (value + term) % p
    return value


def lift(ckdir, witness_path, out_path):
    witness = json.load(open(witness_path))
    p = int(witness["prime"])
    cell_values = {name: int(value) % p
                   for name, value in witness["parked_point"].items()}
    assignment = {name: int(value) % p
                  for name, value in witness["external_point"].items()}
    base_values = [cell_values[name] for name in DR.GBVARS]
    transcript = []
    status = "LIFTED"
    for k in range(26, 43, 2):
        path = os.path.join(ckdir,
                            "d43red_p%d_a00pp_band%d.pkl" % (p, k))
        with open(path, "rb") as fh:
            bank = pickle.load(fh)
        grouped = {h: groups for (h, _s), groups in bank["rows"].items()}
        _hs, ynames, rows, _C, _L, expected_rank = NF.rung_kernel(
            grouped, k, p)
        evaluated = [NF.eval_group_row(row, base_values, cell_values, p,
                                       F.T2X, DR.unpack) for row in rows]
        mapped_y = [F.T2X.get(name, name) for name in ynames]
        if k == 42:
            mapped_y += ["Xf_alpha", "Xg_beta"]
        selected_order = sorted(mapped_y)
        A, b = NF.affine_numeric(evaluated, set(mapped_y), assignment, p)
        before = [evaluate(row, assignment, p) for row in evaluated]
        rank_A = NF.matrix_rank(A, p)
        rank_aug = NF.matrix_rank([row + [(-value) % p]
                                   for row, value in zip(A, b)], p)
        solution, solve_rank, pivots = solve_rectangular(
            A, [(-value) % p for value in b], p)
        record = {
            "rung": k,
            "rows": len(rows),
            "unknowns": selected_order,
            "expected_rank": expected_rank,
            "rank_A": rank_A,
            "rank_augmented": rank_aug,
            "compressed_assignment_raw_nonzero_rows":
                sum(value != 0 for value in before),
        }
        assert rank_A == solve_rank == expected_rank
        if solution is None:
            record["verdict"] = "INCONSISTENT_AFTER_PRIOR_RECONSTRUCTION"
            transcript.append(record)
            status = "NONLIFTING_COMPRESSED_WITNESS"
            break
        old_values = {name: assignment.get(name, 0)
                      for name in selected_order}
        assignment.update(zip(selected_order, solution))
        replay = [evaluate(row, assignment, p) for row in evaluated]
        assert replay == [0] * len(rows)
        changed = {name: {"compressed": old_values[name],
                          "reconstructed": assignment[name]}
                   for name in selected_order
                   if old_values[name] != assignment[name]}
        record.update({
            "verdict": "SOLVED",
            "pivot_variables": [selected_order[j] for j in pivots],
            "changed_from_compressed_assignment": changed,
            "replay_zero_rows": len(rows),
        })
        transcript.append(record)

    result = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "compressed_witness": witness_path,
        "lift_status": status,
        "rungs": transcript,
    }
    if status == "LIFTED":
        result["alpha"] = assignment["Xf_alpha"]
        result["beta"] = assignment["Xg_beta"]
        result["lifted_assignment"] = assignment
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 COMPRESSED-WITNESS LIFT p=%d: %s through %d/%d rungs"
          % (p, status, len(transcript), 9))
    for record in transcript:
        print("  rung %d rank %d/%d raw-nz %d -> %s"
              % (record["rung"], record["rank_A"],
                 record["rank_augmented"],
                 record["compressed_assignment_raw_nonzero_rows"],
                 record["verdict"]))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckdir", required=True)
    parser.add_argument("--witness", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    lift(args.ckdir, args.witness, args.out)


if __name__ == "__main__":
    main()
