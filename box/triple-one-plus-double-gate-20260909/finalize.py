import sys
sys.dont_write_bytecode=True
import json,subprocess,hashlib,datetime,resource,re
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
pins=json.loads((P/'PINS.json').read_bytes());prompt=P/'fable.prompt.md'
qualification=P/'root-qualification.md';rel=str(qualification.relative_to(R))
pins['entries'].insert(0,{'source':rel,'snapshot':rel,'sha256':sha(qualification),'bytes':qualification.stat().st_size,'tier':'DATED_ROOT_PROSE_QUALIFICATION_NOT_A_MATHEMATICAL_PREMISE'})
pins['status']='FINAL_PREP_ONLY_WITH_FROZEN_QUALIFICATION_NOT_LAUNCHED'
with (P/'FINAL-PINS.json').open('x') as f:json.dump(pins,f,indent=2)
(P/'FINAL-PINS.json').chmod(0o444)
for e in pins['entries']:
 require(sha(R/e['source'])==e['sha256'],'source drift')
 require(sha(R/e['snapshot'])==e['sha256'],'snapshot drift')
actual=subprocess.run(['sed','-n','s/^charged_input=//p',str(prompt)],capture_output=True,timeout=25,check=True).stdout.decode().splitlines()
expected=[str((P/'FINAL-PINS.json').relative_to(R))]+[e['snapshot'] for e in pins['entries']]
require(actual==expected,'actual lane sed vector mismatch')
require(len({Path(x).name for x in actual})==len(actual),'basename collision')
body=prompt.read_text();require('{{LANE_INPUTS}}' in body,'placeholder absent')
require(not re.search(r'^charge_basis=',body,re.M),'invalid price declaration')
require('ABSOLUTELY NO mathematical subprocess' in body,'process boundary missing')
require('EXPLICIT CONDITIONAL TABLE' in body,'table boundary missing')
with (P/'preflight.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_parser':'ops/lane.sh sed -n s/^charged_input=//p','vector':actual,'unique_basenames':True,'literal_placeholder':True,'current_source_snapshot_pins':True,'conditional_table_preserved':True,'mathematical_subprocesses':0,'launched':False},f,indent=2)
prompt.chmod(0o444)
cap=json.loads((P/'capability.json').read_bytes());out=[]
require(Path(cap['partial_path']).read_bytes().endswith(b'<!-- BODY-END -->\n'),'body incomplete')
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25);require(r.returncode==0,op+': '+r.stdout.decode()+r.stderr.decode());out.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('x') as f:json.dump(out,f,indent=2)
paths=[p for p in P.rglob('*') if p.is_file() and p.name!='capability.json']+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
entries=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(paths)]
cust={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'/root/nonemptiness_certificate','status':'TERMINAL_PREP_ONLY_READY_FOR_ROOT_NOT_LAUNCHED','writers':'ALL IDLE after this exclusive metadata write','entries':entries,'inputs':pins['entries'],'contact_cover_status':'EXPLICIT CONDITIONAL TABLE ONLY','mathematical_subprocesses':0,'proof_changes':False,'review_absolute_deadline':'root invitation only','remote_agents_launches':0}
with (P/'custody.json').open('x') as f:json.dump(cust,f,indent=2)
for e in entries:require(sha(R/e['path'])==e['sha256'],'owned drift')
for e in pins['entries']:require(sha(R/e['source'])==e['sha256'],'post source drift')
print(json.dumps({'utc':cust['utc'],'report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'prompt_sha256':sha(prompt),'pins_sha256':sha(P/'FINAL-PINS.json'),'qualification_sha256':sha(qualification),'preflight_sha256':sha(P/'preflight.json'),'charged':len(actual),'owned':len(entries),'writers':'IDLE','launched':False},indent=2))
