#!/usr/bin/env python3
"""Audit of the joint Q* pivot ledgers and their closed-form re-derivation
from the Jacobian band mechanism.  Secs 5 and 6.2."""
import json
from fractions import Fraction as Fr
import sympy as sp
LED = (("delta52", "/home/ubuntu/jc2/box/g9966s8-20260903/runs/delta52/stage8.json"),
       ("delta2",  "/home/ubuntu/jc2/box/g9966band-20260903/runs/delta2/stage4.json"))
led = {}
for tag, path in LED:
    pl = json.load(open(path))['joint_elimination']['pivot_ledger']
    bad = [e for e in pl if Fr(e['coefficient']) == 0]
    forb = [e['variable'] for e in pl if e['variable'] in ('rho','c','u','v')]
    print("%s : %d joint Q* pivots ; all coefficients nonzero rational: %s ; "
          "pivot blocks %s ; pivots on rho/c/u/v: %s"
          % (tag, len(pl), not bad,
             sorted({e['variable'].split('_')[0] for e in pl}),
             forb if forb else "none"))
    for e in pl:
        led[(tag, e['row'])] = (e['variable'], Fr(e['coefficient']))
print()
w = sp.Symbol('w'); A0 = w**9*(w-1)**24
D1_killed = {(3, 21), (7, 18)}          # outer D_1 offset-0 block, weight 93
def b1_qs(r): return [q for q in range(33) if 3*r+4*q >= 93 and r+q <= 32]
ok = tot = 0
print("closed form from  [t^n]KJ = A0^3 (99 A0 dB/dw - (99-3n) B dA0/dw),"
      "  A0 = w^9(w-1)^24 :")
for n in range(1, 9):
    r = n-1
    qs = [q for q in b1_qs(r) if (r, q) not in D1_killed]
    b = {q: sp.Symbol('b%d' % q) for q in qs}
    B = sum(b[q]*(w-1)**q for q in qs)
    P = sp.Poly(sp.expand(A0**3*(99*A0*sp.diff(B, w) - (99-3*n)*B*sp.diff(A0, w))), w)
    subs = {}
    line = []
    for i, q in enumerate(qs):
        row = sp.expand(P.coeff_monomial(w**(35+i)).subs(subs))
        co = sp.expand(row).coeff(b[q])
        subs[b[q]] = sp.expand(-(row - co*b[q])/co)
        lbl = "stage%d_J_d%d_k%d" % (n, 163-n, 35+i)
        ent = led.get(("delta52", lbl)); tot += 1
        match = ent is not None and ent[0] == "B1c_%d_%d" % (r, q) and Fr(int(co)) == ent[1]
        ok += match
        assert abs(int(co)) == 9*(99 - 3*n - 11*i), (n, i, co)
        line.append("%d" % int(co))
    print("   n=%d  q=%d..%d  coefficients %s" % (n, qs[0], qs[-1], " ".join(line)))
print("\nreproduced %d of %d delta=5/2 joint Q* pivot coefficients" % (ok, tot))
print("all satisfy |coeff| = 9(99 - 3n - 11 i) ; zero would need 11 | 3n, i.e. 11 | n,"
      " impossible for 1 <= n <= 8")
d2 = [(l, v, c) for (t_, l), (v, c) in led.items() if t_ == "delta2"]
same = sum(1 for l, v, c in d2 if l.startswith("stage") and "_J_" in l)
print("delta=2 ledger: %d pivots, of which %d are J-band rows obeying the same formula;"
      % (len(d2), same))
print("   the other %d are the G pole rows G_local5..8_coord0 with coefficients %s"
      % (len(d2)-same, [str(c) for l, v, c in sorted(d2) if "_G_" in l]))
