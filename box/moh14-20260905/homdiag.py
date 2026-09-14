import json, re, sys
from pathlib import Path
from collections import Counter
meta = json.loads(Path(sys.argv[1]).read_text())
Kp, npr, mpr, ell = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
def w(v):
    m = re.fullmatch(r"h_(\d+)_(\d+)", v)
    if m: return Kp - int(m.group(1)) - int(m.group(2))
    m = re.fullmatch(r"[AB](\d+)_(\d+)_(\d+)", v)
    if m: return int(m.group(1))*Kp - int(m.group(2)) - int(m.group(3))
    if re.fullmatch(r"s\d+", v): return 0
    if v == "c": return npr + mpr - 2 - ell
    raise ValueError(v)
V = meta["variables"]
print("zero-weight vars:", [v for v in V if w(v) == 0][:12], "count", sum(1 for v in V if w(v)==0))
rows_path = Path("/home/ubuntu/jc2")/meta["rows_path"]
term_var = re.compile(r"([A-Za-z_]\w*)(?:\^(\d+))?")
bad = 0; tot = 0; examples = []
with open(rows_path) as f:
    next(f)
    for line in f:
        p = line.rstrip("\n").split("|")
        if len(p) < 5: continue
        hp, xp, yp, e = int(p[1]), int(p[2]), int(p[3]), p[4].strip()
        if e.startswith("(") and e.endswith(")"): e = e[1:-1]
        if len(e) > 4000: continue      # sample the short rows only
        tot += 1
        degs = set()
        for t in re.split(r"(?=[+-])", e.replace(" ", "")):
            if not t or t in "+-": continue
            d = 0
            for name, pw in term_var.findall(t):
                if name.isdigit(): continue
                d += w(name) * (int(pw) if pw else 1)
            degs.add(d)
        want = npr + mpr - 2 - hp*Kp - xp - yp
        if len(degs) != 1 or degs != {want}:
            bad += 1
            if len(examples) < 4: examples.append((p[0], hp, xp, yp, sorted(degs), want))
print("short rows checked:", tot, "inhomogeneous-or-wrong-degree:", bad)
for ex in examples: print("   src=%s (h,x,y)=(%d,%d,%d) term degs %s  expected %d" % ex)
