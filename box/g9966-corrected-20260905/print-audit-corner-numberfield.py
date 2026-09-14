#!/usr/bin/env python3
"""Exact field transport of the saved necessary corner row; no e specialization."""
import hashlib,json,subprocess,time,re
from pathlib import Path
import sympy as s
N=Path(__file__).resolve().parent; pre=N/'print-audit-corner-numberfield-delta52'; start=time.monotonic()
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(x):pre.with_suffix('.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
p=N/'print-audit-corner-quotient-delta52.phase.json';phase=json.loads(p.read_text());source=json.loads((N/'print-audit-corner-quotient-delta52.json').read_text());cfg=source['quotient'];d,e=s.symbols(cfg['d']+' '+cfg['e']);r,ei=s.symbols('Rquad Einv');a,b=s.Rational(cfg['a']),s.Rational(cfg['b']);q=d*d-a*d*e*e+b*e**4;q0=r*r-a*r+b;disc=a*a-4*b
assert disc<0
rows=[(l,s.sympify(v)) for l,v in phase['residual_after']];jrow=dict(rows)['gauge_J_nonzero_wrapper'];ZJ=s.Symbol('ZJ');J=s.expand((jrow+1)/ZJ);assert not J.has(ZJ);assert all(me>0 for (md,me),cf in s.Poly(J,d,e).terms())
C=s.cancel(J.subs({d:r*e**2})/e**13);assert not C.has(e);C=s.rem(C,q0,r);Cinv=s.invert(C,q0,r);assert s.rem(C*Cinv-1,q0,r)==0
norm=s.resultant(q0,C,r);assert norm!=0
bez=s.cancel((C*Cinv-1)/q0);assert bez.is_polynomial(r);assert s.expand(C*Cinv-1-bez*q0)==0
oldactive=set().union(*(v.free_symbols for _,v in rows));unused=set(phase["free_after"])-set(map(str,oldactive));assert len(oldactive)==13 and len(unused)==33
trans={d:r*e**2,ZJ:Cinv*ei**13};oldtofield={}
for label,v in rows:
 x=s.rem(s.expand(v.xreplace(trans)),q0,r)
 if label=='gauge_early_J_constant':corner=x
 else:
  rem=s.reduced(x,[e*ei-1],ei,e,r)[1]
  assert s.rem(rem,q0,r)==0,(label,rem)
 oldtofield[label]=str(x)
# Every reverse map is polynomial in the original localized ring. E inverse
# is explicitly ZJ*(J/e); R is d*Einv^2, and r^2-a*r+b=q*Einv^4.
einv_reverse=s.expand(ZJ*(J/e));assert s.expand(e*einv_reverse-jrow)==1
assert s.expand((r*r-a*r+b).subs(r,d*ei**2)*e**4-q).subs(ei,1/e)==0
others=sorted(corner.free_symbols-{r,e},key=str)
# Place actual independent derivative coordinates first, which makes the
# single corner equation a sparse leading-variable relation.
others=sorted(others,key=lambda x:(0 if str(x) in ['A3c_97_1','B2c_64_1'] else 1,str(x)))
vars=others+[e,ei,s.Symbol('Zc')];c=s.Symbol('c');assert c in vars
poly=s.Poly(corner,*vars,r,domain=s.QQ);den=s.ilcm(*[v.q for v in poly.coeffs()]);ip=s.expand(corner*den)
def singular(x):return str(x).replace('**','^')
script='ring R=(0,Rquad),('+','.join(map(str,vars))+'),dp;\nminpoly='+singular(q0)+';\nideal I='+singular(ip)+',Einv*'+str(e)+'-1,Zc*c-1;\nideal SI=std(I);\nprint("BEGIN");print(dim(SI));print(reduce(1,SI));print(SI);print("END");\nideal Negative=c,Zc*c-1;ideal Positive=c-1,Zc*c-1;\nprint("CONTROLS");print(reduce(1,std(Negative)));print(reduce(1,std(Positive)));print("ENDCONTROLS");quit;\n'
pre.with_suffix('.sing').write_text(script)
record={'status':'SINGULAR_PENDING','branch':'delta52','inherited_t':89,'source_phase':str(p),'source_phase_sha256':sh(p),'source_row_hash':hashlib.sha256(dict(phase['residual_after'])['gauge_early_J_constant'].encode()).hexdigest(),'retained_q':str(q),'field_minimal_polynomial':str(q0),'discriminant':str(disc),'irreducible_over_Q_by_negative_discriminant':True,'J_polynomial':str(J),'C':str(C),'C_inverse_mod_q0':str(Cinv),'C_norm':str(norm),'transport_images':{str(v):str(x) for v,x in trans.items()},'e_inverse_reverse':str(einv_reverse),'all_old_equations_map_to_zero':True,'corner_image':str(corner),'new_ring_generator_order':list(map(str,vars)),'coefficient_field':'Q[Rquad]/(q0), an exact degree-two field; both C embeddings retained','e_preserved_as_Laurent_variable':True,'integer_denominator_scale':str(den),'C_unit_Bezout_quotient':str(bez),'C_unit_Bezout_identity_verified':True,'unused_full_chart_generators_remain_free':sorted(unused),'old_active_without_wrapper':len(oldactive),'full_free_count':len(phase['free_after']),'driver_sha256':sh(Path(__file__)),'singular_sha256':sh(pre.with_suffix('.sing')),'elapsed_seconds':time.monotonic()-start}
write(record);print('FIELD_TRANSPORT_PASS Singular start',time.monotonic()-start,flush=True)
try:
 z=subprocess.run(['Singular','-q',str(pre.with_suffix('.sing'))],capture_output=True,text=True,timeout=240,check=True)
except subprocess.TimeoutExpired:
 record.update(status='COMPUTE_BOUND_IN_NUMBERFIELD_CORNER_GROEBNER',elapsed_seconds=time.monotonic()-start);write(record);print(record['status'],flush=True);raise SystemExit
out=z.stdout+z.stderr;pre.with_suffix('.sing.out').write_text(out);assert not re.search(r'(^|\n)\s*\?',out) and 'error' not in out.lower(),out[:3000]
part=out.split('BEGIN\n')[1].split('\nEND')[0].splitlines();dim=int(part[0]);unit=part[1]=='0';assert unit==(dim==-1);assert out.split('CONTROLS\n',1)[1].split('\nENDCONTROLS')[0].splitlines()==['0','1']
record.update(status='PASS',unit_ideal=unit,transported_ring_dimension=dim,full_gauge_dimension=-1 if unit else len(phase['free_after'])-len(oldactive)+dim,dimension_identity=f'{len(unused)} unused full-chart coordinates + {dim}-dimensional transported active locus = {len(unused)+dim}',singular_output_sha256=sh(pre.with_suffix('.sing.out')),wrapper_controls=True,elapsed_seconds=time.monotonic()-start);write(record);print({k:record[k] for k in ['status','unit_ideal','full_gauge_dimension','elapsed_seconds']},flush=True)
