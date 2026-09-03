#!/usr/bin/env python3
"""Mechanism-by-mechanism census of TEST-55(k) (delta_2' = -1 rows)."""
import sys, os
from math import gcd
from fractions import Fraction as F
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prop55k import test55k

def sweep(k, NMAX=60):
    rows=[]
    for n in range(3, NMAX+1):
        for m in range(2, n):
            d2 = gcd(n,m)
            if d2 < 2: continue
            M2 = n - k - 2
            if M2 <= -m: continue
            for V2 in range(1, d2+1):
                r = test55k(n,m,M2,V2,k)
                if r["kills"] and r["kills"][0].startswith("H-"): continue
                rows.append(r)
    return rows

MECH = ["GALOIS", "A5-SIMPLE", "MONOMIAL", "DIVCHAIN", "MASTER"]
print("delta_2' = -1 (R = k+1), n' <= 60, all m' with gcd >= 2, all admissible V_2'")
print("  k  rows  A'=1  killed   %      GALOIS  A5-SIMPLE MONOMIAL DIVCHAIN MASTER | XOR-holds-but-killed | survivors")
for k in range(0, 9):
    rows = sweep(k)
    triv = [r for r in rows if r["verdict"].startswith("INAPPLIC")]
    live = [r for r in rows if not r["verdict"].startswith("INAPPLIC")]
    killed = [r for r in live if r["verdict"]=="KILLED"]
    c = Counter()
    for r in killed:
        for kk in r["kills"]:
            c[kk.split(":")[0]] += 1
    # rows where Moh's XOR *does* hold (so his chain is the only route)
    xor = [r for r in live if (r["res"][0]==0) != (r["res"][1]==0)]
    xor_killed = [r for r in xor if r["verdict"]=="KILLED"]
    print("  %2d %5d %5d %6d %6.1f%%   %6d %9d %8d %8d %6d | %6d / %-6d | %5d"
          % (k, len(rows), len(triv), len(killed), 100.0*len(killed)/max(len(live),1),
             c["GALOIS"], c["A5-SIMPLE"], c["MONOMIAL"], c["DIVCHAIN"], c["MASTER"],
             len(xor_killed), len(xor), len(live)-len(killed)))

print("\n-- k=0: does Moh's XOR ever hold on an admissible row? (his chain's domain) --")
rows = sweep(0, 120)
live=[r for r in rows if not r["verdict"].startswith("INAPPLIC")]
xor=[r for r in live if (r["res"][0]==0)!=(r["res"][1]==0)]
print("   admissible k=0 rows n'<=120: %d ; XOR holds on %d of them" % (len(live), len(xor)))
for r in xor[:8]:
    print("     (n',m')=(%d,%d) V2'=%d d2'=%d A'=%d res=%s kills=%s"
          % (r["n"],r["m"],r["V2"],r["d2"],r["A"],r["res"],[x.split(":")[0] for x in r["kills"]]))
print("   of those, killed by the DIVCHAIN/MASTER (Moh's inequality): %d"
      % sum(1 for r in xor if any(x.startswith(("DIVCHAIN","MASTER")) for x in r["kills"])))
print("   of those, killed by A5-SIMPLE alone (new): %d"
      % sum(1 for r in xor if any(x.startswith("A5-SIMPLE") for x in r["kills"])
            and not any(x.startswith(("DIVCHAIN","MASTER","GALOIS")) for x in r["kills"])))

print("\n-- survivors at k=1,2 (n'<=40): the residual Diophantine set --")
for k in (1,2):
    rows=[r for r in sweep(k,40) if r["verdict"]=="SURVIVES"]
    print("   k=%d : %d survivors; first 12:" % (k, len(rows)))
    for r in rows[:12]:
        print("     (n',m')=(%2d,%2d) M2'=%2d V2'=%d d2'=%d  d1'=%-6s A'=%-2d res=%s "
              "g0=%s Psi=%s  d2'<=(k+1)V2': %s"
              % (r["n"],r["m"],r["M2"],r["V2"],r["d2"],r["delta1"],r["A"],r["res"],
                 r.get("g0"),r.get("Psi"), r["d2"] <= (k+1)*r["V2"]))
