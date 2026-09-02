import sys
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from starnum import *
from mpmath import mp, fabs, mpf
import time
TRIP = []
for (d,e) in [(2,3),(2,5),(2,7),(3,4),(3,5),(3,7),(4,5),(4,7),(5,6),(5,7),(6,7)]:
    for V in range(1, 7): TRIP.append((d,e,V))
print("%-11s %-4s %-4s %-6s %-9s %-9s %-11s %-11s %-8s" %
      ("(d,e,V)","a_1","b_1","#eqs","kappa!=0","W const","degC/exp","min sep P,Q,C","verdict"))
for (d,e,V) in TRIP:
    b = d*V
    if b > 22: continue
    t0=time.time()
    Pc, Qc, q = solve_star(d,e,V, tries=40, seed=7)
    if Pc is None:
        print("%-11s %-4d %-4d %-6d %-9s %-9s %-11s %-11s %-8s [%.1fs]" %
              (str((d,e,V)), e*V, b, max(0,b-2), "-","-","-","-","NO WITNESS", time.time()-t0))
        sys.stdout.flush(); continue
    const, kap, degC, expC, sP, sQ, sC = verify(Pc,Qc,d,e,V)
    good = const and fabs(kap) > mpf(10)**(-20) and degC==expC and min(sP,sQ,sC) > mpf(10)**(-20)
    print("%-11s %-4d %-4d %-6d %-9s %-9s %-11s %-11s %-8s [%.1fs]" %
          (str((d,e,V)), e*V, b, max(0,b-2), "%.2e"%float(fabs(kap)), str(const),
           "%d/%d"%(degC,expC), "%.1e"%float(min(sP,sQ,sC)),
           "REALISED" if good else "FAIL", time.time()-t0))
    sys.stdout.flush()
