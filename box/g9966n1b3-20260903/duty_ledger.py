#!/usr/bin/env python3
"""Exact remaining-duty ledger for the five open (99,66) skeletons.

For each skeleton: the split leaves that survive the mechanical face screen, and
every no-split partition chart of the Prop 6.3 descent with its exact parameter
count and localizer.  This is the precise finite kill list that remains.
"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
spec = importlib.util.spec_from_file_location(
    "duty_ob", ROOT / "box" / "orderbasis-20260903" / "order_basis_full.py")
ob = importlib.util.module_from_spec(spec); sys.modules["duty_ob"] = ob
spec.loader.exec_module(ob)

ROWS = {
    "S1": ob.Row("S1_n18_m12_Mm4_V1_k6", "S1", 18, 12, -4, 1, 6),
    "S2": ob.Row("S2_n36_m24_M8_V1_k2", "S2", 36, 24, 8, 1, 2),
    "S3": ob.Row("S3_n36_m24_M8_V5_k2", "S3", 36, 24, 8, 5, 2),
    "S4": ob.Row("S4_n27_m18_M6_V1_k4", "S4", 27, 18, 6, 1, 4),
    "S7": ob.Row("S7_n36_m24_M28_V8_k2", "S7", 36, 24, 28, 8, 2),
}


def partitions(total, cap=None):
    if total == 0:
        yield ()
        return
    high = total if cap is None else min(total, cap)
    for first in range(high, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


face = json.loads((HERE / "face-screen.json").read_text())
resolve = json.loads((HERE / "face-resolve.json").read_text())
extra = {}
for case in resolve["cases"]:
    if case["verdict"] == "SOLVABLE":
        extra.setdefault(case["row"], []).append({"delta": case["delta"],
                                                  "partition": case["partition"]})

out = {"schema": "jc2.g9966n1b3.duty-ledger/v1", "rows": {}}
for name, row in ROWS.items():
    C = ob.closed_form(row)
    one = ob.build_full_spec(row, (C["u"],))["meta"]
    parts = list(partitions(C["u"]))
    charts = []
    for part in parts:
        charts.append({"partition": list(part),
                       "label": "+".join(map(str, part)),
                       "stem": ob.stem_for(row, part),
                       "params_without_T": one["params_without_T"] + len(part) - 1,
                       "slopes": len(part) - 1})
    leaves = list(face["rows"][name]["survivors"]) + extra.get(name, [])
    leaves = sorted({(l["delta"], tuple(l["partition"])) for l in leaves})
    out["rows"][name] = {
        "descended": {"n": row.n, "m": row.m, "M2": row.M2, "V2": row.V2, "ell": row.k,
                      "K": C["K"], "u_prime": C["u"]},
        "closed_form": ob.serial_closed_form(C),
        "split_leaves_surviving_face_screen": [{"delta": d, "partition": list(p)}
                                               for d, p in leaves],
        "split_leaf_count": len(leaves),
        "no_split_partition_charts": charts,
        "no_split_chart_count": len(charts),
        "localizer": "T*c*omega-1, omega=prod s_j(s_j-1) prod_{i<j}(s_i-s_j)",
        "target": f"J(Q,P)-c*x^{row.k}",
    }
(HERE / "duty-ledger.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
tot_leaf = tot_chart = 0
for name, rec in out["rows"].items():
    tot_leaf += rec["split_leaf_count"]; tot_chart += rec["no_split_chart_count"]
    print(f"{name}: u'={rec['descended']['u_prime']} "
          f"split_leaves={rec['split_leaf_count']} "
          f"no_split_charts={rec['no_split_chart_count']} "
          f"params={[c['params_without_T'] for c in rec['no_split_partition_charts']][:1]}"
          f"..{[c['params_without_T'] for c in rec['no_split_partition_charts']][-1]} "
          f"leaves={rec['split_leaves_surviving_face_screen']}")
print(f"TOTAL split leaves={tot_leaf}  no-split charts={tot_chart}")
