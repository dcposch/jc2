#!/usr/bin/env python3
"""Exact quadratic-cover base ideals, SymPy only; parse root-generated rows."""
import json, pathlib, sys, time
import sympy as s

t = int(sys.argv[1]); start=time.monotonic()
root = pathlib.Path(__file__).resolve().parent
b = s.Symbol('b3'); pvars = (s.Symbol('b4'),)+tuple(s.Symbol('u'+str(i)) for i in range(2,t))
d=s.Symbol('d'); alpha=s.sqrt(s.Rational(t+1,3)); K=s.QQ.algebraic_field(alpha)
ns={str(x):x for x in pvars+(b,d)}
rows={}
for line in (root/f't{t}_rows.sing').read_text().splitlines():
    if line.startswith('poly '):
        name,expr=line[5:].rstrip(';').split('=',1)
        rows[name]=s.sympify(expr.replace('^','**'),locals=ns).subs(d,alpha)
R=K.poly_ring(*pvars)
Q=s.Poly(rows[f'T{2*t-1}'],b,domain=R)
a0=Q.nth(2); b0=Q.nth(1); c0=Q.nth(0)
assert a0!=0
hs=[s.Poly(rows[f'T{i}'],b,domain=R).rem(Q) for i in range(1,2*t-1)]
h=s.Poly(rows['tau'],b,domain=R).rem(Q)
uv=[(x.nth(1),x.nth(0)) for x in hs]
u,v=h.nth(1),h.nth(0)
poly=lambda x:s.Poly(x,*pvars,domain=K)
ell=poly(2*a0*v-b0*u)
norm=poly(a0*v*v-b0*u*v+c0*u*u)
diff=[poly(v*ui-u*vi) for ui,vi in uv]
j0=[poly(z) for pair in uv for z in pair]
f=[]
for i,(ui,vi) in enumerate(uv):
    f.append(poly(a0*vi*vi-b0*ui*vi+c0*ui*ui))
    for uj,vj in uv[:i]: f.append(poly(vi*uj-vj*ui))
print('PARSED',t,'seconds',time.monotonic()-start,'rows',len(hs),flush=True)
print('BUILD J0',flush=True)
gj=s.groebner(j0,*pvars,domain=K,order='grevlex')
ej=gj.reduce(ell.as_expr())[1]; nj=gj.reduce(norm.as_expr())[1]
print('J0',len(gj.polys),'zero_dimensional',gj.is_zero_dimensional,'ell',ej==0,'norm',nj==0,'elapsed',time.monotonic()-start,flush=True)
print('BUILD F',flush=True)
gf=s.groebner(f,*pvars,domain=K,order='grevlex')
dr=[gf.reduce(x.as_expr())[1] for x in diff]
print('F',len(gf.polys),'zero_dimensional',gf.is_zero_dimensional,'D_members',[x==0 for x in dr],'elapsed',time.monotonic()-start,flush=True)
powers=[]
for x,rem in zip(diff,dr):
    if rem==0: powers.append(1)
    else: powers.append(2 if gf.reduce((x*x).as_expr())[1]==0 else None)
print('D_power_in_F',powers,flush=True)
ff=list(f)
for i,(ui,vi) in enumerate(uv):
    for uj,vj in uv[:i]: ff.append(poly(a0*vi*vj-b0*uj*vi+c0*ui*uj))
print('BUILD FFITT',flush=True)
gff=s.groebner(ff,*pvars,domain=K,order='grevlex')
dfr=[gff.reduce(x.as_expr())[1] for x in diff]
print('FFITT',len(gff.polys),'D_members',[x==0 for x in dfr],flush=True)
result={'t':t,'field':str(K),'J0_gb_size':len(gj.polys),'J0_zero_dimensional':gj.is_zero_dimensional,'ell_in_J0':ej==0,'norm_in_J0':nj==0,'F_gb_size':len(gf.polys),'F_zero_dimensional':gf.is_zero_dimensional,'D_in_F':[x==0 for x in dr],'D_power_in_F':powers,'FFITT_gb_size':len(gff.polys),'D_in_FFITT':[x==0 for x in dfr],'elapsed':time.monotonic()-start}
(root/f'audit_baseprobe_t{t}.json').write_text(json.dumps(result,indent=2)+'\n')
print('DONE',flush=True)
