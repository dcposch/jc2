"""Terminal actual tiny engine evidence, no production source or engine run."""
from pathlib import Path
import hashlib,json,sys
R=Path('/home/ubuntu/jc2');B=Path(__file__).parent;EV=B/'evidence'
sys.path.insert(0,str(R/'box/d125-hybrid81-parent-repair-20260907'));import engine as E
BOOT='886172be-22d4-42e8-939c-0fc0475346fa';GREEN='225f87df5b354b87d647aefe3449fe4f2d2051e1bd2fecf52fe46ef9dae44f58'
def need(c,m):
 if not c:raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(op,suffix):return json.loads((EV/(op+'.'+suffix)).read_bytes())
need(sha(EV/'ROOT-GREEN.md')==GREEN,'physical green drift')
receipts={'hybrid':'7cfd083c18f2fd705886c5a83c394ee830cc451e44373e1492927c61dc11f899','alarm':'a310474644a0d9de198aeb4e4e6072d34f549ef41adeaee8f1906ee926ba58b2'}
for op,pin in receipts.items():
 need(sha(EV/(op+'.receipt.json'))==pin,'receipt drift')
 r=read(op,'receipt.json');t=read(op,'telemetry.json');i=read(op,'identity.json');l=read(op,'launch.json');a=read(op,'authority.json')
 need(r['status']=='ENGINEERING_'+op.upper()+'_PASS' and r['telemetry']==t and not r['group_members_after'],'status/telemetry/group')
 for s,h in r['hashes'].items():need(sha(EV/(op+'.'+s))==h,'output pin '+s)
 need(a['mode']=='engineering_control' and a['boot_id']==BOOT and a['engineering']['root_green_sha256']==GREEN,'scope/physical binding')
 need(t['error'] is None and t['pid']==t['pgid']==i['pid']==i['pgid']==l['payload']['pid'],'payload identity')
 need(t['start_identity']=='boot='+BOOT+';start_ticks='+i['start_ticks'],'start identity')
 need(l['payload']['start_ticks']==i['start_ticks'] and l['payload']['namespace']==i['namespace'] and l['payload']['cgroup']==i['cgroup'],'live identity')
 need(l['runner']['pid']==l['spawn_pid'] and l['runner']['boot']==BOOT and l['payload']['boot']==BOOT,'runner/boot')
 need([s.encode() for s in l['runner']['argv']]==E.expected_parent_argv(op),'exact live parent vector')
 need(l['command']==['/usr/bin/prlimit','--fsize=67108864:67108864','--core=0:0','--']+l['runner']['argv'],'exact generated vector')
 need(t['caps']['wall_seconds']==10 and t['caps']['cpu_seconds']==10 and t['caps']['rss_bytes']==536870912,'actual caps')
 need(i['source_access'] is False and (EV/(op+'.stderr')).read_bytes()==b'','source access/stderr')
 if op=='hybrid':
  need(t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and r['runner_rc']==0,'hybrid exit')
  result=E.check_hybrid((EV/'tiny-engine-fixture.jsonl').read_bytes(),(EV/'hybrid.stdout').read_bytes(),b'')
  need(sha(EV/'hybrid.sing')=='59295067207d4f17eb2acdbd4eac9d4755d16c94bfc36884e2f14d2731b9ad11','control script')
 else:
  need(t['status']=='SIGNAL' and t['child_returncode']==-14 and t['child_signal']==14 and r['runner_rc']==142,'actual alarm')
  need((EV/'alarm.stdout').read_bytes()==b'JC2_HYBRID81_ALARM_READY\n' and 0<i['timer_remaining'][0]<=1 and t['wall_elapsed_seconds']<2,'ready/timer/time')
  need(sha(EV/'alarm.sing')=='446daa14cdedeb55ec9d0753ff48582b9ad3945bf889d471f56059911ea1f4b7','alarm script')
print(json.dumps({'status':'ACTUAL_ENGINEERING_PASS','hybrid':result,'receipts':receipts,'boot':BOOT,'source_access':False},sort_keys=True))
