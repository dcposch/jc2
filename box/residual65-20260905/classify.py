#!/usr/bin/env python3
"""Classification of the 66-row roster (65 under the full conjunction; R001 Xu-removed)."""
import json, sys, os
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
ROSTER = "/tmp/jc2-lane.3peIuR/inputs/roster.jsonl"
rows = [json.loads(l) for l in open(ROSTER)]
W = sys.stdout.write
def src(r): return r["source"]
def ch(r): return r["own_child"]
res = {o["row_id"]: o for o in json.load(open(os.path.join(HERE, "second_gen.json")))}
live = [r for r in rows if r["row_id"] != "R001"]
W("population: %d roster rows; %d after Xu Cor 5.3 (R001 removed)\n\n" % (len(rows), len(live)))

def H(rs, k):
    return dict(sorted(Counter(k(r) for r in rs).items(), key=lambda kv: (str(kv[0]))))
W("== A. by descent route ==\n")
W("  u_s: %s\n" % H(live, lambda r: src(r)["u_s"]))
W("  route/prefix: %s\n" % H(live, lambda r: (r["descent"]["route"], "prefix" if r["descent"]["prefix_only"] else "complete")))
W("  s (source height): %s ; s' (child height): %s\n" % (H(live, lambda r: src(r)["s"]), H(live, lambda r: ch(r)["s_prime"])))
W("  (u_s, s'): %s\n" % H(live, lambda r: (src(r)["u_s"], ch(r)["s_prime"])))
W("  ell = v_s-u_s-1: %s\n" % H(live, lambda r: ch(r)["ell"]))
W("  (u_s, ell): %s\n" % H(live, lambda r: (src(r)["u_s"], ch(r)["ell"])))
W("  d_s: %s\n" % H(live, lambda r: src(r)["d"][src(r)["s"]-1]))
W("  n<=100: %s\n" % H(live, lambda r: src(r)["n"] <= 100))

