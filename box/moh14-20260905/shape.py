#!/usr/bin/env python3
"""Is the 14-row residue exactly the s>=4 (descended s'>=3) shape?"""
import json, ast, sys
sys.path.insert(0, "/home/ubuntu/jc2/box/mohprog-drivers-20260903/repro")
import moh_skeleton_full as B
from collections import Counter

d = json.load(open("/home/ubuntu/jc2/box/mohprog-drivers-20260903/"
                   "full-tree-polynomial-ode-n100-audit.json"))
rows = d["rows"]
surv = [r for r in rows if r["group_feasible"] and r["selected_path_embeds"]]
inp  = [ast.literal_eval(r["row_key"]) for r in rows]

def s_of(t):
    n, m, Ms, V = t
    return B.Skel(n, m, list(Ms), {i: v for (i, v) in V}).s

print("== the operative POLY+ODE screen at n<=100, by skeleton depth s ==")
allc = Counter(s_of(t) for t in inp)
sc   = Counter(s_of(ast.literal_eval(r["row_key"])) for r in surv)
pc   = Counter(s_of(ast.literal_eval(r["row_key"])) for r in surv if r["is_printed"])
ec   = Counter(s_of(ast.literal_eval(r["row_key"])) for r in surv if not r["is_printed"])
print("   %3s %10s %10s %10s %10s %8s" % ("s", "s'=s-1", "input", "survive", "printed", "EXCESS"))
for s in sorted(allc):
    print("   %3d %10d %10d %10d %10d %8d" % (s, s - 1, allc[s], sc[s], pc[s], ec[s]))
print("\n   CLAIM: at s=3 (descended s'=2, Moh's Appendix II shape) the screen is EXACT")
print("          -- survivors are exactly Moh's six printed rows, zero excess.")
print("   CHECK: excess at s=3 = %d ; printed at s>=4 = %d"
      % (ec[3], sum(pc[s] for s in pc if s >= 4)))
ok = (ec.get(3, 0) == 0) and all(s == 3 for s in pc) and all(s >= 4 for s in ec.elements())
print("   %s" % ("[ok]   CLAIM HOLDS" if ok else "[FAIL] CLAIM FAILS"))
