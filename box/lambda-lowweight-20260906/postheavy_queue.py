#!/usr/bin/env python3
"""Two bounded CAS slots, fixed final probe queue, atomic owned-PID custody."""
import concurrent.futures, hashlib, json, os, subprocess, threading, time
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent
LOCK=threading.Lock();ACTIVE={};RESULTS=[];HALT=threading.Event()
DRIVER_HASH=hashlib.sha256((HERE/'run_truncated.py').read_bytes()).hexdigest()
def save():
    runner.persist_small(HERE/'postheavy-owned.json',json.dumps({
        'scheduler_pid':os.getpid(),'driver_sha256':DRIVER_HASH,
        'active_driver_pids':ACTIVE,'finished_jobs':RESULTS,
        'halted_for_unit_candidate':HALT.is_set(),
        'updated_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())},indent=2)+'\n')
def one(job):
    cid,N,variant=job
    if HALT.is_set():return
    assert hashlib.sha256((HERE/'run_truncated.py').read_bytes()).hexdigest()==DRIVER_HASH
    config=HERE/('ux_cached_cases.json' if variant=='UX' else 'run_cases.json')
    if variant=='UX':
        case=next(c for c in json.loads(config.read_text()) if c['id']==cid)
        assert case.get('ux_cache_receipt'),(cid,'cache is not ready')
    args=['python3',str(HERE/'run_truncated.py'),'--cases',str(config),'--ids',cid,
          '--N',str(N),'--packed','--seconds','240']
    suffix='.packed511'
    if variant in ('keller','UX'):
        args+=['--keller'];suffix='.keller'+('.UX' if variant=='UX' else '')+suffix
    if variant=='UX':args+=['--ux']
    key=f'{cid}{suffix}.N{N}';path=HERE/(key+'.json')
    assert not path.exists(),('preserve historical receipt',path)
    proc=subprocess.Popen(args,cwd=runner.ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    with LOCK:
        ACTIVE[str(proc.pid)]={'job':key,'args':args};save()
        print('START '+key+' DRIVER_PID='+str(proc.pid),flush=True)
    output,_=proc.communicate()
    if path.exists():
        result=json.loads(path.read_text())
        entry={k:result.get(k) for k in ['status','input_ready','std_done','cutoff','completed_homogeneous_weight','wall_seconds','peak_rss_bytes','process_pid','process_group']}
        entry.update(job=key,receipt=path.name,driver_pid=proc.pid,returncode=proc.returncode)
        if result['status']=='UNIT_CANDIDATE_NEEDS_COFACTORS':HALT.set()
    else:
        entry={'job':key,'status':'OPEN_QUEUE_DRIVER_ERROR','returncode':proc.returncode,
               'driver_pid':proc.pid,'error_tail':output[-3000:]};HALT.set()
    with LOCK:
        ACTIVE.pop(str(proc.pid));RESULTS.append(entry);save()
        print('DONE '+json.dumps(entry),flush=True)
    return entry
def main():
    jobs=[(c,n,'baseline') for c in ['R002','R004'] for n in [1,2,3]]
    meaningful=[(c,n) for c in ['C109','C171','R001','R002','C341'] for n in [2,3]]+[(c,n) for c in ['R004'] for n in [1,2,3]]
    jobs += [(c,n,'keller') for c,n in meaningful]
    jobs += [(c,n,'UX') for c,n in meaningful]
    assert len(jobs)==32
    with LOCK:save()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(one,j) for j in jobs]
        for f in futures:
            try:f.result()
            except BaseException as exc:
                HALT.set()
                with LOCK:
                    RESULTS.append({'status':'OPEN_QUEUE_ERROR','error':repr(exc)});save()
                print('QUEUE_ERROR '+repr(exc),flush=True)
    with LOCK:save()
    print('POSTHEAVY_QUEUE_DONE',flush=True)
if __name__=='__main__':main()
