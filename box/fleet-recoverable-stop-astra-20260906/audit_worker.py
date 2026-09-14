#!/usr/bin/env python3
"""Read-only exact-worker process/storage snapshot; no actions or CAS."""
from pathlib import Path
import datetime
import json
import os
import socket
import subprocess
import sys

host=socket.gethostname()
if host not in ('ip-172-30-0-63','ip-172-30-0-56'): raise SystemExit('wrong worker')
if Path('/sys/class/dmi/id/sys_vendor').read_text().strip()!='Amazon EC2': raise SystemExit('not EC2')
processes=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit(): continue
    try:
        argv=(p/'cmdline').read_bytes().decode().rstrip('\0').split('\0')
        if not argv or not argv[0]: continue
        raw=(p/'stat').read_text(); fields=raw[raw.rindex(')')+2:].split()
        status=(p/'status').read_text()
        processes.append({'pid':int(p.name),'ppid':int(fields[1]),'pgid':int(fields[2]),
            'state':fields[0],'start_ticks':int(fields[19]),'cpu_ticks':int(fields[11])+int(fields[12]),
            'rss_pages':int(fields[21]),'argv':argv,'uid':p.stat().st_uid,
            'cgroup':(p/'cgroup').read_text()})
    except (FileNotFoundError,ProcessLookupError,PermissionError): continue
def cmd(argv): return subprocess.check_output(argv,text=True)
def inventory(path):
    result=[]
    for p in Path(path).iterdir():
        if p.name=='jc2-lean': continue
        s=p.lstat()
        result.append({'path':str(p),'size':s.st_size,'mode':s.st_mode,
                       'symlink':os.readlink(p) if p.is_symlink() else None})
    return result
data={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'hostname':host,
 'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'audit_pid':os.getpid(),
 'processes':processes,'meminfo':Path('/proc/meminfo').read_text(),
 'swap_counters':{k:int(v) for k,v in (s.split() for s in Path('/proc/vmstat').read_text().splitlines()) if k in ('pswpin','pswpout')},
 'mounts':cmd(['findmnt','-J']),
 'blocks':cmd(['lsblk','-J','-b','-o','NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,SERIAL']),
 'df':cmd(['df','-B1','/home/ubuntu','/tmp','/dev/shm']),
 'home_top_level':inventory('/home/ubuntu'),'tmp_top_level':inventory('/tmp'),
 'dev_shm_top_level':inventory('/dev/shm')}
print(json.dumps(data,sort_keys=True,indent=2))
