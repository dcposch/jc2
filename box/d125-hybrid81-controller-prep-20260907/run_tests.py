"""Tiny local mock-only replay receipt; no AWS, engine or authority."""
from pathlib import Path
import hashlib,json,subprocess,time
R=Path(__file__).resolve().parent;rows=[]
for flags in ([],['-O']):
 cmd=['timeout','30s','prlimit','--cpu=25:25','--as=536870912:536870912','--fsize=67108864:67108864','--core=0:0','--','/usr/bin/python3','-I','-B']+flags+[str(R/'test_controller.py')]
 start=time.monotonic();p=subprocess.run(cmd,capture_output=True,timeout=35)
 rows.append({'argv':cmd,'rc':p.returncode,'elapsed_seconds':time.monotonic()-start,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
 if p.returncode!=0 or p.stderr:raise RuntimeError('mock replay failed')
with (R/'test-results.json').open('x') as f:json.dump(rows,f,indent=2,sort_keys=True);f.write('\n')
paths=[p for p in R.iterdir() if p.is_file()]
pins={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths}
custody={'schema':'jc2.controller-prep/v1','scope':'LOCAL_MOCK_PREP_ONLY','authority_issued':False,'remote_access':False,'source_access':False,'engine_executed':False,'all_children_terminal':True,'files':pins}
with (R/'custody.json').open('x') as f:json.dump(custody,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'status':'PREP_TESTS_PASS','pins':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ('controller.py','test-results.json','custody.json')}},indent=2))
