#!/usr/bin/env python3
"""Isolated repaired full-chart extraction + custody-preserving modular msolve.

No verdict promotion occurs here. Exact-Q confirmation is a separate checked
calculation triggered only by a modular unit. A timeout is never a NONUNIT.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shlex, subprocess, sys, time
ROOT=Path('/home/ubuntu/jc2')
BUNDLE=ROOT/'box/moh14-charts-20260905'
BASE=BUNDLE/'hsupport-gate-20260905/source-complete'
PYTHON='/tmp/jc2-hsupport-solver-venv/bin/python3'
SSH=['ssh','-o','BatchMode=yes','-o','ConnectTimeout=10','-o','ServerAliveInterval=30','-i','/home/ubuntu/.ssh/jc2-fleet']
SCP=['scp','-q','-o','BatchMode=yes','-o','ConnectTimeout=10','-i','/home/ubuntu/.ssh/jc2-fleet']
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args, **kw): return subprocess.run(args,check=True,**kw)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--stem',required=True);ap.add_argument('--host',required=True);ap.add_argument('--threads',type=int,default=8);ap.add_argument('--build-seconds',type=int,default=5400);ap.add_argument('--solve-seconds',type=int,default=900);ap.add_argument('--vm-kib',type=int,default=50000000);ap.add_argument('--mode',choices=['native','direct'],default='native');a=ap.parse_args()
 stem=a.stem; cls=stem.rsplit('_V',1)[0]; src=BASE/'classes'/cls
 work=BASE/'fleet'/a.host/(stem+'_'+a.mode);work.mkdir(parents=True,exist_ok=True)
 builder=src/'builders'/(stem+('_builder.sing' if a.mode=='native' else '_direct_builder.sing'))
 rowname=stem+('_rows.tsv' if a.mode=='native' else '_direct_rows.tsv')
 rows=src/'rows'/rowname;meta=src/'meta'/(stem+'.json')
 status={'stem':stem,'mode':a.mode,'host':a.host,'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'builder_sha256':sha(builder),'state':'BUILD_RUNNING','chart_unknowns':json.loads(meta.read_text())['parameter_count']}
 def save(): (work/'status.json').write_text(json.dumps(status,indent=2)+'\n'); print(json.dumps(status),flush=True)
 save()
 remote='ubuntu@'+a.host
 # Deliberately isolated subtree; prior campaign jobs and chart rows untouched.
 run(SSH+[remote,'mkdir -p '+shlex.quote(str(src/'builders'))+' '+shlex.quote(str(src/'rows'))+' '+shlex.quote(str(work))+' '+shlex.quote(str(BASE/'ops'))])
 run(SCP+[str(builder),remote+':'+str(builder)])
 cmd='ulimit -v '+str(min(a.vm_kib,32000000))+'; cd '+shlex.quote(str(src))+' && /usr/bin/time -v timeout --signal=TERM --kill-after=30s '+str(a.build_seconds)+'s Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc '+shlex.quote(str(builder))+' > '+shlex.quote(str(work/'builder.stdout'))+' 2> '+shlex.quote(str(work/'builder.stderr'))+'; rc=$?; printf "%s\\n" "$rc" > '+shlex.quote(str(work/'builder.rc'))
 run(SSH+[remote,cmd])
 run(SCP+[remote+':'+str(work/'builder.stdout'),remote+':'+str(work/'builder.stderr'),remote+':'+str(work/'builder.rc'),str(work)+'/'])
 run(SCP+[remote+':'+str(rows),str(rows)])
 stdout=(work/'builder.stdout').read_text(errors='replace');rc=int((work/'builder.rc').read_text().strip());count=sum(1 for line in rows.open() if line.strip())-1
 done=re.findall(r'NATIVE_DONE equations=(\d+)',stdout)
 errors=bool(re.search(r'NATIVE_FAIL|NATIVE_GATE [^\n]*=0(?:\n|$)|\?\s',stdout))
 gates=['NATIVE_GATE lead_h_is_yK=1','NATIVE_GATE target_xk_level0_nonzero=1'] if a.mode=='native' else ['DIRECT_GATE target_xk_nonzero=1']
 valid=rc==0 and len(done)==1 and int(done[0])==count and count>0 and all(g in stdout for g in gates) and not errors
 status.update(build_returncode=rc,rows_count=count,rows_sha256=sha(rows),build_valid=valid,state='BUILD_DONE' if valid else ('BUILD_TIMEOUT' if rc==124 else 'BUILD_INCOMPLETE'))
 save()
 if not valid:return
 ms=work/(stem+'_full_p1073741827.ms');manifest=work/'input.manifest.json'
 emit=[PYTHON,str(BUNDLE/'msolve_chart.py'),'emit','--meta',str(meta),'--rows',str(rows),'--builder',str(builder),'--characteristic','1073741827','--output',str(ms),'--manifest',str(manifest),'--json-output',str(work/'emit.json')]
 with (work/'emit.log').open('w') as fh: run(emit,stdout=fh,stderr=subprocess.STDOUT,timeout=1200)
 status.update(state='SOLVE_RUNNING',input_sha256=sha(ms));save()
 run(SCP+[str(ms),remote+':'+str(ms)])
 runner=BASE/'ops'/'run_msolve.sh';run(SCP+[str(runner),remote+':'+str(runner)])
 cmd='export PATH='+shlex.quote(str(BUNDLE/'hsupport-gate-20260905/ops/bin'))+':$PATH; ulimit -v '+str(a.vm_kib)+'; bash '+shlex.quote(str(runner))+' '+shlex.quote(str(ms))+' '+str(a.solve_seconds)+' '+str(a.threads)+' -l 44 -m 1000 > '+shlex.quote(str(work/'solve.driver.log'))+' 2>&1; true'
 run(SSH+[remote,cmd])
 base=str(ms)[:-3]
 files=[base+s for s in ['.g2.out','.g2.stdout','.g2.stderr','.g2.rc','.g2.meta']]+[str(work/'solve.driver.log')]
 # Missing output on a build/solve failure is retained as missing, never inferred.
 for f in files: subprocess.run(SCP+[remote+':'+f,str(work)+'/'],check=False)
 p=Path(base+'.g2.out');rcp=Path(base+'.g2.rc');srcerr=Path(base+'.g2.stderr')
 solve_rc=int(rcp.read_text().strip()) if rcp.exists() else None
 if p.exists():
  parser=[PYTHON,str(BUNDLE/'msolve_chart.py'),'status','--output',str(p),'--stderr',str(srcerr),'--rc-file',str(rcp),'--manifest',str(manifest),'--json-output',str(work/'msolve.status.json')]
  with (work/'status-parse.log').open('w') as fh:subprocess.run(parser,stdout=fh,stderr=subprocess.STDOUT,check=False)
 status.update(state='SOLVE_FINISHED',solve_returncode=solve_rc,finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
 if (work/'msolve.status.json').exists():status['msolve_status']=json.loads((work/'msolve.status.json').read_text())
 save()
if __name__=='__main__':
 try:main()
 except Exception as exc:print('DRIVER_ERROR '+repr(exc),file=sys.stderr,flush=True);raise
