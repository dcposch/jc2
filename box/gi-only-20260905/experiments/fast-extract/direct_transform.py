#!/usr/bin/env python3
"""Emit experimental exact direct-coefficient builders for G-only charts.

This file is intentionally separate from the canonical emitter/builders.  It
replaces repeated monic h-adic division by recomposition of the already-built
formal h-adic expression and extraction of all ordinary x,y coefficients.
No chart coordinate is removed or specialized.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
GI = ROOT / "box" / "gi-only-20260905"
OUT = GI / "experiments" / "fast-extract"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transform(class_dir: Path) -> dict:
    cls = json.loads((class_dir / "class.json").read_text(encoding="utf-8"))
    cid = cls["class_id"]
    stem = cls["canonical_stem"]
    src = class_dir / "builders" / f"{stem}_builder.sing"
    text = src.read_text(encoding="utf-8")
    if "literal coefficient ideal: J(P,Q)" not in text:
        raise AssertionError(f"not a literal P,Q production builder: {src}")
    if "ring R=0,(y,x," not in text or "(lp(1),dp(" not in text:
        raise AssertionError(f"not the required polynomial/y-first ring: {src}")
    split = text.index("if (H0 != 0) {")
    prefix = text[:split]
    levels = [int(x) for x in re.findall(r"^poly H(\d+) = 0;$", prefix, re.M)]
    if levels != list(range(max(levels) + 1)):
        raise AssertionError(f"nonconsecutive formal levels in {src}")
    assigned = [int(x) for x in re.findall(r"\bH(\d+) = H\1 \+", prefix)]
    if not assigned:
        raise AssertionError(f"no formal h-adic summands in {src}")
    active_max = max(assigned)
    ell = int(cls["ell"])

    rows_rel = f"rows/{stem}_direct_rows.tsv"
    direct = prefix
    direct = re.sub(
        r'string rowsfile = "[^"]+";',
        f'string rowsfile = "{rows_rel}";',
        direct,
        count=1,
    )
    direct += "\n// EXPERIMENTAL exact ordinary-coefficient presentation.\n"
    direct += "// Same full G chart and ring; no coordinate specialization.\n"
    direct += "// Monicity of h makes this ideal equal to the h-adic coefficient ideal.\n"
    direct += "poly DIRECT = 0;\n"
    for i in range(active_max, -1, -1):
        direct += f"DIRECT = DIRECT*h + H{i};\n"
    direct += f"poly target_xk = native_coeff_xy(DIRECT, {ell}, 0, WX, WY);\n"
    direct += (
        'if (target_xk != 0) { print("DIRECT_GATE target_xk_nonzero=1"); } '
        'else { print("DIRECT_GATE target_xk_nonzero=0"); }\n'
    )
    direct += f"DIRECT = DIRECT - c*x^{ell};\n"
    direct += "native_append_coeffs(DIRECT, 0, rowsfile, WX, WY);\n"
    direct += 'print("DIRECT_DONE equations=" + string(source_idx));\n'
    direct += 'print("DIRECT_DONE max_degree_x=" + string(max_nf_deg));\n'
    direct += "quit;\n"

    bdir = OUT / "builders"
    rdir = OUT / "rows"
    bdir.mkdir(parents=True, exist_ok=True)
    rdir.mkdir(parents=True, exist_ok=True)
    dst = bdir / f"{stem}_direct_builder.sing"
    dst.write_text(direct, encoding="utf-8")
    return {
        "class_id": cid,
        "stem": stem,
        "unknowns_without_T": cls["unknowns_without_T"],
        "source_builder": str(src.relative_to(ROOT)),
        "source_builder_sha256": sha256(src),
        "direct_builder": str(dst.relative_to(ROOT)),
        "direct_builder_sha256": sha256(dst),
        "direct_rows": str((rdir / f"{stem}_direct_rows.tsv").relative_to(ROOT)),
        "allocated_h_levels": max(levels) + 1,
        "active_max_h_level": active_max,
        "K": cls["K"],
        "ell": ell,
        "ring_preserved_verbatim": re.search(r"^ring R=.*;$", text, re.M).group(0)
        == re.search(r"^ring R=.*;$", direct, re.M).group(0),
        "setup_prefix_preserved_verbatim": hashlib.sha256(prefix.encode()).hexdigest()
        == hashlib.sha256(text[:split].encode()).hexdigest(),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--class-id", action="append", default=[])
    ns = ap.parse_args()
    class_dirs = sorted((GI / "classes").glob("C_*"))
    if ns.class_id:
        wanted = set(ns.class_id)
        class_dirs = [p for p in class_dirs if p.name in wanted]
        missing = wanted - {p.name for p in class_dirs}
        if missing:
            raise SystemExit(f"unknown classes: {sorted(missing)}")
    records = [transform(p) for p in class_dirs]
    manifest = OUT / "direct-transform.json"
    manifest.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(records, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
