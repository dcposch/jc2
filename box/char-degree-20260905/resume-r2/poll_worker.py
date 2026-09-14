#!/usr/bin/env python3
"""Ten-minute worker status polls, compact receipts only."""
import datetime,json,shlex,subprocess,time
from pathlib import Path
BASE=Path(__file__).resolve().parent
CODE='''import datetime,json,os
from pathlib import Path
jobs=[]
for p in Path('/proc').iterdir():
 if not p.name.isdigit(): continue
 if int(p.name)==os.getpid(): continue
 try:
  a=(p/'cmdline').read_bytes().replace(b'\\0',b' ').decode(errors='replace').strip()
  cwd=os.readlink(p/'cwd')
  if ('Singular -q '==a[:12] or ('python3' in a[:10] and ('run_circuit_schedule.py' in a or 'coefficient_circuit_backend' in a))) and ('char-degree-20260905' in cwd or 'char-degree-20260905' in a):
   jobs.append(dict(pid=int(p.name),cwd=cwd,args=a,status=[l for l in (p/'status').read_text().splitlines() if l.startswith(('VmRSS:','VmHWM:'))]))
 except OSError: pass
print(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),jobs=jobs)))
'''
deadline=datetime.datetime(2026,9,6,1,42,55,tzinfo=datetime.timezone.utc).timestamp()
next_poll=datetime.datetime(2026,9,5,23,33,8,tzinfo=datetime.timezone.utc).timestamp()
while time.time()<deadline:
    if time.time()<next_poll:
        time.sleep(min(30,next_poll-time.time()));continue
    p=subprocess.run(['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'-o','BatchMode=yes','-o','ConnectTimeout=15','ubuntu@172.30.0.40','python3 -c '+shlex.quote(CODE)],text=True,capture_output=True,timeout=45)
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    receipt=dict(local_utc=stamp,returncode=p.returncode,stderr=p.stderr,worker=json.loads(p.stdout) if p.returncode==0 else p.stdout)
    (BASE/('poll-'+stamp+'.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
    if p.returncode==0 and not receipt['worker']['jobs']: break
    next_poll+=600
