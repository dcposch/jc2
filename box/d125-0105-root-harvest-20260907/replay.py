"""Bounded root replay of the terminal zero-lambda gate; no CAS or remote I/O."""
import ast, hashlib, json, os, resource, signal, subprocess, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
signal.alarm(30)
PINS={
 'xmodel/d125-zero-lambda-gate-fable5-20260907.md':'33cb032a5d7f52cb12bd9122032ff5336499c3e67b9e650aa2c3c211935dd607',
 'xmodel/d125-zero-lambda-obstruction-astra-20260907.md':'a878a87bdeae772cc66d19ea817d43184882c649769c61d5babb47292d339d3a',
 'box/d125-zero-lambda-obstruction-20260907/check.py':'f0c9acb295d0ff8c1c2dcf8818c705174a04eb3e6d0386c93f2d7675c3c5f425',
 'xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md':'433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
 'xmodel/d125-small-polynomial-lift-gate-fable5-20260906.md':'4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122',
 'FALLACY-v2.md':'e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5',
 'box/d125-zero-lambda-gate-fable5-20260907/gate_controls.py':'51644061231de9dca784df0fa9a3735f12292d569f5a9740be0024a47bc1c12e'}
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def pins():
    for rel,sha in PINS.items():
        data=(ROOT/rel).read_bytes()
        need(hashlib.sha256(data).hexdigest()==sha,'pin drift '+rel)
        if rel.endswith('.py'):
            need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(data))),'removable assert '+rel)
pins(); start=time.monotonic(); results=[]
for mode in ([],['-O']):
    for mutation in (None,'--mutate-sign','--mutate-map','--mutate-det','--mutate-drop'):
        argv=[sys.executable,'-I','-B',*mode,str(ROOT/'box/d125-zero-lambda-gate-fable5-20260907/gate_controls.py')]
        if mutation: argv.append(mutation)
        p=subprocess.run(argv,capture_output=True,text=True,timeout=max(1,29-(time.monotonic()-start)),env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        need(p.returncode==(1 if mutation else 0),'wrong return code '+str(argv))
        need(('STATUS PASS controls=7' in p.stdout) if not mutation else ('Fail:' in p.stderr),'missing actual control outcome')
        results.append({'argv':argv,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
pins()
out={'pass':True,'pins':PINS,'ast_assert_count':0,'runs':results,'wall_seconds':time.monotonic()-start,'child_usage':list(resource.getrusage(resource.RUSAGE_CHILDREN))}
with (HERE/'zero-lambda-results.json').open('x') as f: json.dump(out,f,sort_keys=True); f.write('\n')
print(json.dumps({'pass':True,'runs':len(results),'wall_seconds':out['wall_seconds'],'result_sha256':hashlib.sha256((HERE/'zero-lambda-results.json').read_bytes()).hexdigest()}))
