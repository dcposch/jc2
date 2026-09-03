#!/usr/bin/env python3
"""Normalize the shared exact tangent/Schur pivot table to TSV/JSON."""

from __future__ import annotations

import hashlib
import json
import pathlib

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "source_linear_spine_t2_t6.tsv"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    by_t = {}
    current = None
    for raw in SOURCE.read_text(encoding="utf-8").splitlines():
        if not raw:
            continue
        if raw.startswith("T "):
            left, H = raw.split(" H=", 1)
            current = int(left.split()[1])
            by_t[current] = {"H": H, "pivots": []}
            continue
        fields = raw.split("\t")
        if len(fields) != 9 or fields[0] != "P" or current is None:
            raise RuntimeError(f"unparsed source line: {raw}")
        _kind, band, tag, family, variable, u, resultant, source, deferrals = fields
        by_t[current]["pivots"].append({
            "step": len(by_t[current]["pivots"])+1,
            "band": int(band),
            "tag": tag,
            "family": family,
            "variable": variable,
            "u_primitive_Q_associate": u,
            "resultant_H_raw_u": resultant,
            "source": int(source),
            "unit_deferrals_before_pivot": int(deferrals),
        })

    lines = ["t\tstep\tband\ttag\tfamily\tvariable\tu_primitive_Q_associate"
             "\tresultant_H_raw_u\tsource\tunit_deferrals_before_pivot"
             "\tstatus"]
    record = {
        "typing": ("EXACT tangent/Schur pivot extraction at each fixed t; "
                   "full nonlinear canonical validation is separately typed"),
        "source": {"path": SOURCE.name, "sha256": digest(SOURCE)},
        "runs": {},
    }
    for t in sorted(by_t):
        if t == 2:
            status = "EXACT_FULL_NONLINEAR_VALIDATED"
        elif t == 3:
            status = "EXACT_FULL_NONLINEAR_VALIDATED_SHARED_ARTIFACT"
        else:
            status = "EXACT_SCHUR_DISCOVERY_PENDING_FULL_NONLINEAR_VALIDATION"
        pivots = by_t[t]["pivots"]
        expected = 5*t+2
        if len(pivots) != expected:
            raise AssertionError((t, len(pivots), expected))
        if any(sp.sympify(item["resultant_H_raw_u"]) == 0 for item in pivots):
            raise AssertionError((t, "zero accepted resultant"))
        record["runs"][str(t)] = {
            "H_raw": by_t[t]["H"],
            "pivot_count": len(pivots),
            "all_resultants_nonzero": True,
            "status": status,
            "pivots": pivots,
        }
        for item in pivots:
            lines.append("\t".join(map(str, [
                t, item["step"], item["band"], item["tag"], item["family"],
                item["variable"], item["u_primitive_Q_associate"],
                item["resultant_H_raw_u"], item["source"],
                item["unit_deferrals_before_pivot"], status,
            ])))
    tsv = HERE / "canonical_pivots_schur_t2_t6.tsv"
    tsv.write_text("\n".join(lines)+"\n", encoding="utf-8")
    record["artifact"] = {"path": tsv.name, "sha256": digest(tsv),
                          "bytes": tsv.stat().st_size}
    path = HERE / "canonical_pivots_schur_t2_t6.json"
    path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                    encoding="utf-8")
    print(json.dumps({"json": path.name, "json_sha256": digest(path),
                      "tsv": tsv.name, "tsv_sha256": digest(tsv),
                      "counts": {str(t): len(by_t[t]["pivots"])
                                 for t in sorted(by_t)}}), flush=True)


if __name__ == "__main__":
    main()
