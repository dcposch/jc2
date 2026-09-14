#!/usr/bin/env python3
"""Damped Gauss--Newton search on the exact even/odd coefficient system."""
import contextlib,importlib.util
from pathlib import Path
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
with open('/dev/null','w') as f,contextlib.redirect_stdout(f):
 z=importlib.util.spec_from_file_location('eo',HERE/'even_odd_distribution.py');eo=importlib.util.module_from_spec(z);z.loader.exec_module(eo)
x=s.symbols('x'); avec=s.symbols('a0:4');bvec=s.symbols('b0:7');cvec=s.symbols('q1:10')
A=sum(v*x**i for i,v in enumerate(avec));B=sum(v*x**i for i,v in enumerate(bvec));C=sum(cvec[i-1]*x**i for i in range(1,10))
sub={eo.A:A,eo.B:B,eo.C:C,eo.dA:s.diff(A,x),eo.dB:s.diff(B,x),eo.dC:s.diff(C,x)}
forms=[s.cancel(z.subs(sub)) for z in eo.forms];forms[2]=s.expand(forms[2]-x**8)
vars=list(avec)+list(bvec)+list(cvec)+[eo.k3,eo.k2,eo.k1,eo.k0]
eq=[]
for form in forms:
 p=s.Poly(form,x)
 eq += [s.cancel(z) for z in p.all_coeffs() if z!=0]
# Scale each equation by the l2 norm of its integer/rational coefficient vector.
scaled=[]
for z in eq:
 pp=s.Poly(z,*vars)
 norm=float(np.sqrt(sum(float(q)**2 for q in pp.coeffs())))
 scaled.append(z/max(norm,1.0))
print('vars',len(vars),'eq',len(eq),flush=True)
fun=s.lambdify([vars],scaled,'numpy',cse=True)
jac=s.lambdify([vars],s.Matrix(scaled).jacobian(vars),'numpy',cse=True)

rng=np.random.default_rng(20260905)
best=(1e100,None)
for trial in range(120):
 u=rng.normal(0,1,len(vars))
 # Seed highest coefficients more substantially to avoid the c=0 cone.
 u[3]=rng.choice([-2.,-1.,1.,2.]);u[10]=rng.choice([-2.,-1.,1.,2.]);u[19]=rng.choice([-2.,-1.,1.,2.])
 lam=1e-3
 for it in range(350):
  f=np.asarray(fun(u),dtype=float).reshape(-1); J=np.asarray(jac(u),dtype=float)
  loss=float(f@f)
  if loss<best[0]:best=(loss,u.copy());print('BEST',trial,it,loss,float(np.max(np.abs(f))),u.tolist(),flush=True)
  if np.max(np.abs(f))<1e-10:break
  # Column-scaled Levenberg-Marquardt.
  scale=np.maximum(np.linalg.norm(J,axis=0),1e-8)
  Js=J/scale
  try: step=np.linalg.solve(Js.T@Js+lam*np.eye(len(vars)),-Js.T@f)/scale
  except np.linalg.LinAlgError: lam*=10;continue
  # Trust radius keeps high-degree polynomial steps sane.
  sn=np.linalg.norm(step)
  if sn>2:step*=2/sn
  un=u+step;fn=np.asarray(fun(un),dtype=float).reshape(-1);ln=float(fn@fn)
  if np.isfinite(ln) and ln<loss:u=un;lam=max(lam/3,1e-12)
  else:lam=min(lam*10,1e12)
 if np.max(np.abs(np.asarray(fun(u),dtype=float)))<1e-8:
  print('SOLUTION',trial,u.tolist(),flush=True);break
print('FINAL_BEST',best[0],best[1].tolist() if best[1] is not None else None)
