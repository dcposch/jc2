import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,subprocess,datetime,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');A=R/'box/d125-golden-j12-attachment-gate-20260908';B=R/'box/d125-golden-eight-parameter-gate-prep-20260908'
def need(x,m):
    if not x:raise RuntimeError(m)
def pin(p):
    b=p.read_bytes();return {'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def out(p,x):
    with p.open('xb') as f:f.write((json.dumps(x,sort_keys=True,indent=2)+'\n').encode())
receipt=R/'box/d125-0220-root-harvest-20260907/0256-round-cross-harvest.json'
need(pin(receipt)['sha256']=='919b2dac833371fabac914c3266f43e01bbdc8b6bf819aa1c90297434944ed4e','receipt pin')
known=json.loads(receipt.read_bytes())['pins']
inputs=['xmodel/ideation-20260908T0200Z-fable5.md','xmodel/ideation-20260908T0200Z-cross-fable5.md']
inputs+=['box/ideation-20260908T0200Z/snapshots/'+n for n in ('d125-minimal-monomial-receiver-composition-astra-20260906.md','d125-golden-divisibility-control-astra-20260908.md','d125-cone-first-contact-source-astra-20260908.md')]
for n in inputs:need(pin(R/n)['sha256']==known[n],'input changed '+n)
out(A/'input-pins.json',{'inputs':[pin(R/n) for n in inputs]+[pin(receipt)],'whole_reports_read':True,'scope':'conditional odd-j12 attachment; no ansatz exclusion as premise; no live/unreleased peers'})
pairs=[('xmodel/ideation-20260908T0200Z-cross-astra.md','ansatz-proof.md'),('box/ideation-20260908T0200Z-cross-astra/check.py','ansatz-check.py'),('box/ideation-20260908T0200Z-cross-astra/replay.json','ansatz-replay.json'),('box/ideation-20260908T0200Z-cross-astra/witness.json','ansatz-witness.json'),('box/ideation-20260908T0200Z-cross-astra/custody.json','ansatz-custody.json'),('xmodel/ideation-20260908T0200Z-cross-astra.md.artifact.json','ansatz-transaction.json'),('box/ideation-20260908T0200Z/snapshots/d125-golden-divisibility-control-astra-20260908.md','golden-factor-control.md'),('box/ideation-20260908T0200Z/snapshots/d125-minimal-monomial-receiver-composition-astra-20260906.md','minimal-receiver.md'),('box/d125-0220-root-harvest-20260907/0256-round-cross-harvest.json','root-cross-harvest.json')]
(B/'snapshots').mkdir()
rows=[]
for src,name in pairs:
    p=R/src
    if src in known:need(pin(p)['sha256']==known[src],'snapshot source changed '+src)
    q=B/'snapshots'/name
    with q.open('xb') as f:f.write(p.read_bytes())
    q.chmod(0o444);need(pin(q)['sha256']==pin(p)['sha256'],'literal bytes')
    rows.append({'source':pin(p),'snapshot':pin(q)})
out(B/'PINS.json',{'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PREP ONLY; root launches','inputs':rows,'j12_attachment_charged':False})
p=subprocess.run(['sed','-n','s/^charged_input=//p',str(B/'prompt.md')],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
need(p.returncode==0,'actual parser')
paths=p.stdout.decode().splitlines();need(len(paths)==10 and len(set(Path(x).name for x in paths))==10,'unique exact ten')
need('{{LANE_INPUTS}}' in (B/'prompt.md').read_text(),'literal placeholder')
for n in paths:need((R/n).is_file(),'missing charged input')
out(B/'parser-replay.json',{'status':'PASS','parser':'ops/lane.sh literal sed extraction','paths':paths,'pins':[pin(R/n) for n in paths]})
tasks=[(A,'xmodel/d125-golden-j12-attachment-gate-astra-20260908.md','6d4f3ab7a47c1fd98a30c5a19e6cf0dec03cb863e7a72ed9294e5cff93f0f944'),(B,'xmodel/d125-golden-eight-parameter-gate-prep-astra-20260908.md','64702d0f02085d711abbe8bc500465dd9158df52daad3821a583a4eb3aecd21e')]
result=[]
for own,name,token in tasks:
    final=R/name;commands=[]
    for op in ('close','finalize','verify'):
        a=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',str(final)]
        if op!='verify':a+=['--token',token]
        q=subprocess.run(a,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,cwd=R)
        commands.append({'operation':op,'rc':q.returncode,'stdout':q.stdout.decode(),'stderr':q.stderr.decode()});need(q.returncode==0,'publication '+op)
    out(own/'publication.json',{'status':'VERIFIED','commands':commands,'report':pin(final),'transaction':pin(Path(str(final)+'.artifact.json'))})
    files=sorted(p for p in own.rglob('*') if p.is_file() and p.name!='custody.json')
    entries=[pin(p) for p in files]+[pin(final),pin(Path(str(final)+'.artifact.json'))]
    out(own/'custody.json',{'status':'TERMINAL','owner':'/root/nonemptiness_certificate','entries':entries,'all_writers_idle_at_handoff':True,'last_writer':'this exclusive metadata process; no background writers','no_launch':True,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    result.append({'report':pin(final),'transaction':pin(Path(str(final)+'.artifact.json')),'custody':pin(own/'custody.json'),'entries':len(entries)})
print(json.dumps({'status':'TERMINAL','artifacts':result,'prompt':pin(B/'prompt.md'),'PINS':pin(B/'PINS.json')},sort_keys=True))
