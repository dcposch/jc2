#!/usr/bin/env python3
"""Emit and audit the graph-preserving D43 a00pp family.

INTERNAL / UNREVIEWED.  The stage-2 D43 verdict files contain the 34
parked D25 equations followed by 52 per-rung compatibility equations.
Those compatibility equations do not retain the reconstruction graph.
This driver appends all 89 pristine rung equations and also emits smaller
equivalent solver prefixes containing the parked rows and graph rows only.

The compatibility rows may be omitted from a solver input only after this
driver has regenerated all 52 as exact constant linear combinations of the
89 graph rows and compared their expanded text byte-for-byte with the
banked verdict source.
"""

import argparse
import hashlib
import json
import os
import pickle
import shutil
import sys
import tempfile


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import d25_reduce as DR
import d43_family2 as F
import d43_nf_certificate as NF


RUNG_SIZES = (10, 10, 9, 10, 10, 10, 10, 10, 10)
COMPAT_SIZES = (6, 6, 5, 6, 6, 6, 6, 6, 5)
RUNGS = tuple(range(26, 43, 2))


def sha256_path(path, limit=None):
    digest = hashlib.sha256()
    remaining = limit
    with open(path, "rb") as fh:
        while remaining is None or remaining:
            size = 8 << 20 if remaining is None else min(8 << 20, remaining)
            block = fh.read(size)
            if not block:
                break
            digest.update(block)
            if remaining is not None:
                remaining -= len(block)
    return digest.hexdigest()


def copy_bytes(source, target, limit=None):
    remaining = limit
    with open(source, "rb") as src:
        while remaining is None or remaining:
            size = 8 << 20 if remaining is None else min(8 << 20, remaining)
            block = src.read(size)
            if not block:
                break
            target.write(block)
            if remaining is not None:
                remaining -= len(block)


def trimmed_size(path):
    size = os.path.getsize(path)
    with open(path, "rb") as fh:
        start = max(0, size - 4096)
        fh.seek(start)
        tail = fh.read()
    return start + len(tail.rstrip(b" \t\r\n"))


def ms_body_offset(path):
    with open(path, "rb") as fh:
        fh.readline()
        fh.readline()
        return fh.tell()


def read_ms_rows(path):
    """Yield the header, prime, then expanded one-line rows."""
    fh = open(path, encoding="ascii")
    header = fh.readline().rstrip("\r\n")
    prime = int(fh.readline().strip())

    def rows():
        try:
            for line in fh:
                row = line.rstrip("\r\n")
                if row.endswith(","):
                    row = row[:-1]
                if row:
                    yield row
        finally:
            fh.close()

    return header, prime, rows()


def add_scaled_base(dst, src, scale, p):
    scale %= p
    if not scale:
        return
    for packed, coeff in src.items():
        value = (dst.get(packed, 0) + scale * coeff) % p
        if value:
            dst[packed] = value
        else:
            dst.pop(packed, None)


def add_scaled_grouped(dst, src, scale, p):
    scale %= p
    if not scale:
        return
    for deep, base in src.items():
        target = dst.setdefault(deep, {})
        add_scaled_base(target, base, scale, p)
        if not target:
            dst.pop(deep, None)


def map_grouped(groups, p):
    """Apply the uf30 scope pin and the canonical tail-to-x registry."""
    result = {}
    for deep, base in groups.items():
        if "uf30" in deep:
            continue
        mapped = tuple(sorted(F.T2X.get(name, name) for name in deep))
        for packed, coeff in base.items():
            key = packed, mapped
            value = (result.get(key, 0) + coeff) % p
            if value:
                result[key] = value
            else:
                result.pop(key, None)
    return result


def serialize_poly(poly):
    terms = []
    for (packed, deep), coeff in sorted(poly.items()):
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


def variables_in(poly):
    used = set()
    for (packed, deep) in poly:
        used.update(name for name, exponent in zip(DR.GBVARS,
                                                   DR.unpack(packed))
                    if exponent)
        used.update(deep)
    return used


def degree_of(poly):
    return max((sum(DR.unpack(packed)) + len(deep)
                for packed, deep in poly), default=0)


class JoinedRows:
    def __init__(self, fh):
        self.fh = fh
        self.count = 0

    def write(self, row):
        if self.count:
            self.fh.write(b",\n")
        self.fh.write(row.encode("ascii"))
        self.count += 1


def write_solver_prefix(path, variables, parked_rows, graph_spool,
                        graph_limit, p):
    with open(path, "wb") as out:
        out.write((", ".join(variables) + "\n%d\n" % p).encode("ascii"))
        out.write(",\n".join(parked_rows).encode("ascii"))
        if graph_limit:
            out.write(b",\n")
            copy_bytes(graph_spool, out, graph_limit)
        out.write(b"\n")


