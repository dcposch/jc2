#!/usr/bin/env python3
"""Compare the lane's spine rows (mod p) with the banked terminal_laurent_t4.json rows (R=-E convention)."""
import json, subprocess, re, sys
import sympy as sp
t, p, root = 4, 32029, 25378
pt = [21, 10, 26, 42]
out = subprocess.run(["python3", "rebuild_pair.py", "4", "--modp", str(p), "--fibre", str(root), "--point", ",".join(map(str, pt))], capture_output=True, text=True).stdout
m = re.search(r"TERMINAL rows T_\{t,k\} \(k=0..7\): \[(.*)\]", out)
T = [int(x) for x in m.group(1).split(",")]
rec = json.load(open("/tmp/jc2-lane.9Mpgn1/inputs/terminal_laurent_t4.json"))
syms = dict(zip(["b3", "b4", "q2_0", "q3_0"], pt)); syms["q9_1"] = root
ok = True
for row in rec["terminal"]:
    k = row["band"]
    val = sp.Rational(sp.sympify(row["expr"]).subs({sp.Symbol(n): v for n, v in syms.items()}))
    vp = (int(val.p) * pow(int(val.q), -1, p)) % p
    mine = (-T[k]) % p
    print("T4_JSON_CONTROL band=%d json_mod_p=%d mine(-T_k)=%d %s" % (k, vp, mine, "OK" if vp == mine else "MISMATCH"))
    ok = ok and vp == mine
print("T4_JSON_ROWS_MATCH_MOD_P=%s (point b3,b4,q2,q3=%s; y=%d mod %d)" % (ok, pt, root, p))
