"""Single <=30s/25CPU/512MiB local producer+delta batch; no CAS/remote calls."""
import json,os,resource,signal,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
signal.alarm(30);start=time.monotonic();results=[]
commands=[[sys.executable,'-B','run_tests.py','producer-tests.json']]+[
    [sys.executable,'-B',*mode,'delta_tests.py'] for mode in ([],['-O'])]
for argv in commands:
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True,timeout=max(1,29-(time.monotonic()-start)),
                     env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
    results.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:break
report={'pass':len(results)==3 and all(r['returncode']==0 for r in results),'results':results,
        'wall_seconds':time.monotonic()-start,'child_usage':list(resource.getrusage(resource.RUSAGE_CHILDREN))}
with (ROOT/'delta-results.json').open('x') as out:json.dump(report,out,sort_keys=True);out.write('\n')
print(json.dumps(report,sort_keys=True));raise SystemExit(0 if report['pass'] else 1)
