from pathlib import Path
import json,subprocess,os,time,hashlib
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete')
SSH=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=5','-i','/home/ubuntu/.ssh/jc2-fleet']
programs={'fleet_driver.py','circuit_run.py','final_monitor.py','retry48.py','retry64.py','retry_live_capture.py'}
ours=[]
for pid in os.listdir('/proc'):
 if not pid.isdigit():continue
 try:a=Path('/proc',pid,'cmdline').read_bytes().decode().split('\0')
 except (OSError,UnicodeError):continue
 if len(a)>1 and a[0].split('/')[-1].startswith('python') and Path(a[1]).name in programs and 'hsupport-gate-20260905'in a[1]:ours.append({'pid':int(pid),'argv':a})
remote=[]
script='import os,json,time\np=[]\nfor pid in os.listdir("/proc"):\n if not pid.isdigit():continue\n try:a=open("/proc/"+pid+"/cmdline","rb").read().decode().split("\\0")\n except (OSError,UnicodeError):continue\n if a and a[0].split("/")[-1] in ("Singular","msolve") and any("hsupport-gate-20260905" in x for x in a):p.append({"pid":int(pid),"argv":a})\nprint(json.dumps({"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"lane_CAS_processes":p}))\n'
import shlex
for host in ['172.30.0.7','172.30.0.18','172.30.0.28']:
 p=subprocess.run(SSH+['ubuntu@'+host,'python3 -c '+shlex.quote(script)],capture_output=True,text=True)
 remote.append({'host':host,'ssh_returncode':p.returncode,'stdout':p.stdout.strip(),'stderr':p.stderr.strip()})
 assert p.returncode==0
 assert json.loads(p.stdout)['lane_CAS_processes']==[]
assert ours==[]
aws=subprocess.run(['aws','ec2','describe-instances','--region','us-east-1','--filters','Name=tag:jc2fleet,Values=1','--query','Reservations[].Instances[].{ID:InstanceId,Priv:PrivateIpAddress,State:State.Name,Reason:StateTransitionReason,Type:InstanceType}','--output','json'],capture_output=True,text=True,check=True)
record={'cutoff_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'local_lane_drivers_or_collectors':ours,'surviving_worker_checks':remote,'fleet_ec2_state':json.loads(aws.stdout),'no_instances_created_or_terminated_by_this_lane':True,'solver_UNIT_signals':0,'exact_Q_production_certificates':0,'zero_dangling_lane_processes':True}
(BASE/'ops/final-operational-audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
