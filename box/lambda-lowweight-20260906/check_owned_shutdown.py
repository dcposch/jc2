#!/usr/bin/env python3
"""Read-only worker liveness audit and compact shutdown receipt; sends no signals."""
import hashlib,json,os,time
from pathlib import Path
import run_truncated as runner
HERE=Path(__file__).resolve().parent
HISTORICAL=[1539908,1560059,1782258,1938681,1941265,1948504,2122171]
WORKERS={'run_truncated.py','postheavy_queue.py','final_c455_queue.py',
         'packed_heavy_queue.py','solo_heavy_queue.py','finish_roster.py',
         'ux_row_cache.py','direct_ordinary.py'}
def command(pid):
    try:return Path(f'/proc/{pid}/cmdline').read_bytes().replace(b'\0',b' ').decode(errors='replace').strip()
    except (FileNotFoundError,ProcessLookupError):return ''
def main():
    active=[];groups=[];registry_names=['postheavy-owned.json','final-c455-owned.json']
    known=set(HISTORICAL)
    for name in registry_names:
        p=HERE/name
        if not p.exists():continue
        d=json.loads(p.read_text());known.add(d['scheduler_pid'])
        assert not d.get('active_driver_pids') and not d.get('active_driver_pid'),name
        for r in d['finished_jobs']:
            for k in ('driver_pid','process_pid','process_group'):
                if r.get(k):known.add(r[k])
    for p in Path('/proc').iterdir():
        if not p.name.isdigit():continue
        cmd=command(p.name)
        fields=cmd.split()
        if len(fields)>1 and Path(fields[0]).name.startswith('python') and Path(fields[1]).name in WORKERS and 'lambda-lowweight-20260906/' in fields[1]:
            active.append({'pid':int(p.name),'command':cmd})
        if int(p.name) in known and fields and (Path(fields[0]).name=='Singular' or fields[0]=='/usr/bin/time'):
            groups.append({'pid':int(p.name),'command':cmd})
    result={'status':'STOPPED' if not active and not groups else 'ACTIVE',
            'checked_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            'driver_sha256':hashlib.sha256((HERE/'run_truncated.py').read_bytes()).hexdigest(),
            'historical_pids':sorted(known),'queue_receipts':registry_names,
            'active_pids':active,'active_process_groups':groups,
            'policy':'Read-only /proc inspection; no signals or broad process cleanup.'}
    runner.persist_small(HERE/'shutdown-owned.json',json.dumps(result,indent=2)+'\n')
    print(json.dumps(result));assert result['status']=='STOPPED'
if __name__=='__main__':main()
