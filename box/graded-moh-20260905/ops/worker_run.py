#!/usr/bin/env python3
"""Detached, bounded solver custody; no mathematical verdict inference."""
import argparse, datetime, hashlib, json, os, pathlib, resource, subprocess, time

def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def main():
    p=argparse.ArgumentParser(); p.add_argument('spec'); a=p.parse_args()
    spec=json.loads(pathlib.Path(a.spec).read_text())
    work=pathlib.Path(spec['work']); work.mkdir(parents=True,exist_ok=True)
    status=dict(spec,start_utc=utc(),pid=os.getpid(),host=os.uname().nodename,state='RUNNING',
                input_sha256=digest(spec['input']),solver_sha256=digest(spec['command'][0]))
    def save(): (work/'status.json').write_text(json.dumps(status,indent=2)+'\n')
    save()
    def limits():
        lim=spec['memory_gib']*(1<<30)
        resource.setrlimit(resource.RLIMIT_AS,(lim,lim))
    cmd=['/usr/bin/time','-v','-o',str(work/'time.txt'),'timeout','--signal=TERM','--kill-after=20s',str(spec['timeout_seconds'])+'s',*spec['command']]
    start=time.monotonic()
    with (work/'stdout.log').open('w') as out,(work/'stderr.log').open('w') as err:
        result=subprocess.run(cmd,cwd=work,stdout=out,stderr=err,preexec_fn=limits)
    status.update(state='FINISHED',returncode=result.returncode,end_utc=utc(),elapsed_seconds=time.monotonic()-start)
    status['outputs']={str(f.name):{'bytes':f.stat().st_size,'sha256':digest(f)} for f in sorted(work.iterdir()) if f.is_file() and f.name!='status.json'}
    save()
if __name__=='__main__':main()
