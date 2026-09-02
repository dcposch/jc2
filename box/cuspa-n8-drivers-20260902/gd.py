import sys, itertools, pickle, math; sys.path.insert(0,'/tmp/cuspa')
from ledger import *
from collections import Counter

S=pickle.load(open('/tmp/cuspa/surv.pkl','rb'))
print("== (G-D) trefoil cell: image group and base orbifold")
r=full_record(*[S[(2,3)][0][k] for k in ('A','B','p','q')])
A,B,p,q=r['A'],r['B'],r['p'],r['q']
n=grp_order([A,B],8); print("   |rho(G)| =",n)
z=ppow(A,p)
# structure: center, quotient
seen={pid(8)}; st=[pid(8)]
while st:
    g=st.pop()
    for h in (A,B):
        x=perm_mul(h,g)
        if x not in seen: seen.add(x); st.append(x)
G=sorted(seen)
cen=[g for g in G if all(perm_mul(g,h)==perm_mul(h,g) for h in G)]
print("   |Z(rho(G))| =",len(cen), " orders of elements:",
      Counter(sorted((lambda g: next(k for k in range(1,25) if ppow(g,k)==pid(8)))(g) for g in G)))
print("   rho(alpha) order",next(k for k in range(1,25) if ppow(A,k)==pid(8)),
      " rho(beta) order",next(k for k in range(1,25) if ppow(B,k)==pid(8)))
# blocks + induced orbifold data
blocks=orbits([z],8); bidx={}
for i,b in enumerate(blocks):
    for x in b: bidx[x]=i
ind=lambda g: tuple(bidx[g[next(iter(b))]] for b in blocks)
bA,bB=ind(A),ind(B)
g_,e,f=ext(q,p); m=perm_mul(ppow(A,e),ppow(B,f)); bm=ind(m)
print("   blocks M=%d kappa=%d ; bar-alpha %s  bar-beta %s  bar-m %s"
      % (len(blocks), 8//len(blocks), ctype(bA),ctype(bB),ctype(bm)))
print("   p-side local degrees m_i=%s cone orders p/m_i=%s"
      % (ctype(bA), tuple(p//x for x in ctype(bA))))
print("   q-side local degrees l_j=%s cone orders q/l_j=%s"
      % (ctype(bB), tuple(q//x for x in ctype(bB))))
print("   c=#cyc(bar m)=%d  => genus g=(j-c)/2=%d ; O' = genus %d, %d boundary circles"
      % (len(cycles(bm)), (r['j']-len(cycles(bm)))//2, (r['j']-len(cycles(bm)))//2, len(cycles(bm))))

print()
print("== (3,4) cell orbifold")
r2=full_record(*[S[(3,4)][0][k] for k in ('A','B','p','q')])
A,B,p,q=r2['A'],r2['B'],r2['p'],r2['q']; z=ppow(A,p)
blocks=orbits([z],8); bidx={}
for i,b in enumerate(blocks):
    for x in b: bidx[x]=i
ind=lambda g: tuple(bidx[g[next(iter(b))]] for b in blocks)
g_,e,f=ext(q,p); m=perm_mul(ppow(A,e),ppow(B,f))
print("   M=%d kappa=%d bar-alpha %s bar-beta %s bar-m %s ; cone orders p:%s q:%s ; c=%d"
      % (len(blocks),8//len(blocks),ctype(ind(A)),ctype(ind(B)),ctype(ind(m)),
         tuple(p//x for x in ctype(ind(A))), tuple(q//x for x in ctype(ind(B))),
         len(cycles(ind(m)))))

print()
print("== MEASURED SWEEP of the two gates, N<=6, gcd(p,q)=1, p,q<=7")
rows=[]
for N in (2,3,4,5,6):
    perms=list(itertools.permutations(range(N)))
    for p in range(2,8):
        for q in range(2,8):
            if math.gcd(p,q)!=1: continue
            for A in perms:
                tA=ppow(A,p)
                for B in perms:
                    if ppow(B,q)!=tA: continue
                    if not is_transitive([A,B],N): continue
                    try: r=full_record(A,B,p,q)
                    except Exception: continue
                    if r['tors']: continue
                    if not (2<=r['a']<=N-2): continue
                    if not (2<=r['j']<=r['a']): continue
                    per = (r['t']==r['j']); msp = (r['j']*r['kappa']<=r['a'])
                    rows.append((N,p,q,r['kappa'],r['j'],r['a'],per,msp,per and msp))
print("   candidate reps passing torsion-free + a-window + 2<=j<=a :", len(rows))
print("   passing PERIPHERAL-RANK          :", sum(1 for x in rows if x[6]))
print("   passing MERIDIAN-SPAN            :", sum(1 for x in rows if x[7]))
print("   passing BOTH (theorem says none) :", sum(1 for x in rows if x[8]))
