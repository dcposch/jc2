"""Compact terminal evidence replay; no worker, source or mathematical system."""
from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent;E=B/'evidence';d=json.loads((B/'engineering-custody.json').read_bytes())
def need(ok,msg):
    if not ok:raise ValueError(msg)
checked=0
for name,v in d['files'].items():
    p=(B.parent/'d125-hybrid-pilot-readiness-20260907/host_control.py') if name=='engineering/host_control.py' else E/name
    data=p.read_bytes();need(len(data)==v['bytes'] and hashlib.sha256(data).hexdigest()==v['sha256'],'copy drift '+name);checked+=1
need(d['ids_absent']==[1536,1537,1538,1541,1542,1544] and d['groups_absent']==[1536,1538,1542] and d['production_outputs_absent'] is True,'custody scope')
batch=json.loads((E/'engineering/batch-result.json').read_bytes());need(batch['status']=='ENGINEERING_ONLY_PASS' and batch['elapsed_seconds']<30,'batch status')
for label in ('authorize','rss'):
    t=json.loads((E/f'engineering/{label}.telemetry.json').read_bytes())
    r=json.loads((E/f'engineering/{label}.receipt.json').read_bytes());launch=json.loads((E/f'engineering/{label}.launch.json').read_bytes())
    post=json.loads((E/f'engineering/{label}.identity.json').read_bytes())
    need(not t['error'] and not r['group_members_after'] and r['runner_absent'],'cleanup/error')
    need(t['caps']['cpu_seconds']==10 and t['caps']['wall_seconds']==10 and t['caps']['rss_bytes']==(536870912 if label=='authorize' else 67108864),'runner caps')
    need(post['limits']=={'AS':[536870912,536870912],'CPU':[10,10],'FSIZE':[134217728,134217728],'CORE':[0,0]},'actual limits')
    need(0<launch['remaining_at_spawn']<9.5 and launch['expires_unix']-launch['spawn_unix']==launch['remaining_at_spawn'],'worker dynamic expiry')
    for stream in ('stdout','stderr'):
        p=E/f'engineering/{label}.{stream}';need(p.stat().st_size==t[stream]['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==t[stream]['sha256'],'CAPRUN output pin')
    need(t['stderr']['bytes']==0 and r['runner_stderr']=='','unexpected control stderr')
    if label=='authorize':
        stdout=json.loads((E/'engineering/authorize.stdout').read_bytes())
        need(t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and t['runner_exit_code']==0 and stdout['status']=='REAL_AUTHORIZE_AND_TINY_NORMALIZED_CONTROL_PASS' and stdout['source_access'] is False,'authorize control')
    else:
        term=t['termination'];need(t['status']=='RESOURCE_CAP' and t['resource']=='rss' and t['runner_exit_code']==125 and all(term[k] is True for k in ('term_sent','kill_sent','leader_reaped','cleanup_complete')),'RSS control')
    ap=E/('engineering/authorize.authority.json' if label=='authorize' else 'authority.json')
    need(hashlib.sha256(ap.read_bytes()).hexdigest()==launch['authority_sha256'],'spent/current authority pin')
print(json.dumps(dict(status='ENGINEERING_COMPACT_REPLAY_PASS',checked_files=checked,normal_and_optimized_supported=True,source_read=False),sort_keys=True))
