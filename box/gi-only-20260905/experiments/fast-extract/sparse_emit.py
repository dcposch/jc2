#!/usr/bin/env python3
"""Exact sparse-Python extraction of literal J(P,Q)-c*x^ell coefficients.

The canonical G builder remains the source of the ring and setup.  This
experimental emitter parses only its primitive h/AA/BB definitions, performs
integer sparse-polynomial arithmetic, and emits ordinary x,y coefficient
rows over exactly the original parameter variables.  It introduces neither
specializations nor auxiliary unknowns.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import re
import resource
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
GI = ROOT / "box" / "gi-only-20260905"
OUT = GI / "experiments" / "fast-extract"
ONE = {(): 1}


def addto(target: dict, source: dict, scale: int = 1) -> None:
    for mon, coeff in source.items():
        new = target.get(mon, 0) + scale * coeff
        if new:
            target[mon] = new
        else:
            target.pop(mon, None)


def cmul(a: dict, b: dict) -> dict:
    out: dict[tuple[str, ...], int] = {}
    for am, ac in a.items():
        for bm, bc in b.items():
            mon = tuple(sorted(am + bm))
            new = out.get(mon, 0) + ac * bc
            if new:
                out[mon] = new
            else:
                out.pop(mon, None)
    return out


def xyaddto(target: dict, source: dict, scale: int = 1) -> None:
    for coord, coeff in source.items():
        bucket = target.setdefault(coord, {})
        addto(bucket, coeff, scale)
        if not bucket:
            del target[coord]


def xyconv(a: dict, b: dict) -> dict:
    out: dict[tuple[int, int], dict] = {}
    for (ax, ay), ac in a.items():
        for (bx, by), bc in b.items():
            coord = (ax + bx, ay + by)
            bucket = out.setdefault(coord, {})
            addto(bucket, cmul(ac, bc))
            if not bucket:
                del out[coord]
    return out


def derivative(poly: dict, axis: int) -> dict:
    out = {}
    for coord, coeff in poly.items():
        power = coord[axis]
        if not power:
            continue
        dest = list(coord)
        dest[axis] -= 1
        out[tuple(dest)] = {mon: power * val for mon, val in coeff.items()}
    return out


def parse_primitive(expr: str) -> dict:
    """Parse the canonical setup grammar (sum of monomial primitives)."""
    out: dict[tuple[int, int], dict] = {}
    normalized = expr.replace("-", "+-")
    for raw in normalized.split("+"):
        raw = raw.strip()
        if not raw:
            continue
        sign = 1
        if raw.startswith("-"):
            sign, raw = -1, raw[1:].strip()
        xpow = ypow = 0
        vars_: list[str] = []
        scalar = sign
        for token in raw.split("*"):
            token = token.strip()
            if not token or token == "1":
                continue
            m = re.fullmatch(r"([xy])(?:\^(\d+))?", token)
            if m:
                p = int(m.group(2) or 1)
                if m.group(1) == "x":
                    xpow += p
                else:
                    ypow += p
            elif re.fullmatch(r"-?\d+", token):
                scalar *= int(token)
            elif re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", token):
                vars_.append(token)
            else:
                raise ValueError(f"unsupported primitive token {token!r} in {expr!r}")
        bucket = out.setdefault((xpow, ypow), {})
        addto(bucket, {tuple(sorted(vars_)): scalar})
        if not bucket:
            del out[(xpow, ypow)]
    return out


def ctext(poly: dict) -> str:
    chunks = []
    for mon, coeff in sorted(poly.items()):
        if not coeff:
            continue
        counts = Counter(mon)
        body = "*".join(v if n == 1 else f"{v}^{n}" for v, n in sorted(counts.items()))
        magnitude = abs(coeff)
        if body:
            body = body if magnitude == 1 else f"{magnitude}*{body}"
        else:
            body = str(magnitude)
        chunks.append(("-" if coeff < 0 else "+" if chunks else "") + body)
    return "".join(chunks) or "0"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(class_dir: Path) -> dict:
    t0 = time.monotonic()
    cls = json.loads((class_dir / "class.json").read_text(encoding="utf-8"))
    cid, stem = cls["class_id"], cls["canonical_stem"]
    meta_path = class_dir / "meta" / f"{stem}.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    src = class_dir / "builders" / f"{stem}_builder.sing"
    raw = src.read_text(encoding="utf-8")
    if "literal coefficient ideal: J(P,Q)" not in raw:
        raise AssertionError("source orientation is not literal J(P,Q)")
    ring = re.search(r"^ring R=.*;$", raw, re.M).group(0)
    if not ring.startswith("ring R=0,(y,x,") or "(lp(1),dp(" not in ring:
        raise AssertionError("source ring is not the required polynomial/y-first ring")
    definitions = dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*?);$", raw, re.M))
    polys = {name: parse_primitive(expr) for name, expr in definitions.items()}
    h = polys["h"]

    def horner(prefix: str, degree: int) -> dict:
        current = {(0, 0): ONE}
        for k in range(1, degree + 1):
            current = xyconv(current, h)
            xyaddto(current, polys.get(f"{prefix}{k}", {}))
        return current

    P = horner("AA", int(cls["e"]))
    Q = horner("BB", int(cls["q"]))
    jac = xyconv(derivative(P, 0), derivative(Q, 1))
    xyaddto(jac, xyconv(derivative(P, 1), derivative(Q, 0)), -1)
    target = jac.setdefault((int(cls["ell"]), 0), {})
    addto(target, {("c",): 1}, -1)
    if not target:
        del jac[(int(cls["ell"]), 0)]

    rows_dir = OUT / "sparse-rows"
    rows_dir.mkdir(parents=True, exist_ok=True)
    rows_path = rows_dir / f"{stem}_sparse_direct_rows.tsv"
    with rows_path.open("w", encoding="utf-8") as fh:
        fh.write("source_index|h_power|x_power|y_power|expr\n")
        for idx, ((xpow, ypow), coeff) in enumerate(sorted(jac.items())):
            fh.write(f"{idx}|0|{xpow}|{ypow}|{ctext(coeff)}\n")
    elapsed = time.monotonic() - t0
    variables = meta["variables"]
    if len(variables) != cls["unknowns_without_T"]:
        raise AssertionError("metadata variable count drift")
    row_body = rows_path.read_text(encoding="utf-8").split("\n", 1)[1]
    unknown_in_rows = set(re.findall(r"\b[A-Za-z_][A-Za-z_0-9]*\b", row_body))
    if not unknown_in_rows <= set(variables):
        raise AssertionError(f"unexpected variables: {sorted(unknown_in_rows-set(variables))}")
    return {
        "class_id": cid,
        "stem": stem,
        "representation": "ordinary_xy_coefficients_of_literal_J(P,Q)-c*x^ell",
        "no_specialization": True,
        "no_auxiliary_unknowns": True,
        "unknowns_without_T": len(variables),
        "unknowns_with_T": len(variables) + 1,
        "equations_without_inverse": len(jac),
        "equations_with_inverse": len(jac) + 1,
        "P_xy_support": len(P),
        "Q_xy_support": len(Q),
        "jacobian_xy_support": len(jac),
        "elapsed_seconds": round(elapsed, 6),
        "max_rss_kib_process": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_builder": str(src.relative_to(ROOT)),
        "source_builder_sha256": sha(src),
        "source_meta": str(meta_path.relative_to(ROOT)),
        "source_meta_sha256": sha(meta_path),
        "source_ring": ring,
        "rows": str(rows_path.relative_to(ROOT)),
        "rows_bytes": rows_path.stat().st_size,
        "rows_sha256": sha(rows_path),
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
    manifest = OUT / "sparse-emission.json"
    old = []
    if manifest.exists() and ns.class_id:
        old = json.loads(manifest.read_text(encoding="utf-8"))
        done = {r["class_id"] for r in records}
        old = [r for r in old if r["class_id"] not in done]
    merged = sorted(old + records, key=lambda r: r["class_id"])
    manifest.write_text(json.dumps(merged, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
