#!/usr/bin/env python3
"""All eighteen full exact-Q characteristic systems; bounded independent runs."""
import concurrent.futures,hashlib,json,os,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');HERE=ROOT/'box/char-degree-20260905/g9966'
BACKEND=ROOT/'box/char-degree-20260905/d108/coefficient_circuit_backend_v2.py'
EXPECTED='17a825098e24dcbeb973d7fe6f254c6f5884f2aad9bed196e12166db0520ce35'
assert hashlib.sha256(BACKEND.read_bytes()).hexdigest()==EXPECTED

def run(case):
    branch,stage=case;inp=HERE/'circuit-inputs'/f'{branch}_stage{stage}.input.json'
    out=HERE/'circuit-runs'/f'{branch}_stage{stage}';out.mkdir(parents=True,exist_ok=True)
    script=out/'augmented.sing';start=time.monotonic()
    record={'branch':branch,'stage':stage,'field':'Q','input':str(inp),
      'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'backend':str(BACKEND),
      'backend_sha256':EXPECTED,'memory_gib':16,'cas_wall_limit_seconds':600,
      'started_unix':time.time(),'status':'RUNNING'}
    path=out/'execution.json'
    def save():path.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    def limit():resource.setrlimit(resource.RLIMIT_AS,(16*1024**3,16*1024**3))
    save();print(branch,stage,'START',flush=True)
    with (out/'driver.log').open('w') as stream:
        proc=subprocess.Popen(['python3','-u',str(BACKEND),'--input',str(inp),'--out',str(script),'--timeout','600'],
          cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,preexec_fn=limit)
        record['driver_pid']=proc.pid;save();rc=proc.wait()
    log=(out/'driver.log').read_bytes();record.update(returncode=rc,elapsed_seconds=round(time.monotonic()-start,3),
      driver_log_sha256=hashlib.sha256(log).hexdigest(),backend_hash_unchanged=hashlib.sha256(BACKEND.read_bytes()).hexdigest()==EXPECTED)
    meta=script.with_suffix('.circuit.json')
    if meta.exists():
        d=json.loads(meta.read_text());record.update(backend_status=d['status'],backend_result_sha256=hashlib.sha256(meta.read_bytes()).hexdigest())
        record['status']=d['status'] if d['status'] not in ('BUILDING','EMITTED_NOT_DECIDED') else 'PROCESS_BOUND_OPEN'
    else:record['status']='PROCESS_BOUND_OPEN'
    save();print(branch,stage,record['status'],record['elapsed_seconds'],flush=True)
    return record

def main():
    cases=[(branch,stage) for stage in range(9) for branch in ('delta2','delta52')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(run,cases))
    (HERE/'circuit-schedule.json').write_text(json.dumps({'cases':results,'workers':3,'status':'SCHEDULE_FINISHED'},indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
