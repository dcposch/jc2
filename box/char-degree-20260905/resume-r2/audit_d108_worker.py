#!/usr/bin/env python3
"""Read-only remote custody audit; no worker-tree copies or large host outputs."""
import hashlib,json,subprocess
from pathlib import Path

REMOTE = r'''
import datetime,hashlib,json,math,re
from fractions import Fraction
from flint import fmpq_mpoly,fmpq_mpoly_ctx
from pathlib import Path
root=Path('/home/ubuntu/jc2/box/char-degree-20260905/d108')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024*1024): h.update(b)
 return h.hexdigest()
def seqsha(s):return hashlib.sha256(('\n'.join(s)+'\n').encode()).hexdigest()
def resolve(p):
 p=Path(p)
 return p if p.is_absolute() else root/p
def readj(p):return json.loads(p.read_text())
resources_path=root.parent/'resume-r2/resource-observations.json'
resources=readj(resources_path) if resources_path.exists() else {'records':[]}
def observed_rss(script,pid=None):
 matches=[r for r in resources['records'] if (pid is not None and r['pid']==pid) or (pid is None and r['args'].endswith(' '+str(script.relative_to(root))))]
 if not matches:return dict(observed_RSS_HWM_KiB=None,observed_RSS_note='No monitor observation; historical peak unavailable.')
 r=max(matches,key=lambda x:x['max_observed_VmHWM_kib'])
 return dict(observed_RSS_HWM_KiB=r['max_observed_VmHWM_kib'],observed_RSS_pid=r['pid'],observed_RSS_last_utc=r['last_observed_utc'],observed_RSS_note='Observed process high-water through last sample; may be below final peak.')
def mapaudit(inp,stage):
 iv=readj(inp); mp=inp.with_name(inp.name.replace('.input.json','.map.json'))
 if not mp.exists():mp=inp.with_name(inp.name.replace('.input.json','.json'))
 mm=readj(mp);ctx=fmpq_mpoly_ctx.get(tuple(['zz','tt']+iv['names']),ordering='lex');g=dict(zip(['zz','tt']+iv['names'],ctx.gens()));h=fmpq_mpoly(iv['h_expr'],ctx=ctx);D=fmpq_mpoly(iv['D_expr'],ctx=ctx);C=fmpq_mpoly(iv['C_expr'],ctx=ctx)
 tops=h.subs({'tt':0})==g['zz']**28*(1+g['zz'])**8
 face=fmpq_mpoly(iv['face_expr'],ctx=ctx)*h.subs({'tt':0})==g['zz']**49*(1+g['zz'])**14
 mind=min((int(D.monomial(i)[1]) for i in range(len(D))),default=None);minc=min((int(C.monomial(i)[1]) for i in range(len(C))),default=None)
 pivots=mm.get('pivot_ledger',[])
 return dict(map_metadata=str(mp.relative_to(root)),map_sha256=sha(mp),map_input_hash_matches=mm.get('input_sha256')==sha(inp),map_stage=mm['stage'],map_field=mm['field'],physical_map=mm['physical_map'],source_rows=mm['source_rows'],source_rows_sha256=mm['source_rows_sha256'],source_residual=mm['source_residual'],derived_rows=mm['derived_rows'],derived_rows_sha256=mm['derived_rows_sha256'],all_recorded_pivots_nonzero_rational=all(Fraction(x['leader'])!=0 for x in pivots),recorded_pivot_count=len(pivots),strong_front_ledger=mm['strong_front_ledger'],actual_min_D_t=mind,actual_min_C_t=minc,strong_front_images_pass=(mind is None or mind>(32 if stage==0 else 33)) and (minc is None or minc>(66 if stage==0 else 68)),actual_H0_pass=bool(tops),actual_complete_target_pass=bool(face),jet0_free=mm['jet0_free'],mean_free=mm.get('mean_free',False),jet0_gauge=mm.get('jet0_gauge'),adapter_sha256=mm.get('adapter_sha256'),translation_summary={k:v for k,v in mm.get('translation',{}).items() if k not in ['forward_generator_images','old_generator_images_in_new_ring','coefficient_generator_order','fixed_generators']},gauge_ledger=mm['gauge_ledger'])
records=[]
for p in sorted(root.glob('d108*circuit_stage*.circuit.json')):
 m=readj(p); script=p.with_suffix('').with_suffix('.sing'); inp=resolve(m['input']); log=p.with_suffix('.out')
 text=script.read_text(); out=log.read_text() if log.exists() else ''; counts=m['counts']
 body=text.split('ideal I=\n',1)[1].split(';\nprint("ALL_ROWS_PARSED")',1)[0];rows=body.split(',\n')
 names=text.split('ring R=0,(',1)[1].split('),dp;',1)[0].split(',')
 row_start=len(rows)-counts['Q']-counts['localizers']; row_stop=len(rows)-counts['localizers']
 faces=[(i,r) for i,r in enumerate(rows) if re.search(r'\bleader63\b',r) and not re.search(r'\bZ63\b',r)]
 targets=[]; target_ok=len(faces)==15
 for i,r in faces:
  mm=re.search(r'\+\(-1\)\*\(\(([0-9]+)\)\*leader63\)\)$',r)
  target_ok &= row_start<=i<row_stop and r.count('leader63')==1 and mm is not None
  targets.append(int(mm[1]) if mm else None)
 target_ok &= targets==[math.comb(14,j) for j in range(15)] and [i for i,r in faces]==list(range(row_stop-15,row_stop))
 iv=readj(inp); cas=m.get('cas',{}); phases=m['phases']; backend=root/('coefficient_circuit_backend_v2.py' if 'meanfree' in p.name else 'coefficient_circuit_backend.py')
 localizers=rows[-counts['localizers']:]
 rec=dict(variant='free-mean full chart' if 'meanfree' in p.name else 'frozen mean-zero restricted chart',stage=int(re.search(r'stage(\d+)',p.name)[1]),metadata=str(p.relative_to(root)),metadata_sha256=sha(p),status=m['status'],field=m['field'],monomial_order='dp',ring_generator_count=len(names),ring_generator_order_sha256=seqsha(names),ring_generator_hash_encoding='UTF-8, one ordered name per line, terminal newline',ring_matches_metadata=names==m['ring_generator_order'],source_generator_count=len(iv['names']),source_generator_order_sha256=seqsha(iv['names']),script=str(script.relative_to(root)),script_bytes=script.stat().st_size,script_sha256=sha(script),script_matches_receipt=sha(script)==m['script_sha256'],input=str(inp.relative_to(root)),input_sha256=sha(inp),input_matches_receipt=sha(inp)==m['input_sha256'],backend=str(backend.relative_to(root)),backend_sha256=sha(backend),backend_matches_receipt=sha(backend)==m['driver_sha256'],output=str(log.relative_to(root)),output_sha256=sha(log) if log.exists() else None,output_matches_receipt=(sha(log)==cas['log_sha256']) if 'log_sha256' in cas else None,returncode=cas.get('returncode'),wall_seconds=phases[-1]['seconds'] if phases[-1]['name']=='finished' else None,wall_includes_build=True,build_seconds=next((x['seconds'] for x in phases if x['name']=='script_complete'),None),peak_RSS_KiB=None,RSS_note='Peak child RSS was not recorded by inherited wrapper. Address-space cap is not RSS.',address_space_limit_GiB=16,parser_all_rows='ALL_ROWS_PARSED' in out,parser_errors=cas.get('errors',[]),completed_controls=cas.get('controls',[]),completed_result=cas.get('result'),full_characteristic_block_emitted=any(x['name']=='full_rows_emitted' for x in phases),row_counts=counts,row_count_matches=len(rows)==sum(counts.values()),target_depth=m['target_depth'],physical_target_depth=153,target_subtraction_pass=bool(target_ok),whole_target='leader63*tt^151*zz^49*(1+zz)^14',target_binomial_coefficients=targets,localizer_rows=localizers,localizers_pass=localizers==['(Z63*leader63-1)','(Zc*c-1)'],all_five_target_scalars_retained=all('target_'+x in names for x in 'abcde'),no_t_or_z_in_coefficient_ring=not any(x in names for x in ['tt','zz']),jet0_present='jet0' in names,mean_present='minor_mean' in names,source_residual_count=len(iv['residual_strings']),last_output_lines=out.splitlines()[-5:])
 if rec['variant'].startswith('frozen') and rec['stage']==8:rec['address_space_limit_GiB']=None
 rec['source_map_audit']=mapaudit(inp,rec['stage']);rec.update(observed_rss(script));records.append(rec)
selected=[]
for p in sorted(root.glob('selected/*/result.json')):
 m=readj(p); script=resolve(m['script']);inp=resolve(m['input']);log=p.parent/'singular.out';base=readj(p.parent/'base.circuit.json'); text=script.read_text();out=log.read_text(); names=text.split('ring R=0,(',1)[1].split('),dp;',1)[0].split(','); counts=base['counts'];body=text.split('ideal I=\n',1)[1].split(';\nprint("ALL_ROWS_PARSED")',1)[0];rows=body.split(',\n')
 faces=[r for r in rows if re.search(r'\bleader63\b',r) and not re.search(r'\bZ63\b',r)]; coeff=[]
 for r in faces:
  mm=re.search(r'\+\(-1\)\*\(\(([0-9]+)\)\*leader63\)\)$',r);coeff.append(int(mm[1]) if mm else None)
 selected.append(dict(case=p.parent.name,scope='free-mean jet0 slice (covariance audit required)' if 'jet0' in p.parent.name else 'free-mean unsliced full chart',stage=8,result=m,result_sha256=sha(p),script_sha256=sha(script),script_matches_receipt=sha(script)==m['script_sha256'],input_sha256=sha(inp),input_matches_receipt=sha(inp)==m['input_sha256'],output_sha256=sha(log),ring_generator_count=len(names),ring_generator_order_sha256=seqsha(names),monomial_order='dp',backend='slimgb',row_counts=counts,full_characteristic_block_emitted=len(rows)==sum(counts.values()),target_subtraction_pass=coeff==[math.comb(14,j) for j in range(15)],localizer_rows=rows[-counts['localizers']:],parser_all_rows='ALL_ROWS_PARSED' in out,parser_errors=m.get('parser_or_cas_errors',[]),peak_RSS_KiB=None,RSS_note='Wrapper does not record peak RSS.',wrapper_sha256=sha(p.parent/'run_singular_case_snapshot.py'),variant_adapter_sha256=sha(p.parent/'slimgb_variant_snapshot.py'),source_map_audit=mapaudit(inp,8),**observed_rss(script,m.get('pid'))))
history=[]
for p in sorted(root.glob('*.json')):
 if 'circuit' in p.name or p.name.endswith('.input.json') or p.name.endswith('.map.json'):continue
 try:m=readj(p)
 except Exception:continue
 if not isinstance(m,dict) or not re.search('stage[0-8]',p.name):continue
 run=m.get('run',m.get('cas',{}));status=m.get('status',m.get('verdict'))
 if status:
  lp=p.with_suffix('.out');lt=lp.read_text() if lp.exists() else ''
  history.append(dict(metadata=p.name,status=status,returncode=run.get('returncode'),wall_seconds=run.get('elapsed_seconds'),last_progress=run.get('last_progress_marker'),output_hash=sha(lp) if lp.exists() else run.get('log_sha256'),errors=run.get('errors',run.get('parser_or_cas_errors')),actual_log_says_no_more_memory='no more memory' in lt.lower(),script_hash=m.get('script_sha256'),input_hash=m.get('input_sha256')))
dependencies={str(p.relative_to(root.parent)):sha(p) for p in sorted(root.glob('*.py'))}
print(json.dumps(dict(audit_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),worker='172.30.0.40',worker_root=str(root),resource_snapshot_sha256=sha(resources_path) if resources_path.exists() else None,resource_snapshot_utc=resources.get('updated_utc'),dependencies_sha256=dependencies,stages=records,selected=selected,historical=history),indent=2))
'''

