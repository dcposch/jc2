#!/usr/bin/env python3
"""Tiny controls plus exact runner orphan check, locally or on owned worker."""
import hashlib,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
remote=sys.argv[1]=='remote'
base=HERE/('remote-controls' if remote else 'local-controls');base.mkdir()
if remote:
    import payload
    payload.identity()
    runner=HERE/'run_capped.py';tests=HERE/'test_exporter.py'
else:
    repo=HERE.parent.parent
    runner=repo/'box/full-j-solver-pilot-20260906/evidence/run_capped.py'
    tests=repo/'box/d125-physical-exporter-20260906/test_exporter.py'
if hashlib.sha256(runner.read_bytes()).hexdigest()!='4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2':raise SystemExit('runner drift')
results={}
for name,flags in [('normal',[]),('optimized',['-O'])]:
    p=subprocess.run([sys.executable,*flags,str(tests),str(base/name)],capture_output=True,text=True,timeout=29)
    (base/(name+'.stdout')).write_text(p.stdout);(base/(name+'.stderr')).write_text(p.stderr)
    if p.returncode:raise RuntimeError(p.stderr)
    results[name]=json.loads(p.stdout)
orphan=base/'orphan';orphan.mkdir()
argv=[sys.executable,str(runner),'--wall-seconds','0.5','--rss-bytes',str(512*1024**2),
 '--term-grace-seconds','0.1','--cwd',str(orphan),'--stdout-file',str(orphan/'stdout'),
 '--stderr-file',str(orphan/'stderr'),'--telemetry-file',str(orphan/'telemetry.json'),
 '--',sys.executable,str(HERE/'orphan_control.py')]
p=subprocess.run(argv,capture_output=True,text=True,timeout=10)
(orphan/'runner.stdout').write_text(p.stdout);(orphan/'runner.stderr').write_text(p.stderr)
t=json.loads((orphan/'telemetry.json').read_text())
if not (p.returncode==124 and t['status']=='WALL_TIMEOUT' and t['child_returncode']==0 and
        t['termination']['term_sent'] and t['termination']['kill_sent'] and
        t['termination']['cleanup_complete'] and t['termination']['leader_reaped']):raise RuntimeError(t)
group=[]
for line in subprocess.check_output(['ps','-eo','pid=,pgid=,stat='],text=True).splitlines():
    pid,pgid,status=line.split()
    if int(pgid)==t['pgid'] and not status.startswith('Z'):group.append(int(pid))
if group:raise RuntimeError(('orphan group still live',group))
results['orphan']={'returncode':p.returncode,'telemetry':t,'live_group_after':group}
results['status']='PASS';results['remote']=remote
with (base/'result.json').open('x') as f:json.dump(results,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','remote':remote,'orphan_pgid':t['pgid'],
                  'normal_mutations':len(results['normal']['mutation_rejections']),
                  'optimized_mutations':len(results['optimized']['mutation_rejections'])},sort_keys=True))
