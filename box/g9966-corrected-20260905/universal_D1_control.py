#!/usr/bin/env python3
"""Universal enlargement of the derived D1 face; never a restricted-chart kill.

P=3^24*p(Pi^3), Q=3^16*Pi*q(Pi^3) follow from the source
degree/congruence and nonzero leading coefficients. All lower p/q coefficients
are free here. Normalize only by these fixed nonzero rational leaders.
"""
import hashlib,json,subprocess,time
from pathlib import Path
import sympy as s
N=Path(__file__).resolve().parent
X=s.Symbol('X'); pv=s.symbols('p0:8'); qv=s.symbols('q0:5')
c,z=s.symbols('Jnorm ZJnorm')
p=X**8+sum(v*X**i for i,v in enumerate(pv))
q=X**5+sum(v*X**i for i,v in enumerate(qv))
L=s.Poly(s.expand(p*q+3*X*p*s.diff(q,X)-2*X*s.diff(p,X)*q-c),X)
assert L.degree()==12
mapping={};trace=[]
for k in range(12,4,-1):
    row=s.expand(L.nth(k).subs(mapping));v=pv[k-5]
    lead=s.expand(row).coeff(v)
    assert lead.is_Rational and lead!=0 and v not in lead.free_symbols
    rhs=s.expand(-(row-lead*v)/lead)
    assert v not in rhs.free_symbols
    mapping[v]=rhs;trace.append({'power':k,'row':str(row),'variable':str(v),'leader':str(lead),'rhs':str(rhs)})
assert set(mapping)==set(pv)
rows=[s.expand(L.nth(k).subs(mapping)) for k in range(5)]+[c*z-1]
assert all(s.expand(L.nth(k).subs(mapping))==0 for k in range(5,14))
denominator_scales=[]
def encode(v):
    den,poly=s.Poly(v,*list(qv),c,z,domain=s.QQ).clear_denoms()
    denominator_scales.append(str(den))
    return str(poly.as_expr()).replace('**','^')
script='ring R=0,('+','.join(map(str,list(qv)+[c,z]))+'),dp;\n'
script+='ideal I='+','.join(map(encode,rows))+';\nideal S=std(I);\nprint("BEGIN");print(dim(S));print(S);print("END");\nquit;\n'
path=N/'universal_D1_control.sing';path.write_text(script)
record={'type':'UNIVERSAL D1 FACE ENLARGEMENT, all lower coefficients free',
    'field':'Q','generator_order':list(map(str,list(qv)+[c,z])),
    'source_of_shape':'D1 deck congruence and generated leading coefficients; printed source audit',
    'scalar_map':'Jnorm=3*Jc/3^40; invertible rational scaling, no group spend',
    'rational_pivots':trace,'remaining_rows':list(map(str,rows)),
    'coefficients_P':{str(v):str(rhs) for v,rhs in mapping.items()},
    'QQstar_denominator_scales':denominator_scales,
    'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
    'no_original_chart_implication_claimed_for_nonunit':True}
(N/'universal_D1_control.json').write_text(json.dumps(record,indent=2)+'\n')
start=time.monotonic()
run=subprocess.run(['Singular','-q',str(path)],text=True,capture_output=True,timeout=300)
(N/'universal_D1_control.out').write_text(run.stdout+run.stderr)
assert run.returncode==0 and 'error' not in (run.stdout+run.stderr).lower()
dimension=int(run.stdout.split('BEGIN\n')[1].splitlines()[0])
record.update({'dimension':dimension,'unit':dimension==-1,'seconds':time.monotonic()-start})
(N/'universal_D1_control.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['dimension','unit','seconds']}),flush=True)
