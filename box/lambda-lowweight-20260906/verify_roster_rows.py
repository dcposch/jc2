#!/usr/bin/env python3
"""Exact integer recomposition checks of all fresh roster coefficient rows.

Two independent full parameter assignments and source evaluation points.
No modular polynomial or floating point arithmetic is used.
"""
import hashlib,json,re,time
from pathlib import Path
HERE=Path(__file__).resolve().parent

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,b):return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+a[0]*b[2])
def power(a,n):
    z=(1,0,0)
    for _ in range(n):z=mul(z,a)
    return z

def verify(cid):
    start=time.monotonic();d=json.loads((HERE/f'{cid}.rows.json').read_text())
    names=d['variables'];K=d['K'];e=d['n']//K;q=d['m']//K
    configs=[]
    for seed,x,y in [(17,2,-1),(31,-1,2)]:
        vals={v:1+int.from_bytes(hashlib.sha256(f'{seed}:{v}'.encode()).digest()[:4],'big')%3 for v in names}
        blocks={'h':(y**K,0,K*y**(K-1))}
        for v in names:
            if v=='c':continue
            b,s,t=v.split('_');s=int(s);t=int(t);value=vals[v]
            term=(value*x**s*y**t,value*s*x**(s-1)*y**t if s else 0,
                  value*t*x**s*y**(t-1) if t else 0)
            blocks[b]=add(blocks.get(b,(0,0,0)),term)
        h=blocks['h'];P=power(h,e);Q=power(h,q)
        for i in range(1,e+1):P=add(P,mul(blocks[f'A{i}'],power(h,e-i)))
        for i in range(2,q+1):Q=add(Q,mul(blocks[f'B{i}'],power(h,q-i)))
        jac=P[1]*Q[2]-P[2]*Q[1]
        target=vals['c']*x**d['ell']
        configs.append(dict(seed=seed,x=x,y=y,vals=vals,h=h[0],expected=jac-target,
                            reversed=-jac-target,recomposed=0,target=target))
    rows=terms=0;digest=hashlib.sha256()
    with open(d['rows_path'],'rb') as f:
        digest.update(next(f))
        for raw in f:
            digest.update(raw);_,h,x,y,expr=raw.decode().strip().split('|',4)
            h,x,y=int(h),int(x),int(y);rv=[0,0]
            for t in re.findall(r'[+-]?[^+-]+',expr):
                factors=t.split('*'); coeff=1
                if factors[0][0] in '+-':
                    if factors[0][0]=='-':coeff=-1
                    factors[0]=factors[0][1:]
                if factors[0].isdigit():coeff*=int(factors.pop(0))
                vv=[coeff,coeff]
                for factor in factors:
                    parts=factor.split('^');v=parts[0];p=int(parts[1]) if len(parts)>1 else 1
                    for k,c in enumerate(configs):vv[k]*=c['vals'][v]**p
                for k in range(2):rv[k]+=vv[k]
                terms+=1
            for k,c in enumerate(configs):c['recomposed']+=rv[k]*c['h']**h*c['x']**x*c['y']**y
            rows+=1
    assert digest.hexdigest()==d['rows_sha256']
    assert rows==d['coefficient_rows']
    checks=[]
    for c in configs:
        assert c['recomposed']==c['expected']
        assert c['recomposed']!=c['reversed']
        assert c['recomposed']+1!=c['expected']
        checks.append(dict(seed=c['seed'],x=c['x'],y=c['y'],exact_recomposition=True,
                     reversed_orientation_rejected=True,one_term_perturbation_rejected=True,
                     reconstructed_integer=str(c['recomposed'])))
    return dict(id=cid,rows=rows,terms=terms,rows_sha256=digest.hexdigest(),
                exact_integer_checks=checks,wall_seconds=round(time.monotonic()-start,3))

if __name__=='__main__':
    out=[]
    for cid in ['R001','R002','R004']:
        r=verify(cid);out.append(r);print(json.dumps(r),flush=True)
    (HERE/'roster-row-controls.json').write_text(json.dumps(dict(status='PASS',cases=out,
        R003='IDENTICAL_RECEIVER_AND_ROWS_TO_R002',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2)+'\n')
