"""Current custody plus bounded exact producer controls; never --record."""
import datetime,hashlib,json,resource,subprocess,time
from pathlib import Path
R=Path('/home/ubuntu/jc2'); B=R/'box/d125-pure-critical-remainder-20260907'
start=time.monotonic()
def need(c,m):
    if not c: raise RuntimeError(m)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(B/'custody.json')=='c544c7ea7171517b60d7423a82f4affd7ec84baa9d45f6b67b552104c7685b60','custody drift')
pins={e['path']:e['sha256'] for e in json.loads((B/'custody.json').read_bytes())['entries']}
E=R/'box/d125-cross-e-coefficient-discriminator-20260907/inputs.json'
need(sha(E)=='d4ca02f5dce9ca18a0e0cb1d3ab229944765ef6e8b2d8c776206a40766f54304','notation input manifest')
pins.update(json.loads(E.read_bytes())['pins'])
pins['xmodel/d125-cross-e-coefficient-discriminator-astra-20260907.md']='5a4a824e973db003a0497e1ad14b856eb548d0510e964c9306085e9695f60a27'
for n,h in pins.items():need(sha(R/n)==h,'input drift '+n)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
runs=[]
for ref in json.loads((B/'final-replay.json').read_bytes())['runs']:
    argv=['/usr/bin/python3','-I','-B']+(['-O'] if ref['optimized'] else [])+[str(B/'check.py')]+([ref['mutation']] if ref['mutation'] else [])
    p=subprocess.run(argv,capture_output=True,timeout=30,preexec_fn=caps)
    need(p.returncode==ref['returncode'],'returncode')
    need(hashlib.sha256(p.stdout).hexdigest()==ref['stdout_sha256'],'stdout')
    need(hashlib.sha256(p.stderr).hexdigest()==ref['stderr_sha256'],'stderr')
    runs.append({**ref,'root_replayed':True})
for n,h in pins.items():need(sha(R/n)==h,'post drift '+n)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Root custody and small controls only; whole mathematical argument read separately; no independent-model promotion.'}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
