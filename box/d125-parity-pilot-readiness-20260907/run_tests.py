"""Own tiny subprocess controls only; combined wall30/CPU24, AS512MiB."""
import hashlib,json,resource,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(12,12))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
for optimized in (False,True):
    argv=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(HERE/'test_host_control.py'),'-v']
    result=subprocess.run(argv,cwd=HERE,capture_output=True,timeout=max(.1,30-(time.monotonic()-start)),preexec_fn=cap)
    runs.append(dict(argv=argv,rc=result.returncode,stdout=result.stdout.decode(),stderr=result.stderr.decode()))
    if result.returncode:break
receipt=dict(status='PASS' if len(runs)==2 and all(r['rc']==0 for r in runs) else 'FAIL',
             scope='LOCAL_MOCK_AND_TINY_ONLY_NO_PRODUCTION_NO_HOST_ACCESS',
             elapsed_seconds=time.monotonic()-start,runs=runs,
             pins={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in HERE.glob('*.py')})
target=sys.argv[1] if len(sys.argv)==2 else 'test-results.json'
if Path(target).name!=target:raise ValueError('evidence basename only')
with (HERE/target).open('x') as stream:json.dump(receipt,stream,indent=2,sort_keys=True);stream.write('\n')
print(json.dumps(receipt,sort_keys=True));sys.exit(receipt['status']!='PASS')
