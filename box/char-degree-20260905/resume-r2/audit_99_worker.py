#!/usr/bin/env python3
"""Read-only remote (99,66) audit; print compact evidence, never write worker data."""
import datetime, hashlib, json, math, re, subprocess, time
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
HERE = ROOT / 'box/char-degree-20260905'
BASE = HERE / 'g9966'
def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        while b := f.read(1024*1024): h.update(b)
    return h.hexdigest()
def digest(b): return hashlib.sha256(b).hexdigest()
def read(path): return json.loads(Path(path).read_text())
def cas(script):
    start = time.monotonic()
    p = subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,timeout=30)
    out=p.stdout+p.stderr
    return {'returncode':p.returncode,'wall_seconds':round(time.monotonic()-start,4),
      'output':out,'output_sha256':digest(out.encode()),'script_sha256':digest(script.encode()),
      'parser_error':bool(re.search(r'(^|\n)\s*\?',out) or 'error occurred' in out)}

verification=read(BASE/'circuit-inputs/verification.json')
verified={(d['branch'],d['stage']):d for d in verification['records']}
proofs=read(BASE/'circuit-inputs/proof-custody.json')
proof_check=[]
for p in proofs['proofs']:
    actual=sha(p['retained_snapshot'])
    assert actual==p['sha256']
    proof_check.append({'path':p['retained_snapshot'],'sha256':actual})

records=[]
resource_path=HERE/'resume-r2/resource-observations.json'
resource_data=read(resource_path) if resource_path.exists() else {'records':[]}
for stage in range(9):
  for branch in ('delta2','delta52'):
    inp_path=BASE/'circuit-inputs'/f'{branch}_stage{stage}.input.json'
    inp=read(inp_path); vr=verified[(branch,stage)]
    assert sha(inp_path)==vr['input_sha256']
    cp=ROOT/inp['source_coordinate_input']['path']; coordinates=read(cp)
    assert sha(cp)==inp['source_coordinate_input']['sha256']==vr['coordinate_sha256']
    gp=ROOT/coordinates['stronger_characteristic_front']['parent_input']; gauge=read(gp)
    op=ROOT/gauge['source_gauge']['parent_input']
    assert sha(gp)==coordinates['stronger_characteristic_front']['parent_input_sha256']
    assert sha(op)==gauge['source_gauge']['parent_input_sha256']
    outdir=BASE/'circuit-runs'/f'{branch}_stage{stage}'
    scriptpath=outdir/'augmented.sing';metapath=outdir/'augmented.circuit.json'
    ep=outdir/'execution.json';logpath=outdir/'augmented.circuit.out'
    item={'branch':branch,'stage':stage,'input':str(inp_path),'input_sha256':sha(inp_path),
      'coordinate_sha256':sha(cp),'gauge_sha256':sha(gp),'original_sha256':sha(op),
      'source_map_verification_hash_match':True,'source_map_verification_record':vr,
      'rss_kib':None,'rss_note':'Peak RSS not measured by original schedule; unavailable for a process that ended before adoption.',
      'scope':'Full necessary chart modulo audited jet0=0 translation slice and radical front consequences; no source coordinate pin beyond this gauge.'}
    if not metapath.exists():
      item['status']='NOT_YET_EMITTED';records.append(item);continue
    meta=read(metapath); ex=read(ep) if ep.exists() else {}
    script=scriptpath.read_text();ring=script.splitlines()[0]
    assert ring=='ring R=0,('+','.join(meta['ring_generator_order'])+'),dp;'
    assert meta['script_sha256']==sha(scriptpath)
    assert meta['input_sha256']==sha(inp_path)
    assert len(meta['ring_generator_order'])==len(set(meta['ring_generator_order']))
    assert meta['ring_generator_order'][:len(inp['names'])]==inp['names']
    assert {'target_'+x for x in 'abcde'}|{'leader55','Z55'} <= set(inp['names'])
    assert 'jet0' not in inp['names']
    body=script.split('ideal I=\n',1)[1].split(';\nprint("ALL_ROWS_PARSED")',1)[0]
    rows=body.split(',\n');counts=meta['counts'];assert len(rows)==sum(counts.values())
    sep='rho' if branch=='delta2' else 'c';zinv='Zrho' if branch=='delta2' else 'Zc'
    assert rows[-2:]==['(Z55*leader55-1)',f'({zinv}*{sep}-1)']
    leading=[(i,row) for i,row in enumerate(rows) if 'leader55' in row]
    assert len(leading)==17 and leading[-1][0]==len(rows)-2
    values=[]
    for i,row in leading[:-1]:
      m=re.search(r'\+\(-1\)\*\(\(([0-9]+)\)\*leader55\)\)$',row)
      assert m and row.count('leader55')==1
      values.append(int(m[1]))
    assert values==[math.comb(15,j) for j in range(16)]
    assert [i for i,_ in leading[:-1]]==list(range(len(rows)-18,len(rows)-2))
    assert inp['face_expr']=='zz^16*(1+zz)^6'
    # The actual source zero band is rational and has at most twelve entries.
    import sympy as s
    zz=s.Symbol('zz')
    bands={name:s.expand(sum(s.sympify(v)*zz**q for r,q,v in tab if r==0)) for name,tab in coordinates['maps'].items()}
    H0=s.expand(bands['h3']**3+bands['C2']*bands['h3']+bands['C3'])
    assert s.expand(H0-zz**24*(1+zz)**9)==0
    assert s.expand(H0*s.sympify(inp['face_expr'].replace('^','**'))-zz**40*(1+zz)**15)==0
    ctrl=cas(ring+'\n'+f'ideal n=leader55,Z55*leader55-1;ideal p=leader55-1,Z55*leader55-1;ideal sn={sep},{zinv}*{sep}-1;ideal sp={sep}-1,{zinv}*{sep}-1;print(reduce(1,std(n)));print(reduce(1,std(p)));print(reduce(1,std(sn)));print(reduce(1,std(sp)));quit;\n')
    assert ctrl['returncode']==0 and not ctrl['parser_error'] and ctrl['output'].splitlines()==['0','1','0','1']
    output=logpath.read_text() if logpath.exists() else ''
    item.update(status=ex.get('status',meta['status']),script=str(scriptpath),script_sha256=sha(scriptpath),
      backend_sha256=meta['driver_sha256'],metadata_sha256=sha(metapath),execution_sha256=sha(ep) if ep.exists() else None,
      driver_rc=ex.get('returncode'),cas_rc=meta.get('cas',{}).get('returncode'),
      total_wall_seconds=ex.get('elapsed_seconds'),cas_wall_limit_seconds=ex.get('cas_wall_limit_seconds'),
      backend_phases=meta['phases'],output_sha256=sha(logpath) if logpath.exists() else None,
      output=output,ring_field='Q',ring_order='dp',ordered_generator_count=len(meta['ring_generator_order']),
      ordered_generator_sha256=digest(('\n'.join(meta['ring_generator_order'])+'\n').encode()),
      ring_declaration_sha256=digest((ring+'\n').encode()),ring_generators_retained_in=str(metapath),
      localizers=['Z55*leader55-1',f'{zinv}*{sep}-1'],counts=counts,
      characteristic_block={'status':'PASS','identity':'Q=(3R/4+p)H^2-vUH/8+vR-9U^2/64+pv+q, R=v^2-UH modulo every high-y remainder equation',
      'all_high_R_rows':counts['R_high'],'all_inclusive_Q_rows':counts['Q'],'normalizer':196,'target_depth':141,
      'whole_target':'leader55*z^40*(1+z)^15','target_subtraction':'PASS: 16 binomial coefficients, then leader localizer; no other leader occurrence',
      'all_source_rows_transported':vr['all_raw_rows_checked'],'graph_projection':'acyclic monic graph isomorphism; no graph variable is localized'},
      parser_status='PASS' if 'ALL_ROWS_PARSED\n' in output and not re.search(r'(^|\n)\s*\?',output) else 'UNVERIFIED',
      in_run_controls=meta.get('cas',{}).get('controls',[]),standalone_ring_localizer_controls=ctrl,
      acceptance='COMPUTE-BOUND: no END_GB/END_RESULT, no unit or properness read' if 'END_RESULT' not in output else 'REQUIRES_PARENT_REVIEW')
    observed=[p for p in resource_data['records'] if str(scriptpath) in p['args']]
    if observed:
      item['rss_observations']=observed
      item['rss_kib']=max(p['max_observed_VmHWM_kib'] for p in observed)
      item['rss_note']='Observed process VmHWM through last parent-monitor sample, a lower bound on eventual peak, not an exact final peak.'
    records.append(item)

