#!/usr/bin/env python3
"""Validate only this task's two registered children and capture loaded tools."""
import hashlib
import json
from pathlib import Path
import os
import socket
import sys
import time

root=Path('/home/ubuntu/full-j-solver-pilot-20260906')
if socket.gethostname()!='ip-172-30-0-56' or Path.cwd()!=root:raise SystemExit('wrong worker/root')
records={}
for mode in ['singular','msolve']:
    launch=root/(mode+'.launch.json')
    if not launch.exists():continue
    d=json.loads(launch.read_text()); pid=d['pid']; proc=Path('/proc')/str(pid)
    if not proc.exists():
        records[mode]={'registered_pid':pid,'live':False};continue
    raw=(proc/'stat').read_text()
    old=d['proc_stat'].rsplit(')',1)[1].split()
    now=raw.rsplit(')',1)[1].split()
    if old[19]!=now[19] or int(now[2])!=d['pgid']:raise SystemExit('child identity drift')
    maps=(proc/'maps').read_text().splitlines()
    own=sorted(set(line.split()[-1] for line in maps if '/full-j-solver-pilot-20260906/msolve-source/' in line))
    records[mode]={'registered_pid':pid,'pgid':int(now[2]),'start_ticks':now[19],
        'live':now[0]!='Z','comm':(proc/'comm').read_text().strip(),
        'exe':os.readlink(proc/'exe'),'rss_bytes':int((proc/'statm').read_text().split()[1])*os.sysconf('SC_PAGE_SIZE'),
        'loaded_own_libraries':{name:hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in own}}
stamp=str(time.time_ns())
file=root/('identity.'+stamp+'.json')
file.write_text(json.dumps(records,sort_keys=True,indent=2)+'\n')
print(json.dumps(records,sort_keys=True))
