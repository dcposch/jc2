#!/usr/bin/env python3
"""Actual final Jacobian coefficient on an immutable late quotient locus."""
import argparse,hashlib,importlib.util,json,re,subprocess,sys,time
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--branch',choices=['delta2','delta52'],required=True);ap.add_argument('--singular-seconds',type=int,default=600);args=ap.parse_args()
 N=Path(__file__).resolve().parent;branch=args.branch;prefix=N/f'print-audit-corner-late-{branch}'
 statepath=N/'results-fullJ-quotient'/f'fullJ-quotient-{branch}.json';stateraw=statepath.read_bytes();state=json.loads(stateraw)
 phaseentry=state['phase_certificates'][-1];phasepath=statepath.parent/Path(phaseentry['path']).name;phaseraw=phasepath.read_bytes()
 assert hashlib.sha256(phaseraw).hexdigest()==phaseentry['sha256']
 cert=json.loads(phaseraw);assert state['cumulative_map']==cert['map_after']
 prefix.with_suffix('.source-state.json').write_bytes(stateraw);prefix.with_suffix('.source-phase.json').write_bytes(phaseraw)
 begin=time.monotonic();log=lambda message:print(message,flush=True)
 code=N/'run-code-source-full';sys.path.insert(0,str(code));import deep_gauge_accelerated as G;import engine as E
 spec=importlib.util.spec_from_file_location('safe_export',N/'deep_safe_singular.py');safe=importlib.util.module_from_spec(spec);spec.loader.exec_module(safe)
 mapping={sp.Symbol(v):sp.sympify(rhs) for v,rhs in cert['map_after'].items()}
 assert all(not(rhs.free_symbols&set(mapping)) for rhs in mapping.values())
 free=set(mapping)|{sp.Symbol(v) for v in cert['free_after']}
 residual=[(label,sp.sympify(row)) for label,row in cert['residual_after']]
 assert E.rows_hash(residual)==cert['residual_after_hash']
 h,C2,C3,inner,meta=E.inner_state(branch);outer,outerfree,_=E.outer_state(-1)
 log(f'SOURCE_READY branch={branch} inherited_J={state["last_completed_t"]} seconds={time.monotonic()-begin:.3f}')
 # Exact physical Taylor map from z=ty-1 normalization.
 x,y=sp.symbols('physical_x physical_y');sourcejets={}
 def taylor(poly,D,name):
  slots=[(D,0),(D-1,0),(D-1,1)]
  values={slot:E.substitute_map(sp.sympify(poly.get(slot,0)),mapping) for slot in slots}
  sourcejets[name]={'normalization_degree':D,'slot_images':{str(slot):str(value) for slot,value in values.items()}}
  constant=values[D,0];cx=values[D-1,0]-values[D-1,1];cy=values[D-1,1]
  return constant+cx*x+cy*y
 hd=E.S['h3_degree'];ht=taylor(h,hd,'h3');ct2=taylor(C2,2*hd,'C2');ct3=taylor(C3,3*hd,'C3')
 H=ht**3+ct2*ht+ct3
 Ot={name:taylor(poly,E.S['outer_specs'][name][0],name) for name,poly in outer.items()}
 F=H**3+Ot['A2']*H+Ot['A3'];GG=H**2+Ot['B1']*H+Ot['B2']
 at={x:0,y:0};Fx=sp.diff(F,x).xreplace(at);Fy=sp.diff(F,y).xreplace(at);Gx=sp.diff(GG,x).xreplace(at);Gy=sp.diff(GG,y).xreplace(at)
 actual=sp.expand(Fx*Gy-Fy*Gx);Jc=E.substitute_map(sp.Symbol('Jc'),mapping)
 row=sp.expand(actual-Jc)
 log(f'CORNER_READY terms={len(sp.Add.make_args(row))} symbols={len(row.free_symbols)} seconds={time.monotonic()-begin:.3f}')
 label='gauge_early_J_constant';pending=residual+[(label,row)]
 protected={sp.Symbol(state['coefficient_quotient']['d']),sp.Symbol(state['coefficient_quotient']['e'])}
 loc=sp.Symbol('rho' if branch=='delta2' else 'c')
 remain,new,pivots,zeros=E.qstar_reduce(pending,free-set(mapping)-{loc}-protected)
 new=E.resolve_map(new);after=dict(mapping);after.update(new);after=E.resolve_map(after)
 phase={'phase':'late_actual_corner_J','branch':branch,'field':'Q','localizer':str(loc),
  'free_before':sorted(map(str,free-set(mapping))),'map_before':E.encode_map(mapping),'residual_before':[(l,str(v)) for l,v in residual],
  'raw_new_rows_before_reduction':[(label,str(row))],'raw_new_rows_hash':E.rows_hash([(label,row)]),
  'pivot_steps':[{'label':p.label,'variable':str(p.variable),'rational_leader':str(p.coefficient),'rhs_at_pivot':str(p.rhs),'selected_equation_at_pivot':str(sp.expand(p.coefficient*(p.variable-p.rhs)))} for p in pivots],
  'radical_steps':[],'map_after':E.encode_map(after),'free_after':sorted(map(str,free-set(after))),
  'residual_after':[(l,str(v)) for l,v in remain],'residual_after_hash':E.rows_hash(remain)}
 prefix.with_suffix('.phase.json').write_text(json.dumps(phase,indent=2,sort_keys=True)+'\n')
 record={'status':'SINGULAR_PENDING','branch':branch,'inherited_J_t':state['last_completed_t'],
  'inherited_dimension':state['records'][-1]['dimension'],'source_state':str(prefix.with_suffix('.source-state.json')),
  'source_state_sha256':hashlib.sha256(stateraw).hexdigest(),'source_phase':str(prefix.with_suffix('.source-phase.json')),
  'source_phase_sha256':hashlib.sha256(phaseraw).hexdigest(),'source_code':str(code),
  'code_hashes':{name:hashlib.sha256((code/name).read_bytes()).hexdigest() for name in ['engine.py','source_data.py','minor_maps.py','deep_gauge_accelerated.py']},
  'physical_degree_corner_jets':sourcejets,'actual_constant_J':str(actual),'same_mapped_Jc':str(Jc),'actual_raw_row':str(row),
  'raw_ordinary_source_row_not_quotient_normalized':True,'quotient_retained':state['coefficient_quotient'],
  'new_phase':str(prefix.with_suffix('.phase.json')),'new_phase_sha256':hashlib.sha256(prefix.with_suffix('.phase.json').read_bytes()).hexdigest(),
  'Qstar_pivots':len(pivots),'new_free_count':len(free-set(after)),'new_residual_count':len(remain),
  'scope':'Necessary final constant row reordered on the complete recorded quotient locus; original source polynomial and same nonzero Jc, no new normalization.',
  'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-begin}
 out=prefix.with_suffix('.json');out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 variables=sorted(set().union(*(v.free_symbols for _,v in remain))|{loc},key=str);inv=sp.Symbol('Zrho' if branch=='delta2' else 'Zc');assert inv not in variables
 entries=[safe.encode_polynomial(v,variables) for _,v in remain]
 script='ring R=0,('+','.join(map(str,variables+[inv]))+'),dp;\nideal I='+','.join(v for v,_ in entries)+f',{inv}*{loc}-1;\nideal SI=std(I);\n'
 script+='print("BEGIN_CORNER");print(dim(SI));print(reduce(1,SI));print(SI);print("END_CORNER");\n'
 script+=f'ideal Empty={loc},{inv}*{loc}-1;ideal Point={loc}-1,{inv}*{loc}-1;\n'
 script+='print("BEGIN_CONTROLS");print(reduce(1,std(Empty)));print(reduce(1,std(Point)));print("END_CONTROLS");quit;\n'
 spath=prefix.with_suffix('.sing');spath.write_text(script)
 record['ring_generator_order']=list(map(str,variables+[inv]));record['row_denominator_scales']=[(label,scale) for (label,_),(_,scale) in zip(remain,entries)]
 record['singular_script_sha256']=hashlib.sha256(script.encode()).hexdigest();out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 log(f'SINGULAR_READY active={len(variables)} residual={len(remain)} newpivots={len(pivots)} seconds={time.monotonic()-begin:.3f}')
 try:run=subprocess.run(['Singular','-q',str(spath)],text=True,capture_output=True,check=True,timeout=args.singular_seconds)
 except subprocess.TimeoutExpired as exc:
  record.update(status='COMPUTE_BOUND_IN_CORNER_GROEBNER',elapsed_seconds=time.monotonic()-begin)
  prefix.with_suffix('.sing.out').write_text((exc.stdout or b'').decode() if isinstance(exc.stdout,bytes) else exc.stdout or '')
  out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n');log(record['status']);return
 output=run.stdout+run.stderr;prefix.with_suffix('.sing.out').write_text(output)
 assert not re.search(r'(^|\n)\s*\?',output) and 'error' not in output.lower(),output[:2000]
 section=output.split('BEGIN_CORNER\n')[1].split('\nEND_CORNER')[0].splitlines();dimension=int(section[0]);unit=dimension==-1
 assert section[1]==('0' if unit else '1')
 assert output.split('BEGIN_CONTROLS\n')[1].split('\nEND_CONTROLS')[0].splitlines()==['0','1']
 codim=len(variables)-dimension
 record.update(status='PASS',unit_ideal=unit,active_ring_dimension=dimension,full_gauge_dimension=-1 if unit else len(free-set(after))-codim,
  singular_basis_sha256=hashlib.sha256(('\n'.join(section[2:])+'\n').encode()).hexdigest(),positive_negative_wrapper_controls=True,elapsed_seconds=time.monotonic()-begin)
 out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 log(json.dumps({k:record[k] for k in ('status','branch','inherited_J_t','inherited_dimension','unit_ideal','full_gauge_dimension','Qstar_pivots','elapsed_seconds')}))

if __name__=='__main__':main()
