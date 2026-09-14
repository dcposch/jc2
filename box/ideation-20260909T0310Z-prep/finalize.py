import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,datetime,resource,re
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(c,m):
 if not c:raise RuntimeError(m)
m=json.loads((B/'MANIFEST.json').read_bytes());oldpins=json.loads((B/'PINS.json').read_bytes())
for path,h in oldpins.items():need(sha(R/path)==h,'owned prefrozen drift '+path)
for e in m['entries']:
 need(sha(R/e['source'])==e['source_sha256'],'current source drift '+e['source'])
 need(sha(R/e['path'])==e['sha256'],'snapshot drift '+e['path'])
 if e['lines'] is not None:
  lines=(R/e['source']).read_bytes().splitlines(keepends=True)
  need(b''.join(lines[e['lines'][0]-1:e['lines'][1]])==(R/e['path']).read_bytes(),'literal excerpt mismatch')
for e in m['provenance_only']:need(sha(R/e['source'])==sha(R/e['path'])==e['sha256'],'provenance drift')
paths=[e['path'] for e in m['entries']]+[str((B/'MANIFEST.json').relative_to(R))]
vectors={};normalized=[]
for seat in m['core_models']:
 p=B/(seat+'.prompt.md')
 v=subprocess.run(['sed','-n','s/^charged_input=//p',str(p)],capture_output=True,timeout=25,check=True).stdout.decode().splitlines()
 need(v==paths,'ops/lane.sh vector mismatch '+seat);need(len({Path(x).name for x in v})==len(v),'basename collision')
 text=p.read_text();need('{{LANE_INPUTS}}' in text,'missing placeholder');need(not re.search(r'^charge_basis=',text,re.M),'invalid declaration')
 need('ZERO mathematical subprocesses' in text,'unequal tools')
 dest='xmodel/ideation-20260909T0310Z-'+seat+'.md';need(dest in text,'wrong destination')
 normalized.append(text.replace(dest,'REPORT_TARGET'));vectors[seat]=v
need(len(set(normalized))==1,'prompts differ beyond exact destination')
table=(B/'snapshots/master46-history.md').read_text()
ids=[int(x) for x in re.findall(r'^\|\s*(\d+)\s*\|',table,re.M)]
need(sorted(ids)==list(range(1,47)) and len(ids)==46,'not whole46 table')
need(b'03:09' in (B/'snapshots/latest-live.md').read_bytes().splitlines()[0],'wrong LIVE')
need('The0040 full round is active' not in (B/'snapshots/approaches.md').read_text(),'stale APP active clause')
verifications=[]
for e in m['provenance_only']:
 if e['source'].endswith('.artifact.json'):
  report=e['source'][:-len('.artifact.json')]
  q=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(R/report)],capture_output=True,timeout=25)
  need(q.returncode==0,'transaction invalid '+report);verifications.append({'report':report,'result':json.loads(q.stdout)})
checks={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_parser':'sed -n s/^charged_input=//p from ops/lane.sh','vectors':vectors,'identical_beyond_destinations':True,'all46_exact':True,'unique_basenames':True,'current_source_pins':True,'literal_excerpts':True,'mathematical_subprocesses':0,'invitations':0,'transaction_verifications':verifications}
with (B/'checks.json').open('x') as f:json.dump(checks,f,indent=2)
cap=json.loads((B/'capability.json').read_bytes());need(Path(cap['partial_path']).read_bytes().endswith(b'<!-- BODY-END -->\n'),'incomplete prep body');out=[]
for op in ['close','finalize','verify']:
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 q=subprocess.run(cmd,capture_output=True,timeout=25);need(q.returncode==0,op+' failure '+q.stdout.decode()+q.stderr.decode());out.append({'operation':op,'result':json.loads(q.stdout)})
with (B/'publication.json').open('x') as f:json.dump(out,f,indent=2)
files=[p for p in B.rglob('*') if p.is_file() and p.name!='capability.json']+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
entries=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(files)]
cust={'terminal_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'/root/nonemptiness_certificate','status':'TERMINAL_PREP_ONLY_READY_FOR_ROOT_WHOLE_REVIEW','writers':'IDLE after exclusive custody write','entries':entries,'sources':m['entries'],'provenance':m['provenance_only'],'launch_authorized':False,'root_blind_seen':False,'peer_blinds_seen':False,'mathematical_subprocesses':0,'deadline_policy':'root alone sets actual common invitation after root blind seal'}
with (B/'custody.json').open('x') as f:json.dump(cust,f,indent=2)
for e in entries:need(sha(R/e['path'])==e['sha256'],'terminal drift')
print(json.dumps({'utc':cust['terminal_utc'],'report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(B/'custody.json'),'manifest_sha256':sha(B/'MANIFEST.json'),'pins_sha256':sha(B/'PINS.json'),'packet_sha256':sha(B/'packet.md'),'contract_sha256':sha(B/'contract.md'),'checks_sha256':sha(B/'checks.json'),'prompt_hashes':{s:sha(B/(s+'.prompt.md')) for s in m['core_models']},'owned':len(entries),'charged':len(paths),'writers':'IDLE','launched':False},indent=2))
