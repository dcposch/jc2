#!/usr/bin/env python3
"""Streaming witness replay for the original 1 GB D43 verdict emission.

INTERNAL / UNREVIEWED.  The input format is the campaign's expanded,
plus-only msolve format.  This gate intentionally parses the original
86-row file rather than importing either D43 emitter or NF reducer.
"""

import argparse
import hashlib
import json


def eval_term(term, assignment, p):
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
                  for name, value in witness["full_172_point"].items()}
    digest = hashlib.sha256()
    values = []
    term_counts = []
    with open(ms_path, "rb") as raw:
        header_raw = raw.readline()
        prime_raw = raw.readline()
        digest.update(header_raw)
        digest.update(prime_raw)
        names = [name.strip() for name in header_raw.decode().split(",")]
        assert len(names) == len(set(names)) == 172
        assert set(names) == set(assignment)
        assert int(prime_raw) == p
        for row_index, line_raw in enumerate(raw):
            digest.update(line_raw)
            text = line_raw.decode().strip().rstrip(",")
            if not text:
                continue
            total = 0
            terms = 0
            for term in text.split("+"):
                total = (total + eval_term(term, assignment, p)) % p
                terms += 1
            values.append(total)
            term_counts.append(terms)
            print("row %d: value=%d terms=%d" %
                  (row_index, total, terms), flush=True)
    assert len(values) == 86
    assert values == [0] * 86, [(i, x) for i, x in enumerate(values) if x]
    result = {
        "status": "INTERNAL / UNREVIEWED",
        "prime": p,
        "fiber": "a00pp",
        "source_verdict": ms_path,
        "source_sha256": digest.hexdigest(),
        "witness": witness_path,
        "variables": len(names),
        "rows": len(values),
        "parked_rows_zero": sum(value == 0 for value in values[:34]),
        "compatibility_rows_zero": sum(value == 0 for value in values[34:]),
        "total_terms_replayed": sum(term_counts),
        "term_counts": term_counts,
        "result": "PASS",
    }
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("D43 ORIGINAL VERDICT WITNESS GATE p=%d: PASS 86/86 (%d terms)"
          % (p, sum(term_counts)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ms", required=True)
    parser.add_argument("--witness", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    gate(args.ms, args.witness, args.out)


if __name__ == "__main__":
    main()
