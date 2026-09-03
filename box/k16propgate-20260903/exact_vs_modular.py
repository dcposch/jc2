#!/usr/bin/env python3
"""Decisive test of hypothesis (H-gen): the modular rows produced by
laurent_spine.py --modp equal the REDUCTION mod P of the exact rows.
If so, the modular ideal is J.kappa[x] for the SAME generators as J.K[x].
Usage: exact_vs_modular.py t exact_rows modular_rows p r"""
import re, sys
t, ex, mo, p, r = int(sys.argv[1]), sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
def load(path):
    d = {}
    for line in open(path):
        m = re.match(r"T(\d+) = (.*);$", line.strip())
        if m: d[int(m.group(1))] = m.group(2)
    return d
E, M = load(ex), load(mo)
assert sorted(E) == sorted(M) == list(range(2*t)), (sorted(E), sorted(M))
vars_ = "b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
L = ["ring R=%d,(%s),dp;" % (p, vars_)]
for k in range(2*t):
    L.append("poly E%d = %s;" % (k, re.sub(r"\by\b", "(%s)" % r, E[k])))
    L.append("poly M%d = %s;" % (k, M[k]))
    L.append('if (E%d - M%d == 0) { print("ROWMATCH k=%d OK"); } else { print("ROWMATCH k=%d MISMATCH"); }' % (k, k, k, k))
L.append("quit;")
print("\n".join(L))
