#!/usr/bin/env python3
"""Regenerate and replay D43 source-to-D23-NF membership traces.

Input is the pristine symbolic mod-p bank produced by build_tails_modp.py,
the shipped 509-element D23 Groebner basis, and the recovered per-band NF
checkpoints.  For every base coefficient of every one of the 184 graph rows,
this tool recomputes

    raw = normal_form + sum(trace[g] * G[g])

in F_p[22 base variables], reconstructs both sides exactly, and compares the
normal forms dictionary-for-dictionary with the recovered checkpoint.  The
full traces are deterministically replayable from the three hashed inputs;
the JSON stores canonical per-row and aggregate trace digests rather than a
second multi-gigabyte copy.

This certifies modular source-to-NF membership.  It is not, by itself, an
integral or p-adic lift of the 34 parked generators.
"""

import argparse
import hashlib
import json
import multiprocessing
import os
import pickle
import sys
import time


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_reduce as DR
import d43_reduce as RED
import d43_reduce_modp as RM


RAW = None
GB = None
CHECKPOINT = None
CLASSIFICATION = None
PRIME = None


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def add(target, monomial, coefficient, p):
    value = (target.get(monomial, 0) + coefficient) % p
    if value:
        target[monomial] = value
    else:
        target.pop(monomial, None)


def grouped_raw(poly, classification, p):
    groups = {}
    dropped = 0
    for monomial, coefficient in poly.items():
        exponents = [0] * DR.NV
        deep = []
        drop = False
        for variable_id, exponent in monomial:
            kind, value = classification[variable_id]
            if kind == "base":
                exponents[value] += exponent
            elif kind == "deep":
                deep.extend([value] * exponent)
            else:
                drop = True
                break
        if drop:
            dropped += 1
            continue
        key = tuple(sorted(deep))
        target = groups.setdefault(key, {})
        add(target, DR.pack(exponents), coefficient, p)
        if not target:
            groups.pop(key, None)
    return groups, dropped


def reconstruct(nf, trace, gb, p):
    result = dict(nf)
    for basis_index, quotients in trace.items():
        leading, _degree, tail = gb[basis_index]
        for quotient, coefficient in quotients.items():
            add(result, quotient + leading, coefficient, p)
            for monomial, _term_degree, tail_coefficient in tail:
                add(result, quotient + monomial,
                    coefficient * tail_coefficient, p)
    return result


def trace_digest(trace):
    digest = hashlib.sha256()
    terms = 0
    for basis_index in sorted(trace):
        for quotient, coefficient in sorted(trace[basis_index].items()):
            digest.update(("%d:%d:%d\n" %
                           (basis_index, quotient, coefficient)).encode())
            terms += 1
    return digest.hexdigest(), terms


def reduce_row(label):
    h, band = label
    p = PRIME
    source = RAW["byk"][band][h]
    groups, dropped = grouped_raw(source, CLASSIFICATION, p)
    expected = CHECKPOINT["rows"][(h, band)]
    actual = {}
    row_digest = hashlib.sha256()
    input_terms = output_terms = trace_terms = steps = 0
    for deep in sorted(groups):
        poly = groups[deep]
        nf, trace, count = DR.nf_trace(poly, GB, p)
        replay = reconstruct(nf, trace, GB, p)
        if replay != poly:
            raise AssertionError(("membership replay", band, h, deep,
                                  len(poly), len(replay)))
        if nf:
            actual[deep] = nf
        digest, count_trace = trace_digest(trace)
        row_digest.update((repr(deep) + ":" + digest + "\n").encode())
        input_terms += len(poly)
        output_terms += len(nf)
        trace_terms += count_trace
        steps += count
    if actual != expected:
        missing = set(expected) - set(actual)
        extra = set(actual) - set(expected)
        differing = [deep for deep in set(actual) & set(expected)
                     if actual[deep] != expected[deep]]
        raise AssertionError(("checkpoint mismatch", band, h,
                              len(missing), len(extra), len(differing)))
    return {
        "band": band, "eta": h,
        "raw_terms_after_grouping": input_terms,
        "pin42_terms_dropped": dropped,
        "nf_terms": output_terms,
        "nf_groups": len(actual),
        "trace_quotient_terms": trace_terms,
        "division_steps": steps,
        "trace_sha256": row_digest.hexdigest(),
        "membership_identity": "PASS",
        "checkpoint_dictionary_match": "PASS",
    }


