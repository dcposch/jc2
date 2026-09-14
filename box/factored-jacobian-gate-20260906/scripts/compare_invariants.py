#!/usr/bin/env python3
import sys, json
from fractions import Fraction
from pathlib import Path
OUT = Path('/home/ubuntu/factored-jacobian-review-20260906')
def canon(m):
    if m == '1': return ()
    out = []
    for f in m.split('*'):
        if '^' in f: n, e = f.split('^'); out.append((n, int(e)))
        else: out.append((f, 1))
    return tuple(sorted(out))
fl = {}
for line in (OUT/'flint_row_invariants.tsv').read_text().splitlines()[1:]:
    k, lab, t, d, lc, lm, tc, tm = line.split('\t'); fl[int(k)] = (int(t), int(d), Fraction(lc), canon(lm), Fraction(tc), canon(tm))
sg = {}; markers = []
for line in (OUT/'singular_invariants.txt').read_text().splitlines():
    parts = line.split(' ')
    if len(parts) == 7 and parts[0].isdigit(): k, t, d, lc, lm, tc, tm = parts; sg[int(k)] = (int(t), int(d), Fraction(lc), canon(lm), Fraction(tc), canon(tm))
    else: markers.append(line)
mism = [k for k in fl if sg.get(k) != fl[k]]
r = {"flint_rows": len(fl), "singular_rows": len(sg), "mismatches": mism[:20], "n_mismatch": len(mism), "markers": markers,
     "ok": len(fl) == len(sg) == 1629 and not mism}
(OUT/'invariants_compare.json').write_text(json.dumps(r, indent=1)+'\n'); print(json.dumps(r))
