#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys,shlex,hashlib,time
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete');BUNDLE=BASE.parent.parent
PYTHON='/tmp/jc2-hsupport-solver-venv/bin/python3'
SSH=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=10','-o','ServerAliveInterval=30','-i','/home/ubuntu/.ssh/jc2-fleet'];SCP=['scp','-q','-o','BatchMode=yes','-i','/home/ubuntu/.ssh/jc2-fleet']
stem,mode,host=sys.argv[1:4];remote='ubuntu@'+host;cls=stem.rsplit('_V',1)[0]
work=BASE/'fleet'/host/(stem+'_'+mode+'_retry48GiB');work.mkdir(parents=True,exist_ok=True)
source=BASE/('circuit'if mode=='circuit'else 'classes')/cls
meta=source/'meta'/(stem+('_circuit.json'if mode=='circuit'else '.json'));rows=source/'rows'/(stem+('_circuit_rows.tsv'if mode=='circuit'else '_rows.tsv'));builder=BASE/'classes'/cls/'builders'/(stem+'_builder.sing')
ms=work/(stem+'_full_p1073741827.ms');manifest=work/'input.manifest.json'
status={'stem':stem,'mode':mode,'host':host,'state':'EMITTING','vm_limit_KiB':50331648,'watchdog_seconds':900,'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
def save():(work/'status.json').write_text(json.dumps(status,indent=2)+'\n');print(json.dumps(status),flush=True)
def run(cmd,**kw):return subprocess.run(cmd,check=True,**kw)
save()
# Snapshot host resources immediately before the new bounded solve.
snapshot=run(SSH+[remote,'free -m; ps -eo pid,pcpu,rss,args --sort=-rss | head -12'],capture_output=True,text=True);(work/'preflight-resources.txt').write_text(snapshot.stdout+snapshot.stderr)
cmd=[PYTHON,str(BUNDLE/'msolve_chart.py'),'emit','--meta',str(meta),'--rows',str(rows),'--builder',str(builder),'--characteristic','1073741827','--output',str(ms),'--manifest',str(manifest),'--json-output',str(work/'emit.json')]
with(work/'emit.log').open('w')as fh:run(cmd,stdout=fh,stderr=subprocess.STDOUT,timeout=1200)
status.update(state='SOLVE_RUNNING',input_sha256=hashlib.sha256(ms.read_bytes()).hexdigest());
oldhost='172.30.0.18' if mode=='native' else '172.30.0.7'
oldmanifest=json.loads((BASE/'fleet'/oldhost/(stem+'_'+mode)/'input.manifest.json').read_text())
assert status['input_sha256']==oldmanifest['output']['sha256'], 'retry input custody mismatch'
status['input_identical_to_first_attempt']=True
save()
run(SSH+[remote,'mkdir -p '+shlex.quote(str(work))]);run(SCP+[str(ms),remote+':'+str(ms)])
opts='-l 44 -m 100 -s 12 -u 1'if mode=='circuit'else '-l 44 -m 100 -u 1'
cmd='export PATH='+shlex.quote(str(BASE.parent/'ops/bin'))+':$PATH; ulimit -v 50331648; bash '+shlex.quote(str(BASE/'ops/run_msolve.sh'))+' '+shlex.quote(str(ms))+' 900 12 '+opts+' > '+shlex.quote(str(work/'solve.driver.log'))+' 2>&1; true'
solve_transport=subprocess.run(SSH+[remote,cmd],check=False);status['ssh_returncode']=solve_transport.returncode;base=str(ms)[:-3]
for f in [base+s for s in ['.g2.out','.g2.stdout','.g2.stderr','.g2.rc','.g2.meta']]+[str(work/'solve.driver.log')]:subprocess.run(SCP+[remote+':'+f,str(work)+'/'],check=False)
p=Path(base+'.g2.out');rcp=Path(base+'.g2.rc');err=Path(base+'.g2.stderr');rc=int(rcp.read_text())if rcp.exists()else None
if p.exists():
 cmd=[PYTHON,str(BUNDLE/'msolve_chart.py'),'status','--output',str(p),'--stderr',str(err),'--rc-file',str(rcp),'--manifest',str(manifest),'--json-output',str(work/'msolve.status.json')]
 with(work/'status-parse.log').open('w')as fh:subprocess.run(cmd,stdout=fh,stderr=subprocess.STDOUT,check=False)
status.update(state='SOLVE_FINISHED' if solve_transport.returncode==0 else 'SOLVE_TRANSPORT_INTERRUPTED',returncode=rc,finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
if(work/'msolve.status.json').exists():status['msolve_status']=json.loads((work/'msolve.status.json').read_text())
save()
