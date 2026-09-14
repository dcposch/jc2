#!/usr/bin/env python3
"""Independently verify a physical-origin row on a hash-bound verified prefix."""
from pathlib import Path
import argparse,hashlib,json,sys,time
import sympy as sp
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import minor_final_verify as M
OWN_SHA256=M.digest(__file__)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prefix',type=Path,required=True);ap.add_argument('--prefix-input',type=Path,required=True);ap.add_argument('--trusted-prefix-code',type=Path,required=True);ap.add_argument('--phase',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--driver',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();tick=time.monotonic()
 receipt=json.loads(a.prefix.read_text());state=json.loads(a.prefix_input.read_text());cert=json.loads(a.phase.read_text())
 assert receipt['status']=='PASS' and receipt['merged_result_sha256']==M.digest(a.prefix_input)
 assert receipt['verifier_sha256']==M.digest(a.trusted_prefix_code/'minor_merged_verify.py')
 assert receipt['verifier_core_sha256_at_start']==M.digest(a.trusted_prefix_code/'minor_final_verify.py')
 assert cert['branch']==state['branch']==receipt['branch'] and state['field']=='Q'
 for name,value in state['code_sha256'].items():assert M.digest(a.source/name)==value
 E=M.load_code(a.source,gauge=True);v=M.Verifier(E,state['branch'])
 v.extra_generators={sp.Symbol(name) for name in state['initial_complete_free_ring'] if name.startswith('Zface_')};v.locals.update({str(x):x for x in v.extra_generators})
 assert sorted(map(str,v.basefree))==state['weak_complete_free_ring']
 assert v.equal_map(v.mapping(state['cumulative_map']),v.mapping(cert['map_before']))
 assert v.rows(state['residual_rows'])==v.rows(cert['residual_before']) and state['free_after']==cert['free_before']
 assert E.rows_hash(v.rows(cert['residual_before']))==state['residual_hash']
 cfg=state.get('coefficient_quotient')
 if cfg:
  q=v.expr(cfg['polynomial']);d=v.locals[cfg['d']];e=v.locals[cfg['e']]
  assert receipt['independent_quotient_audits'][-1]['monic_relation']==str(q)
  assert any(row==q for _,row in v.rows(cert['residual_before']))
  assert sp.Poly(q,d).LC()==1 and sp.Poly(q,d).degree()==2
  v.quotient=q;v.quotient_generator=d;v.quotient_parameters={d,e}
 before=v.mapping(cert['map_before']);expected=sp.expand(v.independent_origin_constant(before)-sp.Symbol('Jc').xreplace(before))
 raw=v.rows(cert['raw_new_rows_before_reduction'])
 assert len(raw)==1 and raw[0][0]=='gauge_early_J_constant'
 delta=sp.expand(expected-raw[0][1]);factor=None
 if cfg:
  factor,remainder=sp.div(delta,q,d);assert remainder==0 and sp.expand(delta-factor*q)==0
 else:assert delta==0
 replay=v.replay_phase(cert)
 singular=M.singular_replay(v.rows(cert['residual_after']),v.branch,len(cert['free_after']),a.out.with_suffix('.sing'))
 result={'status':'PASS','branch':v.branch,'type':'INDEPENDENT PHYSICAL-ORIGIN JACOBIAN ROW ON VERIFIED SOURCE CHART',
 'prefix_receipt_sha256':M.digest(a.prefix),'prefix_input_sha256':M.digest(a.prefix_input),'phase_sha256':M.digest(a.phase),
 'driver_sha256':M.digest(a.driver),'source_code_sha256':state['code_sha256'],
 'exact_map_free_residual_boundary_checked':True,'independent_full_source_origin_J_minus_same_Jc_sha256':hashlib.sha256(sp.srepr(expected).encode()).hexdigest(),
 'raw_minus_regenerated_is_multiple_of_proved_monic_row':bool(cfg),'quotient_multiplier_sha256':hashlib.sha256(sp.srepr(factor).encode()).hexdigest() if cfg else None,
 'replay':replay,'Singular':singular,'verifier_sha256_at_start':OWN_SHA256,'core_sha256_at_import':M.VERIFIER_SHA256_AT_IMPORT,
 'gauge_coverage':'minor_gauge-final-audit.md','elapsed_seconds':time.monotonic()-tick}
 a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','dimension':singular['full_dimension'],'unit':singular['unit_ideal']}))

if __name__=='__main__':main()