W("\n== B. degree pairs ==\n")
dp = Counter((src(r)["n"], src(r)["m"]) for r in live)
W("  %d distinct source (n,m): %s\n" % (len(dp), dict(sorted(dp.items()))))
ratio = Counter(F(src(r)["n"], src(r)["m"]) for r in live)
W("  n/m ratio: %s\n" % {str(k): v for k, v in sorted(ratio.items())})
K = Counter(gcd(src(r)["n"], src(r)["m"]) for r in live)
W("  K=gcd(n,m): %s\n" % dict(sorted(K.items())))
small = [(84,56),(75,50),(64,48),(99,66)]
W("  rows at n>100 whose (n,m) is an integer multiple of a Moh <=100 pair:\n")
for r in live:
    n, m = src(r)["n"], src(r)["m"]
    if n > 100:
        for (a, b) in small:
            if n % a == 0 and m % b == 0 and n // a == m // b:
                W("     %s (%d,%d) = %d x (%d,%d)   M=%s V=%s   [M_s=n-2 does not scale: not a tower]\n" % (r["row_id"], n, m, n // a, a, b, src(r)["M"], src(r)["V"]))

W("\n== C. children ==\n")
chd = Counter((ch(r)["n_prime"], ch(r)["m_prime"]) for r in live)
W("  %d distinct child (n',m'): %s\n" % (len(chd), dict(sorted(chd.items()))))
rk = Counter(r["receiver_chart"]["receiver_key_string"] for r in live)
W("  %d distinct receiver keys (n',m',M'_last,ell)\n" % len(rk))
eq = Counter((ch(r)["n_prime"] // r["receiver_chart"]["K"], ch(r)["m_prime"] // r["receiver_chart"]["K"]) for r in live)
W("  child (e,q) = (n'/K, m'/K): %s\n" % dict(sorted(eq.items())))
W("  child K' = gcd(n',m'): %s\n" % H(live, lambda r: r["receiver_chart"]["K"]))
moh_children = {(21,14), (15,10), (16,12)}
W("  rows whose child degree pair is one of Moh's p.207 children (21,14),(15,10),(16,12):\n")
for r in live:
    c = ch(r)
    if (c["n_prime"], c["m_prime"]) in moh_children:
        W("     %s parent (%d,%d) u_s=%d -> child (%d,%d) M'=%s V'=%s ell=%d  %s\n" % (r["row_id"], src(r)["n"], src(r)["m"], src(r)["u_s"], c["n_prime"], c["m_prime"], c["M_prime"], c["V_prime"], c["ell"], ",".join(r["controls"]["tags"])))
W("  children that are themselves census-shaped (M'_{s'} = n'-2, i.e. a Keller-type top): %s\n" % H(live, lambda r: ch(r)["M_prime"][-1] == ch(r)["n_prime"] - 2))
W("  delta'_{s'} = -1 (Prop 6.3 hypothesis for a second descent): %s\n" % H(live, lambda r: str(F(ch(r)["delta_prime"][-1]))))
W("  d'_{s'} - 3 - ell (= l'' at a simple minor point; needs >= 0 for a polynomial grandchild): %s\n" % H(live, lambda r: ch(r)["d_prime"][ch(r)["s_prime"]-1] - 3 - ch(r)["ell"]))
W("  u' = d'_{s'} - V'_{s'} (multiplicity budget of the child's non-selected top points): %s\n" % H(live, lambda r: ch(r)["d_prime"][ch(r)["s_prime"]-1] - ch(r)["V_prime"][-1]))
W("  d = -delta'_{s'} (source-support constant): %s\n" % H(live, lambda r: str(-F(ch(r)["delta_prime"][-1]))))

W("\n== D. chart sizes (receiver_chart.unknowns_without_T) ==\n")
sz = sorted((r["receiver_chart"]["unknowns_without_T"], r["row_id"], src(r)["u_s"], ch(r)["s_prime"]) for r in live)
W("  min %d (%s), median %d, max %d (%s)\n" % (sz[0][0], sz[0][1], sz[len(sz)//2][0], sz[-1][0], sz[-1][1]))
buckets = Counter(("<70" if s < 70 else "<300" if s < 300 else "<700" if s < 700 else "<1500" if s < 1500 else ">=1500") for s, *_ in sz)
W("  buckets: %s\n" % dict(buckets))
W("  ten smallest: %s\n" % sz[:10])
W("  by (u_s): min/median size u=1: %s  u>1: %s\n" % (
    [x[0] for x in sz if x[2] == 1][:1] + [[x[0] for x in sz if x[2] == 1][len([x for x in sz if x[2] == 1])//2]],
    [x[0] for x in sz if x[2] > 1][:1] + [[x[0] for x in sz if x[2] > 1][len([x for x in sz if x[2] > 1])//2]]))

W("\n== E. families (u_s, s', ell, e:q) with members ==\n")
fam = defaultdict(list)
for r in live:
    c = ch(r); Kp = r["receiver_chart"]["K"]
    fam[(src(r)["u_s"], c["s_prime"], c["ell"], (c["n_prime"] // Kp, c["m_prime"] // Kp))].append(r["row_id"])
for k in sorted(fam, key=lambda k: (k[0], k[1], k[2], k[3])):
    W("  u=%d s'=%d ell=%d (e,q)=%s : %2d  %s\n" % (k[0], k[1], k[2], k[3], len(fam[k]), " ".join(fam[k])))

W("\n== F. split-window status of the 20 prefixes ==\n")
for r in live:
    if r["descent"]["prefix_only"]:
        sw = r["split_window"]
        W("  %s (%d,%d) u=%d v=%d d_s=%d: leaves=%d killed=%d orders=%s status=%s\n" % (r["row_id"], src(r)["n"], src(r)["m"], src(r)["u_s"], src(r)["v_s"], src(r)["d"][src(r)["s"]-1], sw.get("leaf_count"), sw.get("killed_count"), sw.get("orders"), sw.get("status")))
