import sys
sys.dont_write_bytecode = True
import os, json, hashlib, subprocess, datetime, resource, urllib.request
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU, (25,25))
resource.setrlimit(resource.RLIMIT_AS, (536870912,536870912))
R=Path('/home/ubuntu/jc2'); P=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
url='https://arxiv.org/pdf/math/0408077v1'
with urllib.request.urlopen(url,timeout=12) as response:
    raw=response.read()
if not raw.startswith(b'%PDF'): raise RuntimeError('not PDF')
with (P/'chau-0408077v1.pdf').open('xb') as f: f.write(raw)
subprocess.run(['pdftotext','-layout',str(P/'chau-0408077v1.pdf'),str(P/'chau-0408077v1.txt')],check=True,timeout=10)
inputs=[]
for name in ['ggv-1401.1784v3.pdf','ggv-1401.1784v3.txt','gghv-1708.07936v1.pdf','gghv-1708.07936v1.txt','makar-limanov-serdica-2025.pdf','makar-limanov-serdica-2025.txt','chau-0408077v1.pdf','chau-0408077v1.txt']:
    q=P/name; inputs.append({'path':str(q.relative_to(R)),'sha256':sha(q),'bytes':q.stat().st_size})
for rel in ['ops/artifact_finalize.py','ops/open_collision.py']:
    q=R/rel; inputs.append({'path':rel,'sha256':sha(q),'bytes':q.stat().st_size})
with (P/'input-pins.json').open('x') as f: json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'additional_primary_url':url,'entries':inputs},f,indent=2)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/f2-fixed-degree-standardization-gate-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=10,check=True)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f: f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'chau_pdf_sha256':sha(P/'chau-0408077v1.pdf'),'chau_text_sha256':sha(P/'chau-0408077v1.txt'),'input_pins_sha256':sha(P/'input-pins.json')}))