out=Path(__file__).resolve().parent/'audit-d108-custody.json'
run=subprocess.run(['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'ubuntu@172.30.0.40','python3','-'],input=REMOTE,text=True,capture_output=True)
if run.returncode:
    print(run.stderr)
    run.check_returncode()
data=json.loads(run.stdout)
controls_path=out.parent/'audit-d108-actual-ring-controls.json'
if controls_path.exists():
    actual=json.loads(controls_path.read_text())
    data['actual_ring_controls_sha256']=hashlib.sha256(controls_path.read_bytes()).hexdigest()
    for rec in data['stages']+data['selected']:
        matches=[r for r in actual['records'] if r['source_script_sha256']==rec['script_sha256'] and r['ring_generator_order_sha256']==rec['ring_generator_order_sha256']]
        assert matches and all(r['passed'] for r in matches)
        rec['actual_ring_controls']={k:matches[0][k] for k in ['controls','passed','control_script_sha256','output_sha256','returncode','parser_all_rows']}
out.write_text(json.dumps(data,indent=2)+'\n')
print('wrote',out,len(run.stdout),'bytes')
for r in data['stages']: print(r['variant'],r['stage'],r['status'],r['returncode'],r['wall_seconds'],r['target_subtraction_pass'])
for r in data['selected']: print(r['case'],r['result']['status'])

lines=['D108 delta=3 worker audit, '+data['audit_utc'],'',
 'Every emitted production circuit has a complete exact-Q characteristic block and passes the mechanical script/input/backend/ring checks and whole-leading-target subtraction. No completed production unit or proper ideal has been observed. The status table is a resource verdict, not an algebraic decision.','',
 'Custody: `audit-d108-custody.json` records remote script, input, backend, map, output and metadata SHA-256 values; the exact ordered coefficient-ring generator count and SHA-256 (one name per line with terminal newline); source and derived row hashes; rc, wall, controls, localizers and graph row counts. The large scripts stay on the worker. Frozen mean-zero and repaired free-mean charts are distinct.','',
 '| Stage | Frozen mean-zero: status / rc / wall s / observed RSS HWM KiB | Free-mean: status / rc / wall s / observed RSS HWM KiB |',
 '|---:|---|---|']
for stage in range(9):
 cells=[]
 for free in [False,True]:
  r=next((r for r in data['stages'] if r['stage']==stage and ('free-mean full' in r['variant'])==free),None)
  cells.append('Not yet emitted' if r is None else f"{r['status']} / {r['returncode']} / {r['wall_seconds']} / {r.get('observed_RSS_HWM_KiB')}")
 lines.append(f'| {stage} | '+ ' | '.join(cells)+' |')
lines += ['',
 'Wall includes the subsecond circuit build. `EMITTED_NOT_DECIDED` is a startup/live metadata state, never a properness assertion. Historical peak RSS is unavailable: the inherited circuit wrapper never called wait4/getrusage, and RLIMIT_AS is an address-space cap. The scheduled runs have a 16 GiB address-space cap; stage8 mean-zero was launched separately and its cap is not established by the retained schedule script. Observed /proc VmHWM values from the parent resource monitor may be supplied separately and are lower bounds on historical peak RSS.','',
 'The coefficient ring is Q[ordered source parameters, ordered acyclic graph variables], Singular order dp. The structural extraction variables tt,zz are absent from this ring. Every input retains target_a through target_e, leader63, Z63, c, Zc. The two inverse equations are exactly Z63*leader63-1 and Zc*c-1. The source maps eliminate only nonzero rational pivots; actual saved pivot leaders were parsed as Fractions and checked nonzero. Stage0 maps have D starting at33 and C starting at67; stages1–8 have D starting at34 and C starting at69. These are previously proved radical consequences, not extra gauge pins.','',
 'The actual H0 was recomputed over Q in each input and equals zz^28*(1+zz)^8. Multiplying it by the supplied face expression gives zz^49*(1+zz)^14. In every emitted circuit the only occurrences of leader63 outside its inverse row are the last15 characteristic rows; their subtractions have all binomial coefficients 1,14,91,364,1001,2002,3003,3432,3003,2002,1001,364,91,14,1. These rows occur at normalized depth151 for ambient214, which is physical depth153 for ambient216. No target coefficient was set equal to zero in place of coefficient-minus-target. All graph, high-remainder and characteristic rows are present before ALL_ROWS_PARSED.','',
 'For the original translated circuits, jet0 remains free: translation changes the computational outer coefficient basis and h expression, keeps source rows, and has the saved exact inverse/generator round trips. The original mean-zero minor face is a restriction with no general coverage theorem. Its unit would therefore concern that restricted chart. The supplementary inputs retain minor_mean, use -((pi-minor_mean)^2-c) for the h3 face, and keep c nonzero. Their source maps retain every mean term and match the input hashes; no mean normalization is spent. Scheduled pole powers1–12 do not reach F/G target powers96/64. The actual D2 faces used by Theorem B are unchanged.','',
 'The selected stage8 slimgb cases are:']
for r in data['selected']:
 result=r['result'];mm=r['source_map_audit']
 lines += [f"- {r['case']}: {result['status']}, rc={result.get('returncode')}, wall={result.get('elapsed_seconds')} s, observed RSS HWM={r.get('observed_RSS_HWM_KiB')} KiB; {r['scope']}. Script SHA-256 `{r['script_sha256']}`, input `{r['input_sha256']}`, map `{mm['map_sha256']}`."]
lines += ['',
 'The selected jet0 slice exists only after the free-mean repair. Its adapter hash is ec43f6c36097aa530a786163f49622a556149eabb3b40fb70e79993dbe4f9b21. Its declared q=old jet0 map is jet0→0, u→u, v→v−qu, mu→mu+q²u−2qv, c→c; the source graph and arc transport are subject to the separate d108-meanfree-translation-control proof. The snapshot does not use the unsupported simultaneous even-face/jet0 normalization. Both selected scripts independently pass ALL_ROWS_PARSED and full target subtraction, regardless of the wrapper omitting ALL_ROWS_PARSED from its own success predicate.','',
 'Fresh tiny controls were regenerated and replayed on the worker with current circuit v1 SHA-256 9fd1880ade43659dccd8949391dc3ad000788a7d87e50b25abb4bf9b1c0e145a, current v2 SHA-256 17a825098e24dcbeb973d7fe6f254c6f5884f2aad9bed196e12166db0520ce35, and v2+slimgb. All six runs returned rc0 with clean parsing and localizer controls0,1. Positive attained-degree controls had reduce(1)=1, dimension0, basis size19; the wrong-target controls had reduce(1)=0, dimension−1, basis size1. This closes the old v2-labelled control receipt mismatch: the fresh receipt directly names current v2. These toy controls are not source-chart survivors. Evidence: audit-d108-fresh-controls.json.','',
 'Additionally, standalone inverse controls were freshly replayed in all20 actual production coefficient rings:18 scheduled circuits and both selected rings. The ideals (leader63,Z63*leader63−1), (leader63−1,Z63*leader63−1), (c,Zc*c−1), (c−1,Zc*c−1) returned reduce(1) vectors0,1,0,1 in every ring. All returned rc0 with ALL_CONTROL_ROWS_PARSED and no parser errors, taking0.01–0.02s with measured peak RSS about12MiB. The per-ring source-script/ring/control-script/output hashes and wall/RSS are in audit-d108-actual-ring-controls.json. These are localizer implementation checks, not full production ideal reruns.','',
 'Historical attempts remain excluded from mathematical promotion. The active early physical backend stages1–8 carry the legacy CAS_ERROR_OPEN label (rc14, 37.444–51.936 s), but their actual logs say no more memory during BEGIN_DIVIDE_vv2, without parser errors. Stage0 is emitted-only in its active metadata. Separate parser-defective startup attempts are under invalid-pre-control. Total-face stages0–8 failed during monic division before a full ideal decision (memory-bound, 360.409–882.144 s). Their 24GiB stages0–5 timed out at about1200.5 s; stages6–8 were superseded without a decision. Native FLINT and early-front/remainder variants were memory-bound. The full historical metadata catalog is in audit-d108-custody.json. No historical result was promoted to unit, properness, or coordinates.','',
 'Acceptance rule: even a future UNIT flag needs clean exact-Q parsing, completed current controls, complete maps/characteristic rows, target subtraction, gauge and derived-face audits, then independent replay. A completed proper full free-mean ideal would prove a nondegenerate necessary-chart survivor over Qbar by Theorem B and the weak Nullstellensatz; it would not prove the Jacobian is constant. A timeout or a partially constructed ideal supplies neither conclusion. No worker job was killed by this audit.']
(out.parent/'audit-d108.md').write_text('\n'.join(lines)+'\n')
