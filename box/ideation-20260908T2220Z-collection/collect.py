import sys
sys.dont_write_bytecode=True
import json,hashlib,datetime,subprocess,re,resource,importlib.util
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
ROOT=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent;PACK=ROOT/'box/ideation-20260908T2220Z'
DEADLINE='2026-09-08T22:56:47.147953+00:00'
PIDS={'fable5':[3739624,3740468,3740470],'sol56':[3739634,3740471,3740475,3740510]}
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def must(c,msg):
 if not c:raise RuntimeError(msg)
def run(cmd):
 r=subprocess.run(cmd,capture_output=True,timeout=25)
 must(r.returncode==0,'command failed: '+r.stderr.decode());return r.stdout
def observation():
 states={}
 for lane,pids in PIDS.items():
  name='jc2-lane-ideation-20260908T2220Z-'+lane+'.service'
  b=run(['systemctl','--user','show',name,'--property=Id,LoadState,ActiveState,SubState,MainPID,ExecMainStatus,ExecMainExitTimestamp,ExecMainStartTimestamp,ControlGroup'])
  d=dict(x.split('=',1) for x in b.decode().splitlines() if '=' in x)
  d['original_pids_alive']=[p for p in pids if Path('/proc',str(p)).exists()];states[lane]=d
 return {'utc':now(),'states':states,'all_terminal':all(v['ActiveState'] in ('inactive','failed') and v['MainPID']=='0' and not v['original_pids_alive'] for v in states.values())}
def save(name,v):
 with (P/name).open('xb') as f:f.write(json.dumps(v,indent=2,sort_keys=True).encode())
