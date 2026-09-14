#!/usr/bin/env python3
"""Bounded exact-Q execution of a complete, hash-bound Singular row driver."""
import argparse,hashlib,json,os,resource,signal,subprocess,time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--script',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--input',type=Path)
    ap.add_argument('--seconds',type=int,default=1800);ap.add_argument('--memory-gib',type=int,default=48)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    record={'status':'RUNNING','field':'Q','script':str(a.script),'script_sha256':hashlib.sha256(a.script.read_bytes()).hexdigest(),
            'wall_limit_seconds':a.seconds,'memory_limit_gib':a.memory_gib,'started_unix':time.time()}
    if a.input:record.update(input=str(a.input),input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest())
    def save():(a.out/'result.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    save();start=time.monotonic()
    def limits():resource.setrlimit(resource.RLIMIT_AS,(a.memory_gib*1024**3,a.memory_gib*1024**3))
    with (a.out/'singular.out').open('w') as stream:
        proc=subprocess.Popen(['Singular','-q',str(a.script)],stdout=stream,stderr=subprocess.STDOUT,start_new_session=True,preexec_fn=limits)
        record['pid']=proc.pid;save();timed=False
        try:rc=proc.wait(timeout=a.seconds)
        except subprocess.TimeoutExpired:
            timed=True;os.killpg(proc.pid,signal.SIGTERM)
            try:rc=proc.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);rc=proc.wait()
    text=(a.out/'singular.out').read_text();errs=[l for l in text.splitlines() if l.lstrip().startswith('?') or 'error occurred' in l]
    record.update(returncode=rc,elapsed_seconds=round(time.monotonic()-start,3),timeout=timed,parser_or_cas_errors=errs[:20],
         last_progress=next((l for l in reversed(text.splitlines()) if l.startswith(('BEGIN_','END_'))),None),
         log_sha256=hashlib.sha256(text.encode()).hexdigest(),script_hash_unchanged=hashlib.sha256(a.script.read_bytes()).hexdigest()==record['script_sha256'])
    if rc==0 and not errs and record['script_hash_unchanged'] and all(x in text for x in ['BEGIN_RESULT\n','\nEND_RESULT','BEGIN_CONTROLS\n','\nEND_CONTROLS']):
        vals=text.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].strip().splitlines()
        controls=text.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].strip().splitlines()
        assert len(vals)==3 and vals[0] in ('0','1') and controls==['0','1'],(vals,controls)
        record.update(status='UNIT-CANDIDATE-NEEDS-INDEPENDENT-REPLAY' if vals[0]=='0' else 'EXACT-Q-PROPER-AUGMENTED-IDEAL',
                      reduce_one=vals[0],dimension=int(vals[1]),basis_size=int(vals[2]),controls=controls)
    elif timed:record['status']='COMPUTE-BOUND-OPEN'
    elif rc!=0 and ('memory' in text.lower() or 'omalloc' in text or rc in (-6,-9,-11)):record['status']='MEMORY-BOUND-OPEN'
    else:record['status']='CAS-ERROR-OPEN'
    save();print(json.dumps(record,sort_keys=True),flush=True)

if __name__=='__main__':main()
