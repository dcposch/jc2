#!/usr/bin/env python3
"""Read-only replay of frozen census and discovered operative screen implementations.
Every emitted row is a numerical candidate; no realization assertion is made.
"""
from pathlib import Path
import importlib.util, sys, json, time, hashlib
from fractions import Fraction as F
ROOT=Path('/home/ubuntu/jc2'); OUT=ROOT/'box/census-coverage-20260905'
INPUTS=Path('/tmp/jc2-lane.94eJYj/inputs')
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
B=load('moh_skeleton_full',INPUTS/'moh_skeleton_full.py');sys.modules['moh_skeleton_full_frozen']=B
OPPATH=OUT/'op-opus5_probe.snapshot.py'
FTPATH=OUT/'op-full_tree_partition.snapshot.py'
XUPATH=OUT/'op-xu_screen.snapshot.py'
OP=load('op_probe',OPPATH)
FT=load('full_tree_partition',FTPATH)
XU=load('op_xu',XUPATH)

def row(n,m,Ms,V): return dict(n=n,m=m,Ms=list(Ms),V=V)
def evaluate(n,m,Ms,V,gate=False,danger=True):
    T=OP.Tree(n,m,Ms,gate=gate,ode=True,capacity=False,passport=False)
    T.recenter=True;T._memo={};T.why=[]
    if not (T.d[T.s]>V[T.s]>F(T.d[T.s],2)):return False
    need=tuple(V[i] for i in range(T.s-1,1,-1))
    return T.ok(T.s-1,(V[T.s],),danger,need) is not None

def main():
    start=time.monotonic();summary={};oprows=[];mismatch=[]
    for n in range(16,201):
        counts=dict(census=0,operative=0,ft_operative=0,xu_killed=0,xu_sharp_killed=0)
        for m,Ms,V in B.census(n,Kmin=2,full=True):
            counts['census']+=1
            op=evaluate(n,m,Ms,V)
            S=B.Skel(n,m,list(Ms),dict(V));ft=FT.full_tree_polynomial_ode_ok(S)
            counts['operative']+=op;counts['ft_operative']+=bool(ft)
            if bool(ft)!=op:mismatch.append(row(n,m,Ms,V))
            if op:
                result=XU.XuBounder(S).row_bound();assert result is not None
                us=S.d[S.s]-S.V[S.s]
                extra=F(S.V[S.s],us)-1 if us>1 else F(0)
                sharp=result['IM_max']>=result['Im_min']+extra
                rr=row(n,m,Ms,V);rr.update(IM_max=str(result['IM_max']),Im_min=str(result['Im_min']),Im_min_sharp=str(result['Im_min']+extra),xu_ok=result['xu_ok'],xu_sharp_ok=sharp)
                oprows.append(rr)
                counts['xu_killed']+=not result['xu_ok'];counts['xu_sharp_killed']+=not sharp
        summary[n]=counts
        if n%20==0:print(n,{k:sum(v[k] for v in summary.values()) for k in counts},round(time.monotonic()-start,2),flush=True)
    totals={k:sum(v[k] for v in summary.values()) for k in counts}
    groups={}
    for r in oprows:groups.setdefault((r['n'],r['m'],tuple(r['Ms']),r['V'][len(r['Ms'])+1]),[]).append(r)
    totals.update(groups=len(groups),xu_killed_groups=sum(all(not r['xu_ok'] for r in rows) for rows in groups.values()),xu_sharp_killed_groups=sum(all(not r['xu_sharp_ok'] for r in rows) for rows in groups.values()))
    result=dict(totals=totals,by_n=summary,operative_rows=oprows,ft_mismatch=mismatch,seconds=time.monotonic()-start,input_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [INPUTS/'moh_skeleton_full.py',OPPATH,FTPATH,XUPATH]})
    (OUT/'op-ft-xu-count.json').write_text(json.dumps(result,indent=1)+'\n')
    print(json.dumps(dict(totals=totals,n_le_100={k:sum(v[k] for n,v in summary.items() if n<=100) for k in counts},ft_mismatch=len(mismatch),seconds=result['seconds']),indent=2),flush=True)
if __name__=='__main__':main()
