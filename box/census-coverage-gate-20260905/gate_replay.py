#!/usr/bin/env python3
"""HOSTILE GATE independent replay: census -> operative -> Xu Cor 5.3, from MY frozen inputs."""
from pathlib import Path
import importlib.util, sys, json, time, hashlib
from fractions import Fraction as F
ROOT=Path('/home/ubuntu/jc2'); OUT=ROOT/'box/census-coverage-gate-20260905'
INPUTS=Path('/tmp/jc2-lane.9sTiQX/inputs')          # MY frozen inputs
SNAP=ROOT/'box/census-coverage-20260905'            # aux impls (verified == live repo)
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
B=load('moh_skeleton_full',INPUTS/'moh_skeleton_full.py');sys.modules['moh_skeleton_full_frozen']=B
OP=load('op_probe',SNAP/'op-opus5_probe.snapshot.py')
FT=load('full_tree_partition',SNAP/'op-full_tree_partition.snapshot.py')
XU=load('op_xu',SNAP/'op-xu_screen.snapshot.py')

def evaluate(n,m,Ms,V,gate=False,ode=True,recenter=True,danger=True):
    T=OP.Tree(n,m,Ms,gate=gate,ode=ode,capacity=False,passport=False)
    T.recenter=recenter;T._memo={};T.why=[]
    if not (T.d[T.s]>V[T.s]>F(T.d[T.s],2)):return False
    need=tuple(V[i] for i in range(T.s-1,1,-1))
    return T.ok(T.s-1,(V[T.s],),danger,need) is not None

def main(kmin=2, nmax=200):
    t0=time.monotonic(); rows=[]; census_n=0; ft_mismatch=0; op_n=0
    for n in range(16,nmax+1):
        for m,Ms,V in B.census(n,Kmin=kmin,full=True):
            census_n+=1
            op=evaluate(n,m,Ms,V)
            S=B.Skel(n,m,list(Ms),dict(V))
            ft=bool(FT.full_tree_polynomial_ode_ok(S))
            if ft!=op: ft_mismatch+=1
            if not op: continue
            op_n+=1
            r=XU.XuBounder(S).row_bound(); assert r is not None
            us=S.d[S.s]-S.V[S.s]
            rows.append(dict(n=n,m=m,Ms=list(Ms),V={str(k):v for k,v in V.items()},
                             us=us, vs=S.V[S.s], ds=S.d[S.s],
                             IM_max=str(r['IM_max']),Im_min=str(r['Im_min']),xu_ok=bool(r['xu_ok'])))
    xu_ok=sum(r['xu_ok'] for r in rows)
    res=dict(kmin=kmin,nmax=nmax,census=census_n,operative=op_n,ft_mismatch=ft_mismatch,
             xu_survivors=xu_ok,xu_killed=op_n-xu_ok,seconds=round(time.monotonic()-t0,2),
             rows=rows)
    (OUT/f'gate-replay-kmin{kmin}.json').write_text(json.dumps(res,indent=1)+'\n')
    print(json.dumps({k:v for k,v in res.items() if k!='rows'},indent=1),flush=True)
if __name__=='__main__':
    main(kmin=int(sys.argv[1]) if len(sys.argv)>1 else 2)
