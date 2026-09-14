#!/usr/bin/env python3
"""Independently reduce source incidence BEFORE expanding minor centres.

This emits no restricted chart: both substitutions pivot only QQ* scalars.
"""
import argparse,json,time
from pathlib import Path
import sympy as sp
import engine as E
import minor_maps as MM
from source_data import SOURCE as S,jsonable


def derive_generic(verbose=True):
    start=time.monotonic();h,hvars=E.h3_template();print('H3_TEMPLATE',time.monotonic()-start,flush=True)
    C2,c2vars,c2meta=E.coefficient_box('C2',S['inner_normalization_degrees']['C2'],S['inner_qcap'],S['C2_floor'])
    C3,c3vars,c3meta=E.coefficient_box('C3',S['inner_normalization_degrees']['C3'],S['inner_qcap'],S['C3_floor'])
    print('COEFFICIENT_BOXES',time.monotonic()-start,flush=True)
    cover,base,child=S['D1_substitution']; multiplier=cover//S['D2_weight'][0]
    cutoff=(S['k2_D1_floor']-1)//multiplier
    low=E.tz_add(E.mul_weight(E.mul_weight(h,h,cutoff),h,cutoff),E.mul_weight(C2,h,cutoff),{p:v for p,v in C3.items() if E.weight(p)<=cutoff})
    beta=sp.Symbol('beta');eq={p:v.subs(beta,1) for p,v in S['k2_equality'].items()}
    positions=set(p for p in low if E.weight(p)<=S['k2_floor'])|set(eq)
    rows=[(f'K2_D2_{r}_{q}',sp.expand(low.get((r,q),0)-eq.get((r,q),0))) for r,q in sorted(positions)]
    d1={}
    for (r,q),v in low.items():
        for k in range(q+1):
            exponent=cover*r+base*q+(child-base)*k
            if exponent<S['k2_D1_floor']:
                tag=(exponent,k);d1[tag]=d1.get(tag,0)+v*sp.binomial(q,k)
    rows += [(f'K2_D1_e{e}_k{k}',sp.expand(v)) for (e,k),v in sorted(d1.items())]
    if verbose: print('GENERIC_EMITTED',len(rows),'seconds',time.monotonic()-start,flush=True)
    residual,mapping,pivots,zero=E.qstar_reduce(rows,c2vars|c3vars)
    assert not residual
    assert all(sp.expand(row.xreplace(mapping))==0 for _,row in rows)
    if verbose: print('GENERIC_REDUCED',len(pivots),'seconds',time.monotonic()-start,flush=True)
    return h,hvars,C2,C3,c2vars,c3vars,rows,mapping,pivots,{'generic_seconds':time.monotonic()-start,'generic_rows':len(rows),'generic_pivots':len(pivots),'generic_remaining':len(set(hvars)|c2vars|c3vars)-len(mapping),'generic_map':{str(v):str(r) for v,r in mapping.items()},'generic_recheck':True,'source_C2':c2meta,'source_C3':c3meta}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--branch',choices=['delta2','delta52']);ap.add_argument('--out',type=Path);a=ap.parse_args()
    h,hvars,C2,C3,c2vars,c3vars,rows,mapping,pivots,result=derive_generic()
    if a.branch:
        start=time.monotonic();hm,hfree,minor=MM.derive_minor_map(a.branch,h,hvars)
        ell,exchange=sp.symbols('E82 Hc_8_3')
        old_rhs=hm[ell];leader=sp.diff(old_rhs,exchange)
        assert leader.is_Rational and leader!=0
        new_rhs=sp.expand((ell-(old_rhs-leader*exchange))/leader)
        hm={v:sp.expand(rhs.xreplace({exchange:new_rhs})) for v,rhs in hm.items() if v!=ell}
        hm[exchange]=new_rhs;hm=E.resolve_map(hm)
        hfree=[v for v in hfree if v!=exchange]+[ell]
        print('MINOR_REDUCED',a.branch,'seconds',time.monotonic()-start,flush=True)
        combined=dict(hm)
        combined.update({v:r.xreplace(hm) for v,r in mapping.items()})
        for v,r in combined.items(): assert not r.free_symbols.intersection(combined)
        assert all(sp.expand(row.xreplace(mapping)).xreplace(hm)==0 for _,row in rows)
        before=set(hfree)|c2vars|c3vars;after=before-set(mapping)
        result.update({'branch':a.branch,'minor_seconds':time.monotonic()-start,'preincidence_count':len(before),'after_incidence_count':len(after),'source_Qstar_pivots':len(pivots),'combined_recheck':True,'recheck_method':'generic identity first; then exact coefficient-ring homomorphism','combined_map':{str(v):str(r) for v,r in combined.items()},'free':sorted(map(str,after)),'minor':minor})
    if a.out:a.out.write_text(json.dumps(jsonable(result),indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if not isinstance(v,(list,dict))},indent=2))

if __name__=='__main__':main()
