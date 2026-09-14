import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,datetime,resource,re
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
pins=json.loads((P/'PINS.json').read_bytes());prompt=P/'fable.prompt.md'
for e in pins['entries']:
 require(sha(R/e['source'])==e['source_sha256'],'source drift '+e['source'])
 require(sha(R/e['snapshot'])==e['sha256'],'snapshot drift')
actual=subprocess.run(['sed','-n','s/^charged_input=//p',str(prompt)],capture_output=True,timeout=10,check=True).stdout.decode().splitlines()
expected=[str((P/'PINS.json').relative_to(R))]+[e['snapshot'] for e in pins['entries']]
require(actual==expected,'literal lane parser vector mismatch');require(len({Path(p).name for p in actual})==len(actual),'duplicate basename')
text=prompt.read_text();require('{{LANE_INPUTS}}' in text,'missing lane placeholder');require(not re.search(r'^charge_basis=',text,re.M),'invalid price declaration');require('ZERO MATHEMATICAL SUBPROCESSES' in text,'prohibition absent')
with (P/'preflight.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_parser':'sed -n s/^charged_input=//p (ops/lane.sh:258)','ordered_vector':actual,'unique_basenames':True,'source_and_snapshot_pins':True,'placeholder':True,'launched':False,'mathematical_subprocesses':0},f,indent=2)
cap=json.loads((P/'capability.json').read_bytes());require(Path(cap['partial_path']).read_bytes().endswith(b'<!-- BODY-END -->\n'),'incomplete body');out=[]
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 run=subprocess.run(cmd,capture_output=True,timeout=10);require(run.returncode==0,op+run.stdout.decode()+run.stderr.decode());out.append({'operation':op,'result':json.loads(run.stdout)})
with (P/'publication.json').open('x') as f:json.dump(out,f,indent=2)
paths=[p for p in P.rglob('*') if p.is_file() and p.name not in ('capability.json','custody.json')]+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
entries=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(paths)]
cust={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'/root/nonemptiness_certificate','status':'TERMINAL_PREP_ONLY_NOT_LAUNCHED','writers':'ALL IDLE after exclusive custody write','inputs':pins['entries'],'entries':entries,'charged_count':len(actual),'mathematical_subprocesses':0,'launches':0,'root_authority':'whole prompt and pins review before actual invitation/deadline','forbidden_peer_protected_access':False}
with (P/'custody.json').open('x') as f:json.dump(cust,f,indent=2)
for e in pins['entries']:require(sha(R/e['source'])==e['source_sha256'] and sha(R/e['snapshot'])==e['sha256'],'post input drift')
for e in entries:require(sha(R/e['path'])==e['sha256'],'owned drift')
print(json.dumps({'utc':cust['utc'],'report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'pins_sha256':sha(P/'PINS.json'),'prompt_sha256':sha(prompt),'preflight_sha256':sha(P/'preflight.json'),'owned':len(entries),'charged':len(actual),'writers':'IDLE','launched':False},indent=2))
