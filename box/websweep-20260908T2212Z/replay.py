import sys
sys.dont_write_bytecode=True
import subprocess,json,ast,hashlib,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
P=Path(__file__).resolve().parent;script=P/'check_c3.py';rows=[]
if any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(script.read_bytes()))):raise RuntimeError('assert prohibited')
for optimized in (False,True):
 for mode in ('normal','changed-map','changed-collision'):
  cmd=['/usr/bin/python3','-I','-B']+(['-O'] if optimized else [])+[str(script),mode]
  r=subprocess.run(cmd,capture_output=True,timeout=25)
  if (r.returncode==0)!=(mode=='normal'):raise RuntimeError('mode result mismatch '+mode)
  if mode=='changed-map' and b'determinant is not' not in r.stderr:raise RuntimeError('wrong failure')
  if mode=='changed-collision' and b'actual point fails collision' not in r.stderr:raise RuntimeError('wrong failure')
  rows.append({'optimized':optimized,'mode':mode,'returncode':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
out={'completed':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'zero_assert':True,'runs':rows,'status':'PASS'}
with (P/'replay.json').open('xb') as f:f.write(json.dumps(out,indent=2).encode())
print(json.dumps({'status':'PASS','runs':len(rows),'zero_assert':True,'checker_sha256':out['checker_sha256']}))
