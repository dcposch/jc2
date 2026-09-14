"""Tiny degree-five top maps and scalar-order controls, never source pairs."""
from fractions import Fraction as F
import json, sys
zero=(F(0),F(0)); one=(F(1),F(0)); a=(F(0),F(1))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def rat(n): return (F(n),F(0))
def inv(x):
 norm=x[0]*x[0]+x[0]*x[1]-x[1]*x[1]
 if not norm: raise ValueError('zero divisor')
 return ((x[0]+x[1])/norm,-x[1]/norm)
def power(x,n):
 if n<0: return power(inv(x),-n)
 y=one
 for _ in range(n): y=mul(y,x)
 return y
def ps(P,Q):
 out=dict(P)
 for k,v in Q.items(): out[k]=add(out.get(k,zero),v)
 return {k:v for k,v in out.items() if v!=zero}
def scale(P,c): return {k:mul(v,c) for k,v in P.items() if mul(v,c)!=zero}
def pm(P,Q):
 out={}
 for k,v in P.items():
  for l,w in Q.items():
   e=(k[0]+l[0],k[1]+l[1])
   if sum(e)>5: raise ValueError('degree-five cap')
   out[e]=add(out.get(e,zero),mul(v,w))
 return {k:v for k,v in out.items() if v!=zero}
def pp(P,n):
 out={(0,0):one}
 for _ in range(n): out=pm(out,P)
 return out
def deriv(P,i):
 out={}
 for k,v in P.items():
  if k[i]:
   e=list(k); e[i]-=1; out[tuple(e)]=mul(rat(k[i]),v)
 return out
def jac(P,Q): return ps(pm(deriv(P,0),deriv(Q,1)),scale(pm(deriv(P,1),deriv(Q,0)),rat(-1)))
g={(1,0):one}; p={(0,1):one}; bad=sys.argv[1] if len(sys.argv)>1 else 'none'
t=inv(a); rho=power(t,2)
if bad=='bad-slope': rho=rat(F(1,4))
source_p=scale(p,a if bad=='wrong-map-sign' else neg(a))
H_old_sub=pm(pp(source_p,2),pm(pp(ps(source_p,scale(g,rat(-1))),2),ps(source_p,scale(g,neg(a)))))
H_new=pm(pp(p,2),pm(ps(p,g),pp(ps(p,scale(g,t)),2)))
scalar=power(neg(a),5)
claims={
 'golden_minpoly':add(sub(power(rho,2),mul(rat(3),rho)),one)==zero,
 't_equation':sub(add(power(t,2),t),one)==zero,
 'golden_top_map':H_old_sub==scale(H_new,scalar),
 'squarefree_top_map':pm(pp(p,2),ps(pp(p,3),scale(pp(scale(g,rat(-1)),3),rat(-1))))==pm(pp(p,2),ps(pp(p,3),pp(g,3))),
 'swap_and_determinant':jac(source_p,g)=={(0,0):a},
 'normalized_scalar':mul(a,power(scalar,-8))==power(a,-39),
 'cusp_budget_8_4_is_not_strict':F(23*8,9-4)>36,
 'double_budget_8_3_is_not_strict':F(15*8,6-3)>36,
 'two_strict_thresholds':F(23*9,6)<36 and F(15*7,3)<36,
 'p_point_has_nonzero_generic_target':True,  # explanatory only, excluded from checks below
}
del claims['p_point_has_nonzero_generic_target']
if bad=='wrong-swap': claims['swap_and_determinant']=jac(g,source_p)=={(0,0):a}
print(json.dumps(dict(mutation=bad,claims=claims,passed=all(claims.values()),scope='factor/scalar controls only; no polynomial receiver')))
if not all(claims.values()): raise SystemExit(2)
