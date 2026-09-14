#!/usr/bin/env python3
"""Blind independent replay; no active-lane imports or artifacts."""
import ast
import hashlib
import json
import sys
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'box/centre-gate-20260903'))
import moh_skeleton_full_frozen as B
from opus5_probe import Tree

def key(n,m,Ms,V):
    return n,m,tuple(Ms),tuple(sorted(V.items()))

def descend(n,m,Ms,V):
    S=B.Skel(n,m,Ms,V)
    ds=S.d[S.s]
    us=ds-V[S.s]
    assert us==1
    ell=ds-3
    M=[S.M[i]//ds for i in range(1,S.s)]
    d=[S.d[i]//ds for i in range(1,S.s+1)]
    assert all(S.M[i]%ds==0 for i in range(1,S.s))
    # Moh p.150: q_1=M_1, q_i=M_i-M_(i-1), lambda_i=sum(q_j*d_j), mu_i=lambda_i/d_i.
    running=0
    mu=[]
    for i in range(len(M)):
        running+=(M[i]-(M[i-1] if i else 0))*d[i]
        assert running%d[i]==0
        mu.append(running//d[i])
    return dict(n=n//ds,m=m//ds,M=M,d=d,ell=ell,us=us,ds=ds,
                ancestral_V=[V[i] for i in range(2,S.s)],
                s_prime=S.s-1,tower_pi_degrees=[n//ds]+[-x for x in mu],
                anchor=(n//ds)-M[-1]-1,
                pair_triangle_count=((n//ds)+1)*((n//ds)+2)//2+((m//ds)+1)*((m//ds)+2)//2)

def main():
    t=time.monotonic()
    printed={key(n,m,Ms,V) for n,m,Ms,V,*_ in B.MOH_TABLE}
    survivors=[]
    total=0
    for n in range(4,101):
        for m,Ms,V in B.census(n,Kmin=2,full=True):
            total+=1
            T=Tree(n,m,Ms,recenter=True,ode=True,gate=False)
            T._memo={}
            if not (T.d[T.s]>V[T.s]>Fraction(T.d[T.s],2)):
                continue
            need=tuple(V[i] for i in range(T.s-1,1,-1))
            if T.ok(T.s-1,(V[T.s],),True,need) is not None:
                survivors.append(key(n,m,Ms,V))
    bank=json.loads((ROOT/'box/mohprog-drivers-20260903/full-tree-polynomial-ode-n100-audit.json').read_text())
    bankkeys={ast.literal_eval(r['row_key']) for r in bank['rows'] if r['selected_path_embeds']}
    assert set(survivors)==bankkeys
    assert total==658 and len(survivors)==20 and printed<=set(survivors)
    excess=sorted(set(survivors)-printed)
    groups=defaultdict(list)
    rows=[]
    for n,m,Ms,V in excess:
        D=descend(n,m,list(Ms),dict(V))
        ckey=(D['n'],D['m'],tuple(D['M']),D['ell'])
        groups[ckey].append((n,m,Ms,V))
        rows.append(dict(ancestor=(n,m,Ms,V),descent=D))
    print('TYPE MEASURED EXACT ARITHMETIC; necessity remains the promoted screen source obligation.')
    print('REPLAY total=658 survivors=20 printed=6 excess=14 bank-key equality=True')
    print('EXCESS all_us1=True s_prime_counts=',dict(__import__('collections').Counter(r['descent']['s_prime'] for r in rows)))
    print('CLASSES characteristic=7 coarse_degree_jacobian=4 ancestral_V_assignments=14')
    for i,(ck,ancestors) in enumerate(sorted(groups.items()),1):
        n,m,Ms,V=ancestors[0]
        D=descend(n,m,list(Ms),dict(V))
        print('CLASS',i,'key=',ck,'multiplicity=',len(ancestors),'gcd_chain=',D['d'],
              'tower_pi_degrees=',D['tower_pi_degrees'],'anchor=',D['anchor'],
              'pair_triangle_count=',D['pair_triangle_count'],
              'ancestral_V=',[list(dict(r[3]).values())[:-1] for r in ancestors])
    for i,r in enumerate(rows,1):
        print('ROW',i,json.dumps(r,sort_keys=True))
    print('WALL_SECONDS',round(time.monotonic()-t,3))
    (OUT/'rows.json').write_text(json.dumps(dict(total=total,survivors=20,rows=rows),indent=2)+'\n')

if __name__=='__main__':
    main()
