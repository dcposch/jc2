#!/usr/bin/env python3
"""Independent exhaustive fixed-global-characteristic sibling closure, Fraction arithmetic.
Only frozen roster input. Moh Prop5.3 takes every major factor r -> r-1; no A/B.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,lcm
import json
from pathlib import Path
ROOT=Path('/tmp/jc2-lane.QKyQBy/inputs')
OUT=Path('box/exact-contact-gate-20260906')
ROWS={r['row_id']:r['source'] for r in map(json.loads,open(ROOT/'roster.jsonl'))}
TARGETS=['R001','R009','R025','R026','R027','R028','R050','R057','R058']
@lru_cache(None)
def partitions(n,lo=1):
    if n==0:return ((),)
    return tuple((a,)+b for a in range(lo,n+1) for b in partitions(n-a,a))

def patterns(P,Q,A,threshold,selected=None):
    for z in range(P%A,P+1,A):
      if A==1 and z>0:continue # Translate centre within its existing lattice.
      if z and z==threshold:continue
      for part in partitions((P-z)//A):
        if A*len(part)+(z>0)>Q:continue
        if any(x==threshold for x in part):continue
        if not any(x>threshold for x in ((z,) if z else ())+part):continue
        if selected is not None and selected not in ((z,) if z else ())+part:continue
        yield z,part

def ser(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):ser(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return list(map(ser,x))
    return x

class Closure:
 def __init__(self,row):
    self.row=row; self.n=row['n'];self.m=row['m'];self.d=[None]+row['d'];self.M=[None]+row['M'];self.V=[None,None]+row['V'];self.s=row['s'];self.log={}
 @lru_cache(None)
 def node(self,i,rho,kappa,L,selected_path=False):
    n,m=self.n,self.m
    W=n-self.M[i]
    delta=1-F(W)*kappa/(W*rho-m)
    lam=F(m)*kappa/(W*rho-m)
    A=(L*delta).denominator
    if i==1:
      rg=F(n)*rho/m
      remf=rho%A;remg=rg%A
      # Both are squarefree and coprime from Prop4.6 r=1 differential identity.
      good=(rg.denominator==1 and remf in (0,1) and remg in (0,1) and not(remf==remg==1))
      # Weak check is report's necessary individual residue law.
      weak=(rg.denominator==1 and remf in (0,1) and remg in (0,1))
      J=F(n)*rho*kappa/((n+m)*rho-m)
      self.log[(i,rho,kappa,L,selected_path)]={'i':i,'rho_f':rho,'rho_g':rg,'kappa':kappa,'L':L,'delta':delta,'A':A,'final_J':J,'galois_ok':good,'weak_galois_ok':weak}
      return {(J,F(0))} if good else set()
    P=F(rho*self.d[i],m);Q=F(rho*W,m)
    if P.denominator>1 or Q.denominator>1:
      self.log[(i,rho,kappa,L,selected_path)]={'i':i,'rho_f':rho,'kappa':kappa,'L':L,'delta':delta,'P':P,'Q':Q,'failure':'P_or_Q_noninteger'}
      return set()
    pats=[];allvals=set();threshold=F(self.d[i],W)
    for z,part in patterns(int(P),int(Q),A,threshold,self.V[i] if selected_path else None):
      factors=([(z,1,'zero')] if z else [])+[(x,A,'orbit') for x in part]
      vals={(F(0),F(0))};factorlog=[]
      # Pattern root selection: one V_i factor uses designated lower path.
      sel_used=False
      for r,count,typ in factors:
        crho=F(m*r,self.d[i]);ck=crho*(1-delta)-lam
        assert crho.denominator==1
        crho=int(crho)
        if ck<0:
          cv={(F(0),-ck/crho)};state={'type':'minor','rho':crho,'kappa':ck,'delta':1-ck/crho}
        else:
          use_sel=selected_path and r==self.V[i] and not sel_used
          if use_sel:sel_used=True
          childL=L if typ=='zero' else lcm(L,delta.denominator)
          cv=self.node(i-1,crho,ck,childL,use_sel)
          state={'type':'major','i':i-1,'rho':crho,'kappa':ck,'L':childL,'selected':use_sel,'outcomes':len(cv)}
        factorlog.append({'r':r,'count':count,'kind':typ,**state})
        # Nonzero Galois orbit must have same subtree. Distinct repeated orbits may differ.
        vals={(a+count*c,b+count*d) for a,b in vals for c,d in cv}
      pats.append({'z':z,'orbit_multiplicities':part,'factors':factorlog,'outcomes':len(vals),'values':sorted(vals)})
      allvals|=vals
    self.log[(i,rho,kappa,L,selected_path)]={'i':i,'rho_f':rho,'kappa':kappa,'L':L,'delta':delta,'A':A,'P':P,'Q':Q,'selected_path':selected_path,'threshold':threshold,'patterns':pats,'outcomes':len(allvals),'values':sorted(allvals)}
    return allvals
 def run(self):
    # Prop4.5 principal split D_s at delta=-1, lambda_f=-m.
    rho=F(self.m*self.row['v_s'],self.d[self.s]);kappa=2*rho-self.m
    assert rho.denominator==1
    vals=self.node(self.s-1,int(rho),kappa,1,True)
    minor_base=1+F(self.row['v_s'],self.row['u_s'])-1
    vals={(im,minor_base+mn) for im,mn in vals}
    return {'source':self.row,'finite_major_levels':self.s-1,'uses_lemma_A':False,'uses_lemma_B':False,'minor_base':minor_base,'full_outcomes':sorted(vals),'integral_major':sorted(v for v in vals if v[0].denominator==1),'survivors':sorted(v for v in vals if v[0].denominator==1 and v[0]>=v[1]),'nodes':[self.log[k] for k in sorted(self.log)]}

if __name__=='__main__':
 out={}
 for rid in TARGETS:
   c=Closure(ROWS[rid]);res=c.run();out[rid]=ser(res)
   print(rid,'nodes',len(c.log),'outcomes',len(res['full_outcomes']),'survivors',res['survivors'])
 (OUT/'closure-fixed-results.json').write_text(json.dumps(out,indent=2)+'\n')
