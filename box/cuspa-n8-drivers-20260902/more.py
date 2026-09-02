import sys, itertools, pickle, math; sys.path.insert(0,'/tmp/cuspa')
from ledger import *

print("== CONTROL N=1 (trivial rho, H=G, E=A_F): gate must PASS")
r=full_record((0,),(0,),2,3)
print("   j=%d a=%d kappa=%d ndist=%d det=%s  -> MERIDIAN-BASIS %s"
      % (r['j'],r['a'],r['kappa'],r['ndist'],r['basis_det'],
         r['ndist']==r['j'] and abs(r['basis_det'])==1))

print()
print("== PREDICTION CHECK  ndist == n_0 = a/kappa  on every N=8 survivor")
S=pickle.load(open('/tmp/cuspa/surv.pkl','rb'))
bad=0; tot=0
for key in S:
    for r0 in S[key]:
        r=full_record(r0['A'],r0['B'],r0['p'],r0['q']); tot+=1
        if r['ndist']!=r['a']//r['kappa']: bad+=1
print("   %d records, mismatches: %d" % (tot,bad))

print()
print("== N=9 spot cell (sweep F9.1: p=2,q=3, M=3, kappa=3, j=2, a=3, mer=(6))")
N=9
found=[]
A0=None
for A in itertools.permutations(range(N)):
    if ctype(A)!=(6,3): continue
    A0=A; break
tgt=ppow(A0,2)
for B in itertools.permutations(range(N)):
    if ctype(B)!=(9,): continue
    if ppow(B,3)!=tgt: continue
    if not is_transitive([A0,B],N): continue
    r=full_record(A0,B,2,3)
    if r['tors'] or r['j']<2 or r['j']>r['a'] or not(2<=r['a']<=N-2): continue
    if grp_order([A0,B],N)<=N: continue
    found.append(r)
print("   survivors at this cell: %d" % len(found))
if found:
    r=found[0]
    print("   j=%d a=%d kappa=%d M=%d mer=%s c=%d t=%d ndist=%d n0=%d"
          % (r['j'],r['a'],r['kappa'],r['M'],r['mer_type'],r['c'],r['t'],
             r['ndist'],r['a']//r['kappa']))
    print("   PERIPHERAL-RANK t=j : %s ;  MERIDIAN-SPAN j<=a/kappa : %s"
          % (r['t']==r['j'], r['j'] <= r['a']//r['kappa']))
