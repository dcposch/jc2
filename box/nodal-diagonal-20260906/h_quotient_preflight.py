#!/usr/bin/env python3
"""Exact supported-lift controls for monic quotient lambda*G/R. No ideal decision."""
import sympy as S
from math import comb
from pathlib import Path
import json,hashlib,time,resource
from fractions import Fraction
w,t,pi=S.symbols('w t pi'); j0,u,v,rho,c,mu=S.symbols('j0 u v rho c mu')

def ceildiv(a,b):return -((-a)//b)
def multrunc(p,q,N):
 out=[S.Integer(0)]*(N+1)
 for i,a in enumerate(p):
  if a==0:continue
  for j,b in enumerate(q[:N+1-i]):
   if b!=0:out[i+j]+=a*b
 return [S.expand(a) for a in out]

def lift(D,spec):
 lm,wm,vm,ln,wn,vn=spec
 bp=[[S.Integer(1)]+[S.Integer(0)]*D]
 base=[0]*(D+1)
 for i,a in [(1,j0),(2,u),(3,v)]:
  if i<=D:base[i]=a
 for i in range(D):bp.append(multrunc(bp[-1],base,D))
 bounds=[]
 for r in range(D+1):
  a=max(0,ceildiv(lm*(D-r)-vm,wm));b=max(0,ceildiv(ln*(D-r)-vn,wn))
  h=D-r+1-a-b;assert h>=0
  bounds.append((a,b,h))
 a,b,h=bounds[0]
 if h==0:return None,bounds
 assert h==1
 ks=[S.Poly(S.expand(w**b*(w-1)**a),w)]
 for r in range(1,D+1):
  a,b,h=bounds[r]
  minor=[]
  for q in range(b):
   known=0
   for i,K in enumerate(ks):
    for (jj,),coef in K.terms():
     if jj>=q:known+=coef*comb(jj,q)*bp[jj-q][r-i]
   minor.append(S.expand(-known))
  inv=[S.Integer((-1)**a)*comb(a+k-1,k) if a else S.Integer(k==0) for k in range(b)]
  conv=[]
  for q in range(b):conv.append(S.expand(sum(minor[i]*inv[q-i] for i in range(q+1))))
  kr=S.expand((w-1)**a*sum(coef*w**q for q,coef in enumerate(conv)))
  assert S.degree(kr,w)<=D-r if kr!=0 else True
  ks.append(S.Poly(kr,w))
 # Check all original major/minor floor rows over unspecialized centres.
 rows=0
 for r,(a,b,h) in enumerate(bounds):
  for q in range(a):
   assert S.expand(sum(coef*comb(jj,q) for (jj,),coef in ks[r].terms() if jj>=q))==0;rows+=1
  for q in range(b):
   known=0
   for i,K in enumerate(ks[:r+1]):
    for (jj,),coef in K.terms():
     if jj>=q:known+=coef*comb(jj,q)*bp[jj-q][r-i]
   assert S.expand(known)==0;rows+=1
 def face(major=True):
  l,ww,vv=(lm,wm,vm) if major else (ln,wn,vn)
  out=0
  for r in range(D+1):
   for q in range(D+1):
    if l*r+ww*q!=l*D-vv:continue
    if major:
     coef=sum(coef*comb(jj,q) for (jj,),coef in ks[r].terms() if jj>=q)
    else:
     coef=0
     for i,K in enumerate(ks[:r+1]):
      for (jj,),cv in K.terms():
       if jj>=q:coef+=cv*comb(jj,q)*bp[jj-q][r-i]
    out+=S.expand(coef)*pi**q
  return S.expand(out)
 return {'D':D,'K':[str(K.as_expr()) for K in ks],'major_face':face(True),'minor_face':face(False),'rows_checked':rows},bounds

def main():
 start=time.monotonic();out={'status':'EXACT_Q_SUPPORTED_LIFTS_CHECKED_NOT_FULL_IDEAL_DECIDED','clients':{}}
 out['exact_face_divisions']={}
 for dd in [3,4]:
  PP=(pi**3-1)**8 if dd==3 else (pi**4-1)**7
  qq=pi-4*pi**4+S.Rational(48,7)*pi**7-S.Rational(216,35)*pi**10+S.Rational(1296,455)*pi**13-S.Rational(243,455)*pi**16 if dd==3 else pi-S.Rational(21,5)*pi**5+S.Rational(112,15)*pi**9-S.Rational(448,65)*pi**13+S.Rational(3584,1105)*pi**17-S.Rational(2048,3315)*pi**21
  leader=-S.Rational(243,455) if dd==3 else -S.Rational(2048,3315)
  hh,rr=S.div(S.expand(leader*PP**2),S.expand(PP*qq),pi)
  target=pi**8-S.Rational(8,3)*pi**5+S.Rational(20,9)*pi**2 if dd==3 else pi**7-S.Rational(7,4)*pi**3
  assert S.expand(hh-target)==0
  assert S.degree(rr,pi)<S.degree(PP*qq,pi) and rr.subs(pi,0)==leader
  out['exact_face_divisions'][str(dd)]={'H_major':str(hh),'S_major_over_C':str(rr),'S_major_degree':int(S.degree(rr,pi)),'S_major_constant_over_C':str(leader)}
 clients=[('99_delta2',11,(3,4,1,1,3,2)),('99_delta52',11,(3,4,1,2,7,1)),('108_free_mean',9,(4,5,1,1,4,1))]
 for name,K,spec in clients:
  lM,wM,vHM,lN,wN,vHN=spec
  DR=55 if K==11 else 63; dg=66 if K==11 else 72
  vRM=5 if K==11 else 7;vRN=10 if name=='99_delta2' else 5 if K==11 else 7
  aR=40 if K==11 else 49;bR=15 if K==11 else 14
  for N in range(DR,dg+1):
   ag=ceildiv(lM*N-vRM-vHM,wM);bg=ceildiv(lN*N-vRN-vHN,wN)
   assert ag>=aR and bg>=bR
   assert ag-aR==ceildiv(lM*(N-DR)-vHM,wM)
   assert bg-bR==ceildiv(lN*(N-DR)-vHN,wN)
  basis=[];allbounds=[]
  for D in range(K+1):
   liftdata,bounds=lift(D,spec);allbounds.append([D,bounds])
   if liftdata:basis.append(liftdata)
  aa=S.symbols('h0:'+str(len(basis)))
  fm=sum(a*b['major_face'] for a,b in zip(aa,basis))
  fn=sum(a*b['minor_face'] for a,b in zip(aa,basis))
  targetM=pi**8-S.Rational(8,3)*pi**5+S.Rational(20,9)*pi**2 if K==11 else pi**7-S.Rational(7,4)*pi**3
  targetN=pi**2*(pi+3*rho) if name=='99_delta2' else pi*(pi*pi-c) if K==11 else -((pi-mu)**2-c)
  eq=[S.expand(fm-targetM).coeff(pi,k) for k in range(K+1)]+[S.expand(fn-targetN).coeff(pi,k) for k in range(K+1)]
  M,rhs=S.linear_eq_to_matrix(eq,aa)
  solutions=list(S.linsolve((M,rhs),aa));assert len(solutions)==1
  vals=solutions[0]
  assert all(S.expand(e.subs(dict(zip(aa,vals))))==0 for e in eq)
  free=[a for a in aa if any(a in z.free_symbols for z in vals)]
  expected=3 if name=='99_delta2' else 1
  assert len(free)==expected
  pivotcols=[i for i,a in enumerate(aa) if a not in free]
  pivotrows=list((M[:,pivotcols].T).rref()[1])
  determinant=S.factor(M[pivotrows,pivotcols].det())
  assert determinant.is_Rational and determinant!=0
  assert len(pivotrows)==len(pivotcols)
  out['clients'][name]={'spec':spec,'all_supported_lift_bounds':allbounds,'support_basis_degrees':[b['D'] for b in basis],'basis':[{**b,'major_face':str(b['major_face']),'minor_face':str(b['minor_face'])} for b in basis],'H_coefficients_after_both_whole_faces':len(free),'H_solution':{str(a):str(vv) for a,vv in zip(aa,vals)},'free_H_variables':[str(a) for a in free],'face_unit_pivot_rows':pivotrows,'face_unit_pivot_columns':pivotcols,'face_unit_pivot_determinant':str(determinant),'all_symbolic_floor_rows_checked':sum(b['rows_checked'] for b in basis),'full_face_rows_checked':len(eq)}
 xx,yy,ss=S.symbols('x y s');zz=yy-xx
 Htoy=yy**3*zz**8-S.Rational(8,3)*yy**2*zz**5+yy*zz**3+S.Rational(20,9)*yy*zz**2
 Ttoy=S.Rational(262236,597051)*xx*yy**3*zz**7-S.Rational(706612,597051)*yy**3*zz**4+yy**2*zz
 majH=S.expand(ss*Htoy.subs({xx:ss**-3,yy:ss**-3+pi*ss}, simultaneous=True))
 minH=S.expand(ss*Htoy.subs({xx:ss**-2,yy:pi*ss**5}, simultaneous=True))
 majT=S.expand(ss**5*Ttoy.subs({xx:ss**-3,yy:ss**-3+pi*ss}, simultaneous=True))
 minT=S.expand(ss**4*Ttoy.subs({xx:ss**-2,yy:pi*ss**5}, simultaneous=True))
 for ee in [majH,minH,majT,minT]:S.Poly(ee,ss,pi)
 assert S.expand(majH.coeff(ss,0)-(pi**8-S.Rational(8,3)*pi**5+S.Rational(20,9)*pi**2))==0
 assert S.expand(minH.coeff(ss,0)-pi*(pi**2-1))==0
 assert S.expand(majT.coeff(ss,0)-pi*(262236*pi**6-706612*pi**3+597051)/597051)==0
 assert S.Poly(Ttoy,xx,yy).total_degree()==11 and S.degree(Ttoy,yy)==10
 out['delta52_reverse_remainder_nonobstruction_control']={'H':str(Htoy),'T':str(Ttoy),'C':1,'lambda':'-243/455','c':1,'j0':0,'u':0,'v':0,'scope':'H and reverse-remainder face control only, not a complete necessary-chart witness','all_four_exact_cover_checks':True}
 out['elapsed_seconds']=time.monotonic()-start;out['cpu_seconds']=time.process_time();out['max_rss_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 out['driver_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:out[k] for k in ['status','elapsed_seconds','cpu_seconds','max_rss_KiB']}))
 print({k:(v['support_basis_degrees'],v['H_coefficients_after_both_whole_faces']) for k,v in out['clients'].items()})
if __name__=='__main__':main()
