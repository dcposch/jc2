"""Descend the excess u_s=1 rows of Moh's <=100 census onto the (K,l) lattice.

Descent law (Opus, 17(eeeeee)(2); Moh Prop 6.3/6.4):
   u_s = d_s - V_s,  (n',m') = ((n/d_s)u_s,(m/d_s)u_s),  l = d_s - 1 - 2 u_s.
Rows are the whole-tree-screen survivors beyond Moh's six printed rows
(box/mohprog-drivers-20260903/tree-independent-notes.md, banked 17(ll)).
"""
import sys, itertools
sys.path.insert(0, 'box/mohprog-drivers-20260903')
from independent_enumerator import numerical_skeletons

want = {
 (84,56): [((70,77,82), {2:5,3:10,4:5})],
 (90,60): [((10,45,88), {2:1,3:8,4:4}), ((10,45,88), {2:3,3:8,4:4}),
           ((45,80,88), {2:2,3:5,4:4}), ((45,80,88), {2:3,3:5,4:4})],
 (96,72): [((-60,56,94), {2:1,3:9,4:3}), ((36,80,94), {2:1,3:9,4:3}),
           ((36,80,94), {2:4,3:9,4:3}), ((84,88,94), {2:3,3:9,4:3}),
           ((36,78,94), {2:1,3:1,4:5}), ((36,78,94), {2:1,3:3,4:5}),
           ((36,78,94), {2:4,3:3,4:5})],
 (96,64): [((48,68,94), {2:2,3:1,4:3}), ((48,68,94), {2:1,3:2,4:3}),
           ((48,68,94), {2:3,3:2,4:3}),
           ((-48,-8,20,94), {2:1,3:1,4:6,5:3}),
           ((80,88,92,94), {2:5,3:10,4:5,5:3})],
}
found, missing = [], []
for (n,m), rows in want.items():
    pool = [r for r in numerical_skeletons(n, fixed_m=m)]
    for Ms, V in rows:
        hit = [r for r in pool if tuple(r[2]) == tuple(Ms) and r[3] == V]
        if not hit:
            missing.append((n,m,Ms,V)); continue
        n_,m_,Ms_,V_,d = hit[0]
        s = len(Ms_)+1; ds = d[s]; Vs = V_[s]
        us = ds - Vs
        assert n % ds == 0 and m % ds == 0, (n,m,ds)
        np_, mp_ = (n//ds)*us, (m//ds)*us
        l = ds - 1 - 2*us
        found.append(dict(n=n,m=m,M=Ms,V=V,s=s,d=tuple(d[i] for i in sorted(d)),
                          ds=ds,Vs=Vs,us=us,np=np_,mp=mp_,l=l))
print("matched %d rows, missing %d" % (len(found), len(missing)))
for r in missing: print("   MISSING", r)
print()
hdr = "%-9s %-16s %-22s %-4s %-4s %-3s %-10s %-3s" % ("(n,m)","M","d-chain","d_s","V_s","u_s","(n',m')","l")
print(hdr); print("-"*len(hdr))
for r in sorted(found, key=lambda r:(r['n'],r['m'],r['M'],tuple(sorted(r['V'].items())))):
    print("%-9s %-16s %-22s %-4d %-4d %-3d %-10s %-3d" %
          ("%d,%d"%(r['n'],r['m']), str(r['M']), str(r['d']), r['ds'], r['Vs'], r['us'],
           "(%d,%d)"%(r['np'],r['mp']), r['l']))
cls = {}
for r in found:
    cls.setdefault((r['np'], r['mp'], r['l']), []).append(r)
print("\nDISTINCT DESCENDED CLASSES (n',m',l): %d  from %d rows" % (len(cls), len(found)))
for k, v in sorted(cls.items()):
    K = k[0]//3 if k[0] % 3 == 0 else None
    print("   (n',m',l)=%-14s  x%d   2K'+3l = %s" %
          (str(k), len(v), (2*(k[0]//3)+3*k[2]) if k[0]%3==0 else 'n/a'))
