#!/usr/bin/env python3
"""Emit a Singular job for the z-type (tau=0) part of the t=8 cone: Jz = <T_1..T_15, T0hom> in the
weighted ring mod 32003 (root 11288 of H_8), rows from Fable's exact spine reduced mod p (frozen file
box/k16terminal-fable5-20260903/t8_p32003_r11288_rows.txt).  Sizes are written (flushed) before std.
mode full : homogeneous z-system;   mode b4zero : slice b4=0 (RESIDUAL-ZERO plus tau);"""
import re, sys
t = 8; mode = sys.argv[1]; rows_path = sys.argv[2]; log = sys.argv[3]; tmo = sys.argv[4] if len(sys.argv) > 4 else "0"
rows = {}
for line in open(rows_path):
    m = re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))] = m.group(2)
assert sorted(rows) == list(range(2 * t))
vars_ = "b3,b4" + "".join(",q(%d)" % j for j in range(2, t))
wts = [t + 1, 1] + list(range(2, t))
L = ["ring R=32003,(%s),wp(%s);" % (vars_, ",".join(map(str, wts))), "intvec W=%s;" % ",".join(map(str, wts)), "option(redSB);"]
for k in range(2 * t): L.append("poly T%d = %s;" % (k, rows[k]))
L.append("poly T0hom = T0 - subst(T0, b3,0, b4,0%s);" % "".join(", q(%d),0" % j for j in range(2, t)))
L.append('write(":a %s", "T0CONST=" + string(T0 - T0hom));' % log)
for k in range(1, 2 * t):
    L.append('write(":a %s", "ROW k=%d terms=" + string(size(T%d)) + " wdeg=" + string(deg(T%d, W)) + " b4zero_terms=" + string(size(subst(T%d, b4, 0))));' % (log, k, k, k, k))
L.append('write(":a %s", "ROW k=0hom terms=" + string(size(T0hom)) + " wdeg=" + string(deg(T0hom, W)) + " b4zero_terms=" + string(size(subst(T0hom, b4, 0))));' % log)
if mode == "full":
    L.append("ideal Jz = " + ",".join("T%d" % k for k in range(1, 2 * t)) + ", T0hom;")
    L.append('write(":a %s", "ZSYS t=8 generators=" + string(size(Jz)) + " variables=%d timeout=%s");' % (log, t, tmo))
    L.append('int tt = timer; ideal G = std(Jz); write(":a %s", "ZSYS_FULL t=8 dim=" + string(dim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt));' % log)
elif mode == "b4zero":
    L.append("ideal Jz = " + ",".join("subst(T%d, b4, 0)" % k for k in range(1, 2 * t)) + ", subst(T0hom, b4, 0), b4;")
    L.append('write(":a %s", "ZSLICE_B4ZERO t=8 generators=" + string(size(Jz)) + " timeout=%s");' % (log, tmo))
    L.append('int tt = timer; ideal G = std(Jz); write(":a %s", "ZSYS_B4ZERO t=8 dim=" + string(dim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt));' % log)
# --- appended modes (b4one, resz) ---
if mode in ("b4one", "resz"):
    L = L[:-1]  # drop quit
    if mode == "b4one":
        L.append("ideal Jo = " + ",".join("subst(T%d, b4, 1)" % k for k in range(1, 2 * t)) + ", subst(T0hom, b4, 1), b4-1;")
        L.append('write(":a %s", "ZCHART_B4ONE t=8 generators=" + string(size(Jo)) + " timeout=%s");' % (log, tmo))
        L.append('int tt = timer; ideal G = std(Jo); if (reduce(1, G) == 0) { write(":a %s", "ZCHART_B4ONE t=8 UNIT time=" + string(timer-tt)); } else { write(":a %s", "ZCHART_B4ONE t=8 NONUNIT dim=" + string(dim(G)) + " vdim=" + string(vdim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt)); write(":a %s", "ZCHART_B4ONE_LEAD=" + string(lead(G))); if (vdim(G) > 0 and vdim(G) < 40) { write(":a %s", "ZCHART_B4ONE_BASIS=" + string(G)); } }' % (log, log, log, log))
    else:
        L.append("ideal Jr = " + ",".join("T%d" % k for k in range(1, 2 * t)) + ", b4;")
        L.append('write(":a %s", "RESZ t=8 generators=" + string(size(Jr)) + " timeout=%s");' % (log, tmo))
        L.append('int tt = timer; ideal G = std(Jr); write(":a %s", "RESZ t=8 dim=" + string(dim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt));' % log)
    L.append("quit;")
    import sys as _s

if mode == "topt":
    L = L[:-1]
    L.append("ideal Jt = " + ",".join("T%d" % k for k in range(t, 2 * t)) + ";")
    L.append('write(":a %s", "TOPT t=8 generators=" + string(size(Jt)) + " (rows T_8..T_15, homogeneous, 8 variables) timeout=%s");' % (log, tmo))
    L.append('int tt = timer; ideal G = std(Jt); write(":a %s", "TOPT t=8 dim=" + string(dim(G)) + " size=" + string(size(G)) + " time=" + string(timer-tt)); write(":a %s", "TOPT_LEAD=" + string(lead(G)));' % (log, log))
    L.append('int NN; poly pw = 1; int found = 0; for (NN=1; NN<=200; NN++) { pw = pw*b4; if (reduce(pw, G) == 0) { write(":a %s", "TOPT_B4_POWER=" + string(NN)); found = 1; break; } } if (found == 0) { write(":a %s", "TOPT_B4_NOT_FOUND_UP_TO=200"); }' % (log, log))
    L.append("quit;")
if mode not in ("full", "b4zero", "b4one", "resz", "topt"):
    raise SystemExit("unknown mode")
if mode in ("full", "b4zero"):
    pass
print("\n".join(L))
