"""Metadata-only terminal cross collection, one exclusive receipt per lane."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys
R=Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260907T2200Z'
def need(ok,msg):
    if not ok:raise RuntimeError(msg)
def pin(p):
    d=p.read_bytes();return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest()}
need(len(sys.argv)==2 and sys.argv[1] in ('astra','sol56','fable5'),'invalid lane')
who=sys.argv[1];tag='ideation-20260907T2200Z-cross-'+who
unit='jc2-lane-'+tag+'.service'
c=subprocess.run(['systemctl','--user','show',unit,'--no-pager',
 '-p','Id','-p','LoadState','-p','ActiveState','-p','SubState','-p','Result',
 '-p','ExecMainPID','-p','ExecMainStatus','-p','ExecMainExitTimestamp'],
 capture_output=True,timeout=10,check=True)
st=dict(x.split('=',1) for x in c.stdout.decode().splitlines() if '=' in x)
need(st['Id']==unit and st['ActiveState']=='inactive' and st['SubState']=='dead'
 and st['ExecMainPID']=='0','not terminal; no receipt access allowed')
p=R/('xmodel/'+tag+'.run.v2');raw=p.read_text()
pairs=[x.split('=',1) for x in raw.splitlines() if '=' in x];v=dict(pairs)
need(len(pairs)==len(v),'duplicate receipt key')
for k,w in {'tag':tag,'charged_inputs':'17','final_status':'DONE',
 'exit_code':'0','adapter_exit_code':'0','report_state':'BODY_SEALED',
 'seal_boundary':'CLEAN','charge_basis_status':'ABSENT'}.items():
    need(v.get(k)==w,'bad receipt '+k)
pins=[]
for i in range(1,18):
    k='charged_input_'+str(i);path=R/v[k];a=pin(path)
    need(v[k+'_post']=='UNCHANGED' and a['sha256']==v[k+'_sha256'],'input drift')
    pins.append(dict(a,path=v[k]))
for k in ('report','prompt','log'):
    path=Path(v[k]);path=path if path.is_absolute() else R/path;a=pin(path)
    need(a['sha256']==v[k+'_sha256'],k+' drift')
    pins.append(dict(a,path=str(path.relative_to(R))))
absence={k:not Path('/proc/'+v[k]).exists() for k in ('pid','child_pid')}
need(all(absence.values()),'PID present; no blind identity assumptions')
now=datetime.now(timezone.utc)
out={'schema':'jc2.terminal-cross-collection/v1','utc':now.isoformat(),
 'lane':who,'systemd':st,'state_scope':'not-found is collected, not retained exit metadata'
 if st['LoadState']=='not-found' else 'terminal retained unit',
 'receipt_raw':raw,'receipt_pin':pin(p),'current_pins':pins,
 'pid_absence':absence,'body_read_before_this_collection':False,
 'root_prior_report_read':who=='astra','remaining_child_processes':0}
target=B/('cross-collection-'+now.strftime('%Y%m%dT%H%M%SZ')+'-'+who+'.json')
with target.open('x') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
target.chmod(0o444)
print(json.dumps({'status':'COLLECTED_BEFORE_BODY','lane':who,
 'path':str(target.relative_to(R)),'pin':pin(target),'report_sha256':v['report_sha256']}))
