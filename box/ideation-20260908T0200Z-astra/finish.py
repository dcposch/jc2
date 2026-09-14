import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,subprocess,datetime,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
ROOT=Path('/home/ubuntu/jc2')
OWN=ROOT/'box/ideation-20260908T0200Z-astra'
FINAL=ROOT/'xmodel/ideation-20260908T0200Z-astra.md'
PART=ROOT/'xmodel/.ideation-20260908T0200Z-astra.md.partial-4e56ba8198c080fc6c45b22c72b332ed'
TOKEN='fa204dd3bdfd6a09bace56a92db9cba10a85454e80250f2893cf857b903fd37c'
def need(x,m):
    if not x:raise RuntimeError(m)
def pin(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def out(p,x):
    with p.open('xb') as f:f.write((json.dumps(x,sort_keys=True,indent=2)+'\n').encode())
prompt=ROOT/'box/ideation-20260908T0200Z/astra.prompt.md'
paths=[ROOT/x.split('=',1)[1] for x in prompt.read_text().splitlines() if x.startswith('charged_input=')]
need(len(paths)==26 and len(set(paths))==26,'exact common26')
manifest=json.loads((ROOT/'box/ideation-20260908T0200Z/MANIFEST.json').read_bytes())
for r in manifest['inputs']:
    p=ROOT/r['snapshot']; q=pin(p)
    need(q['sha256']==r['sha256'] and q['bytes']==r['bytes'],'snapshot drift '+r['snapshot'])
need(pin(ROOT/'box/ideation-20260908T0200Z/packet.md')['sha256']=='5bcaed3a6256033a6bc7eeff178f40ba48d2233e807fa3d29615e649a5fe7458','packet pin')
need(pin(ROOT/'box/ideation-20260908T0200Z/MANIFEST.json')['sha256']=='8f80df66fe367f4926752e3a106d224bd48aa6855d0e4c99f92bad247cb551b2','manifest pin')
b=PART.read_bytes()
need(b.count(b'<!-- BODY-END -->')==1 and b.endswith(b'<!-- BODY-END -->\n'),'body completion')
need(len(b.split())<2800,'word cap')
need(b.count(b'## Card')==2,'two cards')
out(OWN/'input-pins.json',{'inputs':[pin(p) for p in paths],'binding_prompt':pin(prompt),'mutable_sources_read_in_blind':False,'peer_reports_read':False,'read_scope':'Whole required common reports and all46-ID mastermap; full AUDIT supplied for named history lookup, not read cover-to-cover; primary read scope in primary-receipt.json.'})
commands=[]
for operation in ('close','finalize','verify'):
    args=['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),operation,'--final',str(FINAL)]
    if operation!='verify':args+=['--token',TOKEN]
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,cwd=ROOT)
    commands.append({'operation':operation,'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
    need(p.returncode==0,'artifact '+operation)
out(OWN/'publication.json',{'status':'VERIFIED','commands':commands,'report':pin(FINAL),'transaction':pin(Path(str(FINAL)+'.artifact.json'))})
owned=sorted(p for p in OWN.iterdir() if p.is_file() and p.name!='custody.json')
entries=[pin(p) for p in owned]+[pin(FINAL),pin(Path(str(FINAL)+'.artifact.json'))]
out(OWN/'custody.json',{'status':'TERMINAL','owner':'/root/nonemptiness_certificate','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_writers_idle_at_handoff':True,'last_writer':'this exclusive metadata process; no background writer','authority':'independent blind ideation only; no launch/promotion','entries':entries,'inputs_file':'input-pins.json','artifact_helpers':[pin(ROOT/'ops/artifact_finalize.py'),pin(ROOT/'ops/seal.py')],'no_live_peer_reads':True,'worker_actions':[]})
print(json.dumps({'status':'TERMINAL','report':pin(FINAL),'transaction':pin(Path(str(FINAL)+'.artifact.json')),'custody':pin(OWN/'custody.json'),'inputs':len(paths),'owned_entries':len(entries),'body_words_by_whitespace':len(b.split())},sort_keys=True))
