#!/usr/bin/env python3
"""Compare physical inverse radii with the proposed own-child Def5.1 radii.

No child inequalities or radius comparisons are used to alter candidates.
This is a read-only audit of library input/output, writing only this lane.
"""
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "box/lib"))
from descend_own import descend_own, def51_radii


def main():
    spec = importlib.util.spec_from_file_location(
        "hostile_frozen_skeleton", "/tmp/jc2-lane.wwyG4k/inputs/moh_skeleton_full.py")
    B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(B)
    payload = json.loads((ROOT / "box/ctop-gate-20260905/enum-replay.json").read_text())
    rows, groups = [], Counter()
    for r in payload["operative_rows"]:
        S = B.Skel(r["n"], r["m"], r["Ms"], {int(k): v for k, v in r["V"].items()})
        D = descend_own(S)
        if D["us"] != 1:
            continue
        for route in D["routes"]:
            j = route["first_nonzero"]
            V = {i: int(route["V"][i]) for i in range(2, D["s"] + 1)}
            V[D["s"] + 1] = D["d"][D["s"] + 1]
            ds = def51_radii(D["n"], D["M"], D["d"], V, D["ell"] + 1)
            values = []
            for i in ds:
                metric = (D["vs"] - F(D["us"], S.delta[i]) if i >= j else
                          D["vs"] - D["us"] - F(D["us"], S.delta[j]) * (1 - S.delta[i]))
                values.append(dict(i=i, def51=str(ds[i]), inverse_metric=str(metric),
                                   agrees=ds[i] == metric))
            agrees = all(v["agrees"] for v in values)
            groups[f"dropped={D['dropped']},agrees={agrees}"] += 1
            rows.append(dict(n=r["n"], m=r["m"], M=r["Ms"], V=r["V"],
                             dropped=D["dropped"], first_nonzero=j, radii=values))
    out = dict(count_type="DETERMINED", status="MISMATCH_REQUIRES_REPAIR",
               library_sha256=hashlib.sha256((ROOT / "box/lib/descend_own.py").read_bytes()).hexdigest(),
               routes=len(rows), radii=sum(len(r["radii"]) for r in rows),
               mismatches=sum(not v["agrees"] for r in rows for v in r["radii"]),
               groups=groups, rows=rows)
    (HERE / "hostile-metric-audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    main()
