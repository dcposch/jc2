import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,os,datetime
from pathlib import Path
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prompt=R/'box/ideation-20260908T2220Z/cross-astra.prompt.md'
if sha(prompt)!='ff3825366b639c984d5ff08679d8851442af2e0b59b7d8f67af523bdbef2c4af':raise RuntimeError('prompt drift')
old=json.loads((R/'box/ideation-20260908T2220Z/PINS.json').read_bytes());post=json.loads((R/'box/ideation-20260908T2220Z-poststate/PINS.json').read_bytes());known=dict(old)
for e in post['entries']:known[e['snapshot']]=e['snapshot_sha256']
col=json.loads((R/'box/ideation-20260908T2220Z-collection/collection.json').read_bytes())
for e in col['external'].values():known[e['fields']['report']]=e['fields']['report_sha256']
for e in col['local'].values():known[e['report_path']]=e['report_sha256']
known['box/ideation-20260908T2220Z-collection/collection.json']='0d4376fb2f89451ac093260b91e40be9befa08e43b0ea1461aa19698409b2dc9'
rows=[]
for line in prompt.read_text().splitlines():
 if line.startswith('charged_input='):
  path=line.split('=',1)[1];h=sha(R/path)
  if path in known and h!=known[path]:raise RuntimeError('pin mismatch '+path)
  rows.append({'path':path,'sha256':h,'bytes':(R/path).stat().st_size,'independent_expected_pin':path in known})
if len(rows)!=23:raise RuntimeError('vector count')
with (P/'input-pins.json').open('xb') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prompt_sha256':sha(prompt),'entries':rows},indent=2).encode())
b=json.loads((R/'box/ideation-20260908T2220Z/MANIFEST.json').read_bytes())['basis']
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/ideation-20260908T2220Z-cross-astra.md'),'--basis',b,'--owner','/root/nonemptiness_certificate'],capture_output=True,check=True,timeout=25)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
d=json.loads(r.stdout);print(json.dumps({'status':'PASS','input_count':len(rows),'partial':d['partial_path']}))
