#!/usr/bin/env python3
"""Ring-map control: same tests with y an ordinary variable and H_t an ideal generator over Q."""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("t", type=int); ap.add_argument("rows")
a = ap.parse_args(); t = a.t; q = 2*t+1
rows = {}
for line in open(a.rows):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
vars_ = "y,b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
L = ["ring R=0,(%s),(dp(1),wp(%s));" % (vars_, ",".join(map(str, [t+1, 1] + list(range(2, t))))),
     "poly H = %d*y^2%+d*y%+d;" % (12*q*q, -12*q*(t+1), (t+1)*(3*t+2)), "option(redSB);"]
for k in range(2*t):
    L.append("poly T%d = %s;" % (k, rows[k].replace("(", "(").replace(")", ")")))
L.append("poly T0hom = T0 - subst(T0, b3,0, b4,0%s);" % "".join(", q(%d),0" % j for j in range(2, t)))
L.append("ideal Jp = H," + ",".join("T%d" % k for k in range(1, 2*t)) + ";")
L.append("ideal G = std(Jp); print(\"RINGMAP JPLUS t=%d dim=\" + string(dim(G)) + \" vdim=\" + string(vdim(G)));" % t)
L.append('int NN; poly pw = 1; for (NN=1; NN<=40; NN++) { pw = pw*T0hom; if (reduce(pw, G) == 0) { print("RINGMAP T0HOM power=" + string(NN)); break; } }')
L.append("ideal Gr = std(ideal(H, " + ",".join("T%d" % k for k in range(1, 2*t)) + ", b4)); print(\"RINGMAP RESZ dim=\" + string(dim(Gr)) + \" vdim=\" + string(vdim(Gr)));")
L.append("ideal Gt = std(ideal(H, " + ",".join("T%d" % k for k in range(t, 2*t)) + ")); pw = 1; for (NN=1; NN<=80; NN++) { pw = pw*b4; if (reduce(pw, Gt) == 0) { print(\"RINGMAP TOPT b4 power=\" + string(NN)); break; } }")
L.append("quit;")
print("\n".join(L))
