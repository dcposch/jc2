#!/usr/bin/env python3
"""Independent stdlib replay of the banked full-cell linear certificates."""

import argparse
import hashlib
import json
import os
import subprocess
import tempfile


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
P = 105337


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def rref(matrix, p=P):
    M = [[int(x) % p for x in row] for row in matrix]
    pivots = []
    row = 0
    for column in range(len(M[0]) if M else 0):
        pivot = next((i for i in range(row, len(M)) if M[i][column]), None)
        if pivot is None:
            continue
        M[row], M[pivot] = M[pivot], M[row]
        inverse = pow(M[row][column], p - 2, p)
        M[row] = [x * inverse % p for x in M[row]]
        for i in range(len(M)):
            if i != row and M[i][column]:
                multiple = M[i][column]
                M[i] = [(x - multiple * y) % p
                        for x, y in zip(M[i], M[row])]
        pivots.append(column)
        row += 1
        if row == len(M):
            break
    return M, pivots


def rank(matrix, p=P):
    return len(rref(matrix, p)[1])


def matvec(A, x, p=P):
    return [sum(a * b for a, b in zip(row, x)) % p for row in A]


def transpose(A):
    return [list(row) for row in zip(*A)]


def determinant(A, p=P):
    M = [[int(x) % p for x in row] for row in A]
    out = 1
    for column in range(len(M)):
        pivot = next((i for i in range(column, len(M))
                      if M[i][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            M[column], M[pivot] = M[pivot], M[column]
            out = -out
        value = M[column][column]
        out = out * value % p
        inverse = pow(value, p - 2, p)
        for i in range(column + 1, len(M)):
            multiple = M[i][column] * inverse % p
            for j in range(column, len(M)):
                M[i][j] = (M[i][j] - multiple * M[column][j]) % p
    return out % p


def check(condition, message, checks):
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def replay(results_path, source_rerun=False):
    data = json.load(open(results_path))
    checks = []
    check(data["verdict"] == "NONEMPTY-SINGULAR-OR-LOWER-RANK",
          "preregistered verdict string", checks)
    check(data["free_coordinate_order"] == [
        "x57", "x59", "x60", "x62", "x63", "x65", "x66",
        "x68", "x72", "x73", "x16", "x19", "x24", "x27"],
          "A14 free-coordinate registry", checks)

    for relative, entry in data["source_manifest"].items():
        path = os.path.join(ROOT, relative)
        check(os.path.getsize(path) == entry["bytes"] and
              sha256(path) == entry["sha256"],
              "manifest hash %s" % relative, checks)

    origin, sequence = data["records"]
    check(origin["A26"] == sequence["A26"],
          "same source coefficient block at registered points", checks)
    check(rank(origin["A26"]) == 4,
          "independent A26 rank four", checks)
    for lam in origin["left_cokernel_basis"]:
        check(not any(matvec(transpose(origin["A26"]), lam)),
              "independent left-cokernel replay", checks)
    check(len(origin["left_cokernel_basis"]) == 6,
          "cokernel dimension six", checks)

    check(origin["compatible"] and
          origin["compatibility_functions"] == [0] * 6,
          "origin is an exact compatibility zero", checks)
    check(not sequence["compatible"] and
          any(sequence["compatibility_functions"]),
          "same-cell sequence point is cut", checks)

    for record, expected_det in ((origin, 39793), (sequence, 104469)):
        J = record["compatibility_jacobian"]
        witness = record["tangent_diagnostics"]["jacobian_rank_minor"]
        check(rank(J) == 5, "%s Jacobian rank five" % record["tag"], checks)
        check(determinant(witness["matrix"]) == expected_det ==
              witness["determinant_mod_p"],
              "%s independent 5x5 determinant" % record["tag"], checks)

    dependency = data["two_point_shared_dependency"]["coefficient_vector"]
    check(dependency == [104372, 48519, 44983, 31248, 84848, 1],
          "shared dependency literal", checks)
    for record in (origin, sequence):
        J = record["compatibility_jacobian"]
        check(not any(matvec(transpose(J), dependency)),
              "%s dependency kills Jacobian" % record["tag"], checks)
        check(sum(a * b for a, b in zip(
            dependency, record["compatibility_functions"])) % P == 0,
              "%s dependency kills values" % record["tag"], checks)

    mutated = origin["compatibility_functions"][:]
    mutated[0] = 1
    check(sum(a * b for a, b in zip(dependency, mutated)) % P != 0,
          "negative control: one-unit function mutation is detected", checks)

    rerun_equal = None
    if source_rerun:
        python = "/opt/homebrew/opt/python@3.14/bin/python3.14"
        tool = os.path.join(HERE, "fullcell_compat.py")
        with tempfile.TemporaryDirectory(prefix="dtransition-fullcell-") as td:
            scratch = os.path.join(td, "results.json")
            subprocess.run([python, tool, "--run", "--out", scratch],
                           cwd=ROOT, check=True)
            rerun_equal = open(scratch, "rb").read() == \
                open(results_path, "rb").read()
        check(rerun_equal, "fresh source rerun is byte-identical", checks)

    return {
        "tool": "cases/round1_dtransition_fullcell/independent_replay.py",
        "results_sha256": sha256(results_path),
        "checks_passed": len(checks),
        "checks": checks,
        "source_rerun_requested": source_rerun,
        "source_rerun_byte_identical": rerun_equal,
        "scope": "linear/provenance replay only; no global rank upper bound",
        "verdict": "PASS",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", default=os.path.join(HERE, "results.json"))
    parser.add_argument("--out", default=os.path.join(HERE, "replay.json"))
    parser.add_argument("--source-rerun", action="store_true")
    args = parser.parse_args()
    result = replay(args.results, args.source_rerun)
    with open(args.out, "w") as f:
        json.dump(result, f, indent=1, sort_keys=True)
        f.write("\n")
    print("PASS independent replay:", result["checks_passed"], "checks")
    print("WROTE:", args.out)


if __name__ == "__main__":
    main()
