import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,subprocess,datetime,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
ROOT=Path('/home/ubuntu/jc2');OWN=ROOT/'box/ideation-20260908T0200Z-cross-astra'
FINAL=ROOT/'xmodel/ideation-20260908T0200Z-cross-astra.md'
PART=ROOT/'xmodel/.ideation-20260908T0200Z-cross-astra.md.partial-39fb011fb5a2a0ce738bbaf441443aff'
TOKEN='8c09da0bff2ee65d1f335f40376d86fc20e547a16e6dc50790368b4569fb4556'
def need(x,m):
    if not x:raise RuntimeError(m)
def pin(p):
    b=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def out(p,x):
    with p.open('xb') as f:f.write((json.dumps(x,sort_keys=True,indent=2)+'\n').encode())
harvest=ROOT/'box/d125-0220-root-harvest-20260907/0240-round-blind-harvest.json'
need(pin(harvest)['sha256']=='175ff7449246b747e8f17acbd260a82ea6aa9b824b966f5b95228b5a0ad43ad4','collection receipt unchanged')
hp=json.loads(harvest.read_bytes())['pins']
names=['xmodel/ideation-20260908T0200Z-'+s+'.md' for s in ('coordinator','astra','fable5','sol56')]
names+=['box/ideation-20260908T0200Z/packet.md','box/ideation-20260908T0200Z/MANIFEST.json']
names+=['box/ideation-20260908T0200Z/snapshots/'+s for s in ('d125-minimal-monomial-receiver-composition-astra-20260906.md','d125-golden-divisibility-control-astra-20260908.md','d125-common-to-unequal-interface-discriminator-astra-20260908.md')]
for n in names:need(pin(ROOT/n)['sha256']==hp[n],'frozen input '+n)
out(OWN/'input-pins.json',{'inputs':[pin(ROOT/n) for n in names]+[pin(harvest)],'read_scope':'all four full blind reports after original hash verification; named original frozen support/controls, no independent unreleased uniform proof','post_cutoff':'Root supplied15i accepted field-point unequal/Q scope, not used as a mathematical premise of golden certificate','no_live_peer_reads':True})
b=PART.read_bytes();need(b.count(b'<!-- BODY-END -->')==1 and b.endswith(b'<!-- BODY-END -->\n'),'body-end')
need(len(b.split())<=1600,'word cap including exact math')
commands=[]
for op in ('close','finalize','verify'):
    args=['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),op,'--final',str(FINAL)]
    if op!='verify':args+=['--token',TOKEN]
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,cwd=ROOT)
    commands.append({'operation':op,'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
    need(p.returncode==0,'publication '+op)
out(OWN/'publication.json',{'status':'VERIFIED','commands':commands,'report':pin(FINAL),'transaction':pin(Path(str(FINAL)+'.artifact.json'))})
owned=sorted(p for p in OWN.iterdir() if p.is_file() and p.name!='custody.json')
entries=[pin(p) for p in owned]+[pin(FINAL),pin(Path(str(FINAL)+'.artifact.json'))]
out(OWN/'custody.json',{'status':'TERMINAL','owner':'/root/nonemptiness_certificate','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_writers_idle_at_handoff':True,'last_writer':'this exclusive metadata process; no background writers','entries':entries,'inputs_file':'input-pins.json','scope':'cross-reconciliation plus seven projected coefficient implications; no source-stratum promotion','worker_actions':[]})
print(json.dumps({'status':'TERMINAL','report':pin(FINAL),'transaction':pin(Path(str(FINAL)+'.artifact.json')),'custody':pin(OWN/'custody.json'),'entries':len(entries)},sort_keys=True))
