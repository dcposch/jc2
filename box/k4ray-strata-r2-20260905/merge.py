#!/usr/bin/env python3
"""Merge phase-1 (form+solve) and phase-2 (re-solve on the same .ms) payloads.
Per chart we keep the STRONGEST outcome: exact-Q verdict > modular verdict > resource cause."""
import json, glob
B = "/home/ubuntu/jc2/box/k4ray-strata-r2-20260905"
CH = {}   # stem -> record
def rec(stem):
    return CH.setdefault(stem, dict(stem=stem, form_wall=None, nvars=None, ngens=None,
                                    modular=None, exactq=None, form_verdict=None, host=None,
                                    ms_sha=None))
for f in sorted(glob.glob(B + "/pull/*/*.json")):
    try: d = json.load(open(f))
    except Exception: continue
    st = d.get("stem")
    if not st: continue
    r = rec(st)
    if d.get("phase") == 2:
        slot = "exactq" if d.get("char") == 0 else ("modular_prob" if d.get("la") else "modular")
        if slot == "modular_prob": r.setdefault("modular_prob", None)
        cur = r[slot]
        cand = dict(verdict=d["verdict"], wall=d.get("wall"), peak_rss_kb=d.get("peak_rss_kb"),
                    basis_length=d.get("basis_length"), f4_max_degree=d.get("f4_max_degree"),
                    phase=2, msout_full=d.get("msout_full"))
        if cur is None or ("UNIT" in cand["verdict"] and "UNIT" not in (cur.get("verdict") or "")) \
           or (cand.get("wall") or 0) > (cur.get("wall") or 0) and "UNIT" not in (cur.get("verdict") or ""):
            r[slot] = cand
        r["ms_sha"] = r["ms_sha"] or d.get("ms_sha256")
        r["ms_rows"] = d.get("ms_rows")
    else:
        r["K"], r["b"], r["q"] = d.get("K"), d.get("b"), d.get("pin_index")
        r["nvars"] = d.get("nvars"); r["ngens"] = d.get("ngens")
        r["form_wall"] = d.get("form_wall"); r["host"] = d.get("host")
        r["form_verdict"] = d.get("verdict")
        r["ms_sha"] = r["ms_sha"] or d.get("ms_p0_sha256")
        for slot in ("modular", "exactq"):
            v = d.get(slot)
            if not v: continue
            cur = r[slot]
            v = dict(v); v["phase"] = 1
            if cur is None or ("UNIT" in (v.get("verdict") or "") and "UNIT" not in (cur.get("verdict") or "")):
                r[slot] = v
for st, r in CH.items():
    if r.get("K") is None:
        p = st.split("_"); r["K"] = int(p[0][1:]); r["b"] = int(p[1][1:]); r["q"] = int(p[2][1:])
json.dump(CH, open(B + "/merged.json", "w"), indent=1, sort_keys=True, default=str)
print("charts merged:", len(CH))
