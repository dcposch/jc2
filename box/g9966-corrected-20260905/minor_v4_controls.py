#!/usr/bin/env python3
from pathlib import Path
import argparse,copy,hashlib,json,sys
import sympy as sp
ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--fixture',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();sys.path.insert(0,str(a.code.resolve()))
import minor_final_verify as M
import minor_flint_quotient_direct as Q
E=M.load_code(a.source);v=M.Verifier(E,'delta52');cert=json.loads(a.fixture.read_text());v.replay_phase(cert)
negative={}
def rejects(name,action):
 try:action()
 except (AssertionError,ValueError) as err:negative[name]=str(err);return
 raise AssertionError('negative control accepted '+name)
for key,mutate in [('field',lambda c:c.update(field='F_101')),('leader',lambda c:c['pivot_steps'][0].update(rational_leader='0')),('map',lambda c:c['map_after'].update(undeclared_variable='0'))]:
 bad=copy.deepcopy(cert);mutate(bad);rejects(key,lambda:v.replay_phase(bad))
t,z,w,d,e,b=sp.symbols('t z w test_delta test_e test_b');cs=sp.symbols('A2_c A3_c B1_c B2_c');q=d**2+sp.Rational(2,3)*e*d+sp.Rational(5,7)*b
S={'inner_power':3,'outer_power_F':3,'outer_power_G':2,'n':99,'m':66};records=[]
for high in (False,True):
 h={(0,1):sp.Integer(1),(1,0):d**3 if high else d,(2,1):e};c2={(2,0):d**4 if high else d};c3={(3,0):b};outer={name:{(i+1,i%2):c} for i,(name,c) in enumerate(zip(['A2','A3','B1','B2'],cs))}
 def poly(p):return sum(v*t**r*z**k for (r,k),v in p.items())
 H=poly(h)**3+poly(c2)*poly(h)+poly(c3);F=H**3+t*poly(outer['A2'])*H+t*poly(outer['A3']);G=H**2+t*poly(outer['B1'])*H+t*poly(outer['B2'])
 raw=sp.Poly(sp.expand((99*F-t*sp.diff(F,t))*sp.diff(G,z)-sp.diff(F,z)*(66*G-t*sp.diff(G,t))),t)
 for cap in range(7):
  actual,meta=Q.band(h,c2,c3,outer,cap,S,q,d)
  expected=sp.Poly(sp.expand(sp.rem(raw.nth(cap),q,d).subs(z,w-1)),w)
  required={int(k[0]):value for k,value in expected.terms() if value!=0}
  assert set(required)==set(actual) and all(sp.expand(required[k]-actual[k])==0 for k in required)
  records.append({'high_d_input':high,'band':cap,'metadata':meta})
rejects('nonmonic_quotient',lambda:Q.band(h,c2,c3,outer,3,S,2*q,d))
unit=M.singular_replay([('combined_coeff_A',-sp.Integer(1)),('combined_coeff_B',sp.Integer(1))],'delta52',3,a.out.with_name(a.out.stem+'-split-negative.sing'))
nonunit=M.singular_replay([('q',d*d-e),('combined',d-1)],'delta52',3,a.out.with_name(a.out.stem+'-combined-positive.sing'))
assert unit['unit_ideal'] and not nonunit['unit_ideal']
a.out.write_text(json.dumps({'status':'PASS','frozen_verifier_sha256':M.VERIFIER_SHA256_AT_IMPORT,'frozen_direct_quotient_helper_sha256':Q.OWN_SHA256,'full_FG_then_monic_remainder_controls':records,'negative_rejections':negative,'combined_row_nonunit':nonunit,'illegitimate_coefficient_splitting_unit':unit},indent=2)+'\n');print('PASS')
