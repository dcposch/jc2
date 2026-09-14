import sys
sys.dont_write_bytecode=True
import json,subprocess,os
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
b=json.loads((ROOT/'box/ideation-20260908T2220Z/MANIFEST.json').read_bytes())['basis']
r=subprocess.run(['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),'begin','--final',str(ROOT/'xmodel/ideation-20260908T2220Z-collection-astra.md'),'--basis',b,'--owner','/root/nonemptiness_certificate'],capture_output=True,check=True,timeout=25)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
d=json.loads(r.stdout);print(json.dumps({k:v for k,v in d.items() if k!='token'}))