def emit(ckdir, p, parked_path, compat_path, out_prefix, prefixes):
    header, source_prime, source_rows = read_ms_rows(compat_path)
    assert source_prime == p
    header_vars = tuple(x.strip() for x in header.split(","))
    assert len(header_vars) == len(set(header_vars)) == 172

    parked_header, parked_prime, parked_rows_iter = read_ms_rows(parked_path)
    assert parked_prime == p
    parked_vars = tuple(x.strip() for x in parked_header.split(","))
    parked_rows = list(parked_rows_iter)
    assert len(parked_rows) == 34
    assert set(parked_vars) <= set(header_vars)

    # The first 34 banked verdict rows must be the parked presentation.
    for index, wanted in enumerate(parked_rows):
        got = next(source_rows)
        assert got == wanted, ("parked-row regression", index)

    out_dir = os.path.dirname(os.path.abspath(out_prefix))
    os.makedirs(out_dir, exist_ok=True)
    graph_tmp = tempfile.NamedTemporaryFile(prefix="d43_graph_", suffix=".rows",
                                             dir=out_dir, delete=False)
    graph_tmp_path = graph_tmp.name
    graph_writer = JoinedRows(graph_tmp)
    graph_hash = hashlib.sha256()
    compat_hash = hashlib.sha256()
    used = set(parked_vars)
    prefix_meta = {}
    rung_reports = {}
    negative_control = None

    try:
        for expected_rows, expected_compat, k in zip(RUNG_SIZES,
                                                     COMPAT_SIZES, RUNGS):
            bank_path = os.path.join(
                ckdir, "d43red_p%d_a00pp_band%d.pkl" % (p, k))
            with open(bank_path, "rb") as fh:
                bank = pickle.load(fh)
            grouped = {h: groups for (h, _s), groups in bank["rows"].items()}
            hs, ynames, raw_groups, C, L, rank = NF.rung_kernel(grouped, k, p)
            assert len(raw_groups) == expected_rows
            assert len(L) == expected_compat

            mapped_raw = [map_grouped(row, p) for row in raw_groups]
            selected = {F.T2X.get(name, name) for name in ynames}
            if k == 42:
                selected.update(("Xf_alpha", "Xg_beta"))

            compat_terms = []
            for li, vector in enumerate(L):
                combination = {}
                for scale, row in zip(vector, raw_groups):
                    add_scaled_grouped(combination, row, scale, p)
                mapped = map_grouped(combination, p)
                assert not (variables_in(mapped) & selected), \
                    ("compat retains current graph variable", k, li)
                text = serialize_poly(mapped)
                source = next(source_rows)
                assert source == text, ("compat-row regression", k, li,
                                        len(source), len(text))
                compat_hash.update(text.encode("ascii"))
                compat_hash.update(b"\n")
                compat_terms.append(len(mapped))

                if negative_control is None:
                    hit = next(i for i, value in enumerate(vector) if value)
                    bad_rows = [{deep: dict(base) for deep, base in row.items()}
                                for row in raw_groups]
                    bad_deep = next(deep for deep in bad_rows[hit]
                                    if "uf30" not in deep)
                    bad_base = bad_rows[hit][bad_deep]
                    bad_packed = next(iter(bad_base))
                    bad_base[bad_packed] = (bad_base[bad_packed] + 1) % p
                    bad_combination = {}
                    for scale, row in zip(vector, bad_rows):
                        add_scaled_grouped(bad_combination, row, scale, p)
                    bad_text = serialize_poly(map_grouped(bad_combination, p))
                    assert bad_text != text
                    negative_control = {
                        "rung": k, "compat_row": li, "raw_row": hit,
                        "result": "PERTURBATION_DETECTED",
                    }

            raw_terms = []
            raw_degrees = []
            for row in mapped_raw:
                text = serialize_poly(row)
                graph_writer.write(text)
                graph_hash.update(text.encode("ascii"))
                graph_hash.update(b"\n")
                used.update(variables_in(row))
                raw_terms.append(len(row))
                raw_degrees.append(degree_of(row))
            graph_tmp.flush()
            prefix_meta[k] = {
                "graph_bytes": graph_tmp.tell(),
                "graph_rows": graph_writer.count,
                "used": set(used),
            }
            rung_reports[str(k)] = {
                "rows": len(raw_groups), "compat_rows": len(L),
                "rank_C": rank, "graph_terms": raw_terms,
                "graph_max_degree": max(raw_degrees),
                "compat_terms": compat_terms,
                "checkpoint": bank_path,
                "checkpoint_sha256": sha256_path(bank_path),
            }

        # No stale or extra source row is allowed after the 34+52 census.
        try:
            extra = next(source_rows)
        except StopIteration:
            extra = None
        assert extra is None, ("extra row in compatibility source", len(extra))
        assert graph_writer.count == 89
        assert sum(COMPAT_SIZES) == 52
        graph_tmp.close()

        missing_graph_vars = tuple(sorted(used - set(header_vars)))
        full_vars = header_vars + missing_graph_vars
        assert len(full_vars) == len(set(full_vars)) == 184, \
            (len(full_vars), missing_graph_vars)

        full_path = out_prefix + "_full175.ms"
        compat_end = trimmed_size(compat_path)
        compat_body = ms_body_offset(compat_path)
        with open(full_path, "wb") as out:
            out.write((", ".join(full_vars) + "\n%d\n" % p).encode("ascii"))
            with open(compat_path, "rb") as source:
                source.seek(compat_body)
                remaining = compat_end - compat_body
                while remaining:
                    block = source.read(min(8 << 20, remaining))
                    assert block
                    out.write(block)
                    remaining -= len(block)
            out.write(b",\n")
            copy_bytes(graph_tmp_path, out)
            out.write(b"\n")

        emitted_prefixes = {}
        for k in prefixes:
            assert k in prefix_meta
            meta = prefix_meta[k]
            variables = tuple(v for v in full_vars if v in meta["used"])
            prefix_path = out_prefix + "_graph_upto%d.ms" % k
            write_solver_prefix(prefix_path, variables, parked_rows,
                                graph_tmp_path, meta["graph_bytes"], p)
            emitted_prefixes[str(k)] = {
                "path": prefix_path,
                "sha256": sha256_path(prefix_path),
                "rows": 34 + meta["graph_rows"],
                "variables": len(variables),
                "bytes": os.path.getsize(prefix_path),
                "equivalent_compat_rows_omitted": sum(
                    size for rung, size in zip(RUNGS, COMPAT_SIZES)
                    if rung <= k),
            }

        report = {
            "status": "INTERNAL / UNREVIEWED",
            "prime": p,
            "fiber": "a00pp",
            "scope": "residue-A, B-frozen, no-log, PIN42, W1W2 != 0",
            "audit_system": {
                "path": full_path, "rows": 175, "variables": 184,
                "row_blocks": {"parked": 34, "compatibility": 52,
                               "reconstruction_graph": 89},
                "bytes": os.path.getsize(full_path),
                "sha256": sha256_path(full_path),
            },
            "sources": {
                "parked": parked_path,
                "parked_sha256": sha256_path(parked_path),
                "compatibility_verdict": compat_path,
                "compatibility_verdict_sha256": sha256_path(compat_path),
            },
            "gates": {
                "parked_identity_row_regression": "34/34 BYTE-EXACT",
                "compatibility_from_graph_regression": "52/52 BYTE-EXACT",
                "all_graph_rows_retained": "89/89",
                "compatibility_header_unique_variables": "172/172",
                "graph_header_unique_variables": "184/184",
                "graph_variables_missing_from_compatibility_header":
                    list(missing_graph_vars),
                "negative_control": negative_control,
            },
            "graph_rows_sha256": graph_hash.hexdigest(),
            "compatibility_rows_sha256": compat_hash.hexdigest(),
            "rungs": rung_reports,
            "solver_prefixes": emitted_prefixes,
        }
        report_path = out_prefix + "_report.json"
        with open(report_path, "w") as fh:
            json.dump(report, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print("D43 GRAPH FAMILY p=%d: PASS 34+52+89=175 -> %s" %
              (p, full_path), flush=True)
        print("  report -> %s" % report_path, flush=True)
        return report
    finally:
        if not graph_tmp.closed:
            graph_tmp.close()
        try:
            os.unlink(graph_tmp_path)
        except FileNotFoundError:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckdir", required=True)
    parser.add_argument("--prime", type=int, choices=NF.PRIMES, required=True)
    parser.add_argument("--parked", required=True)
    parser.add_argument("--compat-verdict", required=True)
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--prefixes", default="26,28,38")
    args = parser.parse_args()
    prefixes = tuple(int(x) for x in args.prefixes.split(",") if x)
    emit(args.ckdir, args.prime, args.parked, args.compat_verdict,
         args.out_prefix, prefixes)


if __name__ == "__main__":
    main()
