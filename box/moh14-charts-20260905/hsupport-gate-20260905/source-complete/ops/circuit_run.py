#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys,shlex,hashlib,time
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905/source-complete')
BUNDLE=BASE.parent.parent
PYTHON='/tmp/jc2-hsupport-solver-venv/bin/python3'
SSH=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=10','-o','ServerAliveInterval=30','-i','/home/ubuntu/.ssh/jc2-fleet']
SCP=['scp','-q','-o','BatchMode=yes','-i','/home/ubuntu/.ssh/jc2-fleet']
job=next(j for j in json.loads((BASE/'ops/circuit-emission.json').read_text())if j['stem']==sys.argv[1]);stem=job['stem'];host=job['host'];remote='ubuntu@'+host
work=BASE/'fleet'/host/(stem+'_circuit');work.mkdir(parents=True,exist_ok=True)
ms=work/(stem+'_circuit_full_p1073741827.ms');manifest=work/'input.manifest.json'
status=dict(stem=stem,mode='circuit',host=host,intrinsic_unknowns=job['intrinsic_unknowns'],auxiliary_unknowns=job['auxiliary_unknowns'],state='EMITTING',started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
def save(): (work/'status.json').write_text(json.dumps(status,indent=2)+'\n');print(json.dumps(status),flush=True)
def run(args,**kw):return subprocess.run(args,check=True,**kw)
save()
cmd=[PYTHON,str(BUNDLE/'msolve_chart.py'),'emit','--meta',job['meta'],'--rows',job['rows'],'--builder',job['builder'],'--characteristic','1073741827','--output',str(ms),'--manifest',str(manifest),'--json-output',str(work/'emit.json')]
with(work/'emit.log').open('w')as fh:run(cmd,stdout=fh,stderr=subprocess.STDOUT,timeout=1200)
status.update(state='SOLVE_RUNNING',input_sha256=hashlib.sha256(ms.read_bytes()).hexdigest(),input_bytes=ms.stat().st_size);save()
run(SSH+[remote,'mkdir -p '+shlex.quote(str(work))])
run(SCP+[str(ms),remote+':'+str(ms)])
threads=8 if host.endswith(('.166','.254')) else 8
vm=16000000 if host.endswith(('.166','.254')) else 8000000
runner=BASE/'ops/run_msolve.sh'
cmd='export PATH='+shlex.quote(str(BASE.parent/'ops/bin'))+':$PATH; ulimit -v '+str(vm)+'; bash '+shlex.quote(str(runner))+' '+shlex.quote(str(ms))+' 900 '+str(threads)+' -l 44 -m 1000 -s 12 -u 8 > '+shlex.quote(str(work/'solve.driver.log'))+' 2>&1; true'
run(SSH+[remote,cmd])
base=str(ms)[:-3]
for f in [base+s for s in ['.g2.out','.g2.stdout','.g2.stderr','.g2.rc','.g2.meta']]+[str(work/'solve.driver.log')]:subprocess.run(SCP+[remote+':'+f,str(work)+'/'],check=False)
p=Path(base+'.g2.out');rcp=Path(base+'.g2.rc');err=Path(base+'.g2.stderr');rc=int(rcp.read_text())if rcp.exists()else None
if p.exists():
 cmd=[PYTHON,str(BUNDLE/'msolve_chart.py'),'status','--output',str(p),'--stderr',str(err),'--rc-file',str(rcp),'--manifest',str(manifest),'--json-output',str(work/'msolve.status.json')]
 with(work/'status-parse.log').open('w')as fh:subprocess.run(cmd,stdout=fh,stderr=subprocess.STDOUT,check=False)
status.update(state='SOLVE_FINISHED',returncode=rc,finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
if(work/'msolve.status.json').exists():status['msolve_status']=json.loads((work/'msolve.status.json').read_text())
save()
