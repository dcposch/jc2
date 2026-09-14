"""Scan pairs (f,g) with deg g = deg_y g = n and deg_x g = n' < n, computing BOTH
Moh p.150 characteristic data (y-side = Moh's own; x-side = the child's, see report Sec.3)."""
import sys, json, random, itertools
sys.path.insert(0,'/home/ubuntu/jc2/box/child-top-us2-20260905')
from fastchar import chardata_poly
from fractions import Fraction as F
from math import gcd

X0 = [F(7), F(103,5), F(-31,3)]

def eff(cd):
    """p.174 Definition-Remark: drop M_h if M_h = n-1.  Returns (s, effective M list, dropped?)"""
    n=cd['n']; M=[v for v in cd['M'] if v is not None]
    if cd['truncated']: return None
    dropped=False
    if M and M[-1]==n-1: M=M[:-1]; dropped=True
    return len(M), M, dropped

def both(f,g):
    outs=[]
    for x0 in X0:
        cy=chardata_poly(f,g,True,x0); cx=chardata_poly(f,g,False,x0)
        outs.append((tuple(cy['M']),tuple(cy['d']),tuple(cx['M']),tuple(cx['d']),cy['n'],cy['m'],cx['n'],cx['m'],cy['truncated'],cx['truncated']))
    if len(set(outs))!=1: return None            # specialisation-unstable: discard
    cy=chardata_poly(f,g,True,X0[0]); cx=chardata_poly(f,g,False,X0[0])
    return cy,cx

def analyse(f,g,label):
    r=both(f,g)
    if r is None: return None
    cy,cx=r
    e=eff(cy)
    if e is None: return None
    s,Ms,dropped=e
    if s<1: return None
    n=cy['n']; nt=cx['n']; ds=cy['d']
    if s>len(ds)-1: return None
    d_s=ds[s]                                    # cy['d'] = [d_1,d_2,...]; d_{s} sits at index s-1
    d_s=ds[s-1]
    if nt<1 or nt>=n: return None
    if (nt*d_s)%n!=0: return None                # u_s must be an integer
    us=nt*d_s//n
    if us<1: return None
    Mx=[v for v in cx['M'] if v is not None]
    if cx['truncated']: return None
    pred=[F(Mi*us,d_s) for Mi in Ms[:s-1]]
    low_ok = len(Mx)>=s-1 and all(p.denominator==1 and int(p)==o for p,o in zip(pred,Mx[:s-1]))
    dx=cx['d']
    return dict(label=label,n=n,m=cy['m'],M=cy['M'],d=ds,s=s,d_s=d_s,dropped=dropped,
                delta_s_eq_m1=(Ms[-1]==n-2), nt=nt,mt=cx['m'],Mx=cx['M'],dx=dx,u_s=us,
                low_ok=low_ok,extra=Mx[s-1:],nt1=nt-1,
                extra_is_nt1=(len(Mx)==s and Mx[s-1]==nt-1) if len(Mx)>=s else None,
                dx_s=dx[s-1] if len(dx)>=s else None)

def mk(terms):
    d={}
    for (i,j,c) in terms: d[(i,j)]=d.get((i,j),F(0))+F(c)
    return {k:v for k,v in d.items() if v!=0}

from math import comb
LEAD={}
for n_ in range(4,13):
    for U_ in range(2,n_):
        V_=n_-U_
        LEAD[(V_,U_)]=[(i, V_+U_-i, comb(U_,i)*(-1)**i) for i in range(U_+1)]

random.seed(11)
res=[]
seen=set()
for n in range(4,11):
    for U in range(2,n):           # U = deg_x g
        V=n-U
        if V<1: continue
        for trial in range(60):
            # g = y^V (y - x)^U  +  lower total degree, deg_x <= U
            terms=list(LEAD[(V,U)])
            for _ in range(random.randint(1,4)):
                tot=random.randint(1,n-1); i=random.randint(0,min(U,tot)); j=tot-i
                terms.append((i,j,random.choice([-3,-2,-1,1,2,3])))
            g=mk(terms)
            m=random.randint(1,n-1); mt=random.randint(1,max(1,U))
            ft=[]
            ft.append((0,m,1))
            for _ in range(random.randint(1,4)):
                i=random.randint(0,mt); j=random.randint(0,m)
                ft.append((i,j,random.choice([-3,-2,-1,1,2,3])))
            ft.append((mt,random.randint(0,m-1) if m>1 else 0,random.choice([1,2,-1])))
            f=mk(ft)
            key=(tuple(sorted(g.items())),tuple(sorted(f.items())))
            if key in seen: continue
            seen.add(key)
            try: r=analyse(f,g,f'n{n}U{U}t{trial}')
            except Exception: continue
            if r is None: continue
            res.append(r)
json.dump(res,open('/home/ubuntu/jc2/box/child-top-us2-20260905/scan.json','w'),indent=0,default=str)
print('pairs analysed:',len(res))
good=[r for r in res if r['low_ok'] and r['u_s']>=2]
print('u_s>=2 with the banked low-level law holding:',len(good))
import collections
print('  extra==n\'-1 ?',collections.Counter(str(r['extra_is_nt1']) for r in good))
print('  d\'_s == u_s ?',collections.Counter(str(r['dx_s']==r['u_s']) for r in good))
for r in good[:25]:
    print(f"  n={r['n']} m={r['m']} M={r['M']} d={r['d']} s={r['s']} d_s={r['d_s']} Ms=n-2:{r['delta_s_eq_m1']} "
          f"|| n'={r['nt']} m'={r['mt']} u_s={r['u_s']} M'={r['Mx']} d'={r['dx']} extra={r['extra']} n'-1={r['nt1']}")
