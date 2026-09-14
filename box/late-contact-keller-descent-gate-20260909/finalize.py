import sys
sys.dont_write_bytecode = True
import json, subprocess, hashlib, datetime, resource, re
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2'); P=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
    if not c: raise RuntimeError(m)
pins=json.loads((P/'PINS.json').read_bytes()); prompt=P/'fable.prompt.md'
for e in pins['entries']:
    require(sha(R/e['source'])==e['sha256'],'source drift')
    require(sha(R/e['snapshot'])==e['sha256'],'snapshot drift')
actual=subprocess.run(['sed','-n','s/^charged_input=//p',str(prompt)],capture_output=True,timeout=25,check=True).stdout.decode().splitlines()
expected=[str((P/'PINS.json').relative_to(R))]+[e['snapshot'] for e in pins['entries']]
require(actual==expected,'actual ops/lane.sh sed vector mismatch')
require(len({Path(p).name for p in actual})==len(actual),'duplicate basename')
body=prompt.read_text(); require('{{LANE_INPUTS}}' in body,'placeholder absent')
require(not re.search(r'^charge_basis=',body,re.M),'invalid price declaration')
require('late-contact-keller-descent-gate-fable5-20260909' in body,'tag mismatch')
require('ABSOLUTELY NO mathematical subprocess' in body,'mathematical-process prohibition missing')
with (P/'preflight.json').open('x') as f:
    json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_parser':'sed -n s/^charged_input=//p (ops/lane.sh)','vector':actual,'unique_basenames':True,'literal_placeholder':True,'current_source_snapshot_pins':True,'mathematical_subprocesses':0,'launched':False},f,indent=2)
prompt.chmod(0o444)
cap=json.loads((P/'capability.json').read_bytes()); out=[]
require(Path(cap['partial_path']).read_bytes().endswith(b'<!-- BODY-END -->\n'),'body incomplete')
for op in ('close','finalize','verify'):
    cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
    if op!='verify': cmd+=['--token',cap['token']]
    r=subprocess.run(cmd,capture_output=True,timeout=25)
    require(r.returncode==0,op+': '+r.stdout.decode()+r.stderr.decode())
    out.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('x') as f: json.dump(out,f,indent=2)
paths=[p for p in P.rglob('*') if p.is_file() and p.name!='capability.json']+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
entries=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(paths)]
cust={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'/root/nonemptiness_certificate','status':'TERMINAL_PREP_ONLY_READY_FOR_ROOT_REVIEW_NOT_LAUNCHED','writers':'ALL IDLE after this exclusive custody write','entries':entries,'inputs':pins['entries'],'proof_changes':False,'mathematical_subprocesses':0,'review_deadline':'root supplies absolute deadline at actual invitation','agents_aws_remote_launches':0}
with (P/'custody.json').open('x') as f: json.dump(cust,f,indent=2)
for e in entries: require(sha(R/e['path'])==e['sha256'],'owned drift')
for e in pins['entries']: require(sha(R/e['source'])==e['sha256'],'post input drift')
print(json.dumps({'report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'prompt_sha256':sha(prompt),'pins_sha256':sha(P/'PINS.json'),'preflight_sha256':sha(P/'preflight.json'),'charged':len(actual),'owned':len(entries),'writers':'IDLE','launched':False,'utc':cust['utc']},indent=2))
