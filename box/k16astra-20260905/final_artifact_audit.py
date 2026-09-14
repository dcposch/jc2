#!/usr/bin/env python3
"""Check accepted log markers, stopped-job exclusions, and lane custody."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re

p = Path(__file__).resolve().parent
checks = {}

def accept(name, markers, checkpoint_only=False):
    data = (p/name).read_text()
    assert not re.search(r'^\s*\?|FAIL|Traceback', data, re.M), name
    missing = [m for m in markers if m not in data]
    assert not missing, (name, missing)
    checks[name] = {'status': 'ACCEPTED_CHECKPOINTS' if checkpoint_only else 'PASS',
                    'required_markers': markers,
                    'sha256': hashlib.sha256((p/name).read_bytes()).hexdigest()}

for tag, dim, length, power in [('t2m',1,-1,1),('t2p',0,12,1),('t3',0,66,2),('t4',0,338,2)]:
    markers = [f'IPLUS_DIM {dim}', f'IPLUS_LENGTH {length}',
               f'TAU_POWER {power} ZERO 1', 'FULL_T0_NONZERO 1', 'IPLUS_COMPLETE']
    if power == 2:
        markers.append('TAU_POWER 1 ZERO 0')
    if tag != 't4':
        markers.append('CHECKS_COMPLETE')
    else:
        markers.extend(['TAIL_DIM 0', 'TAIL_LENGTH 572', 'TAIL_TAU_POWER 2 ZERO 0'])
    accept(tag+'_checks.log', markers, checkpoint_only=tag=='t4')
    accept(tag+'_abel_generate.log', ['ABEL_ROW_IDENTITY_PASS','LOCAL_IDENTITIES_PASS','ROWS_COMPLETE'])

for tag in ['t3','t4']:
    accept(tag+'_coordinate.log', ['COORDINATE_IMAGES_PASS','ROWS_COMPLETE'])
    accept(tag+'_local_probe.log', ['ROOT_DERIVATIVE_PROPORTIONAL 0','ROOT_IN_GRADIENT 0','LOCAL_PROBE_COMPLETE'])
    accept('audit_baseprobe_'+tag+'_singular.log', ['AUDIT_BASE_DONE'])
    accept('audit_minors_'+tag+'.log', ['AUDIT_MINORS_DONE'])

accept('audit_minors_t3.log', ['MINORS dim=0 vdim=85','STATS MINORS length=85 top=18','AUDIT_MINORS_DONE'])
accept('audit_minors_t4.log', ['MINORS dim=0 vdim=503','STATS MINORS length=503 top=26','AUDIT_MINORS_DONE'])
accept('audit_baseprobe_t4_singular.log', ['SLICE dim=0 vdim=143 tau=0','AUDIT_BASE_DONE'])
accept('structural_abel_general.log', ['ALL_B3_LAURENT_ABEL_PASS','POLYNOMIAL_RECONSTRUCTION_PASS','ALL_NORMALIZED_LEADING_COEFFICIENTS_PASS'])
accept('structural_boundary_jets.log', ['UNIVERSAL_BOUNDARY_JETS_PASS'])
accept('structural_abel.log', ['PASS'])
accept('t3_sympy.log', ['SYMPY_CROSSCHECK_COMPLETE'])
accept('exact_hilbert.log', ['t3 length 66 top_degree 14','t4 length 338 top_degree 21','HILBERT_COMPLETE'])
accept('belyi_identity.log', ['BARE_BELYI_AUDIT_DONE; NO_UNIFORM_ATOM_PROMOTION'])
accept('moment_residues.log', ['MOMENT_RESIDUES_DONE'])
accept('t8p_generate.log', ['PIVOT 17 PASS','LOCAL_IDENTITIES_PASS','ROWS_COMPLETE'])
assert (p/'t3_fast_rows.sing').read_bytes() == (p/'t3_local_rows.sing').read_bytes()

outcomes = json.loads((p/'run_outcomes.json').read_text())
for tag in ['t8p_plus','t8p_tailhint']:
    data = (p/(tag+'.log')).read_text()
    assert 'CONE_COMPLETE' not in data and 'GB_DONE' not in data
    assert outcomes[tag]['returncode'] == 124 and outcomes[tag]['promotion'] == 'NONE'

active = []
for proc in Path('/proc').iterdir():
    if not proc.name.isdigit() or int(proc.name) == os.getpid():
        continue
    try:
        args = (proc/'cmdline').read_bytes().split(b'\0')
        program = Path(os.fsdecode(args[0])).name
        if program not in {'Singular','python3','python','timeout'}:
            continue
        if any(b'k16astra-20260905/' in a for a in args):
            active.append({'pid':int(proc.name),'program':program})
    except (OSError, IndexError):
        pass
assert not active, active

result = {'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'accepted_logs':checks,
          'active_lane_CAS_processes':active,
          't3_fast_rows_equal_local_rows':True,
          'excluded_results':['t8 dimension or theorem promotion',
              'termination-time tau cubed output in t4_checks.log',
              'all development-error and deliberately stopped unoptimized jobs'],
          'all_t_theorem_status':'OPEN'}
(p/'artifact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
files = sorted(f for f in p.rglob('*') if f.is_file()
               and f.name != 'artifacts.sha256' and '__pycache__' not in f.parts)
manifest = ''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+str(f)+'\n' for f in files)
(p/'artifacts.sha256').write_text(manifest)
print('ACCEPTED_LOGS',len(checks))
print('MANIFEST_FILES',len(files))
print('ACTIVE_LANE_CAS_PROCESSES',len(active))
print('ARTIFACT_AUDIT_PASS')
