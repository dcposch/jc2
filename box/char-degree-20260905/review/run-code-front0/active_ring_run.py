#!/usr/bin/env python3
"""Bounded active-ring full characteristic run, with parser/control checks."""
from pathlib import Path
import argparse,hashlib,json,os,signal,subprocess,time
from active_ring_backend import active_normalized_script,from_g9966_input

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--timeout',type=int,default=1200)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    data=json.loads(a.input.read_text());script,meta=active_normalized_script(**from_g9966_input(a.input))
    path=a.out/'augmented.sing';path.write_text(script)
    meta.update(branch=data['branch'],stage=data['stage'],input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest(),
                input_source_gauge=data.get('source_gauge'),status='EMITTED_NOT_DECIDED',timeout_seconds=a.timeout,
                memory_limit_kib=os.environ.get('CHAR_MEMORY_KIB'),runner_pid=os.getpid())
    def save(): (a.out/'result.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    save();print('ACTIVE_RING_EMITTED',len(meta['active_generator_order']),len(meta['full_generator_order']),flush=True)
    started=time.monotonic();timed=False
    with (a.out/'singular.out').open('w') as stream:
        proc=subprocess.Popen(['/usr/bin/time','-f','{"wall_seconds":%e,"max_rss_kib":%M,"exit_status":%x}',
                               '-o',str(a.out/'singular.time.json'),'Singular','-q',str(path)],
                              stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        meta.update(singular_process_group=proc.pid,status='RUNNING');save()
        def stop(signum=None,frame=None):
            if proc.poll() is None:
                os.killpg(proc.pid,signal.SIGTERM)
                try:proc.wait(timeout=5)
                except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
        signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
        try:rc=proc.wait(timeout=a.timeout)
        except subprocess.TimeoutExpired:timed=True;stop();rc=proc.returncode
    output=(a.out/'singular.out').read_text()
    errors=[l for l in output.splitlines() if l.lstrip().startswith('?') or 'error occurred' in l]
    meta.update(returncode=rc,timed_out=timed,elapsed_seconds=round(time.monotonic()-started,3),
                last_marker=next((l for l in reversed(output.splitlines()) if l.startswith(('BEGIN_','END_'))),None),
                parser_or_cas_errors=errors[:30],output_sha256=hashlib.sha256(output.encode()).hexdigest())
    complete=all(s in output for s in ['BEGIN_RESULT\n','\nEND_RESULT','BEGIN_CONTROLS\n','\nEND_CONTROLS','END_EMBED_FULL_RING'])
    if rc==0 and not timed and complete and not errors:
        vals=output.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].strip().splitlines()
        controls=output.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].strip().splitlines()
        assert len(vals)==3 and vals[0] in ('0','1') and controls==['0','1'],(vals,controls)
        meta.update(reduce_one=vals[0],dimension_with_free_t_z=int(vals[1]),basis_size=int(vals[2]),controls=controls,
                    status='UNIT_CANDIDATE_REQUIRES_REPLAY' if vals[0]=='0' else 'EXACT_Q_PROPER_AUGMENTED_IDEAL')
    else:
        memory=any(s in output.lower() for s in ['out of memory','no more memory','omalloc'])
        meta['status']='MEMORY_BOUND_OPEN' if memory else 'COMPUTE_BOUND_OPEN' if timed else 'CAS_ERROR_OPEN' if errors else 'PROCESS_ERROR_OPEN'
    save();print(meta['status'],meta['last_marker'],flush=True)

if __name__=='__main__':main()
