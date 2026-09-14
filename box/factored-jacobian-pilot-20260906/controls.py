#!/usr/bin/env python3
"""Tiny exact controls, only on the allocated registered worker; no solver."""
import ast
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import socket

assert socket.gethostname() == 'ip-172-30-0-56'
assert Path('/sys/class/dmi/id/sys_vendor').read_text().strip() == 'Amazon EC2'
assert os.environ.get('JC2_REGISTERED_JOB') == 'factored-jacobian-pilot-astra-20260906'

def add(*tables):
    out = {}
    for table, scalar in tables:
        for pos, value in table.items():
            out[pos] = out.get(pos, Q(0)) + scalar*value
    return {p:v for p,v in out.items() if v}

def mul(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            p=(i+k,j+l);out[p]=out.get(p,Q(0))+x*y
    return {p:v for p,v in out.items() if v}

def diff(a,k):
    out={}
    for p,v in a.items():
        if p[k]:
            q=list(p);q[k]-=1;out[tuple(q)]=v*p[k]
    return out

def jac(a,b):
    return add((mul(diff(a,0),diff(b,1)),1),(mul(diff(a,1),diff(b,0)),-1))

one={(0,0):Q(1)};X={(1,0):Q(1)};W={(0,1):Q(1)}
def formula(h,D,C,a,b):
    A=add((D,Q(3,2)),(h,b/2),(one,a/2))
    B=add((h,2),(one,-b/3))
    return add((mul(A,jac(h,D)),1),(mul(B,jac(C,h)),1),(jac(C,D),1))

def pair(h,D,C,a,b):
    F=add((mul(mul(h,h),h),1),(mul(add((D,Q(3,2)),(one,a/2)),h),1),(C,1))
    G=add((mul(h,h),1),(h,-b/3),(D,1))
    return F,G

for h,D,C,a,b,expected in [
    ({},W,X,Q(0),Q(0),one),
    (X,{},W,Q(0),Q(0),{(1,0):Q(-2)}),
    (X,W,{},Q(2),Q(6),{(0,1):Q(3,2),(1,0):Q(3),(0,0):Q(1)})
]:
    F,G=pair(h,D,C,a,b)
    assert jac(F,G)==formula(h,D,C,a,b)==expected

raw=Path('delta2_stage8.strongest.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea'
data=json.loads(raw)
def ev(n):
    if isinstance(n,ast.Constant):return Q(n.value)
    if isinstance(n,ast.Name):return Q(1 if n.id=='rho' else 0)
    if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -ev(n.operand)
    if isinstance(n,ast.BinOp):
        a,b=ev(n.left),ev(n.right)
        if isinstance(n.op,ast.Add):return a+b
        if isinstance(n.op,ast.Sub):return a-b
        if isinstance(n.op,ast.Mult):return a*b
        if isinstance(n.op,ast.Div):return a/b
        if isinstance(n.op,ast.Pow):return a**int(b)
    raise ValueError(ast.dump(n))

def table(key,N):
    out={}
    for r,z,e in data['maps'][key]:
        assert int(r)+int(z)<=N
        p=(N-int(r)-int(z),int(z));v=ev(ast.parse(str(e).replace('^','**'),mode='eval').body)
        if v:out[p]=v
    return out

h3,c2,c3=table('h3',11),table('C2',22),table('C3',33)
h=add((mul(mul(h3,h3),h3),1),(mul(c2,h3),1),(c3,1))
D,C=table('B2',65),table('A3',98)
assert not D and not C
F,G=pair(h,D,C,Q(0),Q(0))
assert max(map(sum,F))==99 and max(map(sum,G))==66
assert not jac(F,G) and not formula(h,D,C,Q(0),Q(0))
assert not data['residual_rows']
full=Path('scalar_full.rows.tsv').read_text().splitlines()
low=Path('scalar_low.rows.tsv').read_text().splitlines()
filtered=[full[0]]+[r for r in full[1:] if sum(map(int,r.split('\t')[:2]))<=20]
assert filtered==low and len(low)==101
result={'status':'EXACT_CONTROLS_PASS','affine_positive_control_J':1,
        'orientation_negative_control_J':'-2*X','mixed_control_J':'3/2*W+3*X+1',
        'source_zero_control':{'rho':1,'all_other_source_coordinates':0,'degrees':[99,66],
        'all_positive_J_rows_zero':True,'J0':0,'inverse_row':-1,'Keller_point':False},
        'scalar_full_vs_low_all_100_row_hashes_equal':True,'solver_launched':False}
target=Path('controls.json')
assert not target.exists()
target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
