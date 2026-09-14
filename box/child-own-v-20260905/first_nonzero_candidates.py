#!/usr/bin/env python3
"""Independent exact-rational necessary route enumeration; no pair realization claim.
Prints raw candidates before child root bounds; full source denominators used
until first nonzero coefficient. No whole-sibling source realization inferred.
"""
import json, importlib.util
from pathlib import Path
from fractions import Fraction as F
from collections import Counter, defaultdict

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('frozen_skeleton_own_probe','/tmp/jc2-lane.wwyG4k/inputs/moh_skeleton_full.py')
B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)


def childchain(n,M):
 from math import gcd
 d=[n]
 for m in M:d.append(gcd(d[-1],m))
 return d


def candidates(n,m,Ms,V,q_capacity=False):
 S=B.Skel(n,m,Ms,V);s=S.s;u=S.d[s]-S.V[s];q=S.d[s]
 np=n*u//q;Mp=[S.M[i]*u//q for i in range(1,s)];dp=childchain(np,Mp)
 res=[]; rejected=[]
 for j in range(2,s):
  why=[];route=[]
  if S.delta[j]<=0: why.append('first_nonzero_radius_not_positive')
  for k in range(s-1,j-1,-1):
   P=S.V[k+1]*S.d[k]//S.d[k+1]
   Q=S.V[k+1]*(n-S.M[k])//S.d[k+1]
   b=S.delta[k].denominator;Vk=S.V[k]
   if k>j:
    valid=(P-Vk)>=0 and (P-Vk)%b==0
    z=Vk;orbits=(P-z)//b if valid else None
    if q_capacity and valid: valid=Q>=int(z>0)+b*int(orbits>0)
    if not valid:why.append(f'zero_infeasible_{k}')
    route.append({'k':k,'mode':'zero/removable','P':P,'Q':Q,'den':b,'z':z,'orbit_mass':orbits})
   else:
    valid=P>=b*Vk; zs=[]
    if valid:
     for z in range(P%b,P-b*Vk+1,b):
      mass=(P-z)//b-Vk
      if not q_capacity or Q>=int(z>0)+b*(1+int(mass>0)):zs.append(z)
     valid=bool(zs)
    if not valid:why.append(f'nonzero_infeasible_{k}')
    route.append({'k':k,'mode':'nonzero','P':P,'Q':Q,'den':b,'z_candidates':zs})
  W={i:F(S.V[i]) for i in range(2,j+1)}
  rem=F(np)
  for k in range(s-1,j,-1):
   C=F(n*S.V[k+1],S.d[k+1]);CZ=F(n*S.V[k],S.d[k])
   rem-=S.delta[k]*(C-CZ)
   W[k]=rem/F(n,S.d[k])
  defects=[]
  for i in range(2,s):
   if W[i].denominator!=1:defects.append(f'nonintegral_{i}')
   if W[i]<=0:defects.append(f'nonpositive_{i}')
   if W[i]>dp[i-1]:defects.append(f'above_total_roots_{i}')
   if W[i]<=F(dp[i-1],np-Mp[i-1]):defects.append(f'below_major_window_{i}')
   if i<s-1 and W[i]>W[i+1]*F(dp[i-1],dp[i]):defects.append(f'unnested_{i}')
  rec={'first_nonzero':j,'W':[str(W[i]) for i in range(2,s)],'route':route,'defects':defects}
  if why:rec['rejections']=why;rejected.append(rec)
  else:res.append(rec)
 return {'n':n,'m':m,'M':[-m]+list(Ms),'V':[S.V[i] for i in range(2,s+1)],'u_s':u,'n_prime':np,'M_prime':Mp,'d_prime':dp,'drops':int(Mp[-1]==np-1),'candidates':res,'rejected':rejected}


def summary(rows):
 out={'rows':len(rows),'candidate_sizes':Counter(),'tuple_sizes':Counter(),'defects':Counter(),'empty_us':Counter(),'per_level':defaultdict(Counter),'u_neg':Counter(),'ctop':Counter()}
 for r in rows:
  out['candidate_sizes'][len(r['candidates'])]+=1
  poss={tuple(x['W']) for x in r['candidates']};out['tuple_sizes'][len(poss)]+=1
  if not poss:out['empty_us'][r['u_s']]+=1
  for c in r['candidates']:out['defects'].update(c['defects'])
  for i in range(2,len(r['M_prime'])+1-r['drops']):
   vals={F(p[i-2]) for p in poss};base=r['V'][i-2]
   typ='empty' if not vals else 'determined' if len(vals)==1 else 'set_valued'
   out['per_level'][i][typ]+=1
   if vals:out['per_level'][i]['always_equal' if vals=={base} else 'always_different' if base not in vals else 'sometimes_different']+=1
  utests={F(p[0])>r['d_prime'][1] for p in poss}
  out['u_neg'][str(sorted(utests))]+=1
  h=len(r['M_prime'])-r['drops'];tests={F(p[h-2])>r['d_prime'][h-1] for p in poss}
  out['ctop'][(('licensed_' if r['u_s']==1 else 'conditional_')+str(sorted(tests)))]+=1
 return out


def main():
 src=json.load(open('/home/ubuntu/jc2/box/ctop-gate-20260905/enum-replay.json'))
 out={}
 for cap in [False,True]:
  rows=[candidates(r['n'],r['m'],r['Ms'],{int(k):v for k,v in r['V'].items()},cap) for r in src['operative_rows']]
  out['with_q_capacity' if cap else 'without_q_capacity']={'summary':summary(rows),'rows':rows}
 controls=[]
 for r in src['moh_table'][:5]:controls.append(candidates(r['n'],r['m'],r['Ms'],{int(k):v for k,v in r['V'].items()}))
 controls.extend([candidates(180,120,[132,150,178],{2:2,3:4,4:5}),candidates(96,72,[36,78,94],{2:4,3:3,4:5})])
 out['controls']=controls
 (HERE/'first-nonzero-candidates.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v['summary'] for k,v in out.items() if k!='controls'},indent=2))
 print(json.dumps({'controls':controls},indent=2))

if __name__=='__main__':main()
