#!/usr/bin/env python3
"""Fill the remaining placeholders of the lane report from the outputs that exist now."""
import re, subprocess, os
R = os.environ.get("REPORT", "/home/ubuntu/jc2/xmodel/k16-terminal-proof-fable5-20260903.md")
D = "/home/ubuntu/jc2/box/k16terminal-fable5-20260903"
def grab(fn, pat):
    try:
        for line in open(os.path.join(D, fn)):
            m = re.search(pat, line)
            if m: return m
    except FileNotFoundError: pass
    return None
def elapsed(fn):
    m = grab(fn, r"Elapsed.*: (.*)$"); return m.group(1).strip() if m else "n/a"
s = open(os.environ.get("REPORT_IN", R)).read()
# t=7, t=8 modular JPLUS
res = {}
for t, fn, tag in ((7, "an_t7_p32059_r4425.out", "mod 32059, root 4425"), (8, "an_t8_p32003_r11288.out", "mod 32003, root 11288"), (9, "an_t9_p32003_r14748.out", "mod 32003, root 14748")):
    m = grab(fn, r"JPLUS t=%d dim=(\d+) size=(\d+) time=(\d+)" % t)
    r = grab(fn, r"RESZ t=%d dim=(\d+)" % t); p = grab(fn, r"T0HOM_IN_RADICAL power=(\d+)"); tp = grab(fn, r"TOPT_B4_POWER=(\d+)")
    res[t] = (m, r, p, tp, tag, fn)
def row(t, field):
    m, r, p, tp, tag, fn = res[t]
    if m and m.group(1) == "0":
        return "| %d | `%s` | 0 (%s; %s s) | %s | %s | %s | – / – | PROVED-HERE via 5.1 |" % (t, field, tag, m.group(3), p.group(1) if p else "–", r.group(1) if r else "–", (tp.group(1) + " (mod)") if tp else "–")
    if m:
        return "| %d | `%s` | %s (%s) | – | – | – | – | modular nonzero dimension: NON-RESULT (5.1 is one-directional) |" % (t, field, m.group(1), tag)
    return "| %d | `%s` | not finished (%s; host load ~55) | – | – | – | – | INCONCLUSIVE_TIMEOUT; exact rows and `PIVOT_CONTROL` exist |" % (t, field, tag)
s = s.replace("T7_ROW2", row(7, "Q(sqrt6)") + "\n" + row(8, "Q(sqrt3)"))
proved = [t for t in (7, 8, 9) if res[t][0] and res[t][0].group(1) == "0"]
s = s.replace("T78_VERDICT", (" and at `t=%s`" % ",".join(map(str, proved))) if proved else "")
mod_line = []
for t in (7, 8, 9):
    m, r, p, tp, tag, fn = res[t]
    if m: mod_line.append("`t=%d` %s: `JPLUS dim=%s` (%s s)%s" % (t, tag, m.group(1), m.group(3), (", `RESZ dim=%s`" % r.group(1)) if r else ""))
    else: mod_line.append("`t=%d` %s: not finished (INCONCLUSIVE_TIMEOUT)" % (t, tag))
s = s.replace("MOD78_LINE", "Larger `t` (one root each, exact rows for `t=7,8`, modular spine for `t=9`): " + "; ".join(mod_line) + ".")
# t=11
j7 = grab("an_t11_f723_p32003.out", r"JPLUS t=11 dim=(\d+) size=(\d+) time=(\d+)"); j5 = grab("an_t11_f523_p32003.out", r"JPLUS t=11 dim=(\d+) size=(\d+) time=(\d+)")
z7 = grab("rz_t11_f723.out", r"RESZ_ONLY t=11 dim=(\d+) size=(\d+) time=(\d+)"); z5 = grab("rz_t11_f523.out", r"RESZ_ONLY t=11 dim=(\d+) size=(\d+) time=(\d+)")
def st(m): return ("dim=" + m.group(1) + " (" + m.group(3) + " s)") if m else "not finished"
t11 = "cone test `JPLUS` mod 32003: fibre `7/23` %s, fibre `5/23` %s; RESIDUAL-ZERO cone `RESZ` (rows at `b4=0`, ring without `b4`): fibre `7/23` %s, fibre `5/23` %s" % (st(j7), st(j5), st(z7), st(z5))
both_j = j7 and j5 and j7.group(1) == "0" and j5.group(1) == "0"
both_z = z7 and z5 and z7.group(1) == "0" and z5.group(1) == "0"
if both_j: line = "(8.1), hence (T), PROVED-HERE at the split index `t=11` by 5.1 on each rational fibre (%s)" % t11
elif both_z: line = "RESIDUAL-ZERO PROVED-HERE at `t=11` on both fibres by 5.1; the full cone test did not finish (%s), so (8.1) at `t=11` stays open (INCONCLUSIVE_TIMEOUT), the spine itself replayed" % t11
else: line = "spine replayed on both fibres; cone tests %s (INCONCLUSIVE_TIMEOUT where not finished)" % t11
s = s.replace("T11MOD_LINE", line)
s = s.replace("T11MOD_RESULT", "Cone tests on the modular rows: " + t11 + ".  " + ("Both fibres have empty cone, so by 5.1 with `R=Z_(32003)` the characteristic-zero cones are `{0}` on both factors of the product algebra: (8.1) and (T) hold at `t=11`." if both_j else ("By 5.1 RESIDUAL-ZERO holds at `t=11` on both factors; the full cone statement was not reached in the budget." if both_z else "Unfinished tests are typed `INCONCLUSIVE_TIMEOUT`, never a verdict.")))
extra = [str(t) for t in proved] + (["11"] if (both_j or both_z) else [])
s = s.replace("RESZ_MORE", (", and by 5.1 at `t=%s`" % ",".join(extra)) if extra else "")
# manifest
out = subprocess.run(["bash", os.path.join(D, "build_manifest.sh")], capture_output=True, text=True).stdout.strip()
s = s.replace("MANIFEST_LINE", "Final manifest: " + out.replace("MANIFEST_OK ", "") + ".")
open(R, "w").write(s)
print("placeholders left:", [w for w in ("T7_ROW2","T78_VERDICT","T11MOD_LINE","T11MOD_RESULT","MOD78_LINE","RESZ_MORE","MANIFEST_LINE") if w in s], "bytes:", len(s))
print(out)
