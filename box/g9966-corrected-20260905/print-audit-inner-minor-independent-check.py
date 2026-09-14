#!/usr/bin/env python3
"""Independent numeric full-polynomial substitution for both inner points."""
import hashlib,json
from pathlib import Path
from math import comb
import sympy as sp
import engine as E
import minor_maps as MM
from source_data import SOURCE as S,jsonable

HERE=Path(__file__).resolve().parent

def plus(*items):
    out={}
    for p in items:
        for k,v in p.items():out[k]=out.get(k,0)+v
    return {k:sp.Rational(v) for k,v in out.items() if v!=0}

def multiply(a,b,cut):
    out={}
    for (r,q),v in a.items():
        for (s,k),w in b.items():
            if r+s<=cut:out[(r+s,q+k)]=out.get((r+s,q+k),0)+v*w
    return {k:sp.Rational(v) for k,v in out.items() if v!=0}

def numeric_local(tz,branch,point,cut):
    data=MM.branch_data(branch);denom=data['denominator']
    z={(0,0):sp.Integer(-1)}
    for r,q,v in data['w_terms']:
        v=sp.sympify(v).xreplace(point)
        assert not v.free_symbols
        if v!=0:z[(r,q)]=z.get((r,q),0)+v
    powers=[{(0,0):sp.Integer(1)}]
    for _ in range(max(q for r,q in tz)):
        powers.append(multiply(powers[-1],z,cut))
    result={}
    for (r,q),value in tz.items():
        for (n,k),coef in powers[q].items():
            if denom*r+n<=cut:result[(denom*r+n,k)]=result.get((denom*r+n,k),0)+value*coef
    return {k:sp.Rational(v) for k,v in result.items() if v!=0}

results={}
for branch in ('delta2','delta52'):
    artifact=json.loads((HERE/f'print-audit-inner-minor-{branch}.json').read_text())
    h,C2,C3,free,meta=E.inner_state(branch)
    point={v:sp.Integer(0) for v in free}
    point.update({sp.Symbol(k):sp.Rational(v) for k,v in artifact['native_trial_nonzero'].items()})
    def numeric(poly):
        out={p:sp.expand(v.xreplace(point)) for p,v in poly.items()}
        assert all(not v.free_symbols for v in out.values())
        return {p:sp.Rational(v) for p,v in out.items() if v!=0}
    h,C2,C3=map(numeric,(h,C2,C3))
    k2=plus(multiply(multiply(h,h,S['k2_degree']),h,S['k2_degree']),multiply(C2,h,S['k2_degree']),C3)
    floor=artifact['k2_floor'];got=numeric_local(k2,branch,point,floor)
    P,_=MM.derive_minor_face(branch);P=sp.expand(P.xreplace(point))
    target={(floor,k[0]):v for k,v in sp.Poly(sp.expand(P**S['inner_power']),sp.Symbol('zeta')).terms()}
    assert got==target,(branch,got,target)
    c2got=numeric_local(C2,branch,point,artifact['floors']['C2']-1)
    c3got=numeric_local(C3,branch,point,artifact['floors']['C3']-1)
    assert not c2got and not c3got
    # Perturb a single normalized C3 monomial; the full pullback must detect it.
    first=min(S['Vslots'])
    perturbed=dict(k2);perturbed[first]=perturbed.get(first,0)+1
    negative=numeric_local(perturbed,branch,point,floor)
    differences={k:negative.get(k,0)-target.get(k,0) for k in set(negative)|set(target) if negative.get(k,0)!=target.get(k,0)}
    assert differences
    results[branch]={'full_numeric_K2_coefficients':len(k2),'full_K2_local_identity':True,
       'C2_strict_minor_rows_all_zero':True,'C3_strict_minor_rows_all_zero':True,
       'target_face':str(sp.expand(P**S['inner_power'])),'local_floor':floor,
       'negative_control_added_C3_monomial':list(first),'negative_nonzero_rows':len(differences),
       'negative_first_difference':[list(min(differences)),str(differences[min(differences)])],
       'point_artifact_sha256':hashlib.sha256((HERE/f'print-audit-inner-minor-{branch}.json').read_bytes()).hexdigest()}
(HERE/'print-audit-inner-minor-independent-check.json').write_text(json.dumps(jsonable(results),indent=2,sort_keys=True)+'\n')
print(json.dumps(jsonable(results),indent=2,sort_keys=True))
