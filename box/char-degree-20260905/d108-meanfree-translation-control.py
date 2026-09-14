#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
from math import comb
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'d108'))
import meanfree_stage as A
E=A.E

def translate(tab,N,q):
 out={}
 for (r,z),co in tab.items():
  assert N-r-z>=0
  for j in range(N-r-z+1):
   pos=(r+j,z);out[pos]=out.get(pos,0)+co*comb(N-r-z,j)*q**j
 return {p:s.expand(co) for p,co in out.items() if co!=0}
def assign(tab,point):return {p:s.expand(co.subs(point)) for p,co in tab.items() if co.subs(point)!=0}
olddata=json.loads((HERE/'d108-translation-audit.json').read_text())
point={s.Symbol(n):s.sympify(v) for n,v in olddata['old_exact_stage0_assignment'].items()}
point[A.mean]=0
rows,hvars,h3=A.meanfree_incidence(E.SRC,E.SRC.k3_face,True)
assert all(s.expand(v.subs(point))==0 for _,v in rows)
h3old=assign(h3,point);h3new=translate(h3old,9,1)
j0,u,v=E.symbols_jet();c=s.Symbol('c')
newjets={j0:s.Integer(0),u:s.Integer(1),v:s.Integer(0)}
local=E.minor_local_rows(h3new,8,True)
local={p:s.expand(co.subs(newjets)) for p,co in local.items()}
pi=s.Symbol('pi');newface=s.expand(sum(co*pi**j for (n,j),co in local.items() if n==8))
assert all(co==0 for (n,j),co in local.items() if n<8)
assert newface==-((pi+1)**2-2).expand()
assert all(4*r+5*z>=35 for r,z in h3new)
# Verify the translated major h2 belongs to its actual solved source graph.
h2old,free,meta=E.build_major_h2(E.SRC,h3old,36,True)
h2old=assign(h2old,{a:0 for a in free})
h2image=translate(h2old,36,1)
h2new,newfree,newmeta=E.build_major_h2(E.SRC,h3new,36,True)
newpoint={a:h2image.get(tuple(map(int,str(a).split('_')[1:])),s.Integer(0)) for a in newfree}
h2new=assign(h2new,newpoint)
assert not meta['h2_D1_residual'] and not newmeta['h2_D1_residual']
assert all(s.expand(h2new.get(p,0)-h2image.get(p,0))==0 for p in set(h2new)|set(h2image))
# Check the outer source prefix under actual source graph coordinates at stage8.
outer,ofree,ometa=E.outer_state(E.SRC,8)
opoint={a:s.Integer(i%7-3) for i,a in enumerate(sorted(ofree,key=str))}
outerchecks=[]
for block in ('B2','A3'):
 specs=E.outer_specs(E.SRC)[block];oldtab=assign(outer[block],opoint);newtab=translate(oldtab,specs['degree'],1)
 assert all(4*r+5*z>=specs['W0'] and z<36 and r+z<=specs['degree'] for r,z in newtab)
 nrows=0
 for W in range(specs['W0'],specs['W0']+9):
  for j in range(max(0,specs['threshold']-2*W)):
   assert sum(comb(z,j)*co for (r,z),co in newtab.items() if 4*r+5*z==W and z>=j)==0
   nrows+=1
 outerchecks.append({'block':block,'moment_rows':nrows,'all_translated_moments_zero':True})
# Actual meanfree stage1 input supplies a full finite-source point.
inpath=HERE/'d108/d108_meanfree_stage1_strongfront.input.json'
inp=json.loads(inpath.read_text());t,z=s.symbols('tt zz')
values={n:s.Integer(0) for n in inp['names']};values.update({'jet0':s.Integer(1),'jet1':s.Integer(1),'jet2':s.Integer(1),'minor_mean':s.Integer(2),'c':s.Integer(3),'leader63':s.Integer(1),'Z63':s.Integer(1),'Zc':s.Rational(1,3)})
expr=s.expand(s.sympify(inp['h_expr'],locals={**values,'tt':t,'zz':z}))
htab={(int(mt[0]),int(mt[1])):co for mt,co in s.Poly(expr,t,z).terms()}
ht=translate(htab,36,1)
oldloc={p:s.expand(co.subs({j0:1,u:1,v:1})) for p,co in E.local_rows(htab,12,True).items()}
newloc={p:s.expand(co.subs(newjets)) for p,co in E.local_rows(ht,12,True).items()}
# Exact old_pi map: q=1,u=v=1 => (1+t)^3*pi+1+t.
piold=(1+t)**3*pi+1+t
transport=s.expand(sum(co*t**n*(1+t)**(36-n)*piold**j for (n,j),co in oldloc.items()))
transport={(int(mt[0]),int(mt[1])):co for mt,co in s.Poly(transport,t,pi).terms() if mt[0]<=12}
assert all(s.expand(transport.get(p,0)-newloc.get(p,0))==0 for p in set(transport)|set(newloc))
for name,power in [('F',3),('G',2)]:
 for tab in (oldloc,newloc):
  prod={(0,0):s.Integer(1)}
  for _ in range(power):prod=E.tz_mul(prod,tab,5)
  assert all(co==0 for (n,j),co in prod.items() if n<=5)
# Generic parameter and face covariance identity.
q,uu,vv,mu,cc=s.symbols('q u v mu c')
told=t/(1+q*t);ypart=uu*t+(vv-q*uu)*t**2+pi*t**3
pio=s.cancel((ypart-uu*told-vv*told**2)/told**3)
shift=q*q*uu-2*q*vv
expected=(1+q*t)**3*pi-shift+(3*q*q*vv-2*q**3*uu)*t+(q**3*vv-q**4*uu)*t*t
assert s.expand(pio-expected)==0
assert s.expand((pio-mu)**2-cc).subs(t,0)==s.expand((pi-(mu+shift))**2-cc)
out={'field':'Q','result':'PASS','adapter_sha256':hashlib.sha256(Path(A.__file__).read_bytes()).hexdigest(),
 'source_stage1_input_sha256':hashlib.sha256(inpath.read_bytes()).hexdigest(),
 'h3_translated_full_mean_incidence':True,'new_h3_face':str(newface),'new_jets':[0,1,0],'new_mean':-1,
 'actual_major_h2_graph_roundtrip':True,'outer_stage8_source_moments':outerchecks,
 'exact_minor_generic_parameter_map':str(expected),'full_minor_coefficient_transport_through':12,
 'actual_stage1_F_G_zero_prefixes_before_and_after':5,'not_a_characteristic_chart_verdict':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
