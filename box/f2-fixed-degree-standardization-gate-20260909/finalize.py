import sys
sys.dont_write_bytecode = True
import json, hashlib, subprocess, datetime, resource, importlib.util
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2'); P=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
    if not c: raise RuntimeError(m)
pins=json.loads((P/'input-pins.json').read_bytes())
for e in pins['entries']: require(sha(R/e['path'])==e['sha256'],'input drift: '+e['path'])
cap=json.loads((P/'capability.json').read_bytes()); partial=Path(cap['partial_path'])
body=partial.read_text(); require(body.endswith('<!-- BODY-END -->\n'),'body not complete')
spec=importlib.util.spec_from_file_location('owned_f2_collision',R/'ops/open_collision.py')
module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
questions=module.extract_raised_opens(body)
require(not questions,'raised identifier requires authorized collision check')
rendered=module.render_collisions(questions,())
require(rendered.strip() in body,'report collision block mismatch')
with (P/'collisions.md').open('x') as f: f.write(rendered)
with (P/'collision-custody.json').open('x') as f:
    json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'extractor_sha256':sha(R/'ops/open_collision.py'),'functions':['extract_raised_opens','render_collisions'],'raised_count':0,'status':'EMPTY','corpus_scan':False,'forbidden_blind_or_protected_access':False,'mathematical_subprocesses':0},f,indent=2)
outputs=[]
for op in ('close','finalize','verify'):
    cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
    if op!='verify': cmd+=['--token',cap['token']]
    else: cmd+=['--expected-basis','0d39df3c9fd69c939a8420c54d03228b9077777d']
    run=subprocess.run(cmd,capture_output=True,timeout=10)
    require(run.returncode==0,op+': '+run.stdout.decode()+run.stderr.decode())
    outputs.append({'operation':op,'result':json.loads(run.stdout)})
with (P/'publication.json').open('x') as f: json.dump(outputs,f,indent=2)
paths=[p for p in P.iterdir() if p.is_file() and p.name not in ('capability.json','custody.json')]+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
entries=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(paths)]
for e in pins['entries']: require(sha(R/e['path'])==e['sha256'],'post-input drift')
custody={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'/root/nonemptiness_certificate','status':'TERMINAL_PRIMARY_INTERFACE_AUDIT_AWAITING_ROOT_ADJUDICATION','writers':'ALL IDLE after exclusive custody write','mathematical_subprocesses':0,'metadata_only_subprocesses':True,'primary_table_generation_replayed':False,'canonical_or_shared_writes':False,'blind_or_live_peer_bodies_read':False,'protected_project_access':False,'agents_aws_ssh_cas':0,'entries':entries,'inputs':pins['entries'],'proof_status':'primary-theorem/table trust; no campaign exclusion consumed; original-field rational automorphism descent not claimed'}
with (P/'custody.json').open('x') as f: json.dump(custody,f,indent=2)
for e in entries: require(sha(R/e['path'])==e['sha256'],'owned drift')
print(json.dumps({'utc':custody['utc'],'report':cap['final_path'],'report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'input_pins_sha256':sha(P/'input-pins.json'),'publication_sha256':sha(P/'publication.json'),'collision_custody_sha256':sha(P/'collision-custody.json'),'owned_entries':len(entries),'inputs':len(pins['entries']),'writers':'IDLE','mathematical_subprocesses':0},indent=2))
