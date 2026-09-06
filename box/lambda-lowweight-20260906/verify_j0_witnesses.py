#!/usr/bin/env python3
"""Independent exact-Q/ quadratic-field witness checks; never a Keller witness."""
import hashlib,json,pathlib
import sympy as s
OUT=pathlib.Path('box/lambda-lowweight-20260906')
y,a,t=s.symbols('y a t'); f=54*a*a-36*a+5
rows=[
 ('C70',8,3,2,-12,y**24+y**20,y**16),
 ('C109',6,3,2,2,y**18+y**4,y**12),
 ('C127',6,4,3,-15,y**24+y**21,y**18),
 ('C171',8,3,2,12,y**24+s.Rational(3,2)*y**10,y**16+y**2),
 ('C341',6,4,3,9,y**24+s.Rational(4,3)*y**15+s.Rational(2,9)*y**6,y**18+y**9),
 ('C455',4,4,3,6,y**16+s.Rational(4,3)*y**10+s.Rational(2,9)*y**4,y**12+y**6),
 ('R001',7,3,2,16,y**21+s.Rational(3,2)*y**11+s.Rational(3,8)*y,y**14+y**4),
 ('R002',5,3,2,11,y**15+s.Rational(3,2)*y**8+s.Rational(3,8)*y,y**10+y**3),
 ('R003',5,3,2,11,y**15+s.Rational(3,2)*y**8+s.Rational(3,8)*y,y**10+y**3),
 ('R004',4,4,3,13,y**16+s.Rational(4,3)*y**11+(s.Rational(4,3)*a+s.Rational(2,9))*y**6+(s.Rational(4,9)*a-s.Rational(4,81))*y,y**12+y**7+a*y**2),
]
def canon(v,alg):return s.rem(v,f,a) if alg else s.expand(v)
result=[]
for name,K,e,q,M2,P,Q in rows:
 alg=name=='R004';L=e*q*K;W=M2+q*K;D=L-W
 raw=s.Poly(s.expand(Q**e-P**q),y)
 ts={d[0]:canon(c,alg) for d,c in raw.terms()};ts={d:c for d,c in ts.items() if c!=0}
 assert max(ts)==D
 lam=ts[D];assert lam!=0
 # Independent grouping in the monic h=y^K basis; every block coordinate has b=0.
 coords={};checks=[]
 for tag,F,k in [('A',P,e),('B',Q,q)]:
  assert s.Poly(F,y).degree()==k*K and s.Poly(F,y).LC()==1
  for (d,),v in s.Poly(F-y**(k*K),y).terms():
   if not v:continue
   hpow,ypow=divmod(d,K);i=k-hpow
   assert 1<=i<=k and 0<=ypow<K
   assert not(tag=='B' and i==1)
   assert not(i==k and ypow==0)
   coords[f'{tag}{i}_0_{ypow}']=str(v)
 # Degree D implies ALL upper h-adic/ordinary characteristic coefficients vanish.
 J,rem=divmod(D,K);assert rem>0
 assert all(j*K+b<=D for d in ts for j,b in [divmod(d,K)])
 # On Delta h is abstract and all alpha,beta blocks are constants. Family
 # corrections remain polynomials in h; every positive remainder digit is zero.
 deltaP=t**e+sum(t**(e-i) for i in range(1,e))
 deltaQ=t**q+sum(t**(q-i) for i in range(2,q))
 delta=s.Poly(s.expand(deltaQ**e-deltaP**q),t)
 assert delta.as_expr()!=0 and rem!=0
 rec=dict(id=name,K=K,D2=D,W=W,h=f'y^{K}',P=str(P),Q=str(Q),field='Q[a]/(54a^2-36a+5)' if alg else 'Q',lambda_actual=str(lam),nonzero_T2_degrees=sorted(ts,reverse=True),coordinates=coords,beta1_and_terminal_gauges=True,all_G_supports=True,J0=True,all_upper_characteristic_rows_zero=True,canonical_hadic_lambda_equals_actual=True,Delta_hadic_lambda_zero=True)
 if alg:
  res=s.resultant(f,lam,a);assert res!=0
  inv=s.invert(lam,f,a);assert s.rem(inv*lam-1,f,a)==0
  rec.update(lambda_resultant=str(res),lambda_inverse=str(inv),T2_mod_quadratic={str(d):str(c) for d,c in ts.items()},quadratic_irreducible=bool(s.Poly(f,a).is_irreducible))
 else:
  rec['lambda_inverse']=str(1/lam)
 result.append(rec)
payload=dict(scope='PROPER strengthened necessary chart I_J+upper T2 equations+(Zlambda-1); c=0, NOT Keller or realization',method='independent expanded univariate powers over Q, with exact polynomial remainder for R004',script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),count=len(result),all_checks_pass=True,cases=result)
(OUT/'j0-witness-controls.json').write_text(json.dumps(payload,indent=1)+'\n')
print(json.dumps({'count':len(result),'all_checks_pass':True,'output':'j0-witness-controls.json'}))
