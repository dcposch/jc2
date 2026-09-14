#!/usr/bin/env python3
"""After each full graph solve endpoint, stop only redundant extraction.
Already running msolve calculations keep their independent watchdog endpoints.
"""
from pathlib import Path
import json,os,signal,subprocess,time,shlex
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete')
SSH=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=10','-i','/home/ubuntu/.ssh/jc2-fleet']
SCP=['scp','-q','-o','BatchMode=yes','-i','/home/ubuntu/.ssh/jc2-fleet']
jobs={j['stem']:j for j in json.loads((BASE/'ops/launched-circuit.json').read_text())}
old=json.loads((BASE/'ops/launched-native.json').read_text())+json.loads((BASE/'ops/launched-direct.json').read_text());done=set();events=[]
while len(done)<len(jobs):
 for stem,j in jobs.items():
  if stem in done:continue
  cstatus=BASE/'fleet'/j['host']/(stem+'_circuit')/'status.json'
  if not cstatus.exists():continue
  current=json.loads(cstatus.read_text())
  if current['state']!='SOLVE_FINISHED':continue
  for oldjob in old:
   if oldjob['stem']!=stem:continue
   work=BASE/'fleet'/oldjob['host']/(stem+'_'+oldjob['mode']);sp=work/'status.json'
   if not sp.exists():continue
   state=json.loads(sp.read_text())
   if state.get('state')!='BUILD_RUNNING':continue
   pid=oldjob['pid']
   try:cmdline=Path('/proc',str(pid),'cmdline').read_bytes().split(b'\0')
   except OSError:cmdline=[]
   if any(b'fleet_driver.py' in c for c in cmdline)and any(stem.encode()==c for c in cmdline):os.kill(pid,signal.SIGTERM)
   builder=BASE/'classes'/stem.rsplit('_V',1)[0]/'builders'/(stem+('_builder.sing'if oldjob['mode']=='native'else '_direct_builder.sing'))
   script='import os,signal,json\npids=[]\nfor p in os.listdir("/proc"):\n if not p.isdigit():continue\n try:a=open("/proc/"+p+"/cmdline","rb").read().decode().split("\\0")\n except (OSError,UnicodeError):continue\n if a and a[0].split("/")[-1]=="Singular" and '+repr(str(builder))+' in a:\n  try:os.kill(int(p),signal.SIGTERM);pids.append(int(p))\n  except ProcessLookupError:pass\nprint(json.dumps(pids))\n'
   proc=subprocess.run(SSH+['ubuntu@'+j['host'],'python3 -c '+shlex.quote(script)],capture_output=True,text=True)
   event={'stem':stem,'mode':oldjob['mode'],'host':j['host'],'reason':'SUPERSEDED_BY_COMPLETED_FULL_GRAPH_SOLVE','graph_solve_returncode':current.get('returncode'),'time_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'remote_stop_stdout':proc.stdout.strip(),'remote_stop_stderr':proc.stderr.strip(),'local_driver_pid':pid}
   (work/'superseded-by-circuit.json').write_text(json.dumps(event,indent=2)+'\n');events.append(event)
   # Deliberately collect small logs only; unneeded expanded rows stay remote.
   time.sleep(1)
   for name in ['builder.stdout','builder.stderr','builder.rc']:
    subprocess.run(SCP+['ubuntu@'+j['host']+':'+str(work/name),str(work/name)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
   state.update(state='BUILD_STOPPED_REDUNDANT',stop_reason=event['reason'])
   if(work/'builder.rc').exists():state['build_returncode']=int((work/'builder.rc').read_text())
   sp.write_text(json.dumps(state,indent=2)+'\n')
  done.add(stem)
  (BASE/'ops/final-monitor-events.json').write_text(json.dumps({'completed_circuit_stems':sorted(done),'events':events},indent=2)+'\n')
  print('CIRCUIT_ENDPOINT '+stem+' '+str(current.get('returncode')),flush=True)
 if len(done)<len(jobs):time.sleep(10)
print('ALL_CIRCUIT_ENDPOINTS_OBSERVED',flush=True)
