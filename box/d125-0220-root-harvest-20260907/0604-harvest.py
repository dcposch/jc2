"""Root terminal custody and bounded controls; no full-source arithmetic."""
import sys
sys.dont_write_bytecode = True
import hashlib, json, resource, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
B=ROOT/'box/d125-0220-root-harvest-20260907'
def need(ok,msg):
    if not ok: raise ValueError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
pins={
 'box/d125-uniform-ramification-discriminator-20260907/custody.json':'957d7573988f136a8f9ce40bec92953568a49f3f59efb1aa9fab173ef3746681',
 'box/d125-hybrid-affine-first-attempt-20260907/pins.json':'c9e353f57d755c929841b285311a1a94c6adb2f8a62bb05e022f835587dd920e',
 'xmodel/d125-hybrid-affine-first-attempt-astra-20260907.md':'0ed7aae7ad1fa06a1d241f4155a794f20e7793daffe117c36d9a5273ab211bac',
 'xmodel/d125-hybrid-affine-first-attempt-astra-20260907.md.artifact.json':'544bb3ad95507e31ed3c04a0325f5577f8c314ef683f9aebd65c6cb2f4e96fe4',
 'box/d125-0220-root-harvest-20260907/m4-generic-gate-harvest.json':'b425fcc3d930afd5c765fe648a0882fcca1f4a14dc7e20769b891e1ed851662c',
}
for p,h in pins.items(): need(sha(ROOT/p)==h,'outer pin '+p)
c=json.loads((ROOT/'box/d125-uniform-ramification-discriminator-20260907/custody.json').read_bytes())
need(c['status']=='TERMINAL' and c['all_writers_finished'] and not c['live_jobs'],'uniform custody')
for r in c['inputs']+c['owned']:
    need((ROOT/r['path']).stat().st_size==r['bytes'],'size '+r['path']); pins[r['path']]=r['sha256']
pins.update(json.loads((ROOT/'box/d125-hybrid-affine-first-attempt-20260907/pins.json').read_bytes())['files'])
for p,h in pins.items(): need(sha(ROOT/p)==h,'pre pin '+p)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
runs=[]; start=time.monotonic()
def run(argv,negative=None,expected=None):
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,timeout=30,preexec_fn=caps)
    need((p.returncode!=0)==bool(negative),'unexpected exit '+str(argv))
    if negative: need(negative in p.stderr,'wrong negative gate')
    if expected: need(hashlib.sha256(p.stdout).hexdigest()==expected,'positive output drift')
    runs.append(dict(argv=argv,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
for tag in ('d125-uniform-ramification-discriminator-astra-20260907','d125-hybrid-affine-first-attempt-astra-20260907'):
    run([sys.executable,'-B','ops/artifact_finalize.py','verify','--final','xmodel/'+tag+'.md'])
for opt in ([],['-O']):
    base=[sys.executable,'-B']+opt
    for mut,msg in [('',None),('--mutate-moving-term',b'moving remainder identity'),('--mutate-double-factor',b'mixed cubic double-pole factor'),('--mutate-omit-low-lift',b'both negative lift rows'),('--mutate-origin-bound',b'origin and infinity force')]:
        run(base+['box/d125-uniform-ramification-discriminator-20260907/check.py']+([mut] if mut else []),msg,None if mut else '53669df2e4c5b79023b466d53d484140fa0eaac87e643a53fad197419e431f44')
    run(base+['box/d125-hybrid-affine-first-attempt-20260907/verify_production.py'])
for p,h in pins.items(): need(sha(ROOT/p)==h,'post pin '+p)
result=dict(status='PASS_TERMINAL_UNIFORM_AND_HYBRID_CUSTODY',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-start,scope='uniform tiny controls; hybrid compact terminal custody only; no full source arithmetic, no independent mathematical promotion')
with (B/'0604-harvest.json').open('x') as f: json.dump(result,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps(dict(status=result['status'],pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(B/'0604-harvest.json'))))
