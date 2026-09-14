#!/usr/bin/env python3
"""Per-stratum verdict: DEAD over Q only when BOTH cover charts are exact-Q [1]."""
import json
B = "/home/ubuntu/jc2/box/k4ray-strata-r2-20260905"
CH = json.load(open(B + "/merged.json"))
SCOPE = {7: [6, 7, 8], 8: list(range(7, 16)), 9: list(range(8, 18))}
R1DEAD = {7: [9, 10, 11, 12, 13], 8: [], 9: []}
def cell(K, b, q):
    r = CH.get(f"K{K}_B{b}_Q{q}")
    if r is None: return ("IN-FLIGHT", "no payload at seal")
    e, m = r.get("exactq") or {}, r.get("modular") or {}
    pm = r.get("modular_prob") or {}
    ev, mv, pv = e.get("verdict") or "", m.get("verdict") or "", pm.get("verdict") or ""
    if ev == "EXACTQ_UNIT": return ("Q-UNIT", "")
    if ev == "EXACTQ_NONUNIT": return ("Q-NONUNIT", "*** SURVIVOR: exact-Q basis len %s ***" % e.get("basis_length"))
    if mv == "MODULAR_NONUNIT": return ("p-NONUNIT", "*** modular survivor, basis len %s ***" % m.get("basis_length"))
    if mv == "MODULAR_UNIT": return ("p-UNIT", "modular screen only; exact-Q %s" % (ev or "not reached"))
    if pv == "MODULAR_NONUNIT": return ("p42-NONUNIT", "*** probabilistic-LA modular survivor, len %s ***" % pm.get("basis_length"))
    if pv == "MODULAR_UNIT": return ("p42-UNIT", "probabilistic-LA screen only (-l 42); exact-Q not reached")
    if r.get("form_verdict") == "FORMATION_TIMEOUT":
        return ("FORM-TO", "Singular formation timeout at %ss" % r.get("form_wall"))
    if ev.startswith("EXACTQ_TIMEOUT") or mv.startswith("MODULAR_TIMEOUT") or pv.startswith("MODULAR_TIMEOUT"):
        w = max([x for x in (e.get("wall"), m.get("wall"), pm.get("wall")) if x] or [0])
        return ("MS-TO", "msolve wall cap (longest %ss)" % round(w))
    if ev.startswith("MSOLVE_RC") or mv.startswith("MSOLVE_RC"):
        return ("MS-RC", "msolve rc %s (resource)" % (ev or mv).split("_")[-1])
    if r.get("nvars") and not (ev or mv): return ("FORMED", "chart emitted; msolve not returned")
    return (ev or mv or "?", "")
out, summary = [], {}
for K in (7, 8, 9):
    out.append("")
    dead, partial, undec, surv = [], [], [], []
    for b in SCOPE[K]:
        c0, c1 = cell(K, b, 0), cell(K, b, 1)
        if "NONUNIT" in c0[0] or "NONUNIT" in c1[0]:
            verd = "*** SURVIVOR ***"; surv.append(b)
        elif c0[0] == "Q-UNIT" and c1[0] == "Q-UNIT":
            verd = "DEAD over Q"; dead.append(b)
        elif c0[0] == "Q-UNIT" or c1[0] == "Q-UNIT":
            verd = "partial (one cover exact-Q)"; partial.append(b)
        else:
            verd = "UNDECIDED"; undec.append(b)
        cause = "; ".join(x for x in (c0[1], c1[1]) if x)
        out.append("K=%d b=%-3d q0=%-10s q1=%-10s %-27s %s" % (K, b, c0[0], c1[0], verd, cause))
    summary[K] = (dead, partial, undec, surv)
print("\n".join(out)); print()
for K in (7, 8, 9):
    d, p, u, s = summary[K]
    ex = "  (round 1 exact-Q DEAD: %s)" % R1DEAD[K] if R1DEAD[K] else ""
    print("K=%d scope %s:\n   DEAD-over-Q %s | partial %s | undecided %s | SURVIVORS %s%s" % (K, SCOPE[K], d, p, u, s, ex))