# Tiny known positive and deliberately wrong-face controls are separate from client systems.
backend_controls=[]
for case,expected in [('positive','1'),('negative','0')]:
  p=HERE/'d108'/f'circuit-control-{case}-v2.sing'
  if p.exists():
    result=cas(p.read_text())
    marker=result['output'].split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines()
    controls=result['output'].split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].splitlines()
    assert result['returncode']==0 and not result['parser_error'] and marker[0]==expected and controls==['0','1']
    backend_controls.append({'case':case,'script':str(p),'script_sha256':sha(p),'result':marker,'controls':controls,'replay':result})

result={'audit_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'scope':'Read-only worker harvest; no client Groebner computation restarted or stopped.',
  'records':records,'proof_custody':proof_check,'verification_sha256':sha(BASE/'circuit-inputs/verification.json'),
  'backend_sha256':sha(HERE/'d108/coefficient_circuit_backend_v2.py'),
  'backend_controls':backend_controls,
  'resource_observations_updated_utc':resource_data.get('updated_utc'),
  'source_leading_pole_audit':'Stages0..8 are strictly below F/G leading poles (delta2 powers4..12 <54,81; delta52 powers8..16 <126,189). Their source pole target is zero. At-level forced faces remain coefficient-minus-target; no endpoint unit is read.',
  'rss_note':'No historical peak RSS is inferred from AS=16GiB. Parent polling records live VmHWM separately.'}
print(json.dumps(result,indent=2,sort_keys=True))