def run(raw_path, gb_path, checkpoint_dir, out_path, workers):
    global RAW, GB, CHECKPOINT, CLASSIFICATION, PRIME
    started = time.time()
    with open(raw_path, "rb") as handle:
        RAW = pickle.load(handle)
    p = int(RAW["prime"])
    PRIME = p
    assert RAW["fiber"] == "a00pp" and int(RAW["D"]) == 43
    CLASSIFICATION = RM.classify(RAW["vars"])
    GB = RED.parse_msolve_gb(gb_path, p)
    bands = sorted(int(band) for band in RAW["byk"])
    assert bands == list(range(6, 43, 2))
    reports = []
    context = multiprocessing.get_context("fork")
    for band in bands:
        checkpoint_path = os.path.join(
            checkpoint_dir,
            "d43red_p%d_a00pp_band%d.pkl" % (p, band))
        with open(checkpoint_path, "rb") as handle:
            CHECKPOINT = pickle.load(handle)
        assert int(CHECKPOINT["prime"]) == p
        assert int(CHECKPOINT["band"]) == band
        labels = sorted(CHECKPOINT["rows"])
        # Fork after loading the current checkpoint: raw bank, GB, and the
        # read-only expected rows are copy-on-write shared with workers.
        if workers == 1 or len(labels) == 1:
            current = [reduce_row(label) for label in labels]
        else:
            with context.Pool(min(workers, len(labels))) as pool:
                current = list(pool.imap_unordered(
                    reduce_row, labels, chunksize=1))
        current.sort(key=lambda item: item["eta"])
        reports.extend(current)
        print("band %d: %d rows, raw %d -> NF %d terms, trace %d terms PASS" %
              (band, len(current),
               sum(item["raw_terms_after_grouping"] for item in current),
               sum(item["nf_terms"] for item in current),
               sum(item["trace_quotient_terms"] for item in current)),
              flush=True)
        CHECKPOINT = None

    aggregate = hashlib.sha256()
    for report in reports:
        aggregate.update(("%d:%d:%s\n" %
                          (report["band"], report["eta"],
                           report["trace_sha256"])).encode())
    checkpoint_hashes = {
        str(band): sha256_path(os.path.join(
            checkpoint_dir,
            "d43red_p%d_a00pp_band%d.pkl" % (p, band)))
        for band in bands
    }
    result = {
        "status": "EXACT MOD-p SOURCE-TO-NF TRACE REPLAY",
        "prime": p,
        "fiber": "a00pp",
        "rows": len(reports),
        "bands": bands,
        "raw_terms_after_grouping": sum(
            item["raw_terms_after_grouping"] for item in reports),
        "pin42_terms_dropped": sum(
            item["pin42_terms_dropped"] for item in reports),
        "nf_terms": sum(item["nf_terms"] for item in reports),
        "trace_quotient_terms": sum(
            item["trace_quotient_terms"] for item in reports),
        "division_steps": sum(item["division_steps"] for item in reports),
        "membership_identities_replayed": "%d/%d" %
            (len(reports), len(reports)),
        "checkpoint_rows_dictionary_exact": "%d/%d" %
            (len(reports), len(reports)),
        "aggregate_trace_sha256": aggregate.hexdigest(),
        "row_reports": reports,
        "inputs": {
            "raw_bank": raw_path,
            "raw_bank_sha256": sha256_path(raw_path),
            "groebner_basis": gb_path,
            "groebner_basis_sha256": sha256_path(gb_path),
            "checkpoint_directory": checkpoint_dir,
            "checkpoint_sha256_by_band": checkpoint_hashes,
        },
        "boundary":
            "These are identities over F_p against the D23 GB. They do not supply integral parked generators or integral/p-adic source-to-parked traces.",
        "seconds": round(time.time() - started, 3),
    }
    with open(out_path, "w") as handle:
        json.dump(result, handle, indent=1, sort_keys=True)
        handle.write("\n")
    assert len(reports) == 184
    print("D43 p=%d: 184/184 raw=NF+trace*G and checkpoint exact -> %s" %
          (p, out_path), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True)
    parser.add_argument("--gb", required=True)
    parser.add_argument("--ckdir", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    run(args.raw, args.gb, args.ckdir, args.out, args.workers)


if __name__ == "__main__":
    main()
