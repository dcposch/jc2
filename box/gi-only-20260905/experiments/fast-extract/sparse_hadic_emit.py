#!/usr/bin/env python3
"""Exact sparse h-adic coefficient extraction for canonical G-only charts.

Unlike ``sparse_emit.py`` this emits the *same h-adic remainders* as the
canonical builder.  It performs the formal Jacobian coefficient arithmetic
and monic y-division using sparse integer dictionaries, avoiding Singular's
large ambient-ring polynomial ordering overhead.  It uses every original G
coordinate, introduces no variables, and performs no specialization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import resource
import time
from pathlib import Path

import sparse_emit as S


ROOT = Path(__file__).resolve().parents[4]
GI = ROOT / "box" / "gi-only-20260905"
OUT = GI / "experiments" / "fast-extract"


def xyscale(poly: dict, scalar: int) -> dict:
    if not scalar:
        return {}
    return {coord: {m: scalar * c for m, c in coeff.items()}
            for coord, coeff in poly.items()}


def jacobian(a: dict, b: dict) -> dict:
    out = S.xyconv(S.derivative(a, 0), S.derivative(b, 1))
    S.xyaddto(out, S.xyconv(S.derivative(a, 1), S.derivative(b, 0)), -1)
    return out


def monic_y_div(dividend: dict, h: dict, K: int) -> tuple[dict, dict]:
    """Return quotient,remainder in A[x][y] for y-monic h of degree K."""
    if h.get((0, K)) != S.ONE:
        raise AssertionError("h is not y-monic with unique leading coefficient 1")
    if any(y >= K and (x, y) != (0, K) for x, y in h):
        raise AssertionError("h has a second term at or above degree K")
    work = {coord: dict(coeff) for coord, coeff in dividend.items()}
    quotient: dict[tuple[int, int], dict] = {}
    # All non-leading h terms lower y-degree, so descending y terminates and
    # is independent of x ordering.
    while work:
        max_y = max(y for _, y in work)
        if max_y < K:
            break
        leading_xs = sorted(x for x, y in work if y == max_y)
        for xpow in leading_xs:
            coord = (xpow, max_y)
            coeff = work.get(coord)
            if not coeff:
                continue
            qcoord = (xpow, max_y - K)
            qbucket = quotient.setdefault(qcoord, {})
            S.addto(qbucket, coeff)
            if not qbucket:
                del quotient[qcoord]
            # work -= coeff*x^xpow*y^(max_y-K)*h.  The leading term removes
            # coord exactly; lower h terms cannot recreate this y degree.
            for (hx, hy), hc in h.items():
                dest = (xpow + hx, max_y - K + hy)
                bucket = work.setdefault(dest, {})
                S.addto(bucket, S.cmul(coeff, hc), -1)
                if not bucket:
                    del work[dest]
            if coord in work:
                raise AssertionError(f"leading term failed to cancel at {coord}")
    return quotient, work


def emit(class_dir: Path) -> dict:
    t0 = time.monotonic()
    cls = json.loads((class_dir / "class.json").read_text(encoding="utf-8"))
    cid, stem = cls["class_id"], cls["canonical_stem"]
    meta_path = class_dir / "meta" / f"{stem}.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    builder = class_dir / "builders" / f"{stem}_builder.sing"
    raw = builder.read_text(encoding="utf-8")
    if "literal coefficient ideal: J(P,Q)" not in raw:
        raise AssertionError("source orientation is not literal J(P,Q)")
    ring = re.search(r"^ring R=.*;$", raw, re.M).group(0)
    if not ring.startswith("ring R=0,(y,x,") or "(lp(1),dp(" not in ring:
        raise AssertionError("source ring is not polynomial/y-first")
    definitions = dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*?);$", raw, re.M))
    polys = {name: S.parse_primitive(expr) for name, expr in definitions.items()}
    h = polys["h"]
    K, e, q = int(cls["K"]), int(cls["e"]), int(cls["q"])
    A = {0: {(0, 0): S.ONE}, **{i: polys[f"AA{i}"] for i in range(1, e + 1)}}
    B = {0: {(0, 0): S.ONE}, 1: {}}
    B.update({j: polys[f"BB{j}"] for j in range(2, q + 1)})
    initial: dict[int, dict] = {}
    for i in range(e + 1):
        pi = e - i
        for j in range(q + 1):
            rj = q - j
            if not A[i] or not B[j]:
                continue
            same = jacobian(A[i], B[j])
            if same:
                level = pi + rj
                S.xyaddto(initial.setdefault(level, {}), same)
            lower = {}
            if rj:
                term = S.xyconv(B[j], jacobian(A[i], h))
                S.xyaddto(lower, term, rj)
            if pi:
                term = S.xyconv(A[i], jacobian(h, B[j]))
                S.xyaddto(lower, term, pi)
            if lower:
                level = pi + rj - 1
                if level < 0:
                    raise AssertionError("negative formal h level")
                S.xyaddto(initial.setdefault(level, {}), lower)

    allocated = [int(v) for v in re.findall(r"^poly H(\d+) = 0;$", raw, re.M)]
    if allocated != list(range(max(allocated) + 1)):
        raise AssertionError("canonical H allocation is not consecutive")
    levels = {i: initial.get(i, {}) for i in allocated}
    remainders = {}
    for i in allocated:
        quotient, remainder = monic_y_div(levels[i], h, K) if levels[i] else ({}, {})
        remainders[i] = remainder
        if quotient:
            if i == allocated[-1]:
                raise AssertionError("canonical H allocation too short for final quotient")
            S.xyaddto(levels[i + 1], quotient)

    target_coord = (int(cls["ell"]), 0)
    target = remainders[0].setdefault(target_coord, {})
    S.addto(target, {("c",): 1}, -1)
    if not target:
        del remainders[0][target_coord]

    rows_dir = OUT / "sparse-hadic-rows"
    rows_dir.mkdir(parents=True, exist_ok=True)
    rows_path = rows_dir / f"{stem}_sparse_hadic_rows.tsv"
    row_count = 0
    with rows_path.open("w", encoding="utf-8") as fh:
        fh.write("source_index|h_power|x_power|y_power|expr\n")
        for level in allocated:
            for (xpow, ypow), coeff in sorted(remainders[level].items()):
                fh.write(f"{row_count}|{level}|{xpow}|{ypow}|{S.ctext(coeff)}\n")
                row_count += 1
    variables = meta["variables"]
    body = rows_path.read_text(encoding="utf-8").split("\n", 1)[1]
    seen = set(re.findall(r"\b[A-Za-z_][A-Za-z_0-9]*\b", body))
    if not seen <= set(variables):
        raise AssertionError(f"unexpected variables: {sorted(seen-set(variables))}")
    return {
        "class_id": cid,
        "stem": stem,
        "representation": "canonical_monic_h_adic_coefficients_of_literal_J(P,Q)-c*x^ell",
        "no_specialization": True,
        "no_auxiliary_unknowns": True,
        "unknowns_without_T": len(variables),
        "unknowns_with_T": len(variables) + 1,
        "equations_without_inverse": row_count,
        "equations_with_inverse": row_count + 1,
        "nonzero_h_levels": [i for i in allocated if remainders[i]],
        "elapsed_seconds": round(time.monotonic() - t0, 6),
        "max_rss_kib_process": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_builder": str(builder.relative_to(ROOT)),
        "source_builder_sha256": hashlib.sha256(builder.read_bytes()).hexdigest(),
        "source_meta": str(meta_path.relative_to(ROOT)),
        "source_meta_sha256": hashlib.sha256(meta_path.read_bytes()).hexdigest(),
        "source_ring": ring,
        "rows": str(rows_path.relative_to(ROOT)),
        "rows_bytes": rows_path.stat().st_size,
        "rows_sha256": hashlib.sha256(rows_path.read_bytes()).hexdigest(),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--class-id", action="append", default=[])
    ns = ap.parse_args()
    dirs = sorted((GI / "classes").glob("C_*"))
    if ns.class_id:
        wanted = set(ns.class_id)
        dirs = [p for p in dirs if p.name in wanted]
    records = []
    for directory in dirs:
        record = emit(directory)
        records.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
    manifest = OUT / "sparse-hadic-emission.json"
    old = []
    if manifest.exists() and ns.class_id:
        old = json.loads(manifest.read_text(encoding="utf-8"))
        done = {r["class_id"] for r in records}
        old = [r for r in old if r["class_id"] not in done]
    manifest.write_text(json.dumps(sorted(old + records, key=lambda x: x["class_id"]),
                                   indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
