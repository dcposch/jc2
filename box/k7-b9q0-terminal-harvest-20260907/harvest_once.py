"""Capture terminal receipts and byte-copy bounded K7 artifacts; no arithmetic."""
import concurrent.futures,hashlib,json,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
SSH=['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','ConnectTimeout=8','-o','BatchMode=yes','-o','StrictHostKeyChecking=no','-o','UserKnownHostsFile=/dev/null','ubuntu@172.30.0.73']
SCP=['scp','-i','/home/ubuntu/.ssh/jc2-fleet','-o','ConnectTimeout=8','-o','BatchMode=yes','-o','StrictHostKeyChecking=no','-o','UserKnownHostsFile=/dev/null']
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
need(not (HERE/'terminal.json').exists(),'terminal capture already exists')
start=time.monotonic()
p=subprocess.run(SSH+['python3','-'],input=(HERE/'collect_terminal.py').read_bytes(),capture_output=True,timeout=55)
if p.returncode==75:
    print(p.stdout.decode(),end='');sys.exit(75)
need(p.returncode==0,'remote collector failed: '+p.stderr.decode())
c=json.loads(p.stdout);need(c['status']=='TERMINAL_CUSTODY_ONLY','terminal type')
with (HERE/'terminal.json').open('xb') as f:f.write(p.stdout)
with (HERE/'collector-stderr.txt').open('xb') as f:f.write(p.stderr)
E=HERE/'evidence';E.mkdir(exist_ok=False)
items=list(c['files'].items())
for rel,meta in items:
    path=Path(rel);need(not path.is_absolute() and '..' not in path.parts,'relative path')
    need(meta['bytes']<=64<<20,'bounded copy')
    (E/path).parent.mkdir(parents=True,exist_ok=True)
def copy(item):
    rel,meta=item;dest=E/rel
    need(not dest.exists(),'exclusive target '+rel)
    r=subprocess.run(SCP+['ubuntu@172.30.0.73:'+c['root']+'/'+rel,str(dest)],capture_output=True,timeout=55)
    need(r.returncode==0,'copy '+rel+': '+r.stderr.decode())
    need(dest.stat().st_size==meta['bytes'] and sha(dest)==meta['sha256'],'copy pin '+rel)
    return dict(path=rel,bytes=meta['bytes'],sha256=meta['sha256'])
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    copies=list(pool.map(copy,items))
result=dict(status='TERMINAL_COPIES_VERIFIED',terminal_sha256=sha(HERE/'terminal.json'),
    collector_sha256=sha(HERE/'collect_terminal.py'),copies=copies,
    wall_seconds=time.monotonic()-start,no_CAS_or_extra_arithmetic=True,no_worker_control=True)
with (HERE/'copy-receipt.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=result['status'],files=len(copies),bytes=sum(x['bytes'] for x in copies),wall_seconds=result['wall_seconds'],terminal_sha256=result['terminal_sha256'],copy_receipt_sha256=sha(HERE/'copy-receipt.json'))))
