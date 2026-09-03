#!/usr/bin/env python3
"""Discovery only: reduce exact number-field rows mod p with y -> a root of H_t mod p, emit analyze script.
Usage: modular_from_exact.py t rows p  (prints chosen root(s); emits an_t{t}_p{p}_r{root}.sing for each root)."""
import re, sys, subprocess
t, path = int(sys.argv[1]), sys.argv[2]
q = 2*t+1
roots = []
for p in [int(x) for x in sys.argv[3:]]:
    H = lambda y: (12*q*q*y*y - 12*q*(t+1)*y + (t+1)*(3*t+2)) % p
    roots = [r for r in range(p) if H(r) == 0]
    if roots: break
if not roots: sys.exit("H_%d has no root mod the given primes" % t)
print("PRIME", p)
txt = open(path).read()
for r in roots:
    out = path.replace("_rows.txt", "_p%d_r%d_rows.txt" % (p, r))
    open(out, "w").write(re.sub(r"\by\b", "(%d)" % r, txt))
    sing = "an_t%d_p%d_r%d.sing" % (t, p, r)
    subprocess.run(["python3", "analyze_rows.py", str(t), out, "--fibre", str(r), "--modp", str(p), "--nmax", "200"], stdout=open(sing, "w"), check=True)
    print("ROOT", r, "->", sing)
