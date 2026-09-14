#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,time,shlex
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete')
SSH=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=5','-i','/home/ubuntu/.ssh/jc2-fleet'];SCP=['scp','-q','-o','BatchMode=yes','-o','ConnectTimeout=5','-i','/home/ubuntu/.ssh/jc2-fleet']
jobs=json.loads((BASE/'ops/launched-retry48GiB.json').read_text());active={j['stem']:j for j in jobs};rounds=0
while active and rounds<210:
 rounds+=1
 for stem,j in list(active.items()):
  work=BASE/'fleet'/j['host']/(stem+'_'+j['mode']+'_retry48GiB');sp=work/'status.json';state=json.loads(sp.read_text())if sp.exists()else{}
  if state.get('state')not in ['EMITTING','SOLVE_RUNNING']:active.pop(stem);continue
  ms=work/(stem+'_full_p1073741827.ms')
  script='import os,json,time\na=[]\nfor pid in os.listdir("/proc"):\n if not pid.isdigit():continue\n try:c=open("/proc/"+pid+"/cmdline","rb").read().decode().split("\\0")\n except (OSError,UnicodeError):continue\n if c and c[0].split("/")[-1]=="msolve" and '+repr(str(ms))+' in c:\n  try:s=open("/proc/"+pid+"/status").read();a.append({"pid":int(pid),"status":s})\n  except OSError:pass\nprint(json.dumps({"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"processes":a}))\n'
  p=subprocess.run(SSH+['ubuntu@'+j['host'],'python3 -c '+shlex.quote(script)],capture_output=True,text=True)
  with(work/'live-resources.jsonl').open('a')as fh:fh.write(json.dumps({'ssh_rc':p.returncode,'stdout':p.stdout.strip(),'stderr':p.stderr.strip()})+'\n')
  if rounds%6==1:
   for suffix in ['.g2.stderr','.g2.meta','.g2.out']:
    f=Path(str(ms)[:-3]+suffix)
    # Snapshot names are separate from authoritative runner collection.
    subprocess.run(SCP+['ubuntu@'+j['host']+':'+str(f),str(f)+'.snapshot'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 if active:time.sleep(5)
print('LIVE_CAPTURE_FINISHED',flush=True)
