#!/usr/bin/env python3
"""Exact-Q center/radius diagnostics; imports qstar_reduce from frozen input."""
from pathlib import Path
import importlib.util,sys,json,time
from collections import defaultdict
from math import comb,factorial
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent/'replay'
sys.path.insert(0,str(ROOT/'box/g108gate-20260903'))
spec=importlib.util.spec_from_file_location('frozen_d108_band_engine','/tmp/jc2-lane.8CzNCH/inputs/band_engine.py')
eng=importlib.util.module_from_spec(spec);sys.modules[spec.name]=eng;spec.loader.exec_module(eng)

def template(wq,cutoff):
    h={(0,7):sp.Integer(1),(0,8):sp.Integer(2),(0,9):sp.Integer(1)};vs=[]
    for r in range(1,10):
        vmin=0 if cutoff is None else max(0,-(-(cutoff-4*r)//wq))
        for degree in range(vmin,10-r):
            v=sp.Symbol(f'Hc_{r}_{degree}');vs.append(v)
            for q in range(vmin,degree+1):h[r,q]=h.get((r,q),0)+v*comb(degree-vmin,q-vmin)
    return {k:sp.expand(v) for k,v in h.items()},vs

def incidence(h,leading=False):
    wb=eng.z_to_w(h);jet0,jet1,jet2,c=sp.symbols('jet0 jet1 jet2 c');coll=defaultdict(lambda:sp.Integer(0))
    for (r,j),co in wb.items():
        for d in range(j+1) if leading else [0]:
            for a in range(j-d+1):
                for b in range(j-d-a+1):
                    k=j-d-a-b;lp=r+d+2*a+3*b+4*k
                    if lp>8:continue
                    mn=factorial(j)//(factorial(d)*factorial(a)*factorial(b)*factorial(k))
                    coll[lp,k]+=co*mn*jet0**d*jet1**a*jet2**b
    coll[8,0]-=c;coll[8,2]+=1
    return [(f'minor_n{p}_pi{k}',sp.expand(v)) for (p,k),v in sorted(coll.items())]

def run(tag,wq,cutoff,leading=False):
    tm=time.monotonic();h,hv=template(wq,cutoff);rows=incidence(h,leading)
    resid,subs,piv,zeros=eng.qstar_reduce(rows,hv)
    data={'tag':tag,'weight':[4,wq],'cutoff':cutoff,'minor_jet0':leading,'h3_coordinate_count':len(hv),'variables':list(map(str,hv)),'template':{f'{r},{q}':str(v) for (r,q),v in sorted(h.items())},'raw_rows':{k:str(v) for k,v in rows},'Qstar_pivots':[{'row':p.label,'variable':str(p.variable),'coefficient':str(p.coefficient),'resolved_value':str(subs[p.variable])} for p in piv],'zero_rows':zeros,'residual':{k:str(v) for k,v in resid}}
    (OUT/(tag+'.partial.json')).write_text(json.dumps(data,indent=2)+'\n')
    c,zc=sp.symbols('c Zc');gens=[v for _,v in resid]+[zc*c-1];rv=sorted(set().union(*(v.free_symbols for v in gens)),key=str)
    G=sp.groebner(gens,*rv,order='grevlex');unit=list(G.exprs)==[sp.Integer(1)]
    data.update({'coefficient_field':'QQ','ring_variables':list(map(str,rv)),'generator_order':'residual label ascending, then Zc*c-1','groebner_order':'grevlex','groebner_basis':list(map(str,G.exprs)),'localized_unit':unit,'elapsed_seconds':time.monotonic()-tm})
    (OUT/(tag+'.json')).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'tag':tag,'hvars':len(hv),'pivots':len(piv),'residuals':len(resid),'unit':unit,'groebner_basis':list(map(str,G.exprs)),'seconds':data['elapsed_seconds']}),flush=True)
    return data

if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    cases=[('baseline43',6,43,False),('control42',6,42,False),('physical36',5,36,False),('physical35',5,35,False),('uncapped',6,None,False),('relative_minor_jet0',6,43,True)]
    selected=set(sys.argv[1:])
    for args in cases:
        if not selected or args[0] in selected:run(*args)
