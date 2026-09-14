#!/usr/bin/env python3
"""Actual origin Jacobian row in the already certified monic quotient.

Only degree-corner source coefficients are needed. Full chart coordinates
and the complete original graph map remain declared in the phase record.
"""
import argparse,hashlib,importlib.util,json,re,subprocess,sys,time
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--branch',choices=['delta2','delta52'],required=True);ap.add_argument('--singular-seconds',type=int,default=600);args=ap.parse_args()
 N=Path(__file__).resolve().parent;branch=args.branch;prefix=N/f'print-audit-corner-quotient-{branch}'
 # Use the same immutable parents as the ordinary independent attempt.
 statepath=N/f'print-audit-corner-late-{branch}.source-state.json';phasepath=N/f'print-audit-corner-late-{branch}.source-phase.json'
 stateraw=statepath.read_bytes();phaseraw=phasepath.read_bytes();state=json.loads(stateraw);cert=json.loads(phaseraw)
 assert hashlib.sha256(phaseraw).hexdigest()==state['phase_certificates'][-1]['sha256']
 begin=time.monotonic();log=lambda message:print(message,flush=True)
 code=N/'run-code-source-full';sys.path.insert(0,str(code));sys.path.insert(0,str(N/'print-audit-flint-runtime'))
 import deep_gauge_accelerated as G;import engine as E
 def load(name):
  spec=importlib.util.spec_from_file_location(name,N/(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
 backend=load('print-audit-corner-pair-backend');safe=load('deep_safe_singular')
 encoded=cert['map_after'];domain=set(encoded);cache={}
 def apply(expression):
  expression=sp.sympify(expression);needed=expression.free_symbols&set(map(sp.Symbol,domain));sub={}
  for v in needed:
   if v not in cache:
    image=sp.sympify(encoded[str(v)]);assert not(set(map(str,image.free_symbols))&domain)
    cache[v]=image
   sub[v]=cache[v]
  return sp.expand(expression.xreplace(sub))
 residual=[(label,sp.sympify(row)) for label,row in cert['residual_after']]
 assert E.rows_hash(residual)==cert['residual_after_hash']
 free={sp.Symbol(v) for v in cert['free_after']};h,C2,C3,inner,meta=E.inner_state(branch);outer,outerfree,_=E.outer_state(-1)
 log(f'SOURCE_READY inherited_J={state["last_completed_t"]} seconds={time.monotonic()-begin:.3f}')
 sourcejets={}
 def corner_w(poly,D,name):
  c=apply(poly.get((D,0),0));v0=apply(poly.get((D-1,0),0));v1=apply(poly.get((D-1,1),0))
  sourcejets[name]={'normalization_degree':D,'constant':str(c),'physical_x_derivative':str(sp.expand(v0-v1)),'physical_y_derivative':str(v1)}
  return {pos:value for pos,value in {(D,0):c,(D-1,0):sp.expand(v0-v1),(D-1,1):v1}.items() if value!=0}
 hd=E.S['h3_degree'];hh=corner_w(h,hd,'h3');cc2=corner_w(C2,2*hd,'C2');cc3=corner_w(C3,3*hd,'C3')
 oo={name:corner_w(poly,E.S['outer_specs'][name][0],name) for name,poly in outer.items()}
 cfg=state['coefficient_quotient'];d,e=sp.Symbol(cfg['d']),sp.Symbol(cfg['e']);q=sp.sympify(cfg['polynomial'])
 band,bmeta=backend.jacobian_band(hh,cc2,cc3,oo,163,E.S,progress=log,quotient=cfg)
 assert set(band)<={0};actual=band.get(0,sp.Integer(0));Jc=apply(sp.Symbol('Jc'))
 Jnf=sp.Poly(Jc,d).rem(sp.Poly(q,d)).as_expr();assert sp.Poly(Jc-Jnf,d).rem(sp.Poly(q,d)).is_zero
 row=sp.expand(actual-Jnf);assert sp.Poly(row,d).degree()<=1
 log(f'CORNER_NF_READY terms={len(sp.Add.make_args(row))} symbols={len(row.free_symbols)} usedmap={len(cache)} seconds={time.monotonic()-begin:.3f}')
 label='gauge_early_J_constant';loc=sp.Symbol('rho' if branch=='delta2' else 'c')
 remain,new,pivots,zeros=E.qstar_reduce(residual+[(label,row)],free-{loc,d,e});new=E.resolve_map(new)
 # Compose only affected graph images; all other exact parent strings are
 # carried verbatim. This is the same simultaneous symbol homomorphism.
 after_encoded=dict(encoded)
 if new:
  targets=set(map(str,new))
  for name,rhs in list(after_encoded.items()):
   if targets&set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*',rhs)):
    after_encoded[name]=str(sp.expand(sp.sympify(rhs).xreplace(new)))
  after_encoded.update({str(v):str(rhs) for v,rhs in new.items()})
 freeafter=free-set(new)
 phase={'phase':'late_actual_corner_J_quotient','branch':branch,'field':'Q','localizer':str(loc),
  'free_before':sorted(map(str,free)),'map_before':encoded,'residual_before':cert['residual_after'],
  'raw_new_rows_before_reduction':[(label,str(row))],'raw_new_rows_hash':E.rows_hash([(label,row)]),
  'corner_row_is_normal_form_modulo_retained_q':cfg,
  'pivot_steps':[{'label':p.label,'variable':str(p.variable),'rational_leader':str(p.coefficient),'rhs_at_pivot':str(p.rhs),'selected_equation_at_pivot':str(sp.expand(p.coefficient*(p.variable-p.rhs)))} for p in pivots],
  'radical_steps':[],'map_after':after_encoded,'free_after':sorted(map(str,freeafter)),
  'residual_after':[(l,str(v)) for l,v in remain],'residual_after_hash':E.rows_hash(remain)}
 prefix.with_suffix('.phase.json').write_text(json.dumps(phase,indent=2,sort_keys=True)+'\n')
 record={'status':'SINGULAR_PENDING','branch':branch,'inherited_J_t':state['last_completed_t'],'inherited_dimension':state['records'][-1]['dimension'],
  'source_state':str(statepath),'source_state_sha256':hashlib.sha256(stateraw).hexdigest(),'source_phase':str(phasepath),'source_phase_sha256':hashlib.sha256(phaseraw).hexdigest(),
  'physical_corner_jets':sourcejets,'used_parent_map_images':{str(v):str(rhs) for v,rhs in cache.items()},
  'actual_J_constant_normal_form':str(actual),'same_mapped_Jc':str(Jc),'mapped_Jc_normal_form':str(Jnf),'combined_normal_form_row':str(row),
  'quotient':cfg,'backend_metadata':bmeta,'Qstar_pivots':len(pivots),'new_free_count':len(freeafter),'new_residual_count':len(remain),
  'source_code':str(code),'new_phase':str(prefix.with_suffix('.phase.json')),'new_phase_sha256':hashlib.sha256(prefix.with_suffix('.phase.json').read_bytes()).hexdigest(),
  'necessary_row_proof':'Source polynomials are replaced by their full physical degree<=1 Taylor polynomials, which preserve value and both first derivatives at origin. The normalized Jacobian coefficient at t163 is exactly the actual origin Jacobian. Native computation is modulo the already retained monic q; one combined row is emitted.',
  'scope':'Required actual global constant minus the same retained Jc, reordered on the full saved locus; no new localization or normalization.',
  'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-begin}
 out=prefix.with_suffix('.json');out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 variables=sorted(set().union(*(v.free_symbols for _,v in remain))|{loc},key=str);inv=sp.Symbol('Zrho' if branch=='delta2' else 'Zc');assert inv not in variables
 entries=[safe.encode_polynomial(v,variables) for _,v in remain]
 script='ring R=0,('+','.join(map(str,variables+[inv]))+'),dp;\nideal I='+','.join(v for v,_ in entries)+f',{inv}*{loc}-1;\nideal SI=std(I);\n'
 script+='print("BEGIN_CORNER");print(dim(SI));print(reduce(1,SI));print(SI);print("END_CORNER");\n'
 script+=f'ideal Empty={loc},{inv}*{loc}-1;ideal Point={loc}-1,{inv}*{loc}-1;\n'
 script+='print("BEGIN_CONTROLS");print(reduce(1,std(Empty)));print(reduce(1,std(Point)));print("END_CONTROLS");quit;\n'
 spath=prefix.with_suffix('.sing');spath.write_text(script);record['ring_generator_order']=list(map(str,variables+[inv]));record['row_denominator_scales']=[(l,s) for (l,_),(_,s) in zip(remain,entries)];record['singular_script_sha256']=hashlib.sha256(script.encode()).hexdigest();out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 log(f'SINGULAR_READY active={len(variables)} residual={len(remain)} newpivots={len(pivots)} seconds={time.monotonic()-begin:.3f}')
 try:run=subprocess.run(['Singular','-q',str(spath)],text=True,capture_output=True,check=True,timeout=args.singular_seconds)
 except subprocess.TimeoutExpired as exc:
  record.update(status='COMPUTE_BOUND_IN_CORNER_GROEBNER',elapsed_seconds=time.monotonic()-begin);out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');log(record['status']);return
 output=run.stdout+run.stderr;prefix.with_suffix('.sing.out').write_text(output);assert not re.search(r'(^|\n)\s*\?',output) and 'error' not in output.lower(),output[:1000]
 section=output.split('BEGIN_CORNER\n')[1].split('\nEND_CORNER')[0].splitlines();dimension=int(section[0]);unit=dimension==-1;assert section[1]==('0' if unit else '1')
 assert output.split('BEGIN_CONTROLS\n')[1].split('\nEND_CONTROLS')[0].splitlines()==['0','1']
 record.update(status='PASS',unit_ideal=unit,active_ring_dimension=dimension,full_gauge_dimension=-1 if unit else len(freeafter)-(len(variables)-dimension),
  singular_basis_sha256=hashlib.sha256(('\n'.join(section[2:])+'\n').encode()).hexdigest(),positive_negative_wrapper_controls=True,elapsed_seconds=time.monotonic()-begin)
 out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');log(json.dumps({k:record[k] for k in ('status','branch','inherited_J_t','inherited_dimension','unit_ideal','full_gauge_dimension','Qstar_pivots','elapsed_seconds')}))

if __name__=='__main__':main()
