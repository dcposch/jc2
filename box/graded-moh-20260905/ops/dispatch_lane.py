#!/usr/bin/env python3
"""Dispatch only this lane's jobs to explicitly owned workers."""
import argparse,datetime,json,pathlib,shlex,subprocess
ROOT=pathlib.Path('/home/ubuntu/jc2/box/graded-moh-20260905')
OWNED={'172.30.0.67':'i-05bbedf0197e8eee3','172.30.0.86':'i-02aaa996f54d2c004'}
def ssh(ip,cmd):return subprocess.run(['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','ConnectTimeout=10','ubuntu@'+ip,cmd],capture_output=True,text=True)
def main():
 p=argparse.ArgumentParser();p.add_argument('action',choices=['launch','poll','pull']);p.add_argument('ip',choices=list(OWNED));p.add_argument('spec',nargs='?');a=p.parse_args()
 if a.action=='launch':
  spec=pathlib.Path(a.spec).resolve();s=json.loads(spec.read_text());assert s['ip']==a.ip and s['worker']==OWNED[a.ip]
  work=pathlib.Path(s['work']); assert work.is_relative_to(ROOT)
  inp=pathlib.Path(s['input']); assert inp.is_relative_to(ROOT)
  r=ssh(a.ip,'mkdir -p '+shlex.quote(str(work))+' '+shlex.quote(str(inp.parent)));assert r.returncode==0,r.stderr
  for f in (spec,inp):
   r=subprocess.run(['scp','-q','-i','/home/ubuntu/.ssh/jc2-fleet',str(f),'ubuntu@'+a.ip+':'+str(f)],capture_output=True,text=True);assert r.returncode==0,r.stderr
  cmd='setsid python3 '+shlex.quote(str(ROOT/'ops/worker_run.py'))+' '+shlex.quote(str(spec))+' > '+shlex.quote(str(work/'driver.log'))+' 2>&1 < /dev/null &'
  r=ssh(a.ip,cmd);receipt=dict(ip=a.ip,instance=OWNED[a.ip],command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr,utc=datetime.datetime.now(datetime.timezone.utc).isoformat());(work/'launch.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt));assert r.returncode==0
 elif a.action=='pull':
  r=subprocess.run(['rsync','-az','-e','ssh -i /home/ubuntu/.ssh/jc2-fleet -o BatchMode=yes','ubuntu@'+a.ip+':'+str(ROOT/'runs')+'/',str(ROOT/'runs')+'/']);assert r.returncode==0
 else:
  code='''import pathlib,json,subprocess
p=pathlib.Path("/home/ubuntu/jc2/box/graded-moh-20260905/runs")
for f in sorted(p.glob("*/status.json")):
 d=json.loads(f.read_text()); print(f.parent.name,d["state"],d.get("returncode"))
 for name in ["stdout.log","stderr.log"]:
  s=f.parent/name
  if s.exists():
   with s.open("rb") as h:
    h.seek(max(0,s.stat().st_size-350));tail=h.read().decode(errors="replace")
   print(name,s.stat().st_size,tail)
print("\\n".join(subprocess.check_output(["ps","-eo","pid,ppid,rss,vsz,etime,comm","--sort=-rss"],text=True).splitlines()[:10]))
'''
  r=ssh(a.ip,'python3 -c '+shlex.quote(code));out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),ip=a.ip,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr);print(json.dumps(out));
  log=ROOT/'ops'/('poll-'+a.ip+'.jsonl')
  with log.open('a') as f:f.write(json.dumps(out)+'\n')
if __name__=='__main__':main()
