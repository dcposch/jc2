#!/usr/bin/env python3
"""Independent full F/G first Taylor jets over a retained monic quadratic."""
from pathlib import Path
import hashlib,time
import sympy as sp
import flint
from flint import fmpq,fmpq_mpoly_ctx
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def corner(jets,source,relation,d,jc):
 tick=time.monotonic();q=sp.expand(relation);qp=sp.Poly(q,d);assert qp.degree()==2 and qp.LC()==1
 qa,qb=qp.nth(1),qp.nth(0);assert d not in qa.free_symbols|qb.free_symbols
 values=[sp.sympify(v) for triple in jets.values() for v in triple]+[sp.sympify(jc),q]
 allvars=sorted(set().union(*(v.free_symbols for v in values)),key=str);assert d in allvars
 base=[v for v in allvars if v!=d];assert base
 ctx=fmpq_mpoly_ctx.get(tuple(map(str,base)),'lex');zero=ctx.constant(0);one=ctx.constant(1);P0=(zero,zero);P1=(one,zero);D=(zero,one)
 for i in range(len(base)):
  exp=tuple(int(i==j) for j in range(len(base)));assert ctx.from_dict({exp:fmpq(1)}).to_dict()=={exp:fmpq(1)}
 def scalar(expr):return ctx.from_dict({exp:fmpq(int(c.p),int(c.q)) for exp,c in sp.Poly(expr,*base,domain=sp.QQ).terms()})
 na,nb=scalar(qa),scalar(qb)
 def add(a,b):return a[0]+b[0],a[1]+b[1]
 def neg(a):return -a[0],-a[1]
 def mul(a,b):
  cross=a[1]*b[1]
  return a[0]*b[0]-nb*cross,a[0]*b[1]+a[1]*b[0]-na*cross
 dp=[P1,D]
 def powerd(n):
  while len(dp)<=n:dp.append(mul(dp[-1],D))
  return dp[n]
 def encode(expr):
  ans=P0
  for (n,),coef in sp.Poly(expr,d).terms():
   native=scalar(coef);p=powerd(n);ans=add(ans,(native*p[0],native*p[1]))
  return ans
 assert all(x.is_zero() for x in encode(q)) and not all(x.is_zero() for x in D)
 def jadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
 def jmul(a,b):return (mul(a[0],b[0]),add(mul(a[1],b[0]),mul(a[0],b[1])),add(mul(a[2],b[0]),mul(a[0],b[2])))
 def jpower(a,n):
  r=(P1,P0,P0)
  for _ in range(n):r=jmul(r,a)
  return r
 blocks={name:tuple(encode(sp.sympify(v)) for v in triple) for name,triple in jets.items()}
 h=blocks['h3'];H=jadd(jadd(jpower(h,source['inner_power']),jmul(blocks['C2'],h)),blocks['C3'])
 F=jadd(jadd(jpower(H,source['outer_power_F']),jmul(blocks['A2'],H)),blocks['A3'])
 G=jadd(jadd(jpower(H,source['outer_power_G']),jmul(blocks['B1'],H)),blocks['B2'])
 J=add(add(mul(F[1],G[2]),neg(mul(F[2],G[1]))),neg(encode(sp.sympify(jc))))
 terms=[]
 for power,poly in enumerate(J):
  for exp,c in poly.to_dict().items():terms.append(sp.Rational(int(c.numerator),int(c.denominator))*d**power*sp.Mul(*(v**int(n) for v,n in zip(base,exp) if n)))
 row=sp.Add(*terms);assert sp.degree(row,d)<=1
 return row,{'method':'complete first Taylor F/G products followed by direct determinant in the proved monic coefficient quotient','quotient':str(q),'retained_generator':str(d),'base_generator_order':list(map(str,base)),'base_generator_images_checked':True,'combined_A_plus_B_d_row':True,'no_conjugate_selected':True,'helper_sha256_at_import':OWN_SHA256,'elapsed_seconds':time.monotonic()-tick,'python_flint_version':flint.__version__}
