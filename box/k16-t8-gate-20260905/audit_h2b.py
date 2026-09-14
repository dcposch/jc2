#!/usr/bin/env python3
"""Inspect a completed, harvested F4 job; preserve timeout/error as inconclusive."""
from pathlib import Path
import hashlib,json,re
D=Path(__file__).resolve().parent
W=D/'worker'
status=dict(line.split('=',1) for line in (W/'h2b.status').read_text().splitlines())
log=(W/'h2b.log').read_text()
remote=dict(line.split(maxsplit=1)[::-1] for line in (W/'h2b.remote.sha256').read_text().splitlines())
expected='8be78590cbd8ab8edba4097372f3978986c18e9aa8c0b17da8066ed8f796a8d4'
assert hashlib.sha256((W/'affinew_p32027.ms').read_bytes()).hexdigest()==expected
assert remote['affinew_p32027.ms']==expected
assert remote['/usr/local/bin/msolve']=='0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f'
assert status['threads']=='32' and status['watchdog_seconds']=='10200'
assert re.search(r'#invalid equations\s+0\b',log)
assert re.search(r'field characteristic\s+32027\b',log)
assert re.search(r'#variables\s+6\b',log) and re.search(r'#equations\s+28\b',log)
out={'status':status,'input_sha256':expected,'outcome':'INCONCLUSIVE','artifact_sha256':{}}
if (W/'h2b.gb').exists():
 gb=(W/'h2b.gb').read_text()
 body='\n'.join(line for line in gb.splitlines() if not line.startswith('#')).strip()
 out['gb_body']=body
 out['gb_unit']=(body=='[1]:')
 if status['exit']=='0' and out['gb_unit']:
  assert '#length of basis:      1 element' in gb
  assert '#field characteristic: 32027' in gb
  assert '#variable order:       q2, q3, q4, q5, q6, q7' in gb
  assert 'No solution' in log
  assert re.search(r'size of basis\s+1\b',log)
  assert not re.search(r'\b(?:ERROR|Error|Killed|Segmentation fault)\b',log)
  out['outcome']='UNIT_IDEAL_CONFIRMED'
for k,pat in {
 'elapsed_seconds':r'overall\(elapsed\)\s+([0-9.]+) sec',
 'cpu_seconds':r'overall\(cpu\)\s+([0-9.]+) sec',
 'pairs_reduced':r'#pairs reduced\s+(\d+)',
 'rows_reduced':r'#rows reduced\s+(\d+)',
 'max_matrix':r'max\. matrix data\s+([^\n]+)',
}.items():
 m=re.search(pat,log)
 if m: out[k]=m[1].strip()
degrees=[int(m[1]) for m in re.finditer(r'^\s*(\d+)\s+\d+\s+\d+\s+\d+ x \d+',log,re.M)]
out['deepest_degree']=max(degrees) if degrees else None
for n in ['h2b.status','h2b.log','h2b.time','h2b.gb','h2b.remote.sha256','run_h2b.sh']:
 p=W/n
 if p.exists():out['artifact_sha256'][n]=hashlib.sha256(p.read_bytes()).hexdigest()
(D/'h2b-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
