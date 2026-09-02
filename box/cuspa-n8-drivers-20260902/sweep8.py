import sys, itertools, math; sys.path.insert(0,'/tmp/cuspa')
from ledger import (pid, ppow, cycles, ctype, nfix, orbits, grp_order, ext)
from cover_h1 import cover_h1, to_transport_convention, perm_mul, perm_inv, is_transitive
from sweep import light, types, rep_of
N=8
perms=list(itertools.permutations(range(N)))
powcache={}
for q in range(2,8):
    d={}
    for B in perms: d.setdefault(ppow(B,q),[]).append(B)
    powcache[q]=d
tot=per=msp=both=0; prof={}
for p in range(2,8):
    for q in range(2,8):
        if math.gcd(p,q)!=1: continue
        for ct in types(N):
            A=rep_of(ct,N); tA=ppow(A,p)
            for B in powcache[q].get(tA,()):
                r=light(A,B,p,q,N)
                if r is None: continue
                tot+=1; per+=r['per']; msp+=r['msp']
                key=(p,q,r['kappa'],r['j'],r['a'],r['t'],r['per'],r['msp'])
                prof[key]=prof.get(key,0)+1
                if r['per'] and r['msp']: both+=1
print("N=8, p,q<=7 coprime, alpha normalised to a cycle-type representative")
print("  candidates (transitive, relation, a-window, torsion-free H^ab, 2<=j<=a, nonregular):",tot)
print("  PERIPHERAL-RANK pass:",per,"  MERIDIAN-SPAN pass:",msp,"  BOTH:",both)
for k,v in sorted(prof.items()): print("   %3d x (p,q)=(%d,%d) kappa=%d j=%d a=%d t=%d PER=%s MSP=%s"%(v,)+"" if False else "   %3d x (p,q)=(%d,%d) kappa=%d j=%d a=%d t=%d PER=%s MSP=%s"%((v,)+k))
