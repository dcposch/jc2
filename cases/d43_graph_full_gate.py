#!/usr/bin/env python3
"""Streaming replay of a 175-row graph-preserving D43 emission.

INTERNAL / UNREVIEWED.  This parser is independent of the emitters and
evaluates the expanded msolve text directly at a banked 184-coordinate
point.
"""

import argparse
import hashlib
import json


def evaluate_term(term, assignment, p):
    factors = term.split("*")
    try:
        value = int(factors[0]) % p
        factors = factors[1:]
    except ValueError:
        value = 1
    for factor in factors:
        if "^" in factor:
            name, exponent = factor.split("^", 1)
            exponent = int(exponent)
        else:
            name, exponent = factor, 1
        value = value * pow(assignment[name], exponent, p) % p
    return value


def gate(ms_path, witness_path, out_path):
    witness = json.load(open(witness_path))
    p = int(witness["prime"])
    assignment = {name: int(value) % p
                  for name, value in witness["point"]["full_184"].items()}
    digest = hashlib.sha256()
    values = []
    terms_per_row = []
    with open(ms_path, "rb") as raw:
        header_raw = raw.readline()
        prime_raw = raw.readline()
        digest.update(header_raw)
        digest.update(prime_raw)
        variables = [name.strip() for name in header_raw.decode().split(",")]
        assert len(variables) == len(set(variables)) == 184
        assert set(variables) == set(assignment)
        assert int(prime_raw) == p
        for row_index, raw_line in enumerate(raw):
            digest.update(raw_line)
            line = raw_line.decode().strip().rstrip(",")
            if not line:
                continue
            value = 0
            nterms = 0
            for term in line.split("+"):
                value = (value + evaluate_term(term, assignment, p)) % p
                nterms += 1
            values.append(value)
            terms_per_row.append(nterms)
            print("row %d: value=%d terms=%d" %
                  (row_index, value, nterms), flush=True)
    assert len(values) == 175
    assert values == [0] * 175, [(i, value) for i, value in enumerate(values)
                                 if value]
    report = {
        "status": "INTERNAL / UNREVIEWED",
        "result": "PASS", "prime": p, "fiber": "a00pp",
        "source": ms_path, "source_sha256": digest.hexdigest(),
        "witness": witness_path, "variables": 184, "rows": 175,
        "parked_rows_zero": sum(value == 0 for value in values[:34]),
        "compatibility_rows_zero":
            sum(value == 0 for value in values[34:86]),
        "graph_rows_zero": sum(value == 0 for value in values[86:]),
        "total_terms_replayed": sum(terms_per_row),
        "term_counts": terms_per_row,
    }
    with open(out_path, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 GRAPH FULL GATE p=%d: PASS 175/175 (%d terms)" %
          (p, sum(terms_per_row)), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ms", required=True)
    parser.add_argument("--witness", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    gate(args.ms, args.witness, args.out)


if __name__ == "__main__":
    main()
