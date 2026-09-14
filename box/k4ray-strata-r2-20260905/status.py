#!/usr/bin/env python3
import json, glob, os, sys
B = "/home/ubuntu/jc2/box/k4ray-strata-r2-20260905"
best = {}
for f in glob.glob(B + "/pull/*/*.json"):
    try: d = json.load(open(f))
    except Exception: continue
    st = d.get("stem")
    if not st: continue
    if st not in best or (d.get("total_wall") or 0) >= (best[st].get("total_wall") or 0):
        best[st] = d
hdr = ["stem","K","b","q","verdict","nv","ngens","form_s","mod_verdict","mod_s","mod_rss_GB","mod_deg","exq_verdict","exq_s","exq_rss_GB","exq_len","host"]
print("\t".join(hdr))
def key(s):
    d = best[s]; return (d.get("K",0), d.get("b",0), d.get("pin_index",0))
for st in sorted(best, key=key):
    d = best[st]; m = d.get("modular") or {}; e = d.get("exactq") or {}
    g = lambda v: "." if v is None else v
    rg = lambda v: "." if not v else round(v/1048576.0, 1)
    print("\t".join(str(x) for x in [st, d.get("K"), d.get("b"), d.get("pin_index"),
        d.get("verdict"), d.get("nvars"), g(d.get("ngens")), d.get("form_wall"),
        g(m.get("verdict")), g(m.get("wall")), rg(m.get("peak_rss_kb")), g(m.get("f4_max_degree")),
        g(e.get("verdict")), g(e.get("wall")), rg(e.get("peak_rss_kb")), g(e.get("basis_length")),
        (d.get("host") or ".")]))
