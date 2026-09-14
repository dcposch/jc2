#!/usr/bin/env python3
"""Verify an exact saved direct-F/G oracle band and its full QQ* phase."""
from pathlib import Path
import argparse,hashlib,json,re,sys,time
import sympy as sp
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import minor_final_verify as M
OWN_SHA256=M.digest(__file__)

def main():
 ap=argparse.ArgumentParser()
 for name in ['prefix','prefix-input','trusted-prefix-code','oracle','oracle-code','oracle-driver','phase','source','out']:ap.add_argument('--'+name,type=Path,required=True)
 a=ap.parse_args();tick=time.monotonic();receipt=json.loads(a.prefix.read_text());state=json.loads(a.prefix_input.read_text());oracle=json.loads(a.oracle.read_text());cert=json.loads(a.phase.read_text())
 assert receipt['status']=='PASS' and receipt['merged_result_sha256']==M.digest(a.prefix_input)
 assert receipt['verifier_sha256']==M.digest(a.trusted_prefix_code/'minor_merged_verify.py') and receipt['verifier_core_sha256_at_start']==M.digest(a.trusted_prefix_code/'minor_final_verify.py')
 assert oracle['status']=='REGENERATED' and oracle['input_sha256']==M.digest(a.prefix_input)
 assert oracle['metadata']['helper_sha256_at_import']==M.digest(a.oracle_code/'minor_flint_quotient_direct.py')
 assert oracle['core_sha256_at_import']==M.digest(a.oracle_code/'minor_final_verify.py')
 assert oracle['driver_sha256_at_start']==M.digest(a.oracle_driver)
 assert state['branch']==oracle['branch']==cert['branch']==receipt['branch']
 for name,value in state['code_sha256'].items():assert M.digest(a.source/name)==value
 E=M.load_code(a.source,gauge=True);v=M.Verifier(E,state['branch']);v.native_map_verification=True
 v.extra_generators={sp.Symbol(name) for name in state['initial_complete_free_ring'] if name.startswith('Zface_')};v.locals.update({str(x):x for x in v.extra_generators})
 assert state['weak_complete_free_ring']==sorted(map(str,v.basefree))
 before=v.mapping(cert['map_before']);assert v.equal_map(v.mapping(oracle['map_before']),before) and v.equal_map(v.mapping(state['cumulative_map']),before)
 assert state['free_after']==cert['free_before'] and v.rows(state['residual_rows'])==v.rows(cert['residual_before'])
 cfg=state['coefficient_quotient'];q=v.expr(cfg['polynomial']);d=v.locals[cfg['d']];e=v.locals[cfg['e']]
 assert receipt['independent_quotient_audits'][-1]['monic_relation']==str(q)
 assert sp.expand(v.expr(oracle['metadata']['relation'])-q)==0 and oracle['metadata']['combined_A_plus_B_delta_rows'] and not oracle['metadata']['conjugate_selected']
 v.quotient=q;v.quotient_generator=d;v.quotient_parameters={d,e}
 tp=oracle['tp'];degree=v.S['n']+v.S['m']-2-tp;assert cert['phase']==f'Jacobian_t{tp}' and tp==state['last_completed_t']+1
 expected={f'resumed_J_t{tp}_d{degree}_k{k}':v.expr(value) for k,value in oracle['rows'].items()};raw=dict(v.rows(cert['raw_new_rows_before_reduction']))
 assert set(expected)==set(raw) and all(sp.expand(expected[key]-raw[key])==0 for key in expected)
 assert all(0<=int(k)<=degree for k in oracle['rows'])
 assert all(sp.Poly(value,d).degree()<=1 for value in expected.values())
 replay=v.replay_phase(cert);singular=M.singular_replay(v.rows(cert['residual_after']),v.branch,len(cert['free_after']),a.out.with_suffix('.sing'))
 result={'status':'PASS','branch':v.branch,'type':'INDEPENDENT DIRECT FULL-FG QUOTIENT ORACLE AND COMPLETE PHASE VERIFICATION','J_t':tp,
 'prefix_receipt_sha256':M.digest(a.prefix),'prefix_input_sha256':M.digest(a.prefix_input),'phase_sha256':M.digest(a.phase),'oracle_sha256':M.digest(a.oracle),
 'direct_oracle_helper_sha256_at_import':oracle['metadata']['helper_sha256_at_import'],'direct_oracle_core_sha256_at_import':oracle['core_sha256_at_import'],
 'unchanged_oracle_launcher_content_sha256':M.digest(a.oracle_driver),'exact_source_map_and_free_ring_boundary':True,
 'every_saved_row_matches_executed_independent_direct_oracle':True,'all_omitted_coefficients_are_zero_classes':True,'nonzero_raw_coefficients':len(raw),
 'replay':replay,'Singular':singular,'verifier_sha256_at_start':OWN_SHA256,'core_sha256_at_import':M.VERIFIER_SHA256_AT_IMPORT,'elapsed_seconds':time.monotonic()-tick}
 a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','J_t':tp,'dimension':singular['full_dimension'],'unit':singular['unit_ideal']}))

if __name__=='__main__':main()
