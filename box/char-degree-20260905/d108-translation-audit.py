#!/usr/bin/env python3
"""Exact covariance control using the actual frozen D108 h3 incidence."""
import importlib.util,sys,json,hashlib
from pathlib import Path
from math import comb
import sympy as s
HERE=Path(__file__).resolve().parent
path=HERE.parent/'d108-rekill-20260905/work/rekill_engine.py'
spec=importlib.util.spec_from_file_location('d108_translation_audit_engine',path)
E=importlib.util.module_from_spec(spec);sys.modules[spec.name]=E;spec.loader.exec_module(E)
rows,hvars,h3=E.minor_incidence(E.SRC,E.SRC.k3_face,True)
j0,j1,j2=E.symbols_jet();c=s.Symbol('c')
jets={j0:s.Integer(1),j1:s.Integer(1),j2:s.Integer(1),c:s.Integer(2)}
r2=[(label,s.expand(row.subs(jets))) for label,row in rows]
res,mapping,piv,zero=E.qstar_reduce(r2,set(hvars))
assert res==[]
free=set(hvars)-set(mapping)
assignment={v:s.Integer(0) for v in free};assignment.update(jets)
for _ in range(len(mapping)+1):
 for v,rhs in mapping.items():
  value=s.expand(rhs.subs(assignment))
  if not value.free_symbols:assignment[v]=value
assert all(v in assignment for v in hvars)
assert all(s.expand(row.subs(assignment))==0 for _,row in rows)
old={p:s.expand(v.subs(assignment)) for p,v in h3.items()}
q=s.Integer(1);trans={}
for (r,p),v in old.items():
 deg=9-r-p;assert deg>=0
 for k in range(deg+1):
  key=(r+k,p);trans[key]=trans.get(key,0)+v*comb(deg,k)*q**k
trans={p:s.expand(v) for p,v in trans.items() if v!=0}
newjets={j0:s.Integer(0),j1:s.Integer(1),j2:s.Integer(0)}
local=E.minor_local_rows(trans,8,True)
pi=s.symbols('pi')
face=s.expand(sum(v.subs(newjets)*pi**power for (lp,power),v in local.items() if lp==8))
A=q**2*jets[j1]-2*q*jets[j2]
expected=s.expand(-((pi-A)**2-jets[c]))
assert face==expected
assert face.coeff(pi,1)==-2
restored=s.expand(face.subs(pi,pi+A))
assert restored==-pi**2+2
out={'engine_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'only_declared_jet_symbols':[str(v) for v in E.symbols_jet()],
 'old_exact_stage0_assignment':{str(k):str(v) for k,v in assignment.items()},
 'all_old_raw_h3_incidence_rows_vanish':True,'diagonal_translation_q':'1',
 'new_strict_jets':{str(k):str(v) for k,v in newjets.items()},
 'required_new_at_level_mean':str(A),'new_actual_h3_face':str(face),
 'frozen_even_face_linear_residual':str(face.coeff(pi,1)),
 'reparametrized_face_with_explicit_mean':str(restored),
 'conclusion':'D108 jet0=0 slice has no generic diagonal-translation coverage in the frozen three-jet chart'}
(HERE/'d108-translation-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='old_exact_stage0_assignment'},indent=2))
