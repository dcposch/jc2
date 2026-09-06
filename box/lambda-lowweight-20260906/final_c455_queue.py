#!/usr/bin/env python3
"""Final solo full-memory C455 Keller/necessary-attainment probes."""
import datetime,hashlib,json,os,subprocess,time
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent
DEADLINE=datetime.datetime(2026,9,6,3,40,tzinfo=datetime.timezone.utc).timestamp()
def main():
    prior=json.loads((HERE/'postheavy-owned.json').read_text())
    assert not prior['active_driver_pids'] and not prior['halted_for_unit_candidate']
    receipt={'scheduler_pid':os.getpid(),'active_driver_pid':None,'finished_jobs':[],
             'driver_sha256':hashlib.sha256((HERE/'run_truncated.py').read_bytes()).hexdigest(),
             'hard_shutdown_utc':'2026-09-06T03:40:00Z','wall_cap_per_run':900,'post_input_std_cap':60,
             'rss_cap_gib':15.5,'address_space_cap_gib':15.8}
    def save():runner.persist_small(HERE/'final-c455-owned.json',json.dumps(receipt,indent=2)+'\n')
    save()
    for ux,N in [(False,2),(False,3),(True,2),(True,3)]:
        seconds=min(900,DEADLINE-time.time())
        if seconds<1:
            receipt['stopped_for_lane_deadline']=True;save();break
        config=HERE/('ux_cached_cases.json' if ux else 'run_cases.json')
        suffix='.keller'+('.UX' if ux else '')+'.packed255'
        key=f'C455{suffix}.N{N}';path=HERE/(key+'.json')
        assert not path.exists(),('preserve prior record',path)
        args=['python3',str(HERE/'run_truncated.py'),'--cases',str(config),'--ids','C455','--N',str(N),
              '--keller','--packed','--packed-max-exp','255','--seconds',str(seconds),
              '--std-seconds','60','--rss-gib','15.5','--as-gib','15.8']
        if ux:args+=['--ux']
        proc=subprocess.Popen(args,cwd=runner.ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        receipt['active_driver_pid']=proc.pid;receipt['active_job']=key;save()
        print('START '+key+' DRIVER_PID='+str(proc.pid),flush=True)
        output,_=proc.communicate()
        r=json.loads(path.read_text()) if path.exists() else {'status':'OPEN_DRIVER_ERROR','error_tail':output[-3000:]}
        entry={k:r.get(k) for k in ('status','input_ready','std_done','cutoff','completed_homogeneous_weight','wall_seconds','peak_rss_bytes','process_pid','process_group')}
        entry.update(job=key,receipt=path.name,driver_pid=proc.pid,returncode=proc.returncode)
        receipt['active_driver_pid']=None;receipt['finished_jobs'].append(entry);save()
        print('DONE '+json.dumps(entry),flush=True)
        if r['status'] in ('UNIT_CANDIDATE_NEEDS_COFACTORS','OPEN_DRIVER_ERROR'):
            receipt['halted_for_review']=True;save();break
    print('FINAL_C455_QUEUE_DONE',flush=True)
if __name__=='__main__':main()