def collect():
 o=observation();save('terminal-observation-'+datetime.datetime.now(datetime.timezone.utc).strftime('%H%M%S%f')+'.json',o);must(o['all_terminal'],'refuse any receipt/report access before ALL external lanes terminal')
 # Receipt bytes are accessed first, before report hashes, seals or bodies.
 receipts={}
 for lane in PIDS:
  src=ROOT/f'xmodel/ideation-20260908T2220Z-{lane}.run.v2';b=src.read_bytes()
  dest=P/f'{lane}.run.v2'
  if dest.exists():must(dest.read_bytes()==b,'receipt changed after first collection')
  else:
   with dest.open('xb') as f:f.write(b)
  d={}
  for line in b.decode().splitlines():
   if '=' in line:
    k,v=line.split('=',1);must(k not in d,'duplicate receipt key '+k);d[k]=v
  must('end_utc' in d and 'exit_code' in d,'nonterminal receipt '+lane)
  receipts[lane]={'path':str(src.relative_to(ROOT)),'sha256':hashlib.sha256(b).hexdigest(),'fields':d}
 pins=json.loads((PACK/'PINS.json').read_bytes());inputs={};prompt_pins={}
 for lane in ('coordinator','astra','fable5','sol56'):
  prompt=PACK/f'{lane}.prompt.md';must(sha(prompt)==pins[str(prompt.relative_to(ROOT))],'prompt drift '+lane)
  paths=[x[len('charged_input='):] for x in prompt.read_text().splitlines() if x.startswith('charged_input=')]
  must(len(paths)==19 and len(set(paths))==19,'wrong input vector '+lane)
  if inputs:must(paths==list(inputs),'unequal lane inputs')
  for path in paths:
   must('jc2-lean' not in path,'protected input')
   h=sha(ROOT/path);must(h==pins[path],'input drift '+path);inputs[path]=h
  prompt_pins[lane]=sha(prompt)
 # Parse the canonical external receipt's actual input-vector syntax.
 for lane,r in receipts.items():
  d=r['fields'];must(d.get('charged_inputs')=='19','receipt input count '+lane)
  for i,(path,h) in enumerate(inputs.items(),1):
   key='charged_input_'+str(i)
   must(d.get(key)==path,'receipt source mismatch '+lane+':'+str(i))
   must(d.get(key+'_sha256')==h,'receipt input hash mismatch '+lane+':'+str(i))
   must(d.get(key+'_post')=='UNCHANGED','receipt post-state '+lane+':'+str(i))
  must(d.get('exit_code')=='0' and d.get('adapter_exit_code')=='0','external lane failure '+lane)
  must(d.get('prompt_sha256')==prompt_pins[lane] and d.get('post_prompt_sha256')==prompt_pins[lane],'external prompt drift '+lane)
  for key in ('adapter','launcher','charge_basis_validator','seal_tool','fallacy'):
   if key=='adapter':
    must(re.fullmatch('[a-z0-9_-]+',d['adapter']) is not None,'unsafe adapter metadata');path=ROOT/'ops/adapters'/(d['adapter']+'.sh')
   else:path=ROOT/d[key]
   must(sha(path)==d[key+'_sha256']==d['post_'+key+'_sha256'],'tool input drift '+lane+':'+key)
  must(d.get('report_state') in ('BODY_SEALED','BODY_SEALED_AFTER_DIVERT'),'unsealed external report '+lane)
  report=ROOT/d['report'];must(sha(report)==d['report_sha256'],'report drift '+lane)
  spec=importlib.util.spec_from_file_location('collection_seal',ROOT/'ops/seal.py');module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
  data=report.read_bytes();boundary=module._body_boundary(data)
  if data[boundary:].strip():
   bodybytes,bodysha,basis=module.verify_bytes(data);r['seal_verify']={'type':'CANONICAL_BYTE_SEAL','body_bytes':bodybytes,'body_sha256':bodysha,'basis':basis}
  else:r['seal_verify']={'type':'BODY_END_ONLY_RECEIPT_BOUND','body_bytes':boundary,'body_sha256':hashlib.sha256(data[:boundary]).hexdigest(),'canonical_artifact_transaction':False}
  r['report_bytes']=report.stat().st_size;r['late']=datetime.datetime.fromisoformat(d['end_utc'].replace('Z','+00:00'))>datetime.datetime.fromisoformat(DEADLINE)
  r['lateness_seconds']=str(max(0,(datetime.datetime.fromisoformat(d['end_utc'].replace('Z','+00:00'))-datetime.datetime.fromisoformat(DEADLINE)).total_seconds()))
 # Local terminal manifests and known report pins; no report text is emitted.
 locals={}
 for lane,expected in [('coordinator','32c5ce2b2df6d8f7bac284c9e147c4546c86d3debec11ee75e282ff649cb00f9'),('astra','682383426ee1853646166f07a2f6648ae757572992c869e07f044a89a2ea76c3')]:
  report=ROOT/f'xmodel/ideation-20260908T2220Z-{lane}.md';must(sha(report)==expected,'local report drift '+lane)
  txn=Path(str(report)+'.artifact.json');v=json.loads(run(['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),'verify','--final',str(report)]))
  locals[lane]={'report_path':str(report.relative_to(ROOT)),'report_sha256':expected,'transaction_sha256':sha(txn),'transaction':json.loads(txn.read_bytes()),'verify':v}
 must(locals['astra']['transaction_sha256']=='8709b69be5da2e87c53a4657248ca5b46df4db600914f2d3e991b0ce5315f78a','Astra transaction drift')
 cu=ROOT/'box/ideation-20260908T2220Z-astra/custody.json';must(sha(cu)=='dd45946004d9d4331fac9ec808cdbecb11aae87b4be8cc0cb8c9444bb04fb802','Astra custody drift');cust=json.loads(cu.read_bytes())
 for e in cust['entries']:must(sha(ROOT/e['path'])==e['sha256'],'Astra custody entry drift')
 locals['astra']['custody']=cust;locals['astra']['custody_sha256']=sha(cu)
 replays=ROOT/'box/ideation-20260908T2220Z-astra/replay-and-input-pins.json';locals['astra']['replay_metadata']=json.loads(replays.read_bytes())
 root_closed=locals['coordinator']['transaction']['custody']['closed_utc']
 for lane,r in receipts.items():must(root_closed<r['fields']['start_utc'],'root blind not frozen before invitation/launch '+lane)
 final=observation();must(final['all_terminal'],'process state changed during collection')
 out={'status':'COMPLETE_METADATA_COLLECTION','collected_utc':now(),'deadline':DEADLINE,'peer_bodies_read':False,'inputs':inputs,'prompt_pins':prompt_pins,'external':receipts,'local':locals,'final_state':final,'scope':'receipt/pin/seal/custody collection only; no mathematical adjudication or launch authority'}
 save('collection.json',out);print(json.dumps({'status':out['status'],'collected_utc':out['collected_utc'],'external':{k:{'end':v['fields']['end_utc'],'late':v['late'],'report_sha256':v['fields']['report_sha256']} for k,v in receipts.items()},'inputs':len(inputs),'bodies_read':False},indent=2))
if __name__=='__main__':
 if sys.argv[1]=='observe':
  o=observation();save('observation-'+datetime.datetime.now(datetime.timezone.utc).strftime('%H%M%S')+'.json',o);print(json.dumps(o,indent=2))
 elif sys.argv[1]=='collect':collect()
 else:raise RuntimeError('unknown mode')
