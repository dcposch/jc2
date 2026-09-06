#!/usr/bin/env python3
"""Seal the lane report and write compact, explicitly scoped results."""
from pathlib import Path
import datetime, hashlib, json, re

root=Path(__file__).resolve().parents[2]
lane=Path(__file__).resolve().parent
report=root/'xmodel/k16-utac-astra-20260906.md'
marker=b'<!-- BODY-END -->\n'
raw=report.read_bytes()
if marker in raw:
    body=raw.split(marker,1)[0]+marker
else:
    body=raw.rstrip()+b'\n\n'+marker
assert body.count(marker)==1
assert b'PENDING' not in body
body_hash=hashlib.sha256(body).hexdigest()
seal=(f'\n**Seal.** Body: {len(body)} bytes, through the standalone end marker including its newline. '
      f'Body SHA-256: `{body_hash}`. Frozen basis: '
      '`e584173b8a751ddd6b7fbc5627958ac64cc3d4e7`.\n').encode()
report.write_bytes(body+seal)
assert 15000 <= report.stat().st_size <= 30000

inputs=[]
for line in (lane/'manifest.sha256').read_text().splitlines():
    digest,path=line.split(None,1)
    f=Path(path.strip())
    actual=hashlib.sha256(f.read_bytes()).hexdigest()
    assert digest==actual, str(f)
    inputs.append({'basename':f.name,'sha256':digest,'verified':True})

def replay(name):
    text=(lane/name).read_text()
    dimensions=re.search(r'GB_SIZE=(\d+) DIM=(\d+)',text)
    powers={k:int(v) for k,v in re.findall(r'MIN_EXP (\w+)=(\d+)',text)}
    return {'field_only':'finite characteristic',
            'GB_size':int(dimensions[1]), 'dimension':int(dimensions[2]),
            'minimal_exponents_replayed':powers,
            'diagnostic_error_in_original_log':'? `poly`' in text,
            'full_script_completed':'DONE_CLOSING_CHECK' in text,
            'raw_output':name}

results={
 'schema':1,'lane':'k16-utac-astra-20260906',
 'basis':'e584173b8a751ddd6b7fbc5627958ac64cc3d4e7',
 'sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'verdict':{'uniform_U_eta':'OPEN','counterexample_found':False,
            'uniform_R':'NOT_PROVED','whole_ray_T':'NOT_PROMOTED'},
 'custody':{'mechanism':'receipt awk manifest and sha256sum -c, before reading inputs',
            'inputs':inputs,'final_recheck':'6/6 OK'},
 'proved_here':{
   'exact_radical':{'N':[3,4,5],'field':'Q',
    'ideal':'(u,l2,l4,...,lN,l3-2*w2,B*w2)',
    'coordinate_ring':'Q[B,w2]/(B*w2)',
    'dimension':1,'components':[
      {'L':'-1','P':'-1/4-B*x','eta':'0','B':'free','w2':'0'},
      {'L':'-1+a*x^3','P':'-L^2/4','eta':'0','B':'0','w2':'a/2'}],
    'normalization':'A1 disjoint union A1',
    'component_genera':[0,0],'ordinary_projective_arithmetic_genus':0,
    'B_in_radical':False,'w2_in_radical':False,
    'input_scope':'fresh UF coefficient reconstruction; no ray certificate'},
   'universal_inclusion':{'N_min':3,'claim':'two stated lines contained in V(I_close,N)'},
   'uniform_exponent_lower_bound':{'N_min':4,'bound':'e >= 2N',
     'targets':['eta','u','B*eta'],'also_after_localizing_B':True,
     'proof':'Artin solution over Q[z]/(z^(2N)), B=1,eta=z,L=-1',
     'finite_identity_checks':[4,5,6],
     'not_a_reduced_counterexample':True},
   'square_root_slice':{'map':'u=4z;B=w2=l2=...=lN=0',
     'P':'-1/4*sqrt(1-8z*x^2)','image_ideal':'(z^(N+1))'},
   'saturation_controls':{'exact_N':[4,5],
     'inverse_equation_unit':['u','eta'],
     'inverse_equation_nonunit':['u+1','B','w2'],
     'method':'exact radical theorem plus explicit points in original closing variety'}},
 'modular_only':{
   'radical_N6':{'prime':1000003,'ideal':'(u,l2,l4,l5,l6,l3-2*w2,B*w2)',
       'all_lower_actual_degrees_checked':True,'split_fields_handled_factorwise':True},
   'N4_p31991':replay('check_closing_N4_p31991_wp.out'),
   'N4_p1000003':replay('check_closing_N4_p1000003_wp.out'),
   'N5_p1000003':replay('check_closing_N5_p1000003_wp.out'),
   'N5_Beta_power_upper_bound':27,
   'N5_Beta_minimum':'not determined; stopped optional search after eta minimum',
   'N4_first_row_prefix_dimensions':[5,4,3],
   'parity_exploration':{'actual_degrees':[8,10,12],'prime':1000003,
       'quotient_lengths':[206,1005,4914],'not_full_closing_classification':True}},
 'limits':{
   'exact_N6':'TIMEOUT at 600 seconds; no char0 exclusion claimed',
   'parity_N16':'TIMEOUT at 120 seconds',
   'char0_min_eta_exponents_19_27':'not established; these minima are modular',
   'original_N5_diagnostic':'Phi4 print precedence error; construction unaffected; repaired coefficient replay passes',
   'uniform_obstruction':'eta_m in sqrt(K_m:b^infinity) for every unbounded actual degree m',
   'boundary_bridge':'also need B*eta in sqrt(J_t+(b)) uniformly for the full R chain'},
 'report':{'path':str(report.relative_to(root)),'body_bytes':len(body),
     'body_sha256':body_hash,'sealed_bytes':report.stat().st_size,
     'sealed_sha256':hashlib.sha256(report.read_bytes()).hexdigest()},
 'discipline':{'no_ledger_edits':True,'no_jc2_lean':True,'no_ideation_input':True,
     'no_fleet':True,'no_lane_process_left_running':True}}
(lane/'results.json').write_text(json.dumps(results,indent=2)+'\n')

json_bytes=sum(f.stat().st_size for f in lane.glob('*.json'))
assert report.stat().st_size+json_bytes <= 2_000_000
entries=[]
for f in sorted(lane.iterdir()):
    if f.is_file() and f.name!='artifacts.sha256':
        entries.append(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+str(f.relative_to(root)))
entries.append(hashlib.sha256(report.read_bytes()).hexdigest()+'  '+str(report.relative_to(root)))
(lane/'artifacts.sha256').write_text('\n'.join(entries)+'\n')
print(json.dumps({'report_bytes':report.stat().st_size,'body_bytes':len(body),
    'body_sha256':body_hash,'report_plus_all_JSON_bytes':report.stat().st_size+json_bytes,
    'lane_bytes':sum(f.stat().st_size for f in lane.iterdir() if f.is_file()),
    'input_hashes':'6/6 OK'},indent=2))
