import sys
sys.dont_write_bytecode=True
import os,json,subprocess
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
lease=ROOT/'xmodel/.websweep-20260908T2212Z-astra.md.artifact-lease.json'
t=json.loads(lease.read_bytes()); partial=lease.parent/t['partial_name']
if partial.stat().st_size:raise RuntimeError('refuse recovery of a nonempty report')
os.rename(partial,P/'initial-empty-partial');os.rename(lease,P/'initial-abandoned-lease.json')
cmd=['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),'begin','--final',str(ROOT/'xmodel/websweep-20260908T2212Z-astra.md'),'--basis',t['basis'],'--owner','/root/nonemptiness_certificate']
r=subprocess.run(cmd,check=True,capture_output=True);data=json.loads(r.stdout)
fd=os.open(P/'transaction-capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({k:v for k,v in data.items() if k!='token'}))
