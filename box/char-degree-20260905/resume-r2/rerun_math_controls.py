#!/usr/bin/env python3
"""Rerun inherited exact controls with original __file__ and fresh output paths."""
from pathlib import Path
import concurrent.futures,hashlib,json,os,subprocess,time
ROOT=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent
specs={
 'source-audit-controls':("OUT = Path(__file__).with_suffix('.json')", "OUT = Path(REPLACEMENT_OUTPUT)"),
 'nondegeneracy-controls':("Path(__file__).with_suffix('.json').write_text", "Path(REPLACEMENT_OUTPUT).write_text"),
 'coefficient-circuit-support-control':("Path(__file__).with_suffix('.json').write_text", "Path(REPLACEMENT_OUTPUT).write_text"),
 'remainder-independent-review':("(HERE/'remainder-independent-review.json').write_text", "Path(REPLACEMENT_OUTPUT).write_text")}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,spec):
 original=ROOT/(name+'.py');target=OUT/(name+'.fresh.json');executed=OUT/(name+'.executed.py')
 source=original.read_text();old,new=spec;assert source.count(old)==1
 changed=source.replace(old,new.replace('REPLACEMENT_OUTPUT',repr(str(target))))
 executed.write_text(changed)
 launcher='import pathlib; p='+repr(str(executed))+'; g={"__name__":"__main__","__file__":'+repr(str(original))+'}; exec(compile(pathlib.Path(p).read_text(),p,"exec"),g)'
 env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
 log=OUT/(name+'.fresh.log');start=time.monotonic()
 with log.open('w') as f:
  try:r=subprocess.run(['python3','-c',launcher],cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=60);rc=r.returncode;timed=False
  except subprocess.TimeoutExpired:rc=None;timed=True
 record={'name':name,'original_source':str(original),'original_sha256':sha(original),'executed_source':str(executed),'executed_sha256':sha(executed),'output_redirection_only':True,'replacement_from':old,'replacement_to':new.replace('REPLACEMENT_OUTPUT',repr(str(target))),'original___file___preserved':str(original),'environment_override':{'PYTHONDONTWRITEBYTECODE':'1'},'returncode':rc,'timeout':timed,'elapsed_seconds':round(time.monotonic()-start,3),'log':str(log),'log_sha256':sha(log),'output':str(target),'output_sha256':sha(target) if target.exists() else None,'status':'PASS' if rc==0 and target.exists() else 'FAIL'}
 if target.exists():
  fresh=json.loads(target.read_text());inherited=original.with_suffix('.json')
  record['inherited_output_sha256']=sha(inherited) if inherited.exists() else None
  record['fresh_json_equals_inherited']=fresh==json.loads(inherited.read_text()) if inherited.exists() else None
 (OUT/(name+'.fresh.custody.json')).write_text(json.dumps(record,indent=2)+'\n')
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 records=list(pool.map(lambda item:run(*item),specs.items()))
manifest={'status':'PASS' if all(r['status']=='PASS' for r in records) else 'FAIL','records':records}
(OUT/'fresh-math-controls.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':manifest['status'],'records':[{k:r[k] for k in ('name','status','returncode','elapsed_seconds','output_sha256','fresh_json_equals_inherited')} for r in records]},indent=2))
