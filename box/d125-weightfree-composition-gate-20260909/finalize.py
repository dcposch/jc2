import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def must(c,m):
 if not c:raise RuntimeError(m)
rows=json.loads((P/'known-inputs.json').read_bytes())['entries']+json.loads((P/'root-freeze.json').read_bytes())['entries']
must(len(rows)==9,'snapshot count')
for e in rows:
 must(sha(R/e['source'])==e['sha256'],'source drift '+e['source']);must(sha(R/e['snapshot'])==e['sha256'],'snapshot drift '+e['snapshot'])
packet=P/'packet.md';prompt=P/'fable.prompt.md'
must('DISABLED DRAFT' not in prompt.read_text(),'disabled draft not released');must(packet.is_file(),'packet absent')
pins={'schema':'jc2.weightfree-gate-pins/v1','frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof_status':'UNREVIEWED_FRAMEWORK_AND_CONSUMER_CONDITIONAL_CLIENT_MAP','packet_sha256':sha(packet),'entries':rows}
with (P/'PINS.json').open('xb') as f:f.write(json.dumps(pins,indent=2).encode())
parsed=subprocess.run(['sed','-n','s/^charged_input=//p',str(prompt)],capture_output=True,timeout=25,check=True).stdout.decode().splitlines()
expected=[str((P/'packet.md').relative_to(R)),str((P/'PINS.json').relative_to(R))]+[str((P/'inputs'/name).relative_to(R)) for name in ['framework.md','framework-transaction.json','local-consumer.md','local-consumer-transaction.json','client-interface.md','client-transaction.json','minimal-receiver.md','sufficient-lift.md','published-chain-gate.md']]
must(parsed==expected,'actual lane sed vector mismatch');must(len({Path(x).name for x in parsed})==11,'duplicate basenames');must('{{LANE_INPUTS}}' in prompt.read_text(),'placeholder absent');must(not any(x.startswith('charge_basis=') for x in prompt.read_text().splitlines()),'exit price incorrectly declared')
vector=[{'path':name,'sha256':sha(R/name),'bytes':(R/name).stat().st_size} for name in parsed]
with (P/'preflight.json').open('xb') as f:f.write(json.dumps({'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parser_argv':['sed','-n','s/^charged_input=//p',str(prompt)],'lane_parser_source':'ops/lane.sh lines257-258','lane_sha256':sha(R/'ops/lane.sh'),'prompt_sha256':sha(prompt),'vector':vector,'basenames_unique':True,'launch_performed':False},indent=2).encode())
cap=json.loads((P/'capability.json').read_bytes());results=[]
must(Path(cap['partial_path']).read_text().endswith('<!-- BODY-END -->\n'),'prep report incomplete')
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25);must(r.returncode==0,op+r.stderr.decode()+r.stdout.decode());results.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('xb') as f:f.write(json.dumps(results,indent=2).encode())
for name in parsed:(R/name).chmod(0o444)
prompt.chmod(0o444)
paths=[x for x in P.rglob('*') if x.is_file()]+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
owned=[{'path':str(x.relative_to(R)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in sorted(paths)]
cust={'owner':'/root/nonemptiness_certificate','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'TERMINAL_PREP_ONLY_ROOT_LAUNCH_AUTHORITY','writers':'ALL IDLE after this exclusive custody write; no further writes promised','entries':owned,'charged_inputs':vector,'source_snapshots':rows,'launches':0,'mathematical_subprocesses':0}
with (P/'custody.json').open('xb') as f:f.write(json.dumps(cust,indent=2).encode())
for e in owned:must(sha(R/e['path'])==e['sha256'],'owned drift')
for e in rows:must(sha(R/e['source'])==e['sha256'],'final source drift')
print(json.dumps({'status':'TERMINAL_PREP_ONLY','report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'prompt_sha256':sha(prompt),'PINS_sha256':sha(P/'PINS.json'),'preflight_sha256':sha(P/'preflight.json'),'charged_inputs':len(parsed),'owned_entries':len(owned),'utc':cust['utc']},indent=2))
