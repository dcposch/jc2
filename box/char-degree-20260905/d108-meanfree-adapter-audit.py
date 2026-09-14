#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'d108'))
import meanfree_stage as A
E=A.E;mu=A.mean
old,hvars,h3=A.old_incidence(E.SRC,E.SRC.k3_face,True)
new,newvars,newh3=A.meanfree_incidence(E.SRC,E.SRC.k3_face,True)
assert hvars==newvars and h3==newh3 and mu not in hvars
O=dict(old);N=dict(new)
for key in set(O)|set(N):
 diff=s.expand(N.get(key,0)-O.get(key,0))
 assert diff==({'minor_n8_pi1':-2*mu,'minor_n8_pi0':mu**2}.get(key,s.Integer(0)))
 assert s.expand(N.get(key,0).subs(mu,0)-O.get(key,0))==0
pi,c,alpha=s.symbols('pi c alpha',nonzero=True)
# Use exact original symbols for coefficient comparisons.
pi0,c0=s.symbols('pi c')
for name,power in [('F',12),('G',8)]:
 tab=A.meanfree_target(name)
 expr=sum(co*pi0**j for j,co in tab.items())
 assert s.expand(expr-((pi0-mu)**2-c0)**power)==0
 assert s.expand(expr.subs(mu,0)-(pi0*pi0-c0)**power)==0
# Dilation transforms the entire quadratic, with no leader pin.
assert s.expand(alpha**-8*((alpha**4*pi-mu)**2-c)-((pi-mu*alpha**-4)**2-c*alpha**-8))==0
records=[]
for stage in (0,1):
 path=HERE/'d108'/f'd108_meanfree_stage{stage}_strongfront.input.json'
 inp=json.loads(path.read_text());meta=json.loads(path.with_name(path.name.replace('.input.json','.map.json')).read_text())
 assert hashlib.sha256(path.read_bytes()).hexdigest()==meta['input_sha256']
 assert meta['adapter_sha256']==hashlib.sha256(Path(A.__file__).read_bytes()).hexdigest()
 assert 'minor_mean' in inp['names'] and meta['mean_free'] and meta['jet0_free']
 assert all(p['variable']!='minor_mean' for p in meta['pivot_ledger'])
 assert all(s.sympify(p['leader']).is_Rational and s.sympify(p['leader'])!=0 for p in meta['pivot_ledger'])
 assert meta['strong_front_ledger']['D_cut_inclusive']==(32 if stage==0 else 33)
 assert meta['strong_front_ledger']['C_cut_inclusive']==(66 if stage==0 else 68)
 assert meta['computational_translation'] is False and meta['arc_unchanged']
 assert meta['leading_targets_generalized']=={'F':'((pi-minor_mean)^2-c)^12','G':'((pi-minor_mean)^2-c)^8'}
 assert all(name in inp['names'] for name in ['target_a','target_b','target_c','target_d','target_e','leader63','Z63','c','Zc'])
 records.append({'stage':stage,'input_sha256':meta['input_sha256'],'names':len(inp['names']),
  'minor_mean_occurrences_in_h':inp['h_expr'].count('minor_mean'),
  'source_residual_count':len(inp['residual_strings']),'mu_absent_from_pivots':True,
  'all_pivot_leaders_nonzero_rational':True,'strong_front':meta['strong_front_ledger']})
out={'field':'Q','result':'PASS','adapter_sha256':hashlib.sha256(Path(A.__file__).read_bytes()).hexdigest(),
 'raw_incidence_mu0_recovers_all_frozen_rows':True,'mu_not_in_initial_h3_elimination_set':True,
 'whole_F_G_targets_checked':True,'dilation_covariance':{'jet0':'alpha^-1','u':'alpha^-2','v':'alpha^-3','mu':'alpha^-4','c':'alpha^-8','beta':'alpha^-5'},
 'inputs':records,'not_a_computational_chart_verdict':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
