#!/usr/bin/env python3
"""RESIDUAL-ZERO cone test only: rows at b4=0 in the ring without b4 (weights 2..t-1, t+1)."""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("t", type=int); ap.add_argument("rows"); ap.add_argument("--modp", type=int, required=True)
a = ap.parse_args(); t = a.t
rows = {}
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
vars_ = "b3" + "".join(",q(%d)" % j for j in range(2, t))
wts = [t+1] + list(range(2, t))
L = ["ring R0=%d,(b3,b4%s),wp(%s);" % (a.modp, "".join(",q(%d)" % j for j in range(2, t)), ",".join(map(str, [t+1, 1] + list(range(2, t))))), "ideal Z;"]
for k in range(1, 2*t): L.append("Z[%d] = subst(%s, b4, 0);" % (k, rows[k]))
L.append("ring R=%d,(%s),wp(%s);" % (a.modp, vars_, ",".join(map(str, wts))))
L.append("ideal Z = imap(R0, Z); option(redSB); int tt = timer; ideal G = std(Z);")
L.append('print("RESZ_ONLY t=%d dim=" + string(dim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt)); print("RESZ_ONLY_LEAD=" + string(lead(G))); quit;' % t)
print("\n".join(L))
