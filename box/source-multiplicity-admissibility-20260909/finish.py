import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,datetime,resource,os
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def emit(name,d):
 with (P/name).open('x') as f:json.dump(d,f,indent=2)
old=json.loads((P/'input-pins.json').read_text())['inputs']; changes=[]
for e in old:
 got=sh(R/e['path'])
 if got!=e['sha256']:changes.append({'path':e['path'],'before':e['sha256'],'after':got})
 # Mutable canonical files are history lookup, not unsealed mathematical premises.
 if got!=e['sha256'] and e['path'].startswith(('xmodel/','box/')):raise RuntimeError('frozen input drift')
extra=['xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md','xmodel/positive-face-actual-receiver-gate-fable5-20260906.md','xmodel/order-basis-full-gpt55-20260903.md','box/twopoint-batch-20260903/shape.py']
entries=old+[{'path':n,'sha256':sh(R/n),'bytes':(R/n).stat().st_size} for n in extra]
emit('final-input-pins.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entries':entries,'canonical_history_changes':changes})
runs=[]
for opt in ([],['-O']):
 for mode in ('normal','changed-map','changed-top'):
  argv=['/usr/bin/python3','-I','-B']+opt+[str(P/'controls.py'),mode]
  r=subprocess.run(argv,capture_output=True,timeout=25)
  expected=0 if mode=='normal' else 1
  if r.returncode!=expected:raise RuntimeError('control verdict')
  runs.append({'argv':argv,'returncode':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
emit('replay.json',{'status':'PASS','runs':runs,'scope':'tiny elementary changed-object controls only; no theorem proof replay'})
c=json.loads((P/'capability.json').read_text()); results=[]
for action in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),action,'--final',c['final_path']]
 if action!='verify':cmd+=['--token',c['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25,check=True);results.append(json.loads(r.stdout))
emit('publication.json',{'status':'PASS','results':results})
final=Path(c['final_path']); txn=Path(c['final_path']+'.artifact.json')
own=[p for p in P.rglob('*') if p.is_file() and p.name!='capability.json']+[final,txn]
custody={'status':'TERMINAL','all_writers':'IDLE_AFTER_PUBLICATION','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs':entries,'files':[{'path':str(p.relative_to(R)),'sha256':sh(p),'bytes':p.stat().st_size} for p in own],'forbidden_peer_reads':False,'no_launch':True,'no_CAS':True}
emit('custody.json',custody)
for e in custody['files']:
 if sh(R/e['path'])!=e['sha256']:raise RuntimeError('owned drift')
print(json.dumps({'report':str(final.relative_to(R)),'report_sha256':sh(final),'transaction_sha256':sh(txn),'custody_sha256':sh(P/'custody.json'),'inputs_sha256':sh(P/'final-input-pins.json'),'replay_sha256':sh(P/'replay.json'),'current_inputs':len(entries),'owned_files':len(own),'canonical_changes':changes,'all_writers':'IDLE'},indent=2))
