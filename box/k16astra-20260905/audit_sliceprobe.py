#!/usr/bin/env python3
"""Exact tau in I+(b3) test and quotient-degree check, SymPy only."""
import itertools,json,pathlib,sys,time
import sympy as s
t=int(sys.argv[1]); start=time.monotonic(); root=pathlib.Path(__file__).resolve().parent
pv=(s.Symbol('b4'),)+tuple(s.Symbol('u'+str(i)) for i in range(2,t))
d=s.Symbol('d'); alpha=s.sqrt(s.Rational(t+1,3)); K=s.QQ.algebraic_field(alpha)
ns={str(x):x for x in pv+(d,)}; ns['b3']=s.Integer(0); rows={}
for line in (root/f't{t}_rows.sing').read_text().splitlines():
    if line.startswith('poly '):
        name,expr=line[5:].rstrip(';').split('=',1)
        if name=='T0': continue
        rows[name]=s.sympify(expr.replace('^','**'),locals=ns).subs(d,alpha)
print('PARSED',t,'seconds',time.monotonic()-start,flush=True)
gb=s.groebner([rows[f'T{i}'] for i in range(1,2*t)],*pv,domain=K,order='grevlex')
rem=gb.reduce(rows['tau'])[1]; print('SLICE',len(gb.polys),gb.is_zero_dimensional,'tau_in',rem==0,'seconds',time.monotonic()-start,flush=True)
lm=[p.LM(order=gb.order).exponents for p in gb.polys]
bounds=[]
for i in range(len(pv)):
    exps=[m[i] for m in lm if m[i]>0 and all(m[j]==0 for j in range(len(pv)) if j!=i)]
    bounds.append(min(exps) if exps else None)
length=top=None
if all(bounds):
    std=[m for m in itertools.product(*(range(x) for x in bounds)) if not any(all(a<=b for a,b in zip(g,m)) for g in lm)]
    length=len(std); top=max(sum((i+1)*a for i,a in enumerate(m)) for m in std)
print('STANDARD_MONOMIALS',length,'TOP_WEIGHT',top,'TAU_WEIGHT',4*t+1,flush=True)
result={'t':t,'field':str(K),'tau_in_I_plus_b3':rem==0,'gb_size':len(gb.polys),'zero_dimensional':gb.is_zero_dimensional,'quotient_length':length,'top_weight':top,'tau_weight':4*t+1,'elapsed':time.monotonic()-start}
(root/f'audit_sliceprobe_t{t}.json').write_text(json.dumps(result,indent=2)+'\n'); print('DONE',flush=True)
