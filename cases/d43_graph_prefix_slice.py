#!/usr/bin/env python3
"""Emit a small square slice of a graph-preserving D43 prefix.

INTERNAL / UNREVIEWED.  This is a NONEMPTY witness route only: the parked
A^14 coordinates are fixed at a certified point, Jacobian pivot graph
variables are retained, and every other graph variable is set to zero.
"""

import argparse
import hashlib
import json
import os
import pickle
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d43_nf_certificate as NF
import d43_raw_point_system as RAW


RUNGS = tuple(range(26, 43, 2))
RUNG_SIZES = (10, 10, 9, 10, 10, 10, 10, 10, 10)


def emit(bank_path, rung, out_prefix):
    with open(bank_path, "rb") as fh:
        bank = pickle.load(fh)
    p = int(bank["prime"])
    nrows = sum(size for k, size in zip(RUNGS, RUNG_SIZES) if k <= rung)
    rows = bank["rows"][:nrows]
    used = sorted({name for row in rows for mono in row for name in mono})
    jacobian0 = [[row.get((name,), 0) for name in used] for row in rows]
    pivots = RAW.pivot_columns(jacobian0, p)
    assert len(pivots) == len(rows)
    keep = [used[index] for index in pivots]
    keep_set = set(keep)
    restricted = [{mono: coeff for mono, coeff in row.items()
                   if all(name in keep_set for name in mono)}
                  for row in rows]
    assert {name for row in restricted for mono in row for name in mono} == \
        keep_set
    ms_path = "%s_p%d_upto%d.ms" % (out_prefix, p, rung)
    NF.emit_external_ms(ms_path, keep, restricted, p)
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p, "fiber": "a00pp", "last_rung": rung,
        "meaning": "fixed certified parked point; omitted graph coordinates=0",
        "source_bank": bank_path,
        "rows": len(rows), "full_prefix_variables": len(used),
        "slice_variables": len(keep),
        "slice_terms": sum(map(len, restricted)),
        "slice_max_degree": max(max(map(len, row), default=0)
                                for row in restricted),
        "origin_jacobian_rank": NF.matrix_rank(jacobian0, p),
        "msolve_input": ms_path,
        "msolve_input_sha256": hashlib.sha256(
            open(ms_path, "rb").read()).hexdigest(),
        "variables_kept": keep,
    }
    report_path = "%s_p%d_upto%d.json" % (out_prefix, p, rung)
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 GRAPH PREFIX SLICE p=%d <=%d: %dx%d, %d terms -> %s" %
          (p, rung, len(rows), len(keep), sum(map(len, restricted)), ms_path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", required=True)
    parser.add_argument("--rung", type=int, choices=RUNGS, required=True)
    parser.add_argument("--out-prefix", required=True)
    args = parser.parse_args()
    emit(args.bank, args.rung, args.out_prefix)


if __name__ == "__main__":
    main()
