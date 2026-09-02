import sys, time
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from star import *
import sympy as sp

TRIP = [(2,3,1),(2,5,1),(3,4,1),(3,5,1),(2,7,1),(4,5,1),(3,7,1),(4,7,1),(5,6,1),(5,7,1),(6,7,1),
        (2,3,2),(2,5,2),(2,7,2),(2,3,3),(3,4,2),(2,3,4),(2,5,3)]
print("%-10s %-4s %-4s %-5s %-5s %-9s %-9s %-26s %-11s" %
      ("(d,e,V)","a_1","b_1","#eqs","#unk","#branch","#good","kappa (one witness)","A(p_g),A(p_f)"))
for (d,e,V) in TRIP:
    t0=time.time()
    Q, Pg, eqs, unk, a, b = star_system(d,e,V)
    eqs = [q for q in eqs if q != 0]
    sol = [{}] if not eqs else sp.solve(eqs, unk, dict=True)
    good = []
    for s in sol:
        Qs = sp.expand(Q.subs(s)); Ps = sp.expand(Pg.subs(s))
        free = sorted((Qs.free_symbols | Ps.free_symbols) - {pi_}, key=str)
        for val in (1, 2, -1, 3):
            sub = {f: val for f in free}
            Q2 = sp.expand(Qs.subs(sub)); P2 = sp.expand(Ps.subs(sub))
            okc, kap, degC, expC, s1, s2, s3 = verify(d,e,V,Q2,P2)
            if okc and kap != 0 and degC == expC and s1 and s2 and s3:
                good.append((Q2,P2,kap)); break
    if good:
        Q2,P2,kap = good[0]
        Am, Aq = symmetry_order(P2), symmetry_order(Q2)
    else:
        Am=Aq=None; kap=None
    print("%-10s %-4d %-4d %-5d %-5d %-9d %-9d %-26s %-11s  [%.1fs]" %
          (str((d,e,V)), a, b, len(eqs), len(unk), len(sol), len(good), str(kap), "%s,%s"%(Am,Aq), time.time()-t0))
    if good and b <= 4:
        print("      p_g =", sp.factor(good[0][1]), "   p_f =", sp.factor(good[0][0]))
    sys.stdout.flush()
