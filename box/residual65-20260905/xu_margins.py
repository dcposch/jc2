#!/usr/bin/env python3
"""Xu Cor 5.3 margins (IM_max - Im_min) on the roster, with the licensed principal floor
(V_s/u_s - 1 at u_s = 1, 0 at u_s > 1: Moh Prop 6.4 p.198) and the UNPRINTED sharper floor
V_s/u_s - 1 at u_s > 1 as a diagnostic.  Uses the frozen XuBounder (box/xuscreen-gate-20260903)."""
import sys, json, os
from fractions import Fraction as F
ROOT = "/home/ubuntu/jc2"
sys.path.insert(0, os.path.join(ROOT, "box/mohprog-drivers-20260903"))          # full_tree_partition
sys.path.insert(0, os.path.join(ROOT, "box/mohprog-drivers-20260903/repro"))    # moh_skeleton_full
sys.path.insert(0, os.path.join(ROOT, "box/xuscreen-gate-20260903"))
import xu_screen_replay as XS
M = XS.M
rows = [json.loads(l) for l in open("/tmp/jc2-lane.3peIuR/inputs/roster.jsonl")]
out = []
print("%-5s %-9s u v  IM_max  Im_min  margin  floor_used  sharp_floor  Im_sharp  sharp_kill" % ("row", "(n,m)", ))
for r in rows:
    s = r["source"]; n, m = s["n"], s["m"]
    S = M.Skel(n, m, s["M"][1:], {i + 2: s["V"][i] for i in range(len(s["V"]))})
    b = XS.XuBounder(S).row_bound()
    if b is None:
        print(r["row_id"], "NO-EMBED"); continue
    IMmax, Immin, tmin, pf = b["IM_max"], b["Im_min"], b["tree_minor_min"], b["principal_minor_floor"]
    us, vs = s["u_s"], s["v_s"]
    sharp = max(F(0), F(vs, us) - 1)
    Im_sharp = Immin - pf + sharp
    kill_sharp = IMmax < Im_sharp
    out.append(dict(row_id=r["row_id"], n=n, m=m, u_s=us, v_s=vs, IM_max=str(IMmax), Im_min=str(Immin),
                    margin=str(IMmax - Immin), floor_used=str(pf), sharp_floor=str(sharp), Im_sharp=str(Im_sharp),
                    sharp_kill=kill_sharp, tree_minor_min=str(tmin)))
    print("%-5s (%3d,%3d) %d %2d  %6s  %6s  %6s  %6s      %6s      %6s   %s" % (
        r["row_id"], n, m, us, vs, IMmax, Immin, IMmax - Immin, pf, sharp, Im_sharp, "KILL" if kill_sharp else ""))
json.dump(out, open(os.path.join(ROOT, "box/residual65-20260905/xu_margins.json"), "w"), indent=1)
from collections import Counter
print("\nmargin histogram:", dict(sorted(Counter(o["margin"] for o in out).items(), key=lambda kv: F(kv[0]))))
print("sharp-floor kills (u_s>1 only can change):", [o["row_id"] for o in out if o["sharp_kill"]])
print("rows with margin < 1:", [(o["row_id"], o["margin"]) for o in out if F(o["margin"]) < 1])
